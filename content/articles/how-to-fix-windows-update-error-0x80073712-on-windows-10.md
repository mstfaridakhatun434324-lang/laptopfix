---
title: "How to Fix Windows Update Error 0x80073712 on Windows 10"
slug: how-to-fix-windows-update-error-0x80073712-on-windows-10
date: 2026-09-20
categories: ["windows-update"]
tags: ["windows update", "0x80073712", "component store", "dism", "windows 11"]
description: "Windows 10 update error 0x80073712 signals a corrupted component store. These steps repair the store and get updates flowing."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80073712-on-windows-10.webp"
faqs:
  - q: "What is the component store (WinSxS)?"
    a: "On Windows 10, the component store is the master library under C:\\Windows\\WinSxS holding every version of every system component, plus the manifests describing them. Windows Update works by staging new component versions into this store and then switching the live system to them. Error 0x80073712 means this library is corrupted, so no update transaction can complete."
  - q: "Should I run SFC or DISM first for 0x80073712?"
    a: "Run DISM first. SFC restores damaged system files from the component store — but if the store itself is the corrupted part, SFC has nothing trustworthy to restore from. DISM /Online /Cleanup-Image /RestoreHealth repairs the store, and then SFC can do meaningful work. For this specific error, the order genuinely matters."
  - q: "Can I just delete the WinSxS folder to fix it?"
    a: "No — never delete WinSxS manually. It is not a cache; it is the servicing foundation, and deleting it destroys Windows beyond repair. The safe way to slim it is `DISM /Online /Cleanup-Image /StartComponentCleanup`, which removes only superseded components Windows no longer needs. Deletion by hand is one of the fastest ways to guarantee a reinstall."
  - q: "Why does DISM fail with 'source files could not be found'?"
    a: "Online DISM downloads repair payloads from Windows Update, so a broken update pipeline or a heavily customized image can starve it of sources. The fix is the /Source switch pointing at install.wim or install.esd from matching installation media, as described in Fix 3. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the exact syntax for different media types."
---
On Windows 10, error 0x80073712 (ERROR_SXS_COMPONENT_STORE_CORRUPT) tells you the component store that servicing depends on is damaged. Every update is essentially a transaction against this store — adding, replacing, and superseding component versions — and a corrupted store aborts the transaction before any real change happens, which is why the failure is clean but persistent.

This is deeper than a bad download cache: clearing SoftwareDistribution alone will not fix it, because the damage is in the store itself. The fixes below repair the store in escalating order of thoroughness, ending with an in-place upgrade that rebuilds it entirely.

The [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80073712-on-windows-11/) mirrors this guide for Windows 11, and the [companion guide for 0x8007000d](/articles/how-to-fix-windows-update-error-0x8007000d-on-windows-10/) addresses the corrupted-download side of the family. Work through these in order.

## Why this happens

- **An update was interrupted mid-servicing:** If power failed or the machine was forced off while the servicing stack was writing to the component store, the store can be left half-updated — the classic origin of 0x80073712.
- **Disk errors corrupted store files:** WinSxS contains tens of thousands of small files; bad sectors or file-system corruption anywhere in that tree break the manifests the update engine reads.
- **Debloat or cleanup scripts removed components:** Third-party scripts that aggressively strip Windows components sometimes delete servicing metadata the store needs, and the next update discovers the missing pieces.
- **A previous update failed partway through:** A failed cumulative update can leave the store in a mixed state — some components at the new version, their manifests at the old — which blocks every subsequent update.
- **Manifest files are mismatched or missing:** Each component's manifest describes exactly which files belong to it. Corrupted or missing manifests make the store unreadable to the servicing stack even when the actual files are fine.
- **Malware tampered with system components:** Infections that patch or replace system files corrupt the store's hash records, so servicing validation fails even after the malware is removed.
- **Failing storage corrupts writes silently:** A deteriorating SSD can corrupt store writes without triggering obvious errors elsewhere, producing persistent servicing failures that survive cache clears.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair the store with DISM RestoreHealth

Let it run to 100 percent without interruption — on slow drives with large stores it can take 30 minutes or more.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Wait for the progress bar to reach 100 percent; do not close the window.
4. If it reports success, restart the laptop.
5. Retry the update in Settings > Update & Security > Windows Update before doing anything else.

### Fix 2: Verify with SFC after DISM

This two-punch combination resolves the majority of 0x80073712 cases without any further escalation.

1. Open Command Prompt as administrator (after DISM completed successfully).
2. Run `sfc /scannow` and wait for it to finish.
3. If it reports corrupt files repaired, restart the laptop.
4. If it reports no integrity violations, the file layer is healthy — continue below only if the update still fails.
5. Retry the update in Settings > Update & Security > Windows Update.

### Fix 3: Run DISM with an explicit source image

You need installation media matching your OS version and edition; the install.wim or install.esd inside it becomes the repair source.

1. Create the Windows 10 Media Creation Tool and note its drive letter (for example E:).
2. Open Command Prompt as administrator.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth /Source:E:\Sources\install.wim /LimitAccess` (adjust the letter and use install.esd if that is what the media contains).
4. Wait for completion, then run `sfc /scannow`.
5. Restart and retry the update.

### Fix 4: Check the disk underlying the store

Take recurrence seriously — a store repaired three times is a drive asking to be replaced, not a software problem.

1. Open Command Prompt as administrator.
2. Run `chkdsk C: /f /r` and type Y to schedule it at restart.
3. Restart and let the scan complete fully.
4. After booting, run DISM RestoreHealth once more to fix anything the bad sectors damaged.
5. Retry the update, and check the drive's SMART status if corruption returns.

### Fix 5: Reset the Windows Update components

Think of this as clearing the construction site after rebuilding the foundation: the foundation (store) is fixed, now remove the debris (cache).

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart all four services with the matching `net start` commands.
5. Check for updates in Settings > Update & Security > Windows Update.

### Fix 6: Perform an in-place upgrade repair

Back up important files first anyway; the process is safe, but irreplaceable data deserves a safety net regardless.

1. Create the Windows 10 Media Creation Tool — download it from Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows).
2. Run setup.exe from the media while Windows is running normally.
3. Choose Keep personal files and apps when prompted.
4. Let the upgrade complete (one to two hours); the laptop will restart several times.
5. Afterward, run Windows Update — the rebuilt store accepts updates cleanly.

### Fix 7: Repair the store offline from Windows Recovery

Online repairs sometimes fail because Windows 10 holds the damaged store files open while it runs. The Recovery Environment boots a minimal system instead, leaving your installation's files unlocked and fully serviceable. Running DISM and SFC from there succeeds in cases where every online attempt stalled.

1. Hold Shift while clicking Start > Power > Restart to boot into the Recovery Environment.
2. Choose Troubleshoot > Advanced options > Command Prompt.
3. Find your Windows drive letter with `diskpart`, then `list volume`, then `exit` (it is often D: in WinRE, not C:).
4. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`, adjusting the drive letter to match.
5. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` with the same letter.
6. Type `exit`, choose Continue to boot normally, and retry the update in Settings > Update & Security > Windows Update.

## Closing

On Windows 10, component store corruption feels catastrophic but repairs cleanly in most cases: DISM heals the store, SFC verifies the files, and the in-place upgrade rebuilds everything when both fall short. Work the escalation ladder patiently — each step is more thorough than the last — and resist the urge to jump straight to a full reinstall, which costs far more time for the same result.
