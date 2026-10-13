---
title: "Fix Windows Update Error 0x80070005 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070005-in-windows-11-24h2
date: 2026-09-25
categories: ["windows-update"]
tags: ["error 0x80070005", "access denied", "windows 11 24h2"]
description: "Windows Update error 0x80070005 (Access Denied) in Windows 11 24H2? Fix the permissions blocking your updates with this targeted repair guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070005 mean?"
    a: "It is Windows' 'Access Denied' error. In Windows Update it means the updater was blocked from reading or writing something it needs — a cache folder, a registry key, a system file. The cause is permissions: either the permissions are genuinely broken, or security software is denying access."
  - q: "Can antivirus cause 0x80070005?"
    a: "Yes, frequently. Antivirus and anti-ransomware tools protect system folders aggressively, and Windows Update needs to write to exactly those folders. When the security software blocks the write, the updater reports Access Denied. Temporarily disabling protection during the update is the standard diagnostic."
  - q: "Is it safe to change permissions on Windows folders?"
    a: "With care. The fixes below reset permissions using built-in tools rather than hand-editing ACLs, which is the safe approach. Never take ownership of system folders casually or grant Everyone full control — that creates security holes far worse than a failed update."
  - q: "Why does this error affect only some updates?"
    a: "Because different updates touch different locations. A cumulative update writing to protected system areas hits the permission wall, while a Defender definition update writing to its own folder sails through. The pattern of which updates fail hints at which location has the broken permissions."
---

Error 0x80070005 — Access Denied — is Windows Update telling you it knocked on a door and was refused entry. Unlike the "file not found" family of errors, the files here exist; the updater simply is not allowed to touch them. On Windows 11 24H2 this surfaces when permissions on update folders, registry keys, or system files have drifted from their defaults, or when security software stands in the doorway blocking access.

The fix is about restoring legitimate access, not about granting yourself sweeping powers over the system. The repairs below reset the update pipeline's permissions to known-good defaults, neutralize the security software conflicts that mimic permission damage, and repair the ownership issues that cause this error to recur. Compare with the sibling code [0x80070002](/articles/how-to-fix-windows-update-error-0x80070002-in-windows-11-24h2/) (missing files) — different cause, different fix.

What makes 0x80070005 psychologically tricky is that "Access Denied" sounds like you did something wrong — like you lack permission to update your own computer. You do not. The error is about internal permissions between Windows components, not about your authority as the user. The updater runs as SYSTEM, the most privileged account on the machine, and even it can be denied access when ACLs are damaged or security software intervenes. So do not take it personally, and do not try to fix it by making yourself "more admin" — fix the damaged permissions and the overzealous blockers instead.

## Why this happens

- **Broken permissions on update folders:** SoftwareDistribution or catroot2 with ACLs damaged by disk errors, failed updates, or overzealous "privacy" tools.
- **Antivirus/anti-ransomware blocking writes:** Security suites denying the updater access to protected folders — the most common trigger. This is especially prevalent with suites that include "folder shield" or ransomware-protection features, which treat Windows' own update writes as suspicious.
- **Corrupted user account permissions:** A damaged user profile or broken administrator token affecting even elevated operations.
- **Registry permission drift:** Update-related registry keys with incorrect ownership after third-party "optimizers" ran.
- **Disk errors corrupting ACLs:** Filesystem damage scrambling the access control lists on system folders.
- **Group policy restrictions:** Domain or MDM policies limiting what the update service may modify. These are intentional on managed devices — check with IT rather than fighting them.
- **TrustedInstaller ownership conflicts:** System files whose ownership got changed from TrustedInstaller by some utility.
- **Encrypted folders:** Update staging folders accidentally caught up in EFS encryption.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the update as a true administrator

1. Create the failure conditions cleanly: restart the laptop, log in as an administrator account.
2. Open an elevated Terminal (right-click Start → Terminal (Admin)) — confirm the UAC prompt appears.
3. Retry the update from **Settings → Windows Update**. If it succeeds now, the issue was token/elevation related.

### Fix 2: Temporarily disable security software

1. Disable third-party antivirus real-time protection and any anti-ransomware folder protection (including Controlled Folder Access: **Windows Security → Virus & threat protection → Manage ransomware protection**).
2. Retry the update immediately.
3. If it succeeds, add Windows Update's folders to the security software's exclusions before re-enabling, or switch to Defender, which cooperates with the updater. If Controlled Folder Access was the blocker, leave those folders permanently allowed rather than toggling protection off every Patch Tuesday.

### Fix 3: Reset update folder permissions via cache rebuild

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename (do not delete) `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
3. Restart the services. Windows recreates both folders with correct default permissions — this fixes ACL damage without hand-editing anything.
4. Reboot and retry the update.

### Fix 4: Take ownership repair with system tools

1. Elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth` — this also repairs permission/ownership damage in the component store.
2. Then `sfc /scannow` to verify protected system files and their permissions.
3. Reboot and retry. These built-in tools are the safe way to fix ownership drift. Never "fix" ownership by taking personal ownership of system files — that replaces a repairable problem with a security vulnerability.

### Fix 5: Check the disk for ACL-corrupting errors

1. Elevated Command Prompt: `chkdsk C: /f` — schedule at reboot if prompted, then restart.
2. After chkdsk completes, retry the update.
3. Filesystem corruption is the stealth cause when 0x80070005 appears suddenly on a previously healthy system. If chkdsk found and fixed errors, the permissions were likely collateral damage — the resets above then stick permanently.

### Fix 6: Test with a new administrator account

1. **Settings → Accounts → Other users → Add account** → create a local administrator.
2. Log in as the new account and retry the update.
3. Success here means your main profile's permissions are damaged — migrate to the new profile rather than fighting the old one's ACLs.

### Fix 7: In-place repair for systemic permission damage

1. If 0x80070005 persists across accounts, mount the 24H2 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and run an in-place repair keeping files and apps.
2. The repair reinstalls Windows' permission structures to factory defaults.
3. Afterward, avoid registry cleaners and "permission fixer" utilities — they are a leading cause of this exact error. Permission errors sometimes travel with path errors, so if 0x80070003 appears alongside, the [0x80070003 fix guide](/articles/how-to-fix-windows-update-error-0x80070003-in-windows-11-24h2/) covers that sibling code.

## Closing

0x80070005 is a permissions problem, and permissions problems yield to systematic resets — not to granting Everyone full control of System32. The cache rebuild plus DISM/SFC resolves most cases by restoring defaults the safe way, and the antivirus check catches the mimic. Once updates flow again, leave system permissions alone: the utilities that promise to "optimize" them are the most reliable way to end up back here. Your permissions were fine before something broke them; the goal is restoration, not reinvention. Write down what fixed it — permission errors have a habit of recurring after the same cleaner runs again.
