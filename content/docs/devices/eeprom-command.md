+++
weight = 40999
title = 'Identify Serial EEPROM, Flash and FRAM chips'
katex = true
+++

{{% alert context="info" %}}
This is a placeholder for documentation in progress. 
{{% /alert %}}

## Types of Serial EEPROMs supported

|Type|Part Number*|Ex. Part Num.|Example Manufacturers|
|-|-|-|-|
|SPI Flash|25Qnnn|W25Q128|Winbond, Micron, GigaDevice, PUYA|
|SPI EEPROM|25xnnn, 95xnnn|25LC040|Microchip, Atmel, STMicroelectronics|
|I2C EEPROM|24xnnn|24LC20|Microchip, Atmel, STMicroelectronics|   
|Microwire EEPROM|93xnn|AT93C46|Microchip, Atmel, STMicroelectronics|
|1-Wire EEPROM|243n|DS2341, GX2341|Dallas/Maxim, GX|
|SPI FRAM|FM25xnnn, MB85Xnnn|FM25CL64B, MB85RS512|Ramxeed (Fujitsu), Infineon, ROHM |
|I2C FRAM|FM24xnnn, MB85Xnnn|FM24CL64B, MB85RC64|Ramxeed (Fujitsu), Infineon, ROHM |

*n = device size in Kbits, usually.

## SPI Flash Chips

SPI Flash chips use NOR memory, which is cheap, fast, and small. There are several trade offs though:
1. They are not byte-addressable, data must be read in whole pages (usually 256 bytes) at a time, even if you only want the last byte or two.
2. Whole sectors of 4K, 8K or 64K must be erased at once. 

To update existing data, you must first read all the data in the erase sector, modify it in RAM, erase the whole 4K sector, and then write it back to the flash memory. 

- Write cycles: 100,000-1,000,000
- Data retention: 10-25 years

### Identifying SPI Flash chips
A really common SPI Flash chip is the Winbond W25Qnnn series. 
- Labeled with the Winbond logo
- W25Qnnn part number. 

The "nnn" part of the name indicates the size of the chip in Mbits, so W25Q128 is a 128Mbit chip (16 Mbytes).

Most recent SPI flash chips have their characteristics stored in JEDEC standard **SFDP** (Serial Flash Discoverable Parameters) format. The ```flash``` command in SPI mode will automatically read the SFDP data and display the chip characteristics, including the manufacturer, size, erase sector size, and other parameters.

If SFDP data isn't available, the ```flash``` command has a database of known chips and can identify them by their JEDEC ID.

### Working with SPI Flash chips
The ```flash``` command in SPI mode can probe, read, write, erase, verify and test most SPI flash chips. 

## SPI EEPROM Chips
Unlike Flash (NOR) memory, EEPROM memory is byte-addressable and can be written to one byte at a time. 
- **Size**: 128 bytes to 4 Mbit (512 Kbytes)
- **Read**: Byte addressable, can read any byte in the chip.
- **Write**: 1 byte up to the page size (8 to 256 bytes, depending on chip) at a time.
- **Erase**: No separate erase process is needed, bytes are erased individually before writing.
- **Cost**: EEPROM is generally more expensive than NOR Flash memory.
- **Write cycles**: 1,000,000+
- **Data retention**: 100-200 years

### Identifying SPI EEPROM chips
SPI EEPROM chips are usually labeled with a part number starting with "25" or "95". The "25" series is more common and includes chips like AT25C020, 25LC040, 25AA080, etc. The "95" series is STM's name for their 25x compatible EEPROMs, just substitute the same sized 25x part, e.g. 25LC040 is equivalent to 95LC040.

| Device                      | Density   | Size (bytes)| Page Size (Bytes) |Address Bytes| Block Select Bits |B.S. Offset|
|-----------------------------------|-----------|------------|------|-------------------|----------|-------|
| [25X010](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA010A-25LC010A-1-Kbit-SPI-Bus-Serial-EEPROM-20001832J.pdf)| 1 Kbit    | 128        | 8(AT)/16              | 1  |0|
| [25X020](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA020A-25LC020A-2-Kbit-SPI-Bus-Serial-EEPROM-20001833H.pdf)| 2 Kbit    | 256 | 8(AT)/16 | 1 |0|
| [25X040](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA040A-25LC040A4-Kbit-SPI-Bus-Serial-EEPROM-20001827J.pdf) | 4 Kbit    | 512        | 8(AT)/16              | 1         |1|3|
| [25X080](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/8-Kbit-SPI-Bus-Serial-EEPROM-20002151C.pdf) | 8 Kbit    | 1024   | 16/32(AT,STM)   | 2   |0|
|[25X160](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA160CD-25LC160CD-16-Kbit-SPI-Bus-Serial-EEPROM-20002150C.pdf)| 16 Kbit   | 2048        | 16/32(AT,STM)   | 2   |0|
|[25X320](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA320A-25LC320A-32K-SPI-Bus-Serial-EEPROM-20001828H.pdf)| 32 Kbit   | 4096 | 32   | 2  | 0|
|[25X640](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA640A-25LC640A-64K-SPI-Bus-Serial-EEPROM-20001830G.pdf)  | 64 Kbit   | 8192        | 32                | 2          |0|
|[25X128](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25AA128-25LC128-128K-SPI-Bus-Serial-EEPROM-20001831G.pdf)           | 128 Kbit  | 16384         | 64                | 2             |0|
|[25X256](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LCXXXX-8K-256K-SPI-Serial-EEPROM-High-Temp-Family-Data-Sheet-DS20002131.pdf)| 256 Kbit  | 32768        | 64                | 2          | 0|
|[25X512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LC512-512-Kbit-SPI-Bus-Serial-EEPROM-Data-Sheet-20002065.pdf) | 512 Kbit  | 65536 | 128 |2| 0 |
| [25XM01](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/AT25M01-SPI-Serial-EEPROM-Data-Sheet-20006226A.pdf), [25X1024](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25LC1024-1-Mbit-SPI-Bus-Serial-EEPROM-20002064E.pdf)| 1 Mbit | 131072  |  256 | 3  | 0  |
| [25XM02](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/AT25M02-SPI-Serial-EEPROM-Data-Sheet-20006230A.pdf)| 2 Mbit    |262144 | 256         | 3       |0            |
| [25XM04](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/25CSM04-4-Mbit-SPI-Serial-EEPROM-with-128-Bit-Serial-Number-and-Enhanced-Write-Protection-20005817D.pdf) | 4 Mbit  |524288| 256/512(STM)  |3       | 0             |

{{% alert context="info" %}}
25x/95x chips have a variety of part numbers, but tend to operate in the same way. Often a manufacturer specific part number indicates a different voltage range or upgraded features. AT25, 25LC, 25AA, 25CS and M95 are all part of same basic 25x family of chips. 
{{% /alert %}}  

### Chip voltage requirements

|25x/95x Family|Minimum Voltage|Maximum Voltage|
|---|---|---|---|
|AT25|1.8V|5.5V|
|25LC|2.5V|5.5V|
|25AA|1.8V|5.5V|
|25CS|1.7V|5.5V|
|M95|2.5V|5.5V|

{{% alert context="info" %}}
3.3 volts is a good voltage to use with most 25x/95x chips, but a few chips may have a lower maximum voltage. Always check the datasheet for the specific chip you are using if possible.
{{% /alert %}}

### Working with SPI EEPROM chips
The [```eeprom``` command]({{< relref "/docs/command-reference/#eeprom-read-write-erase-verify-test-dump-spi-eeproms">}}) in SPI mode can probe, read, write, erase, verify and test most SPI EEPROM chips.

## I2C EEPROM Chips
I2C EEPROM chips are also byte-addressable and can be written to one byte at a time. The I2C bus is much slower than the SPI bus, but the internal EEPROM memory has similar write times.
- Write cycles: 1,000,000+
- Data retention: 10-25 years

### Identifying I2C EEPROM chips
I2C EEPROM chips are usually labeled with a part number starting with "24". The "24" series includes chips like 24LC02, 24LC04, AT2402 etc. The "24" series is the most common I2C EEPROM series.

### Working with I2C EEPROM chips
The ```eeprom``` command in I2C mode can probe, read, write, erase, verify and test most I2C EEPROM chips.

## Microwire EEPROM Chips
Microwire EEPROM chips are ancient technology that persists today. Microwire EEPROMs are also byte-addressable and can be written to one byte at a time. They use a funky version of SPI and have a drastically different pinout.

- Write cycles: 1,000,000+
- Data retention: 10-25 years

### Identifying Microwire EEPROM chips
Microwire EEPROM chips are usually labeled with a part number starting with "93". The "93" series includes chips like 93C46, 93C56, 93C66, etc. The "93" series is the most common Microwire EEPROM series.

### Working with Microwire EEPROM chips
The ```eeprom``` command in SPI mode can probe, read, write, erase, verify and test most Microwire EEPROM chips.

## 1-Wire EEPROM Chips
1-Wire EEPROM chips are a unique type of EEPROM that uses the 1-Wire protocol. They are also byte-addressable but they must be written to one page (8 or 32 bytes) at a time. They 1-Wire is even slower than I2C, but can be useful in low-power applications.

- Write cycles: 1,000,000+
- Data retention: 10-25 years
### Identifying 1-Wire EEPROM chips
1-Wire EEPROM chips are usually labeled with a part number starting with "243". The "243" series includes chips like DS2431, DS2432, GX2341, etc. The "243" series is the most common 1-Wire EEPROM series.
### Working with 1-Wire EEPROM chips
The ```eeprom``` command in 1-Wire mode can probe, read, write, erase, verify and test most 1-Wire EEPROM chips.
## SPI FRAM Chips
SPI FRAM chips are a type of non-volatile memory that uses ferroelectric RAM technology. They are faster than EEPROM and Flash, and can be written to one byte at a time. They have a very high endurance and can be used in applications that require frequent writes.
- Write cycles: 10^15+
- Data retention: 100+ years
### Identifying SPI FRAM chips
SPI FRAM chips are usually labeled with a part number starting with "FM25" or "MB85". The "FM25" series includes chips like FM25CL64B, FM25L04B, etc. The "MB85" series is Infineon's name for their FRAM chips, e.g. MB85RS512.        
### Working with SPI FRAM chips
The ```fram``` command in SPI mode can probe, read, write, erase, verify and test most SPI FRAM chips.
## I2C FRAM Chips
I2C FRAM chips are similar to SPI FRAM chips, but use the I2C protocol. They are also faster than EEPROM and Flash, and can be written to one byte at a time. They have a very high endurance and can be used in applications that require frequent writes.
- Write cycles: 10^15+
- Data retention: 100+ years
### Identifying I2C FRAM chips
I2C FRAM chips are usually labeled with a part number starting with "FM24" or "MB85". The "FM24" series includes chips like FM24CL64B, FM24L04B, etc. The "MB85" series is Infineon's name for their FRAM chips, e.g. MB85RC64.        
### Working with I2C FRAM chips
The ```fram``` command in I2C mode can probe, read, write, erase, verify and test most I2C FRAM chips.





|Device|Size|Bytes|Organization|Dummy bits|Address|Total bits|
|-|-|-|-|-|-|-|
|93x46A|1Kbit|128|x8 only|0|7bits|10|
|93x46B|1Kbit|128|x16 only|0|6bits|9|
|93x46C/E|1Kbit|128|x8 or x16|0|7 or 6bits|10 or 9|
|93x56A|2Kbit|256|x8 only|1|8bits|12|
|93x56B|2Kbit|256|x16 only|1|7bits|11|
|93x56C|2Kbit|256|x8 or x16|1|8 or 7bits|12 or 11|
|93x66A|4Kbit|512|x8 only|0|9bits|12|
|93x66B|4Kbit|512|x16 only|0|8bits|11|
|93x66C|4Kbit|512|x8 or x16||10 or 9bits|12 or 11|
|93x76A|8Kbit|1024|x8 only|1|10bits|14|
|93x76B|8Kbit|1024|x16 only|1|9bits|13|
|93x76-/C|8Kbit|1024|x8 or x16|1|10 or 9bits|14 or 13|
|93x86A|16Kbit|2048|x8 only|0|11bits|14|
|93x86B|16Kbit|2048|x16 only|0|10bits|13|
|93x86-/C|16Kbit|2048|x8 or x16|0|11 or 10bits|14 or 13|

*x8 or x16 bits is selected by the ORG pin. If ORG is low, the device is x8, if ORG is high, the device is x16.*



