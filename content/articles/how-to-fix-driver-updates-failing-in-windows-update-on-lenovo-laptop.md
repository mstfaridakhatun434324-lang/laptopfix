---
title: "How to Fix Driver Updates Failing in Windows Update on a Lenovo Laptop"
slug: how-to-fix-driver-updates-failing-in-windows-update-on-lenovo-laptop
date: 2026-09-12
categories: ["windows-update"]
tags: ["driver updates", "windows update", "lenovo", "update failing", "windows 11"]
description: "Driver updates keep failing in Windows Update on your Lenovo laptop? Here's why Lenovo drivers clash with Windows Update and how to fix it."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update-on-lenovo-laptop.webp"
faqs:
  - q: "Why do driver updates fail in Windows Update on Lenovo laptops?"
    a: "The most common reason is a version conflict: Lenovo's own Vantage software or System Update may have already installed a newer or customized driver, so the generic one Windows Update offers fails to apply. Corrupted update cache files, a stalled update service, or a driver package that does not match your exact ThinkPad, IdeaPad, or Legion model can cause the same failure."
  - q: "Should I let Windows Update or Lenovo Vantage handle drivers?"
    a: "For Lenovo laptops, Lenovo's own tools should win. Lenovo Vantage and Lenovo System Update deliver drivers tested for your exact model, including BIOS updates Windows Update never provides. Let Vantage handle drivers and use Windows Update for system patches. When both try to manage the same driver, conflicts and repeated failures are the usual result."
  - q: "Can a failed driver update damage my Lenovo laptop?"
    a: "A failed update itself is harmless — Windows rolls back to the previous driver when the install fails. The real risk is ignoring it: repeatedly failed updates can leave a device running an outdated driver with known bugs. The fixes below get the update to install cleanly or route you to the correct Lenovo-provided driver instead."
  - q: "How do I know which driver is actually failing?"
    a: "Open Settings, go to Windows Update, then View update history. Failed driver updates are listed with their error codes. Matching the error code to the device name tells you exactly which component — graphics, Wi-Fi, audio, chipset — needs attention, so you can fetch the right package from Lenovo support."
---

On Lenovo laptops, Windows Update and Lenovo's own driver tools sometimes fight over the same hardware, and the casualty is a driver update that downloads, attempts to install, and fails — sometimes with an error code, sometimes silently. You might see it in update history as a failed optional or automatic driver update for the graphics chip, Wi-Fi adapter, or chipset. The rest of Windows updates fine; only the drivers refuse to cooperate.

The root of most of these failures is duplication of effort. Lenovo Vantage (or Lenovo System Update on ThinkPads) delivers model-specific drivers that are often newer or customized compared to what Windows Update offers. When Windows Update tries to install its generic version over Lenovo's customized one — or vice versa — the installer balks. Add in the usual Windows Update failure modes like a corrupted cache, and driver updates fail repeatedly.

This guide shows you how to identify the failing driver, stop the conflict between the two update systems, and get the right driver installed from the right source. Work through the fixes in order.

## Why this happens

- **Lenovo Vantage already installed a newer driver.** Windows Update offers a generic or older version, and the installer refuses to downgrade or overwrite the customized Lenovo driver.
- **The driver package does not match your exact model.** Lenovo sells many variants (ThinkPad, IdeaPad, Legion, Yoga); a mismatched package fails its hardware check during installation.
- **The Windows Update cache is corrupted.** Damaged download files cause the driver installer to fail verification every time it runs.
- **A stalled update service breaks the install.** If wuauserv or cryptSvc is stuck, driver packages cannot complete their installation steps.
- **Pending restarts block new driver installs.** Some drivers cannot install until an earlier update's pending restart completes.
- **Third-party driver updaters created conflicts.** External "driver booster" tools install unofficial packages that Windows Update then cannot cleanly replace.
- **Insufficient disk space interrupts extraction.** Driver packages extract to a temp folder first; a nearly full C: drive causes the extraction and install to fail.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact failing driver and its error code

You cannot fix what you have not identified. Start with the specifics.

1. Open **Settings > Windows Update > Update history** and expand the failed entries. Note the device name (for example, "Intel Display driver") and any error code such as 0x80070103.
2. Error 0x80070103 specifically means Windows Update is trying to install a driver that is already installed or older than the current one — the classic Lenovo conflict signature.
3. Check **Device Manager** for the same device. If it shows a warning icon, note the device status message.
4. With the device name and error code in hand, you now know whether to pursue the Windows Update route or go straight to Lenovo's own driver.

### Fix 2: Let Lenovo Vantage take over driver duty

For Lenovo hardware, Lenovo's own tooling delivers the correct, tested drivers — including BIOS updates Windows Update never touches.

1. Open **Lenovo Vantage** (preinstalled on most Lenovo laptops) or install **Lenovo System Update** for ThinkPad models from [Lenovo support](https://support.lenovo.com/us/en/).
2. Run a system scan for driver and firmware updates, and install everything it offers. Vantage knows your exact model and variant.
3. Restart when prompted, then return to **Settings > Windows Update** and check for updates. The failing driver update often disappears or now installs cleanly because Vantage resolved the version conflict.
4. Going forward, treat Vantage as your driver source and Windows Update as your system-patch source. This division of labor prevents most repeat failures.

### Fix 3: Clear the corrupted update cache

If the same driver fails with the same error after Vantage has done its job, the cached download is likely damaged.

1. Open an elevated Command Prompt and stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Check for updates again. Windows re-downloads the driver package fresh, and a clean copy often installs without complaint.

### Fix 4: Hide the problem update if it keeps failing

Some driver updates are simply wrong for your hardware, and Windows will keep offering them. Hiding the update stops the loop.

1. Download Microsoft's **Show or hide updates** troubleshooter package (wushowhide.diagcab) — search for it on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) if you do not have it saved.
2. Run it, choose **Hide updates**, and select the failing driver update from the list.
3. Confirm the update no longer appears in Windows Update. The failure stops because Windows stops attempting it.
4. Install the correct driver manually from Lenovo support by entering your serial number or model — this guarantees a package built for your exact machine.

### Fix 5: Install the driver manually from Lenovo or Intel

When automatic channels fail, a manual install from the authoritative source cuts through the noise.

1. Find your exact model number on the bottom sticker or in Vantage, then go to Lenovo support and download the driver for the failing device.
2. For Intel graphics, Wi-Fi, or Bluetooth, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also detect and install the correct package directly.
3. In **Device Manager**, right-click the device, choose **Update driver > Browse my computer for drivers**, and point it at the downloaded files — or run the manufacturer's installer.
4. Restart and verify in Device Manager that the new driver version is active and the device shows no warnings.

### Fix 6: Uninstall conflicting third-party driver tools

External driver updater utilities are a frequent source of the conflicts that make Windows Update driver installs fail.

1. Open **Settings > Apps > Installed apps** and look for any third-party driver updater or "booster" software.
2. Uninstall it completely, then restart the laptop.
3. In Device Manager, check whether the previously affected device now has a clean driver state.
4. Retry Windows Update. With the unofficial packages gone, the official update path usually works.

### Fix 7: Run the Windows Update troubleshooter and repair system files

If driver updates still fail after the targeted fixes, repair the update pipeline itself.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter.
2. In an elevated Command Prompt, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
3. Restart, then check for updates one final time.
4. If a specific driver still will not install via Windows Update but works when installed from Lenovo, leave it hidden in Windows Update and manage it through Vantage permanently — that is a supported and stable arrangement.

## Closing

Driver update failures on Lenovo laptops are almost always a conflict story: two update systems, one piece of hardware, and a version mismatch in between. The reliable fix is to pick a lane — let Lenovo Vantage own your drivers and let Windows Update own your system patches — and to clear out corrupted caches and unofficial driver tools that muddy the waters. If you are fighting the broader pattern of [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) rather than a Lenovo-specific conflict, that guide covers the Windows-side causes in depth, and the [keep-failing walkthrough](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-lenovo-laptop/) handles the case where the same driver fails again and again on Lenovo hardware.
