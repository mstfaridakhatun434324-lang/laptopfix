---
title: "How to Fix Intel WiFi 6 AX201 Not Working: Step-by-Step Repair"
slug: how-to-fix-intel-wifi-6-ax201-not-working-step-by-step
date: 2026-10-10
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "step by step", "wireless fix"]
description: "Intel WiFi 6 AX201 not working? Follow this ordered step-by-step repair from quick checks to driver rebuilds and hardware tests."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-step-by-step.webp"
faqs:
  - q: "What is the first thing to check when the AX201 stops working?"
    a: "Check Device Manager for the exact device status and error code, and note whether the failure followed a Windows update. Code 10 or Code 43 with a recent update timestamp means a driver problem you can fix in minutes. Also confirm airplane mode is off and the WiFi toggle exists in Settings — a missing toggle points to enumeration failure rather than a connection problem."
  - q: "How is this different from the Windows 10 AX201 guide?"
    a: "The underlying fixes overlap, but this guide is organized as a strict step-by-step sequence you follow top to bottom without skipping, covering both Windows 10 and 11. The Windows 10 guide goes deeper into OS-specific driver branches and CNVio2 chipset coupling. Use this one when you want a checklist; use that one for Windows 10 specifics."
  - q: "Will resetting network settings fix the AX201?"
    a: "A network reset helps when the driver is healthy but connections fail — wrong profiles, corrupted stack, bad DHCP state. It does not fix Code 10 errors, missing adapters, or driver mismatches. Diagnose first: if Device Manager shows an error on the AX201 itself, do the driver steps before any reset."
  - q: "At what point should I replace the AX201 card?"
    a: "Replace it only after a clean driver install, chipset update, BIOS check, and reseat have all failed, and the card still errors on a fresh Windows install. Two different failure modes across those tests — especially Code 10 persisting through everything — is the signal that the card itself is dead rather than its software."
---

The Intel WiFi 6 AX201 fails in a handful of recognizable ways: Code 10 in Device Manager, the WiFi toggle vanishing from Settings, connections that drop every few minutes, or full speed on paper with no actual throughput. This guide is the checklist version of the repair — a strict sequence where each step builds on the last and tells you whether to continue or stop. Follow it top to bottom without skipping.

Before step one, grab two facts: your Windows version (Settings → System → About) and whether the failure started after an update. Those two facts predict the fix correctly most of the time — post-update failures are driver overwrites, and gradual failures are hardware or heat.
A word on how to use this guide: it's a checklist, not a menu. Each step assumes the previous ones passed, and the steps are ordered by a simple rule — cheap and reversible first, invasive last. Skipping ahead to the driver reinstall when you haven't checked the error code is how simple radio-state glitches turn into hour-long ordeals. Trust the order.

## Why this happens

- **Wrong driver branch installed:** Windows Update pairs the AX201 with a driver built for a different Windows version, producing Code 10.
- **Corrupted driver files:** Interrupted updates leave the driver half-written — enumerated but non-functional.
- **Power management trapping the card:** Sleep/wake cycles leave the CNVio2 interface in a dead state the driver cannot recover.
- **Stale chipset drivers:** The AX201's chipset-side logic goes unrecognized when chipset software is outdated.
- **BIOS mishandling the card:** Firmware bugs in CNVio2 initialization, often fixed in later BIOS releases.
- **Router incompatibility:** WiFi 6 settings (WPA3-only, 160 MHz, 802.11ax quirks) that the AX201's current driver handles poorly.
- **Overheating under sustained load:** The card throttles or drops when the chassis runs hot for extended periods.
- **Antenna or card seating:** Loose antenna leads after service work cause weak-or-no signal despite a healthy driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Record the exact failure signature

1. Open **Device Manager → Network adapters** and note the AX201's status: working, Code 10, Code 43, or missing entirely.
2. Open **Settings → Network & internet** and note whether a WiFi toggle exists at all.
3. Check **Event Viewer → Windows Logs → System** for Netwtw10/Netwtw12 errors with timestamps matching the failures.
4. This signature decides the path: error codes mean driver work (Fixes 2–4); a healthy-looking adapter with bad connections means Fixes 5–6.
5. Take a phone photo of the Device Manager status screen — if you end up seeking help, the exact error code and driver version in one image gets you accurate answers instead of twenty questions.

### Fix 2: Toggle airplane mode and restart the WLAN service

1. Turn **Airplane mode on**, wait ten seconds, turn it **off** — this resets the radio state machine.
2. Press **Win + R**, type `services.msc`, and restart **WLAN AutoConfig**.
3. If WiFi returns, the failure was a stuck radio state, not a driver problem — but continue to Fix 4 anyway to prevent recurrence.
4. If nothing changes, proceed; you have ruled out the trivial causes in under two minutes.
5. While you're here, forget the problematic network in **Settings → Network & internet → WiFi → Manage known networks** and rejoin it fresh — corrupted saved profiles cause authentication loops that perfectly mimic driver failures, and this costs nothing to rule out.

### Fix 3: Roll back the driver if an update caused this

1. In Device Manager, right-click the AX201 → **Properties → Driver → Roll Back Driver** (available only if a previous version exists).
2. Restart and test for a full day of normal use, including sleep-wake cycles.
3. If rollback is unavailable or does not help, move to the clean install — do not stack partial fixes.
4. Note the working version number somewhere safe; you will need it if Windows Update offers the bad driver again.

### Fix 4: Clean-install the correct Intel driver

1. Download the latest AX201 WiFi driver for your Windows version from the [Intel driver detection page](https://www.intel.com/content/www/us/en/support/detect.html).
2. In Device Manager, uninstall the AX201 with **Attempt to remove the driver for this device** ticked, then restart with the network cable unplugged or WiFi off to block Windows Update interference.
3. Install the Intel package, restart, and verify the error code is gone.
4. Update the **Intel Chipset Device Software** too — the AX201's CNVio2 design makes chipset drivers load-bearing. Our [Windows 10 AX201 guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-windows-10/) covers the chipset angle in depth.
5. If Device Manager reports Code 10 specifically, cross-reference the [Code 10 wireless driver guide](/articles/how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2/) — Code 10 has its own sub-causes beyond version mismatch, including registry and filter-driver issues.

### Fix 5: Stabilize power and router settings

1. Disable power management on the AX201 (**Properties → Power Management** → uncheck the box).
2. Set **Wireless Adapter Settings → Power Saving Mode** to **Maximum Performance** in Power Options.
3. On the router, try WPA2 instead of WPA3, disable 160 MHz channel width, and update the router firmware.
4. Test against a phone hotspot — success there proves the card is fine and the router configuration is the problem.
5. If the phone hotspot works, log into your router and check for a firmware update before changing settings — several AX201 incompatibilities were fixed router-side, and an update is cleaner than permanently dumbing down your WiFi 6 settings.

### Fix 6: Reset the network stack

1. In **Terminal (Admin)**, run `netsh winsock reset`, `netsh int ip reset`, and `ipconfig /flushdns`.
2. Go to **Settings → Network & Internet → Advanced network settings → Network reset** for the full reset (it clears saved WiFi passwords).
3. Restart, reconnect to your network fresh, and test for 24 hours.
4. Only do this after the driver is healthy — resetting the stack on top of a broken driver wastes the effort.

### Fix 7: Reseat, replace, and verify hardware

1. Power off, open the back panel, reseat the M.2 AX201 card, and confirm both antenna wires are firmly clipped.
2. Check for heat damage or corrosion on the card's connector while you are in there.
3. If reseating fails and errors persist across a fresh Windows install, replace the card (AX201 or compatible AX210 where the BIOS allows).
4. Failure across two cards means the motherboard's CNVio interface is at fault — a service center repair.

## Closing

The AX201 rewards the checklist approach because its failures are so patterned: error codes mean drivers, vanishing toggles mean enumeration, and bad connections with a healthy driver mean power or router settings. Work the steps in order, write down the driver version that works, and keep Windows Update from "helpfully" replacing it. For Windows 10-specific driver branch details, the companion guide linked above goes deeper.
