---
title: "How to Fix Windows Update Error 0xC1900101 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0xc1900101-in-windows-11-24h2
date: 2026-09-05
categories: ["windows-update"]
tags: ["windows update", "0xc1900101", "error code", "windows 11", "driver"]
description: "Error 0xC1900101 means a driver crashed the Windows 11 24H2 upgrade. Update drivers, remove peripherals, and retry with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0xc1900101-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0xC1900101 mean?"
    a: "It means a driver crashed Windows Setup during the feature update, forcing a rollback. Display, storage controller, and antivirus filter drivers are the usual suspects. The extension after the code (like 0x30018) identifies the failing phase. Updating drivers, removing peripherals and third-party antivirus, and retrying resolves the large majority of cases."
  - q: "Will the rollback damage my current Windows?"
    a: "No. When setup hits 0xC1900101 it rolls back to your previous Windows installation automatically, and your files, apps, and settings come back intact. The rollback itself is the safety mechanism working as designed — treat the error as a diagnostic pointing at drivers, not as damage."
  - q: "Should I update the BIOS to fix this?"
    a: "Often yes, if a newer BIOS exists for your model. Outdated firmware mishandles handoffs that 24H2 setup expects, particularly around storage and power. Install BIOS updates only from your laptop maker's official support site, keep AC power connected, and never interrupt a BIOS flash."
  - q: "Can I just stay on my current Windows version instead?"
    a: "Temporarily, but not forever — older builds eventually lose security updates. A better path is fixing the driver issue once: update the big drivers, strip peripherals, and retry. If the upgrade keeps failing after genuine effort, the in-place upgrade with fresh installation media is the next escalation."
---

Error 0xC1900101 is the classic feature-update killer: the 24H2 upgrade runs for a while, then rolls back with this code. It almost always means a driver misbehaved during setup — display drivers, storage controller drivers, and antivirus filter drivers are the repeat offenders on laptops. The good news is that the rollback leaves your current Windows intact, so you can fix the driver situation and try again.

Under the hood, 0xC1900101 means a driver crashed the setup process during the feature update. Technically it is a setup failure with a driver exception: during the 24H2 upgrade, a driver — most often storage, display, or an antivirus filter driver — caused a rollback. The last four hex digits after 0xC1900101 identify the exact phase, which is why reading the full code matters.

The encouraging part: 0xC1900101 is one of the better-understood update errors, and the fixes below are ordered from quickest to most thorough. Work through them in sequence — most readers never need the last two.

## Why this happens

- **Outdated display drivers.** GPU drivers are the single most common 0xC1900101 trigger during the specialize phase.
- **Storage controller driver conflicts.** Old AHCI/RAID or Intel RST drivers crash setup during disk operations.
- **Antivirus filter drivers.** Third-party AV installs kernel drivers that setup cannot work around.
- **Peripheral drivers.** Docks, USB devices, and their drivers inject failures into the upgrade.
- **Insufficient disk space.** Setup needs staging room; running out mid-upgrade produces rollbacks with driver-like codes.
- **Outdated BIOS/UEFI firmware.** Old firmware mishandles the handoff setup expects.
- **Overclocking or driver verifier leftovers.** Aggressive tuning and debugging tools destabilize the setup environment.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the extended error code

0xC1900101 always carries an extension (like 0x30018 or 0x40017) that names the failing phase. That extension focuses the whole repair — do not skip this step.

1. Open **Settings > Windows Update > Update history** and click the failed feature update for details.
2. Note the full code including the extension, e.g. 0xC1900101 - 0x30018 (first boot phase) or 0x40017 (second boot phase).
3. Also check `C:\$Windows.~BT\Sources\Panther\setuperr.log` for the named driver or component.
4. Use the phase to prioritize: boot-phase failures point at storage/display drivers; specialize-phase at drivers generally.

### Fix 2: Update display and storage drivers

Since drivers cause the overwhelming majority of 0xC1900101 rollbacks, bringing the big three — display, storage, chipset — current before retrying resolves most cases.

1. Download the latest display driver for your GPU from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) — use the vendor tool to detect your hardware.
2. Get the latest chipset and storage drivers from your laptop maker's support site (Dell, HP, or Lenovo) for your exact model.
3. Install the drivers, restarting as prompted between them.
4. Retry the 24H2 feature update.

### Fix 3: Disconnect peripherals and remove third-party antivirus

External devices and AV filter drivers are the next most common culprits. Stripping the setup environment to essentials removes whole categories of failure at once.

1. Unplug every non-essential peripheral: docks, USB drives, printers, external GPUs — leave only power, and keyboard/mouse if needed.
2. Uninstall third-party antivirus completely (not just disable — its filter driver must go), relying on Microsoft Defender during the upgrade.
3. Disable any overclocking or undervolting utilities and restore BIOS defaults if you changed them.
4. Run the feature update again in this minimal configuration.

### Fix 4: Free disk space and update the BIOS

Setup needs roughly 20 GB of free space plus firmware that handles modern handoffs. Both are quick to verify and fix common secondary causes.

1. Ensure at least 20 GB free on C: using Disk Cleanup with system files (see our disk-space guidance).
2. Check your laptop maker's support site for a BIOS/UEFI update newer than your current version and install it following their instructions exactly.
3. Keep the laptop plugged into AC power throughout — a battery dip mid-upgrade can corrupt the attempt.
4. Retry the feature update after both are done.

### Fix 5: Run the Windows Update troubleshooter

The built-in troubleshooter knows the usual suspects behind 0xC1900101: it checks the service state, the update cache, and the network path to Microsoft's servers, then applies safe automatic repairs. It will not fix deep corruption, but it clears the simple causes in a few minutes and is worth trying before anything manual.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow the on-screen prompts.
3. Restart the PC when it finishes, then check for updates again at **Settings > Windows Update**. If 0xC1900101 is still there, move on to the next fix.

### Fix 6: Do an in-place upgrade as a last resort

When nothing else clears 0xC1900101, the servicing stack itself is too damaged for targeted repair. An in-place upgrade reinstalls Windows 11 24H2 over your existing install while keeping files and apps. Grab the ISO from Microsoft's official Windows 11 download page — never from a third-party mirror.

1. Download the Windows 11 ISO from Microsoft, double-click it to mount it, and run `setup.exe`.
2. Accept the license terms and choose **Keep personal files and apps** when asked what to keep.
3. Let setup run to completion — 30 to 90 minutes with several restarts. Do not force a shutdown mid-way.
4. After signing in, run **Settings > Windows Update** once more to confirm 0xC1900101 no longer appears.

## Closing

0xC1900101 looks scary but is usually just one bad driver standing between you and 24H2. Update the display and storage drivers, unplug the extras, and try again — most upgrades sail through on the second attempt. For driver-specific help, see our [driver update failure guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/), and our [24H2 update error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) covers the other upgrade codes. Get drivers from Intel, NVIDIA, or AMD support pages.
