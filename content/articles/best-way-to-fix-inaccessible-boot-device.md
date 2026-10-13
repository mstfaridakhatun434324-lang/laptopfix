---
title: "The Best Way to Fix the Inaccessible Boot Device Blue Screen"
slug: best-way-to-fix-inaccessible-boot-device
date: 2026-09-10
categories: ["windows-errors"]
tags: ["inaccessible boot device", "bsod", "boot error", "windows 11"]
description: "Stuck on the INACCESSIBLE_BOOT_DEVICE blue screen? Here's the proven fix sequence — from BIOS storage modes to BCD rebuilds — that gets Windows booting again."
thumbnail: "/images/thumbs/best-way-to-fix-inaccessible-boot-device.webp"
faqs:
  - q: "What causes the Inaccessible Boot Device blue screen?"
    a: "Windows can't read the drive it boots from. The most common triggers are a BIOS storage mode flipped between AHCI and RAID, a failed Windows update that damaged the boot chain, a corrupt Boot Configuration Data store, or a dying drive. It almost always appears right after an update, a BIOS change, or new hardware."
  - q: "Will I lose my files when fixing this error?"
    a: "No — this is a boot problem, not a data problem. Your files sit untouched on the drive while Windows fails to start. Every fix below (BIOS corrections, BCD rebuild, update rollback) targets the boot process only. Only a clean reinstall would erase files, and that is the last resort, not the first step."
  - q: "Should I change AHCI to RAID in the BIOS?"
    a: "Only to restore what it was when Windows was installed. The rule is simple: the setting must match the mode used during installation. If you don't know which it was, try one, and if the error persists, try the other — switching back and forth is harmless as long as you don't reinstall in the wrong mode."
  - q: "What if none of the fixes work?"
    a: "If BCD rebuilds, update rollbacks, and BIOS corrections all fail, suspect the drive itself. Boot your manufacturer's diagnostics from F12 and run the full drive test. A failing drive explains a boot device Windows genuinely can't read — replace it, reinstall Windows, and restore your files from backup."
---

The INACCESSIBLE_BOOT_DEVICE blue screen is refreshingly honest: Windows is telling you exactly what went wrong — it can't read the drive it's supposed to boot from. Stop code 0x0000007B. Your files are still there; the boot chain that reaches them is broken. This error loves to appear at the worst moments: right after a Windows update, after a BIOS update or settings change, or after swapping hardware.

The good news is that the fix sequence is well mapped. Roughly speaking, the causes split into three buckets: a BIOS storage mode that changed (AHCI vs. RAID), boot data damaged by an update, or a drive that's actually failing. The first two are software-level and fixable in under an hour; the third means replacement hardware. This guide walks you through all three in the right order, starting from the recovery environment you're already landing in. If Windows boots but then hangs instead, our [restart screen fix guide](/articles/windows-11-stuck-on-restarting-screen-fix/) covers that adjacent problem.

## Why this happens

- **BIOS storage mode changed**: A BIOS update, reset, or manual change flipping between AHCI and RAID makes the installed Windows unable to talk to its own drive.
- **Failed Windows update**: Updates rewrite boot files; an interrupted or buggy update leaves the boot chain pointing nowhere.
- **Corrupt Boot Configuration Data (BCD)**: The BCD tells Windows where and how to start — damage it and every boot fails identically.
- **Storage driver problems**: A bad or missing chipset/storage driver, sometimes introduced by a driver update, breaks the handoff to the disk.
- **Failing drive**: Bad sectors or a dying controller mean Windows genuinely cannot read the boot device.
- **Changed drive configuration**: Moving the drive to a different slot, changing from UEFI to Legacy boot mode, or altering the boot order.
- **BitLocker or encryption conflicts**: On encrypted drives, a boot-chain change can trip the recovery key prompt or a boot failure if keys aren't accessible.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the BIOS storage mode first

This single setting causes the majority of cases.

1. Restart and enter the BIOS/UEFI — usually **F2** or **Del** on Dell, HP, and Lenovo laptops (watch the boot screen for the prompt).
2. Find the storage/SATA settings — look under **Advanced**, **Storage**, or **System Configuration** for "SATA Operation," "SATA Mode," or "Storage Controller."
3. Note the current value (AHCI, RAID On, or IDE). If you know Windows was installed with the other mode, switch it back.
4. If you don't know which it was, try the other setting — save, exit, and boot. Switching between AHCI and RAID is harmless to your data; pick whichever one boots.
5. While in the BIOS, confirm the boot mode is **UEFI** (not Legacy/CSM) and that your Windows drive appears in the boot priority list at all — a drive missing from the list entirely points to hardware.

### Fix 2: Boot into the recovery environment

If Fix 1 didn't solve it, you'll do the remaining work from Windows Recovery.

1. Power the laptop off and on three times during the Windows logo to force **Automatic Repair**, then click **Advanced options**.
2. Alternatively, boot from Windows installation USB media (create one with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11)) and choose **Repair your computer**.
3. From the recovery menu you have access to **Startup Repair**, **Command Prompt**, and **Uninstall Updates** — the tools for the next fixes.

### Fix 3: Roll back the latest update

If the error started within a day or two of an update, this is very likely the fix.

1. In recovery, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first — it's the quicker, more common culprit.
3. Restart and test. If the error persists, return and try **Uninstall the latest feature update**.
4. Once booted, pause updates (**Settings** > **Windows Update** > **Pause updates**) and check [Microsoft's support pages](https://support.microsoft.com/en-us/windows) for known boot issues with that update before allowing it again.

### Fix 4: Rebuild the BCD and boot files

The definitive fix for corrupted boot data.

1. From recovery, open **Command Prompt** (**Troubleshoot** > **Advanced options** > **Command Prompt**).
2. Run these in order:
   - `bootrec /fixmbr`
   - `bootrec /fixboot` (if you get "Access is denied," continue anyway — the bcdboot step below handles it)
   - `bootrec /scanos`
   - `bootrec /rebuildbcd`
3. If `rebuildbcd` finds no installations, rebuild manually: run `diskpart`, then `list vol` to find the FAT32 **EFI** partition; `select vol N` (its number), `assign letter=Z:`, `exit`; then `bcdboot C:\Windows /s Z: /f UEFI`.
4. Verify your Windows drive letter first — in recovery it may show as **D:** or **E:**, so check with `dir C:` before running bcdboot.
5. Type `exit`, choose **Continue**, and boot.

### Fix 5: Run Startup Repair and check the disk

Let the automated tools have a turn, and verify the hardware.

1. In recovery, go to **Troubleshoot** > **Advanced options** > **Startup Repair** and let it run — it's limited, but occasionally resolves exactly this.
2. Then open **Command Prompt** and run `chkdsk C: /f /r` (adjusting the drive letter to your Windows drive as in Fix 4).
3. Let the full scan complete. Growing bad-sector counts mean a dying drive — skip to Fix 7.
4. If chkdsk is clean, the drive is readable and the problem was software — Fix 4's BCD rebuild plus Fix 3's update rollback covers nearly all remaining cases.

### Fix 6: Update or reinstall the storage driver from recovery

A damaged storage driver can break the disk handoff even when everything else is fine.

1. If you can boot into Safe Mode (recovery > **Startup Settings** > **Restart** > **4**), open **Device Manager** and expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
2. Right-click your storage controller, choose **Uninstall device**, and restart — Windows will install its inbox driver.
3. If Safe Mode won't boot, download the latest storage/chipset driver for your exact laptop model from the vendor (for example, [Dell's support site](https://www.dell.com/support)), put it on a USB stick, and use the recovery Command Prompt's `drvload` or the driver update path from installation media.
4. After any driver change, double-check the BIOS storage mode from Fix 1 still matches — driver and BIOS mode must agree.

### Fix 7: Test the drive and reinstall as a last resort

When software fixes fail, the hardware is telling the truth.

1. Boot your laptop's built-in diagnostics (usually **F12** > **Diagnostics** on Dell, **F2** on HP, **F10** > **Diagnostics** on Lenovo) and run the full hard drive test.
2. If the drive fails: back up immediately. Connect the drive to another PC via a USB adapter or boot a Linux live USB to copy files off before total failure.
3. Replace the drive, reinstall Windows from USB media, and restore from backup.
4. If the drive passes but nothing boots, the partition table itself may be damaged — at that point a clean install (deleting all partitions) is the pragmatic endgame.

## Closing

INACCESSIBLE_BOOT_DEVICE sounds catastrophic, but it resolves to one of three stories: the BIOS flipped a storage setting, an update damaged the boot chain, or the drive is failing. The first two are fixed in well under an hour with the steps above; the third requires a new drive but is confirmed by diagnostics rather than guesswork. The discipline that matters is not reinstalling Windows until you've checked the BIOS mode and rebuilt the BCD — most people who jump straight to a reinstall later discover it was a one-setting BIOS fix all along. For the related case where Windows boots into Safe Mode fine but crashes normally, our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) shows how to use that foothold.
