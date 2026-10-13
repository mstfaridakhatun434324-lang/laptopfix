---
title: "KB5048667 Fails to Install on Windows 11 24H2? Here's the Fix"
slug: how-to-fix-kb5048667-fails-to-install-in-windows-11-24h2
date: 2026-09-23
categories: ["windows-update"]
tags: ["windows 11", "kb5048667", "windows update", "troubleshooting"]
description: "KB5048667 failing or rolling back on Windows 11 24H2? Follow these targeted fixes to get the cumulative update installed successfully."
thumbnail: "/images/thumbs/how-to-fix-kb5048667-fails-to-install-in-windows-11-24h2.webp"
faqs:
  - q: "What happens if I never install KB5048667?"
    a: "Your laptop keeps running, but it misses the security fixes and quality improvements bundled in that cumulative update. Over time, skipped cumulative updates compound: later updates assume earlier ones installed cleanly, so prolonged avoidance can make future updates harder to install. It is better to fix the install failure once than to dodge the update indefinitely."
  - q: "Why does KB5048667 roll back during restart?"
    a: "Rollbacks at restart mean the failure happened while applying low-level system changes — the phase where drivers and the servicing stack are involved. Outdated storage or display drivers, a damaged component store, or interference from security software are the usual causes. Updating drivers, repairing with DISM and SFC, and installing from a clean boot address all three."
  - q: "Is the manual installer the same as Windows Update?"
    a: "Yes. The .msu package from the Microsoft Update Catalog contains the identical update payload; only the delivery mechanism differs. Manual installation is a legitimate, widely used troubleshooting step — not a hack. Just be sure to download the package matching your Windows version and architecture from the official catalog."
  - q: "How do I know if a servicing stack update is missing?"
    a: "Check Update history for servicing stack updates listed near the top — they install separately from cumulative updates. If one failed or never appeared, download the latest servicing stack update for your Windows 11 build from the Microsoft Update Catalog, install it, restart, and then retry KB5048667. The cumulative update's staging depends on the servicing stack being current."
---

Another Patch Tuesday, another cumulative update that will not install. KB5048667 fails on Windows 11 24H2 with the familiar symptoms: an error code in Update history, a rollback during restart, or an install that reaches 100% and then quietly reverts. Your laptop works fine without it, but each failed attempt leaves behind partial state that makes the next attempt more likely to fail too.

The good news is that KB install failures follow a short list of causes, and they respond to a short list of fixes. This guide focuses on the ones that actually resolve KB5048667 failures — cache resets, component store repairs, and the manual install path — rather than generic advice. Work through them in order and the update will go through.

There is also a psychological trap with repeated KB failures: each failed attempt trains you to expect failure, so you start trying riskier fixes — registry cleaners, update blockers, obscure scripts. Resist that. The boring fixes below resolve the overwhelming majority of KB5048667 failures, and they do it without putting the system at risk.

## Why this happens

- **Damaged update cache:** The downloaded KB5048667 package may be incomplete or corrupted. Windows Update keeps retrying the same damaged files, so the failure repeats at the same stage every time.
- **Component store corruption:** Cumulative updates modify hundreds of system components. If the component store is inconsistent, the installer fails its integrity checks and rolls the update back.
- **Missing servicing stack update:** KB5048667 can depend on a servicing stack update that must install first. Without it, the cumulative update cannot stage and the install aborts.
- **Disk space shortage:** Staging a cumulative update needs gigabytes of free space. When the drive is nearly full, the install fails during file expansion with little warning.
- **Driver conflict at restart:** The restart phase applies low-level changes where an outdated storage, display, or security driver can collide with the update and force a rollback.
- **Third-party security software:** Antivirus and endpoint tools that intercept file writes can break the update's atomic file replacements, failing the install midway.
- **Stuck predecessor update:** An earlier update left in a pending or failed state blocks the queue. KB5048667 cannot install until that earlier item is resolved or cleared.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the error code and failure stage

Targeted fixes beat shotgun fixes. The error code in Update history plus the stage where KB5048667 fails — download, install, or restart — tells you which of the remaining fixes to prioritize. If the failure affects every cumulative update rather than this KB alone, the [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-to-install-after-windows-11-update/) is the better starting point. Write down whether the failure happens at the same percentage each time — that detail alone distinguishes cache corruption from servicing damage.

1. Open Settings, Windows Update, Update history, and expand the failed KB5048667 entry.
2. Write down the error code and whether it failed during download, installation, or restart.
3. If a web search on the code plus KB5048667 shows a known issue, apply that specific guidance first.
4. Otherwise continue with the general repair sequence below.

### Fix 2: Clear the update cache and retry

This resolves the most common pattern: a corrupted download failing at the same point. A clean cache means a clean download, and the retry often succeeds on the first attempt afterward.

1. Open Command Prompt as administrator.
2. Run net stop wuauserv and net stop bits.
3. Empty C:\Windows\SoftwareDistribution\Download completely.
4. Run net start wuauserv and net start bits, then check for updates.

### Fix 3: Repair the component store

When the failure happens during installation rather than download, suspect the component store. DISM restores its health from online sources, and SFC then fixes any protected files that reference it. When built-in automated repair is needed, the [Windows Update troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) goes deeper.

1. In an elevated Command Prompt, run DISM /Online /Cleanup-Image /RestoreHealth.
2. When it finishes, run sfc /scannow.
3. Restart the laptop after both complete.
4. Attempt the KB5048667 install again from Windows Update.

### Fix 4: Perform a clean boot and install

Third-party startup programs and services are a frequent hidden cause of install failures and restart rollbacks. A clean boot strips them away so the update installs against a pristine system state.

1. Press Win + R, type msconfig, and open System Configuration.
2. On the Services tab, check Hide all Microsoft services, then click Disable all.
3. On the Startup tab, open Task Manager and disable all startup items.
4. Restart, run Windows Update to install KB5048667, then re-enable your services afterward.

### Fix 5: Install the update manually

The standalone installer bypasses the entire Windows Update pipeline — cache, services, and BITS queue alike. When every automated attempt fails, this is the dependable path that still delivers the exact same update.

1. Search for KB5048667 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
2. Download the x64 package for Windows 11 24H2.
3. Right-click the .msu file and run it as administrator.
4. Restart when prompted and verify success in Update history.

### Fix 6: Check disk space and driver health

Two environmental causes deserve a look before you declare the system broken: a full drive and an outdated low-level driver. Both cause failures that look like update bugs but are really resource problems.

1. Ensure at least 20 GB free on the system drive using Storage settings.
2. Update storage controller and display drivers from the manufacturer's website — [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can identify the right ones automatically.
3. Retry the KB5048667 install after both are addressed.

## Closing

KB5048667 failures look stubborn but they yield to method: identify the failure stage, clear the corrupted cache, repair the component store, and eliminate third-party interference with a clean boot. The manual installer from the Update Catalog stands ready as the final word. Run through these in order and the update installs — no more watching it roll back.
