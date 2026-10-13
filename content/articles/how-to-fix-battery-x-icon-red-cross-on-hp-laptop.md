---
title: "How to Fix the Battery X Icon (Red Cross) on an HP Laptop"
slug: how-to-fix-battery-x-icon-red-cross-on-hp-laptop
date: 2026-09-01
categories: ["battery"]
tags: ["hp", "battery icon", "red x", "windows 11"]
description: "Red X over the battery icon on your HP laptop? Diagnose the cause and fix it, from driver resets to battery replacement."
thumbnail: "/images/thumbs/how-to-fix-battery-x-icon-red-cross-on-hp-laptop.webp"
faqs:
  - q: "What does the red X on the HP battery icon mean?"
    a: "It means Windows can't communicate with the battery — the system doesn't detect a working battery. Hovering usually shows 'No battery is detected' or a similar message. Causes include driver corruption, a disconnected battery, or a failed battery pack."
  - q: "Can I still use my HP laptop with the red X showing?"
    a: "Yes, on AC power — the laptop runs normally plugged in. But you have no battery backup, so any power interruption shuts the laptop down instantly. Don't rely on it for important unsaved work until fixed."
  - q: "Will reinstalling drivers remove the red X?"
    a: "Often, yes. The red X is frequently caused by corrupted ACPI battery drivers after a Windows update. Uninstalling them in Device Manager and restarting lets Windows reinstall clean copies, which restores battery detection."
  - q: "Does the red X always mean the battery is dead?"
    a: "No. Start with software fixes — drivers, BIOS, and HP's battery check. Only conclude the battery is dead if HP's hardware diagnostics fail it or the BIOS doesn't detect it either."
---

That red X over the battery icon is Windows telling you it can't see a battery at all. Your HP laptop probably works fine plugged into the wall, but the moment the power flickers, it dies instantly — there's no battery backup. It's an unsettling icon, but the fix path is well understood. Hover over the icon first and read the tooltip: "No battery is detected" points to a communication problem, while a percentage with the red X can indicate a battery Windows sees but considers failed — the distinction helps you pick where to start below.

The red X almost always means one of two things: Windows lost communication with a physically fine battery (drivers, BIOS, controller state), or the battery itself has failed. A quick check in the BIOS tells you which one you're dealing with.

## Why this happens

- **Corrupted battery drivers:** Windows updates commonly break the ACPI battery driver, producing the red X on reboot.
- **Battery not seated:** The internal battery connector can work loose, especially after the laptop's been dropped or serviced.
- **Failed battery:** Dead cells or a dead controller board mean the battery can't identify itself.
- **Outdated BIOS:** HP BIOS updates fix battery detection issues; old firmware can lose the battery.
- **HP battery check failure:** If HP's own diagnostics flag the battery, Windows may show the red X as a consequence.
- **Stuck embedded controller:** A bad EC state hides the battery from the OS until reset.
- **Third-party battery:** Non-HP batteries sometimes fail authentication and show as undetected.

## How to fix it

Work through these in order — the BIOS check determines your path.

### Fix 1: Check battery detection in BIOS

Restart and press **Esc** repeatedly as the HP logo appears, then press **F10** for BIOS setup (or **F2** for diagnostics directly). Look for battery information — on most HP BIOS versions it's on the main screen or under a **Battery** tab. Note what it says about both the battery and the AC adapter, since an unrecognized adapter can cause its own cascade of symptoms. **If BIOS detects the battery:** it's a Windows/driver issue — continue with Fix 2. **If BIOS shows no battery or unknown:** it's hardware — skip to Fix 5. You can also run HP's built-in test right away: from the startup menu, press **F2** → **Component Tests → Battery** and run both the battery check and the calibration if offered.

### Fix 2: Reinstall the battery drivers

Press **Win + X** → **Device Manager** → expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** → **Uninstall device**, then uninstall **Microsoft AC Adapter** too. Don't check any delete-driver option — you want Windows to reinstall its own clean copies. Restart. Windows reinstalls fresh drivers during boot, which clears the corruption behind most red-X cases. If the red X persists, also check **Device Manager → System devices** for any HP battery-related entries with warning icons and update those drivers. Our full driver guide at [updating battery drivers in Windows 11](/articles/how-to-update-battery-drivers-in-windows-11-24h2/) covers manual updates if the automatic reinstall doesn't work.

### Fix 3: Update the BIOS and HP drivers

Go to [HP Support](https://support.hp.com/us-en), enter your serial number, and install the latest BIOS plus any battery or chipset driver updates. Keep the AC adapter plugged in during the BIOS update and don't interrupt it. HP regularly ships BIOS fixes for battery detection — this is especially worth doing if the red X appeared right after a Windows feature update. After the update, check **Settings → Windows Update** for anything pending and restart.

### Fix 4: Reset the embedded controller

Shut down completely, unplug the AC adapter and all peripherals. If the battery is removable, take it out. Hold the power button for **30 seconds** to drain residual power. Reconnect AC power (reinsert the battery first if removable) and boot. This resets the embedded controller that manages battery detection. On many HP models this alone clears a red X caused by a stuck controller state — it's quick and worth trying before opening anything.

### Fix 5: Reseat the battery

If the BIOS didn't detect the battery, check the physical connection. For removable batteries: remove the pack, inspect the contacts for dirt or corrosion, wipe with a dry cloth, and click it firmly back in. For internal batteries: power off, remove the bottom panel, find the battery connector on the motherboard, unplug it, wait 30 seconds, and reconnect firmly. Look for swollen cells while you're in there — a puffy battery needs replacement, not reseating (see our guide on [battery swelling safety](/articles/battery-swelling-slightly-laptop-safe-troubleshooting/)).

### Fix 6: Run HP's battery calibration

If the battery is detected but Windows still shows the red X intermittently, the fuel gauge may be confused. HP's UEFI diagnostics (**Esc → F2 → Component Tests → Battery**) sometimes offer a calibration routine — run it if available. Alternatively, do a manual cycle: charge to 100%, unplug and drain to about 5% through normal use, then charge uninterrupted to full. Recheck the icon after the cycle.

### Fix 7: Replace the battery

If HP's battery check fails, the BIOS never detects the battery, or reseating changed nothing, the pack has failed. Order a genuine HP battery for your exact model and part number — HP firmware can be picky about third-party packs. After installation, verify the red X is gone and run a battery report to confirm healthy capacity numbers. Our guide on [checking battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through the report.

## Closing

The red X looks alarming, but it's usually Windows losing touch with a battery that's still physically fine — a driver reinstall or EC reset clears it in most cases. The BIOS check is the key fork in the road: battery visible in BIOS means software, invisible means hardware. Work the list in order and you'll either clear the icon or have a definitive hardware answer. Either way, don't ignore it — running without battery backup means any power blip kills your unsaved work, and if the underlying cause is a failing battery, catching it now is far better than discovering it during an important presentation.
