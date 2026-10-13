---
title: "Fan Won't Quit on Windows 10? Cool Your Laptop Down"
slug: how-to-fix-laptop-fan-always-running-on-windows-10
date: 2026-09-28
categories: ["performance"]
tags: ["laptop fan always on", "windows 10 fan noise", "fan running constantly", "cpu overheating"]
description: "Laptop fan blasting nonstop on Windows 10? Diagnose the heat source — from SysMain to dust buildup — and quiet things down with these Windows 10-specific fixes."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-always-running-on-windows-10.webp"
faqs:
  - q: "Why is my Windows 10 laptop fan so loud compared to when it was new?"
    a: "Three things change with age: dust accumulates in the heatsink, thermal paste dries out, and the software load grows — more startup apps, heavier background services, and years of Windows updates. A laptop that was whisper-quiet in 2020 can be a hair dryer in 2026 purely from dust and software creep. The fixes below address both the age-related and software causes."
  - q: "Does Windows 10 have fan control settings?"
    a: "Not directly — Windows controls the CPU's heat output, and the BIOS/EC controls the fan in response. What you can control in Windows 10: the power plan (which sets how aggressively the CPU boosts), maximum processor state, and which background tasks run. Some manufacturers add fan-profile software (Dell Power Manager, Lenovo Vantage, ASUS Armoury Crate) that does control the fan curve."
  - q: "Is SysMain (Superfetch) making my fan run?"
    a: "It can contribute. SysMain preloads frequently-used apps into RAM, which means disk and CPU activity — especially on HDD-equipped laptops, where it can keep the drive and CPU busy enough to raise temperatures. If your laptop has an SSD, SysMain's benefit is minimal and disabling it is a reasonable test; on HDDs, leave it on unless it's clearly misbehaving."
  - q: "Should I disable Windows Update to stop the fan?"
    a: "No — disabling updates trades a temporary annoyance for real security risk, and updates aren't usually the constant heat source anyway. What's more common: an update stuck downloading or installing, looping forever. Fix the stuck update (Settings, Update & Security, Troubleshoot) rather than disabling the whole system. A healthy, fully-updated Windows 10 idles quietly."
---

Windows 10 laptops have their own flavor of the never-ending fan problem. The OS is older, the hardware is older, and the usual suspects skew toward classic Windows 10 background services — SysMain hammering an old hard drive, Windows Update stuck in a retry loop, or a power plan that never lets the CPU rest. Add a few years of dust, and the fan has no choice but to scream.

The diagnostic approach is the same as on any Windows version: find what's generating heat, then fix that — not the fan. But the specific steps differ on Windows 10, from the classic Control Panel power plans to services like SysMain that behave differently here than on Windows 11. For the Windows 11 version of this problem, see [fan always running on Windows 11](/articles/how-to-fix-laptop-fan-always-running-on-windows-11/); for heat-focused guidance, [laptop overheating while charging](/articles/how-to-fix-laptop-overheating-while-charging-on-windows-11/) applies across versions.

Start with the software diagnosis — most Windows 10 fan issues resolve without opening the laptop.

## Why this happens

- **SysMain keeping old drives busy**: On HDD-equipped Windows 10 laptops, SysMain's preloading can saturate the disk, keeping CPU and drive active and warm.
- **Windows Update stuck in a loop**: A failed update that retries forever keeps the CPU and disk churning — a classic Windows 10 fan cause.
- **High-performance power plan**: Many older laptops sit on the High performance plan, which disables CPU idle states and generates constant heat.
- **Startup program creep**: Years of installed software means dozens of startup entries, each adding CPU load from the moment you log in.
- **Dust and dried thermal paste**: Older hardware means more accumulated dust and aging thermal interface — cooling efficiency drops year over year.
- **Antimalware scans colliding with use**: Third-party antivirus suites on Windows 10 often schedule heavy scans during active hours.
- **Failing hard drive working overtime**: A dying HDD retries reads repeatedly, staying active and hot — the fan responds to the sustained load.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the heat source

Two minutes in Task Manager tells you whether you're fighting software or hardware.

1. Press Ctrl + Shift + Esc, sort the Processes tab by CPU, and watch for two minutes.
2. Switch to the Details tab and sort by CPU there too — services like svchost hide there.
3. Note disk activity as well: on HDD laptops, 100% disk usage generates real heat.
4. Low CPU and low disk at idle points to cooling/hardware; anything pegged points to software.

### Fix 2: Set the Balanced power plan and cap max CPU

Windows 10's classic power plans are the biggest lever you have over idle heat.

1. Open Control Panel, Power Options, and select Balanced.
2. Click Change plan settings, then Change advanced power settings.
3. Under Processor power management, set Maximum processor state to 95% on battery and plugged in — this disables turbo boost, cutting heat dramatically with minimal performance loss.
4. Set System cooling policy to Passive on battery so Windows slows the CPU before ramping the fan.

### Fix 3: Fix a stuck Windows Update

A looping update is one of the most common constant-heat causes on Windows 10.

1. Open Settings, Update & Security, Windows Update, and check for a stuck or repeatedly failing update.
2. Run the Windows Update troubleshooter from Settings, Update & Security, Troubleshoot.
3. If it persists, stop the Windows Update service, delete C:\Windows\SoftwareDistribution\Download contents, and restart the service.
4. Let updates complete fully once — a settled system idles far quieter.

### Fix 4: Tame SysMain on SSD systems

On SSD-equipped laptops, SysMain's preloading buys little and can cost heat. Test with it off.

1. Press Win + R, type services.msc, and press Enter.
2. Find SysMain, double-click it, and set Startup type to Disabled, then stop the service.
3. Use the laptop for a day and compare fan behavior and responsiveness.
4. If nothing improves, set it back to Automatic — on HDD systems it genuinely helps. See also [Superfetch high disk usage on HP laptops](/articles/how-to-fix-superfetch-high-disk-usage-on-hp-laptop/).

### Fix 5: Trim startup programs

Years of installs mean years of startup entries. Cut them ruthlessly.

1. In Task Manager, open the Startup tab and sort by Startup impact.
2. Disable everything rated High impact that you don't need immediately at login.
3. Pay special attention to updaters, chat apps, and cloud storage you rarely use.
4. Restart and enjoy a cooler, quieter login.

### Fix 6: Clean dust from vents and fans

On a laptop old enough to run Windows 10 from new, dust is nearly guaranteed.

1. Shut down, unplug, and remove the bottom cover per your manufacturer's manual.
2. Blow short bursts of compressed air through the heatsink fins and fan, holding fan blades still.
3. Check that the fan spins freely by hand — a grinding fan needs replacement, not cleaning.
4. While inside, visually check for swollen capacitors or a bulging battery.

### Fix 7: Check drive health and consider an SSD

A failing HDD runs hot and slow; an SSD upgrade is the single best revival for an old Windows 10 laptop.

1. Open an admin Command Prompt and run wmic diskdrive get status to check SMART status.
2. Listen for clicking or grinding — back up immediately if you hear it.
3. If the drive is healthy but slow, cloning to an SSD cuts heat, noise, and boot time together.
4. Microsoft's storage guidance at [Microsoft's Windows support site](https://support.microsoft.com/en-us/windows) covers the built-in tools.

## Closing

On Windows 10, a constantly running fan is usually a software story — stuck updates, SysMain on old drives, or a power plan that never idles — layered over aging hardware that needs a cleaning. Work the software side first: Balanced plan, settled updates, trimmed startup. Then open it up and evict the dust. Most Windows 10 laptops go from hair dryer to whisper with just the first three fixes.
