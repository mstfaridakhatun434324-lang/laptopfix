---
title: "How to Enable Battery Saver on Your Laptop (The Right Way)"
slug: best-way-to-enable-battery-saver-on-laptop
date: 2026-09-17
categories: ["battery"]
tags: ["battery saver", "power settings", "windows 11"]
description: "Battery Saver can add real runtime — if it's set up right. Here's how to enable it, tune the threshold, and fix it when it won't turn on."
thumbnail: "/images/thumbs/best-way-to-enable-battery-saver-on-laptop.webp"
faqs:
  - q: "What does Battery Saver actually do?"
    a: "It reduces background activity, lowers screen brightness slightly, throttles background app updates, and limits some visual effects and push notifications. On most laptops it adds 30-60 minutes of runtime, more if your normal usage has lots of background activity."
  - q: "Should I leave Battery Saver on all the time?"
    a: "You can, but you'll notice dimmer screens and delayed notifications. The sweet spot for most people is automatic activation at 30 percent — full performance when you have charge, conservation when it matters."
  - q: "Does Battery Saver damage the battery?"
    a: "No — it extends runtime per charge, which actually reduces how deeply you discharge, and shallow discharges are gentler on lithium cells. It has no negative effect on battery health whatsoever."
  - q: "Why won't Battery Saver turn on?"
    a: "It's greyed out while plugged in (by design), and it can break if power settings are corrupted or a group policy disables it. The fixes below cover the greyed-out case and the genuinely broken case."
---

Battery Saver is the most underused free runtime on your laptop. It is sitting right there in Windows, it takes ten seconds to configure, and it can stretch a dying battery through the end of a flight or a meeting. Most people either never turn it on or leave it on the default 20 percent threshold, which kicks in too late to matter.

Here is how to set it up properly, what each option does, and how to fix it when the toggle refuses to cooperate. Ten minutes of setup now pays off every time you are away from an outlet with a draining battery.

## Why this happens

- **Never configured:** Windows defaults to 20 percent, which many users never change — the saver arrives when the battery is nearly gone.
- **Greyed out while charging:** By design, Battery Saver cannot activate on AC power. This confuses people into thinking it is broken.
- **Corrupted power settings:** Damaged power plans can break the Battery Saver toggle entirely.
- **Group policy restrictions:** Work laptops may have Battery Saver disabled by IT policy.
- **Conflicting manufacturer modes:** Some manufacturer power apps override or conflict with Windows' saver.
- **Misunderstood trade-offs:** People avoid it fearing slowness, but on modern laptops the performance hit during light work is barely noticeable.

## How to fix it

Work through these in order, from quickest to most involved. Stop at the step that solves it.

### Fix 1: Enable it and set a smarter threshold

The core setup, done right.

1. Open **Settings > System > Power & battery**.
2. Expand **Battery saver** and click **Turn on now** to test it immediately (unplug the charger first — it will not activate on AC power).
3. Set **Turn battery saver on automatically at** to **30 percent** instead of the default 20. Those extra 10 percent of saver-mode runtime matter.
4. Toggle **Lower screen brightness when using battery saver** on — the display is your biggest power draw.
5. Unplug, let the battery drop to your threshold, and confirm the saver activates on its own.

### Fix 2: Add the quick-settings toggle

Make it one click instead of a settings dive.

1. Click the battery/network/volume icon cluster in the taskbar to open **Quick Settings**.
2. Click the **pencil icon** to edit, then **Add**, and add **Battery saver** if it is not there.
3. Now you can toggle it manually anytime you are on battery — useful before a long meeting or flight.
4. Remember: the toggle is dimmed while plugged in. That is normal behavior, not a bug.

### Fix 3: Pair it with power mode for maximum effect

Battery Saver plus the right power mode stack their savings.

1. In **Settings > System > Power & battery**, set **Power mode** to **Best power efficiency** when you need maximum runtime.
2. The combination of saver + efficiency mode can add over an hour compared to Best performance with no saver.
3. Switch back to **Balanced** or **Best performance** when plugged in — power mode is separate from the saver and you want full speed on AC.
4. For background app control, go to **Settings > Apps > Installed apps**, open heavy apps' **Advanced options**, and set background activity to **Power optimized** or **Never**.
5. Do not forget the screen: dropping brightness from 100 to 70 percent often saves more power than Battery Saver itself. The two together are the real runtime combo.

### Fix 4: Fix Battery Saver when it is greyed out or will not turn on

If the toggle does nothing, work through these.

1. Unplug the charger — Battery Saver physically cannot enable on AC power on most systems.
2. Open **Terminal (Admin)** and run `powercfg /restoredefaultschemes` to reset corrupted power plans, then restart.
3. Check for manufacturer power apps (**Lenovo Vantage**, **MyASUS**, **Dell Power Manager**) overriding Windows settings — set them to **Balanced** or Windows-managed mode.
4. If it is still broken, see the dedicated [battery saver not working guide](/articles/battery-saver-not-working-on-laptop-troubleshooting/) for deeper repairs. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) also documents the expected Battery Saver behavior per Windows version.

### Fix 5: Check group policy on work laptops

IT departments sometimes lock power features.

1. Press **Win + R**, type `gpedit.msc`, and press Enter (Windows 11 Pro only).
2. Navigate to **Computer Configuration > Administrative Templates > System > Power Management**.
3. Look for policies disabling Battery Saver or energy saver features.
4. If a policy is enforced, you will need IT to change it — this is not something to work around on a company machine.

### Fix 6: Measure the actual runtime gain

Know what the saver buys you so you can decide when to use it.

1. Generate a baseline: use the laptop normally on battery with the saver off and note how long 50 percent to 20 percent takes.
2. Repeat a similar workload with the saver on from 50 percent.
3. Most users see 15-25 percent more runtime — enough to matter, not enough to perform miracles.
4. If the gain is near zero, [something else is draining the battery](/articles/best-way-to-find-which-app-is-draining-battery/) faster than the saver can compensate — find that first.

### Fix 7: Build a low-power routine around it

The saver works best as part of a habit, not a panic button.

1. Before travel or long unplugged sessions, manually enable Battery Saver at 60-70 percent — do not wait for the automatic threshold.
2. Dim the screen to 60-70 percent; this alone rivals the saver's own savings.
3. Close unused browser tabs and pause cloud syncs (OneDrive, Dropbox) during critical runtime stretches.
4. For the full picture of where your power goes, generate a [battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) and review the usage history.

## Closing

Battery Saver is not magic, but it is free runtime you are leaving on the table if it is still sitting at the 20 percent default. Set it to 30, add the quick toggle, pair it with Best power efficiency, and flip it on manually before the moments that matter — the flight, the long meeting, the café with no outlets. Your future self will thank you.
