---

# `Device` Class API Documentation

Base abstraction for any LEGO® Powered Up / SPIKE™ Prime device connected to a hub port.  
Wraps low-level `device` module calls with a consistent, Pythonic interface that higher-level classes (motors, sensors, lights) can extend.

---

## Overview

- **Purpose:** Provide a unified interface for identifying a connected device, reading its raw data, controlling power via duty cycle, and switching operational modes.
- **Scope:** Works for all LPF2 devices (e.g., angular motors, DC motors, color/force/distance sensors, lights, and matrices).
- **Design:** Minimal, extensible base class that child classes specialize with device-specific methods and semantics.

---

## Initialization

### `Device(port: Port)`

**Args:**
- `port` (`Port`): The hub port where the device is physically connected.

**Raises:**
- `RuntimeError`: If no device is detected on the given port.

**Behavior:**  
Immediately probes the port by calling `get()` to verify the device is present and responsive.

> 💡 Constructing a `Device`-derived class will fail fast if the expected device is not connected.

---

## Methods

### `get() -> tuple[int]`
Retrieve the current raw data values from the device.

**Returns:**
- `tuple[int]`: Raw sensor or status data.

**Notes:**
- The meaning, count, and range of values depend on the device and its current mode.

---

### `get_duty_cycle() -> int`
Get the current PWM duty cycle.

**Returns:**
- `int`: Range `-10000` to `10000` (positive = forward, negative = reverse).

---

### `set_duty_cycle(duty_cycle: int)`
Set the PWM duty cycle (power level).

**Args:**
- `duty_cycle` (`int`): `-10000` (full reverse) to `10000` (full forward).

**Notes:**
- Direct power control without speed regulation.

---

### `ready() -> bool`
Check if the device is ready to receive commands.

**Returns:**
- `bool`: `True` if ready, `False` otherwise.

---

### `id() -> int`
Get the unique LPF2 device ID.

**Returns:**
- `int`: Device ID.

**Common IDs:**

| ID  | Device |
|-----|--------|
| 0   | No device / port empty |
| 1   | WeDo 2.0 Medium Motor |
| 2   | Powered Up Train Motor |
| 8   | Powered Up Light |
| 34  | WeDo 2.0 Tilt Sensor |
| 35  | WeDo 2.0 Infrared Motion Sensor |
| 37  | BOOST Color Distance Sensor |
| 38  | BOOST Interactive Motor |
| 46  | Technic Large Motor |
| 47  | Technic Extra Large Motor |
| 48  | SPIKE Medium Angular Motor |
| 49  | SPIKE Large Angular Motor |
| 61  | SPIKE Color Sensor |
| 62  | SPIKE Ultrasonic Sensor |
| 63  | SPIKE Force Sensor |
| 64  | SPIKE 3×3 Color Light Matrix |
| 65  | SPIKE Small Angular Motor |
| 75  | Technic Medium Angular Motor |
| 76  | Technic Large Angular Motor |

> ℹ Not exhaustive — LEGO may add new IDs.

---

### `set_mode(mode: int)`
Set the operational mode of the device.

**Args:**
- `mode` (`int`): Mode index (device-specific).

**Examples:**
- **Motors:** Power, Speed, Position, combinations.
- **Color Sensor:** Reflected light, Ambient light, Color index, Raw RGB, HSV.
- **Distance Sensor:** Distance, Presence, Raw composite, Single-shot, Continuous.
- **Force Sensor:** Force (N), Pressed boolean, Raw value.

**Notes:**
- Mode numbers follow the LEGO Wireless Protocol (LPF2).
- Changing mode alters the output of `get()`.

---

### `reset_mode()`
Reset the device to its default mode.

---

## Usage Examples

```python
# Verify a device and read raw data
dev = Device(Port.A)
print("Device ID:", dev.id())
print("Raw data:", dev.get())

# Apply power to a motor
motor = Device(Port.B)
motor.set_mode(0)          # Power mode
motor.set_duty_cycle(4500) # ~45% forward

# Switch sensor modes safely
sensor = Device(Port.C)
sensor.set_mode(2)     # e.g., color index
data = sensor.get()
sensor.reset_mode()    # back to default
```

---
