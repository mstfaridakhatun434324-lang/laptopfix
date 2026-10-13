---
title: "The Best Way to Fix Windows 11 Stuck on the Restarting Screen"
slug: best-way-to-fix-windows-11-stuck-on-restarting-screen
date: 2026-10-07
categories: ["windows-errors"]
tags: ["restarting screen", "windows 11 stuck", "boot loop", "startup repair", "frozen"]
description: "Windows 11 frozen on the 'Restarting' screen? Skip the guesswork — this ordered guide covers the fixes that actually unstick it, fastest first."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should I wait on the Restarting screen before doing something?"
    a: "Give it 15–20 minutes the first time — Windows may genuinely be finishing updates. If the spinner is still going after 30 minutes with no disk activity (no blinking drive light), it's stuck and you should force a shutdown."
  - q: "Will force-shutting down during 'Restarting' damage Windows?"
    a: "Usually not, but there's a small risk of corrupting files mid-write. It's far safer than leaving it stuck for hours. If Windows was mid-update, run Windows Update again afterward and let it complete cleanly."
  - q: "Why does Windows 11 get stuck on Restarting?"
    a: "Most often: a driver refusing to unload, a Windows Update that can't finish, Fast Startup conflicts, or a stuck background service. Less commonly: disk errors or corrupted system files blocking the shutdown sequence."
  - q: "What if it gets stuck on Restarting every single time?"
    a: "That's a systematic problem — usually a driver or service that hangs during shutdown. Disable Fast Startup, clean-boot to find the culprit, and update chipset and storage drivers. The steps below walk through exactly that."
---

The spinning dots keep spinning. Five minutes, twenty minutes, an hour — "Restarting" just sits there, mocking you. This is one of the most common Windows 11 complaints on laptops, and the frustrating part is that the cause is usually mundane: a driver that won't let go, an update that can't finish, or a service hanging during shutdown.

The best approach isn't random troubleshooting — it's ordered troubleshooting, fastest and most likely first. That's what this guide is: the sequence a technician would actually follow, so you stop as soon as you're unstuck.

## Why this happens

- **A driver hangs during shutdown.** Network, audio, and USB drivers that fail to unload keep Windows waiting forever for a response that never comes.
- **Windows Update is stuck mid-install.** An update that can't complete blocks the restart sequence; the spinner keeps going while nothing progresses.
- **Fast Startup conflicts.** The hybrid shutdown feature can leave drivers and the kernel in a confused state that manifests on the next restart.
- **A background service won't stop.** Third-party services (updaters, sync tools, antivirus) with long timeouts delay shutdown indefinitely.
- **Disk errors or a failing drive.** If Windows can't write its shutdown state to disk, the restart never completes.
- **Corrupted system files.** Damage to shutdown-related components breaks the sequence at the same point every time.

## How to fix it

Work through these in order — start with Fix 1 and stop once restarts work normally.

### Fix 1: Wait, then force shutdown if truly stuck

Don't yank the power at minute three — but don't wait all night either.

1. Wait a full **20 minutes**. Watch for disk activity (drive light blinking, faint disk sounds) — if there's activity, Windows is working.
2. If there's zero activity after 20–30 minutes, hold the **power button for 10 seconds** until the laptop shuts off.
3. Wait 30 seconds, then power on normally.
4. Once booted, open **Settings > Windows Update** and check for updates — let any pending update finish cleanly.
5. Restart once more to confirm the problem is gone. One stuck restart after an update is often a fluke.

### Fix 2: Disable Fast Startup

Fast Startup is implicated in a huge share of restart hangs.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable**.
4. Untick **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down fully, wait 10 seconds, power on, then test a normal restart.

This single change fixes the issue permanently for many laptops. The boot takes a few seconds longer, but shutdowns and restarts become far more reliable. If your laptop also has brand-specific restart quirks, see our [ASUS restarting screen guide](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-asus-laptop/).

### Fix 3: Run the Windows Update troubleshooter and clear the update cache

A wedged update is the next most likely cause.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter and apply any fixes it suggests.
3. If updates still misbehave, open **Terminal (Admin)** and run `net stop wuauserv` then `net stop bits`.
4. Delete everything inside `C:\Windows\SoftwareDistribution\Download` (not the folder itself).
5. Run `net start wuauserv` and `net start bits`, then check for updates again.

Clearing the update cache forces Windows to re-download updates cleanly instead of choking on corrupted files.

### Fix 4: Clean-boot to find the hanging driver or service

If restarts hang consistently, something installed is blocking shutdown.

1. Press **Windows + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, tick **Hide all Microsoft services**, then click **Disable all**.
3. Go to the **Startup** tab and click **Open Task Manager** — disable all startup items.
4. Restart (via **Start > Power > Restart**) and see if it completes normally.
5. If yes, re-enable services in small groups, restarting each time, until the hang returns — the last group contains your culprit.

Common offenders: third-party antivirus, cloud sync tools, RGB/fan utilities, and VPN clients. Update or remove whatever you find. For persistent boot problems, our guide on [disabling automatic restart after a blue screen](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/) helps you capture what's actually failing.

### Fix 5: Update chipset and storage drivers

Shutdown hangs frequently trace to storage and chipset drivers that can't unload.

1. Open **Device Manager** and expand **IDE ATA/ATAPI controllers** and **Storage controllers**.
2. Right-click each controller and choose **Update driver > Search automatically for drivers**.
3. Get the latest chipset driver from your laptop manufacturer's support page (or [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel systems).
4. Update the BIOS too if a newer version is available — follow the manufacturer's instructions exactly.
5. Restart and test.

### Fix 6: Check the disk and repair system files

Rule out disk and file corruption as the blocker.

1. Open **Terminal (Admin)** and run `chkdsk C: /f` — schedule it for next restart if prompted, then restart.
2. After booting, open **Terminal (Admin)** again and run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Then run `sfc /scannow`.
4. Restart once more and confirm the restart completes in a reasonable time.
5. If CHKDSK reports bad sectors repeatedly, back up your data — the drive may be failing.

### Fix 7: Reset Windows Update components fully (advanced)

For update-related hangs that survive Fix 3.

1. Open **Terminal (Admin)**.
2. Run these commands one by one: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Check for updates and install them, then test a restart.

Microsoft documents these component resets on the [Windows support site](https://support.microsoft.com/en-us/windows) if you want the official reference.

## Closing

A stuck Restarting screen is almost never serious — it's a driver, an update, or Fast Startup being difficult. The ordered approach above gets most laptops unstuck by Fix 2 or 3, and the deeper fixes cover the stubborn cases. Once restarts work again, keep Fast Startup off and your drivers current, and you'll likely never see that endless spinner again.
