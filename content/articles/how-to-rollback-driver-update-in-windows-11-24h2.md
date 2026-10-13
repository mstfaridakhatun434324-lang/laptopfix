---
title: "How to Roll Back a Driver Update in Windows 11 24H2"
slug: how-to-rollback-driver-update-in-windows-11-24h2
date: 2026-10-11
categories: ["drivers"]
tags: ["rollback driver", "windows 11 24h2", "drivers", "device manager", "guide"]
description: "A driver update broke something on Windows 11 24H2? Roll back to the previous driver version with Device Manager, restore points, and update blocking."
thumbnail: "/images/thumbs/how-to-rollback-driver-update-in-windows-11-24h2.webp"
faqs:
  - q: "How do I roll back a driver in Windows 11 24H2?"
    a: "Open Device Manager, right-click the device, choose Properties, go to the Driver tab, and click Roll Back Driver. Windows restores the previously installed version. If the button is grayed out, no previous driver is stored — use System Restore or manually install the older driver from the manufacturer instead."
  - q: "Why is the Roll Back Driver button grayed out?"
    a: "Windows only keeps one previous driver version, and only if the update happened through the normal driver-install path. Clean installs, DDU wipes, and manual .inf installs often don't preserve a rollback copy. Grayed-out means you'll need System Restore or a manual install of the older driver."
  - q: "Will Windows just reinstall the bad driver again?"
    a: "Yes, unless you stop it — Windows Update will happily re-offer the same driver. After rolling back, hide the driver update with the Show or hide updates troubleshooter or exclude drivers from Windows Update via policy. Otherwise you're fixing the same problem every Patch Tuesday."
  - q: "What's the difference between rolling back and uninstalling a driver?"
    a: "Rollback restores the specific previous version Windows has stored. Uninstall removes the current driver and lets Windows pick whatever it wants on reboot — often the same bad version. Rollback is the precise tool when you know the previous version worked; uninstall is for corrupt-driver situations where any fresh start helps."
---

Driver updates are supposed to help. Sometimes they do the opposite: the new GPU driver crashes games, the new Wi-Fi driver drops connections, the new audio driver kills sound. Windows 11 24H2 keeps rolling these out through Windows Update, and when one breaks your machine, you need the previous version back — quickly and permanently.

Rolling back is a built-in Windows capability, but it has sharp edges: it only works when Windows kept the old driver, and Windows will reinstall the bad one unless you block it. This guide covers the full procedure — rollback, alternatives when rollback isn't available, and the blocking step that makes it stick.

## Why this happens

- **Bad driver release:** the new version has a regression for your hardware.
- **Windows Update auto-install:** the driver arrived without your knowledge or consent.
- **Incompatible driver offered:** Windows Update served a driver not quite right for the variant.
- **Partial update:** the driver updated but its control software didn't, causing mismatch.
- **Firmware mismatch:** new driver expects firmware the device doesn't have.
- **Rollback data missing:** clean installs don't preserve previous versions.
- **Reinstallation loop:** Windows Update keeps re-applying the bad driver.
- **Wrong device targeted:** the update hit a similar-but-different device.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Roll back via Device Manager

1. Open Device Manager (**Win + X > Device Manager**) and find the problem device.
2. Right-click > **Properties** > **Driver** tab > **Roll Back Driver**.
3. Select a reason (any) and confirm. Windows restores the previous driver version.
4. Reboot when prompted, then verify the device works and check the driver version/date on the Driver tab.
5. This is the fastest path when it works — try it first, every time.
6. If the button is grayed out, skip to Fix 3 — no stored previous version exists.

### Fix 2: Confirm the rollback worked

1. After rebooting, reopen the device's **Properties > Driver** tab and check the version and date.
2. The date should be older than the bad update — that's your confirmation.
3. Test the actual symptom: the game that crashed, the Wi-Fi that dropped, the audio that died.
4. Give it a day of normal use before declaring victory — some driver regressions are intermittent.
5. Note the working version number somewhere — you'll need it if this ever recurs.

### Fix 3: Use System Restore when rollback is unavailable

1. Search **Create a restore point** > **System Restore** > choose a restore point from before the driver update.
2. System Restore reverts drivers, registry, and system files — it's the heavy-duty rollback.
3. Your personal files aren't touched, but recently installed programs may need reinstalling.
4. After restoring, verify the device's driver version is the pre-update one.
5. Create a fresh restore point once everything works — your new clean baseline.
6. If no restore point exists, enable System Protection now so you have one next time.

### Fix 4: Manually install the older driver

1. Find the previous driver version: check the manufacturer's driver archive for your device.
2. Download the older version and keep the installer file.
3. In Device Manager, **Uninstall device** (checking driver deletion), then install the downloaded older driver.
4. Or use **Update driver > Browse my computer** and point at the older driver's folder.
5. For GPUs, [NVIDIA's](https://www.nvidia.com/Download/index.aspx) and [AMD's](https://www.amd.com/en/support/download/drivers.html) archives keep old versions; Intel's assistant usually offers only the latest, so check the manual download center.
6. Verify the version on the Driver tab matches what you intended to install.

For the full manual-install technique — pointing Device Manager at an .inf folder, ordering multi-component packages, and handling unsigned drivers — our [manual OEM driver install guide](/articles/how-to-install-oem-drivers-manually-in-windows-11-24h2/) walks through the procedure in detail.

### Fix 5: Block Windows from reinstalling the bad driver

1. This step is mandatory — without it, the bad driver returns.
2. Download Microsoft's **Show or hide updates** troubleshooter and use it to hide the specific driver update.
3. Alternative: **Group Policy** (Pro) > Computer Configuration > Administrative Templates > Windows Components > Windows Update > "Do not include drivers with Windows Update" > Enabled.
4. Or set the device's **Device Installation Restrictions** policy to prevent driver updates for that specific hardware ID.
5. After blocking, check **Windows Update > Optional updates** to confirm the driver no longer appears.
6. Revisit after each Windows feature update — 24H2 updates can reset these policies.

### Fix 6: Handle special cases

1. **GPU drivers:** use DDU in Safe Mode before installing the older version — GPU driver remnants cause the most trouble.
2. **Wi-Fi drivers:** keep a USB tethering option or Ethernet handy; rolling back the Wi-Fi driver while offline-capable avoids stranding.
3. **Chipset drivers:** roll back cautiously — chipset drivers affect many devices; prefer the laptop vendor's known-good package.
4. **Printer drivers:** remove the printer fully (including the driver package in Print Management) before installing the older version.
5. When a driver is merely *unknown* rather than bad, [identifying unknown devices](/articles/best-way-to-fix-unknown-device-in-device-manager/) is the prerequisite step.

### Fix 7: Report and monitor

1. Report the bad driver to the hardware vendor — regressions get fixed faster with reports, and vendors track them.
2. Check the vendor's forums for others hitting the same regression — you're rarely alone, and workarounds surface there.
3. Periodically check for a *newer* driver that fixes the regression — don't stay on the old version forever.
4. When a fixed version appears, unhide the update and upgrade deliberately, with a restore point made first.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official rollback and update-hiding procedures.

## Closing

Driver rollback is a three-part maneuver: restore the working version, verify it, and block the bad one from returning. Most people do only the first part and wonder why the problem comes back monthly. The blocking step — hiding the update or excluding drivers from Windows Update — is what turns a temporary fix into a permanent one. Keep the working driver installer filed away, keep System Protection on, and bad driver updates become a fifteen-minute inconvenience instead of a recurring nightmare. For identifying which device a mystery driver belongs to before you roll it back, [unknown device identification](/articles/best-way-to-fix-unknown-device-in-device-manager/) shows the hardware-ID method.
