---
title: "How to Change the Power Plan to Best Performance in Windows 11 24H2"
slug: how-to-change-power-plan-to-best-performance-in-windows-11-24h2
date: 2026-09-21
categories: ["performance"]
tags: ["power plan", "best performance", "windows 11 24h2", "power mode"]
description: "Switch Windows 11 24H2 to Best Performance mode the right way — power mode slider, legacy power plans, and per-app GPU settings explained."
thumbnail: "/images/thumbs/how-to-change-power-plan-to-best-performance-in-windows-11-24h2.webp"
faqs:
  - q: "Where is the power plan setting in Windows 11 24H2?"
    a: "Microsoft moved the main control to Settings > System > Power & battery, where a Power mode dropdown offers Best power efficiency, Balanced, and Best performance. The classic Control Panel power plans (Balanced, High performance, Power saver) still exist but are hidden — search for 'Choose a power plan' in the Control Panel to find them. On battery, the Quick Settings panel (Win + A) also exposes the power mode slider."
  - q: "Does Best Performance mode actually make my laptop faster?"
    a: "It removes power-saving throttles: the CPU boosts more aggressively, background throttling relaxes, and sleep timers extend. In sustained workloads like gaming or rendering, expect 5–15% better performance versus power-saver modes. The tradeoff is real — higher fan noise, more heat, and significantly shorter battery life. Use it plugged in; switch back to Balanced on battery unless you need the speed."
  - q: "Why is the High performance plan missing from my laptop?"
    a: "On modern laptops with Modern Standby (S0 sleep), Windows hides the legacy High performance and Power saver plans, showing only Balanced in the Control Panel. This is by design — power management is handled through the Power mode slider instead. You can restore the hidden plans with a Registry tweak or the powercfg command, but the Best performance power mode achieves the same practical result."
  - q: "Should I use Best Performance all the time?"
    a: "No — use it when plugged in and doing demanding work. Running Best Performance on battery drains the battery fast and generates unnecessary heat for light tasks like browsing. The smart setup: Best performance power mode while plugged in (or a High performance plan), Balanced on battery. Windows 11 24H2 remembers separate power modes for plugged-in versus on-battery states."
---

If your laptop feels sluggish and you suspect Windows is holding back the hardware to save battery, you're probably right. Windows 11 24H2's default Balanced mode is conservative — it keeps clocks low, parks cores, and throttles background work. Switching to Best Performance removes those limiters and lets the CPU and GPU run at their rated speeds. It won't turn a budget laptop into a workstation, but it eliminates the artificial ceiling power-saving puts on your hardware.

The catch: Microsoft buried the controls across Settings, Quick Settings, and the legacy Control Panel, and on Modern Standby laptops the classic High performance plan is hidden entirely. This guide shows every path — the simple slider, the hidden legacy plans, and per-app performance tuning — so you get maximum speed where it matters. Pair this with trimming [startup programs](/articles/how-to-disable-startup-programs-windows-11/) for the full responsiveness package, and see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) for the broader tune-up.

## Why this happens

- **Balanced mode throttles aggressively**: Default settings favor battery life, keeping CPU clocks and boost behavior conservative.
- **Power Saver may be stuck on**: Battery Saver engaging at low charge — or a misconfigured default — silently caps performance.
- **Legacy plans hidden on Modern Standby**: Laptops with S0 sleep only show Balanced in Control Panel, confusing users looking for High performance.
- **Per-app GPU preference defaults to power saving**: Hybrid laptops run apps on the weak iGPU unless told otherwise.
- **Manufacturer utilities override Windows**: Dell Power Manager, Lenovo Vantage, or ASUS Armoury Crate profiles can fight the Windows setting.
- **Thermal throttling mimics power throttling**: If the cooling can't keep up, no power plan helps — the CPU downclocks from heat anyway.
- **Background power policies**: USB selective suspend and PCIe link-state power management add latency on Balanced.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set Best Performance in Settings (the easy way)

The primary control in 24H2.

1. Open **Settings** > **System** > **Power & battery**.
2. Find the **Power mode** dropdown and select **Best performance**.
3. Note that 24H2 lets you set this separately for plugged-in vs. battery — set **Best performance** for plugged in, and **Balanced** (or Best power efficiency) for on-battery.
4. Also review the **Screen and sleep** timeouts on the same page — overly aggressive sleep timers interrupt long tasks.
5. Test with your actual workload: the difference shows up in sustained tasks (gaming, compiling, rendering), not in opening Notepad.

### Fix 2: Use the Quick Settings slider for fast switching

For toggling on the fly.

1. Click the battery/network/volume icon (or press Win + A) to open **Quick Settings**.
2. Click the **battery icon** to expand the power slider (on some builds it appears directly).
3. Drag to **Best performance** when plugged in and doing heavy work; drag back to **Better battery** or **Best battery life** when unplugged.
4. This slider and the Settings dropdown stay in sync — it's the same underlying setting.
5. Make it a habit: Best performance for gaming/rendering sessions, Balanced for everything else.

### Fix 3: Restore the hidden High performance plan

For those who want the classic Control Panel plans back.

1. Open an admin **Terminal** and run `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61` — this restores the **High performance** plan.
2. Open **Control Panel** > **Hardware and Sound** > **Power Options** — High performance should now appear (click "Show additional plans" if needed).
3. Select it, then click **Change plan settings** > **Change advanced power settings** to fine-tune: set **Processor power management** > **Maximum processor state** to 100% for both battery and plugged in.
4. In the same advanced dialog, set **PCI Express** > **Link State Power Management** to **Off** (plugged in) to remove GPU latency from power saving.
5. Warning: on Modern Standby laptops these legacy plans can behave oddly with sleep — if sleep breaks, revert to Balanced and use the Settings power mode instead. Microsoft's power-management reference on [Microsoft Support](https://support.microsoft.com/en-us/windows) documents the powercfg options in more depth.

### Fix 4: Set per-app GPU and performance preferences

Stop hybrid laptops from running demanding apps on the weak iGPU.

1. Open **Settings** > **System** > **Display** > **Graphics**.
2. Find your game or heavy app in the list (or add it via **Add an app**), click it, then **Options**.
3. Set **GPU preference** to **High performance** — this forces the discrete GPU instead of power-saving integrated graphics.
4. On the same Graphics page, open **Change default graphics settings** and enable **Hardware-accelerated GPU scheduling** plus **Optimizations for windowed games**.
5. This per-app approach gives you performance where it counts without running the whole system hot.

### Fix 5: Check manufacturer power utilities

They can silently override Windows.

1. Open your vendor's tool — **Lenovo Vantage**, **Dell Power Manager**, **HP Command Center**, **MyASUS**, or **Armoury Crate** — and check its thermal/power profile.
2. If it's set to Quiet, Battery Saver, or Whisper mode, it will cap performance regardless of the Windows setting — switch it to **Performance** or **Balanced**.
3. In Lenovo Vantage specifically, check **Intelligent Cooling** mode; in Armoury Crate, the **Turbo/Performance** profile.
4. Align the vendor profile with your Windows power mode so they aren't fighting each other.
5. Also check BIOS: some laptops have a **Thermal mode** or **Performance mode** toggle in firmware that acts as a master limiter.

### Fix 6: Disable USB selective suspend and fine-tune advanced settings

Remove latency from aggressive power saving.

1. Open **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** for your active plan.
2. Expand **USB settings** > **USB selective suspend setting** and set it to **Disabled** (plugged in) — this stops USB devices (docks, external drives) from lagging on wake.
3. Expand **Processor power management** > **Minimum processor state** — raise plugged-in to 50–100% if you want zero ramp-up delay (at the cost of heat and fan noise).
4. Expand **Multimedia settings** > **When playing video** > set to **Optimize video quality** (plugged in).
5. Click OK and test — these micro-settings mainly help stutter and wake latency rather than raw speed.

### Fix 7: Verify thermals aren't the real limiter

A power plan can't fix heat throttling.

1. Install HWMonitor or HWiNFO and run your heavy workload while watching CPU package temperatures.
2. If temps sit at 95–100°C with clocks dropping, you're thermal-throttling — clean the vents with compressed air and consider a cooling pad.
3. Check that fans actually spin up under load; a dead fan makes every power plan perform identically (badly).
4. On older laptops, dried thermal paste is a common cause — a repaste by a repair shop restores headroom.
5. Only after thermals are healthy does Best Performance deliver its full benefit — otherwise you're just making heat faster.

## Closing

Best Performance mode is the right call whenever you're plugged in and doing real work — it simply stops Windows from artificially holding your hardware back. Use the Settings power mode (or the restored High performance plan), align your vendor's utility profile, force demanding apps onto the discrete GPU, and keep thermals healthy. Switch back to Balanced on battery, and you'll have speed when you need it and endurance when you don't.
