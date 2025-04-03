+++
weight = 2
title = 'Bus Syntax'
+++


# Syntax Reference

A simple syntax is used to interact with chips. Syntax characters have
the same general function in each bus mode, such as ```r``` to read a byte
of data.

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> [0x31 r:5]<br/>
<span className="bp-info">CS Select (0)</span><br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0x<span className="bp-float">31</span><br/>
<span className="bp-info"><span className="bp-info">RX:</span></span> 0x<span className="bp-float">00</span> 0x<span className="bp-float">00</span> 0x<span className="bp-float">00</span> 0x<span className="bp-float">00</span> 0x<span className="bp-float">00</span><br/>
<span className="bp-info">CS Deselect (1)</span><br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

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

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> [ 0x03 0 r:5]<br/>
<br/>
CS Select (0)<br/>
<span className="bp-info">TX:</span> 0x<span className="bp-float">03</span> <br/>
<span className="bp-info">TX:</span> 0 <br/>
<span className="bp-info">RX:</span> 0x<span className="bp-float">48</span> 0x<span className="bp-float">65</span> 0x<span className="bp-float">6C</span> 0x<span className="bp-float">6C</span> 0x<span className="bp-float">6F</span> <br/>
CS Deselect (1)<br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

Start commands generate a start condition (I2C), open a UART, control chip select (SPI) and have similar "start" type functions in every mode. A line beginning with these characters is interpreted as syntax.

### **>** Execute syntax (no start)

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> > 0x55 0xaa<br/>
<br/>
<span className="bp-info">TX:</span> 0x<span className="bp-float">55</span> 0x<span className="bp-float">AA</span> <br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

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

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> [<br/>
<span className="bp-info">CS Select (0)</span><br/>
<span className="bp-prompt">SPI></span><br/>
{{% /term %}}

```[``` generally starts bus activity. In various modes it starts (I2C),
selects (SPI), resets (1-wire), or opens (UART).

### **] or }** Bus stop condition

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >]<br/>
<span className="bp-info">CS Deselect (1)</span><br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

```]``` generally stops bus activity. In various modes it stops (I2C), deselects
(SPI), or closes (UART).

### **r** Read byte 
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >r<br/>
<span className="bp-info"><span className="bp-info">RX:</span></span> 0x<span className="bp-float">00</span><br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}


r reads a byte from the bus. Use with the
repeat command (r:1...255) for bulk reads.

{{% alert context="info" %}}
The ```>``` before ```r``` tells the Bus Pirate we want to send data to the bus.
{{% /alert %}}

### **0b01** Write this binary value 

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >0b01<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0b<span className="bp-float">0000</span>0001<br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

Enter a binary value to write it to the bus.

[Binary](http://en.wikipedia.org/wiki/Binary_numeral_system) values are
commonly used in electronics because the 1's and 0's correspond to
register 'switches' that control various aspects of a device. Enter a
binary number as 0b and then the bits. Padding 0's are not required,
0b00000001=0b1. Can be used with the repeat command.

### **0x01** Write this HEX value 

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >0x01<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0x<span className="bp-float">01</span><br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

Enter a HEX value to write it to the bus.

[Hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal) values are base
16 numbers that use a-f for the numbers 10-15, this format is very
common in computers and electronics. Enter HEX values as shown above,
precede the value with 0x or 0h. Single digit numbers don't need 0
padding, 0x01 and 0x1 are interpreted the same. A-F can be lowercase or
uppercase letters.

### **0-255** Write this decimal value

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >1<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 1<br/>
<span className="bp-prompt">SPI></span><br/>
{{% /term %}}

Any number not preceded by 0x, 0h, or 0b is interpreted as a decimal value and sent to the bus.

[Decimal](http://en.wikipedia.org/wiki/Decimal) values are common base
10 numbers. Just enter the value, no special prefix is required.

### **"abc"** Write this ASCII string 

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >"abc"<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 'a' 0x<span className="bp-float">61</span> 'b' 0x<span className="bp-float">62</span> 'c' 0x<span className="bp-float">63</span> <br/>
{{% /term %}}

Characters enclosed in ```" "``` are sent to the bus as their [ASCII equivalent codes](https://en.wikipedia.org/wiki/ASCII).

### **```space```** Value delimiter

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> [1 2 3  rr]<br/>
<span className="bp-info">CS Select (0)</span><br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 1<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 2<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 3<br/>
<span className="bp-info"><span className="bp-info">RX:</span></span> 0x<span className="bp-float">00</span><br/>
<span className="bp-info"><span className="bp-info">RX:</span></span> 0x<span className="bp-float">00</span><br/>
<span className="bp-info">CS Deselect (1)</span><br/>
<span className="bp-prompt">SPI></span><br/>
{{% /term %}}

Use a space to separate numbers. 

{{% alert context="info" %}}
No delimiter is required between non-number commands.
{{% /alert %}}

### **d/D** Delay 1uS/MS 

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >d<br/>
<span className="bp-info"><span className="bp-info">Delay:</span></span> <span className="bp-float">1</span>us<br/>
<span className="bp-prompt">SPI></span> >d:10<br/>
<span className="bp-info"><span className="bp-info">Delay:</span></span> <span className="bp-float">10</span>us<br/>
<span className="bp-prompt">SPI></span> >D<br/>
<span className="bp-info"><span className="bp-info">Delay:</span></span> <span className="bp-float">1</span>ms<br/>
<span className="bp-prompt">SPI></span> >D:10<br/>
<span className="bp-info"><span className="bp-info">Delay:</span></span> <span className="bp-float">10</span>ms<br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

```d``` delays 1us, ```D``` delays 1ms. 

{{% alert context="info" %}}
Use the repeat command for multiple delays.
{{% /alert %}}

### **:** Repeat (e.g. r:10) 

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> [ 0x55:2 D:3 r:3]<br/>
<span className="bp-info">CS Select (0)</span><br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0x<span className="bp-float">55</span> 0x<span className="bp-float">55</span><br/>
<span className="bp-info"><span className="bp-info">Delay:</span></span> <span className="bp-float">2</span>ms<br/>
<span className="bp-info"><span className="bp-info">RX:</span></span> 0x<span className="bp-float">00</span> 0x<span className="bp-float">00</span> 0x<span className="bp-float">00</span><br/>
<span className="bp-info">CS Deselect (1)</span><br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

Many commands can be repeated by adding ```:```, followed by the number of times to repeat. To read five bytes, enter ```r:5```, etc. 

{{% alert context="info" %}}
The repeat values can also be HEX/DEC/BIN formatted.
{{% /alert %}}

### **.** Partial read/write

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >0x5a.4<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0x<span className="bp-float">0A</span>.4<br/>
<span className="bp-prompt">SPI></span><br/>
{{% /term %}}

Write/read partial bytes (where enabled by hardware) using the ```.``` option. ```0x75.4``` will write 0x5 (4 bits) to the bus. 

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >r.4<br/>
<span className="bp-info"><span className="bp-info">RX:</span></span> 0x<span className="bp-float">05</span>.4<br/>
<span className="bp-prompt">SPI></span><br/>
{{% /term %}}

Read 4 bits from the bus.

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >0x5432.12<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0x<span className="bp-float">04</span>32.12<br/>
<span className="bp-prompt">SPI></span><br/>
{{% /term %}}

Write 12 bits of 0x5432 to the bus.

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> >0x5a.4:2<br/>
<span className="bp-info"><span className="bp-info">TX:</span></span> 0x<span className="bp-float">0a</span>.4 0x<span className="bp-float">0a</span>.4<br/>
<span className="bp-prompt">SPI></span> <br/>
{{% /term %}}

Partial write/reads can be combined with the repeat command.

### **v** Measure voltage

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">SPI></span> > v.1 v.2 v.3<br/>
<br/>
<span className="bp-info">Volts on IO1:</span> <span className="bp-float">3.2</span>V<br/>
<span className="bp-info">Volts on IO2:</span> <span className="bp-float">3.2</span>V<br/>
<span className="bp-info">Volts on IO3:</span> <span className="bp-float">3.2</span>V<br/>
<span className="bp-prompt">SPI></span> 
{{% /term %}}

```v.x``` measures the voltage on IO pin x.

### **a/A/@** Auxiliary pin control (low/HIGH/read)

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">UART></span> >a.1<br/>
<span className="bp-info">IO<span className="bp-float">1<span className="bp-info"> set to</span></span></span> OUTPUT: <span className="bp-float">0</span><br/>
<br/>
<span className="bp-prompt">UART></span> >A.1<br/>
<span className="bp-info">IO<span className="bp-float">1<span className="bp-info"> set to</span></span></span> OUTPUT: <span className="bp-float">1</span><br/>
<br/>
<span className="bp-prompt">UART></span> >@.1<br/>
<span className="bp-info">IO<span className="bp-float">1<span className="bp-info"> set to</span></span></span> INPUT: <span className="bp-float">0</span><br/>
<br/>
<span className="bp-prompt">UART></span>
{{% /term %}}

Sometimes it's useful to control a pin directly when executing bus syntax. ```a.X```, ```A.X``` and ```@.X``` set pin X low, high and input (HiZ). The ```@``` command also reads and reports the pin state.

{{% alert context="info" %}}
Syntax a/A/@ use the ```a.X``` notation, the syntax is followed by a **.** and the pin number to control. This is different than the commands a/A/@, which are followed by a space and the pin number to control.
{{% /alert %}}

<DiscourseComments/>
