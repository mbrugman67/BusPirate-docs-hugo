+++
weight = 40215
title = 'SHT30, SHT31 and SHT35 Humidity & Temperature I2C'
katex = true
+++

![](/images/docs/demo/si7021.jpg)

SHT30, SHT31 and SHT35 measure temperature (-40 to 125C) and humidity (0-100%). They're a significant upgrade to the previous [SHT2x]({{< relref "/docs/devices/si7021/">}}) series, with a wider temperature and humidity range, higher accuracy, and a simpler interface.

| Feature | SHT30           | SHT31                | SHT35                | SHT2x Series         |
|-------------|-------------|----------------------|----------------------|----------------------|
| Range  | -40 to 125°C (0–100% RH)| -40 to 125°C  (0–100% RH) | -40 to 125°C  (0–100% RH)  | -10 to 85°C  (0–80% RH) |
| Accuracy | ±0.2°C  (±2% RH)  | ±0.2°C  (±2% RH) | ±0.15°C (±1.5% RH) | ±0.3°C (±2% RH)                 |
| Accuracy at Extremes   | Good      | Better    | **Best**   | Lower   |
| Interface Complexity   | Single read | Single read | Single read| Two reads |

Join below for a journey through the SHT30, SHT31 and SHT35 sensors, from setup to reading temperature and humidity.

{{% readfile "/_common/_footer/_footer-cart.md" %}}

## Connections

![alt text](/images/docs/sht30-sht31-sht35/image-3.png)

|Bus Pirate|SHT3x|Description|
|-|-|-|
|SDA|SDA|I2C Data|
|SCL|SCL|I2C Clock|
|Vout/Vref|VDD|3.3volt power supply|
|GND|GND|Ground|

These sensors are tiny and it's highly likely you're using a breakout board, like us. The important connections are the I2C data (SDA) and clock (SCL) lines, the power supply (Vout/Vref), and ground (GND).

{{% alert context="warning" %}}
The SHT3x address pin should be connected to power or ground, but breakout boards almost always have this pin connected to ground setting the I2C address to 0x44 (0x88 write, 0x89 read).
{{% /alert %}}

Image source: [Sensirion SHT3x Datasheet](https://sensirion.com/media/documents/213E6A3B/63A5A569/Datasheet_SHT3x_DIS.pdf).

## See it in action

{{< asciicast src="/screencast/sht3x-cast.json" poster="npt:0:27"  idleTimeLimit=2 >}}

## Setup

{{< termfile source="static/snippets/sht3x-setup.html" >}}

SHT3x series sensors have an I2C interface, put the Bus Pirate in I2C mode.

- ```m i2c``` - set the Bus Pirate to I2C [mode]({{< relref "/docs/command-reference/#m-set-bus-mode" >}}), or just hit ```m``` to select from the menu.
- ```400``` - set the I2C bus speed to 400kHz.
- ```1``` - disable clock stretching.

{{% alert context="info" %}}
The SHT3x supports clock stretching, which is a way for the device to signal that it needs more time to process a command. It adds some complexity though, so we've disabled it for this demo.
{{% /alert %}}

### Power supply
![alt text](/images/docs/sht30-sht31-sht35/image.png)

According to the datasheet the SHT3x has a wide supply range from 2.15 to 5.5 volts.  

{{< termfile source="static/snippets/sht3x-power.html" >}}

Let’s set the Bus Pirate to power the chip at 3.3volts, a very common voltage for current generation I2C devices.
- ```W 3.3``` - enable the [onboard power supply]({{< relref "/docs/command-reference/#ww-power-supply-offon">}}) at 3.3volts.

### Pull-up resistors

{{< termfile source="static/snippets/sht3x-pullup.html" >}}

I2C is an open collector output bus, the Bus Pirate and the SHT3x can only pull the line low to 0 (ground). A pull-up resistor is needed to pull the line high to 1 (3.3 volts). The Bus Pirate has built-in pull-up resistors that can be enabled with the ```P``` command.
- ```P``` - Enable the [onboard pull-up resistors]({{< relref "/docs/command-reference/#pp-pull-up-resistors">}}).

{{% alert context="warning" %}} 
Be sure to enable the pull-up resistors. Without them, the clock data line will never go high and you'll read only 0s.
{{% /alert %}}

## I2C address scan

{{< termfile source="static/snippets/sht3x-scan.html" >}}

We need the correct I2C address to talk to the sensor. We could look in the datasheet, or we can run the handy [I2C address scanner]({{< relref "/docs/command-reference/#scan-i2c-address-search">}}).
- ```scan``` - Scan the I2C bus for devices

The scanner found an I2C device at address 0x40 (0x80 write, 0x81 read). 0x00 is usually a "general call" address which addresses all devices sharing the bus, we'll ignore that for now.

{{% alert context="info" %}} 
If the scanner doesn't find the device, ensure the power supply is enabled ```W 3.3``` and the pull-up resistors are enabled ```P```.
{{% /alert %}}

## Single shot measurement

{{% alert context="info" %}}
SHT3x can measure temperature and humidity once (**single shot**) or periodically on a timer. We'll use the single shot mode for this demo.
{{% /alert %}}

| Repeatability | Clock Stretching | Cmd. MSB  | Cmd. LSB  |Time Max. (ms)|Repeatability (C) |
|---------------|------------------|------|------|--------------|---------------|
|  High          | **disabled**         | 0x24 | 0x00 |16ms|0.04C|
|  Medium        | **disabled**         | 0x24 | 0x0B |6ms|0.08C|
|  Low           | **disabled**         | 0x24 | 0x16 |4ms|0.15C|
|  High          | enabled          | 0x2C | 0x06 |15ms|0.04C|
|  Medium        | enabled          | 0x2C | 0x0D |6ms|0.08C|
| Low           | enabled          | 0x2C | 0x10 |4ms|0.15C|

Measurements have three repeatability settings: high, medium, and low. The higher the repeatability, the more accurate the measurement, but it takes longer to complete.  

There are two sets of single shot measurement commands, one with clock stretching enabled and one without. 
- **Clock stretching enabled** pauses the master (Bus Pirate) by holding the I2C clock line low until the measurement is complete. 
- **Clock stretching disabled** commands, on the other hand, cause the SHT3x to ignore its I2C read address until the measurement is complete.

{{% alert context="info" %}}
Let's use the **high repeatability clock stretching disabled command (0x24 0x00)** with a 16ms delay. Clock stretching is useful, but it ties up the I2C bus while the measurement is in progress and no other sensors can be read until it completes. 
{{% /alert %}}

### Trigger measurement

Triggering a humidity measurement follows the typical I2C transaction pattern: write the command to the write address, then read the result from the read address. The only trick is that we need to add the [correct delay]({{< relref "/docs/devices/sht30-sht31-sht35/#single-shot-measurement">}}) before reading the result. If we try to read before the measurement is complete, the SHT3x will not acknowledge (NACK) its read address.

![alt text](/images/docs/sht30-sht31-sht35/image-2.png)

Let's break down this diagram from the datasheet into three steps: start the measurement, poll for completion, and read the result.

Start the measurement:
1. **S** - Begin with an I2C START bit
2. **I2C Address + W** - Send the SHT3x write address (0x88)
3. **Command MSB/LSB** - Send the two byte measurement command for the desired repeatability
4. **P** - End with an I2C STOP bit

Poll for measurement complete (or just delay according to the table):
1.  **S** - I2C START bit, begins the next transaction
5. **I2C Address +R, NACK** - The SHT3x will not ACK its read address until the measurement is complete, so we need to wait a bit before reading the result
6. **P** - End with an I2C STOP bit

When the chip ACKs its read address the measurement is complete, we can read the result:
1. **S** - Begin with an I2C START bit
5. **I2C Address + R, ACK** - Send the SI7021 read address (0x81)
6. **Temperature MSB/LSB + CRC** - Read the two byte humidity measurement and checksum byte.
7. **Humidity MSB/LSB + CRC** - Read the two byte temperature measurement and checksum byte.
7. **P** - End with an I2C STOP bit

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;[0x88&nbsp;0x24&nbsp;0x00]&nbsp;D:15&nbsp;[0x89&nbsp;r:6]

I2C&nbsp;START
<span style="color:rgb(191,165,48)">TX:</span>&nbsp;0x<span style="color:rgb(83,166,230)">88</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">24</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">00</span>&nbsp;ACK&nbsp;
I2C&nbsp;STOP
<span style="color:rgb(191,165,48)">Delay:</span>&nbsp;<span style="color:rgb(83,166,230)">15</span>ms
I2C&nbsp;START
<span style="color:rgb(191,165,48)">TX:</span>&nbsp;0x<span style="color:rgb(83,166,230)">89</span>&nbsp;ACK&nbsp;
<span style="color:rgb(191,165,48)">RX:</span>&nbsp;0x<span style="color:rgb(83,166,230)">65</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">4F</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">B0</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">BC</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">7E</span>&nbsp;ACK&nbsp;0x<span style="color:rgb(83,166,230)">43</span>&nbsp;NACK&nbsp;
I2C&nbsp;STOP
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term >}}

We're going to deviate from the datasheet example a bit here. Instead of repeating the read address until the measurement is complete, we'll end the write command with an I2C STOP bit, then wait for a fixed delay of 15ms before reading the result. 

- ```[``` - I2C START bit
- ```0x88``` - SHT3x write address
- ```0x24 0x00``` - High repeatability measurement command with clock stretching disabled
- ```]``` - I2C STOP bit, ends this transaction
- ```D:15``` - [Delay]({{< relref "/docs/command-reference/#dd-delay-1usms">}}) for 15ms while the measurement is in progress
- ```[``` - I2C START bit, begins the read transaction
- ```0x89``` - SHT3x read address
- ```r:6``` - Read six bytes of data
- ```]``` - I2C STOP bit, ends the read transaction

The six byte measurement result is: 0x65 0x4F 0xB0 0xBC 0x7E 0x43

{{% alert context="info" %}}
15ms is the [maximum time]({{< relref "/docs/devices/sht30-sht31-sht35/#single-shot-measurement">}}) it takes to complete a high repeatability measurement. During this delay we could trigger other sensors or do other tasks, then come back to read the result. 
{{% /alert %}}

![alt text](/images/docs/sht30-sht31-sht35/image-4.png)

- Result: ```0x65 0x4F 0xB0 0xBC 0x7E 0x43```

The datasheet shows that the first two bytes are the temperature measurement (0x65 0x4F) plus a CRC error checking byte (0xB0). The next two bytes are the humidity measurement (0xBC 0x7E) and another CRC byte (0x43).

{{% alert context="info" %}}
The CRC bytes can be used to verify the integrity of the data, but we'll skip that. See the datasheet for details on how to calculate the CRC.
{{% /alert %}}

### Convert to temperature

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;=&nbsp;0x654f
&nbsp;=0x<span style="color:rgb(83,166,230)">65</span>4F.16&nbsp;=25935.16&nbsp;=0b<span style="color:rgb(83,166,230)">0110</span>0101<span style="color:rgb(83,166,230)">0100</span>1111.16
<span style="color:rgb(150,203,89)">I2C></span>
{{< /term >}}

Convert the HEX bytes into a decimal number with the ```=``` convert base command: 0x654f is 25935 in decimal. Now we can calculate the temperature in Celsius using a formula from the datasheet:

$$\text{Temp C} = -45 + 175 \times \left(\frac{\text{St}}{2^{16}-1}\right)$$
$$\text{Temp C} = -45 + 175 \times \left(\frac{\text{25935}}{2^{16}-1}\right)$$
$$\text{Temp C} = -45 + 175 \times \left(\frac{25935}{65535}\right)$$
$$\text{Temp C} = -45 + 175 \times 0.3955$$
$$\text{Temp C} = -45 + 69.2$$
$$\text{Temp C} = 24.2$$

Today in the lab we're experiencing a summer heat wave and the temperature is already 24.2C at 10am.

### Convert to humidity

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;=&nbsp;0xbc7e
&nbsp;=0x<span style="color:rgb(83,166,230)">BC</span>7E.16&nbsp;=48254.16&nbsp;=0b<span style="color:rgb(83,166,230)">1011</span>1100<span style="color:rgb(83,166,230)">0111</span>1110.16
<span style="color:rgb(150,203,89)">I2C></span>&nbsp;
{{< /term >}}

Convert the humidity HEX bytes into a decimal number with the ```=``` convert base command: 0xbc7e is 48254 in decimal. Finally, convert the reading to relative humidity using a formula from the datasheet:

$$\text{RH\\%} = 100 \times \left(\frac{\text{Srh}}{2^{16}-1}\right)$$
$$\text{RH\\%} = 100 \times \left(\frac{\text{48254}}{2^{16}-1}\right)$$
$$\text{RH\\%} = 100 \times \left(\frac{48254}{65535}\right)$$
$$\text{RH\\%} = 100 \times 0.7352$$
$$\text{RH\\%} = 73.5$$

A balmy 24C with 73.5% relative humidity, hopefully it rains and cools off soon!


## Get a Bus Pirate

{{% readfile "/_common/_footer/_footer-get.md" %}}

### Community

{{% readfile "/_common/_footer/_footer-community.md" %}}