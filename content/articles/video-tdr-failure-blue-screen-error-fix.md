---
title: "VIDEO_TDR_FAILURE Blue Screen on Windows 11? Here's How to Fix It"
slug: video-tdr-failure-blue-screen-error-fix
date: 2026-09-17
categories: ["windows-errors"]
tags: ["video tdr failure", "blue screen", "gpu driver", "windows 11", "nvlddmkm.sys"]
description: "VIDEO_TDR_FAILURE means your graphics driver stopped responding and Windows couldn't recover it. Here's how to fix the crash with driver, GPU, and hardware checks."
thumbnail: "/images/thumbs/video-tdr-failure-blue-screen-error-fix.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout, Detection, and Recovery — Windows' mechanism for resetting a graphics driver that stops responding. When the GPU hangs for more than about two seconds and the reset also fails, Windows crashes with VIDEO_TDR_FAILURE (stop code 0x116). The faulty file named on the screen, such as nvlddmkm.sys or atikmpag.sys, identifies which driver was involved."
  - q: "Is VIDEO_TDR_FAILURE a hardware problem or a driver problem?"
    a: "Most often it's a driver problem — corrupt, outdated, or conflicting graphics drivers cause the majority of cases. But it can also signal an overheating GPU, an underpowered or failing power supply, a loose card, or a dying graphics chip. The diagnostic order matters: rule out drivers first because they're free to fix, then investigate heat and power."
  - q: "Can overclocking cause VIDEO_TDR_FAILURE?"
    a: "Yes, absolutely. Overclocked GPUs — even mild factory overclocks — are a classic trigger. If you overclocked the card yourself, revert to stock clocks first. Even on a card you never touched, try slightly underclocking the core by 50–100 MHz in MSI Afterburner; if the crashes stop, the card was marginal at its stock settings."
  - q: "Why does VIDEO_TDR_FAILURE happen mostly while gaming?"
    a: "Games push the GPU to sustained full load, which exposes three things at once: driver bugs in the rendering path, heat buildup from inadequate cooling, and power delivery weakness under load. A system that's stable on the desktop but crashes in games is telling you the GPU subsystem can't sustain full load — start with temperatures and drivers."
---

Of all the blue screens Windows can throw at you, VIDEO_TDR_FAILURE is one of the most specific — and that's good news. The stop code 0x116 tells you exactly which subsystem failed: your graphics driver stopped responding, Windows tried its Timeout Detection and Recovery mechanism to reset it, and the reset failed. The screen usually names the culprit file too — `nvlddmkm.sys` for NVIDIA, `atikmpag.sys` for AMD, `igdkmd64.sys` for Intel.

That specificity makes this one of the more fixable blue screens. The overwhelming majority of cases trace back to the graphics driver: a corrupt install, a buggy new release, or a conflict between the integrated and discrete GPUs fighting over the display. A smaller share are hardware — an overheating GPU, dust-choked fans, a power supply that can't sustain load, or a card that's simply dying. The fixes below work in that order, because driver fixes are free and take minutes, while hardware conclusions should only come after software is ruled out.

## Why this happens

- **Corrupt or outdated graphics driver**: The single most common cause. Driver files get damaged by failed updates, antivirus interference, or disk errors, and the GPU starts hanging.
- **Buggy new driver release**: Sometimes the update itself is the problem — a fresh GPU driver with a regression can start TDR crashes on hardware that was previously stable.
- **Overheating GPU**: When the graphics chip runs too hot, it becomes unstable and stops responding to the driver. Dust, dried thermal paste, and blocked vents are the usual culprits on laptops.
- **Overclocking instability**: Core or memory clocks pushed beyond what the silicon tolerates cause exactly this kind of hang under load.
- **Insufficient or unstable power delivery**: A weak charger, a failing power brick, or a degraded battery on a laptop can starve the GPU during load spikes.
- **Conflicting integrated and discrete GPUs**: Laptops with both Intel/AMD integrated graphics and an NVIDIA/AMD discrete GPU can crash when the handoff between them misbehaves.
- **Failing graphics hardware**: A dying GPU or failing VRAM produces TDR crashes that no driver reinstall will fix — but this is the diagnosis of last resort.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the failing file and boot into Safe Mode

The filename on the blue screen is your first diagnostic clue.

1. The next time the blue screen appears, note the file named near the bottom — `nvlddmkm.sys` (NVIDIA), `atikmpag.sys` (AMD), or `igdkmd64.sys` (Intel).
2. Boot into Safe Mode: hold **Shift** while clicking **Restart** (or force WinRE with three interrupted boots), then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
3. Safe Mode loads only the basic display driver. If the system is stable here, the full GPU driver is confirmed as the problem area — proceed to Fix 2. Our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers alternate ways in if Shift+Restart doesn't work.

### Fix 2: Clean-reinstall the graphics driver with DDU

A standard driver reinstall often leaves the corrupt files in place. A truly clean install is the fix that resolves most TDR crashes.

1. Download Display Driver Uninstaller (DDU) and the latest driver for your GPU — [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
2. Boot into Safe Mode (Fix 1), run DDU, and choose **Clean and restart** for your GPU brand.
3. After reboot, install the freshly downloaded driver — choose **Custom/Advanced** install and tick **Clean installation** if the option exists.
4. Test with your normal workload. If crashes persist, try one driver version older than the latest — regressions in new releases are real.

### Fix 3: Roll back a recent driver update

If the crashes started right after a driver update, the update is the suspect, not the solution.

1. Open **Device Manager** (**Windows + X** > **Device Manager**).
2. Expand **Display adapters**, right-click your GPU, and choose **Properties** > **Driver** tab.
3. Click **Roll Back Driver** if it's available, select a reason, and confirm.
4. If the button is greyed out, use DDU (Fix 2) to remove the current driver and manually install the previous version you know was stable.

### Fix 4: Check GPU temperatures and clean the cooling

Heat-induced TDR crashes follow a pattern: fine on the desktop, crashing under load, worse in warm rooms.

1. Install HWMonitor or HWiNFO and watch GPU temperature during a game or stress test. Sustained temperatures above 85–90°C on a laptop GPU are a red flag.
2. Power off, unplug, and clean the vents and fans with compressed air — hold the fan blades still so they don't spin freely.
3. On laptops, make sure you're gaming on a hard flat surface, not a bed or couch that blocks the intakes. A cooling pad helps measurably.
4. If the laptop is several years old and temps stay high after cleaning, the thermal paste has likely dried out — a repaste by a repair shop usually drops temperatures 10–20°C.

### Fix 5: Disable overclocks and test at stock settings

Overclocking — including aggressive factory overclocks — is a classic TDR trigger.

1. If you use MSI Afterburner or similar, reset everything to defaults and test.
2. Even without manual overclocking, try a mild **underclock**: reduce the core clock by 50–100 MHz. If crashes stop, your card's stock settings were marginal.
3. In NVIDIA Control Panel or AMD Software, set **Power management mode** to **Prefer maximum performance** — counterintuitively, aggressive power-saving clock switching can itself cause TDR hangs on some cards.

### Fix 6: Adjust the TDR timeout and disable hardware acceleration

Giving Windows more patience before declaring the GPU dead can stop borderline crashes.

1. Press **Windows + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a new **DWORD (32-bit)** value named `TdrDelay` and set it to `10` (decimal) — this gives the GPU ten seconds to recover instead of two.
3. Optionally add `TdrDdiDelay` set to `20` as well. Restart afterwards.
4. Separately, disable hardware acceleration in your browser and Discord — these keep the GPU lightly loaded in ways that can trigger TDR on unstable drivers.

### Fix 7: Rule out power and memory issues

If driver and heat fixes haven't helped, widen the investigation.

1. On a laptop, test with the original charger plugged in — underpowered third-party chargers cause GPU crashes under load. If the battery is badly degraded, test with it removed (if removable) or check our battery health guide for diagnostics.
2. Run Windows Memory Diagnostic (**Windows + R** > `mdsched.exe`) — faulty system RAM can masquerade as GPU crashes.
3. For deeper confirmation, run a GPU stress test like FurMark for 15 minutes: artifacts or a crash under synthetic load point firmly at the GPU hardware. Compare against our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) if other stop codes appear too.

### Fix 8: Test the hardware and consider replacement

When software is exhausted, it's time to confirm hardware failure.

1. If you have access to another GPU (desktop) or can test the laptop with the discrete GPU disabled in Device Manager (forcing integrated graphics), do so — stability on integrated graphics implicates the discrete chip.
2. Update the motherboard BIOS from your manufacturer's support page — Dell, HP, or Lenovo — since BIOS updates sometimes fix GPU power management bugs.
3. If the GPU is confirmed failing and the laptop is under warranty, contact the manufacturer. Out of warranty, a motherboard/GPU replacement on a laptop is often uneconomical — weigh repair cost against a new machine.

## Closing

VIDEO_TDR_FAILURE looks alarming but it's one of the most diagnosable blue screens you can get: the named driver file points you straight at the graphics subsystem, and a clean driver reinstall with DDU resolves the majority of cases without spending a cent. Work the list in order — drivers, then heat, then power — and resist the urge to declare the GPU dead until software causes are genuinely exhausted. Persistent crashes across multiple clean driver versions plus high temperatures, though, is the hardware telling you the truth. For crashes that name other system files instead, our [driver-focused blue screen guide](/articles/driver-power-state-failure-windows-11-fix/) covers the next most common driver-related stop codes.
