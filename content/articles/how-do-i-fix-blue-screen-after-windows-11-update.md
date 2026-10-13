---
title: "How to Fix a Blue Screen After a Windows 11 Update"
slug: how-do-i-fix-blue-screen-after-windows-11-update
date: 2026-09-22
categories: ["windows-errors"]
tags: ["blue screen", "windows 11 update", "bsod"]
description: "Blue screen right after a Windows 11 update? Follow this ordered fix guide: roll back the update, repair drivers, and stabilize your laptop again."
thumbnail: "/images/thumbs/how-do-i-fix-blue-screen-after-windows-11-update.webp"
faqs:
  - q: "Why does my laptop blue screen after a Windows 11 update?"
    a: "The update usually replaces a working driver with an incompatible one, or installs a patch that conflicts with existing software or firmware. Graphics, Wi-Fi, and storage drivers are the most common culprits, followed by antivirus tools and outdated BIOS firmware that cannot handle the new kernel changes."
  - q: "Can I uninstall a Windows 11 update that causes blue screens?"
    a: "Yes. Go to Settings > Windows Update > Update history > Uninstall updates, select the recent update, and uninstall it. For a feature update, Settings > System > Recovery > Go back lets you return to the previous Windows version within 10 days of the upgrade."
  - q: "What if my laptop won't boot after the update?"
    a: "Interrupt the boot process three times to reach the recovery environment, then use Troubleshoot > Advanced options. From there you can uninstall the latest quality or feature update, run Startup Repair, open System Restore, or use Command Prompt for manual repairs like `bootrec` commands."
  - q: "How do I stop Windows from reinstalling the bad update?"
    a: "After uninstalling it, go to Settings > Windows Update and pause updates for up to 5 weeks. For a driver update specifically, download Microsoft's 'Show or hide updates' troubleshooter to hide that driver so Windows Update skips it permanently."
---
Few things are more frustrating than a laptop that worked fine yesterday and blue-screens today, all because Windows decided to update overnight. The good news is that update-caused blue screens are among the easiest to fix, because the cause is fresh and reversible — you know exactly what changed.

The typical pattern: an update installs, the laptop restarts, and instead of your desktop you get a sad face, a stop code, and a reboot loop. Don't panic and don't reinstall Windows yet. There is a clear path from the bad update back to a working machine, and it starts with getting into the recovery environment.

## Why this happens

- **The update shipped an incompatible driver.** Windows Update often bundles driver updates for graphics, Wi-Fi, or storage controllers that conflict with your specific hardware.
- **A patch conflicts with third-party software.** Antivirus, disk encryption, and some VPN tools hook deep into the kernel; a new Windows build can break those hooks.
- **Outdated BIOS/UEFI firmware.** Major Windows updates expect modern firmware interfaces. An old BIOS can misreport hardware capabilities to the new kernel.
- **Corrupted update installation.** A power cut, full disk, or interrupted download can leave half-applied system files that crash on boot.
- **The update exposed an existing hardware issue.** Marginal RAM or a failing SSD can run fine for months and start crashing only when new code stresses them differently.
- **Insufficient disk space during the update.** When the update cannot stage its files properly, critical components end up incomplete or mismatched.

## How to fix it

Work through these in order — start with the quickest rollback options and move toward deeper repairs only if needed.

### Fix 1: Uninstall the problematic update from recovery

If Windows will not boot, the recovery environment lets you remove the update that broke things.

1. Force the recovery environment: power on the laptop and hold the power button to force it off during the Windows logo, three times in a row. The fourth boot should show **Automatic Repair**.
2. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
3. Choose **Uninstall the latest quality update** first; if the crash came after a big version upgrade, choose **Uninstall the latest feature update** instead.
4. Let the uninstall finish, then select **Continue** to restart into Windows normally.
5. If Windows boots cleanly now, you have confirmed the update was the trigger — the same logic applies to [black screens after updates](/articles/windows-11-black-screen-after-update-fix/), which often share the same root cause.

### Fix 2: Roll back the update from inside Windows

If you can reach the desktop, even in Safe Mode, the uninstall is quicker from Settings.

1. Open **Settings > Windows Update > Update history**.
2. Click **Uninstall updates** at the bottom of the page.
3. Find the most recent update by date, select it, and click **Uninstall**.
4. Restart when prompted and confirm the blue screens are gone.
5. Then pause updates: **Settings > Windows Update** and use **Pause updates** for a few weeks while Microsoft fixes the issue.

### Fix 3: Boot into Safe Mode and update the drivers manually

Safe Mode loads only basic drivers, which lets you reach the desktop and fix the driver the update broke.

1. From the recovery environment, go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. Open **Device Manager** (**Win + X > Device Manager**) and look for devices with yellow warning icons.
3. Right-click the flagged device, choose **Uninstall device**, and restart — Windows will load a basic driver.
4. Download the correct driver from your laptop maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) or the component vendor ([NVIDIA](https://www.nvidia.com/Download/index.aspx), [Intel](https://www.intel.com/content/www/us/en/support/detect.html)) and install it.
5. Never let Windows Update reinstall a known-bad driver — hide it with Microsoft's show/hide updates troubleshooter.

### Fix 4: Run Startup Repair and system file checks

If uninstalling the update did not help, the update may have damaged boot files or system components.

1. Boot to the recovery environment and open **Troubleshoot > Advanced options > Startup Repair**; let it run and restart.
2. If crashes continue, return to **Advanced options > Command Prompt** and run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` to check system files offline.
3. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` to repair the component store.
4. Restart and test. These two tools fix a large share of post-update boot crashes without touching your files.

### Fix 5: Use System Restore to a pre-update point

System Restore rolls back system files, drivers, and registry changes while leaving your personal files alone.

1. In the recovery environment, go to **Troubleshoot > Advanced options > System Restore**.
2. Pick a restore point dated before the problematic update installed.
3. Let the restore complete and restart the laptop.
4. If no restore points exist, enable protection now for next time: search for **Create a restore point** in the Start menu and turn on protection for your system drive.

### Fix 6: Check for firmware and BIOS updates

Sometimes the update is fine and your firmware is the weak link — especially after feature updates.

1. Find your exact laptop model on the manufacturer's support page.
2. Download the latest BIOS/UEFI update and follow the maker's instructions exactly — keep the charger plugged in and do not interrupt it.
3. While there, grab the latest chipset and storage drivers too, since updates often expect newer storage controller behavior.
4. After flashing, reapply the Windows update and see whether the crashes are gone. Firmware mismatches are also behind many [WHEA_UNCORRECTABLE_ERROR](/articles/whea-uncorrectable-error-windows-11-fix/) crashes on laptops.

### Fix 7: Reset Windows while keeping your files

If nothing else works, a reset reinstalls Windows cleanly and removes the broken update state entirely.

1. Boot to recovery and choose **Troubleshoot > Reset this PC**.
2. Select **Keep my files** — your documents, photos, and desktop files survive, though installed programs will be removed.
3. Choose **Cloud download** if you have decent internet; it pulls a fresh Windows image instead of reusing possibly damaged local files.
4. After the reset, install drivers from the manufacturer first, then let Windows Update run — this order prevents the bad-driver-first problem from repeating.

## Closing

Blue screens after a Windows 11 update are almost always a driver or firmware mismatch, not a dying laptop. Uninstall the offending update, fix the driver properly from the manufacturer's site, and pause updates until Microsoft sorts the issue out. Keep a System Restore point habit and a current BIOS, and the next update will be a lot less dramatic. If the crashes started with a specific stop code like [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED](/articles/how-do-i-fix-system-thread-exception-not-handled/), read that dump to name the driver before you roll anything back.
