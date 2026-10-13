---
title: "How to Check Disk for Errors in Windows 11 24H2"
slug: how-to-check-disk-for-errors-in-windows-11-24h2
date: 2026-10-11
categories: ["performance"]
tags: ["chkdsk", "disk errors", "windows 11 24h2", "s.m.a.r.t."]
description: "How to check your disk for errors on Windows 11 24H2: chkdsk the right way, read S.M.A.R.T. data, and know when errors mean replace the drive."
thumbnail: "/images/thumbs/how-to-check-disk-for-errors-in-windows-11-24h2.webp"
faqs:
  - q: "What does chkdsk actually check?"
    a: "Chkdsk verifies the file system's logical integrity — directory structures, file records, security descriptors, and the journal — and optionally the disk surface itself. The /scan and /f modes fix logical corruption (orphaned files, bad indexes); /r additionally scans every sector for physical damage and recovers readable data. It does not predict failure — that's S.M.A.R.T.'s job — but it does repair the corruption that causes crashes and 'corrupt file' errors."
  - q: "Is it safe to run chkdsk on an SSD?"
    a: "Yes for /f and /scan — they only touch file-system structures, which is identical work on SSDs and HDDs. Be cautious with /r on SSDs: it reads every sector, which is heavy wear-adjacent activity, and SSDs remap bad blocks internally anyway, so /r rarely finds anything the SSD's own controller hasn't handled. For SSD health, S.M.A.R.T. attributes (wear level, spare blocks) are far more informative than a surface scan."
  - q: "How long does chkdsk take?"
    a: "An online /scan takes 5-15 minutes with no reboot. An offline /f on the system drive needs a reboot and takes 15 minutes to an hour depending on file count. A full /r surface scan takes hours — roughly 1-2 hours per TB on HDDs. If chkdsk seems stuck at a percentage for a very long time, it's usually grinding through bad sectors (which is informative in itself); let it finish unless the drive is making alarming noises."
  - q: "Chkdsk found bad sectors — do I need a new drive?"
    a: "A few bad sectors that chkdsk remaps, with S.M.A.R.T. otherwise clean and the count stable over months, is a 'watch closely' situation — back up and monitor. Rapidly growing reallocated-sector counts, pending sectors that never clear, or bad sectors reappearing after chkdsk means the drive is actively failing: replace it now, not after the next backup. Back up first, diagnose second."
---

Disk errors are the quiet saboteurs of Windows performance: a few bad sectors and suddenly apps hang, file copies crawl, and the system stutters for no visible reason. Windows 11 24H2 gives you everything needed to check — `chkdsk` for file-system integrity, S.M.A.R.T. data for the drive's self-reported health, and Event Viewer for the history. The trick is knowing which tool answers which question, and recognizing when "errors found" means "replace the drive." For what to do about the slowness bad sectors cause, see [fixing slow file transfers](/articles/how-to-fix-windows-11-slow-file-transfer-reddit/); for system-file corruption rather than disk corruption, [running SFC](/articles/how-to-run-sfc-scannow-in-windows-11-24h2/) is the companion guide.

## Why this happens

- **Bad sectors on aging drives**: Magnetic media degrades; the drive remaps until spares run out.
- **Improper shutdowns**: Power loss mid-write leaves file-system structures inconsistent.
- **Failing flash cells on SSDs**: Worn NAND cells cause read errors the controller can't always hide.
- **Loose/faulty cables (SATA)**: Intermittent connections corrupt in-flight writes.
- **Overheating drives**: Heat-induced errors on drives with poor airflow.
- **File-system corruption from crashes**: BSODs and hard resets interrupting journaled writes.
- **Dying drive electronics**: Controller issues producing errors across a healthy-looking surface.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the online chkdsk scan (no reboot needed)

The quick, non-disruptive first check.

1. Open **Command Prompt as Administrator** (right-click Start > Terminal (Admin)).
2. Run `chkdsk C: /scan` — this performs an online scan of the system drive while Windows keeps running. No reboot, no downtime.
3. Read the output: "No further action required" = file system is logically clean; errors listed = corruption found (move to Fix 2).
4. For non-system drives you can scan directly: `chkdsk D: /scan`.
5. This checks logical structure only — it won't find physical bad sectors. Treat a clean /scan as "file system OK," not "drive healthy" (that's Fix 3).

### Fix 2: Run the offline repair with /f

Fixes the logical corruption the scan found.

1. In the elevated prompt, run `chkdsk C: /f` — Windows will report the drive is locked and ask to schedule the check at next restart. Press **Y**.
2. Reboot — chkdsk runs before Windows loads, displaying its progress. Don't power off during this.
3. Timing: 15–60 minutes depending on file count. The percentage may appear stuck at times — that's normal while it processes large directories.
4. After booting, check what it did: open **Event Viewer** > **Windows Logs** > **Application**, filter source **Wininit** — the chkdsk result log details exactly what was repaired (orphaned files recovered, bad indexes fixed).
5. If chkdsk reports it **couldn't fix** some errors, or errors return on the next scan, the corruption has a physical cause — proceed to Fixes 3–4.

### Fix 3: Read the drive's S.M.A.R.T. health data

The drive's own self-assessment — the real health answer.

1. In elevated PowerShell, run `Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus` — a quick pass/fail overview.
2. For detail, use **CrystalDiskInfo** (free) — it shows the raw S.M.A.R.T. attributes with color-coded health: watch **Reallocated Sector Count**, **Current Pending Sector Count**, **Uncorrectable Sector Count** (HDD), and **Wear Level / Percentage Used / Available Spare** (SSD).
3. Interpret: zeros across error attributes + "Good" = healthy; small stable reallocated counts = aging but functional (back up, monitor monthly); growing counts or any pending sectors = failing.
4. SSD-specific: check **Percentage Used / Wear Leveling Count** — a drive at 95%+ used is near end-of-life regardless of error counts.
5. Record the numbers with dates — S.M.A.R.T. is most useful as a **trend**: stable vs. growing tells you whether to watch or replace.

### Fix 4: Run the full surface scan (/r) when needed

Finds physical damage — use judiciously.

1. For HDDs with suspected bad sectors: `chkdsk C: /r` (schedule at reboot with Y). This reads every sector, recovers readable data from bad ones, and marks them unusable.
2. Budget the time: roughly 1–2 hours per TB on HDDs. Run overnight — interrupting a surface scan mid-way is safe but wastes the progress.
3. On **SSDs**, prefer skipping /r — the SSD controller already remaps bad blocks invisibly, so /r mostly burns time and write cycles for little information. S.M.A.R.T. spare-block counts are the better SSD signal.
4. After /r completes, check the **Wininit** event log entry for the bad-sector count it found and remapped.
5. If /r finds bad sectors and S.M.A.R.T. pending/reallocated counts are growing: the drive is failing — back up immediately (Fix 6) rather than re-scanning.

### Fix 5: Check cables, connections, and thermals

Physical causes produce "disk errors" that aren't the disk's fault.

1. For SATA drives (desktops/some laptops): reseat both ends of the SATA data cable, or replace the cable — intermittent connections are a top cause of phantom disk errors and CRC errors (S.M.A.R.T. attribute **UltraDMA CRC Error Count** implicates the cable specifically).
2. Check drive temperatures: HDDs should stay under ~50°C, SSDs under ~70°C under load — overheating causes transient errors. Improve airflow; laptop cooling pads help.
3. For external drives: try a different USB port (direct to PC, not a hub) and a different cable — USB connection flakiness masquerades as disk errors constantly.
4. Update **storage drivers**: chipset/SATA/NVMe drivers from your laptop maker or Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — buggy storage drivers cause errors the disk gets blamed for.
5. Re-run `chkdsk /scan` after physical fixes — errors that stop appearing were connection-caused, not media-caused.

### Fix 6: Back up and replace a failing drive

When the verdict is failure, act in the right order.

1. **Back up first**: copy critical files to external storage or cloud **before** further diagnostics — every hour on a failing drive risks more loss. Prioritize irreplaceable data (photos, documents) over reinstallable apps.
2. Create a **system image** (Control Panel > Backup and Restore > Create a system image) if the drive still reads reliably — it speeds migration to the replacement.
3. Choose the replacement: any failing HDD should become an **SSD** — a 2.5" SATA SSD for older laptops, NVMe for modern ones. This is also a massive performance upgrade.
4. Migrate via the system image or cloning software (Macrium Reflect Free, vendor tools like Samsung Magician), then verify the new drive with a fresh `chkdsk /scan` and S.M.A.R.T. baseline.
5. Keep the old drive (labeled, dated) for a month as a secondary backup, then securely wipe it. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents backup options officially.

## Closing

Checking a disk for errors is two questions: is the file system logically sound (chkdsk answers), and is the hardware healthy (S.M.A.R.T. answers). Run the online scan regularly, read S.M.A.R.T. as a trend, fix cables before condemning drives — and when the drive is genuinely failing, back up first and replace it with an SSD.
