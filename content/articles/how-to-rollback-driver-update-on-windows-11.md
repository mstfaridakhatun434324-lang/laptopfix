---
title: "How to Roll Back a Driver Update on Windows 11 (Step-by-Step)"
slug: how-to-rollback-driver-update-on-windows-11
date: 2026-10-10
categories: ["drivers"]
tags: ["rollback driver", "driver update", "device manager", "windows 11", "system restore"]
description: "Need to roll back a driver update on Windows 11? Learn the Device Manager rollback, system restore, and manual reinstall methods — plus how to stop it happening again."
thumbnail: "/images/thumbs/how-to-rollback-driver-update-on-windows-11.webp"
faqs:
  - q: "How do I roll back a driver in Windows 11?"
    a: "Open Device Manager (Windows + X), right-click the device, choose Properties, open the Driver tab, and click 'Roll Back Driver.' You'll be asked why you're rolling back — pick a reason and confirm. Windows restores the previously installed driver version. The button is only available if a previous driver version exists on the system; if it's grayed out, use System Restore or manual reinstall instead."
  - q: "Why is the Roll Back Driver button grayed out?"
    a: "The button is grayed out when Windows has no previous driver stored for that device — common after clean Windows installs, when the driver was installed via a method that doesn't preserve the old version, or when Windows Update replaced the driver long ago and the old files were cleaned up. In that case, download the older driver from your laptop maker's support site and install it manually, or use a System Restore point."
  - q: "Will rolling back a driver delete my files?"
    a: "No. Rolling back a driver only replaces the driver software for that specific hardware device — it doesn't touch your documents, apps, or settings. It's one of the safest troubleshooting operations in Windows. That said, creating a System Restore point before any driver change is still good practice in case the rollback itself causes unexpected behavior."
  - q: "How do I stop Windows 11 from updating the driver again?"
    a: "After rolling back, prevent recurrence: open Device Manager → device Properties → Driver tab → 'Update Driver' won't help, so instead use Group Policy (gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Windows Update → 'Do not include drivers with Windows Updates') or the registry equivalent. Alternatively, use the 'Show or hide updates' troubleshooter to hide the specific driver update."
---

Everything worked yesterday. Then Windows Update installed a new driver overnight, and now your WiFi drops, your audio crackles, or your screen flickers. The driver update giveth, and the driver update taketh away — and Windows 11 gives you a built-in undo button for exactly this situation. Rolling back a driver takes about two minutes when the option is available.
This guide covers all three rollback paths: the one-click Device Manager rollback, System Restore for when the button is grayed out, and manual reinstall of the older driver for stubborn cases. Just as important, we'll show you how to stop Windows from 'helpfully' reinstalling the bad driver tomorrow. If you want to compare versions before deciding, our [driver version check guide](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/) shows how to read what's installed.
Rollback is also the correct response when a manual driver update you installed yourself goes wrong — same buttons, same process. And if Windows keeps pushing driver updates you don't want, our guide to [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) is the permanent fix.

## Why this happens

- **Windows Update installed a buggy driver.** The classic trigger — an automatic driver update breaks previously working hardware.
- **Manual update to an unstable release.** You installed the newest driver yourself and it's worse than what you had.
- **OEM driver replaced by generic.** Windows swaps your laptop maker's tuned driver for a Microsoft generic that lacks features.
- **Driver conflict after major Windows upgrade.** Feature updates reshuffle drivers and break previously stable combinations.
- **Partial or interrupted update.** The new driver half-installed, leaving the device in a broken intermediate state.
- **Rollback button grayed out.** No previous driver stored — happens after clean installs or long-ago replacements.
- **Windows re-installs the bad driver.** You roll back, and Update pushes the same bad driver again overnight.
- **Multiple devices affected.** A chipset or platform update breaks several devices at once, needing coordinated rollback.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Device Manager rollback button

The one-click undo — works when Windows kept the previous driver, which it usually does for update-initiated changes.

1. Open Device Manager (Windows + X) and find the misbehaving device.
2. Right-click → Properties → Driver tab.
3. Click 'Roll Back Driver.' If it's grayed out, skip to Fix 2.
4. Select a reason (e.g., 'Previous driver worked better') and click Yes.
5. Restart the laptop and verify the device works — check the Driver tab to confirm the older version/date is active.

### Fix 2: Restore via a System Restore point

When the rollback button is grayed out, a restore point from before the update achieves the same result system-wide.

1. Search 'Create a restore point' → System Protection tab → System Restore.
2. Choose 'Choose a different restore point' to see the full list with dates.
3. Pick a restore point dated before the driver problem started.
4. Click 'Scan for affected programs' to preview what else will revert — drivers and system files only, not documents.
5. Confirm and let it run; the laptop will reboot. Verify the device works afterward.

### Fix 3: Manually install the older driver

The most reliable method when neither rollback nor restore is available — you supply the known-good driver yourself.

1. Find the previous working version: check the driver date in Device Manager, or recall when the device last worked.
2. Download that older driver from your laptop maker's support site (their driver archives list versions and dates).
3. In Device Manager, right-click the device → Uninstall device, checking 'Attempt to remove the driver for this device.'
4. Restart, then install the downloaded older driver package.
5. Verify the version in the Driver tab matches what you intended — then immediately do Fix 4 so Windows doesn't 'fix' it.

### Fix 4: Block Windows from reinstalling the bad driver

Rollback is pointless if Update re-pushes the same driver overnight. This is the step everyone forgets.

1. Download Microsoft's 'Show or hide updates' troubleshooter (wushowhide) and use it to hide the specific driver update.
2. Alternatively, open gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Windows Update → Manage updates offered from Windows Update → enable 'Do not include drivers with Windows Updates.'
3. On Windows 11 Home (no gpedit), set the registry: HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate → DWORD ExcludeWUDriversInQualityUpdate = 1.
4. Verify over the next few days that the driver version stays put.
5. Revisit this policy when you actually want a driver update — blocked means blocked.

### Fix 5: Roll back graphics drivers with DDU when needed

GPU drivers sometimes resist normal rollback; Display Driver Uninstaller gives you a clean slate to install the older version.

1. Download DDU and the older GPU driver version you want (NVIDIA/AMD/Intel archives).
2. Disconnect from the internet so Windows can't interfere mid-process.
3. Boot into Safe Mode and run DDU → 'Clean and restart.'
4. Install the older driver package, choosing Custom/Clean install if offered.
5. Reconnect to the internet and confirm stability under load before re-enabling automatic updates.

### Fix 6: Handle multi-device breakage after feature updates

Major Windows upgrades can break several drivers at once — prioritize and work systematically.

1. List every broken device in Device Manager (yellow icons) before changing anything.
2. Start with the most critical: network (to stay online), then display, then audio.
3. Roll back each via Device Manager where possible; use manual reinstall for grayed-out ones.
4. Consider rolling back the entire feature update: Settings → System → Recovery → 'Go back' (available for 10 days after the upgrade).
5. Document which driver versions work — future you will thank present you. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the recovery options if you need a refresher.

### Fix 7: Verify stability and document the working setup

Rollback isn't done when the device works — it's done when it stays working.

1. Use the laptop normally for a day with the rolled-back driver, exercising the previously broken function.
2. Confirm Windows Update hasn't re-offered the bad driver (check Update history).
3. Write down the working driver version and date from Device Manager's Driver tab.
4. Create a fresh System Restore point labeled with the working configuration.
5. If the device breaks again later, you'll know exactly which version to return to.

## Closing

Driver rollback is Windows' built-in apology mechanism — use it promptly when an update breaks things, then block the bad update so the apology sticks. Two minutes of rollback plus five minutes of prevention beats hours of fighting a driver that never worked.
