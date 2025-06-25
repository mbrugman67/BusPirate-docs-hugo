+++
weight = 40110
title = 'UART Glitch of Arduino'
+++

![](/images/docs/demo/glitch-desktop.png)

The Bus Pirate can be used to trigger glitching attacks based on UART serial timing:
- Power glitching
- EMP "blasting"
- Clock glitching

For this demo, the Bus Pirate will be used to trigger a power glitching attack against an Arduino Uno.  The Arduino's software has a UART that is used to enter a password; this password will by bypassed by a power glitch.  A custom circuit on a Bus Pirate Blank Plank is used to perform the actual power glitch against the Arduino.

{{% alert context="info" %}}
The Bus Pirate is used to time and trigger the "glitching" activity; actual external electrical interface to the target and/or glitching tool is required.  This may be in the form of a separte device, custom plank, breadboarding, or circuit board.
{{% /alert %}}

{{% readfile "/_common/_footer/_footer-get.md" %}}

## Connections

|Bus Pirate|Target/Interface|Description|
|-|-|-|
|TX->|Arduino pin 0 (`RX`)|Serial UART from Bus Pirate to Arduino|
|RX<-|Arduino pin 1 (`TX`)|Serial UART from Arduino to Bus Pirate|
|Vout/Vref|Arduino `5V`|5volt power supply|
|GND|Arduino `GND`|Ground|

{{% alert context="warning" %}} 
Don't enable Bus Pirate power supply; the I/O buffers are powered by the Arduino.
{{% /alert %}}

## See it in action

{{< asciicast src="/screencast/glitch-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}}


## Setup

Considering:

## Get a Bus Pirate


{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community


{{% readfile "/_common/_footer/_footer-community.md" %}}