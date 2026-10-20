---
title: "How to Move Recall Snapshots to an External Drive on Windows 11"
slug: recall-snapshots-external-drive
date: 2026-10-20
categories: ["ai-pc"]
tags: ["recall snapshots", "external drive", "storage", "copilot+ pc", "troubleshooting", "ai pc"]
description: "Running out of space for Recall snapshots? Learn how to move them to an external drive safely, what breaks when the drive disconnects, and how to fix it."
thumbnail: "/images/thumbs/recall-snapshots-external-drive.webp"
faqs:
  - q: "Can Recall store snapshots on an external drive?"
    a: "Yes, Windows lets you change the snapshot storage location to another drive, including an external USB drive. The drive should be fast, stay connected while you use the PC, and be encrypted with BitLocker, since snapshots contain a visual history of your activity."
  - q: "What happens if I unplug the external drive?"
    a: "Recall pauses snapshotting when its storage location is unavailable and resumes automatically when the drive is reconnected. Expect a gap in your timeline for the disconnected period. Never unplug the drive while Recall is actively writing a snapshot."
  - q: "Do snapshots stay encrypted on an external drive?"
    a: "Recall encrypts its snapshot data, but an external drive is easier to lose than your internal SSD, so enable BitLocker on the drive for a second layer of protection. Without it, anyone who finds the drive could potentially access the raw snapshot files."
  - q: "Will moving snapshots slow down Recall search?"
    a: "It can. Recall reads snapshot data constantly, so a slow USB 2.0 drive makes timeline scrolling and search laggy. Use a USB 3.0 or faster SSD-based external drive to keep performance close to internal storage."
---

Recall snapshots pile up fast — weeks of visual history can eat tens of gigabytes of your internal SSD. Moving the snapshot location to an external drive is the official escape valve: Windows lets you point Recall at another disk so your system drive keeps its breathing room.

But an external drive is not just a bigger folder. It can be unplugged, sleep unexpectedly, run slower than your SSD, or walk away in a bag — each a new failure mode for Recall. Most "snapshots not saving" errors and timeline gaps trace to a drive that was not prepared properly first.

This guide covers the safe way to move Recall snapshots to an external drive, what to do when the drive disconnects, and how to move back if you change your mind. If Recall acts up after the move, the same settings area controls the [Recall keyboard shortcut](/articles/recall-keyboard-shortcut-not-working/) — worth a quick check.

## Why this happens

- **The internal SSD is running out of space:** Recall keeps months of snapshots by default, and Windows trims retention automatically when disk space gets low, which looks like missing history.
- **The external drive is too slow:** Recall reads and writes snapshot data constantly. A spinning hard drive or USB 2.0 stick causes lag, timeouts, and failed writes.
- **The drive letter changed:** Windows tracks the snapshot location by path. If the drive mounts with a different letter after a reboot, Recall cannot find its data.
- **The drive was unplugged mid-write:** Disconnecting during an active snapshot can corrupt the snapshot database and force a rebuild.
- **BitLocker or permissions block access:** If the encrypted drive is not unlocked at sign-in, or folder permissions are wrong, Recall silently fails to save.
- **Power saving puts the drive to sleep:** Aggressive USB power management can spin the drive down between snapshots, causing intermittent failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Prepare the external drive correctly

Before touching any Recall setting, get the drive right. Connect a USB 3.0 or faster external SSD — not a flash drive or spinning disk. Format it as NTFS, since Recall's storage relies on NTFS permissions, then enable BitLocker: snapshots are a visual record of everything you do, and an external drive is easy to lose — see Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) for BitLocker setup. Finally, assign the drive a permanent letter like R: in Disk Management so it always mounts the same way.

1. Connect a USB 3.0 or faster external SSD.
2. Format the drive as NTFS if it is not already.
3. Enable BitLocker and save the recovery key somewhere safe.
4. In Disk Management, assign the drive a fixed letter such as R:.
5. Create a folder on the drive for Recall data, e.g. R:\RecallData.

### Fix 2: Move the snapshot location in Settings

With the drive ready, open Settings, go to Privacy and security, then Recall and snapshots, and point the storage location at your new folder. Windows migrates existing snapshots — keep the drive connected and the laptop awake until it finishes, and do not open Recall search mid-migration. Afterwards, create new on-screen activity and confirm it appears in your timeline, proving writes land on the external drive.

1. Open Settings, Privacy and security, Recall and snapshots.
2. Change the snapshot storage location to your external drive folder.
3. Let the migration finish completely without unplugging the drive.
4. Create new on-screen activity and confirm it appears in Recall search.
5. Verify freed space on your internal drive.

### Fix 3: Handle disconnections without corrupting data

The drive will get unplugged eventually. When Recall cannot reach its storage, it pauses capturing and resumes when the drive returns — that is normal, and the timeline gap is expected, not data loss. What causes corruption is unplugging mid-write. Always eject with the Safely Remove Hardware icon first, and consider pausing Recall in Settings before planned disconnections. If snapshots never resume after reconnecting, restart the PC with the drive attached. Account-side oddities sometimes follow drive or profile changes; if you hit sign-in weirdness too, our [Copilot login loop guide](/articles/copilot-login-loop-windows-11/) covers those checks.

1. Always eject with Safely Remove Hardware before unplugging.
2. Pause Recall in Settings before planned disconnections.
3. Reconnect and wait a minute for automatic resume.
4. Accept the timeline gap for the disconnected period as normal.
5. If capture never resumes, restart with the drive connected.

### Fix 4: Fix permission and BitLocker unlock problems

If snapshots stopped saving after a reboot, suspect access: either BitLocker has not unlocked the drive yet, or folder permissions changed. Enable BitLocker auto-unlock so the drive is available at sign-in. Then check the folder's Security properties and confirm your account and SYSTEM both have full control — Recall's background service writes as SYSTEM. If you copied the folder manually instead of letting Windows migrate it, permissions often break; point Recall at a fresh empty folder and let it rebuild. Keep the snapshot folder out of OneDrive or any cloud sync, which can lock files mid-write.

1. Enable BitLocker auto-unlock for the external drive.
2. Confirm SYSTEM has full control of the Recall folder.
3. Remove the folder from OneDrive or cloud sync scope.
4. If writes still fail, point Recall at a fresh empty folder.
5. Verify new snapshots appear in Recall search.

### Fix 5: Keep the drive awake and move back if needed

External drives love to sleep, and a sleeping drive means failed writes. In Device Manager, disable "Allow the computer to turn off this device to save power" on your USB hub, and set USB selective suspend to Disabled in Power Options. If Recall search feels sluggish, the drive is simply too slow — upgrade to a faster external SSD. And if the experiment keeps fighting you, move back: restore the default location in Settings, let Windows migrate, and instead limit retention to 30, 60, or 90 days. If AI features feel off after storage changes, check whether the [NPU disappeared after a Windows update](/articles/npu-disappeared-after-windows-update/).

1. Disable USB power saving for the hub the drive uses.
2. Set USB selective suspend to Disabled in Power Options.
3. If search is slow, upgrade to a faster external SSD.
4. To move back, restore the default location in Settings and let it migrate.
5. Consider shorter snapshot retention instead of external storage.

## Closing

Moving Recall snapshots to an external drive reclaims SSD space, but the drive must earn the job: fast, NTFS, BitLocker-encrypted, with a fixed letter and no aggressive power saving. Prepare the drive first, migrate through Settings, and eject safely. If it causes more trouble than it saves, moving back takes minutes.
