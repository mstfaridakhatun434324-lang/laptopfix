---
title: "Laptop Only Works on AC Power? Here's How to Fix It"
slug: how-to-fix-laptop-only-works-on-ac-power-step-by-step
date: 2026-09-26
categories: ["battery"]
tags: ["ac power", "battery failure", "no battery"]
description: "Laptop dies the instant you unplug it? Reset the battery driver, test the pack's real condition, and find out if it's a dead battery or a board fault."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-on-ac-power-step-by-step.webp"
faqs:
  - q: "Why does my laptop shut off immediately when unplugged?"
    a: "The battery can no longer deliver current — either its cells are fully degraded, its protection circuit has tripped, or the driver/firmware has lost communication with it. In most cases the battery itself is finished, but a driver reset sometimes revives communication."
  - q: "Can a dead battery damage the laptop if I keep using AC?"
    a: "A merely worn-out battery is safe to leave in while running on AC. A swollen, hot, or leaking battery is not — remove it (or stop using the machine) and replace it. If the pack is just dead, running on AC alone is fine indefinitely."
  - q: "Will the laptop work without the battery installed?"
    a: "Most laptops run fine on AC with the battery removed, though some models throttle performance or refuse to boot without a battery present. It's a useful diagnostic: if it runs the same with the battery out, the battery was contributing nothing."
  - q: "Is it worth replacing the battery on an old laptop?"
    a: "If the machine still does everything you need, a battery is usually the cheapest meaningful upgrade — far less than a new laptop. Check that genuine batteries are still available for your model first; discontinued packs from third parties are hit-or-miss."
---
Unplug the charger and the laptop dies instantly — no warning, no graceful shutdown, just black. Plug it back in and it boots like nothing happened. The machine has become a desktop with a screen, and the battery is decoration.

This usually means the battery can no longer deliver power, but "the battery is dead" isn't the only explanation — driver corruption, a tripped protection circuit, and even BIOS issues can produce identical symptoms. Work through these steps to find out which one you're dealing with.

## Why this happens

- **The cells are fully degraded.** After years of cycles, internal resistance climbs until the pack can't sustain even the boot current — voltage collapses the instant the charger disconnects.
- **The protection circuit tripped.** Battery packs have a safety cutoff that can latch permanently after a deep discharge or a fault, making a healthy-looking pack output nothing.
- **Windows lost communication with the battery.** A corrupted ACPI battery driver makes the OS unable to manage the pack, and some systems shut down rather than run on an "unknown" battery.
- **The battery connector is loose or corroded.** Internal ribbon connectors can work free over years of heat cycles, especially after a drop.
- **BIOS battery firmware is stuck.** The embedded controller handles the AC/battery handoff, and buggy firmware can fail the switchover.
- **The charger is marginal.** A weak or wrong-wattage adapter may barely run the system while also failing to charge — the battery slowly emptied and now contributes nothing.

## How to fix it

Work through these in order — the early steps are free and sometimes revive a "dead" battery.

### Fix 1: Confirm the battery's real state

1. With the charger plugged in, hover the battery icon. Note exactly what it says: "0% available (plugged in, charging)" that never moves, "no battery detected," or a percentage that never changes.
2. Open **Terminal (Admin)** and run `powercfg /batteryreport` — if the report shows a full charge capacity near zero or fails to generate battery data, the pack is electrically dead.
3. Open **Device Manager** > **Batteries** and check for warning icons on the battery devices.

### Fix 2: Reset the battery driver and EC

1. In **Device Manager** > **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device** (do both entries if there are two).
2. Shut the laptop down completely and unplug the charger.
3. If the battery is removable, take it out, press and hold the power button for 30 seconds, then reseat the battery firmly.
4. If it's internal, hold the power button for 30 seconds with everything unplugged — this drains flea power and resets the embedded controller.
5. Plug in and boot. Windows reinstalls the drivers; check whether the battery now charges.

### Fix 3: Test with the battery removed

1. Power off, unplug, and remove the battery if it's externally removable.
2. Plug in AC only and boot. If the laptop runs normally, the battery was contributing nothing — it's dead, not merely misconfigured.
3. On internal-battery models, skip physical removal and instead check the BIOS battery status screen (usually under a **Battery** or **System Information** tab) for what the firmware itself reports.

### Fix 4: Verify the charger is adequate

1. Check the wattage printed on your adapter and compare it to what the laptop requires (printed near the charging port or in the manual).
2. An underpowered adapter — like a [65W charger on a gaming laptop](/articles/how-do-i-fix-65w-charger-not-enough-for-gaming-laptop/) — can run the system while slowly starving the battery.
3. Try the original manufacturer charger, not a third-party one, and try a different wall outlet.
4. Inspect the charging port for looseness or debris; a flaky DC jack mimics battery failure.

### Fix 5: Update BIOS and chipset drivers

1. The embedded controller firmware lives in BIOS updates — check your manufacturer's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Flash the latest BIOS with AC connected.
3. Update the chipset driver from the same page.
4. Reboot and test an unplug again — EC firmware fixes do occasionally restore the AC/battery handoff.

### Fix 6: Try a battery calibration as a last software resort

1. If the battery shows some capacity but the laptop still dies on unplug, run a full calibration: charge to 100% for 2 hours, discharge to auto-shutdown, rest 5 hours off, recharge fully.
2. This sometimes unsticks a protection circuit that latched during a deep discharge.
3. The full method is detailed in [how to calibrate a laptop battery](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 7: Replace the battery

1. If nothing above changed anything, the pack is finished. Look up your exact model on the manufacturer's parts store — genuine batteries are worth the premium.
2. For internal batteries, budget for a service center if you're not comfortable opening the chassis; puncturing a lithium pouch during DIY removal is dangerous.
3. Check the [swollen battery guide](/articles/best-way-to-fix-battery-swelling-slightly-laptop-safe/) first if the bottom cover bulges at all — a swollen pack changes this from a repair into a safety job.

### Fix 8: Check for a swollen pack while you're at it

1. A battery that died suddenly rather than fading gradually sometimes swells as it fails — set the laptop on a flat table and check for rocking.
2. Look at the trackpad and bottom cover for new bulging.
3. If you find swelling, stop using the battery immediately and follow the [swollen battery safety steps](/articles/best-way-to-fix-battery-swelling-slightly-laptop-safe/) — a swollen pack is a safety issue, not just a dead one.
4. Even without swelling, a pack that went from working to zero-output overnight has likely tripped its internal protection permanently, which confirms replacement over repair.

## Closing

Nine times out of ten, instant-death-on-unplug is a worn-out battery, and the driver reset in Fix 2 is worth trying because it's free and takes five minutes. Once you've confirmed the pack is truly dead, a genuine replacement gives the laptop its portability back for a fraction of a new machine's cost.
