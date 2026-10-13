---
title: "How to Fix a Laptop Battery Not Charging: Step by Step"
slug: how-to-fix-laptop-battery-not-charging-step-by-step
date: 2026-09-07
categories: ["battery"]
tags: ["not charging", "troubleshooting", "charger", "Windows 11"]
description: "Laptop plugged in but not charging? Work through this complete step-by-step guide from the outlet to the battery itself."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-step-by-step.webp"
faqs:
  - q: "Why is my laptop plugged in but not charging?"
    a: "Start with the physical chain: wall outlet, charger brick, cable, and charging port. Then check software: charge limits in the manufacturer's app, corrupted battery drivers, and Windows power settings. In most cases the fault is the charger or a charge limit, not the battery."
  - q: "What does 'plugged in, not charging' mean?"
    a: "It means Windows detects the charger but the battery isn't accepting charge. This is often intentional — a charge limit holding the battery at 60-80 percent — but it can also indicate a failing charger that can't sustain charging current, a worn battery, or a driver problem."
  - q: "How do I know if my charger or my battery is broken?"
    a: "Test with a known-good charger of the correct wattage first — chargers fail more often and cost less. If a good charger doesn't fix it, run powercfg /batteryreport: a battery under 60 percent of design capacity with charging failures is the likely culprit."
  - q: "Can a Windows update break battery charging?"
    a: "Yes. Updates can corrupt the ACPI battery driver, reset charge-limit settings, or install a buggy driver. If charging broke right after an update, reinstall the battery drivers and check the manufacturer's battery app settings before suspecting hardware."
---

"Plugged in, not charging" is the most searched battery problem for a reason: it has a dozen possible causes, from a dead wall outlet to a dying battery, and the fix for each is completely different. Guessing wastes money — people replace batteries when the charger was broken, and replace chargers when a setting was the issue. This guide gives you the order that wastes the least time and money — physical checks first, then settings, then drivers, then the battery itself.

## Why this happens

- **Dead outlet or power strip:** The simplest cause — no power reaching the charger at all.
- **Failing charger or cable:** Bricks die slowly; they may power the laptop but can't sustain charging current.
- **Charge limit enabled:** Manufacturer apps cap charging at 60-80 percent, which reads as "not charging" above the cap.
- **Dirty or damaged charging port:** Lint, bent pins, or a loose port break the connection intermittently.
- **Corrupted battery drivers:** The ACPI driver stack breaks after updates and misreports charging state.
- **Overheated battery:** Charging pauses when the battery is too hot, resuming when it cools.
- **Worn-out battery:** A degraded battery may refuse charge or charge so slowly it looks stuck.

## How to fix it

Follow in order. Check the battery icon after each step.

### Fix 1: Verify wall power

1. Plug the charger into a wall outlet you know works — test it with a phone charger first.
2. Skip power strips, extension cords, and surge protectors for this test.
3. Check the charger's LED (if it has one): no light means no power or a dead brick.
4. Try a second outlet in a different room to rule out a tripped breaker.

### Fix 2: Inspect the charger and cable

1. Examine the brick for swelling, cracks, discoloration, or a burnt smell.
2. Run your fingers along the cable feeling for kinks, thin spots, or fraying.
3. Check the connector for bent pins, lint, or corrosion; clean gently with a dry cloth.
4. If anything looks or smells wrong, stop using it — a failing charger is a fire risk. Borrow or buy the correct OEM replacement.

### Fix 3: Check the charging port

1. Power off and shine a flashlight into the laptop's charging port.
2. Remove lint and dust with a wooden toothpick or compressed air — never metal.
3. Plug in firmly and wiggle gently: if charging cuts in and out, the port is loose or damaged.
4. A damaged port is a repair-shop job; don't force it.

### Fix 4: Rule out a charge limit

1. Open your manufacturer's app — **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, **MSI Center**, or HP's BIOS settings.
2. Look for conservation modes or charge thresholds capping at 60-80 percent.
3. Temporarily set it to full charge and watch whether charging resumes.
4. This single check resolves a huge fraction of "not charging" reports. Related: our [ASUS stuck-at-80 guide](/articles/how-to-fix-asus-battery-health-charging-stuck-at-80/).

### Fix 5: Cool the laptop down

1. If the laptop is hot, charging may be thermally paused — feel the underside near the battery.
2. Shut down and let it cool for 20-30 minutes.
3. Charge while powered off: this removes heat from the CPU and software from the equation.
4. If it charges while off but not while on, heat or extreme power draw is the cause — see [battery drains while plugged in](/articles/how-do-i-fix-laptop-battery-drains-while-plugged-in/).

### Fix 6: Reset the battery drivers

1. Open **Device Manager > Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter** (don't delete driver software).
3. Shut down, unplug for 60 seconds, then boot on AC power — Windows reinstalls both.
4. This clears corrupted driver state, the most common software cause. Full walkthrough: [resetting the ACPI battery driver](/articles/how-to-reset-acpi-battery-driver-in-windows-11-24h2/).

### Fix 7: Update BIOS, chipset, and Windows

1. Install all **Windows Update** items, including optional driver updates.
2. Get the latest **chipset drivers** and **BIOS** from your manufacturer's support site.
3. BIOS updates often include charging-circuit firmware fixes — install on AC power and don't interrupt.
4. Retest charging after each update so you know which one fixed it.

### Fix 8: Test the battery itself

1. Run `powercfg /batteryreport` in an admin terminal.
2. If **Full Charge Capacity** is under 60 percent of **Design Capacity**, the battery is worn and may not accept charge reliably.
3. If your battery is removable, test the laptop on AC power with the battery out — if it runs fine, the adapter is good and the battery is suspect.
4. Check for swelling (uneven case, trackpad issues) — a swollen battery is a safety issue, not a troubleshooting project.

### Fix 9: Test charging outside Windows

1. Shut down, plug in the charger, and watch the charging LED for 10 minutes without booting.
2. Then boot into the BIOS/UEFI setup and leave the laptop there for 20 minutes — most BIOS screens show battery status.
3. If the battery charges in BIOS but not in Windows, the fault is 100 percent software: drivers, charge-limit apps, or Windows power settings.
4. If it won't charge even in BIOS, it's hardware: charger, port, or battery — no Windows reinstall will fix it. This single test saves hours of misdirected software troubleshooting.

## Closing

Not-charging issues reward methodical work: outlet, charger, port, charge limit, heat, drivers, battery — in that order. Most people find the answer in the first four steps, which is good because they're all free. The expensive answers (new battery, port repair) only make sense after the cheap ones are ruled out. Keep the OEM charger as your reference standard; half of all "battery problems" are really charger problems in disguise.

Microsoft's official charging troubleshooting is at the [Windows support hub](https://support.microsoft.com/en-us/windows). If your battery specifically drains while the charger is connected, read [how to fix a laptop battery that drains while plugged in](/articles/how-do-i-fix-laptop-battery-drains-while-plugged-in/).
