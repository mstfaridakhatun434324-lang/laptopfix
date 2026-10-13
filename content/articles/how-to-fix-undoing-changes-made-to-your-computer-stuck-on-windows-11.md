---
title: "How to Fix 'Undoing Changes Made to Your Computer' Stuck on Windows 11"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11
date: 2026-09-10
categories: ["windows-update"]
tags: ["undoing changes", "windows 11", "windows update", "update stuck", "rollback"]
description: "Stuck on 'Undoing changes made to your computer' in Windows 11? Here's how long to wait, when to force a restart, and how to break the loop."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-windows-11.webp"
faqs:
  - q: "How long should 'Undoing changes' take before I worry?"
    a: "On an SSD laptop, a normal rollback takes 15 to 45 minutes. On a mechanical hard drive, allow up to two hours. If the screen shows no percentage movement for more than two hours and the hard drive activity light is dark, the rollback has almost certainly stalled and you should intervene rather than waiting overnight."
  - q: "Is it safe to force restart during 'Undoing changes'?"
    a: "It is safer than force-restarting during an update installation, because Windows is already rolling back to a known-good state. There is still a small risk of a corrupted boot configuration, which is why you should only intervene after the screen has been frozen for hours. If you do force a restart, have the Windows recovery environment ready in case the laptop needs automatic repair."
  - q: "Why did Windows undo the update instead of finishing it?"
    a: "Windows rolls back an update automatically when the installation fails its final checks — a driver conflict, a corrupted update file, insufficient disk space, or a third-party antivirus blocking a critical step. The 'Undoing changes' screen means the safety mechanism worked. Your job now is to find out which part failed so it does not happen on the next attempt."
  - q: "Will my files be affected by the rollback?"
    a: "No. Undoing changes only reverses the update's system modifications and returns Windows to the state it was in before the update began. Your documents, photos, installed programs, and personal settings are untouched by the rollback process itself, which is exactly why it exists."
---

Few screens are more nerve-wracking than this one. Your Windows 11 laptop tried to install an update, something went wrong, and now it sits on "Undoing changes made to your computer" with a spinning circle — for an hour, maybe two, with no percentage and no sign of progress. The good news is that the screen itself means Windows' safety net is working: rather than booting into a half-updated system, it is rolling back to the state your laptop was in before the update started.

The bad news is that the rollback can stall. A normal rollback on an SSD takes 15 to 45 minutes; on a mechanical hard drive it can take up to two hours.

This guide tells you exactly how long to wait, how to check whether the rollback is genuinely working, and how to break out of the loop safely if it is stuck. Follow the fixes in order — most people never need to go past the third one.

## Why this happens

- **The update itself failed mid-install.** Driver conflicts, corrupted download files, or a third-party antivirus blocking a critical step cause the installer to abort, and Windows automatically starts undoing the changes.
- **The rollback process stalled on a bad sector.** If the drive has failing areas, the rollback can get stuck reading or writing the files it needs to restore.
- **Insufficient disk space chokes the rollback.** Reverting an update needs working space on the C: drive. If the drive is nearly full, the undo process slows to a crawl or freezes.
- **A corrupted update cache replays bad data.** Damaged files in the SoftwareDistribution folder can make the rollback engine chew on the same broken data repeatedly.
- **Pending driver installations conflict with the rollback.** Drivers queued by Windows Update can fight the rollback process, especially graphics and storage drivers.
- **Third-party disk encryption interferes.** Encryption software that hooks the boot process can block the rollback from completing its file operations.
- **Failing RAM causes silent corruption.** Memory errors during the rollback produce corrupt writes, which the rollback engine detects and retries indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it a proper waiting window and verify activity

Many "stuck" rollbacks are just slow. Verify before you intervene.

1. Note the exact time, then wait a full hour from now without touching anything. On HDD-based laptops, allow two hours total from when the screen first appeared.
2. Watch the laptop's disk activity light if it has one. Blinking means the rollback is genuinely working — leave it alone.
3. Listen for the drive or fan. Steady activity sounds mean progress; complete silence for 30 minutes means a stall.
4. If there is any movement — a percentage appearing, the screen flickering, the laptop restarting on its own — the process is alive. Only proceed when there has been zero change and zero activity for the full waiting window.

### Fix 2: Force a restart, then let automatic repair run

If the rollback is truly frozen, a forced restart is the correct move — the system was already reverting to a safe state.

1. Hold the **power button** for a full 10 seconds until the laptop shuts off completely. Unplug any USB drives, docks, and external monitors.
2. Wait 30 seconds, then power on. In most cases Windows boots normally to the desktop or login screen, because the rollback had partially completed.
3. If Windows instead shows the recovery environment, choose **Troubleshoot > Advanced options > Startup Repair** and let it run.
4. Do not run Windows Update again immediately. First confirm the system is stable by using it normally for a while.

### Fix 3: Boot into Safe Mode and clear the update cache

If the laptop boots but the next update attempt lands you back on the same screen, the corrupted cache is the prime suspect.

1. Hold **Shift** while clicking **Restart** from the login screen to reach the recovery environment, then go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4** for Safe Mode.
2. In Safe Mode, open an elevated Command Prompt and stop the update services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services with the matching `net start` commands, reboot normally, and try the update again. If the same failure returns, the update file itself — not just the cache — is the problem.

### Fix 4: Free up disk space before retrying the update

Rollbacks and retries both need breathing room on the C: drive.

1. In Safe Mode or normal Windows, open **Settings > System > Storage** and check free space on C:. You want at least 20 GB free before attempting a feature or cumulative update again.
2. Run **Disk Cleanup** with system files selected, and remove **Windows Update Cleanup**, temporary files, and the Recycle Bin contents.
3. Uninstall programs you no longer use, and move large personal files (videos, downloads) to an external drive temporarily.
4. Retry the update only after the space is confirmed.

### Fix 5: Temporarily disable third-party antivirus and encryption conflicts

Security software that hooks deep into the system is a classic cause of failed updates and frozen rollbacks.

1. If you run a third-party antivirus, disable its real-time protection temporarily — or uninstall it completely before the next update attempt and rely on Windows Security in the meantime.
2. If you use third-party full-disk encryption, check its documentation for update-safe procedures; some products require the drive to be decrypted before major updates.
3. Disconnect from any VPN during the update. VPN drivers have been known to interfere with update staging.
4. Attempt the update again with this software out of the way, then reinstall or re-enable your protection afterward.

### Fix 6: Run the Windows Update troubleshooter and SFC

With the system booted and stable, repair the update pipeline so the retry does not land on the same screen.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter. Apply all suggested repairs.
2. Open an elevated Command Prompt and run `sfc /scannow` to repair damaged system files that may have caused the original failure.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
4. Restart, then check for updates. If the update now installs cleanly, the loop is broken.

### Fix 7: Block the problem update or repair-install Windows

If one specific update keeps failing and rolling back, stop fighting it directly.

1. Identify the failing update in **Settings > Windows Update > Update history**.
2. Download it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install it offline — manual installs bypass several failure modes of the automatic pipeline.
3. If a feature update (like 24H2) is the culprit and your hardware is marginal for it, pause updates for a few weeks under **Advanced options** while Microsoft ships fixes. Guidance on known issues is posted on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
4. As a last resort, perform a repair install using installation media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), keeping your files and apps. This rebuilds the update system from scratch.

## Closing

The "Undoing changes" screen is Windows protecting you from a half-installed update, and most of the time it resolves itself if you give it a real chance. The critical skill is telling a slow rollback from a frozen one: activity means patience, silence means intervention. Once you are back on the desktop, resist the urge to immediately retry the same update the same way — clear the cache, free up space, and identify what failed first. If the undo screen appears after a failed feature upgrade specifically, the walkthrough for [undoing changes after a Windows 11 update](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) covers that variant, and the [step-by-step undoing-changes guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-step-by-step/) is a good companion to keep bookmarked.
