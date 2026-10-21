---
title: "NPU Not Showing in DxDiag? How to Fix It"
slug: npu-not-showing-in-dxdiag
date: 2026-10-21
categories: ["ai-pc"]
tags: ["npu not showing", "dxdiag", "npu missing", "device manager", "ai pc", "troubleshooting"]
description: "NPU missing from your DxDiag report? Learn why the neural processor disappears from the DirectX diagnostic tool and bring it back with six step-by-step fixes."
thumbnail: "/images/thumbs/npu-not-showing-in-dxdiag.webp"
faqs:
  - q: "Why doesn't my NPU appear in DxDiag?"
    a: >
      DxDiag doesn't probe the chip directly — it reports what the installed NPU driver tells Windows. If the driver failed to load, the device is misidentified, or your Windows build predates NPU reporting in DxDiag, the tool has nothing to display. The hardware is almost always fine.
  - q: "Is DxDiag required for NPU features to work?"
    a: >
      No. DxDiag is a reporting tool, not a dependency. Studio Effects, live captions, and Recall can run perfectly while DxDiag shows nothing. Test an actual AI feature before worrying — a working feature means the NPU is alive even if DxDiag disagrees.
  - q: "My NPU is missing from Device Manager too. Is the fix the same?"
    a: >
      Usually, yes — the same root cause hides it from both tools. When Device Manager shows the chip as an unknown device rather than a proper NPU, compare notes with the [unknown-device guide](/articles/npu-unknown-device-in-device-manager/) after working through the driver fixes below.
  - q: "Should I reinstall Windows to fix this?"
    a: >
      Almost never. A missing DxDiag entry is a driver or enumeration problem, not an operating-system problem. The six fixes below resolve it in nearly every case without touching your files, apps, or settings.
---

Running dxdiag and finding no mention of your NPU feels wrong on a laptop sold as an AI PC. The DirectX Diagnostic Tool is supposed to inventory exactly that kind of hardware — the chip behind Windows Studio Effects, live captions, and Recall — so when the NPU line is blank or missing entirely, it is natural to wonder whether the chip is broken.

Almost always the chip is fine: DxDiag doesn't probe hardware directly, it reports what the installed drivers and Windows' device database tell it. If the NPU driver failed to load, the device is misidentified, or your Windows build predates NPU reporting in DxDiag, the tool has nothing to show — a reporting gap, not a hardware gap. The same root cause usually explains why [the NPU shows up as an unknown device in Device Manager](/articles/npu-unknown-device-in-device-manager/).

This guide walks through six fixes in technician order: verify the hardware is present, repair the driver layer, then fix DxDiag itself. Recheck DxDiag after each fix so you know which step solved it.

## Why this happens

- **DxDiag reads from the driver, not the silicon:** DxDiag queries the loaded NPU driver for name, vendor, and capabilities. If no driver is loaded — uninstalled, failed, or disabled — DxDiag has no data source and the NPU entry stays blank.
- **The NPU is misidentified as an unknown device:** When Windows cannot match the chip to a driver, Device Manager parks it under "Other devices." DxDiag cannot interpret an unidentified device, so the NPU vanishes from its report too.
- **Your Windows build predates DxDiag's NPU support:** DxDiag only started reporting NPU details on recent Windows 11 builds. On 23H2 or an early 24H2 install, the tool has no field for a neural processor.
- **The NPU is disabled in BIOS/UEFI:** Some laptops ship with the NPU or "AI Boost" toggle switched off. Disabled hardware is never enumerated at boot, so neither Device Manager nor DxDiag ever sees it.
- **A stale DxDiag scan or saved log:** If you ran DxDiag before the NPU driver was installed, the saved log — and sometimes the in-memory scan — keeps showing the old picture until you run a fresh scan.
- **Corrupt plumbing behind DxDiag:** DxDiag leans on DirectX and WMI components. Damaged system files can make it skip or misread whole device classes, NPUs included.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU actually exists in Device Manager

Before touching DxDiag, establish the ground truth. If Device Manager sees the NPU under "Neural processors," the hardware is enumerated and this is purely a reporting problem. If Device Manager doesn't see it either, you have a driver or firmware issue to fix first — and the steps below cover that.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Neural processors** (on some systems it appears under System devices).
3. If the NPU is listed without a warning, note its exact name for later. If it sits under "Other devices" as unknown, keep reading: the driver fixes below resolve both problems at once.
4. Features like [live captions](/articles/live-captions-overlap-fullscreen-apps/) and [Recall](/articles/recall-duplicate-snapshots-issue/) need the same driver stack, so fixing one usually fixes the others.

### Fix 2: Enable the NPU in BIOS/UEFI

A surprising number of "missing NPU" cases end here: if the firmware toggle is off, no driver work will help because Windows never sees the chip.

1. Restart and enter the BIOS/UEFI (usually **F2**, **Del**, or **Esc** at the logo screen).
2. Under Advanced, CPU, or AI settings, find **NPU**, **AI Boost**, or **Neural Processor**.
3. Set it to **Enabled** (not Auto, on some boards), save, and exit.
4. Boot into Windows, open Device Manager, and confirm the NPU now appears — then re-run DxDiag.

### Fix 3: Update Windows to the current build

DxDiag's NPU reporting lives in the Windows build itself. An outdated build cannot display what it doesn't know about, and may also carry the older driver that caused the gap.

1. Open **Settings > Windows Update** and install every pending update.
2. Check **Advanced options > Optional updates** — NPU drivers often hide there.
3. Restart, press **Win + R**, type **winver**, and confirm a current Windows 11 build.
4. Run DxDiag again; on many systems the NPU appears right after the update with no further work.

### Fix 4: Reinstall the NPU driver with a true purge

A half-installed or mismatched driver leaves the NPU present but unreadable. Uninstalling with driver files deleted forces Windows to load a clean copy instead of the same broken package from its cache.

1. In Device Manager, right-click the NPU, choose **Uninstall device**, and check **"Attempt to remove the driver for this device"**.
2. Restart — the cleanup finishes during boot, so do not skip it.
3. Install a fresh driver: your laptop maker's support page first, or use [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Core Ultra systems.
4. Restart once more and re-run DxDiag.

### Fix 5: Run a fresh DxDiag scan as administrator

Once the driver layer is healthy, make sure DxDiag is producing a new scan rather than echoing stale data. An elevated fresh run forces a full re-query of every device.

1. Close every DxDiag window and any saved dxdiag logs.
2. Press **Win + S**, type **dxdiag**, right-click it, and choose **Run as administrator**.
3. Let the progress bar complete — do not click through the tabs until it finishes.
4. Click **Save All Information** and search the saved text file for your NPU name; the file is the authoritative result, not the tab display. Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows) documents this workflow officially.

### Fix 6: Repair the system files DxDiag depends on

If the driver is fine and a fresh scan still shows nothing, the fault is in DxDiag's own plumbing — corrupt WMI or DirectX components that make the tool skip the NPU class.

1. Open an elevated terminal (**Win + X > Terminal (Admin)**) and run `sfc /scannow`.
2. When it finishes, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for 100%.
3. Restart and run DxDiag one final time.
4. If the NPU appears now, you were dealing with system corruption all along — a failed update is the usual suspect.

## Closing

An NPU missing from DxDiag is a reporting problem far more often than a hardware one: a disabled firmware toggle, an outdated Windows build, or a driver that never loaded. Work the list in order — Device Manager, firmware, Windows, driver, DxDiag — and the entry comes back. Remember the practical test: if Studio Effects and live captions work, your NPU is alive no matter what DxDiag claims.
