+++
title = "Download Firmware"
description = ""
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 1000
+++
<p></p>
{{% btn icon=" " context="success" href="https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999" %}}
Download Firmware
{{% /btn %}}

<p></p>

See the [firmware update tutorial](https://firmware.buspirate.com/tutorial-basics/firmware-update) for detailed instructions.

## Upgrade Instructions

- [Grab the latest and greatest auto-build firmware from the forum](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999)
- Type `$` and press `enter` in the Bus Pirate terminal to enter bootloader/upgrade mode
- The Bus Pirate will print the name of the firmware file to load before entering the bootloader, such as `bus_pirate5_rev10.uf2` or `bus_pirate6_rev2.uf2`
- A USB drive called RPI-RP2, RP2350 or BP__BOOT will connect to your computer, depending on hardware version
- Open the .zip archive and extract the correct firmware
- Drag the .uf2 firmware file into the USB drive

The file copies, the Bus Pirate resets, and you're good to go!

{{% alert context="danger" %}}
Bus Pirate blinking red? Recent firmware detects the hardware revision at startup. It will blink red if there is a mismatch.

[Enter the bootloader manually](https://firmware.buspirate.com/tutorial-basics/firmware-update#manually) (plug in the USB cable while pressing the button on the bottom side) and try the other file.
{{% /alert %}}

## Links

- [Download latest firmware build](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/99999)
- [Get help in the forum](https://forum.buspirate.com)
- [Bus Pirate 5 Hardware repo](https://github.com/DangerousPrototypes/BusPirate5-hardware)
- [Bus Pirate 5 Firmware repo](https://github.com/DangerousPrototypes/BusPirate5-firmware)

## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-cart.md" %}}
