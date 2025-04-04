+++
weight = 70900
title = 'Oscilloscope'
+++

![](/images/docs/fw/scope-cover.jpg)

The Bus Pirate can support an oscilloscope display mode - it's limited by the underlying
RP2040 chip to 0.5Msps so it's suitable for analog audio, not for high speed digital signals greater than 500KHz. Analog signals can be captured on any IO pin.

## Start the scope

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> d
<span style="color:#bfa530">Display selection
 1. Default
 2. Scope
 x. Exit</span>
<span style="color:#96cb59">Display ></span> 2
<span style="color:#bfa530">Display:</span> Scope
{{< /term >}}

The ```d``` command selects the LCD display mode. 
- Choose ```scope``` to load the oscilloscope on the Bus Pirate LCD
- You should see an oscilloscope show up on the Bus Pirate screen
- It's rotated 90 degrees from the normal orientation so we can show longer waveforms

## Display overview

![](/images/docs/fw/scope1a.jpg)

The display is small, to make the scope more useful we have a much larger capture buffer than the actual display and software scales the captured data to fit. The actual resolution is 0.5M samples per second. In the 100uS/div range that's one sample per pixel, any faster (50uS/div and below and samples are interpolated on the screen). If possible we try and capture up to 10 samples per pixel at whatever the current resolution is so that you can zoom into captured data at least 10 times (3 steps) before we start interpolating.

* The text '1V x 100uS' in the top right is the scale (voltage X time), the size of 1 yellow square on the screen. The default scale is "1V x 100uS" - 1 volt by 100 microseconds
* The text '0mS' in the top left is the offset (in time) of the left hand vertical yellow line
* The text '0V' in the bottom left is the offset (in volts) of the bottom yellow line
* The text 'PIN0' in the bottom right tells you which input pin is being sampled
* If the trigger point for the current trace is visible on the display then a small red arrow will appear at the trigger point at the top of the display

By default the screen displays 0V-5V in the vertical direction and 0uS to 640uS horizontally.
The data on the screen is a window into a larger display buffer. After taking a trace you can move around 
inside the buffer to explore different sections of the data.

## Commands

Controls are done from the command line, just like other Bus Pirate functions. There are 5 commands that can be entered:

* **sr {pin} {mode}** - Scope Run, optional capture {pin} (0-7) and/or {mode} ("o n a" Once, Normal, Auto)
* **ss** - Scope Stop
* **x** - Edit timebase (x axis)
* **y** - Edit voltage (y access)
* **t** - Edit trigger

All of these commands enter a more interactive UI where you can type single characters to navigate the captured data. You can skip back out to the normal UI by typing ```ENTER```.


### Scope Run

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> sr 2n  
{{< /term >}}

```sr {pin} {mode}``` ('scope run') starts the oscilloscope, you can specify additional parameters if you don't specify any it will use the previous settings. 

```{pin}``` is a single digit 0-7 to specify which Bus Pirate pin to capture.

```{mode}``` is 'o' 'n' or 'a' to specify which mode you want the display to work in:
- ```o``` ('once') will wait for a single trigger and stop
- ```n``` ('normal') will wait for a trigger, display the waveform and restart looking for the next trigger
- ```a``` ('auto') will wait for a trigger or a timeout (a second or so) whichever comes first and then restart, use this one to measure voltages

### Scope Stop

```ss``` ('scope stop') stops the scope 

### Scope Parameters
In addition there are 3 commands than can be used to alter parameters - these replace the knobs you'd find on a normal oscilloscope:

- ```x``` ('x axis' - timebase)
- ```y``` ('y axis' - voltage)
- ```t``` ('trigger' - trigger voltage and position)

These commands work a bit differently from normal Bus Pirate commands, you can use them two ways, either type the command along with some parameters and hit ```enter```, or just type the command and ```enter``` and you will pop into an interactive mode where you can type parameters to change things interactively on the display, typing ```enter``` again will return you to the main BusPirate prompt.

#### X/Y navigation
{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> x
Timebase: +- ^vT ty rsona> +-
<span style="color:#96cb59">LED-()></span> y
Voltage scale: +- ^vT tx rsona> +-
{{< /term >}}

Interactive parameters in x and y modes are:

- ```+```/```-``` in x mode increases or decreases the timebase scale - it changes the displayed scale but not the underlying data until the next time data is collected.
- ```+```/```-``` in y mode increases or decreases the voltage sensitivity (change the displayed scale)
- ```^```/```v```/```<```/```>``` or the equivalent arrow keys in x or y modes moves the display around within the currently collected data

#### Triggers

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> t
Trigger: +-*b ^vT BME xy rsona> 
{{< /term >}}

In Trigger mode
- ```+```/```-```/```b```/```n``` changes which edge triggers a data capture (positive going, negative going, both edges or no edges respectively)
- ```^```/```v``` or the equivalent arrow keys changes the voltage at which the trigger occurs
- ```<```/```>``` or the equivalent arrow keys moves the next trigger point around (chooses where in the next set of collected data the trigger will be)
- ```B```/```M```/```E``` moves the trigger point to the beginning/middle/end of the sample buffer

In trigger mode you will see a red crosshair that shows the time and voltage that the trigger occurs at,
there's also red test that describes it. If the crosshair is off the screen you'll see a red arrow
pointing at where it's located.

![](/images/docs/fw/scope2a.jpg)

In all 3 modes you can type:
- ```T``` moves the x display point to show the current trigger point
- ```r``` start run (like ```sr```)
- ```s``` stop the scope (like ```ss```)
- ```o``` start the scope in once mode (like ```sr o```)
- ```n``` start the scope in normal mode (like ```sr n```)
- ```a``` start the scope in auto mode (like ```sr a```)
- ```t``` switch to trigger mode
- ```x``` switch to x/timebase mode
- ```y``` switch to y/voltage mode
- ```enter``` leaves interactive mode

Note: commands that require a shift like + can also use their unshifted equivalents (= for +).

The general idea is that you switch into scope display mode with "d", start the scope running with something like "sr 2n" to sample from pin 2, use "t" to set up a trigger use "x" to get into interactive mode and +/- to set up timebase and the arrow keys to look at the result

## Quick Tutorial

Here's a quick start tutorial using only the Bus Pirate hardware. We're going to work on pin # 2, initially wagging it up and down and then setting up a clock.

### Setup

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> m

<span style="color:#bfa530">Mode selection</span>
 1. <span style="color:#bfa530">HiZ</span>
 2. <span style="color:#bfa530">1-WIRE</span>
 3. <span style="color:#bfa530">UART</span>
 4. <span style="color:#bfa530">I2C</span>
 5. <span style="color:#bfa530">SPI</span>
 6. <span style="color:#bfa530">LED</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Mode ></span> 6

<span style="color:#bfa530">LED type</span>
 1. <span style="color:#bfa530">WS2812/SK6812/'NeoPixel' (single wire interface)*</span>
 2. <span style="color:#bfa530">APA102/SK9822 (clock and data interface)</span>
 3. <span style="color:#bfa530">Onboard LEDs (16 SK6812s)</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59">Type (</span>1<span style="color:#96cb59">) ></span> 3
<span style="color:#bfa530">Mode:</span> LED
<span style="color:#96cb59">LED-()></span> W
<span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span>
<span style="color:#96cb59">x to exit (3.30) ></span> 
<span style="color:#53a6e6">3.30</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">3.30</span></span>V
Set current limit?
n 

<span style="color:#bfa530">Power supply:</span>Enabled
<span style="color:#bfa530">
Vreg output: <span style="color:#53a6e6">3.3</span></span>V<span style="color:#bfa530">, Vref/Vout pin: <span style="color:#53a6e6">3.3</span></span>V<span style="color:#bfa530">, Current sense: <span style="color:#53a6e6">2.4</span></span>mA<span style="color:#bfa530">
</span>
<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

Enter LED mode and enable a 3.3volt power supply:
- Enter a mode with the ```m``` command, select LED mode with onboard LEDs
- Set the I/O power supply to 3.3volts using the 'w' command (w ```enter``` ```enter``` n ```enter```)

### Enable Scope

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED></span> d
<span style="color:#bfa530">Display selection
 1. Default
 2. Scope
 x. Exit</span>
<span style="color:#96cb59">Display ></span> 2
<span style="color:#bfa530">Display:</span> Scope
{{< /term >}}

The ```d``` command selects the LCD display mode. 
- Type ```d``` and ```enter``` to configure the display mode
- Choose ```scope``` to load the oscilloscope on the Bus Pirate LCD
- You should see an oscilloscope on the Bus Pirate screen

![](/images/docs/fw/scope1a.jpg)

### Triggers

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> t
Trigger: +-*b ^vT BME xy rsona> b
<span style="color:#96cb59">LED-()></span> sr 2n  
{{< /term >}}

Set the trigger to 'both' edges and begin the scope capture on pin 2:
- Type ```t``` and ```enter``` to get into trigger mode. 
- Press ```b``` to set triggers on both the rising and falling edges, then ```enter``` to exit
- ```sr 2n``` then ```enter``` to start the scope on pin 2 in normal mode

The default trigger point is ~2.4volts.

![](/images/docs/fw/scope2a.jpg)

### Capture

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> P
<span style="color:#bfa530">Pull-up resistors:</span> Enabled (10K ohms @ <span style="color:#53a6e6">3.3</span>V)
<span style="color:#96cb59">LED-()></span> p
<span style="color:#bfa530">Pull-up resistors:</span> Disabled
<span style="color:#96cb59">LED-()></span>
{{< /term >}}

Now we'll use the pull-up resistors to trigger the scope:
- ```P``` and ```enter``` to turn **on** the pull-up resistors. You should see a trace with a rising edge
- ```p``` and ```enter``` to turn **off** the pull-up resistors. You should see a nice exponential decay curve on the scope as pin 2's capacitance discharges

![](/images/docs/fw/scope3a.jpg) ![](/images/docs/fw/scope4a.jpg)

### Edge triggers

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> P
<span style="color:#bfa530">Pull-up resistors:</span> Enabled (10K ohms @ <span style="color:#53a6e6">3.3</span>V)
<span style="color:#96cb59">LED-()></span> t
Trigger: +-*b ^vT BME xy rsona> +
<span style="color:#96cb59">LED-()></span> p
<span style="color:#bfa530">Pull-up resistors:</span> Disabled
<span style="color:#96cb59">LED-()></span> P
<span style="color:#bfa530">Pull-up resistors:</span> Enabled (10K ohms @ <span style="color:#53a6e6">3.3</span>V)
<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

The scope can be triggered by the rising or falling edge of a signal, or both:
- ```P``` and ```enter``` to turn **on** the pull-up resistors again. 
- ```t``` and ```enter``` to configure the trigger. Type ```+``` to trigger only on rising edges, then ```enter``` to leave trigger mode
- ```p``` and ```enter``` to turn **off** the pull-up resistors. This time the scope doesn't capture because the signal is a falling edge
- ```P``` and ```enter``` to turn **on** the pull-up resistors again. The scope is triggered by the rising edge.

### Navigation

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> G 2
<span style="color:#bfa530">Generate frequency</span>
<span style="color:#bfa530">Choose available pin:</span>
 2. IO<span style="color:#53a6e6">2</span>
 3. IO<span style="color:#53a6e6">3</span>
 4. IO<span style="color:#53a6e6">4</span>
 5. IO<span style="color:#53a6e6">5</span>
 6. IO<span style="color:#53a6e6">6</span>
 7. IO<span style="color:#53a6e6">7</span>
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 2
<span style="color:#96cb59">Period or frequency (ns, us, ms, Hz, KHz or Mhz) ></span> 1ms
<span style="color:#bfa530">Frequency:</span> <span style="color:#53a6e6">1.000</span>ms = <span style="color:#53a6e6">1000</span>Hz (<span style="color:#53a6e6">1000.00</span>Hz)
<span style="color:#bfa530">Period:</span> <span style="color:#53a6e6">1000000</span>ns (<span style="color:#53a6e6">1.00</span>ms)

<span style="color:#bfa530">Actual frequency:</span> <span style="color:#53a6e6">1000</span>Hz (<span style="color:#53a6e6">1.00</span>KHz)
<span style="color:#bfa530">Actual period:</span> <span style="color:#53a6e6">999998</span>ns (<span style="color:#53a6e6">1000.00</span>us)

<span style="color:#96cb59">Duty cycle (%) ></span> 33%
<span style="color:#bfa530">Duty cycle:</span> <span style="color:#53a6e6">33.00</span>% = <span style="color:#53a6e6">329999</span>ns (<span style="color:#53a6e6">330.00</span>us)
<span style="color:#bfa530">Actual duty cycle:</span> <span style="color:#53a6e6">330000</span>ns (<span style="color:#53a6e6">330.00</span>us)
Divider: 31, Period: 64515, Duty: 21290

<span style="color:#bfa530">Generate frequency:</span> Enabled on IO<span style="color:#53a6e6">2</span>

<span style="color:#96cb59">LED-()></span> 
{{< /term >}}

Next let's try something more involved, let's set up a square wave on pin 2.
- Generate a frequency on pin 2 (G 2 ```enter``` 1ms ```enter``` 33% ```enter```)

#### Time scale

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> x
Timebase: +- ^vT ty rsona> +-
{{< /term >}}

You should see the display showing a square wave. The capture buffer is large. We can zoom and pan to navigate the data:
- ```x``` and ```enter``` to scale the X axis (time). 
- You should see a bunch of square waves, try ```+``` and ```-``` to change the scale, and the left and right arrows to move around. Freeze a trace with ```o```

![](/images/docs/fw/scope5a.jpg) 

Note you are now in interactive mode - try the ```-``` command a few times and see that you can zoom out from the current display and the ```+``` zooms in, ```<``` and ```>``` let you more right and left within the display.


#### Voltage scale

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">LED-()></span> y
Voltage scale: +- ^vT tx rsona> +-
{{< /term >}}


Type ```y``` on the command line **or** in the x or t interactive mode type. Now you are in 'voltage mode'. ```+``` will zoom in vertically and ```^```/```v``` will let you scroll up and down.
- ```y``` and ```enter``` to scale the Y axis (volts).
- Change the voltage scale with ```+``` and ```-```, and use the up down arrows to move the display

![](/images/docs/fw/scope6a.jpg)

Scroll back to the beginning and use ```-``` zoom out to 1v/div. Now type ```t``` to go into trigger  mode - you'll see a red crosshair showing the trigger voltage and time, and their actual values in red at the top right, you can edit them using the arrow keys, you can also change the trigger type using +-bn - try typing ```-``` and seeing how the display changes. 

Let's move the trigger point to the middle of the capture buffer - type ```M``` and notice how the red vertical line is replaced by a small red arrow pointing right, you can type ```T``` to center the display on the new trigger point. ```BT``` will put it back.

## Limitations and bugs

We're very much limited by the hardware:

* 500k samples per second is the maximum speed of the RP2040 ADC
* 12 bits 
* Tiny display
* No way to make a dual scope (we might be able to have a digital trigger in the future)
