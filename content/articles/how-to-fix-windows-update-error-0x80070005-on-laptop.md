---
title: "How to Fix Windows Update Error 0x80070005 on a Laptop"
slug: "how-to-fix-windows-update-error-0x80070005-on-laptop"
date: "2026-10-10"
categories: ["windows-update"]
tags: ["0x80070005", "access-denied", "windows-update", "permissions"]
description: "Error 0x80070005 is an 'access denied' failure in Windows Update. Fix the permissions, services, and account issues behind it with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-on-laptop.webp"
faqs:
  - q: "What does access denied mean during a Windows update?"
    a: "It means the update engine tried to read, write, or modify a file, folder, or registry key and Windows refused permission. This is not about your user account lacking admin rights in the usual sense — it is about the system-level permissions on update components being wrong. Corrupted permissions on the SoftwareDistribution folder or misconfigured service accounts are the typical culprits."
  - q: "Can antivirus software cause error 0x80070005?"
    a: "Yes, frequently. Real-time protection can lock files the update engine needs to replace, producing access denied errors when the installer tries to overwrite them. Ransomware protection features that guard folders are another common source. Temporarily pausing protection during the update is a legitimate diagnostic step that resolves many cases of this error."
  - q: "Should I take ownership of Windows folders to fix this?"
    a: "No — manually changing ownership of system folders is risky and rarely the right fix for 0x80070005. The correct approach is to reset the permissions on the specific update-related folders using supported methods, or to let the component reset rebuild them with correct permissions. Taking ownership of Windows system directories can destabilize the OS and complicate future updates."
  - q: "Does this error mean my user account is corrupted?"
    a: "Not necessarily, but account issues can contribute. If your Microsoft account has sync problems or your local profile permissions are damaged, update operations that touch user-specific locations can fail. Testing with a fresh administrator account is a useful diagnostic: if updates work there, the problem is profile-specific rather than system-wide."
---

Error 0x80070005 translates to "access denied," and in the Windows Update world it means the update engine was blocked from touching something it needed. Unlike the missing-file errors, everything is present — Windows just will not let the updater at it. The usual suspects are mangled folder permissions, overprotective security software, and service accounts running with the wrong identity.

Permission problems sound scary, but the fixes are methodical: identify what is blocking access, restore correct permissions on the update folders, and remove the interference. Resist the urge to seize ownership of system directories — the supported repairs below do the job safely.

Access denied errors provoke a particular anxiety — the machine seems to be refusing its own update — but the reality is more mundane. The Windows Update engine operates through specific system folders and service accounts, and when the permissions on those folders get mangled, the engine is locked out of its own workspace. Nothing is missing and nothing is broken; the doors are just locked from the inside. The fixes below re-cut the keys: restore correct permissions by rebuilding the update folders, remove the software standing in the doorway, and verify the services are running under the right identity.

## Why this happens

- **Wrong permissions on update folders:** The SoftwareDistribution and catroot2 folders end up with permissions that block the update service.
- **Antivirus file locks:** Real-time scanners lock files the installer needs to replace, causing access denied mid-install.
- **Ransomware protection guarding folders:** Controlled folder access can block the update engine from writing where it must.
- **Corrupted service account configuration:** The update services must run under the correct built-in accounts; misconfiguration breaks their access.
- **Third-party "privacy" tools:** Tools that aggressively lock down system areas often break update permissions as a side effect.
- **Damaged user profile:** Profile permission corruption can fail updates that touch user-specific locations.
- **Pending file operations:** Files locked by a previous incomplete operation deny access to the next attempt.
- **Disk errors:** File system corruption can manifest as access denied when the real problem is unreadable structures.

## How to fix it

Work through these in order — diagnose first, then act.

A warning worth repeating: do not ‘fix’ this by taking ownership of Windows system folders or loosening permissions across the board. That trades a contained update problem for a system-wide security and stability risk. Every fix below works within the supported permission model — rebuild, reset, and verify, never seize.

### Fix 1: Run the update as a proper administrator

Eliminate the simple account-level causes first.

1. Make sure you are signed in with an administrator account, not a standard user.
2. Open Settings and check for updates normally — most update operations elevate automatically.
3. If you use a Microsoft account, confirm it is syncing without errors in Accounts settings.
4. Retry the update after confirming your account status.

### Fix 2: Temporarily disable antivirus and ransomware protection

This is the highest-yield step for access denied errors.

1. Open your third-party antivirus and pause real-time protection.
2. Open Windows Security, Virus & threat protection, Ransomware protection, and temporarily turn off Controlled folder access.
3. Retry the Windows update while protections are paused.
4. Re-enable everything immediately after the update completes or fails.

### Fix 3: Reset the Windows Update components

Rebuilding the update folders restores their correct default permissions.

1. Open Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Reboot and retry the update — the rebuilt folders get correct permissions automatically.

### Fix 4: Verify the update services run under correct accounts

Services running under the wrong identity lose access to everything.

1. Open services.msc and double-click the Windows Update service.
2. On the Log On tab, confirm it is set to Local System account.
3. Check the Background Intelligent Transfer Service the same way.
4. If either was changed, restore Local System, restart the service, and retry.

### Fix 5: Run the Windows Update troubleshooter

The automated tool can repair several permission-related update faults.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart the laptop afterward.
4. Test Windows Update again.
5. If the troubleshooter itself misbehaves, our guide on [fixing the Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working/) covers that scenario.

### Fix 6: Repair system files

Corruption in the servicing stack can produce spurious access denied errors.

1. In an admin Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`.
3. Restart the laptop after both complete.
4. Retry the update.

### Fix 7: Test with a fresh administrator account

Isolate whether the problem lives in your user profile.

1. Create a new local administrator account in Settings, Accounts, Other users.
2. Sign in as the new account and run Windows Update there.
3. If updates succeed, your original profile has permission damage — consider migrating to the new profile.
4. If they fail identically, the problem is system-wide; continue with the remaining fixes.

### Fix 8: Check the disk and install manually

Cover the last two angles: file system damage and bypassing the broken path.

1. Run `chkdsk C: /f` in an admin Command Prompt, schedule it, and restart.
2. After the scan, note the KB number of the failing update.
3. Download the .msu from the Microsoft Update Catalog and install it directly.
4. The standalone installer sometimes succeeds where the service-based path hits permission walls.
5. For the full manual process, see [how to manually install Windows updates](/articles/how-to-manually-install-windows-update-on-windows-11/).

The repeat offender for 0x80070005 is almost always security software with folder-guarding features — ransomware protection, ‘secure folders,’ or hardened antivirus profiles that treat the update engine as a suspicious process modifying system areas. If the error returns, check those features first and add proper exclusions for the Windows Update service rather than disabling protection wholesale. Correctly configured, security software and updates coexist peacefully; the conflict only arises when the guard does not recognize the updater. For the service-side companion to this error, our guide on [fixing the Windows Update service not running](/articles/how-to-fix-windows-update-service-not-running-reddit/) covers the account and startup angles.

## Closing

Access denied errors feel like Windows is fighting you, but they are usually just wrong permissions on update folders or an overprotective security tool standing in the way. Reset the components, pause the interference, verify the service accounts — and leave the ownership of system folders exactly where it is.
