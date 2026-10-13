---
title: "How to Fix the Bad System Config Info Error on Windows 11"
slug: fix-bad-system-config-info-on-windows-11
date: 2026-09-19
categories: ["windows-errors"]
tags: ["bad system config info", "bsod", "registry error", "windows 11"]
description: "The BAD_SYSTEM_CONFIG_INFO blue screen means Windows' registry or boot config is damaged. Here's how to repair it from the recovery environment."
thumbnail: "/images/thumbs/fix-bad-system-config-info-on-windows-11.webp"
faqs:
  - q: "What causes Bad System Config Info?"
    a: "The Windows registry hive or the Boot Configuration Data is corrupt, so Windows can't load its own configuration at startup. Stop code 0x00000074. Common triggers: interrupted updates, disk errors corrupting the registry hives, failed driver installs, bad RAM corrupting data as it's written, and manual registry or BCD edits gone wrong."
  - q: "Can I fix it without losing my files?"
    a: "Yes. Registry restoration, BCD rebuilds, SFC/DISM repairs, and update rollbacks all preserve personal files — they repair configuration data, not user data. Your files only become collateral when the underlying cause is a dying drive, which is why drive testing is part of the sequence. Avoid clean installs until every repair avenue is exhausted."
  - q: "Why does it happen after a Windows update?"
    a: "Updates rewrite registry hives and boot configuration. If the update is interrupted by a power loss or crash, or if it conflicts with disk errors, the hives can be left half-written. Windows then can't parse its own configuration on the next boot. Rolling back the update from recovery often resolves it immediately."
  - q: "Is this error a sign my drive is failing?"
    a: "It can be. Registry hives live on disk, and bad sectors in exactly the wrong place corrupt them the same way a bad update does. If this error recurs after successful repairs, or if chkdsk keeps finding new bad sectors, treat the drive as suspect and run the manufacturer's full diagnostics before trusting the system."
---

BAD_SYSTEM_CONFIG_INFO (stop code 0x00000074) means Windows tried to load its own configuration — the registry hives and boot data it needs to start — and found them damaged. It's the operating system equivalent of showing up to work and finding the office blueprints shredded. The error strikes at boot, which means you'll be doing the repairs from the Windows recovery environment rather than from inside Windows itself.

The encouraging part: configuration can be rebuilt. The registry hives have automatic backups, the BCD can be reconstructed from scratch, and system file tools can repair damaged components — all without touching your personal files. The causes split between software (interrupted updates, bad driver installs, manual registry edits) and hardware (disk errors, bad RAM corrupting data as it's written). This guide works through both, starting from the recovery environment. If you can still boot into Windows intermittently, our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) gives you a stable platform for the software-side fixes; if Windows boots then hangs, see our [restart screen guide](/articles/windows-11-stuck-on-restarting-screen-fix/).

## Why this happens

- **Corrupt registry hives**: The SYSTEM or SOFTWARE hives damaged by interrupted writes — the core cause.
- **Damaged BCD store**: Boot Configuration Data corruption preventing Windows from locating its configuration.
- **Interrupted Windows update**: Power loss or crashes mid-update leaving hives half-written.
- **Disk errors**: Bad sectors landing on registry hive files.
- **Bad RAM**: Memory errors corrupting registry data as it's read into or written from memory.
- **Failed driver installation**: Driver installers that modify system configuration and fail partway.
- **Manual registry/BCD edits**: Tweaks and "optimizer" tools that damage critical keys.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Boot into the recovery environment

All repairs happen from here.

1. Interrupt boot three times at the Windows logo to reach **Automatic Repair**, then click **Advanced options**.
2. If that fails, boot from Windows installation USB (created with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11)) and choose **Repair your computer**.
3. Try **Startup Repair** first (**Troubleshoot** > **Advanced options** > **Startup Repair**) — it occasionally resolves this on its own.
4. For everything below, you'll use **Command Prompt** from **Troubleshoot** > **Advanced options**.

### Fix 2: Restore the registry from automatic backup

Windows keeps a backup of the registry hives — use it.

1. Open the recovery **Command Prompt**.
2. First identify your Windows drive letter: type `dir C:` — in recovery it's often D: or E:. Note the correct letter (we'll call it X: below).
3. Back up the current (corrupt) hives, then restore: 
   - `cd /d X:\Windows\System32\config`
   - `ren SYSTEM SYSTEM.bad` and `ren SOFTWARE SOFTWARE.bad`
   - `copy X:\Windows\System32\config\RegBack\SYSTEM X:\Windows\System32\config\`
   - `copy X:\Windows\System32\config\RegBack\SOFTWARE X:\Windows\System32\config\`
4. Type `exit`, choose **Continue**, and boot. If the RegBack folder is empty (Windows 10/11 later builds sometimes leave it empty), continue to Fix 3 — the BCD rebuild often suffices.

### Fix 3: Rebuild the BCD

Repair the boot configuration alongside the registry.

1. From the recovery **Command Prompt**, run: `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /scanos`, `bootrec /rebuildbcd`.
2. If `rebuildbcd` finds nothing, rebuild manually via diskpart: `list vol`, find the FAT32 EFI partition, `select vol N`, `assign letter=Z:`, `exit`, then `bcdboot X:\Windows /s Z: /f UEFI` (X: = your Windows drive letter).
3. Type `exit` and **Continue** to test the boot.
4. A successful boot after this fix means the BCD was the (or a) problem — proceed to Fix 6 to check the disk so it doesn't recur.

### Fix 4: Uninstall the triggering update

If the timeline implicates an update, reverse it from recovery.

1. Go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Remove the **latest quality update** first, test, then the **latest feature update** if needed.
3. Once booted, check [Microsoft's support pages](https://support.microsoft.com/en-us/windows) for known issues with that KB before reinstalling.
4. Pause updates until you're confident the system is stable — a recurring bad update will just re-corrupt the configuration.

### Fix 5: Run offline SFC and DISM

Repair system files without needing Windows to boot.

1. From the recovery **Command Prompt**, run `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows` (X: = your Windows drive letter).
2. DISM offline repair is complex from recovery; instead, once booted (after any of Fixes 2–4 succeed), immediately run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` from an elevated terminal.
3. If offline SFC reports unfixable corruption, that's a signal the install is deeply damaged — Fix 7's reset becomes the pragmatic path.

### Fix 6: Check the disk and memory

Recurring configuration corruption means the hardware is damaging data.

1. From recovery Command Prompt, run `chkdsk X: /f /r` and let the full scan complete — bad sectors on hive files explain everything.
2. Run Windows Memory Diagnostic (`mdsched.exe` from inside Windows once booted, or from another PC's perspective: test sticks individually).
3. Run the manufacturer's full diagnostics (**F12** > **Diagnostics** on Dell, **F2** on HP) for the drive.
4. If chkdsk keeps finding new bad sectors across runs, the drive is deteriorating — replace it before trusting the system with important data.

### Fix 7: Reset Windows (keep files)

The last resort that preserves your data.

1. From recovery: **Troubleshoot** > **Reset this PC** > **Keep my files**.
2. This reinstalls Windows with a fresh registry and boot configuration while preserving personal files.
3. Reinstall drivers from the laptop manufacturer's site first, then applications.
4. If even the reset fails or the error returns on a fresh install, the drive is the problem — replace it and clean-install.

## Closing

BAD_SYSTEM_CONFIG_INFO is a configuration problem with configuration solutions: restore the registry backup, rebuild the BCD, roll back the update that broke it. The key insight is that your data and your configuration are separate things — every fix here targets the configuration layer and leaves your files alone. The one question worth answering after any successful repair is *why* the configuration got damaged: a one-time interrupted update needs no further action, but recurring corruption means testing the disk and RAM before you trust the machine again. Get the repair done, then get the answer — in that order. If Windows boots but crashes with driver errors instead, our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) is the right next step.
