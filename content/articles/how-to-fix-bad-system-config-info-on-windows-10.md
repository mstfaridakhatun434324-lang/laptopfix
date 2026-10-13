---
title: "How to Fix Bad System Config Info on Windows 10"
slug: how-to-fix-bad-system-config-info-on-windows-10
date: 2026-09-01
categories: ["windows-errors"]
tags: ["bad system config info", "windows 10", "boot error"]
description: "BAD_SYSTEM_CONFIG_INFO stopping Windows 10 from booting? Repair the corrupted registry and boot configuration with this ordered guide."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-on-windows-10.webp"
faqs:
  - q: "What does BAD_SYSTEM_CONFIG_INFO mean?"
    a: "It means the Windows registry — particularly the SYSTEM hive that holds boot configuration — is corrupted. Windows cannot read the settings it needs to start, so it crashes. Common causes are failed updates, disk errors, bad RAM corrupting registry writes, and interrupted shutdowns."
  - q: "Can I fix this without reinstalling Windows?"
    a: "Usually yes. Automatic Repair, manual registry restoration from the RegBack folder, and the bootrec commands repair most cases without touching personal files. Reinstallation is the last resort, not the first step."
  - q: "Will my files survive these fixes?"
    a: "Yes. Registry repair, boot configuration rebuilds, SFC, DISM, and System Restore all leave personal files untouched. Only a clean install with drive formatting deletes data — and even the 'keep my files' reset preserves your documents."
  - q: "What if Automatic Repair can't fix it?"
    a: "Then move to manual repairs from the recovery Command Prompt: restore the registry hives from RegBack, run bootrec /rebuildbcd, and check the disk with chkdsk. The manual registry restore in particular fixes cases where Automatic Repair gives up."
---
BAD_SYSTEM_CONFIG_INFO is Windows 10 telling you its own configuration is unreadable — usually the registry's SYSTEM hive, which holds the boot-critical settings. Without it, Windows can't start, so you get this blue screen instead of a desktop. It sounds dire, but the registry keeps backups, and the boot configuration can be rebuilt. Most cases are repairable without reinstalling anything.

Because this error often prevents booting entirely, nearly all the fixes happen from the recovery environment. Get comfortable with **Troubleshoot > Advanced options** — that's your workshop for this repair.

## Why this happens

- **Corrupted SYSTEM registry hive.** The most direct cause — the registry file Windows needs at boot is damaged.
- **Failed Windows update.** Updates write heavily to the registry; an interrupted update corrupts it.
- **Disk errors.** Bad sectors landing on registry files produce exactly this crash.
- **Bad RAM.** Faulty memory corrupts registry data as Windows writes it — the corruption then persists on disk.
- **Driver conflicts writing bad config.** Buggy drivers can write invalid values into the system configuration.
- **Forced shutdowns during updates.** Power loss mid-write is the classic registry killer.

## How to fix it

Work through these in order from the recovery environment — least invasive first.

### Fix 1: Let Automatic Repair try first

Sometimes the built-in repair handles it alone.

1. Boot to the recovery environment — interrupt the boot three times, or boot from Windows 10 installation media and choose **Repair your computer**.
2. Go to **Troubleshoot > Advanced options > Startup Repair** (labeled Automatic Repair on some builds).
3. Let it run fully and restart when prompted.
4. If Windows boots, immediately back up important files and run `sfc /scannow` — then find what corrupted the registry before it happens again.

### Fix 2: Restore the registry from the RegBack backup

Windows keeps a backup of registry hives — restoring it fixes most BAD_SYSTEM_CONFIG_INFO cases.

1. In recovery, open **Troubleshoot > Advanced options > Command Prompt**.
2. First check whether a backup exists: run `dir C:\Windows\System32\config\RegBack` — you should see SYSTEM, SOFTWARE, SAM, SECURITY, and DEFAULT files with non-zero sizes.
3. Back up the current (corrupted) hives: `md C:\RegBackup` then `copy C:\Windows\System32\config\SYSTEM C:\RegBackup\` (repeat for SOFTWARE if you like).
4. Restore the backup: `copy C:\Windows\System32\config\RegBack\SYSTEM C:\Windows\System32\config\SYSTEM` and confirm the overwrite.
5. Type `exit`, choose **Continue**, and restart. If Windows boots, the registry restore was the fix.

### Fix 3: Rebuild the boot configuration data

If the registry is fine but boot data is damaged, rebuild it.

1. From the recovery Command Prompt, run these in order: `bootrec /fixmbr`, then `bootrec /fixboot`, then `bootrec /rebuildbcd`.
2. If `fixboot` reports access denied, run `diskpart`, then `list vol`, identify the EFI partition, assign it a letter with `assign letter=Z:`, exit diskpart, and run `bcdboot C:\Windows /s Z: /f UEFI`.
3. Restart and test. Boot configuration damage often accompanies registry corruption from the same failed update.

### Fix 4: Check and repair the disk

Registry corruption from disk errors will recur unless the disk is fixed.

1. From the recovery Command Prompt, run `chkdsk C: /f /r` — the `/r` locates bad sectors and recovers readable information.
2. This takes a while on large drives; let it complete.
3. Check SMART health afterward with your manufacturer's diagnostics or CrystalDiskInfo from a working boot.
4. A drive accumulating bad sectors needs replacing — no registry fix survives a dying disk for long. Disk faults also cause [UNEXPECTED_STORE_EXCEPTION](/articles/unexpected-store-exception-windows-11-fix/) errors.

### Fix 5: Test the RAM

If the registry keeps corrupting after repair, bad memory may be the writer.

1. From recovery or a working boot, run **Windows Memory Diagnostic**.
2. For certainty, run **MemTest86** from USB for a full pass.
3. Replace faulty RAM. Memory-caused registry corruption is insidious because every repair works temporarily — then the bad RAM corrupts the fresh registry again. The same faults produce [MEMORY_MANAGEMENT](/articles/memory-management-bsod-windows-11-fix/) blue screens.

### Fix 6: Use System Restore or uninstall updates

Roll back the change that damaged the configuration.

1. In recovery, go to **Troubleshoot > Advanced options > System Restore** and pick a point before the crashes.
2. Alternatively, use **Uninstall Updates** to remove the latest quality or feature update.
3. After restoring, pause updates briefly and verify stability for a few days before allowing updates again.
4. If a specific update caused it, the [update troubleshooting guide](/articles/troubleshoot-blue-screen-after-windows-11-update/) covers blocking the bad update permanently.

### Fix 7: Reset Windows keeping files

When the registry is unrecoverable, rebuild Windows around your data.

1. In recovery, choose **Troubleshoot > Reset this PC > Keep my files**.
2. Prefer **Cloud download** for a fresh image.
3. After the reset, verify the disk health (Fix 4) and RAM (Fix 5) before trusting the system — a reset on failing hardware just postpones the next crash.
4. Set up **System Protection** afterward so future registry damage is a five-minute System Restore instead of this ordeal.

### Fix 8: Rebuild the BCD store manually with bcdboot

When bootrec can't rebuild the boot data, bcdboot can recreate it from the Windows installation.

1. From the recovery Command Prompt, identify your Windows drive letter — in recovery it may not be C:. Run `diskpart`, then `list vol`, note the letters, and type `exit`.
2. Run `bcdboot D:\Windows` (replace D: with your actual Windows drive letter) to rebuild the boot files.
3. For UEFI systems, target the EFI partition explicitly: assign it a letter in diskpart (`assign letter=Z:`), then run `bcdboot D:\Windows /s Z: /f UEFI`.
4. Restart and remove the installation media. If Windows boots, immediately run `sfc /scannow` from the working system to repair any remaining corruption — and set up System Protection so the next registry problem is a quick [System Restore](/articles/troubleshoot-blue-screen-after-windows-11-update/) instead of a recovery-environment expedition.

## Closing

BAD_SYSTEM_CONFIG_INFO is a registry problem, and Windows keeps the tools to fix registry problems: Automatic Repair, the RegBack hive backup, and the bootrec commands. Work them in order from recovery, verify the disk and RAM so the corruption doesn't return, and keep System Restore enabled for next time. Your files survive all of it — this error attacks configuration, not data. For the broader recovery toolkit, Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document every option in the recovery environment.
