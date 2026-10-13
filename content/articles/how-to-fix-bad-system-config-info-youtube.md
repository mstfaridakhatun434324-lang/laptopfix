---
title: "How to Fix BAD_SYSTEM_CONFIG_INFO on Windows (Step-by-Step)"
slug: how-to-fix-bad-system-config-info-youtube
date: 2026-09-11
categories: ["windows-errors"]
tags: ["bad system config info", "bsod", "registry", "boot error"]
description: "BAD_SYSTEM_CONFIG_INFO blue screen stopping Windows from booting? Fix it with registry restore, BCD rebuild, and driver repairs — no video needed."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-youtube.webp"
faqs:
  - q: "What causes BAD_SYSTEM_CONFIG_INFO?"
    a: "The SYSTEM registry hive — which holds driver and service configuration — is corrupted, or the boot configuration data is damaged. Common triggers are interrupted Windows updates, disk errors, faulty RAM corrupting the registry in memory, or registry cleaner tools that deleted keys they shouldn't have. The name literally means Windows found its system configuration unreadable."
  - q: "Can I fix this without losing my files?"
    a: "Yes. Every fix in this guide — Startup Repair, registry restore, BCD rebuild, SFC/DISM, System Restore — leaves your personal files untouched. Only a clean install (the last resort) would remove them, and even then you can back up first from the recovery environment."
  - q: "Do registry cleaner tools cause this error?"
    a: "They're a known cause. Aggressive registry cleaners can delete or damage keys in the SYSTEM hive that Windows needs at boot. If you ran one before the crashes started, that's very likely your culprit — and a strong reason to never run registry cleaners again. Windows does not need its registry 'cleaned.'"
  - q: "What if the RegBack folder is empty?"
    a: "On some Windows 10/11 builds, automatic registry backups are disabled and RegBack contains 0-byte files. In that case, skip the registry restore and rely on System Restore (which backs up the registry as part of restore points), or use DISM and SFC repairs followed by a reset with files kept."
---
BAD_SYSTEM_CONFIG_INFO is Windows telling you it can't read its own configuration — usually the SYSTEM registry hive, the part of the registry that describes every driver and service. Without it, Windows can't even figure out how to start. This error often appears after a bad update, a disk error, or (commonly) a registry cleaner that got too enthusiastic.

The fixes run from the recovery environment since Windows won't boot. They're all non-destructive until the last resort, so work them in order without fear. If you can, note what happened just before the first crash — a Windows update, a new program, a hard shutdown — because that context often points straight at the cause and saves you working through every step.

## Why this happens

- **Corrupted SYSTEM registry hive.** Disk errors, hard shutdowns, or bad RAM can damage the hive Windows reads at boot.
- **Registry cleaner damage.** Third-party cleaners deleting "orphaned" keys can remove entries Windows actually needs.
- **Damaged boot configuration data.** A corrupt BCD produces the same stop code.
- **Failed Windows update.** An update interrupted while writing system configuration leaves it inconsistent.
- **Faulty RAM.** Memory errors corrupt the registry as Windows loads it, producing this error intermittently.
- **Failing storage.** Bad sectors in the registry or boot file areas cause persistent, worsening crashes.
- **Dual-boot tools.** Utilities that modify the BCD for Linux dual-booting can corrupt the boot configuration this stop code checks.

## How to fix it

Work through these in order from the recovery environment.

### Fix 1: Run Startup Repair and System Restore

Start with the automated options.

1. Interrupt boot three times to reach **Automatic Repair**, then go to **Troubleshoot > Advanced options > Startup Repair** and let it run.
2. If that fails, return to **Advanced options** and choose **System Restore**.
3. Pick the most recent restore point from before the crashes — restore points include registry backups, which directly address this error.
4. Let it complete and test the boot. If no restore points exist, continue.
5. If Startup Repair's report names a specific corrupt file, write down the path — it tells you whether the registry (config folder) or the boot files (EFI folder) took the hit, which focuses the manual repairs below.

### Fix 2: Restore the registry from the automatic backup

Replace the corrupted hive with Windows' own backup.

1. Open **Command Prompt** from **Advanced options**.
2. Find your Windows drive letter: run `diskpart`, `list volume`, `exit` (often D: in recovery).
3. Check the backup: `dir D:\Windows\System32\config\RegBack` — proceed only if files have real sizes.
4. Back up current hives: `cd /d D:\Windows\System32\config` then `copy SYSTEM SYSTEM.bad`.
5. Restore: `copy D:\Windows\System32\config\RegBack\SYSTEM D:\Windows\System32\config\SYSTEM` — confirm the overwrite, then restart.

### Fix 3: Rebuild the boot configuration data

Rule out BCD damage as the trigger.

1. In the recovery Command Prompt, run:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
2. If `fixboot` reports access denied, run `bcdboot D:\Windows` (your Windows drive letter) instead.
3. Type `exit` and choose **Continue** to test the boot.
4. A clean BCD eliminates the boot-loader side of this stop code.

### Fix 4: Repair system files offline

Fix corruption in the files surrounding the registry.

1. In the recovery Command Prompt with the correct drive letter, run:
   `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows`
2. Then run `DISM /Image:D:\ /Cleanup-Image /RestoreHealth`.
3. Restart and test.
4. These repairs fix the supporting files; combined with the registry restore, they cover the software causes completely.

### Fix 5: Check the disk for bad sectors

If the registry keeps corrupting, the disk may be damaging it.

1. Run `chkdsk D: /f /r` from the recovery Command Prompt (your Windows drive letter).
2. Let the full scan complete — it can take an hour on large drives.
3. If chkdsk finds and repairs bad sectors in system areas, retest the boot.
4. Recurring corruption after chkdsk repairs means the drive is failing — back up and replace it. The [ASUS-specific variant](/articles/fix-bad-system-config-info-on-asus-laptop/) covers laptop-specific angles.
5. If chkdsk reports bad sectors but the laptop boots afterward, don't consider the job done — schedule a drive replacement soon, because sectors that fail once tend to spread.

### Fix 6: Test the memory

Intermittent BAD_SYSTEM_CONFIG_INFO is a classic RAM symptom.

1. Boot your laptop maker's diagnostics and run the memory test, or use `mdsched.exe` from a working boot.
2. If errors appear, reseat the RAM and retest.
3. Test sticks individually to isolate the faulty one.
4. Replace bad RAM — memory corruption will keep destroying the registry no matter how often you restore it.

### Fix 7: Reset Windows keeping your files

When the configuration is damaged beyond targeted repair.

1. From **Troubleshoot**, choose **Reset this PC > Keep my files > Cloud download**.
2. The reset rebuilds the registry and system configuration from a fresh image.
3. After the reset, install drivers from your laptop maker's site before anything else.
4. Never run registry cleaners again — and consider the [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) for any future stop codes.

## Closing

BAD_SYSTEM_CONFIG_INFO is a configuration problem, not a data problem — your files are fine, Windows just can't read its own instructions. The registry restore in Fix 2 is the highest-value step; it directly replaces what the error says is broken.

And let this be the end of registry cleaners on your PC: the performance benefit is imaginary, but the boot failure they can cause is very real. Windows 10 and 11 manage the registry themselves, and no third-party tool understands your system's keys better than Windows does. If a "speed up your PC" video recommends one, that video is selling you the problem this guide just helped you fix. For any future stop codes, the [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) is the right starting point.
