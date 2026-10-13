---
title: "What to Do If Your MediaTek Wi-Fi Is Not Working"
slug: what-to-do-if-mediatek-wifi-not-working
date: 2026-09-01
categories: ["drivers"]
tags: ["mediatek wifi", "mt7921", "mt7922", "wifi not working", "wireless driver"]
description: "MediaTek Wi-Fi not working on your laptop? Fix the MT7921/MT7922 issues — disconnects, missing adapter, and slow speeds — with the right driver approach."
thumbnail: "/images/thumbs/what-to-do-if-mediatek-wifi-not-working.webp"
faqs:
  - q: "Why is MediaTek Wi-Fi worse than Intel on laptops?"
    a: "It is less about the hardware and more about driver maturity and Windows Update behavior. MediaTek cards like the MT7921 and MT7922 are capable chips, but their Windows drivers have historically had more power-management and sleep-wake bugs than Intel's, and Windows Update frequently replaces the working manufacturer driver with a problematic generic one. With the correct manufacturer driver installed and power management tuned, MediaTek Wi-Fi is generally stable — most complaints trace to those two fixable issues."
  - q: "Should I replace my MediaTek card with an Intel AX210?"
    a: "It is the most reliable permanent fix and a popular upgrade. The Intel AX210 is inexpensive, fits the same M.2 2230 slot, and has far more mature Windows drivers. Before buying, verify your laptop does not have a BIOS whitelist blocking non-approved cards (most modern laptops do not) and that the antenna connectors match. If you would rather not open the laptop, the driver fixes in this guide resolve most MediaTek issues without hardware changes."
  - q: "Why does my MediaTek Wi-Fi disconnect when the laptop sleeps?"
    a: "MediaTek drivers have well-documented issues with modern standby and sleep-wake cycles: the card fails to reinitialize properly, showing as disconnected or vanished until a restart. The most effective fixes are disabling 'allow the computer to turn off this device' in the adapter's power management, updating to the manufacturer's latest driver, and disabling Fast Startup. If disconnects persist only after sleep, these three steps resolve the large majority of cases."
  - q: "Where do I get the correct MediaTek Wi-Fi driver?"
    a: "From your laptop manufacturer's support site, not from MediaTek directly and not from Windows Update. Laptop makers customize the driver package with card-specific firmware and regulatory settings for their antenna design. Download the wireless driver for your exact laptop model from Dell, HP, Lenovo, or ASUS support. Only if the manufacturer has abandoned the model should you try MediaTek's generic driver or a newer driver extracted from another OEM's package."
---

MediaTek Wi-Fi cards — the MT7921 and MT7922 found in countless Ryzen and budget Intel laptops — have a reputation. Disconnects, vanishing adapters, sluggish speeds, and sleep-wake failures fill forums with complaints. The hardware itself is decent; the problems are almost entirely driver and power-management issues, which means they are fixable without opening the laptop.

This guide covers the MediaTek-specific fixes that general Wi-Fi guides miss: the right driver source, the power settings that matter most for these cards, and the settings that stabilize them. Work through in order — most MediaTek issues resolve by Fix 4.

## Why this happens

- **Windows Update replaced the OEM driver:** The single biggest MediaTek issue. Windows installs a generic MediaTek driver that lacks the laptop-specific firmware tuning, and stability collapses.
- **Aggressive power management:** MediaTek cards are sensitive to Windows powering down the adapter. The card often fails to wake cleanly, causing disconnects or a vanished adapter.
- **Modern standby incompatibility:** The card's firmware and Windows modern standby do not always agree, producing the classic "Wi-Fi gone after sleep" failure.
- **Outdated card firmware:** The driver package includes firmware for the card itself. Old firmware has known bugs around roaming, band steering, and WPA3 that newer firmware fixes.
- **Roaming aggressiveness:** MediaTek's default roaming sensitivity can cause the card to hop between access points or bands unnecessarily, manifesting as random disconnects.
- **2.4 GHz / 5 GHz band issues:** Some MediaTek driver versions handle band transitions poorly, dropping the connection when the router steers the client between bands.
- **Antenna design variance:** Budget laptops sometimes pair the MediaTek card with minimal antenna implementations, so driver-level signal problems hit harder than on premium machines.
- **Bluetooth coexistence bugs:** MediaTek combo cards share radio resources between Wi-Fi and Bluetooth. Buggy coexistence handling causes Wi-Fi drops when Bluetooth is active.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your exact card and current driver

MediaTek-specific fixes require knowing exactly what you have.

1. Open **Device Manager → Network adapters** and note the exact adapter name (e.g., "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card") and current driver version (**Properties → Driver**).
2. Check whether the driver provider is **MediaTek** or **Microsoft**. A Microsoft-provider driver on a MediaTek card is the generic replacement — the prime suspect.
3. Note the failure pattern: disconnects only, vanishing adapter, slow speeds, or sleep-related. Each pattern weights the later fixes differently.
4. Write down your laptop's exact model number from the bottom label — you will need it to get the correct OEM driver. General Wi-Fi disappearance is covered in our [Wi-Fi disappeared guide](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 2: Install the manufacturer's MediaTek driver

This is the fix that resolves the most MediaTek complaints. Do not skip to generic drivers first.

1. Go to your laptop manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and download the wireless/Wi-Fi driver for your exact model.
2. In Device Manager, uninstall the current Wi-Fi adapter, checking **Delete the driver software** to remove the generic driver completely.
3. Restart, then install the downloaded OEM driver package. These packages include the matched firmware blob for the card.
4. Verify the driver provider now shows the manufacturer or MediaTek (not Microsoft) and test for a full day, including sleep/wake cycles, before judging the result.

### Fix 3: Tame power management for the MediaTek card

MediaTek cards need gentler power handling than Windows applies by default.

1. In **Device Manager → adapter → Properties → Power Management**, uncheck **Allow the computer to turn off this device to save power**.
2. Go to **Control Panel → Power Options → Change advanced power settings → Wireless Adapter Settings → Power Saving Mode** → set to **Maximum Performance** on battery and plugged in.
3. In the adapter's **Properties → Advanced** tab, look for **Power Saving Mode** or similar properties and set them to **Maximum Performance** / disabled power saving.
4. Disable **Fast Startup** (**Control Panel → Power Options → Choose what the power buttons do**). Fast Startup's hybrid shutdown is a frequent trigger for MediaTek sleep-wake failures.

### Fix 4: Tune the Advanced adapter properties

MediaTek-specific settings that stabilize flaky connections.

1. In the adapter's **Properties → Advanced** tab, find **Roaming Aggressiveness** and set it to **1. Lowest** (or **Disabled** if available). Aggressive roaming is a top cause of random MediaTek disconnects.
2. Look for **Preferred Band** — if your router has band-steering issues, try locking it to **5 GHz** (or 2.4 GHz if range matters more than speed) instead of automatic.
3. Find **802.11a/b/g Wireless Mode** or **VHT Mode** settings and ensure they match your router's capabilities; mismatched mode advertisements cause negotiation failures.
4. If a **Bluetooth Collaboration** or **Coexistence** setting exists, try toggling it — some driver versions handle Bluetooth coexistence better with it explicitly enabled. Related adapter-visibility issues are in our [Wi-Fi adapter not showing up guide](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).

### Fix 5: Update the card firmware via the newest OEM package

The firmware inside the driver package matters as much as the driver.

1. Check the manufacturer's support page again for a newer Wi-Fi driver than the one you installed — OEMs periodically refresh the package with new card firmware.
2. Some ASUS and Lenovo models distribute MediaTek firmware updates through **MyASUS** or **Lenovo Vantage** rather than the manual download page — check those utilities too.
3. After updating, forget and rejoin your Wi-Fi network (**Settings → Network → Manage known networks → Forget**, then reconnect). Stale network profiles can conflict with new firmware behavior.
4. Test WPA3 networks specifically if you use them — several MediaTek firmware revisions fixed WPA3 handshake bugs that caused repeated disconnects.

### Fix 6: Block Windows from replacing the working driver

MediaTek setups are fragile across updates; protect the working combination.

1. Once you have a stable driver, note its exact version.
2. On Windows Pro, enable **Do not include drivers with Windows Updates** in Group Policy (**gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Windows Update → Manage updates offered from Windows Update**).
3. Alternatively, use the **Show or hide updates** troubleshooter to hide the MediaTek driver update specifically.
4. After every major Windows feature update, verify the driver provider is still correct — feature updates are the most likely to silently swap the driver back.

### Fix 7: Consider the Intel AX210 upgrade

When driver tuning is not enough, the hardware swap is cheap and definitive.

1. Verify your laptop uses a standard **M.2 2230** Wi-Fi card (most do) and does not have a BIOS whitelist — check your model's forum or manual.
2. Buy an **Intel AX210** (Wi-Fi 6E) card — inexpensive, widely available, and dramatically better supported on Windows.
3. Power down, remove the bottom panel, swap the card, and reconnect the two antenna wires (main/black and aux/white — note positions before removing).
4. On first boot, install the Intel Wi-Fi driver from Intel's official driver support site. The improvement in stability is usually immediate and obvious.

## Closing

MediaTek Wi-Fi's bad reputation is really a driver-management problem: Windows replaces the tuned OEM driver with a generic one, power management fights the card, and roaming defaults cause disconnects. The OEM driver plus tamed power settings fixes the large majority of cases. And for the stubborn remainder, a thirty-dollar Intel card swap ends the saga permanently — sometimes the best driver fix is a hardware upgrade.
