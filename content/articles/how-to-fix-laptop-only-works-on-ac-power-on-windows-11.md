---
title: "Laptop Only Works on AC Power in Windows 11? Here's How to Fix It"
slug: how-to-fix-laptop-only-works-on-ac-power-on-windows-11
date: 2026-09-24
categories: ["battery"]
tags: ["windows 11", "only works plugged in", "dies when unplugged", "dead battery", "ac power"]
description: "Your laptop dies the second you unplug it on Windows 11. Diagnose whether it's the battery, a driver, or firmware — and fix it."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-on-ac-power-on-windows-11.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug it?"
    a: "The battery is either completely dead, not detected by the system, or disconnected. In a healthy laptop the battery takes over seamlessly when AC power is removed. An instant shutdown means the battery is contributing nothing — start with a battery report to confirm."
  - q: "Can a Windows 11 update cause the laptop to only work on AC power?"
    a: "Yes. Updates can corrupt the battery driver stack so Windows stops recognizing the battery, even though it's physically fine. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver in Device Manager and rebooting resolves most update-triggered cases."
  - q: "Is it safe to use a laptop with a dead battery on AC power?"
    a: "Generally yes, but check for swelling first — a bulging battery is a safety hazard and should be removed by a professional. Also note that without a working battery, any power flicker means an instant shutdown, so save work frequently and consider a UPS."
  - q: "How do I know if the battery is dead or just disconnected?"
    a: "Check Device Manager under Batteries and the BIOS setup screen. If the battery appears in BIOS but not Windows, it's a driver issue. If it's missing everywhere and a battery report shows no battery data, it's dead or physically disconnected."
---

You unplug the charger and the laptop dies instantly — no warning, no graceful shutdown, just black. Plug it back in, and it boots and runs perfectly. Congratulations: you own a very expensive desktop. When a Windows 11 laptop only works on AC power, the battery has dropped out of the equation entirely, and the job is figuring out whether that's a software misunderstanding or a genuinely dead battery.

The good news is that this symptom is highly diagnosable. A dead battery and a driver problem look identical from the outside, but a few checks separate them cleanly. Let's run those checks.

## Why this happens

- **The battery is genuinely dead.** Cells worn past the point of holding any charge — the most common cause on older machines.
- **Windows isn't detecting the battery.** Driver corruption after updates makes a healthy battery invisible.
- **The battery is physically disconnected.** Internal connectors work loose from drops, heat cycling, or swelling.
- **The embedded controller is confused.** The EC manages power switching; a stuck state can prevent battery takeover.
- **BIOS battery settings are wrong.** Some BIOS versions can disable the battery or get stuck after updates.
- **A swollen battery triggered protection.** The system may cut off a swelling battery as a safety measure.
- **Deep discharge lockout.** A battery left at 0% for months can drop below the voltage the charger recognizes.

## How to fix it

Work through these in order — diagnosis first, then fixes, then the hardware verdict.

### Fix 1: Confirm what Windows actually sees

Don't guess. Find out whether Windows knows a battery exists.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You should see **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery**.
3. If the battery entries are missing entirely, Windows doesn't see the battery — that's either driver failure or a dead/disconnected battery.
4. Hover over the battery icon in the taskbar. "No battery is detected" versus a 0% reading tells you different things: no detection points to connection/driver, while 0% with no charging points to dead cells.
5. Also check **Settings > System > Power & battery** — if the battery section is missing, detection has failed.

### Fix 2: Check the BIOS for battery status

The BIOS talks to the battery below Windows, so it separates hardware problems from Windows problems.

1. Shut down, power on, and press **F2**, **Del**, or **F10** to enter BIOS/UEFI setup.
2. Look for a **Battery**, **Power**, or **System Information** page showing battery health or status.
3. If the BIOS shows the battery with a health percentage, the hardware connection works — the problem is in Windows. Skip to Fix 4.
4. If the BIOS shows no battery or an error, the problem is hardware: disconnected, deeply discharged, or dead. Continue to Fix 3.
5. While in the BIOS, check for any **Battery** enable/disable option and make sure it's enabled.

### Fix 3: Reseat the battery connection

Internal battery connectors can work loose, especially after drops or years of heat cycling. Only do this if you're comfortable opening the machine; otherwise a shop can do it in minutes.

1. Shut down, unplug, and remove all peripherals.
2. Open the bottom panel (you'll typically need a small Phillips or Torx screwdriver — check a teardown guide for your exact model first).
3. Locate the battery connector on the motherboard. Unplug it carefully, check for corrosion or bent pins, and plug it back in firmly.
4. While you're in there, look for swelling — any puffiness, and the battery needs professional replacement, not reseating.
5. Reassemble, plug in AC, boot, and check whether Windows now detects the battery.
6. If it was disconnected and now works, run a full charge cycle and then a battery report to assess its health.

### Fix 4: Reinstall the battery drivers

If the BIOS sees the battery but Windows doesn't, this is very likely your fix.

1. In **Device Manager**, under **Batteries**, right-click each entry and choose **Uninstall device**.
2. Shut down completely — don't restart — and unplug the adapter for 30 seconds.
3. Reconnect AC power and boot up.
4. Windows reinstalls the drivers automatically. Check the taskbar icon within a few minutes.
5. If the battery appears but shows 0% and won't charge, the cells are likely dead — the driver was never the real problem, just a compounding one.

### Fix 5: Reset the embedded controller

The EC handles the AC-to-battery handoff. When it gets stuck, unplugging means instant death even with a good battery.

1. Shut down fully and unplug the adapter.
2. Hold the power button for 30 seconds to drain residual power.
3. If your model has a pinhole EC reset button on the bottom, press it for 10 seconds with a paperclip.
4. Reconnect AC, boot, then unplug and watch: if the laptop now stays on even briefly, the EC was stuck and the battery may be healthier than it looked.
5. If it still dies instantly, the battery genuinely can't deliver power.

### Fix 6: Generate a battery report for the final verdict

If Windows detects the battery but it holds nothing, get the numbers.

1. Open **Terminal (Admin)** and run `powercfg /batteryreport`.
2. If the report generates with data, compare **Design Capacity** to **Full Charge Capacity**. Near-zero full charge capacity confirms dead cells.
3. If the report says no battery data is available, the battery is electrically dead or disconnected.
4. Check the usage history for the decline pattern — a gradual fade over months points to normal wear; a sudden cliff suggests cell failure.
5. For help reading the details, see our guide on [checking battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/).

### Fix 7: Try reviving a deeply discharged battery

A battery left at 0% for months can fall into a protection lockout where the charger won't even attempt charging.

1. Plug in the original adapter and leave the laptop charging — powered off — for at least 4 hours. Don't keep checking; some controllers need a long trickle before they'll wake the battery.
2. After 4 hours, boot and check the battery icon.
3. If there's still no life, try a different compatible charger for the same long trickle — occasionally a marginal adapter can't break the lockout.
4. If nothing works after an overnight charge, the cells are beyond recovery.

### Fix 8: Replace the battery

When every check points to dead cells, replacement is the only fix.

1. Order a genuine battery for your exact model — check the part number on the old battery, not just the laptop model.
2. If the battery is internal and you're not comfortable with the repair, a local shop typically charges modest labor for the swap.
3. After installing, charge to 100% uninterrupted, then calibrate: drain to hibernate, rest, recharge.
4. For broader context on detection failures, our article on [laptops that only work when plugged in after updates](/articles/how-to-fix-laptop-only-works-when-plugged-in-after-windows-11-update/) covers the software side in more depth.

## Closing

A laptop that only works on AC power is telling you the battery contributes zero — the only question is why. The BIOS check separates hardware from software in two minutes, the driver reinstall fixes the software cases, and the battery report delivers the final verdict on the hardware ones. Once you know which you're dealing with, the fix is straightforward. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover the OS-side battery diagnostics if you want a second reference.
