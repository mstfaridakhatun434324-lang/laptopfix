---
title: "How to Boot Windows 11 in Safe Mode (4 Working Methods)"
slug: how-to-boot-windows-11-in-safe-mode
date: 2026-09-20
categories: ["windows-errors"]
tags: ["windows-11", "safe-mode", "troubleshooting"]
description: "Need Safe Mode on Windows 11? Here are four reliable methods — including what to do when Windows won't boot at all."
thumbnail: "/images/thumbs/how-to-boot-windows-11-in-safe-mode.webp"
faqs:
  - q: "What is Safe Mode and when should I use it?"
    a: "Safe Mode starts Windows with only the essential Microsoft drivers and services — no third-party drivers, no startup programs. Use it when Windows crashes, won't boot normally, or misbehaves after a driver or software install, so you can uninstall or repair the culprit in a stable environment."
  - q: "Does the old F8 key still work for Safe Mode on Windows 11?"
    a: "No — Windows 11 boots too fast for the F8 interrupt to register reliably. Microsoft replaced it with the recovery environment methods described below. The Shift + Restart trick from the login screen is the modern equivalent and works on every Windows 11 machine."
  - q: "What's the difference between Safe Mode and Safe Mode with Networking?"
    a: "Plain Safe Mode has no network access; Safe Mode with Networking loads network drivers so you can go online to download drivers or research fixes. For troubleshooting driver problems, Networking is usually the better choice. There's also a Command Prompt variant for advanced repairs."
  - q: "How do I get out of Safe Mode?"
    a: "Just restart normally — unless you used msconfig to force Safe Mode, in which case you must open msconfig again and uncheck Safe boot first, or you'll loop back into it. That's the most common 'stuck in Safe Mode' trap."
---
Safe Mode is the single most useful troubleshooting tool in Windows 11. When a bad driver, a crashing program, or a misbehaving update makes normal Windows unusable, Safe Mode gives you a stripped-down, stable environment to undo the damage. Microsoft removed the old F8-during-boot shortcut years ago, so here are the four methods that actually work on Windows 11 — including one for when Windows won't boot at all.

## Why this happens (when you need Safe Mode)

- **A bad driver update.** A new graphics or Wi-Fi driver crashes Windows on every normal boot, but Safe Mode doesn't load it.
- **A program crashing at startup.** Malware or a broken application that launches with Windows and immediately destabilizes it.
- **A Windows update gone wrong.** You need a stable desktop to uninstall the update or roll back the driver it installed.
- **Blue screen loops.** When Windows crashes before you can do anything, Safe Mode (or the recovery environment) is your way in.
- **You need to remove stubborn software.** Some antivirus products and drivers can only be cleanly uninstalled when their services aren't running.

## How to fix it (4 methods to reach Safe Mode)

Work through these in order — start with the easiest method for your situation. The line "work through these in order" doesn't quite apply here since these are alternatives, not steps: pick the first method that fits your situation.

### Fix 1: Shift + Restart from the sign-in screen or Start menu (easiest)

This is the method to use when Windows boots but misbehaves.

1. Hold down the **Shift** key and click **Start > Power > Restart**. (On the sign-in screen, the power icon is at the bottom-right — same Shift + click trick works there.)
2. Keep holding **Shift** until the blue **Choose an option** screen appears.
3. Go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
4. After the reboot, press **4** for Safe Mode, **5** for **Safe Mode with Networking**, or **6** for Safe Mode with Command Prompt.
5. Sign in — you'll see "Safe Mode" in the corners of a low-resolution desktop.

### Fix 2: Interrupt the boot three times (when Windows won't start)

Use this when you can't reach the desktop or even the sign-in screen.

1. Power the laptop on. As soon as the manufacturer's logo appears, press and hold the power button until it shuts off.
2. Repeat step 1 **two more times** (three interrupted boots total).
3. On the fourth boot, Windows enters the **Windows Recovery Environment** automatically and shows **Automatic Repair**.
4. Click **Advanced options**, then go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
5. Press **4**, **5**, or **6** to choose your Safe Mode variant.

### Fix 3: Use msconfig (when Windows boots fine)

Best for when you need to reboot into Safe Mode multiple times while troubleshooting.

1. Press **Win + R**, type `msconfig`, and press **Enter**.
2. Go to the **Boot** tab and check **Safe boot**. Choose **Minimal** (plain Safe Mode) or **Network** (with networking).
3. Click **OK** and **Restart**. Windows will boot into Safe Mode every time until you change it back.
4. **Important:** when you're done, reopen `msconfig`, uncheck **Safe boot**, and restart — otherwise you'll be stuck in Safe Mode indefinitely.

### Fix 4: Use the Settings app or command line

Two more routes to the same recovery screen.

1. **Via Settings:** go to **Settings > System > Recovery**, and under **Advanced startup** click **Restart now**. After rebooting, navigate **Troubleshoot > Advanced options > Startup Settings > Restart** and pick your option.
2. **Via command line:** open **Terminal** or **Command Prompt** and run `shutdown /r /o /f /t 0`. The `/o` flag tells Windows to boot to the advanced startup menu. From there it's the same **Troubleshoot > Advanced options > Startup Settings** path.
3. Once you're in the recovery environment, the options match Fix 1 from step 3 onward.

### What to do once you're in Safe Mode

### Fix 5: Uninstall the suspect driver or program

Getting into Safe Mode is half the battle — now use the stable environment to remove whatever broke normal Windows.

1. Press **Win + X** and open **Device Manager**. Find the device you suspect (usually under **Display adapters** or **Network adapters**).
2. Right-click it, choose **Properties**, go to the **Driver** tab, and click **Roll Back Driver**. If the button is greyed out, choose **Uninstall device** instead and tick **Attempt to remove the driver for this device** if offered.
3. For software, go to **Settings > Apps > Installed apps**, sort by install date, and uninstall anything added right before the trouble started — especially third-party antivirus, system optimizers, or driver updater tools.
4. To remove a bad Windows update, go to **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent one.
5. Restart normally after each removal to test — change one thing at a time so you know what fixed it.

### Fix 6: Run repairs and roll back with System Restore

If you can't identify a single culprit, let Windows repair itself from inside Safe Mode.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run `sfc /scannow` and let it complete (10–15 minutes), then run `DISM /Online /Cleanup-Image /RestoreHealth` — the Networking variant of Safe Mode gives you the internet access DISM needs.
3. For a broader rollback, search the Start menu for **Recovery**, open it, and choose **Open System Restore**. Pick a restore point dated before the problems began and let it run. Our [System Restore guide](/articles/how-to-use-system-restore-on-windows-11/) walks through the whole process including what to do when no restore points exist.
4. If Safe Mode itself is unstable or you can't reach it, skip it entirely and use the recovery environment's tools directly — [Startup Repair](/articles/how-can-i-use-startup-repair-windows-11/) can fix boot problems without ever loading the desktop, and it works from the same blue recovery screen.

## Closing

Safe Mode hasn't gone away on Windows 11 — only the F8 shortcut has. **Shift + Restart** covers most situations, the three-interrupt method covers the cases where Windows won't boot at all, and `msconfig` is best when you'll be going back and forth between Safe Mode and normal Windows several times. Learn one method now, before you need it; when a driver takes down your system at the worst possible moment, you'll be glad the path to Safe Mode is muscle memory. And once you're in, resist the urge to just restart and hope — uninstall the suspect, run the repairs, and confirm the fix before going back to normal. Microsoft documents these options further on their [Windows support hub](https://support.microsoft.com/en-us/windows).
