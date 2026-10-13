---
title: "Fix Windows 11 Stuck on the Restarting Screen on an HP Laptop"
slug: how-to-fix-windows-11-stuck-on-restarting-screen-on-hp-laptop
date: 2026-10-01
categories: ["windows-errors"]
tags: ["stuck on restarting", "hp", "windows 11"]
description: "Fix Windows 11 stuck on the Restarting screen on your HP laptop: force a proper shutdown, disable Fast Startup, and repair the boot process."
thumbnail: "/images/thumbs/how-to-fix-windows-11-stuck-on-restarting-screen-on-hp-laptop.webp"
faqs:
  - q: "My HP laptop has said 'Restarting' for 30 minutes. Is it safe to force it off?"
    a: "Yes — after 15–20 minutes with no disk activity (check the drive light), a restart is genuinely stuck, not slow. Hold the power button for 10 seconds to force it off. One forced shutdown will not damage Windows; the risk only comes from doing it repeatedly."
  - q: "Why does this keep happening on my HP laptop?"
    a: "The usual causes are Fast Startup preserving a bad driver state, a driver hanging during shutdown (often Wi-Fi or graphics), pending Windows updates that cannot complete, or HP utilities conflicting with the shutdown sequence."
  - q: "Will disabling Fast Startup make booting slower?"
    a: "Slightly — cold boots take a few seconds longer because Windows does a full initialization instead of resuming from a hibernation file. On an SSD the difference is barely noticeable, and the reliability gain is worth it."
  - q: "What if it gets stuck again right after I fix it?"
    a: "Then a driver is hanging the shutdown every time. Boot into Safe Mode, update or roll back your Wi-Fi and graphics drivers from HP's support site, and check Event Viewer → System for Event ID 1074/6006 entries naming the hanging component."
---

An HP laptop sitting on the "Restarting" screen with the spinning dots for twenty minutes is not restarting — it is stuck. Windows is waiting on something that will never finish: a hanging driver, a wedged update, or corrupted Fast Startup state. The screen gives you no information, which makes it feel worse than it is.

The fix is straightforward: break the stuck cycle safely, then remove whatever is hanging the shutdown. Work through the steps below in order.

## Why this happens

- **Fast Startup corruption:** Hybrid shutdown saves kernel state to disk; if that state is corrupt, every restart replays the corruption.
- **A driver hanging on shutdown:** Wi-Fi, Bluetooth, and graphics drivers that fail to unload keep the restart waiting indefinitely.
- **Pending updates that cannot apply:** A wedged update holds the restart process hostage while it retries.
- **HP utility conflicts:** HP Support Assistant or old HP drivers occasionally interfere with the power transition.
- **Disk errors:** File system problems can stall the shutdown flush of pending writes.
- **Too many background processes refusing to close:** A hung application with unsaved state can block the restart sequence.

- **HP Wolf Security / Sure Sense drivers:** HP's security stack hooks into shutdown paths; outdated versions can hang the restart sequence indefinitely.
## How to fix it

Work through these in order — break the cycle first, then fix the cause.

### Fix 1: Force the shutdown safely

1. Wait 15–20 minutes first — some restarts with pending updates genuinely take a while. Watch the disk activity light; no blinking for 10+ minutes means stuck.
2. Hold the **power button for 10 seconds** until the laptop powers off completely.
3. Unplug the charger, wait 30 seconds, then power on.
4. Windows should boot normally. One forced shutdown is safe — just do not make it a habit. If it boots into automatic repair, let it run; it is checking for damage from the interrupted restart.

### Fix 2: Disable Fast Startup

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully and power back on. Fast Startup is the single most common cause of stuck restarts — disabling it forces a clean shutdown and boot every time.

### Fix 3: Update HP drivers, especially Wi-Fi and graphics

1. Open **HP Support Assistant** and install all recommended driver and BIOS updates.
2. If you prefer manual: go to [HP support](https://support.hp.com/us-en), enter your model, and download the latest **Wi-Fi**, **Bluetooth**, **graphics**, and **chipset** drivers.
3. Install them and restart (a real restart — hold **Shift** while clicking Restart to bypass Fast Startup remnants if needed).
4. Drivers that hang during shutdown are the second most common cause after Fast Startup; fresh HP-validated drivers resolve it. Similar shutdown hangs are covered in our [restarting-screen guide for other brands](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-dell-laptop/) if you manage multiple laptops.

### Fix 4: Clear pending updates

1. Open **Settings → Windows Update** and check for updates that are stuck downloading or installing.
2. If an update is wedged, open **Terminal (Admin)** and run `net stop wuauserv`, then delete the contents of **C:\Windows\SoftwareDistribution**, then run `net start wuauserv`.
3. Check for updates again and let them install cleanly.
4. A wedged update holding the restart hostage is common after Patch Tuesday — clearing the cache lets it proceed.

### Fix 5: Check what is hanging with Event Viewer

1. Press **Win + R**, type `eventvwr`, and press Enter.
2. Go to **Windows Logs → System** and look for **Event ID 1074** (shutdown process) and errors around the time of the stuck restart.
3. Note any driver or service named — that is your hanging component.
4. Update, roll back, or uninstall that specific driver in **Device Manager**. This turns a mystery hang into a targeted fix.

### Fix 6: Run SFC, DISM, and chkdsk

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Run `chkdsk C: /f`, scheduling at restart with **Y** if asked.
4. Restart. Corrupted system files and disk errors can stall the shutdown sequence; this trio repairs both. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the recovery options if the system will not boot cleanly.

### Fix 7: Test in Clean Boot to find the culprit

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, tick **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, click **Open Task Manager** and disable all startup items. Restart.
4. If restarts are now clean, re-enable services in halves until the hang returns — the last half contains the culprit. Uninstall or update that program.

### Fix 8: Update the BIOS and chipset from HP

Firmware-level power handling affects every shutdown and restart. If drivers did not fix the hang, the BIOS and chipset are the next layer down.

1. Open **HP Support Assistant** and check for a **BIOS** update — install it only while plugged into AC power.
2. Install the latest **chipset** driver from [HP support](https://support.hp.com/us-en) for your exact model.
3. Restart and test several full shutdown/restart cycles deliberately.
4. If hangs persist, compare notes with our [general stuck-on-restarting guide](/articles/windows-11-stuck-on-restarting-screen-fix/) — the underlying causes are the same across brands even when the tools differ.
5. As a last resort before hardware suspicion, run HP's UEFI diagnostics (**F2** at boot → Component Tests) to rule out a failing drive stalling shutdown writes.

## Closing

A stuck "Restarting" screen is Windows waiting politely on something broken — usually Fast Startup state, a hanging driver, or outdated firmware. Force the shutdown once, disable Fast Startup, refresh your HP drivers through Support Assistant, clear any wedged updates, and bring the BIOS current. If it ever recurs, Event Viewer and a clean boot will name the hanging component so you can deal with it directly instead of staring at spinning dots. The dots do not have to be a regular part of your computing life.
