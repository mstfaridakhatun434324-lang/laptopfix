---
title: "How to Troubleshoot a Laptop That Only Runs on AC Power"
slug: troubleshoot-laptop-only-works-on-ac-power
date: 2026-10-04
categories: ["battery"]
tags: ["ac power", "diagnostics", "battery failure", "motherboard"]
description: "A technician-style diagnostic flow for laptops that die the moment AC power is removed — isolate battery, connection, or board failure."
thumbnail: "/images/thumbs/troubleshoot-laptop-only-works-on-ac-power.webp"
faqs:
  - q: "What should I check first when a laptop only works plugged in?"
    a: "Check whether Windows detects the battery at all: look at the taskbar battery icon and generate a battery report with powercfg /batteryreport. A detected-but-dead battery means wear or cell failure; a not-detected battery means driver, connection, or controller problems. That single distinction determines the whole repair path."
  - q: "Can a BIOS update fix a laptop that only works on AC?"
    a: "Sometimes. BIOS updates can fix battery-controller communication bugs and re-enable batteries stuck in ship mode or disabled states. It's worth trying before assuming hardware failure — update the BIOS from the manufacturer's support site while on AC power."
  - q: "Is it a motherboard problem if a new battery doesn't help?"
    a: "Usually, yes. If a known-good battery is detected but the laptop still dies on unplug, or if no battery is ever detected despite driver resets and reseating, the charging circuit or embedded controller on the motherboard is the likely fault — that's professional repair territory."
  - q: "Why does my laptop say 'plugged in, not charging' and then die unplugged?"
    a: "That combination means the battery can't accept or hold charge: it's either deeply worn, has a failed cell, or the charging circuit isn't delivering current to it. The laptop runs on AC passthrough fine, but there's no stored energy to fall back on."
---
This is the diagnostic companion to the quick-fix guide — a structured process for figuring out *exactly* why your laptop can't survive without its charger. We'll isolate the fault layer by layer: software, firmware, battery, connection, and finally the motherboard.

If you haven't tried the basic fixes yet, start with our [quick-fix guide](/articles/how-do-i-fix-laptop-only-works-on-ac-power/) — this page is for when you need to know precisely what's broken.

## Why this happens

- **End-of-life battery.** The cells can no longer store usable energy; voltage collapses the instant load transfers from AC to battery.
- **Battery not detected by the OS.** Driver corruption, EC glitches, or controller failure leave Windows unaware the battery exists.
- **Failed cell or protection circuit.** The battery's internal protection board may have tripped (or a cell died), cutting output entirely.
- **Loose or corroded connector.** Physical connection problems are common after drops, on aging removable batteries, or with third-party replacements.
- **Ship mode / BIOS disconnect.** Some laptops can logically disconnect the battery via BIOS; if stuck in that state, the battery is present but inert.
- **Motherboard charging-circuit failure.** The IC that manages charge/discharge can fail, leaving AC passthrough working while battery operation is dead.

## How to fix it

Work through these in order — each step rules out one layer.

### Fix 1: Classify the failure — detected or not?

Everything downstream depends on this answer.

1. Check the **taskbar battery icon**: does it show a percentage, say "no battery detected," or show nothing battery-related?
2. Run `powercfg /batteryreport /output "C:\battery-report.html"` in an **admin** Command Prompt — a report with battery data means detected; an empty/error report means not detected.
3. Open **Device Manager > Batteries** — is **Microsoft ACPI-Compliant Control Method Battery** present and healthy (no yellow icon)?
4. Write down your classification: **detected but dead** vs **not detected**. If it's the latter, our [charger and detection checklist](/articles/what-to-do-if-laptop-charger-not-detected/) has related hardware checks.

### Fix 2: For "detected but dead" — measure the wear

A detected battery that can't power the laptop is usually just finished.

1. In the battery report, compare **Full Charge Capacity** to **Design Capacity**.
2. Under **20–30%** of design (or a report showing 0 mWh) confirms end-of-life — replace the battery.
3. If wear looks moderate but the laptop still dies instantly, suspect a **failed cell** or tripped **protection circuit** — same remedy: replacement.

### Fix 3: For "not detected" — reset the software stack

Work the software layers before opening anything.

1. In **Device Manager**, uninstall **Microsoft ACPI-Compliant Control Method Battery** and restart.
2. Run `powercfg -restoredefaultschemes` in an **admin** Command Prompt to clear corrupted power configuration.
3. Update the **BIOS** from the manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — this fixes EC/battery-controller communication bugs.
4. Recheck detection after each step.

### Fix 4: EC reset and ship-mode check

The embedded controller mediates everything battery-related.

1. Shut down, unplug AC, and hold the **power button for 60 seconds** (internal battery) or remove the battery for **5 minutes** (removable).
2. Enter **BIOS/UEFI** and look for **ship mode**, **battery disconnect**, or similar — ensure the battery is logically connected.
3. Check whether the BIOS itself detects the battery and reports health — if the BIOS can't see it either, it's hardware, not Windows.

### Fix 5: Physical inspection

Eyes on the actual hardware.

1. For **removable** batteries: remove, inspect contacts for **corrosion, dirt, or damage**, clean gently, and reseat firmly.
2. Check for **swelling** — any puffiness means immediate replacement, handled carefully per our [swollen battery guide](/articles/how-to-fix-laptop-battery-swelling-reddit/).
3. For **internal** batteries: if you're comfortable opening the laptop, check that the battery cable is firmly seated on the motherboard — otherwise, take it to a shop.

### Fix 6: The swap test

The definitive hardware isolation.

1. Test with a **known-good compatible battery** if available — this is the gold standard.
2. Good battery works → your battery is dead; replace it.
3. Good battery also fails → the **motherboard charging circuit** or EC is faulty; professional board-level repair (or replacement) is needed.

### Fix 7: Living with AC-only (temporarily)

If repair must wait, minimize the risk.

1. Treat the laptop like a desktop: use a **UPS or surge protector** so power flickers don't cause instant shutdowns.
2. Enable **autosave** everywhere and consider cloud-synced documents.
3. Don't delay a swelling or overheating battery, though — those are safety issues, not inconveniences.

## Closing

The whole diagnostic comes down to one branch: battery detected (wear/cell failure → replace) or not detected (driver/EC/connection/board → work the layers). That classification, which takes five minutes, prevents hours of fixing the wrong thing. Most cases end at battery replacement — genuine batteries from the manufacturer are worth it for safety and longevity. For the software side of detection problems, our [battery not detected guide](/articles/how-to-fix-battery-not-detected-on-laptop/) covers the Windows-specific angles in depth. Document what you find at each step, even briefly: "BIOS sees battery, Windows doesn't" is exactly the kind of note that turns a vague repair-shop visit into a precise one, and it protects you from paying for exploratory labor when you've already done the exploring.

One more diagnostic worth mentioning: if you have access to a USB power meter (they're inexpensive), put it between the charger and the laptop while testing. It shows actual wattage flowing in real time — a charger delivering far less than its rating is failing even if it "works," and a laptop drawing normal wattage while the battery stays dead points squarely at the battery or charging circuit rather than the adapter. Ten dollars of measurement can save a hundred dollars of wrong parts, and it removes the last bit of guesswork from the charger side of the equation.

And remember the simplest retest of all: after each fix step, unplug the charger for ten seconds and watch what happens. It's the direct test of the actual symptom, and it's easy to skip when you're focused on indicators and Device Manager. The laptop either survives on battery or it doesn't — that binary answer after every step keeps the diagnosis honest and tells you the moment you've actually fixed it.
