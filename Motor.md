---

# `Motor` Class API Documentation

High-level control for LEGO® Powered Up / SPIKE™ Prime motors with built-in rotation sensors.  
Extends [`Device`](#device-class-api-documentation) to provide motion control methods such as running for a set time, angle, or to a target position, with optional acceleration, deceleration, and stop behaviors.

---

## Initialization

### `Motor(port: Port, positive_direction: Direction = Direction.CLOCKWISE, default_stop: Stop = Stop.SMART_BRAKE, acceleration: int = 1000, deceleration: int = 1000)`

**Args:**
- `port` (`Port`): Hub port where the motor is connected.
- `positive_direction` (`Direction`): Direction the motor should turn for positive speed/angle values.
  - `Direction.CLOCKWISE`
  - `Direction.COUNTERCLOCKWISE`
- `default_stop` (`Stop`): Default stop action when the motor halts.
  - `0` – CONTINUE  
  - `1` – COAST  
  - `2` – BRAKE  
  - `3` – HOLD  
  - `4` – SMART_COAST  
  - `5` – SMART_BRAKE
- `acceleration` (`int`): Acceleration in °/sec² (1–10000).
- `deceleration` (`int`): Deceleration in °/sec² (1–10000).

**Raises:**
- `RuntimeError`: If the connected device is not recognized as a motor.

---

## Methods

### `angle() -> int`
Get the cumulative (relative) rotation angle since the last reset.

**Returns:**  
`int`: Rotation in degrees. Positive values follow `positive_direction`.

---

### `absolute_angle() -> int`
Get the absolute rotation angle.

**Returns:**  
`int`: Position in degrees within -179 to 180, independent of resets and `positive_direction`.

---

### `reset_angle(angle: int = 0)`
Reset the cumulative rotation angle.

**Args:**
- `angle` (`int`): New cumulative angle in degrees (default `0`).

---

### `speed() -> int`
Get the current rotational speed.

**Returns:**  
`int`: Speed in degrees/sec (positive or negative).

---

### `stop(then: Stop | None = None)`
Stop the motor with a specified stop mode.

**Args:**
- `then` (`Stop`, optional): Stop behavior. Defaults to `self.default_stop`.

---

### `run(speed: int)`
Run the motor continuously at a given speed.

**Args:**
- `speed` (`int`): Speed in degrees/sec. Sign follows `positive_direction`.

---

### `run_time(speed: int, time: int, then: Stop | None = None, wait: bool = True)`
Run the motor for a set duration.

**Args:**
- `speed` (`int`): Speed in degrees/sec.
- `time` (`int`): Duration in milliseconds.
- `then` (`Stop`, optional): Stop behavior after run. Defaults to `self.default_stop`.
- `wait` (`bool`): If `True`, block until complete; if `False`, run asynchronously.

---

### `run_angle(speed: int, angle: int, then: Stop | None = None, wait: bool = True)`
Run the motor for a specific rotation angle.

**Args:**
- `speed` (`int`): Speed in degrees/sec.
- `angle` (`int`): Rotation in degrees (positive or negative).
- `then` (`Stop`, optional): Stop behavior after run. Defaults to `self.default_stop`.
- `wait` (`bool`): If `True`, block until complete; if `False`, run asynchronously.

---

### `run_target(speed: int, target: int, then: Stop | None = None, wait: bool = True)`
Run the motor until it reaches a target relative position.

**Args:**
- `speed` (`int`): Speed in degrees/sec.
- `target` (`int`): Target relative position in degrees from current angle.
- `then` (`Stop`, optional): Stop behavior after run. Defaults to `self.default_stop`.
- `wait` (`bool`): If `True`, block until complete; if `False`, run asynchronously.

---

### `run_absolute_angle(speed: int, angle: int, direction: Direction = Direction.CLOCKWISE, then: Stop | None = None, wait: bool = True)`
Run the motor to a specific absolute position.

**Args:**
- `speed` (`int`): Speed in degrees/sec.
- `angle` (`int`): Target absolute position (-179 to 180).
- `direction` (`Direction`):
  - `0` – CLOCKWISE
  - `1` – COUNTERCLOCKWISE
  - `2` – SHORTEST_PATH
  - `3` – LONGEST_PATH
- `then` (`Stop`, optional): Stop behavior after run. Defaults to `self.default_stop`.
- `wait` (`bool`): If `True`, block until complete; if `False`, run asynchronously.

**Notes:**
- `angle` refers to the motor’s absolute position within its -179° to 180° range.
- `direction` determines the travel path, not just the final orientation.

---

## Usage Examples

```python
# Initialize motor on Port A
m = Motor(Port.A, positive_direction=Direction.CLOCKWISE)

# Run at 360°/sec for 2 seconds, then brake
m.run_time(360, 2000, then=Stop.BRAKE)

# Rotate 720° at 720°/sec, then hold position
m.run_angle(720, 720, then=Stop.HOLD)

# Move to absolute position 90° via shortest path
m.run_absolute_angle(360, 90, direction=Direction.SHORTEST_PATH)
```

---
