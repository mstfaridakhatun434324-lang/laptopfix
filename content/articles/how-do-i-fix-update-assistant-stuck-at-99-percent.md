---
title: "How to Fix Windows Update Assistant Stuck at 99 Percent"
slug: how-do-i-fix-update-assistant-stuck-at-99-percent
date: 2026-10-01
categories: ["windows-update"]
tags: ["update assistant", "stuck at 99", "windows 11", "feature update"]
description: "Update Assistant stuck at 99 percent for hours? Here's why it happens and 7 proven fixes — from patience checks to clean update cache resets — to finish the update."
thumbnail: "/images/thumbs/how-do-i-fix-update-assistant-stuck-at-99-percent.webp"
faqs:
  - q: "Is it normal for Update Assistant to sit at 99 percent for a long time?"
    a: "Yes, up to a point. The last few percent involve driver migration and component registration, which can take 30 to 60 minutes on slower laptops. If the progress bar and disk activity stop moving entirely for over two hours, the update has genuinely stalled and you should work through the fixes in this guide."
  - q: "Will restarting my laptop break anything while Update Assistant is at 99 percent?"
    a: "A restart during an in-progress feature update can corrupt the update state, so don't force a shutdown unless the process is clearly frozen. First try ending the assistant through Task Manager and restarting the update service. If nothing moves after several hours, a single restart is usually safe and Windows will roll back to the previous build."
  - q: "Why does Update Assistant get stuck at exactly 99 percent?"
    a: "Ninety-nine percent is typically where the assistant copies final system files, migrates drivers, or verifies downloaded packages. A corrupted download, a conflicting third-party driver, or low disk space can halt it right there. The assistant shows no error code at this stage, which is why checking update logs helps diagnose it."
  - q: "Do I need Update Assistant at all, or can I update another way?"
    a: "You don't need it. Windows Update in Settings installs the same feature updates, and the Media Creation Tool from Microsoft's download page performs the same upgrade with better error handling. If the assistant repeatedly stalls, switching to Windows Update or the Media Creation Tool often finishes the job without the freeze."
---

You've watched the progress bar crawl to 99 percent, and then... nothing. The Windows Update Assistant just sits there, hour after hour, and the percentage refuses to budge. It's one of the most nerve-wracking places a Windows laptop can get stuck, because closing the wrong thing at the wrong moment could mean a corrupted install. Take a breath — in almost every case, this is fixable without losing a single file.

The good news is that a stall at 99 percent usually means the heavy lifting is done: the update files are already downloaded, and the failure is happening in the final file-copy or verification stage. That gives us a lot of options. If your download seems to stall earlier in the process, also see our guide to [update downloads that stall out](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) before continuing.

## Why this happens

- **Corrupted downloaded files** — A single bad packet during the download can break package verification at the final stage, and the assistant has no way to skip it.
- **Low disk space on the system drive** — The last percent needs scratch space for temporary files; if C: is nearly full, the copy step stalls silently.
- **Conflicting third-party drivers** — Antivirus filters, old display drivers, or third-party disk tools can block file operations during the final migration phase.
- **Damaged SoftwareDistribution cache** — The local update cache can contain stale or half-written metadata that the assistant can't reconcile.
- **Windows Update service stuck in a bad state** — Services like wuauserv or BITS can hang after hours of work, freezing the pipeline that feeds the assistant.
- **Metered connection throttling** — If Windows treats your connection as metered, background delivery can quietly pause, leaving the assistant waiting.
- **Failing storage or RAM errors** — Rare but real: bad sectors or flaky memory corrupt files as they're written, and the verification step never passes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it a real deadline, then check for actual activity

The first fix costs nothing: don't assume it's frozen too early. The final percent on a spinning hard drive or a low-power laptop can legitimately take 60 to 90 minutes while drivers migrate and the registry finalizes.

1. Note the current time and the exact percentage, then leave the laptop plugged in and untouched for one hour.
2. Open Task Manager (Ctrl + Shift + Esc) and watch the **Disk** column. If any system process shows steady disk activity, work is still happening.
3. Check that the progress number hasn't changed at all. If there's zero disk activity and zero movement for a full hour, move to Fix 2.
4. Do not put the laptop to sleep during this wait — open Settings > System > Power & battery and set sleep to **Never** temporarily.

### Fix 2: End the assistant and restart the update services

If activity is truly dead, the safest first intervention is a clean restart of the update pipeline rather than a hard reboot.

1. Press Ctrl + Shift + Esc to open Task Manager, find **Windows Update Assistant** (Windows10UpgraderApp.exe) and any SetupHost processes, and end them.
2. Press Win + R, type `services.msc`, and press Enter.
3. Restart the **Windows Update**, **Background Intelligent Transfer Service**, and **Cryptographic Services** entries by right-clicking each one.
4. Re-run Update Assistant. If you need a fresh copy of Microsoft's tools, the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) always has the current version.
5. If it stalls at 99 percent again, note how long it takes to get there — a fast stall suggests cached corruption (Fix 3).

### Fix 3: Clear the SoftwareDistribution and catroot2 caches

Corrupted cache files are the single most common cause of a hard 99-percent stall, and clearing them forces Windows to re-download only what's broken.

1. Open an elevated Command Prompt: search for **cmd**, right-click it, and choose **Run as administrator**.
2. Stop the update services by running `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, and `net stop msiserver`, pressing Enter after each.
3. Delete the contents of `C:\Windows\SoftwareDistribution\Download` (leave the folder itself) and rename `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services with `net start wuauserv`, `net start bits`, `net start cryptsvc`, and `net start msiserver`.
5. Reboot, then run the assistant again. The download phase may take a while, but the final percent should now complete.

### Fix 4: Free up space on the system drive

Feature updates need 20 GB or more of breathing room, and the failure mode for not having it is a silent stall near the end.

1. Open Settings > System > Storage and check free space on C:. If it's under 25 GB, act now.
2. Run Disk Cleanup as administrator and tick **Windows Update Cleanup**, **Temporary files**, and **Delivery Optimization Files**.
3. Move large personal folders (Videos, Downloads) to an external drive temporarily.
4. Uninstall programs you don't use from Settings > Apps > Installed apps.
5. Try the assistant again — and if your laptop model has a similar stuck-at-99 report, compare notes with our [Lenovo-specific walkthrough](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-lenovo-laptop/).

### Fix 5: Remove conflicting software and update drivers first

Third-party antivirus suites and old drivers are classic culprits for freezing the final migration step.

1. Temporarily uninstall any third-party antivirus (keep Windows Defender active) — its file-system filter is the usual blocker.
2. Disconnect unnecessary USB devices, docks, and external drives; they can complicate driver migration.
3. Update your chipset and storage drivers from your laptop maker's support site before retrying.
4. If the stall involves audio or display drivers specifically, run the standalone [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) first.
5. Retry the assistant with only the essentials connected.

### Fix 6: Switch to Windows Update or the Media Creation Tool

If the assistant itself is the problem, sidestep it — both alternatives install the identical feature update with different (and often better) error handling.

1. Go to Settings > Windows Update and click **Check for updates**; install the feature update from there instead.
2. If Settings also stalls, download the Media Creation Tool from Microsoft's [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and choose **Upgrade this PC now**.
3. The Media Creation Tool performs the same in-place upgrade while keeping your files and apps.
4. If both stall at the same percentage, return to Fix 3 and Fix 4 — the underlying cause is environmental, not the tool.

### Fix 7: Repair system files and run the update in a clean boot

When everything else stalls, corrupted system components or a background conflict is usually responsible.

1. Run `sfc /scannow` and then `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt, rebooting between them.
2. Press Win + R, type `msconfig`, and on the Services tab hide all Microsoft services, then disable the rest; on the Startup tab, open Task Manager and disable all startup items.
3. Reboot into this clean state and run Update Assistant once more.
4. If it completes, re-enable services in halves to find the conflicting program.
5. As a last resort, use Reset this PC with **Keep my files** — it refreshes Windows while preserving your data.

## Closing

A 99-percent stall looks catastrophic, but it almost always comes down to a corrupted cache, tight disk space, or a conflicting driver — all fixable with the steps above. Work through them patiently, keep the laptop plugged in and awake, and resist the urge to force a shutdown unless the process is truly frozen. Once the update completes, your laptop will be current, and the assistant's drama will be a story, not a problem.
