---
title: "Laptop Battery Not Charging When Plugged In: The Real Fixes"
slug: how-to-fix-laptop-battery-not-charging-when-plugged-in-reddit
date: 2026-10-10
categories: ["battery"]
tags: ["not charging", "plugged in not charging", "troubleshooting"]
description: "Plugged in but not charging? Skip the forum guesswork — these are the fixes that actually work, in the order to try them."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-when-plugged-in-reddit.webp"
faqs:
  - q: "What does 'plugged in, not charging' actually mean?"
    a: "Windows detects the AC adapter but the battery isn't accepting charge. Causes range from intentional (a charge threshold capping at 80%) to driver glitches to genuine hardware faults. The message alone doesn't tell you which — you have to test."
  - q: "Is 'plugged in, not charging' ever normal?"
    a: "Yes. Lenovo Conservation Mode, Dell's Adaptive charging, ASUS Battery Health Charging, and HP's Battery Health Manager all intentionally stop charging at 60–80% to extend battery life. Check your vendor's battery app before troubleshooting — you may be 'fixing' a feature."
  - q: "Can a Windows update cause 'plugged in, not charging'?"
    a: "Absolutely — it's one of the most common triggers. Updates reinstall battery and chipset drivers, reset vendor app settings, and occasionally update the BIOS, any of which can interrupt charging. The driver reinstall fix below resolves most update-triggered cases."
  - q: "How do I know if it's the charger or the laptop?"
    a: "Test with a different adapter of equal or higher wattage with the same connector. If the new adapter charges, your charger is bad. If neither charges, the problem is in the laptop — drivers, settings, battery, or charging circuit, in that order of likelihood."
---

If you've been through the forums, you've seen twenty different "fixes" for "plugged in, not charging" — most of them cargo cult. This guide skips the folklore and gives you the sequence that actually resolves it, ordered by likelihood, with a test after each step so you know when to stop.

One important mindset shift before you start: "not charging" is a symptom with at least six distinct causes, and the correct fix depends entirely on which one you have. That's why the order matters — each step here rules out one cause before you spend time on the next.

## Why this happens

- **Charge threshold intentionally engaged.** Vendor battery-health features capping charge at 60–80% — a feature, not a bug.
- **Driver glitch.** The ACPI battery driver misreports state after updates or crashes.
- **Failing AC adapter.** The brick delivers enough power to run the laptop but not enough to charge — or its identification chip died and the laptop refuses it.
- **Worn-out battery.** A battery at end of life may refuse charge while the system runs fine on AC.
- **Loose or damaged DC jack.** Intermittent connection confuses the charging logic.
- **BIOS/EC confusion.** The embedded controller needs a reset to resume normal charging.
- **Overheating protection.** Some laptops pause charging when the battery is too hot.
- **Corrupt power plan.** A damaged custom power plan can send conflicting charge instructions after updates or tweaking tools.
- **Dust-choked charging area.** Less common, but excessive heat from blocked vents can trigger the same thermal charging pause as Fix 6 describes.

## How to fix it

Work through these in order — stop when charging resumes.

### Fix 1: Check for an intentional charge limit first

1. Open your vendor's battery app: **Lenovo Vantage**, **Dell Power Manager**, **MyASUS**, or HP's **Battery Health Manager** (in BIOS via F10).
2. Look for Conservation Mode, charge thresholds, or "maximize battery health" settings.
3. If a cap is set (e.g., stops at 80%), that's your answer — the laptop is behaving exactly as configured. Adjust or disable it if you want a full charge.
4. Only continue troubleshooting if no limit is set and it still won't charge. Take a screenshot or photo of the battery app's settings page before changing anything — if the "fix" turns out to be elsewhere, you'll want to restore your original longevity settings exactly.

### Fix 2: Inspect the charger and connection

1. Check the charger's LED and the laptop's charging light. No lights at all? Try a different wall outlet first.
2. Examine the cable and connector for damage, and the laptop's jack for looseness or debris.
3. Confirm the wattage matches what the laptop needs — an underpowered adapter (like a phone charger via USB-C) may run the laptop without charging it.
4. If possible, test with a known-good adapter of the correct wattage. Charging resumes? Replace your adapter.

### Fix 3: Run the EC reset

1. Shut down completely (hold **Shift** while clicking Shut down to skip Fast Startup).
2. Unplug the adapter and all peripherals. Remove the battery if it's externally removable.
3. Hold the **power button for 20 seconds**.
4. Reconnect AC power, then power on. Watch the battery icon for 10 minutes.

### Fix 4: Reinstall the battery drivers

1. **Win + X > Device Manager** > expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. **Action > Scan for hardware changes**, then restart with the charger connected.
4. This is the fix that resolves most update-triggered "not charging" cases.
5. After the restart, give it a full 10 minutes on the charger before judging — the charging circuit sometimes takes a few minutes to re-engage after the driver stack is rebuilt.

### Fix 5: Check battery health

1. Run `powercfg /batteryreport` in **Terminal (Admin)** and open the HTML file.
2. If Full Charge Capacity is a small fraction of Design Capacity, the battery may have reached end of life — some worn batteries stop accepting charge entirely.
3. Run your vendor's UEFI diagnostics battery test (Dell: F12 > Diagnostics; HP: F2; Lenovo: F10) for the authoritative verdict.
4. Our guide to [checking battery design vs full charge capacity](/articles/how-to-check-battery-design-vs-full-charge-capacity-on-laptop/) explains how to read the report.

### Fix 6: Cool it down

1. If the laptop is hot, shut it down, unplug, and let it cool for 30 minutes in a ventilated spot.
2. Some laptops deliberately pause charging above a battery temperature threshold — this is protection working correctly.
3. After cooling, plug in and check. If charging resumes only when cool, keep the machine ventilated and avoid heavy loads while charging.

### Fix 7: Update BIOS and chipset drivers

1. Get the latest **BIOS** and **chipset** drivers from your manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Install on AC power; let the BIOS update reboot by itself.
3. After booting, do one more EC reset (Fix 3) and test.

### Fix 8: Test the battery in isolation

1. If the battery is removable: power off, remove it, plug in AC only, and power on. Runs fine? The laptop's charging circuit works — the battery is the suspect.
2. For internal batteries, the vendor diagnostic from Fix 5 is your isolation test.
3. A confirmed dead battery needs replacement with a genuine part for your exact model.
4. If a known-good battery also won't charge, the charging circuit on the motherboard is faulty — professional repair.

## Closing

"Plugged in, not charging" looks scary but the fix is usually mundane: a charge limit you forgot about, a driver needing reinstall, or an EC reset. Work the list in order and you'll either fix it in twenty minutes or arrive at the hardware verdict with evidence instead of guesses — which is exactly what a repair shop needs to help you quickly. And if the fix turns out to be a charge threshold you didn't know was on, consider leaving it on: your battery will last longer for it. If the gauge itself seems untrustworthy after all this, run one [full calibration cycle](/articles/how-to-calibrate-laptop-battery-windows-11/) before concluding the battery is dead.
