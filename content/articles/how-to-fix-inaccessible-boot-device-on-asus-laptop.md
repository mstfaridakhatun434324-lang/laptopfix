---
title: "How to Fix INACCESSIBLE_BOOT_DEVICE on an ASUS Laptop"
slug: how-to-fix-inaccessible-boot-device-on-asus-laptop
date: 2026-09-26
categories: ["windows-errors"]
tags: ["bsod", "boot-error", "asus"]
description: "Stuck on INACCESSIBLE_BOOT_DEVICE on your ASUS laptop? Follow these proven steps to get Windows booting again without losing your files."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-on-asus-laptop.webp"
faqs:
  - q: "What causes INACCESSIBLE_BOOT_DEVICE on ASUS laptops?"
    a: "Windows can't talk to the drive it booted from. On ASUS laptops the usual triggers are a storage driver update gone wrong, a BIOS storage mode change (AHCI vs RAID/Intel RST), a Windows update that replaced the boot driver, or a genuinely failing SSD. The error appears as a blue screen during the Windows logo."
  - q: "Will I lose my files fixing INACCESSIBLE_BOOT_DEVICE?"
    a: "Almost certainly not. The error means Windows can't reach the drive, not that the data is gone. Every fix here — Safe Mode boot, driver updates, boot repair — works on the system configuration while leaving your personal files untouched. Still, back up from a recovery USB if you get one successful boot."
  - q: "How do I get into Safe Mode on an ASUS laptop with this error?"
    a: "Interrupt the boot three times in a row: hold the power button to force shutdown while Windows is loading, and on the third boot Windows enters Automatic Repair. Go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 4 for Safe Mode or 5 for Safe Mode with Networking."
  - q: "Can a BIOS setting cause INACCESSIBLE_BOOT_DEVICE?"
    a: "Yes, and it's one of the most common causes on ASUS machines. If the SATA/NVMe storage mode was changed between AHCI and RAID (Intel RST Premium) — by a BIOS reset, update, or manual change — Windows boots with the wrong storage driver and throws this exact error. Setting it back to the original mode usually fixes it instantly."
---
You press the power button on your ASUS laptop, the logo appears, the spinner turns — and then a blue screen: INACCESSIBLE_BOOT_DEVICE. The laptop restarts and does it again. Your files are on that drive, your work is on that drive, and Windows suddenly can't find its way to any of it.

Take a breath — this error is about access, not destruction. Windows has lost the driver handshake with your storage, and in most cases the fix is a settings or driver repair that leaves your data exactly where it is. Here's how to work through it.

## Why this happens

- **Storage mode changed in BIOS** — ASUS BIOS updates or resets can flip the SATA/NVMe controller between AHCI and RAID (Intel RST). Windows only has the driver for the mode it was installed with, so the other mode is unreadable.
- **Bad storage driver update** — a Windows Update or ASUS Live Update that replaces the Intel RST or NVMe driver with an incompatible version breaks the boot chain.
- **Corrupted boot configuration data (BCD)** — the bootloader's record of where Windows lives gets damaged by a failed update or improper shutdown.
- **Failing SSD** — sectors holding boot-critical drivers go bad; the drive is readable in BIOS but Windows can't load from it reliably.
- **Windows update mid-installation crash** — if an update was applying driver changes when the machine lost power, the driver store ends up half-written.
- **Disk encryption driver conflict** — BitLocker or third-party encryption filter drivers that fail to load block access to the volume.

## How to fix it

Work through these in order — most people are fixed by step 2 or 3. You'll need to reach the Windows Recovery Environment (WinRE) for several steps.

### Fix 1: Check the storage mode in BIOS

This single setting fixes a surprising number of INACCESSIBLE_BOOT_DEVICE cases on ASUS laptops.

1. Power on and immediately start tapping **F2** (or **Del** on some models) to enter the BIOS/UEFI setup.
2. Press **F7** to switch to **Advanced Mode** if you land in the EZ Mode screen.
3. Navigate to **Advanced** > **SATA Configuration** (on newer models: **Advanced** > **VMD setup menu** or **PCH Storage Configuration**).
4. Note the current setting — **AHCI** or **RAID / Intel RST Premium**. Change it to the other option, then press **F10** to save and exit.
5. If Windows boots, you've found it — leave the setting where it works. If it still blue-screens, reboot, go back, and restore the original value before continuing to the next fix.

### Fix 2: Boot into Safe Mode and roll back the storage driver

Safe Mode loads a minimal driver set that often boots fine even when normal mode can't.

1. Force Windows into Automatic Repair: power on, and as soon as the ASUS logo with the spinner appears, hold the power button for 5 seconds to force shutdown. Repeat this three times.
2. On the fourth boot you'll see **Preparing Automatic Repair**, then **Choose an option** — select **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. After the restart, press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need internet).
4. Once in Safe Mode, press **Windows + X** and open **Device Manager**. Expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
5. Right-click the Intel chipset SATA/PCIe RST controller, choose **Properties** > **Driver** tab, and click **Roll Back Driver** if the button is active. Restart and test a normal boot.
6. If roll back isn't available, instead choose **Update driver** > **Browse my computer for drivers** > **Let me pick from a list** and select the older **Standard SATA AHCI Controller** driver.

### Fix 3: Rebuild the boot configuration data

A damaged BCD is repaired from the recovery command prompt.

1. Boot into Automatic Repair using the three-interrupted-boots method from Fix 2.
2. Go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
3. Run these commands one at a time, pressing Enter after each:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /scanos`
   `bootrec /rebuildbcd`
4. If `fixboot` reports "Access is denied," run `diskpart`, then `list vol`, note the EFI partition's letter (often hidden — assign one with `assign letter=Z:`), exit diskpart, and run `bcdboot C:\Windows /s Z: /f UEFI` (adjust the Windows drive letter if needed).
5. Type `exit`, choose **Continue** to restart, and see if Windows loads.

### Fix 4: Run Startup Repair and system file checks

Let Windows attempt its own repair, then verify system files.

1. From **Troubleshoot** > **Advanced options**, choose **Startup Repair** and let it run — it fixes common bootloader issues automatically.
2. If that doesn't resolve it, go back to **Command Prompt** and run:
   `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`
   (Replace C: with your Windows drive letter if different — check with `diskpart` > `list vol`.)
3. Then run `chkdsk C: /f /r` to scan the drive for bad sectors. This can take a while on large SSDs — let it finish.
4. Restart normally after both complete.

### Fix 5: Uninstall the latest Windows update from recovery

If the error started right after an update, remove it.

1. In WinRE, go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall latest quality update** first, restart, and test.
3. If the problem persists, go back and choose **Uninstall latest feature update** — this rolls back the bigger version upgrade.
4. Once you're booting again, pause updates for a few weeks: **Settings** > **Windows Update** > **Pause updates**, and check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) later for a revised driver.

### Fix 6: Check the SSD's health

If software fixes fail, the drive itself may be dying.

1. Boot into the BIOS (**F2** at power-on) and confirm the SSD still appears in the storage device list — if it's missing entirely, reseat it (power off, remove the bottom panel, unplug and replug the M.2 drive) or have it serviced.
2. If you can reach a command prompt in WinRE, run `wmic diskdrive get status` — anything other than **OK** means the drive is reporting failure.
3. ASUS laptops also include **MyASUS** diagnostics; if you can boot to a USB Windows installer, you can run the SSD manufacturer's toolbox from another PC by removing the drive.
4. A failing drive means replacement — but your data is often still recoverable by connecting the old SSD via a USB enclosure to another computer before it degrades further.

### Fix 7: Reinstall Windows keeping your files

The last resort that still preserves your data.

1. Create a Windows 11 USB installer on another PC using the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and the Media Creation Tool.
2. Boot your ASUS from the USB (tap **Esc** at power-on for the boot menu), choose your language, then **Install now**.
3. When asked, choose **Upgrade: Install Windows and keep files, settings, and applications** — this reinstalls Windows over itself without wiping your data.
4. After installation, install chipset and storage drivers from ASUS support for your exact model before running Windows Update.

## Closing

INACCESSIBLE_BOOT_DEVICE looks catastrophic but is usually a 15-minute fix once you know where to look — the BIOS storage mode and the storage driver are the culprits the vast majority of the time. Work the list in order, and don't skip the BIOS check just because you "didn't change anything": BIOS updates and resets change it for you. If you're seeing other stop codes alongside this one, our [step-by-step INACCESSIBLE_BOOT_DEVICE guide](/articles/how-to-fix-inaccessible-boot-device-step-by-step/) covers additional scenarios, and the general [blue screen of death fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) helps when the error keeps changing names between crashes.
