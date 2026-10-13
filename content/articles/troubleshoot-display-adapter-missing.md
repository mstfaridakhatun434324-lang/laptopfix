---
title: "Troubleshoot a Missing Display Adapter: Find Your Vanished GPU"
slug: troubleshoot-display-adapter-missing
date: 2026-10-11
categories: ["drivers"]
tags: ["display adapter troubleshooting", "gpu missing", "code 43", "nvidia not detected", "device manager"]
description: "Troubleshoot a missing display adapter step by step: decode error codes, clean-install GPU drivers, check BIOS, and prove hardware vs software."
thumbnail: "/images/thumbs/troubleshoot-display-adapter-missing.webp"
faqs:
  - q: "What does Code 43 mean on a display adapter?"
    a: "Code 43 means Windows stopped the device because it reported problems — the GPU driver crashed during initialization or the hardware signaled a fault. It's the most common error on a misbehaving display adapter. Start with a clean driver reinstall using DDU in Safe Mode. If Code 43 survives a clean driver, test the GPU in another OS or machine to separate driver issues from hardware failure."
  - q: "Why does my GPU show up as Microsoft Basic Display Adapter?"
    a: "That means Windows sees the GPU hardware but has no functional driver bound to it, so it fell back to the generic basic driver. The hardware is detected — which is good news — and the fix is installing the proper driver from NVIDIA, AMD, or Intel. If the proper driver won't install or bind, the existing driver store is likely corrupted and needs a DDU cleanup."
  - q: "How do I troubleshoot a GPU that vanishes intermittently?"
    a: "Intermittent disappearance points at power delivery, heat, or a loose connection rather than drivers — drivers tend to fail consistently. Note when it vanishes: under load suggests heat or power; after sleep suggests firmware power-state bugs; randomly suggests a seating or power-connector issue. Check temperatures, reseat power connections, and update the BIOS."
  - q: "Should I use DDU for a missing display adapter?"
    a: "Yes, when standard reinstalls fail. Display Driver Uninstaller in Safe Mode removes every trace of GPU drivers — registry entries, folders, and services — that a normal uninstall leaves behind. Those remnants are exactly what prevent a fresh driver from binding correctly. It's the standard escalation when Device Manager uninstalls don't restore the adapter."
---

A missing display adapter needs real troubleshooting, not tip-collecting — because "the GPU is gone" has at least six distinct causes, and the fix for a Code 43 is different from the fix for a BIOS-disabled GPU, which is different from the fix for a card that Windows sees but can't bind a driver to. This guide is a diagnostic decision tree: each fix extracts a piece of evidence, and the evidence routes you to the answer. You'll end knowing whether it's the driver, the firmware, or the silicon.

The single most informative step is Fix 1 — the hidden-devices check with error codes. Everything branches from what you find there.

## Why this happens

- **Driver failed to bind (Code 31/43).** Corrupted driver store preventing the GPU driver from loading.
- **Device disabled.** In Device Manager, BIOS, or by manufacturer software.
- **Failed driver update.** Interrupted or incompatible installer leaving the adapter in limbo.
- **GPU power-state failure.** Firmware not powering the discrete GPU correctly.
- **Hardware not seated/powered.** Loose card or auxiliary power (desktops mostly).
- **Dead GPU silicon.** Rare — proven only by elimination.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Extract the evidence from Device Manager

The diagnostic foundation — do this first, carefully.

1. **Device Manager > View > Show hidden devices** → expand **Display adapters**.
2. Record exactly what you see: nothing at all, a grayed-out GPU, a GPU with yellow warning, or **Microsoft Basic Display Adapter**.
3. For warnings, open **Properties > General** and record the **error code**: Code 43 (device reported problems), Code 31 (driver failed), Code 45 (disconnected), Code 10 (failed to start).
4. Check **Events** tab for the driver's load history — timestamps of failures correlate with updates.
5. Also check **Other devices** for unbound "Video Controller" entries — hardware seen, driver missing.

The hidden-device technique in full: [how to enable hidden devices in Device Manager](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/). The companion recovery guide is [what to do if the display adapter is missing](/articles/what-to-do-if-display-adapter-missing/).

### Fix 2: Clean-install the GPU driver with DDU

The definitive driver-layer fix.

1. Download **Display Driver Uninstaller (DDU)** and the correct driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker (Intel iGPU).
2. Boot into **Safe Mode** (Settings > Recovery > Advanced startup).
3. Run DDU, select the GPU brand, choose **Clean and restart** — this removes all driver remnants.
4. After reboot, install the downloaded driver with **Custom > Clean installation**.
5. Verify in Device Manager: proper GPU name, no warnings, correct driver date on the Driver tab.

### Fix 3: Decode and address the specific error code

Targeted fixes per code.

1. **Code 43**: clean driver install (Fix 2) first; if it persists, full power drain (shutdown, unplug, hold power 30s) — Code 43 latches until power-cycled; if still persistent, suspect hardware.
2. **Code 31**: the driver binary is corrupt or mismatched — DDU cleanup plus the correct driver version fixes it.
3. **Code 45**: Windows thinks the hardware is disconnected — check BIOS enablement (Fix 4) and physical seating/power.
4. **Code 10**: device failed to start — try an older driver version; the newest isn't always the most compatible.
5. **Microsoft Basic Display Adapter**: hardware detected, driver unbound — install the proper driver; if it won't bind, DDU first.

### Fix 4: Check firmware-level GPU controls

BIOS and vendor software can hide the GPU.

1. Enter **BIOS/UEFI** → graphics settings → ensure the discrete GPU / switchable graphics is **enabled** (not iGPU-only).
2. **Load optimized defaults** to clear corrupted firmware GPU configuration.
3. Check manufacturer apps (Vantage, MyASUS, OMEN Hub) for **GPU modes** — eco/iGPU-only modes hide the discrete GPU from Windows.
4. Update the **BIOS** — GPU power-sequencing fixes appear in changelogs.
5. Note whether the BIOS hardware inventory lists the GPU — absent in BIOS plus absent in OS means hardware until proven otherwise.

### Fix 5: Investigate power and thermals

For intermittent disappearance.

1. Correlate disappearances: **under load** → heat or power delivery; **after sleep** → firmware power states; **random** → seating/power connectors.
2. Monitor GPU temperatures — a GPU that vanishes at high temps may be thermally protecting itself; clean cooling (see the fan-fix method in [the best way to fix a laptop fan not working](/articles/best-way-to-fix-laptop-fan-not-working/)).
3. Test on **AC power** with the battery charged — some firmware hides the discrete GPU on low battery.
4. Desktops: reseat the card and verify **auxiliary PCIe power connectors** are firmly attached.
5. Laptops: a full power drain resets GPU power sequencing — worth trying for sleep-related vanishes.

### Fix 6: Isolate with an independent OS

The definitive software-versus-hardware test.

1. Boot a **Linux live USB** → terminal → `lspci | grep -i vga` → note whether the GPU appears.
2. **Appears in Linux, missing in Windows** → Windows driver/OS problem. Consider an in-place Windows repair install.
3. **Missing in both** → hardware or firmware — recheck BIOS (Fix 4), then accept the hardware verdict.
4. For dual-GPU laptops, check whether the **integrated GPU** is also affected — both missing suggests chipset/platform issue, not the discrete GPU alone.
5. Document your findings — a repair shop or warranty claim goes faster with "absent in Linux and Windows, BIOS shows no GPU" than with "it's broken."

### Fix 7: The hardware verdict and workarounds

When evidence points at silicon.

1. **Under warranty** → file a claim with your diagnostic notes — laptop GPU failure is a motherboard replacement, a warranty job.
2. Out of warranty → professional diagnosis before assuming the worst; GPU power circuits are sometimes repairable.
3. **Integrated graphics** keep the laptop fully usable for non-3D work — the machine isn't dead, just less capable.
4. **Thunderbolt eGPU** enclosures can replace a dead internal discrete GPU where supported.
5. Back up data now — platform-level hardware faults occasionally cascade to storage.

## Closing

Missing-GPU troubleshooting is evidence work: the hidden-devices view and the error code tell you which of the six causes you're facing, DDU in Safe Mode settles the driver question definitively, and the Linux live-USB test delivers the final hardware verdict. Most cases end at the driver — a corrupted driver store that a normal uninstall can't clear, which is exactly what DDU exists for. Collect the evidence in order, and the answer presents itself; skip the diagnosis, and you'll reinstall drivers for a BIOS toggle.
