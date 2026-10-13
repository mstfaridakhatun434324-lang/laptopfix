---
title: "Step-by-Step: Fix Windows Update Stuck on 'Undoing Changes'"
slug: how-to-fix-windows-update-undoing-changes-stuck-step-by-step
date: 2026-09-20
categories: ["windows-update"]
tags: ["undoing changes", "windows update stuck", "rollback", "windows 11", "step by step"]
description: "A clear step-by-step sequence for Windows stuck on 'Undoing changes made to your computer': wait windows, safe recovery, cache reset, and a clean retry."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-step-by-step.webp"
faqs:
  - q: "How do I know if the undo screen is stuck or just slow?"
    a: "Give it one hour on an SSD or two hours on a hard drive. Watch the disk activity light and listen for drive noise during that window. Blinking or chatter means the rollback is still working, so keep waiting. Total silence plus zero screen change for the entire window means it is genuinely stalled, and that is when you may intervene with a forced restart."
  - q: "Will forcing a restart during 'Undoing changes' damage Windows?"
    a: "Not once the rollback has genuinely stalled. The rollback was already restoring your previous working system, so interrupting a frozen one is far less risky than interrupting an active update. Hold the power button for ten seconds, remove peripherals, and boot. Windows will usually start normally or enter automatic repair, which fixes interrupted boot files on its own."
  - q: "Does the rollback delete my documents and apps?"
    a: "No. Undoing changes reverses only the system modifications the failed update had started to make. Your documents, photos, installed programs, and personal settings are preserved. The rollback exists to hand you back the exact working system you had before the update attempt, with your files untouched."
  - q: "What should I do so the next update does not fail the same way?"
    a: "Clear the update cache by renaming the SoftwareDistribution folder, free at least 20 GB on the C: drive, update your drivers, and run SFC and DISM before retrying. Temporarily disable third-party antivirus during the attempt. A prepared retry succeeds far more often than an immediate repeat of the same failing conditions."
---

"Undoing changes made to your computer" is Windows' safety net in action. When an update fails partway through, the operating system automatically reverses the partial installation and hands you back the system you had before. On a healthy machine that process finishes in 15 to 45 minutes on an SSD, or up to two hours on a mechanical hard drive, and life goes on.
The trouble starts when the screen freezes in place. No progress indicator, no new messages, just the spinning dots for hours on end. That is a stalled rollback, and it calls for a different response than a slow one: patience first, then a careful intervention, then a methodical fix for whatever caused the original failure. Guessing and rebooting at random can turn a recoverable situation into a boot-repair project.
This guide lays out the exact sequence, step by step, with nothing skipped and nothing out of order. You will verify the stall, recover the machine safely, reset the update machinery, and prepare a retry that actually succeeds. If you want the overview of what causes this screen, see the [best-practice approach to a stuck undo screen](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/), and if you ever need the recovery environment, [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) has you covered.

## Why this happens

- **An update failed and triggered the rollback.** Corrupted downloads, driver clashes, or security software blocking file writes abort the install; Windows reverses what it started.
- **The rollback is slow, not stuck.** File restoration takes real time, and the screen gives no progress readout, so slow progress looks identical to a freeze.
- **The rollback stalled mid-process.** A failing drive sector, exhausted disk space, or conflicting software can stop the undo engine partway through.
- **The update cache is corrupted.** Damaged files in SoftwareDistribution and catroot2 give the rollback bad data to reverse.
- **The system drive is nearly full.** The undo operation needs working space; below a few free gigabytes it stalls.
- **Security software interfered.** Overly aggressive antivirus or endpoint protection can block the file operations the rollback needs.
- **A driver package conflicts.** Half-installed or incompatible driver updates fight with the files being restored.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall with the full wait window

Never act on the first hour. The rollback gives no progress display, so patience with verification beats an early restart that adds boot problems.

1. Note the time the screen first appeared, then wait one full hour on an SSD or two hours on a hard drive.
2. Watch the disk activity light throughout: blinking means the rollback is working, so keep waiting.
3. Listen for drive chatter or fan noise. Steady activity means progress; dead silence for 30 minutes means a stall.
4. Only continue after the full window with zero screen change and zero drive activity.

### Fix 2: Perform a safe forced restart

A genuinely stalled rollback will not recover on its own. Interrupting it is safe because the system was already being restored to its previous state.

1. Hold the power button for 10 seconds until the laptop powers off completely.
2. Disconnect all USB devices, docks, external monitors, and SD cards to rule out peripheral boot hangs.
3. Wait 30 seconds, then power on. Most machines boot to the login screen or desktop.
4. If the blue recovery screen appears, let Automatic Repair run to completion without interrupting it.

### Fix 3: Enter Safe Mode and reset the update components

Once Windows is reachable, clear the corrupted update cache so the next attempt does not fail on the same bad data.

1. Hold Shift while choosing Restart from the login screen, then go to Troubleshoot > Advanced options > Startup Settings > Restart and press 4 for Safe Mode.
2. Open an elevated Command Prompt and run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Start the services again with the matching `net start` commands, then restart the laptop normally.

### Fix 4: Free disk space and clean temporary files

Rollback stalls and repeat update failures both trace back to cramped system drives. Give the retry the room it needs.

1. Open Settings > System > Storage and verify at least 20 GB free on C:.
2. Run Disk Cleanup with the system-files option and remove Windows Update Cleanup, temporary files, and delivery optimization files.
3. Move large media files to external storage and uninstall unused applications.
4. Re-check the free space before any retry — this single step fixes a surprising share of repeat failures.

### Fix 5: Repair the system image with SFC and DISM

Corrupted system files are a top cause of the original update failure. Repairing the image before the retry breaks the failure cycle.

1. Open an elevated Command Prompt and run `sfc /scannow` to completion.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`, allowing 15 to 30 minutes.
3. Restart the laptop after both tools finish, regardless of what SFC reported.

### Fix 6: Update drivers and pause security interference

Driver clashes and antivirus blocks abort updates silently. Address both before the retry.

1. Open Device Manager and update the display, storage, and network drivers from the manufacturer's site.
2. Update your third-party antivirus, then temporarily disable its real-time protection for the update attempt.
3. Leave Windows Defender active as your baseline protection during the retry.
4. Consult the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) if a specific error code appears.

### Fix 7: Retry the update under controlled conditions

With the cache cleared, space freed, the image repaired, and drivers current, the retry has every advantage. Run it on your terms.

1. Connect to AC power and a stable, non-metered network — never update on battery.
2. Go to Settings > Windows Update and click Check for updates.
3. Install updates one group at a time rather than all at once if the machine has a history of failures.
4. If the update fails again, record the exact error code and check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for that specific package.

## Closing

A stuck undo screen is frustrating precisely because it gives you no information, but the sequence is always the same: verify the stall, restart safely, reset the update machinery, fix the root cause, and retry under good conditions. Follow the steps in order and you will spend one afternoon fixing this instead of three evenings fighting it.
