---
title: "How to Fix HDR Not Working on Your ARM Laptop"
slug: hdr-not-working-arm-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["hdr", "display", "arm laptop", "adreno", "windows 11", "troubleshooting"]
description: "Fix HDR not working on ARM laptops — verify panel support, update Adreno drivers, fix the HDR toggle and SDR brightness, and solve external-monitor HDR."
thumbnail: "/images/thumbs/hdr-not-working-arm-laptop.webp"
faqs:
  - q: "How do I know if my ARM laptop panel actually supports HDR?"
    a: "Open Settings > System > Display > HDR and read the display capabilities list — Windows reports exactly what the panel's EDID claims, including HDR video support and peak brightness. If HDR video streaming shows 'Not supported,' the panel is SDR regardless of what the marketing sheet implied."
  - q: "Why does everything look washed out when I turn HDR on?"
    a: "Washed-out HDR is almost always the SDR content brightness slider set too low, or an app rendering SDR content without tone mapping. Raise the SDR brightness slider in the HDR settings page first — it controls how bright non-HDR content appears while HDR is active."
  - q: "HDR works on the laptop screen but not my external monitor. Why?"
    a: "External HDR needs the full chain: an HDR-capable monitor, a cable and port with enough bandwidth (HDMI 2.0+ or DisplayPort), and the monitor's own HDR mode enabled in its on-screen menu. A weak link anywhere in that chain makes Windows hide the HDR toggle for that display."
  - q: "Does HDR drain the battery faster on ARM laptops?"
    a: "Yes, measurably. HDR pushes the display pipeline and backlight harder, and on Copilot+ laptops the difference can be 10–15% less runtime in video playback. If battery matters more than color, leave HDR off except when watching HDR content."
---

The HDR toggle is grayed out in Settings, or you flip it on and everything looks washed out and wrong — the "HDR" your Snapdragon laptop advertised is nowhere to be found. Meanwhile your old Intel machine handled HDR fine, which makes the ARM laptop feel broken by comparison.

On ARM laptops, HDR runs through the Adreno display pipeline and a Windows HD Color stack that gets less validation than the Intel/AMD path. The failure points are specific: "HDR-ready" panels that are really SDR, Adreno drivers missing parts of the HDR path, the ignored SDR-brightness slider, and HDMI handshakes that silently fall back to SDR.

This guide gives you six fixes in technician order: verifying the panel is genuinely HDR first, then repairing the driver, setting the toggle and brightness correctly, fixing the external-monitor chain, handling per-app HDR, and resetting the color pipeline. Check the HDR settings page after each step.

## Why this happens

- **Panel is not truly HDR:** Many laptop panels are "HDR400" or "HDR-ready" in marketing but lack the brightness and color depth for real HDR; Windows reads the EDID and hides the toggle.
- **Adreno driver missing the HDR path:** Early and generic Adreno drivers on Windows on ARM exposed SDR only — the HDR toggle appears only with the OEM's validated driver.
- **SDR content brightness set wrong:** With HDR on, SDR content brightness is governed by a separate slider; set too low, the whole desktop looks washed out and HDR looks broken.
- **External monitor chain failure:** HDR over HDMI/DisplayPort needs monitor-side HDR enabled, a capable cable, and the right port mode — one weak link and Windows offers SDR only.
- **App not using the HDR pipeline:** Browsers, video players, and games each negotiate HDR separately; the system toggle being on does not force an SDR app to render in HDR.
- **Stale color profile or EDID:** A corrupted ICC profile or misread EDID can make Windows misreport the panel's capabilities and gray out controls that should work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the panel is genuinely HDR-capable

Do not troubleshoot a feature the hardware lacks. Windows tells you exactly what the panel claims — read it before changing anything.

1. Open **Settings > System > Display > HDR** (on some builds: **Settings > System > Display > Windows HD Color settings**).
2. Read the **Display capabilities** list — HDR video streaming, WCG, peak brightness. "Not supported" means the panel is SDR, full stop.
3. If the spec sheet claims HDR400 but Windows says unsupported, trust Windows — the EDID is the ground truth.
4. If the capabilities show HDR support but the toggle is grayed out, the problem is software — continue to Fix 2 with confidence the panel can do it.
5. If the panel is genuinely SDR, stop here: no driver or setting creates HDR on an SDR panel, and chasing it further wastes an afternoon.

### Fix 2: Install the OEM Adreno graphics driver

The single most common fix on Snapdragon laptops. Generic Microsoft display drivers and early Adreno packages expose an SDR-only pipeline, and the HDR toggle simply does not appear until the OEM's validated driver is installed.

1. In **Device Manager > Display adapters**, check the driver — "Microsoft Basic Display Adapter" or an old Qualcomm date means no HDR path.
2. Download the latest graphics/display driver for Windows 11 on ARM from your maker's support page (Dell, HP, Lenovo, or ASUS — match your exact model).
3. Run the installer as administrator, let it finish without sleep or interruption, and restart when prompted.
4. Reopen the HDR settings page — on most models the toggle and capabilities list appear immediately after the OEM driver loads.
5. If Windows Update later replaces the driver and HDR vanishes again, check the [Windows support pages](https://support.microsoft.com/en-us/windows) for the supported method to block that specific driver update.

### Fix 3: Toggle HDR correctly and set SDR brightness

With a capable panel and driver, most remaining "HDR looks wrong" complaints are the SDR brightness slider. HDR mode changes how the desktop composites, and SDR content needs its own brightness level.

1. In the HDR settings page, toggle **Use HDR** (or **Play streaming HDR video**) **On** for the built-in display.
2. Drag the **SDR content brightness** slider up until the desktop looks normal — this single slider fixes most washed-out desktops.
3. Play an actual HDR video (the HDR settings page often links a sample, or use the Movies & TV app with HDR content) to confirm real HDR engages — the screen should visibly shift in contrast, not just brightness.
4. If HDR video looks good but the desktop still looks off, that is normal tone-mapping — many users simply leave HDR off for desktop work.
5. Windows 11 remembers the setting, so this is a one-time preference: HDR on for media, off for desktop work if you prefer.

### Fix 4: Fix the external-monitor HDR chain

External HDR fails at the weakest link, and the laptop is rarely it. Work the chain methodically: monitor, cable, port.

1. In the monitor's on-screen menu, enable its HDR mode explicitly — many monitors ship with HDR off and will not advertise it to Windows until you turn it on.
2. Connect directly with a known-good cable — HDMI 2.0+ or DisplayPort, no docks; cheap cables silently fall back to SDR bandwidth.
3. Set the monitor's HDMI port to full-bandwidth mode ("Enhanced" or 2.0/2.1) — default 1.4-compatibility modes cap the handshake below HDR.
4. In Windows, select the external display in **Settings > System > Display**, then open its HDR settings page and confirm the capabilities list now shows HDR support.
5. HDMI renegotiation for HDR can also drop the audio endpoint — a cousin of the device-handoff bugs behind [Audacity issues on ARM Windows](/articles/audacity-arm-windows-issues/). If audio vanishes when HDR toggles on, reseat the cable.

### Fix 5: Handle per-app HDR (browsers and players)

System HDR being on does not make every app HDR. Browsers and players negotiate HDR independently, and on ARM the per-app gaps are wider than on x86.

1. Test HDR in more than one app — Edge, Movies & TV, YouTube. If it works in one but not another, the app is the variable, not the system.
2. Browsers differ in their HDR video pipelines: if HDR plays in Edge but not Firefox, the browser is the difference — the known gaps are covered under [Firefox ARM64 issues on Windows](/articles/firefox-arm64-windows-issues/).
3. For the best results with local files, use the **Movies & TV** app or a player that explicitly supports Windows HDR, and enable HDR in the player's own settings if it has a toggle.
4. Some apps use their own color pipeline and ignore the system toggle — if OneNote looks washed out while HDR video plays fine, that is an app rendering choice, separate from [OneNote Copilot not working](/articles/onenote-copilot-not-working/).
5. Run Microsoft's **Windows HDR Calibration** app from the Store once — it builds a profile tuned to your panel and fixes most residual "slightly off" complaints.

### Fix 6: Reset the color profile and re-read the panel

When the panel is HDR, the driver is OEM, and the toggle still misbehaves, stale color state is the last suspect — a bad ICC profile or a misread EDID that survives driver reinstalls.

1. In **Settings > System > Display > Advanced display**, check the reported bit depth — 8-bit with dithering is normal on ARM panels; a wrong report hints at EDID trouble.
2. In **Color Management** (search it in Start), remove any custom ICC profiles assigned to the display and set the profile back to the system default.
3. Disconnect external monitors, then do a full cold boot: hold **Shift** and click **Shut down**, wait ten seconds, power on — this forces the firmware to re-enumerate the panel and its EDID.
4. Reopen the HDR settings page and re-read the capabilities list; a corrected EDID read restores toggles that a stale read had grayed out.
5. If capabilities still misreport after a cold boot and clean driver, check for a panel firmware update from your maker. A fresh [Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) and in-place repair install is the final software resort.

## Closing

HDR on ARM laptops fails at predictable points: a panel that was never really HDR, a generic driver hiding the toggle, the SDR brightness slider, or a weak external-monitor link. Verify the panel, install the OEM driver, set the slider, work the chain.
