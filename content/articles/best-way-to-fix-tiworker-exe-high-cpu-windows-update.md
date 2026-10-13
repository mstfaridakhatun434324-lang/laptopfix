---
title: "TiWorker.exe High CPU? The Best Way to Calm It Down Fast"
slug: best-way-to-fix-tiworker-exe-high-cpu-windows-update
date: 2026-10-06
categories: ["windows-update"]
tags: ["tiworker.exe", "high cpu", "windows update", "windows modules installer worker"]
description: "The best way to fix TiWorker.exe high CPU during Windows Update: let it finish safely, repair the component store, and stop the endless update loop."
thumbnail: "/images/thumbs/best-way-to-fix-tiworker-exe-high-cpu-windows-update.webp"
faqs:
  - q: "What is TiWorker.exe and is it a virus?"
    a: "TiWorker.exe is the Windows Modules Installer Worker, a legitimate Microsoft process that installs updates and optional features. It is not a virus. If it runs hot after an update, it is doing real work — but if it never stops, something in the update pipeline is stuck."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "After a feature update, thirty minutes to a few hours is normal, especially on laptops with spinning hard drives or modest CPUs. If it is still pinning a core after six to eight hours of idle time, treat it as stuck and work through the repair steps."
  - q: "Can I just end TiWorker.exe in Task Manager?"
    a: "You can, and it will stop the CPU spike immediately, but the underlying update job resumes later and the problem returns. Ending the task is a pause button, not a fix. Repair the component store or reset update components for a lasting result."
  - q: "Will disabling Windows Update stop TiWorker.exe forever?"
    a: "Pausing updates stops TiWorker temporarily, but it leaves your laptop unpatched against new threats and the process returns the moment updates resume. The better path is fixing whatever is making the installer worker loop, which keeps both your CPU quiet and your security intact over the long run."
---

TiWorker.exe — the Windows Modules Installer Worker — is supposed to work hard. It installs updates, enables optional features, and repairs the component store. The problem starts when it never stops: fans screaming, battery draining, and one CPU core pinned at 100% for hours after an update that should have finished long ago.

The best way to fix it is not to kill the process and hope. It is a short, ordered routine: confirm what it is doing, give legitimate work a chance to finish, then repair the update pipeline that is keeping it stuck. Follow this sequence and you will know exactly which case you have.

## Why this happens

- **Post-update component cleanup:** After a cumulative or feature update, TiWorker compresses superseded components and cleans the WinSxS store. On slower laptops this legitimately takes hours.
- **A stuck update loop:** A failed update keeps retrying its install phase, and TiWorker restarts the same doomed job every time.
- **Corrupted component store:** Damaged files in WinSxS force the installer worker to repeatedly attempt repairs that never complete.
- **Conflicting third-party software:** Antivirus filters and "optimizer" tools can block the files TiWorker needs, so it retries endlessly.
- **Pending reboot jobs:** Updates waiting on a restart keep TiWorker active across sessions until the reboot actually happens.
- **Low disk space:** With little free space, cleanup operations crawl and the worker spins far longer than it should.
- **Failing storage:** A dying SSD or HDD makes every file operation slow, stretching normal installer work into an all-day event. Persistent slowness pairs with the [stuck update downloads](/articles/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2/) many users see alongside it.
- **Paused-then-resumed update states:** Interrupting updates mid-install leaves the component store in a half-applied state that TiWorker keeps trying to resolve.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what it is doing, then give it a fair window

1. Open **Task Manager → Details**, find TiWorker.exe, and note its CPU and disk activity.
2. Open **Settings → Windows Update** and check whether an update is actively installing or pending a restart.
3. If an update is genuinely in progress, plug in the charger, close your apps, and give it **up to two hours** of idle time.
4. If nothing is installing and TiWorker has run hot for over **six hours**, move on — it is stuck, not busy.

### Fix 2: Restart and clear the pending reboot queue

1. Save your work and do a full **Restart** (not shutdown with fast startup) from the Start menu.
2. After rebooting, check **Settings → Windows Update** and install anything pending, rebooting again if asked.
3. Many TiWorker marathons end here: the worker was waiting on a reboot that fast startup kept deferring.
4. If the spike returns within an hour of a clean boot with no pending updates, continue.

### Fix 3: Repair the component store with DISM

1. Open **Terminal (Admin)** or an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and let it complete — this can take 15–30 minutes.
3. Follow with `sfc /scannow` to repair protected system files.
4. Reboot and watch TiWorker for an hour. A repaired component store removes the most common reason the installer worker loops forever. Microsoft documents these repair tools on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Reset the Windows Update components

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart all four services with the matching `net start` commands.
4. Check for updates again. Fresh caches give TiWorker a clean job queue instead of the corrupted one it was choking on.

### Fix 5: Run the Windows Update troubleshooter

1. Go to **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply every fix it suggests.
3. Reboot when it asks, then check for updates manually.
4. The troubleshooter catches misconfigured services and permissions that manual steps miss, and it is safe to run repeatedly.

### Fix 6: Update chipset and storage drivers

1. Identify your platform and grab fresh chipset drivers — [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects and installs the right ones automatically.
2. Update your storage/NVMe driver from the laptop maker's support page as well.
3. Reboot and observe. Slow or buggy storage drivers make TiWorker's file-heavy work take far longer than it should, mimicking a stuck process. On Dell machines the same workload is covered in our [Dell-focused TiWorker guide](/articles/how-to-fix-tiworker-exe-high-cpu-windows-update-on-dell-laptop/).

### Fix 7: Rule out third-party interference with a clean boot

1. Press **Win + R**, type `msconfig`, and on the **Services** tab check **Hide all Microsoft services**, then **Disable all**.
2. In **Task Manager → Startup apps**, disable everything, then reboot.
3. If TiWorker behaves in a clean boot, re-enable services in halves until the culprit returns — usually an antivirus filter or system "tweaker."
4. Remove or replace the offending program rather than living in a permanent clean boot.

### Fix 8: Set active hours and use a metered connection strategy

1. Open **Settings → Windows Update → Advanced options** and set **Active hours** to cover your workday so installs happen overnight.
2. On a metered Wi-Fi connection, Windows defers most updates; use this on travel networks to keep TiWorker from firing at bad times.
3. Schedule a weekly plugged-in idle window — for example Sunday night — and let pending updates install then.
4. Controlling *when* the installer worker runs turns a disruptive CPU spike into background maintenance you never notice.

## Closing

TiWorker.exe at high CPU is usually either honest post-update work or a stuck installer loop, and the sequence above tells you which within a day. Give real work time to finish, repair the component store with DISM, reset the update caches, and update your chipset drivers. Do that, and the fans go quiet for the right reason: the job is actually done.
