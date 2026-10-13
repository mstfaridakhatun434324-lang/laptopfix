---
title: "How to Fix Windows Update Error 0x80070005 on Windows 10"
slug: how-to-fix-windows-update-error-0x80070005-on-windows-10
date: 2026-09-09
categories: ["windows-update"]
tags: ["0x80070005", "access denied", "windows 10", "update error"]
description: "Windows Update error 0x80070005 (Access Denied) on Windows 10? Here's how to fix the permissions problem blocking your updates."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070005 mean?"
    a: "It is the Windows error code for 'Access Denied.' In the context of Windows Update, it means the update engine tried to read, write, or register a file, folder, or registry key and was refused permission. The update files are fine; the permissions on the system locations they need are not."
  - q: "Can a non-admin account cause 0x80070005?"
    a: "Yes, and it is a common cause. Installing updates requires administrator privileges because the update engine writes to protected system folders and the registry. If your account is a standard user, sign in as an administrator or have one approve the update through User Account Control."
  - q: "Will resetting permissions harm my system?"
    a: "The fixes here reset permissions only on the specific update-related folders and registry keys that Microsoft's own tools target. They do not change permissions on your personal files. Used as directed, the SubInACL-style resets are the same repairs Microsoft support recommends for this error."
  - q: "Why does 0x80070005 keep coming back?"
    a: "Recurrence usually points to a third-party security suite or a system 'optimizer' that re-locks the update folders after every repair, or to disk corruption that keeps damaging permissions. Address the underlying cause — usually the security software — or the error will return with the next Patch Tuesday."
---

Error **0x80070005** is Windows telling you "Access Denied" in its most cryptic form. When it shows up in Windows Update on Windows 10, it means the update engine reached for a file, folder, or registry key it needed and was refused. The update itself is not corrupt and your internet is fine — the permissions on your own system are blocking the install. It is one of the more fixable update errors because the cause is structural, not random: something owns or locks the paths Windows Update needs.

What makes this error confusing is that the denial often comes from your own security software or from permission changes you never made yourself. Windows Update runs as the SYSTEM account, which normally outranks everything — but third-party antivirus, aggressive "privacy" tools, and even corrupted permission inheritance can put up walls that SYSTEM cannot cross. The engine does not get a helpful message explaining who blocked it; it just gets "access denied" and reports the code, leaving you to play detective across folders, registry keys, and security products.

The fixes below target the usual suspects in order: account rights, the specific folders and registry keys involved, the security software that locks them, and finally the component store itself.

## Why this happens

- **Your account lacks administrator rights.** Update installation requires admin privileges; a standard user account gets access-denied errors on protected system paths.
- **Wrong permissions on update folders.** The `SoftwareDistribution`, `Catroot2`, or system32 folders have inherited or broken ACLs that refuse the update service's writes.
- **Registry key ownership is broken.** Keys under `HKEY_LOCAL_MACHINE` that the update engine must write to are owned by the wrong account or have restrictive permissions.
- **Third-party antivirus locks system paths.** Security suites can deny even SYSTEM-level processes access to folders they are "protecting," including update cache locations.
- **Corrupted user profile or missing admin token.** A damaged profile can fail to elevate properly, so the update engine runs without the rights it expects.
- **Disk errors damaging security descriptors.** Bad sectors or filesystem corruption can scramble the permission metadata on update-related files.
- **Group Policy or registry hardening.** Debloating scripts and "privacy" tools sometimes lock down update-related paths so aggressively that Windows Update itself cannot write to them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the update as a true administrator

The simplest cause is the simplest to check.

1. Confirm your account is an administrator: **Settings** > **Accounts** > **Your info** should say "Administrator" under your name.
2. If it says "Standard user," sign in with an administrator account to install updates.
3. Even as an admin, run the check from an elevated context: right-click **Command Prompt**, choose **Run as administrator**, and run `usoclient StartScan` to trigger a privileged scan.

### Fix 2: Take ownership of the update folders

Reset the permissions on the exact folders Windows Update needs.

1. Open an elevated Command Prompt.
2. Run these commands to grant the Administrators group full control of the key update folders:
   ```
   icacls "C:\Windows\SoftwareDistribution" /reset /t /c /q
   icacls "C:\Windows\System32\catroot2" /reset /t /c /q
   ```
3. Restart the update services:
   ```
   net stop wuauserv
   net stop bits
   net start wuauserv
   net start bits
   ```
4. Retry the update. Resetting inherited permissions this way is safe — it restores Microsoft's defaults rather than inventing new ones.

### Fix 3: Temporarily disable third-party security software

Overprotective antivirus is a leading cause of 0x80070005.

1. Open your third-party antivirus or firewall and disable real-time protection temporarily.
2. Run Windows Update and let the pending updates install.
3. Re-enable protection immediately afterward.
4. If the error disappears with protection off, add permanent exclusions for `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2`. Do not leave real-time protection disabled as a "fix."

### Fix 4: Run the Windows Update troubleshooter

Microsoft's troubleshooter checks service registrations and permissions automatically.

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters** > **Windows Update** > **Run the troubleshooter**.
2. Apply every fix it recommends, then restart.
3. The troubleshooter re-registers update DLLs and repairs service permissions that commonly produce access-denied errors.

### Fix 5: Check the drive for permission-scrambling errors

Filesystem damage can corrupt the security descriptors on update files.

1. Open an elevated Command Prompt and run `chkdsk C: /f /r`. Confirm the restart prompt and reboot — the scan runs before Windows loads.
2. After the scan completes and Windows boots, retry the update.
3. If chkdsk reports bad sectors, back up your data promptly; recurring 0x80070005 errors can be an early warning of drive failure.

### Fix 6: Reset the update components completely

A fresh component set with default permissions eliminates accumulated damage.

1. In an elevated Command Prompt, stop the services and rename the cache folders:
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
2. Retry the update. Windows rebuilds the folders with correct default permissions. Our guide to [resetting stuck update components](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) explains what each of these folders does if you want the background. The same access-denied repair applies on newer systems as well — the [Windows 11 version of this 0x80070005 fix](/articles/how-to-fix-windows-update-error-0x80070005-on-windows-11/) covers the differences on a modern install.

### Fix 7: Create a fresh administrator account

If your profile's security token is damaged, no amount of folder repair will help.

1. Open an elevated Command Prompt and run:
   ```
   net user FixAdmin TempPass123 /add
   net localgroup administrators FixAdmin /add
   ```
2. Sign in as FixAdmin, run Windows Update, and install the pending updates.
3. Once updates succeed, you can delete the temporary account. If updates work here but not in your main profile, the profile itself is the problem — [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the profile-repair path from there.

## Closing

Error 0x80070005 is a permissions problem wearing an update-error costume. Work it like one: confirm admin rights, reset the folder permissions, get security software out of the way, and rebuild the update components with clean defaults. The error looks intimidating but it almost never indicates real system damage — it is Windows being denied access to its own update machinery, and restoring that access restores updates. If access-denied errors persist across every update rather than one package, the engine itself likely needs the broader [reset covered in our update component repair guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/).
