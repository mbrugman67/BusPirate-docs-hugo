+++
title = "BPIO2 Flat Buffer Interface"
description = "Bus Pirate Flat Buffer Interface (BPIO2) protocol documentation"
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

The Bus Pirate BPIO2 binmode is a [flat buffer](https://flatbuffers.dev/) interface designed for simple and complete control of the Bus Pirate hardware from an application or script. It allows for sending and receiving data in a structured format, enabling various operations such as reading and writing to GPIO pins, controlling peripherals, and more.

Pre-compiled BPIO2 flat buffer "tooling" is available for 15 common languages. This means you can easily integrate the BPIO2 protocol into your projects without needing to write extensive parsing or serialization code.

- [Python Library](#python-library) - A demonstration library for interacting with BPIO2 
- [Debugging](#debugging) - Display BPIO2 debug information in the Bus Pirate terminal
- [Flat Buffer Tooling Download](#flat-buffer-tooling-download) - Download precompiled FlatBuffer tooling for BPIO2 in 15 languages
- [Compile your own tooling](#compiling-your-own-tooling) - How to generate your own tooling from the BPIO2 schema
- [Schema](#schema) - Explanation of the low level flatbuffer tables used in BPIO2

## Why BPIO2?

Bus Pirate v3.x has a **BBIO1** interface, an abbreviation for **Bit Bang Input/Output**. The interface was originally designed for simple bit-banging only, other protocols were hacked in later. If I may say so, it was a bit of a mess. 

We *could* call this BBIO2, but it's in no way similar to the original BBIO1 interface and it's only marginally for bit-banging. Instead, we call it BPIO2 meaning the second generation of Bus Pirate I/O.

## Python Library

### Install

In addition to Python 3 or later, pyserial and COBS are required to use the BPIO2 library. You can install them using pip:

```bash
pip3 install -r requirements.txt
```

### Show Status

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
### Status DICT

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

#### Version

You can also get the version of the Bus Pirate firmware and hardware.

```python
>>> print(status['hardware_version_major'])
5
>>> print(status['hardware_version_minor'])
10
>>> print(status['firmware_version_major'])
0
>>> print(status['firmware_version_minor'])
0
>>> print(status['firmware_git_hash'])
unknown
>>> print(status['firmware_date'])
Aug 14 2025 14:11:17
```

{{% alert context="info" %}}
This is a development firmware so `firmware_git_hash` is not set. In a production firmware, this will be the git hash of the firmware commit.
{{% /alert %}}

#### Mode

Mode information is available:
- ```modes_available``` - An array containing the names of all available modes.
- ```mode_current``` - The name of the current mode.
- ```mode_pin_labels``` - An array containing the current IO pin labels.
- ```mode_bitorder_msb``` - Currently configured bit order for the current mode (True for MSB first, False for LSB first).

```python
>>> print(status['modes_available'])
['HiZ', '1WIRE', 'UART', 'HDUART', 'I2C', 'SPI', '2WIRE', '3WIRE', 'DIO', 'LED', 'INFRARED', 'JTAG']
>>> print(status['mode_current'])
HiZ
>>> print(status['mode_pin_labels'])
['OFF', '', '', '', '', '', '', '', '', 'GND']
>>> print(status['mode_bitorder_msb'])
True
```

#### Power Supply

Power supply status info is available:

- ```psu_enabled``` - Whether the power supply is enabled
- ```psu_set_mv``` - The voltage set for the power supply in millivolts.
- ```psu_set_ma``` - The current limit set for the power supply in milliamps, 0 for none.
- ```psu_measured_mv``` - The measured voltage of the power supply in millivolts.
- ```psu_measured_ma``` - The measured current of the power supply in milliamps.
- ```psu_current_error``` - Whether there is an over current error.  

```python
>>> print(status['psu_enabled'])
True
>>> print(status['psu_set_mv'])
3299
>>> print(status['psu_set_ma'])
300
>>> print(status['psu_measured_mv'])
3314
>>> print(status['psu_measured_ma'])
6
>>> print(status['psu_current_error'])
False
```
#### Pull-up Resistors
Pull-up resistor status info is available:
- ```pullup_enabled``` - Whether the pull-up resistors are enabled.

```python
>>> print(status['pullup_enabled'])
True
```

#### ADC
ADC status info is available:
- ```adc_mv``` - An array of ADC measurements for each IO pin in millivolts.

```python
>>> print(status['adc_mv'])
[3287, 3275, 3274, 3267, 3264, 3269, 3291, 3300]
```


#### IO Pins
IO pin status info is available:
- ```io_direction``` - A bitmask of the IO pin directions (1 for output, 0 for input).
- ```io_value``` - A bitmask of the IO pin values (1 for high, 0 for low).

```python
>>> print(f"{status['io_direction']:08b}")  
00000000
>>> print(f"{status['io_value']:08b}")
11111111
```

#### Disk
Disk status info is available:
- ```disk_size_mb``` - The size of the disk in megabytes.
- ```disk_used_mb``` - The amount of disk space used in megabytes.

```python
>>> print(status['disk_size_mb'])
97.69779205322266
>>> print(status['disk_used_mb'])
0.0
```
#### LED Count
LED status info is available:
- ```led_count``` - The number of LEDs on the Bus Pirate.

```python
>>> print(status['led_count'])
18
```

//#### max (packet size)

//#### Query to increase speed and reduce packet size

### Power supply config



### pull-ups
### io
### led
### print string
### hardware
### Changing modes, mode configuration
### Read/write data
### Errors

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

## COBS Encoding

## Flat Buffer Tooling Download

{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

We provide precompiled FlatBuffer tooling in the firmware repository.

### Compile your own tooling

To generate your own tooling from the BPIO2 schema, you can use a FlatBuffers compiler with `src/bpio2.fbs`.

#### C language tooling

```
flatcc -a bpio2.fbs
```

To generate C tooling, use the [flatcc](https://github.com/dvidelabs/flatcc) compiler. This is the version we use to generate C tooling for the Bus Pirate firmware.

#### Other languages tooling
```
flatc --python bpio.fbs
```

For C++, C#, Dart, Go, Java, JavaScript, Kotlin, Lobster, Lua, PHP, Python, Rust, Swift, TypeScript use [flatc](https://github.com/google/flatbuffers).

## Schema

BBIO2 uses **Request** and **Response** tables to communicate with the Bus Pirate. 
- The host device sends a **Request** to the Bus Pirate, which contains the operation to be performed.
- The Bus Pirate processes the request and sends back a **Response** containing the result of the operation.

There are currently several Request and Response pair 'tables':
- *StatusRequest/StatusResponse* - Used to check the status of the Bus Pirate and read pin states.
- *ConfigurationRequest/ConfigurationResponse* - Used to configure the Bus Pirate settings and hardware.
- *DataRequest/DataResponse* - Used to send and receive data to/from the Bus Pirate.

Additionally there are wrapper tables for the requests and responses:
- *RequestPacket* - Contains the request type and the request data.
- *ResponsePacket* - Contains the response type and the response data.

There is a table for mode configuration:
- *ModeConfiguration* - Contains mode-specific settings, such as speed and other parameters.

Finally, there is an *ErrorResponse* table that is used to return error messages when a request fails.
- *ErrorResponse* - Contains an error message if a request fails.

### Status
- The **StatusRequest** is used to query the current status of the Bus Pirate. It can include options to read pin states or check the Bus Pirate's operational status.
- The **StatusResponse** contains the requested status information, such as pin states and operational flags.

#### StatusRequest

```flatbuffer
enum StatusRequestTypes:byte{All, Version, Mode, Pullup, PSU, ADC, IO, Disk, LED}

table StatusRequest{
  query:[StatusRequestTypes]; // List of status queries to perform.
}
```

StatusRequest has a single field, `query`, which is an array of `StatusRequestTypes`. **All** returns everything, while the other types return specific queries which reduces the size of the StatusResponse. 

##### Python Example
```python
# Create the query vector BEFORE starting the StatusRequest table
StatusRequest.StartQueryVector(builder, 2)
builder.PrependUint8(StatusRequestTypes.StatusRequestTypes.All)
builder.PrependUint8(StatusRequestTypes.StatusRequestTypes.Version)
query_vector = builder.EndVector()

# Create a StatusRequest
StatusRequest.Start(builder)
StatusRequest.AddQuery(builder, query_vector)
status_request = StatusRequest.End(builder)
```

{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

#### StatusResponse

```flatbuffer
// returns the status queries requested in StatusRequest
table StatusResponse {
  error:string; // Error message if any.
  hardware_version_major:uint8; //HW version
  hardware_version_minor:uint8; //HW revision
  firmware_version_major:uint8;//FW version
  firmware_version_minor:uint8; //FW revision
  firmware_git_hash:string; //Git hash of the firmware.
  firmware_date:string; //Date of the firmware build.
  modes_available:[string]; // List of modes available on the device.
  mode_current:string; // Current mode name.
  mode_pin_labels:[string]; // Labels for the pins in the current mode.
  mode_bitorder_msb:bool; // Bit order for the current mode (true for MSB first, false for LSB first).
  psu_enabled:bool; // Power supply enabled.
  psu_set_mv:uint32; // Power supply voltage in millivolts.
  psu_set_ma:uint32; // Power supply current in milliamps.
  psu_measured_mv:uint32; // Measured power supply voltage in millivolts.
  psu_measured_ma:uint32; // Maximum power supply current in milliamps.
  psu_current_error:bool; // Power supply fuse error.
  pullup_enabled:bool; // Pull-up resistors enabled.
  pullx_config:uint32; //configuration for pull-x on BP7+
  adc_mv:[uint32]; // ADC values in millivolts.
  io_direction:uint8; // IO pin directions (true for output, false for input).
  io_value:uint8; // IO pin values (true for high, false for low).
  disk_size_mb:float; // Size of the disk in megabytes.
  disk_used_mb:float; // used space on the disk in megabytes.
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
{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

### Configuration
- The **ConfigurationRequest** is used to configure the Bus Pirate's settings and hardware. It allows for setting various parameters such as power supply voltage, pull-up resistors, and pin directions.
- The **ConfigurationResponse** contains any error message.

#### ConfigurationRequest

```flatbuffer
table ConfigurationRequest {
  mode:string; // Name of the mode to configure.
  mode_configuration:ModeConfiguration; // Configuration for the mode.
  mode_bitorder_msb:bool; // Bit order for the mode (true for MSB first, false for LSB first).
  mode_bitorder_lsb:bool; // Bit order for the mode (true for LSB first, false for MSB first).
  psu_disable:bool; // Disable power supply.
  psu_enable:bool; // Enable or disable power supply.
  psu_set_mv:uint32; // Set voltage in millivolts.
  psu_set_ma:uint16=300; // Set current in milliamps.
  pullup_disable:bool; // Disable pull-up resistors.
  pullup_enable:bool; // Enable pull-up resistors.
  pullx_config:uint32; //configuration for pull-x on BP7+
  io_direction_mask:uint8; // Bitmask for IO pin directions (1=modify this pin).
  io_direction:uint8; // IO pin directions in 8 bit byte (1 output, 0 input).
  io_value_mask:uint8; // Bitmask for IO pin values (1=modify this pin).
  io_value:uint8; // IO pin values in 8 bit byte (1 high, 0 low).
  led_resume:bool; // Resume LED effect after configuration.
  led_color:[uint32]; // LED colors in RGB format (0xRRGGBB).
  print_string:string; // string to print on terminal 
  hardware_bootloader:bool; // Enter bootloader mode.
  hardware_reset:bool; // Hardware reset the device.
}
```

The `ConfigurationRequest` table allows you to set various parameters for the Bus Pirate. 

{{% alert context="warning" %}}
Requests are processed in the order they are listed in the table. This means a single request can be used to enable a mode, set the power supply voltage, enable pull-up resistors, and configure pin directions in one go.
{{% /alert %}}

##### Mode Configuration
The `mode_configuration` field is a `ModeConfiguration` table that contains mode-specific settings. This allows you to configure different modes, such as I2C, SPI, UART, etc.

```flatbuffer
// move mode string name here too?
table ModeConfiguration {
  speed_khz:uint32; // Speed in kHz for the mode.
}
```

A ModeConfiguration table must be provided for the requested mode.

##### Python Example
```python
```
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

{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

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

#### DataResponse

```flatbuffer
table DataResponse {
  error:string; // Error message if any.
  data_read:[ubyte]; // Data read from device
}
```

The `DataResponse` table contains an `error` string that will be populated if there is an error during the data transaction. If the transaction is successful, the `data_read` field will contain the data read from the device.

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
### Request & Response Wrappers