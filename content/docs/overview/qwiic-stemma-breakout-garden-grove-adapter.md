+++
weight = 20802
title = 'Qwiic, Stemma (3P/4P/QT), Breakout Garden, Grove I2C Adapter'
+++

{{% alert context="info" %}}
This is a placeholder for a future plank. 
{{% /alert %}}

One fabulous I2C quick connect adapter to rule them all! The quick connect adapter combines the most popular I2C breakout standards in one Bus Pirate compatible plank.

I2C is a simple communication protocol used by many sensors and devices. Over the years, manufacturers created "standard" I2C breakout board connectors for quick solder-free prototyping. All have the same basic four connections: power (V+), ground (GND), I2C Serial Data (SDA), and I2C Serial Clock (SCL). However, the pinout and connector types vary. 



## I2C Breakout Standards

- Adafruit Industries: [Stemma 3P, Stemma 4P (I2C), Stemma QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt/technical-specs)
- SparkFun Electronics: [Qwiic](https://www.sparkfun.com/qwiic)
- Seeed Studio: [Grove](https://wiki.seeedstudio.com/Grove_System/)
- DFRobot: [Gravity](https://www.dfrobot.com/gravity)
- Pimoroni: [Breakout Garden](https://shop.pimoroni.com/collections/breakout-garden)

{{% alert context="info" %}}
Adafruit's Stemma 3P is a single signal connector, not an I2C connector. 
{{% /alert %}}

## Pinout Table

|Pin| Stemma 3P| Stemma 4P |Stemma QT| Qwiic | Grove | Gravity | Breakout Garden |
|---|---|---|---|---|---|---|---|
|1  |SIGNAL        |   SCL     |GND    |   GND |   GND | SDA       |   V+|
|2  |V+         |   SDA     |V+     |   V+  |   V+  | SCL       |   SDA|
|3  |GND       |   VOUT    |SDA    |   SDA |   SDA | GND       |   SCL|
|4  |--         |   GND     |SCL    |   SCL |   SCL | V+        |   INT|
|5  |--         |   --      |--     |   --  |   --  | --        |   GND|

{{% alert context="info" %}}
Breakout Garden is a dual row PCB edge connector. The connections on each side are mirrored so boards can be inserted in both directions. The table above shows the pinout for a single row on one side.
{{% /alert %}}

## Connector Types

|Standard | Connector | Pitch | Example Part Number |
|---|---|---|---|
| Stemma 3P | JST PH 3P | 2.0mm |JST: S3B-PH-SM4-TB, Generic: HC-PH-3AWT|
| Stemma 4P | JST PH 4P | 2.0mm |JST: S4B-PH-SM4-TB, Generic: HC-PH-4AWT|
| Stemma QT | JST SH 4P | 1.0mm |JST: SM04B-SRSS-TB, Generic: HC-1.0-4PWT|
| Qwiic     | JST SH 4P | 1.0mm |JST: SM04B-SRSS-TB, Generic: HC-1.0-4PWT|
| Grove     | "HY" 4P | 2.0mm |HY-4P, HY2.0-4P-SMD, A2008WR-S-4P|
| Gravity   | JST PH 4P | 2.0mm |JST: S4B-PH-SM4-TB, Generic: HC-PH-4AWT|
| Breakout Garden | PCB edge slot conn. 2 x 5P | 2.54mm |ED10BGFBK|

## Thanks!

A huge thank you to Funcan, kd7eir, grymoire, and henrygab for testing the various connectors with genuine breakout boards! 

## Resources

-  [schematic and PCB]()
- [Development thread](https://forum.buspirate.com/t/qwiic-stemma-qt-breakout-garden-grove-plank/1177)

## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community 

{{% readfile "/_common/_footer/_footer-community.md" %}}

### Documentation

{{% readfile "/_common/_footer/_footer-docs.md" %}}



