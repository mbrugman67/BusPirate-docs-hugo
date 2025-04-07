+++
title = "Change Binary Interface"
description = "Access logic analyzers, programmers, and more"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 80100
+++

{{< term "Bus Pirate [/dev/ttyS0]" >}}
<span style="color:#96cb59">HiZ></span> binmode

<span style="color:#bfa530">Select binary mode</span>
 1. SUMP logic analyzer
 2. Binmode test framework
 3. Arduino CH32V003 SWIO
 4. Follow along logic analyzer
 5. Legacy Binary Mode for Flashrom and AVRdude (EXPERIMENTAL)
 x. <span style="color:#bfa530">Exit</span>
<span style="color:#96cb59"> ></span> 1
<span style="color:#bfa530">Binmode selected:</span> SUMP logic analyzer

<span style="color:#96cb59">HiZ></span> 
{{< /term >}}

The Bus Pirate has two USB serial ports. One is used for the command line terminal. The other can be configured to use various protocols that support software running on a PC.  

- [SUMP logic analyzer protocol]({{< relref "protocol-sump" >}})
- [Binmode test framework](https://forum.buspirate.com/t/bbio2-binary-mode/219/10?u=ian)
- Arduino CH32V003 SWIO
- [Follow Along Logic Analyzer protocol]({{< relref "protocol-faladata" >}}) 
- [Legacy Binary Mode for Flashrom and AVRdude]({{< relref "/docs/software/avrdude" >}})

Use the ```binmode``` command see the currently supported binary modes and to select the active binary mode.