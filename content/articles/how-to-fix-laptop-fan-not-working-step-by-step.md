---
title: "Laptop Fan Not Working? Fix It Step by Step"
slug: how-to-fix-laptop-fan-not-working-step-by-step
date: 2026-10-13
categories: ["drivers"]
tags: ["laptop fan not working", "fan not spinning", "overheating laptop", "cpu fan error"]
description: "Laptop fan not spinning? Diagnose dead fans vs. dust-clogged cooling with BIOS tests, EC resets, and safe cleaning steps."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-not-working-step-by-step.webp"
faqs:
  - q: "Is it safe to use my laptop if the fan is not spinning?"
    a: "Only for very light use and only briefly. Modern CPUs throttle and then shut down to protect themselves, but sustained heat shortens the life of the battery and nearby components. If the fan never spins even under load, treat it as urgent: diagnose now, and avoid gaming or video rendering until it is fixed."
  - q: "Why does my fan only spin sometimes?"
    a: "That is normal on many modern laptops — the fan stays off at idle and spins up under load. It is only a fault if the fan never spins even when the CPU is hot (check temperatures with HWMonitor), or if the laptop overheats and shuts down. Fan curves are controlled by the BIOS/EC, not by Windows."
  - q: "Can dust really stop a laptop fan completely?"
    a: "Dust rarely stops the motor outright, but packed dust and pet hair can jam the blades, and dust-clogged heatsinks make the fan run at full speed constantly trying to compensate. If the fan buzzes, rattles, or spins weakly, debris or a failing bearing is likely. Compressed-air cleaning through the vents is the safe first step."
  - q: "Will updating the BIOS fix a dead fan?"
    a: "Sometimes. The embedded controller (EC) inside the BIOS firmware drives the fan, and EC bugs can leave the fan off. If the fan is not detected or never spins, a BIOS update that mentions fan, thermal, or EC fixes is worth trying. But a fan that is physically jammed or has a dead motor needs hardware service regardless of firmware."
---

A laptop fan that never spins is an emergency in slow motion. Without airflow, heat builds until the CPU throttles, performance collapses, and eventually the machine shuts itself off to survive. The tricky part is that 'fan not working' has two very different meanings: the fan is dead, or the fan is fine but never told to spin.

Modern laptops only run the fan under load, so the first job is determining which case you are in. The steps below start with that distinction — temperature monitoring and BIOS fan tests — then move through the software causes, the safe cleaning you can do yourself, and finally the hardware verdict.

## Why this happens

- **Fan only runs under load by design** — mistaken for failure at idle on modern laptops.
- **Dust and debris jamming the blades** or clogging the heatsink fins.
- **Embedded controller (EC) bug** leaving the fan off after sleep or a firmware glitch.
- **BIOS fan settings or a failed BIOS fan test**, indicating the EC cannot see the fan.
- **Dead fan motor or seized bearing** — no spin even with direct power.
- **Disconnected fan cable** after a repair or a drop.
- **Aggressive silent/fanless power profile** in vendor software capping the fan at zero.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the fan is actually broken

Install HWMonitor and watch CPU temperatures while running a heavy task like a 4K YouTube video or a benchmark. If temperatures climb past 90°C and the fan never spins, the fan is genuinely not working. If the fan spins up under load, it was never broken — your laptop just idles silently by design. Do not skip this test; it prevents fixing a non-problem. Note that heat also manifests as graphics trouble — a hot machine that crashes in games may need [the NVIDIA driver crash guide](/articles/nvidia-driver-keeps-crashing-windows-11/) after cooling is restored.

1. Install HWMonitor and note idle CPU temperatures.
2. Run a heavy workload for five minutes.
3. Watch temperatures and listen/feel for fan airflow.
4. No spin above 90°C = real fault. Spin under load = normal behavior.

### Fix 2: Run the BIOS fan test

Most laptop BIOS setups (Dell, HP, Lenovo) include a fan or cooling diagnostic. Reboot into the BIOS or the vendor's diagnostics (often F12 or F2) and run it. The test spins the fan directly, bypassing Windows entirely — if the fan spins here, the hardware is fine and the problem is software or EC configuration.

1. Reboot into the BIOS or vendor diagnostics.
2. Run the fan/cooling test.
3. Fan spins in the test = hardware OK, fix the software side.
4. Fan fails the test = hardware fault, skip to the repair steps.

### Fix 3: Reset the embedded controller

The EC controls the fan, and it can lock up. Shut down, unplug everything including the charger, hold the power button for 15-30 seconds, then reconnect and boot. On some models, removing the battery (if removable) for a minute does the same. This clears EC states that survive normal reboots and restores fan control.

1. Shut down and unplug the charger and all devices.
2. Hold the power button for 15-30 seconds.
3. Reconnect the charger and boot.
4. Stress-test and check whether the fan now spins.

### Fix 4: Check vendor power profiles

Dell Power Manager, Lenovo Vantage, HP Command Center, ASUS Armoury Crate, and MyASUS all include thermal profiles — and their quiet or silent modes can hold the fan at zero far longer than is safe. Switch to Balanced or Performance and retest. Also check Windows Power Options: the 'System cooling policy' should be Active, not Passive. Vendor thermal tools are documented on each maker's support site, such as [Dell support](https://www.dell.com/support).

1. Open the vendor's power/thermal utility.
2. Switch from Quiet/Silent to Balanced or Performance.
3. In Windows Power Options, set System cooling policy to Active.
4. Stress-test and verify the fan responds.

### Fix 5: Clean the vents and fan safely

With the laptop off and unplugged, blow compressed air through the intake and exhaust vents in short bursts, holding the can upright. This dislodges dust without opening the machine. Never spin the fan with the air blast — hold the blades still with a toothpick through the vent if you can see them, since overspinning can damage the bearing.

1. Power off and unplug the laptop.
2. Blow short bursts of compressed air through vents, can upright.
3. Avoid spinning the fan with the air stream.
4. Boot and check fan behavior under load.

### Fix 6: Update the BIOS

If the EC reset did not help, check the laptop maker's support page for a BIOS update mentioning fan, thermal, or EC fixes. Flash it with the charger connected and the battery charged, and do not interrupt the process. A BIOS update rewrites the EC firmware that drives the fan, fixing the firmware-level causes.

1. Find your exact model on the maker's support page.
2. Download the BIOS update only if the changelog mentions fan/thermal/EC.
3. Flash with the charger connected; do not interrupt.
4. Retest the fan under load.

### Fix 7: Face the hardware verdict

Fan failed the BIOS test, never spins under load, and cleaning plus EC resets changed nothing — the motor, bearing, or cable has failed. Laptop fans are model-specific parts costing little, but replacement means opening the machine. If you are comfortable, follow a teardown guide for your exact model; otherwise a repair shop charges modestly for the job. Until then, use the laptop only lightly and on a cooling pad.

1. Confirm the failure with the BIOS test and temperature monitoring.
2. Order the exact fan part number for your model if self-repairing.
3. Or take it to a repair shop — describe the failed BIOS fan test.
4. Use a cooling pad and light workloads until repaired.

## Closing

A non-spinning fan is either a misunderstanding (silent-idle design), a confused controller (EC reset or BIOS fix), a dust problem (cleaning), or a dead motor (replacement). The temperature test and the BIOS fan test tell you which within minutes, so you never waste time cleaning a fan that only needed an EC reset — or resetting an EC when the motor is seized. Heat is the enemy of every component in the chassis, so do not let this one wait. Chronic heat also shortens battery life — if the machine runs hot while charging too, see [fixing laptop overheating](/articles/how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2/).
