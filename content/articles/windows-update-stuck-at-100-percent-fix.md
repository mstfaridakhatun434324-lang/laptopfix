---
title: "Windows Update Stuck at 100%? 7 Fixes That Actually Work"
slug: windows-update-stuck-at-100-percent-fix
date: 2026-10-02
categories: ["windows-update"]
tags: ["windows update", "stuck", "windows 11", "troubleshooting"]
description: "Windows Update frozen at 100% for hours? Don't force-shutdown yet — try these 7 safe fixes, from the Update troubleshooter to resetting components."
thumbnail: "/images/thumbs/windows-update-stuck-at-100-percent-fix.webp"
faqs:
  - q: "How long should I wait before deciding Windows Update is truly stuck?"
    a: "For a monthly quality update, 30 to 60 minutes with visible disk activity is normal. Feature updates can take one to three hours on a mechanical hard drive or a nearly full SSD. Only treat the update as stuck if the screen has not changed for two to three hours and there is no disk activity — a dark disk LED, or Task Manager showing disk usage at zero."
  - q: "Is it safe to force-shutdown a PC stuck at 100%?"
    a: "It is a last resort, not a first step. Cutting power mid-update can corrupt the component store and leave Windows unbootable, which takes far longer to repair than simply waiting. If you must do it, hold the power button once, then work through the fixes in this guide — especially renaming the SoftwareDistribution folder — before checking for updates again."
  - q: "Why does my laptop get stuck on updates so often?"
    a: "Laptops are more likely to have the three ingredients of a stuck update: a nearly full drive, a slower hard disk or older SSD, and aggressive power-saving that suspends background tasks. Keeping 20 to 30 GB free, updating drivers regularly, and letting updates run while plugged in all reduce the chances of a stall."
  - q: "Will renaming the SoftwareDistribution folder delete my files?"
    a: "No. That folder only holds temporary update downloads and the update history log. Windows rebuilds it automatically the next time you check for updates. Your documents, apps, and settings are completely untouched."
---

Few screens are as nerve-wracking as a progress bar parked at 100%. You have been watching "Working on updates" or "Getting Windows ready — don't turn off your computer" for well over an hour, the disk light flickers occasionally, and you are seriously weighing whether holding the power button is worth the risk. This is one of the most common Windows Update complaints on laptops, and fortunately a genuinely frozen update is rarer than it feels.

Most of the time, that 100% refers to only one phase of the installation — the download, the pre-install, or the post-reboot configuration — while other work continues invisibly in the background. Interrupting it can corrupt the update and turn a slow install into an unbootable PC, so patience and the right order of checks almost always win. Work through the fixes below from safest to most involved, and stop as soon as your update finishes.

## Why this happens

- **Misleading multi-phase progress.** Windows reports each stage (downloading, installing, rebooting, configuring) as its own bar, so 100% on one phase while the next quietly prepares is normal — not frozen.
- **A slow or nearly full drive.** Feature updates copy gigabytes of data and need room to stage it. On a nearly full disk or an older HDD, the final "configuring" phase can crawl for an hour with the bar sitting at 100%.
- **Corrupted temporary update files.** A partially downloaded package in the SoftwareDistribution folder can make the installer loop on the same stage forever.
- **A conflicting driver or security program.** Third-party antivirus and old storage or chipset drivers can block the final configuration pass, especially after major feature updates.
- **A previously interrupted update.** An earlier force-shutdown or sleep during an install leaves the update state inconsistent, and the next attempt stalls where the last one died.

## How to fix it

Start with Fix 1 — most "stuck" updates aren't actually stuck — and move down the list only if the previous step changes nothing.

### Fix 1: Wait it out (longer than you think)

Monthly quality updates usually finish in 30 to 60 minutes; feature updates can take one to three hours on an HDD or a nearly full SSD. Only treat the update as stuck if the screen has not changed for two to three hours **and** there is no disk activity — a dark disk LED, or Task Manager's Performance tab showing disk usage at 0%.

1. Keep the laptop plugged in — power-saving sleep can pause the install mid-way.
2. Leave it alone for at least two hours from the moment it hit 100%.
3. Do **not** force-shutdown during this window. Cutting power mid-update risks corrupting the component store and leaving Windows unbootable, a far bigger repair than waiting.

### Fix 2: Run the Windows Update troubleshooter

If you can reach the desktop, Windows can often diagnose its own updater.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow the prompts.
3. Restart the PC when it finishes, then go to **Settings > Windows Update** and click **Check for updates**.

### Fix 3: Restart the Windows Update and BITS services

A hung background service is a classic cause, and restarting both takes about a minute.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Update** (service name `wuauserv`), right-click it, and choose **Restart** (or Stop, then Start).
3. Do the same for **Background Intelligent Transfer Service** (service name `bits`).
4. Go back to **Settings > Windows Update** and retry. If the update was mid-install, reboot first so the installer can resume cleanly.

### Fix 4: Rename the SoftwareDistribution folder

This clears corrupted temporary downloads without touching your files.

1. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
2. Run `net stop wuauserv` and then `net stop bits`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `net start wuauserv` and then `net start bits`.
5. Go to **Settings > Windows Update** and check for updates again — Windows rebuilds the folder from scratch.

### Fix 5: Repair system files with SFC and DISM

If the update engine itself is damaged, repairing the component store usually unblocks it.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` (takes 15 to 30 minutes — let it finish).
2. When it completes, run `sfc /scannow` and wait for the verification to reach 100%.
3. Restart the PC, then retry the update at **Settings > Windows Update**.

### Fix 6: Free up disk space

Feature updates need staging room — aim for at least 20 to 30 GB free on the system drive.

1. Open **Settings > System > Storage** and review **Cleanup recommendations**; remove temporary files and uninstall apps you no longer use.
2. Search for `cleanmgr`, open Disk Cleanup, click **Clean up system files**, then check **Windows Update Cleanup** and **Temporary files**.
3. Empty the Recycle Bin, reboot, and retry the update.

### Fix 7: Install the update manually from the Microsoft Update Catalog

If automatic update keeps stalling, the standalone installer often succeeds. Use this as the last resort, once the PC is booted normally.

1. Find the stuck update's KB number at **Settings > Windows Update > Update history**.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number, and download the version matching your system (usually **x64**).
3. Right-click the downloaded `.msu` file, run it as administrator, and reboot when prompted. If the install fails with a specific error code such as 0x800F081F, see our guide on [fixing Windows Update error 0x800F081F](/articles/fix-windows-update-error-0x800f081f/) for the repair steps.

Most stuck updates resolve by Fix 4, so don't skip ahead — the safest fixes are first for a reason. And if your update finishes but leaves something broken afterward (wireless adapters are a frequent casualty), see how to fix [Wi-Fi not working after a Windows 11 update](/articles/wifi-not-working-after-windows-11-update-fix/). Patience matters here too — some updates genuinely need an hour on slower drives before the percentage moves.
