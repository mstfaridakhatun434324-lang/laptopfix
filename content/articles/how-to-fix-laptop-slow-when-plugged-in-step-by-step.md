---
title: "How to Fix a Laptop That Runs Slow When Plugged In (Step by Step)"
slug: "how-to-fix-laptop-slow-when-plugged-in-step-by-step"
date: "2026-09-20"
categories: ["performance"]
tags: ["laptop slow when plugged in", "charger slow performance", "power plan issues", "thermal throttling", "windows power settings"]
description: "Laptop slower on AC power than on battery? That is backwards — and fixable. Follow this step-by-step guide to find whether the charger, power plan, or thermals are to blame."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-when-plugged-in-step-by-step.webp"
faqs:
  - q: "Can a phone charger make my laptop slow when plugged in?"
    a: "Yes, absolutely. USB-C phone chargers typically deliver 18–25W, while most laptops need 45–65W or more. The laptop detects the weak supply and throttles the CPU to stay within it, which feels exactly like ‘slow when plugged in.’ Always use a charger rated at or above your laptop's required wattage, printed on the original brick or the spec sheet."
  - q: "Why is my laptop fast on battery but slow on AC?"
    a: "On battery, the CPU runs at modest clocks and stays cool. On AC, it tries to boost to full speed — which exposes weak chargers (power-limit throttling), dirty cooling (thermal throttling), or misconfigured plugged-in power states. The AC boost itself is what reveals the underlying weakness, so the fix targets the charger, cooling, or power settings, not the battery."
  - q: "Will a higher-wattage charger damage my laptop?"
    a: "No. Laptops only draw the power they need; a 90W charger on a 65W laptop is perfectly safe as long as the voltage matches (USB-C PD negotiates this automatically, and barrel chargers must match the printed voltage). Using a higher-wattage OEM-quality charger is actually the fix when the original brick was underpowered."
  - q: "Should I update the BIOS to fix AC throttling?"
    a: "It is worth checking. Embedded-controller firmware controls how the laptop responds to AC power detection, and manufacturers do fix power-state bugs in BIOS updates. Only update from your manufacturer's official support site, follow their instructions exactly, and keep the laptop on AC with a charged battery during the flash — an interrupted BIOS update can brick the machine."
---

A laptop that slows down the moment you plug in the charger is experiencing something backwards: AC power should unlock maximum performance, not throttle it. Yet it happens — stuttering, laggy typing, and fans screaming the instant the power brick connects. The usual suspects are a counterfeit or underpowered charger, a power plan that misbehaves on AC, or thermal and firmware logic that misreads the power state.

Because the trigger is so specific (plugged in = slow, on battery = fine), diagnosis is actually straightforward. Work through these steps in order and you will isolate whether the charger, the power settings, or the cooling system is responsible — each has a very different fix.

## Why this happens

- **Underpowered or third-party charger:** A 45W brick on a laptop that wants 65W+ forces power-limit throttling the moment it connects.
- **Faulty charger or damaged cable:** Voltage droop under load makes the EC (embedded controller) panic and throttle the CPU protectively.
- **Power plan set to throttle on AC:** Misconfigured ‘plugged in’ processor states can cap CPU below its battery behavior.
- **BIOS/EC power-state bug:** Outdated firmware may apply the wrong power limits when AC is detected.
- **Thermal throttling masked on battery:** On battery the CPU already runs slower and cooler; on AC it boosts, hits thermal limits, and throttles hard.
- **Dust-clogged cooling revealed by AC boost:** The extra heat of AC-boosted clocks overwhelms a dirty heatsink that coped fine at battery clocks.
- **Background tasks triggered by AC:** Indexing, updates, and backups configured to run ‘only when plugged in’ all fire at once.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with the original charger (or a known-good one)

The charger is suspect number one. An underpowered or failing brick is the most common cause of ‘slow when plugged in,’ and the test is simple: borrow the correct wattage and compare.

1. Check the wattage printed on your original charger and on the laptop's spec sheet.
2. Test with the original OEM charger if you have been using a third-party one.
3. If the laptop behaves normally with the right charger, replace the bad brick with an OEM-equivalent.
4. Inspect the DC jack and cable for looseness or damage while you are at it.

### Fix 2: Compare power plans for plugged-in vs battery

Windows keeps separate settings for battery and AC. If the plugged-in processor state got set strangely — by an optimizer tool or a Windows bug — the CPU may be capped harder on AC than on battery. [Switching to the Best performance power plan](https://support.microsoft.com/en-us/windows) for the plugged-in state is the quick baseline test.

1. Go to Settings > System > Power & battery and set Power mode to Best performance.
2. Open the legacy Power Options (search ‘power plan’) > Change plan settings > Change advanced power settings.
3. Under Processor power management, verify Maximum processor state is 100% for Plugged in.
4. Set Minimum processor state for Plugged in to 5–10% so idle still idles.

### Fix 3: Check thermals: AC boost may be exposing overheating

On battery, your CPU sips power and stays cool. On AC it boosts to full clocks, generates far more heat, and — if the cooling is compromised — slams into thermal throttling that feels like ‘slow when plugged in.’ Monitor temperatures to confirm.

1. Install HWMonitor or HWiNFO and watch CPU package temperature on battery vs plugged in.
2. If temps jump past 95°C on AC and clocks collapse, cooling is the issue.
3. Blow out vents with compressed air and ensure the laptop sits on a hard flat surface.
4. If cleaning does not help, the thermal paste or fan may need professional service.

### Fix 4: Update BIOS and chipset drivers

The embedded controller decides power limits based on what it detects from the charger. Firmware bugs here cause exactly this symptom — throttling on AC that no Windows setting explains. Manufacturers regularly fix power-state behavior in BIOS updates.

1. Identify your exact model and check the manufacturer's support site for BIOS updates.
2. Install the latest chipset and power-management drivers too.
3. Apply the BIOS update on AC power with the battery charged (follow the maker's instructions exactly).
4. Retest plugged-in performance after the update.

### Fix 5: Stop AC-triggered background task storms

Windows Update, Search indexing, OneDrive sync, and backup tools are often configured to run aggressively ‘when plugged in.’ The moment you connect power, they all wake up at once — which looks exactly like charger-caused slowness. Trimming [startup and background load](/articles/how-to-disable-startup-programs-windows-11/) reduces this pile-on.

1. Open Task Manager when the slowdown hits and sort by CPU and Disk.
2. If TiWorker, SearchIndexer, or OneDrive top the list, those are your culprits.
3. Reschedule backups and indexing to overnight hours.
4. In OneDrive settings, pause syncing during work hours if needed.

### Fix 6: Reset power plans to defaults

If settings have been mangled by ‘optimizer’ utilities, the cleanest fix is a full reset of every power plan to factory defaults, then reconfiguring only what you need.

1. Open Command Prompt as administrator.
2. Run powercfg -restoredefaultschemes and press Enter.
3. Restart the laptop, then set Power mode to Best performance again.
4. Test plugged-in behavior before reinstalling any optimizer tools — leave them off.

### Fix 7: Rule out a failing battery confusing the EC

A degraded battery can send erratic signals to the embedded controller, which then misjudges available power and throttles on AC. If the battery is swollen, drains in minutes, or reports nonsense percentages, it may be the hidden cause. A general [laptop speed-up pass](/articles/how-to-speed-up-windows-11-laptop/) will not fix this — the battery needs testing.

1. Generate a battery report: run powercfg /batteryreport in Command Prompt.
2. Open the report and compare Design Capacity vs Full Charge Capacity.
3. If wear exceeds 40–50%, consider a battery replacement.
4. Test with the battery removed (if removable) on AC alone.

## Closing

A laptop that slows down when plugged in is telling you something specific: the charger, the AC power configuration, or the thermals that AC-boosted clocks expose. Start with the charger swap test — it resolves the majority of cases in minutes — then verify power-plan settings and temperatures before touching firmware. Worked in order, these steps turn a baffling backwards symptom into a straightforward fix.
