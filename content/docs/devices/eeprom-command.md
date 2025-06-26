+++
weight = 40999
title = 'I2C EEPROM Command'
katex = true
+++

{{% alert context="info" %}}
This is a placeholder for a documentation in progress. 
{{% /alert %}}

|Device|Size|Size (bytes)|Page Size|Address Bytes|Block Select Bits|Block Select Bit Offset|
|---|---|---|---|---|---|---|
|[24xM02](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/AT24CM02-2-Mbit-I2C-Serial-EEPROM-DS20006197.pdf)|256 KB|262144|256|2|2|0|
|[24xM01](https://ww1.microchip.com/downloads/en/DeviceDoc/AT24CM01-I2C-Compatible-Two-Wire-Serial-EEPROM-Data-Sheet-20006170A.pdf)|128 KB|131072|256|2|1|0|
|[24xx1026](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA1026-24FC1026-24LC1026-1024-Kbit-I2C-Serial-EEPROM-DS20002270.pdf)|128 KB|131072|128|2|1|0|   
|[24xx102*5*](https://ww1.microchip.com/downloads/en/devicedoc/21941b.pdf)|128 KB|131072|128|2|1|3|
|[24xx512](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA512-24LC512-24FC512-512-Kbit-I2C-Serial-EEPROM-DS20001754.pdf)|64 KB|65536|128|2|0|0|
|[24xx256](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA256-24LC256-24FC256-256K-I2C-Serial-EEPROM-DS20001203.pdf)|32 KB|32768|64|2|0|0|
|[24xx128](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA128-24LC128-24FC128-128-Kbit-I2C-Serial-EEPROM-DS20001191.pdf)|16 KB|16384|64|2|0|0|
|[24xx64](https://ww1.microchip.com/downloads/aemDocuments/documents/MPD/ProductDocuments/DataSheets/24AA64-24FC64-24LC64-64-Kbit-I2C-Serial-EEPROM-DS20001189.pdf)|8 KB|8192|32|2|0|0|
|[24xx32](https://ww1.microchip.com/downloads/en/DeviceDoc/21072G.pdf)|4 KB|4096|32|2|0|0|
|[24xx16](https://ww1.microchip.com/downloads/en/DeviceDoc/20002213B.pdf)|2 KB|2048|16|1|3|0|
|[24xx08](https://ww1.microchip.com/downloads/en/devicedoc/21710k.pdf)|1 KB|1024|16|1|2|0|
|[24xx04](https://ww1.microchip.com/downloads/en/DeviceDoc/21708K.pdf)|512 B|512|16|1|1|0|
|[24xx02](https://ww1.microchip.com/downloads/en/devicedoc/21709c.pdf)|256 B|256|8|1|0|0|
|[24xx01](https://ww1.microchip.com/downloads/en/devicedoc/21711j.pdf)|128 B|128|8|1|0|0|

{{% alert context="info" %}}
24xx chips have a variety of part numbers, but tend to operate in the same way. Often a manufacturer specific part number indicates a different voltage range or upgraded features. AT24C, 24C, 24LC, 24AA, 24FC are all generally part of same basic 24xx family of chips. **Most should be fine with a 3.3 volt power supply, but if possible check the datasheet to be sure!**
{{% /alert %}}  

|24xx Family|Minimum Voltage|Maximum Voltage|Notes|
|---|---|---|---|
|AT24C|2.7V|5.5V|400kHz max|
|24C|2.7V|5.5V|400kHz max|
|24LC|2.5V|5.5V|400kHz max|
|24AA|1.7V|5.5V|400kHz max|
|24FC|1.8V|5.5V|1MHz max|