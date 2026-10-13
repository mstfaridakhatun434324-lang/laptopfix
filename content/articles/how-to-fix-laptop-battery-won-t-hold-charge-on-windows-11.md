---
title: "Laptop Battery Won't Hold a Charge on Windows 11: Fixes"
slug: how-to-fix-laptop-battery-won-t-hold-charge-on-windows-11
date: 2026-09-14
categories: ["battery"]
tags: ["won't hold charge", "battery drain", "windows 11"]
description: "Charges to 100% then dies in an hour? A battery that won't hold charge has specific causes — from runaway apps to worn cells. Fix it here."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-won-t-hold-charge-on-windows-11.webp"
faqs:
  - q: "What does 'won't hold a charge' actually mean?"
    a: "The battery charges up normally but drains far faster than it should — an hour or two instead of five or six. It's different from 'not charging' (never fills) and from sudden shutdowns (gauge errors). The battery fills fine; it just empties too fast."
  - q: "Is it the battery or something draining it?"
    a: "That's the key question, and the battery report answers it. If full charge capacity is close to design capacity but runtime is short, something is draining it — apps, settings, or hardware. If capacity is far below design, the battery itself is worn and drains fast because there's little to drain."
  - q: "Can Windows 11 itself drain the battery fast?"
    a: "Windows doesn't drain batteries by itself, but its settings and background tasks can: high-performance power mode, background apps, search indexing after an update, and wake timers. A clean look at Task Manager's battery usage screen usually reveals the hog."
  - q: "How long should a healthy laptop battery last?"
    a: "It varies hugely by model — ultrabooks often do 8–12 hours of light use, gaming laptops 3–5. Compare against your model's advertised battery life and your own history, not against other laptops. The red flag is a big drop from what your machine used to do."
---

It charges to 100% without complaint. Then you unplug, and it's a race: 80%... 60%... dead in ninety minutes. The battery isn't refusing to charge — it's refusing to *keep* the charge. That's a different problem with different suspects. And it's one of the most misdiagnosed battery complaints, because "drains fast" describes two completely different failures.

The divide that matters: is the battery emptying fast because something is drinking it dry, or because there's barely anything in the tank to begin with? Answer that, and the fix follows.

## Why this happens

- **Worn battery with low capacity:** The most common cause — a battery at 50% of design capacity simply holds half the energy, so it drains "fast" relative to your memory of it new.
- **Runaway background processes:** A stuck updater, runaway browser tab, or crypto-miner can drain a healthy battery in a fraction of the normal time.
- **High-performance power mode:** Best performance mode keeps clocks high and drains batteries dramatically faster than Balanced.
- **High screen brightness:** The display is often the single biggest power draw; 100% brightness can halve runtime vs 50%.
- **Failing cell with high self-discharge:** A damaged cell leaks charge even at idle, so the battery drains quickly regardless of use.
- **Old battery drivers misreporting:** Sometimes the drain is partly an illusion — the gauge drops fast but the actual energy use is normal.
- **Peripherals and radios:** External drives, Bluetooth, and Wi-Fi scanning all add constant drain.
- **Battery left at 100% for months:** A pack floated at full charge degrades faster, and the lost capacity shows up exactly as "won't hold charge."

## How to fix it

Work through these in order — measure first, then fix the drain, then judge the battery.

### Fix 1: Measure actual runtime vs capacity

Separate "drains fast" from "holds little."

1. Run `powercfg /batteryreport` in **Terminal (Admin)** and calculate wear: full charge capacity ÷ design capacity.
2. Above 80% capacity with short runtime: something is draining it — continue with the software fixes.
3. Below 60% capacity: the battery is the main story; software tweaks help only at the margins.
4. Note your real runtime from 100% to 20% under normal use as a baseline to compare against after fixes.

### Fix 2: Find the power hogs

Open Task Manager and follow the energy.

1. Press **Ctrl+Shift+Esc**, go to the **Processes** tab, and sort by **CPU** and **Power usage** — look for anything marked Very high.
2. Check **Settings > System > Power & battery** and expand **Battery usage** to see per-app consumption over the last 24 hours.
3. Common culprits: browsers with dozens of tabs, video calls, cloud sync tools stuck syncing, and Windows Update working in the background.
4. Close or uninstall the worst offenders, then re-measure runtime. If drain persists while plugged in too, see our guide to [batteries draining while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/).

### Fix 3: Fix the power settings

The defaults might be working against you.

1. Set **Settings > System > Power & battery > Power mode** to **Balanced** or **Best power efficiency**.
2. Lower screen brightness to 50–60% — use **Settings > System > Display** or the keyboard brightness keys.
3. In **Settings > System > Power & battery > Screen, sleep, & hibernate timeouts**, set aggressive timeouts: screen off after 3–5 minutes on battery.
4. Turn off keyboard backlighting when you don't need it; it's a bigger drain than people expect.

### Fix 4: Tame background activity

Stop the silent drain.

1. Go to **Settings > Apps > Installed apps**, and for apps you don't need running, set **Background app permissions** to **Never** (via the three-dot menu > Advanced options).
2. In **Settings > Windows Update**, check for stuck updates — pause updates for a week if one is looping.
3. Disable unnecessary startup apps in **Task Manager > Startup apps**.
4. Run `powercfg /sleepstudy` to see what's consuming power during sleep — overnight drain compounds the "won't hold charge" feeling. For the fast-drain variant, compare with [laptop battery drains fast](/articles/laptop-battery-drains-fast-windows-11/).

### Fix 5: Calibrate and retest

Make sure the fast drain isn't a gauge illusion.

1. Run a full calibration: charge to 100% (+2 hours), drain to auto-shutdown, rest off for hours, recharge uninterrupted.
2. Re-measure runtime from 100% to 20% after calibration.
3. If the reported drain rate improves, the gauge was exaggerating.
4. If runtime is unchanged, the drain is real — proceed to the battery verdict.

### Fix 6: Check for malware and system corruption

Rule out malicious drain.

1. Run a full scan in **Windows Security > Virus & threat protection**.
2. In **Terminal (Admin)**, run `sfc /scannow` to check for corrupted system files that could cause abnormal CPU usage.
3. Check **Task Manager > Performance > CPU** for sustained high usage at idle — a healthy idle laptop sits under 10%.
4. If idle CPU is pinned high with no visible process, check the **Details** tab sorted by CPU, and consider a clean boot to isolate it.

### Fix 7: Replace a worn battery

When the tank is the problem, get a bigger tank.

1. Confirm: capacity below 60–65% of design, calibrated, with settings optimized — and runtime still unacceptable.
2. Check warranty; premature wear is sometimes covered.
3. Buy a genuine battery for your exact model — capacity ratings on cheap packs are often fiction.
4. After installing, calibrate once and verify the new runtime. For the post-update variant of this problem, see [battery won't hold charge after Windows 11 update](/articles/how-to-fix-laptop-battery-won-t-hold-charge-after-windows-11-update/). General power guidance is also on [Microsoft's Windows support](https://support.microsoft.com/en-us/windows).

## Closing

A battery that won't hold charge is either being drained or worn out — and the battery report tells you which in thirty seconds. Kill the power hogs, fix the settings, calibrate the gauge, and if the capacity number is the problem, replace the pack. Runtime you can measure is runtime you can fix — so measure first, spend money later, and stop guessing entirely.
