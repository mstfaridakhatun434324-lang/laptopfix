---
title: "External Monitor Not Detected on an ASUS Laptop? Here's What to Do"
slug: how-to-fix-external-monitor-not-detected-on-asus-laptop
date: 2026-09-25
categories: ["drivers"]
tags: ["external monitor", "asus laptop", "monitor not detected", "hdmi"]
description: "ASUS laptop not detecting your external monitor? Check Armoury Crate GPU modes, cables, and drivers with this step-by-step fix guide."
thumbnail: "/images/thumbs/how-to-fix-external-monitor-not-detected-on-asus-laptop.webp"
faqs:
  - q: "Why won't my ASUS laptop detect the external monitor?"
    a: "The common causes are the monitor's input selection, a bad cable or adapter, Windows display detection being stuck, or a graphics driver problem. ASUS adds its own wrinkle: Armoury Crate's GPU modes (Eco, Standard, Ultimate) change which GPU drives the external ports — Ultimate mode routes ports to the discrete GPU, and a broken discrete driver then kills external output."
  - q: "Which ASUS GPU mode should I use for external monitors?"
    a: "For troubleshooting, switch Armoury Crate to Standard mode, which keeps both GPUs available with normal port routing. Ultimate mode disables the integrated GPU and routes everything through the discrete GPU for lowest latency — great for gaming, but if the NVIDIA or AMD discrete driver is broken, external ports go dark. Test in Standard first."
  - q: "Does MyASUS help with monitor detection problems?"
    a: "Yes, for the driver side. MyASUS (or Armoury Crate on ROG/TUF models) offers validated BIOS, chipset, and graphics updates for your exact model. When external detection fails after a Windows update, installing the ASUS-validated graphics driver through MyASUS often fixes what the GPU maker's generic driver does not."
  - q: "Can a USB-C dock break external monitor detection?"
    a: "Docks are a frequent culprit — their DisplayPort MST hubs and firmware add failure points. Test with a direct HDMI or USB-C cable to the monitor first. If direct works but the dock does not, update the dock's firmware and the laptop's Thunderbolt/USB4 and graphics drivers before blaming the laptop."
---

The external monitor is powered, the HDMI cable is seated, and the ASUS shows only its own screen. Windows Settings lists one display. The monitor works on another machine, the cable is fine — but this laptop refuses to see it.

Monitor detection is a handshake across the cable, the GPU driver, and Windows' display topology — and ASUS laptops add a GPU-mode layer through Armoury Crate that can reroute or disable the external ports. Work the physical chain first, then the ASUS-specific software, then the drivers. (Acer owners: our [Acer external monitor guide](/articles/how-to-fix-external-monitor-not-detected-on-acer-laptop/) covers the same problem on that brand.)

## Why this happens

- **Monitor on the wrong input.** The display is listening on a different HDMI/DP port than the cable uses.
- **Bad cable or adapter.** Damaged cables and cheap adapters break the EDID handshake.
- **Armoury Crate GPU mode routing.** Ultimate/Eco modes change which GPU drives the external ports.
- **Discrete GPU driver broken.** In Ultimate mode, a bad NVIDIA/AMD driver kills all external output.
- **Windows detection stuck.** Stale display topology cache ignores the newly connected monitor.
- **Projection mode on PC-screen-only.** Windows policy, not hardware, hides the monitor.
- **Dock or MST hub failing.** The dock's firmware or chipset breaks the handshake.
- **BIOS display settings.** Firmware graphics options interfere with port initialization.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the monitor input and simplify the cable

On the monitor, manually select the exact input the cable uses — never trust auto-detect. Unplug the monitor's power for 30 seconds to reset its input logic. Then connect directly: one cable, no dock, no adapters, into the ASUS. If you are using USB-C, verify the port supports DisplayPort Alt Mode and use a video-rated cable. A direct connection that works immediately proves the dock or adapter was the failure point. Microsoft's display troubleshooting is at [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 2: Check Armoury Crate GPU mode

Open **Armoury Crate** (ROG/TUF models) and check the **GPU Mode** or **GPU Power Saving** setting. If it is on **Ultimate**, the discrete GPU drives everything including external ports — switch to **Standard** mode and restart, which restores normal hybrid port routing. If it is on **Eco Mode**, the discrete GPU is fully off, which can darken ports wired to it — again, **Standard** is the troubleshooting baseline. Retest detection after the mode change and restart. This ASUS-specific setting explains "worked yesterday, dead today" cases where an Armoury Crate update flipped the mode.

### Fix 3: Force Windows detection and projection mode

Press **Windows + P** and choose **Extend** — "PC screen only" is a five-second fix when it is the cause. Then go to **Settings > System > Display**, click **Detect**, and if a greyed-out display appears, select it and set **Extend desktop to this display**. Do the detect twice; the first pass sometimes only wakes the topology service. If detection finds the monitor but it will not stay extended, note the error — that points at the driver rather than the handshake. If the monitor appears but the image flickers or drops out, our [second monitor flickering guide](/articles/how-to-fix-second-monitor-flickering-in-windows-11-24h2/) continues from there with refresh-rate and cable fixes.

### Fix 4: Update graphics drivers via MyASUS and the GPU makers

Open **MyASUS** (or Armoury Crate) and install any offered **graphics, chipset, and BIOS** updates for your exact model — ASUS validates these against your port wiring. Then update the discrete GPU driver directly: NVIDIA users from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), AMD users from the [AMD driver support page](https://www.amd.com/en/support/download/drivers.html), choosing clean install. Restart and retest. On ASUS gaming laptops the HDMI port is typically wired to the discrete GPU, so its driver health directly determines whether external monitors are detected.

### Fix 5: Reinstall the monitor device entry

In **Device Manager**, expand **Monitors**, right-click any external or generic monitor entry, choose **Uninstall device**, then click **Action > Scan for hardware changes** with the monitor connected and on the right input. This forces Windows to re-read the monitor's EDID handshake. If Device Manager shows the monitor correctly but Windows still will not use it, the issue is topology-level — repeat Fix 3 after this reset, since the fresh EDID read often unblocks detection.

### Fix 6: Update the dock firmware and Thunderbolt drivers

If you use a USB-C dock, check the dock maker's site for a **firmware update** — dock MST hub firmware bugs are a real and common cause of detection failures. On the laptop, update the **Thunderbolt/USB4** and **chipset** drivers through MyASUS. Test the monitor both through the dock and direct; if direct works and the dock never does even with current firmware, the dock's chipset may be incompatible with your ASUS model's USB-C implementation — a different dock, not a laptop repair, is the answer.

### Fix 7: Check BIOS settings and isolate the hardware

Restart and press **F2** or **Del** to enter the ASUS BIOS. Look for graphics configuration — **iGPU Multi-Monitor**, graphics mode, or display output options — and ensure external output is not disabled. Check for a **BIOS update** in MyASUS and flash on AC power. For hardware isolation: test the ASUS port with a different monitor, and test the monitor with a different computer. If no display is ever detected on any ASUS port with any cable, while the internal screen is fine, the external output circuitry needs service-center diagnosis.

## Closing

ASUS external-monitor failures usually trace to four things: the monitor's input, the cable chain, Armoury Crate's GPU mode, or the graphics driver. Set Armoury Crate to Standard while troubleshooting, verify the physical chain, then rebuild the drivers through MyASUS and the GPU makers. Once the second screen lights up, you can switch GPU modes back — now knowing exactly which setting to blame if it ever goes dark again.
