---
title: "How to Check a Disk for Errors on Windows 11"
slug: how-to-check-disk-for-errors-on-windows-11
date: 2026-09-10
categories: ["performance"]
tags: ["disk errors", "chkdsk", "windows 11", "storage", "diagnostics"]
description: "Worried about disk errors on Windows 11? Run chkdsk correctly, read SMART health data, and know when the drive needs replacing."
thumbnail: "/images/thumbs/how-to-check-disk-for-errors-on-windows-11.webp"
faqs:
  - q: "What does chkdsk actually check?"
    a: "Chkdsk verifies the logical integrity of the file system — it finds and repairs corrupt file records, cross-linked files, bad security descriptors, and directory errors. With the /r flag it also scans the entire disk surface for bad sectors and recovers readable data from them. It checks the file system's bookkeeping and the physical media, which is why it's the first tool for suspected disk problems."
  - q: "How long does chkdsk take?"
    a: "A basic chkdsk /f on a healthy drive takes a few minutes. A full chkdsk /f /r surface scan takes much longer — roughly one to two hours per terabyte on a hard drive, faster on SSDs. Schedule it when you don't need the laptop, keep it plugged in, and don't interrupt it: stopping a surface scan mid-pass is safe but wastes all progress."
  - q: "Can chkdsk damage my data?"
    a: "Chkdsk is designed to be safe — it repairs file system structures and recovers data from bad sectors rather than deleting it. In rare cases on already-failing drives, the stress of a full surface scan can push marginal hardware over the edge, which is why you should back up first if the drive shows SMART warnings. On a healthy drive, chkdsk is routine and safe."
  - q: "What's the difference between chkdsk and SMART?"
    a: "Chkdsk checks the file system and disk surface right now — it's a point-in-time repair tool. SMART is the drive's own continuous self-monitoring: it tracks reallocated sectors, read errors, and wear indicators over the drive's life. Use chkdsk to fix logical problems; use SMART data to judge whether the drive itself is dying and needs replacement."
---

Disk errors announce themselves subtly at first: a file that won't open, a freeze during a save, Windows suggesting you "scan and fix" a drive, or chkdsk running uninvited at boot. Catching disk problems early is the difference between a repair and data loss — and Windows 11 gives you solid built-in tools for both checking and interpreting drive health.

This guide covers the full disk-health check: the quick GUI scan, the proper chkdsk command sequence, reading SMART data to judge the drive's remaining life, and the signs that mean "back up now, replace the drive." Run these in order whenever you suspect the disk.

## Why this happens

- **Bad sectors develop:** Magnetic media degrades; SSD cells wear out — both produce unreadable spots over time.
- **Improper shutdowns:** Power loss mid-write corrupts file system structures.
- **Aging drives:** Mechanical wear on HDDs and write-cycle exhaustion on SSDs accumulate errors.
- **Failing controllers or cables:** Intermittent connection faults corrupt data in transit.
- **File system corruption:** Software crashes and bugs damage the NTFS bookkeeping.
- **Overheating:** Sustained heat accelerates media degradation on both HDDs and SSDs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the quick GUI error check first

Open File Explorer → right-click C: → Properties → Tools → Check. This runs a fast, non-invasive scan and reports whether errors were found — it won't fix deep problems, but it tells you in two minutes whether there's anything to worry about. If it reports no errors and your symptoms are mild, the disk is probably fine and your problem lies elsewhere. If it finds errors or recommends a deeper scan, continue to chkdsk. This quick check is the triage step: fast, safe, and decisive for the easy cases.

1. Open drive Properties → Tools → Check.
2. Let the quick scan complete.
3. If clean and symptoms are mild, look elsewhere.
4. If errors found, continue to the chkdsk sequence.

### Fix 2: Run chkdsk with the right flags

Open an admin Command Prompt. Start with `chkdsk C: /f` — the /f flag fixes file system errors; if Windows says the drive is locked, agree to schedule at next reboot and restart. For a thorough check, follow with `chkdsk C: /f /r` — the /r flag adds a full surface scan that finds bad sectors and recovers readable data. Read the summary at the end: "bad sectors" found means physical media damage (note the count); file system errors fixed means logical corruption repaired. A clean /r pass is strong evidence the drive media is healthy.

1. Run `chkdsk C: /f` in an admin Command Prompt.
2. Schedule at reboot if the drive is locked.
3. Follow with `chkdsk C: /f /r` for the surface scan.
4. Read the summary for bad sectors vs. fixed file errors.

### Fix 3: Check SMART data for the drive's health verdict

Chkdsk checks the file system; SMART judges the hardware. Open an admin Command Prompt and run `wmic diskdrive get status` for the basic verdict (OK vs. Pred Fail). For detail, use CrystalDiskInfo (free) or your drive manufacturer's tool — look at Reallocated Sector Count, Current Pending Sector Count, and (for SSDs) wear/remaining life percentage. Any raw values above zero in reallocated/pending sectors on an HDD, or SSD life below 20%, means the drive is degrading — back up and plan replacement regardless of what chkdsk said. SMART is the prognosis; chkdsk was the checkup. The [24H2 disk-check guide](/articles/how-to-check-disk-for-errors-in-windows-11-24h2/) covers the newest Windows builds specifically.

1. Run `wmic diskdrive get status` for the quick verdict.
2. Inspect detailed SMART attributes with CrystalDiskInfo.
3. Treat reallocated sectors or low SSD life as replacement signals.
4. Back up immediately if SMART shows warnings.

### Fix 4: Repair system files damaged by disk errors

Disk errors often corrupt Windows files as collateral. After chkdsk, run `sfc /scannow` in an admin Command Prompt, then `DISM /Online /Cleanup-Image /RestoreHealth` — these repair system files that bad sectors or file system corruption may have damaged. If SFC reports it fixed corrupted files, reboot and verify the original symptoms (freezes, app crashes) are gone. This step matters because a repaired disk with still-corrupted system files keeps misbehaving — the disk fix and the file fix are a pair. Microsoft documents both tools in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Run `sfc /scannow` after chkdsk completes.
2. Follow with DISM restore-health.
3. Reboot and verify original symptoms resolved.
4. Repeat chkdsk if new errors appear quickly.

### Fix 5: Back up and replace a failing drive

If SMART shows failing attributes, chkdsk keeps finding new bad sectors, or freezes persist after repair — stop troubleshooting and replace the drive. Back up immediately: copy personal files to external storage or cloud, and consider a full disk image (Macrium Reflect Free or similar) if the drive still reads. For the replacement, an SSD is the obvious choice — faster, more shock-resistant, no mechanical wear. After replacement, reinstall Windows fresh (via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) rather than cloning a damaged file system. A failing drive is a countdown, not a condition to manage.

1. Back up personal files immediately.
2. Consider a disk image if the drive still reads reliably.
3. Replace with an SSD, not another HDD.
4. Do a fresh Windows install on the new drive.

### Fix 6: Set up ongoing disk health monitoring

After the crisis, prevent the next one. Enable your manufacturer's drive utility (Samsung Magician, WD Dashboard, Crucial Storage Executive) for continuous SMART monitoring with alerts. Keep 15–20% free space — full drives accelerate wear and hide problems. Schedule the quick GUI check quarterly, and keep backups current (a failing drive with a fresh backup is an inconvenience; without one, it's a disaster). If this scare taught you anything, let it be the backup habit — the [freezing troubleshooting guide](/articles/what-to-do-if-windows-11-freezing-randomly/) shows how disk issues masquerade as other problems.

1. Install the manufacturer's monitoring utility with alerts.
2. Maintain 15–20% free space on all drives.
3. Run the quick error check quarterly.
4. Keep backups current — automate them.

## Closing

Checking a disk for errors is a three-layer job: chkdsk for the file system and surface, SMART for the hardware's prognosis, SFC/DISM for the collateral damage. Clean on all three means the disk is fine — look elsewhere. Warnings on any layer mean act: back up, and replace a drive that's telling you it's dying. Drives are consumables; your data isn't.
