---
title: "Microsoft Store Errors Causing Blue Screens: How to Fix It"
slug: microsoft-store-error-blue-screen-error-fix
date: 2026-09-07
categories: ["windows-errors"]
tags: ["microsoft store", "blue screen", "store error", "windows 11", "app crash"]
description: "Microsoft Store throwing errors and blue-screening your laptop? Fix the underlying driver and Store issues causing the crashes in 7 steps."
thumbnail: "/images/thumbs/microsoft-store-error-blue-screen-error-fix.webp"
faqs:
  - q: "Can the Microsoft Store itself cause a blue screen?"
    a: "The Store app itself almost never causes a blue screen directly. What usually happens is that a Store update installs a new driver or app update that triggers the crash, or the Store's background services collide with a buggy storage or network driver. The fix targets the driver layer, not just the Store."
  - q: "What is error 0x80070002 in the Microsoft Store?"
    a: "Error 0x80070002 means 'file not found' — usually a corrupted Store cache or a failed download. Clear the cache with wsreset.exe, then check for Windows updates. Our [fix for install error 0x80070002 on Windows 11](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/) walks through the deeper repair steps."
  - q: "Why does my laptop crash when the Store updates apps?"
    a: "Automatic Store updates can push new drivers (especially for peripherals and GPUs) without warning. If a freshly updated driver is buggy, the first crash often happens right when the Store installs it. Check update history and roll back recently installed drivers."
  - q: "Should I reinstall the Microsoft Store?"
    a: "Re-registering the Store with PowerShell fixes most Store-only problems and is safe. A full reinstall is rarely needed. If you're also getting blue screens, though, the Store is a symptom — prioritize driver and storage diagnostics first."
---

When the Microsoft Store throws errors *and* your laptop is blue-screening, it's natural to blame the Store. In practice, the Store is usually the messenger, not the murderer: Store updates deliver new drivers and app updates in the background, and if one of those updates is bad, the crash lands right around the time you notice Store errors. Fix the underlying cause and both problems disappear together.

This guide tackles the pair of problems in the right order — stabilize the system first, then repair the Store itself.

## Why this happens

- **A Store-delivered driver update is buggy.** The Store's automatic updates can install new peripheral or GPU drivers that immediately crash the system.
- **Corrupted Store cache collides with failing storage.** If your SSD is developing bad blocks, the Store's cache files corrupt first because they're written constantly.
- **Network filter drivers break Store downloads.** VPN and security drivers that mangle Store traffic can also destabilize the network stack enough to blue-screen.
- **Corrupted system components shared by the Store.** The Store depends on AppX deployment services and system files; damage there causes both Store errors and instability.
- **Pending Windows updates leave the system half-patched.** A stuck update leaves driver and system files in mismatched versions, a classic recipe for crashes.
- **Third-party "Store fixer" or debloat scripts.** Aggressive scripts that rip out Store components often break dependencies other parts of Windows need.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Check what changed and pause Store updates

Stop the bleeding before diagnosing.

1. Open the **Microsoft Store**, click your profile icon, and open **Settings**.
2. Turn off **App updates** temporarily so nothing new installs while you troubleshoot.
3. Open **Settings > Windows Update > Update history** and note any driver updates installed just before the problems started.
4. If a driver update lines up with the crashes, roll it back in **Device Manager > Properties > Driver > Roll Back Driver**.
5. Also check **Settings > Windows Update** for failed or pending updates and let them finish or retry them.

### Fix 2: Update or clean-reinstall your GPU and chipset drivers

Display and chipset drivers are the most common blue-screen sources tied to Store update cycles.

1. Open **Device Manager** and check **Display adapters** and **System devices** for warning icons.
2. For the GPU, do a clean install from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) — choose the clean-install option to wipe old remnants.
3. Get chipset and storage drivers from your laptop manufacturer's support page (Dell, HP, and Lenovo all ship these as one package).
4. Restart and confirm a full day of stability before re-enabling Store app updates.
5. If crashes name a specific `.sys` file, search our site for that stop code — for example, storage-related crashes often turn out to be [UNEXPECTED_STORE_EXCEPTION](/articles/unexpected-store-exception-windows-11-fix/).

### Fix 3: Reset the Microsoft Store cache

This fixes the Store-side errors without touching your installed apps.

1. Press **Windows + R**, type `wsreset.exe`, and press Enter.
2. A blank command window opens for 10–30 seconds, then the Store launches fresh — don't close the window yourself.
3. Try downloading or updating an app to confirm the Store works again.
4. If `wsreset.exe` fails or the Store still errors, move to the next fix for a deeper repair.
5. This step is safe: it clears temporary cache only, never your apps or purchases.

### Fix 4: Re-register the Store and repair AppX components

When the cache reset isn't enough, re-register the Store package.

1. Open **Terminal (Admin)** (right-click **Start** and select it).
2. Run this command to re-register the Store for your account:
   `Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to finish — errors in red about packages "in use" are usually harmless.
4. Restart the laptop and test the Store again.
5. If Store errors persist alongside crashes, the problem is deeper than the Store; continue with system repairs below.

### Fix 5: Run SFC, DISM, and check the disk

Corrupted system files and a failing drive cause both symptoms at once.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for 100%.
2. Then run `sfc /scannow` and restart when it completes.
3. After rebooting, run `chkdsk C: /f /r` in **Terminal (Admin)** — type **Y** when asked and let it scan on the next restart (this can take an hour on large drives).
4. If `chkdsk` finds many bad sectors, back up immediately — the drive is failing and needs replacement.
5. Once the disk and system files are clean, test the Store and watch for further blue screens.

### Fix 6: Remove interfering network filter drivers

VPNs and "internet security" suites install drivers that break Store downloads and can crash the network stack.

1. Open **Settings > Apps > Installed apps** and uninstall any VPN client or third-party firewall you added recently.
2. In **Device Manager**, expand **Network adapters**, right-click your Wi-Fi adapter, and choose **Uninstall device** (don't tick "delete driver" unless you have the driver file ready), then restart — Windows reinstalls it cleanly.
3. Test Store downloads over a plain connection with no VPN active.
4. Reinstall the VPN only after confirming stability, and keep it updated.
5. For step-by-step Store-specific repair beyond this, see [Windows Store not opening after a Windows 11 update](/articles/how-to-fix-windows-store-not-opening-after-windows-11-update/).

### Fix 7: Reset Windows while keeping your files

If Store errors and blue screens both survive everything above, the OS installation is damaged.

1. Open **Settings > System > Recovery**.
2. Click **Reset PC** and choose **Keep my files**.
3. Choose **Cloud download** for the freshest system files (needs a stable connection).
4. After the reset, install drivers from your manufacturer's support page before letting the Store auto-update everything.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has guided troubleshooters if the reset itself fails.

## Closing

Treat Store errors plus blue screens as one problem with two symptoms, and attack the driver and storage layers first. In most cases the Store was never really broken — it was just the first thing to visibly fail when a bad driver or a dying SSD started corrupting things. Once the system is stable, a quick `wsreset.exe` usually brings the Store back to life on its own.
