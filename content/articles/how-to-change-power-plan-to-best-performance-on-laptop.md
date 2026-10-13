---
title: "Switch Your Laptop Power Plan to Best Performance"
slug: how-to-change-power-plan-to-best-performance-on-laptop
date: 2026-10-13
categories: ["performance"]
tags: ["power plan", "best performance", "power mode", "battery", "windows 11"]
description: "Windows 11 hides its power plans behind a slider — here's how to get maximum performance mode, when to use it, and what it actually changes under the hood."
thumbnail: "/images/thumbs/how-to-change-power-plan-to-best-performance-on-laptop.webp"
faqs:
  - q: "Where did the High Performance power plan go in Windows 11?"
    a: "Microsoft replaced the classic Power Plans UI with the Power mode slider (Best power efficiency / Balanced / Best performance) on most modern laptops, especially those using Modern Standby — the old Control Panel plans are hidden, not gone. You can still reveal the full schemes (including Ultimate Performance) via powercfg commands, which this guide covers. The slider's 'Best performance' is the supported everyday option."
  - q: "Does Best Performance mode actually make my laptop faster?"
    a: "It prevents the CPU and GPU from downclocking aggressively, which helps bursty workloads: app launches, compiles, photo exports, and games see snappier response and fewer clock-ramp delays. It doesn't overclock anything — it just stops power-saving from throttling you. Sustained heavy workloads (long renders) are usually thermally limited anyway, where the plan matters less than cooling."
  - q: "How much battery does Best Performance use?"
    a: "Noticeably more at idle and light use — the CPU stays at higher clocks instead of dropping to power-saving states, which can cut battery life by 15–30% in light workloads. Under heavy load the difference shrinks, since the CPU would be maxed regardless. The practical approach: Best performance on AC power, Balanced or Best power efficiency on battery, switched automatically."
  - q: "What is the Ultimate Performance plan and should I use it?"
    a: "Ultimate Performance is a hidden power scheme (powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61) that removes virtually all power-saving idle states — designed for workstations, not laptops. On a laptop it mainly generates heat and fan noise for negligible gains over Best performance, while hammering battery life. It's safe to try, but for laptops Best performance is the sweet spot; Ultimate is for plugged-in desktops."
---

Somewhere in Windows 11's redesign, the familiar High Performance power plan vanished from most laptops — replaced by a three-position Power mode slider that feels like less control, not more. The plans aren't gone; they're hidden, especially on Modern Standby machines where Microsoft decided the slider was enough. This guide covers both: the slider everyone sees, and the full powercfg schemes underneath for when you want the real controls — plus when Best performance actually helps and when it's just fan noise.

The honest framing first: a power plan doesn't make your CPU faster — it stops Windows from making it slower. If your laptop stutters because the CPU downclocks between bursts, Best performance fixes it. If it's slow because of background bloat, see [how to speed up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) and [trimming startup programs](/articles/how-to-disable-startup-programs-windows-11/) — no power plan fixes those.

## Why this happens

- **Aggressive default power saving**: Balanced/Battery-saver modes downclock the CPU deeply, adding ramp-up latency to every burst of work.
- **Hidden classic plans**: Modern Standby laptops hide the Control Panel power plans, leaving only the slider.
- **Updates resetting power mode**: Windows updates frequently revert custom power settings to defaults.
- **OEM profiles overriding**: Lenovo Vantage, Armoury Crate, and Dell Power Manager impose their own profiles over Windows'.
- **Battery-saver auto-engaging**: Windows drops into efficiency modes at battery thresholds without telling you clearly.
- **Misunderstood tradeoffs**: users fear Best performance "damages" the laptop — it doesn't; thermals, not the plan, are the limiter.
- **Per-app GPU preferences**: the power plan is only half the story; graphics preference per app matters too.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Power mode slider correctly

The supported, everyday control.

1. Go to **Settings > System > Power & battery**.
2. Find **Power mode** and set it to **Best performance** — this is Microsoft's intended "go fast" setting.
3. Understand what changes: higher minimum processor states, less aggressive CPU parking, GPU allowed to boost sooner.
4. Test your actual workload for a day — bursty tasks (compiles, exports, game loading) should feel snappier.
5. Note the battery cost over a full day of light use — if it's unacceptable, Fix 6 shows how to automate switching.

### Fix 2: Reveal the classic power plans

For the full traditional control panel.

1. Open an elevated terminal and run `powercfg /list` — see which schemes exist (often just Balanced).
2. Restore the missing schemes: `powercfg -duplicatescheme 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c` (High performance) and `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61` (Ultimate Performance).
3. Open **Control Panel > Power Options** — the restored plans now appear for selection.
4. Select **High performance** as your plugged-in plan — the time-tested scheme.
5. On Modern Standby laptops these may not fully apply to sleep behavior — the slider still governs standby; the classic plans govern active use.

### Fix 3: Tune the plan's advanced settings

The defaults are conservative; tune what matters.

1. **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. **Processor power management > Minimum processor state**: on AC, try 50–100% if you want zero ramp latency (at the cost of heat and fan).
3. **Maximum processor state**: leave at 100% — lowering it is a throttle, not an optimization.
4. **PCI Express > Link State Power Management**: set to **Off** on AC if you suspect GPU power-state stutter.
5. **USB selective suspend**: disable as a test if USB devices misbehave on Best performance — then re-enable if unrelated.

### Fix 4: Set per-app GPU preferences

The power plan doesn't choose which GPU an app uses — this does.

1. **Settings > System > Display > Graphics** — add your demanding apps/games via **Add an app**.
2. Set each to **High performance** GPU preference — forces the discrete GPU instead of power-saving integrated.
3. This matters enormously on dual-GPU laptops: the wrong GPU choice dwarfs any power-plan effect.
4. Verify in Task Manager > Performance which GPU is active during your workload.
5. Pair with our [HAGS guide](/articles/best-way-to-enable-hardware-accelerated-gpu-scheduling/) for the full GPU-latency stack.

### Fix 5: Stop OEM tools from overriding you

Your plan means nothing if Vantage overrides it hourly.

1. Check your vendor utility (Lenovo Vantage, Armoury Crate, Dell Power Manager, OMEN Hub) — note its current thermal/power profile.
2. Align it with Windows: set the vendor profile to its performance mode when you want Best performance behavior.
3. Disable "intelligent" auto-switching features that change profiles based on detected apps — they fight your manual choice.
4. After Windows updates, re-check both layers — updates reset Windows' slider and sometimes the vendor profile.
5. When in doubt, the vendor's performance profile + Windows Best performance is the maximum-speed combination.

### Fix 6: Automate AC versus battery behavior

Best of both: speed on AC, battery on battery.

1. Windows doesn't auto-switch the slider by power source — but your vendor utility might (check its settings for AC/battery profiles).
2. Alternative: create two powercfg schemes and switch with a desktop shortcut — `powercfg /setactive <GUID>` in a .bat file, one for AC, one for battery.
3. Find GUIDs with `powercfg /list`; make shortcuts and pin them to the taskbar for one-click switching.
4. Set **Battery saver** threshold thoughtfully: **Settings > System > Power & battery > Battery saver > Turn on at** — 20% is sane.
5. Microsoft documents power management at the [Windows support hub](https://support.microsoft.com/en-us/windows) for the official details.

## Closing

Best performance mode is simple and honest: it tells Windows to stop economizing your CPU. Use the slider for everyday control, reveal the classic plans when you want the real knobs, align your vendor's profiles so they don't fight Windows, and automate the AC/battery split. It's not overclocking and it won't hurt the laptop — thermals are the real speed limit, and no power plan changes physics. But for everything below that limit, Best performance makes sure you actually get what you paid for.
