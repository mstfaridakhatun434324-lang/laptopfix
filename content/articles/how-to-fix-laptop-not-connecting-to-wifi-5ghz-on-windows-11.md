---
title: "Fix a Laptop That Won't Connect to 5GHz Wi-Fi on Windows 11"
slug: how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-11
date: 2026-09-03
categories: ["drivers"]
tags: ["5ghz wifi", "wifi not connecting", "windows 11", "wireless adapter", "wifi 6"]
description: "Fix Windows 11 laptops that can't see or join 5GHz Wi-Fi: band preference settings, driver repair, and router channel compatibility."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-11.webp"
faqs:
  - q: "Why can't my Windows 11 laptop find 5GHz networks?"
    a: "The adapter may be 2.4GHz-only hardware, the driver may have the 5GHz band disabled, or the router may broadcast on DFS channels or 160MHz widths the adapter cannot use. Check radio capability with netsh wlan show drivers first."
  - q: "Where is the preferred band setting in Windows 11?"
    a: "Open Device Manager, expand Network adapters, right-click your Wi-Fi adapter, and open Properties, then the Advanced tab. Set Preferred Band to Prefer 5GHz band — the exact label varies between Intel, Realtek, and Qualcomm drivers, but every 5GHz-capable driver exposes some version of this setting."
  - q: "Why does my laptop see 5GHz but fail to connect?"
    a: "Failed association on a visible 5GHz network usually means a corrupted saved profile, an incompatible router channel or width setting, or a driver bug in the 5GHz radio path. Forget the network in Wi-Fi settings, reconnect fresh, and check that the router uses a non-DFS channel at 80MHz width."
  - q: "Is 5GHz always better than 2.4GHz on a laptop?"
    a: "For speed near the router, yes — 5GHz is much faster. For range through walls, 2.4GHz wins. If your laptop sits far from the router, the 2.4GHz band may genuinely be the better connection despite the slower headline speed."
---

Windows 11 laptops that cannot see or join 5GHz Wi-Fi networks are usually dealing with one of three things: a driver that has the 5GHz band disabled, a router broadcasting on channels or widths the adapter cannot use, or — the honest answer in some cases — a 2.4GHz-only radio. Sorting hardware capability from software blockage first saves you from "fixing" something unfixable, and the check takes seconds.

The 5GHz path involves the adapter driver, Windows' WLAN profiles, and the router's radio settings. The sequence below walks all three layers in the order that resolves most cases: capability, band preference, driver, router, then stack reset.

## Why this happens

- **5GHz band disabled in adapter settings:** Preferred Band forced to 2.4GHz, or VHT/802.11a modes turned off in the driver's Advanced tab.
- **2.4GHz-only adapter hardware:** Budget and older laptops ship single-band radios with no 5GHz capability at all.
- **Router on DFS channels:** Channels 52–144 require radar detection; many laptop adapters cannot use them, making the network invisible.
- **160MHz channel width unsupported:** Older 5GHz adapters top out at 80MHz; a router set to 160MHz-only can be unjoinable.
- **Corrupted saved network profile:** A stale profile with wrong security or band data fails association even though the network is visible.
- **Driver replaced by Windows Update:** A generic driver without proper 5GHz/band-steering support replaces the vendor driver.
- **Band steering hiding the SSID:** Router features that merge bands can keep the laptop pinned to 2.4GHz.
- **Power management throttling the radio:** The higher-power 5GHz chain is the first thing aggressive power saving shuts down.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check 5GHz radio capability

1. Open Command Prompt and run `netsh wlan show drivers`.
2. Under **Radio types supported**, look for **802.11a**, **802.11ac**, or **802.11ax** — any of these means 5GHz hardware is present.
3. Only **802.11b/g/n** means 2.4GHz-only hardware: the answer is a USB Wi-Fi adapter, and no software step below applies.
4. With 5GHz hardware confirmed, continue — the blockage is software or router-side.

### Fix 2: Force the preferred band to 5GHz

1. **Device Manager → Network adapters** → right-click your Wi-Fi adapter → **Properties → Advanced**.
2. Set **Preferred Band** to **5. Prefer 5GHz band** (wording varies: "Prefer 5G band" on some drivers).
3. Enable **VHT Mode** if present; set **802.11a/b/g Wireless Mode** to include **a**.
4. Click OK, then rescan networks (**Settings → Network & internet → Wi-Fi → Show available networks**). This single setting resolves a large fraction of cases.

### Fix 3: Delete the corrupted profile and reconnect

1. Go to **Settings → Network & internet → Wi-Fi → Manage known networks**, select the 5GHz network, and **Forget** it.
2. Rescan and reconnect, entering the password fresh.
3. If it fails, open Command Prompt and run `netsh wlan delete profile name="SSID"` for a deeper removal, then reconnect.
4. Corrupted profiles are the top cause of "I can see it but can't join" — the radio is fine, the saved handshake data is not.

### Fix 4: Reinstall the wireless driver

1. Note your adapter model in Device Manager, then download the Wi-Fi driver from your vendor — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for Intel adapters.
2. Right-click the adapter → **Uninstall device**, checking **Attempt to remove the driver**.
3. Reboot and install the downloaded driver.
4. Windows Update drivers for Wi-Fi adapters are a frequent source of band-preference regressions; the vendor package restores proper 5GHz behavior. The same driver hygiene helps other wireless faults described in the [Intel AX201 guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

### Fix 5: Fix the router's 5GHz radio settings

1. Log into the router admin page and open the 5GHz wireless settings.
2. Ensure the 5GHz radio is **enabled** with SSID broadcast on (or note the exact hidden SSID).
3. Change the channel to **36, 40, 44, or 48** (non-DFS) and set channel width to **80MHz** or **20/40/80MHz auto**.
4. Temporarily disable band steering / Smart Connect and give the 5GHz network its own SSID (e.g., "Home-5G") for testing.
5. Reboot the router after changes and rescan from the laptop.

### Fix 6: Disable adapter power management

1. In the adapter's **Properties → Power Management**, uncheck **Allow the computer to turn off this device to save power**.
2. In the **Advanced** tab, set **Power Saving Mode** to **Maximum Performance** and **Transmit Power** to **5. Highest**.
3. **Settings → System → Power & battery → Power mode → Best performance** while testing.
4. If 5GHz appears on AC power but vanishes on battery, power management was the culprit.

### Fix 7: Reset the network stack

1. Elevated Command Prompt: `netsh winsock reset`, `netsh int ip reset`, then reboot.
2. Or **Settings → Network & internet → Advanced network settings → Network reset**.
3. After the reset, reinstall the vendor Wi-Fi driver (Windows uses generic drivers post-reset) and reconfigure the band preference (Fix 2).
4. If 5GHz works in a Linux live USB but not in Windows after all this, a clean Windows network stack rebuild via `netsh` plus vendor drivers is the definitive software answer — documented further in [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

If the laptop loses the entire Wi-Fi option rather than just the 5GHz band, that is a deeper adapter failure — the [vanished Wi-Fi adapter guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers diagnosis for a completely missing wireless device. The 5GHz mystery always resolves to capability, preference, driver, or router — checked in that order. `netsh wlan show drivers` settles capability in seconds; the Preferred Band setting and a clean vendor driver fix most software blockages; non-DFS channels at 80MHz fix most router-side invisibility. When the hardware is genuinely single-band, say so plainly and recommend a USB adapter rather than promising a software miracle.
