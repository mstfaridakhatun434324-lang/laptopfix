---
title: "How to Fix Windows Update Error 0x80070570 on Windows 11 24H2"
slug: "how-to-fix-windows-update-error-0x80070570-in-windows-11-24h2"
date: 2026-09-12
categories: ["windows-update"]
tags: ["0x80070570", "windows update error", "windows 11 24h2", "corrupt update files", "windows update"]
description: "Windows Update failing with error 0x80070570 on Windows 11 24H2 means the downloaded files are corrupted and unreadable. Here is how to clear the bad files, check your drive and memory, and get the update installed."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-in-windows-11-24h2.webp"
faqs:
  - q: "What does Windows Update error 0x80070570 mean?"
    a: "Error 0x80070570 translates to ERROR_FILE_CORRUPT, which means a file or directory is corrupted and unreadable. In the context of Windows Update, it almost always means the update package downloaded to your PC is damaged — either the download itself was interrupted, the disk wrote it incorrectly, or faulty RAM corrupted it in memory. Windows refuses to install a package that fails its integrity checks, so the update aborts with this code."
  - q: "Can bad RAM cause error 0x80070570?"
    a: "Yes, and it is one of the most overlooked causes. Faulty or unstable memory can corrupt data as it moves between the network, RAM, and disk, so the update file that lands on your drive no longer matches what Microsoft sent. If 0x80070570 keeps returning after you clear the update cache, and especially if you also see random application crashes, running the built-in Windows Memory Diagnostic is a smart next step before assuming the disk is at fault."
  - q: "Will error 0x80070570 damage my files or installed programs?"
    a: "No. The error fires during the download and verification stage, before anything is installed, so your existing files and programs are untouched. The worst it does is leave behind a broken partial download in the update cache and possibly repeated failed attempts. Clearing the SoftwareDistribution folder removes those leftovers safely without affecting personal data or installed software."
  - q: "How long does it take to fix error 0x80070570?"
    a: "Most cases resolve within 30 to 60 minutes. Clearing the update cache and re-running the update takes about 15 minutes, a system file check adds another 15 to 20, and a disk check can take 30 minutes or more on a large drive. A memory test takes the longest — plan for at least an hour if you run the extended pass. The manual install from the Update Catalog is the fastest workaround when you need the update today."
---
You click "Check for updates," the download finishes, and instead of installing you get the blunt message: error 0x80070570. On Windows 11 24H2 this code means one thing — the update files sitting on your drive are corrupted and Windows will not touch them. It is not a permissions problem and not a server problem; the package itself failed its integrity check.

The corruption can happen at several points. A flaky Wi-Fi connection can truncate the download, a disk with developing bad sectors can garble the write, and unstable RAM can scramble the data in transit. Third-party antivirus products that intercept downloads sometimes mangle large update packages too. The good news is that the fix is almost always local: throw away the damaged files, verify the hardware that touched them, and let Windows download a fresh copy.

Work through the fixes below in order. Fix 1 alone resolves the majority of cases, and the hardware checks in Fixes 3 and 4 catch the stubborn ones that keep coming back. If the update downloads but the machine later hangs on a restart screen, our guide to [fixing Windows Update stuck on the restarting screen in 24H2](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) picks up where this one leaves off.

## Why this happens

- **Corrupted download in the update cache** — An interrupted or truncated download leaves a damaged package in C:\Windows\SoftwareDistribution. Windows detects the mismatch during verification and aborts with 0x80070570 instead of installing garbage.

- **Bad sectors on the system drive** — A drive developing bad sectors can corrupt files as they are written. Update packages are large multi-gigabyte files, so they are statistically the first thing to hit a dying sector.

- **Faulty or unstable RAM** — Memory errors corrupt data in transit between the network adapter, RAM, and disk. This produces exactly the 'corrupted file' symptom even when the disk itself is healthy.

- **Antivirus interfering with the download** — Some third-party security suites scan and quarantine parts of large update packages mid-download, leaving a package that no longer matches its checksum.

- **Corrupted system files in the component store** — If the servicing stack or component store is already damaged, even a perfect download can fail integrity checks during installation, surfacing as 0x80070570.

- **Interrupted update service** — Windows Update services (wuauserv, BITS) crashing or being force-stopped mid-download leave partial files that the next attempt tries to resume from instead of replacing.

- **Disk running critically low on space** — When the system drive has almost no free space, large update files get written incompletely or fragmented across bad areas, and verification fails.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

Start with the built-in troubleshooter. It is not magic, but on 24H2 it specifically detects corrupted update cache states and resets the pending-download flags that keep Windows retrying the same broken package. If the troubleshooter itself errors out, our guide to [repairing a broken Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) gets it working again.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Windows Update** in the list and click **Run**.
3. Let it complete — it may take several minutes — and apply any fixes it offers.
4. Restart the laptop, then open **Settings > Windows Update** and click **Check for updates** to force a fresh download attempt.

### Fix 2: Clear the corrupted update cache manually

The troubleshooter does not always empty the cache. Doing it by hand guarantees Windows downloads a completely fresh copy instead of resuming the damaged one.

1. Open Command Prompt as administrator (search **cmd**, right-click, **Run as administrator**).
2. Stop the update services: run `net stop wuauserv`, then `net stop bits`, then `net stop cryptsvc`.
3. Delete the contents of **C:\Windows\SoftwareDistribution\Download** (leave the folder itself in place).
4. Restart the services with `net start wuauserv`, `net start bits`, and `net start cryptsvc`, then check for updates again.

### Fix 3: Check the drive for bad sectors with CHKDSK

Because 0x80070570 literally means 'corrupted and unreadable,' the disk itself is a prime suspect. CHKDSK finds bad sectors and recovers readable information, and on 24H2 it runs cleanly from within Windows with a reboot.

1. Open Command Prompt as administrator.
2. Run `chkdsk C: /f /r` and press **Y** when asked to schedule the check at next restart.
3. Restart the laptop and let the scan finish — do not interrupt it, even if the percentage appears stuck.
4. After booting back into Windows, retry the update. If CHKDSK reported bad sectors, consider replacing the drive soon.

### Fix 4: Test your RAM with Windows Memory Diagnostic

If the error returns after a clean cache and a healthy disk, suspect memory. One failing stick can corrupt every large download while the rest of the system seems fine.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**.
3. Let the standard test complete; for a deeper check, press **F1** at the blue screen and select **Extended**.
4. If errors are reported, reseat the RAM modules or test with one stick at a time to identify the faulty one.

### Fix 5: Repair system files with SFC and DISM

Damaged servicing components can make even good downloads fail verification. SFC repairs protected system files, and DISM repairs the component store that SFC itself relies on — run them in that order.

1. Open an elevated Command Prompt.
2. Run `sfc /scannow` and wait for it to finish (typically 10-20 minutes).
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and let it complete.
4. Restart and run Windows Update again. Microsoft documents both tools in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Temporarily disable third-party antivirus

If you run a non-Microsoft antivirus, its download interception may be the corrupting agent. A short, controlled test with it disabled tells you definitively.

1. Open your antivirus settings and disable real-time protection temporarily (Microsoft Defender stays active as a safety net).
2. Clear the update cache once more using the steps in Fix 2.
3. Run Windows Update and see if the download now completes and installs.
4. If it succeeds, add an exclusion for the update process in your antivirus or switch to Defender permanently.

### Fix 7: Install the update manually from the Microsoft Update Catalog

When the built-in updater keeps producing corrupt downloads, bypass it entirely. Downloading the standalone package from the official catalog gives you a fresh file over a normal browser download.

1. Open **Settings > Windows Update > Update history** and note the exact **KB number** that failed.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB number.
3. Download the package matching your system (x64 for most modern laptops) and run the .msu file.
4. Restart when prompted. If even the manual package fails verification, an in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) is the final option.

## Closing

Error 0x80070570 looks alarming, but it is Windows protecting you from installing a damaged package. Clear the cache, verify the disk and memory, and give it a fresh download — that sequence resolves nearly every case without touching your files or programs.
