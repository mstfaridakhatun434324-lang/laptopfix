---
title: "Laptop Slow Only When Plugged In? Fix for Windows 11 24H2"
slug: "how-to-fix-laptop-slow-when-plugged-in-in-windows-11-24h2"
date: "2026-10-02"
categories: ["performance"]
tags: ["laptop slow when plugged in", "charging slowdown", "power plan", "windows 11 24h2", "thermal throttling"]
description: "Your laptop is fast on battery but crawls when you plug in the charger? This 24H2-specific slowdown has a few known causes — here's how to diagnose and fix each one."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-when-plugged-in-in-windows-11-24h2.webp"
faqs:
- q: "Why is my laptop slower when charging than on battery?"
  a: "Charging adds significant internal heat, and modern laptops throttle the CPU to protect components when temperatures rise. Additionally, a 24H2 power-management bug can apply the wrong power plan state, and some chargers fail to deliver the wattage the laptop expects, triggering a low-power safety mode that caps performance."
- q: "Can a faulty charger make my laptop slow?"
  a: "Yes. If the charger can't deliver its rated wattage — because of a damaged cable, a failing power brick, or a low-wattage third-party adapter — the laptop's firmware detects the shortfall and locks the CPU at a low frequency. You will see full battery charging but terrible performance. Test with the original charger to rule this out."
- q: "Does Windows 11 24H2 change power plans when plugged in?"
  a: "Yes, Windows switches between separate battery and AC power-plan profiles. 24H2 introduced changes to how these profiles apply, and on some laptops the plugged-in profile ends up with overly aggressive throttling or a stuck power-saver state. Manually reviewing both profiles in the advanced power settings usually reveals the problem."
- q: "Should I disable CPU throttling when plugged in?"
  a: "You can raise the minimum processor state for the plugged-in profile, which helps if throttling is too aggressive, but you should not disable thermal protection entirely. Throttling exists to prevent overheating damage. If your laptop runs hot while charging, clean the vents and cooling system first, then adjust power settings."
---

It's one of the weirdest performance problems you'll ever see: unplug the charger and your laptop runs fine, plug it in and everything stutters. It feels backwards — you'd expect plugged-in power to mean *more* performance, not less. But this is a real, reported pattern, especially on Windows 11 24H2, and it almost always traces back to one of three things: heat from charging, a power-plan mismatch, or a charger that isn't delivering what the laptop expects.

The diagnosis matters here because the fixes are opposites. If heat is the cause, you cool the laptop down. If it's a power-plan bug, you change settings. If it's the charger, no setting in the world will help — you need different hardware. Run through the checks in order and you'll land on the right one.

## Why this happens

- **Charging generates extra heat** — the battery charging circuit adds 10–20°C of internal heat, pushing the CPU into thermal throttling sooner than on battery.
- **24H2 applies the wrong power-plan state** — a known behavior where the plugged-in profile gets stuck in a power-saver configuration after the update.
- **Underpowered or failing charger** — the firmware detects insufficient wattage and caps CPU frequency as a safety measure.
- **Dust-clogged cooling** — vents and fans that barely cope on battery can't handle the extra heat of charging, so throttling kicks in fast.
- **BIOS power management bugs** — some laptop BIOS versions mishandle the AC/battery transition after a Windows update changes the handshake.
- **Background tasks triggered on AC power** — Windows schedules heavy maintenance (indexing, updates, Defender scans) to run when plugged in, stealing CPU.
- **Battery in poor health** — a degraded battery draws charge inefficiently, generating more heat and confusing the power management firmware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the pattern and check temperatures

First, verify this is really a plugged-in problem and measure what's happening thermally. Guessing wastes time.

Steps:

1. Unplug the charger, open Task Manager → Performance tab, and note your CPU speed under a moderate load.
2. Plug in the charger, wait two minutes, and check the CPU speed again under the same load.
3. Install a temperature monitor (HWiNFO or Core Temp) and compare CPU temps plugged vs. unplugged.
4. If temps jump 15°C+ when plugged in and CPU frequency drops, heat is your primary suspect.
5. If temps are fine but frequency still drops, the cause is power-plan or charger related — skip to Fix 3.

### Fix 2: Clean the cooling system

If heat is the trigger, this is the fix. Dust is the number one cause of laptops that can't handle charging heat.

Steps:

1. Shut down the laptop completely and unplug everything.
2. Use short bursts of compressed air through the exhaust vents (hold the can upright).
3. For a deeper clean, remove the bottom panel (check your manual — some laptops make this easy) and clear dust from fans and heatsink fins.
4. If the laptop is over two years old, consider having the thermal paste replaced by a technician.
5. Test again plugged in — on many machines, this alone restores full speed.
6. As a stopgap, elevate the rear of the laptop or use a cooling pad while charging.

### Fix 3: Check and fix the plugged-in power plan

24H2 changed how power plans behave, and the AC profile is where the bug bites. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has current guidance on power settings.

Steps:

1. Go to **Settings → System → Power & battery**.
2. Check the Power mode dropdown while plugged in — set it to **Best performance**.
3. Open Control Panel → Power Options and click "Change plan settings" on your active plan.
4. Click "Change advanced power settings" and expand **Processor power management**.
5. Set "Minimum processor state" for Plugged in to 50–100% (try 80% as a starting point).
6. Check "Maximum processor state" for Plugged in is 100%.
7. Expand "PCI Express → Link State Power Management" and set Plugged in to **Off** — this one setting causes slowdowns on many laptops.

### Fix 4: Stop background maintenance from hogging AC power

Windows deliberately runs heavy maintenance when plugged in. If your laptop is borderline thermally, this pushes it over the edge.

Steps:

1. Open Task Scheduler and check **Microsoft → Windows → TaskScheduler** for the "Regular Maintenance" task timing.
2. In Settings → Windows Update, check whether updates are downloading/installing while you work — pause updates during work hours.
3. Reschedule Windows Defender full scans to overnight (see our guide on [Antimalware Service Executable high CPU](/articles/what-to-do-if-antimalware-service-executable-high-cpu-fix/)).
4. In Settings → Privacy & security → Windows Security → Device performance & health, review the health report for driver issues.
5. Consider switching active hours so restarts and maintenance don't collide with your usage.

### Fix 5: Test with the original charger

This is the fastest hardware test you can do, and it rules out the most expensive mistake — chasing software fixes for a hardware problem.

Steps:

1. Unplug any dock, hub, or USB-C adapter between the charger and the laptop.
2. Connect the charger that came with the laptop directly to the wall outlet.
3. Check the charger's rated wattage (printed on the brick) matches your laptop's requirement.
4. In the BIOS or your manufacturer's power app, look for a message like "AC adapter not recognized" or a wattage reading.
5. If performance returns with the original charger, your third-party or aging charger is the problem — replace it with a correctly rated unit.

### Fix 6: Update the BIOS and chipset drivers

The firmware handles the AC/battery handoff, and manufacturers release BIOS updates specifically to fix power-management quirks after Windows updates.

Steps:

1. Check your current BIOS version (run `msinfo32` and look at "BIOS Version/Date").
2. Visit your manufacturer's support page and compare against the latest release for your exact model.
3. Install the BIOS update following the manufacturer's instructions exactly — keep the charger connected during the update.
4. Also install the latest chipset and power-management drivers.
5. After updating, re-check the plugged-in power plan settings, since BIOS updates can reset them.

### Fix 7: Reset power plans to defaults and rebuild

If settings have been tweaked over time, a clean reset of the power subsystem clears out stuck states from the 24H2 update.

Steps:

1. Open an elevated Command Prompt.
2. Run `powercfg /restoredefaultschemes` to reset all power plans to factory defaults.
3. Restart the laptop.
4. Set your preferred plan again and re-apply the Fix 3 adjustments.
5. If your manufacturer provides a power management utility (Lenovo Vantage, Dell Power Manager), check its thermal and charging profiles too — these can override Windows settings.

## Closing

A laptop that's slow only when plugged in is telling you something specific: heat, a power-plan glitch, or a weak charger. The temperature check in Fix 1 points you down the right path in five minutes, and from there it's either cleaning, settings, or hardware. If the slowdown persists after all of these, run a [full performance tune-up](/articles/how-to-speed-up-windows-11-laptop/) to rule out background software drag — but in my experience, the plugged-in-only pattern resolves at Fix 2, 3, or 5.
