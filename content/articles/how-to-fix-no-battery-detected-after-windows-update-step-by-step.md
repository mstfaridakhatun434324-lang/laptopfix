---
title: "Step by Step: Fix \"No Battery Detected\" After a Windows Update"
slug: how-to-fix-no-battery-detected-after-windows-update-step-by-step
date: 2026-09-18
categories: ["battery"]
tags: ["no battery detected", "windows update", "battery driver", "device manager", "troubleshooting"]
description: "Windows update left you with a 'no battery detected' error? Follow these exact steps to reinstall drivers and restore battery detection."
thumbnail: "/images/thumbs/how-to-fix-no-battery-detected-after-windows-update-step-by-step.webp"
faqs:
  - q: "How long does it take to fix the no battery detected error?"
    a: "Usually under 15 minutes. Reinstalling the ACPI battery drivers and restarting fixes it for most people. The longer fixes — rolling back an update or doing a Windows repair install — take 30 to 90 minutes but are rarely needed."
  - q: "Will I lose my files fixing this?"
    a: "No. Every fix in this guide except the last-resort repair install only touches drivers and settings. Even the repair install has a 'keep personal files and apps' option. Still, having a backup before major system work is always smart."
  - q: "My battery icon disappeared entirely. Is that the same problem?"
    a: "Related but different. A missing icon is usually a taskbar settings issue — right-click the taskbar, go to Taskbar settings, and check the system tray icons. 'No battery detected' with a red X on the icon means Windows sees the icon but can't communicate with the battery."
  - q: "Can I still use my laptop while it says no battery detected?"
    a: "Yes, on AC power it runs normally. Just know you have no safety net — if the power cable comes out, the machine dies instantly. Don't do important unsaved work until the battery is detected again."
---

A Windows update finishes, the laptop reboots, and there it is: a battery icon with a red X and the words "No battery detected." Your battery was fine an hour ago. The update didn't eat it — it just broke the conversation between Windows and the battery.

This is one of the most common post-update complaints on Windows laptops, and it follows a predictable pattern: the update touched the battery or chipset drivers, something failed to reload cleanly, and now Windows reports a battery it can't see. Work through the steps below in order. Each one takes a few minutes, and the fix is usually in the first three.

## Why this happens

- **The ACPI battery driver didn't survive the update.** The driver that reports battery status to Windows is stuck, crashed, or mismatched.
- **A generic driver replaced the manufacturer's driver.** Windows Update sometimes swaps in its own version, which lacks the hooks for your laptop's battery controller.
- **The driver installation was interrupted.** If the update rebooted mid-install, the driver stack can be left half-written.
- **Fast Startup preserved the broken state.** The corrupted driver state is saved to disk and faithfully reloaded on every shutdown.
- **The embedded controller glitched** during the update's multiple reboots and needs a hard reset.
- **Pending updates are queued behind the broken one**, and the system won't stabilize until the queue clears.

## How to fix it

Work through these in order — don't skip ahead. Each step builds on the last.

### Fix 1: Reinstall the battery drivers in Device Manager

This forces Windows to throw away the broken driver state and rediscover the battery.

1. Right-click **Start** (or press **Win + X**) and open **Device Manager**.
2. Expand the **Batteries** section.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** → **Uninstall device**. Leave the "delete driver" checkbox unticked.
4. Right-click **Microsoft AC Adapter** → **Uninstall device** as well.
5. At the top of Device Manager, click **Action → Scan for hardware changes**. Both devices should reappear within seconds.
6. Restart the laptop normally and check the battery icon.

This single procedure resolves the issue roughly two times out of three. If your icon is simply missing rather than showing an error, see our guide on the [battery icon missing from the taskbar](/articles/how-to-fix-battery-icon-missing-from-taskbar-step-by-step/) instead.

### Fix 2: Perform a true full shutdown

Fast Startup means "shut down" doesn't actually reset your drivers. Let's do a real one.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Type `shutdown /s /t 0` and press Enter. The laptop powers off completely — no hybrid hibernation.
3. Unplug the charger, wait a full 60 seconds, then plug it back in and power on.
4. Log in and wait about a minute for Windows to finish detecting hardware. Check the battery icon.

If the battery comes back now, the culprit was Fast Startup caching the broken driver. Consider disabling it: **Control Panel → Hardware and Sound → Power Options → Choose what the power buttons do → Change settings that are currently unavailable** → untick **Turn on fast startup**.

### Fix 3: Hard-reset the embedded controller

The embedded controller (EC) is the low-level chip managing battery communication. Updates that reboot the machine several times can leave it confused.

1. Shut down the laptop completely (use the `shutdown /s /t 0` command from Fix 2).
2. Disconnect the AC adapter and every USB device.
3. If the battery is removable, take it out. If it's internal, leave it — the next step still works.
4. Hold the **power button down for 20 seconds**. You might see lights blink; that's the residual charge draining.
5. Reconnect everything and power on. Windows will re-enumerate the battery hardware from a clean EC state.

### Fix 4: Install your manufacturer's chipset and battery drivers

Windows Update's generic drivers are the usual suspect when the problem survives a driver reinstall.

1. Identify your exact model (check the sticker on the bottom or run `wmic csproduct get name` in Terminal).
2. Go to the maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and download the latest **chipset** driver plus any **power management / battery** driver for your model.
3. Install the chipset driver first, restart, then install the battery driver and restart again.
4. Open **Device Manager → Batteries**, uninstall both devices once more, and **Scan for hardware changes** so the fresh drivers bind properly.

HP owners should also see our [HP-specific no battery detected guide](/articles/how-to-fix-no-battery-detected-after-windows-update-on-hp-laptop/), which covers HP's UEFI diagnostics.

### Fix 5: Uninstall the update that broke it

If the battery disappeared right after a specific KB update, remove that update.

1. Open **Settings → Windows Update → Update history**.
2. Click **Uninstall updates** at the bottom.
3. Sort by install date, select the most recent update, and click **Uninstall**.
4. Restart the laptop and check the battery.
5. If it worked, go back to **Settings → Windows Update** and **Pause updates** for 1-2 weeks. This gives Microsoft time to fix the bad update before it reinstalls.
6. Optional: open **Feedback Hub** (search it in Start) and report the battery detection failure with the KB number — it genuinely helps get bad updates pulled.

### Fix 6: Clear the update queue and repair system files

Sometimes the breakage comes from a half-finished update queue rather than one bad update.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow` and let it finish — this repairs corrupted Windows system files, including driver infrastructure.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store that SFC draws from.
4. Restart, then go to **Settings → Windows Update** and install anything pending. A clean, complete update pass often resolves the detection failure on its own.

### Fix 7: Do an in-place Windows repair

The last resort, but it keeps your files and apps.

1. Download the Windows 11 installer from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run `setup.exe` from within Windows (not from a bootable USB).
3. Choose **Keep personal files and apps** when asked.
4. Let it complete — this reinstalls Windows core files and re-runs full hardware detection, which rebuilds the entire battery driver stack.
5. Afterward, install your manufacturer's chipset drivers before running Windows Update again.

## Closing

"No battery detected" after an update is Windows forgetting how to talk to hardware that's still there. Reinstall the ACPI drivers, force a genuine full shutdown, and reset the embedded controller — that trio fixes it for the vast majority of laptops without touching your files or your update history.
