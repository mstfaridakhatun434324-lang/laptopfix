---
title: "Blue Screen After a Windows 11 Update: Troubleshooting Guide"
slug: blue-screen-after-windows-11-update-troubleshooting
date: 2026-09-08
categories: ["windows-errors"]
tags: ["bsod", "windows update", "windows 11"]
description: "Blue screen right after a Windows 11 update? The update likely broke a driver or system file. Here's how to roll back and stabilize."
thumbnail: "/images/thumbs/blue-screen-after-windows-11-update-troubleshooting.webp"
faqs:
  - q: "Why would a Windows update cause a blue screen?"
    a: "Updates replace drivers, kernel components, and system files. If a new driver is incompatible with your hardware, if the update installed incompletely, or if it conflicts with third-party software (antivirus, encryption), the system can crash on boot or during use."
  - q: "Should I uninstall the update or wait for a fix?"
    a: "If the blue screens started immediately after the update and make the laptop unusable, uninstall it — waiting doesn't help when you can't work. You can reinstall the update later once Microsoft or your manufacturer ships a fixed driver."
  - q: "What if I can't boot into Windows to uninstall the update?"
    a: "Use the recovery environment: force-power-off three times during boot to reach Automatic Repair, then Troubleshoot > Advanced options > Uninstall Updates. Both quality and feature updates can be removed from there without booting Windows."
  - q: "How do I stop the bad update from reinstalling?"
    a: "Pause updates for 1-4 weeks in Settings > Windows Update, and use Microsoft's 'Show or hide updates' troubleshooter (wushowhide.diagcab) to hide the specific update. For drivers, this prevents Windows Update from reimposing the bad version."
---

Few things are more frustrating than a Windows update — something meant to improve your laptop — leaving it blue-screening. The pattern is distinctive: everything worked yesterday, the update installed overnight, and now you get stop codes on boot, on login, or randomly during use.

The good news: update-caused crashes are among the most fixable, because the cause has a timestamp. You know exactly what changed. The fixes below undo that change methodically, from least to most invasive.

## Why this happens

- **Incompatible driver pushed by the update**: Windows Update installs a new driver version (graphics, Wi-Fi, storage) that doesn't work with your hardware.
- **Incomplete or interrupted update**: Power loss or forced shutdown mid-update leaves system files half-replaced.
- **Third-party software conflict**: Antivirus, disk encryption, or VPN kernel drivers that worked before break under the new build.
- **Corrupted update download**: A damaged update package installs broken files.
- **Firmware mismatch**: The new Windows build expects BIOS/firmware behavior your current firmware doesn't provide.
- **Insufficient disk space during update**: Updates need breathing room; a full drive causes partial application and corruption.

## How to fix it

Work through these in order — start by undoing the update, then stabilize.

### Fix 1: Uninstall the latest quality update

If a cumulative update caused it, removing it is the fastest fix.

1. Open **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Find the most recent update (check the install date against when crashes began) and uninstall it.
3. Restart and test for a day. If crashes stop, you've confirmed the cause.
4. Can't boot? Force Automatic Repair (power off three times during the Windows logo), then **Troubleshoot** > **Advanced options** > **Uninstall Updates** > **Uninstall latest quality update**.
5. Our [Automatic Repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-youtube/) covers the full recovery-environment workflow if you're stuck at boot.

### Fix 2: Roll back the offending driver

Often it's not the update's system files but the driver it bundled.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. For each recently updated device (graphics, network, storage), right-click > **Properties** > **Driver** tab > **Roll Back Driver**.
3. If roll-back is greyed out, uninstall the device (check **Delete the driver software**), restart, and install the manufacturer's version from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
4. Block the bad driver with the **Show or hide updates** troubleshooter so Windows Update doesn't reinstall it.
5. For graphics specifically: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 3: Pause updates and hide the bad one

Don't let Windows reinstall the problem while you stabilize.

1. Go to **Settings** > **Windows Update** and **Pause updates** for 2-4 weeks.
2. Download Microsoft's **Show or hide updates** troubleshooter (`wushowhide.diagcab`), run it, and hide the problematic update.
3. Use the pause period to check your manufacturer's support page and community forums for a fixed driver or BIOS.
4. When you unpause, install updates one at a time with a restore point before each (see Fix 6).

### Fix 4: Repair system files damaged by the update

A bad update can corrupt files beyond what uninstalling removes.

1. Open an elevated Command Prompt (**Win + S**, type `cmd`, right-click > **Run as administrator**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store using Windows Update as the source.
3. Then run `sfc /scannow`.
4. Restart and test. If DISM fails because the update broke the servicing stack, run it with installation media as the source — see Microsoft's documentation on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 5: Remove conflicting third-party software

If crashes persist after rollback, something installed is fighting the new build.

1. Temporarily uninstall third-party antivirus — its kernel drivers are the most common conflict. Defender takes over automatically.
2. Uninstall or update VPN clients, disk encryption tools, and system utilities with kernel drivers.
3. Clean-boot to confirm: **Win + R** > `msconfig` > **Services** tab > check **Hide all Microsoft services** > **Disable all**; then Task Manager > **Startup** > disable all. Restart and test.
4. Re-enable in halves to identify the conflicting program, then check its vendor for a compatible version.

### Fix 6: Create restore points and update BIOS

Stabilize the platform so the next update attempt succeeds.

1. Update your BIOS from the manufacturer's support site — update-related crashes are frequently fixed by firmware released alongside the Windows build.
2. Free up disk space: **Settings** > **System** > **Storage** > **Cleanup recommendations**. Aim for at least 20 GB free before any feature update.
3. Create a manual restore point before future updates: **Win + R** > `sysdm.cpl` > **System Protection** tab > **Create**.
4. When ready to try the update again, install it manually and watch for the first sign of trouble — you'll know within a day whether it's safe.

### Fix 7: In-place upgrade as the final repair

If the system is still unstable after rollback and repairs, refresh Windows without losing files.

1. Download the [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) on a working PC and create a USB installer.
2. Boot the USB, or run `setup.exe` from within Windows if it boots.
3. Choose **Upgrade this PC** / keep personal files and apps.
4. This reinstalls Windows cleanly over the broken update state, replacing all system files and the driver store.
5. Afterward, install drivers from the manufacturer before letting Windows Update run wild.

For stop-code-specific help once you've stabilized, see our guides on [DRIVER_POWER_STATE_FAILURE after updates](/articles/how-to-fix-driver-power-state-failure-after-windows-11-update/) and [MEMORY_MANAGEMENT after updates](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/).

## Closing

A blue screen after a Windows update is annoying, but it's also one of the most diagnosable crashes you'll encounter — the timeline tells you exactly where to look. Uninstall the update, roll back its drivers, block the bad version, and repair any damage it left behind. Then update your BIOS, free up space, and set a restore point before trying again. The update isn't the enemy; the untested driver it carried is.
