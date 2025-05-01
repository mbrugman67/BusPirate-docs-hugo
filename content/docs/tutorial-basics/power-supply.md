+++
weight = 30400
title = 'Programmable Power Supply'
+++

{{< asciicast src="/qs-psu.json" poster="npt:0:14" terminalFontSize="medium" idleTimeLimit=2 >}}

The Bus Pirate has a 'Programmable Power Supply Unit' (PPSU) that can power devices from the VOUT/VREF pin of the main connector.

- 1-5volts adjustable output, 400mA max
- 0-500mA current sense 
- 0-500mA current limit with digital fuse
- Backflow prevention to protect the PPSU when an external voltage is applied to the VREF/VOUT pin

## Overview

|Command|Description|
|---|---|
|```W```|Enable the power supply, configure voltage and current limit.|
|```w```|Disable the power supply.|
|```v```|Show the power supply voltage report.|

## Enable
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> W
<span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span>
<span style="color:#96cb59">x to exit (3.30) ></span> 5
<span style="color:#bfa530">Maximum current (0mA-500mA), 0 for none</span>
<span style="color:#96cb59">x to exit (300) ></span> 100
<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">5.00</span></span>V
<span style="color:#53a6e6">100.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">100.0</span></span>mA

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">Vreg output: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Current: <span style="color:#53a6e6">3.0</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">I2C></span> 
{{< /term >}}

{{% alert context="info" %}}
Enter any protocol mode (```m```) to use the power supply. The power supply is always disabled in HiZ safe mode.
{{% /alert %}}

Type uppercase ```W``` followed by ```enter``` to enable the power supply. 

- Enter the desired output in volts, for example ```5``` followed by ```enter```.
- Enter the desired current limit in milliamps, for example ```100``` followed by ```enter```.

The Bus Pirate will calculate the closest possible values and enable the PPSU.

{{% alert context="info" %}}
Press enter to accept the default values of 3.3 volts and 300mA current limit fuse.
{{% /alert %}}

### Quick enable

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> W 5 100
<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">5.00</span></span>V
<span style="color:#53a6e6">100.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">100.0</span></span>mA

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">Vreg output: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Current: <span style="color:#53a6e6">2.3</span></span>mA<span style="color:#bfa530">
</span>
{{< /term >}}

The ```W``` command accepts voltage and current as command line options. ```W 5 100``` is equivalent to the previous example.
- The first parameter specifies the voltage
- The second parameter specifies the current limit (omit for no current limit)

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> W 5
<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">5.00</span></span>V
<span style="color:#bfa530">Current limit:</span>300mA
{{< /term >}}

Omit the second parameter for the default 300mA current limit fuse.

## Check voltage and current

![](/images/docs/fw/psu-statusbar1a.png)

Check the voltage and current in the live view statusbar if active, or show the power supply voltage report using the ```v``` command followed by ```enter```.

- The top line indicates the power supply is set at 5.0 volts with a 100mA current limit. 
- The third line shows that 2.1mA is being consumed on VOUT/VREF. Since nothing is connected this is the power used by the IO pin buffers, current leakage, offset error and noise in the RP chip's analog to digital converter.
- The last line shows that VOUT currently measures 5.0 volts, and all IO pins measure 0 volts.

{{% alert context="warning" %}}
400mA is the rated maximum of the PPSU, but we added some headroom in the current limit to account for current spikes.
{{% /alert %}}

## Current limit

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> W 5 10
<span style="color:#53a6e6">5.00</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">5.00</span></span>V
<span style="color:#53a6e6">10.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">10.0</span></span>mA

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">Vreg output: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">5.0</span></span>V<span style="color:#bfa530">, Current: <span style="color:#53a6e6">2.3</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">I2C></span>
<span style="color:#bf3030">Error:<span style="color:#bfa530"> Current over limit, power supply disabled</span></span>

<span style="color:#96cb59">I2C></span> 
{{< /term >}}

When the programmed current limit is exceeded the PPSU hardware fuse disables the power supply. 
- The terminal colors invert repeatedly.
- An alarm bell sounds
- An error message is shown 
- Command execution is halted. 

Use the ```W``` command to restart the PPSU again, or the ```w``` command to disable.

{{% alert context="info" %}}
To test the current limit, set the current limit to 10mA, the connect a wire from the VOUT pin to the GND (pin). The Bus Pirate will disable the power supply when the current exceeds 10mA.
{{% /alert %}}

## Disable

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span>w
<span style="color:#bfa530"><span style="color:#bfa530">Power supply: </span></span>Disabled
<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Lowercase ```w``` disables the PPSU.
