+++
title = "Commands"
description = ""
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 100
+++

{{% term "Bus Pirate [/dev/ttyS0]" %}}
HiZ> i

Bus Pirate 5 REV6
Firmware v0.1 (unknown), Bootloader N/A
RP2040 with 264KB RAM, 16MB FLASH
S/N: 2509449B952069E4
https://DangerousPrototypes.com/
Flash Storage: 0.10GB (FAT16)

Configuration file: Loaded
Available modes: HiZ UART I2C SPI LED DUMMY1
Active mode: HiZ ()=()
Display format: Auto

HiZ>
{{% /term %}}

This guide is updated with to reflect feature changes with each firmware
release. To check your firmware version type `i` followed by `enter` in the Bus
Pirate terminal window. Here, the Bus Pirate is running firmware v0.1.


{{% alert icon="💡" context="success" %}}
TIP

It's always best to use the latest firmware, especially in these early days of
a new design. There will be continuous improvements and new features. See the
upgrade guide for the simple drag and drop bootload process.
{{% /alert %}}

## User Terminal

![](images/docs/cmd-toolbar.png)

The Bus Pirate is accessed from a command line in a serial terminal. Use your
terminal of choice. On Windows we like the latest version of [Tera
Term](https://ttssh2.osdn.jp/index.html.en).

{{% alert icon="💡" context="success" %}}
TIP

Talk to the Bus Pirate from a serial terminal of your choice set to 115200bps,
8/N/1. The serial port is emulated over USB, so higher bitrate (bps) settings
will also work with no extra configuration. If the user interface feels slow,
check that the speed is at least 115200bps.
{{% /alert %}}


