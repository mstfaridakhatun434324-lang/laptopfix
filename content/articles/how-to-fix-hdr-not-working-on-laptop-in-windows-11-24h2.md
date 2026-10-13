---
title: "HDR Not Working on Your Laptop in Windows 11 24H2? Fix It Now"
slug: how-to-fix-hdr-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-16
categories: ["drivers"]
tags: ["hdr not working", "windows 11 24h2", "display driver", "hdr calibration"]
description: "The HDR toggle is greyed out or does nothing after Windows 11 24H2? Restore HDR on your laptop display with these driver and settings fixes."
thumbnail: "/images/thumbs/how-to-fix-hdr-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why is the HDR toggle greyed out after 24H2?"
    a: "Windows greys out the HDR toggle when it believes the display does not support HDR. After 24H2, that belief is often wrong — the update replaced the display driver with a version that does not report the panel's HDR capability, or it corrupted the monitor driver binding. Reinstalling the proper display and monitor drivers restores the capability report and the toggle."
  - q: "Does my laptop display actually support HDR?"
    a: "Check your laptop's specifications for HDR support — look for DisplayHDR certification or HDR10 mentions. Many laptop panels accept an HDR signal but have limited brightness and contrast, so the effect is subtle. If the spec sheet never mentions HDR, the toggle was never supposed to appear and no driver fix will create it."
  - q: "Why does HDR look washed out when I enable it?"
    a: "Washed-out HDR usually means the SDR content brightness slider is set wrong, or the display's HDR calibration is off. Open Settings, then System, then Display, then HDR, and adjust the SDR content brightness balance. Running the Windows HDR Calibration app from the Microsoft Store fine-tunes the tone mapping for your specific panel."
  - q: "Can the graphics driver break HDR while everything else works?"
    a: "Yes, and it does regularly. HDR metadata handling is a specific driver capability independent of normal rendering — a driver can drive the desktop perfectly while failing to pass HDR metadata to the panel. That is why a clean graphics driver reinstall is the central fix even when the display otherwise looks fine."
---

You open **Settings > System > Display**, and the **Use HDR** toggle is greyed out — or it toggles but the screen looks identical, or HDR worked last month and now Windows insists your display does not support it. The 24H2 update has a habit of breaking HDR on laptop panels that handled it perfectly before.

HDR on a laptop is a negotiation between Windows, the graphics driver, and the panel: the driver must report the panel's HDR capability, Windows must enable the HDR pipeline, and the content must carry HDR metadata. The 24H2 update most commonly breaks the first step — the driver stops reporting HDR support, Windows concludes the panel cannot do HDR, and the toggle dies. Rebuilding the driver side restores the negotiation. For general display weirdness on a second screen, our [second monitor flickering guide](/articles/how-to-fix-second-monitor-flickering-in-windows-11-24h2/) covers related driver issues.

## Why this happens

- **Display driver replaced by 24H2.** The new driver does not report the panel's HDR capability to Windows.
- **Monitor driver binding corrupted.** The EDID data carrying HDR metadata support is unreadable.
- **HDR certification data lost.** The driver's HDR capability flags got reset during the update.
- **Wrong color profile active.** A stale ICC profile overrides the HDR pipeline.
- **Auto HDR or HDR calibration app conflicting.** Leftover calibration data mismatches the new driver.
- **External display confusion.** Windows reads the external monitor's capabilities instead of the laptop panel's.
- **Power saving disabling HDR.** Battery-saver modes can silently disable the HDR pipeline.
- **BIOS display initialization changed.** Firmware updates alter how the panel reports its capabilities.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the panel actually supports HDR

Before troubleshooting, confirm HDR was ever possible. Check your laptop's spec sheet for DisplayHDR certification or HDR10 support. In Windows, go to **Settings > System > Display > Advanced display** and look at the reported capabilities — if it says the display does not support HDR here, note whether that changed after 24H2 (a change means driver trouble; never having it means the panel lacks HDR). Do this check with no external monitor connected, since Windows can report the wrong display's capabilities.

### Fix 2: Reinstall the monitor driver

Open **Device Manager**, expand **Monitors**, right-click your laptop display, choose **Uninstall device**, and restart. Windows redetects the panel and re-reads its EDID — the data block that declares HDR support. A corrupted EDID binding is a common reason Windows suddenly "forgets" a panel's HDR capability after an update. After the restart, recheck **Settings > System > Display** for the HDR toggle. If it is back, you are done; if it is still greyed out, the graphics driver is the broken layer.

### Fix 3: Clean-install the graphics driver

HDR metadata handling lives in the graphics driver. Download the latest driver for your GPU — Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), AMD from the [AMD driver support page](https://www.amd.com/en/support/download/drivers.html) — and choose a **clean install** if the installer offers it. Restart and recheck the HDR toggle. The clean install matters: HDR capability flags can survive a regular update install, and only a clean pass resets them.

### Fix 4: Reset the color profile

Search for **Color Management** in the taskbar, select your laptop display, and check the profiles list. Remove any custom ICC profile that predates the 24H2 update — stale profiles can override the HDR pipeline and wash out or block HDR. Check **Use my settings for this device** and ensure the default sRGB or the manufacturer's profile is active. Restart after changing profiles. A wrong color profile is the classic cause of HDR that "enables" but looks grey and lifeless.

### Fix 5: Run the Windows HDR Calibration app

Install **Windows HDR Calibration** from the Microsoft Store and run it on the laptop display (not an external monitor). The app walks through test patterns to set the panel's peak brightness, black level, and saturation for HDR. 24H2 can invalidate old calibration data, leaving HDR technically enabled but visually broken. Recalibrating after the driver fixes ensures the tone mapping matches your panel's actual capabilities — never skip calibration, since defaults are tuned for external desktop monitors rather than laptop panels. Then go to **Settings > System > Display > HDR** and adjust the **SDR content brightness** slider until desktop apps look natural alongside HDR video.

### Fix 6: Check power and battery-saver settings

Go to **Settings > System > Power & battery** and make sure **Battery saver** is off while testing — battery saver can disable the HDR pipeline silently. In the advanced power plan settings, check that the display is not being forced into a power-saving mode that strips HDR. Test HDR with the charger connected: some laptops disable HDR on battery by design, and 24H2 made that behavior more aggressive on certain models. If HDR works plugged in but never on battery, that is firmware policy, not a bug — check the manufacturer's power utility for an override.

### Fix 7: Update the BIOS and isolate external displays

Check the manufacturer's site for a **BIOS update** — panel capability reporting is firmware-mediated, and vendors fixed HDR regressions in firmware after 24H2. Flash with the charger connected. Then disconnect all external monitors and docks, restart, and test HDR on the laptop panel alone — external displays can confuse Windows' capability detection, especially mixed HDR/SDR setups. If HDR remains greyed out on the bare laptop panel with clean drivers and current BIOS, verify against the spec sheet once more; panels without true HDR hardware cannot be fixed in software.

## Closing

HDR failures after 24H2 are capability-reporting failures: the driver stopped telling Windows the panel can do HDR. Reinstall the monitor driver, clean-install the graphics driver, reset the color profile, and recalibrate. Brightness controls often break alongside HDR after the same update — our [Windows 11 brightness repair guide](/articles/how-to-fix-display-brightness-not-working-on-windows-11/) covers that companion problem.
