+++
weight = 40903
title = 'NMEA GPS module UART'
+++  

![GPS Module connected to Bus Pirate](/images/docs/demo/gps-with-bp.png)

GPS modules generally communicate over TTL serial and can be used to add GPS functionality to a variety of projects.

{{% alert context="info" %}}    
These GPS devices use a protocol called [`NMEA`](https://en.wikipedia.org/wiki/NMEA_0183), consisting of ASCII "sentences" (messages).  The Bus Pirate can decode these sentences and can be used to test or explore a GPS module.
{{% /alert %}}

{{% readfile "/_common/_footer/_footer-cart.md" %}}

## Connections
GPS modules will usually have at least 4 connections: `VCC`, `GND`, `TX`, and `RX`.  The actual location and order of these connections can vary from module to module and should be verified by the datasheet or silkscreen labels on the board.  The GPS module may have additional signals, but only the4 listed above are needed.

|Bus Pirate|GPS Module|Description|
|-|-|-|
|Vout|VCC|3.3 volt power supply|
|IO4/TX|RX|Transmit from Bus Pirate to GPS receive|
|IO5/RX|TX|Transmit from GPS to Bus Pirate receive|
|GND|GND|Ground|

The connections can be made with the Bus Pirate cable or "dupont" style jumpers.

## See it in action

{{< asciicast src="/screencast/gps-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}}

## Setup 
#### Mode setup

{{< termfile source="static/snippets/gps-command-setup.html" >}}

Communications to GPS modules are TTL serial, so start by setting the Bus Pirate mode to UART.  The data format for most of these modules is 9600 buad, 8 bits, no parity, and one stop bit.  Set as appropriate.

- `m uart` to change to [**UART**]({{< relref "/docs/command-reference/#uart" >}}) [mode]({{< relref "/docs/command-reference/#m-set-bus-mode" >}}).
If current data format is not 9600/8/n/1:
- 'n' to change communications parameters
- `9600` to select **9600** baud
- `8` to select **8** data bits
- `1` to select **None** parity
- `1` to select **1** stop bit
- `1` to select **None** hardware flow control
- `1` to select **Non-inverted** signal levels
#### Power supply setup
Most GPS modules operate at `3.3Volts`, but check the datasheet to be sure.

{{< termfile source="static/snippets/gps-power-setup.html" >}}

- `W 3.3` to turn on the Bus Pirate's power supply and set to **3.3** volts.  Current limit will be set to the default **300** milliamp current limit.

The power supply voltage and actual output current will be displayed

{{% alert context="warning" %}}

Verify actual voltage requirements to your GPS module and replace the `3.3` with the appropriate value!
{{% /alert %}}

## GPS Command

{{< termfile source="static/snippets/gps-gps-command.html" >}}

The [**gps**]({{< relref "/docs/command-reference/#gps-decoding-gps-nmea-sentences" >}}) command will set the UART to begin receiving sentences from the GPS module.  The Bus Pirate will decode the sentences as they come in.

Press any key to stop the command.

