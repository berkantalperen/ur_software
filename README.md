# UR Software

This repository contains simple examples for controlling a Universal Robots arm using the [`urx`](https://pypi.org/project/urx/) Python library.

## Prerequisites

- **Python 3.8+**
- Install the `urx` package:
  ```bash
  pip install urx
  ```
- A reachable UR robot. The scripts assume the robot is at `192.168.0.100`; modify the IP in the code if needed.

## Running the examples

### `main.py`

Runs a pick-and-place loop using `programs/pick_place.py`:

```bash
python main.py
```

The script executes five cycles by default. Edit `main.py` if you want a different number of cycles (pass `-1` to run indefinitely).

### `monitor.py`

Provides a basic live monitor for the robot using `curses`:

```bash
python monitor.py
```

Press `q` to exit. The monitor refreshes several times per second and displays joint positions, TCP pose and other data.

### Optional arguments

Command‐line options for adjusting robot IP and number of cycles will be added in future revisions. Check the source files for the most up‑to‑date usage information.

