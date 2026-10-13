---
title: "How to Fix a Laptop That Only Works When Plugged In"
slug: how-to-fix-laptop-only-works-when-plugged-in-reddit
date: 2026-09-27
categories: ["battery"]
tags: ["laptop only works plugged in", "laptop dies when unplugged", "battery not detected"]
description: "Laptop shuts off the instant you unplug it? Diagnose whether the battery is dead, disconnected, or just not detected — and fix it."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-when-plugged-in-reddit.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug the charger?"
    a: "The laptop is running purely on AC power because the battery isn't contributing — it's either completely worn out, not detected by the system, disconnected internally, or its protection circuit has tripped. Windows may show 'no battery detected' or a battery icon that never really charges."
  - q: "Can a dead battery cause a laptop to shut off when unplugged?"
    a: "Yes — this is the most common cause. A battery worn past usefulness can't deliver current, so the moment AC power disappears, there's nothing to take over and the laptop dies instantly. A battery report showing near-zero full charge capacity confirms it."
  - q: "Will my laptop work without a battery if I just remove it?"
    a: "Most laptops run fine on AC power with the battery removed — that's essentially what yours is doing now. It's safe as a temporary workaround, but you lose your built-in UPS: any power flicker means an instant shutdown, so save often."
  - q: "Is it worth replacing the battery or should I get a new laptop?"
    a: "If the laptop otherwise meets your needs, a battery replacement is far cheaper — typically a fraction of a new machine's cost. Replace the battery when the machine is 1–4 years old and still performs well; consider a new laptop when the battery is one of several aging components."
---

Unplug the charger and the laptop dies instantly — not a graceful shutdown, just off, as if you'd pulled the plug on a desktop. Plug it back in and it boots fine. Your laptop has become a very portable desktop, and the battery is decorative.

This symptom is refreshingly straightforward: the battery isn't delivering power, period. The only question is why — dead cells, a detection problem, or a connection issue. Here's how to answer that and what to do about each.

## Why this happens

- **The battery is completely worn out.** Cells degraded past the point of delivering usable current — the most common cause, especially in laptops 3+ years old.
- **Windows doesn't detect the battery.** Driver corruption, an EC glitch, or a failed battery controller makes the battery invisible to the OS.
- **The battery disconnected internally.** The internal connector worked loose (drops and heat cycles do this), or corrosion broke the contact.
- **The protection circuit tripped.** Deeply discharged or overheated packs can trip their safety circuit and refuse to wake without a reset.
- **A swollen battery was disconnected.** Sometimes a previous repair shop disconnected a swelling battery for safety and never said so.
- **Charging circuit failure.** Rare, but the motherboard's charging path can fail — the battery might be fine while the board can't talk to it.

## How to fix it

Work through these in order — Fix 1 tells you which of the above you're dealing with.

### Fix 1: Check what Windows sees

1. Look at the taskbar battery icon: **no battery icon**, a **red X**, or **"no battery detected"** all point to detection failure rather than simple wear.
2. Open **Device Manager > Batteries** — is **Microsoft ACPI-Compliant Control Method Battery** present? Any warning icons?
3. Run `powercfg /batteryreport /output "C:\battery-report.html"` in an elevated terminal. If it errors out or shows no battery, Windows genuinely can't see one.
4. Check **Settings > System > Power & battery** for battery information versus a "not detected" message.
5. Detection failure → Fix 2–4. Battery detected but useless → Fix 5–6. This distinction saves you from replacing a battery that was never the problem.

### Fix 2: EC reset and driver reinstall

1. Shut down completely and unplug the charger and all peripherals.
2. Hold the **Power** button for **30 seconds** (embedded controller reset).
3. If the battery is removable, take it out, wait a minute, and reseat it firmly.
4. Plug in only the charger, boot up, and check Device Manager again.
5. If the battery appears now, generate a battery report and check capacity — an EC glitch can mask a merely worn battery. Our [battery health guide](/articles/how-to-check-battery-health-on-windows-11-laptop/) shows how to read it.

### Fix 3: Reinstall the battery drivers

1. In **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
2. Do the same for **Microsoft AC Adapter** if listed.
3. Shut down (full shutdown, not restart), unplug the charger for 30 seconds, plug back in, and power on.
4. Windows reinstalls both drivers during boot — check whether the battery is now detected.
5. If detection comes and goes, suspect the internal connector (Fix 4) rather than software.

### Fix 4: Check the physical connection

1. For removable batteries: remove it, inspect the contacts for corrosion or bent pins, clean gently with a dry cloth or pencil eraser, and reseat firmly.
2. For internal batteries: if you're comfortable opening the bottom panel (check warranty first), verify the battery connector is fully seated on the motherboard — press it gently but firmly into place.
3. Look for swelling while you're in there — a puffy battery explains everything and needs replacement, not reseating.
4. Check for liquid damage or corrosion around the battery connector.
5. If the connector looks fine but detection is intermittent, the battery's internal controller may have failed — replacement time.

### Fix 5: Confirm the battery is truly dead

1. With the battery detected, run the battery report and compare **Full Charge Capacity** to **Design Capacity**.
2. Near-zero full charge capacity, or a battery that shows 0% and never charges despite hours plugged in, means dead cells.
3. Try a full calibration cycle anyway (charge 8+ hours, then test unplugged) — very occasionally a tripped protection circuit wakes up.
4. If the laptop is under warranty, contact the maker now — batteries are often covered for the first year.
5. Our [won't-hold-charge guide](/articles/how-to-fix-laptop-battery-won-t-hold-charge-youtube/) covers the full dead-battery decision process.

### Fix 6: Replace the battery

1. Get the exact part number from the battery label (or the maker's parts lookup by serial number).
2. Buy genuine or reputable third-party — the cheapest packs fail fast and sometimes dangerously.
3. Removable: swap it yourself in seconds. Internal: follow the service manual carefully, disconnect the old pack's connector first, and never puncture the cells.
4. After installing, charge to 100% uninterrupted, then run one calibration cycle.
5. Verify with a fresh battery report — full charge capacity should be near design capacity.

### Fix 7: When it's the motherboard, not the battery

1. If a known-good battery still isn't detected or charged, the charging circuit is suspect.
2. Try a BIOS update from the maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — since charging logic lives in firmware.
3. Test with the original charger at correct wattage; an underpowered adapter can cause bizarre charging behavior (see our [charger guide](/articles/how-to-fix-laptop-charger-not-detected-step-by-step/)).
4. Motherboard-level charging faults need professional repair — get a quote before deciding.
5. As a stopgap, the laptop remains usable on AC power; just treat it like a desktop and save often.

## Closing

A laptop that only works plugged in is giving you a clear message: the battery is out of the picture. Figure out whether it's undetected (fixable: EC reset, drivers, reseat) or truly dead (replaceable: new pack, correct part number) with the battery report, and act accordingly. Either way, it's one of the most solvable laptop problems there is — your portable computer can be portable again.
