---
title: "How to Fix Error 0x80070005 (Access Denied) in Windows 11 24H2"
slug: how-to-fix-error-0x80070005-in-windows-11-24h2
date: 2026-09-25
categories: ["windows-errors"]
tags: ["0x80070005", "access denied", "permissions", "windows update"]
description: "Fix error 0x80070005 in Windows 11 24H2 — take ownership of blocked files, repair permissions, fix the Store, and clear Windows Update failures."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070005-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070005 mean?"
    a: "Access denied. Windows (or an app, or Windows Update) tried to read, write, or execute something and the permissions system said no. The file might be owned by another account, locked by antivirus, or have corrupted ACLs — the fixes below address each variant."
  - q: "Is 0x80070005 a virus?"
    a: "No, it is a permissions error, not malware. That said, malware sometimes triggers it by locking files, so a Defender scan is a reasonable step if the error appeared suddenly alongside other strange behavior."
  - q: "Can I just take ownership of everything to fix it?"
    a: "No — blanket ownership changes on system folders break Windows worse than the original error. Only adjust permissions on the specific file, folder, or registry key involved, and prefer the targeted fixes below over sweeping changes."
  - q: "Why does 0x80070005 appear in the Microsoft Store?"
    a: "The Store hits it when it cannot access its own cache or license files — usually after an update changes permissions. Resetting the Store (wsreset.exe plus the Settings reset) resolves the Store-specific variant; see our [Microsoft Store errors guide](/articles/how-to-fix-microsoft-store-error-on-acer-laptop/) for that path."
---

**Error 0x80070005** — "Access is denied" — is Windows' permissions system refusing a request. It shows up in Windows Update, the Microsoft Store, app installations, System Restore, and even File Explorer, which makes it confusing: the same code, very different problems. The unifying thread is always permissions — something trying to touch something it is not allowed to touch.

This guide covers the 24H2-era variants systematically: the quick permission repairs, the update-specific fixes, and the Store variant. The key discipline: fix the *specific* permission problem, never carpet-bomb your system folders with ownership changes. For the "file not found" sibling error, see our [0x80070002 guide](/articles/how-to-fix-error-0x80070002-in-windows-11-24h2/).

It helps to know how Windows permissions actually work, because the error message gives you no clue. Every file, folder, and registry key has an access control list (ACL) — a list of which accounts may do what — plus an owner. Error 0x80070005 fires when the requesting account is not on that list with the needed permission. The list gets damaged most often by updates that replace files without preserving their ACLs, by disk corruption flipping bits in the security descriptors, or by one program changing permissions that another program depends on. The fixes below are all variations on one theme: find the object with the wrong list, and put the right list back.

## Why this happens

- **Corrupted ACLs after an update.** 24H2 updates occasionally leave files or registry keys with broken permission entries.
- **Antivirus locking files.** Third-party AV can deny even SYSTEM access to files it is scanning or quarantining.
- **Wrong ownership.** Files created under a different user account (or a previous Windows installation) may not grant your current account access.
- **Store cache permission drift.** The Microsoft Store's cache folder loses its expected permissions, blocking the Store from itself.
- **Windows Update service account issues.** The update engine runs as SYSTEM; if system folders' permissions are damaged, updates fail with 0x80070005.
- **Ransomware protection blocking legitimate apps.** Controlled Folder Access sometimes blocks installers and updaters it does not recognize.

## How to fix it

Work through these in order — identify your scenario first, then apply the matching fix.

### Fix 1: Run as administrator (the 10-second check)

1. If the error appears when installing or running a program, right-click it and choose **Run as administrator**.
2. If that works, the issue is elevation, not corruption — check the program's compatibility settings or install it for all users. Some older installers need permanent elevation: right-click the executable, choose **Properties > Compatibility**, and check **Run this program as an administrator**.
3. For Windows Update errors, this does not apply (Update already runs as SYSTEM) — skip to Fix 3.

### Fix 2: Fix permissions on the specific file or folder

1. Identify the exact path from the error message or log.
2. Right-click it, choose **Properties > Security > Advanced**.
3. Click **Change** next to the owner, enter your username (or **Administrators**), and check **Replace owner on subcontainers and objects**.
4. Back in Advanced Security, click **Add**, select your account, grant **Full control**, and check **Replace all child object permission entries**.
5. Click **OK** through everything and retry. **Only do this for the specific path involved** — never for `C:\Windows` wholesale.

### Fix 3: Reset Windows Update components

For 0x80070005 during Windows Update:

1. Open **Terminal (Admin)** with **Win + X**.
2. Run:
   - `net stop wuauserv`, `net stop bits`, `net stop cryptSvc`
   - `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   - `ren C:\Windows\System32\catroot2 catroot2.old`
   - `net start wuauserv`, `net start bits`, `net start cryptSvc`
3. Retry the update at **Settings > Windows Update**.
4. If it still fails, run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` — damaged servicing-stack permissions are a known 24H2 issue, documented on Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 4: Reset the Microsoft Store

For the Store variant of 0x80070005:

1. Press **Win + R**, type `wsreset.exe`, and press Enter.
2. Go to **Settings > Apps > Installed apps > Microsoft Store > ... > Advanced options** and click **Repair**, then **Reset** if needed.
3. Sign back into the Store and retry. The reset restores the Store's folder permissions to their expected state.

### Fix 5: Check Controlled Folder Access and antivirus

1. Open **Windows Security > Virus & threat protection > Ransomware protection**.
2. If **Controlled folder access** is on and blocking your app or installer, either turn it off or click **Allow an app through Controlled folder access** and add the blocked program.
3. If you run third-party antivirus, temporarily disable it and retry — AV file locks are a classic 0x80070005 source. Re-enable it immediately after the test.

### Fix 6: Use SubInACL-style reset via command line (targeted)

For stubborn registry or folder permission corruption, reset to defaults on the specific branch:

1. In an admin terminal, for a folder: `icacls "C:\path\to\folder" /reset /t /c /q`
2. This restores inherited permissions — safer than manual ownership surgery.
3. **Never** run `/reset` on `C:\Windows`, `C:\Program Files`, or the drive root. Target only the problem path.
4. For registry keys: open `regedit`, navigate to the key, right-click **Permissions > Advanced**, and restore inheritance from the parent.

### Fix 7: System Restore or in-place repair

1. If the error started after a specific change, use **System Restore** (**System Properties > System Protection > System Restore**) to roll back. Your files are unaffected.
2. If permissions are damaged system-wide, do an in-place repair: download the 24H2 ISO from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run **setup.exe**, and choose **Keep personal files and apps**. This reinstalls Windows' default ACLs cleanly.

## Closing

**0x80070005** is always a permissions story — the trick is finding *which* permission, on *what* object, rather than flailing at the whole system. Run elevated first, fix the specific path second, reset the affected subsystem (Update, Store) third, and check your security software throughout. Resist the urge to take ownership of all of Windows; precision beats force with access-denied errors every time. When the access-denied error is coming specifically from Windows Update rather than files or the Store, our [Windows Update 0x80070005 guide for 24H2](/articles/how-to-fix-windows-update-error-0x80070005-in-windows-11-24h2/) goes deeper on that branch.
