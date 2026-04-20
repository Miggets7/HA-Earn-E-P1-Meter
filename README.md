# EARN-E P1 Meter

> ## ⚠️ Deprecated — now in Home Assistant core
>
> This integration has been merged into Home Assistant core and ships with
> Home Assistant out of the box. This custom component is no longer maintained
> here — please use the built-in integration instead (see [Installation](#installation-home-assistant-core) below).
>
> - Documentation: [home-assistant.io/integrations/earn_e_p1](https://www.home-assistant.io/integrations/earn_e_p1)
> - Upstream: [home-assistant/core](https://github.com/home-assistant/core)
> - Author's fork: [Miggets7/core](https://github.com/Miggets7/core)
>
> ---
>
> ## ⚠️ Verouderd — nu in Home Assistant core
>
> Deze integratie is samengevoegd in Home Assistant core en wordt standaard met
> Home Assistant meegeleverd. Deze custom component wordt hier niet langer
> onderhouden — gebruik in plaats daarvan de ingebouwde integratie (zie
> [Installatie](#installatie-home-assistant-core) hieronder).
>
> - Documentatie: [home-assistant.io/integrations/earn_e_p1](https://www.home-assistant.io/integrations/earn_e_p1)
> - Upstream: [home-assistant/core](https://github.com/home-assistant/core)
> - Fork van de auteur: [Miggets7/core](https://github.com/Miggets7/core)

[![GitHub Release][release-badge]][release-url]
[![License][license-badge]][license-url]

[release-badge]: https://img.shields.io/github/v/release/Miggets7/HA-Earn-E-P1-Meter
[release-url]: https://github.com/Miggets7/HA-Earn-E-P1-Meter/releases
[license-badge]: https://img.shields.io/github/license/Miggets7/HA-Earn-E-P1-Meter
[license-url]: https://github.com/Miggets7/HA-Earn-E-P1-Meter/blob/main/LICENSE

🇬🇧 [English](#english) | 🇳🇱 [Nederlands](#nederlands)

---

## English

Home Assistant integration for the [EARN-E energy monitor](https://earn-e.com/product/energiemonitor/). The EARN-E reads your smart meter's P1 port and broadcasts real-time energy data via UDP on the local network. This integration listens for those broadcasts and exposes them as sensor entities in Home Assistant.

### Features

- Automatic device discovery — no manual IP entry needed
- Real-time power and voltage/current updates (~1s)
- Energy and gas meter totals from full telegrams (~60s)
- WiFi signal strength monitoring
- All sensors grouped under a single device
- No cloud, no polling — pure local push via UDP

### Sensors

| Sensor | Unit | Update Frequency |
|--------|------|-----------------|
| Power Delivered | kW | ~1s |
| Power Returned | kW | ~1s |
| Voltage L1 | V | ~1s |
| Current L1 | A | ~1s |
| Energy Delivered Tariff 1 | kWh | ~60s |
| Energy Delivered Tariff 2 | kWh | ~60s |
| Energy Returned Tariff 1 | kWh | ~60s |
| Energy Returned Tariff 2 | kWh | ~60s |
| Gas Delivered | m³ | ~60s |
| WiFi RSSI | dBm | ~60s |

### Installation (Home Assistant core)

The integration is included in Home Assistant out of the box — no HACS, no
`custom_components/` copy needed. See the official docs:
[home-assistant.io/integrations/earn_e_p1](https://www.home-assistant.io/integrations/earn_e_p1).

1. Make sure Home Assistant is updated to a version that includes the
   integration.
2. Go to **Settings → Devices & Services → Add Integration**.
3. Search for **EARN-E** and select the integration.
4. Follow the setup prompts (automatic discovery on the local network; fallback
   to manual IP entry if needed).

### Setup

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for "EARN-E P1 Meter"
3. The integration will automatically listen for UDP broadcasts on port 16121 for ~10 seconds. If your EARN-E is found, you'll see a confirmation screen with its IP address — just confirm to finish setup.
4. If no device is discovered (e.g. the meter is on a different subnet), you'll be asked to enter the IP address manually.

Sensors will populate once the first data packets arrive.

### Removal

1. Go to **Settings → Devices & Services**
2. Click on the **EARN-E P1 Meter** integration
3. Click the three-dot menu (⋮) and select **Delete**

<details>
<summary>Legacy install (pre-core, custom component)</summary>

For users on a Home Assistant version that does not yet include the integration,
the custom component in this repo can still be installed manually:

#### HACS

1. Open HACS in Home Assistant
2. Go to **Integrations → ⋮ → Custom repositories**, add `https://github.com/Miggets7/HA-Earn-E-P1-Meter` with category **Integration**
3. Search for "EARN-E P1 Meter" and click **Download**
4. Restart Home Assistant

#### Manual

1. Copy `custom_components/earn_e_p1/` to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant

</details>

---

## Nederlands

Home Assistant integratie voor de [EARN-E energiemonitor](https://earn-e.com/product/energiemonitor/). De EARN-E leest de P1-poort van je slimme meter en verstuurt realtime energiedata via UDP over het lokale netwerk. Deze integratie luistert naar die uitzendingen en maakt ze beschikbaar als sensorentiteiten in Home Assistant.

### Kenmerken

- Automatische apparaatdetectie — geen handmatige IP-invoer nodig
- Realtime vermogen- en spanning/stroomupdates (~1s)
- Energie- en gasmetertellingen uit volledige telegrammen (~60s)
- WiFi-signaalsterkte monitoring
- Alle sensoren gegroepeerd onder één apparaat
- Geen cloud, geen polling — puur lokale push via UDP

### Sensoren

| Sensor | Eenheid | Updatefrequentie |
|--------|---------|-----------------|
| Vermogen geleverd | kW | ~1s |
| Vermogen teruggeleverd | kW | ~1s |
| Spanning L1 | V | ~1s |
| Stroom L1 | A | ~1s |
| Energie geleverd tarief 1 | kWh | ~60s |
| Energie geleverd tarief 2 | kWh | ~60s |
| Energie teruggeleverd tarief 1 | kWh | ~60s |
| Energie teruggeleverd tarief 2 | kWh | ~60s |
| Gas geleverd | m³ | ~60s |
| WiFi RSSI | dBm | ~60s |

### Installatie (Home Assistant core)

De integratie zit standaard in Home Assistant — geen HACS of `custom_components/`
kopie nodig. Zie de officiële documentatie:
[home-assistant.io/integrations/earn_e_p1](https://www.home-assistant.io/integrations/earn_e_p1).

1. Zorg dat Home Assistant is bijgewerkt naar een versie die de integratie bevat.
2. Ga naar **Instellingen → Apparaten & Services → Integratie toevoegen**.
3. Zoek naar **EARN-E** en selecteer de integratie.
4. Volg de installatiestappen (automatische detectie op het lokale netwerk;
   handmatige IP-invoer als terugval).

### Instellen

1. Ga naar **Instellingen → Apparaten & Services → Integratie toevoegen**
2. Zoek naar "EARN-E P1 Meter"
3. De integratie luistert automatisch ~10 seconden naar UDP-uitzendingen op poort 16121. Als je EARN-E wordt gevonden, verschijnt een bevestigingsscherm met het IP-adres — bevestig om de installatie af te ronden.
4. Als er geen apparaat wordt gevonden (bijv. de meter staat op een ander subnet), wordt gevraagd om het IP-adres handmatig in te voeren.

Sensoren worden gevuld zodra de eerste datapakketten binnenkomen.

### Verwijderen

1. Ga naar **Instellingen → Apparaten & Services**
2. Klik op de **EARN-E P1 Meter** integratie
3. Klik op het drie-puntjes menu (⋮) en selecteer **Verwijderen**

<details>
<summary>Verouderde installatie (pre-core, custom component)</summary>

Voor gebruikers met een Home Assistant versie die de integratie nog niet bevat,
kan de custom component uit deze repo nog handmatig worden geïnstalleerd:

#### HACS

1. Open HACS in Home Assistant
2. Ga naar **Integraties → ⋮ → Aangepaste repositories**, voeg `https://github.com/Miggets7/HA-Earn-E-P1-Meter` toe met categorie **Integratie**
3. Zoek naar "EARN-E P1 Meter" en klik op **Downloaden**
4. Herstart Home Assistant

#### Handmatig

1. Kopieer `custom_components/earn_e_p1/` naar de `config/custom_components/` map van je Home Assistant
2. Herstart Home Assistant

</details>
