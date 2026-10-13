---
title: "Fix Windows Modules Installer (TiWorker.exe) High CPU"
slug: "how-to-fix-windows-modules-installer-high-cpu-youtube"
date: "2026-09-21"
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "high cpu", "windows update", "trustedinstaller"]
description: "TiWorker.exe pinning your CPU at 100%? Understand what Windows Modules Installer does and how to fix it when it gets stuck."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-youtube.webp"
faqs:
  - q: "What is Windows Modules Installer (TiWorker.exe)?"
    a: "It is the worker process behind Windows Update and optional-feature installation — it downloads, verifies, stages, and installs update components, and cleans up afterward. High CPU from TiWorker means Windows is actively working on updates. It is legitimate system work, but when it runs for many hours without progress, the update pipeline is stuck and needs repair."
  - q: "How long should TiWorker.exe run normally?"
    a: "For routine monthly cumulative updates, 15–60 minutes of elevated activity is normal. Feature updates can keep it busy for 1–3 hours. Beyond 4–6 hours with no progress in Settings > Windows Update, or TiWorker running hot on every boot for days, indicates a stuck update that the fixes in this guide address."
  - q: "Can I disable Windows Modules Installer?"
    a: "You should not. Disabling it breaks Windows Update entirely, leaving you without security patches — a far worse problem than temporary CPU usage. The correct approach is fixing the stuck update so TiWorker finishes its job and goes idle, which is what this guide does."
  - q: "Will ending TiWorker.exe in Task Manager help?"
    a: "Temporarily — it restarts automatically because the update orchestrator relaunches it. Force-ending it mid-install risks corrupting the component store, which makes the problem worse. Only end it as a last resort before running the repair steps, never as the fix itself."
---

**TiWorker.exe** — Windows Modules Installer Worker — is the process that does the heavy lifting of Windows Update: downloading packages, verifying signatures, staging files, and committing them to the system. When updates are flowing, TiWorker legitimately uses significant CPU and disk — that is your machine getting patched, and interrupting it is a bad idea. The problem this guide addresses is TiWorker that never finishes: hours at high CPU, day after day, with Windows Update showing no progress or the same update failing repeatedly.

The distinction matters because the fix for "working normally" is patience, while the fix for "stuck" is repair. This guide starts by telling them apart — via the Windows Update status page, which is the ground truth — then walks the standard repair ladder: troubleshooter, update cache reset, component store repair, and manual update installation.

Never "solve" TiWorker CPU by disabling Windows Update or the TrustedInstaller service. An unpatched Windows is a compromised Windows; the goal is a working update pipeline, not a silent one.

## Why this happens

- **Large update in progress:** Cumulative and feature updates legitimately occupy TiWorker for extended periods.
- **Corrupted update cache:** Damaged files in the SoftwareDistribution folder cause download-verify-fail-retry loops.
- **Failing update:** A specific update that errors out gets retried indefinitely by the orchestrator.
- **Damaged component store:** Corruption in WinSxS makes every install operation struggle and retry.
- **Low disk space:** Updates need gigabytes of staging space; without it, installs fail and retry.
- **Conflicting third-party software:** Aggressive antivirus or "optimizer" tools interfering with update file operations.
- **Metered connection confusion:** Updates partially downloading over metered connections, then restarting.
- **Stuck post-reboot phase:** An update awaiting its reboot-phase completion keeps TiWorker active across restarts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Windows Update status before touching anything

Open **Settings > Windows Update** — this page is the ground truth. If it shows downloading/installing with a progressing percentage, TiWorker is working: leave it alone, stay plugged in, and give it time. If it shows an error code, a stuck percentage for hours, or "retry," you have a stuck update and the repairs below apply. Note any error codes (e.g., 0x80070002) — they identify the specific failure. This five-minute check prevents "fixing" a healthy update in progress. The after-update variant of this process is covered in our [TiWorker after-update guide](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/).

1. Open **Settings > Windows Update**.
2. Note the exact status: progressing, stuck, or error (record error codes).
3. If progressing, wait — do not interrupt.
4. Proceed only if stuck for hours or showing errors.

### Fix 2: Run the Windows Update troubleshooter

The built-in troubleshooter automatically detects and fixes the most common update pipeline problems: stuck services, corrupted cache metadata, and misconfigured update components. Run it from **Settings > System > Troubleshoot > Other troubleshooters > Windows Update**, apply everything it suggests, and restart. It resolves a surprising share of TiWorker loops on its own because many are simple service-state issues. After it completes, check Windows Update again — if the stuck update now progresses, let it finish.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run **Windows Update** and apply all suggested fixes.
3. Restart the laptop.
4. Check whether the update now progresses.

### Fix 3: Reset the update cache (SoftwareDistribution)

When the troubleshooter is not enough, the update cache itself is usually corrupted — partially downloaded packages that fail verification and retry forever. The fix: stop the update services, rename the `SoftwareDistribution` and `catroot2` folders (Windows rebuilds them fresh), and restart the services. Your installed updates are untouched; only the pending-download cache is cleared. This is the classic, Microsoft-documented repair for update loops and resolves most persistent TiWorker CPU cases.

1. Open **Command Prompt as administrator**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`; then check for updates.

### Fix 4: Repair the component store with DISM and SFC

If TiWorker struggles even with a fresh cache, the component store (WinSxS) it installs into may be damaged. Run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the store from Windows Update, then `sfc /scannow` to fix protected system files. This takes 15–30 minutes and requires internet for DISM's repair source. After completion, retry Windows Update — installs that previously failed verification often succeed once the store is healthy. Microsoft documents these tools on the official [Windows support hub](https://support.microsoft.com/en-us/windows).

1. In elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`.
3. Restart the laptop.
4. Retry Windows Update and watch TiWorker behavior.

### Fix 5: Free disk space for update staging

Updates need room: feature updates want 20+ GB free, cumulative updates several GB. If C: is cramped, downloads fail partway and retry — a perfect TiWorker CPU loop. Free space with Disk Cleanup (including system files / Windows Update Cleanup), empty the Recycle Bin, and move large personal files off C:. Re-check with at least 20 GB free before judging whether the update problem persists. Space starvation is the most embarrassing cause because the fix is so simple — check it early. Our full cleanup sequence is in the [C: drive space guide](/articles/how-to-fix-low-disk-space-on-c-drive-on-lenovo-laptop/).

1. Check free space on C: (need 20+ GB for feature updates).
2. Run Disk Cleanup with **Clean up system files**.
3. Move large personal files off C:.
4. Retry the update with adequate free space.

### Fix 6: Install the stuck update manually from the Catalog

When Windows Update itself cannot deliver a specific update, bypass it: identify the failing KB number from Update history, download it manually from the official [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), and install the .msu directly. Manual installation sidesteps whatever is broken in the automated pipeline for that package. After it installs and the reboot completes, TiWorker should go idle — the retry loop ends because there is nothing left to retry. Resume normal Windows Update afterward to confirm the pipeline is healthy.

1. Note the failing KB number in **Update history**.
2. Download it from the Microsoft Update Catalog.
3. Run the .msu installer and reboot when prompted.
4. Verify TiWorker is idle and Update shows no errors.

### Fix 7: Pause updates strategically (not permanently)

If you need immediate relief while planning the deeper repair — say, TiWorker is making the laptop unusable during work hours — pause updates for up to 5 weeks from **Settings > Windows Update > Pause updates**. This is a breather, not a fix: security patches matter, so use the pause to schedule the repair work, not to avoid it. Never disable the Windows Update service or set your connection permanently metered to dodge updates; both create bigger problems than TiWorker CPU. For the 24H2-specific TiWorker variant, see our [TiWorker in 24H2 guide](/articles/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2/).

1. **Settings > Windows Update > Pause updates** (max 5 weeks).
2. Schedule the repair fixes above during the pause.
3. Unpause and let updates complete normally.
4. Confirm TiWorker settles after the update cycle.

## Closing

TiWorker.exe high CPU is Windows Update working — or trying to. The discipline is checking the Update status first (patience for real progress, repair for stuck loops), then walking the repair ladder: troubleshooter, cache reset, component store repair, manual install. A healthy update pipeline finishes its work and goes quiet; these steps get you back to that state without ever compromising your security posture.
