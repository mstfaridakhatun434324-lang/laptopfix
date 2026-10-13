---
title: "Fix Windows Update Error 0x80070005 on an ASUS Laptop"
slug: how-to-fix-windows-update-error-0x80070005-on-asus-laptop
date: 2026-10-06
categories: ["windows-update"]
tags: ["0x80070005", "access denied", "asus laptop", "windows update"]
description: "Error 0x80070005 (Access Denied) on your ASUS laptop? Permissions or security software is blocking updates. Here are 7 fixes to restore access."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-on-asus-laptop.webp"
faqs:
  - q: "What does error 0x80070005 mean on an ASUS laptop?"
    a: "It is Windows' ACCESS_DENIED code: the updater was refused permission to read or write something it needs — a folder, a registry key, or a service. On ASUS machines the usual suspects are half-removed trial antivirus still filtering file access, broken permissions on the update cache folders, or ASUS utilities holding locks. The cure is removing the blocker and restoring correct permissions."
  - q: "Why does 0x80070005 appear even though I am an administrator?"
    a: "Administrator membership and file permissions are separate things. You can hold administrator rights while specific folders or registry keys carry broken access control lists that shut out even elevated processes — typically from a bad cleanup utility, a failed uninstall, or malware damage. The permission resets below repair those ACLs directly, which is what actually controls access."
  - q: "Could Armoury Crate or MyASUS cause error 0x80070005?"
    a: "Indirectly, yes. These utilities rarely break permissions themselves, but they hold locks on update-related files during their own operations, and a locked file produces the same access-denied result as a genuine permission fault. Pausing ASUS services during the update — covered in the steps below — separates a lock conflict (it clears when paused) from real permission damage (which needs the ACL reset)."
  - q: "Is it safe to reset permissions on Windows folders?"
    a: "The resets below touch only the Windows Update cache folders, using Windows' own icacls reset-to-inherited-defaults operation — that restores Microsoft's intended permissions rather than inventing new ones. Your personal files stay untouched, and the System Restore point from Fix 1 gives you a one-click rollback for extra safety."
---

Error 0x80070005 means ACCESS_DENIED — Windows Update reached for something and got refused. On ASUS laptops this appears as updates that download and then fail, or die instantly with the bare code and no explanation. The reflex is to run everything as administrator, yet that rarely helps: the trouble is not your authority but the permissions on the exact folders and keys the updater needs.

ASUS machines carry a few signature triggers. A trial antivirus removed halfway leaves filter drivers silently policing file access, with no console remaining to configure them. ASUS's own utilities lock update folders while they operate. And aggressive "optimizer" tools sometimes strip permissions they should never have touched. The repairs below clear the blockers and restore permissions in a technician's order.

## Why this happens

- **Filter drivers from dead trial antivirus.** Half-removed security software still intercepting file access with no working console.
- **Corrupted folder permissions.** Damaged ACLs on SoftwareDistribution or catroot2 shutting out the update services.
- **ASUS utility file locks.** Armoury Crate, MyASUS, or ASUS Live Update holding files open during their operations.
- **Overeager active antivirus.** Real-time protection flagging the updater's writes as suspicious.
- **A damaged administrator profile.** The admin account itself carrying corrupted privileges.
- **Registry permission damage.** Broken ACLs on update-related registry keys.
- **Malware interference.** Rare, but certain malware deliberately sabotages update permissions so that patches cannot install.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set a restore point and exclude malware

Safety net first, malicious cause second — then the benign repairs.

1. Search **Create a restore point**, open System Protection, and create one named "Before 0x80070005 fix".
2. Run a **Full scan** under **Windows Security > Virus & threat protection**; remove anything found. If malware turned up and got removed, retry Windows Update before continuing — the error may clear by itself.
3. With a clean scan and a restore point secured, proceed: the cause is benign and the repairs below are safe.

### Fix 2: Evict third-party antivirus entirely

The most common benign cause on ASUS laptops — expired preinstalled trials in particular.

1. Under **Settings > Apps > Installed apps**, uninstall any third-party antivirus, expired trials included.
2. Follow with the vendor's official removal tool — ordinary uninstalls routinely leave filter drivers behind.
3. In Device Manager, enable **View > Show hidden devices** and delete leftover AV filter drivers.
4. Reboot, then retry Windows Update under Windows Security alone — if 0x80070005 is gone, the antivirus was the blocker.

### Fix 3: Silence ASUS utilities to test for locks

Distinguish a lock conflict from genuine permission damage — locks vanish when the locker is paused.

1. In `services.msc`, temporarily stop ASUS-related services (Armoury Crate, MyASUS, ASUS Live Update entries) and end their processes in Task Manager.
2. Retry Windows Update. A cleared error means an ASUS utility was holding files — update the ASUS apps to current versions before re-enabling them.
3. An error that persists with ASUS software paused means genuine permission damage — continue to Fix 4.

### Fix 4: Restore the update folders' permissions

Give the updater back Microsoft's intended permissions on the folders it needs.

1. Open an administrator Command Prompt.
2. Seize ownership of the download cache: `takeown /f C:\Windows\SoftwareDistribution /r /d y`.
3. Reset its ACLs to inherited defaults: `icacls C:\Windows\SoftwareDistribution /reset /t /c /q`.
4. Apply the same pair to the catalog store — `takeown /f C:\Windows\System32\catroot2 /r /d y` followed by `icacls C:\Windows\System32\catroot2 /reset /t /c /q`.
5. Restart and retry the update; `/reset` reinstates the inherited defaults the updater expects.

### Fix 5: Rebuild the cache on clean permissions

A freshly rebuilt cache inherits correct permissions by itself — combine the rebuild with the permission repair.

1. From an administrator Command Prompt, stop wuauserv first (`net stop wuauserv`), then BITS (`net stop bits`), then the cryptographic service (`net stop cryptsvc`).
2. Rename the download cache via `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`; rename the catalog store via `ren C:\Windows\System32\catroot2 catroot2.old`. An access-denied here means a process still grips the folder; revisit Fix 2 and Fix 3.
3. Start wuauserv again (`net start wuauserv`), then BITS (`net start bits`), then cryptsvc (`net start cryptsvc`); afterward, check for updates. For the deeper background, our [0x80070002 companion for ASUS](/articles/how-to-fix-windows-update-error-0x80070002-on-asus-laptop/) covers the sibling failure mode.

### Fix 6: Check the account and heal system files

When access is denied even to elevated processes, repair the account context and the system image.

1. Verify your account reads **Administrator** at **Settings > Accounts > Your info**.
2. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and then `sfc /scannow`.
3. Repaired security descriptors in SFC's report likely mark the root cause — restart and retry. For store damage that will not yield, our [DISM RestoreHealth deep-dive](/articles/how-to-run-dism-restore-health-on-windows-11/) covers the ISO-sourced repair.

### Fix 7: Troubleshooter first, in-place upgrade last

Final options when permission damage resists targeted repair.

1. Run **Settings > System > Troubleshoot > Other troubleshooters > Windows Update** and apply everything offered; if the troubleshooter itself will not start, see [our troubleshooter repair notes](/articles/windows-update-troubleshooter-not-working-troubleshooting/).
2. As the last resort, get the Windows 11 ISO ([Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11)), mount the image, launch `setup.exe` with Keep personal files and apps chosen — the in-place upgrade rebuilds every system permission.
3. Afterward, install security software cleanly and remove trials fully instead of letting them expire in place.

## Closing

0x80070005 on an ASUS laptop is an access problem dressed as an update problem: something — usually half-removed antivirus, broken folder permissions, or a locking ASUS utility — is denying the updater its own workspace. Remove the blocker, reset the permissions, rebuild the cache. When updates then fail on missing files rather than denied access, our [0x80070002 companion for ASUS](/articles/how-to-fix-windows-update-error-0x80070002-on-asus-laptop/) covers that sibling code; for keeping ASUS drivers fresh without update conflicts, see our [driver-update best practices](/articles/best-way-to-update-drivers-on-windows-11/).
