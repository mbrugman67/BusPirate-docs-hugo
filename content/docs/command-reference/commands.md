+++
weight = 1
title = 'Commands'
+++

# Command Reference

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> i
<span style="color:#bfa530">
Bus Pirate 5 REV6
Firmware <span style="color:#53a6e6">v0.1</span></span> (<span style="color:#53a6e6">unknown</span>), Bootloader <span style="color:#53a6e6">N/A</span>
<span style="color:#53a6e6">RP2040</span> with <span style="color:#53a6e6">264KB</span> RAM, <span style="color:#53a6e6">16MB</span> FLASH
S/N: <span style="color:#53a6e6">2509449B952069E4</span>
https://DangerousPrototypes.com/
Flash Storage: <span style="color:#53a6e6"> 0.10GB</span> (FAT16)

<span style="color:#bfa530">Configuration file:</span> Loaded
<span style="color:#bfa530">Available modes:</span> HiZ UART I2C SPI LED DUMMY1
<span style="color:#bfa530">Active mode:</span> HiZ ()=()
<span style="color:#bfa530">Display format:</span> Auto

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

This guide is updated with to reflect feature changes with each firmware release. To check your firmware version type ```i``` followed by ```enter``` in the Bus Pirate terminal window. Here, the Bus Pirate is running firmware v0.1. 

{{% alert context="info" %}}
It's always best to use the latest firmware, especially in these early days of a new design. There will be continuous improvements and new features. See the upgrade guide for the simple drag and drop bootload process.
{{% /alert %}}

## User terminal

![](./img/cmd-toolbar.png)

The Bus Pirate is accessed from a command line in a serial terminal. Use your terminal of choice. On Windows we like the latest version of [Tera Term](https://ttssh2.osdn.jp/index.html.en).

{{% alert context="info" %}}
Talk to the Bus Pirate from a serial terminal of your choice set to 115200bps, 8/N/1. The serial port is emulated over USB, so higher bitrate (bps) settings will also work with no extra configuration. If the user interface feels slow, check that the speed is at least 115200bps.
{{% /alert %}}

### VT100 terminal emulation
{{< term "Bus Pirate [/dev/ttyS0]" >}}
VT100 compatible color mode? (Y/n)>
{{< /term >}}

Press ```enter``` to show the command prompt if your terminal is blank. 

If the Bus Pirate has just restarted you will be prompted to choose the terminal emulation mode.
- VT100 mode - Supports color and a live view statusbar at the bottom of the terminal. This should be your first choice unless you specifically need the legacy ASCII mode.
- ASCII mode - Legacy monochrome text only mode.

{{% alert context="info" %}}
If you choose VT100 mode and see lots of garbage characters in the terminal, check that your terminal emulator has VT100 support and that VT100 support is enabled.
{{% /alert %}}

Your terminal mode choice will be saved and automatically loaded the next time the Bus Pirate is connected. Just press ```enter``` to start the command prompt.

The terminal mode can be changed from the configuration menu. Open the configuration menu with the ```c``` command followed by ```enter```. 

{{% alert context="info" %}}
If you're stuck in a terminal mode that's not working, press and hold the Bus Pirate button and then plug in the USB cable. The Bus Pirate will start without loading any saved settings.

You can also navigate to the Bus Pirate USB disk, delete the bpconfig.bp file and restart the Bus Pirate. You will be prompted to choose VT100 or ASCII mode after restarting. 
{{% /alert %}}

### Command line
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

The Bus Pirate has a simple Linux-like command line interface. Enter a command followed by optional parameters and then press ```enter```.

The Bus Pirate always starts in high impedance mode (HiZ), a safe mode with all outputs disabled. HiZ mode intends to protect any connected devices from conditions beyond their specifications. From the HiZ prompt, a bus mode can be selected to use a specific protocol.

### Terminal control

| Keyboard Key  |Action          |
|---------------|-----------------|
| ```left arrow```  |  Moves the cursor left one character                                                                |
| ```right arrow``` |  Moves the cursor right one character                                                               |
| ```up arrow```    |  Copies the previous command in the command history buffer to the command line                      |
| ```down arrow```  |  Copies the next command in the command history buffer to the command line                          |
| ```home```        | Moves the cursor to the beginning of the line                                                      |
| ```end```         |  Moves the cursor to the end of the line                                                            |
| ```backspace```   |  Erases the character to the left of the cursor and moves the cursor left one character             |
| ```delete```      |  Erases the character under (or to the right of) the cursor and moves the cursor left one character |

Bus Pirate 5 understands some common control keys.

### Default options

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">Mode ></span> 3

<span style="color:#bfa530">I2C speed</span>
 1KHz to 1000KHz
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">KHz (</span>400KHz*<span style="color:#96cb59">) ></span> 

<span style="color:#bfa530">Data bits</span>
 1. <span style="color:#bfa530">8*</span>
 2. <span style="color:#bfa530">10</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Bits (</span>1<span style="color:#96cb59">) ></span> 

<span style="color:#bfa530">Mode:</span> I2C

<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Most configuration and option prompts have a default value shown in ( ) and the option to exit without changes.
- Press ```enter``` to select the default option. 
- Press ```x``` followed by ```enter``` to exit a menu without changes.

### Saved options

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">Mode ></span> 3

<span style="color:#bfa530">Use previous settings?</span>
 I2C speed: 400KHz
 Data bits: 8
y/n> y

<span style="color:#bfa530">Mode:</span> I2C

<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Many options will be saved to flash storage. You will be prompted to reloaded previous settings the next time.

## Disk Commands
Several Linux-like disk commands can be used to navigate the Bus Pirate flash storage.

### **ls** List directory contents

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> ls
   DIR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System Volume Information
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;81&nbsp;&nbsp;bpspi.bp
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;256&nbsp;&nbsp;test.txt
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;333&nbsp;&nbsp;bpconfig.bp
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35&nbsp;&nbsp;bpi2c.bp
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31&nbsp;&nbsp;bpled.bp
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;256&nbsp;&nbsp;sample.txt
1 dirs, 6 files.

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

List the contents of the current directory in flash storage. Type ```ls``` followed by ```enter```. ``ls`` followed by a directory name lists the contents of that directory.

### **mkdir** Make directory

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> mkdir test

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Make a directory in the current location in the flash storage. Type ```mkdir``` followed by a directory name and then ```enter```.

### **cd** Change directory

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> cd test
/test

<span style="color:#96cb59">HiZ></span> ls
0 dirs, 0 files.

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Change directory. Type ```cd``` followed by a directory name and then ```enter```.

### **rm** Remove file or directory

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> rm test

<span style="color:#96cb59">HiZ></span>
{{< /term >}}

Remove file or directory (if empty). Type ```rm``` followed by the name of a file or empty directory, then hit ```enter```.

### **cat** Print file contents

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> cat sample.txt
Bus Pirate 5 can program and dump EEPROM, flash and other memory chips directly to the flash storage! No need for external software on your computer. No need to install toolchains and compile scripts. What you need, where you need it. Bus Pirate 5 is here! --EOM

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Print the contents of a file. Type ```cat``` followed by a file name, then hit ```enter```.

## Configuration

### **?/h/H** Help menu with latest options

![Bpv52-help](./img/bp-term2.png)

Type ```?``` followed by ```enter``` to display a help screen with all available menu and syntax options in the current firmware.

### **i** Version information
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> i
<span style="color:#bfa530">
Bus Pirate 5 REV6
Firmware <span style="color:#53a6e6">v8</span></span> (<span style="color:#53a6e6">unknown</span>), Bootloader <span style="color:#53a6e6">N/A</span>
<span style="color:#53a6e6">RP2040</span> with <span style="color:#53a6e6">264KB</span> RAM, <span style="color:#53a6e6">16MB</span> FLASH
S/N: <span style="color:#53a6e6">2509449B952069E4</span>
https://DangerousPrototypes.com/
Flash Storage: <span style="color:#53a6e6"> 0.10GB</span> (FAT16 File System)

<span style="color:#bfa530">Configuration file:</span> Loaded
<span style="color:#bfa530">Available modes:</span> HiZ UART I2C SPI LED DUMMY1
<span style="color:#bfa530">Active mode:</span> HiZ ()=()
<span style="color:#bfa530">Display format:</span> Auto

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Type ```i``` followed by ```enter``` to see the hardware, firmware, and microcontroller version.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">Active mode:</span> HWI2C (speed)=(0)
<span style="color:#bfa530">Display format:</span> Auto
<span style="color:#bfa530">Data format:</span> 8 bits, MSB bitorder
<span style="color:#bfa530">Pull-up resistors:</span> ON
<span style="color:#bfa530">Power supply:</span> ON (3.3V/3.3V)
<span style="color:#bfa530">Current limit:</span> OK (8.0mA/50.0mA)
<span style="color:#bfa530">Frequency generators:</span> OFF
{{< /term >}}

If a bus mode is configured additional
 information about the configuration is printed.

### **c** Configuration options menu

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> c
<span style="color:#bfa530">
<span style="color:#bfa530">Configuration options</span></span>
 1. <span style="color:#bfa530">Language</span>
 2. <span style="color:#bfa530">ANSI color mode</span>
 3. <span style="color:#bfa530">ANSI toolbar mode</span>
 4. <span style="color:#bfa530">LCD screensaver</span>
 5. <span style="color:#bfa530">LED effect</span>
 6. <span style="color:#bfa530">LED color</span>
 7. <span style="color:#bfa530">LED brightness</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 1

<span style="color:#bfa530">Language</span>
 1. <span style="color:#bfa530">English</span>
 2. <span style="color:#bfa530">Chinese (simplified)</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 1
Language <span style="color:#bfa530">set to</span> English

<span style="color:#bfa530">Configuration options</span>
 1. <span style="color:#bfa530">Language</span>
 2. <span style="color:#bfa530">ANSI color mode</span>
 3. <span style="color:#bfa530">ANSI toolbar mode</span>
 4. <span style="color:#bfa530">LCD screensaver</span>
 5. <span style="color:#bfa530">LED effect</span>
 6. <span style="color:#bfa530">LED color</span>
 7. <span style="color:#bfa530">LED brightness</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> x

<span style="color:#bfa530">Configuration file:</span> Saved

<span style="color:#96cb59">I2C></span>
{{< /term >}}

Type ```c``` followed by ```enter``` to show the configuration menu. 

Press ```x``` followed by ```enter``` to exist the configuration menus and save the current settings to flash storage.

### **m** Set bus mode

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> m
<span style="color:#bfa530">
<span style="color:#bfa530">Mode selection</span></span>
 1. <span style="color:#bfa530">HiZ</span>
 2. <span style="color:#bfa530">UART</span>
 3. <span style="color:#bfa530">I2C</span>
 4. <span style="color:#bfa530">SPI</span>
 5. <span style="color:#bfa530">LED</span>
 6. <span style="color:#bfa530">DUMMY1</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Mode ></span> 1
<span style="color:#bfa530">Mode:</span> HiZ
<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

Type ```m``` followed by ```enter``` to select a bus mode. HiZ is a safe mode with all pins set to high-impedance and all peripherals disabled.

### **l/L** Set MSB/LSB first
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> l
<span style="color:#bfa530"><span style="color:#bfa530">Bitorder:</span></span> MSB 0b<span style="color:#bfa530">1</span>0000000
<span style="color:#96cb59">HiZ></span> L
<span style="color:#bfa530"><span style="color:#bfa530">Bitorder:</span></span> LSB 0b0000000<span style="color:#bfa530">1</span>
<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

The l/L commands determines the [bit order](http://en.wikipedia.org/wiki/Most_significant_bit) for reading and writing bytes. 

The current bit order configuration is displayed on the extended information screen using the ```i``` command while in a mode other than HiZ.

### **o** Data output display format
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> o
<span style="color:#bfa530">
<span style="color:#bfa530">Number display format</span></span>
 <span style="color:#bfa530">Current setting: Auto</span>
 1. <span style="color:#bfa530">Auto</span>
 2. <span style="color:#bfa530">HEX</span>
 3. <span style="color:#bfa530">DEC</span>
 4. <span style="color:#bfa530">BIN</span>
 5. <span style="color:#bfa530">ASCII</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Mode ></span> 1
<span style="color:#bfa530">Mode:</span> Auto
<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

The Bus Pirate can display values as [hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal), [decimal](http://en.wikipedia.org/wiki/Decimal), [binary](http://en.wikipedia.org/wiki/Binary_numeral_system) and a raw
[ASCII](http://en.wikipedia.org/wiki/ASCII) byte. Change the setting in
the data display format menu (o). The default display format is Auto.

- Auto display mode attempts to mirror user input formatting. Each value is displayed in the HEX/DEC/BIN format entered.
- RAW display mode sends data to the terminal as raw bytes without any text conversion. This is useful for talking to ASCII serial interfaces that don't need further conversion.

### **d** Display mode
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> d
<span style="color:#bfa530">Display selection
 1. Default
 2. Scope
 x. Exit</span>
<span style="color:#96cb59">Display ></span> 2
<span style="color:#bfa530">Display:</span> Scope
{{< /term >}}

```d``` selects the LCD display mode.
1. Default: Pin labels and voltage
2. Scope: Oscilloscope mode

### **~** Self-test 
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> ~
<span style="color:#bfa530">SELF TEST STARTING
DISABLE IRQ: OK
ADC SUBSYSTEM: VUSB  5.08V OK
DAC READ/WRITE: OK
FLASH STORAGE: OK
PSU ENABLE: OK
BIO FLOAT TEST (SHOULD BE 0/0.2V)
BIO0 FLOAT: 0/0.04V OK
BIO1 FLOAT: 0/0.04V OK
BIO2 FLOAT: 0/0.04V OK
BIO3 FLOAT: 0/0.04V OK
BIO4 FLOAT: 0/0.04V OK
BIO5 FLOAT: 0/0.04V OK
BIO6 FLOAT: 0/0.04V OK
BIO7 FLOAT: 0/0.04V OK
BIO HIGH TEST (SHOULD BE >3.0V)</span>
{{< /term >}}

Perform a factory self-test. The Bus Pirate is capable of twiddling pins and checking for hardware faults. See the Bus Pirate self-test guide for a complete list of tests and the problems they detect.

### **#** Reset

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> #

VT100 compatible color mode? (Y/n)>
{{< /term >}}

Reset the Bus Pirate. 

Depending on your serial terminal software you may need to reconnect to the Bus Pirate serial port. The latest versions of many terminal emulators, such as Tera Term, reconnect automatically.

### **$** Jump to bootloader 
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> $
{{< /term >}}

Activate the Bus Pirate bootloader for firmware updates. The bootloader appears as a USB disk drive connected to your computer. Drag a **.uf2** firmware file into the disk. After an update the Bus Pirate resets.

{{% alert context="info" %}}
If the firmware update is interrupted and you find yourself locked out of the Bus Pirate terminal don't panic. Use the 2mm HEX key included with Bus Pirate 5 (or a paperclip) to press and hold the bootloader button on the bottom of the board. Plug in the USB cable while holding the button down. The bootloader with connect and you can try the update again. The bootloader is frozen in hardware and cannot be corrupted or overwritten.
{{% /alert %}}

## Utilities

### **w/W** Power supply (off/ON) 
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> W
<span style="color:#bfa530"><span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span></span>
<span style="color:#96cb59">x to exit (3.30) ></span> 2.1
<span style="color:#53a6e6">2.10</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">2.10</span></span>V
Set current limit?
y

<span style="color:#bfa530">Maximum current (0mA-500mA)</span>
<span style="color:#96cb59">x to exit (100.00) ></span> 50
<span style="color:#53a6e6">50.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">50.0</span></span>mA

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">
Vreg output: <span style="color:#53a6e6">2.1</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">2.1</span></span>V<span style="color:#bfa530">, Current sense: <span style="color:#53a6e6">7.3</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Bus Pirate 5 has a single 'Programmable Power Supply Unit' (PPSU) with several handy features:
- 1-5volts adjustable output
- 0-500mA current sense 
- 0-500mA current limit with digital fuse
- One-way valve to protect the PPSU when an external voltage is applied to the VREF/VOUT pin

Uppercase ```W``` enables the onboard power supply unit. You will be prompted for the output voltage and an optional current limit.

Check the voltage and current in the live view statusbar if active, or show the power supply voltage report using the ```v``` command.

{{% alert context="danger" %}}
400mA is the rated maximum of the PPSU, but we added some headroom in the current limit to account for current spikes.

The PPSU is capable of 0.8 to 5volts output. However, the maximum working range is limited to 1-5volts because of the Vgs of the P-channel MOSFET used in the one-way valve. Many will be capable of the full range, but some may not. The Bus Pirate 5 IO buffers are only rated to 1.65volts, so in practice this isn't an issue over the specified working range.
{{% /alert %}}

When the programmed current limit is exceeded the PPSU hardware fuse disables the power supply. The terminal colors invert repeatedly, an alarm bell will sound, an error message is shown and command execution is halted. Use the ```W``` command to restart the PPSU again.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span>w
<span style="color:#bfa530"><span style="color:#bfa530">Power supply: </span></span>Disabled
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Lowercase ```w``` disables the PPSU.

### **v/V** Power supply voltage report 

{{< term "Bus Pirate [/dev/ttyS0]" >}}

![](./img/cmd-v.png)

{{< /term >}}

The voltage report shows the current state of all the Bus Pirate pins and peripherals. This is a duplicate of the information shown on the live view statusbar.

- The first line is the pin number and probe color. The colors also match the Bus Pirate LCD and the live view statusbar.
- The second line is the pin function.
- The third line shows the voltage measured
 on each pin. 

Lowercase ```v``` displays a one time voltage measurement. Uppercase ```V``` displays a continuously updated voltage measurement, press any key to exit.

### **p/P** Pull-up resistors 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> P
<span style="color:#bfa530"><span style="color:#bfa530">Pull-up resistors:</span></span> Enabled (10Kohms @ <span style="color:#53a6e6">3.3</span>V)

<span style="color:#96cb59">I2C></span> p
<span style="color:#bfa530"><span style="color:#bfa530">Pull-up resistors:</span></span> Disabled

<span style="color:#96cb59">I2C></span> 
{{< /term >}}

```p``` and ```P``` toggle the pull-up resistors off and on. Pull-up resistors are generally used with open collector/open drain bus types such as 1-Wire and I2C.

The onboard pull-up resistors **are powered through the VREF/VOUT pin
of the IO header**, either by the onboard power supply or an external voltage applied to the VREF/VOUT pin. 

{{% alert context="info" %}}
A warning is displayed if there's no voltage on the VREF/VOUT pin. Check the voltage report ```v``` and verify that a voltage is present on VOUT/VREF.
{{% /alert %}}

### **g/G** Frequency generator

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> G
<span style="color:#bfa530"><span style="color:#bfa530">Generate frequency</span></span>
<span style="color:#bfa530">Choose available pin:</span>
 0. IO<span style="color:#53a6e6">0</span>
 1. IO<span style="color:#53a6e6">1</span>
 2. IO<span style="color:#53a6e6">2</span>
 3. IO<span style="color:#53a6e6">3</span>
 4. IO<span style="color:#53a6e6">4</span>
 5. IO<span style="color:#53a6e6">5</span>
 6. IO<span style="color:#53a6e6">6</span>
 7. IO<span style="color:#53a6e6">7</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 0
<span style="color:#96cb59">Period or frequency (ns, us, ms, Hz, KHz or Mhz) ></span> 12.4KHz
<span style="color:#bfa530">Frequency:</span> <span style="color:#53a6e6">12.400</span>KHz = <span style="color:#53a6e6">12400</span>Hz (<span style="color:#53a6e6">12.40</span>KHz)
<span style="color:#bfa530">Period:</span> <span style="color:#53a6e6">80645</span>ns (<span style="color:#53a6e6">80.65</span>us)

<span style="color:#bfa530">Actual frequency:</span> <span style="color:#53a6e6">12401</span>Hz (<span style="color:#53a6e6">12.40</span>KHz)
<span style="color:#bfa530">Actual period:</span> <span style="color:#53a6e6">80640</span>ns (<span style="color:#53a6e6">80.64</span>us)

<span style="color:#96cb59">Duty cycle (%) ></span> 35%
<span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.00</span>% = <span style="color:#53a6e6">28224</span>ns (<span style="color:#53a6e6">28.22</span>us)
<span style="color:#bfa530">Actual duty cycle:</span> <span style="color:#53a6e6">28227</span>ns (<span style="color:#53a6e6">28.23</span>us)
Divider: 16, Period: 10079, Duty: 3528

<span style="color:#bfa530">Generate frequency:</span> Enabled on IO<span style="color:#53a6e6">0</span>

<span style="color:#96cb59">LED-()></span>
{{< /term >}}

Uppercase ```G``` displays the frequency generation menu. Choose an available pin and enter the period or frequency, including the units (ns, us, ms, Hz, KHz or Mhz). Enter a duty cycle as a percent, don't forget the ```%```. The Bus Pirate will find the closest match and generate a frequency on the pin. 

{{< term "Bus Pirate [/dev/ttyS0]" >}}

![](./img/cmd-freq.png)

{{< /term >}}

The frequency generator will be displayed in the live view statusbar and on the LCD with the label ***PWM***.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> g 0
<span style="color:#bfa530">Generate frequency:</span> Disabled on IO<span style="color:#53a6e6">0</span>

<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

To stop the frequency generator on a single pin, use the lowercase ```g.X``` command where X is the pin number.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> g
<span style="color:#bfa530">Generate frequency:</span> Disabled on IO<span style="color:#53a6e6">0</span>

<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

To stop frequency generation on all pins, use the lowercase ```g``` command without specifying a pin.

{{% alert context="danger" %}}
Not all pins will be available due to the PWM structure of the RP2040, and adjacent pairs must share the same frequency. There is also an issue with the PPSU using a PWM slice. This should all be solvable with the PIO, but for now the Bus Pirate will warn you about the limitations.
{{% /alert %}}

### **f/F** Measure frequency

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> F
<span style="color:#bfa530"><span style="color:#bfa530">Frequency measurement</span></span>
<span style="color:#bfa530">Choose available pin:</span>
 1. IO<span style="color:#53a6e6">1</span>
 3. IO<span style="color:#53a6e6">3</span>
 5. IO<span style="color:#53a6e6">5</span>
 7. IO<span style="color:#53a6e6">7</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 7
<span style="color:#bfa530">Frequency measurement:</span> Enabled on IO<span style="color:#53a6e6">7</span>
<span style="color:#bfa530">Frequency</span> IO<span style="color:#53a6e6">7</span>: <span style="color:#53a6e6">12.40</span>KHz <span style="color:#53a6e6">80.65</span>us (<span style="color:#53a6e6">12400</span>Hz), <span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.0</span>%

<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

```F``` displays the frequency measurement menu. Choose one of the available pins. 

{{< term "Bus Pirate [/dev/ttyS0]" >}}

![](./img/cmd-freq.png)

{{< /term >}}

The frequency will be measured continuously and displayed in the live view statusbar and LCD with the label **FREQ**.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> f 7
<span style="color:#bfa530"><span style="color:#bfa530">Frequency</span></span> IO<span style="color:#53a6e6">7</span>: <span style="color:#53a6e6">12.40</span>KHz <span style="color:#53a6e6">80.65</span>us (<span style="color:#53a6e6">12400</span>Hz), <span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.0</span>%
<span style="color:#96cb59">LED-()></span>
{{< /term >}}

Lowercase ```f X``` measures the frequency and duty cycle on pin X once.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> F 7
<span style="color:#bfa530"><span style="color:#bfa530">Press any key to exit</span></span>
<span style="color:#bfa530">Frequency</span> IO<span style="color:#53a6e6">7</span>: <span style="color:#53a6e6">12.40</span>KHz <span style="color:#53a6e6">80.65</span>us (<span style="color:#53a6e6">12400</span>Hz), <span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">35.0</span>%
{{< /term >}}

Uppercase ```F X``` continuously measures the frequency and duty cycle on pin X. Press any key to exit.


{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> f 6
<span style="color:#bfa530">IO6 has no frequency measurement hardware!
Freq. measure is currently only possible on odd pins (1,3,5,7).
In the future we will fix this using the RP2040 PIO.
</span>
{{< /term >}}

Only half of the RP2040 pins support frequency measurement. The Bus Pirate will warn you if hardware isn't available. To see which pins are currently available use the ```F``` command.

{{% alert context="danger" %}}
Not all pins will be available due to the PWM structure of the RP2040, and adjacent pairs share the same PWM slice. There is also an issue with the PPSU using a PWM slice. This should all be solvable with the PIO, but for now the Bus Pirate will warn you about the limitations.
{{% /alert %}}

### **=X** Convert X to HEX/DEC/BIN number format

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> = 0b110
<span style="color:#bfa530"> </span>=0x<span style="color:#53a6e6">06</span> =6 =0b<span style="color:#53a6e6">0000</span>0110
<span style="color:#96cb59">I2C></span> = 0x6
<span style="color:#bfa530"> </span>=0x<span style="color:#53a6e6">06</span> =6 =0b<span style="color:#53a6e6">0000</span>0110
<span style="color:#96cb59">I2C></span> = 6
<span style="color:#bfa530"> </span>=0x<span style="color:#53a6e6">06</span> =6 =0b<span style="color:#53a6e6">0000</span>0110
<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Type ```=``` and enter a value to see the HEX/DEC/BIN equivalent. Base conversion command, available in all modes. 

{{% alert context="info" %}}
To change the Bus Pirate output display format see the ```o``` command.
{{% /alert %}}

### **| X** Reverse bits in byte X 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> | 0b11110000
<span style="color:#bfa530">|0x0F000000.32|0001700000000.32|0b00001111000000000000000000000000.32</span>
<span style="color:#96cb59">I2C></span>
{{< /term >}}

Reverse bit order in byte X. Displays the HEX/DEC/BIN value of the reversed byte.

{{% alert context="info" %}}
To change the Bus Pirate read/write bit order see the ```l```/```L``` command.
{{% /alert %}}

### **a/A/@** Auxiliary pin control (low/HIGH/read)

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">UART></span> a 1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> OUTPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">UART></span> A 1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> OUTPUT: <span style="color:#53a6e6">1</span>

<span style="color:#96cb59">UART></span> @ 1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> INPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">UART></span>
{{< /term >}}

Sometimes it's useful to control a pin directly from the user terminal.
 ```a X```, ```A X``` and ```@ X``` set pin X low, high and input (HiZ). The ```@``` command also reads and reports the pin state.

{{% alert context="info" %}}
Commands a/A/@ are followed by a space and the pin number to control. This is different than syntax a/A/@  which use the ```a.X``` notation.
{{% /alert %}}

{{% alert context="info" %}}
Pins already assigned a function cannot be changed with the a/A/@ commands. The Bus Pirate will report an error.
{{% /alert %}}


## Macros

Macros perform complex actions, like scanning for I2C addresses,
interrogating a smart card or probing a JTAG chain. Macros are numbers
entered inside ```( )```. Macro ```(0)``` always displays a list of macros available in the current bus mode.

### **(0)** List mode macros 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> (0)
<span style="color:#bfa530"> 1. I2C Address search
</span>
<span style="color:#96cb59">I2C></span>
{{< /term >}}

Macro ```(0)``` always displays a list of macros available in the current bus mode.

### **(#)** Run macro 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> (1)
<span style="color:#bfa530">
I2C Bus Scan
   0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
00 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
10 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
20 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
30 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
40 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
50 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
60 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
70 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
Done.
</span>
<span style="color:#96cb59">I2C></span>
{{< /term >}}

Execute a macro by typing the macro number between ```( )```.

