---
title: "Driver Updates Failing in Windows Update on Windows 11 (Fix)"
slug: how-to-fix-driver-updates-failing-in-windows-update-on-windows-11
date: 2026-09-26
categories: ["windows-update"]
tags:
  - windows 11
  - driver updates
  - windows update
  - device drivers
  - optional updates
description: "Driver updates failing on Windows 11? Use the Optional updates path, roll back bad drivers, and install vendor drivers to end the failure loop."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-on-windows-11.webp"
faqs:
  - q: "Where are driver updates in Windows 11 Settings?"
    a: >
      They live under Settings > Windows Update > Advanced options > Optional updates, in the Driver updates section. Unlike Windows 10, Windows 11 does not show driver updates on the main Windows Update page unless you open Optional updates. Ticking a driver there and clicking Download & install is the supported manual install path.
  - q: "Why does Windows 11 keep replacing my NVIDIA driver with an older one?"
    a: >
      Windows Update's catalog sometimes lists a WHQL-certified driver with a higher internal version number than NVIDIA's own release, so Windows considers its copy newer and installs it over yours. Prevent it by hiding that driver with wushowhide or disabling automatic driver updates after installing the vendor driver — your manually installed driver is almost always the better one.
  - q: "Is it safe to use wushowhide on Windows 11?"
    a: >
      Yes. The Show or hide updates troubleshooter works on Windows 11 and only blocks the specific driver package you select. Security and cumulative updates are unaffected, and you can unhide the driver at any time. It remains Microsoft's recommended tool for skipping a single problematic driver update.
  - q: "Do I need GeForce Experience or Intel DSA if Windows Update provides drivers?"
    a: >
      For graphics, Wi-Fi, and chipset drivers, the vendor tools are worth keeping. They deliver newer, better-tested drivers than the Windows Update catalog and handle the install cleanly. Let Windows Update cover everything else. This division of labor avoids most driver conflicts on Windows 11 laptops.
---

Windows 11 changed where driver updates live — they moved under Optional updates, the Device Manager dialogs look different, and the Settings app buries the history a click deeper. But the failure itself is the same old story: Windows Update downloads a driver, tries to install it, fails with a hex code, and tries again tomorrow.

What makes Windows 11 cases distinct is how often the operating system fights your manually installed drivers. You install the latest NVIDIA or Intel driver from the vendor, and Windows Update cheerfully replaces it with an older WHQL copy — which then fails because your hardware wants the newer one. The loop is Windows arguing with itself.

This Windows 11-specific guide breaks the cycle: find the failing driver, use the Optional updates path correctly, roll back bad swaps, and get the vendor driver installed so it stays.

## Why this happens

- **Windows replacing your newer vendor driver:** Windows 11 aggressively offers WHQL drivers that can be older than your manually installed vendor driver, then fails installing them — error 0x80070103.
- **Optional updates auto-installing bad drivers:** on Windows 11, checked optional driver updates install automatically and can push a mismatched package.
- **Driver rank and signature conflicts:** a driver whose signature or hardware-ID match is slightly off fails with 0x800F020B or 0x800F0247.
- **Corrupted DriverStore after upgrades:** in-place upgrades to Windows 11 can leave stale driver packages that poison fresh installs.
- **Firmware-level devices with no inbox driver:** fingerprint readers and special function keys on laptops sometimes have only vendor drivers, and the catalog copy fails.
- **Antivirus blocking driver staging:** real-time protection can quarantine driver .inf operations mid-install.
- **Low disk space breaking staging:** with under ~10 GB free on C:, driver staging fails and the install reports a generic error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Optional updates and install the driver manually

On Windows 11, driver updates live under Advanced options > Optional updates. The manual install there re-downloads cleanly and often succeeds where the background attempt failed.

1. Open Settings > Windows Update > Advanced options > Optional updates.
2. Expand Driver updates and look for the failing driver.
3. Tick it and click Download & install, then watch for the result.
4. If it succeeds, you are done. If it fails with the same code, continue — the package is the problem, not the method.

### Fix 2: Roll back a driver Windows wrongly replaced

If the failures started right after Windows swapped your working vendor driver, roll it back first — then stop Windows from doing it again.

1. Open Device Manager (Win + X > Device Manager), find the device, and open Properties.
2. On the Driver tab, click Roll Back Driver and choose a reason.
3. Reboot and confirm the device works on the previous driver.
4. Then follow our guide to [disable automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) so Windows stops re-replacing it.

### Fix 3: Install the vendor driver and block the Windows copy

The durable fix: put the manufacturer's driver in place, then hide Microsoft's older offering with wushowhide so the loop cannot restart.

1. Download the latest driver for your exact model from Dell, HP, Lenovo, or ASUS support.
2. For Intel graphics or Wi-Fi, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the right package automatically; NVIDIA and AMD users should use GeForce Experience or AMD Adrenalin.
3. Install the vendor driver as administrator and reboot.
4. Run the wushowhide troubleshooter, choose Hide updates, and tick the failing Windows Update driver.

### Fix 4: Uninstall the device cleanly in Device Manager

When the driver store holds a broken entry for the device, a full removal plus rescan clears what simple reinstalls cannot.

1. In Device Manager, right-click the device and choose Uninstall device.
2. Tick Attempt to remove the driver for this device if the option appears.
3. Click Action > Scan for hardware changes after rebooting.
4. Install the vendor driver from Fix 3 onto the clean detection.

### Fix 5: Pause updates to stop the bleeding

While you work, pause Windows Update so it stops re-downloading the bad driver every hour and interfering with your manual installs.

1. Go to Settings > Windows Update and click Pause for 1 week next to Pause updates.
2. Extend it if needed — you can pause up to five weeks.
3. Do your driver work in peace, then unpause and check for updates once.
4. This is a breathing-room tactic, not a solution — always unpause when done.

### Fix 6: Reset Windows Update components

A corrupted download cache makes every driver retry fail identically. Clearing it is the standard cure.

1. Open Terminal as administrator (Win + X > Terminal (Admin)).
2. Run: net stop wuauserv; net stop bits; net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old; ren C:\Windows\System32\catroot2 catroot2.old.
4. Restart the services, unpause updates, and check again.

### Fix 7: Repair the system image as the final step

If several different drivers fail, the problem is beneath the drivers — in the servicing stack or system image. Repair it.

1. In elevated Terminal run: DISM /Online /Cleanup-Image /RestoreHealth.
2. Follow with: sfc /scannow, then reboot.
3. Reinstall the vendor drivers once more and confirm update history is clean.
4. A driver that crashes the system rather than just failing to install is a different beast — see [fixing DRIVER_IRQL_NOT_LESS_OR_EQUAL after a Windows 11 update](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/).

## Closing

On Windows 11, driver update failures are usually Windows fighting your vendor drivers — an older WHQL copy failing against a newer installed one. The winning sequence is Optional updates first, rollback second, vendor driver plus wushowhide third. Do that and the loop ends permanently instead of pausing until next Tuesday. Your Windows 11 laptop then runs the drivers you chose — newer, vendor-validated, and stable — rather than whichever catalog copy Windows happened to prefer that week.
