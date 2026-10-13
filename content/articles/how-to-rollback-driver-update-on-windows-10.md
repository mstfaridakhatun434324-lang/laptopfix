---
title: "How to Roll Back a Driver Update on Windows 10 (Step-by-Step)"
slug: how-to-rollback-driver-update-on-windows-10
date: 2026-09-05
categories: ["drivers"]
tags: ["rollback driver", "windows 10", "driver update", "device manager", "system restore"]
description: "Roll back a bad driver update on Windows 10: Device Manager rollback, System Restore, manual older-driver installs, and blocking repeat updates."
thumbnail: "/images/thumbs/how-to-rollback-driver-update-on-windows-10.webp"
faqs:
  - q: "How do I roll back a driver on Windows 10?"
    a: "Right-click Start → Device Manager → right-click the device → Properties → Driver tab → 'Roll Back Driver.' Choose a reason and confirm, then restart. Windows restores the previously installed driver. If the button is grayed out, no previous driver is stored — use System Restore to a point before the update, or manually install the older driver from your laptop maker's site."
  - q: "Why is Roll Back Driver grayed out in Windows 10?"
    a: "The option needs a stored previous driver version. It's unavailable after clean installs, when the driver was installed by a method that doesn't preserve history, or when the old driver files were cleaned up long ago. The workarounds are System Restore (if a restore point predates the problem) or downloading the older driver version manually and installing it over the current one."
  - q: "How do I stop Windows 10 from updating drivers automatically?"
    a: "Use Microsoft's 'Show or hide updates' troubleshooter to hide the specific driver update, or set the policy: gpedit.msc (Pro) → Computer Configuration → Administrative Templates → Windows Components → Windows Update → 'Do not include drivers with Windows Updates' → Enabled. On Home edition, the same setting exists via registry, or use the wushowhide tool per-driver."
  - q: "Will System Restore remove my personal files?"
    a: "No. System Restore reverts system files, drivers, and registry settings to the restore point — your documents, photos, and personal files are untouched. Installed programs and drivers added after the restore point may be affected, which is why the wizard offers 'Scan for affected programs' before you commit. It's the safest broad undo in Windows."
---

Windows 10's update engine doesn't ask permission before swapping drivers, and every so often it swaps in a bad one — WiFi dies, audio crackles, the screen flickers, all starting the morning after Patch Tuesday. Rolling back the driver is the intended escape hatch, and on Windows 10 it lives in the classic Device Manager interface that hasn't changed in years.
This is the Windows 10 edition of the rollback procedure: the Device Manager rollback button, System Restore through the classic System Protection UI, manual installation of older drivers, and — critically — the Windows 10-specific ways to stop the bad driver from coming back. (On Windows 11? See our [Windows 11 rollback guide](/articles/how-to-rollback-driver-update-on-windows-11/).) If you need to compare versions first, our [Windows 10 driver version guide](/articles/how-to-check-driver-version-in-device-manager-on-windows-10/) shows how.
Timing matters with rollback: the sooner after the bad update, the more options you have. System Restore points age out, the 10-day feature-update rollback window closes, and old driver files get cleaned up. If you just noticed the breakage, act now — don't 'live with it' until the undo options expire.

## Why this happens

- **Automatic driver update via Windows Update.** Windows 10 installs driver updates alongside patches with no separate consent.
- **Feature update driver reshuffle.** Twice-yearly feature updates replace whole driver sets and break stable configs.
- **Manual update to a bad release.** You installed the latest driver yourself; latest isn't always greatest.
- **OEM-to-generic driver swap.** Update replaces the maker's tuned driver with a Microsoft generic.
- **Grayed-out rollback button.** No stored previous driver — clean install, old replacement, or cleaned-up files.
- **Repeat offense.** You roll back; Windows Update reinstalls the same bad driver.
- **Multiple broken devices.** Chipset/platform updates break several devices simultaneously.
- **Expired undo windows.** Restore points aged out or the 10-day 'go back' period lapsed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Roll back in Device Manager

Windows 10's classic path — two minutes when a previous driver is stored.

1. Right-click Start → Device Manager.
2. Right-click the broken device → Properties → Driver tab → 'Roll Back Driver.'
3. If grayed out, move to Fix 2 — don't waste time on it.
4. Pick a reason, click Yes, and restart when prompted.
5. Verify the Driver tab shows the older version/date and the device works.

### Fix 2: Use System Restore to before the update

The classic Windows 10 safety net — reverts drivers and system files without touching your documents.

1. Search 'Create a restore point' → System Protection tab → System Restore → Next.
2. Check 'Show more restore points' to see the full history with dates and descriptions.
3. Select a point from before the driver broke — descriptions often name the update.
4. 'Scan for affected programs' previews what will change.
5. Finish and let it reboot; verify the device works, then immediately do Fix 4.

### Fix 3: Manually install the older driver version

When no undo is stored, you become the undo — supply the known-good driver yourself.

1. Identify the last working version (driver date in Device Manager, or your memory of when it worked).
2. Download it from your laptop maker's Windows 10 driver archive for your exact model.
3. Device Manager → Uninstall device → check 'Delete the driver software for this device' → restart.
4. Install the older package; if the installer refuses on version grounds, extract it and use 'Have Disk' — our [compatibility mode guide](/articles/how-to-install-driver-in-compatibility-mode-on-windows-10/) walks through that.
5. Confirm the version in the Driver tab, then block updates (Fix 4) before Windows 'corrects' you.

### Fix 4: Block the bad driver on Windows 10

Windows 10 gives you solid tools to hide a specific update — use them the same day you roll back.

1. Download Microsoft's 'Show or hide updates' troubleshooter (wushowhide.diagcab).
2. Run it → Hide updates → select the offending driver update → Next.
3. For a blanket block (Pro): gpedit.msc → ...Windows Update → 'Do not include drivers with Windows Updates' → Enabled.
4. Home edition alternative: the wushowhide tool per driver, which is usually sufficient.
5. Check Windows Update history over the next days to confirm the driver stays at your version.

### Fix 5: Roll back the whole feature update if needed

When a feature update broke multiple drivers at once, reverting the update beats fixing drivers one by one.

1. Settings → Update & Security → Recovery → 'Go back to the previous version of Windows 10' (available 10 days).
2. Tell it why, check for updates when asked (it won't hurt), and let it revert.
3. Your files are preserved; drivers return to their pre-update state.
4. If the 10 days expired, this option is gone — fall back to per-driver rollback.
5. After going back, pause feature updates (Settings → Update & Security → Windows Update → pause) while you research the breakage.

### Fix 6: Rebuild via Safe Mode when the driver blocks boot

Rare but serious: a bad display or storage driver can prevent normal boot — Safe Mode loads minimal drivers.

1. Interrupt boot three times (hold power during the Windows logo) to reach Automatic Repair → Advanced options.
2. Troubleshoot → Advanced options → Startup Settings → Restart → press 4 for Safe Mode.
3. In Safe Mode, open Device Manager and roll back or uninstall the offending driver.
4. Restart normally — Windows loads the fallback driver.
5. Install the known-good driver version from Safe Mode with Networking if needed.

### Fix 7: Document and verify the stable state

Rollback is complete when the fix survives updates, not when the device merely works once.

1. Run the laptop for a few days across reboots, exercising the previously broken device.
2. Record the working driver version, date, and source in a note.
3. Create a manual restore point: System Protection → Create → name it clearly.
4. Keep the working driver installer archived on a USB drive.
5. If breakage recurs, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents recovery options, and our [driver version guide](/articles/how-to-check-driver-version-in-device-manager-on-windows-10/) helps you spot unwanted changes early.

## Closing

Windows 10's driver rollback tools are mature and reliable — the Device Manager button, System Restore, and wushowhide form a complete undo system. Use them promptly after a bad update, block the offender, and document what works. Future Patch Tuesdays will be much less exciting.
