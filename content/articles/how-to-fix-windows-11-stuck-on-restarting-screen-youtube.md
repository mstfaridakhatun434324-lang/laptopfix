---
title: "Windows 11 Stuck on the Restarting Screen? Here's How to Fix It"
slug: how-to-fix-windows-11-stuck-on-restarting-screen-youtube
date: 2026-09-20
categories: ["windows-errors"]
tags: ["stuck on restarting", "windows 11", "frozen restart", "boot loop", "startup"]
description: "Windows 11 frozen on the 'Restarting' screen with spinning dots? Force a safe shutdown and fix the stuck restart with these step-by-step repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-11-stuck-on-restarting-screen-youtube.webp"
faqs:
  - q: "How long should I wait before forcing a shutdown?"
    a: "Give it 15 to 20 minutes. A genuine restart with pending updates can legitimately take that long on a slower drive. If the spinning dots are still going after 20 minutes with no disk activity light, it is genuinely stuck and safe to force a shutdown by holding the power button for 5 to 10 seconds."
  - q: "Will force-shutting down during 'Restarting' damage Windows?"
    a: "It is very unlikely to cause damage on a modern system. Windows is designed to tolerate power loss during shutdown, and NTFS journals file operations. The main risk is if an update was mid-install — in that case Windows usually rolls back cleanly on the next boot. Repeated forced shutdowns are a bad habit, but one is fine."
  - q: "Why does my laptop get stuck restarting every time?"
    a: "Recurring stuck restarts are usually caused by Fast Startup holding a corrupted hibernation state, a driver that refuses to unload, a pending update that cannot complete, or a misbehaving USB device. If it happens on every restart rather than just once, work through the fixes below instead of just force-shutting down each time."
  - q: "Is this the same as being stuck on 'Shutting down'?"
    a: "They are closely related but not identical. 'Shutting down' hangs happen while Windows is closing programs and services; 'Restarting' hangs happen after that, during the handoff back to the bootloader. The fixes overlap heavily — Fast Startup, drivers, and updates are the usual suspects for both."
---
The spinning dots say "Restarting." Five minutes pass. Then fifteen. The dots are still spinning, the fan might be whirring, and nothing is happening. This is one of the most common Windows 11 complaints, and the good news is that a single stuck restart is almost always harmless — the trick is knowing when to wait, when to intervene, and how to stop it from becoming a habit.

Let's get you unstuck, then fix the underlying cause so it does not happen again.

## Why this happens

- **Fast Startup holds a corrupted hibernation state:** Instead of a true shutdown, Windows saves a hibernation file — and a corrupted one can jam the restart cycle indefinitely.
- **A pending Windows update cannot complete:** The restart phase is when updates finalize; a stuck or corrupted update keeps the "Restarting" screen up forever.
- **A driver refuses to unload:** Faulty network, audio, or USB drivers can block the shutdown sequence that precedes the restart.
- **A misbehaving USB device:** External drives, docks, and even some mice/keyboards can stall the restart handshake with the BIOS.
- **Background apps block shutdown:** Programs with unsaved work or hung processes can silently veto the restart.
- **Corrupted system files:** Damaged shutdown-related components leave Windows unable to complete the restart sequence.
- **Disk errors:** Bad sectors in critical areas slow the restart process to a crawl that looks like a freeze.

## How to fix it

Work through these in order, starting at Fix 1. Fix 1 gets you unstuck right now; Fixes 2-7 stop it from recurring.

### Fix 1: Wait, then force a shutdown safely

First, make sure it is actually stuck — then shut down cleanly.

1. Wait a full 15-20 minutes. Watch for the drive activity light — if it is blinking, Windows is still working; leave it alone.
2. If nothing has changed after 20 minutes, press and hold the power button for 5-10 seconds until the laptop powers off completely.
3. Unplug all USB devices — external drives, docks, hubs, even the charger for a moment.
4. Wait 30 seconds, then power on normally.
5. Windows will usually boot fine. If it says "Windows didn't shut down correctly," just choose **Start Windows normally**.

If your machine also struggles with general boot problems, our guide to [Windows stuck on the restarting screen](/articles/windows-11-stuck-on-restarting-screen-fix/) covers related startup hangs in more depth.

### Fix 2: Disable Fast Startup

Fast Startup is the number one cause of recurring restart hangs. Turning it off forces a genuine full shutdown every time.

1. Press **Win + R**, type `powercfg.cpl`, and press Enter to open Power Options.
2. Click **Choose what the power buttons do** on the left.
3. Click **Change settings that are currently unavailable** (requires admin).
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes** and restart to test — the restart should now complete in a normal timeframe.

### Fix 3: Disconnect peripherals and test a clean restart

Rule out a USB device jamming the restart handshake.

1. Shut down the laptop fully.
2. Disconnect everything except the power adapter — all USB drives, docks, printers, external monitors, SD cards.
3. Power on, then go to **Start > Power > Restart** and time it.
4. If the restart completes quickly, reconnect devices one at a time, restarting after each, until you find the culprit. Update or replace that device's driver.

### Fix 4: Install pending updates properly

A half-installed update is a classic cause. Let it finish in a controlled way.

1. Go to **Settings > Windows Update** and click **Check for updates**.
2. Install everything offered, including **Advanced options > Optional updates** — especially driver updates.
3. Restart when prompted and give it up to 30 minutes without touching the machine.
4. If an update repeatedly fails, note its KB number and grab it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), then install the downloaded package.

### Fix 5: Update or roll back device drivers

Drivers that will not unload cleanly stall the shutdown phase of a restart.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Look for any device with a yellow warning icon — update those drivers first.
3. Pay special attention to **Network adapters**, **Sound, video and game controllers**, and **Universal Serial Bus controllers** — the usual offenders.
4. Right-click each, choose **Update driver > Search automatically for drivers**.
5. If the problem started after a driver update, use **Properties > Driver > Roll Back Driver** instead.

For Safe Mode driver troubleshooting techniques, see [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 6: Run system file and disk checks

Corruption in shutdown components or the disk itself causes repeat hangs.

1. Open **Terminal (Admin)** (**Win + X > Terminal (Admin)**).
2. Run `sfc /scannow` and wait for completion.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Finally, schedule a disk check: `chkdsk C: /f`, type **Y** when prompted, and restart — the check runs before Windows loads.
5. After all three, test a normal restart.

### Fix 7: Perform a clean boot to find software conflicts

If restarts still hang, a third-party program is likely vetoing the shutdown.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. Go to the **Startup** tab and click **Open Task Manager** — disable every startup item.
4. Restart. If the restart is now quick, re-enable services and startup items in small groups, restarting each time, until the hang returns — the last group contains your culprit.
5. Microsoft's own [Windows support page](https://support.microsoft.com/en-us/windows) documents this clean-boot procedure with screenshots if you want a visual reference.

## Closing

A stuck "Restarting" screen is alarming the first time, but it is rarely serious — one patient forced shutdown gets you back in, and disabling Fast Startup plus clearing out pending updates prevents the encore in most cases. If restarts hang every single time even after these fixes, treat it as an early warning: run the disk check, update your drivers, and make sure your backups are current, because a machine that cannot restart cleanly is telling you something wants attention.
