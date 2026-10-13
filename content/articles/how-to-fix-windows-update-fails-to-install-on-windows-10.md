---
title: "How to Fix Windows Update Failing to Install on Windows 10"
slug: how-to-fix-windows-update-fails-to-install-on-windows-10
date: 2026-09-13
categories: ["windows-update"]
tags: ["windows 10", "update fails", "install error", "windows update"]
description: "Windows 10 updates download but fail during installation? Diagnose the real blocker and fix it with this ordered guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-fails-to-install-on-windows-10.webp"
faqs:
  - q: "Why do Windows 10 updates fail at the installing stage?"
    a: "The install phase modifies protected system files, updates the component store, and migrates drivers — any of which can fail if files are corrupted, drivers conflict, disk space runs out, or a previous update left the servicing state inconsistent. The download succeeding only proves the network works; installation is a much deeper operation."
  - q: "What does 'We couldn't complete the updates, undoing changes' mean?"
    a: "It means the installer detected a failure partway through and rolled the system back to its pre-update state to keep Windows bootable. Your files are safe. The message is actually good news — the rollback worked — but you still need to find and fix whatever caused the failure before retrying."
  - q: "Should I use the Update Assistant instead of Windows Update?"
    a: "The Update Assistant is worth trying when Windows Update itself keeps failing, because it uses a different installation path and often succeeds where the built-in engine stalls. It is Microsoft's official tool, so it is safe — just make sure you have a backup and a stable power connection first."
  - q: "Can a failing hard drive cause update install failures?"
    a: "Yes. Updates write thousands of files, and a drive with bad sectors or failing flash cells will corrupt some of them, causing installs to fail at random points. If failures happen at different percentages each time, check the drive health with chkdsk and your manufacturer's diagnostic before blaming software."
---

On Windows 10, the failure pattern is depressingly familiar: the update downloads fine, the install begins, and then — sometimes at 30%, sometimes at 96% — it fails and Windows spends twenty minutes "undoing changes." You are back where you started, minus half an hour. The download working tells you the network and Microsoft's servers are fine. The problem is on your machine, in the installation phase, where Windows modifies its own guts.

Windows 10's servicing stack is the oldest still in mainstream use, and it shows. It has been patching itself for a decade, accumulating component store cruft, superseded updates, and driver migrations that newer engines handle more gracefully. The Component-Based Servicing log (CBS.log) on a long-lived Windows 10 machine often tells a story of years of small corruptions, each harmless alone, that collectively make the installer unable to assemble a consistent new state. That is why the standard advice — reset the components, repair the store, refresh the drivers — works: it gives the aging engine a clean foundation to build on.

Windows 10's update engine is older and fussier than Windows 11's, and it accumulates cruft: old caches, half-finished servicing operations, and drivers that have not been touched in years. This guide diagnoses the failure properly before fixing it, in the order that wastes the least of your time.

## Why this happens

- **Corrupted system files.** The installer verifies files as it works; damaged ones abort the install.
- **A damaged component store.** Years of updates can leave the WinSxS store inconsistent, and the installer cannot build on a broken foundation.
- **Driver conflicts.** Old or incompatible drivers — especially storage and display drivers — crash the install phase.
- **Insufficient disk space.** The install needs staging space well beyond the download size; Windows 10 is quiet about this requirement.
- **Pending operations from a previous update.** An earlier update that never finished its restart holds locks the new install needs.
- **Third-party interference.** Antivirus, encryption, and "tune-up" utilities can block or corrupt the installer's file operations.
- **Failing storage.** Bad sectors corrupt files mid-install, producing failures at inconsistent percentages.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the exact failure point and error code

The failure's fingerprint tells you where to look.

1. Open **Settings** > **Update & Security** > **Windows Update** > **View update history** and find the failed update's error code.
2. Note the percentage where it fails. Same percentage every time points to a specific file or driver; random percentages point to disk or memory.
3. Check the time: failures after a reboot (during the blue "Working on updates" screen) are driver or servicing issues; failures before reboot are usually file or space issues.

### Fix 2: Free up space aggressively

Windows 10 needs more staging room than it admits.

1. Open **Settings** > **System** > **Storage** and confirm at least 20 GB free on C:.
2. Run **Disk Cleanup** as administrator, click **Clean up system files**, and select **Windows Update Cleanup**, **Temporary Windows installation files**, and **Delivery Optimization Files**.
3. Consider moving the page file or hibernation file temporarily if you are critically short — `powercfg /h off` frees gigabytes instantly.

### Fix 3: Finish any pending update first

Clear the queue before adding to it.

1. Check for a pending restart in Windows Update. If one exists, restart now and let it complete fully.
2. Verify in **Update history** that the earlier update shows successful.
3. Then attempt the new update. This simple sequencing fix resolves a surprising number of "fails to install" cases.

### Fix 4: Reset the Windows Update components

Give the installer a clean cache to work from.

1. Open an elevated Command Prompt and run:
   ```
   net stop wuauserv
   net stop cryptSvc
   net stop bits
   net stop msiserver
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   net start wuauserv
   net start cryptSvc
   net start bits
   net start msiserver
   ```
2. Retry the update. If you want the background on why this works, see [how to reset stuck update components](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/).

### Fix 5: Repair the component store and system files

Fix the foundation on Windows 10's older servicing stack.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated prompt. On Windows 10 this can take 30+ minutes — let it finish.
2. Then run `sfc /scannow`.
3. Restart and retry. For Windows 10 specifically, you can also [install updates manually](/articles/how-to-manually-install-windows-update-on-windows-10/) to bypass a damaged automatic engine.

### Fix 6: Update storage and display drivers

Old drivers are the classic Windows 10 install-killer.

1. Open **Device Manager** and update drivers for storage controllers and display adapters from the manufacturer's site — not just Windows Update.
2. For Intel systems, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html); for discrete GPUs use NVIDIA or AMD.
3. Temporarily disable third-party antivirus during the install attempt.

### Fix 7: Use the Update Assistant or a manual install

When the built-in engine will not cooperate, go around it.

1. Download the **Windows 10 Update Assistant** from Microsoft's software download page and run it — it uses a separate install path.
2. Alternatively, grab the specific KB from [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually.
3. If both fail identically, the servicing stack is damaged and an in-place repair install is the remaining option — [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows) documents that path.

## Closing

Windows 10 update install failures reward diagnosis over repetition: the error code and failure percentage tell you whether you are fighting space, files, drivers, or the disk itself. Work the list in order — space, pending restarts, cache reset, file repair, drivers — and use the Update Assistant as the alternate route. Most "undoing changes" loops break at Fix 4 or Fix 5; the ones that do not are usually telling you about a driver or a dying drive.
