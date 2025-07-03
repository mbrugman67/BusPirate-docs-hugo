+++
weight = 40999
title = 'SPI EEPROM Command'
katex = true
+++

{{% alert context="info" %}}
This is a placeholder for documentation in progress. 
{{% /alert %}}

### ```eeprom``` Read, write, erase, verify, test, dump SPI EEPROMs

{{< asciicast src="/screencast/i2c-eeprom-command-cast.json" poster="npt:0:58"  idleTimeLimit=2 >}}

```eeprom``` is a command to read, write, erase, verify, test and dump common 25x SPI EEPROMs. 

{{% alert context="info" %}}
You do need to specify the device type, there is no non-destructive autodetect method for I2C EEPROMs.
{{% /alert %}}


#### SPI EEPROM list supported devices

{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;list
{{< /term>}}

- ```eeprom list``` - list all EEPROM devices supported by the ```eeprom``` command


| Product(s)                       | Density   | Size (bytes)| Page Size (Bytes) |Address Bytes| Block Select Bits |
|-----------------------------------|-----------|------------|------|-------------------|----------|-------|
| [AT25010B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25010B-AT25020B-AT25040B-1-2-4-Kbit-SPI-Serial-EEPROM-Industrial-Grade-DS20006251.pdf)| 1 Kbit    | 128       | 8   | 1|0|
| [25AA/LC010A](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA010A-25LC010A-1-Kbit-SPI-Bus-Serial-EEPROM-20001832J.pdf)| 1 Kbit    | 128        | 16              | 1  |0|
| [AT25020B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25010B-AT25020B-AT25040B-1-2-4-Kbit-SPI-Serial-EEPROM-Industrial-Grade-DS20006251.pdf)| 2 Kbit    | 256   | 8 | 1  |0|
| [25AA/LC020A](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA020A-25LC020A-2-Kbit-SPI-Bus-Serial-EEPROM-20001833H.pdf), [25AA02UID](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/20005205A.pdf) (32 bit ID, 0XC0 locked, location 0xFA-0xFF)), [25AA02E64/48](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/25AA02E48-25AA02E64-2K-SPI-Bus-Serial-EEPROM-DataSheet_DS20002123G.pdf)(64 or 48 bit EUI-x Node Address, 0XC0 locked, location 0xFA-0xFF or 0xF8 to 0xFF)| 2 Kbit    | 256 | 16 | 1 |0|
| [AT25040B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25010B-AT25020B-AT25040B-1-2-4-Kbit-SPI-Serial-EEPROM-Industrial-Grade-DS20006251.pdf)        | 4 Kbit    | 512        | 8     | 1          |opcode 0x02 bit 3|
| [25AA/LC040A](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA040A-25LC040A4-Kbit-SPI-Bus-Serial-EEPROM-20001827J.pdf) | 4 Kbit    | 512        | 16              | 1         |opcode 0x02 bit 3|
| [25AA/LC080C](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LCXXXX-8K-256K-SPI-Serial-EEPROM-High-Temp-Family-Data-Sheet-DS20002131.pdf) | 8 Kbit    | 1024   | 16   | 2   |0|
| [AT25080B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25080B-AT25160B-8-16-Kbit-SPI-Serial-EEPROM-Industrial-Grade-Data-Sheet-DS20006244.pdf), [25AA/LC080D](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/8-Kbit-SPI-Bus-Serial-EEPROM-20002151C.pdf) | 8 Kbit    | 1024        | 32             | 2          |0|
|[25AA/LC160C](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA160CD-25LC160CD-16-Kbit-SPI-Bus-Serial-EEPROM-20002150C.pdf)| 16 Kbit   | 2048        | 16   | 2   |0|
|[AT25160B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25080B-AT25160B-8-16-Kbit-SPI-Serial-EEPROM-Industrial-Grade-Data-Sheet-DS20006244.pdf), [25AA/LC160D](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA160CD-25LC160CD-16-Kbit-SPI-Bus-Serial-EEPROM-20002150C.pdf)| 16Kbit  | 2048        | 32   | 2   | 0|
| [25CS320](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25CS320-32-Kbit-SPI-Serial-EEPROM-DS20006923.pdf) (ECC), [AT25320B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25320B-AT25640B-32-64-Kbit_SPI-Serial_EEPROM-Data-Sheet-DS20005993.pdf), [25AA/LC320A](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA320A-25LC320A-32K-SPI-Bus-Serial-EEPROM-20001828H.pdf)| 32 Kbit   | 4096 | 32   | 2  | 0|
| [25CS640](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25CS640-64-Kbit-SPI-Serial-EEPROM-128-Bit-Serial-Number-Enhanced-Write-Protection-DS20005943.pdf), [AT25640B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25320B-AT25640B-32-64-Kbit_SPI-Serial_EEPROM-Data-Sheet-DS20005993.pdf), [25AA/LC640A](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA640A-25LC640A-64K-SPI-Bus-Serial-EEPROM-20001830G.pdf)  | 64 Kbit   | 8192        | 32                | 2          |0|
| [AT25128B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25128B-AT25256B-128-256-Kbit-SPI-Serial-EEPROM-Industrial-Grade-Data-Sheet-DS20006193.pdf), [25AA/LC128](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA128-25LC128-128K-SPI-Bus-Serial-EEPROM-20001831G.pdf)           | 128 Kbit  | 16384         | 64                | 2             |0|
| [AT25256B](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25128B-AT25256B-128-256-Kbit-SPI-Serial-EEPROM-Industrial-Grade-Data-Sheet-DS20006193.pdf), [25LC256](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LCXXXX-8K-256K-SPI-Serial-EEPROM-High-Temp-Family-Data-Sheet-DS20002131.pdf), [25AA256](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA256-25LC256-256K-SPI-Bus-Serial-EEPROM-20001822J.pdf)| 256 Kbit  | 32768        | 64                | 2          | 0|
| [AT25512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT25512-SPI-Serial-EEPROM-512-Kbits-%2865%2C536x8%29-20006218B.pdf), [25LC512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LC512-512-Kbit-SPI-Bus-Serial-EEPROM-Data-Sheet-20002065.pdf), [25AA512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA512-512-Kbit-SPI-Bus-Serial-EEPROM-Data-Sheet.pdf) | 512 Kbit  | 65536 | 128 |2| 0 |
| [AT25M01](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/AT25M01-SPI-Serial-EEPROM-Data-Sheet-20006226A.pdf), [25LC1024](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LC1024-1-Mbit-SPI-Bus-Serial-EEPROM-20002064E.pdf), [25AA1024](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/1-Mbit-SPI-Bus-Serial-EEPROM-Data-Sheet-20001836K.pdf)| 1 Mbit | 131072  |  256 | 3  | 0  |
| [AT25M02](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/AT25M02-SPI-Serial-EEPROM-Data-Sheet-20006230A.pdf)| 2 Mbit    |262144 | 256         | 3       |0            |
| [25CSM04](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25CSM04-4-Mbit-SPI-Serial-EEPROM-with-128-Bit-Serial-Number-and-Enhanced-Write-Protection-20005817D.pdf) | 4 Mbit  |524288| 256  |3       | 0             |


## Registers

![alt text](/images/docs/eeprom-command/image.png)

## Status Register

![alt text](/images/docs/eeprom-command/image-1.png)

The status register bit 0 indicates a write is in progress, bit 1 indicates if the write enable latch is set (data can be written to the memory or status register).

### Write protection blocks

![alt text](/images/docs/eeprom-command/image-2.png)

Many, but not all, EEPROMs have a write protection block feature. This allows you to protect a portion of the EEPROM from being written to, even if the write enable latch is set. The block select bits are used to select which block is protected: none (0b00), the upper 1/4 (0b01), the upper 1/2 (0b10), or the entire EEPROM (0b11).

![alt text](/images/docs/eeprom-command/image-3.png)

Fewer devices have a WPEN bit that disables the Write Protect (WP) pin. When WPEN is 0, the WP pin is ignored. When WPEN is 1, the WP pin is used to control write protection. If the WP pin is high, the EEPROM is write protected. If the WP pin is low, the EEPROM can be written to.

We can test which bits are available in a chip by writing 0x00 to the status register, then writing 0b10001100, enabling all the protection bits. If the chip supports WPEN or BPx bits, they will be set to 1 after the write. If they are not supported, they will remain 0.

{{% alert context="info" %}}
24x chips have a variety of part numbers, but tend to operate in the same way. Often a manufacturer specific part number indicates a different voltage range or upgraded features. AT24C, 24C, 24LC, 24AA, 24FC are all generally part of same basic 24x family of chips. 
{{% /alert %}}  

##### Chip voltage requirements

|24xx Family|Minimum Voltage|Maximum Voltage|Notes|
|---|---|---|---|
|AT24C|2.7V|5.5V|400kHz max|
|24C|2.7V|5.5V|400kHz max|
|24LC|2.5V|5.5V|400kHz max|
|24AA|1.7V|5.5V|400kHz max|
|24FC|1.8V|5.5V|1MHz max|

Before using the ```eeprom``` command, you'll need to enable a power supply with the [```W``` command]({{< relref "/docs/command-reference/#ww-power-supply-offon">}}) and pull-up resistors with the [```P``` command]({{< relref "/docs/command-reference/#pp-pull-up-resistors">}}).

{{% alert context="danger" %}}
**Most EEPROMs should be fine with a 3.3 volt power supply, but if possible check the datasheet to be sure!**
{{% /alert %}}

#### I2C EEPROM dump to terminal

{{< termfile source="static/snippets/i2c-eeprom-command-dump-partial.html" >}}

Display the contents of an I2C EEPROM in the terminal. 
- ```dump -d <device>``` - display EEPROM contents
- ```dump -d <device> -s <start>``` - display EEPROM contents, starting at address `<start>`
- ```dump -d <device> -s <start> -b <bytes>``` - display a specific range of bytes, starting at address `<start>` and reading `<bytes>` bytes

#### I2C EEPROM read to file
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;read&nbsp;-d&nbsp;24x02&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Read:&nbsp;Reading&nbsp;EEPROM&nbsp;to&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;complete
Read&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Read&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}

Read the contents of an I2C EEPROM and save it to a file.
- ```read -d <device> -f <file>``` - read EEPROM contents to file `<file>`
- ```read -d <device> -f <file> -v``` - read EEPROM contents to file `<file>`, verify the read operation

#### I2C EEPROM write from file
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;write&nbsp;-d&nbsp;24x02&nbsp;-f&nbsp;eeprom.bin&nbsp;-v
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Write:&nbsp;Writing&nbsp;EEPROM&nbsp;from&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}
Write the contents of a file to an I2C EEPROM.
- ```write -d <device> -f <file>``` - write EEPROM from file `<file>`
- ```write -d <device> -f <file> -v``` - write EEPROM from file `<file>`, verify the write operation

#### I2C EEPROM verify against file
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;verify&nbsp;-d&nbsp;24x02&nbsp;-f&nbsp;eeprom.bin
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Verify:&nbsp;Verifying&nbsp;EEPROM&nbsp;contents&nbsp;against&nbsp;file&nbsp;eeprom.bin...
Progress:&nbsp;[###########################]&nbsp;100.00%
Verify&nbsp;complete
Success&nbsp;:)
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}
Verify the contents of an I2C EEPROM match a file.
- ```verify -d <device> -f <file>``` - verify EEPROM contents against file `<file>`

#### I2C EEPROM erase
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;erase&nbsp;-d&nbsp;24x02&nbsp;-v
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase: Writing 0xFF to all bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete
Success&nbsp;:)
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}

Erase the contents of an I2C EEPROM, writing 0xFF to all bytes.
- ```erase -d <device>``` - erase EEPROM contents
- ```erase -d <device> -v``` - erase EEPROM contents, verify the erase operation
#### I2C EEPROM test
{{< term  >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;eeprom&nbsp;test&nbsp;-d&nbsp;24x02
24X02:&nbsp;256&nbsp;bytes,&nbsp;&nbsp;0&nbsp;block&nbsp;select&nbsp;bits,&nbsp;1&nbsp;byte&nbsp;address,&nbsp;8&nbsp;byte&nbsp;pages

Erase:&nbsp;Writing&nbsp;0xFF&nbsp;to&nbsp;all&nbsp;bytes...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;complete
Erase&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Erase&nbsp;verify&nbsp;complete

Test:&nbsp;Writing&nbsp;alternating&nbsp;patterns
Writing&nbsp;0xAA&nbsp;0x55...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Writing&nbsp;0x55&nbsp;0xAA...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;complete
Write&nbsp;verify...
Progress:&nbsp;[###########################]&nbsp;100.00%
Write&nbsp;verify&nbsp;complete
Success&nbsp;:)

<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term>}}
Test I2C EEPROM functionality. Erase the EEPROM to 0xff and verify the erase. Then write alternating patterns of 0xAA and 0x55, verifying each write operation. Any stuck bits should be detected during the test.
- ```test -d <device>``` - test EEPROM functionality

#### I2C EEPROM options and flags
|Option|Description|
|---|---|
|```eeprom list```|List all supported EEPROM devices|
|```eeprom dump```|Dump EEPROM contents to terminal|
|```eeprom read```|Read EEPROM contents to file|
|```eeprom write```|Write EEPROM from file|
|```eeprom verify```|Verify EEPROM contents against file|
|```eeprom erase```|Erase EEPROM contents, writing 0xFF to all bytes|
|```eeprom test```|Test EEPROM functionality, erase and write alternating patterns|

Options tell the ```eeprom``` command what to do.

|Flag|Description|
|---|---|
|```-d <device>```|Specify the EEPROM device type, e.g. 24x02|
|```-f <file>```|Specify the file for read, write and verify|
|```-s <start>```|Specify the start address for dump and read operations|
|```-b <bytes>```|Specify the number of bytes to read for dump operations|
|```-v```|Verify the read or write operation|
|```-a```|Specify an alternate I2C address (0x50 default)|
|```-h```|Show help for the ```eeprom``` command|

