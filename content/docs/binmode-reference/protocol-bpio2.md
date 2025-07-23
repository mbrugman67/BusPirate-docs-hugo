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

The Bus Pirate BPIO2 protocol is a flat buffer interface designed for simple and complete control of the Bus Pirate hardware. It allows for sending and receiving data in a structured format, enabling various operations such as reading and writing to GPIO pins, controlling peripherals, and more.

[Flat Buffers](https://flatbuffers.dev/) automatically create "tooling" to for most common languages and compilers. This means you can easily integrate the BPIO2 protocol into your projects without needing to write extensive parsing or serialization code.

## Why BPIO2?

Bus Pirate v3.x has a **BBIO** interface, an abbreviation for **Bit Bang Input/Output**. The interface was originally designed for simple bit-banging only, other protocols were hacked in later. 

We *could* call this BBIO2, but it's in no way similar to the original BBIO interface and it's only marginally for bit-banging. Instead, we call it BPIO2 meaning the second generation of Bus Pirate I/O.

## Debugging

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
BPIO2 can display detailed debugging data in the Bus Pirate terminal. Enable this by setting ```"bpio_debug_enable":1``` in your BPCONFIG.BP JSON file on the Bus Pirate internal storage. **The reboot the Bus Pirate for this to take effect.**
{{% /alert %}}

The Bus Pirate firmware will print debugging information to the terminal when BPIO2 requests are processed. This can help you understand how the protocol works and troubleshoot any issues.

{{% alert context="warning" %}}
If you don't have a BPCONFIG.BP file, type configuration command ```c``` in the Bus Pirate terminal. At the prompt type x to exit, the configuration file will be created.
{{% /alert %}}

## Flat Buffers

{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

We provide precompiled FlatBuffer tooling in the firmware repository.

To generate your own tooling from the BPIO2 schema, you can use a FlatBuffers compiler with `src/bpio2.fbs`.

### C language tooling

```
flatcc -a bpio2.fbs
```

To generate C tooling, use the [flatcc](https://github.com/dvidelabs/flatcc) compiler. This is the version we use to generate C tooling for the Bus Pirate firmware.

### Other languages tooling
```
flatc --python bpio.fbs
```

For C++, C#, Dart, Go, Java, JavaScript, Kotlin, Lobster, Lua, PHP, Python, Rust, Swift, TypeScript use [flatc](https://github.com/google/flatbuffers).

## Schema

BBIO2 uses **Request** and **Response** tables to communicate with the Bus Pirate. 
- The host device sends a **Request** to the Bus Pirate, which contains the operation to be performed.
- The Bus Pirate processes the request and sends back a **Response** containing the result of the operation.

### Tables
There are currently three Request and Response pair 'tables':
- *StatusRequest/StatusResponse* - Used to check the status of the Bus Pirate and read pin states.
- *ConfigurationRequest/ConfigurationResponse* - Used to configure the Bus Pirate settings and hardware.
- *DataRequest/DataResponse* - Used to send and receive data to/from the Bus Pirate.

## Status
- The **StatusRequest** is used to query the current status of the Bus Pirate. It can include options to read pin states or check the Bus Pirate's operational status.
- The **StatusResponse** contains the requested status information, such as pin states and operational flags.

### StatusRequest

```flatbuffer
enum StatusRequestTypes:byte{All, Version, Mode, Pullup, PSU, ADC, IO, Disk, LED}

table StatusRequest{
  query:[StatusRequestTypes]; // List of status queries to perform.
}
```

StatusRequest has a single field, `query`, which is an array of `StatusRequestTypes`. **All** returns everything, while the other types return specific queries which reduces the size of the StatusResponse. 

#### Python Example
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

### StatusResponse

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

#### Python Example
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

## Configuration
- The **ConfigurationRequest** is used to configure the Bus Pirate's settings and hardware. It allows for setting various parameters such as power supply voltage, pull-up resistors, and pin directions.
- The **ConfigurationResponse** contains any error message.

### ConfigurationRequest

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

#### Mode Configuration
The `mode_configuration` field is a `ModeConfiguration` table that contains mode-specific settings. This allows you to configure different modes, such as I2C, SPI, UART, etc.

```flatbuffer
// move mode string name here too?
table ModeConfiguration {
  speed_khz:uint32; // Speed in kHz for the mode.
}
```

A ModeConfiguration table must be provided for the requested mode.

#### Python Example
```python
```
### ConfigurationResponse

```flatbuffer
table ConfigurationResponse{
  error:string; // Error message if any.
}
```

The `ConfigurationResponse` table contains an `error` string that will be populated if there is an error during the configuration process. If the configuration is successful, the `error` field will be empty.

#### Python Example
```python
```

{{% alert context="info" %}}
Most people won't need to interact with the FlatBuffer tooling directly. Ideally there will be a library that abstracts this away into simpler functions for common languages.
{{% /alert %}}

## Data
- The **DataRequest** table requests a data transaction in the currently selected mode.
- The **DataResponse** table contains any data received while processing the request.

### DataRequest

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

#### Mode Specific DataRequests

##### I2C

start, stop, write and read can all be done individually, or as a complete I2C write/read transaction.

- If `start_main` is true, the Bus Pirate will send a start condition 
- In a transaction the first byte of `data_write` is used as the **8 bit**  I2C address. The I2C Read/Write bit is set and cleared automatically.
- If `data_write` has more than one byte (the I2C address), the Bus Pirate will send the first byte as the I2C address and the rest of the bytes as data to write.
- If `data_write` has more than one byte **and** `bytes_read` is greater than 0, the Bus Pirate will send an I2C RESTART. 
- If `bytes_read` is greater than 0, the Bus Pirate will send the I2C Read address (`data_write` byte 0) and then read that many bytes from the I2C device. The Bus Pirate will NACK the last byte read.
- If `stop_main` is true, the Bus Pirate will send a stop condition.

### DataResponse

```flatbuffer
table DataResponse {
  error:string; // Error message if any.
  data_read:[ubyte]; // Data read from device
}
```

The `DataResponse` table contains an `error` string that will be populated if there is an error during the data transaction. If the transaction is successful, the `data_read` field will contain the data read from the device.