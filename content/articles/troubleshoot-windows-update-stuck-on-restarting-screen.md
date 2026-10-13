---
title: "Troubleshoot a Windows Update That Freezes on the Restarting Screen"
slug: troubleshoot-windows-update-stuck-on-restarting-screen
date: 2026-10-13
categories: ["windows-update"]
tags: ["restarting screen freeze", "windows update", "diagnostics", "safe mode", "windows 11"]
description: "A systematic troubleshooting workflow for Windows Update freezing on the restarting screen — isolate the phase, test the drivers, and repair the servicing stack."
thumbnail: "/images/thumbs/troubleshoot-windows-update-stuck-on-restarting-screen.webp"
faqs:
  - q: "What is the difference between a slow restart and a stuck one?"
    a: "A slow restart still shows disk activity and eventually progresses, sometimes taking up to an hour on older drives. A stuck restart shows zero activity — no blinking drive light, no fan changes, frozen dots — for an extended period, usually beyond 45 to 60 minutes. When in doubt, watch the drive activity light — it is the most honest indicator of whether the servicing engine is still working."
  - q: "Can Safe Mode help diagnose a restarting-screen freeze?"
    a: "Yes. If the laptop boots into Safe Mode but a normal restart with updates pending freezes, the cause is almost certainly a third-party driver or startup service. Clean-boot testing then isolates the exact culprit. Safe Mode loads only Microsoft drivers, so a clean boot there strongly implicates third-party software rather than Windows itself."
  - q: "Will System Restore remove my personal files?"
    a: "No. System Restore rolls back system files, drivers, and registry settings to the restore point but leaves documents, photos, and other personal files untouched. Installed programs added after the point may need reinstalling. That safety is what makes System Restore the ideal first recovery attempt — it can only help the system, never harm your data."
  - q: "How do I prevent this from happening with future updates?"
    a: "Keep drivers current from the vendor, maintain at least 20 gigabytes of free space, disable Fast Startup if you have a history of stalls, and install cumulative updates promptly rather than letting many pile up at once. Machines that install updates monthly almost never develop the tangled servicing states that cause these freezes."
---

Troubleshooting a Windows Update that freezes on the restarting screen is detective work: the symptom is identical every time — spinning dots that never end — but the cause hides in one of several layers. A driver that will not unload. A servicing transaction that cannot commit. A disk that cannot write. Guessing wastes hours, so this guide gives you a diagnostic workflow that isolates the layer first, then applies the targeted fix. Follow it in order and you will stop throwing random solutions at the problem.

## Why this happens

- **Third-party driver refusing to unload:** The shutdown phase asks every driver to release; one stubborn driver — often audio, network, or storage filter drivers — blocks the whole sequence.
- **Servicing stack transaction failure:** The update engine writes changes as a transaction; if it cannot commit, the restart phase retries instead of failing cleanly.
- **Startup service deadlock:** A third-party service that starts with Windows can deadlock against the update installer during the reboot handoff.
- **Corrupted pending.xml:** The file that queues servicing operations can become malformed, leaving the boot loader unsure what the update was supposed to do.
- **Hybrid shutdown state pollution:** Fast Startup's hibernation file can preserve a broken driver state across the "restart," replaying the freeze every time.
- **Failing storage:** Intermittent write failures during the file-replacement phase produce freezes that look like software problems but are hardware.
- **Overfull system drive:** With almost no free space, the servicing engine cannot stage its rollback data and stalls instead of aborting gracefully.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine which layer is stuck

1. On the frozen screen, check for drive activity (light or sound) and whether the dots animate or are frozen solid.
2. Animating dots with disk activity means the servicing engine is still working — wait up to an hour before intervening.
3. Frozen dots with zero activity for 45+ minutes means a hard stall; note the time, because Event Viewer will later show what was happening at that minute.
4. This observation decides everything downstream: patience for a working engine, forced shutdown for a dead one.

### Fix 2: Force shutdown and boot into Safe Mode for diagnosis

1. Hold the power button 10 seconds to force off, then power on while tapping **F8** or interrupting boot three times to reach Recovery, then **Troubleshoot > Advanced options > Startup Settings > Safe Mode**.
2. If Safe Mode boots fine, the core OS is healthy — the freeze is a driver or service problem, not system corruption.
3. In Safe Mode, open **Event Viewer > Windows Logs > System** and look at the minutes before the freeze for driver or service errors.
4. Safe Mode also lets you run the deeper repairs below without the update engine fighting you.

### Fix 3: Perform a clean boot to isolate the culprit

1. Press **Win + R**, type `msconfig`, and on the **Services** tab tick **Hide all Microsoft services**, then **Disable all**.
2. On the **Startup** tab (or Task Manager > Startup apps), disable all third-party startup items.
3. Restart normally with updates pending. If the restart completes, re-enable services in halves until the freeze returns — the last half contains the culprit.
4. Audio enhancement suites, VPN clients, and RGB control software are the most common offenders found this way.

### Fix 4: Repair the servicing transaction files

1. In an elevated Command Prompt, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
2. If DISM reports it cannot complete, run it with an explicit source: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:C:\Sources\install.wim:1` (adjust the path to your recovery media).
3. Check `C:\Windows\WinSxS\pending.xml` — if it is dated from the failed update and enormous, the servicing queue is jammed; the DISM repair usually clears it.
4. Detailed servicing-stack repair steps are in Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) if the corruption resists these commands.

### Fix 5: Clear hybrid shutdown state and disable Fast Startup

1. In an elevated Command Prompt, run `powercfg /h off` to delete the hibernation file that preserves broken driver states.
2. Then go to **Control Panel > Power Options > Choose what the power buttons do** and uncheck **Turn on fast startup**.
3. Run `powercfg /h on` afterward only if you want hibernation back; leave Fast Startup off on machines with restart-freeze history.
4. Test with a plain restart (no update) to confirm the shutdown path is clean before the next update attempt.

### Fix 6: Test the storage hardware

1. Run `chkdsk C: /f /r` from an elevated prompt and let it complete at reboot.
2. Check SMART data with the drive maker's tool or `wmic diskdrive get status` — anything other than "OK" means replace the drive.
3. Free up space to at least 20 GB on C: — the servicing engine needs room for staging and rollback data.
4. If the disk is healthy and spacious, you have ruled out hardware; the problem is software, and the next fix targets the update pipeline itself. If later updates leave you with a [black screen instead](/articles/black-screen-after-windows-update-troubleshooting/), that guide continues the diagnosis.

### Fix 7: Reset update components and reinstall cleanly

1. Stop the update services (`net stop wuauserv`, `net stop bits`, `net stop cryptSvc`) and rename the SoftwareDistribution and Catroot2 folders.
2. Restart the services and install the pending update from a fresh download.
3. For stubborn cumulative updates, download the standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and install it manually — this bypasses the cached delivery pipeline entirely.
4. After a successful install, re-enable your startup items one group at a time and watch the next restart closely. For the driver side of the diagnosis, our [driver-update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) pairs well with this workflow.

## Closing

The restarting-screen freeze is a symptom, not a diagnosis — and this workflow turns it into one. Observe the freeze, boot to Safe Mode, clean-boot to isolate, repair servicing, clear hybrid state, test storage, reset components. Each step rules out a layer. Work it methodically once and you will not only unstick this update but know exactly which layer to watch when the next one arrives.
