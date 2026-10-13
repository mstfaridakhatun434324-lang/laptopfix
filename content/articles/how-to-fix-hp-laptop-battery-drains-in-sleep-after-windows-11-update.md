---
title: "HP Laptop Draining Battery in Sleep Mode After the Windows 11 Update? Fix It"
slug: how-to-fix-hp-laptop-battery-drains-in-sleep-after-windows-11-update
date: 2026-09-02
categories: ["battery"]
tags: ["hp", "sleep drain", "modern standby", "windows 11 update"]
description: "Your HP laptop loses serious battery in sleep mode since the Windows 11 update? Find what's keeping it awake and fix sleep drain."
thumbnail: "/images/thumbs/how-to-fix-hp-laptop-battery-drains-in-sleep-after-windows-11-update.webp"
faqs:
  - q: "Why does my HP laptop lose battery in sleep mode after the Windows 11 update?"
    a: "Modern Standby keeps the system in a light sleep where network, USB, and background apps stay active. The update can re-enable wake timers, reset network-during-standby settings, or install drivers that prevent deep sleep. HP's own utilities (like HP Support Assistant updates) can also wake the machine."
  - q: "How much battery drain in sleep is normal?"
    a: "One to two percent over 8 hours is normal for Modern Standby. Five percent or more — or a hot laptop in your bag — means something is preventing proper sleep. Run powercfg /sleepstudy to see the drain rate hour by hour."
  - q: "Should I use hibernate instead of sleep on my HP laptop?"
    a: "If sleep drain resists fixing, hibernate is an excellent workaround: it writes RAM to disk and powers off fully, using zero battery. Enable it in Power Options and set the laptop to hibernate after 30–60 minutes of sleep."
  - q: "Can HP Support Assistant cause sleep drain?"
    a: "Its scheduled hardware scans and updates can wake the laptop, yes. Open HP Support Assistant, go to settings, and reschedule or disable automatic tasks that run while on battery."
---

You close the lid at 90%. A few hours later you open it and you're at 71% — or worse, the laptop is warm inside your bag, fan vents blowing hot air into your backpack like it never slept at all. That warmth is the giveaway: a properly sleeping laptop is stone cold. Since the Windows 11 update, your HP's "sleep" is more of a light doze with one eye open — technically asleep, practically browsing.

Sleep drain on HP laptops usually traces to Modern Standby (S0 low-power idle), where Windows stays semi-awake handling network and background tasks. The update loves to reset the settings that keep this behavior in check. The fixes below are HP-flavored: the right report commands, the HP-specific wake sources, and the hibernate fallback that makes the whole problem moot. For drain when fully [shut down](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-11/) instead of sleeping, that's a different hunt with different culprits.

## Why this happens

- **Modern Standby stays too active.** S0 sleep keeps Wi-Fi and background apps alive; the update can crank up what's allowed to run.
- **Wake timers re-enabled.** Windows Update and maintenance tasks get fresh permission to wake the machine after a feature update.
- **Network stays connected during standby.** "Stay connected to Wi-Fi while asleep" means the radio never rests.
- **HP Support Assistant scheduled tasks.** Automatic tune-ups and update checks wake the laptop on their own schedule.
- **USB devices preventing deep sleep.** An attached mouse, drive, or dock can hold the system in a lighter sleep state.
- **Outdated network or audio drivers.** The update sometimes leaves drivers that don't support the deepest sleep states, so the machine hovers in light sleep.
- **Fast Startup interacting with sleep.** The hybrid shutdown cache can confuse sleep/wake transitions after the update.
- **Bluetooth devices waking the system.** A paired mouse or headphones can wake the laptop when they reconnect or send signals. In Device Manager, check Bluetooth radios' Power Management tabs and disable wake privileges.

## How to fix it

Work through these in order.

### Fix 1: Generate a sleep study to see the drain

1. Open **Terminal (Admin)** and run `powercfg /sleepstudy`.
2. Open the HTML report and find last night's sleep session.
3. Check the **Drain rate** (% per hour) and the **Top offenders** list — it names exactly what's eating power, down to the specific device or app.
4. A drain rate above 1% per hour with the lid closed needs fixing; note the specific offenders before changing anything, so you can confirm the fix worked later.

### Fix 2: Disconnect Wi-Fi during standby

1. Open **Settings > System > Power & battery > Screen, sleep & hibernate timeouts** (or **Power mode** section on some builds).
2. Find **Network connection in standby** / **Stay connected to Wi-Fi while asleep** and set it to **Never** or **Disconnect**.
3. Alternatively, turn on **Airplane mode** before closing the lid as a nightly habit — one click, same effect.
4. Retest one sleep session — network activity is the single biggest Modern Standby drain, and this test isolates it cleanly.

### Fix 3: Disable wake timers

1. Open **Control Panel > Hardware and Sound > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **Sleep > Allow wake timers** → **Disable** for both On battery and Plugged in.
3. Run `powercfg /waketimers` in an elevated terminal to audit what's scheduled.
4. In Task Scheduler, neuter the worst offenders' wake permissions under **Conditions**.

### Fix 4: Tame HP Support Assistant

1. Open **HP Support Assistant** from the Start menu.
2. Go to **Settings** (gear icon) and review scheduled tune-ups and updates.
3. Set them to run only when plugged in, or disable automatic tasks and run them manually monthly.
4. Check [HP's support site](https://support.hp.com/us-en) for updated Assistant and driver versions — old builds are worse behaved.

### Fix 5: Update network, audio, and chipset drivers

1. In **Device Manager**, update your Wi-Fi adapter, audio device, and chipset drivers.
2. Better: download HP's driver pack for your exact model from HP support — HP validates sleep behavior per model, which generic drivers don't.
3. Pay special attention to the Wi-Fi driver version; HP's release notes often mention standby power fixes explicitly.
4. Restart after installing.
5. Drivers that don't support deep idle states are a classic post-update sleep drain cause.

### Fix 6: Unplug USB devices before sleep

1. Disconnect external drives, docks, and USB hubs before closing the lid.
2. In **Device Manager > Universal Serial Bus controllers**, open each **USB Root Hub > Properties > Power Management** and enable **Allow the computer to turn off this device to save power**.
3. Wireless mouse dongles are notorious sleep-blockers — unplug the dongle, not just the mouse.
4. Retest with nothing attached.

### Fix 7: Set up hibernate as the safety net

1. Open **Terminal (Admin)** and run `powercfg /h on` to ensure hibernation is available.
2. Go to **Control Panel > Power Options > Choose what closing the lid does** and set **On battery** to **Hibernate** (keep Plugged in on Sleep if you like — drain doesn't matter on wall power).
3. In advanced power settings, expand **Sleep > Hibernate after** and set 60 minutes on battery.
4. Hibernate uses zero power — even if sleep misbehaves, the laptop lands safely in hibernate within the hour, and your morning percentage matches your evening one. If sleep drain turns out to be a [worn battery](/articles/laptop-battery-drains-fast-windows-11/) amplifying normal drain, hibernate masks that too — though the underlying wear still deserves attention eventually, before it becomes a shutdown-without-warning problem.

## Closing

HP sleep drain after an update is Modern Standby doing too much while you're not looking. The sleep study report shows you exactly what, and the fixes — Wi-Fi off in standby, wake timers dead, HP Assistant tamed, hibernate as backup — put sleep back to sleep. Your bag should be cool and your percentage should barely move; anything else means something is still awake in there, and now you know how to find it.
