+++
title = "Change Binary Mode"
description = "Access logic analyzers, programmers, and more"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 100
+++

import DiscourseComments from '@site/src/components/DiscourseComments';
import BrowserWindow from '@site/src/components/BrowserWindow';

# Binary Interfaces

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">HiZ></span> binmode<br/>
<br/>
<span className="bp-info">Select binary mode</span><br/>
 1. SUMP logic analyzer<br/>
 2. Binmode test framework<br/>
 3. Arduino CH32V003 SWIO<br/>
 4. Follow along logic analyzer<br/>
 5. Legacy Binary Mode for Flashrom and AVRdude (EXPERIMENTAL)<br/>
 x. <span className="bp-info">Exit</span><br/>
<span className="bp-prompt"> ></span> 1<br/>
<span className="bp-info">Binmode selected:</span> SUMP logic analyzer<br/>
<br/>
<span className="bp-prompt">HiZ></span> 
{{% /term %}}

The Bus Pirate has two USB serial ports. One is used for the command line terminal. The other can be configured to use various protocols that support software running on a PC.  

- [SUMP logic analyzer protocol](/binmode-reference/protocol-sump)
- [Binmode test framework](https://forum.buspirate.com/t/bbio2-binary-mode/219/10?u=ian)
- Arduino CH32V003 SWIO
- [Follow Along Logic Analyzer protocol](/binmode-reference/protocol-fala)
- [Legacy Binary Mode for Flashrom and AVRdude](/software/avrdude)

Use the ```binmode``` command see the currently supported binary modes and to select the active binary mode.