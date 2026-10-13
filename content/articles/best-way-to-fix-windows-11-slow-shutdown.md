---
title: "Best Way to Fix a Slow Shutdown in Windows 11"
slug: best-way-to-fix-windows-11-slow-shutdown
date: 2026-09-27
categories: ["performance"]
tags: ["slow shutdown", "windows 11", "fast startup", "fix", "power"]
description: "The most effective fixes for Windows 11 slow shutdown, ranked by impact — from disabling Fast Startup to hunting down the hung app with Event Viewer."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-slow-shutdown.webp"
faqs:
  - q: "What is the fastest fix for slow shutdown?"
    a: "Disabling Fast Startup resolves the largest share of slow shutdown complaints with a single settings change. It takes 30 seconds: Control Panel > Power Options > Choose what the power buttons do > uncheck Turn on fast startup. If your shutdowns were hanging or taking minutes, this alone often brings them back to 15-30 seconds."
  - q: "Will disabling Fast Startup make booting slower?"
    a: "Slightly. Fast Startup makes boot faster by hibernating the kernel session instead of fully shutting down. With it off, boots take a few seconds longer — but shutdowns become cleaner and more reliable, and many shutdown hangs disappear entirely. Most users find the trade-off worthwhile."
  - q: "How do I find which app is slowing my shutdown?"
    a: "Use Event Viewer: navigate to Applications and Services Logs > Microsoft > Windows > Diagnostics-Performance > Operational, and look for events 200-210 timestamped during your slow shutdowns. The event details name the exact application or service that delayed shutdown, so you can update, replace, or remove that specific software."
  - q: "Should I change the shutdown timeout in the registry?"
    a: "You can reduce the WaitToKillServiceTimeout value to make Windows wait less long for hung services, but this treats the symptom — forcefully killing services that need time to shut down cleanly risks data loss. Fix the hanging software first; registry timeout tweaks are a last resort, not a first step."
---

If your Windows 11 laptop takes minutes to shut down — stuck on the spinning dots long after you've clicked Shut down — you don't need a troubleshooting marathon. You need the fixes ranked by how often they actually work. This guide gives you exactly that: the highest-impact fixes first, so most people solve the problem in the first two steps and never need the deeper ones.

The ranking comes from the underlying mechanics of shutdown. Windows shuts down in phases — apps close, services stop, drivers power down — and the overwhelming majority of delays come from just two sources: Fast Startup interfering with the shutdown sequence, and a single hung application or service refusing to close. Fix those two and you've covered the vast majority of cases. Everything after that is for the stubborn remainder.

Time your shutdowns as you go (count from clicking Shut down to power-off). A healthy target is 15-30 seconds. You'll know immediately when a fix works.

One more note before you start: occasional slow shutdowns right after a Windows update are normal — the system is finalizing updates. Only treat it as a problem if slow shutdowns happen consistently, update after update.

## Why this happens

- **Fast Startup hybrid shutdown bugs**: The hibernation-based shutdown conflicts with drivers and firmware on many laptops, causing hangs.
- **One hung application**: A single non-responsive app can stall the entire shutdown sequence for minutes.
- **Stubborn third-party services**: Antivirus, updaters, and vendor utilities that won't stop cleanly delay the service-stop phase.
- **Driver power-down problems**: Network and storage drivers that hang during power transition stall the final phase.
- **Windows Update finalizing**: Legitimate but slow — updates finalizing during shutdown add minutes, though only occasionally.
- **Page file clearing policy**: A security setting that wipes the page file on every shutdown, adding major delay each time.
- **USB device hangs**: External drives and docks that don't power down cleanly hold up shutdown.
- **Corrupted system files**: Damaged shutdown-related components cause unpredictable delays.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable Fast Startup (highest impact)

This single change fixes more slow shutdowns than everything else combined.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** (requires admin).
3. Uncheck **Turn on fast startup (recommended)**.
4. Click **Save changes**.
5. Shut down and time it — most users see immediate improvement to 15-30 seconds.

The trade-off: cold boots take a few seconds longer. If you hate that, you can re-enable it later — but test with it off first so you know whether it's your culprit.

### Fix 2: Close everything before shutdown (diagnostic + fix)

Determines whether a running app is the hang source.

1. Close all applications manually.
2. Open Task Manager and end remaining third-party background processes.
3. Shut down and time it.
4. If fast: the hang is one of your apps. Over the next few days, shut down with different app combinations to isolate it, then update or replace the offender.

### Fix 3: Use Event Viewer to name the culprit

When you want precision instead of trial and error.

1. Press **Win + R**, type `eventvwr.msc`, press Enter.
2. Go to **Applications and Services Logs > Microsoft > Windows > Diagnostics-Performance > Operational**.
3. Find events **200-210** from your slow shutdown times.
4. The details name the delaying app, service, or driver — update, reconfigure, or remove that specific software.
5. This is the single most precise diagnostic for shutdown issues; it removes all guesswork. Pay special attention to events marked with long durations (tens of seconds), since those are the ones actually causing your delay rather than normal background noise.

Our full [slow shutdown troubleshooting guide](/articles/windows-11-slow-shutdown-troubleshooting/) walks through Event Viewer analysis in more detail.

### Fix 4: Set problematic services to Manual

Third-party services that hang during stop phase.

1. Open **services.msc**.
2. Identify non-Microsoft services set to Automatic — especially antivirus, vendor updaters, and remote tools.
3. Double-click each suspect, set **Startup type** to **Manual**, click OK.
4. Test shutdown. Manual services still start when needed; they just don't run constantly.
5. If a specific vendor utility is the hang, check for an updated version before re-enabling.

### Fix 5: Update drivers (chipset, storage, network)

Driver power-down hangs are the deep cause behind many stubborn cases.

1. Get chipset, storage controller, and network drivers from your laptop manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — not just Windows Update.
2. Install chipset first, then storage, then network. Restart after each.
3. Check for a BIOS update too; firmware power-transition fixes are common in release notes.
4. Time a shutdown after the updates.

### Fix 6: Disconnect peripherals and check the page file policy

Two quick checks that each fix a meaningful minority of cases.

1. Unplug all USB devices and shut down — if fast, reconnect one at a time to find the offender.
2. Check the page file clearing policy: `gpedit.msc` > Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options > **Shutdown: Clear virtual memory pagefile** should be **Disabled** unless you need it for security compliance.
3. Eject external drives before shutdown as a habit if they're implicated.

### Fix 7: Repair system files

For corruption-related shutdown delays that survive everything above.

1. Open an **elevated Command Prompt**.
2. Run `sfc /scannow`, restart when done, and time a shutdown.
3. If still slow, run `DISM /Online /Cleanup-Image /RestoreHealth`, restart, retest.
4. These repair Windows' shutdown components without affecting your files or apps.

Microsoft's Windows support documentation covers additional power and shutdown settings. If startup (not shutdown) is your problem, see our guide on [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/).

## Closing

Slow shutdown in Windows 11 has a short list of usual suspects, and Fast Startup sits at the top of it. Disable it, identify any hung app with Event Viewer, tame stubborn services — and your laptop will power off in seconds instead of minutes. Ranked by impact, worked in order, done.
