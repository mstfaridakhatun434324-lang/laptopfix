---
title: "How to Fix Windows Update Error 0x80070005 After a Windows 11 Update"
slug: "how-to-fix-windows-update-error-0x80070005-after-windows-11-update"
date: 2026-10-10
categories: ["windows-update"]
tags: ["error 0x80070005", "windows update", "access denied", "windows 11"]
description: "Windows Update error 0x80070005 (access denied) after a Windows 11 update? Six fixes that restore permissions, clear blocks, and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-after-windows-11-update.webp"
faqs:
  - q: "What does error 0x80070005 actually mean?"
    a: "Error 0x80070005 is the standard Windows “Access Denied” code. In the Windows Update context it means the update installer was refused permission to read or write files it needs — usually in the SoftwareDistribution folder, the driver store, or the component store. It is a permissions or file-lock problem, not a missing-file problem, which is why the fixes focus on ACLs, antivirus interference, and the update services’ accounts."
  - q: "Can my antivirus cause 0x80070005?"
    a: "It can, if it is configured aggressively. Real-time protection suites that sandbox unknown processes or lock system directories sometimes intercept the update installer’s file operations and deny them. Temporarily disabling real-time protection during the update install is a legitimate diagnostic step. Windows Defender stays active, and you re-enable the third-party suite immediately after the install completes."
  - q: "Do I need to reinstall Windows to fix 0x80070005?"
    a: "Only as a last resort. Error 0x80070005 is specifically a permissions and access problem, and the fixes above — resetting update components, checking service accounts, repairing the component store — resolve the vast majority of cases. A repair install (in-place upgrade) is worth trying before a clean install, since it preserves files and apps while rebuilding system permissions. Clean-install only if the ACL damage is system-wide."
  - q: "Is Controlled folder access behind this?"
    a: "Rarely on its own. Controlled folder access blocks apps from writing to protected folders, and the update installer’s temporary files can occasionally trip it. If you have it enabled and updates fail with access-denied errors, check Windows Security, then Protection history, for blocked update operations. Adding the updater as an allowed app — or briefly testing with the feature off — confirms whether it is the cause."
---

Error 0x80070005 is Windows’ blunt way of saying “access denied” — the update installer tried to read or write files it needs and was refused. It usually appears right after a Windows 11 update attempt, on the update that ran fine for everyone else, which makes it feel personal. It is not: something changed the permissions or locked the folders the updater depends on.

The encouraging part is that access-denied errors are among the most fixable update failures. Unlike corruption deep in the OS, a permissions problem has a permissions solution, and the diagnostic path is short. If you are seeing the sibling error about missing files instead, the [0x80070002 fix guide](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) covers that distinct cause.

## Why this happens

- **SYSTEM account lost permissions on update folders:** Error 0x80070005 literally means “access denied.” If the SYSTEM or TrustedInstaller account lost write rights on SoftwareDistribution, catroot2, or WinSxS, the installer cannot stage files.
- **Third-party antivirus blocking file operations:** Security suites that sandbox or lock system directories can deny the updater access to the very folders it must write to.
- **Corrupted user or system ACLs after a migration:** Disk clones, profile migrations, and some backup restores rewrite folder permissions incorrectly, breaking the updater’s access.
- **Windows Update services running under the wrong account:** If the wuauserv or BITS service logon account was changed (sometimes by tweaking tools), the services lose the privileges they need.
- **Damaged component store blocking assembly:** When the installer cannot read manifests it needs from WinSxS due to corruption, Windows reports the failure as access denied.
- **Pending file locks from a previous failed install:** A crashed earlier install can leave files locked with stale handles, so the next attempt is denied access to its own staging area.
- **Ransomware protection blocking the updater:** Controlled folder access in Windows Security occasionally blocks legitimate update operations writing to protected locations.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Reset the update folders so permissions rebuild cleanly

The fastest fix for most 0x80070005 cases is also the simplest: fresh update folders get fresh, correct permissions. Renaming (rather than deleting) preserves the old data as a backup while the rebuilt folders inherit the proper ACLs from their parent directories.

1. Open an elevated Command Prompt.
2. Stop the services: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.
3. Rename the working folders: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services with net start and retry the update — the fresh folders inherit correct default permissions.

### Fix 2: Temporarily disable real-time antivirus protection

Before assuming system damage, rule out the most common external cause. Antivirus products that hook file-system operations are the number one third-party trigger for access-denied update failures, and the test takes two minutes.

1. Open Windows Security > Virus & threat protection > Manage settings.
2. Temporarily turn off Real-time protection.
3. If you run a third-party suite, disable its real-time shield the same way.
4. Run the Windows Update install now, then re-enable protection immediately after.

### Fix 3: Verify the update services run as Local System

The update services must run as Local System to have the privileges their job requires. Tweaking tools and some enterprise scripts change these logon accounts, silently breaking updates with 0x80070005 until someone looks.

1. Press Win + R, type services.msc, and press Enter.
2. Double-click Windows Update, open the Log On tab, and confirm “Local System account” is selected with “Allow service to interact with desktop” unchecked.
3. Repeat for Background Intelligent Transfer Service.
4. If either was changed, correct it, restart the service, and retry the update.

### Fix 4: Repair the component store with DISM and SFC

When corruption (rather than true permission loss) makes files unreadable, Windows reports the failure as access denied. DISM rebuilds the component store’s integrity, which resolves the cases where 0x80070005 masks underlying store damage.

1. Open Terminal (Admin) and run: DISM /Online /Cleanup-Image /RestoreHealth.
2. Follow with: sfc /scannow.
3. Restart the laptop.
4. Retry the update — the repaired store lets the installer read the manifests it was previously denied.

### Fix 5: Check Controlled folder access blocks

Controlled folder access is designed to stop ransomware, but its allowlist does not always recognize every update helper process. The protection history log shows exactly what was blocked, turning a guessing game into a five-minute check.

1. Open Windows Security > Virus & threat protection > Manage ransomware protection.
2. Open “Protection history” and look for blocked operations naming update or installer processes.
3. If Controlled folder access is blocking them, add the blocked process via “Allow an app through Controlled folder access”.
4. Alternatively, test one update cycle with the feature temporarily off.

### Fix 6: Install the update manually as administrator

The standalone installer runs in a different security context than the automatic client and often succeeds where the client fails with access denied. It is both a workaround and a diagnostic: success here proves your system can install the update, narrowing the problem to the update client itself.

1. Download the latest cumulative update .msu for your build from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Right-click the .msu and choose “Run as administrator”.
3. If it installs cleanly, the problem was the automatic client’s permissions context, not the system.
4. Follow up with the [Windows Update support guidance](https://support.microsoft.com/en-us/windows) to repair the client for next month.

### Fix 7: Retry the update from a clean boot state

Access-denied errors sometimes come not from broken permissions but from a third-party service holding locks on the update folders at the wrong moment. A clean boot starts Windows with only Microsoft services, eliminating every third-party lock candidate in one step. If the update succeeds in a clean boot, you know a startup program was the blocker — a far more pleasant diagnosis than ACL damage. The [Windows 11-specific 0x80070005 notes](/articles/how-to-fix-windows-update-error-0x80070005-on-windows-11/) cover additional permission-repair steps if the clean boot does not resolve it.

1. Press Win + R, type msconfig, and press Enter.
2. On the Services tab, tick “Hide all Microsoft services”, then click “Disable all”.
3. On the Startup tab, open Task Manager and disable all startup items.
4. Restart — Windows now boots with a minimal service set.
5. Run the Windows Update install; re-enable services afterward via msconfig.

## Closing

Error 0x80070005 is Windows telling you the updater was locked out of its own workspace. Restore the right permissions, clear the interference from security software, and repair the component store — in that order — and the access-denied failures clear. It is a permissions problem with a permissions solution, not a reason to reinstall Windows.
