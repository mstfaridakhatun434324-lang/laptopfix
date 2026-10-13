---
title: "How to Enable Adaptive Charging in Windows 11 24H2"
slug: how-to-enable-adaptive-charging-in-windows-11-24h2
date: 2026-09-28
categories: ["battery"]
tags: ["adaptive charging", "Windows 11 24H2", "battery longevity"]
description: "Windows 11 24H2 adds adaptive charging to protect your battery. Here's where to find it and how to turn it on."
thumbnail: "/images/thumbs/how-to-enable-adaptive-charging-in-windows-11-24h2.webp"
faqs:
  - q: "What is adaptive charging in Windows 11?"
    a: "It's a battery longevity feature that automatically limits charging — typically pausing around 80% — when the system detects the laptop stays plugged in most of the time. When your routine changes and you start using it on battery, it allows full 100% charges again. It reduces the chemical stress of sitting at full charge."
  - q: "Where is the adaptive charging setting in Windows 11 24H2?"
    a: "Go to Settings → System → Power & battery. On supported devices with 24H2, you'll find charging options under the Battery section — look for Adaptive charging or Battery charge options. Availability depends on your manufacturer supporting the feature in firmware; it's not present on every laptop."
  - q: "Why don't I see adaptive charging on my laptop?"
    a: "The feature requires both Windows 11 24H2 and manufacturer firmware support. Many laptops predate the feature or the OEM hasn't enabled it — in that case use the manufacturer's own tool instead (Lenovo Vantage, MyASUS, Dell Power Manager, Surface app). The Windows toggle simply won't appear on unsupported hardware."
  - q: "Should I use adaptive charging or a fixed 80% limit?"
    a: "Use adaptive if your routine varies — it gives you full capacity when you travel and protection when you're docked. Use a fixed 80% limit if your laptop almost never leaves the desk; it's simpler and the protection is constant. Either beats charging to 100% every day."
---

Windows 11's 24H2 update brought a genuinely useful battery feature: **adaptive charging**. Instead of a dumb fixed cap, Windows watches how you actually use the laptop. Desk-bound all week? It holds the charge around 80% to spare the cells. Heading out with it? It lets the battery fill to 100% so you get full runtime. It's the best of both worlds — if your laptop supports it and you can find the switch.

Here's where the setting lives, how to enable it, what to do when it's missing, and how it compares to the manufacturer tools you might already have.

## Why this happens

- **Firmware support is required.** Adaptive charging needs cooperation between Windows and the BIOS/EC firmware. Without OEM support, Windows can't control charging behavior.
- **The setting is easy to miss.** Microsoft placed it inside Power & battery settings without much fanfare, and its exact label varies by manufacturer implementation.
- **Manufacturer tools can conflict.** If Lenovo Vantage, MyASUS, or Dell Power Manager is already managing charge limits, the Windows toggle may be hidden or overridden.
- **Staged rollout.** Like many Windows features, adaptive charging reached different devices at different times through cumulative updates, not just the base 24H2 install.
- ** Misunderstanding the behavior.** Users enable it, see 100% after a trip, and assume it's broken — but allowing full charge when mobile is the feature working correctly.

## How to fix it

Work through these in order — confirm 24H2, find the setting, enable it, and handle the cases where it won't appear.

### Fix 1: Confirm you're actually on Windows 11 24H2

The feature doesn't exist on older builds.

1. Press **Win + R**, type `winver`, and press Enter.
2. Check the version: you need **Version 24H2** (OS Build 26100.x or later).
3. If you're on 23H2 or older, go to **Settings → Windows Update** and install the 24H2 feature update.
4. After updating, install all cumulative updates too — adaptive charging support was refined in post-24H2 patches. The [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) has the latest installation media if Windows Update is stuck.

### Fix 2: Find and enable adaptive charging

Now locate the actual toggle.

1. Go to **Settings → System → Power & battery**.
2. Look under the **Battery** section for **Battery charge options**, **Charging**, or **Adaptive charging** — the label depends on your OEM's implementation.
3. If you see an **Adaptive** option among choices like Off / Adaptive / Maximum lifespan (or similar), select **Adaptive**.
4. If there's only an on/off **Adaptive charging** toggle, turn it on.
5. Give it several days of your normal routine before judging — the system needs to observe your plugged-in patterns before it starts limiting. For the general concept across brands, see [how to limit battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/).

### Fix 3: Resolve conflicts with manufacturer tools

Two charge managers cause confusion.

1. Check your OEM utility: **Lenovo Vantage → Battery** (Conservation Mode / charge thresholds), **MyASUS → Battery Health Charging**, **Dell Power Manager → Battery Settings**, **Surface app → Smart Charging**, **HP BIOS → Battery Health Manager**.
2. Decide on ONE manager. If you prefer Windows adaptive charging, set the OEM tool to its neutral/standard mode (e.g., Lenovo's "Optimized battery charging" off, conservation mode off).
3. If you prefer the OEM tool (they're often more mature), leave Windows adaptive charging off instead.
4. After choosing, run one full charge cycle and observe which behavior actually applies — the winner is whichever cap engages.

### Fix 4: Update BIOS and drivers when the option is missing

No toggle often means old firmware.

1. Visit your manufacturer's support site — [Dell](https://www.dell.com/support) or [Lenovo](https://support.lenovo.com/us/en/) — and install the latest **BIOS** and **chipset/power management** drivers for your exact model.
2. Install the latest **BIOS** and **chipset/power management** drivers for your exact model.
3. Restart and recheck **Settings → System → Power & battery** for the charging options.
4. Some manufacturers added 24H2 adaptive charging support through BIOS updates months after the Windows release — it's worth checking even on 1–2 year old laptops.

### Fix 5: Verify it's actually working

Don't assume — observe.

1. Keep the laptop plugged in at your desk for 3–5 days of normal use.
2. Watch the battery percentage: when adaptive charging engages, it typically holds around 80% despite being plugged in.
3. Hover over the battery icon — some implementations show a status like "Plugged in, charging paused" or similar.
4. Then unplug and use it on battery for a day or two. Plug back in — the next charges should go toward 100% since the system saw mobile use. That's adaptation working, not a bug.
5. You can cross-check real behavior with `powercfg /batteryreport` — look at whether recent charges plateau at 80%. Our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) explains the usage graphs.

### Fix 6: Use the OEM alternative if Windows doesn't offer it

No toggle after all updates? Your hardware likely doesn't support the Windows implementation.

1. Use the manufacturer's tool instead — they all predate and mostly exceed the Windows feature: Lenovo Vantage charge thresholds, MyASUS Battery Health Charging, Dell Power Manager, Surface Smart Charging, HP BIOS Battery Health Manager.
2. These are arguably better anyway: Lenovo lets you set exact thresholds (e.g., start at 40%, stop at 80%).
3. Don't chase the Windows toggle further — it's a firmware limitation, not a settings problem.

### Fix 7: Report it if the toggle exists but does nothing

For the rare genuinely broken case:

1. Document behavior: screenshots of the setting enabled plus a battery report showing charges going to 100% despite a week of desk use.
2. Check **Settings → Windows Update** for any pending firmware/driver updates you missed.
3. Use the **Feedback Hub** (**Win + F**) to report it to Microsoft with your device model — include the screenshots.
4. Fall back to the OEM tool in the meantime; there's no reason to leave the battery unprotected while waiting.

## Closing

Adaptive charging in 24H2 is a quiet win for battery longevity — once you find it and give it a few days to learn your habits. Confirm the build, pick one charge manager (Windows or OEM, not both), and let it do its thing. Your battery's second year will look a lot more like its first.
