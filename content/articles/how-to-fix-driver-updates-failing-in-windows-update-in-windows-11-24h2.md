---
title: "Driver Updates Keep Failing in Windows Update on Windows 11 24H2? Fixed"
slug: how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2
date: 2026-10-03
categories: ["windows-update"]
tags: ["driver updates", "windows update", "windows 11 24h2", "driver install failed", "device manager"]
description: "Windows 11 24H2 keeps failing to install driver updates? Learn why driver packages fail, how to install them manually, and when to block a bad one."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2.webp"
faqs:
  - q: "Why do driver updates fail while other updates install fine?"
    a: "Driver packages go through a stricter installation path than regular updates — Windows verifies the driver's signature, checks hardware ID matches, and runs the vendor's installer. Any mismatch, from a wrong hardware revision to a signature problem, fails the whole package while cumulative updates sail through unaffected."
  - q: "Should I even install driver updates from Windows Update?"
    a: "For most users, yes — they're tested and convenient. But if a specific driver update keeps failing, it's fine to skip it and install the driver directly from the manufacturer instead. Graphics and chipset drivers especially are often better sourced from NVIDIA, AMD, Intel, or your laptop maker."
  - q: "Will a failed driver update harm my laptop?"
    a: "No. Failed driver installs roll back automatically — Windows keeps the previous working driver safely in place. The annoyance is the repeated failure notifications and wasted download bandwidth, not system damage. Your current driver keeps working exactly as before, so there's no urgency beyond stopping the retry loop."
  - q: "How do I stop Windows Update from retrying a bad driver?"
    a: "Use Microsoft's 'Show or hide updates' troubleshooter to hide the specific driver update, or set the device's hardware ID to be ignored via Group Policy. Hiding is reversible and is the right call when a driver update fails repeatedly or installs a version that breaks something."
---

Windows Update handles most drivers quietly in the background — you never notice, which is the point. So when a driver update starts failing, it announces itself loudly: the same update appears in your history again and again, each attempt ending in "Failed to install," sometimes with an error code like 0x80070103 (already have a better driver) or 0x800F020B. The rest of your updates install fine. It's just this one driver, failing on a loop, and retrying it changes nothing.

Driver updates fail for different reasons than regular updates — they involve hardware matching, digital signatures, and vendor installer packages, any of which can reject the install. On Windows 11 24H2, Microsoft expanded the range of drivers offered through Windows Update, which means more opportunities for these mismatches. The fixes below sort the failures into their real categories: already-installed, wrong-driver, corrupt-download, and blocked-install — each with its own solution.

## Why this happens

- **You already have a newer driver (0x80070103)**: Windows Update offers an older driver version than what's installed; the installer correctly refuses the downgrade.
- **Hardware ID mismatch**: The offered driver targets a slightly different hardware revision than your laptop actually has.
- **Signature verification failure**: The driver package's digital signature doesn't validate, often due to a corrupt download.
- **Vendor installer conflicts**: The driver's own setup program clashes with software already on the system (common with audio and printer drivers).
- **Corrupt driver store**: Damage to the DriverStore means new drivers can't stage properly.
- **Pending restart blocks installation**: A previous update left the system in a "restart required" state that blocks driver installs.
- **Third-party driver utilities interfere**: Tools that "manage" your drivers can lock files the update needs to replace.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the failure even matters

Error 0x80070103 — "a newer version is already installed" — is Windows Update being overeager, not a real problem. Don't fix what isn't broken.

1. Go to **Settings > Windows Update > Update history** and find the failed driver.
2. Note the error code. **0x80070103** means your installed driver is newer — this is harmless.
3. Open **Device Manager**, find the device, right-click > **Properties > Driver tab**, and check the driver date and version.
4. If your driver is newer than what Windows Update offered, hide the update (Fix 7) and move on.
5. Only continue below if the error is something else, or the driver is genuinely outdated.

### Fix 2: Install the driver manually from the manufacturer

Manufacturer drivers are newer, better matched to your hardware, and bypass Windows Update's packaging entirely. This resolves most genuine failures.

1. Identify the exact device in **Device Manager** (e.g., "Intel Wi-Fi 6E AX211").
2. Go to your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and enter your model or service tag.
3. Download the driver for the failing device (chipset, Wi-Fi, Bluetooth, and audio are the usual suspects).
4. For graphics: use Intel's driver assistant, NVIDIA, or AMD's official driver pages rather than Windows Update's versions.
5. Install the downloaded driver, restart, then check Windows Update — it should now show the driver as current and stop offering the failing package.

### Fix 3: Clear the driver download cache

A corrupt download fails signature verification on every retry. Clearing the cache forces a fresh download.

1. Open **Command Prompt as administrator**.
2. Run `net stop wuauserv` and `net stop bits`.
3. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
4. Run `net start wuauserv` and `net start bits`.
5. In **Settings > Windows Update > Advanced options > Optional updates**, check **Driver updates** and retry the specific driver.
6. If it fails identically, the package itself is bad — skip to Fix 7 and hide it.

### Fix 4: Remove the old driver completely, then reinstall

A half-installed or conflicting old driver blocks the new one. A clean removal breaks the deadlock.

1. Open **Device Manager** and find the failing device.
2. Right-click it and choose **Uninstall device**.
3. If offered, check **"Attempt to remove the driver for this device"** — this clears the old package from the DriverStore.
4. Restart the laptop. Windows will install a basic driver automatically.
5. Now install the manufacturer's driver from Fix 2 on the clean slate.
6. This is especially effective for audio, printer, and network drivers that leave behind conflicting components.

### Fix 5: Resolve the pending-restart block

Driver updates won't install while Windows is waiting on a restart from a previous update. The failure message rarely says this clearly.

1. Go to **Settings > Windows Update** and look for "Restart required" messaging.
2. Restart the laptop fully — not shut down (Fast Startup can preserve the pending state), but **Restart**.
3. After reboot, check Windows Update again before doing anything else.
4. Retry the driver update immediately — install it before other pending updates queue up.
5. If restarts themselves hang, see our guide to [updates stuck on the Restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).

### Fix 6: Repair the driver store and system files

When multiple different drivers fail, the problem is systemic — the DriverStore or servicing stack is damaged.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Follow with `sfc /scannow`.
4. Restart and retry the driver updates.
5. For a deeper driver-store cleanup, run `pnputil /enum-drivers` to list third-party drivers and `pnputil /delete-driver oemXX.inf /uninstall` to remove stale ones (replace oemXX.inf carefully — only remove drivers you recognize as obsolete).
6. Back up your working drivers first with our [driver backup walkthrough](/articles/how-to-backup-drivers-before-update-in-windows-11-24h2/) before pruning anything.

### Fix 7: Hide the bad update so it stops retrying

Some driver packages are just broken for your hardware configuration, and no amount of retrying will fix Microsoft's packaging. Hiding the update is the correct, supported response.

1. Download Microsoft's **"Show or hide updates"** troubleshooter (search Microsoft's site for "wushowhide").
2. Run it, choose **Hide updates**, and select the failing driver package.
3. Windows Update will stop offering it.
4. Install the manufacturer's driver manually (Fix 2) so the device still gets updates — just not through Windows Update.
5. If a future driver version fixes the packaging, unhide it with the same tool.
6. For Lenovo-specific driver update failures, our [Lenovo driver update guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-lenovo-laptop/) covers Vantage-based alternatives.

## Closing

Failed driver updates look alarming but are usually benign — the old driver keeps working, and the failure is Windows refusing a bad package rather than breaking something. The winning pattern: check if the failure matters (0x80070103 means ignore it), install the manufacturer's driver directly for real gaps, and hide packages that are broken on Microsoft's side. Your devices stay current, and Windows Update stops crying wolf.
