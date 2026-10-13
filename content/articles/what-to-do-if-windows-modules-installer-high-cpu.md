---
title: "Windows Modules Installer High CPU? What to Do While TiWorker Runs"
slug: what-to-do-if-windows-modules-installer-high-cpu
date: 2026-10-07
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "high cpu", "windows update", "trustedinstaller"]
description: "Windows Modules Installer (TiWorker.exe) pinning your CPU? Understand what it's doing and when to wait, when to intervene, and when to worry."
thumbnail: "/images/thumbs/what-to-do-if-windows-modules-installer-high-cpu.webp"
faqs:
  - q: "What is Windows Modules Installer Worker?"
    a: "Windows Modules Installer Worker (TiWorker.exe) is the engine behind Windows Update and optional-feature installation. When Windows downloads updates, installs features on demand, or runs post-update cleanup, TiWorker.exe does the heavy lifting — expanding packages, registering components, and updating the component store. High CPU from it usually means update work is actively happening."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "After a feature update, 30–90 minutes of heavy TiWorker activity is normal, especially on older laptops with spinning hard drives or modest CPUs. On a modern SSD laptop, routine monthly updates should settle within 15–30 minutes. If it's been hammering the CPU for several hours across multiple days with no update in progress, something is stuck and needs attention."
  - q: "Can I end TiWorker.exe in Task Manager?"
    a: "You can end it, but Windows will restart it — and interrupting an update mid-install risks component-store corruption, which is worse than the CPU usage. Ending the task is only sensible as a diagnostic: if CPU instantly returns and stays normal, the worker was genuinely stuck rather than working. Never end it while an update shows as installing in Settings."
  - q: "Is Windows Modules Installer Worker a virus?"
    a: "The legitimate TiWorker.exe lives in C:\\Windows\\WinSxS and C:\\Windows\\System32 and is signed by Microsoft. Malware occasionally impersonates it. Verify via Task Manager > Details > right-click > Open file location — if it opens anywhere other than a Windows system folder, run a full Microsoft Defender scan immediately."
---

Few things are more maddening than a laptop that idles at 60% CPU with the fan screaming — and the culprit is a process called `Windows Modules Installer Worker`, also known as TiWorker.exe. It looks like bloatware, it feels like a bug, and the internet is full of people telling you to disable Windows Update to kill it. Slow down: this process is Windows doing legitimate, important work. The trick is knowing when to let it finish, when to help it along, and when it's genuinely stuck.

TiWorker.exe handles installing, modifying, and removing Windows system components — monthly cumulative updates, .NET updates, features on demand, and the cleanup afterward. On a healthy system it works hard in bursts and then goes quiet. If your laptop never gets that quiet part, this guide walks through diagnosis and repair. Related update-engine issues are covered in our [TiWorker high CPU fix](/articles/best-way-to-fix-windows-modules-installer-high-cpu/) and [Windows Modules Installer deep-dive](/articles/best-way-to-fix-tiworker-exe-high-cpu-windows-update/).

## Why this happens

- **A Windows update is actively installing**: The most common cause — TiWorker is expanding and registering update packages right now.
- **Post-update component cleanup running**: After updates, Windows runs cleanup and optimization passes that keep TiWorker busy.
- **Corrupt Windows Update cache**: Damaged downloads in the SoftwareDistribution folder make the worker retry in a loop.
- **Stuck or failed update**: An update that fails repeatedly re-triggers the installer on every boot.
- **Corrupt component store (WinSxS)**: Damage in the component store forces TiWorker into expensive repair/retry cycles.
- **Features on Demand installing silently**: Language packs, .NET versions, or optional features installing in the background.
- **Third-party "update blockers" interfering**: Tools that aggressively block Windows Update can leave the update engine in a half-started state that TiWorker keeps retrying.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether an update is actually running

The first question is always: is it working, or is it stuck?

1. Open **Settings** > **Windows Update** — if it shows "Downloading" or "Installing" with a percentage, TiWorker is doing its job. Let it finish; plug in the laptop and walk away.
2. Click **Update history** and look for failed updates (red error codes like 0x80070002). Repeated failures on the same KB number mean a stuck update, not normal work.
3. Open Task Manager > **Details** > right-click **TiWorker.exe** > **Open file location** to verify legitimacy, then check the **Disk** column too — heavy disk + CPU together is classic update-installation behavior.
4. Note the duration: under an hour after Patch Tuesday (second Tuesday of the month) is expected. Multiple days of constant activity is not.
5. If Windows Update shows "You're up to date" yet TiWorker still burns CPU for hours, proceed to Fix 2 — something is looping.

### Fix 2: Run the Windows Update troubleshooter

Microsoft's automated tool fixes the common stuck-update states.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. Let it complete and apply any recommended repairs — it commonly resets the update service states and clears stale pending flags.
3. Restart the PC after the troubleshooter finishes, even if it says no problems were found — the service restart alone unsticks many workers.
4. After reboot, open **Settings** > **Windows Update** > **Check for updates** and let any pending update install cleanly while plugged in.
5. Monitor Task Manager for 30 minutes post-update — TiWorker should taper off. If it immediately ramps back to high CPU with no update showing, the cache is likely corrupt (Fix 3).

### Fix 3: Clear the Windows Update cache

Damaged downloads are the number one cause of looping TiWorker.

1. Open **Services** (`services.msc`) and stop the **Windows Update** service (right-click > **Stop**). Also stop **Background Intelligent Transfer Service**.
2. Open File Explorer and navigate to `C:\Windows\SoftwareDistribution` — rename the **Download** folder to `Download.old` (this preserves it as a backup while forcing fresh downloads).
3. Restart the **Windows Update** and **BITS** services.
4. Go to **Settings** > **Windows Update** > **Check for updates** — Windows will re-download what it needs with clean files.
5. Delete the `Download.old` folder after a week of stable updates. See Microsoft's official [Windows support hub](https://support.microsoft.com/en-us/windows) for additional update troubleshooting steps.

### Fix 4: Repair the component store with DISM

When WinSxS itself is damaged, TiWorker thrashes trying to work around it.

1. Open **Terminal (Admin)** or **Command Prompt as Administrator**.
2. Run `DISM /Online /Cleanup-Image /ScanHealth` to check for component store corruption — this is read-only and safe.
3. If corruption is found, run `DISM /Online /Cleanup-Image /RestoreHealth`. This downloads clean component files from Windows Update and can take 15–30 minutes — TiWorker-like CPU during this is the repair working, not the problem.
4. Follow with `sfc /scannow` to verify system file integrity.
5. Restart, then check Windows Update for the previously failing KB — with a healthy component store it usually installs on the first try, and TiWorker goes quiet.

### Fix 5: Identify and remove the stuck update

One bad update can poison the whole queue.

1. In **Settings** > **Windows Update** > **Update history**, find the update with a failed status and note its KB number.
2. Download that specific KB manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — search the KB number, download the version matching your system (x64 for most laptops), and install it directly.
3. Manual installation bypasses whatever was failing in the automated pipeline (often a BITS or service-state issue).
4. If the manual install also fails, use **Show or hide updates** troubleshooter (`wushowhide.diagcab` from Microsoft) to hide the problematic update so TiWorker stops retrying it.
5. Report persistent failures via **Feedback Hub** — Microsoft does fix bad updates, and hiding is a stopgap, not a strategy.

### Fix 6: Tame update timing so TiWorker works when you're idle

You can't (and shouldn't) disable updates — but you can schedule the pain.

1. Open **Settings** > **Windows Update** > **Advanced options** > set **Active hours** to cover your real usage — Windows avoids restarting and heavy install work during these hours.
2. In **Advanced options** > **Optional updates**, install pending driver updates deliberately rather than letting them ambush you — driver updates are a frequent TiWorker trigger.
3. Metered-connection trick (use sparingly): setting your Wi-Fi as metered pauses automatic downloads, letting you choose when the TiWorker storm happens. Don't leave it metered forever or you'll miss security updates.
4. Keep the laptop plugged in and awake overnight once a month after Patch Tuesday — giving TiWorker an uninterrupted window prevents the multi-day dribble of partial work.
5. Check **Delivery Optimization** settings — turn off "allow downloads from other PCs" if TiWorker-adjacent processes (DoSvc) are also consuming resources.

### Fix 7: In-place repair when the update engine is deeply broken

For TiWorker that survives every fix above.

1. Confirm the depth of the problem: `DISM /Online /Cleanup-Image /ScanHealth` still reports unfixable corruption, or the same update fails after cache clears and manual installs.
2. Download the Windows 11 ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, and run `setup.exe`.
3. Choose **Keep personal files and apps** — this reinstalls Windows over itself, rebuilding the component store and update engine cleanly.
4. The process takes 30–60 minutes and several restarts; TiWorker will be busy during it (that's the fix working).
5. Afterward, run Windows Update once fully — the update engine should now complete work in normal timeframes and go quiet. For general update-related slowness, also see our [slow shutdown troubleshooting](/articles/best-way-to-fix-windows-11-slow-shutdown/).

## Closing

Windows Modules Installer Worker high CPU is Windows doing its job in the vast majority of cases — the fix is giving it a clean shot (clear cache, repair the store, install the stuck update) rather than fighting it. A TiWorker that finishes its work and goes quiet is a healthy system; one that never stops is telling you the update pipeline needs repair, and now you know exactly where to look.
