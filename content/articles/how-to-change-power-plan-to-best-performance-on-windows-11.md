---
title: "Switch Windows 11 to Best Performance Mode: Power Plan Guide"
slug: how-to-change-power-plan-to-best-performance-on-windows-11
date: 2026-09-05
categories: ["performance"]
tags: ["power plan", "best performance", "windows 11", "power mode", "battery"]
description: "Learn how to change the power plan to Best Performance on Windows 11 — including the hidden Ultimate Performance plan — for faster laptops."
thumbnail: "/images/thumbs/how-to-change-power-plan-to-best-performance-on-windows-11.webp"
faqs:
  - q: "Where is the Best Performance power plan in Windows 11?"
    a: "Windows 11 replaced the old Control Panel power plans with a simpler Power mode slider: Settings > System > Power & battery > Power mode. Choose Best performance from the dropdown. The classic High performance and Ultimate Performance plans still exist but are hidden by default; you can unlock them with a powercfg command in an elevated Command Prompt, after which they appear in the old Power Options panel."
  - q: "Does Best Performance mode actually make a laptop faster?"
    a: "Yes, measurably — especially for bursty workloads like opening apps, compiling code, or loading games. Best performance keeps CPU boost clocks available longer, raises the minimum processor state, and prevents aggressive power-saving states that add wake-up latency. Expect snappier responsiveness and a few percent more sustained throughput, at the cost of shorter battery life and more fan noise during heavy loads."
  - q: "Will Best Performance mode damage my laptop battery?"
    a: "No, it won't damage the battery directly — it simply lets components draw more power, which drains the battery faster per charge. Battery wear comes from heat and full charge cycles, and sustained high performance does generate more heat, so long-term heavy use can slightly accelerate wear. For plugged-in desktop-style use it's harmless; on battery, switch back to Balanced or Best power efficiency for daily work."
  - q: "What is the Ultimate Performance power plan and should I use it?"
    a: "Ultimate Performance is a hidden power plan Microsoft added for workstations that disables nearly all power-saving throttles, including CPU parking. You can unlock it with powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 in an elevated terminal. It helps only in niche sustained workloads and uses noticeably more power, so for most laptops the standard Best performance mode is the better choice — enable Ultimate Performance only on workstations that stay plugged in."
---

If your Windows 11 laptop feels sluggish — apps take a beat too long to open, games stutter, the whole machine just feels held back — the cause might not be hardware at all. Windows 11 ships on the Balanced power plan (and many laptops add a Battery saver default), which aggressively throttles your CPU to save power. Switching to Best Performance tells Windows to prioritize speed: higher sustained clock speeds, less core parking, and snappier wake-from-idle behavior.

The payoff is real and free. Benchmarks on typical thin-and-light laptops show 5–15% better burst performance and noticeably faster app launches on Best performance versus Balanced, simply because the CPU is allowed to boost sooner and stay boosted longer. There's a tradeoff — battery life and fan noise — but you can switch plans in seconds, so there's no reason not to use the fast one when you're plugged in and the efficient one on the go.

In this guide I'll show you the modern way (the Power mode dropdown in Settings), how to unlock the classic High performance and Ultimate Performance plans with one command, what each setting actually changes under the hood, and when each plan makes sense. For the broader picture of a sluggish machine, also see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); if battery drain is the bigger worry, check our [battery optimization tips](/articles/laptop-battery-drains-fast-windows-11/).

## Why this happens

- **Balanced plan is the default**: Every Windows 11 install starts on Balanced, which caps boost behavior to save power.
- **OEM power utilities override Windows**: Dell Power Manager, Lenovo Vantage, HP Omen, and ASUS Armoury Crate often impose their own quiet/eco profiles that ignore the Windows slider.
- **Battery saver kicks in silently**: At 20% battery (default), Windows drops into Battery saver mode, throttling background activity and CPU — performance tanks without warning.
- **CPU parking and C-states**: Power-saving plans aggressively park cores and drop into deep sleep states, adding latency every time the CPU has to wake up.
- **Thermal throttling compounded**: A hot laptop already throttles; an eco plan makes it worse by lowering the thermal ceiling too.
- **GPU power limits**: Power plans also govern the discrete GPU — Balanced can hold it at lower clocks during gaming or rendering.
- **Minimum processor state at 5%**: On Balanced, the CPU is allowed to drop to 5% of max frequency, which makes light-but-bursty tasks feel laggy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Switch Power mode to Best performance in Settings

This is the official Windows 11 method and covers 90% of users.

1. Open **Settings** > **System** > **Power & battery**.
2. Find the **Power mode** dropdown (if you're on battery you'll see one dropdown; plugged in shows a second one — set both).
3. Change it to **Best performance**.
4. If you only see the option greyed out or missing, your OEM utility (Dell Power Manager, Lenovo Vantage, Armoury Crate) has taken control — check that app for its own performance/quiet toggle first.
5. Test with your actual workload — open a few apps, play your game. The difference should be obvious within minutes.

### Fix 2: Unlock the classic High performance plan

For users who want the old Control Panel plans with granular settings.

1. Open Terminal as administrator (right-click **Start** > **Terminal (Admin)**).
2. Run `powercfg /list` to see your current schemes — you'll typically see Balanced and a power-saver scheme.
3. To restore High performance, run: `powercfg -duplicatescheme 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c`
4. Open **Control Panel** > **Hardware and Sound** > **Power Options** — High performance should now appear.
5. Select it, then click **Change plan settings** > **Change advanced power settings** to fine-tune: set **Minimum processor state** to 100% on plugged-in for maximum responsiveness (and 5–10% on battery to save power).

### Fix 3: Unlock the hidden Ultimate Performance plan

For workstations and plugged-in power users who want every throttle removed.

1. In an elevated Terminal, run: `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`
2. Open **Power Options** in Control Panel — **Ultimate Performance** now appears.
3. Select it and check advanced settings: it disables USB selective suspend, PCIe link-state power management, and processor performance core parking by default.
4. Only use this plan when plugged in — on battery it will drain the charge noticeably faster than Balanced.
5. Honest assessment: on most laptops it adds single-digit percentage gains over High performance. It's most worthwhile on desktop-replacement machines with good cooling. Microsoft documents power plans at [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 4: Stop Battery saver from throttling you unexpectedly

Battery saver is useful — but not when it surprises you mid-task.

1. Go to **Settings** > **System** > **Power & battery** > **Battery saver**.
2. Check the **Turn battery saver on automatically at** threshold — the default 20% is fine for most, but if you frequently do heavy work on battery, consider 10%.
3. Note that while Battery saver is active, Windows lowers screen brightness, pauses background sync (OneDrive, mail), and limits background apps — all of which feel like slowness.
4. Toggle it manually from Quick Settings (Win + A) when you need a burst of speed on battery — just watch your remaining charge.
5. For gaming or rendering on battery: honestly, don't. The battery can't sustain full performance anyway; these workloads belong on the charger.

### Fix 5: Check your OEM utility's performance profile

This is the step most guides skip — and it's often the real bottleneck.

1. **Dell**: Open Dell Power Manager (or MyDell) > **Thermal Management** > set to **Ultra Performance** instead of Quiet/Cool. See [Dell Support](https://www.dell.com/support) for your model's options.
2. **Lenovo**: Lenovo Vantage (or Legion toolkit) > **Thermal Mode** or **Power** > choose **Performance**. Lenovo machines also have a physical Fn+Q shortcut on many models that cycles Quiet/Balanced/Performance.
3. **HP**: HP Omen Gaming Hub or OMEN devices have a Performance mode; business models use HP Power Manager. Check [HP Support](https://support.hp.com/us-en) for your model.
4. **ASUS**: Armoury Crate > **Operating Mode** > **Turbo** (or Performance). ASUS laptops notoriously ignore the Windows slider when Armoury Crate is set to Silent.
5. Rule of thumb: the OEM utility wins. If you set Windows to Best performance but the OEM app says Quiet, Quiet wins.

### Fix 6: Tune advanced processor settings for responsiveness

For users comfortable in the advanced power settings dialog.

1. In **Power Options** > **Change advanced power settings**, expand **Processor power management**.
2. Set **Minimum processor state** (plugged in) to 100% — this eliminates the ramp-up lag when the CPU has to climb from idle to boost.
3. Set **System cooling policy** to **Active** — fans spin up sooner to sustain boost clocks instead of throttling early.
4. Under **PCI Express** > **Link State Power Management**, set to **Off** on plugged-in — this stops the GPU link from downshifting, which can cause micro-stutter in games.
5. Under **USB settings** > **USB selective suspend**, disable it if you use external drives or audio interfaces — selective suspend can cause disconnects and latency spikes.

### Fix 7: Verify the change actually took effect

Don't trust the slider alone — confirm the CPU behaves differently.

1. Open **Task Manager** > **Performance** > **CPU** and watch the **Speed** readout while you do something demanding — on Best performance it should jump to boost clocks (3–4+ GHz) immediately instead of lingering at low speeds.
2. Use **powercfg /query** in Terminal to dump the active scheme's settings if you want to confirm values programmatically.
3. Run your real workload — export a video, compile, game for 10 minutes — and compare fan behavior and completion time against Balanced.
4. Check **Settings** > **System** > **Power & battery** again after a reboot — some OEM tools reset the plan on restart; if yours does, set the default inside the OEM app instead.

## Closing

Best Performance mode is the simplest free speed boost in Windows 11: one dropdown, no software to install, instantly reversible. Use it when you're plugged in and doing real work, let Balanced or Best power efficiency handle your on-battery hours, and remember that your laptop maker's utility app gets the final say — check it first if the Windows setting seems to do nothing.
