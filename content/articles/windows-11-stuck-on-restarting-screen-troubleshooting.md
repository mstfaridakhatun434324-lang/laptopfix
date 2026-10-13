---
title: "Windows 11 Stuck on the Restarting Screen: Full Troubleshooting Guide"
slug: windows-11-stuck-on-restarting-screen-troubleshooting
date: 2026-09-05
categories: ["windows-errors"]
tags: ["restarting screen", "windows 11", "troubleshooting", "frozen restart", "startup"]
description: "Complete troubleshooting guide for Windows 11 stuck on the Restarting screen — from quick fixes to deep repairs, ordered by what works most often."
thumbnail: "/images/thumbs/windows-11-stuck-on-restarting-screen-troubleshooting.webp"
faqs:
  - q: "Why is my laptop stuck on the Restarting screen?"
    a: "Usually a driver that won't unload, a Windows Update that can't finish, or a hanging background service. Fast Startup conflicts and disk errors are the other common causes. It's rarely serious — the fixes below resolve it in most cases."
  - q: "Is it safe to force shutdown when stuck on Restarting?"
    a: "Yes, after waiting 20–30 minutes with no disk activity. Hold the power button for 10 seconds. There's a small risk of file corruption if Windows was mid-write, so run Windows Update and a disk check afterward."
  - q: "How do I stop it happening every time I restart?"
    a: "Disable Fast Startup, update chipset and storage drivers, and clean-boot to find hanging services. Recurring hangs are systematic — something specific is blocking shutdown, and the steps below identify it."
  - q: "Could a Windows update be causing it?"
    a: "Very likely if it started after an update. Run the Windows Update troubleshooter, clear the SoftwareDistribution cache, and let pending updates finish cleanly. Stuck updates are one of the top causes."
---

"Restarting" with spinning dots, forever. It's one of Windows 11's most reported annoyances on laptops, and it has a dozen possible causes — which is exactly why random troubleshooting fails. This guide is the full, ordered troubleshooting sequence: quick checks first, deeper repairs later, so you stop the moment you're unstuck.

Whether this happened once after an update or every single restart, the steps below cover it.

## Why this happens

- **A driver hangs during shutdown.** Network, audio, and USB drivers that fail to unload keep Windows waiting indefinitely.
- **A Windows Update can't complete.** Corrupted update files block the restart sequence while the spinner keeps spinning.
- **Fast Startup conflicts.** Hybrid shutdown leaves drivers in a state that breaks the next restart.
- **Hanging background services.** Third-party updaters, sync tools, and antivirus services with long timeouts stall shutdown.
- **Disk errors.** If Windows can't write its shutdown state, the restart never finishes.
- **Corrupted system files.** Damage to shutdown components breaks the sequence at the same point every time.
- **Failing hardware.** A dying drive or overheating component can hang the shutdown process — uncommon but real.

## How to fix it

Work through these in order — start with Fix 1 and stop once restarts work.

### Fix 1: Wait, then force a shutdown

Rule out "actually still working" before intervening.

1. Wait **20 full minutes**, watching for disk activity (blinking drive light).
2. If there's activity, keep waiting — Windows may be finishing updates.
3. With zero activity after 20–30 minutes, hold the **power button 10 seconds** to force off.
4. Wait 30 seconds, power on, and open **Settings > Windows Update** to let anything pending finish.
5. Test one normal restart to see if it was a one-off.

### Fix 2: Disable Fast Startup

The single most effective permanent fix.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** > **Change settings that are currently unavailable**.
3. Untick **Turn on fast startup (recommended)** and **Save changes**.
4. Shut down fully, wait 10 seconds, power on.
5. Test a restart — this resolves the issue outright for a large share of laptops.

Brand-specific restart quirks exist too: Dell owners should check our [Dell restarting screen guide](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-dell-laptop/), and HP owners the [HP version](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-hp-laptop/).

### Fix 3: Clear the Windows Update cache

Fix the stuck-update scenario.

1. Open **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter.
2. Open **Terminal (Admin)**: run `net stop wuauserv` and `net stop bits`.
3. Delete all files in `C:\Windows\SoftwareDistribution\Download`.
4. Run `net start wuauserv` and `net start bits`.
5. Check for updates and install them fully, then test a restart.

### Fix 4: Perform a clean boot to find the hanging software

Identify what's blocking shutdown.

1. Press **Windows + R**, type `msconfig`, press Enter.
2. On **Services**, tick **Hide all Microsoft services**, click **Disable all**.
3. On **Startup**, open Task Manager and disable all startup items.
4. Restart via **Start > Power > Restart**.
5. If the restart completes, re-enable in groups until the hang returns — the last group holds the culprit.

Typical offenders: third-party antivirus, cloud sync, VPN clients, RGB utilities. Update or remove what you find. Be systematic here rather than re-enabling everything at once — enabling five services, restarting, and repeating narrows it down within a few cycles. Once identified, check the vendor's site for an updated version before uninstalling outright; many shutdown hangs are fixed in newer releases.

### Fix 5: Update chipset, storage, and BIOS

Shutdown hangs often live in low-level drivers.

1. In **Device Manager**, update drivers under **IDE ATA/ATAPI controllers** and **Storage controllers**.
2. Install the latest chipset driver from your laptop manufacturer's support page (or [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html)).
3. Check for a BIOS update and apply it following the manufacturer's instructions exactly, with the charger connected.
4. Restart and test.
5. If a specific driver update coincides with the problem starting, roll it back via **Device Manager > Properties > Driver > Roll Back Driver**.

### Fix 6: Check disk health and repair system files

Rule out storage and corruption.

1. Open **Terminal (Admin)** and run `chkdsk C: /f` (schedule at reboot if prompted).
2. After booting, run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Then run `sfc /scannow`.
4. Review CHKDSK results in **Event Viewer > Windows Logs > Application** (**Wininit** source).
5. Recurring bad sectors mean a failing drive — back up immediately.

Microsoft documents startup and shutdown repair options on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Reset the PC (keep files) as a last resort

When the cause won't reveal itself, refresh Windows.

1. Open **Settings > System > Recovery**.
2. Click **Reset PC** and choose **Keep my files**.
3. Choose **Cloud download** for the freshest Windows image (needs internet).
4. Let the reset complete — reinstall your apps afterward.
5. Test restarts before reinstalling third-party software, so you'll know if one of your apps was the cause.

## Closing

A Windows 11 laptop stuck on "Restarting" is annoying but almost never dire — it's a driver, an update, or Fast Startup, and the ordered sequence above finds which one. Disable Fast Startup permanently, keep your chipset drivers current, and be suspicious of any new background utility that coincides with the hangs returning. The spinner doesn't have to be a way of life.

One preventive step worth taking once you're unstuck: create a system restore point right now (**Control Panel > System > System Protection > Create**) and name it "restart fixed." If a future driver or update reintroduces the hang, you can roll back in minutes instead of repeating this whole guide. Restarts should take under a minute on a healthy laptop with an SSD — anything consistently longer is worth investigating with the steps above before it becomes another frozen spinner. And if the hangs ever return right after you install something new, you already know the drill: clean-boot, isolate, update or remove.
