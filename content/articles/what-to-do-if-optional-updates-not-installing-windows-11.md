---
title: "Optional Updates Won't Install on Windows 11? Here's What to Do"
slug: what-to-do-if-optional-updates-not-installing-windows-11
date: 2026-09-18
categories: ["windows-update"]
tags: ["windows 11", "optional updates", "windows update", "drivers"]
description: "Optional updates stuck, failing, or looping on Windows 11? This technician's guide walks you through diagnosing the cause and getting them installed."
thumbnail: "/images/thumbs/what-to-do-if-optional-updates-not-installing-windows-11.webp"
faqs:
  - q: "What are optional updates in Windows 11?"
    a: "Optional updates are a separate category in Windows Update containing driver updates, firmware, and non-security improvements that Microsoft does not consider mandatory. They appear under Advanced options rather than installing automatically. Installing them is usually safe and can fix hardware quirks, but skipping them will not leave your system insecure, since critical security patches arrive through the regular update channel regardless."
  - q: "Is it safe to skip optional updates?"
    a: "Yes, in most cases. Optional updates are not security patches, so skipping them does not expose your laptop to known vulnerabilities. The main downside is missing out on driver improvements that could fix device-specific problems like audio glitches or Wi-Fi drops. If a particular optional update keeps failing, skipping it and installing the driver from your manufacturer's website is a perfectly reasonable alternative."
  - q: "Why do optional updates keep failing with an error?"
    a: "The most common reasons are a corrupted download cache, a driver version conflict where a newer driver is already installed, a metered connection blocking the download, or a pending restart holding up the install queue. Checking the exact error code in Update history narrows it down fast. Clearing the SoftwareDistribution cache resolves the majority of repeat failures without touching anything else on the system."
  - q: "How do I install optional updates manually?"
    a: "You can download the exact package from the Microsoft Update Catalog by searching for its KB number, which you will find in Update history. Run the downloaded installer as an administrator and restart afterward. For driver-type optional updates, an even better route is often the laptop manufacturer's support site, which usually hosts a newer version of the same driver with its own installer."
---

You open Settings, head to Windows Update, and there they sit: a list of optional updates that refuse to install. They fail silently, throw a vague error code, or reinstall themselves every time you check. It is annoying, but it is rarely dangerous — optional updates are exactly that: optional. Still, they often contain driver fixes and firmware improvements your laptop could genuinely use.

When [optional updates keep failing on Windows 11](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop/), the culprit is almost always a stale download cache, a driver that is already installed in a newer form, or a policy quietly blocking the install. The good news is that the fix is usually quick once you know which of those you are dealing with. This guide walks you through the diagnosis and repair in the order a technician would do it.

## Why this happens

- **A newer driver is already installed:** Windows Update sometimes offers a driver that is older than the one already on your system. The installer detects the conflict and aborts, which shows up as a failed optional update even though nothing is actually wrong.
- **Corrupted download cache:** Optional updates download into the same SoftwareDistribution folder as regular updates. If those files are incomplete or corrupted, every install attempt fails at the same point until the cache is cleared.
- **Metered connection is enabled:** Windows 11 pauses most optional downloads on metered connections to save data. The updates appear in the list but never progress, which looks like a stall rather than a policy block.
- **A pending restart is holding the queue:** Some updates cannot install until the laptop restarts. If a restart has been deferred for days, new optional items pile up behind it and every install attempt quietly fails.
- **Third-party driver tools are fighting Windows Update:** OEM utilities and third-party driver updaters can lock driver files or install competing versions, causing Windows Update's own driver installs to fail with generic errors.
- **Low disk space in the driver store:** Driver packages need room in the driver store and the WinSxS folder. On laptops with small SSDs that are nearly full, optional updates fail during the staging phase.
- **Group policy or registry deferral:** On some systems, a policy disables optional content delivery or defers it indefinitely. This is common on former work or school laptops that still carry old management settings.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the actual error before touching anything

Optional updates fail for boring reasons more often than dramatic ones, so start by reading what Windows is actually telling you. Open Settings, go to Windows Update, then Update history, and expand the failed optional item to see its error code. If you have been dealing with [driver updates failing inside Windows Update](/articles/how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2/), this step also tells you whether the optional item and the driver failure share the same root cause.

1. Open Settings with Win + I and go to Windows Update.
2. Click Update history and expand the failed optional update entry.
3. Note the exact error code, then click Retry once to rule out a one-off glitch.
4. If it fails again with the same code, move on to the next fix instead of hammering Retry.

### Fix 2: Clear the SoftwareDistribution download cache

A corrupted download cache is the single most common cause of optional updates that fail repeatedly at the same percentage. Resetting it forces Windows to re-download clean copies. This does not remove installed updates or personal files — it only clears pending downloads.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv and net stop bits to pause the update services.
3. Open File Explorer and navigate to C:\Windows\SoftwareDistribution\Download.
4. Delete everything inside the Download folder, then restart the two services with net start wuauserv and net start bits.
5. Return to Windows Update and check for updates again.

### Fix 3: Run the Windows Update troubleshooter

Windows 11 ships with a dedicated troubleshooter that repairs broken update components, resets permissions on update folders, and re-registers update DLLs. It resolves a surprising number of optional update failures with one click, and [Microsoft's own support guidance](https://support.microsoft.com/en-us/windows) recommends it as the first automated step.

1. Open Settings, go to System, then Troubleshoot.
2. Click Other troubleshooters and find Windows Update.
3. Click Run and let the troubleshooter complete without interrupting it.
4. Apply any fixes it suggests, restart the laptop, and retry the optional updates.

### Fix 4: Install the driver from the manufacturer instead

Many optional updates are just drivers that the manufacturer also publishes on its own support site — often newer and better tested than the Windows Update copy. If the optional item is a display, audio, Wi-Fi, or chipset driver, grab it from Dell, HP, Lenovo, or your laptop maker's support page and install it directly. Once the newer driver is in place, the optional update usually disappears from the list on its own.

1. Identify the failing item in Update history (note the device name and version).
2. Visit your laptop manufacturer's support site and search your exact model.
3. Download the matching driver and install it following the on-screen prompts.
4. Restart the laptop, then check Windows Update to confirm the optional item is gone.

### Fix 5: Turn off the metered connection setting

If your Wi-Fi is flagged as metered, Windows 11 will hold optional updates back indefinitely. This is easy to miss because the updates still appear in the list — they just never download. Disabling the metered flag lets them through immediately.

1. Open Settings and go to Network and internet, then Wi-Fi.
2. Click your connected network name.
3. Toggle Metered connection to Off.
4. Go back to Windows Update and click Check for updates to start the downloads.

### Fix 6: Install the update manually from the Microsoft Update Catalog

When Windows Update itself is the bottleneck, you can bypass it entirely. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) hosts the same packages as standalone installers. Search for the KB number or driver name from your update history, download the file matching your system (x64 for most laptops), and run it.

1. Copy the KB number or exact update title from Update history.
2. Search for it on the Microsoft Update Catalog site.
3. Download the version matching your architecture and Windows build.
4. Run the downloaded file as administrator and restart when prompted.

## Closing

Optional updates that refuse to install look alarming but are almost never a sign of serious damage — they are usually a cache problem, a version conflict, or a quiet policy block. Work through the fixes above in order, and install stubborn drivers straight from the manufacturer when Windows Update will not cooperate. Your laptop will be fully patched and running smoothly without the failed-update clutter.
