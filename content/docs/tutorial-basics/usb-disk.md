+++
weight = 30800
title = 'USB Flash Storage'
+++

![](/images/docs/fw/usb-flash-storage.png)

The Bus Pirate has a NAND flash chip for storing settings and data. The flash chip also appears as a USB flash drive when the Bus Pirate is connected to a computer. Sharing the chip between the Bus Pirate and the computer operating system is a bit tricky.

## Navigation

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> ls
<span style="color:#96cb59">       350 <span style="color:#bfa530">bpconfig.bp</span></span>
<span style="color:#bfa530">0 dirs, 1 files</span>

<span style="color:#96cb59">HiZ></span> mkdir temp

<span style="color:#96cb59">HiZ></span> cd temp
/TEMP

<span style="color:#96cb59">HiZ></span> cd ..
/

<span style="color:#96cb59">HiZ></span> ls
<span style="color:#96cb59">       350 <span style="color:#bfa530">bpconfig.bp</span></span>
<span style="color:#96cb59">   &#x003c;DIR>   <span style="color:#bfa530">temp</span></span>
<span style="color:#bfa530">1 dirs, 1 files</span>

<span style="color:#96cb59">HiZ></span> rm temp

<span style="color:#96cb59">HiZ></span> ls
<span style="color:#96cb59">       350 <span style="color:#bfa530">bpconfig.bp</span></span>
<span style="color:#bfa530">0 dirs, 1 files</span>

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Linux-like commands are used to navigate the flash storage from the Bus Pirate command line. 

- ```ls```      List files
- ```cd```      Change directory
- ```mkdir```   Make directory
- ```rm```      Remove file/directory
- ```cat```     Print file contents as text
- ```hex```     Print file contents in HEX
- ```format```  Format storage disk (FAT16)
- ```label```   get or set the disk label

These common commands are supported in the firmware as of this update, but always use ```help``` or ```?``` to see the latest commands available. Add -h to any command for extended help: ```hex -h```.

## USB Flash Drive Use

![](/images/docs/fw/usb-flash-storage.png)


Sharing the NAND chip between the Bus Pirate and a computer is a bit tricky. The USB mass storage driver doesn't have a mechanism to signal when changes are made to the disk, leading to data corruption. This is why e.g. Android uses MTP protocol for file transfer.

To keep the Bus Pirate and the computer happy, and prevent data corruption, we use a bit of trickery. This can seem odd if you don't expect it.

### Read Only Mode

When a terminal is connected to the Bus Pirate, the flash storage appears as a read only disk to the computer. 

- Bus Pirate has read/write access to the disk
- The computer can read files from the disk
- The computer can't write to the disk
- The disk with re-attach after file changes

Let's elaborate on the last point. When the Bus Pirate makes changes to the flash - say saving a configuration file or dumping a flash chip - the drive will detach from the PC and then re-attach. This is to ensure that the computer sees the updated contents.

{{% alert context="info" %}}
The disk will detach and re-attach when the Bus Pirate writes to the disk.
{{% /alert %}}

### Read/Write Mode

When a terminal is not connected, the flash storage appears as a read/write disk to the computer. You can copy and delete files as you would with any other USB flash drive.

{{% alert context="info" %}}
To enable read/write mode, disconnect any terminals from the Bus Pirate serial ports.
{{% /alert %}}
