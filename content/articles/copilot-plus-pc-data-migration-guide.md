---
title: "How to Move Your Files, Apps, and Settings to a New Copilot+ PC"
slug: copilot-plus-pc-data-migration-guide
date: 2026-10-21
categories: ["ai-pc"]
tags: ["data migration", "copilot+ pc", "windows backup", "onedrive", "app reinstall", "file transfer"]
description: "Move files, apps, and settings to your new Copilot+ PC safely. A 6-step migration guide covering Windows Backup, OneDrive, external drives, and ARM app checks."
thumbnail: "/images/thumbs/copilot-plus-pc-data-migration-guide.webp"
faqs:
  - q: "Does Windows Backup move everything to my new Copilot+ PC?"
    a: >
      Windows Backup restores your Microsoft Store apps, most settings, credentials, and your Desktop, Documents, and Pictures folders if they sync to OneDrive. It does not move files stored outside those folders, drivers, or traditionally installed desktop apps — you reinstall those separately.
  - q: "Will my old apps work on a Snapdragon Copilot+ PC?"
    a: >
      Most do, either as native ARM64 builds or through Prism emulation for x64 apps. A small number of apps with kernel-level drivers — some VPN clients, anti-cheat tools, and older utilities — may fail. Check each critical app's ARM status before you wipe the old machine.
  - q: "How long does a full data migration take?"
    a: >
      Plan for 2 to 4 hours of active work plus overnight file copying if you have hundreds of gigabytes. The cloud restore during first boot is fastest for typical profiles; bulk media is quicker over a USB-C external SSD than re-downloading.
  - q: "Should I wipe my old laptop after migrating?"
    a: >
      Only after you have opened every key file and app on the new machine and confirmed nothing is missing. Then sign out of your Microsoft account, deactivate licensed apps, and use Windows Reset with data erasure before selling or recycling it.
---

Unboxing a new Copilot+ PC is exciting — until you realize your files, apps, passwords, and settings still live on the old laptop. A careless move leaves you with missing documents, broken app licenses, and features that worked yesterday suddenly refusing to run on the new machine. On AI laptops this matters more than usual, because some Copilot+ PCs run on Snapdragon ARM chips where not every old program behaves the same.

You have several good paths: Microsoft's cloud backup restore during first boot, OneDrive sync, a direct external-drive copy, or a mix of all three. The trap most people fall into is copying only the obvious folders and assuming everything else followed. Settings, browser profiles, email accounts, game saves, and app licenses each travel by their own route, and each needs a plan.

This guide walks you through migration in six ordered stages: audit the old machine, restore from Windows Backup, sweep up what the cloud missed, reinstall apps with ARM compatibility in mind, move licenses and credentials, and verify before you wipe anything. Before you start, confirm your new machine meets the [Copilot+ PC requirements](/articles/copilot-plus-pc-requirements/) so you know exactly which AI features should work after the move.

## Why this happens

- **Files live in unexpected places:** Beyond Documents and Desktop, real data hides in Downloads, secondary partitions, external-profile folders, and app-specific directories. A folder-by-folder copy of the obvious locations routinely misses gigabytes.
- **Snapdragon Copilot+ PCs are ARM-based:** Apps compiled for Intel/AMD chips run through emulation on ARM. Most work fine, but kernel drivers, anti-cheat engines, and some pro tools do not — and discovering this after wiping the old laptop is painful.
- **Windows Backup does not cover everything:** It restores settings, Microsoft Store apps, and OneDrive-synced folders. Traditionally installed desktop apps, drivers, and files outside synced folders must be handled manually.
- **OneDrive selective sync tricks you:** Files showing a cloud icon are stubs, not local copies. If you copy those stubs to an external drive without downloading them first, you copy placeholders, not data.
- **Licenses are tied to machines:** Adobe, Office retail keys, and many developer tools count activations per device. Migrating without deactivating first can burn an activation and trigger a support call.
- **NPU drivers do not transfer:** Drivers are machine-specific. The new laptop needs its own fresh NPU driver set from the manufacturer, not anything copied from the old machine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Audit the old machine before touching the new one

Migration fails when you do not know what you own. Spend thirty minutes inventorying the old laptop so nothing hides from you later — this is the step everyone skips and everyone regrets skipping.

1. List every folder that holds real data: check Desktop, Documents, Downloads, Pictures, Videos, Music, plus any D: or secondary drive, and note their sizes.
2. Open each browser and export bookmarks, then confirm passwords sync to your Microsoft or Google account rather than living only on the device.
3. Write down your must-have apps and their license keys or login methods — Office, Adobe, VPN clients, password managers, and anything paid.
4. Photograph or screenshot the old Start menu and taskbar so you can rebuild your workflow layout from memory.

### Fix 2: Back up with Windows Backup and restore during first boot

Windows Backup to your Microsoft account is the fastest way to move your profile — settings, credentials, Store apps, and synced folders land on the new machine during setup with almost no effort from you.

1. On the old laptop, open **Settings > Accounts > Windows backup** and turn on every toggle — Microsoft's [backup overview](https://support.microsoft.com/en-us/windows) explains what each one covers — then click **Back up now** and wait for it to finish.
2. During the new Copilot+ PC's first-boot setup, sign in with the same Microsoft account and choose **Restore from this PC** when offered.
3. Let the restore complete before installing anything else — it also pulls your Wi-Fi networks, theme, and accessibility settings.
4. After setup, verify Desktop, Documents, and Pictures match the old machine, and reinstall any Microsoft Store apps the restore queued but did not finish.

### Fix 3: Sweep up what the cloud missed with an external drive

Cloud restore handles the profile, but bulk media, archives, and files outside synced folders need a physical copy. A USB-C SSD is far faster than re-downloading terabytes.

1. In OneDrive settings on the old machine, choose **Download all files** for any folder you plan to copy, so stubs become real files first.
2. Copy the leftovers — media libraries, project folders, downloads archives, game saves in Documents subfolders — to the external drive.
3. On the new PC, paste these into matching locations and double-check a few large files open correctly rather than trusting the copy blindly.
4. Keep the external drive untouched for a week as a fallback copy, in case something you forgot surfaces later.

### Fix 4: Reinstall apps — check ARM compatibility first

Never copy Program Files folders between machines. Fresh installs register correctly, and on Snapdragon Copilot+ PCs the installer you choose determines whether an app runs natively or through emulation.

1. Install your browser first and sign in, so bookmarks, extensions, and passwords arrive immediately.
2. For each critical app, download the **ARM64** version if the vendor offers one — Adobe, Chrome, Firefox, Zoom, and most major tools now ship native ARM builds.
3. For apps with no ARM build, install the x64 version and test it; Prism emulation handles most, but flag anything with kernel-level drivers (VPNs, anti-cheat) for the vendor's compatibility notes.
4. If you later hit NPU or chipset driver trouble on the new machine, a [manual INF install of the Intel NPU driver](/articles/manually-install-intel-npu-driver-inf/) can resolve device errors that a generic driver package misses.

### Fix 5: Move licenses, email accounts, and credentials

Files are only half the migration. The other half is the invisible web of logins, activations, and two-factor approvals that makes a laptop actually yours.

1. Sign into your Microsoft account on the new PC and let Edge import everything; then add your other email accounts in Outlook or your mail app one by one.
2. Activate paid software and deactivate it on the old machine afterward to free the seat — do this while the old laptop still boots.
3. Move your authenticator app or security keys over and confirm 2FA logins work before you rely on them.
4. Re-pair Bluetooth devices, printers, and network drives, since none of these travel with a backup.

### Fix 6: Verify everything, then retire the old machine

Do not wipe the old laptop until the new one has survived a full work week. Verification is boring and essential — it is your last chance to find the one folder you forgot.

1. Open your five most important files and apps on the new PC and confirm they behave identically, including any NPU features you rely on.
2. Run an AI feature end-to-end — for example, check that [Click to Do image actions appear](/articles/click-to-do-image-actions-missing/) when you select text or images, confirming the AI stack migrated cleanly.
3. Compare free disk space and folder counts between old and new for the big libraries as a sanity check.
4. Only then: sign out of the old machine, deactivate remaining licenses, and run **Settings > System > Recovery > Reset PC** with data erasure.

## Closing

A clean migration is 80 percent preparation and 20 percent copying. Audit the old machine, let Windows Backup do the heavy lifting, sweep the leftovers onto an external drive, reinstall apps with ARM compatibility in mind, and verify before you wipe. Do it in this order and your new Copilot+ PC feels like home by the end of the first evening — with none of the missing-file surprises that haunt rushed moves.
