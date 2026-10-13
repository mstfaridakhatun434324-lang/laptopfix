---
title: "Laptop Fan Not Working: Troubleshoot Before Replacing"
slug: laptop-fan-not-working-troubleshooting
date: 2026-09-14
categories: ["drivers"]
tags: ["laptop fan not working", "fan not spinning", "overheating", "cooling"]
description: "Laptop fan not spinning? Diagnose BIOS, driver, and hardware causes of fan failure before paying for a replacement, with this Windows 11 guide."
thumbnail: "/images/thumbs/laptop-fan-not-working-troubleshooting.webp"
faqs:
  - q: "Is it normal for a laptop fan to stop sometimes?"
    a: "Yes — modern laptops use semi-passive cooling, so the fan stops at low temperatures and spins up under load. A fan that never spins even during gaming or stress tests is the problem, not one that's quiet while browsing. Test with a real workload before concluding the fan is broken."
  - q: "Can a driver cause the fan to stop working?"
    a: "Indirectly. The embedded controller (EC) manages the fan, but chipset drivers, BIOS bugs, and power plans influence its behavior. A corrupted chipset driver or a bad BIOS update can leave the fan mismanaged. Reinstalling chipset drivers and checking for BIOS updates are valid software steps before assuming hardware failure."
  - q: "How hot is too hot for a laptop CPU?"
    a: "Sustained temperatures above 95°C under load indicate a cooling problem; modern CPUs throttle around 100°C to protect themselves. Idle temperatures should sit roughly between 40-60°C depending on ambient conditions. If your CPU hits thermal limits while the fan never spins, the fan control path is broken."
  - q: "Can I run a laptop with a dead fan?"
    a: "Briefly and lightly, but it's risky. The CPU will throttle to protect itself, making the machine slow, and sustained overheating can damage the battery and other components. Limit use to light tasks, elevate the rear for airflow, and treat a dead fan as a repair-soon problem, not a configuration to live with."
---

A laptop fan that never spins is easy to misdiagnose, because modern laptops deliberately keep fans off at idle. The real test is under load: if the fan stays silent while the CPU climbs past 85°C, something is wrong — in the fan control path, the fan itself, or the software managing it. This guide troubleshoots in the right order, because replacing a fan for what turns out to be a BIOS setting is an expensive mistake.

Safety note first: a truly dead fan plus heavy load equals overheating, throttling, and potential component damage. While troubleshooting, keep workloads light and watch temperatures with a monitoring tool like HWMonitor — and if heat is the broader symptom, see [fixing laptop overheating while charging](/articles/how-to-fix-laptop-overheating-while-charging-after-windows-11-update/). Don't run stress tests on a laptop you suspect has no working cooling.

## Why this happens

- **Semi-passive cooling by design:** The fan is programmed to stay off below a temperature threshold — normal behavior.
- **BIOS fan control bug:** A BIOS update or corruption breaks the embedded controller's fan curve.
- **Dust-clogged heatsink:** The fan spins but moves no air; from outside it can seem dead or weak.
- **Fan power cable disconnected:** The fan's tiny connector works loose, especially after chassis work.
- **Failed fan motor or bearing:** The fan itself is mechanically dead — no spin even with power applied.
- **Chipset driver issues:** Corrupted chipset drivers disrupt EC communication for fan control.
- **Aggressive quiet power plan:** A silent/whisper power profile caps the fan at zero to reduce noise.
- **EC firmware stuck:** The embedded controller hangs in a bad state and never commands the fan.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the fan is actually broken

Install HWMonitor or HWiNFO and watch CPU temperature and fan RPM while putting the laptop under real load — open a dozen browser tabs with video, or run a game. If temperatures climb past 85°C with zero RPM, the fan genuinely isn't working. If the fan spins up at high temperatures, it was just semi-passive cooling doing its job. Also listen closely at the vent during load; a faint spin you can't feel is still a working fan. Don't proceed to hardware fixes until this test confirms a real failure.

1. Install HWMonitor or HWiNFO.
2. Put the laptop under sustained load.
3. Watch CPU temperature and fan RPM together.
4. Zero RPM past 85°C confirms real failure.
5. Fan spinning at high temps means normal semi-passive behavior.

### Fix 2: Check BIOS fan settings and run diagnostics

Restart into BIOS setup and look for fan or thermal settings — some BIOSes have a fan test, a "fan always on" option, or thermal profiles. Enable any built-in fan diagnostic. Many makers (Dell, HP, Lenovo) include fan tests in their boot diagnostics (F12 on Dell, F2 on HP, F10 on Lenovo). Run the full hardware scan: a failed fan test is definitive hardware evidence, while a passing test points back at Windows-side control. Note the BIOS version too — you'll need it for Fix 4.

1. Enter BIOS setup and find fan/thermal settings.
2. Enable any fan test or always-on option.
3. Run the maker's boot-time hardware diagnostics.
4. Note pass/fail on the fan test specifically.
5. Record the current BIOS version.

### Fix 3: Clean the cooling system

Power off, unplug, and open the chassis per the service manual. You'll likely find the heatsink fins packed with dust — the most common "fan problem" that isn't the fan at all. Blow out the fins and fan with compressed air (hold the fan blades still to avoid overspinning the bearing), working from inside outward. Check that the fan's power cable is firmly seated on the motherboard header — reseat it. While inside, look at the thermal paste situation only if you're experienced; repasting is optional and risky for beginners.

1. Power off, unplug, and open the chassis.
2. Blow dust from heatsink fins and fan with compressed air.
3. Hold fan blades still while cleaning.
4. Reseat the fan's power connector firmly.
5. Reassemble and retest under load.

### Fix 4: Update BIOS and chipset drivers

The embedded controller's fan logic lives in BIOS/EC firmware. Check your laptop maker's support page for BIOS updates mentioning thermal, fan, or EC fixes — [Dell's support portal](https://www.dell.com/support) or [Lenovo's support site](https://support.lenovo.com/us/en/) — and apply with the charger connected. Then reinstall the chipset driver package, which handles EC communication on many platforms ([Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can help on Intel systems). Reboot and retest the fan under load.

1. Check for BIOS updates mentioning fan, thermal, or EC.
2. Apply BIOS updates with the charger connected.
3. Reinstall the chipset driver package.
4. Reboot and retest under load.
5. Verify fan RPM responds to temperature.

### Fix 5: Reset the embedded controller

The EC can hang in a state where it never commands the fan. Reset it: shut down fully, unplug the charger, and if the battery is removable, take it out; then hold the power button for 30-60 seconds to drain residual power. On sealed-battery models, many makers have a pinhole EC reset on the bottom — hold a paperclip in it for 30 seconds. Reconnect power and boot. This clears stuck EC states without touching any software, and it revives "dead" fans more often than you'd expect.

1. Shut down fully and unplug the charger.
2. Remove the battery if possible; otherwise use the EC reset pinhole.
3. Hold the power button 30-60 seconds to drain power.
4. Reconnect and boot normally.
5. Test fan behavior under load.

### Fix 6: Check Windows power plans and fan curves

Open Power Options and switch to Balanced or High performance — some manufacturer "Quiet" or "Battery saver" plans suppress the fan aggressively. Check the maker's control app (Dell Power Manager, Lenovo Vantage, HP Command Center, ASUS Armoury Crate) for thermal profiles; set it to Balanced or Performance rather than Silent for testing. If you use third-party fan control software, disable it — conflicting fan control programs fight the EC, and Microsoft's support pages document the power plan settings involved.

1. Switch to the Balanced power plan.
2. Set the maker's thermal profile to Balanced or Performance.
3. Disable third-party fan control software.
4. Retest fan spin-up under load.
5. Re-enable quiet profiles only after confirming the fan works.

### Fix 7: Replace the fan

If the fan never spins across BIOS tests, EC resets, clean drivers, and a clean heatsink, the fan motor is dead. Laptop fans are model-specific parts — order by exact part number from the service manual, not just the laptop model. Replacement is usually a few screws and one connector, though some designs bury the fan under the heatsink assembly. While you're in there, consider fresh thermal paste if the machine is several years old. If the fan is soldered or the design is hostile, a repair shop quote is the sensible path. For related thermal issues, see our [laptop fan fix guide](/articles/how-to-fix-laptop-fan-not-working-in-windows-11-24h2/).

1. Confirm hardware failure with BIOS diagnostics.
2. Order the exact fan part number for your model.
3. Follow the service manual for replacement.
4. Consider fresh thermal paste on older machines.
5. Test thoroughly before closing the chassis.

## Closing

Fan failures are guilty-until-proven-innocent in reverse: prove the fan is actually broken under load first, then work through dust, EC resets, BIOS, and drivers before buying parts. Most "dead fan" reports end at a dust-clogged heatsink or a stuck embedded controller — both free fixes. When the motor is genuinely dead, replacement is usually straightforward; just make sure the diagnosis is solid before you order.
