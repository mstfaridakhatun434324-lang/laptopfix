---
title: "Best Way to Fix a Laptop That Only Works When Plugged In"
slug: best-way-to-fix-laptop-only-works-when-plugged-in
date: 2026-09-17
categories: ["battery"]
tags: ["battery dead", "won't run on battery", "power"]
description: "Laptop dies the instant you unplug it? The battery may be disconnected, disabled, worn out, or blocked by a driver — here's the fix order."
thumbnail: "/images/thumbs/best-way-to-fix-laptop-only-works-when-plugged-in.webp"
faqs:
  - q: "Why does my laptop shut off immediately when I unplug it?"
    a: "The laptop is running purely on AC power because the battery is not contributing — it may be disconnected, disabled in software, fully worn out, or blocked by a corrupted driver. Less commonly, the charging circuit on the motherboard has failed. Work through the checks below to find which one it is."
  - q: "Can a dead battery cause instant shutdown on unplug?"
    a: "Yes, and it is the most common cause. A lithium-ion pack with collapsed capacity cannot hold any meaningful charge, so the moment AC power disappears, the voltage drops and the laptop dies. A battery report showing full charge capacity near zero confirms this."
  - q: "Will my laptop work without a battery installed?"
    a: "Most laptops run fine on AC power with the battery removed, though some models throttle performance without a battery present. If your battery is removable, testing without it is a useful diagnostic — if the laptop behaves the same, the battery was already contributing nothing."
  - q: "Could a Windows update cause this?"
    a: "Yes. Updates can corrupt the battery driver stack so Windows stops recognizing the battery entirely, which looks identical to a dead pack. Reinstalling the battery drivers in Device Manager often brings the battery back after an update. See our update-specific guide for [laptops that only work plugged in after a Windows update](/articles/how-to-fix-laptop-only-works-when-plugged-in-after-windows-11-update/)."
---

A laptop that runs perfectly on the charger but dies the second you unplug it is telling you something simple: the battery is not in the circuit. Either it cannot hold a charge, the laptop cannot see it, or something is preventing it from delivering power. The machine itself is fine — it proves that every time it boots on AC.

The best fix order starts with the cheapest explanations. A disconnected or software-disabled battery costs nothing to fix; a worn-out pack costs the price of a replacement; a failed charging circuit is the rare expensive one. This guide walks you from free to costly so you never pay for a battery you did not need.

## Why this happens

- **Worn-out battery:** Cells with near-zero usable capacity cannot sustain the laptop for even a second off AC.
- **Disconnected battery:** The internal connector worked loose, or a removable pack is not seated properly.
- **Battery disabled in software:** The battery driver is corrupted or the device is disabled in Device Manager.
- **Charge threshold confusion:** A stuck limit feature can leave the battery at a level the firmware treats as unusable.
- **Failed charging circuit:** The motherboard's charging IC no longer charges or reads the pack — rare but real.
- **Swollen battery safety cutoff:** A swelling pack triggers protection circuits that take it offline entirely.

## How to fix it

Work through these in order — free checks first, purchases last.

### Fix 1: Check what Windows thinks about the battery

Get the facts before touching hardware.

1. Click the battery icon in the system tray — note whether it says **No battery detected**, shows 0 percent, or shows a charge that never changes.
2. Press **Win + X**, open **Device Manager**, and expand **Batteries**.
3. If **Microsoft ACPI-Compliant Control Method Battery** has a yellow warning or is missing, the driver is your problem — skip to Fix 4.
4. Right-click the battery device and check **Properties → General** for the device status message.
5. If Windows sees the battery fine but it never charges, the pack itself is the prime suspect.

### Fix 2: Reseat the battery connection

A loose connector mimics a dead battery perfectly.

1. Shut down the laptop and unplug the charger.
2. If the battery is removable, slide it out, inspect the contacts for dirt or corrosion, and firmly reseat it.
3. If the battery is internal, only open the bottom panel if you are comfortable doing so and the warranty allows — disconnect and reconnect the battery cable to the motherboard.
4. Reconnect the charger, power on, and check whether the battery is now detected and charging.
5. Never force a swollen battery back into place — if the pack or trackpad area is bulging, skip to Fix 7.

### Fix 3: Run a battery report

Let the numbers tell you whether the pack has any life left.

1. Press **Win + X** and open **Terminal (Admin)**.
2. Run `powercfg /batteryreport /output "C:\battery-report.html"` and open the resulting file.
3. Compare **Full Charge Capacity** with **Design Capacity**.
4. If full charge capacity is a small fraction of design capacity — or the report shows no usable capacity at all — the battery is worn out and needs replacing.
5. A healthy-looking capacity paired with instant shutdown points to a connection or circuit problem instead.

### Fix 4: Reinstall the battery drivers

Corrupted drivers can hide a perfectly good battery.

1. In **Device Manager → Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
2. Uninstall **Microsoft AC Adapter** as well if it is listed.
3. Shut down completely (hold **Shift** while clicking **Shut down** for a full shutdown), unplug for 30 seconds, then reconnect and boot.
4. Windows rebuilds the driver stack from scratch on startup.
5. Check the battery icon after the desktop loads — a reappearing battery means the driver was the whole problem.

### Fix 5: Reset the EC and power hardware

Clear stuck charge-controller state.

1. Shut down, unplug the charger, and disconnect all peripherals.
2. Hold the power button for **30 to 45 seconds** to drain residual power and reset the embedded controller.
3. On some models there is a pinhole reset button on the bottom — press it for 30 seconds with a paperclip.
4. Reconnect only the charger and power on.
5. If the battery was stuck in a protection state, it may now be detected and begin charging.

### Fix 6: Check manufacturer battery settings

A limit feature can park the battery where the firmware will not use it.

1. Open your maker's utility — **Lenovo Vantage**, **MyASUS**, **MSI Center**, **Dell Power Manager** — and review battery health, threshold, and conservation settings.
2. Turn off any charge limits temporarily and see whether the battery starts contributing.
3. Check the BIOS for battery-related options (**F2**, **F10**, or **Delete** at boot) and load optimized defaults.
4. Update the BIOS from the manufacturer's support site if a newer version mentions battery or charging fixes.
5. For general charging failures, our guide to [laptops not charging when plugged in](/articles/best-way-to-fix-laptop-battery-not-charging-when-plugged-in/) covers the wider picture.

### Fix 7: Replace the battery — or check for swelling first

When the pack is truly done, replacement is the fix.

1. Inspect for swelling: a bulging bottom panel, a lifting trackpad, or a case that will not sit flat are warning signs — do not puncture or bend a swollen pack.
2. A swollen battery is a safety issue: stop using it, do not charge it unattended, and take it to a repair shop or recycler promptly.
3. For a merely worn (not swollen) battery, note your exact model number and buy an OEM or reputable third-party replacement.
4. After installing the new pack, charge it to 100 percent uninterrupted before first use.
5. If a brand-new battery still does not work, the motherboard charging circuit is likely at fault — that is a professional repair, not a DIY job.
6. For charging-specific diagnostics, Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents the built-in power troubleshooter and battery settings.

## Closing

"Only works plugged in" is the battery's way of saying it has left the building — disconnected, disabled, or depleted. Reseat it, check the report, reinstall the drivers, and only then spend money on a replacement. In the rare case a new battery changes nothing, you have narrowed it to the charging circuit, which is genuinely useful information to hand a repair technician. A related symptom with its own causes is covered in [battery only charges when the laptop is off](/articles/battery-only-charges-when-laptop-is-off-troubleshooting/).
