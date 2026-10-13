---
title: "The Best Way to Fix Intel Wi-Fi 6 AX201 Not Working"
slug: best-way-to-fix-intel-wifi-6-ax201-not-working
date: 2026-09-19
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "intel wireless", "wlan driver", "code 10"]
description: "Intel Wi-Fi 6 AX201 not working or showing Code 10? Install the correct Intel WLAN driver, fix power management, and restore Wi-Fi 6 connectivity."
thumbnail: "/images/thumbs/best-way-to-fix-intel-wifi-6-ax201-not-working.webp"
faqs:
  - q: "Why does my Intel AX201 show a Code 10 error?"
    a: "Code 10 means the driver failed to start the device, and on the AX201 it usually traces to a driver version mismatch with your Windows build or a corrupted driver installation. The AX201 is particularly sensitive to driver versions because it shares firmware duties with the chipset's connectivity engine. A clean install of the Intel-recommended driver for your exact Windows build resolves it in most cases."
  - q: "Should I get the AX201 driver from Intel or my laptop maker?"
    a: "Start with your laptop maker's support page, because some manufacturers customize the AX201 driver for their antenna and power design. If the maker's driver is old and broken, Intel's generic driver from the Intel Driver and Support Assistant is the next best option and works on the vast majority of laptops. Avoid third-party driver sites entirely."
  - q: "Can the AX201 disappear completely from Device Manager?"
    a: "Yes. When the driver fails badly or the card is power-gated, the AX201 can vanish from Device Manager entirely, sometimes not even appearing as a hidden device. Check the BIOS wireless toggle first, then power-drain the laptop to force bus re-enumeration. If it never reappears, the module may have failed."
  - q: "Does the AX201 need a specific Windows version for Wi-Fi 6?"
    a: "The AX201 needs Windows 10 version 2004 or later, or Windows 11, for full Wi-Fi 6 (802.11ax) support with the right driver. On older Windows builds the card may work but fall back to Wi-Fi 5 speeds or fail to initialize. Keep both Windows and the Intel driver current to hold the 802.11ax connection."
---

The Intel Wi-Fi 6 AX201 is one of the most common wireless cards in modern laptops — and one of the most troublesome when its driver goes wrong. The typical failure signature is distinctive: the adapter shows a yellow warning with **Code 10** (device cannot start), or it vanishes from Device Manager entirely, or Wi-Fi works but crawls at a fraction of its rated speed. The AX201's tight integration with the Intel chipset makes it fussier about driver versions than older cards.

The fix sequence below is ordered for this specific card: verify the right driver generation, do a true clean install (the AX201 remembers bad installs stubbornly), then address the power and firmware quirks that are unique to Intel's 6-series wireless.

## Why this happens

- **Driver/Windows build mismatch:** The AX201 requires matched driver and Windows builds. A driver meant for a newer Windows release can throw Code 10 on an older one.
- **Windows Update installed the wrong generation:** Windows Update sometimes pushes a generic Intel wireless driver that lacks the AX201-specific firmware handshake.
- **Corrupted driver store entry:** Partial uninstalls leave fragments in the driver store, and the AX201 re-detects the broken copy on every reinstall attempt.
- **Power management starving the card:** The AX201 is sensitive to PCIe link-state power management; aggressive settings can prevent it from initializing at boot.
- **Firmware handshake failure:** The AX201 loads firmware from the driver at startup. If that handshake fails, the card either errors or disappears.
- **Antenna or M.2 seating issues:** The AX201 uses a CNVio2 interface on many boards — a partially seated module fails in ways that look exactly like driver problems.
- **BIOS wireless settings reset:** BIOS updates occasionally flip the WLAN toggle or change the wireless mode, hiding or crippling the card.
- **Conflicting VPN or filter drivers:** Third-party network filter drivers can block the AX201's initialization sequence even when the Intel driver itself is correct.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact failure mode in Device Manager

1. Press **Win + X**, open **Device Manager**, and expand **Network adapters**.
2. Note exactly what you see: **Intel Wi-Fi 6 AX201** with a yellow warning, a greyed-out hidden entry, or nothing at all. Each points to a different fix path.
3. If there is a warning, open **Properties** and read the error code — **Code 10** means driver start failure, **Code 45** means hardware not connected.
4. Check the **Driver** tab and note the current version and date. Drivers older than your Windows feature update are prime suspects.
5. If the card is completely absent, enable **View → Show hidden devices** first — a hidden AX201 changes the diagnosis from "hardware gone" to "driver failed," matching the pattern in the [missing adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-youtube/).

### Fix 2: Run Intel Driver & Support Assistant for the matched driver

1. Go to [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and install the detection tool.
2. Let it scan your system — it identifies your exact AX201 revision and Windows build, then offers the validated driver.
3. Install the recommended wireless driver and restart.
4. Verify in Device Manager that the warning is gone and the driver date is current.
5. Intel's tool is the safest source for AX201 drivers because it enforces the driver-to-OS-build matching this card demands. If your laptop maker customizes wireless drivers, try their support page first ([Dell](https://www.dell.com/support)).

### Fix 3: Perform a true clean install with driver store purge

1. In Device Manager, right-click the AX201 and choose **Uninstall device**, checking **Attempt to remove the driver for this device**.
2. Open an elevated Command Prompt and run `pnputil /enum-drivers` to list third-party drivers.
3. Find entries with **Intel** and **Wireless/Netwtw** in the name, then remove each with `pnputil /delete-driver oemXX.inf /uninstall` (replace oemXX with the actual number).
4. Restart, then install the fresh driver from Fix 2.
5. This purge matters because the AX201 aggressively reuses driver store fragments; a surface-level uninstall often "reinstalls" the same broken driver. The same clean-install discipline fixes [Wi-Fi 6 issues generally](/articles/best-way-to-fix-wifi-6-not-working-on-laptop/).

### Fix 4: Disable power management strangling the card

1. In Device Manager, open the AX201's **Properties → Power Management** and uncheck **Allow the computer to turn off this device to save power**.
2. Go to **Power Options → Change advanced power settings → Wireless Adapter Settings → Power Saving Mode** and set both profiles to **Maximum Performance**.
3. In the adapter's **Properties → Advanced** tab, find **Transmit Power** and set it to **Highest** if available.
4. Restart and test. AX201 cards that vanish after sleep or fail to initialize on cold boot are frequently victims of PCIe power gating rather than bad drivers.
5. If your BIOS has ASPM (Active State Power Management) settings for wireless, try disabling them as a test — re-enable if it makes no difference.

### Fix 5: Update the BIOS and chipset drivers

1. Check your laptop maker's support page for a BIOS update mentioning wireless, WLAN, or Intel connectivity fixes.
2. Install the latest **chipset driver** package too — the AX201's CNVio2 interface depends on chipset components initializing correctly.
3. Apply BIOS updates only with the charger connected and the battery charged; never interrupt the process.
4. After updating, enter BIOS setup and confirm the **WLAN/Wireless** toggle is still enabled — updates sometimes reset it.
5. Retest wireless. On several laptop lines, an Intel chipset driver update alone resolved chronic AX201 Code 10 errors that driver reinstalls could not.

### Fix 6: Remove conflicting network filter drivers

1. In Device Manager with hidden devices shown, expand **Non-Plug and Play Drivers** and look for third-party network filters from VPN clients or old security software.
2. Open **Settings → Network & internet → Advanced network settings** and check for extra virtual adapters from VPNs you no longer use — remove the software properly through **Apps**.
3. In the AX201's connection properties (**ncpa.cpl** → right-click Wi-Fi → Properties), uncheck non-essential items like third-party protocols, keeping the standard Microsoft items.
4. Restart and test the AX201 in isolation.
5. Reinstall VPN software afterward if you need it — modern versions coexist with the AX201 far better than older ones.

### Fix 7: Force 802.11ax mode and correct band settings

1. In the AX201's **Properties → Advanced** tab, locate **802.11a/b/g Wireless Mode** or **VHT Mode** and set it to allow ax/HE rates.
2. Set **Preferred Band** to **Prefer 5GHz** if your router supports Wi-Fi 6 on 5GHz — this avoids the card camping on a congested 2.4GHz band at low rates.
3. Set **Roaming Aggressiveness** to **Medium** (level 3) — the highest setting can cause disconnect loops on some access points.
4. Apply, restart the adapter (disable/enable it in Device Manager), and run a speed test.
5. If speeds are still poor, test against a different Wi-Fi 6 router before blaming the card — many "AX201 slow" reports turn out to be router-side issues.

### Fix 8: Power-drain and reseat to rule out hardware

1. Shut down, unplug, remove the battery if possible, and hold the power button **30 seconds** to force full bus re-enumeration on next boot.
2. If the card appears after the drain but fails again later, suspect a seating or thermal issue.
3. On models with a socketed M.2/CNVio2 module, reseating the card and its antenna leads (black and white wires, noting their positions) can fix intermittent detection — follow your model's service manual.
4. If the card never appears in any view after all software fixes, the module has likely failed electrically.
5. A USB Wi-Fi adapter is a cheap stopgap, but for a soldered-down AX201 that has died, manufacturer service is the real answer.

## Closing

The AX201 rewards precision: the right driver matched to your Windows build, installed truly clean with the driver store purged, and freed from aggressive power management. Code 10 errors and vanishing adapters on this card are software problems in the overwhelming majority of cases. When they persist after a power drain and reseat, the module itself is done.
