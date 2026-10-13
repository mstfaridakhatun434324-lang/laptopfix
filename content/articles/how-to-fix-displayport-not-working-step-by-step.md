---
title: "How to Fix DisplayPort Not Working — Step by Step"
slug: how-to-fix-displayport-not-working-step-by-step
date: 2026-09-29
categories: ["drivers"]
tags: ["displayport not working", "external monitor", "no signal", "gpu driver", "multi monitor"]
description: "DisplayPort not working — no signal on your external monitor? Step-by-step fixes for cables, GPU drivers, MST hubs, and monitor input settings."
thumbnail: "/images/thumbs/how-to-fix-displayport-not-working-step-by-step.webp"
faqs:
  - q: "Why does DisplayPort say no signal but HDMI works?"
    a: "HDMI and DisplayPort negotiate their links differently — HDMI's handshake is simpler and more tolerant of marginal cables, while DisplayPort's link training aborts on signal issues HDMI would tolerate. A cable or port that is 'good enough' for HDMI can fail DisplayPort training entirely. This is why the certified-cable test is step one: it is genuinely the most common root cause of DP-specific failures."
  - q: "Do I need a special cable for 4K 144Hz over DisplayPort?"
    a: "Yes — you need a VESA-certified DisplayPort cable rated for HBR3 (DP 1.4) bandwidth, kept as short as practical. Uncertified or long passive cables cannot sustain the ~26 Gbps that 4K144 needs even with DSC. If 4K60 works but 4K144 shows no signal, the cable is the prime suspect, followed by DSC negotiation settings on the monitor and GPU."
  - q: "What is the DisplayPort pin 20 problem?"
    a: "The DisplayPort spec says pin 20 (power) should not be wired through on standard cables, but cheap cables wire it anyway, backfeeding 3.3V between devices. This can prevent link training, cause intermittent black screens, and in rare cases damage ports. VESA-certified cables do not have this problem. If a no-name cable causes issues that a certified cable does not, pin 20 is a likely explanation."
  - q: "Can daisy-chaining monitors cause DisplayPort to stop working?"
    a: "Yes. Daisy-chaining (MST) requires the first monitor to have MST explicitly enabled in its OSD, correct in/out port ordering, and total bandwidth within a single DP link. A firmware bug in the first monitor or exceeding the bandwidth budget kills the whole chain silently. Always test each monitor directly connected first — if both work solo, the problem is the MST configuration, not the laptop."
---

DisplayPort's 'no signal' failure is maddening because the standard is finicky about link training: the GPU and monitor negotiate lanes, bandwidth, and protocol at every connection, and any weak link — cable, driver, firmware, or setting — aborts the handshake silently. The monitor stays dark, Windows may or may not show a second display in Settings, and reseating the cable sometimes 'fixes' it until the next reboot.

The diagnostic order matters: cable and monitor input first (physical), then Windows display settings, then GPU drivers, then the deeper DisplayPort-specific issues like MST daisy-chaining, DSC compression, and pin-20 power problems on cheap cables. Most failures are in the first three steps.

For the broader 'monitor not detected' problem on laptops, see our [second-monitor guides](/articles/how-to-fix-laptop-not-detecting-second-monitor-after-windows-11-update/) and the [external monitor walkthrough](/articles/how-to-fix-external-monitor-not-detected-after-windows-11-update/); this guide is DisplayPort-specific.

## Why this happens

- **Cheap or damaged DisplayPort cable** — Non-certified cables fail link training, especially at high refresh rates and resolutions.
- **Monitor on wrong input** — The monitor sits on HDMI input while the cable is in DisplayPort — embarrassingly common.
- **GPU driver failing link training** — Corrupt or outdated graphics drivers botch the DP handshake.
- **Pin-20 powered cables** — Cheap cables wire pin 20 (power) through, backfeeding voltage that disrupts negotiation.
- **MST daisy-chain misconfiguration** — Daisy-chained monitors need MST enabled on the first monitor; wrong order breaks the chain.
- **DSC / high-bandwidth mode mismatch** — 4K144+ over DSC fails when either end mishandles compression negotiation.
- **BIOS / firmware display output settings** — Laptops with dGPUs may route DP through the discrete GPU with its own driver state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the monitor input and cable seating

The two-minute physical check that resolves a large share of 'no signal' reports.

1. Use the monitor's OSD buttons to select the **DisplayPort** input explicitly (not Auto).
2. Unplug both ends of the DP cable and reseat firmly — DP connectors should click via their latch.
3. If the cable has a latch button, press it when unplugging to avoid damaging the port.
4. Power-cycle the monitor (unplug 30 seconds) — monitors cache failed link-training state.

### Fix 2: Test with a certified cable

The cable is the number-one DisplayPort failure point. A certified cable is the cheapest definitive test.

Length matters as much as certification: passive DisplayPort cables are only reliable up to about 2 meters at full HBR3 bandwidth. If your setup needs a longer run, use an active (or fiber-optic) DisplayPort cable rated for the length — a 5-meter passive cable that 'should' work is one of the most common sources of intermittent no-signal complaints.

1. Borrow or buy a **VESA-certified** DisplayPort cable in the shortest length that reaches.
2. Avoid 'DP 1.4' claims on no-name cables; certification is what matters, not the printed version.
3. Test at a lower resolution/refresh first (1080p60) to confirm the link, then raise it.
4. If the certified cable works, discard the old one — intermittent DP cables are not worth keeping.

### Fix 3: Verify Windows sees the display

Determines whether this is a link failure or a configuration failure.

1. Press Win + P and select **Extend** (not PC screen only).
2. Open Settings > System > Display and click **Detect** / check for the second display rectangle.
3. If Windows sees it but shows no image, lower the resolution and refresh rate for that display to 1080p60 as a test.
4. If Windows does not see it at all, continue to driver fixes.

### Fix 4: Reinstall the graphics driver

Driver-side link-training failures are fixed by a clean driver reinstall.

1. Download the current driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
2. Use DDU in Safe Mode for a full clean removal, then install fresh.
3. After reinstalling, reconnect the DisplayPort cable and let link training run fresh.
4. On laptops with dual GPUs, update both Intel/AMD integrated and NVIDIA/AMD discrete drivers.

### Fix 5: Adjust DisplayPort version and DSC settings

Forcing a lower DP version sidesteps negotiation bugs at high bandwidth.

1. In the monitor OSD, find DisplayPort version/stream settings and try **DP 1.2** instead of 1.4.
2. In the GPU control panel (NVIDIA Control Panel / AMD Adrenalin), disable **Display Stream Compression (DSC)** for testing.
3. Lower refresh rate to 60Hz temporarily to stabilize the link.
4. If the link works at DP 1.2/60Hz but not 1.4/144Hz, the cable or port cannot sustain the bandwidth — upgrade the cable.

### Fix 6: Fix MST daisy-chain setups

Daisy-chaining has strict ordering and settings requirements.

1. Connect laptop → Monitor 1 (DP in), Monitor 1 (DP out) → Monitor 2.
2. In Monitor 1's OSD, enable **MST / DisplayPort 1.2 MST / Daisy Chain**.
3. Keep total bandwidth within one DP link (e.g., two 1080p or 1440p monitors; dual 4K needs DSC or two cables).
4. Test each monitor directly on the laptop first to prove both panels work solo.

### Fix 7: Check firmware and alternate ports

Last isolation steps before suspecting the GPU port hardware.

1. Update the monitor's firmware if the maker offers it (fixes many DP handshake bugs).
2. Try a different DisplayPort output on the GPU/dock, and a different DP input on the monitor.
3. On USB-C/Thunderbolt docks, verify the dock's DP alt-mode support and update dock firmware.
4. Microsoft's official display troubleshooting guidance covers multi-monitor enumeration if the OS side still fails.

## Closing

DisplayPort 'no signal' is a handshake problem, and handshakes fail at the weakest link: usually the cable, sometimes the driver, occasionally the monitor's input or MST settings. The certified-cable test in Fix 2 is the highest-value step — it converts guessing into knowing — and the driver reinstall in Fix 4 covers the software side completely.
