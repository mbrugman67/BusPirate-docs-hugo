+++
weight = 70600
title = 'Half-Duplex UART'
+++

-   **Bus:** Half-duplex [UART](http://en.wikipedia.org/wiki/Serial_uart),
    [MIDI](http://en.wikipedia.org/wiki/Musical_Instrument_Digital_Interface)
    (universal asynchronous receiver transmitter), RX and TX on the same wire
-   **Connections:** one data pin (RXTX) and ground
-   **Output type:** open collector - pull-up resistors required
-   **Maximum Voltage:** 5volts

{{% alert context="info" %}}
Half-duplex UART is a common serial UART, but receive and transmit share a single data line. This is used to interface mobile phone SIM cards and bank IC cards.
{{% /alert %}}


## Connections
| Bus Pirate | Direction                     | Circuit | Description   |
|------------|--------------------------|---------|---------------|
| RXTX       | <font size="+2">←→</font> | RXTX    | Bus Pirate Transmit and Receive   |
| GND        | <font size="+2">⏚</font> | GND     | Signal Ground |

## Configuration options

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bfa530">UART speed</span>
 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200 etc
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Baud (</span>115200*<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Data bits</span>
 5 to 8 bits
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Bits (</span>8*<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Parity</span>
 1. <span style="color:#bfa530">None*</span>
 2. <span style="color:#bfa530">Even</span>
 3. <span style="color:#bfa530">Odd</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Parity (</span>1<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Stop bits</span>
 1. <span style="color:#bfa530">1*</span>
 2. <span style="color:#bfa530">2</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Bits (</span>1<span style="color:#96cb59">) ></span> 
<span style="color:#bfa530">Mode:</span> HDPLXUART
<span style="color:#96cb59">HDPLXUART></span> 
{{< /term >}}

**Pull-up resistors**

Half-duplex UART is an open-collector bus, it requires pull-up resistors to hold the data line high to create the data '1'. The Bus Pirate doesn't
output high, it only pulls low. Without pull-up resistors there can
never be a '1'. 

Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.

{{% alert context="info" %}}
- Half-duplex UART requires pull-up resistors to hold the data line high.
- Without pull-up resistors there can never be a '1'. 
- Enable the Bus Pirate onboard pull-up resistors with the ```P``` command.
{{% /alert %}}

## Syntax

|Command| Description  |
|---------|-------|
| [      | Open UART, use ```r``` to read bytes. |
| \{       | Open UART, display data as it arrives asynchronously. |
| \] or } | Close UART.  |
| r       | Check UART for byte, or fail if empty. (r:1…255 for bulk reads) |
| 0b      | Write this binary value. Format is 0b00000000 for a byte, but partial bytes are also fine: 0b1001.|
| 0x      | Write this HEX value. Format is 0x01. Partial bytes are fine: 0xA. A-F can be lower-case or capital letters. |
| 0-255   | Write this decimal value. Any number not preceded by 0x or 0b is interpreted as a decimal value. |
| ```space```| Value delimiter. Use a space to separate numbers. No delimiter is required between non-number values: \{0xa6 0 0 16 5 0b111 0xaF rrrr}. |
| \(#\)   | Run macro, (0) for macro list. |


## Commands

Bus Pirate 5 has global commands available everywhere, and mode commands specific to the currently selected mode. Type ```help``` to see all commands in every mode, or ```help mode``` for the currently available mode commands.

{{% alert context="info" %}}
Most Bus Pirate commands have help. Add the ```-h``` flag to any command to see the latest available options and usage examples. 
{{% /alert %}}

### bridge

Transparent UART ```bridge```. Bidirectional UART pass-through to interact with other serial devices from inside the Bus Pirate terminal. Press the Bus Pirate button to exit.

#### Help

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HDPLXUART></span> bridge -h
usage:
<span style="color:#bfa530">bridge	[-h(elp)]</span>
<span style="color:#bfa530">Transparent UART bridge: bridge</span>
<span style="color:#bfa530">Exit: press Bus Pirate button</span>

<span style="color:#bfa530">open UART with raw data IO, usb to serial bridge mode</span>
<span style="color:#96cb59">-t</span>	<span style="color:#bfa530">ENABLE toolbar while bridge is active (default: disabled)</span>
<span style="color:#96cb59">-s</span>	<span style="color:#bfa530">Suppress local echo, don't echo back sent data</span>
<span style="color:#96cb59">-h</span>	<span style="color:#bfa530">Get additional help</span>

<span style="color:#96cb59">HDPLXUART></span> 
{{< /term >}} 
 

{{% alert context="info" %}}
Use ```bridge -h``` to see the latest options and features.
{{% /alert %}}






