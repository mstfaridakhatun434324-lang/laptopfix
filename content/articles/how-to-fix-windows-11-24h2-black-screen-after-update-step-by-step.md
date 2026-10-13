---
title: "Windows 11 24H2 Black Screen After Update: Step-by-Step Recovery"
slug: how-to-fix-windows-11-24h2-black-screen-after-update-step-by-step
date: 2026-09-23
categories: ["windows-update"]
tags:
  - black screen
  - windows 11 24h2
  - windows update
  - step-by-step
  - recovery
description: "Black screen after installing Windows 11 24H2? Follow this step-by-step recovery: from the 60-second checks to Safe Mode, driver rollback, and WinRE repair."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-black-screen-after-update-step-by-step.webp"
faqs:
  - q: "How do I know if the black screen is the update still installing?"
    a: >
      Check for signs of life: drive activity light blinking, fan noise changing, heat from the vents, and the Caps Lock light toggling when pressed. These mean Windows is working behind the black screen — give it up to an hour. A completely silent, cold machine with a frozen display and no keyboard response for 30+ minutes is genuinely stuck.
  - q: "What does Win + Ctrl + Shift + B do?"
    a: >
      It restarts the graphics driver without rebooting Windows — you will hear a beep and the screen may flicker. It is the fastest fix when the OS is running but the display pipeline wedged, which is exactly what happens when an update swaps in a bad GPU driver. It cannot harm anything, so it is always worth trying first.
  - q: "Will uninstalling the 24H2 update delete my files?"
    a: >
      No. Uninstalling a feature update from WinRE rolls back system files, drivers, and settings to the pre-update state but leaves your personal files, installed programs, and documents untouched. It is one of the safest recovery operations in Windows, which is why it appears before the more drastic options in this guide.
  - q: "Why does Safe Mode work when normal boot gives a black screen?"
    a: >
      Safe Mode loads Microsoft's basic display driver instead of your GPU's full driver, bypassing the broken driver the update installed. That contrast is itself the diagnosis: if Safe Mode shows a picture, the GPU driver is the problem, and rolling it back or reinstalling the vendor's version is the fix.
---

The update finished, the laptop rebooted, and now there is nothing — no login screen, no cursor, just a black display with the fan humming. A black screen after the Windows 11 24H2 update is one of the most alarming things a laptop can do, and also one of the most fixable. In the large majority of cases your files and Windows itself are fine; the machine simply cannot get a picture to the screen.

The causes cluster tightly: a display driver that the update replaced with a broken one, an external display confusing the output, or the update stalling before the login screen loads. Each has a distinct fix, and the order matters — you always rule out the trivial before rebuilding anything.

Work through these steps exactly as written. Most black screens resolve by Fix 4 without touching your data.

## Why this happens

- **Broken display driver from the update:** 24H2 sometimes replaces a working vendor graphics driver with a generic or mismatched one that cannot initialize the laptop panel.
- **Output routed to a phantom external display:** the update can reset display topology and send the picture to an HDMI port with nothing — or something sleeping — attached.
- **Update stalled before login:** the machine may actually still be finishing the update behind the black screen, especially on slower drives.
- **Fast Startup resuming a bad graphics state:** hybrid shutdown can restore a corrupted display driver state on every boot, making the black screen perfectly repeatable.
- **Peripheral confusing the boot:** docks, USB-C adapters, and external GPUs can hang the display handoff during the first post-update boot.
- **Corrupted user profile or shell:** rarely, the update damages the login shell so Windows loads but cannot draw the desktop.
- **BIOS/display firmware mismatch:** on some models the new OS build expects firmware behavior the old BIOS does not provide, breaking panel initialization.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out a still-running update and wake the display

Before assuming breakage, confirm the machine is truly stuck and try the built-in display reset shortcut — it fixes a surprising number of black screens instantly.

1. Wait a full 30 minutes with the charger plugged in — 24H2 can sit black while finalizing.
2. Press Win + Ctrl + Shift + B to restart the graphics driver; listen for a beep and watch for a flicker.
3. Press Caps Lock and check whether the keyboard light toggles — if it does, Windows is alive behind the black screen.
4. If the light toggles but the screen stays black after the shortcut, continue — the OS is running and only the display path is broken.

### Fix 2: Disconnect everything and force a clean boot

External displays and docks are the second most common cause. Strip the machine to its bare panel and give it one clean boot.

1. Hold the power button 10 seconds to force off, then unplug every USB device, dock, HDMI cable, and SD card.
2. Unplug the charger, wait 30 seconds, reconnect only the charger.
3. Power on and watch the panel — manufacturer logo means the display path works.
4. If it boots to login now, reconnect devices one at a time to find the offender.

### Fix 3: Boot into Safe Mode and roll back the display driver

Safe Mode loads a basic display driver, which is why the screen usually works there. From inside, you can remove the driver update that broke the panel. If the screen stays black even in Safe Mode, skip to Fix 5.

1. Interrupt startup three times (power off at the logo) to reach Automatic Repair, then Advanced options.
2. Go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 4 for Safe Mode.
3. In Safe Mode open Device Manager, expand Display adapters, right-click your GPU, and choose Properties > Driver > Roll Back Driver.
4. If rollback is greyed out, choose Uninstall device (keep the driver files), reboot normally, and let Windows reinstall.

### Fix 4: Uninstall the 24H2 update from Safe Mode or WinRE

When the black screen started the exact boot after 24H2 installed, removing that update is the most direct fix — and your files are untouched.

1. In WinRE go to Troubleshoot > Advanced options > Uninstall Updates.
2. Choose Uninstall latest feature update and let it complete — this takes a while.
3. Reboot and confirm the login screen returns.
4. Pause updates for two weeks in Settings > Windows Update, then check the vendor's driver page before trying 24H2 again. If you ever need fresh installation media, download it only from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 5: Run Startup Repair from the Recovery Environment

If Windows itself is damaged and cannot reach Safe Mode, Startup Repair can rebuild the boot and system files the update left inconsistent.

1. Reach WinRE via the triple-interrupt method, then Advanced options.
2. Choose Troubleshoot > Advanced options > Startup Repair.
3. Let it diagnose and repair — it may reboot several times.
4. If it reports it could not repair, continue to Fix 6 rather than repeating it.

### Fix 6: Repair the system image offline with DISM and SFC

A half-applied 24H2 update can leave the component store inconsistent. Repairing it from WinRE's command prompt fixes what Startup Repair cannot.

1. In WinRE go to Troubleshoot > Advanced options > Command Prompt.
2. Run: DISM /Image:C:\ /Cleanup-Image /RestoreHealth (adjust the drive letter if needed).
3. Then run: sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows.
4. Reboot and check for the login screen.

### Fix 7: Reset Windows while keeping your files

The last resort that still preserves your data: reinstall Windows from recovery, keeping personal files while replacing system files and drivers wholesale.

1. In WinRE go to Troubleshoot > Reset this PC.
2. Choose Keep my files and then Cloud download for the freshest image.
3. Let the reset complete — it takes 30 to 60 minutes.
4. After setup, install your laptop maker's drivers before running Windows Update, and [back up your drivers](/articles/best-way-to-backup-drivers-before-update/) once stable.

## Closing

A black screen after 24H2 is a display-path problem far more often than a dead machine: the graphics shortcut, a bare-panel reboot, and a driver rollback resolve the great majority. Only escalate to update removal and system repair when the simple steps fail. Once you are back in, update the graphics driver from your laptop maker's site before letting Windows Update near it again — and if the black screen is specific to your brand, see [troubleshooting black screens after Windows update](/articles/troubleshoot-black-screen-after-windows-update/) and the [best way to fix a black screen after Windows Update](/articles/best-way-to-fix-black-screen-after-windows-update/).
