---
title: "How to Fix Error 0x80070005 on Windows 10"
slug: how-to-fix-error-0x80070005-on-windows-10
date: 2026-10-06
categories: ["windows-errors"]
tags: ["error-0x80070005", "windows-10", "access-denied"]
description: "Error 0x80070005 access denied on Windows 10? Fix the permission and service issues behind it with these steps."
thumbnail: "/images/thumbs/how-to-fix-error-0x80070005-on-windows-10.webp"
faqs:
  - q: "What does error 0x80070005 mean?"
    a: "It means 'access denied' — Windows or an app tried to read or write something and lacked permission. It appears in Windows Update, Microsoft Store, app installs, and System Restore, and the fix depends on where you see it."
  - q: "Why does Windows Update fail with access denied?"
    a: "Usually because the update services lack proper permissions on their folders, a security product is blocking file writes, or the user account's permissions are damaged. Resetting the update components and checking permissions fixes most cases."
  - q: "Can I just run everything as administrator to avoid this?"
    a: "Running installers as administrator helps for app installs, but it won't fix systemic permission damage or service misconfiguration. Use it as a workaround, not the fix — repair the underlying permissions so normal operation works."
  - q: "Is 0x80070005 caused by malware?"
    a: "It can be — malware sometimes strips permissions to protect itself. If the error appeared suddenly alongside other weird behavior, run a full Windows Security scan while working through the fixes."
---
# How to Fix Error 0x80070005 on Windows 10

**Error 0x80070005** means "access denied," and it shows up in the most annoying places: Windows Update refusing to install, the Microsoft Store failing downloads, apps that won't install, and System Restore erroring out. The code is the same everywhere, but the right fix depends on where you're seeing it.

This guide covers the most common scenarios in order: update failures first, then Store and app installs, then the deeper permission repairs. Before starting, note exactly where you see the error — the dialog title or the app that's failing — because that determines which fix applies to you, and the wrong fix wastes your time.

If your error code is different, our [error 0x80070057 fix](/articles/error-code-0x80070057-fix/) covers the parameter-is-incorrect sibling of this error.

## Why this happens

- **Broken permissions on system folders:** The Windows Update or Store cache folders have wrong ownership or ACLs.
- **Disabled or misconfigured services:** Update and installer services running under the wrong account or not running at all.
- **Antivirus blocking writes:** Security software denying legitimate system processes access to their own files.
- **Corrupted user account permissions:** The profile's security descriptors damaged by disk errors or bad migrations.
- **Full or failing drive:** Writes fail when there's no space, and Windows sometimes reports it as access denied.
- **Malware:** Malicious software stripping permissions to protect itself or breaking the security subsystem.

## How to fix it

Work through these in order, starting with the scenario that matches yours.

### Fix 1: Reset Windows Update components (update failures)

When 0x80070005 blocks Windows Update, the cache permissions are usually the problem.

1. Open an **admin Command Prompt**.
2. Stop the services:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
3. Rename the cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services with matching `net start` commands.
5. Check for updates. Fresh folders get correct permissions automatically.
6. If the error persists, also verify the **Windows Update** and **BITS** services are running under their proper accounts in `services.msc` — a service running as the wrong user produces access-denied errors that cache resets can't fix.

### Fix 2: Run the Windows Update troubleshooter

The automated tool fixes service accounts and permissions Windows Update depends on.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply its fixes.
3. Restart and retry the update.
4. If it reports it couldn't fix everything, continue — the manual fixes below go further. For Store-specific failures, our [unexpected store exception guide](/articles/unexpected-store-exception-windows-11-fix/) covers that side.

### Fix 3: Take ownership of the problem folders (Store and app installs)

When the Store or installers hit access denied, the app repository permissions are usually damaged.

1. Press **Win + R**, type `wsreset.exe`, and press **Enter** — this clears the Store cache without touching your apps.
2. If installs still fail, open an admin Command Prompt and reset the Store package permissions:
   `icacls "C:\Program Files\WindowsApps" /reset /t /c /q`
   This can take several minutes; let it finish.
3. Never take personal ownership of `WindowsApps` or delete from it manually — the icacls reset restores Microsoft's intended permissions, which is what you want.
4. Re-register the Store: in admin PowerShell, run
   `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
5. Retry the failing install.

### Fix 4: Check your account and UAC

A damaged admin token or disabled UAC breaks installers in subtle ways.

1. Go to **Settings > Accounts > Your info** and confirm your account shows **Administrator**.
2. If you're on a standard account, switch to an admin account for installs — or have an admin approve the UAC prompt.
3. Check UAC: search **Change User Account Control settings** and set it to the default level (second from top). Fully disabling UAC breaks Store apps and some installers.
4. Try right-clicking the failing installer and choosing **Run as administrator** as a test — if it works, permissions on your normal token are the issue.

### Fix 5: Temporarily disable third-party antivirus

Security products denying system writes is a real and common trigger.

1. Disable real-time protection in your antivirus temporarily.
2. Retry the update or install immediately.
3. Re-enable protection right away.
4. If this fixed it, update the antivirus to its latest version — vendors fix these false blocks regularly — and consider adding Windows Update and the Store to its exclusions if it documents how.

### Fix 6: Run a full malware scan

Since malware causes permission damage, rule it out before deeper repairs.

1. Open **Windows Security > Virus & threat protection** and run a **Full scan**.
2. Follow with a **Microsoft Defender Offline scan** under **Scan options**.
3. Remove all threats, restart, and retry the failing operation.
4. If malware damaged system permissions broadly, continue to Fix 7 — cleaning the malware doesn't automatically repair what it broke.

### Fix 7: Repair system files and reset permissions

For widespread permission damage, repair the OS itself.

1. Open an admin Command Prompt.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Check disk space — ensure at least 10–15 GB free on C:, since full drives produce misleading access-denied errors.
4. Run `chkdsk C: /f` to fix file-system corruption that may underlie the permission errors.
5. As a final measure, create a fresh administrator account and test there — if the new account works, your old profile's permissions are damaged beyond practical repair and migrating is the answer. Microsoft documents account and permission troubleshooting on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Error 0x80070005 is Windows saying "I'm not allowed to do that" — so the fix is always about restoring the right permissions to the right places: the update cache, the Store repository, the service accounts, or your user profile. Work from the specific scenario outward, and resist the urge to just disable security features to make the error go away. Proper permissions fixed once stay fixed, and your updates, Store, and installers will work normally again.
