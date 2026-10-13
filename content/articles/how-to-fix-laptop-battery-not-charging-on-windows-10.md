---
title: "Laptop Battery Not Charging on Windows 10: Proven Fixes"
slug: how-to-fix-laptop-battery-not-charging-on-windows-10
date: 2026-09-02
categories: ["battery"]
tags: ["not charging", "windows 10", "plugged in"]
description: "'Plugged in, not charging' on Windows 10? Reset the battery driver, check the charger, and work through these proven fixes in order."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-not-charging-on-windows-10.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean on Windows 10?"
    a: "Windows detects the charger but the battery isn't accepting charge. Common causes: a charge limit set by manufacturer software (Dell, Lenovo, ASUS all have them), a worn battery the controller paused on, a driver issue, or a charger problem. It's a status, not a diagnosis — the fixes below find the actual cause."
  - q: "How do I fix plugged in not charging on Windows 10?"
    a: "Start with the driver reset: uninstall the Microsoft ACPI-Compliant Control Method Battery in Device Manager and reboot. Then check for manufacturer charge limits, test the charger, update the BIOS, and evaluate battery health — in that order."
  - q: "Can a Windows 10 update stop the battery charging?"
    a: "Yes — updates can install a bad battery driver, reset EC behavior, or re-enable a charge limit. If charging broke right after an update, the driver reset plus checking manufacturer software settings resolves most cases."
  - q: "When is 'not charging' actually normal?"
    a: "When a charge limit is active: Lenovo Conservation Mode holds at 60%, Dell's custom profiles stop at your set ceiling, ASUS caps at 80%. 'Plugged in, not charging' at exactly 60% or 80% is the limit working as designed — check your manufacturer's app before troubleshooting."
---
"Plugged in, not charging." Four words that turn a laptop into a desktop. The charger is connected, Windows sees it, but the battery percentage sits frozen — or worse, slowly drops. On Windows 10 this is one of the most reported power issues, and it has a satisfyingly high fix rate: most cases resolve in the first three steps below.

Before anything else: check whether a charge limit is doing this on purpose (Fix 1). It saves a lot of unnecessary troubleshooting — and it's the answer more often than you'd guess.

## Why this happens

- **A manufacturer charge limit is active.** Lenovo Conservation Mode (60%), Dell custom ceiling, ASUS 80% cap — all report "not charging" when the limit is reached. This is the #1 "false alarm."
- **The battery driver is corrupted.** Especially after Windows 10 updates, the ACPI driver can lose proper communication with the pack.
- **The charger is inadequate or failing.** Wrong wattage, damaged cable, or a dying brick that Windows detects but can't draw charging current from.
- **The battery is worn out.** Controllers pause charging on badly degraded packs or charge them so slowly it looks like nothing.
- **Overheating protection.** Hot batteries pause charging until they cool — common during gaming or in warm rooms.
- **The EC needs a reset.** The embedded controller's charging logic can latch into a stuck state that survives reboots.
- **A recent BIOS update changed charge behavior.** Firmware updates sometimes adjust charge thresholds or re-enable manufacturer charge management with new defaults — if "not charging" appeared right after a BIOS flash, check the manufacturer's app for a newly activated limit.

## How to fix it

Work through these in order — the first fix alone resolves a huge share of cases.

### Fix 1: Check for an intentional charge limit

1. Think: is the battery stuck at exactly 60% or 80%? Those are the classic limit values, not random failure points.
2. Open your manufacturer's app — **Lenovo Vantage** (Conservation Mode), **Dell Power Manager** (Battery Settings), **MyASUS** (Battery Health Charging), **Acer Care Center** — and check whether a charge limit is enabled.
3. If you want a full charge, disable the limit temporarily; if the laptop lives on a desk, leave it on — it's protecting your battery.
4. The Lenovo version is detailed in [turning on Conservation Mode](/articles/how-to-turn-on-conservation-mode-lenovo-on-windows-10/).

### Fix 2: Reset the battery driver

1. Right-click **Start** > **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**. Repeat for any duplicate entry.
3. **Shut down** fully — hold **Shift** while clicking Shut down to bypass Windows 10's fast startup.
4. Unplug the charger for 60 seconds. If the battery is removable, take it out too.
5. Reconnect everything and boot. Windows rebuilds the driver stack; charging usually resumes.

### Fix 3: Reset the embedded controller

1. With the laptop off and unplugged (battery out if removable), hold the power button for 30 seconds.
2. This drains flea power and resets the EC's charging logic — the component that actually decides "charge" vs. "not charging."
3. Reconnect AC first, then battery, then boot.

### Fix 4: Test the charger properly

1. Verify wattage: the brick's rating should match the laptop's requirement.
2. Try a different wall outlet, no power strip.
3. Inspect cable and port for damage; try the manufacturer's genuine charger if you're on a third-party one.
4. If you have access to another compatible charger, swap it — a charger that "works" for running the laptop can still fail at delivering charge current.

### Fix 5: Rule out heat

1. If the laptop is hot, power it off and let it cool 20–30 minutes.
2. Clean vents with compressed air; use a hard surface.
3. Charging resumes on its own once the battery temperature drops back into the safe window — no setting to change.

### Fix 6: Update BIOS and chipset drivers

1. Check the manufacturer's support page for BIOS updates: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Flash with AC connected.
3. Update the chipset driver from the same page — it handles the OS-to-EC communication path.

### Fix 7: Evaluate the battery's health

1. Open an admin **Command Prompt** and run `powercfg /batteryreport`.
2. High wear (50%+) with "not charging" often means the controller has given up on the pack — replacement is the fix.
3. Run the manufacturer's diagnostic (Dell ePSA via **F12**, HP via **Esc** > **F2**, Lenovo Vantage scan) for a definitive answer.
4. If the battery is swollen, stop here and read the [swollen battery safety guide](/articles/best-way-to-fix-battery-swelling-slightly-laptop-safe/).
5. For the deeper dive on charge-while-off variants, see [battery only charges when off](/articles/troubleshoot-battery-only-charges-when-laptop-is-off/).

### Fix 8: Know the "normal" cases so you don't chase ghosts

1. "Plugged in, not charging" at 95–100% with a healthy battery is often just the controller's float behavior — lithium doesn't like being force-topped, so charging pauses near full and resumes when it dips. That's not a fault.
2. Some business laptops delay charging when the battery is above 90% by design (charge hysteresis) to reduce micro-cycling.
3. If the status appears only near full charge and the battery works fine otherwise, it's working as designed — check [design vs full charge capacity](/articles/troubleshoot-design-capacity-vs-full-charge-capacity/) to confirm the pack is healthy and move on.
4. Real faults show "not charging" at low percentages or with a draining battery — those are the ones this guide is for.

## Closing

"Plugged in, not charging" on Windows 10 is usually a charge limit doing its job, a driver needing a reset, or a tired charger — in that order of likelihood. Check the limit first, reset the driver second, and you'll fix most cases without spending anything. And remember Fix 8's normal cases: near-full "not charging" is the battery protecting itself, not a problem to solve.
