---
title: "Fix Windows Update Error 0x80070005 on an Acer Laptop"
slug: how-to-fix-windows-update-error-0x80070005-on-acer-laptop
date: 2026-09-26
categories: ["windows-update"]
tags: ["0x80070005", "access denied", "acer laptop", "windows update"]
description: "Error 0x80070005 (Access Denied) blocking updates on your Acer laptop? It is a permissions problem. Here are 7 fixes to restore update access."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-on-acer-laptop.webp"
faqs:
  - q: "What does Windows Update error 0x80070005 mean?"
    a: "It's the standard Windows ACCESS_DENIED code: the update process tried to read or write a file, folder, or registry key and was refused permission. On Acer laptops the usual triggers are mangled permissions on the SoftwareDistribution folder, an overzealous antivirus blocking the updater, or a user account with damaged administrator rights. The fix is restoring correct permissions and removing the blocker."
  - q: "Is 0x80070005 caused by a virus?"
    a: "Rarely, though one scan is worth it. Some malware deliberately wrecks update permissions to stop security patches from installing — a known persistence trick. Far more common are benign causes: third-party antivirus overreach, mangled folder permissions from a bad cleanup tool, or registry damage. Run a full Windows Security scan to rule malware out, then proceed with the permission repairs below."
  - q: "Why does this error appear on Acer laptops specifically?"
    a: "The error isn't Acer-specific, but Acer machines meet it often because Acer Care Center and Acer's preinstalled security trials — which many users never fully remove — interfere with update file access. Partially uninstalled trial antivirus is a classic trigger: its leftover drivers still filter file access while its management console is gone, so nothing can whitelist the updater."
  - q: "Will fixing permissions risk my files?"
    a: "The permission repairs below target only Windows Update's own folders and registry keys — SoftwareDistribution, catroot2, and the update service registrations. Your personal files, documents, and programs stay untouched. The registry edits are confined to update-related keys, and the System Restore point in Fix 1 gives you a rollback if anything unexpected happens."
---

Error 0x80070005 is Windows Update running into a locked door: ACCESS_DENIED. The updater tries to write a downloaded file, read a registry key, or start a service, and Windows refuses. On Acer laptops this frequently follows a half-removed trial antivirus, an aggressive system "optimizer," or Acer Care Center's own file operations — anything that leaves update-related folders with broken permissions.

The key insight is that 0x80070005 is a permissions problem, not a download problem. The update files are usually fine; the updater simply can't reach the locations it needs. That's why retrying never helps and why the fixes concentrate on ownership, permissions, and removing whatever stands in the updater's way. Take them in order — most cases resolve by Fix 3 or Fix 4.

## Why this happens

- **Mangled permissions on update folders.** The SoftwareDistribution or catroot2 folder has ownership or ACLs that shut out the update services.
- **Leftover trial antivirus drivers.** Half-uninstalled security software still filters file access with no console left to configure it.
- **Overactive real-time antivirus.** Active third-party AV blocking the updater's file writes as they happen.
- **A damaged administrator account.** The administrator account itself has broken rights, so even elevated processes get denied.
- **Registry permission damage.** Update-related registry keys with broken ACLs block the updater's configuration reads.
- **Acer Care Center conflicts.** Acer's utility locking update folders during its own maintenance operations.
- **Malware interference.** Rare, but some malware deliberately breaks update permissions to block patching.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set a restore point and scan for malware

Before touching permissions, rule out the malicious cause and give yourself a safety net.

1. Search for **Create a restore point**, open it, and create a restore point named "Before update fix" — permission changes are reversible, but a restore point makes undoing trivial.
2. Open **Windows Security, then Virus & threat protection**, and run a **Full scan**. Remove anything it finds and restart.
3. If the scan catches malware that targets updates, the 0x80070005 may vanish on its own after removal — retry Windows Update before continuing.
4. With a clean scan, proceed: the cause is benign permission damage, and the fixes below are safe.

### Fix 2: Remove or fully neutralize third-party antivirus

The most common benign cause. Trial AV leftovers on Acer laptops are notorious for this.

1. Open **Settings, then Apps, then Installed apps**, and look for any third-party antivirus — including expired trials that shipped with the Acer.
2. Uninstall it properly through Settings (not by deleting folders). For stubborn ones, use the vendor's official removal tool — most AV vendors publish one.
3. Check Device Manager's **View, then Show hidden devices**, for leftover AV filter drivers and uninstall those too.
4. Restart and retry Windows Update with only Windows Security active. If 0x80070005 clears, the AV was the blocker — keep Windows Security in charge or reinstall a clean copy of your preferred AV.

### Fix 3: Restore permissions on the update folders

Fix the ownership and access rights on the folders the updater needs.

1. Open Command Prompt as administrator.
2. Take ownership and reset ACLs on the cache: run `takeown /f C:\Windows\SoftwareDistribution /r /d y` then `icacls C:\Windows\SoftwareDistribution /reset /t /c /q`.
3. Repeat for the catroot2 folder: `takeown /f C:\Windows\System32\catroot2 /r /d y` then `icacls C:\Windows\System32\catroot2 /reset /t /c /q`.
4. Restart and retry the update. Correct permissions let the updater read and write freely again.

### Fix 4: Rebuild the update cache with correct permissions

Pair the cache rebuild with the permission fix — a fresh cache inherits correct permissions automatically.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`. If the rename is denied, some process still holds the folder — look for Acer Care Center or AV leftovers in Task Manager.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Check for updates. The rebuilt folders get fresh, correct permissions from the system.

### Fix 5: Repair the administrator account and system files

If access is denied even to elevated processes, the account or the system files themselves need repair.

1. Open **Settings, then Accounts, then Your info**, and confirm your account shows **Administrator**. If not, enable the built-in administrator: in an elevated Command Prompt run `net user administrator /active:yes`, sign in as Administrator, and test updates there.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` in an administrator Command Prompt.
3. If SFC finds corruption in security descriptors, that was likely the root cause — restart and retry.
4. After testing, disable the built-in administrator again with `net user administrator /active:no` for security.

### Fix 6: Pause Acer utilities and look for policy blocks

Acer's own software and system policies can both deny the updater access.

1. In `services.msc`, temporarily stop **Acer Care Center** services and any Acer updater entries; end their Task Manager processes too.
2. Retry Windows Update with Acer's tools paused. If it works, update Acer Care Center itself before re-enabling — outdated versions cause the repeat conflicts.
3. Check for policy restrictions: on Pro editions, open `gpedit.msc` and inspect **Computer Configuration, then Administrative Templates, then Windows Components, then Windows Update** for anything unusual.
4. On a work-managed Acer, MDM policies can restrict update permissions — your IT administrator owns that configuration.

### Fix 7: Run the troubleshooter, then repair-install Windows

The final rungs for permission damage that resists targeted repair.

1. Run **Settings, then System, then Troubleshoot, then Other troubleshooters, then Windows Update**, and apply all suggested fixes.
2. If the troubleshooter reports it can't fix the problem, see our guide to the [troubleshooter not working](/articles/windows-update-troubleshooter-not-working-troubleshooting/).
3. As the last resort, download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run `setup.exe`, and choose **Keep personal files and apps** — the in-place upgrade rebuilds all system permissions cleanly.
4. Afterward, reinstall only the security software you actually use, and fully remove trial AV instead of letting it expire in place.

## Closing

Error 0x80070005 is Windows Update being denied entry to its own workspace — and on Acer laptops, the denier is usually a half-removed trial antivirus, broken folder permissions, or Acer's own utilities. Remove the blocker, reset the permissions, and rebuild the cache. If updates then fail with a different signature — say, files reported missing rather than access denied — our guide to [error 0x80070002](/articles/how-to-fix-windows-update-error-0x80070002-on-dell-laptop/) covers that sibling code; and for keeping Acer drivers current without update conflicts, see our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/).
