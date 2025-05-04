+++
weight = 90200
title = 'Writing Documentation'
+++
This page describes how to write documentation for the Bus Pirate firmware. The Bus Pirate firmware is open source and the documentation is open source too.

- This site is built using [Hugo](https://gohugo.io/documentation/), a static site generator, with the [Lotus Docs theme](https://lotusdocs.dev/).
- [autosnip](https://github.com/DangerousPrototypes/BusPirate-docs-hugo/blob/main/tools/autosnip.py) is a Python script that automatically generates the terminal output for the documentation.
- [autodoc](https://github.com/DangerousPrototypes/BusPirate-docs-hugo/blob/main/tools/autodoc.py) is a Python script that captures terminal screencasts to use with the [asciinema player](https://docs.asciinema.org/manual/player/).

Why scripts? The goal is to automate documentation updates when the firmware changes. 

## Install

### Requirements

- **git**
- **Go ≥ v1.21**
- **Hugo ≥ v0.140.0** (**Extended Version**)

### Install Hugo

Install the [Hugo CLI](https://github.com/gohugoio/hugo/releases/latest), using the specific instructions for your operating system below:

{{< tabs tabTotal="4">}}
{{% tab tabName="Linux" %}}

Your Linux distro’s package manager may include Hugo. If this is the case, install it directly using your distro’s package manager – for instance, in Ubuntu, run the following command. This will install the extended edition of Hugo:

```shell
sudo apt install hugo
```

{{% /tab %}}
{{% tab tabName="Homebrew (macOS)" %}}

If you use the package manager [Homebrew](https://brew.sh/), run the `brew install` command in your terminal to install Hugo:

```shell
brew install hugo
```

{{% /tab %}}
{{% tab tabName="Windows (Chocolatey)" %}}

If you use the package manager [Chocolatey](https://chocolatey.org/), run the `choco install` command in your terminal to install Hugo:

```shell
choco install hugo --confirm
```

{{% /tab %}}
{{% tab tabName="Windows (Scoop)" %}}

If you use the package manager [Scoop](https://scoop.sh/), run the `scoop install` command in your terminal to install Hugo:

```shell
scoop install hugo
```

{{% /tab %}}
{{< /tabs >}}

### Install Bus Pirate Docs

```shell
hugo mod init github.com/DangerousPrototypes/BusPirate-docs-hugo.git
```

Hugo can grab the docs from the git repository and setup all the needed modules.

### Start the server

```shell
hugo serve -D
```
This starts a local server on port 1313 that will update as you make changes to the docs. Open your web browser and go to [http://localhost:1313](http://localhost:1313).

## Static Terminal Output

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> m
<span style="color:#bfa530">
<span style="color:#bfa530">Mode selection</span></span>

{{< /term >}}

To avoid using screenshots, which have variable quality and aren't screen reader friendly, most of the Bus Pirate terminal output is shown as actual text inside terminal tag. 

### Write an autosnip script

```
m hiz
# change-mode
m
x
# stop
W 5 100
```

autosnip.py send commands to the Bus Pirate and logs the terminal output to vt100 format and HTML. It uses a dead simple script format. Each line is a command to send to the Bus Pirate, then the script waits for the prompt to return before sending the next command.

```
# change-mode
```

Each script can create multiple terminal capture files. The # character followed by a file name begins capturing. The script above will create a file called ```change-mode.vt1``` and ```change-mode.html```. By default files are saved in the ```/static/snippets/``` directory.

**Note: do not include the file extension in the name. The script will add the correct extension.**

```
# stop
```
This line ends the capture. 

Only output between the ```# change-mode``` and ```# stop``` lines will be captured. The lines before and after are not captured, and can be used to configure and prepare the "scene".

### Disable the Bus Pirate toolbar

The screen redraw activity form the Bus Pirate toolbar will make a mess in the output. Open [Tera Term](https://ttssh2.osdn.jp/index.html.en) and disable the toolbar before logging.

* From the Bus Pirate command prompt choose ```c``` for the configuration menu. 
* Choose ```ANSI toolbar mode``` and ```Disable```.

Remember to close your terminal before running the script.

### Capture Terminal Output

```
python autosnip.py -p COM34 -i commands.txt -d
```

- ```-p``` specifies the Bus Pirate serial port.
- ```-i``` specifies the input file with the commands to send to the Bus Pirate.
- ```-d``` enables debug output. This is useful to see what the script is doing, and to help troubleshoot any problems.


### Add to the Documentation

```go
{{</* termfile source="static/snippets/change-mode.html" /*/>}}
```

Use the ```termfile``` short code to display the file in the documentation. The autosnip.py script will save html files in the ```/static/snippets/``` directory by default. 

## asciinema Screencasts

{{< asciicast src="/screencast/tut-power-supply.json" poster="npt:0:14" terminalFontSize="medium" idleTimeLimit=2 >}}

ascinema is a terminal screencast tool that can be used to record and share terminal sessions. It replays VT100 output in a web browser, so it is much lighter weight than a video file.

### Write an autodoc script

```
rm bpled.bp
m led
3
# tut-power-supply.json
W # W - enable PSU (interactive)
5
100
W 5 100 # W 5 100 - enable PSU (command line options)
W 5 # W 5 - enable PSU (default current limit)
w # w - disable PSU
# stop
m hiz
```

autodoc.py is a Python script that captures terminal screencasts to use with the asciinema player. It uses a dead simple script format. Each line is a command to send to the Bus Pirate, then the script waits for the prompt to return before sending the next command. 

```
# tut-power-supply.json
```

As above, the # character followed by a file name begins capturing and ```# stop``` ends. The script above will save output to files in the ```/static/screencast/``` directory.

**NOTE: DO include the file extension in the name this time.**

```
W # W - enable PSU (interactive)
```

Text after # following a command is saved as a marker in the screencast. Please include markers for major steps in the tutorial.

### Capture Terminal Output

```shell
python autodoc.py -p COM34 -i commands.txt -d
```

- ```-p``` specifies the Bus Pirate serial port.
- ```-i``` specifies the input file with the commands to send to the Bus Pirate.
- ```-d``` enables debug output. This is useful to see what the script is doing, and to help troubleshoot any problems.


{{% alert context="info" %}}
Leave the Bus Pirate status bar active. ascinema is able to play back the toolbar output as well.
{{% /alert %}}

### Add to the Documentation

```go
{{</* asciicast src="/screencast/tut-power-supply.json" poster="npt:0:14" /*/>}}
```

Use the ```asciicast``` short code to display the screencast in the documentation. autodoc.py will save json files in the ```/static/screencast/``` directory by default. 

## Resources

### Files


{{% readfile "/_common/_footer/_footer-files.md" %}}

### Community


{{% readfile "/_common/_footer/_footer-community.md" %}}
