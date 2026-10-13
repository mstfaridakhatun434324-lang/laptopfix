---
title: "How to Fix Windows 10 Update Error 0x800f0900"
slug: how-to-fix-error-0x800f0900-on-windows-10
date: 2026-09-08
categories: ["windows-errors"]
tags: ["0x800f0900", "Windows Update", "CBS corruption"]
description: "Error 0x800f0900 means Windows 10 can't process an update due to corrupted component files. Repair the component store and get updates flowing again."
thumbnail: "/images/thumbs/how-to-fix-error-0x800f0900-on-windows-10.webp"
faqs:
  - q: "What does error 0x800f0900 mean?"
    a: "It indicates corruption in the Component-Based Servicing (CBS) manifest data — the internal catalog Windows uses to track system components. When update files or their manifests are damaged, the update engine cannot verify what it is installing and aborts with this code. The standard fix is repairing the component store with DISM, which rebuilds the damaged manifests from known-good sources."
  - q: "Will DISM fix 0x800f0900 by itself?"
    a: "Usually, yes. Running DISM /Online /Cleanup-Image /RestoreHealth repairs the component store that 0x800f0900 complains about. Run SFC afterward to fix any system files that reference the repaired components. If DISM itself fails, point it at a Windows 10 ISO as a repair source, which bypasses the need to download files from Windows Update."
  - q: "Is 0x800f0900 related to .NET Framework updates?"
    a: "Often. This error frequently appears when installing cumulative updates that include .NET Framework components, because the .NET manifests are a common corruption point. If the error names a .NET update, try repairing the .NET installation or installing the update manually from the Microsoft Update Catalog before running the full DISM repair."
  - q: "Can I just skip the failing update?"
    a: "You can hide it temporarily, but that is not a real fix — the underlying component store corruption will block future updates too, including security patches. Repair the corruption properly with DISM so the update pipeline works again. Skipping should only be a stopgap while you schedule time for the repair."
---

Error 0x800f0900 shows up when Windows 10 tries to install an update and discovers its own internal component catalog is damaged. The update engine relies on Component-Based Servicing (CBS) manifests to know exactly which files belong where, and when those manifests are corrupt, the whole installation aborts. You will typically see it on cumulative updates, and it has a particular fondness for updates that touch the .NET Framework.

The fix is almost always the same: repair the component store with DISM, verify with SFC, and retry the update. It is a methodical process rather than a quick one — the DISM scan alone can take 20 minutes — but it resolves this error reliably. Work through the steps below in order.

## Why this happens

- **Corrupted CBS manifests.** The component catalog gets damaged by interrupted updates, disk errors, or bad shutdowns.
- **Damaged .NET Framework components.** .NET manifests are a frequent corruption point for this specific error.
- **Corrupted update cache.** Badly downloaded update files in SoftwareDistribution poison subsequent attempts.
- **Third-party "cleaner" tools.** Aggressive system cleaners sometimes delete or modify component store files.
- **Disk errors.** Bad sectors in the WinSxS folder corrupt the manifests stored there.
- **Interrupted servicing operations.** A power loss during a previous update leaves the component store half-written.

## How to fix it

Work through these in order, retrying the update after each major repair.

### Fix 1: Run DISM to repair the component store

This is the core fix for 0x800f0900 — it rebuilds the damaged CBS data.

1. Open **Command Prompt (Admin)** from `Win + X`.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait — this typically takes 15 to 30 minutes.
3. Do not close the window or shut down while it runs.
4. When it finishes, immediately run `sfc /scannow` to repair system files against the fixed store.
5. Restart the laptop.
6. Go to **Settings > Update & Security > Windows Update** and retry the update.

### Fix 2: Use a Windows 10 ISO as the DISM repair source

If DISM fails or reports it cannot find source files, feed it a known-good source.

1. Download the Windows 10 ISO from Microsoft's website (linked via [Microsoft Support](https://support.microsoft.com/en-us/windows)) and mount it by double-clicking — note the drive letter, e.g. E:.
2. Open **Command Prompt (Admin)**.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth /Source:E:\Sources\install.wim` (use `install.esd` if that is what the ISO contains).
4. If the command complains about the WIM index, specify it: `/Source:E:\Sources\install.wim:1`.
5. Follow with `sfc /scannow`, restart, and retry the update.

### Fix 3: Reset the Windows Update cache

Clear out corrupted downloads that may be compounding the problem.

1. Open **Command Prompt (Admin)**.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptSvc`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptSvc`.
5. Retry the update.

### Fix 4: Install the failing update manually from the Update Catalog

Bypassing the automatic updater sometimes sidesteps the corruption.

1. In **Settings > Update & Security > Windows Update > View update history**, note the KB number of the failing update.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB number.
3. Download the version matching your system (x64 for most laptops).
4. Run the downloaded .msu file and follow the prompts.
5. If the manual install also fails with 0x800f0900, the component store still needs the DISM repair — go back to Fix 1.

### Fix 5: Repair or reinstall the .NET Framework

Since .NET updates trigger this error disproportionately, address .NET directly.

1. Open **Control Panel > Programs > Programs and Features > Turn Windows features on or off**.
2. Uncheck **.NET Framework 3.5** and **.NET Framework 4.8 Advanced Services**, click OK, and restart.
3. Reopen the same dialog, re-check both items, click OK, and restart again — this reinstalls the frameworks from the component store.
4. Retry the Windows update.
5. If problems persist, download the .NET repair tool from Microsoft's site and run it.

### Fix 6: Check the disk for errors

Corruption in WinSxS may come from a failing drive.

1. Open **Command Prompt (Admin)**.
2. Run `chkdsk C: /f` and confirm the schedule for the next restart with **Y**.
3. Restart and let the check complete.
4. Afterward, re-run the DISM repair from Fix 1, since CHKDSK may have quarantined damaged manifest files.

### Fix 7: Perform an in-place upgrade

When the component store resists all repair, reinstall Windows over itself.

1. Download the **Media Creation Tool** for Windows 10 (find it through [Microsoft Support](https://support.microsoft.com/en-us/windows)).
2. Run it, choose **Upgrade this PC now**, and select **Keep personal files and apps**.
3. The upgrade rebuilds the entire component store from fresh media.
4. After it completes, run Windows Update — it should work normally.

The closely related [error 0x800f0922](/articles/how-to-fix-error-0x800f0922-in-windows-11-24h2/) has similar servicing roots, and our walkthrough on [running SFC in Windows 11 24H2](/articles/how-to-run-sfc-scannow-in-windows-11-24h2/) covers the scan technique in more depth.

### Fix 8: Disable third-party filter drivers and security tools during the update

Kernel-level filters from security and disk tools can interfere with servicing operations.

1. Temporarily uninstall (not just disable) third-party antivirus — filter drivers stay loaded even when "disabled."
2. Uninstall disk encryption, backup agents, or "system protection" utilities that install file-system filters.
3. Confirm Windows Defender is active so you remain protected during the update.
4. Retry the update, then reinstall the third-party tools afterward if you want them.

## Closing

Error 0x800f0900 is Windows telling you its own bookkeeping is broken, and DISM is the tool built specifically to fix that bookkeeping. Run the repair, verify with SFC, clear the update cache, and the update that kept failing will almost always install cleanly on the next attempt. If you had to use the ISO-source method, keep that ISO around — it is handy for any future servicing repair. And go easy on aggressive system cleaners going forward; the WinSxS folder is not junk, and "cleaning" it is how many people end up with this error.
