---
title: "KB5036893 Stuck Downloading on Your Dell Laptop? Here's How to Fix It"
slug: how-to-fix-kb5036893-stuck-downloading-on-dell-laptop
date: 2026-09-03
categories: ["windows-update"]
tags: ["kb5036893", "stuck download", "dell laptop", "windows 11", "update fix"]
description: "KB5036893 stuck at 0% or looping on your Dell laptop? These Dell-specific and Windows fixes get the download moving again without breaking anything."
thumbnail: "/images/thumbs/how-to-fix-kb5036893-stuck-downloading-on-dell-laptop.webp"
faqs:
  - q: "Why does KB5036893 get stuck downloading specifically on Dell laptops?"
    a: "Dell laptops frequently combine two friction points: Dell's own SupportAssist and driver layers competing with Windows Update for bandwidth and locks, plus enterprise-style Dell firmware settings that delay certain payloads. When the Windows Update cache corrupts mid-download, the progress bar freezes — commonly at 0%, 20%, or 99% — and retrying from Settings alone rarely clears the underlying stall."
  - q: "How long should I wait before deciding the download is truly stuck?"
    a: "Give it a full two hours on a stable connection before intervening. Cumulative updates verify cryptographic signatures and merge delta packages, which looks like zero progress. If the percentage hasn't moved after two hours and Delivery Optimization shows no network activity in Task Manager, treat it as stuck and work through the fixes in this guide."
  - q: "Is it safe to restart my Dell while KB5036893 is stuck downloading?"
    a: "Yes — restarting during the download phase is safe, because nothing has been staged for installation yet. The risk window is during installation and the reboot phase, when interrupting can corrupt the component store. A plain restart while the bar is frozen on 'Downloading' is a legitimate first troubleshooting step."
  - q: "Can I just install KB5036893 manually instead of waiting?"
    a: "Yes. Search for KB5036893 on the Microsoft Update Catalog, download the x64 package matching your Windows build, and run the .msu file. Manual installation bypasses the corrupted download cache entirely. After it installs, run a Dell driver check so firmware and chipset drivers stay aligned with the updated OS."
---

You're watching the same number on the screen for the second hour in a row: KB5036893, downloading, 0%. Or maybe 20%. Or the particularly cruel 99%. Your Dell laptop is otherwise fine — Wi-Fi works, everything else is responsive — but this one update refuses to finish pulling down its payload. The instinct is to keep hammering 'Retry download,' but that almost never works, because the stall isn't a button problem. It's a corrupted cache problem, a competing-service problem, or a Dell-specific layer getting in the way.

KB5036893 is a Windows 11 cumulative update, and like all cumulative updates it arrives as a large signed package that Windows verifies chunk by chunk. On Dell machines, the usual suspects multiply: SupportAssist's background updater, Dell's firmware-level update scheduling, a Delivery Optimization cache that has gone stale, or a SoftwareDistribution folder with a half-written manifest. The good news is that every one of these has a deterministic fix. For a newer cousin of this exact problem, see our guide on [KB5055523 stuck downloading on Dell laptops](/articles/how-to-fix-kb5055523-stuck-downloading-on-dell-laptop/).

Before you touch anything, confirm the basics: you need at least 10 GB free on the system drive, a stable (not metered) connection, and no third-party 'PC optimizer' running a background scan. Then work through the fixes below in order. The early ones are gentle and take minutes; the later ones reset the update machinery itself.

## Why this happens

- **Corrupted SoftwareDistribution cache**: The download cache under C:\Windows\SoftwareDistribution holds partial package data. A single bad manifest or interrupted write makes the downloader loop forever without failing cleanly.
- **Delivery Optimization stall**: Peer-to-peer and CDN sources can both wedge when the local cache index disagrees with the server manifest, freezing progress at a fixed percentage.
- **Dell SupportAssist conflicts**: Dell's updater sometimes locks the same driver payloads Windows Update is trying to fetch, creating a tug-of-war that stalls the download phase.
- **Metered connection quietly enabled**: Dell laptops moved between hotspots and office Wi-Fi often inherit a metered flag, which silently pauses large update downloads.
- **Insufficient staging space**: Cumulative updates need working room beyond their download size for extraction and verification — tight SSDs stall the process mid-way.
- **Stuck Background Intelligent Transfer Service**: BITS manages the actual download; if its queue corrupts, the percentage counter stops advancing even though the service reports running.
- **Antivirus download interception**: Some third-party security suites scan each chunk as it arrives and can hold the file handle open, blocking the final assembly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it a real deadline, then restart the update services

Don't intervene in the first hour — early progress is genuinely invisible while signatures verify. But once two hours pass with zero movement and no network activity from the update processes, stop waiting and restart the two services that own the download. This clears transient wedges without touching your data.

1. Open Task Manager (Ctrl + Shift + Esc) → Performance → Wi-Fi or Ethernet and confirm update-related network traffic is flat at 0 Kbps.
2. Press Win + R, type `services.msc`, and press Enter.
3. Right-click **Windows Update** → Restart. Then right-click **Background Intelligent Transfer Service** → Restart.
4. Go to Settings → Windows Update and click **Retry**. Watch for 10 minutes to see if the percentage advances.

### Fix 2: Check the metered connection and Delivery Optimization settings

A metered flag is the quietest cause of a stuck download — Windows simply refuses to pull large payloads. Delivery Optimization problems compound it by wedging the peer cache.

1. Go to Settings → Network & internet → Wi-Fi (or Ethernet), open your connection, and make sure **Metered connection** is OFF.
2. Go to Settings → Windows Update → Advanced options → **Delivery Optimization**.
3. Toggle **Allow downloads from other PCs** off and back on to rebuild the peer cache index.
4. Click **Check for updates** again and observe whether the download resumes from a higher percentage.

### Fix 3: Pause Dell SupportAssist and Dell Update temporarily

Dell's background updaters can lock driver payloads that Windows Update also wants. Pausing them for the duration of the KB download removes the contention.

1. Open Dell SupportAssist (or Dell Update) from the Start menu.
2. Pause or disable automatic scanning and updating — look for a settings/gear option to turn off scheduled checks.
3. In Task Manager → Startup apps, temporarily disable SupportAssist entries, then restart the laptop.
4. Retry the KB5036893 download in Settings → Windows Update. Re-enable Dell's updaters afterward so firmware updates still arrive.

### Fix 4: Run the Windows Update troubleshooter

The built-in troubleshooter clears common registry flags and service states that manual restarts miss. It's quick and safe.

1. Go to Settings → System → **Troubleshoot** → **Other troubleshooters**.
2. Click **Run** next to Windows Update and let it complete.
3. Apply every fix it recommends, then restart the laptop when prompted.
4. Return to Settings → Windows Update and retry the download.

### Fix 5: Reset the SoftwareDistribution and catroot2 folders

This is the definitive fix for a corrupted download cache. You're deleting only the update working files — Windows rebuilds them automatically — not your documents or programs.

1. Open Command Prompt **as administrator**.
2. Stop the services: run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, and `net stop msiserver`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
5. Go to Settings → Windows Update → **Check for updates**. The KB will download fresh from 0% — this time with a clean cache. For the full component-reset walkthrough, see [how to reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).

### Fix 6: Free staging space on the system drive

Cumulative updates need elbow room. If your C: drive is under 10 GB free, the download can stall during the verification stage with no useful error.

1. Open Settings → System → **Storage** and check free space on C:.
2. Click **Temporary files**, select Delivery Optimization Files, Recycle Bin, and previous Windows installations you no longer need, then **Remove files**.
3. Uninstall one or two large apps or games you don't use if space is still tight.
4. Retry the update once you have at least 10–15 GB free.

### Fix 7: Install KB5036893 manually from the Update Catalog

If the in-place downloader simply won't cooperate, bypass it entirely with the standalone installer. This is Microsoft's own package — identical to what Windows Update would fetch.

1. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and search for **KB5036893**.
2. Download the x64 version matching your Windows 11 build (check Settings → System → About for your build number).
3. Double-click the .msu file and follow the installer; restart when prompted.
4. After rebooting, open Settings → Windows Update → **Check for updates** to confirm nothing is pending.

### Fix 8: Repair the component store, then retry

A damaged component store can make the downloader reject chunks it can't verify. DISM and SFC repair the underlying image so downloads validate cleanly.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to reach 100%.
3. Then run `sfc /scannow` and restart the laptop.
4. Retry the KB5036893 download. If it still stalls, install it manually via the Catalog (Fix 7) — the repaired store will accept the .msu cleanly.

## Closing

A KB stuck downloading on a Dell is almost always a cache or contention problem, not a broken laptop. Work the list top to bottom — restart services, clear the metered flag, quiet Dell's updaters, reset the cache — and the package will come down. The manual Catalog install is your guaranteed fallback: same Microsoft bits, no downloader drama. Related guides: [KB5055523 stuck downloading on Dell laptops](/articles/how-to-fix-kb5055523-stuck-downloading-on-dell-laptop/) and [how to reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).
