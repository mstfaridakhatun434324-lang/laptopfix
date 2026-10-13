---
title: "Network Adapter Missing from Device Manager? Restore Wi-Fi and Ethernet"
slug: what-to-do-if-network-adapter-missing
date: 2026-10-03
categories: ["drivers"]
tags: ["network adapter missing", "wifi adapter missing", "ethernet not detected", "device manager network", "windows 11"]
description: "Network adapter missing from Device Manager? Bring back vanished Wi-Fi and Ethernet adapters with driver reinstalls, BIOS checks, and power-drain resets."
thumbnail: "/images/thumbs/what-to-do-if-network-adapter-missing.webp"
faqs:
  - q: "Why did my Wi-Fi adapter disappear from Device Manager?"
    a: "The Wi-Fi adapter usually vanishes because its driver failed to load — Windows Update replacing the manufacturer's wireless driver is the top cause — or the adapter got disabled at the BIOS or function-key level. Showing hidden devices in Device Manager reveals whether it's disabled, failed with an error code, or truly unseen, which determines the fix."
  - q: "Can airplane mode hide the network adapter?"
    a: "Airplane mode disables the radios but shouldn't remove the adapter from Device Manager. However, some laptops' airplane-mode implementations and function-key toggles do cut power to the wireless card in ways that make it vanish from the device list. If the adapter disappeared after touching a function key, press it again and restart before doing driver work."
  - q: "Why is my Ethernet adapter missing but Wi-Fi works?"
    a: "The two adapters are independent devices with separate drivers, so one can vanish while the other works. A missing Ethernet adapter specifically suggests its driver failed, it was disabled in BIOS, or the port's controller has an issue. USB Ethernet adapters can also disappear if USB selective suspend cuts their power — a different fix from PCI wireless cards."
  - q: "Does resetting the network settings bring back a missing adapter?"
    a: "Network reset (Settings, Network and internet, Advanced network settings, Network reset) reinstalls network components and usually restores adapters hidden by configuration corruption — but it cannot fix a missing driver or a BIOS-disabled card. Use it after driver reinstallation fails, not before; and note it forgets all saved Wi-Fi networks."
---

A missing network adapter is the "no internet" problem at its most fundamental: not a wrong password or a router issue, but Windows genuinely unable to see the Wi-Fi or Ethernet hardware. Device Manager's Network adapters section is empty of the expected entry, the Wi-Fi toggle vanishes from quick settings, and the taskbar shows the dreaded globe icon. The causes split cleanly: driver failure (most common), disabled at some layer (BIOS, function key, Device Manager), or hardware death (rare). The diagnostic sequence below identifies which in minutes.

Note which adapter is missing — Wi-Fi, Ethernet, or both — because they have independent drivers and the fixes diverge.

## Why this happens

- **Wireless driver replaced by Windows Update.** The dominant cause — a generic or broken driver that fails to load.
- **Adapter disabled in BIOS/UEFI.** Firmware-level disable hiding the card from Windows.
- **Function-key or airplane-mode radio kill.** Power cut to the wireless card at the hardware level.
- **Adapter disabled in Device Manager.** Accidental disable or a "tuning" utility's work.
- **Corrupted network stack.** Configuration corruption hiding a healthy adapter.
- **Failed wireless card.** Hardware death — rare, confirmed by elimination.
- **USB selective suspend (USB adapters).** Power cut to USB Wi-Fi/Ethernet dongles.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the radio kill switches

The fastest tier — hardware-level disables mimic driver failure.

1. Toggle **airplane mode** off (taskbar quick settings) — then toggle it on and back off to reset radio state.
2. Press the **wireless function key** (Fn+F2/F5 or a radio-tower icon key) — the classic accidental trigger.
3. Check for a **physical wireless switch** on the laptop's side edge (still present on some business models).
4. Restart after toggling — radio power-state changes don't always register without a reboot.
5. If the adapter reappears in Device Manager after this, you had a radio kill, not a driver problem — stop here.

### Fix 2: Reveal the adapter in Device Manager

See what Windows actually thinks about the hardware.

1. **Device Manager > View > Show hidden devices** → expand **Network adapters**.
2. Grayed-out adapter → right-click → **Enable device**. Note any error code: **Code 45** (disconnected), **Code 10** (failed to start), **Code 31** (driver failed).
3. Check under **Other devices** for unknown "Network Controller" entries — the adapter without a bound driver.
4. If the adapter appears here but not in the normal view, it's a driver or disable issue, not hardware absence.
5. For the full hidden-device method, see [how to enable hidden devices in Device Manager](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/).

### Fix 3: Reinstall the network driver

The core fix for driver-vanished adapters.

1. Identify your adapter: Intel, Realtek, MediaTek, or Qualcomm — note the exact model from the hidden-device view or your laptop's specs.
2. On another device if needed, download the **Wi-Fi/Ethernet driver** from your laptop maker's support page.
3. In Device Manager, right-click the adapter (or unknown Network Controller) → **Uninstall device** → check "delete the driver software."
4. Install the downloaded driver and **restart**.
5. Intel wireless cards: the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) provides the newest Wi-Fi and Bluetooth drivers reliably.
6. Verify the adapter appears normally in Device Manager and the Wi-Fi toggle returns to quick settings.

The driver-reinstall pattern matches the broader method in [how to update drivers on a Windows 11 laptop](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 4: Power-drain the wireless card

For adapters that vanish intermittently or after sleep.

1. Shut down fully (Shift + Shut down to bypass fast startup).
2. Unplug AC and all peripherals; hold the power button **30 seconds**.
3. Boot on AC power only and check Device Manager immediately.
4. This resets the embedded controller's power state for the wireless card — a common fix for cards that vanish after sleep/wake cycles.
5. If the adapter appears after drain but vanishes again after sleep, update the **BIOS** — sleep/wake card-power bugs are firmware issues.

### Fix 5: Check BIOS network settings

Firmware can hide the adapter completely.

1. Enter **BIOS/UEFI** → look under **Advanced**, **Devices**, or **Security** for **Wireless**, **WLAN**, or **LAN** toggles.
2. Ensure both wireless and Ethernet (if applicable) are **Enabled**.
3. **Load optimized defaults**, save, and exit — clears corrupted firmware configuration.
4. Recheck Device Manager in Windows after booting.
5. If the BIOS's own hardware inventory doesn't list the wireless card, suspect hardware (Fix 7) — but only after the drain in Fix 4.

### Fix 6: Reset the network stack

For configuration corruption hiding a healthy adapter.

1. **Terminal (Admin)**: run `netsh winsock reset` and `netsh int ip reset`, then restart.
2. **Settings > Network & internet > Advanced network settings > Network reset** → Reset now — this reinstalls all network components.
3. Note: network reset **forgets all saved Wi-Fi networks** — have passwords handy.
4. After reset and reboot, reinstall the manufacturer's wireless driver (Fix 3) if the adapter is still missing — reset doesn't fix driver problems.
5. Check [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows) for known network issues with your build if problems persist.

### Fix 7: Verify the hardware

The final verdict on the card.

1. Boot a **Linux live USB** — if the wireless card appears there (`lspci`), it's alive and Windows is the problem.
2. For **USB Wi-Fi/Ethernet adapters**: test in different ports, disable USB selective suspend, and test the adapter on another computer.
3. Internal wireless cards are usually replaceable **M.2 modules** (Intel AX210-class) where socketed — a cheap part and a moderate DIY job.
4. If Wi-Fi is dead but Ethernet works (or vice versa), only the failed adapter needs attention — they're independent.
5. A **USB wireless adapter** is an instant, cheap workaround while you arrange internal repair.

## Closing

A missing network adapter is a visibility problem, and visibility has layers: radio kill switches, Device Manager disables, driver failures, BIOS toggles, and finally hardware. The hidden-devices check plus the error code tells you which layer in under a minute — Code 45/31 means driver, total absence after BIOS checks means hardware. Reinstall the manufacturer's driver (not Windows' generic), power-drain the card if it's intermittent, and save the hardware verdict for the Linux live-USB test. Internet access feels like oxygen, but the fix is almost always terrestrial.
