---
title: "How to Fix a Laptop Fan Not Working on Windows 10"
slug: how-to-fix-laptop-fan-not-working-on-windows-10
date: 2026-09-18
categories: ["drivers"]
tags: ["laptop fan not working", "windows 10", "overheating laptop", "fan control", "cooling fix"]
description: "Laptop fan not spinning on Windows 10? Diagnose whether it is a driver, BIOS, or dead fan — with safe tests and seven fixes ordered by risk."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-not-working-on-windows-10.webp"
faqs:
  - q: "Is it normal for my laptop fan to never spin?"
    a: "Often, yes. Most modern laptops use passive cooling at idle and light loads — the fan stays off below roughly 50–65°C to keep the machine silent. It should spin up audibly under sustained load like gaming, video rendering, or stress tests. Only worry if temperatures climb past 85–90°C under load with no fan activity, or if the machine thermal-throttles during tasks that used to run cool and quiet."
  - q: "Can a Windows update break my laptop fan?"
    a: "Indirectly, yes. Updates that replace the chipset driver, power management subsystem, or BIOS-adjacent firmware can disrupt communication with the embedded controller that drives the fan, or reset cooling policies to passive. Reinstalling the chipset driver from the laptop maker's site and checking the BIOS cooling mode resolves most update-triggered fan issues."
  - q: "How hot is too hot for a laptop CPU?"
    a: "Sustained temperatures above 95°C under load indicate a cooling problem — the CPU will throttle performance to protect itself, and prolonged overheating shortens component life. Brief spikes into the 90s during heavy all-core work are normal on thin laptops; what matters is whether the fan responds and temperatures stabilize. If the machine idles above 70°C, clean the cooling system regardless of fan behavior."
  - q: "Should I replace the thermal paste when fixing fan issues?"
    a: "Only if temperatures remain high after cleaning and confirming the fan works. Dried thermal paste typically becomes a factor after 3–5 years. Repasting requires full heatsink removal and carries real risk of damage on laptops with fragile ribbon cables — treat it as advanced maintenance, not a first step. Clean dust and verify fan operation first; repaste only if load temps stay excessive with a working fan and clear vents."
---

A laptop fan that never spins is an emergency disguised as a minor annoyance: modern CPUs throttle hard when hot, so the machine feels merely 'slow' right up until heat damages something. Before assuming the fan is dead, know that most laptop fans are supposed to sit still at idle — many models do not spin below 50–60°C by design. The real question is whether the fan spins under load.

When a fan genuinely fails to respond to heat, the causes split into software (BIOS fan curves, chipset/EC drivers, Windows power plans parking the fan) and hardware (seized bearing, broken fan cable, failed fan header). Software causes are far more common after Windows updates that touch the chipset or power subsystem — which is why this sits in the drivers category.

Test first: run a demanding task and watch temperatures. If the fan stays dead while the CPU climbs past 85°C, work through the fixes below. For broader [Device Manager driver checks](/articles/how-to-check-driver-version-in-device-manager-on-windows-10/) during diagnosis, that guide covers the workflow used here.

## Why this happens

- **Fan curve set to passive in BIOS/power plan** — Silent profiles keep the fan off until high temperatures; a stuck profile never ramps up.
- **Chipset / embedded controller driver issue** — The EC manages fans; a bad chipset driver after a Windows update can break EC communication.
- **Dust-clogged heatsink and seized bearing** — Dust mats block airflow so thoroughly the fan cannot move air; bearings seize after years.
- **Fan cable disconnected or damaged** — The tiny fan header cable can work loose, especially after any disassembly.
- **BIOS bug or outdated firmware** — Some BIOS versions mishandle fan tables; vendors fix this in updates.
- **Third-party fan control software conflict** — Notebook FanControl or vendor tools fighting the EC can park the fan.
- **Dead fan motor** — Motors do fail — usually with warning signs like grinding noise beforehand.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the fan actually should be spinning

Do not 'fix' normal behavior. Confirm a real fault under controlled load first.

1. Install HWiNFO64 and note CPU/GPU temperatures at idle.
2. Run a stress test (Cinebench, or a heavy game) for 5 minutes while watching temps.
3. If the fan spins up as temps pass ~65–70°C, it is healthy — your 'problem' was the passive-at-idle design.
4. If temps exceed 90°C with zero fan activity, continue — the fault is real.

### Fix 2: Check BIOS fan settings

The firmware owns the fan curve. A wrong setting here overrides everything Windows does.

1. Restart into BIOS/UEFI (Del/F2/Esc depending on maker).
2. Look for Fan, Cooling, Thermal, or Performance settings.
3. Set fan/cooling mode to **Active** or **Performance** (not Silent/Passive) for testing.
4. Save, boot into Windows, and repeat the load test.

### Fix 3: Reinstall chipset and EC-related drivers

The embedded controller talks to Windows through the chipset driver. Refreshing it restores fan control after bad updates.

While you are refreshing drivers, it is worth confirming the rest of the driver stack is healthy too — a general [driver health check](/articles/how-to-check-driver-version-in-device-manager-on-windows-10/) takes a few minutes and rules out companion issues. Chipset, BIOS, and power-management drivers all interact with the embedded controller, so a fully current stack gives the fan control path the best chance of working.

1. Download the latest **chipset driver** for your exact laptop model from the manufacturer's support site.
2. In Device Manager, expand System devices and uninstall the chipset/Intel Management Engine entries (do not delete drivers unless reinstalling).
3. Install the downloaded chipset package and restart.
4. Also update the BIOS if the maker lists fan/thermal fixes in the changelog — follow their instructions exactly.

### Fix 4: Clean the cooling system

A fan buried in dust cannot cool, and the EC may not even bother spinning a blocked fan hard. This is maintenance, not repair.

1. Power off, unplug, and remove the bottom panel (check your model's service manual).
2. Hold the fan blades still and blow dust out with short bursts of compressed air — never let the fan spin freely from air pressure.
3. Clear the heatsink fins and vents; a solid dust mat peels off in one piece on neglected machines.
4. Reassemble, boot, and load-test. If the fan now spins, schedule cleaning every 6–12 months.

### Fix 5: Remove third-party fan control software

Two drivers fighting over the EC means nobody wins and the fan parks.

1. Uninstall Notebook FanControl, SpeedFan, or similar tools.
2. In vendor apps (Armoury Crate, OMEN Hub, Lenovo Vantage), set thermal mode to **Balanced/Performance** and disable manual fan curves.
3. Restart and load-test with only the vendor's default control active.
4. Reintroduce custom curves only after confirming the default works.

### Fix 6: Reset the power plan to defaults

Corrupt power-plan settings can pin the cooling policy to passive permanently.

1. Open Command Prompt as admin and run `powercfg -restoredefaultschemes`.
2. In Power Options > Change plan settings > Change advanced power settings, expand **Processor power management > System cooling policy** and set it to **Active** for both battery and plugged-in.
3. Restart and load-test. Microsoft's [Windows power support](https://support.microsoft.com/en-us/windows) documents these policies.

### Fix 7: Inspect the fan hardware

When software is exhausted, look with your eyes. Only proceed if you are comfortable opening the machine.

1. Open the bottom panel and locate the fan's thin cable to the motherboard header — reseat it firmly.
2. Try spinning the blades by hand: gritty resistance or wobble means a seized bearing.
3. Check for a replacement fan by part number (usually printed on the fan) — laptop fans are model-specific but inexpensive.
4. If the cable and fan look fine yet nothing spins under 95°C load, the motherboard fan header or EC may have failed — professional repair territory.

## Closing

A silent laptop fan is normal at idle and an emergency under load — the load test in Fix 1 is what separates the two. From there, BIOS cooling mode, chipset drivers, and dust cover the vast majority of genuine faults; only the last fix involves hardware, and by then you will know with confidence whether the fan itself is dead. If your problem is the mirror image — the fan screaming non-stop even at idle — the [fan always running on Windows 10](/articles/how-to-fix-laptop-fan-always-running-on-windows-10/) guide diagnoses that side of the coin.
