+++
title = "1-Wire Protocol"
description = "1-Wire Protocol"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 10
+++

# 1-Wire Protocol Commands

## Overview

-   **Bus:** [1-Wire](https://en.wikipedia.org/wiki/1-Wire)
-   **Connections:** one pin (OWD) and ground
-   **Output type:** open drain/open collector
-   **Pull-up resistors:** always required (2K - 10K ohms)
-   **Maximum voltage:** 5volts

1-Wire is a common bus for low speed interfaces.

## Configuration options

- None

**Pull-up resistors**

1-Wire is an open-collector bus, it requires pull-up resistors to hold the
data line high and create the data '1'. 1-Wire parts don't
output high, they only pull low, without pull-up resistors there can
never be a '1'. 

Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.

{{% alert context="info" %}}
- 1-Wire requires a pull-up resistor to hold the data line high.
- 1-Wire parts don't output high, they only pull low.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.
{{% /alert %}}

## Connections

| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| OWD       | <font size="+2">↔</font> | OWD     | 1-Wire Data   |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

## Syntax

|Command|Description|
|-------|-----------|
| \{ or [ | Issue 1-Wire reset, detect device presence. |
| r       | Read one byte. (r:1…255 for bulk reads)|
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |
| \(#\)   | Run macro, (0) for macro list. |


## Commands

Bus Pirate 5 has global commands available everywhere, and mode commands specific to the currently selected mode. Type ```help``` to see all commands in every mode, or ```help mode``` for the currently available mode commands.

{{% alert context="info" %}}
Most Bus Pirate commands have help. Add the ```-h``` flag to any command to see the latest available options and usage examples. 
{{% /alert %}}

### scan

```scan``` performs a 1-Wire ROM search. Find all connected device IDs.

#### help

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">1-WIRE></span> scan -h
usage:
<span className="bp-info">scan	[-h(elp)]</span>
<span className="bp-info">Scan 1-Wire address space: scan</span>

<span className="bp-info">scan for 1-Wire devices</span>
<span style="color:#96cb59">-h</span>	<span className="bp-info">Get additional help</span>

<span style="color:#96cb59">1-WIRE></span> 
{{% /term %}}

#### use
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">1-WIRE></span> scan
<span className="bp-info">
1-Wire ROM search:
1: 28 5c aa 13 0a 00 00 19
</span>
<span style="color:#96cb59">1-WIRE></span>
{{% /term %}}

```scan``` performs a 1-Wire ROM search to detect the ID of every connected 1-Wire device. They type of device is shown if the family ID is known.

### ds18b20    

```ds18b20``` reads the temperature from a single 18B20 sensor.

#### help

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">1-WIRE></span> ds18b20 -h
usage:
<span className="bp-info">ds18b20	[-h(elp)]</span>
<span className="bp-info">measure temperature (single sensor bus only): ds18b20</span>

<span className="bp-info">Query DS18B20 temperature sensor</span>
<span style="color:#96cb59">-h</span>	<span className="bp-info">Get additional help</span>

<span style="color:#96cb59">1-WIRE></span> 
{{% /term %}}

#### use

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">1-WIRE></span> ds18b20
<span className="bp-info">
RX: 1a 01 00 00 7f ff 06 10 12
Temperature: 17.625
</span>
<span style="color:#96cb59">1-WIRE></span>
{{% /term %}}

Macro ```ds18b20``` reads the temperature from a single 18B20 temperature sensor. The macro uses the skip ROM command, so it will only work with a single DS18B20 device connected.
