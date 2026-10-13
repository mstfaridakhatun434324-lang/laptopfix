---
title: "Windows Update Error 0x80070005 on YouTube? Fix It in Text"
slug: how-to-fix-windows-update-error-0x80070005-youtube
date: 2026-09-19
categories: ["windows-update"]
tags: ["0x80070005", "access denied", "windows update", "windows 11", "permissions"]
description: "Error 0x80070005 means access denied — something is blocking the update. Here's the text walkthrough matching what video guides demonstrate."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070005-youtube.webp"
faqs:
  - q: "What does error 0x80070005 mean in Windows Update?"
    a: "It is the Windows error code for access denied. The update installer tried to read, write, or replace something and was refused permission. The usual gatekeepers are antivirus software locking files, incorrect permissions on system folders, a non-administrator account, or corrupted security descriptors. The fix is finding which gatekeeper is refusing and clearing it."
  - q: "Can antivirus really cause 0x80070005?"
    a: "Yes, it is one of the top causes of this exact code. Real-time protection locks system files to scan them, and if the update installer needs to replace a locked file at that precise moment, the operation fails with access denied. Temporarily pausing third-party antivirus during the update is a standard, safe troubleshooting step used by technicians everywhere — just remember to re-enable protection immediately after the update completes."
  - q: "Do I need an administrator account to fix this?"
    a: "Yes. Nearly every 0x80070005 repair requires elevation: resetting folder permissions, editing the registry, running DISM, and taking ownership all need administrator rights. If you are on a standard user account, switch to an administrator account before starting — without admin rights, the permission repairs at the heart of this fix cannot apply, and you will go in circles."
  - q: "Will resetting permissions harm my system?"
    a: "Resetting permissions on the specific update-related folders using documented procedures is safe. What you should avoid is blindly taking ownership of the entire Windows folder or running permission resets on the whole drive, which can cause real damage. Stay targeted: SoftwareDistribution, catroot2, and the user profile temp folders."
---

Error 0x80070005 is Windows saying "access denied" in hexadecimal. The update installer reached for something — a file, a folder, a registry key — and was refused. Video tutorials demonstrate the fixes visually, but permission repairs deserve careful, readable steps you can follow exactly. This is the text companion: same fixes, at your pace, with nothing rushed.

The suspects are a short list: antivirus locking files, wrong permissions on update folders, a non-admin account, or corrupted access control lists. We will clear them in order.


Access-denied errors are about finding the guard that said no. Before changing anything, ask: what runs with the power to refuse? Antivirus, permission tools, group policies, and disk errors are the usual guards. The fixes below interrogate them in order of likelihood, starting with the ones you can test in under a minute.
## Why this happens

- **Antivirus file locks:** Real-time scanning holding files the installer must replace.
- **Wrong folder permissions:** SoftwareDistribution or system folders with broken access control lists.
- **Non-administrator account:** The install running without the rights it needs.
- **Corrupted security descriptors:** Damaged permission metadata on system objects.
- **Third-party "privacy" tools:** Aggressive utilities that strip permissions from system folders.
- **Disk errors:** Filesystem corruption manifesting as access failures.
- **User profile issues:** Temp folder permission problems breaking the installer's staging.
- **Encrypted folders:** EFS-encrypted system folders the installer cannot read.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run as administrator and pause antivirus

1. Confirm you are signed in as an **administrator** in **Settings > Accounts > Your info**.
2. Temporarily disable third-party antivirus real-time protection (keep Defender on).
3. Close system utilities, disk tools, and "privacy" apps that might lock files.
4. Retry the update. This alone resolves the single most common 0x80070005 trigger.
5. Verify the admin account is not a Microsoft-account-linked standard user in disguise.
6. If UAC prompts do not appear, check that User Account Control is actually enabled.

### Fix 2: Reset the update folders' permissions

1. In an elevated Command Prompt, run `net stop wuauserv` and `net stop bits`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` — the folder is recreated with correct permissions on restart.
3. Do the same for `C:\Windows\System32\catroot2`.
4. Restart both services and retry. Fresh folders inherit correct access control lists automatically.
5. After renaming, confirm the new folders inherit permissions from C:\Windows correctly.
6. If the rename fails with access denied, boot into Safe Mode and try there.
7. After the rename, restart and verify the new folders were recreated with today's date.
8. If Windows cannot recreate them, run the update troubleshooter to rebuild the pipeline.

### Fix 3: Take ownership of the temp staging area

1. Press **Win + R**, type `%temp%`, and check you can create and delete files there.
2. If access is denied, right-click the Temp folder, open **Properties > Security**, and ensure your account has full control.
3. Clear the temp folder's contents (skip files in use).
4. The installer stages files here; a broken temp folder permission fails every update with 0x80070005.
5. Check both the user Temp and the system Temp (C:\Windows\Temp) permissions.
6. Clear both temp locations — the installer uses each at different stages.

### Fix 4: Run the update troubleshooter

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Windows Update**.
2. The troubleshooter includes permission checks on the update pipeline.
3. Apply its fixes and restart.
4. If the troubleshooter will not run at all, see our guide on [troubleshooter problems](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) before continuing.
5. Read the troubleshooter's detailed results for permission-specific repairs.
6. Run it from an elevated context by launching Settings as administrator.

### Fix 5: Repair system files

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
2. Follow with `sfc /scannow` — it specifically repairs corrupted security descriptors on system files.
3. Restart the laptop after both complete.
4. Corrupted ACLs on system files are an invisible but real cause of this code. Microsoft documents both tools on its [Windows support pages](https://support.microsoft.com/en-us/windows).
5. SFC specifically repairs file security descriptors — let it complete fully.
6. Check the CBS log for 'access denied' repairs to confirm the fix applied.
7. After the repairs, retry the update before changing anything else — test one variable at a time.

### Fix 6: Check for disk errors

1. Run `chkdsk C: /f` in an elevated Command Prompt and approve the next-restart scan.
2. Restart and let the scan complete fully.
3. Filesystem corruption can present as access denied when the real problem is unreadable sectors.
4. If chkdsk finds extensive damage, back up your data promptly — the disk may be failing.
5. Schedule the chkdsk for the next restart and let it run uninterrupted.
6. If bad sectors cluster on system files, plan a drive replacement — permissions will keep breaking.

### Fix 7: Manual install with a clean security context

1. Find the KB number in Update history and download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Right-click the .msu and choose **Run as administrator** explicitly.
3. Install with antivirus still paused and other software closed.
4. If the manual install succeeds, the automated pipeline had the permission problem — consider the full component reset in our guide on [update errors in 24H2](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) to heal it.
5. Create a fresh administrator account and try the manual install there to isolate profile issues.
6. If it works in the new profile, migrate your data — the old profile's permissions are damaged.

## Closing

0x80070005 is a permission problem wearing an error code costume: find the gatekeeper — usually antivirus or broken folder ACLs — and clear it. Run elevated, pause the guards, refresh the folders, and repair the descriptors. Access denied stops being mysterious once you know where to look, and it rarely requires anything drastic. Permission problems feel personal but they are mechanical: something guards a resource the installer needs. Identify the guard, satisfy it, and the update proceeds. Document the cause — access-denied errors love to recur.
