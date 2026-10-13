---
title: "Fix DWM.exe High GPU Usage After a Windows 11 Update"
slug: how-to-fix-high-gpu-usage-dwm-exe-after-windows-11-update
date: 2026-09-29
categories: ["performance"]
tags: ["dwm.exe", "high gpu", "windows 11 update", "desktop window manager", "gpu drivers"]
description: "dwm.exe GPU usage spiked after a Windows 11 update? Roll back drivers, fix the update damage, and calm the compositor step by step."
thumbnail: "/images/thumbs/how-to-fix-high-gpu-usage-dwm-exe-after-windows-11-update.webp"
faqs:
  - q: "Why did a Windows update cause dwm.exe high GPU usage?"
    a: "Windows updates — especially feature updates like 24H2 — commonly replace your GPU driver with a generic Microsoft version, reset display settings (refresh rate, HDR), and disturb the compositor's cached state. The Microsoft-provided GPU driver is the prime suspect: it's often months older than the manufacturer's and lacks DWM-specific optimizations. The update can also re-enable transparency effects you'd disabled and change GPU scheduling settings."
  - q: "Should I roll back the GPU driver after a Windows update?"
    a: "Yes, if the high DWM GPU started immediately after the update — that's the strongest signal the update swapped your driver. Device Manager > Display adapters > your GPU > Properties > Driver tab > Roll Back Driver Windows Update from replacing it again (Settings > Windows Update > Advanced options > turn off driver updates, or the Group Policy equivalent) until you've manually installed a current driver from Intel, NVIDIA, or AMD."
  - q: "How do I stop Windows Update from replacing my GPU driver?"
    a: "On Pro: gpedit.msc > Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update > enable 'Do not include drivers with Windows Updates'. On Home: the same setting exists via registry (create DWORD ExcludeWUDriversInQualityUpdate = 1 under HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate). Then update GPU drivers manually from the manufacturer — you stay current without surprise downgrades."
  - q: "How long should I wait before troubleshooting post-update DWM spikes?"
    a: "Give it one full day of normal use. Post-update, Windows runs background maintenance (indexing, Store updates, Defender scans) that can inflate GPU-adjacent numbers, and the compositor rebuilds its caches. If dwm.exe GPU is still abnormally high after 24–48 hours with no maintenance running — check Task Manager's Processes sorted by GPU to confirm nothing else is active — it's a real regression, not settling-in, and the driver rollback below is the fix."
---

**dwm.exe** GPU usage jumping from negligible to 20–40% right after a Windows 11 update is one of the most clearly update-caused performance regressions there is — the timing tells the whole story. Desktop Window Manager didn't change; what changed is everything around it: the update swapped your GPU driver for Microsoft's generic version, reset display settings, and left the compositor's state scrambled. The fix is correspondingly update-focused: undo what the update did to your graphics stack.

This guide is specifically for the "it was fine yesterday, I installed the update, now DWM is hot" scenario — different from chronic DWM issues (see our brand guides for [Dell](/articles/how-to-fix-desktop-window-manager-high-gpu-on-dell-laptop/), [ASUS](/articles/how-to-fix-desktop-window-manager-high-gpu-on-asus-laptop/), and [Acer](/articles/how-to-fix-desktop-window-manager-high-gpu-on-acer-laptop/)). Work the steps in order; most people are fixed by step two. For other post-update resource hogs, see [SysMain high disk usage](/articles/how-to-fix-sysmain-high-disk-usage-after-windows-11-update/).

## Why this happens

- **Driver replaced by Windows Update**: The update installed Microsoft's generic GPU driver over the manufacturer's optimized one.
- **Display settings reset**: Refresh rate, HDR, and GPU scheduling settings reverted to defaults.
- **Compositor state corruption**: The update left DWM's cached composition state inconsistent.
- **Transparency/effects re-enabled**: Update reset personalization settings you'd turned off.
- **Background maintenance inflating numbers**: Post-update indexing and Store updates competing for GPU-adjacent resources.
- **Multi-monitor config disturbed**: Update changed display topology handling or scaling.
- **HDR re-enabled**: Updates sometimes re-enable HDR on capable displays, multiplying composition cost.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the update/driver swap

Establish the causal chain before rolling anything back.

1. **Settings** > **Windows Update** > **Update history** — note the date of the last feature or quality update and compare with when DWM GPU spiked.
2. **Device Manager** > **Display adapters** > your GPU > **Properties** > **Driver** tab — check the **Driver Date**. If it's dated to the update day and the provider is Microsoft (not Intel/NVIDIA/AMD), the update swapped your driver. Case closed.
3. **Task Manager** > **Performance** > **GPU** — confirm it's DWM (dwm.exe in Processes > GPU column), not a game or browser misattributed.
4. Check **Settings** > **System** > **Display** > **Advanced display** — verify refresh rate and HDR are what you had before; updates reset these.
5. If the driver date is old and the provider is Microsoft, skip straight to Fix 2 — you've found it.

### Fix 2: Roll back the GPU driver

The highest-yield fix for update-caused DWM spikes.

1. **Device Manager** > **Display adapters** > right-click your GPU > **Properties** > **Driver** tab > **Roll Back Driver** — select "driver update caused problems" as the reason.
2. Restart when prompted and measure DWM GPU in Task Manager — for most users this alone restores pre-update behavior.
3. If **Roll Back Driver** is greyed out, the update didn't keep the old driver — proceed to Fix 3 (manual install) instead.
4. After rollback, immediately do Fix 4 (block driver updates) or Windows will "helpfully" reinstall the generic driver.
5. Note which driver version worked — write it down for future troubleshooting.

### Fix 3: Clean-install the manufacturer's current driver

When rollback isn't available or you want the latest proper driver.

1. Download the current driver for your exact GPU: Intel via [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html), NVIDIA via [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), AMD via AMD's official driver download page — or your laptop maker's official support page.
2. Run the installer with **clean installation** checked (NVIDIA) or use **DDU** in Safe Mode first for a complete wipe if the update left driver state tangled.
3. Restart and verify in Device Manager that the provider is now Intel/NVIDIA/AMD with a recent date.
4. Measure DWM GPU at idle — manufacturer drivers include DWM composition optimizations the Microsoft generic lacks.
5. Keep the installer file — if a future update swaps the driver again, reinstalling takes two minutes.

### Fix 4: Stop Windows Update from swapping drivers again

Prevent the recurrence.

1. **Pro**: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Update** > **Manage updates offered from Windows Update** > enable **Do not include drivers with Windows Updates**.
2. **Home**: registry — create DWORD `ExcludeWUDriversInQualityUpdate` = `1` under `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` (create keys as needed; back up first).
3. Alternative lighter touch: **Settings** > **Windows Update** > **Advanced options** > turn off **Receive updates for other Microsoft products** — reduces but doesn't fully block driver updates.
4. Commit to updating GPU drivers manually every few months — you're now responsible for them.
5. This single policy prevents an entire class of post-update regressions, not just DWM's.

### Fix 5: Restore your display settings

Undo the update's settings reset.

1. **Settings** > **System** > **Display** > **Advanced display** — restore your refresh rate (if the update dropped your 144Hz panel to 60Hz, DWM behavior changes — but also check: sometimes the update raised it, increasing DWM load).
2. Toggle **HDR** back to your preference — if the update enabled HDR and your driver handles it poorly, that's a DWM spike source; turn it off.
3. **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** — verify **Hardware-accelerated GPU scheduling** and **Variable refresh rate** are as you had them.
4. **Settings** > **Accessibility** > **Visual effects** — re-disable **Transparency effects** and **Animation effects** if the update turned them back on.
5. Multi-monitor users: recheck arrangement, scaling, and per-display refresh rates — updates scramble these.

### Fix 6: Reset the compositor and clear its state

For scrambled DWM state the driver fix doesn't clear.

1. **Win + Ctrl + Shift + B** — resets the graphics driver live; if DWM GPU normalizes instantly, it was transient compositor state.
2. Restart (full restart, not Fast Startup hybrid — hold Shift while clicking Restart, or disable Fast Startup temporarily) to clear kernel graphics state.
3. Switch to a default Windows theme temporarily (**Settings** > **Personalization** > **Themes** > Windows default) — corrupted theme composition data occasionally survives updates.
4. Clear and rebuild icon/thumbnail caches (Settings > Storage > Temporary files > Thumbnails) — Explorer's rendering feeds DWM.
5. Re-measure after each step to identify which state was stuck.

### Fix 7: Repair the update damage system-wide

When the update broke more than the driver.

1. Elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` — updates occasionally corrupt system files DWM depends on.
2. Check **Settings** > **Windows Update** for failed or pending updates — a half-applied update leaves the graphics stack inconsistent; let it finish or troubleshoot it.
3. If a specific KB is the known culprit (check the update history date against DWM spike onset), you can uninstall it: **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — then pause updates while Microsoft fixes it.
4. Last resort: in-place upgrade repair from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — refreshes the entire OS while keeping files and apps.
5. Report it via **Feedback Hub** — update-caused driver regressions get fixed faster when reported with your hardware details. Microsoft's official support site has guided update troubleshooting.

## Closing

DWM.exe high GPU after a Windows 11 update is the update's fingerprints all over your graphics stack: a swapped driver, reset display settings, scrambled compositor state. Roll the driver back, block future driver swaps, restore your display settings, and the compositor goes back to its quiet, invisible self. Updates should improve your machine — when one doesn't, undoing its graphics changes is fast, safe, and usually the whole fix.
