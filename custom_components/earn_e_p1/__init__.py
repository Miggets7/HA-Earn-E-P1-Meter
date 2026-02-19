"""The EARN-E P1 Meter integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant

from .coordinator import EarnEP1Coordinator

PLATFORMS: list[Platform] = [Platform.SENSOR]

type EarnEP1ConfigEntry = ConfigEntry[EarnEP1Coordinator]


async def async_setup_entry(hass: HomeAssistant, entry: EarnEP1ConfigEntry) -> bool:
    """Set up EARN-E P1 Meter from a config entry."""
    coordinator = EarnEP1Coordinator(hass, entry.data[CONF_HOST])
    await coordinator.async_start()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: EarnEP1ConfigEntry) -> bool:
    """Unload a config entry."""
    await entry.runtime_data.async_stop()
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
