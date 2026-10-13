---
title: "How to Enable Hardware-Accelerated GPU Scheduling"
slug: how-can-i-enable-hardware-accelerated-gpu-scheduling
date: 2026-09-17
categories: ["performance"]
tags: ["hardware accelerated gpu scheduling", "hags", "gpu performance", "windows 11"]
description: "Want to enable Hardware-Accelerated GPU Scheduling (HAGS) on Windows 11? Check requirements, turn it on, and know when it helps — and when to leave it off."
thumbnail: "/images/thumbs/how-can-i-enable-hardware-accelerated-gpu-scheduling.webp"
faqs:
  - q: "What does Hardware-Accelerated GPU Scheduling actually do?"
    a: "Normally the CPU-based Windows scheduler manages GPU work queues; HAGS lets the GPU's own dedicated scheduling processor take over that job. This reduces scheduling latency and CPU overhead, which can improve frame rates and reduce stutter in games by a few percent. The gains are modest on modern systems but real, particularly on machines where the CPU is the bottleneck during gaming."
  - q: "Does HAGS work on all graphics cards?"
    a: "No — you need a GPU with a hardware scheduler and a WDDM 2.7+ driver. That means NVIDIA GeForce 10 series and newer, AMD RX 5600/5700 series and newer (RDNA and later), or Intel integrated graphics from 11th-gen onwards with current drivers. Older cards simply won't show the toggle. Both the GPU hardware and an up-to-date driver must support it."
  - q: "Can HAGS cause problems or lower performance?"
    a: "Yes, occasionally. Some users report stuttering, driver crashes, or slightly lower performance with HAGS enabled, particularly with older drivers or certain game engines. It's also known to conflict with some recording and streaming software. That's why testing matters: enable it, benchmark your actual games, and keep it only if your numbers improve."
  - q: "Do I need to restart after enabling HAGS?"
    a: "Yes — Windows requires a full restart for the scheduling change to take effect. The Settings page tells you this explicitly. A fast-startup shutdown may not be enough on some systems; use Restart to be certain. After rebooting, the toggle should show as On, and you can verify it's active with GPU monitoring tools that report the scheduling mode."
---

Hardware-Accelerated GPU Scheduling (HAGS) is one of those Windows settings that sounds like free performance — let the GPU schedule its own work instead of making the CPU do it, and games get a little faster with a little less stutter. On the right hardware with current drivers, that's roughly true: expect single-digit percentage gains, not miracles. On the wrong setup, it can cause stutter or instability.

This guide shows you how to check whether your laptop supports it, how to enable it, and how to test whether it's actually helping you. For broader gaming and graphics smoothness, see our GPU scheduling deep-dive link target; for general speed, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) and [freeing up disk space](/articles/how-to-free-up-disk-space-on-windows-11/).

## Why this happens

- **GPU lacks a hardware scheduler**: Cards older than the supported generations physically can't do HAGS.
- **Outdated graphics driver**: The driver must be WDDM 2.7+ — old drivers hide the toggle entirely.
- **Windows version too old**: HAGS needs Windows 10 May 2020 update or later; it's mature on Windows 11.
- **OEM driver blocking the feature**: Some laptop vendor drivers lag behind and don't expose HAGS.
- **Conflicting virtualization or capture software**: Certain hypervisors and screen recorders conflict with the GPU scheduler.
- **HAGS enabled but causing stutter**: On some driver/game combinations the feature regresses performance.
- **Toggle missing after update**: Driver updates can reset the setting or the new driver may have dropped support reporting.
- **Integrated + discrete GPU confusion**: On laptops with switchable graphics, the setting applies to the active GPU path.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether your hardware supports HAGS

Don't hunt for a toggle your GPU can't provide.

1. Open **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** — look for the **Hardware-accelerated GPU scheduling** toggle. If it's there, your hardware qualifies.
2. No toggle? Check your GPU: **Task Manager** > **Performance** > **GPU** shows the model. You need NVIDIA GTX 10-series or newer, AMD RDNA (RX 5000+) or newer, or Intel 11th-gen+ integrated graphics.
3. Check your driver version in **Device Manager** > **Display adapters** > **Properties** > **Driver** — then verify against the vendor's site that it's a WDDM 2.7+ driver. Update if it's old: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html).
4. Confirm Windows is current: **Settings** > **Windows Update** — install pending updates.
5. If hardware qualifies but the toggle is missing after a driver update, the new driver may have a reporting bug — try the previous driver version.

### Fix 2: Enable HAGS the standard way

The two-click method.

1. Go to **Settings** > **System** > **Display** > **Graphics**.
2. Click **Change default graphics settings** (or **Default graphics settings**).
3. Turn on **Hardware-accelerated GPU scheduling**.
4. Restart the laptop — use **Restart**, not shutdown, to ensure the scheduler change applies.
5. Return to the same page after reboot and confirm the toggle shows **On** — if it reverted, something (driver, policy, or software) is blocking it; continue below.

### Fix 3: Enable HAGS via the registry

When the Settings toggle is missing or won't stick.

1. Press **Win + R**, type `regedit`, and back up (**File** > **Export**).
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Find or create the DWORD (32-bit) value `HwSchMode` and set it to `2` (enabled). `1` means disabled.
4. Restart the laptop.
5. Check the Settings toggle afterward — it should now show On. If the value resets to `1` on reboot, a driver or OEM utility is forcing it off; update the graphics driver and check vendor utilities (Lenovo Vantage, Armoury Crate, etc.) for GPU settings.

### Fix 4: Update the graphics driver for HAGS support

The toggle depends entirely on the driver.

1. Identify your GPU exactly (**Task Manager** > **Performance** > **GPU**).
2. Download the latest driver from the vendor: [Intel's tool](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) — prefer the vendor driver over the laptop OEM's older one for HAGS support.
3. Choose **Custom/Advanced install** and check **Perform a clean installation** (NVIDIA) or use DDU in Safe Mode for a truly clean slate.
4. Restart, then check for the HAGS toggle again.
5. On laptops with both integrated and discrete GPUs, update both drivers — the scheduler setting interacts with the active rendering path.

### Fix 5: Test whether HAGS actually helps you

Enabled isn't the same as beneficial — measure.

1. Pick 2–3 games or GPU-heavy apps you actually use, and note baseline FPS (use the game's built-in counter or an overlay like the Xbox Game Bar's **Win + G** performance widget).
2. Enable HAGS, restart, and re-run the same scenes — compare average FPS and, more importantly, stutter (1% lows).
3. Also test your recording/streaming setup if you use one — some capture software misbehaves with HAGS on.
4. Give it a few days of normal use — some HAGS issues (occasional driver crashes, micro-stutter) only show up over time.
5. If numbers are flat or worse, turn it off — there's no prize for running a feature that doesn't help your specific hardware and games.

### Fix  6: Resolve conflicts with other software

When HAGS and something else fight.

1. If you use virtualization (Hyper-V, VMware, VirtualBox), test with HAGS off — hypervisors and the GPU scheduler have a rocky history together.
2. Screen recorders and overlays (OBS, Discord overlay, etc.) — if crashes started when you enabled HAGS, disable their hardware acceleration or turn HAGS off.
3. Check for GPU driver crashes in **Event Viewer** > **Windows Logs** > **System** (source: nvlddmkm, amdkmdap, or igfx) — crashes correlating with HAGS-on mean the combination is unstable on your system.
4. Some games have known HAGS issues documented in their forums — check before assuming your system is broken.
5. When in doubt, stability beats 3% more FPS — turn HAGS off and enjoy a crash-free system.

### Fix 7: Keep it working across updates

Drivers and Windows updates can silently change the setting.

1. After every graphics driver update, verify the HAGS toggle is still in your preferred state — updates sometimes reset it.
2. After Windows feature updates, recheck too — the migration can flip the setting or the registry value.
3. Keep a note of your tested preference (on or off) so you don't re-run the whole benchmark process after each update.
4. If a new driver removes the toggle that an old one showed, report it to the vendor — and roll back to the working driver in the meantime.
5. Re-test performance yearly or after major game/driver changes — the HAGS calculus can shift as drivers mature.

## Closing

Hardware-Accelerated GPU Scheduling is a legitimate, if modest, performance feature — when your hardware supports it, your driver is current, and your games actually benefit. Check support, enable it, measure honestly, and keep it only if the numbers say so. That's the entire philosophy: no setting is "always better," but the ones you verify are.
