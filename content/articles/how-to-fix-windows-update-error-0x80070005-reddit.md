---
title: "Windows Update Error 0x80070005? Fix the Access Denied Error"
slug: "how-to-fix-windows-update-error-0x80070005-reddit"
date: "2026-09-21"
categories: ["windows-update"]
tags: ["windows update", "0x80070005", "access denied", "error fix"]
description: "Error 0x80070005 blocking Windows Update on your laptop? This access-denied error has specific causes, and these seven fixes address each one."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-reddit.webp"
faqs:
  - q: "What does Windows Update error 0x80070005 mean?"
    a: "Error 0x80070005 is the Windows access denied error code, and in the update context it means the installer was blocked from reading or writing files it needs. The usual causes are incorrect permissions on system folders, a corrupted user profile context for the update service, antivirus blocking file operations, or corrupted system files. Because it is a permissions problem, the fixes focus on restoring correct access rather than re-downloading anything."
  - q: "Can antivirus cause error 0x80070005?"
    a: "Yes, third-party antivirus software is one of the most common triggers for 0x80070005 during updates. When the antivirus blocks the servicing stack from modifying protected files, Windows reports the operation as access denied. Temporarily disabling real-time protection during the update, as described in this guide, quickly determines whether your antivirus is the culprit."
  - q: "Is it safe to reset permissions on system folders?"
    a: "Resetting permissions should be done carefully and only with the documented methods, such as the subinacl approach or taking ownership through the proper dialogs. Indiscriminate permission changes can weaken system security. The steps in this guide target only the specific folders Windows Update needs, which is safe and restores the default access the installer expects."
  - q: "What if 0x80070005 appears for the Microsoft Store too?"
    a: "When 0x80070005 affects both Windows Update and the Microsoft Store, the cause is usually system-wide, such as corrupted permissions on shared folders, a damaged user profile, or broken system files. The DISM and SFC repairs plus the permission reset steps in this guide address the shared root cause, and creating a fresh local administrator account is a good diagnostic test."
---
Error 0x80070005 is Windows telling you, in its blunt way, that access was denied. When it appears in Windows Update, it means the installer tried to read or write files it needs and the operating system refused. The update itself is probably fine; the problem is that something, permissions, antivirus, or corruption, is standing between the installer and the files it must touch.

This error frustrates people because retrying never helps. The same blocked operation fails identically every time until the underlying access problem is fixed. The causes are specific and diagnosable: wrong permissions on system folders, an antivirus product blocking servicing writes, a damaged user profile, or corrupted system files confusing the security subsystem.

This guide targets each cause directly with seven ordered fixes. You will check the simple things first, reset the relevant permissions safely, isolate antivirus interference, and repair system files as the final measure. If you are hitting a different code instead, our guides on [0x80070002](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) and [0x800f0900](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) cover those.

## Why this happens

- **Incorrect folder permissions:** Wrong ACLs on SoftwareDistribution or system folders block the installer's writes.
- **Antivirus blocking file operations:** Security suites intercept servicing writes and Windows reports access denied.
- **Corrupted user profile:** A damaged profile context can break the security tokens update services rely on.
- **Broken system files:** Corruption in the security or servicing components produces false access failures.
- **Third-party permission tools:** Privacy utilities that lock down folders can over-block system paths.
- **Stuck service credentials:** Update services running under wrong credentials fail privileged operations.
- **Disk errors:** File system corruption can manifest as access denied on damaged sectors.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

The automated tool checks service states and common configuration problems that can surface as access errors. It also re-registers update components and verifies that the cryptographic and transfer services have the permissions they need, which clears many 0x80070005 instances without any manual work on your part.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart the laptop.
4. Retry the update and note whether the code persists.

### Fix 2: Temporarily disable third-party antivirus

Isolate the most common external cause quickly before touching permissions.

1. Open your antivirus suite and disable real-time protection until restart.
2. Keep Windows Defender active as the safety net.
3. Run Windows Update and attempt the failing update.
4. If it succeeds, the antivirus was blocking the operation.
5. Re-enable protection and add exclusions for Windows Update paths if the suite allows.

### Fix 3: Reset the Windows Update cache with correct ownership

Clear the cache folders, which also resolves permission drift inside them.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the services with `net start` and reboot.
6. Retry the update with fresh, correctly permissioned folders.

### Fix 4: Verify the update services run correctly

Services running under wrong accounts or stuck states generate access errors.

1. Open services.msc and find Windows Update.
2. Confirm Startup type is Manual and the service can start.
3. Check the Log On tab shows Local System account.
4. Verify Background Intelligent Transfer Service and Cryptographic Services similarly.
5. Restart the laptop and retry.

### Fix 5: Check disk for file system errors

Rule out disk-level corruption masquerading as access denied.

1. Open Command Prompt as administrator.
2. Run `chkdsk C: /f` and approve the scan on next restart.
3. Restart and let the disk check complete fully.
4. After booting, retry the Windows Update.
5. If chkdsk found and fixed errors, the access failures may be resolved.

### Fix 6: Test with a fresh administrator account

A corrupted user profile can break the security context. A new account isolates this cleanly.

1. Go to Settings, Accounts, Other users, and add a new local administrator account.
2. Sign out and sign in to the new account.
3. Run Windows Update from the new account.
4. If updates succeed there, migrate to the new profile.
5. If they fail identically, the problem is system-wide, not profile-specific.

### Fix 7: Repair system files with DISM and SFC

Fix corruption in the security and servicing components as the final repair.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` to 100 percent.
3. Run `sfc /scannow` and wait for verification.
4. Restart the laptop.
5. Retry the update and confirm 0x80070005 is gone.

If you want the fuller DISM picture — what each switch does, how long it really takes, and when to point it at an explicit source — our [DISM RestoreHealth walkthrough](/articles/how-to-run-dism-restore-health-on-windows-11/) covers the pass in detail.

Microsoft's general update guidance is at https://support.microsoft.com/en-us/windows.

### Fix 8: Reset ACLs on the Windows Update folders

When permissions on the update folders themselves are wrong, the installer hits access denied no matter how healthy the rest of the system is. Resetting the access control lists on SoftwareDistribution and its related folders restores the default permissions the servicing stack expects. This is a targeted permission repair, not a system-wide change, so it carries none of the risk of broad permission resets while directly addressing the 0x80070005 cause.

1. Open Command Prompt as administrator.
2. Stop the update services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`.
3. Take ownership of the folder: `takeown /f C:\Windows\SoftwareDistribution /r /d y`.
4. Reset its permissions: `icacls C:\Windows\SoftwareDistribution /reset /t /c /q`.
5. Restart the services with `net start` and reboot the laptop.
6. Retry the update with correctly permissioned folders in place.

## Closing

Error 0x80070005 is a permissions story, not a download story, so the fix is restoring access: quiet the antivirus, reset the cache folders, verify service accounts, check the disk, and repair system files. Work the sequence in order and the access denied wall comes down in most cases at step two or three. Once updates flow again, avoid permission-tweaking utilities that caused the drift in the first place.
