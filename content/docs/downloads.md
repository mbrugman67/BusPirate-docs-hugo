+++
title = "Downloads"
description = ""
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 100
+++

{{% alert icon="💡" context="success" %}}
TIP

The latest bleeding edge firmware is auto-compiled and posted in the forum.
[Get the latest and
greatest](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999).
{{% /alert %}}

{{% alert icon="🛈" context="info" %}}
INFO

See the [firmware update tutorial](https://firmware.buspirate.com/tutorial-basics/firmware-update) for detailed instructions.

- [Grab the latest and greatest auto-build firmware from the forum](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999)
- Open the .zip archive and extract your firmware
- If your Bus Pirate came in a case (most boards), use `bus_pirate5_rev10.uf2`
- Type `$` and press `enter` in the Bus Pirate terminal to enter bootloader/upgrade mode
- A USB drive called RPI-RP2 will connect to your computer
- Drag a .uf2 firmware file into the RPI-RP2 drive

The file copies, the Bus Pirate resets, and you're good to go!
{{% /alert %}}

{{% alert icon="🔥" context="danger" %}}
DANGER

Bus Pirate blinking red? Recent firmware detects the hardware revision at startup. It will blink red if there is a mismatch.

[Enter the bootloader manually](https://firmware.buspirate.com/tutorial-basics/firmware-update#manually) (plug in the USB cable while pressing the button on the bottom side) and try the other file.
{{% /alert %}}

## Links

- [Download latest firmware build](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/99999)
- [Bus Pirate 5 Hardware repo](https://github.com/DangerousPrototypes/BusPirate5-hardware)
- [Bus Pirate 5 Firmware repo](https://github.com/DangerousPrototypes/BusPirate5-firmware)

## Get Bus Pirate 5

{{% btn icon="🛒" context="danger" href="https://buspirate.com/get" %}}
Get Bus Pirate 5 & Accessories
{{% /btn %}}
