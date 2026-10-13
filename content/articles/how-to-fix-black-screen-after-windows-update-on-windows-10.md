---
title: "How to Fix a Black Screen After a Windows 10 Update"
slug: how-to-fix-black-screen-after-windows-update-on-windows-10
date: 2026-09-09
categories: ["windows-errors"]
tags: ["windows 10", "black screen", "windows update"]
description: "Stuck on a black screen after a Windows 10 update? From a quick graphics reset to uninstalling the update, these steps will bring your display back."
thumbnail: "/images/thumbs/how-to-fix-black-screen-after-windows-update-on-windows-10.webp"
faqs:
  - q: "How do I know if the black screen is hardware or software?"
    a: "Watch the boot sequence. If you see the manufacturer's logo or the spinning dots before the screen goes black, the display and GPU work and the problem is software — almost always the driver or the update. No logo, no backlight, no external-monitor output at all points to hardware."
  - q: "Will I lose my files fixing a black screen?"
    a: "Not with the steps in this guide. Graphics resets, driver rollbacks, update uninstalls, SFC, DISM, and System Restore all leave personal files alone. Only a clean install wipes data, and that is not on this list — the in-place upgrade explicitly keeps your files and apps."
  - q: "Why does this keep happening after every Windows update?"
    a: "Because Windows Update keeps replacing your working graphics driver with its own version. The permanent fix is to install the driver from Intel, NVIDIA, or AMD directly, then use the manufacturer's update tool instead of relying on Windows Update for graphics drivers."
  - q: "The screen is black but I can hear Windows sounds. What does that mean?"
    a: "Windows is fully booted and only the display output is wrong — usually the picture is going to a phantom second monitor or the driver crashed. The Win+P trick in Fix 1 and the graphics reset shortcut are made for exactly this situation, so start there."
---

Few things are as unnerving as a laptop that powers on — fans spinning, lights blinking — but shows nothing at all after a Windows 10 update. The good news: a black screen after an update is rarely a dead machine. In most cases Windows is actually running behind that black void, and the update simply broke the handshake between the operating system and your display.

The usual suspects are a display driver the update replaced with an incompatible one, an update stuck halfway through its final restart, or the fast startup cache holding onto a bad graphics state. Start with the thirty-second checks below — they resolve this more often than you would expect — and work down to the heavier repairs only if you need them.

## Why this happens

- **The update replaced your display driver:** Windows Update loves swapping the manufacturer's graphics driver for its own version. If that version disagrees with your GPU, you get a black screen with a working system underneath.
- **The update stalled mid-install:** the screen can go black during the final restart phase and just stay there if a driver or service hangs while Windows is trying to come back up.
- **Fast startup restored a bad state:** the hibernation snapshot saved before the update can reload a graphics state that no longer matches the updated system.
- **A second display is confusing things:** with a monitor or TV connected, Windows may be sending the picture to a display that is off or disconnected, leaving the laptop screen dark.
- **Explorer failed to start:** sometimes Windows boots fine but the shell (explorer.exe) crashes on login, leaving a black screen with a lonely mouse cursor.
- **Disk errors interrupted the update:** bad sectors or file-system corruption can leave update files half-written, and Windows cannot complete the boot sequence.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Wake the display with the graphics reset shortcut

Before anything drastic, try the built-in graphics driver reset. It takes five seconds and fixes black screens caused by a hung display driver.

1. Press **Windows key + Ctrl + Shift + B** all at once. You should hear a beep and see the screen flicker as the graphics driver restarts.
2. If nothing happens, press **Win + P**, then tap the **Down arrow** once and hit **Enter** — this switches to duplicate display mode in case Windows is outputting to a phantom monitor.
3. Still black? Disconnect every external display, dock, and USB-C adapter, then try the graphics reset shortcut once more.
4. If you see anything at all — even a flicker — the hardware is fine and this is a driver problem. Move to Fix 3.

### Fix 2: Force a proper cold boot

A black screen can be a failed hybrid shutdown rather than a failed update. A true cold boot clears it.

1. Hold the power button for 10 seconds until the laptop is fully off — no lights, no fan.
2. Unplug the charger and all peripherals. If the battery is removable, take it out for 30 seconds.
3. Hold the power button down for 20 seconds with everything disconnected to drain residual charge.
4. Reconnect only the charger and power on. Watch carefully: if you see the manufacturer's logo, Windows is trying to boot and the issue is software.

### Fix 3: Boot into Safe Mode and roll back the display driver

Safe Mode uses the basic Microsoft display driver, so if the screen works there, your real driver is the problem. This is the most common fix for update-caused black screens.

1. Interrupt the boot three times (power off at the logo) to reach **Automatic Repair**, then **Advanced options > Troubleshoot > Advanced options > Startup Settings > Restart**, and press **4**.
2. In Safe Mode, open **Device Manager** (right-click **Start**), expand **Display adapters**, right-click your GPU, and open **Properties**.
3. On the **Driver** tab click **Roll Back Driver**. If it is greyed out, choose **Uninstall device**, tick **Delete the driver software for this device**, and restart.
4. Windows will boot with the basic display adapter. Then install the correct driver from the manufacturer's site — [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html), the [NVIDIA download page](https://www.nvidia.com/Download/index.aspx), or [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) depending on your GPU.

### Fix 4: Uninstall the update that caused it

If the black screen appeared immediately after Patch Tuesday or a feature update, removing that update is the direct fix. You can do it from Safe Mode or recovery.

1. In Safe Mode, open **Settings > Update & Security > Windows Update > View update history > Uninstall updates**.
2. Sort by **Installed On**, right-click the most recent update (usually a cumulative update with a KB number), and uninstall it.
3. If you cannot reach Safe Mode, do it from recovery: **Automatic Repair > Advanced options > Troubleshoot > Advanced options > Uninstall Updates > Uninstall latest quality update**.
4. After uninstalling, restart normally. Then pause updates for 7 days under **Windows Update > Pause updates** so the same update does not reinstall overnight before you have a working driver in place.

### Fix 5: Repair system files and the disk

A half-applied update can leave corrupted files behind. These commands check both the file system and the Windows image itself.

1. Boot into Safe Mode with Command Prompt (option **6** in Startup Settings) or use **Troubleshoot > Advanced options > Command Prompt** from recovery.
2. Run `chkdsk C: /f /r` and let it complete — answer **Y** if it asks to schedule on restart, then reboot and let it scan.
3. Back at the prompt, run `sfc /scannow` to repair protected system files.
4. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to fix the component store. Restart normally when all three finish.

### Fix 6: Check whether Explorer is the problem

A black screen with a working mouse cursor often means Windows booted fine but the desktop shell crashed. This is a two-minute check.

1. On the black screen, press **Ctrl + Shift + Esc**. If Task Manager appears, Windows is running — only the shell failed.
2. In Task Manager, click **File > Run new task**, type `explorer.exe`, and press Enter. If the desktop appears, the shell just needed a kick.
3. To stop it recurring, open **Registry Editor** in Safe Mode and check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` — the **Shell** value must read exactly `explorer.exe`.
4. If Task Manager will not open at all, the problem is deeper than the shell — continue to Fix 7. A related startup hang is covered in [Windows 11 stuck on restarting](/articles/windows-11-stuck-on-restarting-screen-fix/), which shares several of these steps.

### Fix 7: Do a System Restore or in-place upgrade

When nothing else works, roll the whole system back to before the update. System Restore is quick; an in-place upgrade is the thorough fallback.

1. From recovery, go to **Troubleshoot > Advanced options > System Restore** and pick a restore point dated before the update.
2. If no restore point exists, create Windows 10 installation media on another PC, boot from it, and choose **Repair your computer** — not Install.
3. As a last resort before wiping, run an in-place upgrade: boot into Safe Mode, run setup.exe from the installation media, and choose **Upgrade** with **Keep personal files and apps**.
4. After recovery, immediately update the graphics driver manually (Fix 3's links) before letting Windows Update run again, or you will be back at the black screen. If you need the minimal environment again, [this Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers every entry method.

## Closing

A black screen after a Windows 10 update is one of those problems that looks catastrophic and usually is not. The graphics reset shortcut and a driver rollback resolve the large majority of cases in under fifteen minutes. Save the heavy tools for last, keep a known-good graphics driver installer on a USB stick for next time, and pause updates for a few days after a bad one so you stay in control of what installs and when.
