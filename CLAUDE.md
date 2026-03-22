# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Home Assistant custom integration for the EARN-E energy monitor. The device reads a smart meter's P1 port and broadcasts real-time energy data via UDP on the local network. This integration listens for those broadcasts and exposes them as sensor entities in Home Assistant.

- **Integration domain:** `earn_e_p1`
- **IoT class:** `local_push` (no polling; data pushed via UDP on port 16121)
- **Platform:** Sensor only
- **Distributed via:** HACS (Home Assistant Community Store)
- **Minimum HA version:** 2024.1.0
- **PyPI dependency:** `earn-e-p1` (device communication library, [source](https://github.com/Miggets7/earn-e-p1))

## Development

```bash
# Install test dependencies
pip install -r requirements_test.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=custom_components.earn_e_p1 --cov-report=term-missing
```

The integration is pure Python with no compilation step. Uses a venv — run tests via `.venv/bin/pytest`. For manual testing, copy `custom_components/earn_e_p1/` into the HA config directory.

## Architecture

```
custom_components/earn_e_p1/
├── __init__.py       # Entry point: manages shared EarnEP1Listener lifecycle
├── config_flow.py    # Config flow with discovery, validation (waits for serial), reconfigure
├── const.py          # DOMAIN only
├── coordinator.py    # DataUpdateCoordinator, registers with shared listener
├── entity.py         # Base entity class with device_info (common-modules pattern)
├── sensor.py         # SensorEntity subclass + EarnEP1SensorEntityDescription definitions
├── manifest.json     # Integration metadata
├── strings.json      # UI strings (config flow steps, entity names)
└── translations/
    ├── en.json
    └── nl.json

tests/
├── __init__.py
├── conftest.py         # Shared fixtures
├── test_config_flow.py # Config flow tests (100% coverage target)
├── test_init.py        # Setup/unload tests
└── test_sensor.py      # Sensor entity tests
```

**Data flow:** Device UDP broadcast → shared `EarnEP1Listener` (from `earn-e-p1` library) → callback updates `EarnEP1Coordinator` → `EarnEP1Sensor` entities read from coordinator data.

**Key patterns:**
- All sensors defined via `SENSOR_DESCRIPTIONS` tuple of `EarnEP1SensorEntityDescription` in `sensor.py`. To add a sensor, add a description there.
- A shared `EarnEP1Listener` (stored in `hass.data[DOMAIN]`) is created on first entry setup and stopped when the last entry unloads. Multiple entries share one UDP socket.
- The coordinator registers/unregisters with the shared listener. It does not manage sockets directly.
- Config flow requires serial for entry creation — validation waits for a full telegram containing the serial.
- Config flow uses shared listener's instance methods when one is running, standalone `discover()`/`validate()` otherwise.
- Sensor availability depends on the sensor's JSON key being present in the coordinator's merged data dict.

## Related Repositories

- **[earn-e-p1](https://github.com/Miggets7/earn-e-p1)** — PyPI library handling UDP communication. Managed with `uv`. Located at `~/Developer/OpenSource/earn-e-p1/`.

## Conventions

- All modules use `from __future__ import annotations`
- Async/await throughout; all HA lifecycle methods are async
- Module-level `_LOGGER = logging.getLogger(__name__)`
- Type hints on all function signatures
- Follows standard Home Assistant integration structure and naming conventions
