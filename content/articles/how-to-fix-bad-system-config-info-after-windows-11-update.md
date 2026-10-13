---
title: "Bad System Config Info After a Windows 11 Update: How to Fix It"
slug: how-to-fix-bad-system-config-info-after-windows-11-update
date: 2026-09-29
categories: ["windows-errors"]
tags: ["windows 11", "bad system config info", "windows update"]
description: "BAD_SYSTEM_CONFIG_INFO after a Windows 11 update? The update damaged your boot configuration data — here is how to rebuild it and boot again."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-after-windows-11-update.webp"
faqs:
  - q: "Will I lose my files to BAD_SYSTEM_CONFIG_INFO?"
    a: "No — the damage is in boot configuration and registry hives, not in your user data. Every fix in this guide (BCD rebuild, hive restore, update uninstall, System Restore) preserves personal files. Only a Reset with Remove everything would touch them, and that option is not needed for this error."
  - q: "What's the difference between the BCD and the registry hive here?"
    a: "The BCD (Boot Configuration Data) tells the bootloader where Windows is and how to start it — damage here stops the boot before Windows loads. The SYSTEM registry hive holds Windows' own configuration, read as Windows starts — damage here crashes the boot slightly later. This error covers both, which is why the guide repairs both."
  - q: "Why does this happen specifically after updates?"
    a: "Updates rewrite boot files and merge registry changes — they touch exactly the structures this error verifies. An interruption, a driver conflict, or a disk error during that rewrite window corrupts the new configuration. It is the most dangerous few minutes of the update process for boot integrity, which is why uninterrupted updates on AC power matter."
  - q: "The RegBack folder is empty. Now what?"
    a: "Windows 10/11 changed the automatic registry backup behavior, so RegBack is sometimes empty or zero-byte — that just means Fix 3 is unavailable, not that you are out of options. The BCD rebuild (Fix 2), update uninstall (Fix 4), and System Restore (Fix 7) do not depend on RegBack at all."
---

BAD_SYSTEM_CONFIG_INFO means the registry hive or boot configuration Windows needs to start is damaged or inconsistent. After a Windows 11 update, this typically happens when the update process was interrupted, when it collided with a driver, or when it wrote boot configuration data that does not match the actual system. Windows detects the inconsistency at boot and stops rather than start with a configuration it cannot trust.

The good news: this is one of the more repairable blue screens. The damage is in configuration data, not in your files, and the recovery environment contains every tool needed to rebuild it. Work from the automatic repairs down to the manual registry work in order.

## Why this happens

- **Interrupted update:** a forced shutdown, dead battery, or crash mid-update leaves the boot configuration half-written.
- **Corrupted BCD store:** the Boot Configuration Data took damage during the update's boot-file rewrite phase.
- **Damaged SYSTEM registry hive:** the update's registry merge went wrong, leaving the SYSTEM hive inconsistent.
- **Driver conflict during update:** a storage or chipset driver that disagrees with the new build breaks the configuration the update tried to write.
- **Disk errors in system areas:** bad sectors landing on the BCD or registry hives corrupt exactly the data this error checks.
- **Incorrect BIOS settings after update:** on some machines the update process (or a bundled firmware update) changes SATA mode or boot settings the configuration does not expect.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Let Startup Repair try first

The automated repair handles the simple variants of this error. Give it one proper shot.

1. Boot into **Automatic Repair** (three interrupted boots at the logo).
2. Go to **Advanced options > Troubleshoot > Advanced options > Startup Repair**.
3. Select your account, enter the password, and let it run uninterrupted.
4. If it succeeds, boot into Windows and immediately run **Settings > Windows Update** to let the update complete cleanly this time.
5. If it fails, click **Advanced options** to return to the menu — do not reboot into the loop. Continue below.

### Fix 2: Rebuild the BCD

The highest-success manual fix for this error. Rewrites the boot configuration the update damaged.

1. From **Troubleshoot > Advanced options**, open **Command Prompt**.
2. Run `bootrec /fixmbr`, `bootrec /fixboot`, and `bootrec /rebuildbcd` in sequence.
3. If `fixboot` gives Access Denied: `diskpart`, `list vol`, find the FAT32 EFI partition, `select vol N`, `assign letter=S:`, `exit`, then `bcdboot C:\windows /s S: /f UEFI`.
4. Answer **Y** to any add-installation prompts.
5. Type `exit`, choose **Continue**, and test the boot. This resolves the BCD-damage variant outright.

### Fix 3: Repair the registry hives from backup

When the BCD is fine but the SYSTEM hive is corrupt, restore it from Windows' automatic backup.

1. In the recovery command prompt, type `cd C:\Windows\System32\config` and press Enter.
2. Check for the backup: `dir RegBack` — if the files have real sizes (not 0), a usable backup exists.
3. Back up the current hives first: `md backup` then `copy * backup` (skip files that refuse).
4. Restore: `copy C:\Windows\System32\config\RegBack\SYSTEM C:\Windows\System32\config\SYSTEM` (confirm the overwrite). Repeat for SOFTWARE if needed.
5. Type `exit`, **Continue**, and boot. Note: the restore point is from the last successful boot, so very recent settings changes may revert — a small price for a working system.

### Fix 4: Uninstall the update that caused it

If the timeline is clear — update installed, then this error — remove the update from recovery.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. **Uninstall latest quality update** first, restart, test.
3. Still failing? Return and **Uninstall latest feature update** (20–40 minutes, do not interrupt).
4. Once booting, pause updates for a week: **Settings > Windows Update > Pause updates**.
5. Before unpausing, update storage and chipset drivers manually so the next attempt does not hit the same conflict. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with the KB.

### Fix 5: Check the disk and repair system files

Configuration damage that keeps recurring has a storage cause. Find it.

1. Recovery command prompt: `chkdsk C: /f /r`. Let it finish fully.
2. Then `sfc /scannow /offbootdir=C:\ /offwindir=C:\windows`.
3. Then `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Restart via **Continue**. If chkdsk found bad sectors in system areas, back up immediately after booting — the drive may be failing.
5. This error overlapping with disk problems is also covered from the boot-log angle in the [SrtTrail.txt guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-on-lenovo-laptop/) — the repair commands are cousins.

### Fix 6: Verify BIOS boot settings

A settings mismatch between BIOS and the boot configuration produces this exact error. Check the usual suspects.

1. Enter BIOS (**F2**/**Del** at boot, varies by brand).
2. Confirm **Boot Mode** is **UEFI** (not Legacy/CSM) if Windows was installed as UEFI — which it was on any modern laptop.
3. **SATA Mode** should be whatever it was at install time (usually **AHCI** or **Intel RST Premium**) — changing it after the fact breaks the boot configuration.
4. **Secure Boot** should be enabled for Windows 11 (it is a requirement).
5. Save, exit, and test. If a firmware update changed these without telling you, this fix feels like magic.

### Fix 7: System Restore or reset

The final options when manual repairs do not hold: roll back the system state, then reinstall if needed.

1. **Troubleshoot > Advanced options > System Restore** — pick the newest point before the update.
2. No restore point? **Troubleshoot > Reset this PC > Keep my files**.
3. After recovery, create a manual restore point before the next major update (**Create a restore point** in Start search) — future you will thank present you.
4. Then update drivers (chipset, storage) before letting Windows Update run the big update again.
5. If even a reset fails to hold, the drive itself is suspect — replace it rather than repair it a fourth time. The [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers reaching recovery if the boot menu itself becomes unreachable.

## Closing

BAD_SYSTEM_CONFIG_INFO after a Windows 11 update is configuration damage, and configuration damage is repairable: rebuild the BCD, restore the hives, remove the offending update, in that order. The error looks severe because it strikes at boot, but your files are untouched and the recovery tools are purpose-built for exactly this. Keep updates on AC power, keep restore points enabled, and this one stays a story rather than a saga.
