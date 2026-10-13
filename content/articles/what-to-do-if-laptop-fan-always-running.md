---
title: "Laptop Fan Always Running? What to Do Right Now"
slug: what-to-do-if-laptop-fan-always-running
date: 2026-09-20
categories: ["performance"]
tags: ["laptop fan", "overheating", "fan noise", "cooling"]
description: "Laptop fan running non-stop? Diagnose why your fan never stops and fix it — from dust-clogged vents to runaway background processes."
thumbnail: "/images/thumbs/what-to-do-if-laptop-fan-always-running.webp"
faqs:
  - q: "Is it normal for a laptop fan to run constantly?"
    a: "Brief fan activity under load is normal, but a fan that never stops — even at idle on a cool desk — signals a problem. Healthy laptops go silent or near-silent when doing light work. Constant full-speed fan means sustained heat, which comes from high CPU usage, blocked cooling, dried thermal paste, or a fan-control malfunction. It's worth investigating, not ignoring."
  - q: "Can a constantly running fan damage my laptop?"
    a: "The fan itself is just doing its job, but the underlying heat shortens component lifespan, degrades the battery faster, and causes thermal throttling that makes everything slower. A fan running at maximum for months also wears its bearings, eventually becoming noisy or failing. Fix the heat source and the fan quiets down on its own."
  - q: "Why is my fan loud even when Task Manager shows low CPU?"
    a: "Low CPU with high fan usually means poor heat transfer rather than high heat generation — dust-clogged heatsinks, dried thermal paste, or blocked vents trap normal heat inside. It can also be a stuck fan curve in the BIOS, or the GPU (not shown in the CPU column) working hard. Check GPU usage in Task Manager's Performance tab too."
  - q: "Should I use a cooling pad for a constantly running fan?"
    a: "A cooling pad helps marginally — typically 2–5°C — by improving airflow under the laptop. It's a reasonable band-aid, but it doesn't fix dust-clogged internals, dried thermal paste, or a runaway process. Use one for comfort while you address the real cause, not as a permanent substitute for cleaning and diagnosis."
---

A laptop fan that never stops is telling you something: the machine is hot, or thinks it is, all the time. Maybe it's a background process grinding away invisibly. Maybe the vents are packed with two years of dust. Maybe the thermal paste has dried into chalk. Whatever the cause, the fix starts with figuring out whether the heat is real (something generating it) or trapped (cooling that can't escape) — because those are very different repairs.

Work through this in order: software causes first (free, fast), then physical causes (cleaning, paste). For heat-related slowdowns generally, see our [overheating guide](/articles/how-to-fix-laptop-overheating-while-charging/); for the performance side, [speeding up Windows 11](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Runaway background process**: High CPU from a stuck service or app generates constant heat — the most common cause.
- **Dust-clogged vents and heatsinks**: Dust blankets the cooling fins, trapping heat no matter how hard the fan blows.
- **Dried-out thermal paste**: After 2–4 years, paste between CPU and heatsink dries, crippling heat transfer.
- **Blocked ventilation**: Using the laptop on a bed, couch, or lap smothers the intake vents.
- **Aggressive power plan**: "Best performance" mode keeps clocks high and generates heat even at light loads.
- **Stuck fan curve or BIOS bug**: Firmware telling the fan to run fast regardless of temperature.
- **GPU working in the background**: Crypto miners (malware), game launchers, or browsers using GPU acceleration heat the shared cooling system.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find the heat source in Task Manager

Software heat is the easiest to fix — check first.

1. Open **Task Manager** > **Processes**, sort by **CPU**, and look for anything consistently above 10–15% at idle.
2. Switch to the **Performance** tab and check **GPU** usage too — browsers, Discord, and game launchers can heat the GPU without touching CPU much.
3. Note temperatures if your laptop exposes them (some show in Task Manager's Performance tab; otherwise use HWMonitor or Core Temp — free).
4. Above 70°C at idle is abnormal; above 90°C under load is throttling territory. Write down your numbers.
5. If a specific process is the heater, fix that process (end it, update it, or uninstall it) — then recheck the fan.

### Fix 2: Scan for malware and miners

Malicious background load is a classic "fan never stops" cause.

1. Run a **Full scan** in **Windows Security** > **Virus & threat protection** > **Scan options**.
2. Crypto-mining malware specifically targets idle CPU/GPU — symptoms match perfectly: high load, hot laptop, nothing visible.
3. Run a second-opinion scan with the free **Malwarebytes** scanner if anything seems off.
4. Check **Task Manager** > **Startup** for unfamiliar entries, and **Task Scheduler** for suspicious tasks that relaunch miners.
5. Our [antivirus CPU guide](/articles/antimalware-service-executable-high-cpu-windows-11/) helps if Defender itself is contributing to the load.

### Fix 3: Switch to a balanced power plan

Stop the laptop from running hot for no reason.

1. Go to **Settings** > **System** > **Power & battery** > **Power mode** and select **Balanced** (not Best performance).
2. For deeper control, open **Control Panel** > **Power Options** and check which plan is active — manufacturer "performance" plans often disable CPU power-saving states.
3. In the plan's advanced settings, check **Processor power management** > **Maximum processor state** — 99% (instead of 100%) disables turbo boost, massively cutting heat with minimal performance loss on many laptops.
4. Set **System cooling policy** to **Active** (fan speeds up before throttling) rather than Passive.
5. Test for a day on Balanced — fan behavior at idle should improve noticeably if the power plan was the cause.

### Fix 4: Clear the vents and elevate the laptop

Free fixes for trapped heat.

1. Power off, then blast the intake and exhaust vents with short bursts of compressed air — hold the can upright, use the straw, and don't spin the fan to extreme speeds.
2. Always use the laptop on a hard, flat surface — beds and couches block intakes completely. A simple laptop stand or even two books at the back edge improves airflow dramatically.
3. Check that all rubber feet are intact — missing feet reduce the under-laptop air gap the cooling depends on.
4. Work in a cooler room if possible; a laptop in a 30°C room starts 5–8°C hotter than in a 22°C room, and the fan curve notices.
5. After cleaning and elevating, compare idle temperatures — a 5–10°C drop from this alone is common.

### Fix 5: Deep-clean the heatsink and fans

When compressed air through the vents isn't enough.

1. Power off, unplug, and remove the bottom panel (check a teardown video for your exact model — screw locations and clips vary).
2. Use compressed air and a soft brush to clear dust caked between the heatsink fins — this is where the real blockage lives, invisible from outside.
3. Hold fan blades still while blowing air through them to avoid overspinning the bearings.
4. Check that both fans (if two) spin freely by hand — a seized fan explains constant max-speed on the other one.
5. Reassemble and test — this is the fix for most 2+ year old laptops with gradually worsening fan noise. If you're not comfortable opening the laptop, a repair shop does this cheaply.

### Fix 6: Replace the thermal paste

For older laptops where cleaning didn't help.

1. If idle temps stay high after deep cleaning, the thermal paste has likely dried out (typical lifespan 2–4 years).
2. This involves removing the heatsink, cleaning old paste with isopropyl alcohol, and applying new paste (pea-sized dot method) — follow a model-specific teardown guide.
3. Use a quality paste (e.g., Noctua NT-H1, Arctic MX-4) — the difference vs. dried stock paste is often 10–15°C.
4. While the heatsink is off, check the thermal pads on VRAM/VRM chips — replace any that are crumbling.
5. Not comfortable? A shop charges modestly for a repaste, and the temperature improvement is usually dramatic. Only attempt if you're confident — this is the most invasive fix here.

### Fix 7: Update BIOS and check fan control

Firmware-level fan misbehavior.

1. Check your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for BIOS updates mentioning "fan," "thermal," or "cooling" — install the latest.
2. Enter BIOS/UEFI setup and look for fan or thermal settings — some laptops let you choose quiet/balanced/performance fan curves.
3. If your laptop has a manufacturer control app (Dell Power Manager, Lenovo Vantage, HP Omen Gaming Hub), check its thermal/fan profile — set it to Balanced or Quiet.
4. As a diagnostic, some apps let you manually set fan speed — if manual control works but automatic doesn't, the automatic curve is the problem.
5. After BIOS updates, recheck idle temps and fan behavior over a full day before declaring victory.

## Closing

A fan that never stops is a symptom, not the disease — it's faithfully fighting heat that shouldn't be there. Find the heat (runaway process, dust, dead paste), fix the heat, and the fan remembers how to be quiet. Start with Task Manager, end with thermal paste, and don't skip the free steps in between.
