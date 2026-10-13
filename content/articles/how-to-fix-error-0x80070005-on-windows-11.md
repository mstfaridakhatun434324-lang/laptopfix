---
title: "How to Fix Windows 11 Error 0x80070005 (Access Denied)"
slug: how-to-fix-error-0x80070005-on-windows-11
date: 2026-09-12
categories: ["windows-errors"]
tags: ["0x80070005", "access denied", "permissions"]
description: "Error 0x80070005 means Access Denied during updates, installs, or activation. Fix broken permissions and get Windows 11 working again."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070005-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070005 mean?"
    a: "It is Windows' generic Access Denied error: a program or system process tried to read, write, or modify something it did not have permission for. It appears during Windows updates, Microsoft Store installs, app installations, and Windows activation. The trigger varies — corrupted permissions on system folders, a misbehaving antivirus blocking access, or a broken user account — so the fix depends on where you see the error."
  - q: "Can antivirus cause 0x80070005?"
    a: "Yes, frequently. Third-party antivirus software can block Windows Update or the Store from writing files, producing Access Denied errors. If the error started after installing or updating security software, temporarily disable its real-time protection and retry. If that works, add the affected program to the antivirus exclusions or switch to Microsoft Defender."
  - q: "Is 0x80070005 a virus?"
    a: "No, it is a legitimate Windows error code, not malware. However, malware can damage file permissions in ways that produce this error, so if it appears alongside other strange behavior — new unknown programs, browser redirects, disabled security settings — run a full scan with Microsoft Defender or Malwarebytes before doing permission repairs."
  - q: "How do I fix 0x80070005 during Windows Update?"
    a: "Start with the Windows Update troubleshooter, then reset the SoftwareDistribution cache, then check that you have administrator rights and that no antivirus is blocking the update. If it persists, run SFC and DISM to repair system files, and use the SubInACL-free manual method of resetting folder permissions via an admin Command Prompt with icacls on the affected directories."
---

Error 0x80070005 is Windows saying "Access Denied" in its least helpful way. It pops up in the middle of Windows updates, Store app installs, program setups, and even activation — always with the same unhelpful code and rarely with an explanation of what was denied. The underlying story is permissions: something tried to touch a file, folder, or registry key it was not allowed to touch.

Because the same code appears in so many contexts, the fix depends on where you hit it. The steps below cover the common scenarios in the order you should try them, starting with the quick checks that resolve most cases and moving to permission repairs for the stubborn ones.

## Why this happens

- **Corrupted file or folder permissions.** System directories end up with wrong ownership or ACLs after bad updates or migrations.
- **Antivirus blocking legitimate operations.** Third-party security tools deny file access to updaters and installers.
- **Non-administrator account.** Standard users hit Access Denied on operations that need elevation.
- **Corrupted user profile.** A damaged profile carries broken permissions everywhere.
- **Windows Update component corruption.** Damaged update services fail their own permission checks.
- **Malware damage.** Infections sometimes rewrite permissions to protect themselves, breaking legitimate access.

## How to fix it

Work through these in order, noting the driver name from the blue screen if shown.

### Fix 1: Confirm you are an administrator and retry elevated

The simplest cause is the most overlooked.

1. Go to **Settings > Accounts > Your info** and check that it says **Administrator** under your name.
2. If it says Standard, sign into an admin account or have one promote yours via **Settings > Accounts > Other users**.
3. For installers, right-click the setup file and choose **Run as administrator**.
4. Retry the operation that failed.

### Fix 2: Run the Windows Update troubleshooter

For update-related 0x80070005, start here.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart and retry the update.
4. If the error appears in the Microsoft Store instead, run the **Windows Store Apps** troubleshooter from the same page.

### Fix 3: Temporarily disable third-party antivirus

Security software is a leading cause of false Access Denied errors.

1. Open your antivirus and turn off real-time protection temporarily.
2. Retry the update, install, or activation that failed.
3. If it succeeds, open the antivirus exclusions and add the affected app or the Windows Update folders.
4. Re-enable protection right away.
5. Consider whether Microsoft Defender alone meets your needs — it never conflicts with Windows' own operations.

### Fix 4: Reset the Windows Update components

Corrupted update services can deny themselves access.

1. Open **Terminal (Admin)** from `Win + X`.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptSvc`.
3. Rename the cache: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptSvc`.
5. Retry the update from **Settings > Windows Update**.

### Fix 5: Repair system files with SFC and DISM

Damaged system files produce phantom permission errors.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow`.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and retry.

### Fix 6: Reset permissions on the affected folders

When a specific folder has broken ACLs, fix them directly.

1. Open **Terminal (Admin)**.
2. For Store app issues, reset the WindowsApps-adjacent permissions carefully — safer: run `wsreset.exe` from `Win + R` to clear the Store cache first.
3. For general permission corruption, Microsoft's documented approach uses `icacls`: e.g. `icacls "C:\Program Files\WindowsApps" /reset /t /c /q` — run only on the folder actually causing the error, never blindly on the whole drive.
4. If ownership is the issue, take ownership first via the folder's **Properties > Security > Advanced > Change** owner to **Administrators**, then re-run the operation.
5. Microsoft's official guidance for permission-related update failures is on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 7: Create a fresh administrator account

A corrupted profile carries broken permissions that repairs cannot always fix.

1. Go to **Settings > Accounts > Other users > Add account**.
2. Choose **I don't have this person's sign-in information > Add a user without a Microsoft account**.
3. Create the account, then change it to **Administrator**.
4. Sign into the new account and retry the failing operation.
5. If it works there, migrate your files from the old profile.

A related install-blocking error with its own walkthrough is [error 0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/), and the Windows 11 24H2-specific variant of this code is covered in our [0x80070005 in 24H2 guide](/articles/how-to-fix-error-0x80070005-in-windows-11-24h2/).

### Fix 8: Use the built-in Administrator account for stubborn cases

Some permission corruption is tied to the user profile itself; the hidden Administrator account sidesteps it entirely.

1. Open **Terminal (Admin)** and run `net user administrator /active:yes`.
2. Sign out and sign into the **Administrator** account that now appears on the login screen.
3. Retry the update, install, or activation that was failing with 0x80070005.
4. If it succeeds there, your main profile has permission damage — migrate to a fresh profile rather than fighting the old one.
5. When finished, disable the hidden account again for security: `net user administrator /active:no`.

## Closing

Error 0x80070005 is almost never as serious as it looks — it is a permissions dispute, not system damage. Check admin rights, get the antivirus out of the way, reset the update components, and repair system files, and the Access Denied wall comes down in the large majority of cases. When it does not, a fresh admin account sidesteps profile-level corruption cleanly. Note where the error appears before you start, since the context tells you which of these fixes to try first — and resist the urge to take ownership of entire system folders, which creates bigger permission problems than it solves. When in doubt, fix the specific folder, not the whole drive. Broad permission changes are how small access problems turn into unbootable systems.
