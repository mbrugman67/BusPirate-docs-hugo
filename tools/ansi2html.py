import re
from html import escape

class AnsiToHtml:
    def __init__(self, fg="#FFF", bg="#000", newline=False, escape_xml=False, stream=False, colors=None):
        self.defaults = {
            "fg": fg,
            "bg": bg,
            "newline": newline,
            "escape_xml": escape_xml,
            "stream": stream,
            "colors": self.get_default_colors()
        }
        if colors:
            self.defaults["colors"].update(colors)
        self.options = self.defaults
        self.stack = []
        self.sticky_stack = []

    @staticmethod
    def get_default_colors():
        colors = {
            0: "#000", 1: "#A00", 2: "#0A0", 3: "#A50", 4: "#00A", 5: "#A0A", 6: "#0AA", 7: "#AAA",
            8: "#555", 9: "#F55", 10: "#5F5", 11: "#FF5", 12: "#55F", 13: "#F5F", 14: "#5FF", 15: "#FFF"
        }
        for red in range(6):
            for green in range(6):
                for blue in range(6):
                    c = 16 + (red * 36) + (green * 6) + blue
                    r = red * 40 + 55 if red > 0 else 0
                    g = green * 40 + 55 if green > 0 else 0
                    b = blue * 40 + 55 if blue > 0 else 0
                    colors[c] = f"#{r:02x}{g:02x}{b:02x}"
        for gray in range(24):
            c = gray + 232
            l = gray * 10 + 8
            colors[c] = f"#{l:02x}{l:02x}{l:02x}"
        return colors

    def reset_styles(self):
        stack_clone = self.stack[:]
        self.stack.clear()
        return "".join(f"</{tag}>" for tag in reversed(stack_clone))

    def push_tag(self, tag, style=None):
        self.stack.append(tag)
        return f"<{tag}{f' style=\"{style}\"' if style else ''}>"

    def push_style(self, style):
        return self.push_tag("span", style)

    def push_foreground_color(self, color):
        return self.push_tag("span", f"color:{color}")

    def push_background_color(self, color):
        return self.push_tag("span", f"background-color:{color}")

    def close_tag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
            return f"</{tag}>"
        return ""

    def handle_display(self, code):
        code = int(code)
        if code == 0:
            return self.reset_styles()
        elif code == 1:
            return self.push_tag("b")
        elif code == 3:
            return self.push_tag("i")
        elif code == 4:
            return self.push_tag("u")
        elif code == 8:
            return self.push_style("display:none")
        elif code == 9:
            return self.push_tag("strike")
        elif code == 22:
            return self.push_style("font-weight:normal;text-decoration:none;font-style:normal")
        elif code == 23:
            return self.close_tag("i")
        elif code == 24:
            return self.close_tag("u")
        elif code == 39:
            return self.push_foreground_color(self.options["fg"])
        elif code == 49:
            return self.push_background_color(self.options["bg"])
        elif 30 <= code <= 37:
            return self.push_foreground_color(self.options["colors"][code - 30])
        elif 40 <= code <= 47:
            return self.push_background_color(self.options["colors"][code - 40])
        elif 90 <= code <= 97:
            return self.push_foreground_color(self.options["colors"][8 + (code - 90)])
        elif 100 <= code <= 107:
            return self.push_background_color(self.options["colors"][8 + (code - 100)])
        return ""

    def tokenize(self, text):
        tokens = [
            (r"^\x08+", lambda _: ""),
            (r"^\x1b\[[012]?K", lambda _: ""),
            (r"^\x1b\[\(B", lambda _: ""),
            (r"^\x1b\[999;999H", lambda _: ""),  # Ignore cursor position
            (r"^\x1b\[6n", lambda _: ""),  # Ignore device status report
            (r"^\x1b\[\?3l", lambda _: ""),  # Ignore VT100 mode reset
            (r"^\x1b\]0;.*?\x07", lambda _: ""),  # Ignore OSC (Operating System Command) sequences            
            (r"^\x1b\[2J", lambda _: ""),  # Ignore "clear screen"
            (r"^\x1b7", lambda _: ""),  # Ignore "save cursor position"
            (r"^\x1b8", lambda _: ""),  # Ignore "restore cursor position"
            (r"^\x1b\[38;2;(\d+);(\d+);(\d+)m", lambda m: self.push_foreground_color(f"rgb({m.group(1)},{m.group(2)},{m.group(3)})")),
            (r"^\x1b\[48;2;(\d+);(\d+);(\d+)m", lambda m: self.push_background_color(f"rgb({m.group(1)},{m.group(2)},{m.group(3)})")),
            (r"^\x1b\[38;5;(\d+)m", lambda m: self.push_foreground_color(self.options["colors"][int(m.group(1))])),
            (r"^\x1b\[48;5;(\d+)m", lambda m: self.push_background_color(self.options["colors"][int(m.group(1))])),
            (r"^\n", lambda _: "<br/>" if self.options["newline"] else "\n"),
            (r"^\x1b\[((?:\d{1,3};?)+|)m", lambda m: "".join(self.handle_display(code) for code in m.group(1).split(";") if code)),
            (r"^(([^\x1b\x08\r\n])+)", lambda m: escape(m.group(1)) if self.options["escape_xml"] else m.group(1))
        ]
        while text:
            for pattern, handler in tokens:
                match = re.match(pattern, text)
                if match:
                    yield handler(match)
                    text = text[match.end():]
                    break
            else:
                break

    def to_html(self, input_text):
        buf = []
        for token in self.tokenize(input_text):
            buf.append(token)
        if self.stack:
            buf.append(self.reset_styles())
        return "".join(buf)
    
# add a main to load a file and convert it to html
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ansi2html.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        input_text = f.read()
    
    #remove unprinted character \x03
    input_text = input_text.replace("\x03", "")

    converter = AnsiToHtml()
    html_output = converter.to_html(input_text)
    
    with open(input_file.replace(".txt", ".html"), "w") as f:
        f.write(html_output)
    print(f"Converted {input_file} to HTML format.")