---
title: "Laptop Only Works When Plugged In: Troubleshooting Guide"
slug: laptop-only-works-when-plugged-in-troubleshooting
date: 2026-10-09
categories: ["battery"]
tags: ["battery dead", "not charging", "hardware"]
description: "Laptop dies the instant you unplug it? That means the battery isn't contributing at all. Here's how to confirm it and what to do next."
thumbnail: "/images/thumbs/laptop-only-works-when-plugged-in-troubleshooting.webp"
faqs:
  - q: "Why does my laptop only work when plugged in?"
    a: "The battery has stopped contributing power entirely — it's either completely dead, disconnected, or no longer detected by the system. The laptop runs fine on AC power because the charger bypasses the battery. This is a hardware-level problem, not a settings issue."
  - q: "Can a dead battery damage my laptop?"
    a: "A dead-but-stable battery generally doesn't damage anything — the laptop just runs on AC. But a swollen, leaking, or extremely hot battery is different: stop using it and replace it promptly, since those are safety hazards, not just inconveniences."
  - q: "Will the battery come back to life if I leave it charging?"
    a: "If it's deeply discharged but healthy, sometimes — leave it charging (powered off) for several hours. But if the battery is chemically worn out or the system reports it as failed, no amount of charging revives it. Check the battery report to see which case you're in."
  - q: "Is it worth replacing the battery on an old laptop?"
    a: "If the laptop otherwise meets your needs, a battery replacement is usually far cheaper than a new machine — often $40–$120 for the part. Consider the laptop's overall age and condition: on a 6+ year old machine with other issues, put the money toward a replacement laptop instead."
---

Unplug the charger and the laptop dies instantly — no warning, no graceful shutdown, just off. Plug it back in and it works perfectly. That's the signature of a battery that has completely stopped participating: your laptop is effectively a desktop now, tethered to the wall.

This is different from "battery drains fast" or "won't charge." Here the battery contributes *zero*. The troubleshooting is correspondingly direct: confirm the battery's status, try the few things that can revive it, and then replace it if it's truly done.

## Why this happens

- **The battery is chemically dead.** After hundreds of cycles, lithium cells lose the ability to hold any meaningful charge. The battery reports 0% (or isn't detected) because there's genuinely nothing there.
- **The battery is deeply discharged past recovery.** Left at 0% for weeks or months, lithium packs can drop below the voltage where the charging circuit will even attempt a charge — a protection behavior.
- **The battery is disconnected.** A loose internal connector means the pack is fine but electrically absent. Common after drops or amateur repairs.
- **Windows can't see the battery.** Failed ACPI drivers or a stuck embedded controller can make a working battery invisible to the OS.
- **The charging circuit failed.** Rare, but the motherboard's charging circuitry can fail such that the battery neither charges nor discharges — the laptop runs on AC only.

## How to fix it

Work through these in order — from "maybe it's just confused" to "it's definitely hardware."

### Fix 1: Confirm what Windows actually sees

Get the facts before doing anything else.

1. Click the battery icon in the taskbar. Note exactly what it says: **0%**, **Unknown**, a red X, or no battery icon at all.
2. Press **Win + X** > **Device Manager** > **Batteries**. Is **Microsoft ACPI-Compliant Control Method Battery** listed? Any warning icons?
3. Open **Terminal (Admin)** and run `powercfg /batteryreport`. If the report generates but shows no battery data, Windows truly can't see the pack.
4. These three checks tell you whether you're dealing with a dead-but-detected battery (revivable, maybe) or an undetected one (driver or hardware). If Windows can't see the battery at all, the [battery not detected guide](/articles/laptop-battery-not-detected-windows-11/) goes deeper on the detection side.

### Fix 2: Try a long, powered-off charge

A deeply discharged battery sometimes needs patience, not intervention.

1. Shut the laptop down completely — not sleep.
2. Plug in the original charger directly to a wall outlet.
3. Leave it charging, powered off, for **4–6 hours** undisturbed.
4. Boot up and check the battery percentage. If it's climbed above 0% and holds, the pack was just deeply discharged — let it charge fully, then run a calibration cycle.
5. If it's still at 0% or undetected after 6 hours, the battery isn't taking a charge at all. Move on.

### Fix 3: Reinstall the battery drivers and reset the EC

Rule out the software side completely before concluding it's hardware.

1. In **Device Manager** > **Batteries**, uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
2. Shut down fully, unplug everything, and hold the power button for **30 seconds** (or use the EC reset pinhole if your laptop has one).
3. If the battery is removable, take it out, inspect the contacts, and reseat it firmly.
4. Reconnect the charger and boot. If Windows now detects the battery and it starts charging, you had a driver/EC problem, not a dead pack.

### Fix 4: Test with the battery removed (diagnostic)

This tells you whether the battery is actively interfering.

1. Shut down, unplug, and remove the battery if it's removable.
2. Plug in the charger (no battery) and boot. If the laptop runs fine, the charging circuit and adapter are good — the problem is isolated to the battery.
3. Shut down, reinstall the battery firmly, and boot again. Sometimes the remove-reinstall cycle alone restores detection.
4. If the laptop *won't* boot without the battery but runs with it installed (while plugged in), the battery is at least completing the circuit — note this for the repair shop, as it hints at a pack failure rather than a connector issue.

### Fix 5: Check the battery's physical condition

Look at the pack itself — it may be telling you the answer visually.

1. For removable batteries: take it out and look for swelling (the pack doesn't sit flat), discoloration, or a chemical smell.
2. For sealed laptops: check whether the bottom panel bulges, the trackpad sits raised, or the laptop rocks on a flat surface.
3. Any swelling = stop. Don't charge it, don't keep using it on AC with the swollen pack inside if you can remove it. Swollen lithium batteries are a fire risk — replace through proper channels.
4. No swelling but the pack is several years old? It's probably just worn out. Normal end of life.

### Fix 6: Get a definitive verdict from diagnostics

Before spending money, confirm with the manufacturer's own tools.

1. Run the built-in hardware diagnostics: **Dell** (F12 > Diagnostics), **HP** (F2), **Lenovo** (Vantage > Run diagnostics).
2. Run the **battery** test specifically and note the result code.
3. A failed battery test is the definitive answer — and it's what warranty support and repair shops want to see.
4. Check warranty status on the manufacturer's support site: [Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en). Batteries often have 1-year coverage.

### Fix 7: Replace the battery

When every test points to a dead pack, replacement is the fix. There's no software for this one.

1. For user-replaceable batteries: order the exact manufacturer part number. Avoid the cheapest third-party packs — weak cells and bad fuel gauges will have you troubleshooting again in months.
2. For sealed-in batteries: this is a professional job. Get a quote from the manufacturer or a reputable local shop.
3. After replacement, charge to 100% once, then run a full calibration cycle so the new pack's gauge starts clean.
4. Going forward, avoid leaving the laptop at 0% for extended periods — that's what pushes an aging battery past the point of recovery.

## Closing

A laptop that only works plugged in has a battery contributing nothing — and the path is short: confirm detection, try a long powered-off charge, reset the drivers and EC, check the pack physically, and run diagnostics. If the battery does get detected but refuses to charge, the [plugged-in-not-charging guide](/articles/best-way-to-fix-laptop-plugged-in-not-charging/) takes over from there. If the battery won't take a charge after all that, it's done, and replacement is the only fix. The silver lining: everything else in the laptop works fine, so a new battery gives you back a fully portable machine for a fraction of the cost of a new one.
