---
title: "How to Switch Your Power Plan to Best Performance"
slug: how-can-i-change-power-plan-to-best-performance
date: 2026-09-16
categories: ["performance"]
tags: ["power plan", "best performance", "battery", "windows 11"]
description: "Switch Windows to Best Performance mode the right way: power plans, the hidden Ultimate Performance plan, and when speed is worth the battery cost."
thumbnail: "/images/thumbs/how-can-i-change-power-plan-to-best-performance.webp"
faqs:
  - q: "Where is the power plan setting in Windows 11?"
    a: "The quick setting is in Settings, then System, then Power and battery, under Power mode — choose Best performance. The classic full Power Options panel (Balanced, Power saver, High performance) lives in the Control Panel under Hardware and Sound, then Power Options. Windows 11 hides the classic plans on some laptops, which is why this guide also covers restoring them."
  - q: "Does Best Performance mode actually make a laptop faster?"
    a: "For bursty tasks — app launches, web browsing, compiling — yes, noticeably, because the CPU ramps to full speed immediately instead of easing up gradually. For sustained heavy loads like gaming or rendering, the difference is smaller because thermal limits cap the CPU anyway. The biggest wins are in responsiveness, not in benchmark scores."
  - q: "Will Best Performance mode damage my laptop or battery?"
    a: "No. It does not overclock anything — it only tells Windows to prefer speed over efficiency within the manufacturer's safe limits. The trade-offs are heat, fan noise, and shorter battery life, not hardware damage. Thermal protection still works exactly as before, throttling the CPU if temperatures get too high."
  - q: "What is the Ultimate Performance plan and should I use it?"
    a: "Ultimate Performance is a hidden power scheme that removes even the micro-latency power savings of High performance — originally built for workstations. On a laptop it offers negligible gains over Best performance while costing more battery. Enable it only for latency-critical work like audio production; for everything else, Best performance is the practical ceiling."
---

Every Windows laptop ships in **Balanced** mode — a compromise that sips battery when you are idle and ramps up when you work. It is a good default, but it is not the fastest setting. When you are plugged in and need every bit of responsiveness — gaming, video editing, compiling code, or just a snappy feel on an older machine — switching to **Best Performance** removes the hesitation built into power saving.

This is a simple change, but there are right and wrong ways to do it, plus a hidden plan most people never see. This guide covers the quick toggle, the classic plans, the Ultimate Performance unlock, and the honest trade-offs so you choose speed deliberately rather than accidentally.

## Why this happens

- **Balanced mode hesitates:** The CPU governor ramps clock speed gradually to save power, adding perceptible lag to bursty tasks.
- **Background power throttling:** Windows parks CPU cores and throttles background apps aggressively on Balanced, which slows multitasking.
- **GPU power states lag:** The graphics chip also scales up gradually, causing stutters in games and GPU-accelerated apps.
- **OEM "eco" defaults:** Many laptops ship with manufacturer power profiles even more conservative than Balanced.
- **Best Performance is hidden in places:** The classic High performance plan is hidden on modern laptops, so users assume Balanced is the only option.
- **Battery anxiety keeps people on Balanced:** Users leave power saving on while plugged in, paying a responsiveness tax for battery savings they are not using.
- **Per-app GPU settings override:** Even on Best Performance, individual apps may be assigned to the power-saving GPU — the plan alone does not fix that.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the quick Power mode toggle

1. Open **Settings → System → Power & battery**.
2. Find the **Power mode** dropdown and select **Best performance**.
3. Confirm the charger is connected — on battery, Best performance drains noticeably faster, so consider switching back when unplugged.
4. Test your typical workload for an hour. For many users, this single dropdown is the entire fix.

### Fix 2: Restore the classic power plans

1. Open **Control Panel → Hardware and Sound → Power Options**.
2. If you only see **Balanced**, click **Show additional plans** — **High performance** and **Power saver** may be hiding there.
3. Select **High performance** for the classic maximum-speed behavior while plugged in.
4. If the extra plans are missing entirely (common on modern laptops), continue to Fix 3 to unlock them.

### Fix 3: Unlock the Ultimate Performance plan

1. Open an elevated Command Prompt (**Win + R** → `cmd` → **Ctrl + Shift + Enter**).
2. Run: `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`.
3. Return to **Power Options** — **Ultimate Performance** now appears in the list. Select it.
4. Reserve this for plugged-in, latency-critical work. For daily use, **High performance** or the Settings **Best performance** toggle is the saner choice — the gains beyond that are marginal on a laptop.

### Fix 4: Set per-app GPU preferences

1. Go to **Settings → System → Display → Graphics**.
2. For each demanding app or game, click it → **Options** → select **High performance** (this pins it to the discrete/powerful GPU).
3. Add any missing apps with the **Add an app** button — Windows does not always detect games correctly.
4. The power plan sets the policy; this setting enforces it per app. Both matter — a Best Performance plan with apps assigned to the efficiency GPU still stutters.

### Fix 5: Stop the plan from resetting

1. Some laptops revert to Balanced on reboot because of manufacturer utilities — check your OEM's control app (Dell Power Manager, Lenovo Vantage, HP Command Center) for its own power/thermal mode and align it.
2. In **Power Options → Change plan settings → Change advanced power settings**, verify **Processor power management → Maximum processor state** is **100%** on **Plugged in**.
3. Check **PCI Express → Link State Power Management** — set to **Off** on Plugged in for maximum responsiveness.
4. If a Windows update resets your plan, re-select it and check the OEM utility — updates sometimes reinstall the manufacturer's power profile. Background on power settings lives on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Manage heat — the price of speed

1. Expect more fan noise and warmth on Best/Ultimate Performance — that is the CPU actually working at full speed.
2. Use a cooling pad or at least a hard flat surface; soft surfaces block intake vents and turn "best performance" into thermal throttling.
3. Clean dust from vents every few months — a clogged laptop cannot sustain the speeds the plan allows.
4. Monitor temperatures with HWiNFO during heavy loads; sustained CPU temps above 95°C mean the cooling cannot keep up, and no power plan fixes that — repasting or professional cleaning is the answer.

### Fix 7: Use the right plan at the right time

1. **Plugged in, demanding work:** Best performance / High performance / Ultimate Performance.
2. **On battery, light work:** Balanced or Best power efficiency — the speed difference is invisible in browsing and documents, but the battery difference is hours.
3. **Gaming on battery:** just do not — even Best Performance cannot overcome a battery's power delivery limits, and you will get throttling regardless.
4. Consider creating a habit: Best performance when the charger is in, Balanced when it is out. If your disk is the actual bottleneck rather than CPU policy, our [100% disk guide](/articles/how-to-fix-disk-active-time-100-percent-youtube/) will tell you — no power plan fixes a saturated drive.

## Closing

Best Performance mode is a trade, not a free upgrade: responsiveness now for battery and quiet later. Use the Settings toggle for simplicity, unlock Ultimate Performance only for latency-critical plugged-in work, pin demanding apps to the fast GPU, and switch back to Balanced on battery. Speed on demand, efficiency the rest of the time — that is the whole game.

One more thing worth knowing: power plans affect the whole system, so if your laptop still feels sluggish on Best Performance, the bottleneck is elsewhere — a saturated disk, exhausted RAM, or thermal throttling. Our [DWM GPU fix guide](/articles/how-to-fix-high-gpu-usage-dwm-exe-in-windows-11-24h2/) helps when graphics specifically feel held back despite the fastest plan. Measure, then tune — never the other way around.
