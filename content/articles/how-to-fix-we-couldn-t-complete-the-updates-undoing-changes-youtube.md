---
title: "How to Fix 'We Couldn't Complete the Updates, Undoing Changes' on Windows"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-youtube
date: 2026-09-30
categories: ["windows-update"]
tags: ["couldn't complete updates", "undoing changes", "windows update", "update failed", "windows 11"]
description: "Seeing 'We couldn't complete the updates, undoing changes'? Here's what the message means and the exact steps to fix the failed update."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-youtube.webp"
faqs:
  - q: "What does 'We couldn't complete the updates, undoing changes' mean?"
    a: "It means Windows tried to install updates, the installation failed partway, and the system is now reversing the partial changes to restore your previous working state. The message is the rollback notification, not the problem itself. Once it finishes, your laptop returns to exactly how it was before the update attempt, with your files untouched."
  - q: "Why do I see this message after every update?"
    a: "A repeating message means the same blocker defeats every attempt: a corrupted update download, a driver that conflicts with the new build, or insufficient free disk space are the usual suspects. Windows retries automatically and fails identically each time. The fix is to identify the specific failing update and remove the blocker rather than letting the loop continue."
  - q: "How do I find out which update keeps failing?"
    a: "Open Settings, then Windows Update, then Update history. Failed updates appear with their KB numbers and error codes. That history tells you whether the problem is a cumulative update, a feature update, or a driver update, and the error code narrows the cause dramatically — for example, 0x80070002 points to missing files while 0x800f0922 points to EFI partition problems."
  - q: "Is my laptop damaged when this message appears?"
    a: "No. The message proves the safety mechanism worked: rather than booting a half-updated system, Windows restored the last known-good state. The update failed, but the system is intact. Repeated failures are frustrating and worth fixing, but they do not damage your hardware or your files."
---
"We couldn't complete the updates, undoing changes" is Windows telling you, in plain language, that an update failed and the system is rolling itself back to safety. It is the notification for the automatic rollback — the message itself is not the problem. The problem is whatever made the update fail, and if you see this message repeatedly, that cause is still sitting there waiting to defeat the next attempt too.

This message shows up across Windows 10 and Windows 11, on every brand of laptop, and it has become one of the most searched update errors because it is both alarming and vague. It does not name the update, the error, or the cause. This guide fills in all three: how to identify the failing update, what the common causes are, and the exact steps to break the cycle.

A useful mental model: the message has two halves. "We couldn't complete the updates" describes the failed install — that is where the fix lives. "Undoing changes" describes the automatic recovery — that part needs no fixing, only patience while it finishes. Most people who get into trouble do so by attacking the second half (interrupting the rollback) instead of the first (fixing the failed update). Work through the fixes in order — diagnose first, then act.

## Why this happens

- **The update download was corrupted.** Damaged payload files fail the installer's verification, aborting the install.
- **A driver conflicts with the new build.** Incompatible graphics, storage, or chipset drivers fail the install's final checks.
- **Free disk space ran out.** Updates need staging room; a nearly full C: drive aborts installs partway.
- **Third-party antivirus blocked the install.** Security software hooking the file system can prevent critical file replacements.
- **A previous update never finished.** Pending operations from an earlier update leave the system in a state the next one cannot build on.
- **System files are corrupted.** Damage in the component store fails the installer's integrity checks.
- **The update itself is problematic.** Occasionally Microsoft ships an update with a genuine bug affecting certain hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish, then identify the failed update

Do not interrupt the undo — then get the specifics.

1. Let the "undoing changes" phase complete fully, even if it takes an hour. Interrupting a rollback is riskier than interrupting an install.
2. Once on the desktop, open **Settings > Windows Update > Update history**.
3. Note the failed update's KB number, type (cumulative, feature, driver), and error code.
4. Search the KB number on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues before doing anything else.

### Fix 2: Clear the corrupted update cache

The most common fix for the most common cause. When the same update fails repeatedly with the same behavior, the downloaded files are the prime suspect — every retry reuses the same damaged payload.

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Run Windows Update again. A clean download resolves the majority of repeat failures, and the renamed .old folders give you a fallback if anything unexpected happens.

### Fix 3: Free up disk space

Space-starved installs fail in exactly this pattern.

1. Check **Settings > System > Storage** — you need at least 10 GB free for cumulative updates, 20 GB or more for feature updates.
2. Run **Disk Cleanup** with system files selected and clear **Windows Update Cleanup** and temporary files.
3. Move large personal files off C: temporarily and uninstall unused programs.
4. Retry the update with confirmed free space.

### Fix 4: Resolve driver conflicts

If the failing update is a driver update — or a system update failing on driver checks — handle drivers first.

1. Open **Device Manager** and look for warning icons on display, storage, and network devices.
2. Update suspect drivers from your laptop manufacturer's support site: Dell, HP, or Lenovo.
3. Uninstall any third-party driver updater tools, which are a frequent conflict source.
4. Retry the Windows update with clean drivers in place.

### Fix 5: Remove antivirus and VPN interference

Security software blocking the installer is a classic mid-install failure cause.

1. Temporarily disable third-party antivirus real-time protection, or uninstall it and use Windows Security during the update.
2. Disconnect from any VPN.
3. Retry the update.
4. Restore your protection afterward.

### Fix 6: Repair system files

Damaged components fail the installer's verification and trigger the rollback.

1. In an elevated Command Prompt, run `sfc /scannow` to completion.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 15 to 30 minutes.
3. Restart and retry the update.
4. If the same update fails identically after repairs, the update package itself may be the problem — continue to Fix 7.

### Fix 7: Install manually, hide, or pause the problem update

When the automatic pipeline cannot handle one specific update, route around it.

1. Download the failing update by KB number from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it manually.
2. If the manual install works, the pipeline was the problem — resume normal updates.
3. If it fails too, hide the update with the show/hide troubleshooter, or pause updates for a few weeks while Microsoft ships a fixed version.
4. For feature updates that repeatedly fail on older hardware, a repair install from the Windows 11 download page rebuilds the system cleanly.

## Closing

"We couldn't complete the updates, undoing changes" looks scary but means the safety net worked — the real work is finding why the update failed. Identify it in update history, clear the cache, fix the drivers, and free up space, in that order, and the message stops appearing. If the rollback screen itself freezes rather than completing, the [undoing-changes stuck guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11/) covers the frozen-rollback case, and the [step-by-step undoing-changes walkthrough](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-step-by-step/) takes you through the full recovery sequence.
