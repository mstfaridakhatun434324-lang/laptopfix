---
title: "Windows 11 Slow After the 24H2 Update? Here's How to Fix It"
slug: how-do-i-fix-windows-11-slow-after-24h2-update
date: 2026-10-03
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "performance", "windows update", "troubleshooting"]
description: "Windows 11 feeling sluggish after the 24H2 update? Learn why feature updates slow laptops down and the exact steps to restore full speed."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-slow-after-24h2-update.webp"
faqs:
  - q: "How long does Windows 11 stay slow after the 24H2 update?"
    a: "Mild slowness for 24 to 72 hours after a feature update is normal — Windows re-indexes files, Defender re-baselines its scans, and background optimization runs. If your laptop is still noticeably slow after three to four days of regular use, the cause is something fixable: a driver mismatch, a stuck update component, or a background process in a loop."
  - q: "Will reinstalling Windows fix 24H2 slowness?"
    a: "A clean install usually does fix it, but it's the last resort, not the first step. Most 24H2 slowdowns come from identifiable causes — outdated chipset or storage drivers, re-enabled startup apps, or corrupted update components — that take an hour to fix versus a full day of reinstalling and reconfiguring everything. Try the targeted fixes first."
  - q: "Can I roll back the 24H2 update if it's too slow?"
    a: "Yes, within ten days of installing it: Settings > System > Recovery > Go back. After ten days Windows deletes the rollback files automatically. Rolling back is reasonable if the slowdown appeared immediately after 24H2 and nothing fixes it, but check drivers and startup apps first — a surprising number of 'update broke my PC' cases are actually driver issues."
  - q: "Does the 24H2 update itself make laptops slower permanently?"
    a: "No — 24H2 doesn't permanently reduce performance on supported hardware. The update changes driver requirements and resets some settings, which creates temporary or fixable slowdowns. Once drivers are current, background tasks finish, and startup bloat is trimmed, a 24H2 system should feel as fast as or faster than it did on 23H2."
---

You installed the Windows 11 24H2 update expecting new features, and instead your laptop now takes twice as long to boot, apps stutter, and Task Manager shows mysterious processes chewing CPU. This is one of the most common post-update complaints, and the good news is that it's almost always fixable without reinstalling Windows. Feature updates touch drivers, reset settings, and kick off days of background housekeeping — any one of which can masquerade as a permanently slower PC.

The pattern to look for: if the slowdown started within a day of the 24H2 install, the update is involved — directly or through a driver it replaced. Work through the fixes below in order, giving the system a little time between steps, and most laptops return to full speed. For a deeper diagnostic walkthrough, see [troubleshooting 24H2 slowness step by step](/articles/how-to-fix-laptop-slow-after-windows-11-24h2-update-step-by-step/); for general speed-ups, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Post-update background housekeeping**: Search re-indexing, Defender re-baselining, and .NET optimization run heavily for 1–3 days after a feature update.
- **Driver mismatches**: 24H2 replaces or invalidates older chipset, storage, and graphics drivers, causing stutter and high CPU.
- **Re-enabled startup apps**: Feature updates frequently re-enable startup entries you had previously disabled.
- **Stuck Windows Update components**: A partially completed update keeps retrying in the background, burning CPU and disk.
- **Corrupted system files from the upgrade**: Interrupted or glitchy upgrades leave damaged components behind.
- **Power plan reset**: Updates can silently switch you from Best performance back to Balanced or Power saver.
- **Old update cleanup backlog**: Gigabytes of Windows.old and update cache files sit on a nearly full drive, choking the system.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it 48 hours, then measure properly

Don't start surgery during normal recovery.

1. Use the laptop normally for two to three days after the update, keeping it plugged in and connected — background tasks finish faster when the machine is powered and idle.
2. After that window, open **Task Manager** > **Performance** and note CPU, memory, and disk baselines at idle — idle CPU should sit under 10%.
3. Check **Settings** > **Windows Update** — if it shows updates still installing or pending restart, let them finish before judging performance.
4. Look at **Task Manager** > **Processes** sorted by CPU: note the top consumers by name. Common post-update culprits include Windows Module Installer, Search Indexer, and Antimalware Service Executable.
5. Only proceed to active fixes if high usage persists beyond the 72-hour mark — fixing too early means fighting processes that would have finished on their own.

### Fix 2: Update chipset, storage, and graphics drivers

The single highest-yield fix for 24H2 slowness.

1. Open **Device Manager**, expand **IDE ATA/ATAPI controllers**, **Storage controllers**, and **Display adapters**, and check for warning icons.
2. Visit your laptop manufacturer's support site and download the latest **chipset**, **storage (NVMe/SATA)**, and **graphics** drivers for your exact model — HP, Dell, and Lenovo all host model-specific driver packages on their official support sites.
3. Install chipset first, then storage, then graphics, rebooting between each — order matters because later drivers depend on the chipset being current.
4. For Intel systems, also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch anything the OEM package missed.
5. Reboot and re-check Task Manager baselines — driver-related stutter and interrupt storms usually vanish immediately after the right driver lands.

### Fix 3: Re-trim your startup apps

24H2 loves to re-enable things you turned off.

1. Open **Task Manager** > **Startup apps** and sort by **Startup impact**.
2. Disable everything rated **High** impact that you don't need within seconds of boot — updaters, chat clients, cloud storage, and manufacturer bloat are the usual suspects.
3. Check **Settings** > **Apps** > **Startup** as well — the two lists don't always match, and 24H2 sometimes repopulates this one.
4. Restart (not shut down — use **Restart** so Fast Startup doesn't mask the result) and time your boot.
5. If boot is still slow, open **Task Manager** > **Startup apps** again after the reboot and confirm your disables actually stuck — occasionally a repair install reverts them.

### Fix 4: Clear the update debris

Free the gigabytes 24H2 left behind.

1. Open **Settings** > **System** > **Storage** > **Temporary files**, check **Windows Update Cleanup**, **Delivery Optimization Files**, and **Previous Windows installation(s)** (Windows.old).
2. Click **Remove files** — this can free 10–30 GB, and a nearly full system drive is itself a major slowdown cause.
3. Run **Disk Cleanup** as administrator (`cleanmgr`), click **Clean up system files**, and remove anything update-related it offers.
4. Keep Windows.old for a week or two in case you need the rollback option (Settings > System > Recovery > Go back), then delete it.
5. After cleanup, check that your C: drive has at least 15–20% free space — SSDs slow down measurably when nearly full.

### Fix 5: Repair stuck Windows Update components

For updates that never quite finish.

1. Open **Settings** > **Windows Update** and install everything pending, restarting as requested until no updates remain.
2. If updates fail or loop, run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
3. Still stuck? Open an elevated terminal and run `net stop wuauserv`, `net stop bits`, rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then `net start wuauserv` and `net start bits` — this forces a fresh update state.
4. Check for optional driver updates under **Windows Update** > **Advanced options** > **Optional updates** — 24H2-era driver fixes often hide here.
5. Microsoft's [Update Catalog](https://www.catalog.update.microsoft.com/) carries standalone installers if Windows Update itself refuses to fetch a specific fix.

### Fix 6: Check and repair system files

For upgrades that left corruption behind.

1. Open an elevated terminal (right-click Start > **Terminal (Admin)**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to complete — this repairs the component store the upgrade may have damaged.
3. Then run `sfc /scannow` to fix individual corrupted system files.
4. Reboot and test — file corruption from a glitchy upgrade commonly shows up as random app hangs and Explorer stutter.
5. If SFC reports unfixable corruption, an in-place repair install (using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) media, choosing **Keep personal files and apps**) fixes it without wiping your data.

### Fix 7: Reset the power plan and visual settings

Quick wins the update may have undone.

1. Go to **Settings** > **System** > **Power & battery** > **Power mode** and set it to **Best performance** while plugged in.
2. Open **Control Panel** > **Power Options** and confirm the active plan is what you expect — 24H2 sometimes resets custom plans.
3. In **Settings** > **Accessibility** > **Visual effects**, turn off **Transparency effects** and **Animation effects** — these cost GPU cycles on integrated graphics.
4. Check **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** and confirm **Hardware-accelerated GPU scheduling** is on if your GPU supports it.
5. Compare responsiveness before and after — on older integrated GPUs, the visual-effects toggle alone can make the UI feel dramatically snappier. Our [24H2 slowdown guide for Lenovo systems](/articles/how-to-fix-windows-11-slow-after-24h2-update-on-lenovo-laptop/) covers brand-specific variants of these steps.

## Closing

Post-24H2 slowness is frustrating precisely because the update caused it, but it's rarely permanent damage — it's unfinished business. Update the drivers the upgrade disturbed, re-trim the startup list it repopulated, clear the debris it left behind, and give background tasks their 72 hours. Do that, and 24H2 should feel like an upgrade again instead of a downgrade.
