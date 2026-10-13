---
title: "Laptop Only Works When Plugged In on Windows 11 (24H2)? How to Fix It"
slug: how-to-fix-laptop-only-works-when-plugged-in-in-windows-11-24h2
date: 2026-10-03
categories: ["battery"]
tags: ["only works plugged in", "battery dead", "windows 11 24h2", "shuts down unplugged", "battery replacement"]
description: "Laptop dies the instant you unplug it on Windows 11 24H2? Diagnose the dead battery and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my laptop shut off immediately when I unplug it?"
    a: "The battery can no longer deliver power — its cells are depleted, its protection circuit has tripped, or the battery connector isn't making contact. Windows may still show a charge percentage, but that number is meaningless if the cells can't sustain a load."
  - q: "Can a Windows update cause a laptop to only work plugged in?"
    a: "Rarely, but it happens: an update can corrupt the battery driver so Windows mismanages the battery, or a BIOS update can change battery thresholds. Far more often the timing is coincidence and the battery was already dying."
  - q: "Is it safe to use a laptop with a dead battery still inside?"
    a: "Generally yes, if the battery isn't swollen, hot, or smelling odd. A dead-but-stable battery is just dead weight. But a swollen battery is a fire risk — check for case bulging and stop using it if you see any."
  - q: "Will removing the battery let me use the laptop normally?"
    a: "On models with removable batteries, yes — many run fine on AC alone. On sealed models you can't easily remove it, but a dead internal battery doesn't prevent AC operation. Some laptops throttle slightly without a battery; that's normal."
---

Unplug the charger and the laptop dies instantly. No warning, no graceful shutdown — just black. Plug it back in and it works perfectly. Your laptop has become a desktop, and it's telling you something unambiguous: the battery is no longer participating.

On Windows 11 24H2, this is usually a dead or disconnected battery rather than a Windows problem — but "usually" isn't "always," and there are software causes worth ruling out before you buy a replacement. Here's the full diagnostic path.

## Why this happens

- **The battery cells are depleted.** After hundreds of cycles, the cells can't hold meaningful charge or deliver current under load.
- **The battery's protection circuit tripped** and latched — the pack refuses to discharge as a safety measure.
- **The battery connector is loose or corroded**, so the system can't draw from the pack.
- **The battery is deeply discharged** from months of storage and the charger can't wake it through normal charging.
- **A corrupted battery driver** makes Windows mismanage charging and discharging.
- **BIOS battery settings** (like a fault-triggered safety cutoff) are blocking battery use.
- **The battery is swollen**, which often comes with protection-circuit shutdown.

## How to fix it

Work through these in order. We're ruling out the fixable causes before concluding the battery is dead.

### Fix 1: Check what Windows thinks about the battery

Start with data, not assumptions.

1. Open **Terminal (Admin)** (**Win + X**) and run `powercfg /batteryreport`.
2. Open `C:\Windows\System32\battery-report.html`. Check whether a battery is even listed — if the report shows no battery, Windows can't see the hardware at all.
3. Compare **Full Charge Capacity** to **Design Capacity**. A battery at 10-20% of design is effectively dead.
4. Look at recent **Battery usage** history: if the laptop never records discharging (only "AC" states), the battery hasn't delivered power in a long time.
5. If Windows sees no battery whatsoever, also check **Device Manager → Batteries** — missing entries point to hardware detection failure. For the related "shuts down when unplugged" scenario, see [laptop shuts down when unplugged](/articles/how-do-i-fix-laptop-shuts-down-when-unplugged/).

### Fix 2: Reset the embedded controller and reseat the battery

A latched protection circuit or confused EC mimics a dead battery perfectly.

1. Shut down completely. Unplug the charger and all USB devices.
2. If the battery is removable: remove it, inspect the contacts, and reinsert firmly.
3. Hold the **power button for 20-30 seconds** to drain residual charge and reset the EC.
4. Plug in the charger (leave the battery out if removable) and power on. Then shut down, reinstall the battery, and boot again.
5. Unplug the charger and see if the laptop survives. If it now runs on battery, the EC was latched — problem solved.

### Fix 3: Reinstall the battery drivers

Driver corruption after the 24H2 update can block battery discharging.

1. Open **Device Manager** (**Win + X**) → **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter** (don't delete drivers).
3. **Action → Scan for hardware changes**, then restart.
4. After reboot, unplug and test. If Windows was simply mismanaging a healthy battery, this restores normal behavior.
5. Also install your maker's latest **chipset driver** — on 24H2, stale chipset drivers cause power-management faults. Intel users can use Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 4: Try a full shutdown and extended charge

A deeply discharged battery sometimes needs coaxing.

1. With the laptop plugged in and powered **off**, leave it charging for **4+ hours** — overnight is fine.
2. Charging while powered off avoids Windows' power management interfering with the wake-up charge.
3. Power on, check the reported percentage, then unplug and time how long it lasts.
4. If it went from "instant death" to "20 minutes of life," the battery was deeply discharged rather than dead — run 2-3 full cycles to rebuild capacity.
5. If nothing changed, the cells can't take a charge — continue.

### Fix 5: Check BIOS battery status and thresholds

The firmware may be blocking the battery for a reason.

1. Reboot and enter BIOS (**F2**, **F10**, **Del**, or **Esc** depending on maker).
2. Find the **Battery Information / Battery Health** section. Note what it reports — many BIOSes flag failed batteries explicitly.
3. Look for any **battery cutoff**, **ship mode**, or **battery disconnect** option that might be enabled. Disable it if found.
4. Check for a **BIOS update** on your maker's support site — some updates fix battery detection bugs. Flash with the charger connected.
5. If the BIOS itself reports battery failure or shows no battery, believe it over Windows.

### Fix 6: Inspect for swelling and physical damage

A swollen battery often triggers exactly this behavior — and it's a safety issue.

1. Power off and unplug. Place the laptop on a flat table — does it rock or sit unevenly?
2. Look for a **trackpad that's raised or hard to click**, a **keyboard that's bowed**, or **case seams separating**.
3. If you see any of these, **stop**: don't charge it further, don't puncture it, don't put it in the trash. Take it to a professional or e-waste facility.
4. Our [battery swelling guide](/articles/how-to-fix-laptop-battery-swelling-on-windows-10/) covers safe handling in detail.
5. A swollen battery explains everything — replacement is the only fix, and it's urgent.

### Fix 7: Replace the battery

When the diagnostics point to dead cells, this is the fix.

1. Confirm the verdict: battery report shows tiny full charge capacity, BIOS flags failure, or the battery is several years old with heavy use.
2. Get the exact part number from the battery label or your maker's support site (use the serial/Service Tag). Buy **genuine** — aftermarket batteries are a gamble on safety circuits.
3. On removable-battery models, swap it yourself in a minute. On sealed models, it's a bottom-panel job — straightforward with a guide for your model, or a quick shop visit.
4. After installing, charge to 100% and run 2-3 full cycles so the gauge learns the new cells.

## Closing

A laptop that only works plugged in is almost always telling you the battery can't deliver power anymore — dead cells, a tripped protection circuit, or a disconnected pack. The EC reset and driver reinstall are worth trying because they're free and occasionally the whole story. But if the battery report shows a tiny full charge capacity and the BIOS agrees, stop troubleshooting software and replace the battery.
