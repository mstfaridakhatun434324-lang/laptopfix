---
title: "MediaTek WiFi Not Working on Windows 10? Complete Fix Guide"
slug: how-to-fix-mediatek-wifi-not-working-on-windows-10
date: 2026-10-13
categories: ["drivers"]
tags: ["mediatek wifi", "windows 10", "mt7921", "wifi driver", "code 10"]
description: "MediaTek WiFi not working on Windows 10? Fix dead adapters, Code 10 errors, and sleep-related WiFi death with 7 proven repairs."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-on-windows-10.webp"
faqs:
  - q: "Why does my MediaTek WiFi keep failing on Windows 10?"
    a: "MediaTek's MT7921 and MT7961 cards are picky about driver versions, and Windows 10's update-delivered driver often mismatches the laptop's firmware — producing a dead adapter, Code 10, or WiFi that dies after sleep. The fix that sticks is the driver from your laptop maker's support site, installed clean, with Windows Update blocked from replacing it. Generic Windows drivers are the usual villain."
  - q: "How do I fix Code 10 on a MediaTek WiFi adapter in Windows 10?"
    a: "Code 10 means the driver loaded but the hardware wouldn't start — on MediaTek cards this is a driver/firmware mismatch far more often than dead hardware. Uninstall the adapter with driver deletion checked, do a full shutdown (Shift+Shutdown to skip Fast Startup), then install the laptop maker's MediaTek driver. If Code 10 survives that plus a BIOS update, the M.2 card itself is suspect."
  - q: "Where do I download the correct MediaTek WiFi driver for Windows 10?"
    a: "From your laptop maker's support site — ASUS, Acer, Lenovo, MSI, or HP — filtered to your exact model and Windows 10. Their package is validated against your machine's BIOS and card firmware. Avoid third-party driver updaters and generic MediaTek downloads; mismatched builds are what cause these failures in the first place."
  - q: "Why does MediaTek WiFi work after reboot but die after sleep?"
    a: "The card's firmware fails to reinitialize when Windows 10's power management cuts its power during sleep — a known issue with several MediaTek driver builds. Uncheck 'Allow the computer to turn off this device' on the adapter, set Wireless Adapter power saving to Maximum Performance, and disable Fast Startup. The laptop maker's latest driver usually contains the actual firmware-side fix."
---

Windows 10 laptops with MediaTek wireless cards — the MT7921, MT7961, and older MT7630E — suffer a familiar cycle: WiFi works, then a Windows update or a sleep/wake cycle kills it. Device Manager shows Code 10, or the adapter vanishes, or networks appear but nothing connects. The card hardware is rarely at fault; MediaTek's Windows drivers are simply version-sensitive, and Windows 10's habit of installing its own build over the manufacturer's is the engine of most failures.

This is the Windows 10 edition of the MediaTek fix sequence: correct driver sourcing, the power settings that wedge these cards, and the Code 10 drill.

## Why this happens

- **Windows Update driver mismatch.** Microsoft's MediaTek build conflicting with the laptop firmware — the top cause.
- **Sleep/wake reinitialization failure.** The card not coming back after power management cycles it.
- **Code 10 from version mismatch.** Driver loads, hardware won't start.
- **Fast Startup resuming wedged state.** Hybrid boot carrying the card's bad state across reboots.
- **Corrupt driver files.** Partial updates mixing old and new driver binaries.
- **Outdated BIOS.** Platform firmware predating the card's initialization requirements.
- **Failing M.2 module.** Actual hardware failure — uncommon, last resort.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact failure state

Precise symptoms dictate the fix — spend two minutes here.

1. Open **Device Manager > Network adapters** and find the **MediaTek** entry (MT7921, MT7961, MT7630E, or similar).
2. Classify it: **missing** (driver not loading), **yellow bang** (check Properties > General for the code — usually Code 10), or **present but broken** (no networks, or networks that won't connect).
3. Note the trigger if you can: **after Windows Update**, **after sleep**, or **random**.
4. Do a full cold boot — **Shift + Shut down**, wait 30 seconds, power on — and see if the card returns. Returning after cold boot but dying after sleep = power management issue.
5. Check **Settings > Network & Internet** — a missing WiFi section means Windows sees no adapter at all.

### Fix 2: Install the manufacturer's MediaTek driver

The central fix — the validated driver, cleanly installed.

1. Go to your **laptop maker's support site** and download the **Wireless/MediaTek driver** for your exact model and Windows 10 64-bit.
2. In **Device Manager**, right-click the MediaTek adapter > **Uninstall device** — check **Delete the driver software for this device**.
3. Restart the laptop.
4. Install the downloaded driver **before reconnecting to WiFi** if practical, then restart again.
5. Verify in **Properties > Driver** that the date/version matches the package you installed — not a Windows Update build.

### Fix 3: Block Windows Update from replacing the driver

Without this, the fix unravels at the next update.

1. After the maker driver is working, download Microsoft's **Show or hide updates** troubleshooter package (wushowhide.diagcab).
2. Run it, choose **Hide updates**, and hide any **MediaTek** or wireless driver update it offers.
3. On Windows 10 Pro, you can also set **Group Policy > Computer Configuration > Administrative Templates > Windows Components > Windows Update > Do not include drivers with Windows Updates** to Enabled.
4. Recheck the driver version a week later — if it changed, something replaced it and you need to re-hide.
5. Keep updating the driver yourself from the maker's site on your own schedule.

### Fix 4: Disable the power settings that kill the card

The sleep-death workaround that MediaTek cards specifically need.

1. **Device Manager > MediaTek adapter > Properties > Power Management** — uncheck **Allow the computer to turn off this device to save power**.
2. **Control Panel > Power Options > Change plan settings > Change advanced power settings > Wireless Adapter Settings > Power Saving Mode** — set **Maximum Performance** for both battery and plugged in.
3. **Power Options > Choose what the power buttons do > Change settings that are currently unavailable** — uncheck **Turn on fast startup**.
4. Do a full shutdown and cold boot after these changes.
5. Test sleep/wake three times — MediaTek sleep failures are intermittent, so one successful wake isn't proof.

### Fix 5: Reset TCP/IP and the wireless profiles

For cards that are present with networks visible but won't connect.

1. **Command Prompt as administrator**: `netsh winsock reset` then `netsh int ip reset` then `ipconfig /flushdns`.
2. Restart.
3. **Settings > Network & Internet > WiFi > Manage known networks** — **Forget** the problem network and reconnect fresh.
4. If it still won't connect, **Settings > Network & Internet > Status > Network reset** — wipes all adapters and profiles back to defaults.
5. Re-apply Fix 4's power settings after a network reset — it restores driver defaults.

### Fix 6: Update the BIOS and try alternate driver builds

Firmware-level fixes for stubborn cards.

1. Check the maker's support site for a **BIOS update** — install on AC power, nothing else running.
2. BIOS changelogs mentioning **WLAN, MT7921, or connectivity** are directly relevant — retest sleep behavior after updating.
3. If the maker's driver still fails, try a newer MediaTek build from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — search your card model (e.g., MT7921), download, and install via **Device Manager > Update driver > Browse my computer**.
4. If a catalog build works, hide it from Windows Update too (Fix 3) so a worse build doesn't replace it.
5. Also try the **previous** maker driver version — occasionally the newest maker build is the broken one.

### Fix 7: The Code 10 deep drill and hardware verdict

For Code 10 that survives everything above.

1. Confirm it's truly **Code 10** in **Properties > General** — Code 43 or 45 need different handling (see [how to fix unknown device in Device Manager in Windows 11 24H2](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) for the identification method).
2. Full power-cycle drill: uninstall with driver deletion, **Shift+Shutdown**, unplug AC, hold power 15 seconds, boot, install maker driver offline.
3. Boot a **Linux live USB** — working WiFi there proves the hardware is fine and isolates it to Windows drivers.
4. If the card is a removable **M.2** module (check the service manual), reseat it — loose M.2 cards cause exactly Code 10. An **Intel AX210** replacement (~$20) is the popular permanent upgrade.
5. If the card is soldered and Code 10 persists across drivers and BIOS, a **USB WiFi adapter** is the pragmatic workaround.

For 5GHz-specific failures rather than a dead adapter: [how to fix laptop not connecting to WiFi 5GHz on Windows 10](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-10/). Microsoft's wireless reference is on [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

MediaTek WiFi on Windows 10 fails in a predictable loop — Windows Update installs a mismatched driver, sleep wedges the card, Code 10 appears — and the fix is equally predictable: the maker's validated driver, installed clean, protected from Windows Update, with the card's power management tamed. Break the loop once, properly, and it stays broken... in the good way.
