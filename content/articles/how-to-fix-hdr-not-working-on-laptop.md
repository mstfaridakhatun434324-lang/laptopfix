---
title: "HDR Not Working on Your Laptop? Fix Washed-Out and Missing HDR"
slug: how-to-fix-hdr-not-working-on-laptop
date: 2026-10-10
categories: ["drivers"]
tags: ["hdr not working", "hdr washed out", "windows 11 hdr", "display driver", "hdr calibration"]
description: "HDR not working on your laptop? Fix missing HDR toggles, washed-out colors, and HDR that won't stay on with driver, cable, and calibration repairs."
thumbnail: "/images/thumbs/how-to-fix-hdr-not-working-on-laptop.webp"
faqs:
  - q: "Why is there no HDR toggle in my Windows 11 display settings?"
    a: "The HDR toggle only appears when Windows detects an HDR-capable display through a proper driver handshake. A missing toggle means the panel isn't HDR-capable, the display driver isn't exposing HDR support, or the cable can't carry the HDR metadata. Reinstalling the GPU driver from the manufacturer is the first fix — generic drivers often hide the toggle."
  - q: "Why does HDR look washed out on my laptop?"
    a: "Washed-out HDR is almost always an SDR/HDR brightness balance problem, not broken HDR. Windows renders SDR content inside the HDR container, and if the balance slider is wrong, everything looks faded. Run the Windows HDR Calibration app from the Microsoft Store and adjust the SDR content brightness — that single calibration fixes most washed-out complaints."
  - q: "Can an HDMI cable prevent HDR from working?"
    a: "Yes. HDR metadata needs the bandwidth headroom that only High Speed or Premium High Speed HDMI cables (for 4K HDR) reliably provide. An old or very long cable may carry the video signal but drop the HDR metadata, leaving you with SDR and no toggle. For DisplayPort, use a VESA-certified cable. Cable swaps fix a surprising number of HDR failures."
  - q: "Why does HDR turn itself off after restart?"
    a: "HDR settings that don't persist usually indicate a driver or EDID handshake problem — Windows re-detects the display on boot and fails the HDR capability check. Updating the GPU driver, the monitor firmware, and disabling fast startup (which preserves the bad detection state) typically makes the setting stick."
---

HDR on Windows laptops fails in three distinct ways: the toggle is missing entirely, HDR is on but everything looks washed out, or HDR won't stay enabled. Each has different causes, and the washed-out case in particular sends people down driver rabbit holes when the actual fix is a thirty-second calibration slider. The underlying theme is that HDR is a negotiation — between the GPU driver, the cable, and the panel — and any party can veto it silently.

This guide handles all three failure modes, starting with capability verification (is HDR even possible here?) because a surprising number of "HDR not working" cases are non-HDR panels.

## Why this happens

- **Panel not actually HDR-capable.** "HDR-ready" marketing versus true HDR hardware.
- **Generic display driver hiding HDR.** Driver not exposing HDR support to Windows.
- **Under-spec cable dropping HDR metadata.** Signal carries video but not the HDR info frames.
- **SDR/HDR brightness imbalance.** Washed-out look from wrong calibration, not broken HDR.
- **EDID handshake failing HDR detection.** Monitor not advertising HDR capability correctly.
- **Conflicting color management.** ICC profiles and GPU color settings fighting HDR.
- **Fast startup preserving bad detection.** Stale display state across boots.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify HDR is actually possible

Don't troubleshoot hardware you don't have.

1. Check your laptop/panel **specifications** for HDR certification (DisplayHDR 400/600/1000, or Dolby Vision) — "HDR support" in marketing sometimes means tone-mapping, not true HDR.
2. **Settings > System > Display > Advanced display** → check **"HDR certification"** — Windows reports what the panel claims.
3. For external monitors: confirm the monitor's HDR mode is **enabled in its on-screen menu** — many ship with HDR off by default.
4. Verify the connection: HDR over HDMI needs a **High Speed+** cable; over USB-C needs **DisplayPort alt-mode 1.4**.
5. If the panel genuinely isn't HDR-capable, no software fix applies — the remaining fixes are for capable hardware.

### Fix 2: Reinstall the display driver

The core fix for missing HDR toggles.

1. **Device Manager > Display adapters** → uninstall the GPU driver (check "delete driver software") → restart.
2. Install the proper driver from your laptop maker or the GPU manufacturer ([NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), Intel).
3. Check **Settings > System > Display** for the HDR toggle after reinstalling — its appearance confirms the driver now exposes HDR.
4. On dual-GPU laptops, update **both** drivers — the integrated GPU typically handles the display pipeline.
5. If HDR broke after a driver update, **roll back** first.

The driver method generalizes from [how to fix the display driver stopped responding](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/).

### Fix 3: Calibrate away the washed-out look

For HDR that's on but ugly.

1. Install the **Windows HDR Calibration** app from the Microsoft Store and run it — it's Microsoft's official tool for this exact problem.
2. Adjust the **SDR content brightness** slider — this is the control that fixes washed-out desktops in HDR mode.
3. In **Settings > System > Display > HDR**, check the HDR-specific brightness and color settings.
4. Reset any custom **ICC color profiles** (`colorcpl.exe` → set to system default) — custom profiles fight HDR tone mapping.
5. Reset GPU control panel color settings (NVIDIA Control Panel, Intel Graphics Command Center) to defaults — stacked adjustments wash out HDR.

### Fix 4: Fix the cable and connection

For missing toggles and HDR that won't engage on external displays.

1. Swap to a **short, certified cable**: Premium High Speed HDMI for 4K HDR, VESA-certified DisplayPort otherwise.
2. Connect **directly** — remove docks, adapters, and KVM switches from the chain for testing.
3. Try a different port on both the laptop and the monitor.
4. In the monitor's menu, enable **HDMI Ultra HD Deep Color / Enhanced format** on the port you're using — required for HDR metadata on many TVs/monitors.
5. Power-cycle the monitor (unplug 30 seconds) with the cable connected to force a fresh EDID handshake advertising HDR.

Related external-display handshake repair: [how to fix an external monitor not detected after a Windows 11 update](/articles/how-to-fix-external-monitor-not-detected-after-windows-11-update/).

### Fix 5: Make HDR settings persist

For HDR that turns off after restart or sleep.

1. Disable **fast startup** (Power Options → Choose what the power buttons do) — it preserves the stale display detection.
2. Update the **monitor firmware** from the maker's site — EDID/HDR advertisement bugs get fixed in firmware.
3. Update the laptop **BIOS** — display output firmware lives there.
4. In the monitor menu, disable **deep sleep** for the input — aggressive sleep breaks the HDR handshake on wake.
5. After waking from sleep, toggle HDR off and on once — if that restores it, you're working around a handshake bug (firmware updates are the real fix).

### Fix 6: Resolve app and content issues

When HDR works in some apps but not others.

1. In the app or game, enable **HDR explicitly** in its own video settings — Windows HDR on doesn't auto-enable in-app HDR.
2. For games: enable HDR in Windows **before** launching the game; toggling mid-game breaks the swap chain.
3. Streaming apps (Netflix, YouTube) need their own HDR/premium tiers and supported browsers/apps — verify the content is actually HDR.
4. Disable **Auto HDR** per-game in **Settings > System > Display > Graphics** if specific games look wrong — Auto HDR's tone mapping doesn't suit every title.
5. Check [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows) for known HDR issues on your build.

### Fix 7: Reset the display pipeline

The last-resort tier.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Delete custom color profiles and reset the GPU control panel to defaults (Fix 3's steps, applied aggressively).
3. Test HDR on a **fresh Windows user profile** — per-user display settings can corrupt the HDR state.
4. As a final measure, an in-place Windows repair install rebuilds the display stack while keeping files.
5. If HDR never works on a panel advertised as HDR-capable across drivers, cables, and OSes — it's a firmware/panel defect; use the warranty.

For the related blue-light feature that shares this pipeline, see [how to fix Night Light not working](/articles/how-to-fix-night-light-not-working-in-windows-11-24h2/).

## Closing

HDR troubleshooting is negotiation troubleshooting: verify the panel's capability, reinstall the driver so Windows sees it, use a cable with the bandwidth to carry it, and calibrate the SDR balance so it looks right. The washed-out case is the most common and the most misdiagnosed — it's a calibration slider, not a driver bug, and the Windows HDR Calibration app exists precisely for it. Get the handshake right and the toggle appears; get the calibration right and it looks the way HDR should.
