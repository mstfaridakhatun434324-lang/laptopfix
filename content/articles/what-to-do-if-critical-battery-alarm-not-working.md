---
title: "What to Do If the Critical Battery Alarm Is Not Working"
slug: what-to-do-if-critical-battery-alarm-not-working
date: 2026-09-12
categories: ["battery"]
tags: ["critical battery", "alarm", "notification", "power plan", "low battery"]
description: "No warning before your laptop dies? Here is how to fix the critical battery alarm and low battery notifications when they stop working."
thumbnail: "/images/thumbs/what-to-do-if-critical-battery-alarm-not-working.webp"
faqs:
  - q: "Why doesn't my laptop warn me before the battery dies?"
    a: "The usual reasons are the notification being disabled in the power plan's advanced settings, the critical battery level set too low for the alarm to trigger in time, or Windows notification settings muting system alerts. On some machines, Do Not Disturb or a muted system volume also swallows the warning."
  - q: "Where are the critical battery settings in Windows 11?"
    a: "They live in the classic power plan settings: Control Panel, Hardware and Sound, Power Options, Change plan settings, Change advanced power settings, then expand Battery. There you will find low and critical battery levels, notifications, and the critical battery action for each power plan."
  - q: "My laptop hibernates without any warning. How do I get the warning back?"
    a: "Set the low battery notification to On and the low battery level a few points above the critical level, so the warning fires first. For example, low at 15 percent with notification on, and critical at 7 percent with hibernate as the action. That gap is what gives you time to react."
  - q: "Does the critical battery alarm make a sound?"
    a: "It can. The notification appears as a system alert, and whether you hear it depends on your volume and sound scheme. If you need an audible warning, make sure system sounds are not muted and notifications are allowed to play sounds in Settings, System, Notifications."
---
The critical battery alarm exists for one job: giving you a few minutes of warning before the laptop gives up. When it stops working, the machine just blinks out mid-sentence with no warning at all, and unsaved work goes with it. The alarm is controlled by a small stack of settings across the power plan, notifications, and sound, and any one of them can silently break it.

Here is how to check each layer and get your warning back.

## Why this happens

- **The notification is disabled in the power plan.** The low and critical battery notifications can be toggled off per plan, and a plan switch can inherit the wrong state.
- **Thresholds are set badly.** If the critical level is nearly the same as the low level, or both are set to 3 percent, there is no room for a warning.
- **Do Not Disturb is swallowing alerts.** Focus settings can suppress the notification visually while the battery keeps draining.
- **System sounds are muted.** If the alarm is configured but volume is at zero, you will never hear it.
- **A corrupted power plan.** Damaged schemes can carry notification settings that the UI cannot display or change.
- **Group policy overrides.** Managed machines can have battery notifications forced off by policy.
- **Fast shutdown on worn batteries.** A badly degraded battery can plunge from 10 percent to zero faster than the alarm polling interval, so no warning ever fires.

## How to fix it

Work through these in order, testing with a controlled drain at the end.

### Fix 1: Enable the notifications in advanced power settings

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **Battery**. Set **Low battery notification** to **On** for both **On battery** and **Plugged in**.
4. Set **Critical battery notification** to **On** for **On battery**.
5. Set **Low battery level** to 15 percent and **Critical battery level** to 7 percent on battery. The gap between them is your warning window.
6. Set **Critical battery action** to **Hibernate** on battery, so even if you miss the alarm, your work is preserved.
7. Click **Apply**, then repeat for every power plan you use, since each plan carries its own settings. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document these options if your dialog looks different.

### Fix 2: Allow system notifications and sounds

1. Open **Settings > System > Notifications** and make sure **Notifications** is turned on.
2. Scroll down and confirm system and power-related notifications are allowed to show banners and play sounds.
3. Check the volume mixer: right-click the speaker icon, open **Volume mixer**, and make sure **System sounds** is not muted or at zero.
4. Turn off **Do Not Disturb** (the bell icon in the taskbar corner) while testing, since it can suppress the low battery banner.

### Fix 3: Check the sound scheme

1. Open **Control Panel > Hardware and Sound > Sound**, then the **Sounds** tab.
2. Make sure a sound scheme with actual sounds is selected, not **No Sounds**.
3. Scroll the program events list for **Critical Battery Alarm** and **Low Battery Alarm**. Click **Test** on each to confirm they play.
4. If they are silent, assign any WAV sound you like. A distinct, impossible-to-ignore tone works best for something this important.

### Fix 4: Reset the power plans

1. Press **Win + R**, type `cmd`, then press **Ctrl + Shift + Enter** for an elevated prompt.
2. Run `powercfg -restoredefaultschemes` to rebuild all plans from defaults.
3. Restart, then redo Fix 1's notification settings on the fresh plan.
4. Corrupted plans can show notifications as enabled while actually suppressing them. A reset clears that invisible state.

### Fix 5: Rule out group policy

1. Press **Win + R**, type `gpedit.msc`, and press Enter (skip on Windows Home).
2. Navigate to **Computer Configuration > Administrative Templates > System > Power Management > Notification Settings**.
3. Set any battery notification policies to **Not Configured**.
4. Run `gpupdate /force` in an elevated Command Prompt and restart. On a work or school machine, IT may need to make this change.

### Fix 6: Address the underlying battery health

1. If the battery plunges from 15 percent to dead in under a minute, no alarm setting can warn you in time.
2. Run `powercfg /batteryreport` in an elevated Command Prompt and compare full charge capacity against design capacity.
3. On a worn battery, raise your thresholds: set the low level to 25 percent and critical to 12 percent to buy back warning time.
4. Consider a replacement if capacity is under 60 percent of design. An honest battery gives the alarm time to do its job. If the machine also [drains while plugged in](/articles/how-to-fix-laptop-battery-drains-while-plugged-in-in-windows-11-24h2/), fix that first, since it distorts every threshold.

### Fix 7: Test the alarm with a controlled drain

1. Unplug the charger at around 30 percent and use the laptop normally while watching the percentage.
2. Confirm the low battery notification appears at your set level and the critical alarm fires at its level.
3. If the alarm appears but makes no sound, revisit Fix 3. If nothing appears at all, recheck Fix 1, making sure you edited the active plan.
4. Once verified, plug back in. You now have a tested warning system instead of a hopeful one.

## Closing

The critical battery alarm is a small feature with an outsized job, and it usually breaks for boring reasons: a notification toggled off, thresholds set too tight, or sounds muted. Set the levels with a real gap between them, make sure notifications and sounds can actually fire, and test it once with a controlled drain. If your machine tends to lose charge while supposedly asleep, also look into [overnight battery drain](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-step-by-step/), since starting each day at a deficit makes every threshold less forgiving. Then the next time your battery runs low, you will get the warning you were promised instead of a black screen.
