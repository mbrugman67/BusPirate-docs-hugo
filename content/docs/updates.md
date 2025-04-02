+++
title = "Theme Updates"
description = ""
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 1
+++

## Console

![](images/docs/cmd-toolbar.png)

With `style`:

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span style="color:#96cb59">I2C></span>
<span style="color:#96cb59">I2C></span>
<span style="color:#96cb59">I2C></span> W
<span style="color:#bfa530"><span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span></span>
<span style="color:#96cb59">x to exit (3.30) ></span>
<span style="color:#53a6e6">3.30</span>V<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">3.30</span></span>V
Set current limit?
y D

<span style="color:#bfa530">Maximum current (0mA-500mA)</span>
<span style="color:#96cb59">x to exit (100.00) ></span> 2
<span style="color:#53a6e6">2.0</span>mA<span style="color:#bfa530"> requested, closest value: <span style="color:#53a6e6">2.0</span></span>mA
<span style="color:#bf3030">Error:<span style="color:#bfa530"> Current over limit, power supply disabled</span></span>

a<span style="color:#96cb59">I2C></span>
<span style="color:#96cb59">I2C></span>
{{% /term %}}

With `class`:

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span class="bp-prompt">HiZ></span> i<br/>
<span class="bp-info"><br/>
Bus Pirate 5 REV6<br/>
Firmware 
<span class="bp-float">v0.1</span>

</span> 
(<span class="bp-float">unknown</span>), Bootloader 
<span class="bp-float">N/A</span>
<br/>
{{% /term %}}

{{% alert icon="❓" context="danger" %}}
QUESTION

Should we create a different shortcode to process the `class` version? The
format looks a bit broken, but I'm not sure this is how it should look. Also,
maybe automatically replace `className` with `class` in the shortcode?
{{% /alert %}}

Nice looking console view, and light/dark modes work great.
- Disable any syntax highlighting
- Enable HTML formatting. 

### Console HTML formatting

The color text output from our device is processed from VT100 to HTML. There are two ways to handle the color in docs.

```html
<span style="color:#96cb59">I2C></span>
<span style="color:#96cb59">I2C></span>
<span style="color:#96cb59">I2C></span> W
<span style="color:#bfa530"><span style="color:#bfa530">Power supply
Volts (0.80V-5.00V)</span></span>
<span style="color:#96cb59">x to exit (3.30) ></span>
```
This is the raw output of a NodeJS converter script. The colors are hex color codes inserted in the stype tag.

```html
<span className="bp-prompt">HiZ></span> i<br/>
<span className="bp-info"><br/>
Bus Pirate 5 REV6<br/>
Firmware 
<span className="bp-float">v0.1</span>

</span> 
(<span className="bp-float">unknown</span>), Bootloader 
<span className="bp-float">N/A</span>
<br/>
```

For docusaurus we have an annoying two step process. The colors are replaced by className and the class names are added to docusaurus CSS.

```css
.bp-prompt{ color:#96cb59;} 
.bp-info{ color:#bfa530;} 
.bp-error{ color:#bf3030;} 
.bp-float{ color:#53a6e6;}

.bp-pre{
	color: #FFFFFF;
}
```

These are the HTML classes for this method (not preferred).

## Header
If at all possible some links on the header for desktop view, same as old site

## Footer
Is it possible to add a footer in desktop and mobile, similar to the old site?

## Responsive images
Are the responsive images enabled?

## Root directory
The site will have it’s own subdomain  http://docs.buspirate.com, so it would be ideal if it wasn’t served from /docs/. If that is difficult or breaks things, then I’ll live with it :)

## Landing page
Please disable the landing/home page and use one of the docs pages instead. (I don’t know what this entails, in Docusaurus I just change a configuration setting to make https://firmware.buspirate.com/ show the overview doc.

