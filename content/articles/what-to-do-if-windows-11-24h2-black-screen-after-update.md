---
title: "Black Screen After Windows 11 24H2 Update? Do This First"
slug: what-to-do-if-windows-11-24h2-black-screen-after-update
date: 2026-09-19
categories: ["windows-update"]
tags:
  - "windows 11 24h2"
  - "black screen"
  - "after update"
  - "display driver"
description: "A black screen after the 24H2 update is frightening but usually a display driver issue. Learn the safe recovery sequence: from quick checks to Safe Mode driver repair."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-24h2-black-screen-after-update.webp"
faqs:
  - q: "My screen is black after 24H2 — is my laptop dead?"
    a: "Almost certainly not. A black screen after an update is usually Windows running fine behind a broken display driver, or the display output routed wrong. The laptop is typically working — you just cannot see it. The recovery steps below confirm this quickly."
  - q: "How do I know if it's a black screen or the laptop won't boot?"
    a: "Listen and look: fan noise, disk activity, keyboard backlight, or the Caps Lock light toggling all mean Windows is running fine behind a display problem rather than suffering a boot failure. Complete silence and no lights after pressing power suggests a boot problem instead — a different repair path."
  - q: "Will I lose my files fixing a black screen?"
    a: "No. Every fix here — Safe Mode, driver rollback, even uninstalling the update — fully preserves your files. The black screen is a display/output problem, not a disk problem, and none of the repairs touch your data, documents, photos, or installed programs."
  - q: "Why does 24H2 cause black screens?"
    a: "24H2 migrates display drivers to the new build, and on some laptops the migrated driver fails to initialize the panel — especially with certain Intel, NVIDIA, or AMD driver versions, or with external-display configurations. Rolling the driver back or reinstalling it resolves nearly all cases."
---

The update finished, the laptop restarted, and now: nothing. A black screen, maybe a cursor, maybe not. Your stomach drops — but here is the reassuring truth from years of post-update recoveries: a black screen after 24H2 is one of the most fixable problems in Windows, and it is almost never hardware damage.

In the great majority of cases, Windows is running perfectly behind that black screen. What broke is the display driver — 24H2 migrated it, and the migrated version cannot drive your panel. The fix is to get into Safe Mode (which uses a basic driver), repair or replace the display driver, and reboot to a working screen.

Do the steps below in order, and do not skip the early quick checks — a surprising number of black screens are cables, brightness, or display routing, not drivers at all. For the update-side companion issues, see our [full 24H2 problem guide](/articles/how-to-fix-windows-11-24h2-update-problems-step-by-step/).

## Why this happens

- **Migrated display driver fails:** 24H2's driver migration produces a display driver that cannot initialize the laptop panel.

- **External display routing stuck:** the update leaves the output routed to a disconnected external display.

- **Brightness set to zero:** rare, but driver migration can reset brightness tables to minimum.

- **Fast Startup conflicts:** the hybrid shutdown state interacts badly with the new driver on some laptops.

- **Multiple GPU confusion:** laptops with Intel+NVIDIA or AMD switchable graphics can end up with the wrong GPU driving the panel.

- **Corrupted user profile shell:** Explorer fails to start, leaving a black screen with or without a cursor.

- **Pending update operations:** a stuck post-install phase can delay the shell indefinitely on first boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out the trivial causes first

Two minutes of checks before any repair: many post-update black screens are brightness, display routing, or a stuck external-display state — all fixable with keystrokes.

1. Press the brightness-up key several times — migration can zero the brightness.
2. Press Win + Ctrl + Shift + B to restart the graphics driver (you will hear a beep).
3. Press Win + P, then Enter — this cycles display modes and can restore the laptop panel.
4. Disconnect all external displays, docks, and adapters, then wait 60 seconds.
5. Force a full shutdown (hold power 10 seconds), wait 30 seconds, and power on.

### Fix 2: Boot into Safe Mode

Safe Mode loads a basic display driver, which bypasses the broken migrated driver entirely. If Safe Mode shows a desktop, you have confirmed a driver problem — and you are in the repair environment.

1. Force-power-off the laptop twice during the Windows logo to trigger Automatic Repair.
2. Choose Troubleshoot, then Advanced options, then Startup Settings, then Restart.
3. Press 4 for Safe Mode (or 5 for Safe Mode with Networking).
4. If the desktop appears, the diagnosis is confirmed: display driver issue.
5. Stay in Safe Mode for the driver repairs below.

### Fix 3: Roll back the display driver

The fastest fix when it is available: Windows keeps the previous driver, and rolling back restores the version that worked before 24H2 migrated it.

1. In Safe Mode, open Device Manager (Win + X).
2. Expand Display adapters, right-click your GPU, and choose Properties.
3. On the Driver tab, click Roll Back Driver (if greyed out, skip to Fix 4).
4. Choose a reason, confirm, and restart normally.
5. If the screen works, block the bad driver version from reinstalling via Optional updates.

### Fix 4: Clean-install the display driver

When rollback is unavailable, a clean driver install replaces the broken migrated driver completely. Get the driver from the right source for your GPU.

1. In Safe Mode with Networking, identify your GPU (Device Manager, Display adapters).
2. Download the latest driver: [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel, [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) for NVIDIA, or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) for AMD.
3. For laptops, prefer the laptop maker's customized graphics driver when offered.
4. Run the installer (choose Clean install if the option exists) and restart.
5. Verify normal boot to a working desktop.

### Fix 5: Disable Fast Startup

Fast Startup's hybrid shutdown can trap the new driver in a bad initialized state across reboots. Disabling it forces a true cold boot every time, which clears a class of black-screen-on-restart issues.

1. In Safe Mode, open Control Panel, Power Options.
2. Click Choose what the power buttons do, then Change settings currently unavailable.
3. Untick Turn on fast startup and save changes.
4. Shut down fully (not restart), wait 30 seconds, then power on.
5. Confirm the desktop appears on the cold boot.

### Fix 6: Repair a shell that will not start

If you see a cursor on the black screen, Windows and the driver may be fine — but Explorer is not starting. Launching it manually both confirms and works around this.

1. On the black screen, press Ctrl + Shift + Esc to open Task Manager.
2. Click Run new task, type `explorer.exe`, and press Enter.
3. If the desktop appears, the shell was the problem, not the display.
4. In that session, run `sfc /scannow` from an admin terminal to repair shell files.
5. Check Task Manager's Startup apps for anything blocking Explorer and disable it.

### Fix 7: Uninstall 24H2 as the last resort

When every driver repair fails, remove the update that caused it. Windows keeps the previous build for ten days precisely for this situation, and uninstalling is safe and complete.

1. Boot to the Recovery Environment (two interrupted boots, Troubleshoot).
2. Choose Advanced options, then Uninstall Updates, then Uninstall latest feature update.
3. Let the rollback complete — it can take up to an hour; do not interrupt.
4. Back in Windows, pause feature updates while you research the driver conflict.
5. Update the display driver from the maker first, then retry 24H2 later.

## Closing

Black screens after 24H2 are scary and almost always benign: check the trivial causes, get into Safe Mode, and repair the display driver that the migration broke. Work the sequence in order, keep the laptop plugged in throughout, and you will be looking at your desktop again — usually within the hour. If the machine instead loops on undoing changes after the failed update, our [undoing-changes guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/) covers that recovery.
