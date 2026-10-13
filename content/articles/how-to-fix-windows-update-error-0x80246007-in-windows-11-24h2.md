---
title: "How to Fix Windows Update Error 0x80246007 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80246007-in-windows-11-24h2
date: 2026-09-01
categories: ["windows-update"]
tags: ["windows update", "0x80246007", "error code", "windows 11", "bits"]
description: "Error 0x80246007 means Windows Update never finished downloading because BITS stalled. Unjam the download pipeline with these repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80246007-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80246007 mean?"
    a: "The designation is WU_E_DM_NOTDOWNLOADED — the update's payload never fully arrived, so there is nothing to install. The breakdown is in the delivery chain: a wedged BITS queue, confused cache bookkeeping, or a BITS service trapped in a broken state. Repairing that chain, rather than the update itself, clears the error in most cases."
  - q: "What is BITS and why does Windows Update need it?"
    a: "BITS, the Background Intelligent Transfer Service, is Windows' quiet courier for update files. It downloads in the background, yields bandwidth to your active work, and resumes after interruptions. When that courier jams or gets switched off, no update download can finish — and 0x80246007 is what you see."
  - q: "Is bitsadmin /reset /allusers safe to run?"
    a: "Yes. It only cancels background transfer jobs that are currently stuck, and Windows Update restarts anything it still needs on its own. Your documents, programs, and settings are never touched. It is the standard first response to a suspected jam in the BITS queue."
  - q: "BITS will not start at all. What now?"
    a: "Confirm its dependencies are alive in services.msc — COM+ Event System and Remote Procedure Call must both be running. If they are, re-register qmgr.dll and qmgrprxy.dll from an elevated prompt, then reset the Windows Update components. A BITS service that still refuses to start signals deeper damage, where DISM and SFC or an in-place upgrade come into play."
---

Ever had a parcel marked "failed delivery" when the courier never even picked it up? That is 0x80246007 in a nutshell. Windows Update lists the update as failed, yet nothing was installed — because nothing ever finished downloading. The usual preludes on 24H2 laptops: a download that died halfway, a cache whose records stopped matching reality, or the Background Intelligent Transfer Service getting itself wedged.

Microsoft's formal label for it is WU_E_DM_NOTDOWNLOADED. The important word there is the implication: the fault sits with the delivery crew — BITS and the SoftwareDistribution cache — not with the update package. Fix the courier and the parcels start arriving again.

That framing decides the whole repair strategy below. The fixes are ordered from least to most invasive, and in practice the answer is almost always found before the halfway mark.

## Why this happens

- **The BITS queue has jammed.** A single wedged transfer job can blockade every download queued behind it.
- **Cache records drifted from reality.** The download cache may insist files exist that were never fully written.
- **An interrupted transfer left a phantom entry.** When a connection dies mid-download, the queue can wrongly conclude the job finished.
- **BITS' supporting services got switched off.** Aggressive tuning tools sometimes disable the dependencies BITS relies on.
- **Security software grips the cache files.** Real-time scanning can stop BITS from writing finished downloads to disk.
- **The disk filled up mid-transfer.** If C: runs out of room during the download, the pipeline aborts.
- **The queue database itself is corrupt.** When BITS' own data file goes bad, every queued download stalls.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Inspect BITS and the services around it

Since the failure lives in the delivery layer, examine that layer before touching anything update-related.

1. Press Win + R, enter `services.msc`, and find **Background Intelligent Transfer Service** in the list.
2. It should show a status of Running and a startup type of Automatic (Delayed Start) — note whatever you actually find.
3. Check that **Windows Update** and **Cryptographic Services** are running too.
4. Try starting BITS manually if it is stopped; any error it throws is a useful clue. A service that will not stay running points to Fix 2, while a healthy one points to Fix 3.

### Fix 2: Flush the queue and bounce the service

Cancelling every stuck transfer and restarting BITS hands the pipeline a clean slate, and none of your files are involved.

1. Launch a Command Prompt with administrator rights.
2. Run `bitsadmin /reset /allusers` to cancel all stuck background transfers.
3. Then run `net stop bits`, pause a moment, and run `net start bits`.
4. Run another update check and observe whether the download starts moving.

### Fix 3: Re-register the pipeline's core libraries

An empty queue with a still-misbehaving BITS points at damaged component registrations. Re-registering the key DLLs rebuilds the plumbing.

1. Stop the three related services first: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Run `regsvr32 qmgr.dll` and acknowledge the confirmation dialog, then do the same with `regsvr32 qmgrprxy.dll`.
3. Start everything again: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Attempt the update download once more.

### Fix 4: Let the automated troubleshooter try

Windows includes a diagnostic that already understands this pattern — dead services, wrecked cache, broken route to Microsoft. It applies only safe automatic repairs, so there is no risk in trying it before manual work.

1. Open Settings and travel to System > Troubleshoot > Other troubleshooters.
2. Hit Run alongside the Windows Update item and respond to its inquiries.
3. Once done, restart the laptop and revisit Windows Update. If the code remains, continue below.

### Fix 5: Rebuild the update components from scratch

When BITS-specific repairs do not end the error, the engine's own cache is usually rotten. Renaming the cache folders out of the way forces Windows to regenerate its download state; your data is never involved.

1. In the elevated prompt, halt the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename both folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Relaunch the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Open Settings > Windows Update, check again, and confirm the error lifted.

### Fix 6: Fetch the update yourself from the Catalog

A broken automatic pipeline can simply be walked around by fetching the exact KB yourself. Every cumulative and servicing-stack package is published on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

1. In Update history, find the failed update and copy its KB number.
2. Search the Catalog for that KB and download the x64 Windows 11 package.
3. Run the downloaded `.msu` and complete its installer.
4. Reboot if prompted, then verify the update appears in your history.

### Fix 7: Reinstall Windows while preserving the existing copy

Reserved for when every targeted repair fails: Windows 11 24H2 installed over itself, with files and programs kept. The ISO must come from [Microsoft's Windows 11 download site](https://www.microsoft.com/en-us/software-download/windows11) and nowhere else.

1. Download the ISO, double-click to mount it, and start `setup.exe` from the new drive.
2. Agree to the license terms, then keep **Keep personal files and apps** selected.
3. Give the installer 30 to 90 minutes with several automatic restarts; never cut power mid-way.
4. Sign back in and run Windows Update to confirm the error is gone for good.

## Closing

Delivery failures bow to pipeline repairs: a flushed BITS queue, a running service, and a rebuilt cache get downloads finishing on their own. If downloads then succeed but installation stumbles, the [24H2 update-failure guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) picks up the story, and the [troubleshooter walkthrough](/articles/best-way-to-fix-windows-update-with-troubleshooter/) automates the service checks. BITS internals are documented in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
