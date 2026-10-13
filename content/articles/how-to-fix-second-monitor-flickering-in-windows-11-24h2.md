---
title: "Second Monitor Flickering in Windows 11 24H2? Stop the Flicker"
slug: how-to-fix-second-monitor-flickering-in-windows-11-24h2
date: 2026-09-18
categories: ["drivers"]
tags: ["monitor flickering", "second monitor", "windows 11 24h2", "display driver"]
description: "Your second monitor flickers, flashes, or strobes after Windows 11 24H2? Pinpoint whether it's the refresh rate, cable, or driver — then fix it for good."
thumbnail: "/images/thumbs/how-to-fix-second-monitor-flickering-in-windows-11-24h2.webp"
faqs:
  - q: "Why does only my second monitor flicker?"
    a: "The second monitor usually runs through a different output, cable, refresh rate, or GPU than the laptop panel, so it has more failure points. The most common causes are a refresh-rate mismatch, a marginal cable or adapter, or the graphics driver mishandling the external output after an update. The laptop panel's stability actually helps diagnosis — it proves the GPU's core rendering is fine."
  - q: "Can a bad cable cause flickering but still show a picture?"
    a: "Yes — this is the classic marginal-cable symptom. A damaged or low-quality cable can carry enough signal for a picture but drop enough data to cause flicker, sparkles, or momentary blackouts, especially at high refresh rates or resolutions. Swapping in the monitor's original cable is the fastest way to rule this out."
  - q: "Why did flickering start right after the 24H2 update?"
    a: "The update commonly replaces the graphics driver with a version that mishandles the external output's timing, resets the refresh rate to an incompatible value, or breaks variable refresh rate (FreeSync/G-Sync) negotiation. Rolling back the graphics driver or clean-installing the GPU maker's release usually stops update-triggered flicker."
  - q: "Is flickering dangerous for the monitor?"
    a: "Flicker itself rarely damages modern monitors, but the underlying cause can matter — a failing cable or port will only get worse, and running at an out-of-range refresh rate stresses the panel's timing controller. Fix it promptly rather than tolerating it, and avoid forcing refresh rates the monitor's spec sheet does not list."
---

The second monitor was fine yesterday. Today it flickers — a rapid strobing, intermittent black flashes, or a shimmering that makes text unreadable. The laptop's own screen is perfect. The 24H2 update installed overnight, and now the external display is having a seizure.

Flicker on one display while the other is stable is actually good news diagnostically: it rules out the GPU's core rendering and points at the external output path — refresh rate, cable, or the driver's handling of that output. The 24H2 update is a frequent trigger because it resets refresh rates and replaces graphics drivers. Work from the cheapest checks (settings, cable) to the driver rebuild. If the monitor is not detected at all rather than flickering, start with our [USB-C display guide](/articles/how-to-fix-usb-c-display-not-working-in-windows-11-24h2/) or the external monitor detection fixes.

## Why this happens

- **Refresh rate set wrong.** 24H2 reset the external monitor to a rate its panel cannot sustain cleanly.
- **Marginal cable or adapter.** The cable carries a picture but drops data, causing flicker and black flashes.
- **Graphics driver mishandling the output.** The updated driver has broken timing for the external port.
- **Variable refresh rate conflict.** FreeSync/G-Sync negotiation fails after the driver update.
- **Resolution beyond cable bandwidth.** 4K over an old HDMI cable exceeds what the cable can carry.
- **Interference from power cables.** Poorly shielded cables pick up noise from nearby power bricks.
- **Monitor overdrive set too high.** Aggressive response-time overdrive causes inverse-ghosting shimmer.
- **Failing monitor backlight or panel.** Hardware flicker that persists across cables, ports, and computers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the correct refresh rate

Right-click the desktop, choose **Display settings**, select the second monitor in the diagram, scroll to **Advanced display**, and check the **Refresh rate** dropdown. Set it to the monitor's native rate — usually 60 Hz, or the high rate (120/144/165 Hz) the spec sheet lists. The 24H2 update frequently resets external monitors to a wrong rate, and a panel driven off-spec flickers. Apply, and watch for a full minute — some flicker takes time to manifest. If the desired rate is missing from the dropdown, the cable or driver is limiting the reported modes, which points at Fix 2 or Fix 4.

### Fix 2: Swap the cable and simplify the chain

Replace the cable with the one that came with the monitor, or a certified high-speed cable rated for your resolution and refresh rate. Remove adapters, docks, and splitters for the test — plug directly into the laptop. Route the video cable away from power bricks and chargers. If the flicker stops on the direct certified cable, the old cable or adapter was marginal — 4K and high-refresh signals are merciless to cheap cables. Do not reintroduce the dock until the direct connection is proven stable for a day.

### Fix 3: Disable variable refresh rate temporarily

Go to **Settings > System > Display > Graphics > Default graphics settings** and turn off **Variable refresh rate**. On the monitor itself, open the on-screen menu and disable **FreeSync**/**G-Sync**/**Adaptive-Sync** temporarily. Driver updates routinely break VRR negotiation on external monitors, producing flicker that looks like a hardware fault. If disabling VRR stops the flicker, you have identified the layer — re-enable it after the driver fix in Fix 4, since a correct driver should handle VRR properly.

### Fix 4: Clean-install the graphics driver

Download the latest driver for your GPU — Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), AMD from the [AMD driver support page](https://www.amd.com/en/support/download/drivers.html) — and select **clean install** during setup. Restart and retest the second monitor at its native refresh rate. The clean install resets the driver's display-timing tables, which is exactly what update-triggered flicker needs. If the newest driver flickers but the previous one did not, roll back to the older build and report the regression to the GPU maker.

### Fix 5: Match resolution to cable bandwidth

In **Display settings**, try lowering the second monitor to a modest resolution and refresh rate (1080p at 60 Hz) temporarily. If the flicker vanishes, the cable or port cannot sustain the higher mode's bandwidth — you need a better cable (Ultra High Speed HDMI or certified DisplayPort) or a lower mode. This test distinguishes bandwidth problems from driver problems cleanly: bandwidth flicker scales with resolution, driver flicker does not. Never run above the cable's rated spec and call the monitor broken.

### Fix 6: Adjust the monitor's own settings

Open the monitor's on-screen display menu and reset it to factory defaults — a firmware quirk or a bad overdrive setting can flicker independently of the PC. Specifically check **Response Time / Overdrive** and set it to Normal or Off; maximum overdrive causes visible shimmer on many panels. Disable any **eco** or **dynamic contrast** modes that modulate the backlight, since backlight modulation reads as flicker. If the monitor has a firmware update available from its maker, install it — monitor firmware fixes for flicker are more common than people expect.

### Fix 7: Isolate the hardware

Connect the monitor to a different computer with a known-good cable. Flicker there too means the monitor or its panel/backlight is failing — no driver will fix it. No flicker there means your laptop's port, cable, or driver is at fault; try the laptop's other video outputs. Also test the laptop with a different monitor: if every external display flickers on this laptop, the GPU's output circuitry or the port hardware is suspect. Port and GPU-output failures are board-level repairs for a service center, but confirm with the cross-testing first — most "hardware" flicker turns out to be cable or driver. If the monitor is not detected at all rather than flickering, start with our [Acer external monitor detection guide](/articles/how-to-fix-external-monitor-not-detected-on-acer-laptop/).

## Closing

Second-monitor flicker is a path problem: refresh rate, cable bandwidth, driver timing, monitor settings. Work the path in order and change one thing at a time — flicker diagnosis punishes shotgun troubleshooting. Once the picture is stable, note the exact driver version and cable that worked, because both are the first suspects the next time it happens.
