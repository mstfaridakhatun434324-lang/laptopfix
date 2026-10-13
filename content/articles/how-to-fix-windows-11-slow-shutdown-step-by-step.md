---
title: "Windows 11 Slow Shutdown? A Step-by-Step Fix Guide"
slug: how-to-fix-windows-11-slow-shutdown-step-by-step
date: 2026-10-11
categories: ["performance"]
tags: ["slow shutdown", "windows 11", "step by step", "shutdown hang", "troubleshooting"]
description: "Windows 11 taking minutes to shut down? Follow this ordered, step-by-step guide to find the hang and restore fast shutdowns."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-shutdown-step-by-step.webp"
faqs:
  - q: "What is the first thing to check when shutdown is slow?"
    a: "Check Event Viewer after a slow shutdown: Windows Logs > System, looking for the time gaps around Event ID 1074 (shutdown started). The Diagnostics-Performance log (Event ID 203) often names the exact application or service that delayed shutdown. Starting with evidence instead of random tweaks saves hours and prevents you from breaking things that weren't broken."
  - q: "Should I disable Fast Startup to fix slow shutdown?"
    a: "It's one of the most effective single steps. Fast Startup hibernates the kernel session during shutdown, and on systems with certain storage or chipset drivers that hibernation write hangs. Disabling it (Control Panel > Power Options > Choose what the power buttons do) frequently converts multi-minute shutdowns into 15-second ones, at the cost of slightly slower cold boots."
  - q: "Can Windows updates cause slow shutdown every time?"
    a: "Updates legitimately extend shutdown when they need to finalize — but only for that one shutdown. If every shutdown is slow, you likely have a stuck or repeatedly-failing update retrying each time. Check Settings > Windows Update > Update history for red failed entries, clear the update cache, and install the failing KB manually from the Microsoft Update Catalog."
  - q: "Is editing shutdown timeouts in the registry safe?"
    a: "The commonly recommended tweaks — lowering WaitToKillAppTimeout, WaitToKillServiceTimeout, and enabling AutoEndTasks — are safe and widely documented. They only change how long Windows waits before force-closing hung programs during shutdown; they don't affect normal operation. Export the keys before editing so you can restore them if needed."
---

A slow shutdown is death by a thousand cuts: Windows politely asks every running program and service to close, and each one that dawdles adds its delay to your evening. This guide is deliberately ordered — each step builds on the last, and most people find their culprit by step 3 or 4 without needing the heavier repairs at the end. Budget about 30 minutes and a couple of restarts.

Before starting: time one shutdown with your phone's stopwatch so you have a baseline. Anything consistently over 60 seconds is worth fixing; the goal is 10–20 seconds. For the HP-specific version of this problem, see [slow shutdown on HP laptops](/articles/how-to-fix-windows-11-slow-shutdown-on-hp-laptop/); for shutdowns that hang forever rather than just crawl, [shutdown takes too long](/articles/best-way-to-fix-shutdown-takes-long-windows-11/).

## Why this happens

- **Programs ignoring the shutdown signal**: Apps with background tasks or unsaved state that don't close when asked.
- **Services with long stop timeouts**: Windows gives services 20 seconds each by default — a few slow ones stack up fast.
- **Fast Startup hibernation hanging**: The kernel-session hibernate write stalls on certain drivers.
- **Pending or stuck Windows updates**: Finalization work — or a failed update retrying — at every shutdown.
- **Network waits**: Mapped drives, offline files, or domain timeouts blocking the shutdown sequence.
- **Corrupt hibernation or pagefile**: Damaged hiberfil.sys turns the Fast Startup write into a long stall.
- **Third-party "shutdown" utilities and overlays**: Ironically, tools that promise to speed up shutdown sometimes hook the process and slow it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure and identify the hang (10 minutes)

Evidence first, tweaks second.

1. Time a full shutdown with a stopwatch: click **Shut down**, start the timer, stop it when the power light goes off. Write down the number.
2. Boot up, open **Event Viewer** > **Windows Logs** > **System**, and find **Event ID 1074** (the shutdown you just did). Note its timestamp.
3. Open **Applications and Services Logs** > **Microsoft** > **Windows** > **Diagnostics-Performance** > **Operational**, and look for **Event ID 203** entries near that time — the details name the application or service that degraded shutdown and by how many milliseconds.
4. Common named culprits: cloud sync clients, browser updaters, printer software, and audio services. Write down every repeat offender.
5. If Event ID 203 names nothing and the gap is between 1074 and the kernel power-off event, the delay is in the driver/service phase — continue to Fix 2.

### Fix 2: Close the identified culprits before shutdown (5 minutes)

Test whether the named offenders are really the cause.

1. For the next two shutdowns, manually quit the apps named in Event Viewer first (right-click tray icons > **Quit/Exit** — not just closing the window).
2. If shutdown is suddenly fast, you've confirmed the culprit. Make the fix permanent: disable the app's **launch at startup** (Task Manager > **Startup apps**) if you don't need it resident, or check its settings for a "close to tray" vs "fully exit" option.
3. For cloud sync apps (OneDrive, Dropbox, Google Drive): pause syncing before shutdown as a test. If that fixes it, the app was finishing uploads during shutdown — schedule large syncs for when you're actively using the PC.
4. For browser updaters and helper processes: disable their background persistence in the app's settings ("Continue running background apps when the browser is closed" — turn it off).
5. Re-time shutdown. If it's now under 30 seconds, you're done — skip to the Closing. If not, the hang is systemic: continue.

### Fix 3: Disable Fast Startup (5 minutes)

The highest-yield single toggle for shutdown hangs.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**, uncheck **Turn on fast startup (recommended)**, and **Save changes**.
3. Perform a full **Shut down** (not Restart) and time it — this is the first shutdown without the hibernation write.
4. If shutdown drops to normal speed, the hibernation write was hanging — usually a storage/chipset driver issue worth updating (see Fix 6), but leaving Fast Startup off is a fine permanent choice on SSD systems.
5. If shutdown is still slow, leave Fast Startup off for now (it removes one variable) and continue — you'll revisit it at the end.

### Fix 4: Tighten shutdown timeouts in the registry (10 minutes)

Stop Windows from waiting so politely.

1. Press **Win+R**, type `regedit`, and back up first: right-click **Computer** > **Export** (or export the specific keys below).
2. Go to `HKEY_CURRENT_USER\Control Panel\Desktop`: set **WaitToKillAppTimeout** to `5000`, **HungAppTimeout** to `2000`, and **AutoEndTasks** to `1` (create as String values if missing).
3. Go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`: set **WaitToKillServiceTimeout** to `5000`.
4. These change the shutdown waits from 20 seconds to 5 seconds per hung item — normal apps still close instantly; only hung ones get hurried along.
5. Restart (to load the new values), then time a shutdown. Documented further on Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Rule out stuck Windows updates (15 minutes)

Updates should extend shutdown once — not every night.

1. Open **Settings** > **Windows Update** > **Update history** — look for failed updates with error codes.
2. If failures repeat: open `services.msc`, stop **Windows Update**, rename `C:\Windows\SoftwareDistribution\Download` to `Download.old`, restart the service, and **Check for updates**.
3. Let one full update cycle complete while plugged in — don't shut down mid-install to "test" speed.
4. If a specific KB keeps failing, download it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it directly.
5. After updates are fully clean, time another shutdown — update finalization no longer in the mix.

### Fix 6: Update chipset, storage, and BIOS drivers (20 minutes)

Power-transition bugs live in low-level drivers.

1. Open **Device Manager** > expand **IDE ATA/ATAPI controllers** and **Storage controllers** — note the driver dates. Anything over a year old is suspect.
2. Get fresh drivers: [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel systems, AMD's driver support page for AMD, or your laptop vendor's support site for OEM-tuned versions.
3. Update the **BIOS** if a newer version lists power, shutdown, or S3/modern-standby fixes in its changelog — follow the vendor's instructions exactly with the charger connected.
4. Also update the **network adapter** driver — network drivers waiting on timeouts are a classic shutdown delayer, especially with mapped drives.
5. After driver updates, you can experimentally re-enable Fast Startup (reverse Fix 3) to see if the underlying conflict is resolved.

### Fix 7: Clean-boot isolation and repair install (30+ minutes)

For shutdowns that resist everything above.

1. Press **Win+R**, type `msconfig` > **Services** tab > check **Hide all Microsoft services** > **Disable all** > **OK** > restart.
2. Time a shutdown in the clean-boot state. If it's fast, re-enable services in halves (binary search) until the slowdown returns — you've found your hanging service.
3. Common winners of this grim lottery: printer/scanner services, third-party firewall services, and RGB peripheral services.
4. Once identified, set the offending third-party service to **Manual** or update/reinstall its parent software.
5. If even a clean boot shuts down slowly, run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` — deep system corruption can stall the shutdown path itself. For related boot/shutdown performance, see [fixing slow boot on SSD](/articles/best-way-to-fix-windows-11-boot-time-slow-ssd/).

## Closing

Slow shutdown is a solvable, step-by-step problem — not a mysterious Windows curse. Measure it, name the hanging component in Event Viewer, eliminate the usual suspects (Fast Startup, dawdling apps, stuck updates), and tighten the timeouts. Most shutdowns go from minutes back to seconds by step 4, and the few that don't have a driver or service culprit that the clean-boot binary search will smoke out.
