---
title: "How to Extend Laptop Battery Life on Windows 11 24H2"
slug: how-to-extend-laptop-battery-life-in-windows-11-24h2
date: 2026-09-12
categories: ["battery"]
tags: ["battery life", "windows 11 24h2", "power efficiency", "energy saver"]
description: "Running Windows 11 24H2 and want more hours per charge? Here's how to squeeze the most battery life out of your laptop with built-in settings."
thumbnail: "/images/thumbs/how-to-extend-laptop-battery-life-in-windows-11-24h2.webp"
faqs:
  - q: "What is Energy Saver in Windows 11 24H2 and should I use it?"
    a: "Energy Saver is Windows 11's battery-stretching mode that reduces background activity, lowers screen brightness slightly, and limits some visual effects. Turn it on at 20-30% battery (or always on battery) in Settings > System > Power & battery. It noticeably extends remaining runtime with minimal impact on everyday tasks."
  - q: "Does Windows 11 24H2 have better battery life than older versions?"
    a: "24H2 includes improved power management, including Energy Saver enhancements and better background task throttling. Most users see slightly better idle efficiency than 23H2, though the biggest gains still come from your own settings: brightness, power mode, and background apps."
  - q: "How much difference does the power mode actually make?"
    a: "A lot. Best power efficiency versus Best performance can mean the difference between 4 hours and 7 hours on the same laptop during light work. The CPU's ability to drop into deep idle states is the main factor — performance mode keeps clocks high even when you're just reading."
  - q: "Should I disable Wi-Fi and Bluetooth to save battery?"
    a: "Only if you're not using them. Modern Wi-Fi and Bluetooth radios sip power when idle, so toggling them off saves little unless they're actively transferring data. Airplane mode helps most when you're working offline for hours, since it also stops background sync attempts."
---

Windows 11 24H2 brought some genuine improvements to power management, but the operating system can only do so much on its own — most of your battery life is decided by your settings and habits. The good news is that a focused 15-minute tune-up can easily add an hour or more to your runtime, and you don't need any third-party tools.

This guide covers the settings that matter most in 24H2, in order of impact. Start at the top; the first three fixes deliver the majority of the gains.

## Why this happens

- **Display brightness too high** — the screen remains the largest power consumer on every laptop.
- **Best performance power mode** — prevents the CPU from entering deep idle states.
- **Background apps and sync services** — dozens of processes sipping power around the clock.
- **Energy Saver not enabled** — 24H2's best battery tool, left off by default.
- **High refresh rate display** — 120Hz+ panels draw noticeably more power than 60Hz.
- **Always-on connectivity** — Wi-Fi scanning, Bluetooth, and background sync while idle.

## How to fix it

Work through these in order of impact — the first three are the big wins.

### Fix 1: Set brightness sensibly and shorten the screen timeout

The display is your biggest lever:

1. Use **Win + A** to open quick settings and set brightness to **50–60%** for indoor use.
2. Go to **Settings > System > Power & battery > Screen, sleep, & hibernate timeouts** and set **Turn off my screen after** to **3–5 minutes** on battery.
3. If your laptop has an OLED screen, switch Windows and your apps to **dark mode** — dark pixels use dramatically less power on OLED.

On most laptops, dropping from full to half brightness alone buys 30–60 extra minutes.

### Fix 2: Use Best power efficiency mode

Go to **Settings > System > Power & battery** and set **Power mode** to **Best power efficiency** for battery use. This is the single most impactful software setting: it lets the CPU race to sleep between tasks instead of hovering at high clocks. Browsing, documents, and video calls all run fine in this mode — reserve **Best performance** for plugged-in heavy work like gaming or rendering. If your runtime is mysteriously short, check this first; Windows sometimes flips it after updates.

### Fix 3: Turn on Energy Saver

24H2's Energy Saver is more aggressive and smarter than the old Battery Saver:

1. Go to **Settings > System > Power & battery > Energy saver**.
2. Set **Turn energy saver on automatically at** to **30%** (or even 40% if you want earlier savings).
3. Toggle **Always use energy saver** when you know you'll be away from a charger all day.

Energy Saver trims background activity, sync frequency, and some visual effects. You'll barely notice it during normal work, but it stretches the last stretch of battery noticeably.

### Fix 4: Audit background apps and startup items

Background activity is death by a thousand cuts:

1. In **Settings > Apps > Installed apps**, open the **...** menu on apps you don't need live and set **Background app permissions** to **Never**.
2. Open **Task Manager** (**Ctrl + Shift + Esc**) > **Startup apps** and disable anything non-essential — cloud storage clients, chat apps, and updaters you can launch manually.
3. In **Settings > System > Power & battery > Battery usage**, check which apps consumed the most over the last 24 hours and address the surprises.

Fewer background processes means the CPU spends more time in deep sleep, which is where efficiency lives.

### Fix 5: Lower the refresh rate when on battery

A 120Hz or 144Hz panel looks smooth but costs power:

1. Go to **Settings > System > Display > Advanced display**.
2. Change **Choose a refresh rate** to **60Hz** when running on battery.

Some laptops offer **Dynamic refresh rate (DRR)** — enable it if available, since it drops to 60Hz automatically when you're not scrolling or gaming. If your display settings lack these options, your panel is fixed-rate and you can skip this step.

### Fix 6: Manage connectivity and sync

Radios and sync services add up over a long day:

1. Turn on **Airplane mode** (via **Win + A**) when working offline for extended periods.
2. In **Settings > Bluetooth & devices**, turn Bluetooth off if you're not using wireless peripherals.
3. Pause cloud sync (OneDrive, Dropbox) while on battery if you're not actively collaborating — right-click the tray icon and pause for a few hours.
4. In **Settings > Windows Update**, avoid downloading updates on battery; let them run while plugged in.

### Fix 7: Keep drivers current and check battery health

Outdated drivers can prevent proper idle states, silently costing you an hour:

1. Run **Windows Update** and install all updates including optional driver updates.
2. Grab fresh chipset and graphics drivers from your manufacturer's support site or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html).
3. Run `powercfg /batteryreport` and compare full charge capacity to design capacity — if wear is significant, no setting recovers lost capacity. Our guide to [checking battery health](/articles/how-to-check-battery-health-on-windows-11-laptop/) shows how to read the report.

### Fix 8: Consider a charge limit for desk-bound days

If your laptop spends most days plugged in, limiting the charge to 80% preserves long-term capacity, which protects your future battery life. Most manufacturers offer this in their companion app — see our guide on [limiting battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/) for per-brand instructions. A battery that holds its capacity longer is a battery that keeps giving you good runtime in year three.

One more habit that pays off: avoid letting the battery sit at 0% for days. Deep discharge followed by long storage at empty is one of the fastest ways to kill a lithium battery's capacity. If you're storing the laptop, leave it around 50% charged, and if you won't use it for weeks, top it up to half every month or so.

## Closing

Battery life on Windows 11 24H2 comes down to a handful of high-impact choices: moderate brightness, Best power efficiency mode, Energy Saver enabled, and background apps under control. Set those once and they keep paying off every day. Revisit the battery report every few months to make sure wear — not settings — isn't the reason your runtime is shrinking, and you'll get the most out of every charge for the life of the machine.
