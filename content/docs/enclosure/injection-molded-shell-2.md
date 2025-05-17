+++
weight = 120401
title = 'Injection Molded Shell v2'
+++

![](/images/docs/enclosure/enclosure-v2.jpeg)  

## Updates to enclosure v2

After our first [disastrous attempt at injection molding]({{< relref "/docs/enclosure/injection-molded-shell/">}}), we decided to try again with a new factory. In addition to filling the abandoned SD card slot, we made a few other tweaks to the design.
- **The Plug** - The Bus Pirate doesn't have an SD card slot, but the enclosure was designed to fit one. We've been SLA printing a plug to fill the hole. That's fixed in enclosure v2.
- **Rounded corners** - The corners of the enclosure are now rounded. This is a minor aesthetic change, but it makes the case look a bit more polished and the LED effect is more pronounced.
- **Proper bosses** - In enclosure v1 thick corners were used for the insert nuts, leading to injection molding problems. The new design has proper bosses for the insert nuts, which should make the injection molding process easier and more reliable.
- **Improved auxiliary connector access** - We cut a bunch of plastic away from the auxiliary connector area. It is not possible to pry the connector out, instead of yanking on the wires. 
- **Indents for silicone feet** - The new design has indents for silicone feet on the bottom. 3M brand silicone feet are included with the enclosure. They are not installed in the factory, but they are included in the bag of accessories.
- **Bootloader hole is an insert** - The bootloader hole is now a mold insert, and it can be moved if we need to change the location of the bootloader button in the future. 

The [case was developed](https://forum.buspirate.com/t/injection-molded-enclosure-v2/693) in the forum with lots of feedback from the community. We're super proud of the new enclosure.

## Components

The encloser has three main components:
- **Polypropylene shell** - The top and bottom shells are injection molded in clear-ish polypropylene (PP) plastic with a bit of titanium dioxide for color.
- **M3 brass insert nuts** - Nuts that hold the halves together are inserted into the mold during manufacturing. 
- **M3 7mm DIN7991 bolts** - The bolts are used to hold the two halves of the enclosure together. 

### Polypropylene Shell

![](/images/docs/enclosure/enclosure2-b.jpeg)
![](/images/docs/enclosure/enclosure2-a.jpeg)

|**Reference**  |**Value**|**Quantity**|**Rating**  |**Note**|
|-|-|-|-|-|
|Top shell  ||1  ||Clear PP|
|Bottom shell||1||Clear PP|

Top and bottom enclosure injection molded in clear-ish polypropylene (PP) plastic with a bit of titanium dioxide for color. 

- [Enclosure top STL](https://github.com/DangerousPrototypes/BusPirate5-hardware/blob/main/enclosure/BusPirate-enclosure-v2-a.stl)
- [Enclosure bottom STL](https://github.com/DangerousPrototypes/BusPirate5-hardware/blob/main/enclosure/BusPirate-enclosure-v2-b.stl)

### M3 brass insert nuts

![](/images/docs/enclosure/enclosure2-nuts.jpeg)

|**Reference**|**Package**|**Value**|**Quantity**|**Rating**|**Note**|
|-|-|-|-|-|-|
|Nuts  |M3x3mmLx4.0mmD|M3 brass insert nut  |4  ||Should be 4mm height|

Brass insert nuts for injection molding. Nuts are placed into the tooling before each case is injection molded. This is labor intensive, leads to scheduling problems and the results vary.

### M3 7mm DIN7991 bolt
  
![](/images/docs/enclosure/din7991.png)

|**Reference**|**Package**|**Value**|**Quantity**|**Rating**|**Note**|
|-|-|-|-|-|-|
|Bolts|M3x**7mm** DIN7991|M3 **7mm** bolt DIN7991 silver|4||Silver color|

**7mm** bolts are a non-standard size. 

{{% alert context="danger" %}}
Bolts should be finger tight. Over tightening bolts may pull the insert nut out of the case, or crush the LCD.
{{% /alert %}}

{{% alert context="info" %}}
The 3D printable versions of the enclosure work with standard 8mm DIN7991 bolts, only the injection molded version specifies 7mm bolts. 8mm bolts will work, but some heads may not sit fully flush with the front of the case. 
{{% /alert %}}

## Get a Bus Pirate
 

{{% readfile "/_common/_footer/_footer-get.md" %}}
