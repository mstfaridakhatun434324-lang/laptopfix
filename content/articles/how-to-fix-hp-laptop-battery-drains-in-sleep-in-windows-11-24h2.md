---
title: "Fix HP Laptop Battery Drain in Sleep on Windows 11 (24H2)"
slug: how-to-fix-hp-laptop-battery-drains-in-sleep-in-windows-11-24h2
date: 2026-09-22
categories: ["battery"]
tags: ["hp laptop", "sleep drain", "modern standby", "windows 11 24h2", "battery drain"]
description: "HP laptop losing 20%+ overnight in sleep on Windows 11 24H2? It's usually Modern Standby — here's how to tame it."
thumbnail: "/images/thumbs/how-to-fix-hp-laptop-battery-drains-in-sleep-in-windows-11-24h2.webp"
faqs:
  - q: "How much battery should sleep use overnight?"
    a: "Traditional sleep (S3) uses about 1-3% over 8 hours. Modern Standby (S0) — which most current HP laptops use — can burn 5-15% or more overnight because the system stays semi-active. Anything above 10% overnight deserves investigation."
  - q: "Why does my HP get warm in my bag while asleep?"
    a: "That's Modern Standby keeping the CPU and network active — email sync, updates, and background apps running while the lid is closed. A warm bag means the laptop never really slept, and it's draining battery the whole time."
  - q: "Should I use hibernate instead of sleep on my HP?"
    a: "For overnight or bag transport, yes. Hibernate writes RAM to disk and powers fully off, using essentially zero battery. Sleep is fine for short breaks at your desk. Setting the laptop to hibernate after 60-120 minutes of sleep gives you the best of both."
  - q: "Did Windows 11 24H2 make sleep drain worse on HP laptops?"
    a: "Many users report exactly that. Feature updates can reset power plans, re-enable wake timers, and reinstall network drivers with aggressive wake settings. HP's own firmware updates around the same time changed standby behavior on several models too."
---

You close your HP's lid at 80%, toss it in your bag, and open it the next morning at 58% — and it's faintly warm, like it spent the night thinking instead of sleeping. This is the classic Modern Standby problem, and HP laptops on Windows 11 24H2 seem especially prone to it.

Here's the uncomfortable truth: on most modern HPs, "sleep" isn't really sleep. It's S0 Modern Standby, a low-power idle state where Windows keeps doing things — syncing mail, checking updates, keeping the network alive. Done right it's convenient. Done wrong it's a space heater in your backpack. Let's fix it.

## Why this happens

- **Modern Standby (S0) keeps the system semi-awake.** Unlike old S3 sleep, the CPU, Wi-Fi, and apps remain active enough to drain 1-2% per hour.
- **Network connectivity during standby.** "Connected standby" lets apps sync overnight — great for a phone, terrible for a laptop in a bag.
- **Wake timers and scheduled tasks** fire during the night: Windows Update, maintenance, HP's own utilities.
- **USB devices keep the system awake.** Docks, receivers, and external drives can prevent deep idle.
- **A misbehaving driver blocks low-power states.** Audio, network, and graphics drivers that won't idle properly keep power draw high — check with `powercfg /sleepstudy`.
- **HP's 24H2-era firmware or driver updates** changed default standby behavior or re-enabled aggressive wake settings.
- **Background apps with no restraint.** Browsers, launchers, and sync tools doing real work while the lid is closed.

## How to fix it

Work through these in order. The sleep study report in Fix 1 tells you exactly where your power is going.

### Fix 1: Run a sleep study to see what's actually happening

Don't guess — Windows logs every sleep session in detail.

1. Open **Terminal (Admin)** from **Win + X**.
2. Run `powercfg /sleepstudy`. Open the generated report at `C:\Windows\System32\sleepstudy-report.html`.
3. Look at the overnight sessions. The report shows **% Active** time, top power offenders by component (screen-off, networking, audio), and which devices blocked deep idle.
4. Pay special attention to the **"Top Offenders"** list — it names the exact drivers and devices burning power. A network driver at the top means Fix 3 is your fix; an audio driver means Fix 4.
5. Also run `powercfg /lastwake` to see what most recently woke the machine.
6. If you'd rather identify the apps behind the drain, [find which app is draining your battery](/articles/how-can-i-find-which-app-is-draining-battery/) walks through Battery Usage in Settings.

### Fix 2: Make sleep actually sleep — disable connected standby networking

The single biggest standby power saver on most HPs.

1. Go to **Settings → System → Power & battery → Screen, sleep, & hibernate timeouts** (expand it).
2. Find the standby network setting. On Windows 11 24H2 it's under **Settings → System → Power & battery** — look for **"When my PC is asleep and on battery power, disconnect from the network"** or in advanced power settings: **Control Panel → Power Options → Change plan settings → Change advanced power settings → Sleep → Allow network connectivity during connected-standby** → set **On battery** to **Disable**.
3. This stops mail sync, OneDrive, and update checks from running all night on battery.
4. Test overnight. Many users see drain drop from 15% to 3-4% from this change alone.

### Fix 3: Stop wake timers and scheduled tasks

Something waking the laptop at 3 AM undoes all your standby savings.

1. In advanced power settings (**Control Panel → Hardware and Sound → Power Options → Change plan settings → Change advanced power settings**), expand **Sleep → Allow wake timers** and set **On battery** to **Disable**.
2. Open **Device Manager** (**Win + X**), expand **Network adapters**, right-click your Wi-Fi adapter → **Properties → Power Management**, and untick **Allow this device to wake the computer**.
3. Do the same for USB input devices you don't need as wake sources.
4. Open **Task Scheduler**, navigate to **Task Scheduler Library → Microsoft → Windows → UpdateOrchestrator**, and for tasks like **Reboot**, open **Properties → Conditions** and untick **Wake the computer to run this task**.
5. Check HP's own scheduled tasks too — **Task Scheduler Library → HP** — and disable wake conditions on anything non-essential.

### Fix 4: Update the drivers that block deep idle

The sleep study's offender list points here.

1. Identify the top offender driver from your sleep study (common culprits: Realtek audio, Intel/Realtek/MediaTek Wi-Fi, NVIDIA graphics).
2. Go to [HP Support](https://support.hp.com/us-en), enter your model, and install HP's latest versions of exactly those drivers — HP tests them against your firmware.
3. For Intel Wi-Fi/Bluetooth, Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is a reliable second source.
4. Restart and run another overnight sleep study to confirm the offender is gone.

### Fix 5: Set hibernate to take over after sleep

The pragmatic compromise: fast sleep for short breaks, true hibernate for the long haul.

1. Open advanced power settings as in Fix 2.
2. Expand **Sleep → Hibernate after**. Set **On battery** to **60 or 120 minutes**, **Plugged in** to **180 minutes** or **Never**.
3. Make sure hibernate is enabled: in admin Terminal, run `powercfg /hibernate on`.
4. Also check **Power buttons and lid → Lid close action** — set **On battery** to **Sleep** (hibernate-after will still kick in later).
5. If hibernate itself drains battery, see our guide on [battery drain in hibernate](/articles/how-to-fix-laptop-battery-drains-in-hibernate-in-windows-11-24h2/).

### Fix 6: Tame background apps and HP utilities

Fewer things running means less for standby to keep alive.

1. Go to **Settings → Apps → Installed apps**. For browsers, launchers, and sync tools you don't need overnight, open **⋯ → Advanced options → Background apps permissions → Never**.
2. Open **Task Manager → Startup apps** and disable anything non-essential — fewer startup apps means fewer background residents.
3. Check HP utilities (HP Support Assistant, HP Command Center / OMEN Gaming Hub): open their settings and disable background monitoring and automatic wake/scan features you don't use.
4. In **Settings → System → Power & battery → Battery saver**, set it to turn on automatically at 30-40% so the system clamps background activity when charge gets low.

### Fix 7: Update BIOS and reset HP power defaults

HP firmware updates regularly adjust standby behavior.

1. On [HP Support](https://support.hp.com/us-en), install the latest **BIOS** for your exact model (keep the charger plugged in during the flash).
2. After updating, enter BIOS (**Esc** at boot → **F10**), load **Setup Defaults**, save, and exit.
3. Back in Windows, re-apply Fixes 2 and 3 — BIOS updates can reset Windows power settings.
4. Run one final overnight test with the lid closed and nothing plugged in except... nothing. The laptop should be cool and the battery nearly untouched in the morning.

## Closing

Sleep drain on HP laptops is Modern Standby doing exactly what it was designed to do — just far too enthusiastically. Disconnect the network during standby, kill the wake timers, update the offending drivers, and let hibernate take over after an hour or two. Your bag will stay cool, and your morning battery will match your nighttime battery.
