+++
weight = 13
title = 'SPI Protocol'
+++

-   **Bus:** [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) (serial peripheral interface)
-   **Connections:** four pins (CDO/CDI/CLK/CS) and ground
-   **Output type:** 1.65-5volts
-   **Maximum voltage:** 5volts

SPI is a common 4 wire full duplex protocol. Separate connections for data-in and data-out allow communication to and from the controller at the same time. Multiple sub devices can share the bus, but each will need an individual Chip Select (CS) connection. Chip Select is generally active when low.

## Connections

| Bus Pirate | Direction                    | Circuit | Description          |
|------------|--------------------------|---------|----------------------|
| MOSI       | <font size="+2">→</font> | MOSI    | Master Out Sub In |
| MISO       | <font size="+2">←</font> | MISO    | Master In Sub Out |
| CS         | <font size="+2">→</font> | CS      | Chip Select          |
| CLK        | <font size="+2">→</font> | CLK     | Clock signal         |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground        |

## Configuration options

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">SPI speed</span>
 1 to 62500KHz
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">KHz (</span>100KHz*<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Data bits</span>
 4 to 8 bits
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Bits (</span>8*<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Clock polarity</span>
 1. <span style="color:#bfa530">Idle LOW*</span>
 2. <span style="color:#bfa530">Idle HIGH</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Polarity (</span>1<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Clock phase</span>
 1. <span style="color:#bfa530">LEADING edge*</span>
 2. <span style="color:#bfa530">TRAILING edge</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Phase (</span>1<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Chip select</span>
 1. <span style="color:#bfa530">Active HIGH (CS)</span>
 2. <span style="color:#bfa530">Active LOW (/CS)*</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">CS (</span>2<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Actual speed:</span> 122KHz
<span style="color:#bfa530">Mode:</span> SPI
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

## Syntax

|Command|Description|
|-------|--------------|
| [ | Chip select (CS) active (low)|
| \{ | CS active (low), show the SPI read byte after every write   |
| ] or } | CS disable (high)|
| r    | Read one byte by sending dummy byte (0xff). (r:1…255 for bulk reads) |
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |
| \(#\)   | Run macro, (0) for macro list. |

## Macro

| Number  |Description  |
|-----|-----------------|
| 0   | Macro menu      |

<!-- 

| 1   | SPI bus sniffer, sniff when CS is low (hardware CS filter)                                                |
| 2   | SPI bus sniffer, sniff all traffic (no CS filter)                                                         |
| 3   | <s>SPI bus sniffer, sniff when CS is high (software CS filter)</s> Temporarily removed to increase speed. |
| 10  | Change clock polarity to 0 without re-entering SPI mode                                                   |
| 11  | Change clock polarity to 1 without re-entering SPI mode                                                   |
| 12  | Change clock edge to 0 without re-entering SPI mode                                                       |
| 13  | Change clock edge to 1 without re-entering SPI mode                                                       |
| 14  | Change sample phase to 0 without re-entering SPI mode                                                     |
| 15  | Change sample phase to 1 without re-entering SPI mode                                                     |

### SPI Bus sniffer

The Bus Pirate can read the traffic on an SPI bus.

The SPI sniffer is implemented in hardware and should work up to 10MHz.
It follows the configuration settings you entered for SPI mode.

`Warning! Enter sniffer mode before connecting the target!!`  
`The Bus Pirate SPI CLOCK or DATA lines could be grounded and ruin the target device!`  
`Reset with the CS pin to clear garbage if needed`

Pin connections are the same as normal SPI mode. Connect the Bus Pirate
clock to the clock on the SPI bus you want to sniff. The data pins MOSI
and MISO are both inputs, connect them to the SPI bus data lines.
Connect the CS pin to the SPI bus CS pin.

-   \[/\] – CS enable/disable
-   0xXX – MOSI read
-   (0xXX) – MISO read

SPI CS pin transitions are represented by the normal Bus Pirate syntax.
The byte sniffed on the MISO pin is displayed inside (). 
```
SPI> (0)
0.Macro menu
1.Sniff CS low
2.Sniff all traffic
SPI> (1) 
Sniffer 
Any key to exit
[0x30(0x00)0xff(0x12)0xff(0x50)][0x40(0x00)] 
```
The SPI sniffer
can read all traffic, or filter by the state of the CS pin. The byte
sniffed on the MOSI pin is displayed as a HEX formatted value, the byte
sniffed on the MISO pin is inside the ().

`There may be an issue in the sniffer terminal mode from v5.2+.`  
`Try the `[`binary`` ``mode`` ``sniffer`` ``utility`](http://dangerousprototypes.com/docs/Bus_Pirate_binary_SPI_sniffer_utility)` for best results.`

**Notes**

The sniffer uses a 4096byte output [ring
buffer](http://en.wikipedia.org/wiki/Circular_buffer). Sniffer output
goes into the ring buffer and gets pushed to the PC when the UART is
free. This should eliminate problems with dropped bytes, regardless of
UART speed or display mode.

`Warning! Enter sniffer mode before connecting the target!!`  
`The Bus Pirate SPI CLOCK or DATA lines could be grounded and ruin the target device!`  
`Reset with the CS pin to clear garbage if needed`

-   A long enough stream of data will eventually overtake the buffer,
    after which the MODE LED turns off (v5.2+). No data can be trusted
    if the MODE LED is off - this will be improved in a future firmware.
-   The SPI hardware has a 4 byte buffer. If it fills before we can
    transfer the data to the ring buffer, then the terminal will display
    "Can't keep up" and drop back to the SPI prompt. This error and the
    ring buffer error will be combined in a future update.
-   Any commands entered after the sniffer macro will be lost.
-   Pins that are normally output become inputs in sniffer mode. MOSI,
    CLOCK, MISO, and CS are all inputs in SPI sniffer mode.
-   Since v5.3 the SPI sniffer uses hardware chip select for the CS low
    sniffer mode. The minimum time between CS falling and the first
    clock is 120ns theoretical, and less then 1.275us in tests. The
    software CS detect (CS high sniffer mode) requires between 27usec
    and 50usec minimum delay between the transition of the CS line and
    the start of data. Thanks to Peter Klammer for testing and updates.
-   The sniffer follows the output clock edge and output polarity
    settings of the SPI mode, but not the input sample phase.

### Clock edge/clock polarity/sample phase macros

Macros 10-15 change SPI settings without disabling the SPI module. I
have no idea if this will work or if it's allowable. These macros were
added at a user's request, but they never reported if it worked. [More
here](http://dangerousprototypes.com/forum/index.php?topic=870.msg9082#msg9082).
```
SPI> (10)(11)(12)(13)(14)(15) 
SPI (spd ckp ske smp csl hiz)=( 3 0 1 0 1 1 ) 
SPI (spd ckp ske smp csl hiz)=( 3 1 1 0 1 1 ) 
SPI (spd ckp ske smp csl hiz)=( 3 1 0 0 1 1 ) 
SPI (spd ckp ske smp csl hiz)=( 3 1 1 0 1 1 ) 
SPI (spd ckp ske smp csl hiz)=( 3 1 1 0 1 1 ) 
SPI (spd ckp ske smp csl hiz)=( 3 1 1 1 1 1 ) 
SPI>
```

-->



## Commands

Bus Pirate 5 has global commands available everywhere, and mode commands specific to the currently selected mode. Type ```help``` to see all commands in every mode, or ```help mode``` for the currently available mode commands.

### flash 

The ```flash``` command can read, write, and erase common SPI flash memory chips directly in the Bus Pirate terminal. The [Serial Flash Universal Driver](https://github.com/armink/SFUD) at the heart of the flash command attempts to identify the flash chip and select the appropriate settings. Most modern flash chips contain SFDP tables that describe the chip capabilities. If a chip doesn't have SFDP tables, the driver has a database of common chips on which to fall back .

#### Help
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash -h
usage:
<span style="color:#bfa530">flash [init|probe|erase|write|read|verify|test]
	[-f(ile)] [-e(rase)] [-v(verify)] [-h(elp)]</span>
<span style="color:#bfa530">Initialize and probe: flash probe</span>
<span style="color:#bfa530">Erase and program, with verify: flash write -f example.bin -e -v</span>
<span style="color:#bfa530">Read to file: flash read -f example.bin</span>
<span style="color:#bfa530">Verify with file: flash verify -f example.bin</span>
<span style="color:#bfa530">Test chip (full erase/write/verify): flash test</span>
<span style="color:#bfa530">Force dump: flash read -o -b bytes -f file</span>

<span style="color:#bfa530">read, write and erase flash chips using SFDP info if available</span>
<span style="color:#96cb59">init</span>	<span style="color:#bfa530">Reset and initialize flash chip. Default if no options given. flash</span>
<span style="color:#96cb59">probe</span> <span style="color:#bfa530">Probe flash chip for ID and SFDP info. flash probe</span>
<span style="color:#96cb59">erase</span>	<span style="color:#bfa530">Erase flash chip. flash erase [-v(erify)]</span>
<span style="color:#96cb59">write</span>	<span style="color:#bfa530">Write file to flash chip. flash write -f file [-e(rase)] [-v(erify)]</span>
<span style="color:#96cb59">read</span>	<span style="color:#bfa530">Read flash chip to file. flash read -f file</span>
<span style="color:#96cb59">verify</span>	<span style="color:#bfa530">Verify flash chip against file. flash verify -f file</span>
<span style="color:#96cb59">test</span>	<span style="color:#bfa530">Erase and write full chip with dummy data, verify. flash test</span>
<span style="color:#96cb59">-f</span>	<span style="color:#bfa530">File flag. File to write, read or verify. flash verify -f file</span>
<span style="color:#96cb59">-e</span>	<span style="color:#bfa530">Erase flag. Add erase before write. flash write -f file -e</span>
<span style="color:#96cb59">-v</span>	<span style="color:#bfa530">Verify flag. Add verify after write or erase. flash write -f file -v</span>
{{< /term >}}

 
{{% alert context="info" %}}
Use ```flash -h``` to see the latest options and features.
{{% /alert %}}

Most Bus Pirate commands have help and usage examples. Add the ```-h``` flag to any command to see the available options and examples.

#### Options and flags

| Option | Description |
|---------|-------------|
| ```flash init``` | Reset and initialize flash chip. Default if no options given. |
| ```flash probe``` | Probe flash chip for ID and SFDP info. |
| ```flash erase``` | Erase flash chip. |
| ```flash write``` | Write file to flash chip. Specify file with -f flag. Use -e flag to erase before write|
| ```flash read``` | Read flash chip to file. Specify file with -f flag|
| ```flash verify``` | Verify flash chip against file. Specify file with -f flag |
| ```flash test``` | Erase and write full chip with dummy data, verify. |

| Flag | Description |
|------|-------------|
| ```-f``` | File flag. File to write, read or verify. |
| ```-e``` | Erase flag. Add erase before write. |
| ```-v``` | Verify flag. Add verify after write or erase. |

#### Initialize and identify a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash init
Probing:
		Device ID	Manuf ID	Type ID		Capacity ID
RESID (0xAB)	0x13
REMSID (0x90)	0x13		0xef
RDID (0x9F)			0xef		0x40		0x14

Initializing SPI flash...
Flash device manufacturer ID 0xEF, type ID 0x40, capacity ID 0x14
SFDP V1.5, 0 parameter headers
		Type		Ver.	Length	Address
Table 0		JEDEC (0x00)	1.5	64B	0x000080
JEDEC basic flash parameter table info:
MSB-LSB  3    2    1    0
[0001] 0xFF 0xF1 0x20 0xE5
...
[0009] 0x00 0x00 0xD8 0x10
4 KB Erase is supported throughout the device (instruction 0x20)
Write granularity is 64 bytes or larger
Flash status register is non-volatile
3-Byte only addressing
Capacity is 1048576 Bytes
Flash device supports 4KB block erase (instruction 0x20)
Flash device supports 32KB block erase (instruction 0x52)
Flash device supports 64KB block erase (instruction 0xD8)
Found a Winbond  flash chip (1048576 bytes)
Flash device reset success
{{< /term >}}

```flash```, ```flash init```, and ```flash probe``` provide various levels of details about a flash chip. The flash command tries three common methods to identify a flash chip (RESID, REMSID, RDID), then attempts to read the SFDP tables.  

#### Read a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash read -f example.bin
Reading 1048576 bytes from flash to example.bin
[-------C o o o o o]
{{< /term >}}

Read the contents of a flash chip to a file with the ```flash read``` command. The file name is specified with the ```-f``` flag.

#### Write a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash write -f example.bin -e -v
Erasing 1048576 bytes
[-----------------C]
Writing 1048576 bytes from example.bin to flash
[-----------------C]
Verifying 1048576 bytes from example.bin to flash
[-------c o o o o]
{{< /term >}}

Write a file to a flash chip with the ```flash write``` command. The file name is specified with the ```-f``` flag. Use the ```-e``` flag to erase the chip before writing, and the ```-v``` flag to verify the write.

#### Verify a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash verify -f example.bin
Verifying 1048576 bytes from example.bin to flash
[-------c o o o o]
{{< /term >}}

Verify the contents of a flash chip against a file with the ```flash verify``` command. The file name is specified with the ```-f``` flag.

#### Test a flash chip

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> flash test
Erasing 1048576 bytes
[-----------------C]
Writing 1048576 bytes to flash
[-----------------C]
Verifying 1048576 bytes
[-------c o o o o]
{{< /term >}}

The ```flash test``` command erases the chip, writes dummy data, and verifies the write. This is a way to test a chip.



