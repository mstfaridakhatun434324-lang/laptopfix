---
title: "Laptop Fan Not Working? What to Do Before Panicking"
slug: what-to-do-if-laptop-fan-not-working
date: 2026-09-20
categories: ["drivers"]
tags: ["laptop fan", "not working", "overheating", "cooling"]
description: "Laptop fan not spinning? Before assuming the worst, work through these checks — from BIOS settings to power drains to real hardware tests."
thumbnail: "/images/thumbs/what-to-do-if-laptop-fan-not-working.webp"
faqs:
  - q: "Is it normal for a laptop fan to not spin sometimes?"
    a: "Yes, completely normal on modern laptops. Most current machines use semi-passive cooling — the fan stays off under light loads and only spins up when temperatures cross a threshold, typically around 50-60°C. A silent fan during web browsing is a feature, not a fault. Worry only when the laptop gets hot and the fan still doesn't spin."
  - q: "Can a laptop be damaged if the fan isn't working?"
    a: "Modern CPUs and GPUs protect themselves by throttling performance and, in extreme cases, force-shutting down — so catastrophic damage is unlikely during brief testing. But sustained overheating degrades thermal paste, stresses components, and tanks performance. Don't run heavy workloads until you've confirmed the fan situation, and shut down if temperatures climb past 95°C."
  - q: "Why would a fan stop working after a BIOS update?"
    a: "BIOS updates rewrite the fan curve tables and embedded controller firmware that governs fan behavior. Occasionally an update introduces a bug or resets custom fan settings to an overly passive profile. Check for a newer BIOS that mentions fan fixes, and look in the BIOS for fan control options that the update may have changed."
  - q: "How do I know if my fan is dead or just dirty?"
    a: "Listen and feel: a dead fan is silent even when the laptop is hot; a struggling fan makes grinding, clicking, or rattling noises. Software like HWiNFO64 shows fan RPM — zero RPM at high temperature means dead or disconnected, while erratic RPM with noise means a failing bearing. Dust alone rarely stops a fan completely, but it can slow it significantly."
---

A silent laptop fan triggers immediate dread, but here is the calming fact first: on most modern laptops, the fan is *supposed* to be silent most of the time. Semi-passive cooling keeps the fan off until temperatures demand it. So the real question is not "is my fan spinning?" but "does my fan spin when the laptop is actually hot?" Answer that under load before doing anything else, because a huge share of "fan not working" reports turn out to be normal behavior.

If the laptop is genuinely hot and the fan is genuinely still, then you have a real problem — but even then, the causes range from a BIOS setting to a dust-clogged bearing to a dead motor, and the fixes escalate accordingly. This guide orders them from observation to intervention. For the deeper troubleshooting walkthrough, see our [laptop fan troubleshooting guide](/articles/troubleshoot-laptop-fan-not-working/), and for heat-related GPU crashes, the [NVIDIA driver crashing guide](/articles/what-to-do-if-nvidia-driver-crashing/).

## Why this happens

- **Normal semi-passive behavior.** The fan correctly stays off because temperatures are below the spin-up threshold.
- **Dust and debris.** Buildup in the heatsink fins forces the fan to work harder until the bearing wears or the fan stalls.
- **Failed fan bearing.** Grinding or clicking precedes total failure; bearings wear out after years of heat.
- **BIOS/EC fan curve bug.** Firmware updates can introduce overly passive curves or break fan control.
- **Power management settings.** Aggressive quiet/eco modes suppress the fan even at moderate temperatures.
- **Disconnected fan cable.** The fan's tiny motherboard connector can loosen after drops or repairs.
- **Dead fan motor.** Electrical failure — the fan receives signal but cannot spin.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the fan is actually needed

Establish whether there is a real problem.

1. Install **HWiNFO64** and note the CPU/GPU temperatures and the fan RPM reading at idle.
2. Put the laptop under load — run a game, a 4K video, or a stress test like Cinebench — and watch temperatures climb.
3. A healthy fan starts spinning as temperatures pass roughly **50–65°C**. If RPM rises with temperature, your fan is fine and was simply idle.
4. Only if temperatures climb past **85–90°C** with the fan at 0 RPM do you have a confirmed fan problem. Stop the load test at that point to avoid overheating.

### Fix 2: Check power and thermal modes

Software can suppress the fan deliberately.

1. Open your manufacturer's control app (**MyASUS**, **Lenovo Vantage**, **Dell Power Manager**, **HP Omen Gaming Hub**, **MSI Center**, **Acer NitroSense**) and check the thermal/fan mode — **Silent**, **Quiet**, or **Eco** modes keep the fan off aggressively.
2. Switch to **Balanced** or **Performance** mode and rerun the load test from Fix 1.
3. In **Settings > System > Power & battery**, set power mode to **Best performance** while testing.
4. Check the BIOS for fan-related options (**Fan Always On**, **Fan Performance Mode**) and enable them as a test.

### Fix 3: Perform an EC reset (power drain)

Reset the embedded controller that drives the fan.

1. Shut down the laptop completely and unplug the charger and all peripherals.
2. If the battery is removable, remove it. Hold the power button for **30–60 seconds**.
3. Some laptops have a dedicated **EC reset** pinhole on the underside — press it with a paperclip for 30 seconds per the manual.
4. Reconnect power and boot. The EC reset restores default fan control behavior and clears stuck controller states that can leave the fan off.

### Fix 4: Clean the cooling system

Dust is the slow killer of laptop fans.

1. Power off and unplug. Use short bursts of **compressed air** through the intake and exhaust vents, holding the fan still with a toothpick through the vent if reachable (spinning the fan with air can damage the bearing).
2. For a thorough clean on out-of-warranty machines: remove the back panel, lift out dust mats from the heatsink fins with tweezers, and clean the fan blades with a soft brush.
3. While inside, check that the fan's cable is firmly connected to the motherboard — reseat it.
4. If the thermal paste is several years old and temperatures are high even with a spinning fan, repasting the CPU/GPU is the next step — but that is a separate job from fan repair.

### Fix 5: Update the BIOS and chipset drivers

Fix firmware-level fan control bugs.

1. Check the laptop manufacturer's support page for a BIOS update — read the release notes for mentions of fan, thermal, or EC fixes.
2. Install the BIOS update exactly per instructions, on AC power.
3. Also install the latest **chipset** driver package, since the EC and sensor readings depend on it.
4. After updating, recheck the BIOS fan settings — updates sometimes reset them — and rerun the load test.

### Fix 6: Test the fan directly and listen for bearing failure

Distinguish dead from dying.

1. With HWiNFO64 running, watch the fan RPM during the load test. **0 RPM at 90°C+** with no sound = dead motor, disconnected cable, or no signal.
2. **Erratic RPM, grinding, clicking, or rattling** = failing bearing. A fan in this state may spin sometimes — it is unreliable and will fail completely.
3. Some manufacturer apps (**Lenovo Vantage**, **Dell SupportAssist**) include a **fan diagnostic** that spins the fan to full speed on command — run it. If the diagnostic cannot spin the fan, hardware failure is confirmed.
4. A failing-but-spinning fan can sometimes be kept alive temporarily by cleaning, but plan for replacement — bearing failure does not reverse.

### Fix 7: Replace the fan or get professional repair

The endpoint for confirmed hardware failure.

1. Look up your exact model's fan part number — laptop fans are model-specific, and the CPU and GPU fans may differ.
2. Replacement fans are usually inexpensive; the cost is in the disassembly, which ranges from trivial (one panel) to involved (full motherboard removal) depending on the model.
3. Follow a video teardown for your exact model if doing it yourself, and replace the thermal paste while you are in there.
4. If the machine is under warranty, contact the manufacturer — a dead fan is a straightforward warranty claim. Until repaired, limit the laptop to light tasks and keep it on a cooling pad; avoid sustained heavy loads. For persistent overheating damage assessment, [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) covers system diagnostics, but fan replacement itself is a hardware job.

## Closing

The fan investigation starts with the least dramatic possibility — that the fan is behaving exactly as designed — and the HWiNFO64 load test in Fix 1 answers that in five minutes. From there, the escalation is logical: modes and settings, EC reset, cleaning, firmware, then the bearing-versus-motor diagnosis that tells you whether to order a part. Most "dead fan" scares end at Fix 1 or Fix 2. For the ones that do not, you now know precisely what failed and what to do about it — which beats panic every time.
