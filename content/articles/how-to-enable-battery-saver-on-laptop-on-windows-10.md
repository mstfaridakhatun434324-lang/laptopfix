---
title: "How to Enable Battery Saver on a Windows 10 Laptop"
slug: how-to-enable-battery-saver-on-laptop-on-windows-10
date: 2026-10-09
categories: ["battery"]
tags: ["battery saver", "Windows 10", "power settings", "battery life"]
description: "Stretch your Windows 10 laptop's battery further. Learn every way to turn on Battery Saver and configure it to kick in automatically."
thumbnail: "/images/thumbs/how-to-enable-battery-saver-on-laptop-on-windows-10.webp"
faqs:
  - q: "Where is Battery Saver in Windows 10?"
    a: "The fastest way is the battery icon in the taskbar — click it and move the slider to Best battery life, or click the Battery saver tile in the Action Center (Win + A). For full settings, go to Settings > System > Battery and configure when it turns on automatically."
  - q: "What does Battery Saver actually change?"
    a: "Battery Saver reduces screen brightness by about 30 percent, stops most background app activity, pauses Windows Update downloads, disables push notifications for many apps, and throttles non-essential background tasks. Your apps keep working; they just sync and update less aggressively."
  - q: "Can Battery Saver turn on automatically?"
    a: "Yes. In Settings > System > Battery, tick 'Turn battery saver on automatically if my battery falls below' and choose a percentage — 20 percent is the default, but 30 or 40 percent gives you a longer cushion. It switches off automatically when you plug in."
  - q: "Does Battery Saver slow down my laptop?"
    a: "It can slightly reduce performance in demanding apps because background activity is throttled, but foreground apps generally run normally. For heavy work like video editing or gaming, plug in instead — Battery Saver is designed for light tasks like browsing, email, and documents."
---

Battery Saver is Windows 10's built-in emergency stretch mode. One toggle dims the screen, quiets background apps, and pauses update downloads — often buying you an extra hour or more when you're far from an outlet. Most people know it exists but never configure it, so it kicks in too late or not at all. Worse, many users confuse it with the taskbar power slider, which is a different control entirely.

Here's every way to turn it on and set it up so it actually helps.

## Why this happens

- **It's off by default at high charge:** Battery Saver only engages automatically below 20 percent unless you change the threshold.
- **Background apps eat the savings:** If nothing restricts background activity, Battery Saver's gains are partially cancelled out.
- **Screen brightness dominates drain:** The display is the single biggest consumer; Battery Saver's auto-dim is doing most of the work.
- **Confusion with power plans:** People tweak the legacy power plan slider while Battery Saver sits disabled, missing the bigger lever.
- **Notifications and sync keep firing:** Mail, chat, and cloud apps waking the system repeatedly undermine power savings.

## How to fix it

### Fix 1: Turn on Battery Saver right now

1. Click the **battery icon** in the taskbar notification area.
2. In the flyout, click the **Battery saver** tile to enable it immediately.
3. Alternatively, press **Win + A** to open the Action Center and click the **Battery saver** quick-action tile.
4. You'll see a small leaf icon over the battery icon confirming it's active.

### Fix 2: Set it to turn on automatically

1. Open **Settings > System > Battery**.
2. Tick **Turn battery saver on automatically if my battery falls below:**.
3. Move the slider to **30%** or **40%** instead of the default 20% — earlier activation saves noticeably more.
4. Untick **Lower screen brightness while in battery saver** only if you need full brightness; leave it on for maximum savings.

### Fix 3: Use the taskbar battery slider

1. Click the **battery icon** in the taskbar.
2. Drag the slider left toward **Best battery life**.
3. This is separate from Battery Saver — it adjusts the power/performance balance for normal use.
4. Combine both: slider at Best battery life for everyday use, Battery Saver as the emergency layer below your threshold.

### Fix 4: Restrict background apps

1. Go to **Settings > Privacy > Background apps**.
2. Turn off **Let apps run in the background** entirely, or toggle off individual apps you don't need live.
3. Keep essentials like your email or messaging app on if you rely on their notifications.
4. This amplifies Battery Saver because fewer apps compete to wake the system.

### Fix 5: Reduce the biggest drain — the display

1. Open **Settings > System > Display** and lower brightness manually to a comfortable minimum.
2. Set **Turn off display after** to 2-3 minutes under **Settings > System > Power & sleep** for battery mode.
3. Consider a dark theme and dark wallpaper — on OLED screens this saves real power.
4. Battery Saver already dims the screen, but starting from a lower baseline multiplies the effect.

### Fix 6: Pause Windows Update downloads

1. Battery Saver pauses most update downloads automatically while active.
2. To be sure, go to **Settings > Update & Security > Windows Update > Advanced options** and enable **Pause updates** when you're critically low.
3. Resume updates when you're back on AC power so you don't fall behind on security patches.

### Fix 7: Check what's still draining with the battery report

1. Open **Command Prompt as administrator** and run `powercfg /batteryreport`.
2. Open the report and look at recent drain rates — if an app still dominates, restrict it per Fix 4.
3. If the battery itself is worn, no saver setting will fix short runtime; check **Design Capacity** vs **Full Charge Capacity** in the report. Our guide on [finding which app is draining your battery](/articles/how-to-find-which-app-is-draining-battery-on-laptop/) walks through the detective work.

### Fix 8: Build a custom power plan for maximum savings

1. Open **Control Panel > Hardware and Sound > Power Options** and click **Create a power plan**.
2. Base it on **Power saver**, name it something like "Max Battery," and set aggressive timeouts: display off after 2 minutes, sleep after 5 minutes on battery.
3. Click **Change plan settings > Change advanced power settings** and set **Maximum processor state** to 80 percent on battery — this caps the biggest power draw with minimal noticeable slowdown for office work.
4. Switch to this plan manually (click the battery icon) whenever you need to stretch a low battery, alongside Battery Saver.

### Fix 9: Fix a missing or greyed-out Battery Saver option

1. If the Battery saver tile is missing from the Action Center, click **Expand** to show all tiles, then right-click any tile and choose **Edit** to add it back.
2. If the option is greyed out while plugged in, that's normal — Battery Saver is a battery-mode feature and can't engage on AC power.
3. On some systems a group policy disables it: press **Win + R**, type `gpedit.msc`, and check **Computer Configuration > Administrative Templates > System > Power Management** for anything set to Disabled.
4. If you're on a work laptop, your IT department may have locked power settings — check with them before changing policies.

## Closing

Battery Saver works best as a configured system, not a panic button: set the auto threshold to 30-40 percent, keep background apps trimmed, and run the taskbar slider at Best battery life day to day. Those three habits together can easily add an hour to a healthy battery. Check the settings once after every major Windows update, since feature updates sometimes reset power options to defaults. And remember — Battery Saver stretches what's there; if your battery is heavily worn, the real fix is a replacement, not a setting.

For Microsoft's official power-saving tips, see the [Windows battery support hub](https://support.microsoft.com/en-us/windows). If your battery drops fast even in light use, read [how to fix a laptop battery that drains while plugged in](/articles/how-do-i-fix-laptop-battery-drains-while-plugged-in/) to rule out charger problems.
