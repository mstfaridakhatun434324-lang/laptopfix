---
title: "Windows Modules Installer High CPU: Complete Troubleshooting"
slug: windows-modules-installer-high-cpu-troubleshooting
date: 2026-09-20
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "high cpu", "troubleshooting", "windows update"]
description: "TiWorker.exe stuck at high CPU? Complete troubleshooting for Windows Modules Installer Worker — from diagnosis to deep repair."
thumbnail: "/images/thumbs/windows-modules-installer-high-cpu-troubleshooting.webp"
faqs:
  - q: "What exactly does Windows Modules Installer Worker do?"
    a: "TiWorker.exe is the execution arm of Windows servicing: it installs Windows updates, enables/disables optional features (.NET Framework, Hyper-V, language packs), and maintains the component store (WinSxS). It runs under the TrustedInstaller service. High CPU is normal while it's actively doing these jobs — each involves extracting, verifying, and registering thousands of system files. Abnormal is when it runs at high CPU for many hours with no progress, or returns to high CPU on every boot indefinitely."
  - q: "How do I know if TiWorker.exe is stuck versus just working?"
    a: "Check Settings > Windows Update for progress: if updates show percentages climbing, it's working. Time-box it: legitimate post-update servicing takes 30 minutes to 2 hours on an SSD. Check Task Manager's disk activity alongside CPU — working servicing shows heavy disk I/O; a stuck process often shows CPU with little disk activity. And check Update history for failed updates that keep reappearing — that's the hallmark of the stuck loop."
  - q: "Can I safely stop the Windows Modules Installer service?"
    a: "Temporarily, for diagnosis — stopping the TrustedInstaller/Windows Modules Installer service halts servicing, which confirms whether TiWorker.exe was the CPU consumer. But leaving it disabled breaks Windows Update permanently and degrades over time as the component store goes unmaintained. Use it as a 10-minute diagnostic, then re-enable and fix the underlying stuck update instead."
  - q: "Why does TiWorker.exe spike after every Patch Tuesday?"
    a: "Patch Tuesday (the second Tuesday of each month) delivers the month's cumulative update, which TiWorker.exe must install — that's its busiest regular day. The spike should subside within a couple of hours of the update installing. If it doesn't subside by the next day, that month's update likely hit a problem on your system, and the troubleshooting steps below apply."
---

`TiWorker.exe` — Windows Modules Installer Worker — is the process that does Windows' heavy lifting: installing updates, managing optional features, maintaining the component store. When it's working, your CPU spikes for a while and then peace returns. When it's broken, the spike never ends, and your laptop becomes a space heater that occasionally runs programs.

This is the complete troubleshooting reference for TiWorker.exe high CPU: structured as a diagnostic flowchart you can follow top to bottom. Each section either resolves the issue or routes you to the next deeper layer. By the end, you'll have either fixed it or identified exactly which deep repair is needed.

For the focused best-practice fix sequence, see [the best way to fix Windows Modules Installer high CPU](/articles/best-way-to-fix-windows-modules-installer-high-cpu/). For the post-update sluggishness angle, [Windows 11 slow after update](/articles/windows-11-slow-after-update-how-to-fix/) is the companion read.

## Why this happens

- **Legitimate update installation in progress**: The normal case — servicing doing real work.
- **Failed update in a retry loop**: A KB that fails and retries on every boot, forever.
- **Corrupt component store**: Damaged WinSxS making every servicing operation slow and failure-prone.
- **Corrupt update download cache**: Damaged SoftwareDistribution causing repeated failed installs.
- **Pending feature update**: Major version upgrades run TiWorker.exe for hours.
- **Insufficient disk space**: Servicing starved of working room, crawling and failing.
- **Third-party interference**: "Optimizer" tools or AV products damaging the servicing pipeline.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Triage — working, stuck, or looping?

Classify your case in five minutes.

1. Open **Settings** > **Windows Update**: note the exact status. "Downloading/Installing X%" = working. "You're up to date" + TiWorker.exe at high CPU = stuck/looping. Error messages = failed update case.
2. Open **Update history** — look for failed updates, especially ones appearing multiple times. A repeating failed KB is the classic loop signature.
3. In Task Manager, correlate CPU with disk: high CPU + high disk = working; high CPU + idle disk for 30+ minutes = stuck.
4. Note the duration: under 2 hours since it started = probably working, give it time. Over 4 hours or recurring across reboots = broken, continue troubleshooting.
5. Your classification routes you: **working** → Fix 2; **stuck/looping** → Fix 3+; **failed update** → Fix 4.

### Fix 2: The patience protocol (for the "working" case)

Let legitimate servicing finish efficiently.

1. Plug in the laptop and set **Best performance** power mode — servicing is throttled on battery and power-saver modes.
2. Close your applications — every open app competes for the CPU and disk that servicing needs.
3. Ensure 15GB+ free on C: — servicing needs scratch space; a full drive turns a 40-minute job into a multi-hour crawl.
4. Leave it alone for 60–90 minutes — check progress periodically but don't reboot. Reboots during servicing force phase restarts.
5. Verify completion: Windows Update shows "You're up to date," Update history shows success, and TiWorker.exe drops to zero. If it doesn't complete, reclassify as stuck and continue.

### Fix 3: Run the automated troubleshooters

Let Windows attempt the standard repairs.

1. **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run** — apply everything it recommends, then restart.
2. Check Windows Update again and click **Check for updates** — the troubleshooter often unblocks the queue, producing one final legitimate TiWorker.exe burst followed by calm.
3. If the troubleshooter reports unfixable problems, note the details — they point to which manual repair (Fix 4–6) you need.
4. Also run the **Background Intelligent Transfer Service** check implicitly covered by the troubleshooter — BITS problems starve the download side of servicing.
5. Re-measure TiWorker.exe 30 minutes after the restart — improvement here means you're on the right track; no change means go deeper.

### Fix 4: Reset the update cache (SoftwareDistribution)

Clear the corrupted download pipeline.

1. Open **Terminal (Admin)** and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver` — wait for each to confirm.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. Go to **Windows Update** > **Check for updates** — Windows rebuilds clean caches and re-downloads pending updates from scratch.
5. Monitor TiWorker.exe through one full update cycle — clean caches usually mean one clean pass instead of endless retries. Delete the `.old` folders after a week of stability.

### Fix 5: Repair the component store (DISM/SFC)

Fix the servicing engine itself.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 10–20 minutes; it fetches clean component copies from Windows Update.
2. Follow with `sfc /scannow` — repairs protected files from the now-healthy store.
3. Restart and observe — this is the fix that permanently resolves most recurring TiWorker.exe loops, because it repairs the corruption that kept servicing retrying.
4. If DISM errors on its source, supply installation media: mount the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) and run DISM with `/Source` pointing at the mounted `install.wim`.
5. Verify with a second `sfc /scannow` showing no integrity violations — then run Windows Update to confirm servicing completes cleanly.

### Fix 6: Surgically remove the failing update

When one specific KB is the loop source.

1. Identify it: **Update history** shows the repeatedly failing KB number (e.g., KB50XXXXX).
2. Try hiding it: download Microsoft's **Show or Hide Updates** troubleshooter (`wushowhide.diagcab`) — hide the problematic update so Windows stops retrying it.
3. Or install it manually: search the KB on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), download the standalone `.msu`, and install it — manual installs bypass whatever was failing in the automatic path.
4. Check Microsoft's official [Windows support page](https://support.microsoft.com/en-us/windows) for known issues with that KB — some updates have documented conflicts with specific hardware or software, with workarounds.
5. After handling the KB, unhide it after the next Patch Tuesday — the superseding update usually installs cleanly where its predecessor failed.

### Fix 7: Deep repair — in-place upgrade

Rebuild the servicing stack when nothing else works.

1. Back up your important files (the process keeps them, but backups are non-negotiable before deep repairs).
2. Download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, and run **setup.exe**.
3. Choose **Keep personal files and apps** — this reinstalls Windows over itself, rebuilding the entire servicing stack, component store, and update pipeline.
4. The process takes 30–90 minutes with several restarts — TiWorker.exe will be busy during it (legitimately), then settle.
5. After completion, run Windows Update fully — a rebuilt servicing stack should process updates cleanly. If TiWorker.exe loops even after this, suspect hardware: check drive health (`wmic diskdrive get status`) and RAM (`mdsched.exe`), since failing hardware corrupts servicing data.

## Closing

TiWorker.exe troubleshooting is triage followed by escalating repair: confirm whether it's working or stuck, give legitimate work a fair window, reset the update cache, repair the component store, surgically handle the failing KB, and rebuild the stack only if everything else fails. Follow the sequence and the loop breaks — servicing goes back to being something that happens quietly in the background, a few hours a month, exactly as designed.
