+++
title = "FALA Logic Analyzer"
description = "Live action follow along logic analyzer"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 300
+++

# Follow Along Logic Analyzer

An asynchronous logic analyzer that triggers each time bus syntax is run from the terminal. It eliminates the need setup triggers and arm a second tool for debugging.  We like to call it FALA for short.

The Bus Pirate can be [used as a logic analyzer in multiple ways](/logic-analyzer/logicanalyzer). This is the documentation for the "follow along logic analyzer" interface.

{{% alert context="danger" %}}
All Bus Pirate hardware supports follow along logic analyzer, however only Bus Pirate 6 has a second buffer to capture pins directly. In earlier hardware **all output pins are measured behind the IO buffer**. This means the logic capture may not match the actual output of the IO buffer. **This is not a problem when the Bus Pirate is used as a logic analyzer only and all pins are inputs**.
{{% /alert %}}

## Capabilities

- 62.5MSPS (or more if overclocked)
- 131K samples
- 8 channels
- Trigger: single pin, high or low
- Follow along logic analyzer mode
- Base pin can be set to an internal pin for debugging the Bus Pirate itself

## Enable FALA Interface

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">HiZ></span> binmode

<span style="color:#bfa530">Select binary mode</span>
 1. SUMP logic analyzer
 2. Binmode test framework
 3. Arduino CH32V003 SWIO
 4. Follow along logic analyzer
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 4
<span style="color:#bfa530">Binmode selected:</span> Follow along logic analyzer

<span style="color:#96cb59">HiZ></span> 
{{% /term %}}

Enable the FALA binary interface with the ```binmode``` command. This will configure the logic analyzer and send capture notifications to the Bus Pirate's second serial port.

### Auto Capture Speed
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#bfa530">Actual speed:</span> 10kHz
<span style="color:#bfa530">Logic analyzer speed:</span> 80000Hz (8x oversampling)
<span style="color:#bfa530">Use the 'logic' command to change capture settings</span>

<span style="color:#bfa530">Mode:</span> SPI
<span style="color:#96cb59">SPI></span> 
{{% /term %}}

When changing protocol modes with the ```m``` command, FALA will automatically set the capture speed to oversample the bus speed by a factor of 8. 

### Change Capture Speed
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">SPI></span> logic -o 16
Oversample rate set to: 16

Logic Analyzer settings
 Oversample rate: 16
 Sample frequency: 10000Hz

Note: oversample rate is not 1
Actual sample frequency: 160000Hz (16 * 10000Hz)

<span style="color:#96cb59">SPI></span> 
{{% /term %}}

The base capture speed or the oversample rate can can be changed with the ```logic``` command. Changing the oversample rate with the ```-o``` flag is probably easiest as the Bus Pirate will calculate the new sample frequency for you.

### Capture Samples

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">SPI></span> [ 0xaa 0x55]

CS Enabled
<span style="color:#bfa530">TX:</span> 0x<span style="color:#53a6e6">AA</span> 0x<span style="color:#53a6e6">55</span> 
CS Disabled

<span style="color:#bfa530">Logic analyzer:</span> 144 samples captured
<span style="color:#96cb59">SPI></span> 
{{% /term %}}

Every time you send data to the bus, the logic analyzer will capture samples. The capture notification will be sent to the second serial port.

## Protocol


### Asynchronous Capture Notification

```$FALADATA,8,0,0,N,40000,168,0\n```

Data arrives asynchronously, like GPS NMEA packets, so we structured notifications in a similar way. The notification is a string of comma separated values with the following fields:

- $FALADATA - Notification header
- capture pins (ex: 8)
- trigger pin mask (ex: 10100000)
- trigger mask (ex: 10000000)
- edge trigger (Y/N)
- capture speed in hz
- samples captured
- number of samples captured before the trigger (for pre-capture)
- terminated with a new line (\n)

Most languages can easily parse CSV. 

### **+** - Dump Samples

- ```+``` - Dump samples

In response to a capture notification, the host can request the samples with the ```+``` command.

Data format is a binary blob. Sample order is "backwards" with the newest sample first, oldest sample last.

### **?** - Request Status

- ```?``` - Request status

Returns the most recent capture notification. Can be used to retrieve missed capture notifications, or to check if the interface is active.

## Logic Analyzer System

![](./img/logic-system.png)

{{% alert context="info" %}}
The ```logic``` command and the [follow along binmode interface](/logic-analyzer/pulseview-fala) can be run at the same time. However, the capture buffer is shared with [SUMP logic analyzer mode](/logic-analyzer/pulseview-sump). SUMP and follow along logic analyzer modes cannot be used at the same time and will result in a memory error warning.
{{% /alert %}}


