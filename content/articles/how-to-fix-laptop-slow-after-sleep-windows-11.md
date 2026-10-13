---
title: "Laptop Slow After Sleep in Windows 11? Wake It Back Up to Speed"
slug: how-to-fix-laptop-slow-after-sleep-windows-11
date: 2026-10-09
categories: ["performance"]
tags: ["slow after sleep", "windows 11", "wake from sleep", "sleep performance", "laptop slow"]
description: "Laptop sluggish for minutes after waking from sleep in Windows 11? Fix the drivers, power settings, and background tasks causing post-sleep slowdowns."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-after-sleep-windows-11.webp"
faqs:
  - q: "Why is my laptop so slow right after waking from sleep?"
    a: "After waking, Windows 11 re-initializes drivers, restores compressed memory pages, and resumes background tasks that were suspended. If a driver (often graphics, Wi-Fi, or chipset) re-initializes slowly, or if Windows Update and maintenance tasks fire immediately on wake, the system stays sluggish for several minutes. Outdated drivers and aggressive Modern Standby networking are the two most common culprits."
  - q: "Should I use sleep, hibernate, or shutdown on my laptop?"
    a: "For short breaks, sleep is fine. For overnight or longer, hibernate saves more battery and avoids the slow-wake driver dance, since the system fully powers off after writing RAM to disk. Shutdown is cleanest but slowest to resume. If sleep consistently wakes slowly, switching your lid-close and power-button actions to hibernate is a practical workaround while you fix the underlying driver issue."
  - q: "Does Fast Startup affect waking from sleep?"
    a: "Fast Startup only affects cold boots, not sleep resume, but its hibernation file is involved in hybrid sleep. Disabling hybrid sleep and hibernate can simplify the resume path and rule out a corrupt hiberfil.sys as the cause. If wake speed improves after turning hibernate off, delete and rebuild the hibernation file with powercfg commands."
  - q: "Can a background app cause slow wake from sleep?"
    a: "Yes. Apps with wake timers — backup tools, messaging apps, updaters — can start heavy work the instant the machine wakes, competing with the resume process for CPU and disk. A clean boot that isolates the problem to a third-party app confirms this. Check Task Scheduler for tasks configured to run on workstation unlock as well."
---

You close the lid, grab coffee, open it back up — and your laptop behaves like it just woke from a coma. The mouse stutters, windows take forever to redraw, the fan spins up, and for two or three minutes the machine is barely usable. Then, mysteriously, it recovers and runs fine. This post-sleep sluggishness in Windows 11 is one of the most reported laptop complaints, and it's almost never a sign of failing hardware.

What actually happens on wake: the system brings every driver back online, decompresses memory pages, re-establishes Wi-Fi, and restarts suspended tasks. If any link is slow — a graphics driver re-initializing badly, a network driver scanning endlessly, a scheduled task firing on unlock — the whole resume feels broken. For the related problem where the machine takes too long to wake at all, see [fixing a laptop that's slow to wake from sleep](/articles/how-to-fix-laptop-slow-to-wake-from-sleep-step-by-step/); for slowness tied to AC power specifically, see [fixing a laptop that's slow when plugged in](/articles/how-to-fix-laptop-slow-when-plugged-in-step-by-step/).

## Why this happens

- **Outdated chipset or graphics drivers**: Drivers that re-initialize slowly after sleep stall the entire resume sequence.
- **Hybrid sleep with a corrupt hiberfil.sys**: A damaged hibernation file makes every resume read garbage before recovering.
- **Modern Standby network activity**: The Wi-Fi stays partially active during sleep, syncing mail and updates that all demand CPU on wake.
- **Wake timers firing maintenance tasks**: Windows Update, disk optimization, and app updaters launching the moment you unlock.
- **USB selective suspend misbehaving**: External devices (docks, drives, dongles) that don't resume cleanly force driver retries.
- **Memory compression backlog**: With limited RAM, Windows compresses pages during sleep and must decompress them on wake — CPU-heavy on older processors.
- **Third-party apps resuming badly**: Antivirus, VPN clients, and sync tools (OneDrive, Dropbox) that hammer the disk the second the session unlocks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update chipset, graphics, and network drivers

Stale drivers are the number one cause of slow resume.

1. Open **Device Manager**, expand **System devices**, and note your chipset — then visit your laptop maker's support page for the latest chipset driver package rather than relying on Windows Update alone.
2. Update the graphics driver from the GPU vendor: use [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics, [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx) for GeForce GPUs, or AMD's driver page for Radeon graphics.
3. In **Device Manager**, expand **Network adapters**, right-click your Wi-Fi adapter > **Update driver** — and then check the manufacturer's site, since Windows Update often lags on Wi-Fi drivers.
4. Restart (a full restart, not sleep) after driver updates so the new drivers load cleanly.
5. Test: sleep the laptop for 10 minutes, wake it, and time how long until it's responsive. Note the improvement — or lack of it — before moving on.

### Fix 2: Disable hybrid sleep and rebuild the hibernation file

Simplify the resume path and rule out hiberfil.sys corruption.

1. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings**.
2. Expand **Sleep** > **Allow hybrid sleep** and set it to **Off** for both battery and plugged in.
3. Open an elevated Command Prompt and run `powercfg /h off`, wait a few seconds, then run `powercfg /h on` — this deletes and recreates the hibernation file cleanly.
4. While you're in the power settings, expand **Sleep** > **Hibernate after** and set a generous value (e.g., 180 minutes) so short naps use plain sleep.
5. Sleep and wake the laptop twice to confirm the resume feels snappier.

### Fix 3: Tame wake timers and scheduled maintenance

Stop the pile-on of tasks that fire the instant you unlock.

1. In the advanced power settings from Fix 2, expand **Sleep** > **Allow wake timers** and set it to **Disable** (or **Important Wake Timers Only** if you rely on alarms).
2. Open **Task Scheduler** (`taskschd.msc`) and check **Task Scheduler Library** > **Microsoft** > **Windows** > **UpdateOrchestrator** — note any tasks set to run on unlock or wake.
3. Go to **Settings** > **Windows Update** > **Advanced options** and pause updates for a week as a test — if post-sleep slowness vanishes, update activity was the culprit.
4. Open **Settings** > **System** > **Notifications** and turn off **suggestions** and tips, which can trigger background content downloads on wake.
5. Check third-party apps: backup tools, cloud sync, and messaging apps often surge on unlock — stagger or disable their auto-start in Task Manager's **Startup apps** tab.

### Fix 4: Disable USB selective suspend and PCIe power saving

These power-saving features can make device resume painfully slow.

1. In advanced power settings, expand **USB settings** > **USB selective suspend setting** and set it to **Disabled** for both battery and plugged in.
2. Expand **PCI Express** > **Link State Power Management** and set it to **Off** (plugged in) — this stops the PCIe bus from downshifting aggressively during sleep.
3. In **Device Manager**, expand **Universal Serial Bus controllers**, right-click each **USB Root Hub** > **Properties** > **Power Management**, and uncheck **Allow the computer to turn off this device to save power**.
4. If you use a docking station, check the dock manufacturer's support page for firmware updates — docks are notorious for slow resume handshakes.
5. Test wake speed with external devices disconnected, then reconnected, to isolate a misbehaving peripheral.

### Fix 5: Reduce memory pressure before sleep

Less compressed memory means a faster wake.

1. Press **Ctrl+Shift+Esc**, check the **Performance** > **Memory** tab — if you're regularly above 80% usage, the system compresses heavily during sleep.
2. Close memory-hungry apps (browsers with dozens of tabs, Electron apps) before closing the lid — or at least let the system idle a minute before sleeping so it can settle.
3. Check your pagefile: **Settings** > **System** > **About** > **Advanced system settings** > **Performance Settings** > **Advanced** > **Virtual memory** — leave it **system managed** unless you have a specific reason to change it.
4. Run **Windows Memory Diagnostic** (`mdsched.exe`) to rule out bad RAM — faulty memory makes resume decompression error-prone and slow.
5. If the laptop has 8 GB or less RAM and you constantly multitask, a RAM upgrade is the honest long-term fix for resume sluggishness.

### Fix 6: Turn off network connectivity during Modern Standby

Stop the Wi-Fi from doing chores while the laptop sleeps.

1. Open an elevated Command Prompt and run `powercfg /a` — if it lists **Standby (S0 Low Power Idle)**, your laptop uses Modern Standby.
2. Go to **Settings** > **System** > **Power & battery** > **Screen, sleep, & hibernate timeouts** and review what's allowed to run during sleep.
3. In advanced power settings, look for **Sleep** > **Allow network connectivity during connected-standby** (wording varies) and set it to **Disable** — the laptop will fully disconnect Wi-Fi during sleep.
4. In **Device Manager**, open your Wi-Fi adapter's **Properties** > **Power Management** and check **Allow the computer to turn off this device to save power**.
5. Trade-off: no instant email/sync on wake — but wake itself becomes dramatically faster.

### Fix 7: Clean-boot to catch the misbehaving app

If nothing above fully fixed it, isolate the software culprit.

1. Press **Win+R**, type `msconfig`, go to the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
2. Open Task Manager's **Startup apps** tab and disable everything non-Microsoft.
3. Restart, then sleep and wake the laptop — if it's fast now, a third-party app was the problem.
4. Re-enable services and startup apps in small groups (half at a time), testing sleep/wake after each group, until the slowness returns.
5. Once identified, update, reconfigure, or replace the offending app — common offenders are VPN clients, RGB control software, and aggressive antivirus suites. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the clean-boot procedure in full detail.

## Closing

Post-sleep slowness is a resume problem, not a performance problem — the hardware is fine once awake. Updated drivers, hybrid sleep off, wake timers tamed, and USB power saving disabled resolve it for most machines. Work the fixes in order, testing each sleep/wake cycle, and the instant-on feel returns.
