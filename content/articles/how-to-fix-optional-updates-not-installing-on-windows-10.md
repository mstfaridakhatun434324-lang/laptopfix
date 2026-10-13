---
title: "How to Fix Optional Updates Not Installing on Windows 10"
slug: how-to-fix-optional-updates-not-installing-on-windows-10
date: 2026-09-28
categories: ["windows-update"]
tags: ["optional updates", "driver updates", "windows 10", "not installing"]
description: "Optional updates won't install on Windows 10? Fix the optional update pipeline and get those driver updates installed."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-on-windows-10.webp"
faqs:
  - q: "Where do I find optional updates on Windows 10?"
    a: "Go to Settings > Update & Security > Windows Update > View optional updates. They are grouped into Driver updates and Other updates. Select the ones you want and click Download and install. If the section is missing entirely, a policy or registry setting may be hiding it — Fix 5 below covers that."
  - q: "Are optional driver updates safe on Windows 10?"
    a: "Generally yes — they are Microsoft-tested driver versions. But Windows 10's driver offerings skew older, and manufacturer drivers are usually newer and better matched to your hardware. For misbehaving hardware, try the optional update first; if it does not help, go to the manufacturer's site for the current driver."
  - q: "Why do optional updates fail when cumulative updates work?"
    a: "Optional updates install through the driver and firmware path rather than the main cumulative pipeline, so they fail for driver-specific reasons: the device is in use, a conflicting driver version is installed, or the driver package metadata is corrupted. The main update engine can be perfectly healthy while the optional path is broken."
  - q: "Can I just ignore optional updates on Windows 10?"
    a: "You can, and many people do — Windows 10 runs fine without them. But if a piece of hardware is misbehaving, the optional driver update for it is often the intended fix and is worth trying before deeper troubleshooting. Think of them as targeted medicine rather than required vitamins."
---

Windows 10 tucks its optional updates under **View optional updates**: driver updates and assorted extras that Microsoft offers but does not force. They are the first place to look when hardware misbehaves — a flaky network adapter, a sulking printer, audio that crackles. But sometimes they refuse to install: you select them, click install, and they fail or hang while the regular cumulative updates sail through without a problem.

Windows 10's driver servicing has a particular quirk that makes optional updates fussier here than on Windows 11. The driver store on a long-lived Windows 10 machine often contains multiple generations of drivers for the same device — inbox versions, manufacturer versions, previous Windows Update versions — and the ranking logic that decides which one "wins" can deadlock when the offered optional update does not clearly outrank what is installed. Add in devices whose drivers date back years and were never designed for in-place replacement, and you get a pipeline that fails on specific machines while working fine on others. It is not random; it is the accumulated history of that particular driver store.

That split — main updates fine, optional updates broken — tells you the optional pipeline has its own issue. This guide fixes that pipeline and shows you when to skip it for the manufacturer's driver instead.

## Why this happens

- **The target device is in use.** Driver files locked by running hardware cannot be replaced, failing the install.
- **A conflicting driver is already installed.** A newer or vendor-customized driver blocks the version Windows offers.
- **Corrupted optional update metadata.** Out-of-sync catalog data causes download or verification failures.
- **Standard user account.** Driver installation needs elevation that limited accounts cannot provide.
- **Firmware updates awaiting restart.** Staged firmware packages fail when the required reboot never happens.
- **Damaged update components.** Cache corruption affecting the optional pipeline independently of the main one.
- **Policy hiding optional updates.** Group Policy or registry settings disabling the optional updates UI or driver installation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install them one at a time

Turn an opaque batch failure into a clear single failure.

1. Open **Settings** > **Update & Security** > **Windows Update** > **View optional updates**.
2. Check only one driver update — preferably for hardware you actually use — and click **Download and install**.
3. Note the exact result. Single installs reveal which specific update is the problem instead of failing the whole batch mysteriously.

### Fix 2: Restart first, then install immediately

Beat the file locks.

1. Restart the laptop cleanly and, right after booting, install the optional update before opening other programs.
2. Fresh-boot installation avoids the in-use file failures that hit driver updates hardest.
3. If the update is firmware-class, do a full shutdown (hold **Shift** while clicking **Shut down**) instead of a restart, then install after powering on.

### Fix 3: Get the driver from the manufacturer

The pragmatic bypass that is often the better driver anyway.

1. Identify the device in **Device Manager**.
2. Download the current driver from the manufacturer: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA, AMD, or your laptop maker's support page.
3. Install it manually. Once the driver is current, the optional update entry usually disappears on the next scan.

### Fix 4: Reset the update components

Repair the delivery pipeline.

1. Open an elevated Command Prompt:
   ```
   net stop wuauserv
   net stop bits
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   net start wuauserv
   net start bits
   ```
2. Check for updates, then revisit **View optional updates**. Clean metadata rebuilds the list correctly.
3. For the full four-service reset, see [our update component repair guide](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/).

### Fix 5: Check for policies hiding optional updates

Make sure the UI is not suppressed.

1. Press **Windows key + R**, type `gpedit.msc`, and check **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Update** for policies disabling optional or driver updates. Set them to **Not configured**.
2. In the Registry, inspect `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for values like `ExcludeWUDriversInQualityUpdate` and remove them if you want driver updates offered.
3. Restart and check whether **View optional updates** now appears and functions.

### Fix 6: Run the troubleshooter and check system health

Cover the general repairs.

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters** > **Windows Update** > **Run the troubleshooter**.
2. Run `sfc /scannow` from an elevated Command Prompt to repair system file damage affecting the installer.
3. Retry the optional update. Persistent failure of one specific driver update means hiding it and using the manufacturer driver from Fix 3.

### Fix 7: Manage firmware updates separately

Treat firmware as the special case it is.

1. For optional firmware/BIOS updates, prefer the laptop manufacturer's own updater over Windows Update — it validates the hardware match more strictly.
2. Never interrupt a firmware update: AC power connected, no sleep, no shutdown until it completes.
3. If optional updates generally misbehave, [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the official guidance, and our [manual install guide](/articles/how-to-install-kb-update-manually-from-catalog-on-laptop/) covers the Catalog route for updates Windows Update will not handle.

## Closing

Optional updates failing on Windows 10 while everything else works is a driver-pipeline issue with a practical answer: install them singly, restart first, and default to the manufacturer's driver when Windows Update fumbles. The optional list is a convenience feed, not the only source — the hardware maker's driver page is usually newer and more reliable anyway. Reset the components to fix the pipeline, but do not let one stubborn optional driver consume your afternoon when the manufacturer hands you a better one directly. Check back on skipped optional updates every few months; a driver that failed in January may install cleanly in June once its package or metadata has been refreshed. In practice, patience plus the manufacturer driver solves nearly every optional-update standoff you will encounter on Windows 10.
