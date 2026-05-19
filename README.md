# flexibleloop

A Python utility that extends the standard `while` loop with built-in timeout control, iteration limits, pre-iteration hooks, and dynamic condition functions — all through a clean `for`-loop interface.

---

## Why

Python's `while` loop is simple but limited. Adding a timeout, counting iterations, or updating variables before checking a condition requires boilerplate every time. `FlexibleWhile` packages all of that into a reusable, configurable object.

---

## Features

- **Timeout** — Stop the loop automatically after a set number of seconds
- **Max iterations** — Cap the number of iterations without a counter variable
- **Before function** — Run a function before each iteration; its return value becomes the loop variable
- **Condition function** — Define the loop condition as a callable instead of inline logic
- **Callbacks** — Execute custom functions when timeout or max iterations are hit
- **Clean interface** — Used as a standard `for` loop; no new syntax to learn

---

## Installation

```bash
pip install flexibleloop
```

```python
from flexibleloop.FlexibleLoop import FlexibleWhile
```

---

## Usage

### Basic loop with timeout

```python
from FlexibleLoop import FlexibleWhile

loop = FlexibleWhile(timeout=5.0)

for _ in loop:
    # Runs until 5 seconds have elapsed
    do_something()
```

### Loop with a condition function

```python
def condition(value):
    return value < 100

def update(value):
    return value + 7

loop = FlexibleWhile(
    before_func=update,
    cond_func=condition,
    start_vals=(0,)
)

for value in loop:
    print(value)
# Prints: 7, 14, 21, ... up to 98
```

### Loop with max iterations and a callback

```python
def on_limit():
    print("Max iterations reached")

loop = FlexibleWhile(
    max_iterations=10,
    on_max_iterations=on_limit
)

for _ in loop:
    do_something()
```

### Accessing loop metadata

```python
loop = FlexibleWhile(timeout=3.0)
for _ in loop:
    pass

print(f"Completed {loop.iterations} iterations in {loop.time_elapsed:.2f}s")
```

---

## API Reference

### `FlexibleWhile(before_func, cond_func, start_vals, timeout, max_iterations, on_timeout, on_max_iterations)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `before_func` | callable | None | Called before each iteration. Return value updates loop variable(s). |
| `cond_func` | callable | None | Loop continues while this returns `True`. `None` is equivalent to `while True`. |
| `start_vals` | tuple | `(None,)` | Initial values passed to `before_func` and `cond_func` on first iteration. |
| `timeout` | float | None | Maximum loop duration in seconds. |
| `max_iterations` | int | None | Maximum number of iterations. |
| `on_timeout` | callable | None | Called when timeout is reached. |
| `on_max_iterations` | callable | None | Called when max iterations is reached. |

### Instance attributes (after iteration)

| Attribute | Description |
|---|---|
| `loop.iterations` | Number of completed iterations |
| `loop.time_elapsed` | Total elapsed time in seconds |
| `loop.values` | Current value(s) of the loop variable |

---

## License

MIT License — free to use, modify, and distribute, including commercially.  
Attribution required: please credit **Dr. Tolga Kaan Kanatlı** in any derivative work or product.

---

## Author

**Dr. Tolga Kaan Kanatlı**  
PhD in Chemical Engineering — PEM Fuel Cells & Hydrogen Production  
[GitHub](https://github.com/tolgakanatli) · [LinkedIn](https://www.linkedin.com/in/tolgakanatli) · tolgakanatli@hotmail.com
