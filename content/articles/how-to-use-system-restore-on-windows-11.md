---
title: "How to Use System Restore on Windows 11: The Complete Guide"
slug: how-to-use-system-restore-on-windows-11
date: 2026-09-29
categories: ["windows-errors"]
tags: ["system restore", "restore point", "windows 11", "recovery", "rollback"]
description: "System Restore can undo bad updates, drivers, and settings in minutes. Learn how to enable it, create restore points, and roll back — even when Windows won't boot."
thumbnail: "/images/thumbs/how-to-use-system-restore-on-windows-11.webp"
faqs:
  - q: "Does System Restore delete my personal files?"
    a: "No. System Restore only reverses system files, installed programs, drivers, and registry settings to the state captured in the restore point. Your documents, photos, music, and other personal files are explicitly excluded and remain untouched. Programs installed after the restore point was created will be removed, so you may need to reinstall recent software — but your data is safe."
  - q: "Why is System Restore turned off on my Windows 11 laptop?"
    a: "Windows 11 ships with System Protection disabled on most new installations — Microsoft's default favors other recovery mechanisms. You have to enable it manually per drive, which takes thirty seconds in System Properties. Many users only discover it's off when they need it most, which is why enabling it proactively is one of the highest-value maintenance tasks on this list."
  - q: "How much disk space do restore points use?"
    a: "Windows lets you cap it — typically 2–10% of the drive, configurable in System Protection settings. On a 512GB SSD, 5% gives you about 25GB, enough for many restore points. Old points delete automatically when the cap is reached. If you're short on space, 3–5% is a reasonable minimum; the protection is worth far more than the gigabytes."
  - q: "Can I use System Restore if Windows won't boot?"
    a: "Yes. Boot into the Windows Recovery Environment — via Settings > Recovery > Advanced startup, or by interrupting the boot three times — then go to Troubleshoot > Advanced options > System Restore. The wizard works the same as in Windows. This is one of the most valuable recovery options available when a bad update or driver leaves the system unbootable."
---

System Restore is the closest thing Windows 11 has to a time machine for your system — not your files, your *system*. Installed a driver that blue-screens on boot? Applied an update that broke everything? Changed a setting you can't un-change? A restore point rolls the system files, drivers, registry, and installed programs back to an earlier state, usually in under fifteen minutes, without touching a single personal file.

There's a catch, and it's an important one: on most Windows 11 laptops, System Restore is turned **off** by default. Microsoft doesn't enable System Protection on fresh installs, so the feature silently does nothing until you switch it on. This guide covers the whole lifecycle: enabling protection, creating manual points before risky changes, performing a restore from inside Windows, performing one from the recovery environment when Windows won't boot, and what to do when restore points are missing or the restore fails.

## Why this happens

- **System Protection disabled by default**: Fresh Windows 11 installs don't create restore points unless you enable the feature — the number one reason it's "not working."
- **Insufficient disk space allocation**: If the protection storage cap is tiny or the drive is full, Windows silently deletes old points or stops creating new ones.
- **Restore points deleted by updates**: Major feature updates sometimes wipe existing restore points during the upgrade process.
- **Corrupted restore point data**: Disk errors or interrupted point creation produce points that fail when you try to use them.
- **Third-party "optimizer" tools**: Disk cleaners and debloaters often delete restore points as "junk" or disable the Volume Shadow Copy service they depend on.
- **Antivirus blocking restore**: Some security software interferes with the restore process, causing it to fail partway through.
- **Trying to restore too far**: Very old points on a heavily changed system can fail because the gap between then and now is too wide.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable System Protection (do this now, before you need it)

If you take one action from this guide, make it this one.

1. Press **Windows + R**, type `sysdm.cpl`, press Enter, and go to the **System Protection** tab.
2. Select your system drive (usually C:), click **Configure**, choose **Turn on system protection**, and set **Max Usage** to 5–10%.
3. Click **OK**, then click **Create** to make your first restore point right now. Name it something clear like "Baseline working state."
4. Repeat for any other drives holding installed programs. From now on, Windows creates automatic points before updates and driver installs.

### Fix 2: Create manual restore points before risky changes

Automatic points are good; deliberate ones are better.

1. Before any driver update, major Windows update, registry edit, or unfamiliar software install, open the **System Protection** tab and click **Create**.
2. Name the point after what you're about to do: "Before NVIDIA driver 571.20" beats "Restore point 47."
3. The creation takes a minute or two. Verify it appears in the point list via **System Restore** > **Choose a different restore point**.
4. Make this a habit and you'll never fear a driver update again — the rollback is always one wizard away.

### Fix 3: Perform a restore from inside Windows

The standard scenario: Windows boots, but something is broken.

1. Press **Windows + R**, type `rstrui.exe`, and press Enter to open the System Restore wizard.
2. Choose **Choose a different restore point** to see the full list with dates and descriptions.
3. Select a point from before the problem started. Click **Scan for affected programs** — this shows exactly which programs and drivers the restore will remove, so there are no surprises.
4. Confirm and let it run. The PC restarts, the restore applies (5–15 minutes), and Windows boots to the earlier state. Your files are untouched.

### Fix 4: Perform a restore when Windows won't boot

The scenario that makes System Restore worth its weight in gold.

1. Boot into WinRE: **Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now** — or interrupt the boot three times if Windows won't start.
2. Go to **Troubleshoot** > **Advanced options** > **System Restore**.
3. Pick your account, enter your password, and the familiar wizard appears. Choose a restore point from before the failure.
4. Let it complete and choose **Continue** to boot Windows. If the boot failure was caused by the update or driver you rolled back, you're done. For persistent boot failures, our [automatic repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) covers the next steps.

### Fix 5: Fix "no restore points have been created"

When the wizard shows an empty list, work through the causes.

1. Verify System Protection is actually on for C: (Fix 1) — this is the cause 90% of the time.
2. Check the **Volume Shadow Copy** service in `services.msc` — it should be set to **Manual** and running when needed. Some "privacy" tools disable it.
3. Check free disk space — with under ~10% free, Windows may fail to create points silently. Free up space and create one manually.
4. Check your disk-cleanup habits: tools like CCleaner delete restore points by default in some configurations. Exclude them or stop using the tool.

### Fix 6: Deal with a failed or incomplete restore

Restores occasionally fail — usually for fixable reasons.

1. Note the error code. **0x80070005** (access denied) often means antivirus interference — temporarily disable third-party antivirus and retry.
2. Try a different, older restore point — the one you picked may itself be corrupt.
3. Try restoring from WinRE (Fix 4) instead of inside Windows — fewer running processes means fewer things that can interfere.
4. Run `chkdsk C: /f` and `sfc /scannow` first if you suspect disk or system-file damage is breaking the restore mechanism itself.

### Fix 7: Use restore points strategically alongside other tools

System Restore is one tool in the recovery kit — know when it's the right one.

1. **Bad driver or update?** System Restore is the fastest fix — use it first.
2. **Windows won't boot at all?** Try System Restore from WinRE before Startup Repair — it's faster and more targeted when you know what changed.
3. **Suspect malware?** Don't rely on restore alone — malware can hide in restore points. Scan first with Windows Defender offline scan.
4. **Need to undo a settings change?** Restore is overkill for a single setting, but perfect when you can't identify which of fifty changes broke things. Microsoft's [support hub](https://support.microsoft.com/en-us/windows) documents the full recovery option comparison.

### Fix 8: Set up ongoing protection hygiene

Make future-you grateful.

1. Verify monthly that System Protection is still on — major updates occasionally reset it. A calendar reminder takes ten seconds to check.
2. Keep the storage allocation at 5–10% and don't let the drive fill past 90% — full drives silently kill point creation.
3. Create a manual point before every Patch Tuesday and every driver update. Name them clearly.
4. Know the limits: System Restore doesn't protect personal files (use File History or proper backups for those) and can't fix hardware failures. It's a system-rollback tool — superb within its lane, useless outside it. For blue screens that persist after a restore, our [general BSOD guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) continues the investigation.

## Closing

System Restore is the most underused recovery feature in Windows 11, mostly because it's off by default and nobody tells you. Enable it today — thirty seconds in System Protection settings — and you buy yourself a fifteen-minute escape hatch from bad updates, bad drivers, and bad decisions. Create manual points before risky changes, name them clearly, and remember what it does and doesn't touch: system state yes, personal files no. It's not a backup and it's not a hardware fix, but for the large category of "Windows worked yesterday and doesn't today," it's the fastest way back.
