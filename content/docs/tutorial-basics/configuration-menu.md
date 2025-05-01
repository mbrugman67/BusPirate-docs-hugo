+++
weight = 30600
title = 'Configuration Menu'
+++

{{< asciicast src="/screencast/tut-config-menu.json" poster="npt:0:14" terminalFontSize="medium" idleTimeLimit=2 >}}    

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> c
<span style="color:#bfa530">Configuration options</span>
 1. <span style="color:#bfa530">Language / Jezik / Lingua </span>
 2. <span style="color:#bfa530">ANSI color mode</span>
 3. <span style="color:#bfa530">ANSI toolbar mode</span>
 4. <span style="color:#bfa530">LCD screensaver</span>
 5. <span style="color:#bfa530">LED effect</span>
 6. <span style="color:#bfa530">LED color</span>
 7. <span style="color:#bfa530">LED brightness</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 
{{< /term >}}

Type ```c``` followed by ```enter``` to show the Bus Pirate configuration menu. These options control things like the language, live view statusbar and LEDs.

## Configuration

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59"> ></span> 5

<span style="color:#bfa530">LED effect</span>
 1. <span style="color:#bfa530">Disable</span>
 2. <span style="color:#bfa530">Solid</span>
 3. <span style="color:#bfa530">Angle wipe</span>
 4. <span style="color:#bfa530">Center wipe</span>
 5. <span style="color:#bfa530">Clockwise wipe</span>
 6. <span style="color:#bfa530">Top side wipe</span>
 7. <span style="color:#bfa530">Scanner</span>
 8. <span style="color:#bfa530">Gentle glow</span>
 9. <span style="color:#bfa530">Party mode</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 9
LED effect <span style="color:#bfa530">set to</span> Party mode

{{< /term >}}

Type a menu option number followed by ```enter```. Choose a configuration setting by typing the number followed by ```enter```.

## Exit and Save
{{< term "Bus Pirate [/dev/ttyS0]" >}}
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> x

<span style="color:#bfa530">Configuration file:</span> Saved
{{< /term >}}

Press ```x``` followed by ```enter``` at any prompt to exit the configuration menu. 

## Settings file

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> ls
<span style="color:#96cb59">       350 <span style="color:#bfa530">bpconfig.bp</span></span>
<span style="color:#bfa530">0 dirs, 1 files</span>
{{< /term >}}

Settings are saved in bpconfig.bp and will load automatically when the Bus Pirate restarts.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> cat bpconfig.bp
{
"terminal_language": 0,
"terminal_ansi_color": 1,
"terminal_ansi_statusbar": 0,
"display_format": 0,
"lcd_screensaver_active": 0,
"lcd_timeout": 0,
"led_effect": 8,
"led_color": "0xFF0000",
"led_brightness_divisor": 10,
}
{{< /term >}}

All Bus Pirate config files contain simple JSON formatted data.

