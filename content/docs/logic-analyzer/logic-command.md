+++
weight = 20
title = "Logic Command"
+++

# ```logic``` Command

![](./img/logic-command-nav.png)

The ```logic``` command configures the logic analyzer core, and can display logic capture graphs directly in the terminal. It supports the "follow along" logic analyzer mode that triggers each time you send data to a bus. It eliminates the need setup triggers and arm a second tool for debugging. 

The Bus Pirate can be [used as a logic analyzer in multiple ways](/logic-analyzer/logicanalyzer). This page documents the ```logic``` command in the terminal.

{{% alert context="danger" %}}
All Bus Pirate hardware supports the follow along logic analyzer, however only Bus Pirate 6 has a second buffer for the follow along mode. In earlier hardware **all output pins are measured behind the IO buffer**. This means the logic capture may not match the actual output of the IO buffer. **This is not a problem when the Bus Pirate is used as a logic analyzer only and all pins are inputs**.
{{% /alert %}}

## Capabilities

- 62.5MSPS (or more if overclocked)
- 131K samples
- 8 channels
- Trigger: single pin, high or low
- Follow along logic analyzer mode
- Base pin can be set to an internal pin for debugging the Bus Pirate itself

## Latest Features and Help

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> logic -? h
usage:
<span className="bp-info">logic analyzer usage</span>
<span className="bp-info">logic	[start|stop|hide|show|nav]</span>
<span className="bp-info">	[-i] [-g] [-o oversample] [-f frequency] [-d debug]</span>
<span className="bp-info">start logic analyzer: logic start</span>
<span className="bp-info">stop logic analyzer: logic stop</span>
<span className="bp-info">hide logic analyzer: logic hide</span>
<span className="bp-info">show logic analyzer: logic show</span>
<span className="bp-info">navigate logic analyzer: logic nav</span>
<span className="bp-info">configure logic analyzer: logic -i -o 8 -f 1000000 -d 0</span>
<span className="bp-info">undocumented: set base pin (0=bufdir, 8=bufio, 20=follow along) -b: logic -b 20</span>

<span className="bp-info">logic analyzer control</span>
<span className="bp-prompt">start</span>	<span className="bp-info">start logic analyzer</span>
<span className="bp-prompt">stop</span>	<span className="bp-info">stop logic analyzer</span>
<span className="bp-prompt">hide</span>	<span className="bp-info">hide logic graph</span>
<span className="bp-prompt">show</span>	<span className="bp-info">show logic graph</span>
<span className="bp-prompt">nav</span>	<span className="bp-info">navigate logic graph with arrow keys, x to exit</span>
<span className="bp-prompt">-i</span>	<span className="bp-info">show configuration info</span>
<span className="bp-prompt">-o</span>	<span className="bp-info">set oversample rate, multiplies the sample frequency</span>
<span className="bp-prompt">-f</span>	<span className="bp-info">set sample frequency in Hz</span>
<span className="bp-prompt">-0</span>	<span className="bp-info">set character used for low in graph (ex:_)</span>
<span className="bp-prompt">-1</span>	<span className="bp-info">set character used for high in graph (ex:*)</span>
<span className="bp-prompt">-d</span>	<span className="bp-info">set debug level: 0-2</span>
<span className="bp-prompt">-h</span>	<span className="bp-info">Get additional help</span>

<span className="bp-prompt">SPI></span> 
{{% /term %}}

```logic -h``` will display the help menu with the latest options for the ```logic``` command.

## Start Logic Analyzer
![](./img/logic-start.png)

```logic start``` configures the logic analyzer core for follow along mode and draws a blank logic graph. Use ```logic stop``` to stop the logic analyzer and release any resources used.

{{% alert context="info" %}}
The ```logic``` command and the [follow along binmode interface](/logic-analyzer/pulseview-fala) can be run at the same time. However, the capture buffer is shared with [SUMP logic analyzer mode](/logic-analyzer/pulseview-sump). SUMP and follow along logic analyzer modes cannot be used at the same time and will result in a memory error warning.
{{% /alert %}}

### Show/Hide Logic Graph

![](./img/logic-hide.png)

If the graph isn't needed, use ```logic hide``` to release it from the toolbar. Use ```logic show``` to draw the graph again showing the current capture buffer.

## Auto Capture Speed
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-info">Actual speed:</span> 10kHz
<span className="bp-info">Logic analyzer speed:</span> 80000Hz (8x oversampling)
<span className="bp-info">Use the 'logic' command to change capture settings</span>

<span className="bp-info">Mode:</span> SPI
<span className="bp-prompt">SPI></span> 
{{% /term %}}

When changing protocol modes with the ```m``` command, FALA will automatically set the capture speed to oversample the bus speed by a factor of 8. 

### Change Capture Speed
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> logic -o 16
Oversample rate set to: 16

Logic Analyzer settings
 Oversample rate: 16
 Sample frequency: 10000Hz

Note: oversample rate is not 1
Actual sample frequency: 160000Hz (16 * 10000Hz)

<span className="bp-prompt">SPI></span> 
{{% /term %}}

The base capture speed or the oversample rate can can be changed with the ```logic``` command. Changing the oversample rate with the ```-o``` flag is probably easiest as the Bus Pirate will calculate the new sample frequency for you.

## Capture Samples

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> [ 0xaa 0x55]

CS Enabled
<span className="bp-info">TX:</span> 0x<span className="bp-float">AA</span> 0x<span className="bp-float">55</span> 
CS Disabled

<span className="bp-info">Logic analyzer:</span> 144 samples captured
<span className="bp-prompt">SPI></span> 
{{% /term %}}

Every time you send data to the bus, the logic analyzer will capture samples and the logic graph will update (if visible).

{{% alert context="info" %}}
Currently the ```logic``` command only supports automatic capture in follow along mode. It does not currently support pin triggers, but it will eventually. Use ```logic -h``` to see the most recent features. 
{{% /alert %}}

## Navigation

![](./img/logic-command-nav.png)

If there are too many samples to display at once, use ```logic nav``` to navigate the graph. The arrow keys will move the graph left and right, and ```x``` will exit the navigation mode.

## Logic Analyzer System

![](./img/logic-system.png)

{{% alert context="info" %}}
The ```logic``` command and the [follow along binmode interface](/logic-analyzer/pulseview-fala) can be run at the same time. However, the capture buffer is shared with [SUMP logic analyzer mode](/logic-analyzer/pulseview-sump). SUMP and follow along logic analyzer modes cannot be used at the same time and will result in a memory error warning.
{{% /alert %}}

