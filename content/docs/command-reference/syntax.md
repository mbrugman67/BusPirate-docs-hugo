+++
weight = 70200
title = 'Bus Syntax Reference'
+++

A simple syntax is used to interact with chips. Syntax characters have
the same general function in each bus mode, such as ```r``` to read a byte
of data.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [0x31 r:5]
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">31</span>
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

This example syntax sends a bus start, the value 0x31, and then reads 5
bytes, followed by bus stop. Up to 255 characters of syntax may be
entered into the Bus Pirate terminal at once, press ```enter``` to execute the
syntax.

{{% alert context="info" %}}
It's always best to use the latest firmware, especially in these early days of a new design. There will be continuous improvements and new features. See the upgrade guide for the simple drag and drop bootload process.
{{% /alert %}}

## Execute syntax
Start a line with ```[```, ```\{```, or ```>``` to tell the Bus Pirate to send data to an attached device.
### **[ or \{** Execute syntax with start

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [ 0x03 0 r:5]

CS Select (0)
<span style="color:#bfa530">TX:</span> 0x<span style="color:#53a6e6">03</span> 
<span style="color:#bfa530">TX:</span> 0 
<span style="color:#bfa530">RX:</span> 0x<span style="color:#53a6e6">48</span> 0x<span style="color:#53a6e6">65</span> 0x<span style="color:#53a6e6">6C</span> 0x<span style="color:#53a6e6">6C</span> 0x<span style="color:#53a6e6">6F</span> 
CS Deselect (1)
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Start commands generate a start condition (I2C), open a UART, control chip select (SPI) and have similar "start" type functions in every mode. A line beginning with these characters is interpreted as syntax.

### **>** Execute syntax (no start)

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> > 0x55 0xaa

<span style="color:#bfa530">TX:</span> 0x<span style="color:#53a6e6">55</span> 0x<span style="color:#53a6e6">AA</span> 
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

While the first two commands actually output something to the bus, this command tells the Bus Pirate to execute syntax without generating any output of its own.

{{% alert context="info" %}}
The ```>``` command is used to send syntax without sending a start command to the bus.
{{% /alert %}}

## Bus interaction syntax 

A simple syntax manipulates the bus and interacts with chips.
Syntax has the same general function in each bus mode, such as
```r``` to read a byte of data. See the individual bus mode guides for
each protocol.

### **\{ or [** Bus start condition

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#96cb59">SPI></span>
{{< /term >}}

```[``` generally starts bus activity. In various modes it starts (I2C),
selects (SPI), resets (1-wire), or opens (UART).

### **] or }** Bus stop condition

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >]
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

```]``` generally stops bus activity. In various modes it stops (I2C), deselects
(SPI), or closes (UART).

### **r** Read byte 
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >r
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}


r reads a byte from the bus. Use with the
repeat command (r:1...255) for bulk reads.

{{% alert context="info" %}}
The ```>``` before ```r``` tells the Bus Pirate we want to send data to the bus.
{{% /alert %}}

### **0b01** Write this binary value 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0b01
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0b<span style="color:#53a6e6">0000</span>0001
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Enter a binary value to write it to the bus.

[Binary](http://en.wikipedia.org/wiki/Binary_numeral_system) values are
commonly used in electronics because the 1's and 0's correspond to
register 'switches' that control various aspects of a device. Enter a
binary number as 0b and then the bits. Padding 0's are not required,
0b00000001=0b1. Can be used with the repeat command.

### **0x01** Write this HEX value 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x01
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">01</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Enter a HEX value to write it to the bus.

[Hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal) values are base
16 numbers that use a-f for the numbers 10-15, this format is very
common in computers and electronics. Enter HEX values as shown above,
precede the value with 0x or 0h. Single digit numbers don't need 0
padding, 0x01 and 0x1 are interpreted the same. A-F can be lowercase or
uppercase letters.

### **0-255** Write this decimal value

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >1
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 1
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Any number not preceded by 0x, 0h, or 0b is interpreted as a decimal value and sent to the bus.

[Decimal](http://en.wikipedia.org/wiki/Decimal) values are common base
10 numbers. Just enter the value, no special prefix is required.

### **"abc"** Write this ASCII string 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >"abc"
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 'a' 0x<span style="color:#53a6e6">61</span> 'b' 0x<span style="color:#53a6e6">62</span> 'c' 0x<span style="color:#53a6e6">63</span> 
{{< /term >}}

Characters enclosed in ```" "``` are sent to the bus as their [ASCII equivalent codes](https://en.wikipedia.org/wiki/ASCII).

### **```space```** Value delimiter

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [1 2 3  rr]
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 1
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 2
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 3
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Use a space to separate numbers. 

{{% alert context="info" %}}
No delimiter is required between non-number commands.
{{% /alert %}}

### **d/D** Delay 1uS/MS 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >d
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">1</span>us
<span style="color:#96cb59">SPI></span> >d:10
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">10</span>us
<span style="color:#96cb59">SPI></span> >D
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">1</span>ms
<span style="color:#96cb59">SPI></span> >D:10
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">10</span>ms
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

```d``` delays 1us, ```D``` delays 1ms. 

{{% alert context="info" %}}
Use the repeat command for multiple delays.
{{% /alert %}}

### **:** Repeat (e.g. r:10) 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> [ 0x55:2 D:3 r:3]
<span style="color:#bfa530">CS Select (0)</span>
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">55</span> 0x<span style="color:#53a6e6">55</span>
<span style="color:#bfa530"><span style="color:#bfa530">Delay:</span></span> <span style="color:#53a6e6">2</span>ms
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span> 0x<span style="color:#53a6e6">00</span>
<span style="color:#bfa530">CS Deselect (1)</span>
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Many commands can be repeated by adding ```:```, followed by the number of times to repeat. To read five bytes, enter ```r:5```, etc. 

{{% alert context="info" %}}
The repeat values can also be HEX/DEC/BIN formatted.
{{% /alert %}}

### **.** Partial read/write

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x5a.4
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">0A</span>.4
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Write/read partial bytes (where enabled by hardware) using the ```.``` option. ```0x75.4``` will write 0x5 (4 bits) to the bus. 

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >r.4
<span style="color:#bfa530"><span style="color:#bfa530">RX:</span></span> 0x<span style="color:#53a6e6">05</span>.4
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Read 4 bits from the bus.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x5432.12
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">04</span>32.12
<span style="color:#96cb59">SPI></span>
{{< /term >}}

Write 12 bits of 0x5432 to the bus.

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> >0x5a.4:2
<span style="color:#bfa530"><span style="color:#bfa530">TX:</span></span> 0x<span style="color:#53a6e6">0a</span>.4 0x<span style="color:#53a6e6">0a</span>.4
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

Partial write/reads can be combined with the repeat command.

### **v** Measure voltage

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">SPI></span> > v.1 v.2 v.3

<span style="color:#bfa530">Volts on IO1:</span> <span style="color:#53a6e6">3.2</span>V
<span style="color:#bfa530">Volts on IO2:</span> <span style="color:#53a6e6">3.2</span>V
<span style="color:#bfa530">Volts on IO3:</span> <span style="color:#53a6e6">3.2</span>V
<span style="color:#96cb59">SPI></span> 
{{< /term >}}

```v.x``` measures the voltage on IO pin x.

### **a/A/@** Auxiliary pin control (low/HIGH/read)

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">UART></span> >a.1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> OUTPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">UART></span> >A.1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> OUTPUT: <span style="color:#53a6e6">1</span>

<span style="color:#96cb59">UART></span> >@.1
<span style="color:#bfa530">IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span></span> INPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">UART></span>
{{< /term >}}

Sometimes it's useful to control a pin directly when executing bus syntax. ```a.X```, ```A.X``` and ```@.X``` set pin X low, high and input (HiZ). The ```@``` command also reads and reports the pin state.

{{% alert context="info" %}}
Syntax a/A/@ use the ```a.X``` notation, the syntax is followed by a **.** and the pin number to control. This is different than the commands a/A/@, which are followed by a space and the pin number to control.
{{% /alert %}}


