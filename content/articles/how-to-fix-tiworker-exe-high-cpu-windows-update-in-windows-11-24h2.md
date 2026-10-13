---
title: "TiWorker.exe High CPU After Windows Update on 24H2 (How to Calm It)"
slug: how-to-fix-tiworker-exe-high-cpu-windows-update-in-windows-11-24h2
date: 2026-09-19
categories: ["windows-update"]
tags:
  - tiworker.exe
  - high cpu
  - windows update
  - windows 11 24h2
  - performance
description: "TiWorker.exe eating 50-100% CPU after a Windows 11 24H2 update? Learn what it does, when to leave it alone, and how to fix it when it never stops."
thumbnail: "/images/thumbs/how-to-fix-tiworker-exe-high-cpu-windows-update-in-windows-11-24h2.webp"
faqs:
  - q: "Is TiWorker.exe a virus?"
    a: >
      No. TiWorker.exe (Windows Modules Installer Worker) is a legitimate Microsoft process that installs Windows updates, optional features, and system components. It lives in the System32 folder and is digitally signed by Microsoft. Malware sometimes uses similar names, so verify the file location is C:\\Windows\\System32 — anything running from another folder under that name should be scanned immediately.
  - q: "How long should TiWorker.exe use high CPU after an update?"
    a: >
      Up to one to two hours of elevated CPU on the first idle period after a large update is normal, especially on older laptops. It should taper off on its own. If CPU stays pegged above 30 percent across multiple days and reboots with no new updates installing, it is stuck and needs the repair steps in this guide rather than more waiting.
  - q: "Can I just disable TiWorker.exe or Windows Update to stop the CPU usage?"
    a: >
      You should not. Disabling the Windows Modules Installer or update services breaks future updates and leaves security holes, and TiWorker will often return anyway. The correct fix is to repair whatever it is choking on — usually the update cache or component store — so it finishes its work and goes quiet by itself.
  - q: "Why does TiWorker.exe spike every time I leave my laptop idle?"
    a: >
      Idle time is when Windows schedules maintenance: update finalization, component cleanup, and Defender scans. Spikes during idle are by design. If the spikes are extreme or never end, run the DISM repair and clear the update cache as described above, and check that your power plan is not aggressively parking CPU cores, which makes normal maintenance look worse.
---

After a Windows 11 24H2 update, many laptop owners open Task Manager and find TiWorker.exe — the Windows Modules Installer Worker — sitting at 40, 60, or even 100 percent CPU, with fans screaming and the battery draining. The instinct is to kill it. Do not. TiWorker is the process that actually installs updates and cleans up afterward, and killing it mid-job is how you get corrupted updates.

The real question is whether TiWorker is doing legitimate work or stuck in a loop. Legitimate work finishes: after a big update, an hour or two of high CPU while it finalizes components is normal, especially on first boot. A loop never finishes — the same CPU load persists across days and reboots, and that is what this guide fixes.

Below you will learn how to tell the difference, the cases where waiting is the correct action, and the repair sequence for a genuinely wedged TiWorker.

## Why this happens

- **Post-update component finalization:** after 24H2 installs, TiWorker reconciles the component store, a CPU-heavy job that is completely legitimate and finishes on its own within an hour or two.
- **A corrupted component store:** if the WinSxS store has damaged entries, TiWorker retries the same reconciliation endlessly, burning CPU without ever completing.
- **Stuck or looping Windows Update downloads:** when the update engine cannot finish a download or install, TiWorker keeps spinning as the servicing stack retries in the background.
- **Corrupted system files the worker keeps hitting:** damaged manifests or payload files make TiWorker fail and retry the same operation thousands of times.
- **Third-party drivers conflicting with servicing:** badly behaved filter drivers can cause the component installer to error and restart its pass repeatedly.
- **Pending operations from an interrupted update:** a shutdown during install leaves half-applied operations that TiWorker tries to complete on every boot, failing each time.
- **Windows Update services in a bad state:** if wuauserv or the trusted installer service is wedged, TiWorker inherits the confusion and churns without progress.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm TiWorker is the real culprit and let legitimate work finish

Before repairing anything, verify what is actually burning CPU and give genuine post-update work a fair chance to complete. Most TiWorker panics resolve right here.

1. Open Task Manager (Ctrl + Shift + Esc), click Processes, and sort by CPU to confirm TiWorker.exe or Windows Modules Installer Worker is the top consumer.
2. Check the Details tab for sustained high CPU over 10 minutes rather than brief spikes.
3. If the high CPU started within a day of an update, plug in the charger, leave the laptop idle and awake for up to 2 hours, and watch whether CPU drops on its own.
4. If it drops, nothing was broken — move on. If it is still pegged after 2 idle hours, continue.

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter detects stuck update states and resets the exact services TiWorker depends on. It is the fastest safe intervention.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Click Run next to Windows Update and let it complete.
3. Apply any fixes it recommends, then reboot.
4. Check Task Manager after 15 minutes to see whether TiWorker has calmed down.

### Fix 3: Clear the SoftwareDistribution and catroot2 caches

When TiWorker is choking on a corrupted download, wiping the update cache removes the poisoned files it keeps retrying. Your installed updates are untouched.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv and net stop bits and net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the three services with net start, reboot, and check CPU after 20 minutes.

### Fix 4: Repair the component store with DISM

TiWorker lives and dies by the component store. DISM scans WinSxS for corruption and repairs it from Windows Update, which directly fixes the retry loops.

1. Open Command Prompt as administrator.
2. Run: DISM /Online /Cleanup-Image /ScanHealth to assess damage.
3. Run: DISM /Online /Cleanup-Image /RestoreHealth and wait — this takes 15 to 30 minutes.
4. Reboot and observe TiWorker for 30 minutes before judging the result.

### Fix 5: Follow up with SFC

DISM repairs the store; SFC then uses the repaired store to fix protected system files. Running both in this order covers the full chain TiWorker depends on.

1. In the same elevated Command Prompt, run: sfc /scannow.
2. Wait for the verification to reach 100 percent.
3. If it reports repaired files, reboot and monitor CPU again.
4. If both tools report no problems yet TiWorker still spins, continue to Fix 6.

### Fix 6: Check for a stuck update in the history and remove it

Sometimes one specific update is the stone in TiWorker's shoe. The update history names it, and removing it lets the worker finish everything else.

1. Go to Settings > Windows Update > Update history and look for failed or repeatedly reinstalling updates.
2. Note the KB number of the suspect update.
3. Go to Installed updates, uninstall that KB, and reboot.
4. Pause updates for a few days, then allow the KB to return — or install it [manually from the catalog](https://www.catalog.update.microsoft.com/) where you control the process.

### Fix 7: Perform a clean boot to rule out third-party interference

If TiWorker only spins when your normal startup programs load, a third-party driver or service is provoking it. A clean boot isolates the offender.

1. Press Win + R, type msconfig, and on the Services tab tick Hide all Microsoft services, then Disable all.
2. On the Startup tab open Task Manager and disable all startup items, then reboot.
3. If TiWorker is calm now, re-enable services in halves until the culprit returns.
4. Update or remove the offending program — if a driver is implicated, grab a fresh copy from the [Intel driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop maker's site.

## Closing

TiWorker.exe high CPU is usually Windows finishing legitimate update work — the fix is patience, a charger, and an idle machine. When it truly never stops, the chain is almost always a corrupted update cache or component store, and the DISM plus cache-clear sequence above resolves it. Do not kill TiWorker or disable the TrustedInstaller service; both just trade a slow afternoon for a broken update system. For a related CPU hog with a different cause, see our guide to [Antimalware Service Executable high CPU on Windows 11](/articles/antimalware-service-executable-high-cpu-windows-11/), and if the whole update cycle drags, read [why Windows Update takes too long](/articles/how-to-fix-windows-update-taking-too-long-after-windows-11-update/).
