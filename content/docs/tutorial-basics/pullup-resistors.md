+++
weight = 30500
title = 'Pull-up Resistors and IO'
+++

{{< asciicast src="/screencast/tut-pull-io.json" poster="npt:0:14" terminalFontSize="medium" idleTimeLimit=2 >}}

Protocols such as I2C and 1-Wire use open collector outputs for two way communication on a single data wire. In this type of protocol there is no 1/high level without a pull-up resistor. The pull-up resistor connects to a voltage that "pulls" the wire high. Devices use their output to ground the wire and pull it low.

The Bus Pirate has 10KΩ onboard pull-up resistors that can be toggled with the ```p``` and ```P``` commands.

# Overview

|Command|Description|
|---|---|
|```p```|Disable pull-up resistors.|
|```P```|Enable pull-up resistors.|
|```a X```|Set pin X to output and low.|
|```A X```|Set pin X to output and high.|
|```@ X```|Set pin X to input.|
|```W```|Enable the power supply, configure voltage and current limit.|


## Enter LED mode

This tutorial uses LED mode configured for the onboard LEDs, see [Blink Some LEDs tutorial]({{< relref "/docs/tutorial-basics/leds-demo.md" >}}). In this mode all the Bus Pirate IO pins are free for experimenting.

{{% alert context="info" %}}
See the 'Blink Some LEDs' tutorial to enter and configure LED mode.
{{% /alert %}}

## Voltage Source

The pull-up resistors are powered by the voltage on the VOUT/VREF pin. This can come from two sources:

- The onboard [programmable power supply unit]({{< relref "/docs/tutorial-basics/power-supply.md" >}})
- Externally through the VOUT/VREF pin on the Bus Pirate main connector

For this tutorial let's use the onboard power supply.

### Programmable Power Supply Unit

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span>  W 5 100
<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">5.00</span></span>V
<span style="color:#53a6e6">100.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">100.0</span></span>mA

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">Vreg output: <span style="color:#53a6e6">5.00</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">5.00</span></span>V<span style="color:#bfa530">, Current: <span style="color:#53a6e6">2.3</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

Enable the power supply, this will power the pull-up resistors and the IO buffers.

{{% alert context="info" %}}
Here, we use ```W 5 100``` to quickly enable a 5 volt supply and 100mA current limit fuse. 

You can also use the ```W``` command with no options to see the configuration menu.
{{% /alert %}}

![](/images/docs/fw/pullup-statusbar-3.png)

Check the live view statusbar at the bottom of the terminal. 
- The top line indicates the power supply is set at 5 volts with a 100mA current limit. 
- The third line shows that 7.8mA is being consumed on VOUT. Since nothing is connected this represents the IO buffer current, base current of the PPSU, op-amp offset error and noise in the RPi chip analog to digital converter.
- The last line shows that VOUT currently measures 5volts, and other pins measure 0 volts.

### External Power Supply

Hacking a device with its own power supply? You can use that instead. 

- Connect the device power to the Bus Pirate VOUT/VREF pin
- Connect the device ground to the Bus Pirate ground pin.

{{% alert context="danger" %}}
The Bus Pirate is rated for 5volts DC maximum. Exceeding this limit will damage the Bus Pirate and your computer.
{{% /alert %}}

## Enable Pull-up Resistors

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> P
<span style="color:#bfa530"><span style="color:#bfa530">Pull-up resistors:</span></span> Enabled (10K ohms @ <span style="color:#53a6e6">5.0</span>V)

<span style="color:#96cb59">LED-()></span> 


{{< /term >}}

Type uppercase ```P``` followed by ```enter``` to activate the pull-up resistors.

![](/images/docs/fw/pullup-statusbar-1.png)

In the live view statusbar all pins should be high, close to 5.0 volts.
- The top line now shows that the pull-up resistors are enabled.
- The bottom line shows that IO0 to IO7 all measure 4.9 volts.

{{% alert context="info" %}}
4.9volts isn't exactly 5, but that's not a problem.
{{% /alert %}}

## Controlling IO Pins

Sometimes it's helpful to toggle or read a pin. The ```a```/```A```/```@``` commands toggle the Bus Pirate pins low, high and input.

### Auxiliary Pins Low

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> a 0
IO<span style="color:#53a6e6">0<span style="color:#bfa530"> set to</span></span> OUTPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">LED-()></span> a 1; a 2; a 3; 
IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span> OUTPUT: <span style="color:#53a6e6">0</span>
IO<span style="color:#53a6e6">2<span style="color:#bfa530"> set to</span></span> OUTPUT: <span style="color:#53a6e6">0</span>
IO<span style="color:#53a6e6">3<span style="color:#bfa530"> set to</span></span> OUTPUT: <span style="color:#53a6e6">0</span>

<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

```a 0``` configures IO 0 as output and low. Multiple commands can be chained with the ```;```, ```||``` and ```&&``` operators.

- Type ```a 0; a 1; a 2; a 3``` and press ```enter``` to configure IO0 to IO3 as output and low.

![](/images/docs/fw/pullup-statusbar-2.png)

Verify that the pins are low in the live view statusbar if active, or use the ```v``` command to view a voltage report.
- The third line shows that IO0 to IO3 are configured as auxiliary-low (AUXL).
- The last line shows that IO0 to IO3 now measure close to ground (0.1volt).

### Auxiliary Pins Input

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> @ 0; @ 1; @ 2; @ 3
IO<span style="color:#53a6e6">0<span style="color:#bfa530"> set to</span></span> INPUT: <span style="color:#53a6e6">1</span>
IO<span style="color:#53a6e6">1<span style="color:#bfa530"> set to</span></span> INPUT: <span style="color:#53a6e6">1</span>
IO<span style="color:#53a6e6">2<span style="color:#bfa530"> set to</span></span> INPUT: <span style="color:#53a6e6">1</span>
IO<span style="color:#53a6e6">3<span style="color:#bfa530"> set to</span></span> INPUT: <span style="color:#53a6e6">1</span>
{{< /term >}}

```@ X``` makes the corresponding Bus Pirate pin an input, allowing the pull-up resistors to hold the pin high again.  
- Type ```@ 0; @ 1; @ 2; @ 3``` followed by ```enter```.

{{% alert context="info" %}}
```@ X``` also reads the state of the input pin. In this case the Bus Pirate reads '1' because the pull-up resistors are holding the pin high.
{{% /alert %}}

![](/images/docs/fw/pullup-statusbar-1.png)

Verify that all the pins are around 5volts in the live monitor statusbar, or by using the voltage report command ```v```.
- All pins should be pulled high again.

### Disable Pull-ups
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> p
<span style="color:#bfa530">Pull-up resistors:</span> Disabled
<span style="color:#96cb59">LED-()></span>
{{< /term >}}

- Type lowercase ```p``` then hit ```enter``` to disable the pull-up resistors.

![](/images/docs/fw/pullup-statusbar-4.png)

Verify that all the pins show 0volts in the live monitor statusbar or voltage report.
- All pins should now be at 0volts because the pull-up are disabled.

### Auxiliary Pins High
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> A 0
IO<span style="color:#53a6e6">0<span style="color:#bfa530"> set to</span></span> OUTPUT: <span style="color:#53a6e6">1</span>
<span style="color:#96cb59">LED-()></span> 
{{< /term >}}
![](/images/docs/fw/aux-a.png)

```A X``` sets the corresponding Bus Pirate pin to output and high.
- Type ```A 0``` followed by ```enter``` to set IO0 high.
- The live view statusbar should show that IO0 is now high (AUXH) and measures 5 volts.