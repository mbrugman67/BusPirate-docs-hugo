+++
title = "BPIO2 FlatBuffers Interface"
description = "Bus Pirate FlatBuffers Interface (BPIO2) protocol documentation"
icon = "article"
date = "2023-05-22T00:27:57+01:00"
lastmod = "2023-05-22T00:27:57+01:00"
draft = false
toc = true
weight = 80505
+++

{{% alert context="danger" %}}
Work in progress documenting the BPIO2 protocol.
{{% /alert %}}

The Bus Pirate BPIO2 binmode is a [FlatBuffers](https://flatbuffers.dev/) interface designed for simple and complete control of the Bus Pirate hardware from an application or script. It allows for sending and receiving data in a structured format, enabling various operations such as reading and writing to GPIO pins, controlling peripherals, and more.

Pre-compiled BPIO2 FlatBuffer "tooling" is available for 15 common languages. This means you can easily integrate the BPIO2 protocol into your projects without needing to write extensive parsing or serialization code.

- [Python Library](#python-library) - A demonstration library for interacting with BPIO2 
- [Debugging](#debugging) - Display BPIO2 debug information in the Bus Pirate terminal
- [FlatBuffer Tooling Download](#flat-buffer-tooling-download) - Download precompiled FlatBuffer tooling for BPIO2 in 15 languages
- [Compile your own tooling](#compiling-your-own-tooling) - How to generate your own tooling from the BPIO2 schema
- [Schema](#schema) - Explanation of the low level flatbuffer tables used in BPIO2

## Why BPIO2?

Bus Pirate v3.x has a **BBIO1** interface, an abbreviation for **Bit Bang Input/Output**. The interface was originally designed for simple bit-banging only, other protocols were hacked in later. If I may say so, it was a bit of a mess. 

We *could* call this BBIO2, but it's in no way similar to the original BBIO1 interface and it's only marginally for bit-banging. Instead, we call it BPIO2 meaning the second generation of Bus Pirate I/O.

## Python Library

[Download the BPIO2 Python library and examples](https://github.com/DangerousPrototypes/BusPirate-BBIO2-flatbuffer-interface/tree/main/python):
- `/` - Example Python scripts for BPIO2
- `/pybpio/` - Python library for BPIO2
- `/tooling/` - FlatBuffer generated Python tooling
- `/flatbuffers/` - FlatBuffer library for Python

### Install

In addition to Python 3 or later, pyserial and COBS are required to use the BPIO2 library. You can install them using pip:

```bash
pip3 install -r requirements.txt
```

### Client Show Status

The BPIO2 client has a `show_status()` method that sends a `StatusRequest` to the Bus Pirate and prints the `StatusResponse`.

1. Import the BPIOClient class from the bpio_client module.
2. Create an instance of the BPIOClient class, passing the serial port as an argument.
3. Call the `show_status()` method to retrieve and print the status of the Bus Pirate.

```python
>>> from bpio_client import BPIOClient
>>> client = BPIOClient("COM35")
>>> client.show_status()
StatusResponse:
  Hardware version: 5 REV10
  Firmware version: 0.0
  Firmware git hash: unknown
  Firmware date: Aug 14 2025 14:11:17
  Available modes: HiZ, 1WIRE, UART, HDUART, I2C, SPI, 2WIRE, 3WIRE, DIO, LED, INFRARED, JTAG
  Current mode: 1WIRE
  Mode bit order: MSB
  Pin labels: ON, OWD, , , , , , , , GND
  Number of LEDs: 18
  Pull-up resistors enabled: True
  Power supply enabled: True
  PSU set voltage: 3299 mV
  PSU set current: 300 mA
  PSU measured voltage: 3295 mV
  PSU measured current: 6 mA
  PSU over current error: No
  IO ADC values (mV): 2321, 2309, 2320, 2320, 2341, 2338, 2339, 2347
  IO directions: IO0:IN, IO1:IN, IO2:IN, IO3:IN, IO4:IN, IO5:IN, IO6:IN, IO7:IN
  IO values: IO0:HIGH, IO1:HIGH, IO2:HIGH, IO3:HIGH, IO4:HIGH, IO5:HIGH, IO6:HIGH, IO7:HIGH
  Disk size: 97.69779205322266 MB
  Disk space used: 0.0 MB
```
### Client Get Status

You can also get the status as a dictionary, and access the individual fields.

```python
>>> from bpio_client import BPIOClient
>>> client = BPIOClient("COM35")
>>> status = client.status_request()
>>> print(status['error'])
None
```
{{% alert context="info" %}}
The ```error``` field will be populated if there is an error in the request. If the request is successful, it will be `None`.
{{% /alert %}}

```python 
>>> print(status)
{'error': None, 
'hardware_version_major': 5, 
'hardware_version_minor': 10, 
'firmware_version_major': 0, 
'firmware_version_minor': 0, 
'firmware_git_hash': 'unknown', 
'firmware_date': 'Aug 14 2025 14:11:17', 
'modes_available': ['HiZ', '1WIRE', 'UART', 'HDUART', 'I2C', 'SPI', '2WIRE', '3WIRE', 'DIO', 'LED', 'INFRARED', 'JTAG'], 
'mode_current': '1WIRE', 
'mode_pin_labels': ['ON', 'OWD', '', '', '', '', '', '', '', 'GND'], 
'mode_bitorder_msb': True, 
'psu_enabled': True, 
'psu_set_mv': 3299, 
'psu_set_ma': 300, 
'psu_measured_mv': 3300, 
'psu_measured_ma': 3, 
'psu_current_error': False, 
'pullup_enabled': True, 
'pullx_config': 0, 
'adc_mv': [3279, 3287, 3303, 3316, 3314, 3304, 3300, 3295], 
'io_direction': 0, 
'io_value': 255, 
'disk_size_mb': 97.69779205322266, 
'disk_used_mb': 0.0, 
'led_count': 18}
```

### Mode Change

Each mode has a Python class to interact with the Bus Pirate in that mode. You can change the mode by creating an instance of the class for that mode. You can also configure the mode and other hardware during configuration.

```python
>>> from bpio_client import BPIOClient
>>> from bpio_i2c import BPIOI2C
>>> client = BPIOClient("COM35")
>>> i2c = BPIOI2C(client)
>>> i2c.configure(speed=400000, pullup_enable=True, psu_enable=True, psu_voltage_mv=3300, psu_current_ma=0)
True
>>>
```

Create a new instance of the `BPIOI2C` class, passing the BPIO2 client connection as an argument.

```python
i2c.configure(speed=400000, pullup_enable=True, psu_enable=True, psu_voltage_mv=3300, psu_current_ma=0)
```

The `configure()` function accepts arguments for the mode configuration and other hardware settings. Here we set the I2C speed to 400kHz, enable pull-ups, and set the power supply for 3.3volt with no current limit. The method returns `True` if the configuration was successful, or `False` if there was an error.

Mode configuration arguments are generic for all modes, and correspond to the FlatBuffer mode configuration table names:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `speed` | uint32 | 20000 | Speed in Hz or baud for the mode |
| `data_bits` | uint8 | 8 | Data bits for the mode (e.g., 8 for UART) |
| `parity` | bool | false | Parity for the mode (true for even parity, false for no parity) |
| `stop_bits` | uint8 | 1 | Stop bits for the mode (1 or 2) |
| `flow_control` | bool | false | Flow control for the mode (true for enabled, false for disabled) |
| `signal_inversion` | bool | false | Signal inversion for the mode (true for inverted, false for normal) |
| `clock_stretch` | bool | false | Clock stretching for I2C mode (true for enabled, false for disabled) |
| `clock_polarity` | bool | false | Clock idle polarity for SPI mode (true for high, false for low) |
| `clock_phase` | bool | false | Clock phase for SPI mode (false for leading edge, true for trailing edge) |
| `chip_select_idle` | bool | true | Chip select idle state for SPI and 3-wire modes (true for idle high, false for idle low) |
| `submode` | uint8 | - | Submode for LED and INFRARED modes (e.g., "RGB", "IR TX", "IR RX") |
| `tx_modulation` | uint32 | - | TX modulation frequency for INFRARED mode |
| `rx_sensor` | uint8 | - | RX sensor configuration for INFRARED mode|

Other hardware can be configured at the same time as the mode change, for example power supply, and pull-up resistors. The parameters are also identical to the FlatBuffer configuration request table names:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mode_bitorder_msb` | bool | - | Bit order MSB |
| `mode_bitorder_lsb` | bool | - | Bit order LSB |
| `psu_disable` | bool | - | Disable power supply |
| `psu_enable` | bool | - | Enable power supply |
| `psu_set_mv` | uint32 | - | Set voltage in millivolts (psu_enable must = true) |
| `psu_set_ma` | uint16 | 300 | Set current in milliamps, 0 for unlimited (psu_enable must = true) |
| `pullup_disable` | bool | - | Disable pull-up resistors |
| `pullup_enable` | bool | - | Enable pull-up resistors |
| `io_direction_mask` | uint8 | - | Bitmask for IO pin directions (1=modify this pin) |
| `io_direction` | uint8 | - | IO pin directions in 8 bit byte (1 output, 0 input) |
| `io_value_mask` | uint8 | - | Bitmask for IO pin values (1=modify this pin) |
| `io_value` | uint8 | - | IO pin values in 8 bit byte (1 high, 0 low) |
| `led_resume` | bool | - | Resume LED effect after setting with led_color |
| `led_color` | [uint32] | - | LED colors in RGB format (0xRRGGBB) |
| `print_string` | string | - | String to print on terminal |

### Mode Getter Methods

Each mode class inherits getter methods from the BPIOBase class to query Bus Pirate status information. These methods provide access to specific hardware and firmware details without needing to parse the full status dictionary.

#### Get All Status Info
{{% alert context="danger" %}}
Each call to a getter method sends a request to the Bus Pirate and waits for a response. This can be slow. If you need a lot of status info it's faster to use `get_status()` which retrieves all status information in one go, and then access the specific fields from the returned dictionary.
{{% /alert %}}

```python
>>> status = i2c.get_status()
>>> print(status['mode_current'])
I2C
```

{{% alert context="info" %}}
The mode ```get_status()``` method returns a dictionary with all status information for the current mode. This is the same DICT returned by the `client.status_request()` method. Each mode also has a `show_status()` method that prints the status in a human-readable format for debugging.
{{% /alert %}}

#### Version Information

| Method | Returns | Description |
|--------|---------|-------------|
| `get_hardware_version_major()` | int | Hardware version major number |
| `get_hardware_version_minor()` | int | Hardware revision number |
| `get_firmware_version_major()` | int | Firmware version major number |
| `get_firmware_version_minor()` | int | Firmware version minor number |
| `get_firmware_git_hash()` | string | Git hash of the firmware build |
| `get_firmware_date()` | string | Date and time of firmware build |

#### Mode Information

| Method | Returns | Description |
|--------|---------|-------------|
| `get_modes_available()` | list | Array of all available mode names |
| `get_mode_current()` | string | Name of the currently active mode |
| `get_mode_pin_labels()` | list | Array of pin labels for current mode |
| `get_mode_bitorder_msb()` | bool | Current bit order (True for MSB first) |

#### Power Supply Status

| Method | Returns | Description |
|--------|---------|-------------|
| `get_psu_enabled()` | bool | Whether power supply is enabled |
| `get_psu_set_mv()` | int | Set voltage in millivolts |
| `get_psu_set_ma()` | int | Set current limit in milliamps |
| `get_psu_measured_mv()` | int | Measured voltage in millivolts |
| `get_psu_measured_ma()` | int | Measured current in milliamps |
| `get_psu_current_error()` | bool | Over-current error status |

#### Hardware Status

| Method | Returns | Description |
|--------|---------|-------------|
| `get_pullup_enabled()` | bool | Whether pull-up resistors are enabled |
| `get_pullx_config()` | int | Pull-x configuration for BP7+ |
| `get_adc_mv()` | list | ADC measurements for each IO pin in mV |
| `get_io_direction()` | int | IO pin directions bitmask (1=output, 0=input) |
| `get_io_value()` | int | IO pin values bitmask (1=high, 0=low) |
| `get_led_count()` | int | Number of LEDs on the device |

#### Storage Information

| Method | Returns | Description |
|--------|---------|-------------|
| `get_disk_size_mb()` | float | Total disk size in megabytes |
| `get_disk_used_mb()` | float | Used disk space in megabytes |

#### Usage Examples

```python
>>> i2c = BPIOI2C(client)
>>> print(f"Hardware: {i2c.get_hardware_version_major()}.{i2c.get_hardware_version_minor()}")
Hardware: 5.10
>>> print(f"Current mode: {i2c.get_mode_current()}")
Current mode: I2C
>>> print(f"PSU voltage: {i2c.get_psu_measured_mv()}mV")
PSU voltage: 3300mV
>>> print(f"IO directions: {i2c.get_io_direction():08b}")
IO directions: 00000000
```

All getter methods return `None` if there is an error or if the Bus Pirate is not properly configured.

#### Remove Pull-x for now
#### max (packet size)
#### Query to increase speed and reduce packet size


### Mode Setter Methods

Each mode class inherits setter methods from the BPIOBase class to configure Bus Pirate hardware settings. These methods allow you to modify individual configuration parameters without needing to reconfigure the entire mode.

#### Bit Order Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_mode_bitorder_msb()` | None | Set mode bit order to MSB (Most Significant Bit) first |
| `set_mode_bitorder_lsb()` | None | Set mode bit order to LSB (Least Significant Bit) first |

#### Power Supply Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_psu_disable()` | None | Disable the Bus Pirate power supply |
| `set_psu_enable(voltage_mv, current_ma)` | `voltage_mv` (int, default=3300)<br>`current_ma` (int, default=300) | Enable power supply with specified voltage and current limit |

{{% alert context="info" %}}
Power supply voltage is specified in millivolts, current in milliamps. If you set the current to 0, it will be unlimited.
{{% /alert %}}

#### Pull-up Resistor Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_pullup_disable()` | None | Disable pull-up resistors |
| `set_pullup_enable()` | None | Enable pull-up resistors |

#### IO Pin Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_io_direction(direction_mask, direction)` | `direction_mask` (int)<br>`direction` (int) | Set IO pin directions (1=output, 0=input) |
| `set_io_value(value_mask, value)` | `value_mask` (int)<br>`value` (int) | Set IO pin values (1=high, 0=low) |

{{% alert context="info" %}}
For IO operations, use bitmasks to specify which pins to modify. For example, to set pin 7 as output and drive it high, use `set_io_direction(0x80, 0x80)` and `set_io_value(0x80, 0x80)`.
{{% /alert %}}

#### LED Control

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_led_resume()` | None | Resume LED effect after configuration |
| `set_led_color(colors)` | `colors` (list) | Set LED colors in RGB format (0xRRGGBB) |

#### Utility Functions

| Method | Parameters | Description |
|--------|------------|-------------|
| `set_print_string(string)` | `string` (str) | Print string on Bus Pirate terminal |
| `set_hardware_bootloader()` | None | Enter bootloader mode |
| `set_hardware_reset()` | None | Perform hardware reset of the device |

#### Usage Examples

```python
# Enable power supply at 5V with 500mA limit
>>> i2c.set_psu_enable(voltage_mv=5000, current_ma=500)
True

# Set IO pin 7 as output and drive it high
>>> i2c.set_io_direction(direction_mask=0x80, direction=0x80)
True
>>> i2c.set_io_value(value_mask=0x80, value=0x80)
True

# Set all LEDs to red
>>> i2c.set_led_color([0xFF0000] * 18)
True

# Print debug message
>>> i2c.set_print_string("Debug: I2C configured")
True
```

All setter methods return `True` if successful, `False` if there was an error, or `None` if not configured
 
### I2C Data

The `BPIOI2C` class provides methods for I2C communication, inheriting from the `BPIOBase` class for configuration and status functionality.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(speed, clock_stretch, **kwargs)` | `speed` (int, default=400000)<br>`clock_stretch` (bool, default=False)<br>`**kwargs` (additional config) | Configure I2C mode with specified speed and clock stretching |

{{% alert context="info" %}}
Speed is specified in Hz (e.g., 400000 for 400kHz).
{{% /alert %}}  

#### I2C Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `start()` | None | Send I2C start condition |
| `stop()` | None | Send I2C stop condition |
| `write(data)` | `data` (list of bytes) | Write data bytes to I2C bus |
| `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from I2C bus |
| `transfer(write_data, read_bytes)` | `write_data` (list, optional)<br>`read_bytes` (int, default=0) | Perform complete I2C transaction with start, write, restart, read, and stop |
| `scan(start_addr, end_addr)` | `start_addr` (int, default=0x00)<br>`end_addr` (int, default=0x7F) | Scan I2C bus for devices in specified address range |

{{% alert context="info" %}}
The first byte in `write_data` should be the 8 bit I2C device address, it will be used for both the write and read operation.
{{% /alert %}}

#### Basic Configuration
```python
>>> from bpio_client import BPIOClient
>>> from bpio_i2c import BPIOI2C
>>> client = BPIOClient("COM35")
>>> i2c = BPIOI2C(client)
>>> i2c.configure(speed=400000, clock_stretch=False)
True
```

#### Manual I2C Operations
```python
>>> i2c.start()                   # Send start condition
>>> i2c.write([0xA0, 0x00])       # Write device address and register
>>> i2c.stop()                    # Send stop condition
>>> i2c.start()                   # Send start condition again
>>> i2c.write([0xA1])             # Write read address
>>> data = i2c.read(2)            # Read 2 bytes
>>> i2c.stop()                    # Send stop condition
```

#### Complete Transaction
```python
>>> # Write to register 0x00 of device at address 0x50
>>> result = i2c.transfer(write_data=[0xA0, 0x00, 0x42])
>>> # Read 2 bytes from device at address 0x50, location 0x00 (e.g. 24x02 EEPROM)
>>> result = i2c.transfer(write_data=[0xA0, 0x00], read_bytes=2)
```

#### Bus Scanning
```python
>>> devices = i2c.scan()
Scanning I2C bus from 0x00 to 0x7F...
>>> print(f"Found devices: {[hex(addr) for addr in devices]}")
Found devices: ['0xa0', '0xa1']
```
### SPI Data

The `BPIOSPI` class provides methods for SPI communication, inheriting from the `BPIOBase` class for configuration and status functionality.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(speed, clock_polarity, clock_phase, chip_select_idle, **kwargs)` | `speed` (int, default=1000000)<br>`clock_polarity` (bool, default=0)<br>`clock_phase` (bool, default=0)<br>`chip_select_idle` (bool, default=1)<br>`**kwargs` (additional config) | Configure SPI mode with clock settings and chip select polarity |

{{% alert context="info" %}}
Speed is specified in Hz (e.g., 1000000 for 1MHz).
{{% /alert %}}

#### SPI Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `select()` | None | Select SPI device|
| `deselect()` | None | Deselect SPI device|
| `write(data)` | `data` (list of bytes) | Write data bytes to SPI device |
| `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from SPI device |
| `transfer(write_data, read_bytes)` | `write_data` (list of bytes)<br>`read_bytes` (int, optional) | Perform complete SPI transaction with select, write/read, and deselect |

{{% alert context="info" %}}
The actual Chip Select pin state is set according to the SPI `chip_select_idle` state set during configuration.
{{% /alert %}}

#### Basic Configuration
```python
>>> from bpio_client import BPIOClient
>>> from bpio_spi import BPIOSPI
>>> client = BPIOClient("COM35")
>>> spi = BPIOSPI(client)
>>> spi.configure(speed=1000000, clock_polarity=False, clock_phase=False, chip_select_idle=True)
True
```

#### Manual SPI Operations
```python
>>> spi.select()                  # Pull chip select low
>>> spi.write([0x9F])             # Send command
>>> data = spi.read(3)            # Read response
>>> spi.deselect()                # Pull chip select high
```

#### Complete Transaction
```python
>>> # Send command 0x9F and read 3 bytes response
>>> result = spi.transfer(write_data=[0x9F], read_bytes=3)
>>> print(f"Device ID: {[hex(b) for b in result['data_read']]}")
Device ID: ['0xef', '0x40', '0x18']
```

### 1-Wire Data

The `BPIO1Wire` class provides methods for 1-Wire communication, inheriting from the `BPIOBase` class for configuration and status functionality.

#### Configuration

| Method | Parameters | Description |
|--------|------------|-------------|
| `configure(**kwargs)` | `**kwargs` (configuration options) | Configure 1-Wire mode with additional hardware settings |

#### 1-Wire Operations

| Method | Parameters | Description |
|--------|------------|-------------|
| `reset()` | None | Reset the 1-Wire bus and check for device presence |
| `write(data)` | `data` (list of bytes) | Write data bytes to 1-Wire device |
| `read(num_bytes)` | `num_bytes` (int) | Read specified number of bytes from 1-Wire device |
| `transfer(write_data, read_bytes)` | `write_data` (list, optional)<br>`read_bytes` (int, default=0) | Perform complete 1-Wire transaction with reset, write, and read |


#### Basic Configuration
```python
>>> from bpio_client import BPIOClient
>>> from bpio_1wire import BPIO1Wire
>>> client = BPIOClient("COM35")
>>> ow = BPIO1Wire(client)
>>> ow.configure()
True
```

#### Manual 1-Wire Operations
```python
>>> ow.reset()                    # Reset bus and check for presence
>>> ow.write([0xCC])              # Skip ROM command
>>> ow.write([0x44])              # Start temperature conversion
>>> ow.reset()                    # Reset again
>>> ow.write([0xCC])              # Skip ROM command  
>>> ow.write([0xBE])              # Read scratchpad command
>>> data = ow.read(9)             # Read 9 bytes from scratchpad
```

#### Complete Transaction
```python
>>> # Read temperature from DS18B20
>>> result = ow.transfer(write_data=[0xCC, 0x44])  # Skip ROM + convert
>>> # Wait for conversion...
>>> result = ow.transfer(write_data=[0xCC, 0xBE], read_bytes=9)  # Read data
>>> print(f"Temperature data: {[hex(b) for b in result[:2]]}")
Temperature data: ['0x50', '0x05']
```

#### DS18B20 Temperature Sensor Example
```python
>>> # Complete temperature reading sequence
>>> ow.reset()
>>> ow.write([0xCC, 0x44])        # Skip ROM, start conversion
>>> # Wait 750ms for conversion
>>> import time
>>> time.sleep(0.75)
>>> ow.reset()
>>> ow.write([0xCC, 0xBE])        # Skip ROM, read scratchpad
>>> temp_data = ow.read(2)        # Read temperature bytes
>>> temp = (temp_data[1] << 8 | temp_data[0]) / 16.0
>>> print(f"Temperature: {temp}°C")
Temperature: 21.3125°C
```

##  Debugging

{{< term>}}
[BPIO] Flatbuffer length: 64
[BPIO] Flatbuffer received, length: 64
[BPIO] Packet Type: 3
[Data Request] Start main condition: true
[Data Request] Start alternate condition: false
[Data Request] Data write vector is present
[Data Request] Data write vector length: 2
[Data Request] Data write: 0xA0 0x00
[Data Request] Bytes to read: 16
[Data Request] Stop main condition: true
[Data Request] Stop alternate condition: false
[Data Request] Protocol request
[I2C] Performing transaction
{{</ term>}}


{{% alert context="danger" %}}
BPIO2 can display detailed debugging data in the Bus Pirate terminal. Enable this by setting ```"bpio_debug_enable":1``` in your BPCONFIG.BP JSON file on the Bus Pirate internal storage. **Then reboot the Bus Pirate for this to take effect.**
{{% /alert %}}

The Bus Pirate firmware will print debugging information to the terminal when BPIO2 requests are processed. This can help you understand how the protocol works and troubleshoot any issues.

{{% alert context="warning" %}}
If you don't have a BPCONFIG.BP file, type configuration command ```c``` in the Bus Pirate terminal. At the prompt type x to exit, the configuration file will be created.
{{% /alert %}}

## FlatBuffers Tooling Download

Download precompiled FlatBuffer tooling, required includes, and demo libraries from the BPIO2 repo.
- [Download BPIO2 FlatBuffer Tooling and Libraries](https://github.com/DangerousPrototypes/BusPirate-BBIO2-flatbuffer-interface/tree/main)


{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

### Compile your own tooling

To generate your own tooling from the BPIO2 schema, you can use a FlatBuffers compiler with [bpio2.fbs](https://github.com/DangerousPrototypes/BusPirate-BBIO2-flatbuffer-interface/blob/main/bpio.fbs).

#### C language tooling

```
flatcc -a bpio2.fbs
```

To generate C tooling, use the [flatcc](https://github.com/dvidelabs/flatcc) compiler. This is the version we use to generate C tooling for the Bus Pirate firmware.

#### Other language tooling
```
flatc --python bpio.fbs
```

For C++, C#, Dart, Go, Java, JavaScript, Kotlin, Lobster, Lua, PHP, Python, Rust, Swift, TypeScript use [flatc](https://github.com/google/flatbuffers).

{{% alert context="info" %}}
Javasscript tooling was deprecated in flatc. Transpile the TypeScript tooling to JavaScript using the TypeScript compiler.
{{% /alert %}}

#### FlatBuffers Includes

In addition to the generated tooling, you will need to include the FlatBuffers support library for your language. Check the /include/ folder in the BPIO2 repository for the required files.

## COBS Encoding

FlatBuffers request and response packets are encoded using COBS (Consistent Overhead Byte Stuffing) to ensure that the data can be transmitted over serial without issues. COBS encoding replaces zero bytes with a special marker, allowing the data to be sent as a continuous stream without needing to escape zero bytes. Most languages have a simple COBS library available, for example the [COBS Python library](https://pypi.org/project/cobs/).

## Schema

BBIO2 uses **Request** and **Response** tables to communicate with the Bus Pirate. 
- The host device sends a **Request** to the Bus Pirate, which contains the operation to be performed.
- The Bus Pirate processes the request and sends back a **Response** containing the result of the operation.

There are currently several Request and Response pair 'tables':
- *StatusRequest/StatusResponse* - Used to check the status of the Bus Pirate and read pin states.
- *ConfigurationRequest/ConfigurationResponse* - Used to configure the Bus Pirate mode, settings and hardware.
- *DataRequest/DataResponse* - Used to send and receive data to/from the Bus Pirate.

Additionally there are wrapper tables for the requests and responses:
- *RequestPacket* - Contains the request type and the request data.
- *ResponsePacket* - Contains the response type and the response data.

There is a table for mode configuration:
- *ModeConfiguration* - Contains mode-specific settings, such as speed and other parameters.

Finally, there is an *ErrorResponse* table that is used to return error messages when a request fails.
- *ErrorResponse* - Contains an error message if a request fails.

### Status
- The **StatusRequest** is used to query the current status of the Bus Pirate.
- The **StatusResponse** contains the requested status information.

#### StatusRequest

```flatbuffers
enum StatusRequestTypes:byte{All, Version, Mode, Pullup, PSU, ADC, IO, Disk, LED}

table StatusRequest{
  query:[StatusRequestTypes]; // List of status queries to perform.
}
```

StatusRequest has a single field, `query`, which is an array of `StatusRequestTypes`. **All** returns everything, while the other types return specific queries which reduces the size of the StatusResponse. 

{{% alert context="info" %}}
If no `query` is specified, all status information is returned.
{{% /alert %}} 

##### Python Example
```python
# Create the query vector BEFORE starting the StatusRequest table
StatusRequest.StartQueryVector(builder, 1)
builder.PrependUint8(StatusRequestTypes.StatusRequestTypes.All)
query_vector = builder.EndVector()

# Create a StatusRequest
StatusRequest.Start(builder)
StatusRequest.AddQuery(builder, query_vector)
status_request = StatusRequest.End(builder)
```

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

#### StatusResponse

```flatbuffer
// returns the status queries requested in StatusRequest
// if query is empty, then all queries are performed
table StatusResponse {
  error:string; // Error message if any.
  version_hardware_major:uint8; //HW version
  version_hardware_minor:uint8; //HW revision
  version_firmware_major:uint8;//FW version
  version_firmware_minor:uint8; //FW revision
  version_firmware_git_hash:string; //Git hash of the firmware.
  version_firmware_date:string; //Date of the firmware build.
  modes_available:[string]; // List of modes available on the device.
  mode_current:string; // Current mode name.
  mode_pin_labels:[string]; // Labels for the pins in the current mode.
  mode_bitorder_msb:bool; // Bit order for the current mode (true for MSB first, false for LSB first).
  mode_max_packet_size:uint32; // Maximum flat buffer packet size for the current mode.
  mode_max_write:uint32; // Maximum data write size for the current mode.
  mode_max_read:uint32; // Maximum data read size for the current mode.
  psu_enabled:bool; // Power supply enabled.
  psu_set_mv:uint32; // Power supply set voltage in millivolts.
  psu_set_ma:uint32; // Power supply set current in milliamps.
  psu_measured_mv:uint32; // Measured power supply voltage in millivolts.
  psu_measured_ma:uint32; // measured power supply current in milliamps.
  psu_current_error:bool; // Power supply fuse error.
  pullup_enabled:bool; // Pull-up resistors enabled.
  adc_mv:[uint32]; // IO pin ADC values in millivolts.
  io_direction:uint8; // IO pin directions (true for output, false for input).
  io_value:uint8; // IO pin values (true for high, false for low).
  disk_size_mb:float; // Size of the disk in megabytes.
  disk_used_mb:float; // Used space on the disk in megabytes.
  led_count:uint8; // Number of LEDs.
}
```

Depending on the query parameters, all of some of the fields in the `StatusResponse` will be populated. If an error occurs, the `error` field will contain a message describing the error.

##### Python Example
```python
#test packet type and error field
contents_type = resp_packet.ContentsType()
if contents_type != ResponsePacketContents.ResponsePacketContents.StatusResponse:
    print(f"Expected StatusResponse, got {contents_type}")
    return None
status_resp = StatusResponse.StatusResponse()
status_resp.Init(resp_packet.Contents().Bytes, resp_packet.Contents().Pos)
print("StatusResponse:")

# Print hardware and firmware versions, test if fields are present
print(f"  Hardware version: {status_resp.HardwareVersionMajor()} REV{status_resp.HardwareVersionMinor()}")
print(f"  Firmware version: {status_resp.FirmwareVersionMajor()}.{status_resp.FirmwareVersionMinor()}")
print(f"  Firmware git hash: {status_resp.FirmwareGitHash().decode('utf-8')}")
print(f"  Firmware date: {status_resp.FirmwareDate().decode('utf-8')}")

```

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

### Configuration
- The **ConfigurationRequest** is used to configure the Bus Pirate's settings and hardware. 
- The **ConfigurationResponse** contains any error message.

#### ConfigurationRequest

```flatbuffers
table ConfigurationRequest {
  mode:string; // Name of the mode to configure.
  mode_configuration:ModeConfiguration; // Configuration for the mode.
  mode_bitorder_msb:bool; // Bit order MSB.
  mode_bitorder_lsb:bool; // Bit order LSB.
  psu_disable:bool; // Disable power supply.
  psu_enable:bool; // Enable power supply.
  psu_set_mv:uint32; // Set voltage in millivolts (psu_enable must = true).
  psu_set_ma:uint16=300; // Set current in milliamps, 0 for unlimited (psu_enable must = true).
  pullup_disable:bool; // Disable pull-up resistors.
  pullup_enable:bool; // Enable pull-up resistors.
  io_direction_mask:uint8; // Bitmask for IO pin directions (1=modify this pin).
  io_direction:uint8; // IO pin directions in 8 bit byte (1 output, 0 input).
  io_value_mask:uint8; // Bitmask for IO pin values (1=modify this pin).
  io_value:uint8; // IO pin values in 8 bit byte (1 high, 0 low).
  led_resume:bool; // Resume LED effect after configuration.
  led_color:[uint32]; // LED colors in RGB format (0xRRGGBB).
  print_string:string; // string to print on terminal 
  hardware_bootloader:bool; // Enter bootloader mode.
  hardware_reset:bool; // Hardware reset the device.
  hardware_selftest:bool; // Perform a self-test on the device.
}
```

The `ConfigurationRequest` table allows you to set various parameters for the Bus Pirate. 

{{% alert context="warning" %}}
Requests are processed in the order they are listed in the table. This means a single request can be used to enable a mode, set the power supply voltage, enable pull-up resistors, and configure pin directions in one go.
{{% /alert %}}

##### Mode Configuration
The `mode_configuration` field is a `ModeConfiguration` table that contains mode-specific settings. This allows you to configure different modes, such as I2C, SPI, UART, etc.

```flatbuffer
table ModeConfiguration {
  speed:uint32=20000; // Speed in Hz or baud for the mode.
  data_bits:uint8=8; // Data bits for the mode (e.g., 8 for UART).
  parity:bool=false; // Parity for the mode (true for even parity, false for no parity).
  stop_bits:uint8=1; // Stop bits for the mode (1 or 2).
  flow_control:bool=false; // Flow control for the mode (true for enabled, false for disabled).
  signal_inversion:bool=false; // Signal inversion for the mode (true for inverted, false for normal).
  clock_stretch:bool=false; // Clock stretching for I2C mode (true for enabled,  false for disabled).
  clock_polarity:bool=false; // Clock idle polarity for SPI mode (true for high, false for low).
  clock_phase:bool=false; // Clock phase for SPI mode (false for leading edge, true for trailing edge).
  chip_select_idle:bool=true; // Chip select idle (0=idle low, 1=idle high) for SPI and 3-wire modes.
  submode:uint8; // Submode for LED and INFRARED modes (e.g., "RGB", "IR TX", "IR RX").
  tx_modulation:uint32; // TX modulation for INFRARED mode 
  rx_sensor:uint8; // RX sensor for INFRARED mode 
}
```
A ModeConfiguration table must be provided for the requested mode.

##### Python Example
```python
```

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.
#### ConfigurationResponse

```flatbuffer
table ConfigurationResponse{
  error:string; // Error message if any.
}
```

The `ConfigurationResponse` table contains an `error` string that will be populated if there is an error during the configuration process. If the configuration is successful, the `error` field will be empty.

##### Python Example
```python
```
See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

### Data
- The **DataRequest** table requests a data transaction in the currently selected mode.
- The **DataResponse** table contains any data received while processing the request.

#### DataRequest

```flatbuffer
table DataRequest {
  start_main:bool; // Start condition.
  start_alt:bool; // Alternate start condition.
  data_write:[ubyte]; // Data to write
  bytes_read:uint16; // Number of bytes to read.
  stop_main:bool; // Stop condition.
  stop_alt:bool; // Alternate stop condition.
}
```

The `DataRequest` table has fields that mimic the general Bus Pirate bus syntax/commands: start, write, read, stop.

The goal is to do a complete transaction in a single request, such as writing and reading an I2C or SPI device. However, you have complete control over the transaction, so you can write, read, start or stop individually as well.

|Field|Bus Pirate Syntax|Description|
|---|---|---|
|start_main|`[`|Any mode specific "start condition": 1-Wire RESET, I2C START, SPI Chip Select, etc |
|start_alt|`{`|Any mode specific "alternate start condition": SPI Chip Select Read with Write mode, 2WIRE Reset Pin, etc.|
|data_write|`0x00`|Write data (array) to the currently configured bus.|
|bytes_read|`r`|Read this many bytes from the currently configured bus.|
|stop_main|`]`|Any mode specific "stop condition": I2C STOP, SPI Chip Deselect, etc.|
|stop_alt|`}`|Any mode specific "alternate stop condition": currently unused.|

##### Python Example
```python
```
See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

#### DataResponse

```flatbuffer
table DataResponse {
  error:string; // Error message if any.
  data_read:[ubyte]; // Data read from device
}
```

The `DataResponse` table contains an `error` string that will be populated if there is an error during the data transaction. If the transaction is successful, the `data_read` field will contain the data read from the device.

##### Python Example
```python
```

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

### ErrorResponse

```flatbuffer
table ErrorResponse {
  error:string; // Error message if any.
}
```

The `ErrorResponse` table is used to return error messages when a request fails. It contains a single `error` string that describes the error.

##### Python Example
```python 
# Check if the response is an ErrorResponse
contents_type = resp_packet.ContentsType()  
if contents_type != ResponsePacketContents.ResponsePacketContents.ErrorResponse:
    print(f"Expected ErrorResponse, got {contents_type}")
    return None
error_resp = ErrorResponse.ErrorResponse()
error_resp.Init(resp_packet.Contents().Bytes, resp_packet.Contents().Pos)
# Print the error message
if error_resp.Error() is not None:
    print(f"Error: {error_resp.Error().decode('utf-8')}")
else:
    print("No error")
```

See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

### Request & Response Wrappers




#### RequestPacket

```flatbuffer
union RequestPacketContents { StatusRequest, ConfigurationRequest, DataRequest}

table RequestPacket {
  version_major:uint8=2;
  version_minor:uint8=0;
  contents:RequestPacketContents;
}
```

#### Python Example
```python
```
See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.
#### ResponsePacket

```flatbuffer
union ResponsePacketContents { ErrorResponse, StatusResponse, ConfigurationResponse, DataResponse}

table ResponsePacket{
  version_major:uint8=2;
  version_minor:uint8=0;
  contents:ResponsePacketContents;
}
```
#### Python Example
```python

```
See [flatc](https://flatbuffers.dev/quick_start/) for language-specific usage instructions.

##### I2C

I2C data requests have a few special considerations:

In a transaction, including start, stop, write and read can all be done individually, or as a complete I2C write/read transaction.

start, stop, write and read can all be done individually, or as a complete I2C write/read transaction.

- If `start_main` is true, the Bus Pirate will send a start condition 
- In a transaction the first byte of `data_write` is used as the **8 bit**  I2C address. The I2C Read/Write bit is set and cleared automatically.
- If `start_main` is true and `data_write` has more than one byte (the I2C address), the Bus Pirate will send the first byte as the I2C address and the rest of the bytes as data to write.
- If `data_write` has more than one byte **and** `bytes_read` is greater than 0, the Bus Pirate will send an I2C RESTART. 
- If `bytes_read` is greater than 0, the Bus Pirate will send the I2C Read address (`data_write` byte 0) and then read that many bytes from the I2C device. The Bus Pirate will NACK the last byte read.
- If `stop_main` is true, the Bus Pirate will send a stop condition.