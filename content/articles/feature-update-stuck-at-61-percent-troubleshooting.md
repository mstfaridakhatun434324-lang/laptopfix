---
title: "Feature Update Stuck at 61%: How to Troubleshoot It"
slug: feature-update-stuck-at-61-percent-troubleshooting
date: 2026-09-26
categories: ["windows-update"]
tags: ["feature update stuck", "61 percent", "windows 11 update", "troubleshooting"]
description: "Your feature update freezes at 61 percent every time? This troubleshooting guide pinpoints the driver-migration bottleneck and gets the install moving."
thumbnail: "/images/thumbs/feature-update-stuck-at-61-percent-troubleshooting.webp"
faqs:
  - q: "What is happening at 61 percent of a feature update?"
    a: "Around 61 percent, the installer is in the second-boot and driver-migration phase, moving your existing drivers into the new Windows build. This phase has almost no progress reporting, so it looks frozen even when working. A single incompatible driver, especially storage or graphics, can genuinely stall it here, which is why this percentage is such a common sticking point."
  - q: "How long should a feature update stay at 61 percent?"
    a: "On a modern laptop with an SSD, expect 20 to 45 minutes at this stage. On a machine with a hard drive, up to two hours is still normal. Only treat it as stuck if the disk activity light is completely dark and Task Manager shows no CPU or disk usage from setup processes for over an hour."
  - q: "Can I safely restart if the update is stuck at 61 percent?"
    a: "A restart during the offline install phase will trigger an automatic rollback to your previous Windows version, which is safe for your files but wastes the whole attempt. Only force a restart after confirming genuine zero activity for over an hour, and make sure the laptop is on AC power before you retry the update."
  - q: "Does stuck at 61 percent mean my hardware is too old?"
    a: "Not necessarily. This stall happens on brand-new laptops too, and it is usually a driver or software conflict rather than a hardware limit. Update your storage, chipset, and graphics drivers from the manufacturer first. Only if the same stall repeats with fully updated drivers should you investigate deeper hardware issues."
---

Sixty-one percent has a reputation among technicians. Feature updates stall there often enough that it is practically a landmark: the installer enters the driver-migration phase, the progress bar goes quiet, and hours can pass with nothing visibly changing. Users assume the update is broken. Sometimes it is. Often it is just slow and silent.

The tricky part is that both situations look identical from the outside. The difference is only visible in disk activity, process behavior, and the setup logs. This guide teaches you to read those signals, fix the common bottlenecks that genuinely stall at 61 percent, and retry the update with the odds in your favor.

You will not need to reinstall Windows or lose any data. Every fix here is reversible and safe.

## Why this happens

- **Storage driver migration hang:** The installer moves disk controller drivers at this stage, and an outdated AHCI or NVMe driver can stall the handoff.
- **Graphics driver conflict:** Display drivers are migrated in the same phase, and old Intel or NVIDIA drivers frequently block it.
- **USB device driver deadlock:** A connected peripheral's driver waits on hardware that is mid-reset, freezing the whole queue.
- **Corrupt driver store:** Damaged entries in the driver repository cause the migration engine to retry silently instead of failing loudly.
- **Antivirus kernel drivers:** Security software hooks the boot process, and its drivers can deadlock against the new kernel during second boot.
- **Failing hard drive:** Bad sectors in the middle of migrated files cause endless read retries with no error shown.
- **Insufficient system reserved space:** The migration needs staging room, and a nearly full system partition throttles it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm whether it is slow or truly stuck

1. Watch the laptop's disk activity LED. Flickering means work is happening, even if the percentage never moves.
2. Press **Ctrl + Shift + Esc** for Task Manager, go to the Performance tab, and check Disk and CPU graphs. Setup processes like `SetupHost.exe` should show activity.
3. If there is any activity at all, plug in the AC adapter, disable sleep, and wait up to two hours on HDD machines or one hour on SSD machines.
4. Declare it stuck only after a full hour of absolute zero activity across disk, CPU, and the LED. Everything below assumes you have confirmed a genuine stall.

### Fix 2: Strip all USB devices and docks

1. If the update is confirmed stuck, hold the power button to force shutdown. Windows will roll back automatically, which is safe for your files.
2. Before retrying, unplug every USB device: drives, printers, hubs, external monitors, and docking stations. These are the number one cause of migration-phase deadlocks.
3. Turn off Bluetooth in Settings so no wireless peripheral drivers load during the install.
4. Retry the feature update with only the charger connected. This single step resolves a surprising share of 61 percent stalls.

### Fix 3: Update storage and chipset drivers first

1. Open Device Manager, expand **IDE ATA/ATAPI controllers** and **Storage controllers**, and note the driver versions and dates.
2. Visit your laptop maker's support page for your exact model and download the latest chipset and storage drivers. Install them and restart.
3. For Intel-based laptops, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can detect and update chipset components automatically.
4. With fresh storage drivers in place, the migration phase has far less to choke on. Retry the update after a clean restart.

### Fix 4: Update or clean-install the graphics driver

1. Download the latest graphics driver for your GPU from the manufacturer rather than relying on Windows Update's version.
2. During installation, choose the clean install option to remove old driver remnants that Device Manager cannot see.
3. If you have both integrated and discrete graphics, update both. The migration phase touches every display driver on the system.
4. After restarting, retry the feature update. Graphics drivers are the second most common 61 percent blocker after storage drivers.

### Fix 5: Remove third-party antivirus before retrying

1. Uninstall your third-party antivirus completely through **Settings > Apps**, then run the vendor's cleanup tool to remove leftover kernel drivers.
2. Restart so that Windows Security takes over protection duties.
3. Antivirus filter drivers are notorious for deadlocking during the second-boot phase, which is exactly where 61 percent sits.
4. Retry the update now. You can reinstall your preferred antivirus once the new build is running. If driver-code errors appear instead, the [0xC1900101 guide](/articles/best-way-to-fix-update-fails-with-error-0xc1900101/) covers that family of failures.

### Fix 6: Repair the driver store and system files

1. Open an admin Command Prompt and run `sfc /scannow` to repair protected system files. Let it finish completely.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store that SFC draws from.
3. If you suspect a specific bad driver, open Device Manager, show hidden devices, and uninstall any grayed-out or warning-marked entries.
4. Restart and retry the update. A clean driver store gives the migration engine nothing to trip over.

### Fix 7: Use the Media Creation Tool for a cleaner install path

1. If the stall repeats after all driver work, download the Media Creation Tool from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Choose **Upgrade this PC now** and keep your files and apps.
3. The tool stages the installation differently from Windows Update and often sails past the phase where the built-in updater stalls.
4. Should the update instead fail outright with an error code, the [cumulative update failure guide](/articles/cumulative-update-fails-to-install-troubleshooting/) walks through the repair sequence for failed installs.

## Closing

The 61 percent stall is a driver-migration bottleneck wearing a frozen progress bar as a disguise. Confirm it is genuinely stuck, strip the peripherals, update storage and graphics drivers, remove the antivirus, and retry. Worked in this order, the update almost always completes on the next attempt.
