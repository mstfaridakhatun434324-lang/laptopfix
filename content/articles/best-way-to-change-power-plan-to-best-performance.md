---
title: "The Best Way to Switch Your Power Plan to Best Performance"
slug: best-way-to-change-power-plan-to-best-performance
date: 2026-10-09
categories: ["performance"]
tags: ["power plan", "best performance", "power mode", "windows 11", "cpu performance"]
description: "Switch Windows to Best Performance mode the right way — Settings, Control Panel, and manufacturer utilities — plus when to use it and when Balanced is smarter."
thumbnail: "/images/thumbs/best-way-to-change-power-plan-to-best-performance.webp"
faqs:
  - q: "Does Best Performance mode actually make my laptop faster?"
    a: "Yes, measurably, for sustained workloads. Best Performance prevents the CPU from downclocking aggressively, keeps boost clocks available longer, and stops Windows from parking cores to save power. The difference is most visible in gaming, video rendering, and compilation — often 10 to 25 percent. For web browsing and office work, you will notice little difference."
  - q: "Will Best Performance mode damage my laptop or battery?"
    a: "No, it will not damage the hardware — thermal protections still work normally. It will drain the battery much faster and make the laptop run hotter and louder, since the CPU stays at higher clocks. The sensible approach is using Best Performance while plugged in for demanding tasks and switching back to Balanced on battery."
  - q: "Why don't I see the High Performance plan in Windows 11?"
    a: "On modern laptops, Microsoft hides the classic High Performance plan in favor of the Power mode slider in Settings. The slider's Best performance setting is the modern equivalent. You can still unhide the classic plans with a command (powercfg), but the slider plus your manufacturer's performance utility usually covers everything you need."
  - q: "Should I use Best Performance or my manufacturer's Turbo mode?"
    a: "Use the manufacturer's mode (Turbo, Performance, or Extreme) for gaming and heavy work — it controls fan curves and power limits that Windows cannot touch. Use Windows' Best Performance slider as the complement: set Windows to Best performance and let the manufacturer utility handle the thermal side. They work together, not against each other."
---

Switching to Best Performance sounds like a single click, and in Settings it nearly is — but doing it the right way means understanding the three layers that control your laptop's speed: Windows' power mode, the classic power plans underneath, and your manufacturer's own performance utility. Set only one layer and you get half the benefit; set all three coherently and the laptop actually sustains its top speeds.

This guide covers the best method for each layer, when Best Performance genuinely helps, and the situations where it is the wrong choice.

## Why this happens

- **Balanced mode downclocks aggressively:** The default Balanced plan parks CPU cores and drops clocks at the slightest idle, costing responsiveness in bursty workloads.
- **Boost behavior differs by plan:** Best Performance allows the CPU to hold boost clocks longer before thermal or power limits pull it back.
- **Background power saving interrupts work:** USB selective suspend, PCIe link-state saving, and disk sleep can all introduce micro-stutters that Best Performance disables.
- **Manufacturer utilities override Windows:** Dell, Lenovo, HP, and ASUS utilities set their own power limits and fan curves that can cap performance regardless of the Windows plan.
- **Battery vs. plugged-in profiles differ:** Windows applies different settings per power source, so a plan that flies on AC may crawl on battery by design.
- **Modern Standby complicates idle:** Sleep and idle behavior on modern laptops interacts with power plans in ways the classic High Performance plan never anticipated.
- **Thermal limits still apply:** No power plan overrides physics — if cooling is inadequate, the CPU throttles at the same temperature regardless of the plan.
- **Stuck plans cause confusion:** Updates and manufacturer tools sometimes leave the system on Power Saver silently, making the laptop feel broken rather than merely economical.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what power mode you are actually on

1. Open **Settings → System → Power & battery** and look at the **Power mode** dropdown.
2. Note whether it says **Best power efficiency**, **Balanced**, or **Best performance** — and check it separately for plugged-in versus on-battery if your laptop shows both.
3. Many "slow laptop" complaints trace to this slider sitting on Best power efficiency after an update or a battery-saving session.
4. This single check takes ten seconds and resolves a surprising number of performance complaints outright.

### Fix 2: Set Best performance in Settings (the modern method)

1. In **Settings → System → Power & battery**, set **Power mode** to **Best performance**.
2. Do this while plugged in — Windows 11 lets some laptops set separate modes per power source, so verify the plugged-in setting specifically.
3. Test your workload: launch a game or heavy app and confirm the improvement with Task Manager's CPU speed readout.
4. Leave it here for demanding sessions, and switch back to Balanced for everyday battery use. This slider is the officially supported path — Microsoft documents power modes at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 3: Unhide the classic High Performance plan (optional)

1. Open an **admin Terminal** and run `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61` to restore the classic High Performance scheme.
2. Open **Control Panel → Power Options** — High Performance should now appear alongside Balanced and Power saver.
3. Select it and click **Change plan settings → Change advanced power settings** to fine-tune: processor min/max states, USB selective suspend, and PCIe link-state management.
4. The classic plan offers more granular control than the slider, at the cost of complexity most users do not need.

### Fix 4: Set your manufacturer's performance mode

1. Open your manufacturer's utility — **Lenovo Vantage, Dell Power Manager, HP Omen Gaming Hub / Command Center, ASUS Armoury Crate, or Acer NitroSense**.
2. Switch its thermal/performance mode to **Performance** or **Turbo** (names vary).
3. This controls fan curves and CPU/GPU power limits that Windows plans cannot reach — it is the layer that actually sustains high clocks under load.
4. Expect more fan noise; that is the cooling system doing its job. For the full walkthrough of this layer, see [changing power plan to Best Performance in 24H2](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/).

### Fix 5: Tune advanced settings for sustained loads

1. In **Control Panel → Power Options → Change plan settings → Change advanced power settings**, expand **Processor power management**.
2. Set **Maximum processor state** to **100%** for both battery and plugged in; set **Minimum processor state** to **5%** so the CPU can still idle.
3. Expand **PCI Express → Link State Power Management** and set it to **Off** while plugged in — this prevents GPU-adjacent micro-stutters.
4. Set **USB settings → USB selective suspend** to **Disabled** while plugged in if you use external drives or audio interfaces that stutter.

### Fix 6: Verify the change took effect

1. Open **Task Manager → Performance → CPU** and watch the **Speed** readout during a heavy task — it should hold near the processor's boost clock rather than bouncing low.
2. Run your actual workload (game, render, compile) and compare before/after — synthetic benchmarks are less useful than your real task.
3. Check temperatures with a hardware monitor: sustained high clocks mean more heat, and thermal throttling will cap gains if cooling is inadequate.
4. If speeds do not improve, the manufacturer utility (Fix 4) is likely still capping power — Windows plans cannot override its limits.

### Fix 7: Know when NOT to use Best Performance

1. On battery, Best Performance can halve your runtime — switch to **Balanced** or **Best power efficiency** when unplugged unless you need every drop of speed.
2. For light work (browsing, documents, video calls), Balanced delivers identical perceived speed with less heat, noise, and power draw.
3. In hot environments, Best Performance plus inadequate cooling equals thermal throttling — which performs worse than Balanced with headroom.
4. Make switching a habit: Best performance for plugged-in heavy work, Balanced for everything else. If the laptop feels slow on battery specifically, see [laptop slow when plugged in after update](/articles/how-to-fix-laptop-slow-when-plugged-in-after-windows-11-update/) — the inverse problem has its own causes.

### Fix 8: Lock it in against resets

1. Windows updates occasionally reset the power mode slider — check it after each feature update.
2. Manufacturer utilities sometimes revert to Quiet/Balanced after their own updates; re-verify after those too.
3. If you used the command-line plan from Fix 3, export it with `powercfg /export` so you can reimport your tuned settings instantly.
4. A thirty-second check after updates prevents the mystery slowdowns that are really just reset power settings.

## Closing

The best way to switch to Best Performance is not one toggle but three aligned layers: Windows' power mode slider, the classic plan underneath if you want fine control, and your manufacturer's performance utility handling thermals and power limits. Set all three while plugged in for heavy work, drop back to Balanced on battery, and recheck after updates. Done this way, Best Performance delivers its full 10–25 percent instead of fighting your own settings.
