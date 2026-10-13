---
title: "How to Fix the INACCESSIBLE_BOOT_DEVICE Blue Screen on Windows"
slug: inaccessible-boot-device-blue-screen-error-fix
date: 2026-10-05
categories: ["windows-errors"]
tags: ["blue screen", "boot error", "inaccessible boot device", "windows 11", "startup repair"]
description: "INACCESSIBLE_BOOT_DEVICE means Windows lost access to your drive during boot. Here's how to fix it with Startup Repair, bootrec, and driver fixes."
thumbnail: "/images/thumbs/inaccessible-boot-device-blue-screen-error-fix.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "It means Windows started loading but lost access to the system drive partway through boot. Common triggers are a corrupted storage driver, a bad boot configuration, a failed Windows update, or BIOS/UEFI storage mode (AHCI/RAID) changes. The files are usually fine — Windows just can't reach them."
  - q: "Can I fix INACCESSIBLE_BOOT_DEVICE without losing my files?"
    a: "Almost always, yes. This error is a driver or boot configuration problem, not data loss. Startup Repair, rebuilding the BCD, and restoring the right storage driver all fix the issue without touching your personal files. A clean install is only a last resort."
  - q: "Why did this happen right after a Windows update?"
    a: "Updates sometimes replace or reset the storage controller driver (like Intel RST or the NVMe driver) with a version that doesn't match your hardware. The fix is to boot into Safe Mode or WinRE and reinstall the correct driver from your laptop manufacturer's support site."
  - q: "How do I get into recovery mode when my PC won't boot?"
    a: "Interrupt the boot three times in a row — hold the power button during the Windows logo until it shuts off. On the third attempt, Windows loads WinRE (Automatic Repair). You can also boot from a Windows USB installer and choose Repair your computer."
---

Seeing the **INACCESSIBLE_BOOT_DEVICE** stop code on a blue screen is one of the more nerve-wracking Windows errors, because it shows up before you can even reach the desktop. The good news is that in most cases your data is completely fine — Windows simply lost the ability to talk to your drive during startup.

This is one of those problems where the fix order matters. Work through the steps below from least destructive to most destructive, and there's a very good chance you'll be back in Windows without losing a single file. If your laptop is stuck in a restart loop rather than a single blue screen, our guide to [fixing Windows 11 boot loops](/articles/how-to-fix-windows-11-boot-loop-step-by-step/) covers the loop-specific angles.

## Why this happens

- **Storage driver mismatch:** Windows updated or replaced your SATA/NVMe/RAID controller driver with a version that doesn't match your hardware, so it can't mount the drive mid-boot.
- **BIOS/UEFI storage mode changed:** If the SATA controller mode was flipped between AHCI and RAID (or Intel RST with Optane), Windows can't find the boot volume with the driver it has loaded.
- **Corrupted Boot Configuration Data (BCD):** A failed update, power cut, or disk error damaged the boot files that tell Windows where the system drive lives.
- **Pending Windows update damage:** An update that failed partway through can leave boot-critical drivers in a half-installed state.
- **Disk or file system corruption:** Bad sectors or file system damage on the system partition can block Windows from reading what it needs to finish booting.
- **BitLocker + hardware change:** On some laptops, a firmware change or driver update can trigger a BitLocker recovery prompt that looks like a boot failure if you don't have the key.

## How to fix it

Work through these in order — each step is slightly more involved than the last, and you should stop as soon as Windows boots normally.

### Fix 1: Boot into the Windows Recovery Environment

Before you can repair anything, you need WinRE — and Windows is good at getting you there on its own.

1. Power on your laptop and, as soon as you see the Windows logo or spinning dots, press and hold the power button until it shuts off.
2. Repeat this **two more times** (three interrupted boots total).
3. On the next start, Windows should load **Automatic Repair** instead of crashing.
4. Click **Advanced options**, then **Troubleshoot**, then **Advanced options** again to see the repair tools.

If your PC never offers Automatic Repair, boot from a Windows 11 USB installer (create one with the [Windows 11 download tool](https://www.microsoft.com/en-us/software-download/windows11)), choose your language, and click **Repair your computer** instead of Install.

### Fix 2: Run Startup Repair

This is the automated first attempt, and it genuinely fixes simple boot file problems.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows installation and your administrator account (enter the password if asked).
3. Let it run — it can take 5–15 minutes. If it says it couldn't repair your PC, that's fine; continue to the next fix. It hasn't changed anything harmful.

### Fix 3: Check your BIOS storage mode (AHCI vs RAID)

This is the single most common cause I've seen after hardware changes or BIOS updates.

1. Restart and enter BIOS/UEFI setup (usually **F2**, **Del**, or **F12** during the manufacturer's logo — on some laptops it's the **Novo button** or **F10**).
2. Find the storage or SATA controller setting, often under **Advanced > SATA Configuration** or **Storage**.
3. Note the current value. If it's **RAID** or **Intel RST Premium**, try switching to **AHCI**; if it's already AHCI and Windows was installed in RAID mode, try switching back. Change only one thing at a time.
4. Save and exit (usually **F10**), then try booting.

**Warning:** only change this if you suspect it was changed (after a BIOS update or someone poking around in settings). If Windows was installed in one mode, it needs that same mode. If you're not sure, your laptop maker's [support page](https://www.dell.com/support) usually documents the factory default.

### Fix 4: Rebuild the Boot Configuration Data

From WinRE's **Command Prompt** (Troubleshoot > Advanced options > Command Prompt), run these in order:

1. `bootrec /fixmbr` — rewrites the master boot record. Safe and quick.
2. `bootrec /fixboot` — if you get "Access is denied," first run `diskpart`, then `list vol`, note the EFI partition's letter, `sel vol <n>`, `assign letter=S:`, `exit`, then `bcdboot C:\Windows /s S: /f UEFI`.
3. `bootrec /scanos` — checks which Windows installations it can see.
4. `bootrec /rebuildbcd` — rebuilds the boot list from what it found. Type **Y** when it asks to add an installation.

Close Command Prompt and choose **Continue** to restart. If Windows boots, you're done.

### Fix 5: Check the disk and system files

Still in the WinRE Command Prompt:

1. Run `chkdsk C: /r` (your system drive might be D: in WinRE — check with `diskpart` > `list vol` first). This finds bad sectors and repairs file system errors. It can take a while on large drives; let it finish.
2. Then run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` to repair protected system files offline. Adjust the drive letter to match yours.

Reboot and test. Disk errors are also a frequent cause of other stop codes like [memory management crashes](/articles/how-to-fix-memory-management-bsod-in-windows-11-24h2/), so it's worth ruling them out here.

### Fix 6: Roll back the storage driver in Safe Mode

If the error started after a Windows update, the storage driver is the prime suspect.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. If Safe Mode loads, right-click **Start** and open **Device Manager**.
3. Expand **Storage controllers** (and **IDE ATA/ATAPI controllers**), right-click the controller (e.g., Intel Chipset SATA/PCIe RST or Standard NVM Express Controller), and choose **Properties**.
4. On the **Driver** tab, click **Roll Back Driver** if it's available. If not, click **Uninstall device** (check "attempt to remove the driver" only if you have the replacement ready), then restart and let Windows reinstall the inbox driver.
5. For the most reliable result, download the storage driver for your exact model from your manufacturer's support site (e.g., [Lenovo Support](https://support.lenovo.com/us/en/)) using another computer, copy it over on USB, and install it in Safe Mode.

### Fix 7: Undo the last Windows update

1. In WinRE, go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. First choose **Uninstall latest quality update**, restart, and test.
3. If it still crashes, repeat and choose **Uninstall latest feature update**.

This is safe — it just rolls the system back to before the update that likely broke the driver.

### Fix 8: Reset Windows while keeping your files

If nothing above works, this is the last stop before a clean install.

1. In WinRE, go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files**, then **Local reinstall** (cloud download is fine too if your internet is fast).
3. Follow the prompts. This reinstalls Windows, keeps your personal files, but removes installed programs — so you'll need to reinstall apps afterward.

## Closing

INACCESSIBLE_BOOT_DEVICE almost always comes down to one of three things: a wrong storage driver, a wrong BIOS storage mode, or damaged boot files — and all three are fixable without touching your data. The bootrec/BCD rebuild in Fix 4 and the storage driver rollback in Fix 6 resolve the vast majority of cases I see. If you've tried everything and it still won't boot, run your manufacturer's hardware diagnostics (most have a boot-time diagnostic via F12 or a dedicated key) to rule out a dying SSD before reinstalling Windows.
