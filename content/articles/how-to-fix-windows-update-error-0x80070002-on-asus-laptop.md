---
title: "Fix Windows Update Error 0x80070002 on an ASUS Laptop"
slug: how-to-fix-windows-update-error-0x80070002-on-asus-laptop
date: 2026-09-16
categories: ["windows-update"]
tags: ["0x80070002", "windows update error", "asus laptop", "windows 11"]
description: "Error 0x80070002 stopping Windows Update on your ASUS laptop? It means missing update files. Here are 7 fixes — cache reset, manual download, and more."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070002-on-asus-laptop.webp"
faqs:
  - q: "What does Windows Update error 0x80070002 actually mean?"
    a: "It translates to ERROR_FILE_NOT_FOUND: Windows Update tried to read a file it expected to exist — usually in the SoftwareDistribution cache or the component store — and it was not there. Common triggers are interrupted downloads, a renamed or moved update folder, or missing system files. The standard cure is to reset the update cache so Windows downloads fresh copies."
  - q: "Can I just ignore 0x80070002 and update later?"
    a: "You can postpone, but you should not ignore it permanently. Skipping updates leaves security patches uninstalled and the underlying corruption can spread — a broken update cache today becomes failed cumulative updates next month. Fixing it takes about fifteen minutes with the cache-reset steps below, which is far easier than untangling months of backlog later."
  - q: "Why does this error appear on ASUS laptops specifically?"
    a: "The error itself is not ASUS-specific, but ASUS machines hit it often because MyASUS and Armoury Crate services compete with Windows Update for downloads, and ASUS firmware updates sometimes rename the update cache mid-download. Disabling those services during the update window, then updating them separately, prevents most ASUS-flavored 0x80070002 failures."
  - q: "Will resetting SoftwareDistribution delete my files or installed updates?"
    a: "No. The SoftwareDistribution folder only holds temporary download caches and logs. Renaming it forces Windows to rebuild the cache and re-download pending updates, which is exactly what you want. Your personal files, installed programs, and already-installed updates are completely untouched by this procedure."
---

Error 0x80070002 is one of the oldest Windows Update error codes in existence, and it still shows up on brand-new ASUS laptops. The update downloads, chugs along, then fails with "Some update files are missing or have problems. We'll try to download the update again later." The message is vague enough that most people just keep clicking "Retry" — which fails again, because retrying does not recreate the missing files.

Technically, 0x80070002 is ERROR_FILE_NOT_FOUND. Windows Update expected a file to be somewhere — in the SoftwareDistribution download cache, in the component store, or in a temp directory — and it was not there. On ASUS laptops this commonly traces back to interrupted downloads (a sleep timeout mid-download is a classic), overzealous disk cleaners deleting cache files, or ASUS's own utilities renaming update folders. Whatever the trigger, the repair path is well established: give Windows a clean, complete set of update files and the error goes away.

## Why this happens

- **Interrupted update downloads.** The laptop slept, lost Wi-Fi, or restarted mid-download, leaving half-written files in the cache that Windows Update treats as corrupt.
- **A damaged SoftwareDistribution folder.** Bad sectors, crashes, or cleaner apps can mangle the folder's internal database so files appear "missing."
- **ASUS utility conflicts.** MyASUS, Armoury Crate, and ASUS Live Update services sometimes lock or rename update-related folders during their own updates.
- **Corrupted system files.** Damage in the component store means the payload Windows tries to stage is never fully written, tripping the file-not-found error.
- **Wrong date and time.** An out-of-sync system clock breaks the cryptographic validation of downloaded update files, so they are discarded as invalid.
- **Insufficient disk space.** Downloads that cannot finish writing produce incomplete files — functionally the same as missing ones.
- **Third-party antivirus interference.** Real-time scanners can quarantine update payloads mid-download, deleting files Windows Update then expects to find.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the basics — clock, space, and connection

A surprising number of 0x80070002 failures trace to trivial environmental problems. Rule them out first.

1. Check the system clock: right-click the clock, choose **Adjust date/time**, and enable **Set time automatically**. Sync errors invalidate downloads.
2. Confirm at least 10 GB of free space on C: at **Settings > System > Storage**. Feature and cumulative updates fail silently when space runs out.
3. Connect to a stable, non-metered network. If you are on a metered connection, Windows Update downloads may be throttled or truncated — go to **Settings > Network & internet > Wi-Fi**, click your network, and turn off **Metered connection**.
4. Restart the laptop once, then retry the update. If the code returns, the cache is damaged — continue to Fix 2.

### Fix 2: Reset the Windows Update cache

This is the fix that resolves most 0x80070002 cases. You stop the update services, rename the damaged cache, and let Windows rebuild it from scratch.

1. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`. If the rename fails, a process is still locking the folder — check Task Manager for ASUS Live Update or Armoury Crate and end them first.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`. Go to **Settings > Windows Update** and check for updates — the download now starts clean.

### Fix 3: Pause ASUS's competing updaters

ASUS utilities and Windows Update sometimes step on each other, renaming or locking cache folders. Let Windows have the field.

1. Open Task Manager (**Ctrl + Shift + Esc**), go to the **Startup apps** tab, and disable **ASUS Live Update**, **MyASUS**, and **Armoury Crate** entries temporarily.
2. Open **Services** (search `services.msc`) and set the **ASUS Update Service** entries to Manual, stopping them if they are running.
3. Retry Windows Update. If 0x80070002 clears, update your ASUS apps afterward — an out-of-date MyASUS is the usual culprit — then re-enable their startup entries.
4. Consider updating ASUS drivers directly from the vendor instead; our guide to [updating drivers on Windows 11](/articles/best-way-to-update-drivers-on-windows-11/) explains the safe order.

### Fix 4: Run the Windows Update troubleshooter

Microsoft's troubleshooter automates the cache check and service repair, and it occasionally catches things the manual reset misses.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow every prompt, including any "apply this fix" offers.
3. Restart, then check for updates again.
4. If the troubleshooter itself will not run or reports it cannot fix the problem, see our dedicated guide to the [Windows Update troubleshooter not working](/articles/windows-update-troubleshooter-not-working-troubleshooting/) before continuing.

### Fix 5: Repair system files with DISM and SFC

If the missing files are inside the component store rather than the download cache, the cache reset is not enough — you need to repair Windows itself.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`. Give it 15 to 30 minutes.
2. Then run `sfc /scannow` and wait for it to reach 100%.
3. If either tool reports repaired damage, restart and retry the update.
4. If DISM errors out with a source complaint, the store needs files from installation media — our guide to [running DISM RestoreHealth](/articles/how-to-run-dism-restore-health-on-windows-11/) walks through the ISO-based repair.

### Fix 6: Download the update manually from the Update Catalog

When Windows Update refuses to fetch a file, bypass it entirely: grab the update package directly from Microsoft.

1. Find the failing update's KB number in **Settings > Windows Update > Update history**.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search for that KB number, and download the package matching your architecture (x64 for nearly all ASUS laptops).
3. Double-click the downloaded `.msu` file to install it directly — no Windows Update involvement.
4. If the manual install also fails with 0x80070002, the problem is in the component store, not the download path — repeat Fix 5, and if that fails, see Fix 7.

### Fix 7: Do an in-place upgrade as the last resort

If every targeted repair fails, an in-place upgrade reinstalls Windows over itself, rebuilding the component store completely while keeping your files and apps.

1. Download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, and run `setup.exe`.
2. Choose **Keep personal files and apps** when prompted.
3. Let the install finish — 30 to 90 minutes with several restarts — then retry Windows Update.
4. Afterward, leave your ASUS utilities updated and your clock on automatic sync; both are cheap insurance against a repeat.

## Closing

Error 0x80070002 looks intimidating, but it is really just Windows saying "I can't find a file I need" — and the file it needs is almost always in a clean re-download away. On ASUS laptops, reset the cache, quiet the competing ASUS updaters, and repair the component store, and updates flow again. If a later update downloads fine but then hangs during installation instead, see our guide on updates [stuck downloading on Windows 11](/articles/how-to-fix-windows-update-stuck-downloading-on-windows-11/); and once you are patched up, following our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) — while keeping MyASUS itself updated — keeps the next cycle smooth.
