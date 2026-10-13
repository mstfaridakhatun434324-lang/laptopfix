---
title: "How to Fix High CPU Usage on an ASUS Laptop"
slug: how-to-fix-high-cpu-usage-on-asus-laptop
date: 2026-09-12
categories: ["performance"]
tags: ["high cpu", "asus laptop", "windows 11", "armoury crate", "troubleshooting"]
description: "ASUS laptop CPU pinned at 100%? From Armoury Crate bloat to Windows services, here's how to find the culprit and fix high CPU usage on ASUS machines."
thumbnail: "/images/thumbs/how-to-fix-high-cpu-usage-on-asus-laptop.webp"
faqs:
  - q: "Why do ASUS laptops often have high CPU usage?"
    a: "ASUS ships Armoury Crate, MyASUS, and several background services that poll hardware sensors and check for updates continuously. Combined with the usual Windows background processes, this creates higher-than-average idle CPU usage. Gaming models add more services for RGB lighting, fan control, and performance profiles."
  - q: "Is Armoury Crate causing my high CPU usage?"
    a: "It can be. Armoury Crate runs multiple background services (ArmouryCrateService, Armoury Crate User Session Helper) that sometimes get stuck polling hardware. If Task Manager shows these near the top of CPU usage, updating or reinstalling Armoury Crate — or replacing it with the lighter G-Helper alternative — usually fixes it."
  - q: "Should I uninstall MyASUS?"
    a: "MyASUS is relatively light and useful for driver and BIOS updates, so most users should keep it. If Task Manager shows its services consuming CPU constantly, try updating it first through the Microsoft Store. Only uninstall it if you've confirmed it's the culprit and you get drivers another way."
  - q: "Does the ASUS power plan affect CPU usage?"
    a: "Yes. ASUS power profiles (Silent, Performance, Turbo) change how aggressively the CPU boosts. Turbo mode keeps clocks high even at light loads, which shows as higher CPU percentages and more heat. For everyday use, the Windows Balanced plan or ASUS Silent profile gives the best mix of responsiveness and efficiency."
---

ASUS laptops — especially ROG and TUF gaming models — are powerful machines, but they have a reputation for busy background activity. Between Armoury Crate's hardware-monitoring services, MyASUS utilities, and the standard Windows background processes, an ASUS laptop can show surprisingly high CPU usage while doing nothing at all. Add a stuck Windows service or a runaway app to the mix, and you've got a machine that's hot, loud, and sluggish.

The diagnostic approach is the same as on any Windows laptop: find the specific process, then fix that process. But ASUS machines have their own usual suspects that are worth checking first, because the fix for "Armoury Crate service stuck at 25% CPU" is completely different from the fix for "Windows Update worker stuck at 50%." This guide covers both the ASUS-specific culprits and the general Windows ones, in the order a technician would check them.

Before you start, open Task Manager (Ctrl + Shift + Esc), sort by CPU, and write down the top processes. That list determines which fixes below actually apply to your situation.

## Why this happens

- **Armoury Crate background services**: ArmouryCrateService and its helpers continuously poll sensors and devices; bugs or corrupted installs make them consume far more CPU than they should.
- **MyASUS and ASUS update services**: Scheduled update checks and system diagnostics run in the background, occasionally getting stuck.
- **Aggressive performance profiles**: Turbo/Performance modes in Armoury Crate keep CPU clocks boosted, inflating usage percentages and heat at idle.
- **Windows Update and telemetry**: The usual Windows culprits (TiWorker, CompatTelRunner, SearchUI) hit ASUS laptops like any other — see our general [high CPU checklist](/articles/how-to-fix-high-cpu-usage-on-acer-laptop/) for those.
- **RGB and peripheral services**: LightingService and device-specific helpers for keyboards, mice, and headsets add constant low-level CPU load.
- **Outdated ASUS drivers**: Old chipset or ACPI drivers from ASUS can cause the System process to consume excessive CPU.
- **Bloatware and startup accumulation**: Preinstalled McAfee trials, ASUS GiftBox, and other bundled software pile onto startup and background load.
- **Dust and thermal throttling**: Gaming laptops collect dust fast; clogged cooling makes the CPU throttle, which keeps usage percentages high.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact process

Don't skip this. The fix depends entirely on what's actually consuming CPU.

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Sort the **Processes** tab by **CPU**, highest first.
3. Write down the top 3 process names and their percentages.
4. If an ASUS service (ArmouryCrateService, LightingService, asus*) is at the top → Fixes 2–3. If it's a Windows process → Fixes 4–5. If it's a third-party app → Fix 6.

### Fix 2: Update or repair Armoury Crate

A corrupted Armoury Crate install is the single most common ASUS-specific cause of high CPU. The fix is to update it cleanly.

1. Open the **Microsoft Store**, go to Library, and update **Armoury Crate** and **MyASUS** to the latest versions.
2. If CPU usage persists, uninstall Armoury Crate completely: **Settings > Apps > Installed apps > Armoury Crate > Uninstall**.
3. Download the official Armoury Crate uninstall tool from ASUS support, run it, and restart.
4. Reinstall Armoury Crate fresh from the Microsoft Store.
5. Check Task Manager after reinstalling — the services should now idle near zero.

Some users prefer **G-Helper**, a lightweight open-source alternative that replaces Armoury Crate for fan and power control with a fraction of the background load. It's worth considering if Armoury Crate keeps misbehaving.

### Fix 3: Switch to a sensible power profile

Turbo mode is for gaming, not for browsing the web. Running it 24/7 keeps your CPU boosted and hot.

1. Open **Armoury Crate** and set the operating mode to **Silent** or **Performance** for everyday use — reserve **Turbo** for gaming.
2. Alternatively, in Windows **Settings > System > Power & battery**, set the power mode to **Balanced** or **Best power efficiency**.
3. Check Task Manager after switching — idle CPU percentages should drop noticeably.

### Fix 4: Clean up ASUS bloatware and startup items

ASUS bundles trial software that most users never need, and each piece adds background load.

1. Open **Settings > Apps > Installed apps** and remove: McAfee trial (Windows Security is enough for most users), ASUS GiftBox, and any bundled games or utilities you don't use.
2. Keep **MyASUS** if you use it for updates; remove it only if testing proves it's the problem.
3. In Task Manager's **Startup apps** tab, disable everything non-essential.
4. Restart and compare idle CPU usage.

Our [bloatware removal guide](/articles/how-to-remove-bloatware-from-windows-11-laptop/) walks through a full cleanup.

### Fix 5: Update ASUS drivers and BIOS

Outdated chipset, ACPI, and BIOS versions cause the System process to burn CPU on ASUS hardware. ASUS tests driver packages specifically for your model.

1. Open **MyASUS** and check for driver and BIOS updates for your exact model number. For Intel-based systems, the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can identify the correct chipset drivers.
2. Install chipset drivers first, then ATK/ACPI drivers, then everything else.
3. Update the BIOS only on AC power with the battery charged — never interrupt a BIOS update.
4. Restart and check whether System process CPU usage has dropped.

### Fix 6: Handle runaway Windows processes

If Task Manager points at Windows components rather than ASUS software, apply the standard fixes.

1. **SearchUI.exe / Cortana high** → follow our [Cortana high CPU fix](/articles/how-to-fix-cortana-high-cpu-step-by-step/).
2. **CompatTelRunner.exe high** → follow our [CompatTelRunner fix](/articles/best-way-to-fix-compattelrunner-high-cpu/).
3. **Antimalware Service Executable high** → check for an active scan in Windows Security, and uninstall the McAfee trial if it's conflicting.
4. **Service Host high** → see our guide on [fixing Service Host high CPU](/articles/how-to-fix-service-host-high-cpu-youtube/).

### Fix 7: Clean the cooling system

Gaming laptops ingest enormous amounts of dust. When cooling degrades, the CPU thermal-throttles, and throttled CPUs show higher usage percentages for the same work.

1. Power off and unplug the laptop.
2. Blow compressed air through the intake and exhaust vents (short bursts, hold the fan still if you can).
3. For older machines, consider a repaste — but only if you're comfortable opening the chassis, as it voids some warranties.
4. After cleaning, monitor temperatures with HWMonitor during normal use.

Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) has additional performance diagnostics if you've worked through this list and still see unexplained high usage.

## Closing

High CPU on ASUS laptops usually traces back to one of three things: a misbehaving Armoury Crate install, too-aggressive performance profiles, or the standard Windows background culprits. Work the list in order, test after each change, and you'll find the specific cause — most ASUS users see idle CPU drop back to single digits without any hardware changes.
