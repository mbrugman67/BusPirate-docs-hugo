+++
weight = 20100
title = 'Bus Pirate Hardware'
+++

![](/images/docs/fw/bp5rev10-cover-angle.jpg)

Bus Pirate is the universal serial interface tool trusted by hackers since 2008.

What can the Bus Pirate do? Probe and debug serial protocols like [I2C]({{< relref "/docs/command-reference/#i2c">}}), [SPI]({{< relref "/docs/command-reference/#spi">}}), [UART]({{< relref "/docs/command-reference/#uart">}}), [1-Wire]({{< relref "/docs/command-reference/#1-wire">}}) and more - without writing code! Read and write [Flash memory]({{< relref "/docs/command-reference/#flash-readwriteerase-common-flash-chips">}}), [24x/25x/93x/95x EEPROMs]({{< relref "/docs/command-reference/#eeprom-read-write-erase-verify-test-dump-i2c-eeproms">}}), [DDR5 SPD]({{< relref "/docs/devices/ddr5/">}}), [smart cards]({{< relref "/docs/devices/sle4442/">}}), and [FRAM]({{< relref "/docs/devices/identify-serial-memory-chips/#fram-memory">}}). Several types of [logic analyzer support]({{< relref "/docs/logic-analyzer/logicanalyzer/">}}), and a [low speed oscilloscope]({{< relref "/docs/scope/">}}). Discover [JTAG and SWD debug ports]({{< relref "/docs/devices/jtag-swd-pin-finder/">}}). [Sniff I2C]({{< relref "/docs/command-reference/#sniff-i2c-bus-sniffer">}}) and other busses. Glitch hack an [Arduino]({{< relref "/docs/devices/uart-glitch-command/">}}). [Record]({{< relref "/docs/command-reference/#irrx">}}) and [playback]({{< relref "/docs/command-reference/#irtx">}}) infrared remote control signals, also works with [AnalysIR software]({{< relref "/docs/software/analysir/">}}). Control common serial LEDs like [WS2812, SK6812]({{< relref "/docs/devices/ws2812-sk6812-neopixel/">}}), [APA102]({{< relref "/docs/devices/apa102-sk9822/">}}), and read [RGB color sensors]({{< relref "/docs/devices/tcs3472x/">}}). Works with [FlashRom]({{< relref "/docs/software/flashrom/">}}) and [AVRDUDE]({{< relref "/docs/software/avrdude/">}}). Nearly constant [firmware releases]({{< relref "/docs/downloads/">}}) and updates, active community support.

Can't get a chip to work? Is it the circuit, code, bad part or a burned out pin? The Bus Pirate sends commands over common serial protocols (1-Wire, I2C, SPI, UART, MIDI, serial LEDs, etc) so you can get to know a chip before prototyping. Updated with tons of new features, talking to chips and probing interfaces is more fun than ever!



{{% readfile "/_common/_footer/_footer-cart.md" %}}

## VT100 terminal interface

<!-- ![](/images/docs/fw/teraterm-done.png) -->

{{< asciicast src="/sizzle/sizzle-cast.json" poster="npt:1:23"  idleTimeLimit=2 >}}

VT100 terminal emulation supports color and a live statusbar view of the voltage and functions on each pin. Type simple commands into the terminal, the Bus Pirate translates them into popular serial protocols and displays the response. Learn how a chip works without touching a line of code.

## Specifications

- Raspberry Pi RP chip paired with 128Mbit program flash
- 8 powerful IO pins - Support multiple protocols from 1.2-5volts. Analog voltage measurement and optional 10K pull-ups on all pins
- 1-5volt output power supply - 0-500mA current limit, current sense, resettable fuse and protection circuit
- 1Gbit NAND flash - Store settings and files. Appears as a USB drive.
- LCD - A beautiful 240x320 pixel color IPS (all angle viewing) LCD acts as a pin label, while also showing the voltage on each pin and the current consumption of the programmable power supply unit
- 18 RGB LEDs - It's customary to have an indicator LED, so to check that box we added 16 SK6812 RGB LEDs.
- Just one button - 18 party LEDs but just one button!
- 1-Wire, I2C, SPI, UART, MIDI, serial LEDs supported, more to come!

Bus Pirate is the universal serial interface tool designed by hackers, for hackers. It's crammed full of hardware and firmware features to make probing chips pleasant and easy.

### Get a Bus Pirate
 

{{% readfile "/_common/_footer/_footer-get.md" %}}  

{{% alert context="info" %}}
This is the user guide for Bus Pirate 5. See the [hardware documentation]({{< relref "/docs/hardware" >}}) for all the technical details.
{{% /alert %}}

## Color IPS LCD

![](/images/docs/fw/bp5rev10-cover-2.jpg)

A beautiful 240x320 pixel color IPS (all angle viewing) LCD acts as a pin label, while also showing the voltage on each pin and the current consumption of the programmable power supply unit

## Main connector
![](/images/docs/hw/bp6rev2/connectors.jpg)

2.54mm 10 pin connector - A keyed locking connector that works just as well with common jumper wires and 2.54mm 'DuPont' style connectors.

|Pin|Label|Description|
|-|-|-|
|1|VOUT/VREF|Pin supplies 1-5volts up to 300mA with current limit and resetable fuse (VOUT) **OR** connects an external voltage source to the Bus Pirate IO interface|
|2-9|IO0 - IO7|Buffered IO pins 1.2-5volt output with voltage measurement and optional 10K pull-up resistors|
|10|GND| Ground pin|

## Auxiliary connector

![](/images/docs/fw/bp5-aux.jpg)

1mm 9 pin connector - Intended as a tap point for a logic analyzer. No more trying to balance two or three probes on a single pin, just tap the bus activity from this secondary header.

|Pin|Label|Description|
|-|-|-|
|1-8|IO0 - IO7|Buffered IO pins with voltage measurement and optional 10K pull-up resistors|
|9|GND| Ground pin|

## 1Gbit NAND flash

![](/images/docs/fw/bp5rev10-nand.jpg)

1Gbit (~100MB usable) NAND flash - Appears as a readable and writable disk drive when plugged into a USB port. 

![](/images/docs/fw/json-config.png)

Flash storage is used to save global and mode configuration preferences in simple JSON files. 

## Just one button

![](/images/docs/fw/bp5-onebutton.jpg)

18 party LEDs but just one button! This is due to the low pin count of the RP2040. The button is used to escape modes, production programming and user defined functions.

## USB C connector
![](/images/docs/fw/bp5-usbc.jpg)

Modern USB C connector. Only RP2040 supported USB modes are available.

## USB bootloader

![](/images/docs/fw/bp5-back.jpg)

Updating is as simple as dragging a file onto the disk. 

Normally the ```$``` key in the Bus Pirate terminal enters bootloader mode for firmware upgrades. You can also use the button on the bottom to activate the bootloader manually. 

## JTAG debug header
![](/images/docs/fw/bp5-debug.jpg)

A three pin debugging port is exposed on the bottom of the board. See the development section for more info on developing for the Bus Pirate.

|Pin|Label|Description|
|-|-|-|
|1|GND|Ground connection (furthest from the edge of the PCB/case)|
|2|SWDIO|JTAG Data IO|
|3|SWCLK|JTAG Clock (closest to the edge of the PCB/case)|

## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-get.md" %}}

### Files


{{% readfile "/_common/_footer/_footer-files.md" %}}

### Community


{{% readfile "/_common/_footer/_footer-community.md" %}}

### Documentation


{{% readfile "/_common/_footer/_footer-docs.md" %}}

## FCC compliance statement
This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

## CE compliance
The Bus Pirate has been lab tested to comply with European CE requirements.




