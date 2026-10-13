---
title: "How to Fix Windows Update Error 0x800F020B on Windows 11 24H2"
slug: "how-to-fix-windows-update-error-0x800f020b-in-windows-11-24h2"
date: 2026-09-15
categories: ["windows-update"]
tags: ["0x800f020b", "driver update failed", "windows update error", "windows 11 24h2", "windows update"]
description: "Error 0x800F020B on Windows 11 24H2 almost always means an optional driver update failed. Identify the offending driver, hide it, and install the right driver from your manufacturer instead."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f020b-in-windows-11-24h2.webp"
faqs:
  - q: "What does Windows Update error 0x800F020B mean?"
    a: "Error 0x800F020B occurs when Windows Update tries to install a driver package that does not apply to your hardware — typically an optional driver update for a device that is no longer present, already has a newer driver, or was misidentified. The driver installer fails, and Windows Update reports the failure with this code. It is a driver problem wearing an update error's clothes."
  - q: "Is error 0x800F020B serious?"
    a: "Usually not. It affects an optional driver update, not a security or cumulative update, so your system is not left vulnerable. The annoyance is that Windows keeps retrying the same failing driver, which clutters update history and can block the 'everything is up to date' state. Hiding the offending driver update resolves it permanently in most cases."
  - q: "Why does Windows keep offering a driver I don't need?"
    a: "Windows Update matches drivers to hardware IDs reported by your devices, and the matching is imperfect — especially for printers, docks, and devices connected only occasionally. A driver for a printer you returned, or a generic driver for a device your manufacturer handles differently, can get queued. Once it fails, Windows often retries it on every update cycle until you hide it."
  - q: "Should I let Windows Update install drivers at all?"
    a: "For core devices it is fine, but manufacturer drivers are usually better for laptops. Chipset, graphics, Wi-Fi, and power-management drivers from Dell, HP, Lenovo, or ASUS are tuned for your exact model, while Windows Update ships generic versions. Many technicians hide driver updates in Windows Update entirely and manage drivers through the manufacturer's tool, which sidesteps 0x800F020B-class failures altogether."
---
Error 0x800F020B has a distinctive signature: Windows Update reports everything else installed fine, but one item — almost always listed as a driver — failed. On Windows 11 24H2 this happens when the update service pushes a driver package that does not actually fit your hardware: a printer driver for a printer you no longer own, a graphics driver older than the one already installed, or a misidentified device. The driver installer chokes, and Windows blames the update.

The fix is refreshingly targeted. Unlike corruption errors where you rebuild caches and scan disks, here you identify the specific driver, stop Windows from offering it, and get the correct driver from the source that actually knows your laptop — the manufacturer. The whole job takes about twenty minutes once you know which driver is failing.

Start by opening **Settings > Windows Update > Update history** and expanding the failed entry — the driver name is your most important clue. If driver updates fail across the board rather than just one, our guide to [driver updates failing in Windows Update on 24H2](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) covers the systemic version of this problem.

## Why this happens

- **Driver for a device no longer present** — A driver queued for a printer, dock, or USB device you disconnected or returned. The installer cannot find the hardware and fails.

- **Driver older than the installed version** — Windows Update sometimes offers a driver that predates the one your manufacturer already installed, and the installer refuses to downgrade.

- **Misidentified hardware** — Generic hardware IDs can match the wrong driver package, especially for audio, card readers, and older peripherals.

- **Corrupted driver package in the cache** — A damaged download of the driver package fails integrity checks before installation even begins.

- **Third-party driver already managing the device** — Manufacturer utilities (like printer software suites) that manage their own drivers can conflict with Windows Update's attempt to install a parallel version.

- **Pending reboot blocking driver staging** — Driver installs often require a clean device state; a pending restart from an earlier update can cause the new driver install to abort.

- **Component store corruption** — Damage to the servicing stack breaks driver package staging even when the driver itself is perfectly good.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which driver failed

You cannot fix what you cannot name. The update history names the driver — write it down before doing anything else.

1. Open **Settings > Windows Update > Update history**.
2. Expand the failed update entry and note the full driver name and version.
3. Open **Device Manager** (Win + X), find the matching device, and check its current driver version under **Properties > Driver**.
4. If the installed driver is already newer, you have confirmed the mismatch — proceed to hide the update.

### Fix 2: Hide the failing driver update

Once identified, tell Windows Update to stop offering the bad driver. Microsoft's 'Show or hide updates' troubleshooter does exactly this.

1. Download the **Show or hide updates** troubleshooter (wushowhide.diagcab) — guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).
2. Run it, click **Hide updates**, and check the failing driver.
3. Confirm, then run **Check for updates** — the driver should no longer appear.
4. The 0x800F020B error stops recurring because the trigger is gone. If driver updates are failing across the board rather than just this one, our guide to [driver updates failing in Windows Update on 24H2](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) covers the systemic problem.

### Fix 3: Install the correct driver from your manufacturer

The right driver comes from the company that built the laptop, not the generic Windows Update catalog. This is the permanent fix.

1. Go to your manufacturer's support page (Dell, HP, or Lenovo's official support site).
2. Enter your exact model or serial number and open the **Drivers** section.
3. Download the driver matching the failed device (chipset, graphics, audio, network) and install it.
4. Restart and confirm the device works in Device Manager with no warning icons.

### Fix 4: Update Intel drivers with the Driver & Support Assistant

For Intel-based laptops, Intel's own detection tool finds the correct chipset, graphics, Wi-Fi, and Bluetooth drivers without guesswork — useful when the failing driver is Intel hardware.

1. Visit the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and install the tool.
2. Run a scan and review the drivers it flags as outdated.
3. Install the recommended packages one at a time, restarting between major ones.
4. Re-run Windows Update to confirm the 0x800F020B entry no longer returns.

### Fix 5: Remove ghost devices from Device Manager

Drivers for long-gone devices linger as 'ghost' entries and keep attracting Windows Update's attention. Clearing them stops the cycle.

1. Open Device Manager, click **View > Show hidden devices**.
2. Look for grayed-out entries matching the failed driver (old printers, docks, USB devices).
3. Right-click each ghost device and choose **Uninstall device**, checking **Delete the driver software** if offered.
4. Restart, then check for updates — with the ghost gone, the driver offer disappears.

### Fix 6: Repair the component store with DISM

If driver updates fail even for hardware you definitely own, the staging machinery may be damaged. DISM repairs it.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
3. Follow with `sfc /scannow`.
4. Restart and retry the driver update — or hide it and use the manufacturer driver per Fix 3.

### Fix 7: Block driver updates via Windows Update (optional, lasting)

If you prefer managing drivers yourself, stop Windows Update from offering them at all. This is a legitimate, supported configuration.

1. Press **Win + R**, type `gpedit.msc` (Pro editions) and go to **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
2. Enable **Do not include drivers with Windows Updates**.
3. On Home editions, set the same via Registry: create DWORD `ExcludeWUDriversInQualityUpdate` = 1 under `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`.
4. Manage drivers through your manufacturer's update tool from now on — no more surprise driver failures.

## Closing

Error 0x800F020B is Windows Update stubbornly offering the wrong driver. Name the driver, hide it, install the manufacturer's version, and the error — and the endless retry loop — is finished for good. On a laptop rather than a desktop 24H2 build, the same code benefits from the notebook angle — our [laptop-focused 0x800F020B walkthrough](/articles/how-to-fix-windows-update-error-0x800f020b-on-laptop/) adds how to spot a genuinely failing device by its hardware IDs.
