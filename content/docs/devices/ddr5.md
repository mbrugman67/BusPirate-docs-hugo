+++
weight = 40910
title = 'DDR5 SDRAM module'
+++  

<!--![](/images/docs/demo/24c02-adapter.jpg)-->



- DDR5 SDRAM modules are the memory sticks used in computers and laptops. 
- SPD, or Serial Presence Detect, is a small EEPROM chip on the module that stores information about the memory, such as its size, speed, and timings.
- From SODIMMs to DDR1-DDR5 modules have had SPD chips

![](/images/docs/demo/ddr5-datasheet-front-view.png)

- DDR5 is a major evolution of memory module design. While previous RAM modules had a simple EEPROM, DDR5 has a "SPD hub" chip that contains EEPROM memory but also temperature monitoring/alarms. The SPD hub in turn configures the PMIC (Power Management IC) that generates the voltages used to supply the memory ships. DDR5 ram ragulates its own voltages from a 5 volt supply, giving more granuality and control over the memory power supply. 

## Connections

![](/images/docs/demo/ddr5-connection.png)

|Bus Pirate|DDR5 UDIMM (288 pins)|DDR5 SODIMM (262 pins)|Description|   
|-|-|-|-|
|SDA (IO0)|HSDA (5)|HSDA (6)|I2C Data (3.3volt)|
|SCL (IO1)|HSCL (4)|HSCL (4)|I2C Clock (3.3volt)|
|--|PWR_EN(151)|PWR_EN (8)|Power Enable, connect to 3.3 volts|
|--|HSA (148)|HSA (2)|Host Sideband Address, connect to ground for address 0|
|--|BULK_VIN (1)|BULK_VIN (1)|Bulk Voltage Input, connect to 5 volts|
|GND|GND (150)|GND(9)|Ground|
|--|PWR_GOOD (147)|PWR_GOOD (7)|Power Good, optional (low for error)|

- Which pins
-table for UDIMM SODIMM
- not all power or supply need to be connected

**HSDA** and **HSCL** are the I2C bus pins. **PWR_EN** enables the DDR5 module power supply when connected to 3.3 volts.

Motherboards can accept multiple DDR5 modules, so each module needs a unique I2C address. A pull-down resistor connected to the HSA pin sets the last four bits of the base I2C address (0x50). When **HSA** is connected to ground the module goes into a special service mode that allows us to override write protected portions of the EEPROM. 

**BULK_VIN** is the single 5 volt power supply for the SDP hub and PMIC, which generates a precision ~1.1 volt supply for the DDR memory chips. There are multiple BULK_VIN and **GND** pins on the module, but only one if each needs to be connected to access the SPD hub.

**PWR_GOOD** is an open drain output signal from the PMIC. If the power is stable this pin will float, but if the supply is interrupted it will pull low. This might be useful for diagnosing a faulty DDR5 module power supply.

{{% alert context="danger" %}}
The DDR5 HSDA and HSCL pins **must** be no more than 3.3 volts, but the DDR5 module is powered by 5 volts! 
- Run Bus Pirate at 3.3 volts and power BULK_VIN with an external 5 volt supply.
- Run the Bus Pirate IO at 5 volts and use a 3.3 volt level shifter to connect the HSDA and HSCL pins.
{{% /alert %}}

## DDR5 adapter board

{{% readfile "/_common/_footer/_footer-cart.md" %}}

It's possible to gently solder wires on to each pad of the chip, but a KF-011C (or similar) smart card socket is useful if you don't want to destroy the card.

{{% alert context="info" %}}
A [smart IC card and SIM card adapter]({{< relref "/docs/overview/sim-iccard-adapter" >}}) is available for Bus Pirate 5 with the correct connections already set. The adapter accepts most ISO 7816-3 smart cards and mini/micro/nano SIM cards. 
{{% /alert %}} 


## See it in action

{{< asciicast src="/screencast/ddr5-cast.json" poster="npt:0:22"  idleTimeLimit=2 >}}

## Setup

{{< termfile source="static/snippets/24c02-setup.html" >}}

24C02 IC cards use the common and friendly [I2C interface]({{< relref "/docs/command-reference/#i2c" >}}). Speeds under 100kHz should work with most cards, though speed demons might try up to 400kHz.

- ```m i2c``` - change to [**I2C**]({{< relref "/docs/command-reference/#i2c" >}}) [mode]({{< relref "/docs/command-reference/#m-set-bus-mode" >}}).
- ```100``` - configure I2C for **100kHz**.
- ```1``` - disable clock stretching.

{{% alert context="info" %}}
Original I2C EEPROM cards were slow and highly limited by early EEPROM technology. The new cards available today generally use more modern EEPROM devices, but there's no way to know exactly what modern features it may have unless the manufacturer provides a datasheet. Even a datasheet is no guarantee that the chip used in the card will match.
{{% /alert %}}

### Power supply

{{< termfile source="static/snippets/24c02-power.html" >}}

This is old tech - it needs a 5 volt power supply.

- ```W 5``` - enable the [onboard power supply]({{< relref "/docs/command-reference/#ww-power-supply-offon" >}}) at 5 volts.

### Pull-up resistors
{{< termfile source="static/snippets/24c02-pullup.html" >}}

I2C is an open collector output bus, the Bus Pirate and the 24C02 can only pull the line low to 0 (ground). A pull-up resistor is needed to pull the line high to 1 (5 volts). The Bus Pirate has built-in pull-up resistors that can be enabled with the ```P``` command.
- ```P``` - Enable the [onboard pull-up resistors]({{< relref "/docs/command-reference/#pp-pull-up-resistors">}}).

{{% alert context="warning" %}} 
Be sure to enable the pull-up resistors. The data line will never go high without them and you'll read only 0s.
{{% /alert %}}

## I2C address scan

![](/images/docs/demo/ddr5-datasheet-address.png)

{{< termfile source="static/snippets/24c02-scan.html" >}}

Let's see if we can find the card I2C address. We could look in the datasheet, or we can be lazy and run an I2C [address scan]({{< relref "/docs/command-reference/#scan-i2c-address-search">}}).
- ```scan``` - Scan the I2C bus for devices

The scanner found an I2C device at address 0x50 (0xA0 write, 0xA1 read). That's the 24C02 EEPROM.

{{% alert context="info" %}} 
If the scanner doesn't find the device, ensure the power supply is enabled ```W 5``` and the pull-up resistors are enabled ```P```. Also check that slide switches SW1 and SW2 select VOUT and GND respectively.
{{% /alert %}}



## SPD Hub Memory Areas

![](/images/docs/demo/ddr5-datasheet-readcmd.png)

The SPD hub has two different memory areas:
- **Registers** - 128 bytes of registers that control the SPD hub and store things like the current temperature sensor reading.
- **Non-Volatile Memory** - 1024 byte EEPROM that stores JEDEC 5118 standard SPD data such as the memory size, speed, and timings.

Accessing the SPD hub follows the common I2C pattern of setting the address pointer, then reading or writing data. **Here's the trick**: the MemReg bit (bit 7) of the register address determines which memory area to access. 
- If MemReg is 0, the registers are accessed
- If MemReg is 1, the non-volatile memory is accessed


## SPD Hub Registers
![](/images/docs/demo/ddr5-datasheet-regmap.png)

Let's look a the registers first. We can read out all 128 bytes with a single I2C transaction. 

{{< termfile source="static/snippets/.html" >}}

We'll start reading at address 0, with MemReg set to 0 to access the registers. The write and read command **must** be separated by an I2C repeated start, the address pointer will reset to 0 after any STOP bit.

- ```[``` - I2C START bit
- ```0xa0``` - I2C address and write bit
- ```0b00000000``` - Register address pointer, MemReg = 0, address 0, 
- ```[``` - I2C Repeated START bit
- ```0xa1``` - I2C address and read bit
- ```r:128``` - Read 128 bytes
- ```]``` - I2C STOP bit

Let's break it down and look at a few of the interesting registers.

### Device Type

![](/images/docs/demo/ddr5-datasheet-mr0102.png) 

Register 0 and 1 contain the device type, 0x5118 for SPD5 hub with temperature sensor. The designers were being cute - 5118 is the JEDEC standard number for DDR5 SPD hubs.

{{< termfile source="static/snippets/ddr5-mr01.html" >}}
- ```[ 0xa0 0x00 [ 0xa1 r:2 ]``` - Read the first two registers.

### Temperature Sensor

Hold on! Reading the temperature is quite the ride.
1. Read the temperature sensor resolution from register 36 (0x24).
2. Read the temperature from register 49 and 50 (0x31, 0x32).
3. Shift some bits around.
4. Multiply by the resolution multiplier.

#### Temperature Sensor Resolution
![](/images/docs/demo/ddr5-datasheet-mr36.png)

First we need to know the currently configured temperature sensor resolution. This is stored in register 36 (0x24). 

{{< termfile source="static/snippets/ddr5-mr24.html" >}}

- ```[ 0xa0 0x24 [ 0xa1 r:1 ]``` - Read the temperature sensor resolution from register 36 (0x24).

Register 36 is currently 0x00, so each bit of the temperature reading is 0.5 degrees Celsius.

{{% alert context="info" %}}
Use the [```=``` convert format command]({{< relref "/docs/command-reference/#x-convert-to-hexdecbin-number-format">}}) to convert between number formats.
- ```= 0x01``` = 0b01 (10-bit resolution, 0.25 celsius per bit)
- ```= 0x02``` = 0b10 (11-bit resolution, 0.125 celsius per bit)
- ```= 0x03``` = 0b11 (12-bit resolution, 0.0625 celsius per bit)
{{% /alert %}}

#### Change Temperature Sensor Resolution
{{% alert context="warning" %}}
Is your default resolution something other than 9 bits? Let's change it to 9 bits so it matches this demo.
{{% /alert %}}


{{< termfile source="static/snippets/ddr5-mr24-write.html" >}}
Write 0b00 to register 36 (0x24) to set the temperature sensor resolution to 9 bits (0.5 degrees Celsius per bit).
- ```[ 0xa0 0x24 0b00]``` - Write the temperature sensor resolution to register 36 (0x24).

You can repeat the [previous step]({{< relref "/docs/devices/ddr5/#temperature-sensor-resolution">}}) to verify the register is configured for 9 bits temperature sensing. 

#### Read Temperature
![](/images/docs/demo/ddr5-datasheet-mr4950.png)

Registers 49 and 50 (0x31, 0x32) contain the current temperature sensor measurement.

{{< termfile source="static/snippets/ddr5-mr4950.html" >}}

- ```[ 0xa0 0x31 [ 0xa1 r:2 ]``` - Read the temperature from registers 49 and 50 (0x31, 0x32).

The raw temperature sensor reading is 0x54 0x01. Now we need to shift the bits around and multiply by the resolution multiplier to get the actual temperature in degrees Celsius.

#### Calculate Temperature
![](/images/docs/demo/ddr5-datasheet-9bit-temp.png)

A 9 bit sensor measurement is packed into the two register bytes as shown in the table. 

Let's start with the low byte: 0x54 = 0b0101'0100.
- 0b```0101'0```000 - Bits 7 to 3 are the low bits of the temperature measurement.
- 0b0101'0```000``` - Bits 2 to 0 are discarded

The lower bits of the temperature are 0b01010. Now let's do the high byte: 0x01 = 0b0000'0001.
- 0b```000```0'0001 - Bits 7 to 5 are discarded.
- 0b000```0```'0001 - Bit 4 is the sign bit, 0 for positive, 1 for negative.
- 0b0000'```0001``` - Bits 3 to 0 are the high bits of the temperature measurement.

Put it all together:
- 0b```0'001```0'1010 - The four bits from the high byte.
- 0b0'001```0'1010``` - The five bits from the low byte.

Converting from binary to decimal gives us 0b0'0010'1010 = 42. Multiply by the resolution multiplier of 0.5 degrees Celsius per bit to get 21 degrees Celsius. The sign bit is 0, so the temperature is a positive value. 

### EEPROM Block Protection Bits
{{% alert context="info" %}}
The next three sections are SPD registers that control how the EEPROM/Non-Volatile Memory is configured. 
{{% /alert %}}

![](/images/docs/demo/ddr5-datasheet-mr1213.png)

The SPD EEPROM is made up of 16 block of 64 bytes each. Each block can be protected by setting the corresponding bit in register 12 and 13 from 0 to 1.

{{< termfile source="static/snippets/ddr5-mr1213.html" >}}

Read register 12 and 13 (0x0C, 0x0D) to see the current block protection configuration.
- ```[ 0xa0 0x0c [ 0xa1 r:2 ]``` - Read the block protection bits from registers 12 and 13 (0x0C, 0x0D).

The JEDEC standard directs that manufacturers protect blocks 0 to 9, though some don't lock 8 and 9. 

- 0x03 0xFF = 0b0000'0011'1111'1111, so blocks 0 to 9 are protected.

To write protect additional blocks, set the corresponding bit in register 12 and 13 to 1. For example write 0xFF 0xFF to write protect all blocks: 

- ```[0xa0 0x0c 0xff 0xff]``` - Write protect all blocks.

It is always possible to protect new blocks, but **write protection cannot be disabled (change 1 to 0) unless the module is in offline mode, with the HSA pin connected to ground**. 

{{% alert context="warning" %}}
Write protection cannot be disabled unless the module is in offline mode, with the HSA pin connected to ground.
{{% /alert %}}

### Device Status Register
![](/images/docs/demo/ddr5-datasheet-mr48-short.png)

The Device Status register (48, 0x30) has two especially useful bits. 

{{< termfile source="static/snippets/ddr5-mr1213.html" >}}

- ```[0xa0 0x30 [ 0xa1 r:1 ]``` - Read the device status register from register 48 (0x30).

Device status is 0x04 = 0b0000'0100. Let's decipher the bits with the datasheet.

![](/images/docs/demo/ddr5-datasheet-mr48.png)

Bit 2 is set to 1, indicating the module is in **offline mode**. This means the HSA pin is connected to ground and we can remove write protection from the EEPROM blocks. 

Bit 3 is set to 0, indicating that there is no write operation in progress. Writing to the EEPROM **and** updating the block protection registers take time, so the SPD hub sets this bit to 1 while a write is in progress.

### Legacy Mode and Page Setting

![](/images/docs/demo/ddr5-datasheet-mr11.png)

Our final stop on the tour of registers is the Legacy Mode Device Configuration register (11, 0x0B). Bit 3 controls how we select where in the EEPROM to read and write when the [MemReg bit]({{< relref "/docs/devices/ddr5/#spd-hub-memory-areas">}}) is high.

![](/images/docs/demo/ddr5-datasheet-1byteadd.png)

The EEPROM is divided into 8 pages of 128 bytes. In **Legacy Mode** (register 11 bit 3 = 0) when MemReg bit is 1 in the byte following the write address, the lower seven bits select byte 0-127 in the EEPROM page (Blk_Addr[0] + Address[5:0]). Bits 2:0 in the Legacy Mode Device Configuration register select page 0-7. 

Two transaction are needed to change between pages. 
1. A write to the Legacy Mode Device Configuration register to set the page. 
2. A write to the EEPROM with the MemReg bit set to 1 and the lower 7 bits set to the byte address within the page. 

![](/images/docs/demo/ddr5-datasheet-2byteadd.png)

The EEPROM is divided into 8 pages of 128 bytes. In **2 Byte Addressing mode** (register 11 bit 3 = 1) when the MemReg bit is 1 in the byte following the write address, the lower seven bits select bytes 0-127 in the EEPROM  (Blk_Addr[0] + Address[5:0]). A second address byte selects page 0-7 (Blk_Addr[4:1]).

{{% alert context="warning" %}}
Non-Legacy Mode is easier to use because the page is selected with a second address byte. **However**, if the Legacy Mode configuration is wrong the second byte can be interpreted as data and will be accidentally written to the EEPROM. We're going to stick with legacy mode for the added safety.
{{% /alert %}}

{{% alert context="info" %}}
This description is only partly accurate. Technically when MemReg is 1 bit 6 is the first bit of the "block address" bits (Blk_Addr[0]), corresponding to the 16 write protect blocks of 64 bytes each. Functionally it can be treated as 7th address bit. This datasheet treats it both ways without actually addressing the inconsistency.
{{% /alert %}}


{{< termfile source="static/snippets/ddr5-mr11.html" >}}

Legacy Mode addressing should be enabled by default, but let's configure and verify it anyway.

- ```[0xa0 0x0b 0b00000000]``` - Set the Legacy Mode Device Configuration register to 0, enabling legacy mode and setting the page to 0.
- ```[0xa0 0x0b [ 0xa1 r:1 ]``` - Read the Legacy Mode Device Configuration register to verify it was set correctly.

Now we have the tools to read and write the SPD hub non-volatile memory. 

## Read SPD Hub Non-Volatile Memory

We've been through the swap of registers, now let's see the show: the DDR5 SRAM settings stored in the SPD hub non-volatile memory. The content is defined by JEDEC standard [JESD400-5C](https://www.jedec.org/document_search?search_api_views_fulltext=JESD400-5C), free to download but registration required.

{{% alert context="info" %}}
Normally we like to provide screenshots of actual datasheets to explain how devices work, but JEDEC is techy about sharing and watermarks each PDF. We'll present a few simplified tables here instead of the normal screenshots.
{{% /alert %}}

### Memory Organization
| Block | Range      | Address Range   | Description                                      |
|-------|------------|----------------|--------------------------------------------------|
| 0-1   | 0-127      | 0x000-0x07F    | Basic Information           |
| 2     | 128-191    | 0x080-0x0BF    | Reserved                              |
| 3-6  | 192-447    | 0x0C0-0x1BF    | Module Parameters         |
| 7     | 448-509    | 0x1C0-0x1FD    | Reserved                              |
| 7     | 510-511    | 0x1FE-0x1FF    | CRC for bytes 0-509                              |
| 8-9   | 512-639    | 0x200-0x27F    | Manufacturer Information                        |
| 10-15 | 640-1023    | 0x280-0x2FF    | End User Programmable                            |

This is a simplified table of the SPD hub non-volatile memory organization. 

### Read Key Bytes

{{< termfile source="static/snippets/ddr5-read-key.html" >}}

The first four bytes are key to identifying a DDR5 module. First we need to set the Legacy Page address to 0, then the location to read inside page 0 with the MemReg bit set to 1. 
- ```[0xa0 0x0b 0x00]``` - Set Legacy Mode page pointer to page 0.
- ```[0xa0 0b10000000 [ 0xa1 r:4 ]``` - Read the first four bytes of the non-volatile memory, note the MemReg bit is set to 1.

**Byte 2 (0x12) is the protocol type**, which is always 0x12 for DDR5 modules. This indicates the module uses the DDR5 protocol.

**Byte 3 (0x02 = 0b0000'```0010```) is the module type**. The lower four bits indicate the type of module, 0b0010 is UDIMM and 0b0011 is SODIMM. There's a large list of module types in JEDEC JESD400-5C, so be sure to check there if you're working with something exotic.

|Bits 3:0|Type|
|-|-|
|0010|UDIMM|
|0011|SODIMM|

The upper four bits are used to indicate hybrid module types, which we won't cover here.

**Byte 0 bits 4 to 6 (0x30 = 0b0```011```'000) encode the EEPROM size**. This should be 011 for DDR5 SDP5112, 1024 bytes total.

**Byte 1 (0x10 = 0b0001'0000) encode the SPD revision**. The high four bits are the major revision, the low four bits are the minor revision. 0x10 is revision 1.0.

{{% alert context="info" %}}
After the key bytes there is information about the SDRAM chips on the module: capacity, organization, speed, timings, etc. See the [JEDEC JESD400-5C](https://www.jedec.org/document_search?search_api_views_fulltext=JESD400-5C) standard for all the juicy details.
{{% /alert %}}

### Read Manufacturer Info

| Byte Number | Address   | Description                        | 
|-------------|-----------|---------------------------------------------|
| 512-513     | 0x200-0x201| Module Manufacturer JEDEC ID  |
| 515-516     | 0x203-0x204 | Module Manufacturing Date                 | 
| 517-520     | 0x205-0x208 | Module Serial Number                      | 
| 521-550     | 0x209-0x226 | Module Part Number                        | 
| 552-553     | 0x228-0x229 | DRAM Manufacturer ID     | 
| 555-637     | 0x22B-0x27D | Manufacturer Specific Data       |

This is a simplified table of the manufacturer information stored in the SPD hub non-volatile memory. Only the most interesting fields are shown here. 

{{% alert context="info" %}}
The manufacturer information is stored in block 8 and 9, equivalent to page 4. 
{{% /alert %}}

#### Module Manufacturer JEDEC ID
{{< termfile source="static/snippets/ddr5-read-manufacturer.html" >}}

First we need to set the Legacy Page address to 4, then we can read the manufacturer JEDEC ID from the non-volatile memory.
- ```[0xa0 0x0b 0x04]``` - Set Legacy Mode page pointer to page 4.
- ```[0xa0 0b10000000 [ 0xa1 r:2 ]``` - Read the module manufacturer JEDEC ID at the beginning of the page.

0x859B is the JEDEC ID for Crucial Technology. JEDEC maintains a list, but it's easier to find it with a web search. 

#### Module Manufacture Date
{{< termfile source="static/snippets/ddr5-read-manufacturer.html" >}}
Read the module manufacturing date from registers 515 and 516 (0x203, 0x204). The date is encoded as a year and week number.
- ```[0xa0 0x0b 0x04]``` - Set Legacy Mode page pointer to page 4.
- ```[0xa0 0x83 [ 0xa1 r:2 ]``` - Read the module manufacturing date.

0x22 is the year, 0x04 is the week number. This module was manufactured in the 4th week of 2022.

{{% alert context="info" %}}
At this stage we'll stop writing the MemReg and address values in binary, and instead use hexadecimal. 0b10000000 = 0x80
{{% /alert %}}

#### Module Serial Number
{{< termfile source="static/snippets/ddr5-read-manufacturer.html" >}}
Read the module serial number from registers 517 to 520 (0x205 to 0x208). The serial number is a 32-bit value.
- ```[0xa0 0x0b 0x04]``` - Set Legacy Mode page pointer to page 4.
- ```[0xa0 0x85 [ 0xa1 r:4 ]``` - Read the module serial number.

0xE6FFB785 is the serial number, and it matches the serial printed on the module under the QR code.

#### Module Part Number
{{< termfile source="static/snippets/ddr5-read-manufacturer.html" >}}


{{% alert context="warning" %}}
The part number is a string of ASCII characters, so we'll change the Bus Pirate [output format]({{< relref "/docs/command-reference/#o-data-output-display-format">}}) to ASCII (type ```o```, choose ASCII).
{{% /alert %}}

The part number is an 30 character ASCII text string starting at register 521 (0x209). 
- ```[0xa0 0x0b 0x04]``` - Set Legacy Mode page pointer to page 4.
- ```[0xa0 0x89 [ 0xa1 r:30 ]``` - Read the module part number.

The part number string is "CT8G48C40U5.M4A1".

{{% alert context="warning" %}}
Change the Bus Pirate [output format]({{< relref "/docs/command-reference/#o-data-output-display-format">}}) back to AUTO before continuing (type ```o```, choose AUTO).
{{% /alert %}}

#### DRAM Manufacturer JEDEC ID
{{< termfile source="static/snippets/ddr5-read-manufacturer.html" >}}

There is a second JEDEC ID specifically to encode the DRAM chip manufacturer. We can grab this from registers 552 and 553 (0x228, 0x229).
- ```[0xa0 0x0b 0x04]``` - Set Legacy Mode page pointer to page 4.
- ```[0xa0 0xa8 [ 0xa1 r:2 ]``` - Read the DRAM manufacturer JEDEC ID.

0x802C is the JEDEC ID for Micron Technology. Again, easiest to find with a web search.

#### Manufacturer Specific Data
{{< termfile source="static/snippets/ddr5-read-manufacturer.html" >}}
The last section is manufacturer specific data. This is a free area that can be used for anything the manufacturer wants, so it varies widely between manufacturers. It may contain additional overclocking profiles in EXPO (AMD) or XMP (Intel) format, it may also contain special keys that unscrupulous manufacturers use to lock a system to their specific brand of RAM module.
- ```[0xa0 0x0b 0x04]``` - Set Legacy Mode page pointer to page 4.
- ```[0xa0 0xab [ 0xa1 r:85 ]``` - Read the manufacturer specific data from registers 555 to 637 (0x22B to 0x27D).

This module has a bit of extra data, but nothing special. It looks like it could be a short ASCII string "4510904819".

## Write SPD Hub Non-Volatile Memory

{{% alert context="danger" %}}
**Writing to the SPD hub non-volatile memory is dangerous!**
- It can make the module unbootable.
- It can make the module unusable.

Before writing to the SPD hub non-volatile memory, make sure you have a [backup of the original data]({{< relref "/docs/devices/ddr5/#ddr5-command">}}). Better yet, only experiment with a module you don't care about.
{{% /alert %}}

We're going to write a 16 byte page in the End User Programmable area of the SPD hub non-volatile memory, block 15. Despite the name, manufacturers do use this area to store overclocking profiles and other data. **It is NOT safe to write in this area**.

### Unlock NVM Block Protection

{{< termfile source="static/snippets/ddr5-unlock-nvm.html" >}}
According to the JEDEC standard, the End User Programmable area is not write protected by default. Let's update the [EEPROM Block Protection Bits]({{< relref "/docs/devices/ddr5/#eeprom-block-protection-bits">}}) to make sure block 14 & 15 are not write protected.

- ```[0xa0 0x0c 0xff 0x3f]``` - Write protect all blocks except block 14 & 15.

Writing 0xff (0b1111'1111) to register 12 (0x0C) write protects block 7-0. The next byte 0x7f (0b0011'1111) programs register 13 to protect blocks 8-13, while leaving blocks 14 & 15 unprotected. 

#### Poll For Write Operation to Complete

{{< termfile source="static/snippets/ddr5-unlock-nvm.html" >}}

Block protection is a persistent non-volatile setting that sticks even after power off. The SPD hub will take a few milliseconds to write the new block protection settings. We need to check in on our friend from earlier, the [Device Status Register]({{< relref "/docs/devices/ddr5/#device-status-register">}}), to see when the write is complete.
- ```[0xa0 0x30 [ 0xa1 r:1 ]``` - Read the device status register to check if the write operation is complete.

Bit 3 is set to 0 (0x04 = 0b0000'```0```100), indicating the write operation is complete. The block protection bits are now set to protect all blocks except block 15.

{{% alert context="info" %}}
Since we're typing these commands manually, the write opertion is complete by the time we read the device status register. If you were writing a script or program to automate this, you would need to poll the device status register until bit 3 is 0.
{{% /alert %}}

##### Verify Write Protection Bits

{{< termfile source="static/snippets/ddr5-unlock-nvm.html" >}}

Let's verify the block protection bits are set correctly. We can read registers 12 and 13 (0x0C, 0x0D) to check the current block protection configuration.
- ```[0xa0 0x0c [ 0xa1 r:2 ]``` - Read the block protection bits from registers 12 and 13 (0x0C, 0x0D).

Block protection bits are now 0xFF 0x7F, the update was successful.

{{% alert context="warning" %}}
If the Write Protection Bits are not correct, ensure that the module is in **offline mode** (HSA pin connected to ground) and check the Write Protect Override Status in the [Device Status Register]({{< relref "/docs/devices/ddr5/#eeprom-block-protection-bits">}}). 
{{% /alert %}}

### Read 16 Bytes

{{% alert context="danger" %}}
**Writing to the SPD hub non-volatile memory is dangerous!**

Before writing to the SPD hub non-volatile memory, make sure you have a [backup of the original data]({{< relref "/docs/devices/ddr5/#ddr5-command">}}). Better yet, only experiment with a module you don't care about.

In this step we will read 16 bytes **before** writing to verify it is empty. If you see anything other then 0x00s then **ABSOLUTLY DO NOT WRITE TO THAT LOCATION**. It is likely that area is already programmed with some data, and writing to it will make the module unbootable or unusable.
{{% /alert %}}

{{< termfile source="static/snippets/ddr5-read-nvm.html" >}}

First let's read the target block to make sure it is empty. We'll read the 16 bytes starting from byte 0 of block 14 (page 7).
- ```[0xa0 0x0b 0x07]``` - Set Legacy Mode page pointer to page 7 (block 14 & 15).
- ```[0xa0 0b10000000 [ 0xa1 r:16 ]``` - Read the 16 bytes from the non-volatile memory.

Every byte should be 0x00 if the bytes are empty.

{{% alert context="danger" %}}
If you see anything other than 0x00s, then **ABSOLUTELY DO NOT WRITE TO THAT LOCATION**. It is likely that area is already programmed with some data, and writing to it will make the module unbootable or unusable.
{{% /alert %}}

### Write 16 Byte Page

{{< termfile source="static/snippets/ddr5-write-nvm.html" >}}

The EEPROM is written 16 bytes at a time. Each write page must also be aligned to a 16 byte boundary, so the address of the first byte of the write page must be 0, 16, 32, etc. We'll write 16 bytes of data to the non-volatile memory beginning at byte 0 of block 14.
- ```[0xa0 0x0b 0x07]``` - Set Legacy Mode page pointer to page 7 (block 14 & 15).
- ```[0xa0 0b10000000 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]```

{{% alert context="info" %}}
Again, if you were writing a script or program to automate this, you would need to poll the [Device Status Register]({{< relref "/docs/devices/ddr5/#device-status-register">}}) until bit 3 is 0 to ensure the write operation is complete. We're moving slow enough that the write is complete by the next step.
{{% /alert %}}

### Verify 16 Byte Page

{{< termfile source="static/snippets/ddr5-verify-nvm.html" >}}  

Finally! let's read back the 16 byte page we just wrote to verify it was written correctly.
- ```[0xa0 0x0b 0x07]``` - Set Legacy Mode page pointer to page 7 (block 14 & 15).
- ```[0xa0 0b10000000 [ 0xa1 r:16 ]``` - Read the 16 byte page from the non-volatile memory.

The read data should match the data we wrote: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15.

## ```ddr5``` Command
{{< termfile source="static/snippets/ddr5-command.html" >}}

All of this and more is automated by the ```ddr5``` command. It can read, write, verify, dump, lock and unlock the SPD hub non-volatile memory, decode the registers and even read the temperature sensor. 

## Get a Bus Pirate


{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community


{{% readfile "/_common/_footer/_footer-community.md" %}}
