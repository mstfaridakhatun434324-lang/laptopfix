---
title: "HDR Not Working on a Windows 11 Laptop? 7 Fixes to Enable It"
slug: how-to-fix-hdr-not-working-on-laptop-on-windows-11
date: 2026-09-19
categories: ["drivers"]
tags: ["hdr", "windows 11", "display settings", "color calibration"]
description: "HDR won't enable on your Windows 11 laptop? Get it working with these 7 fixes — driver updates, HDR calibration, display settings, and hardware checks."
thumbnail: "/images/thumbs/how-to-fix-hdr-not-working-on-laptop-on-windows-11.webp"
faqs:
  - q: "Where is the HDR setting on Windows 11?"
    a: "Go to Settings then System then Display, select the display, and look for the HDR toggle under Brightness and color — it only appears on HDR-capable displays with a proper driver. There's also the Windows HDR Calibration app in the Microsoft Store, which fine-tunes the HDR response. If the toggle is missing entirely, your display driver isn't reporting HDR capability, which Fix 2 addresses."
  - q: "Why does HDR look worse than SDR on Windows 11?"
    a: "This happens when the HDR calibration is off, the SDR content brightness slider is misconfigured, or you're viewing SDR content with HDR forced on. Run the Windows HDR Calibration app to set proper black and white points, then adjust the SDR content brightness under Display settings. Also verify you're watching actual HDR content — HDR mode doesn't upgrade SDR videos, and forcing it on can make them look dull."
  - q: "Does Windows 11 Auto HDR work on all games?"
    a: "Auto HDR works with DirectX 11 and DirectX 12 games that don't already have native HDR, but not with every title — some games conflict with it or look worse. Toggle it per-game under Settings then System then Display then Graphics: select the game and adjust its HDR preference. If a specific game looks wrong, disable Auto HDR for that game rather than turning the system-wide feature off."
  - q: "Can I use HDR on battery power?"
    a: "Yes, but Windows 11 may limit display brightness on battery to save power, which reduces HDR impact since HDR relies on high peak brightness. Go to Settings then System then Display then HDR and check the battery-related options — you can allow HDR and higher brightness on battery at the cost of faster drain. For brightness-specific issues, see the [display brightness guide](/articles/how-do-i-fix-display-brightness-not-working/)."
---

Windows 11 has the best HDR support Windows has ever shipped — and yet the HDR toggle is missing, greyed out, or produces washed-out colors on plenty of laptops. HDR on a laptop needs the panel, the GPU driver, Windows' calibration, and the content to line up. When any piece is off, HDR either won't enable or looks worse than SDR.

This guide is Windows 11-specific: the current Settings paths, the Windows HDR Calibration app, Auto HDR for games, and the driver behaviors of recent Windows 11 builds. Work in order.

## Why this happens

- **Driver not reporting HDR capability:** The Settings toggle only appears when the GPU driver advertises HDR support for the panel.
- **Display not actually HDR-capable:** Many laptop panels lack the brightness and gamut for real HDR.
- **HDR calibration never run:** Uncalibrated HDR looks washed out or crushed.
- **Wrong color depth:** 8-bit output prevents proper HDR signaling.
- **External monitor HDR off:** The monitor's own HDR mode disabled in its menu.
- **Battery power limiting brightness:** Power saving caps the brightness HDR depends on.
- **App or game not HDR-aware:** SDR content doesn't benefit from the HDR toggle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm HDR capability in Windows 11 settings

Start with what Windows actually detects.

1. Open **Settings > System > Display** and select your display at the top if you have multiple.
2. Look for **HDR** under **Brightness & color** — if the toggle exists, the driver reports HDR support.
3. Click into the HDR settings page: it shows the display's certified capabilities (or lack thereof).
4. If the toggle is missing, note it and move to Fix 2 — the driver is the issue.

Also check **Advanced display** settings for **Bit depth** — HDR wants 10-bit. The [HDR capability reference](/articles/best-way-to-fix-hdr-not-working-on-laptop/) has a deeper checklist for ambiguous cases.

### Fix 2: Update the GPU driver from the manufacturer

The driver advertises HDR capability to Windows — a generic driver often doesn't.

1. Identify your GPU in Device Manager under **Display adapters**.
2. Download the driver from your laptop maker's support site, or from [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics, or the GPU vendor for discrete cards.
3. Install, restart, and recheck **Settings > System > Display** for the HDR toggle.
4. If HDR broke after a driver update, roll back instead (**Device Manager > Properties > Driver > Roll Back Driver**).

Manufacturer drivers include panel-specific HDR metadata that generic Windows drivers omit.

### Fix 3: Run the Windows HDR Calibration app

Uncalibrated HDR is the top cause of "HDR looks worse."

1. Install **Windows HDR Calibration** from the Microsoft Store (free).
2. Run it with HDR turned on, in a normally lit room.
3. Follow the test patterns: set the minimum luminance until the pattern disappears, then maximum luminance until it clips.
4. Save the profile — Windows applies it as your display's HDR calibration.
5. Re-test with HDR video (YouTube HDR in Edge, or the Movies & TV app).

Calibration makes a dramatic difference — most "washed out HDR" complaints disappear after this step.

### Fix 4: Set 10-bit color depth and full range

HDR signaling needs the right output format.

1. Open your GPU control panel (**Intel Graphics Command Center**, **NVIDIA Control Panel**, or **AMD Software**).
2. Set **color depth** to **10 bpc** and **output dynamic range** to **Full**.
3. You may need to lower the refresh rate to fit 10-bit within the cable/port bandwidth (e.g., 120Hz instead of 144Hz).
4. Recheck the HDR toggle in Windows settings.

On the internal laptop panel this is usually automatic, but external monitors often need manual configuration.

### Fix 5: Enable HDR on the external monitor and check the cable

For external displays, the monitor gates HDR.

1. In the monitor's on-screen menu, enable **HDR** / **HDMI HDR** / **HDR Mode** (often under Picture settings, sometimes per-input).
2. Use an **HDMI 2.0+** or **DisplayPort 1.4** cable — old cables drop HDR metadata.
3. Power-cycle the monitor after enabling HDR so it re-advertises capabilities to Windows.
4. Try a different port on the monitor — HDR is sometimes limited to specific inputs.

After the power cycle, Windows should show the HDR toggle for that display.

### Fix 6: Tune Auto HDR, SDR brightness, and battery settings

Windows 11's HDR-adjacent settings all affect the result.

1. Under **Settings > System > Display > HDR**, adjust **SDR content brightness** so non-HDR content looks normal with HDR on.
2. For games: **Settings > System > Display > Graphics > Change default graphics settings** — toggle **Auto HDR** and test per-game (disable it for games that look wrong).
3. On the HDR settings page, allow HDR on battery if you want full brightness unplugged — expect faster drain.
4. Test with genuine HDR content only: HDR YouTube videos, HDR games, or HDR photos.

Remember: Auto HDR enhances SDR games; it doesn't fix a broken HDR pipeline. Judge the fix on native HDR content.

### Fix 7: Reset the display configuration and update Windows

Persistent HDR failure after all settings are right means driver or OS state.

1. Install all Windows updates (**Settings > Windows Update**) — HDR handling improves with builds.
2. In Device Manager, uninstall the display adapter (ticking **remove driver**), restart, and install the manufacturer's driver fresh.
3. Re-run the HDR Calibration app after the driver reinstall.
4. Check the laptop maker's site for **display firmware** updates — rare, but some HDR bugs are panel-firmware issues.

If the panel is confirmed HDR-capable (DisplayHDR certification in specs) and HDR still won't engage with current drivers, contact the manufacturer's support — it's a firmware-level defect. For brightness problems that persist alongside HDR, the [brightness troubleshooting guide](/articles/how-do-i-fix-display-brightness-not-working/) covers the backlight side.

## Closing

HDR on Windows 11 is a chain: capable panel, reporting driver, calibration, correct color depth, real HDR content. The calibration app is the step most people skip and the one that transforms "washed out" into "vivid." Walk the chain in order and HDR stops being a broken toggle and starts being the feature you paid for.
