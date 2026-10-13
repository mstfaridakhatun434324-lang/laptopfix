---
title: "Critical Battery Alarm Not Working on Windows 11 24H2? Fix It"
slug: how-to-fix-critical-battery-alarm-not-working-in-windows-11-24h2
date: 2026-09-06
categories: ["battery"]
tags: ["battery", "alarm", "notification", "windows 11 24h2"]
description: "No low or critical battery warning on Windows 11 24H2? Restore your battery alarms with these 7 fixes."
thumbnail: "/images/thumbs/how-to-fix-critical-battery-alarm-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is there no low battery warning on Windows 11 24H2?"
    a: "The usual causes are notification settings blocking the alert, the low/critical battery levels being set to 0 or disabled in the power plan, a corrupted power scheme from the 24H2 upgrade, or the critical battery action being misconfigured. The alert system is still there — it's just muted or misconfigured."
  - q: "Where are battery alarm settings in Windows 11?"
    a: "They live in the advanced power plan settings: Control Panel > Hardware and Sound > Power Options > Change plan settings > Change advanced power settings, then expand the Battery section. There you'll find Low battery level, Critical battery level, Low battery notification, and Low/Critical battery action."
  - q: "What's the difference between low and critical battery alarms?"
    a: "Low battery (default around 10%) triggers a notification warning you to plug in. Critical battery (default around 5%) triggers the critical action — sleep, hibernate, or shutdown — to protect against data loss from a dead battery. Both are configurable."
  - q: "Can I make the critical battery alarm louder or more noticeable?"
    a: "Windows doesn't offer volume control for the battery alarm specifically, but you can make it more noticeable by setting the critical battery action to Hibernate (which visibly saves your session), keeping notification banners enabled, and setting the low battery level higher (like 15%) for earlier warning."
---

Your laptop used to warn you at 10% and take protective action at 5%. Now on Windows 11 24H2, it just... dies. No notification, no alarm, no automatic sleep — one moment you're working, the next the screen is black and your unsaved work is gone. The battery alarm system didn't disappear; the 24H2 upgrade muted or misconfigured it.

Windows 11 buried these settings deeper than Windows 10 did, which is why most people never find the actual controls. The alarm pipeline has four stages — level thresholds, notification permission, the notification itself, and the critical action — and a break at any stage silences everything. These seven fixes walk the pipeline from end to end. The whole repair takes about fifteen minutes, and the peace of mind is worth far more.

## Why this happens

- **Notification settings blocking the alert.** 24H2's notification system can suppress the battery warning if notifications are muted, Focus is on, or the alert was dismissed permanently.
- **Power plan levels set to zero or Never.** The upgrade can migrate the low/critical battery levels to 0%, which effectively disables the alarms.
- **A corrupted power scheme.** The 24H2 upgrade sometimes damages the advanced power settings, leaving the Battery section nonfunctional.
- **The critical battery action misconfigured.** If the critical action got set to "Do nothing," the laptop takes no protective action at 5% and simply dies.
- **Fast startup interfering with level detection.** A stale hibernation state can confuse the battery-level monitoring service.
- **Third-party "gaming" or "performance" utilities overriding plans.** Vendor tools can replace the Windows power plan with one that lacks alarm settings entirely.

## How to fix it

Work through these in order.

### Fix 1: Check notification settings first

The alarm may be firing into a muted notification system.

1. Open **Settings > System > Notifications** and make sure notifications are **On**.
2. Scroll down and verify **Focus** (Do Not Disturb) isn't permanently enabled — check its automatic rules too.
3. Look for any battery or power-related entries in the notification senders list and ensure they're allowed to show banners.
4. Drain the battery to the low level (or temporarily set the low level high — see Fix 2) and confirm the banner appears.

### Fix 2: Set the low and critical battery levels

The thresholds themselves may be zeroed out.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **Battery**. Set **Low battery level** (On battery) to **10%** and **Critical battery level** to **5%**.
4. Set **Low battery notification** to **On**.
5. If the Battery section is missing entirely, your power scheme is corrupted — skip to Fix 4.

### Fix 3: Configure the low and critical battery actions

The alarm without an action is just a suggestion the laptop ignores.

1. In the same **Advanced power settings > Battery** section, find **Critical battery action**.
2. Set **On battery** to **Hibernate** — this saves your entire session to disk before the battery dies.
3. Set **Low battery action** to **Do nothing** (the notification is enough at the low stage).
4. Click **Apply** and **OK**.
5. Test: let the battery fall to the critical level and confirm the laptop hibernates instead of dying. Hibernate is safer than Sleep here because sleep still drains the battery.

### Fix 4: Restore the default power schemes

When the Battery section is missing or the settings won't stick, rebuild the schemes.

1. Open **Terminal (Admin)** and run `powercfg -restoredefaultschemes`.
2. Restart the laptop.
3. Reopen **Advanced power settings** and verify the **Battery** section is back with sensible defaults.
4. Reconfigure your low/critical levels and actions as in Fixes 2–3.
5. If a vendor utility (Lenovo Vantage, Armoury Crate) immediately re-applies its own plan, configure the alarms inside that utility's plan too — vendor documentation at [Lenovo](https://support.lenovo.com/us/en/), [Dell](https://www.dell.com/support), or [HP](https://support.hp.com/us-en) explains how their plans interact with Windows settings.

### Fix 5: Check the notification with a manual test

Don't wait for a real low-battery event to discover it's still broken.

1. In **Advanced power settings > Battery**, temporarily set **Low battery level** to **90%**.
2. Unplug the charger and wait a minute — the low battery notification should appear.
3. Once confirmed, set the level back to **10%**.
4. This five-minute test saves you from discovering a still-broken alarm during actual important work.

### Fix 6: Disable fast startup

A stale hybrid-shutdown state can break battery-level monitoring.

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and save.
4. Shut down fully and boot fresh. The battery monitoring service now starts clean every boot. This also helps with [overnight battery drain issues](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-11/), and if the saver itself misbehaves, see [how to fix Battery Saver not working on 24H2](/articles/how-to-fix-battery-saver-not-working-on-laptop-in-windows-11-24h2/).

### Fix 7: Create a custom alarm with Task Scheduler (belt and suspenders)

If the built-in alarm stays unreliable, build your own that can't be silenced.

1. Open **Task Scheduler** (search it in Start) and create a basic task named "Battery Low Warning."
2. Set the trigger to **On an event**, with log **System**, source **Kernel-Power** — or simpler: trigger **When the computer is on battery** via the Conditions tab.
3. For the action, choose **Display a message**... note: modern Windows removed the message action, so instead set the action to run `msg * "Battery low - plug in now!"`.
4. Alternatively, use a PowerShell script action that plays a sound and shows a toast notification at your chosen level.
5. This independent alarm fires regardless of power-plan corruption.

## Closing

A silent battery alarm turns every low-battery situation into a potential data-loss event. The fix is almost always in the advanced power settings — restore the levels, enable the notification, set hibernate as the critical action — and verify with the 90% test. Once the laptop warns you and hibernates gracefully at 5%, the safety net is back. Don't skip the verification test; an alarm you haven't tested is an alarm you can't trust. Five minutes with the temporary 90% threshold confirms the whole pipeline works — and you'll never again discover a dead alarm at the worst possible moment.
