+++
weight = 50400
title = "Logic Command"
+++

![](/images/docs/fw/logic-command-nav.png)

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

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> logic -? h
usage:
<span style="color:#bfa530">logic analyzer usage</span>
<span style="color:#bfa530">logic	[start|stop|hide|show|nav]</span>
<span style="color:#bfa530">	[-i] [-g] [-o oversample] [-f frequency] [-d debug]</span>
<span style="color:#bfa530">start logic analyzer: logic start</span>
<span style="color:#bfa530">stop logic analyzer: logic stop</span>
<span style="color:#bfa530">hide logic analyzer: logic hide</span>
<span style="color:#bfa530">show logic analyzer: logic show</span>
<span style="color:#bfa530">navigate logic analyzer: logic nav</span>
<span style="color:#bfa530">configure logic analyzer: logic -i -o 8 -f 1000000 -d 0</span>
<span style="color:#bfa530">undocumented: set base pin (0=bufdir, 8=bufio, 20=follow along) -b: logic -b 20</span>

<span style="color:#bfa530">logic analyzer control</span>
<span style="color:#96cb59">start</span>	<span style="color:#bfa530">start logic analyzer</span>
<span style="color:#96cb59">stop</span>	<span style="color:#bfa530">stop logic analyzer</span>
<span style="color:#96cb59">hide</span>	<span style="color:#bfa530">hide logic graph</span>
<span style="color:#96cb59">show</span>	<span style="color:#bfa530">show logic graph</span>
<span style="color:#96cb59">nav</span>	<span style="color:#bfa530">navigate logic graph with arrow keys, x to exit</span>
<span style="color:#96cb59">-i</span>	<span style="color:#bfa530">show configuration info</span>
<span style="color:#96cb59">-o</span>	<span style="color:#bfa530">set oversample rate, multiplies the sample frequency</span>
<span style="color:#96cb59">-f</span>	<span style="color:#bfa530">set sample frequency in Hz</span>
<span style="color:#96cb59">-0</span>	<span style="color:#bfa530">set character used for low in graph (ex:_)</span>
<span style="color:#96cb59">-1</span>	<span style="color:#bfa530">set character used for high in graph (ex:*)</span>
<span style="color:#96cb59">-d</span>	<span style="color:#bfa530">set debug level: 0-2</span>
<span style="color:#96cb59">-h</span>	<span style="color:#bfa530">Get additional help</span>

<span style="color:#96cb59">SPI></span> 
{{< /term >}}

```logic -h``` will display the help menu with the latest options for the ```logic``` command.

## Start Logic Analyzer
![](/images/docs/fw/logic-start.png)

```logic start``` configures the logic analyzer core for follow along mode and draws a blank logic graph. Use ```logic stop``` to stop the logic analyzer and release any resources used.

{{% alert context="info" %}}
The ```logic``` command and the [follow along binmode interface](/logic-analyzer/pulseview-fala) can be run at the same time. However, the capture buffer is shared with [SUMP logic analyzer mode](/logic-analyzer/pulseview-sump). SUMP and follow along logic analyzer modes cannot be used at the same time and will result in a memory error warning.
{{% /alert %}}

### Show/Hide Logic Graph

![](/images/docs/fw/logic-hide.png)

If the graph isn't needed, use ```logic hide``` to release it from the toolbar. Use ```logic show``` to draw the graph again showing the current capture buffer.

## Auto Capture Speed
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">Actual speed:</span> 10kHz
<span style="color:#bfa530">Logic analyzer speed:</span> 80000Hz (8x oversampling)
<span style="color:#bfa530">Use the 'logic' command to change capture settings</span>

<span style="color:#bfa530">Mode:</span> SPI
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

When changing protocol modes with the ```m``` command, FALA will automatically set the capture speed to oversample the bus speed by a factor of 8. 

### Change Capture Speed
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> logic -o 16
Oversample rate set to: 16

Logic Analyzer settings
 Oversample rate: 16
 Sample frequency: 10000Hz

Note: oversample rate is not 1
Actual sample frequency: 160000Hz (16 * 10000Hz)

<span style="color:#96cb59">SPI></span> 
{{< /term >}}

The base capture speed or the oversample rate can can be changed with the ```logic``` command. Changing the oversample rate with the ```-o``` flag is probably easiest as the Bus Pirate will calculate the new sample frequency for you.

## Capture Samples

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [ 0xaa 0x55]

CS Enabled
<span style="color:#bfa530">TX:</span> 0x<span style="color:#53a6e6">AA</span> 0x<span style="color:#53a6e6">55</span> 
CS Disabled

<span style="color:#bfa530">Logic analyzer:</span> 144 samples captured
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Every time you send data to the bus, the logic analyzer will capture samples and the logic graph will update (if visible).

{{% alert context="info" %}}
Currently the ```logic``` command only supports automatic capture in follow along mode. It does not currently support pin triggers, but it will eventually. Use ```logic -h``` to see the most recent features. 
{{% /alert %}}

## Navigation

![](/images/docs/fw/logic-command-nav.png)

If there are too many samples to display at once, use ```logic nav``` to navigate the graph. The arrow keys will move the graph left and right, and ```x``` will exit the navigation mode.

## Logic Analyzer System

![](/images/docs/fw/logic-system.png)

{{% alert context="info" %}}
The ```logic``` command and the [follow along binmode interface](/logic-analyzer/pulseview-fala) can be run at the same time. However, the capture buffer is shared with [SUMP logic analyzer mode](/logic-analyzer/pulseview-sump). SUMP and follow along logic analyzer modes cannot be used at the same time and will result in a memory error warning.
{{% /alert %}}

