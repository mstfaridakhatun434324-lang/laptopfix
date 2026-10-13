---
title: "How to Fix Optional Updates Not Installing on Windows 11"
slug: how-to-fix-optional-updates-not-installing-on-windows-11
date: 2026-09-14
categories: ["windows-update"]
tags: ["optional updates", "driver updates", "windows 11", "not installing"]
description: "Optional updates show up but won't install on Windows 11? Here's how to fix the optional update pipeline and get drivers installed."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-on-windows-11.webp"
faqs:
  - q: "What are optional updates in Windows 11?"
    a: "Optional updates are driver updates, firmware updates, and non-security quality updates that Microsoft does not install automatically. They appear under Settings > Windows Update > Advanced options > Optional updates. They are safe to install selectively, especially driver updates for hardware that is misbehaving."
  - q: "Do I actually need to install optional updates?"
    a: "Not always. If your hardware works fine, you can skip them. But if a device is malfunctioning — Wi-Fi dropping, audio crackling, the touchpad acting up — the optional driver update listed for it is often the exact fix. Install optional updates selectively for hardware you are having trouble with."
  - q: "Why do optional updates fail while regular updates succeed?"
    a: "They use a slightly different installation path focused on drivers and firmware, so they can fail for driver-specific reasons — a locked device, a conflicting existing driver, or a firmware update that needs a restart — even when the main cumulative update pipeline is perfectly healthy."
  - q: "Is it safe to install all optional updates at once?"
    a: "Usually yes, but selectively is smarter. Install the ones matching hardware you use or have problems with, and skip obscure ones for devices you do not have. If an optional driver update causes trouble, you can roll it back in Device Manager."
---

Optional updates are Windows 11's quiet corner: driver updates, firmware packages, and preview quality updates that sit under **Advanced options** waiting for you to choose them. They are genuinely useful — that optional driver update is often the fix for misbehaving Wi-Fi or audio. But on some systems they refuse to install: you check the box, click download, and they fail, hang, or vanish. Regular cumulative updates work fine, which makes the whole thing more confusing.

The reason the two pipelines fail independently comes down to how drivers are handled. Cumulative updates mostly touch Windows system files, which the servicing stack manages with full transactional protection. Optional driver updates, by contrast, have to replace files owned by running hardware, negotiate with the driver store, and satisfy driver ranking rules that decide which driver version "wins" for a device. A manufacturer-customized driver already on the system can outrank the offered one and block it; a device that never fully releases its driver files defeats the installer. The servicing stack can be perfectly healthy while the driver path is jammed.

The optional update pipeline is separate enough from the main one to break independently. This guide covers why optional updates fail and how to get them installing again, plus what to do when the right move is skipping Windows Update and going straight to the manufacturer.

## Why this happens

- **The driver is locked by a running device.** The installer cannot replace a driver file that is in active use, so the update fails.
- **A conflicting driver version is already installed.** A newer or manufacturer-customized driver blocks the older generic one Windows offers.
- **Corrupted optional update metadata.** The catalog data describing available optional updates gets out of sync, causing download or install failures.
- **Insufficient permissions or a standard user account.** Driver installation requires elevation; limited accounts fail silently or with access errors.
- **Firmware updates need a restart that never happens.** Some optional firmware packages stage correctly but fail because the required reboot is deferred indefinitely.
- **The update components are damaged.** The same cache corruption that breaks regular updates can break the optional pipeline independently.
- **Group Policy hides or blocks optional updates.** Enterprise or debloat policies can disable the optional updates UI or block driver installation.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install optional updates one at a time

Batch installs fail opaquely; single installs fail informatively.

1. Go to **Settings** > **Windows Update** > **Advanced options** > **Optional updates**.
2. Select just one update — start with the driver for hardware you actually use — and install it alone.
3. Note the exact error if it fails. One-at-a-time installation turns a mysterious batch failure into a diagnosable single failure.

### Fix 2: Restart before installing driver updates

Clear the locks that block driver replacement.

1. Close all applications and restart the laptop cleanly.
2. Immediately after booting, before opening anything heavy, install the optional update.
3. Fresh-boot installation avoids the "file in use" failures that plague driver updates on long-running sessions.

### Fix 3: Install the driver from the manufacturer instead

Skip the middleman when Windows Update fumbles the driver.

1. Identify the device in **Device Manager** and note its exact model.
2. Download the driver from the manufacturer: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA, AMD, or your laptop maker's support site.
3. Install it manually. A manufacturer driver is usually newer and better matched than the optional update version anyway.
4. After a manual install, the optional update entry typically disappears — the system recognizes the driver is current.

### Fix 4: Reset the update components

Repair the pipeline that delivers optional updates.

1. Open an elevated Command Prompt and run:
   ```
   net stop wuauserv
   net stop bits
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   net start wuauserv
   net start bits
   ```
2. Check for updates, then revisit **Optional updates**. The list rebuilds from clean metadata. See [how to reset stuck update components](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) for the full version of this repair.

### Fix 5: Check policies blocking optional updates

Make sure nothing is configured to suppress them.

1. Press **Windows key + R**, type `gpedit.msc`, and navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Update** > **Manage updates offered from Windows Update**.
2. Look for policies disabling optional updates or driver updates and set them to **Not configured**.
3. Check the Registry at `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for related values and remove them.

### Fix 6: Run the update troubleshooter and repair system files

Cover the general-health bases.

1. Run **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run**.
2. In an elevated Command Prompt, run `sfc /scannow` to repair any system file damage affecting the installer.
3. Restart and retry the optional update. If a specific driver update persistently fails, hide it and use the manufacturer driver from Fix 3 instead.

### Fix 7: Handle firmware updates with a full shutdown

Firmware-class optional updates are the fussiest of all.

1. For firmware or BIOS-class optional updates, do a full shutdown (hold **Shift** while clicking **Shut down** to bypass Fast Startup), then power on.
2. Install the firmware update immediately after boot.
3. If it still fails, get the firmware from the laptop manufacturer's support site instead — firmware is one category where the manufacturer's own updater is genuinely more reliable than Windows Update. Microsoft's [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the official guidance for failed optional updates.

## Closing

Optional updates failing while regular updates work is a driver-pipeline problem, not a system problem: install them one at a time, restart first, and do not hesitate to bypass Windows Update for the manufacturer driver. The optional update list is a convenience, not the only route — the manufacturer's driver page usually has a newer version anyway. Fix the pipeline with a component reset, but treat per-driver failures pragmatically: get the driver from the source and move on. If optional updates are not appearing at all rather than failing, the cause may be a policy suppressing them — see [how to fix Windows Update greyed out in Windows 11](/articles/how-to-fix-windows-update-greyed-out-in-windows-11-24h2/) for the policy side of the problem.
