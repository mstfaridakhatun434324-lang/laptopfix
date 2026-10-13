---
title: "Windows Update Says 'Undoing Changes Made to Your Computer': How to Fix It"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer
date: 2026-09-13
categories: ["windows-update"]
tags: ["undoing changes", "windows update", "update failed", "rollback", "windows 11"]
description: "Windows Update keeps saying 'Undoing changes made to your computer'? Find out why updates roll back and how to get them to install."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer.webp"
faqs:
  - q: "What does 'Undoing changes made to your computer' mean?"
    a: "It means a Windows update failed during installation and Windows is automatically reversing the partial changes to restore your previous working system. It is a built-in safety mechanism, not a sign of permanent damage. Once the rollback finishes, your laptop returns to exactly the state it was in before the update attempt began."
  - q: "Why does the same update keep undoing itself?"
    a: "A repeating undo cycle almost always points to one persistent blocker: a corrupted update download, a driver that conflicts with the new build, or too little free disk space. Windows retries the update automatically, hits the same blocker, and rolls back again. Identifying the specific failing update and clearing the blocker breaks the cycle."
  - q: "How can I see which update is failing?"
    a: "Go to Settings, then Windows Update, then Update history. Failed updates are listed with their KB numbers and error codes. That history is your diagnostic starting point: it tells you whether you are dealing with a cumulative update, a feature update, or a driver update, and the error code points to the specific failure cause."
  - q: "Should I just disable Windows Update to stop this?"
    a: "No. Disabling updates leaves known security vulnerabilities unpatched and eventually breaks other things that depend on current system components. The right approach is to fix the underlying failure so updates install cleanly. If one specific update is problematic, pause updates temporarily or hide that update rather than disabling the whole service."
---

When Windows Update says "Undoing changes made to your computer," it is telling you something specific: an update tried to install, failed partway through, and Windows is now reversing the partial installation to get you back to a working system. It is the operating system's safety net doing its job. The screen itself is not the problem — the failed update behind it is.

This message becomes a real headache when it repeats. Windows retries failed updates automatically, so a persistent blocker — a corrupted download, a conflicting driver, a nearly full drive — produces a loop: attempt, fail, undo, repeat. Each cycle can take 30 minutes or more, and the laptop may feel unusable in the meantime.

This guide treats the message as a symptom and goes after the causes. You will learn how to identify which update is failing, clear the common blockers, and get the update to install instead of rolling back. Work through the fixes in order.

## Why this happens

- **A corrupted update download.** Damaged payload files fail verification during installation, so the installer aborts and triggers the rollback.
- **A driver conflicts with the new build.** Graphics, storage, or chipset drivers that are incompatible with the update cause the install to fail its final checks.
- **Insufficient free disk space.** Updates need working room to stage files; a nearly full C: drive causes installs to fail partway through.
- **Third-party antivirus blocks critical steps.** Security software that hooks the file system can prevent the installer from replacing protected files.
- **Pending operations from a previous update.** An earlier update that never finished its restart leaves the system in a state the next update cannot build on.
- **Corrupted system files.** Damage in the component store makes the installer's verification fail, which triggers the automatic undo.
- **A failing drive or memory.** Hardware faults produce corrupt writes during installation, which the installer detects and rolls back.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the failing update in update history

Guessing wastes time. Get the specifics first.

1. Open **Settings > Windows Update > Update history** and look for entries marked as failed. Note the KB number and any error code.
2. Determine the update type: cumulative updates, feature updates, and driver updates each have different common causes.
3. Search the KB number on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues — some updates have documented conflicts with specific hardware.
4. Write down the error code. Codes like 0x80070002 (missing files) and 0x800f0922 (EFI partition issues) point to very specific fixes, and you will use this information in the steps below.

### Fix 2: Clear the update cache and retry

A corrupted download is the most common single cause, and clearing the cache forces a fresh copy.

1. Open an elevated Command Prompt and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Run Windows Update again. A clean download resolves a large share of repeat undo cycles.

### Fix 3: Free up disk space on the system drive

Space-starved updates fail in exactly this way, and the fix is straightforward.

1. Check **Settings > System > Storage** for free space on C:. You need at least 20 GB free for feature updates and 10 GB for cumulative updates.
2. Run **Disk Cleanup** with system files selected and remove **Windows Update Cleanup**, temporary files, and old delivery optimization files.
3. Move large personal files to external storage and uninstall unused programs.
4. Retry the update after confirming the free space.

### Fix 4: Resolve driver conflicts before retrying

If update history shows a driver update failing alongside the system update, handle the driver first.

1. Open **Device Manager** and look for devices with warning icons — these are your suspects.
2. For the suspect device, right-click and choose **Update driver > Search automatically**, or download the driver from your laptop manufacturer's support site (Dell, HP, or Lenovo).
3. If a third-party driver updater tool is installed, uninstall it — these tools are a frequent source of driver conflicts.
4. Once Device Manager is clean, retry the Windows update.

### Fix 5: Temporarily remove antivirus interference

Security software blocking the installer is a classic cause of mid-install failures.

1. If you use a third-party antivirus, disable real-time protection temporarily, or uninstall it and rely on Windows Security during the update.
2. Disconnect from any VPN, whose drivers can interfere with update staging.
3. Retry the update with this software out of the way.
4. Re-enable or reinstall your protection afterward — do not leave the laptop unprotected longer than necessary.

### Fix 6: Repair system files with SFC and DISM

Damaged system components cause the installer's verification to fail and trigger the undo.

1. In an elevated Command Prompt, run `sfc /scannow` and let it finish.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store; allow 15 to 30 minutes.
3. Restart and retry the update. Repaired files often break the failure cycle.

### Fix 7: Install the update manually or pause it

When the automatic pipeline keeps failing on one specific update, go around it.

1. Download the failing update by its KB number from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it offline.
2. If the manual install succeeds, the automatic pipeline was the problem, not the update itself.
3. If the update is a feature update your hardware struggles with, pause updates under **Advanced options** for a few weeks while Microsoft ships fixes.
4. For a persistently bad driver update, use the show/hide updates troubleshooter to hide it and install the manufacturer's driver manually instead.

## Closing

"Undoing changes made to your computer" is a message about a failed update, not a broken laptop — the rollback is Windows protecting you. The fix is almost always upstream of the message: a corrupted cache, a conflicting driver, or a full drive. Identify the failing update in your history, clear the blocker, and retry rather than letting the loop run indefinitely. If the rollback itself appears frozen rather than just repeating, our guide to the [undoing-changes screen on Windows 11](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11/) covers the stuck-rollback case, and the [step-by-step undoing-changes walkthrough](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-step-by-step/) goes deeper into the full recovery sequence.
