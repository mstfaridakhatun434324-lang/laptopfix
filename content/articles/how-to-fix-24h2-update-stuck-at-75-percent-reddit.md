---
title: "How to Fix the 24H2 Update Stuck at 75 Percent (Reddit's Best Fixes)"
slug: how-to-fix-24h2-update-stuck-at-75-percent-reddit
date: 2026-10-03
categories: ["windows-update"]
tags: ["24h2", "stuck at 75", "feature update", "windows 11"]
description: "24H2 update frozen at 75 percent? These are the fixes Reddit users confirm actually work — cache resets, driver cleanup, and the clean-boot method."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-reddit.webp"
faqs:
  - q: "How long should I wait at 75 percent before assuming it's stuck?"
    a: "Give it at least two hours of genuine inactivity before intervening. The 24H2 update performs heavy driver and component migration around the 70 to 80 percent mark, which can look frozen on slower laptops. Only treat it as stuck when the percentage, disk activity, and CPU usage all stay flat for a full two hours while the laptop stays plugged in and awake."
  - q: "Is it safe to force-restart a 24H2 update stuck at 75 percent?"
    a: "A forced restart is a last resort, not a first step. At 75 percent the update is mid-installation, and cutting power can leave the system in a state that needs repair. Try stopping the assistant, clearing the update cache, or using the Media Creation Tool first. If you must force a restart, Windows will usually roll back automatically, but you may then need to repair with SFC and DISM."
  - q: "Why do so many people report 24H2 stalling at exactly 75 percent?"
    a: "The 75 percent mark coincides with the driver migration phase, where Windows swaps in new drivers for your hardware. A single incompatible or unsigned driver — often from an old peripheral or a third-party utility — can halt the whole process silently. That's why driver cleanup and clean-boot installs resolve so many of these stalls."
  - q: "Will the Media Creation Tool fix a 24H2 stall at 75 percent?"
    a: "Often, yes. The Media Creation Tool performs the same 24H2 upgrade but with more robust error handling and clearer progress reporting than the Update Assistant. Many users who stall repeatedly at 75 percent in the assistant complete the upgrade cleanly through the tool. Download it from Microsoft's official download page and choose Upgrade this PC now."
---

Scroll through any Windows forum and you'll find the same story: the 24H2 update climbs steadily to 75 percent, then stops dead. Hours pass. The fans spin down, the disk goes quiet, and the progress bar mocks you. Reddit threads on this exact stall run hundreds of comments deep, and the good news is that the community has converged on a handful of fixes that genuinely work — not the generic "restart and pray" advice.

This guide collects those battle-tested fixes, ordered from least invasive to most thorough. They apply whether you're upgrading through Windows Update, the Update Assistant, or the ISO — the stall point is the same because the underlying migration phase is the same. If your feature update fails outright instead of stalling, our [step-by-step failed feature update guide](/articles/how-to-fix-feature-update-to-windows-11-24h2-failed-step-by-step/) covers that path.

## Why this happens

- **Driver migration deadlock** — Around 75 percent, 24H2 migrates hardware drivers; one bad or unsigned driver halts the entire phase silently.
- **Corrupted update payload** — A damaged download that passed initial checks fails verification mid-install, freezing progress.
- **Third-party antivirus filters** — File-system filters from security suites can block the file operations 24H2 performs during migration.
- **Insufficient disk space** — The migration phase needs substantial scratch space; near-full drives stall without an error message.
- **Stale SoftwareDistribution cache** — Old or half-written cache metadata confuses the installer about what's already been staged.
- **Failing storage sectors** — Bad blocks encountered during the heavy write phase of migration can freeze the copy loop.
- **BIOS or firmware incompatibility** — Outdated laptop firmware can conflict with 24H2's hardware checks, stalling the install mid-flight.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall is real (two-hour rule)

Reddit's most repeated advice is also the simplest: most "stuck" 24H2 installs aren't stuck at all — they're just slow at the heaviest phase.

1. Note the exact percentage and time, then leave the laptop plugged into AC power with the lid open.
2. Set sleep to **Never** in Settings > System > Power & battery so the laptop can't doze mid-migration.
3. Open Task Manager (Ctrl + Shift + Esc) and check the Disk and CPU columns for sustained activity from setup or system processes.
4. Wait a full two hours. If percentage or disk activity changes at any point, it's working — be patient.
5. Only proceed to Fix 2 when everything has been flat for the entire two hours.

### Fix 2: Disconnect peripherals and kill conflicting software

The driver migration phase chokes on unexpected hardware, so strip the system down to essentials before retrying.

1. Unplug every USB device except the charger — docks, external drives, printers, and especially USB audio interfaces.
2. Temporarily uninstall third-party antivirus, keeping Windows Defender enabled as your protection.
3. Disable VPN clients and virtual network adapters, which can stall network-dependent verification steps.
4. Retry the update with this minimal configuration; if it sails past 75 percent, reconnect devices one at a time afterward.
5. Check the laptop manufacturer's support site for a BIOS update — outdated firmware is a known 24H2 migration blocker.

### Fix 3: Clear the update cache completely

A corrupted payload is the second-most common cause, and the fix is a full cache purge that forces a clean re-download.

1. Open an elevated Command Prompt (search **cmd**, right-click, **Run as administrator**).
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
3. Delete everything inside `C:\Windows\SoftwareDistribution\Download` and rename `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services with the matching `net start` commands, then reboot.
5. Run Windows Update again — the 24H2 download will restart from scratch, and the previously stalled phase usually completes on the fresh payload.

### Fix 4: Free disk space and run the update troubleshooter

24H2 needs room to maneuver. Combine a cleanup with the built-in troubleshooter for a solid mid-level fix.

1. Check C: free space in Settings > System > Storage — you want at least 25–30 GB free.
2. Run Disk Cleanup as administrator and select **Windows Update Cleanup**, **Temporary files**, and **Delivery Optimization Files**.
3. Move personal media off C: temporarily if you're still tight on space.
4. Go to Settings > System > Troubleshoot > Other troubleshooters and run the **Windows Update** troubleshooter.
5. Retry the update. For persistent installer weirdness, compare symptoms with our [black screen after 24H2 guide](/articles/how-to-fix-windows-11-24h2-black-screen-after-update-step-by-step/) in case the stall is masking a display-driver issue.

### Fix 5: Update drivers manually before the upgrade

Instead of letting 24H2 migrate ancient drivers mid-install, update the critical ones yourself first.

1. Open Device Manager and check Display adapters, Storage controllers, and Network adapters for warning icons.
2. Download fresh chipset, storage, and graphics drivers from your laptop maker's support page (Dell, HP, Lenovo, or ASUS).
3. For Intel-based laptops, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch anything you missed.
4. Reboot after the driver updates, then launch the 24H2 upgrade again.
5. Many users report that this single step — especially the storage driver — unfreezes the 75-percent stall permanently.

### Fix 6: Do a clean-boot upgrade

Background services are the hidden variable in most stall reports. A clean boot removes them from the equation.

1. Press Win + R, type `msconfig`, and open System Configuration.
2. On the Services tab, tick **Hide all Microsoft services**, then click **Disable all**.
3. On the Startup tab, open Task Manager and disable every startup item.
4. Reboot — you'll be in a minimal state with no third-party software running.
5. Start the 24H2 upgrade from Settings > Windows Update. Clean-boot upgrades have one of the highest success rates in community reports.

### Fix 7: Use the Media Creation Tool or ISO

When every in-place method stalls at the same point, switch tools. The Media Creation Tool handles errors more gracefully than the assistant.

1. Download the Media Creation Tool from Microsoft's official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it and choose **Upgrade this PC now**, keeping personal files and apps.
3. Alternatively, download the 24H2 ISO, mount it, and run `setup.exe` from the mounted drive.
4. The tool's progress reporting is more honest — if it hits a real blocker, it usually tells you what it is.
5. If even the ISO stalls at the same phase, suspect hardware: run your manufacturer's storage diagnostics before trying again.

## Closing

The 24H2 stall at 75 percent is frustrating precisely because it's silent — no error code, no explanation. But the community has mapped it thoroughly: it's the driver migration phase, and the fix is almost always clearing the cache, cleaning up drivers, or removing the conflicting software that's jamming the works. Work the list in order, give each attempt a fair chance, and you'll join the long thread of users posting "finally past 75%" instead of asking why it won't move.
