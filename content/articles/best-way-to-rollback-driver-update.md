---
title: "Best Way to Roll Back a Driver Update on a Windows Laptop"
slug: best-way-to-rollback-driver-update
date: 2026-09-09
categories: ["drivers"]
tags: ["rollback driver", "driver update", "device manager", "windows 11"]
description: "A bad driver update broke something on your laptop? Learn the best way to roll back a driver update in Windows 11 and block it from reinstalling."
thumbnail: "/images/thumbs/best-way-to-rollback-driver-update.webp"
faqs:
  - q: "How do I roll back a driver update in Windows 11?"
    a: "Open Device Manager (Win + X), right-click the device, choose Properties, go to the Driver tab, and click Roll Back Driver. Windows restores the previously installed driver version and asks why you're rolling back — pick a reason and confirm. This only works if the device was updated recently and the old driver files are still present."
  - q: "What if the Roll Back Driver button is greyed out?"
    a: "A greyed-out Roll Back Driver button means Windows no longer has the previous driver package — the device was never updated through Windows, the old driver was purged, or the driver was installed fresh rather than updated. In that case, uninstall the device (checking delete driver software if offered), restart, and let Windows install its inbox driver, or install the older version manually from your manufacturer."
  - q: "Will Windows Update reinstall the bad driver after I roll it back?"
    a: "Very likely, yes. Windows Update treats driver versions as upgrades and will offer the newer driver again. To stop this, use the Show or hide updates troubleshooter to hide that specific driver update, or install the driver version you want from your laptop manufacturer's support page, which usually takes precedence over the Windows Update version."
  - q: "Is rolling back a driver safer than reinstalling it?"
    a: "Rolling back is faster and lower-risk because Windows simply reactivates the previously working driver package instead of changing the installation. Reinstalling (uninstall + fresh install) is more thorough but takes longer and requires you to have the right installer handy. Start with rollback; reinstall only if rollback fails or the old driver is gone."
---

A driver update that makes things worse is one of the most frustrating Windows experiences: everything worked yesterday, Windows Update installed a new graphics, audio, or Wi-Fi driver overnight, and now the screen flickers, the sound crackles, or the network drops. The good news is that Windows keeps the previous driver around specifically for this situation, and reverting takes about two minutes if you know where to look.

The rollback path is: confirm which driver changed, roll it back through Device Manager, verify the fix, then block the bad version from coming back. Do it in that order — skipping the blocking step is how people end up rolling back the same driver every Patch Tuesday. For situations where the device has no previous driver to return to, see our guide to [reinstalling your Wi-Fi driver the right way](/articles/best-way-to-reinstall-wifi-driver/), and for update-caused display problems, [fixing a display driver that stopped responding](/articles/how-to-fix-display-driver-stopped-responding-after-windows-11-update/).

## Why this happens

- **Windows Update pushes newer but buggier drivers**: Microsoft's driver catalog sometimes ships versions with regressions the vendor hasn't fully validated on your exact hardware.
- **OEM-specific hardware needs OEM drivers**: Generic vendor drivers (Realtek, Intel) can miss laptop-specific power or thermal tuning that the manufacturer's build includes.
- **The old driver was a better match**: On older laptops, a newer driver may target newer silicon and behave badly on yours.
- **Partial or interrupted driver installation**: A driver that installed while the laptop was sleeping or on low battery can leave mismatched binaries.
- **Driver conflicts after the update**: The new driver may fight with companion software — audio enhancements, GPU control panels, or network utilities.
- **Rollback data was purged**: Disk cleanup tools or storage sense sometimes delete the old driver package, leaving nothing to roll back to.
- **The "update" was actually a downgrade**: Occasionally Windows Update installs an older-signed driver over a newer manufacturer one, breaking features the newer driver added.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm which driver changed

Don't guess — check the evidence first.

1. Open **Settings** > **Windows Update** > **Update history** and scan the driver updates section for anything installed around the time the problem started.
2. Note the exact device and date. Problems that begin within a day of a driver update are almost always caused by that update.
3. Open **Device Manager** (**Win + X** > **Device Manager**), find the device, right-click > **Properties** > **Driver** tab, and check the **Driver Date** and **Driver Version** — compare with your memory of when things last worked.
4. Also check **Settings** > **System** > **Display** or the relevant settings page to confirm the symptom matches the driver (e.g., audio issues after an audio driver date change).

### Fix 2: Roll back the driver in Device Manager

The core move — two minutes, no downloads.

1. In **Device Manager**, right-click the problem device and choose **Properties**.
2. Go to the **Driver** tab and click **Roll Back Driver**. If the button is greyed out, skip to Fix 3.
3. Windows will ask why you're rolling back — select a reason (usually "previous version seemed more reliable") and click **Yes**.
4. Restart the laptop when prompted. The device will now run the previously installed driver.
5. Test the exact symptom that appeared after the update. If it's gone, the update was the cause — proceed to Fix 5 to block it.

### Fix 3: Uninstall and let Windows install its inbox driver

When there's no previous driver to roll back to.

1. In **Device Manager**, right-click the device and choose **Uninstall device**.
2. If you see the checkbox **Attempt to remove the driver for this device** (or "Delete the driver software"), check it — this purges the bad update's files.
3. Restart the laptop. Windows will detect the hardware and install its built-in inbox driver, which is older but heavily tested.
4. Test thoroughly. The inbox driver may lack advanced features (GPU control panels, audio enhancements), but it tells you whether the hardware itself is fine.
5. If the inbox driver works, decide: stay on it for stability, or move to Fix 4 for the manufacturer's version.

### Fix 4: Install the manufacturer's driver version

The long-term correct driver usually comes from your laptop maker, not Windows Update.

1. Identify your exact laptop model (check the sticker on the bottom or run `msinfo32` and note **System Model**).
2. Go to your manufacturer's support page — [Dell's support site](https://www.dell.com/support) (or HP's or Lenovo's equivalent) — and find your model.
3. Download the driver for the affected device, choosing the version dated *before* the problem started if multiple versions are listed.
4. Disconnect from the internet temporarily before installing, so Windows Update can't race you with the bad version.
5. Run the installer, restart, and verify. Manufacturer drivers include laptop-specific tuning and usually take precedence over Windows Update versions afterward.

### Fix 5: Block the bad driver from reinstalling

This is the step everyone skips — and the reason rollbacks "stop working."

1. Download Microsoft's **Show or hide updates** troubleshooter from [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) and run it.
2. Choose **Hide updates**, select the problematic driver update from the list, and confirm.
3. Hidden driver updates won't be offered again, so your rolled-back or manufacturer driver stays in place.
4. Re-check after major Windows feature updates (once or twice a year), which can reset hidden-update lists.
5. Alternatively, in **Settings** > **Windows Update** > **Advanced options**, review whether driver updates are included with quality updates and adjust to your preference.

### Fix 6: Use System Restore as a fallback

When rollback isn't available and uninstall doesn't help.

1. Type **Create a restore point** in Start search, open it, and click **System Restore**.
2. Choose **Choose a different restore point** and pick one dated before the driver update.
3. Review the affected programs list, then restore. The laptop will restart and revert system files and drivers to that point.
4. Note this doesn't touch personal files — only system state, drivers, and installed programs.
5. After the restore, immediately apply Fix 5 so the bad driver doesn't return on the next update check.

### Fix 7: Clean-install the driver with Display Driver Uninstaller (graphics only)

For GPU drivers that resist every other method.

1. Download DDU (Display Driver Uninstaller) and the known-good GPU driver version from your manufacturer or the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx).
2. Boot into Safe Mode (**Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now** > **Troubleshoot** > **Safe Mode**).
3. Run DDU, select your GPU brand, and choose **Clean and restart**.
4. After restart, install the downloaded driver version with the network still disconnected.
5. Verify with a stress test — play a video, run a game, or run the workload that crashed before.

## Closing

Rolling back a driver is one of the highest-leverage fixes in Windows troubleshooting: it takes minutes, it directly reverses the most common cause of sudden breakage, and it works precisely because Windows keeps the old driver for you. The discipline is in the follow-through — confirm the culprit, roll back, then block the bad version so you only do this job once.
