+++
weight = 30400
title = 'Programmable Power Supply'
+++

![](/images/docs/fw/ppsu-1024.jpg)

## Features
Bus Pirate 5 has a single 'Programmable Power Supply Unit' (PPSU) that can power devices from the VOUT/VREF pin of the main connector.

- 1-5volts adjustable output, 400mA max
- 0-500mA current sense 
- 0-500mA current limit with digital fuse
- Backflow prevention to protect the PPSU when an external voltage is applied to the VREF/VOUT pin

## Enable
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span> W
<span style="color:#bfa530"><span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span></span>
<span style="color:#96cb59">x to exit (3.30) ></span> 2.1
<span style="color:#53a6e6">2.10</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">2.10</span></span>V
Set current limit?
y

<span style="color:#bfa530">Maximum current (0mA-500mA)</span>
<span style="color:#96cb59">x to exit (100.00) ></span> 50
<span style="color:#53a6e6">50.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">50.0</span></span>mA

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">
Vreg output: <span style="color:#53a6e6">2.1</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">2.1</span></span>V<span style="color:#bfa530">, Current sense: <span style="color:#53a6e6">7.3</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Type uppercase ```W``` followed by ```enter``` to enable the power supply. 

- Enter the desired output in volts, for example ```2.1``` followed by ```enter```.
- Press ```y``` and ```enter``` to enable the current limit system.
- Enter the desired current limit in milliamps, for example ```50``` followed by ```enter```.

The Bus Pirate will calculate the closest possible values and enable the PPSU.

{{% alert context="info" %}}
Enter any protocol mode (```m```) to use the power supply. The power supply is always disabled in HiZ safe mode.
{{% /alert %}}

## Check voltage and current

![](/images/docs/fw/ppsu-vreport.png)

Check the voltage and current in the live view statusbar if active, or show the power supply voltage report using the ```v``` command followed by ```enter```.

- The top line indicates the power supply is set at 2.1volts with a 50mA current limit. 
- The third line shows that 9.2mA is being consumed on VOUT/VREF. Since nothing is connected this is the current leakage, offset error and noise in the RP2040 analog to digital converter.
- The last line shows that VOUT currently measures 2.1volts, and other pins measure 0 volts.

{{% alert context="info" %}}
The difference in voltages (2.1, 2.19) is due to some code inconsistencies in float handling. It will be fixed shortly. 
{{% /alert %}}

{{% alert context="warning" %}}
400mA is the rated maximum of the PPSU, but we added some headroom in the current limit to account for current spikes.
{{% /alert %}}

## Current limit

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#bf3030">Error:<span style="color:#bfa530"> Current over limit, power supply disabled</span></span>

<span style="color:#96cb59">I2C></span> 
{{< /term >}}

When the programmed current limit is exceeded the PPSU hardware fuse disables the power supply. The terminal colors invert repeatedly, an alarm bell will sound, an error message is shown and command execution is halted. Use the ```W``` command to restart the PPSU again.

## Disable

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">I2C></span>w
<span style="color:#bfa530"><span style="color:#bfa530">Power supply: </span></span>Disabled
<span style="color:#96cb59">I2C></span> 
{{< /term >}}

Lowercase ```w``` disables the PPSU.
