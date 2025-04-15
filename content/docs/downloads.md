+++
title = "Download Firmware"
description = ""
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 10000
+++
<p></p>
{{% btn icon="📁" context="danger" href="https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999" %}}
Download Firmware
{{% /btn %}}

<p></p>

See the [firmware update tutorial]({{< relref "tutorial-basics/firmware-update.md" >}}) for detailed instructions.

## Upgrading
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> $
Jump to bootloader for firmware upgrades

Bus Pirate 5 REV10
Firmware download:
https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999
Hardware revision: 10
Firmware file: bus_pirate5_rev10.uf2
A USB disk named "RPI-RP2" will appear
Drag a firmware file to the disk to upgrade
Later Alligator!
{{< /term >}}

- [Download the latest auto-build firmware from the forum](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/999999).
- Enter bootloader/upgrade mode by typing ```$``` in the Bus Pirate terminal and pressing ```Enter```.
- The Bus Pirate will display the firmware file name to load, such as ```bus_pirate5_rev10.uf2``` or ```bus_pirate6_rev2.uf2```.
- A USB drive will appear on your computer, named **RPI-RP2** (v5), **RP2350** (v6), or **BP__BOOT** (v6), depending on your hardware version.
- Extract the correct firmware file from the downloaded ```.zip``` archive.
- Drag and drop the ```.uf2``` firmware file into the USB drive.

Once the file is copied, the Bus Pirate will reset automatically, and you're ready to go!

{{% alert context="danger" %}}
**Red LED blinking?** The firmware checks the hardware revision at startup and blinks red if there's a mismatch.

[Manually enter the bootloader]({{< relref "tutorial-basics/firmware-update.md#manually" >}}) by plugging in the USB cable while holding the button on the bottom side, then try the other firmware file.
{{% /alert %}}

## Links

- [Detailed firmware update tutorial]({{< relref "tutorial-basics/firmware-update" >}})
- [Download latest firmware build](https://forum.buspirate.com/t/bus-pirate-5-auto-build-main-branch/20/99999)
- [Get help in the forum](https://forum.buspirate.com)
- [Bus Pirate Hardware repo](https://github.com/DangerousPrototypes/BusPirate5-hardware)
- [Bus Pirate Firmware repo](https://github.com/DangerousPrototypes/BusPirate5-firmware)

## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-cart.md" %}}
