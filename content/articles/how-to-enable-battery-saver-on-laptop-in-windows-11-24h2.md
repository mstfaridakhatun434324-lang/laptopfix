---
title: "How to Enable Battery Saver on Your Laptop in Windows 11"
slug: how-to-enable-battery-saver-on-laptop-in-windows-11-24h2
date: 2026-09-06
categories: ["battery"]
tags: ["battery saver", "power settings", "windows 11", "energy saver"]
description: "Battery Saver (Energy Saver) in Windows 11 24H2 can add serious runtime. Here's how to turn it on, automate it, and squeeze the most out of every charge."
thumbnail: "/images/thumbs/how-to-enable-battery-saver-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Where is Battery Saver in Windows 11 24H2?"
    a: "Go to Settings > System > Power & battery > Energy saver. In 24H2, Microsoft renamed and expanded Battery Saver to 'Energy saver' — it now works on desktops too and can run while plugged in. You can toggle it instantly from Quick Settings (Win + A) by clicking the battery icon."
  - q: "Does Battery Saver actually make a noticeable difference?"
    a: "Yes — typically 15-30% more runtime depending on your workload. It dims the screen slightly, throttles background activity, pauses OneDrive/Outlook sync, stops some background apps, and reduces visual effects. On light workloads like browsing and documents, the difference is very noticeable."
  - q: "Should I leave Energy Saver on all the time?"
    a: "On battery, yes — there's little downside for everyday tasks. While plugged in, it's optional; it slightly reduces performance and dims the screen. Many people set it to turn on automatically at 30-40% battery and leave it off when plugged in for full performance."
  - q: "What's the difference between Energy Saver and Best power efficiency mode?"
    a: "They stack. 'Best power efficiency' (in Power mode) mainly scales CPU performance. Energy Saver additionally restricts background activity, sync, and notifications. Using both together gives maximum runtime; using just Best power efficiency keeps full background functionality with moderate savings."
---

Your laptop's battery is draining faster than you'd like, and you've heard Battery Saver helps — but in Windows 11 24H2, Microsoft renamed it, moved things around, and added new options. If you're hunting through Settings for the old toggle, here's the current map: it's now called **Energy saver**, it lives in **Settings > System > Power & battery**, and it's more capable than the old Battery Saver ever was.

This guide shows you how to turn it on, automate it so you never think about it, and combine it with the other settings that actually move the needle on battery life.

## Why this happens (why your battery drains without it)

- **Background apps:** Mail, OneDrive, Teams, Spotify, and dozens of updaters keep the CPU and Wi-Fi active even when you're just reading a document.
- **Full screen brightness:** The display is the single biggest power draw on most laptops — often 40-60% of total consumption at full brightness.
- **High performance power mode:** The default Balanced/High performance modes let the CPU boost aggressively for trivial tasks.
- **Sync and notifications:** Constant email, cloud sync, and notification wake-ups prevent the CPU from entering deep idle states.
- **Visual effects and transparency:** Animations and acrylic effects keep the GPU awake.
- **Always-on radios:** Bluetooth, Wi-Fi scanning, and location services draw power continuously in the background.

## How to fix it

Work through these in order — each layer adds runtime.

### Fix 1: Turn on Energy Saver manually

The fastest win, taking ten seconds.

1. Press **Windows key + A** to open **Quick Settings**.
2. Click the **battery icon** (or the Energy saver tile if visible) to toggle **Energy saver** on immediately.
3. Alternatively, go to **Settings > System > Power & battery > Energy saver** and flip the toggle.
4. You'll notice the screen dim slightly and a small leaf icon on the battery indicator — that's your confirmation it's active.
5. Test your typical workload for an hour and note the battery drain rate versus before. Most people see the percentage dropping noticeably slower.

### Fix 2: Automate it — turn on automatically at a battery level

Manual toggling is forgettable. Automation is the real fix.

1. Go to **Settings > System > Power & battery > Energy saver**.
2. Find **Turn energy saver on automatically at** and set the slider to **30%** (a good balance) or **40%** if your battery is aging.
3. Below it, check **Lower screen brightness when using energy saver** — keep this on.
4. Decide on **Always use energy saver**: leave it **off** if you want full performance while plugged in, or turn it **on** to also save power (and reduce fan noise/heat) on AC.
5. From now on, Windows handles it: Energy saver kicks in at your threshold on battery and turns itself off when you plug in (unless you set Always on).

### Fix 3: Set the Power mode to Best power efficiency

Energy Saver and Power mode stack — use both on battery.

1. Go to **Settings > System > Power & battery**.
2. Find the **Power mode** dropdown and set it to **Best power efficiency**.
3. This caps CPU boost behavior. For browsing, Office, and video streaming you won't feel a difference; for gaming or rendering, switch back to Balanced/Best performance temporarily.
4. Windows 11 remembers power mode separately for battery vs plugged-in on many laptops — set **Best power efficiency** for On battery and **Balanced** for Plugged in.
5. Combined with Energy Saver, this pairing is the single biggest software-side battery improvement available.

### Fix 4: Tame background apps

Background activity is what Energy Saver throttles — you can also cut it directly.

1. Go to **Settings > System > Power & battery > Battery usage**.
2. Click **Battery usage by app** and sort by usage. Identify apps consuming power in the background that you don't need (updaters, launchers, chat apps you rarely open).
3. Go to **Settings > Apps > Installed apps**, click an app's **...** menu → **Advanced options**, and set **Background apps permissions** to **Never** for the worst offenders.
4. In **Settings > System > Notifications**, turn off notifications for apps you don't need pinging you — each wake-up costs power.
5. Pause OneDrive sync while on battery: click the OneDrive cloud icon → **Pause syncing** → **2 hours**. Our guide on [turning off background apps to save battery](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/) goes deeper on the biggest offenders.

### Fix 5: Reduce the display's power draw

The screen dwarfs everything else. Small changes here beat everything else combined.

1. Lower brightness to a comfortable minimum: **Settings > System > Display > Brightness**, or use the slider in Quick Settings (**Win + A**).
2. Enable **Change brightness automatically when lighting changes** if your laptop has an ambient light sensor.
3. Set a short screen timeout: **Settings > System > Power & battery > Screen and sleep** → **Turn off my screen after** → **2-3 minutes** on battery.
4. Enable **dark mode**: **Settings > Personalization > Colors > Choose your mode > Dark**. On OLED screens this saves significant power; on LCD it's minor but reduces eye strain.
5. Lower the refresh rate on battery: **Settings > System > Display > Advanced display** → **Choose a refresh rate** → **60Hz** instead of 120/144Hz. High refresh rates are a hidden battery killer.

### Fix 6: Trim radios, effects, and startup load

The remaining easy wins.

1. Turn off **Bluetooth** in Quick Settings when not using it.
2. Go to **Settings > Bluetooth & devices > Devices** and disable **Bluetooth device discovery** extras you don't need.
3. Reduce visual effects: search **"Adjust the appearance and performance of Windows"** → select **Adjust for best performance** (or uncheck animations and transparency manually).
4. Open **Task Manager** (**Ctrl + Shift + Esc**) → **Startup apps** tab → disable anything you don't need at boot (updaters, game launchers, chat clients).
5. In **Settings > Privacy & security > Location**, turn off location for apps that don't need it.
6. If battery still drains suspiciously fast even with all of this, run a diagnostic: our walkthrough on [fixing fast battery drain](/articles/how-to-fix-laptop-battery-drains-fast-in-windows-11-24h2/) helps identify rogue processes.

### Fix 7: Verify it's actually working

Don't assume — measure.

1. Charge to 100%, unplug, enable Energy saver + Best power efficiency, and use the laptop normally for one hour.
2. Note the percentage drop. Then repeat the same hour of use with Energy saver off.
3. Check **Settings > System > Power & battery > Battery usage** for the per-app breakdown to confirm background usage dropped.
4. For detailed numbers, run `powercfg /batteryreport` from an admin terminal and compare drain rates in the usage history.
5. If the improvement is under 10%, something is overriding the savings — usually a single misbehaving app (check Task Manager sorted by CPU) or the display at full brightness.

## Closing

Energy Saver in Windows 11 24H2 is genuinely effective — but only if it's actually on, automated, and paired with sensible brightness and background-app settings. Set the automatic threshold once, fix the two or three worst background offenders, and you'll stop thinking about your battery for most of the day.

*Related reading: [turn off background apps to save battery](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/), [battery drains fast](/articles/how-to-fix-laptop-battery-drains-fast-in-windows-11-24h2/)*
