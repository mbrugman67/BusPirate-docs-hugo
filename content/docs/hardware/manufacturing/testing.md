+++
weight = 11
title = 'Testing'
+++
import BrowserWindow from '@site/src/components/BrowserWindow';

# Testing

Every Bus Pirate is lovingly tested by our crack team before it ships. The Bus Pirate firmware has a self-test that will help make sure no failed components are on the board before we ship.

## Start the self-test

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-prompt">HiZ></span> ~
<span className="bp-info">SELF TEST STARTING</span>
{{% /term %}}

- Type ```~``` followed by ```enter```.

## Press button when prompted
{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-info">
PUSH BUTTON TO COMPLETE: OK
</span>
{{% /term %}}

- Press the Bus Pirate button to complete the test. The Bus Pirate will pause and wait indefinitely. 

## Results

### Success

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-info">

PASS :)
</span>
<span className="bp-prompt">HiZ></span> 
{{% /term %}}

### Error

{{% term "Bus Pirate [/dev/ttyS0]" %}}
<span className="bp-info">
PSU: CODE 3. ERROR!
...
ERRORS: 1
FAIL! :(</span>
{{% /term %}}
