---
title: "How to Fix MSI Laptop Battery Not Charging: 7 Proven Fixes"
slug: best-way-to-fix-msi-battery-not-charging
date: 2026-09-30
categories: ["battery"]
tags: ["msi laptop", "battery not charging", "msi center"]
description: "MSI laptop plugged in but not charging? Work through these 7 proven fixes — from MSI Center charge limits to EC resets and driver repairs."
thumbnail: "/images/thumbs/best-way-to-fix-msi-battery-not-charging.webp"
faqs:
  - q: "Why does my MSI laptop say 'plugged in, not charging'?"
    a: "The most common cause is a battery charge limit set in MSI Center, Dragon Center, or the BIOS. MSI laptops often ship with a 'Best for Battery' mode that caps charging at 60% or 80%. Other causes include a bad charger, EC firmware glitches, corrupted battery drivers, or a failing battery. Check MSI Center first — it takes 30 seconds and fixes the majority of cases."
  - q: "What is MSI EC reset and does it fix charging issues?"
    a: "An EC (Embedded Controller) reset clears the chip that manages battery charging and power states. It resolves charging glitches caused by stuck power states after updates or static buildup. On most MSI laptops you hold the power button for 45 seconds with everything unplugged, or press the EC reset pinhole on the bottom. It is safe and does not delete any data."
  - q: "Should the battery charge limit in MSI Center be on or off?"
    a: "If you mostly use your laptop plugged in at a desk, keep a limit at 60% or 80% — it significantly extends battery lifespan. If you need full runtime on battery, set it to 100% (Best for Mobility). The 'problem' most users report is simply a limit they forgot they enabled. The setting is in MSI Center under Features, then Battery or Battery Health Option."
  - q: "How do I know if my MSI battery needs replacement?"
    a: "Generate a battery report with `powercfg /batteryreport` in an elevated Command Prompt and compare Design Capacity to Full Charge Capacity. If the full charge capacity is below 50-60% of design capacity, or the battery drains in under an hour of light use, replacement is the realistic fix. Also check for swelling — a swollen battery is a safety issue and must be replaced immediately."
---

Your MSI laptop is plugged in, the light is on, but the battery percentage refuses to budge. Nine times out of ten this is not a hardware failure — it is a charge limit you (or an update) enabled in MSI Center, or the embedded controller getting stuck in a bad power state. Both take minutes to fix.

Before you buy a new charger or battery, work through this guide. It is ordered from the quickest checks to the deeper ones, and it covers the MSI-specific settings that generic Windows guides miss. If you want to understand what your battery is actually reporting first, [generate a battery report with powercfg](/articles/how-to-generate-battery-report-windows-11-powercfg/) — it takes a minute and tells you whether the hardware is healthy.

## Why This Happens

- **MSI Center battery limit is enabled.** The "Best for Battery" mode caps charging at 60% or 80%. Windows then reports "plugged in, not charging" — which is normal behavior, not a fault.
- **EC (Embedded Controller) glitch.** The EC chip manages charging. After Windows updates, sleep/wake cycles, or static buildup, it can get stuck and refuse to charge until reset.
- **Wrong or underpowered charger.** MSI gaming laptops need their full wattage (often 180W-280W). A lower-wattage USB-C charger may run the laptop but not charge the battery.
- **Corrupted Microsoft ACPI battery drivers.** The two drivers Windows uses to talk to the battery can corrupt after updates, breaking charge reporting.
- **Loose or worn charging port.** The barrel connector on MSI laptops can develop play over time, causing intermittent contact.
- **Battery wear or swelling.** A battery with high wear may refuse to charge past a point or stop charging entirely.

## How to Fix It

Work through these in order. Most MSI "not charging" cases are solved by Fix 1 or Fix 2.

### Fix 1: Check the MSI Center Battery Limit

This is the number one cause. MSI Center's battery health options silently cap your charge.

1. Open **MSI Center** from the Start menu (or **Dragon Center** on older models).
2. Go to **Features** > **Battery** (on some models: **General Settings** > **Battery Health Option**).
3. You will see three modes: **Best for Mobility** (charges to 100%), **Balanced** (charges to 80%), and **Best for Battery** (charges to 60%).
4. If your battery is stuck at exactly 60% or 80%, you found it. Select **Best for Mobility** to charge to 100%.
5. Unplug and replug the charger, then watch the percentage for 2-3 minutes.
6. Decide your long-term setting: keep a limit if you live on AC power — it genuinely extends battery life. For full details on tuning this, see [how to set a battery charge threshold](/articles/best-way-to-set-battery-charge-threshold/).

### Fix 2: Perform an EC Reset

If no limit is set, reset the Embedded Controller. This clears stuck power states without touching your data.

1. Shut down the laptop completely — not sleep, a full shutdown.
2. Unplug the charger and remove all USB devices, docks, and peripherals.
3. Hold the power button down for **45 seconds**. (On some MSI models there is a small EC reset pinhole on the bottom — press it with a paperclip for 30 seconds instead.)
4. Release, wait 10 seconds, then reconnect only the original MSI charger.
5. Power on and check whether the battery icon shows charging.
6. If it now charges, the EC was stuck. This fix survives reboots, so you are done.

### Fix 3: Verify the Charger and Port

A surprising number of "not charging" cases are power delivery problems, not battery problems.

1. Use only the original MSI charger with the correct wattage printed on its label.
2. Check the charger's LED (if it has one) and feel the brick — it should get warm during charging. Stone cold plus no charging means it may be dead.
3. Inspect the DC barrel plug and the laptop's jack for bent pins, debris, or looseness. Wiggle gently — if charging flickers, the port may need repair.
4. Plug the charger directly into a wall outlet, not a power strip or extension.
5. Try a different outlet to rule out a dead socket.
6. If you have access to a multimeter, check the charger's output voltage against the label. If it reads zero or far off, replace the charger — not the battery. You can also follow the general steps in [how to test a laptop charger](/articles/how-to-test-laptop-charger-on-windows-11/).

### Fix 4: Reinstall the Battery Drivers

Corrupted ACPI drivers make Windows misreport battery state and block charging.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You will see **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery** (sometimes two of the latter).
3. Right-click each entry and choose **Uninstall device**. Check **"Attempt to remove the driver"** only if offered — do not worry, Windows reinstalls these on reboot.
4. Shut down the laptop, unplug the charger, and if your MSI model has a removable battery, take it out for 60 seconds.
5. Reconnect everything and power on. Windows reinstalls the drivers automatically.
6. Check the battery icon. If it now charges normally, the drivers were the culprit. Official driver updates are also available from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if Windows Update keeps offering a bad one.

### Fix 5: Update the BIOS and EC Firmware

MSI periodically fixes charging bugs in BIOS/EC updates.

1. Open MSI Center and go to **Support** > **Live Update**, or visit MSI's support site for your exact model.
2. Check for BIOS and EC firmware updates newer than what you have (see your version in **System Information** via `msinfo32`).
3. Install with the charger plugged in and the battery above 30%. Do not interrupt a BIOS flash.
4. After the update, re-enter MSI Center and re-check your battery health option — BIOS updates sometimes reset it to a capped mode.
5. Test charging. If the problem started right after a Windows update, also check **Settings** > **Windows Update** for optional driver updates.

### Fix 6: Run a Battery Calibration

A miscalibrated fuel gauge can make a healthy battery behave as if it is full or dead.

1. In MSI Center, look for a **Battery Calibration** tool under **Support** or **System Diagnosis** (available on many newer models).
2. If present, run it with the charger connected — it charges to full, discharges, and recharges to reset the gauge. This takes several hours; let it finish.
3. No tool? Do it manually: charge to 100%, unplug and use the laptop until it sleeps at low battery, leave it off for 3-5 hours, then charge uninterrupted to 100%.
4. Afterwards, generate a fresh battery report and compare **Design Capacity** vs **Full Charge Capacity** to see the battery's real health. The walkthrough at [how to check battery health on Windows 11](/articles/how-to-check-battery-health-on-windows-11-laptop/) explains how to read those numbers.

### Fix 7: Check Battery Health and Consider Replacement

If nothing above helped, the battery itself may be worn out.

1. Open an elevated Command Prompt (**Win + X** > **Terminal (Admin)**) and run `powercfg /batteryreport`. Open the generated HTML file.
2. Compare **Design Capacity** to **Full Charge Capacity**. Below 60% of design means the battery is heavily worn.
3. Look at the usage history graph — a battery that drops from 80% to dead in minutes has failing cells.
4. Physically inspect the laptop: a swollen battery pushes up the trackpad or keyboard deck. If you see this, stop using the battery immediately and do not puncture it.
5. For replacement, use a genuine MSI battery for your exact model. Third-party batteries often lack proper EC communication and can cause new charging quirks.
6. If the laptop is under warranty, contact MSI support before opening anything — battery replacement is often covered.

## Closing

MSI charging issues look alarming but are usually one setting or one stuck chip away from fixed. Check MSI Center's battery limit first, do the EC reset second, and only then start suspecting hardware. If your battery report shows healthy capacity and the fixes above did not help, the charging circuit or port is the next suspect — and that is a repair-shop job, not a settings job. Either way, you now know exactly which one it is.
