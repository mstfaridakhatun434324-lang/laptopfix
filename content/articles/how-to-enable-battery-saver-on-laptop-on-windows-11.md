---
title: "How to Enable Battery Saver on a Windows 11 Laptop"
slug: how-to-enable-battery-saver-on-laptop-on-windows-11
date: 2026-09-08
categories: ["battery"]
tags: ["battery saver", "energy saver", "windows 11", "power settings"]
description: "Enable and configure Energy saver on Windows 11: turn it on manually, set the automatic threshold, and get the most from every charge."
thumbnail: "/images/thumbs/how-to-enable-battery-saver-on-laptop-on-windows-11.webp"
faqs:
  - q: "Where is Battery saver in Windows 11?"
    a: "It's now called Energy saver. Find it in Settings > System > Power & battery > Energy saver, or toggle it instantly from Quick Settings (Win + A). It does the same job as the old Battery saver: throttling background activity to stretch remaining charge."
  - q: "What exactly does Energy saver do?"
    a: "It reduces background app activity and push notifications, lowers screen brightness slightly, throttles some sync operations, and applies more aggressive power management. You'll notice the biggest effect on idle and light-work drain — heavy tasks like gaming are less affected."
  - q: "Should I leave Energy saver on all the time?"
    a: "You can — many people do, with minimal noticeable impact on everyday tasks like browsing and office work. Turn it off temporarily when you need maximum performance or when background sync matters (large downloads, for example). The automatic threshold handles this for you — set it once and Energy saver engages without you remembering."
  - q: "Does Energy saver damage the battery or reduce its lifespan?"
    a: "No — it extends usable runtime per charge and slightly reduces heat and cycle depth, which is gentler on the battery. There's no downside for battery health; it's purely a power-management mode. In fact, by reducing heat and deep discharges, regular use is slightly kinder to long-term battery health."
---

Windows 11 renamed it "Energy saver," but it's the same lifeline the old Battery saver always was: one toggle that tells Windows to stop spending power you don't need to spend. It throttles background activity, dims the screen a touch, quiets notifications and sync — and can easily add an hour or more to a dwindling charge. Most people either don't know it's there or never configure it properly. Here's how to enable it, automate it, and get the most out of it.

## Why this happens (why you'd want it)

- **Background activity is the silent drain.** Even when you're just reading a document, dozens of apps sync, check, and refresh. Energy saver is the master switch that quiets them all at once.
- **The screen is the biggest consumer.** Energy saver's automatic brightness reduction targets the single hungriest component without you having to think about it.
- **Windows 11 is busier than you think.** Indexing, updates, telemetry, and maintenance tasks run in the background; Energy saver deprioritizes them on battery.
- **Manual toggling gets forgotten.** The real power of the feature is automation — having it kick in at 30% without you remembering. Most people who "tried it once" never set up the automatic trigger.
- **It stacks with other savings.** Energy saver plus trimmed [background apps](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/) plus sensible brightness multiplies the gains.
- **It's free runtime.** Unlike buying a bigger battery, this costs nothing and takes two minutes to configure.

## How to fix it

Work through these in order — each step builds on the last, from the immediate toggle to the automated setup.

### Fix 1: Turn on Energy saver manually right now

The immediate toggle for when the battery is low and you need help now.

1. Press **Win + A** to open **Quick Settings**.
2. Click the **battery icon** area, then toggle **Energy saver** on. (On some builds it's directly in the Quick Settings panel.)
3. Alternatively: **Settings** > **System** > **Power & battery** > **Energy saver** > toggle **On**.
4. You'll notice the screen dim slightly — that's normal and part of the savings.
5. Toggle it back off the same way when you're plugged in or need full performance.

### Fix 2: Set the automatic trigger

This is the configuration most people miss — make it automatic.

1. Go to **Settings** > **System** > **Power & battery** > **Energy saver**.
2. Find **Turn on energy saver automatically at** and set your threshold. **30%** is a good balance; **40%** if you're often far from outlets; **20%** if you want maximum performance until the last stretch.
3. You can also set it to **Always** — Energy saver stays on whenever you're on battery. Many users prefer this; the performance impact on everyday tasks is minimal.
4. Enable **Lower screen brightness when using energy saver** while you're here.
5. Test it: unplug, drain to your threshold (or just toggle manually), and confirm the leaf icon appears on the battery indicator.

### Fix 3: Combine it with the right power mode

Energy saver and power mode are teammates, not competitors.

1. Go to **Settings** > **System** > **Power & battery** > **Power mode**.
2. Set it to **Best power efficiency** for battery sessions. This keeps CPU clocks conservative, which Energy saver complements.
3. Avoid **Best performance** on battery unless you're doing something that genuinely needs it — it fights everything Energy saver is trying to do.
4. Remember that power mode is separate from Energy saver: you can run Best power efficiency with Energy saver off, or vice versa. For maximum runtime, use both.
5. Create the habit: Best performance when plugged in, Best power efficiency + Energy saver when not.

### Fix 4: Tame what Energy saver can't fully control

Energy saver throttles background activity, but per-app permissions are still yours to set.

1. Go to **Settings** > **Apps** > **Installed apps**. For apps you don't need live updates from, click the **three dots** > **Advanced options** > set **Background apps permissions** to **Never**.
2. In **Settings** > **Apps** > **Startup**, disable everything non-essential.
3. Pause **OneDrive** syncing (tray icon > **Pause syncing**) during critical low-battery stretches.
4. Our full walkthrough of [turning off background apps](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/) pairs perfectly with Energy saver.
5. After this cleanup, check **Battery usage** in a week — the worst offenders should be gone from the chart.

### Fix 5: Optimize the display alongside it

The screen dwarfs everything else; Energy saver's dimming is just the start.

1. Manually lower brightness to 60–70% for indoor use: **Settings** > **System** > **Display**.
2. Set screen-off timeout to 2–3 minutes on battery: **Settings** > **System** > **Power & battery** > **Screen, sleep, & hibernate timeouts**.
3. If your laptop has a 120Hz+ display, drop to 60Hz on battery via **Settings** > **System** > **Display** > **Advanced display**.
4. Turn off keyboard backlighting or set it to the dimmest level when on battery.
5. These display tweaks plus Energy saver routinely add 1–2 hours versus default settings.

### Fix 6: Verify it's actually engaging

Trust, but verify — especially the automatic trigger.

1. Drain (or manually toggle) to activate Energy saver and confirm the battery icon shows the saver state.
2. Open **Task Manager** and check that background CPU activity drops compared to saver-off.
3. If the automatic threshold never seems to kick in, double-check the setting in **Settings** > **System** > **Power & battery** > **Energy saver** — Windows updates occasionally reset it.
4. If Energy saver won't turn on at all or the toggle is greyed out, see [Battery saver not working](/articles/how-to-fix-battery-saver-not-working-on-laptop-in-windows-11-24h2/) for the troubleshooting sequence.
5. If runtime is still poor with everything enabled, the issue may be [fast battery drain](/articles/laptop-battery-drains-fast-windows-11/) from a deeper cause — investigate that next.

### Fix 7: Build the low-battery routine

Make Energy saver part of a habit, not a panic button.

1. Set the automatic threshold (Fix 2) and forget it — automation beats willpower.
2. Keep a mental "20% routine": brightness down, Energy saver confirmed on, heavy tabs closed, charger located.
3. In **Settings** > **System** > **Power & battery**, review **Battery usage** monthly to catch new drain offenders early.
4. Recalibrate the battery every few months so the percentage Energy saver triggers on is accurate.
5. The goal: you should rarely *notice* Energy saver working. It just quietly gives you the extra hour that gets you to an outlet.

Microsoft documents Energy saver behavior on the official [Windows support pages](https://support.microsoft.com/en-us/windows) if you want the full technical reference.

## Closing

Energy saver is the easiest battery win in Windows 11 — one toggle, one automatic threshold, and it just works in the background from then on. Enable it manually when you're in trouble, automate it so you never have to think about it, and pair it with sane brightness and background-app hygiene. It's not glamorous, but the extra hour it buys you, every single charge, adds up to days of recovered productivity over a laptop's lifetime.
