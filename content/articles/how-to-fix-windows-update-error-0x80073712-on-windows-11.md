---
title: "Fix Windows Update Error 0x80073712 on Windows 11 (Component Store Corrupt)"
slug: how-to-fix-windows-update-error-0x80073712-on-windows-11
date: 2026-09-19
categories: ["windows-update"]
tags: ["windows update", "0x80073712", "component store", "dism", "windows 11"]
description: "Windows 11 error 0x80073712 signals a corrupted component store. Repair it with DISM, SFC, and servicing-stack fixes so updates install again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80073712-on-windows-11.webp"
faqs:
  - q: "What is the component store (WinSxS)?"
    a: "On Windows 11, the component store is the master library under C:\\Windows\\WinSxS holding every version of every system component, plus their manifests. Windows Update stages new component versions into this store, then switches the live system to them. Error 0x80073712 means this library is damaged, so no update transaction can complete."
  - q: "Should I run SFC or DISM first for 0x80073712?"
    a: "DISM first. SFC restores damaged system files from the component store — but if the store itself is what is damaged, SFC has nothing trustworthy to draw from. DISM /Online /Cleanup-Image /RestoreHealth mends the store, after which SFC can work properly. For this specific error, the order truly matters."
  - q: "Can I just delete the WinSxS folder to fix it?"
    a: "No — never delete WinSxS by hand. It is not a cache; it is the servicing foundation, and deleting it destroys Windows beyond repair. The safe slimming method is `DISM /Online /Cleanup-Image /StartComponentCleanup`, which removes only superseded components Windows no longer needs. Manual deletion is one of the quickest routes to a guaranteed reinstall."
  - q: "Why does DISM fail with 'source files could not be found'?"
    a: "Online DISM fetches repair payloads from Windows Update, so a broken update pipeline or a heavily customized image can leave it without sources. The answer is the /Source switch pointing at install.wim or install.esd from matching installation media, as Fix 3 shows. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the exact syntax per media type."
---
With 0x80073712, the ground Windows Update stands on has cracked: the component store — the WinSxS master library of every system-file version — contains corrupted or missing entries. The update engine tries to assemble the new system state from that library and fails with this code. On Windows 11 the usual preludes are an interrupted update, a disk fault, or an aggressive debloat script that removed servicing components.

The repair order runs outside-in: attempt to heal the store with DISM first, confirm with SFC, and reserve the in-place upgrade — which rebuilds the store while keeping your files — for damage that online repair cannot fix.

If you are actually seeing the invalid-data flavor of this trouble, the [Windows 10 guide](/articles/how-to-fix-windows-update-error-0x80073712-on-windows-10/) covers Windows 10 and the [companion guide for 0x8007000d](/articles/how-to-fix-windows-update-error-0x8007000d-on-windows-11/) targets corrupted update payloads. For store-level damage, begin below.

## Why this happens

- **An update was interrupted mid-servicing:** power loss or a forced shutdown while the servicing stack wrote to the store can leave it half-updated — the classic origin of 0x80073712.
- **Disk errors corrupted store files:** WinSxS holds tens of thousands of small files; bad sectors or file-system damage anywhere in that tree break the manifests the engine reads.
- **Debloat or cleanup scripts removed components:** aggressive third-party scripts sometimes delete servicing metadata the store needs, and the next update finds the missing pieces.
- **A previous update failed partway:** a failed cumulative update can leave the store mixed — some components at the new version, their manifests at the old — blocking every later update.
- **Manifests are mismatched or missing:** each manifest describes exactly which files belong to its component. Corrupted or absent manifests make the store unreadable to servicing even when the files themselves are fine.
- **Malware tampered with system components:** infections that patch or replace system files corrupt the store's hash records, so servicing validation fails even after the malware is gone.
- **Failing storage silently corrupts writes:** a deteriorating SSD can damage store writes without obvious errors elsewhere, producing persistent servicing failures that survive cache clears.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Heal the store with DISM RestoreHealth

RestoreHealth exists for exactly this error: it scans the component store against Windows Update (or a local source) and swaps out corrupted entries. It is the highest-yield single command for 0x80073712 and always precedes SFC, since SFC draws its repair source from the very store DISM mends.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Let the progress bar reach 100 percent without closing the window.
4. On success, restart the laptop.
5. Retry the update in Settings > Windows Update before anything else.

### Fix 2: Verify with SFC after DISM

With the store mended, SFC can do its job: scanning protected system files and restoring any that differ from the store's known-good copies. SFC after DISM — never before — keeps the repair source trustworthy.

1. Open Command Prompt as administrator (after DISM finished successfully).
2. Run `sfc /scannow` and wait for completion.
3. If it reports repaired files, restart the laptop.
4. If it reports no integrity violations, the file layer is healthy — only continue below if the update still fails.
5. Attempt the update again in Settings > Windows Update.

### Fix 3: Give DISM an explicit source image

Online DISM repairs from Windows Update, but if the update pipeline is itself broken, that source may be unreachable or incomplete, so pointing DISM at a local Windows image from installation media supplies a guaranteed-clean source and succeeds where online repair stalls.

1. Create Windows 11 installation media and note its drive letter (for example, E:).
2. Open an administrator Command Prompt.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth /Source:E:\Sources\install.wim /LimitAccess` (adjust the letter; use install.esd if that is what the media holds).
4. When it completes, run `sfc /scannow`.
5. Reboot and retry the update.

### Fix 4: Inspect the disk beneath the store

A store that keeps recorrupting after successful DISM repairs implicates the hardware: the disk damages files as fast as DISM fixes them. CHKDSK locates bad sectors and file-system errors so the store stops being rewritten onto failing storage.

1. Start a Command Prompt with administrator rights.
2. Run `chkdsk C: /f /r` and type Y to schedule at restart.
3. Reboot and let the scan run to completion.
4. After booting, run DISM RestoreHealth once more to fix anything the bad sectors harmed.
5. Retry the update, and inspect the drive's SMART status if corruption returns.

### Fix 5: Reset the Windows Update components

Even with a healthy store, a corrupted download cache or a wedged servicing state can keep triggering 0x80073712. Resetting the components — renaming SoftwareDistribution and catroot2, restarting the services — clears the operational layer so the repaired store can actually be used.

1. Bring up Command Prompt as administrator.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Bring all four services back with the matching `net start` commands.
5. Check for updates once more in Settings > Windows Update.

### Fix 6: Repair via an in-place upgrade

When DISM cannot mend the store, an in-place upgrade reinstalls Windows over itself — reconstructing the entire component store from pristine media — while keeping your files, apps, and settings. It is the definitive answer for store corruption resisting command-line repair, succeeding in the large majority of otherwise-hopeless 0x80073712 cases.

1. Create Windows 11 installation media — download it from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run setup.exe from the media while Windows runs normally.
3. Select Keep personal files and apps when prompted.
4. Let the upgrade finish (one to two hours); the laptop restarts several times.
5. Afterward, run Windows Update — the rebuilt store takes updates cleanly.

### Fix 7: Service the store offline from Windows Recovery

When online DISM cannot fix the store because the running system keeps corrupted files locked, remove the system from the equation: boot into the Windows Recovery Environment and run the repairs offline. Offline servicing can replace files beyond online repair's reach, making it the strongest command-line option short of an in-place upgrade.

1. Hold Shift while clicking Start > Power > Restart to enter the Recovery Environment.
2. Select Troubleshoot > Advanced options > Command Prompt.
3. Locate the Windows drive letter: run `diskpart`, then `list volume`, then `exit` (in WinRE it is often D:, not C:).
4. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`, swapping in the correct drive letter.
5. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`, substituting the same drive letter.
6. Type `exit`, choose Continue to boot normally, and attempt the update again in Settings > Windows Update.

## Closing

Error 0x80073712 means the servicing library itself is damaged: mend it with DISM, confirm with SFC, and rebuild via in-place upgrade when mending fails. Most Windows 11 cases resolve at the DISM stage. But if corruption keeps returning after successful repairs, switch from repairing to investigating the disk — a store that will not stay fixed is often the first candid warning of failing storage.
