---
title: "How to Fix Windows Update Error 0x80070005 on Windows 11"
slug: how-to-fix-windows-update-error-0x80070005-on-windows-11
date: 2026-09-27
categories: ["windows-update"]
tags: ["0x80070005", "access denied", "windows 11", "update error"]
description: "Error 0x80070005 blocking Windows 11 updates? Fix the access-denied permissions issue with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-on-windows-11.webp"
faqs:
  - q: "What causes 0x80070005 on Windows 11 specifically?"
    a: "The same access-denied root causes as on Windows 10, with Windows 11 additions: stricter default permissions on system folders, security software that has not been updated for Windows 11's servicing paths, and debloat scripts that lock down update-related registry keys more aggressively than the system tolerates."
  - q: "Can Windows 11's built-in security cause this error?"
    a: "Rarely, but Controlled Folder Access in Windows Security can block the update engine from writing to protected folders, producing access-denied errors. If you have it enabled, check its blocked history during a failed update — whitelisting the update processes there is safer than disabling the feature."
  - q: "Do I need to edit the registry to fix 0x80070005?"
    a: "Usually not. The folder-permission resets and component resets in this guide resolve the error without registry editing. Registry permission repairs are a deeper step reserved for cases where the standard fixes fail, and they should follow Microsoft's documented procedures rather than random forum advice."
  - q: "Why does the error return after every fix?"
    a: "Something is re-breaking the permissions between repairs — almost always third-party security software re-locking the folders, a scheduled 'optimizer' task, or disk corruption re-damaging the security descriptors. Identify the recurring cause rather than repeating the repair, or the error will outlast your patience."
---

Error **0x80070005** — Access Denied — on Windows 11 means the update engine was refused permission to touch something it needs: a folder, a file, a registry key. Windows 11 did not change the fundamental meaning of this error from Windows 10, but it did tighten default permissions and add new security features like Controlled Folder Access that create new ways to trigger it. The update package is fine; your system's permissions are the problem.

Windows 11's tightened permission model is a deliberate security improvement that has a side effect on servicing. Default ACLs on system folders are stricter, virtualization-based security isolates more of the update process, and features like Controlled Folder Access treat even Microsoft's own installer with suspicion until explicitly told otherwise. Most of the time this machinery is invisible. But when any piece of it — a third-party antivirus that has not kept up with Windows 11's paths, a debloat script that locked down more than it should have, a corrupted inheritance chain — denies the engine something it needs, you get 0x80070005 with no indication of which guard said no.

This guide works the error like the permissions problem it is: verify rights, reset the specific folders involved, remove the software that locks them, and rebuild the components with clean defaults.

## Why this happens

- **Non-administrator account.** Update installation requires admin rights; standard users get access-denied failures.
- **Broken permissions on update folders.** Corrupted ACLs on SoftwareDistribution, Catroot2, or servicing paths refuse the update service.
- **Third-party antivirus locking system paths.** Security suites denying even SYSTEM processes access to "protected" folders.
- **Controlled Folder Access blocking the engine.** Windows Security's ransomware protection intercepting update writes.
- **Registry key ownership problems.** Update-related keys owned by the wrong principal or with restrictive ACLs.
- **Debloat or hardening scripts.** Aggressive privacy tools locking down update paths beyond what the servicing stack tolerates.
- **Disk corruption damaging security descriptors.** Filesystem errors scrambling permission metadata on update files.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm administrator rights

Start with the account.

1. Check **Settings** > **Accounts** > **Your info** — it should say "Administrator" under your name.
2. If you are a standard user, switch to an administrator account for updates.
3. As an admin, trigger a privileged scan to rule out elevation issues: open an elevated Command Prompt and run `usoclient StartScan`.

### Fix 2: Check Controlled Folder Access

Windows 11's own ransomware protection is a new suspect.

1. Open **Windows Security** > **Virus & threat protection** > **Manage ransomware protection**.
2. If **Controlled folder access** is on, click **Block history** and look for blocked update-related processes during your failed update attempts.
3. Click **Allow an app through Controlled folder access** and whitelist the legitimate Windows Update executables — do not disable the feature entirely.

### Fix 3: Reset permissions on the update folders

Restore Microsoft's default ACLs on the paths the engine needs.

1. Open an elevated Command Prompt and run:
   ```
   icacls "C:\Windows\SoftwareDistribution" /reset /t /c /q
   icacls "C:\Windows\System32\catroot2" /reset /t /c /q
   ```
2. Restart the update services:
   ```
   net stop wuauserv
   net stop bits
   net start wuauserv
   net start bits
   ```
3. Retry the update. The `/reset` flag restores inherited default permissions — safe and targeted.

### Fix 4: Temporarily disable third-party security software

Find out if your antivirus is the one denying access.

1. Disable real-time protection in your third-party suite temporarily.
2. Run Windows Update and install the pending updates.
3. Re-enable protection immediately. If the error vanished, add permanent exclusions for `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` rather than disabling protection again next month.

### Fix 5: Run the troubleshooter and repair system files

Cover the automated and structural repairs.

1. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**, and apply all fixes.
2. In an elevated Command Prompt, run `sfc /scannow` to repair protected file permissions and contents.
3. Restart and retry. The troubleshooter re-registers update components whose broken registrations manifest as access errors.

### Fix 6: Reset the update components completely

Rebuild with clean default permissions.

1. In an elevated Command Prompt:
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
2. Retry the update. Fresh folders mean fresh, correct permissions. Our [component reset guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) explains each folder's role.

### Fix 7: Audit for recurring permission-breakers

Stop the cycle if the error keeps returning.

1. Check for scheduled tasks from "optimizer" or "debloat" tools that run at boot or on a schedule — disable them.
2. Run `chkdsk C: /f` to rule out filesystem damage re-corrupting permissions.
3. As a diagnostic, create a fresh admin account (`net user TestAdmin * /add` then add to administrators) and test updates there — success isolates the problem to your profile. For persistent cases, [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the deeper permission-repair procedures.

## Closing

Work systematically rather than frantically, and the error resolves. When 0x80070005 appears alongside updates that will not even start, the root cause is often the update service itself rather than permissions — [repairing the Windows Update service](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) addresses what permission resets cannot, and knowing [which updates installed and when](/articles/how-to-view-installed-kb-updates-in-windows-11-24h2/) helps correlate the failure with a specific package. There is also value in documenting what you changed: note which exclusions you added and which permissions you reset, so that if the error returns in six months you can check whether the same guard re-broke rather than starting the diagnosis from zero. Permissions problems are rarely mysterious on the second occurrence — they are usually the same cause wearing a slightly different error message, and your notes turn a repeat incident into a five-minute fix instead of another afternoon.
