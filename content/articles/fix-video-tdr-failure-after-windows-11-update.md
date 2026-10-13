---
title: "Fix VIDEO_TDR_FAILURE After a Windows 11 Update"
slug: fix-video-tdr-failure-after-windows-11-update
date: 2026-10-11
categories: ["windows-errors"]
tags: ["video-tdr", "gpu-driver", "windows-update"]
description: "VIDEO_TDR_FAILURE blue screen after updating Windows 11? Fix the GPU timeout: clean driver reinstall, TDR tweaks, and rolling back the bad update."
thumbnail: "/images/thumbs/fix-video-tdr-failure-after-windows-11-update.webp"
faqs:
  - q: "What is VIDEO_TDR_FAILURE?"
    a: "TDR stands for Timeout Detection and Recovery. Windows gives the GPU two seconds to respond; if the graphics driver hangs longer, Windows tries to reset the GPU. When the reset fails, you get the VIDEO_TDR_FAILURE blue screen, usually naming the GPU driver file like nvlddmkm.sys or amdkmdag.sys."
  - q: "Why did a Windows update cause VIDEO_TDR_FAILURE?"
    a: "Updates can install an incompatible graphics driver automatically, change power management behavior the GPU driver relied on, or introduce stricter timeout enforcement. The update didn't break your GPU — it broke the driver/GPU coordination, which is fixable in software."
  - q: "Is VIDEO_TDR_FAILURE a sign my GPU is dying?"
    a: "Usually not, especially when it starts right after an update — that's a software signature. A dying GPU causes TDR failures too, but with a different pattern: artifacts, crashes under any driver version, and failures in Safe Mode or during basic desktop use, not just under load."
  - q: "Should I increase the TDR delay in the registry?"
    a: "It can help as a workaround for marginal cases — raising TdrDelay gives a slow GPU more time before Windows declares a timeout. But it's a bandage: fix the driver first. Only tweak TDR registry values after a clean driver install has failed, and document the change so you can undo it."
---
VIDEO_TDR_FAILURE after a Windows 11 update is one of the clearest cause-and-effect blue screens in Windows: the update changed something in the graphics stack, the GPU driver started hanging, Windows' timeout watchdog fired, and the recovery failed. The screen usually names the driver — `nvlddmkm.sys` for NVIDIA, `amdkmdag.sys` for AMD, `igdkmd64.sys` for Intel — which is both the diagnosis and the to-do list.

Because the trigger was an update, the fix path has two prongs: repair the driver situation the update created, and deal with the update itself if needed. Work both prongs in the order below.

## Why this happens

- **Windows Update installed a bad or mismatched graphics driver** over your working one.
- **The update changed GPU power management** behavior that the old driver depended on.
- **Stricter TDR timeout enforcement** in the new build exposing a driver that was already marginal.
- **Corrupted driver files** from the update process itself.
- **Conflicting integrated + discrete GPU drivers** after the update touched only one of them.
- **Overheating or dust** — the update is coincidental, and the GPU was already on the edge.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Confirm the driver and the update timeline

Establish the link before treating it.

1. Open **Settings** → **Windows Update** → **Update history** and note the date of the latest update versus when crashes began.
2. Install **WinDbg Preview**, open the latest dump in `C:\Windows\Minidump`, run `!analyze -v`, and confirm the named driver is graphics-related.
3. In **Device Manager**, check the display adapter's **Driver** tab for the driver date — a date matching the update confirms Windows Update replaced it.
4. If the timeline doesn't match any update, suspect thermals or hardware instead and jump to Fix 6.

### Fix 2: Clean-reinstall the graphics driver (DDU method)

The core fix — remove what the update installed, install what works.

1. Download the last known-good driver version (or the latest stable) from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
2. Boot into [Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/), run Display Driver Uninstaller (DDU), and wipe the graphics driver completely.
3. Restart normally and install the downloaded driver. Choose **Custom** → **Clean installation** in the NVIDIA/AMD installer for good measure.
4. Test with the workload that crashed — if it's stable for several days, the driver was the whole story.

### Fix 3: Roll back or pause the Windows update

If the driver is fine but the update's other changes broke TDR behavior, address the update.

1. Go to **Settings** → **Windows Update** → **Update history** → **Uninstall updates** and remove the most recent cumulative update.
2. Restart and test for a few days. Stable? The update was the trigger.
3. **Pause updates** for 2–3 weeks to avoid immediate reinstallation while Microsoft ships fixes.
4. Before unpausing, update the GPU driver to the newest stable — the combination of fixed update + fresh driver usually holds.

### Fix 4: Stop Windows Update from replacing your driver

Windows Update will happily reinstall the bad driver the moment you look away.

1. After your clean driver install, open **System Properties** (`sysdm.cpl`) → **Hardware** → **Device Installation Settings** → **No**.
2. In **Settings** → **Windows Update** → **Advanced options** → **Optional updates**, uncheck any offered graphics drivers.
3. Note your working driver version (**Device Manager** → display adapter → **Driver** tab) so you can spot silent replacements.
4. Re-enable driver updates after a month or two — permanent blocks leave security-relevant driver fixes undelivered.

Driver-update fights like this are also behind many [driver power state failures](/articles/driver-power-state-failure-windows-11-fix/) — same prevention steps apply.

### Fix 5: Adjust TDR behavior (targeted workaround)

When the driver is the best available but still trips timeouts, give the GPU more slack.

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a DWORD (32-bit) named **TdrDelay** and set it to **8** (seconds, up from the default 2).
3. Optionally create **TdrDdiDelay** set to **10** as well.
4. Restart and test. If crashes stop, the GPU was just slow to respond, not broken — but keep this as a workaround while watching for a better driver, and document the change.

### Fix 6: Rule out heat and hardware

Updates make convenient scapegoats; verify the GPU is actually healthy.

1. Monitor GPU temperatures under load — sustained temps above 85–90°C on a laptop GPU invite TDR timeouts.
2. Clean vents with compressed air and ensure the laptop sits on a hard surface during heavy use.
3. Run a GPU stress test (FurMark, 20 minutes) on the clean driver — artifacts or crashes here suggest hardware, not the update.
4. If TDR failures happen in Safe Mode or on the basic display driver, that's a hardware red flag — software TDR issues don't occur without the real driver loaded.

### Fix 7: Repair system files and the update components

A damaged update can leave the graphics stack half-migrated.

1. In **Terminal (Admin)**, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Reset Windows Update components:
   `net stop wuauserv` → `net stop bits` → `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` → `net start wuauserv` → `net start bits`
3. Reinstall the latest cumulative update fresh from **Settings** → **Windows Update**.
4. Re-verify your graphics driver version afterward — updates love to "help" with drivers.

### Fix 8: In-place repair install for a corrupted graphics stack

When clean drivers and update surgery both fail, refresh the OS layer.

1. Back up your files.
2. Run setup from official Windows 11 media inside Windows, keeping files and apps.
3. Install the known-good GPU driver before Windows Update runs.
4. Block driver replacement (Fix 4) until you've confirmed a week of stability.

## Closing

VIDEO_TDR_FAILURE after an update is Windows telling you exactly what happened: the update disturbed the graphics driver, the driver hung, the watchdog fired. Clean out the driver with DDU, handle the update (roll back or update past it), and stop Windows from reinstalling the bad driver behind your back. It's a software problem with a software fix — no new GPU required. And next time an update lands, check the GPU driver version afterward; thirty seconds of verification beats a week of blue screens.
