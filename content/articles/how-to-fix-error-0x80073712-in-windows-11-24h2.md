---
title: "How to Fix Error 0x80073712 in Windows 11 24H2"
slug: how-to-fix-error-0x80073712-in-windows-11-24h2
date: 2026-09-30
categories: ["windows-errors"]
tags: ["windows update error", "0x80073712", "windows 11 24h2"]
description: "Windows Update failing with error 0x80073712 on 24H2? This means damaged component store files. Here's how to repair them and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-error-0x80073712-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80073712 mean?"
    a: "Error 0x80073712 (ERROR_SXS_COMPONENT_STORE_CORRUPT) means the Windows component store — the internal library Windows Update draws from — is corrupted. Files the update needs are missing or damaged, so the installation aborts. It commonly appears after interrupted updates, failed upgrades, or disk corruption on Windows 11 24H2."
  - q: "Can error 0x80073712 be fixed without reinstalling Windows?"
    a: "Almost always, yes. DISM's RestoreHealth command is designed exactly for this: it repairs the component store using files from Windows Update or a known-good source. Only if DISM itself fails with source errors do you need heavier measures like an in-place upgrade, which still keeps your files."
  - q: "How long does DISM /RestoreHealth take?"
    a: "Typically 10–30 minutes depending on your drive speed and how damaged the store is. On slower hard drives it can take longer. Let it finish without interrupting it — stopping DISM mid-repair can make the corruption worse."
  - q: "Will this error stop all future Windows updates?"
    a: "Yes, until it's fixed. Every update that touches the damaged components will fail the same way. That's why repairing the component store first is essential — clearing the update cache alone won't help, because the underlying files are still broken."
---
Error 0x80073712 is Windows Update's way of telling you its internal parts bin is broken. Every update pulls files from the "component store," and when that store is corrupted, updates fail no matter how many times you retry. It's especially common on Windows 11 24H2 after interrupted updates or disk issues.

The good news: this is one of the most fixable update errors because Windows ships with a dedicated repair tool for exactly this problem. Work through these fixes in order — most people are done by Fix 2. If you're seeing a different code instead, check our guides for [error 0x80070003](/articles/how-to-fix-error-0x80070003-in-windows-11-24h2/) or [error 0x80070057](/articles/how-to-fix-error-0x80070057-in-windows-11-24h2/).

## Why this happens

- **Corrupted component store:** The WinSxS component store that services updates has damaged or missing files — the literal definition of this error.
- **Interrupted update:** A power loss or forced shutdown during a previous update left the store half-written.
- **Disk corruption:** Bad sectors or file system errors on the system drive damaged store files over time.
- **Failed feature update to 24H2:** Upgrades that don't complete cleanly are a top source of component store damage.
- **Third-party "cleaner" tools:** Aggressive system cleaners that delete WinSxS files to save space can break the store.
- **Malware or antivirus interference:** Kernel-level software blocking system file writes during servicing can corrupt components.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as updates install successfully.

### Fix 1: Run the Windows Update troubleshooter

Quick and occasionally sufficient — worth the two minutes before the heavier repairs.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Find **Windows Update** and click **Run**.
3. Apply any fixes it suggests and restart.
4. Try the update again. If 0x80073712 returns, move on — the troubleshooter rarely fixes component store corruption on its own.

### Fix 2: Repair the component store with DISM

This is the core fix. DISM's RestoreHealth specifically repairs the damage this error code describes.

1. Open an **administrator Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and press Enter.
3. Wait for it to reach 100% — this takes 10–30 minutes. Do not close the window or shut down.
4. When it completes successfully, immediately run `sfc /scannow` to fix any system files that depended on the repaired store.
5. Restart and retry the update in **Settings** > **Windows Update**.

### Fix 3: Run DISM with an explicit source

If Fix 2 fails with "source files could not be found," DISM needs a known-good copy to work from.

1. Download the Windows 11 24H2 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Double-click the ISO to mount it and note the drive letter (e.g., E:).
3. In an **administrator Command Prompt**, run:
   `DISM /Online /Cleanup-Image /RestoreHealth /Source:E:\Sources\install.wim`
   (Replace E: with your mounted drive letter.)
4. If your ISO contains `install.esd` instead, first check the index with `dism /Get-WimInfo /WimFile:E:\sources\install.esd`, then use `/Source:E:\sources\install.esd:1`.
5. Restart and retry the update.

### Fix 4: Check the disk for corruption

Since disk damage is a common root cause, verify the drive itself is healthy.

1. Open an **administrator Command Prompt**.
2. Run `chkdsk C: /f` and press **Y** to schedule it at restart.
3. Restart and let the scan complete.
4. After booting back, re-run Fix 2's DISM command — it may now succeed where it failed before.
5. If CHKDSK reports bad sectors repeatedly, consider the drive failing and back up your data.

### Fix 5: Reset Windows Update components

Once the store is repaired, clear out the stale update cache so the retry starts clean.

1. Open an **administrator Command Prompt**.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
5. Retry the update.

### Fix 6: Install the update manually from the Microsoft Update Catalog

If Windows Update still refuses, bypass it and install the failing KB directly.

1. In **Settings** > **Windows Update** > **Update history**, note the exact **KB number** that's failing.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB number.
3. Download the version matching your system (x64 for most laptops).
4. Run the downloaded `.msu` file and follow the prompts.
5. Restart when prompted. Manual installs often succeed where the automated pipeline chokes.

### Fix 7: Do an in-place upgrade repair

When DISM can't repair the store, reinstalling Windows over itself rebuilds it while keeping your files and apps.

1. Download the Windows 11 24H2 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO and run **setup.exe**.
3. Choose **Keep personal files and apps** when prompted.
4. Let the upgrade complete — it rebuilds the component store from scratch.
5. Afterward, run Windows Update normally; 0x80073712 should be gone.

## Closing

Error 0x80073712 sounds technical, but it boils down to one thing: Windows' update parts bin is damaged, and DISM is the tool built to rebuild it. For most people, Fix 2's `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` ends the story. If it doesn't, work down through the explicit-source repair and the in-place upgrade — both preserve your files. And going forward, avoid "cleaner" apps that promise to slim down WinSxS, and don't force-shutdown during updates: that's how component stores get broken in the first place. A healthy component store also means faster, more reliable updates overall, so the repair pays off beyond just this one error. Run a quick `sfc /scannow` every few months as preventive maintenance.
