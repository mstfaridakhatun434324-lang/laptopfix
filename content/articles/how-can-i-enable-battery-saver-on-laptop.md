---
title: "How to Enable Battery Saver on Your Laptop (Windows 10/11)"
slug: how-can-i-enable-battery-saver-on-laptop
date: 2026-10-09
categories: ["battery"]
tags: ["battery saver", "power mode", "windows 11"]
description: "Enable Battery Saver on Windows 10 or 11 to stretch runtime by 20-30%. Manual toggle, automatic thresholds, and the settings that matter most."
thumbnail: "/images/thumbs/how-can-i-enable-battery-saver-on-laptop.webp"
faqs:
  - q: "How do I turn on Battery Saver in Windows 11?"
    a: "Click the battery icon in the taskbar (or open Settings, then System, then Power & battery), and toggle Battery saver on. For automatic control, set 'Turn battery saver on automatically at' to 20% or 30%. You can also lower screen brightness and switch the power mode to Best power efficiency on the same page."
  - q: "Does Battery Saver actually make a difference?"
    a: "Yes — typically 20-30% more runtime. It reduces background activity, throttles non-essential processes, lowers screen brightness, and pauses push notifications and some syncing. The trade-off is slightly reduced performance and delayed email/calendar sync, which most people never notice during light work."
  - q: "Why is Battery Saver greyed out on my laptop?"
    a: "It is unavailable while plugged into AC power — unplug the charger and the toggle activates. It can also be greyed out if a manufacturer power utility or group policy controls power settings, or on some devices where the battery is not detected. Check that Windows sees your battery first."
  - q: "Should I leave Battery Saver on all the time?"
    a: "You can, but the smarter setup is automatic: let it kick in at 20-30% battery. Running it constantly means background sync and full performance are always throttled, which gets annoying. Combine automatic Battery Saver with the Best power efficiency power mode for the best everyday balance."
---

Battery Saver is the easiest runtime win in Windows. One toggle cuts background activity, dims the display, and throttles power-hungry processes — typically buying you 20-30% more time away from the outlet. Most people only discover it when Windows turns it on automatically at 20% and everything suddenly feels sluggish. Better to set it up deliberately.

This guide covers enabling it manually and automatically on Windows 10 and 11, plus the companion settings that multiply its effect. If your battery drains fast even with Saver on, the problem is deeper — work through [fast drain troubleshooting](/articles/what-to-do-if-laptop-battery-drains-fast/) next.

## Why This Happens

- **People do not know it exists.** Battery Saver is buried in Settings; many users have never opened the Power & battery page.
- **It is off by default until 20%.** Windows waits until you are almost empty before helping — configuring an earlier threshold helps more.
- **Plugged-in confusion.** The toggle is greyed out on AC power, which convinces people it is broken.
- **Saver alone is not enough.** Without also fixing the power mode and background apps, Saver's gains are modest.
- **Manufacturer utilities override it.** Some brand power tools fight Windows' settings, silently undoing your configuration.
- **Expectations mismatch.** Saver extends runtime; it cannot fix a worn battery or a runaway process eating 40% CPU.

## How to Fix It

Work through these in order. By Fix 3 you will have more runtime than most laptop owners.

### Fix 1: Turn On Battery Saver Manually (Windows 11)

The direct toggle, for right now.

1. Click the **battery icon** in the taskbar system tray (bottom-right).
2. In the Quick Settings panel, click the **Battery saver** tile to turn it on. The tile highlights when active.
3. Alternatively, open **Settings** > **System** > **Power & battery** and toggle **Battery saver** on.
4. Notice the screen dim slightly — that is Saver working. You can manually raise brightness back if needed.
5. Remember: the toggle only works on battery power. Plugged in, it greys out — that is normal, not a bug.
6. When you are back near an outlet, toggle it off to restore full performance and background sync.

### Fix 2: Turn On Battery Saver Manually (Windows 10)

Same feature, slightly different location on Windows 10.

1. Click the **battery icon** in the taskbar.
2. Drag the power mode slider toward **Better battery** or **Best battery life** — on Windows 10 this slider is the primary control.
3. For the dedicated Saver: open **Settings** > **System** > **Battery**, and toggle **Battery saver** on.
4. Check **Battery saver status until next charge** if you want it to stay on until you plug in.
5. Uncheck **Lower screen brightness while in battery saver** only if you need full brightness — leaving it checked saves meaningful power.
6. As on Windows 11, the toggle requires battery power; it is disabled while charging.

### Fix 3: Set Battery Saver to Turn On Automatically

Manual toggling is for emergencies. Automatic is for everyday life.

1. Open **Settings** > **System** > **Power & battery** (Windows 11) or **Settings** > **System** > **Battery** (Windows 10).
2. Find **Turn battery saver on automatically at** and set it to **20%** — or **30%** if you want earlier intervention on long days.
3. On Windows 11, expand the **Battery saver** section to see the threshold dropdown.
4. Test it: the next time your battery crosses the threshold, you will see a notification and the Quick Settings tile will activate.
5. Pair this with a sensible threshold — 20% gives you roughly an extra 30-45 minutes of light work on most modern laptops.
6. If you use [a charge limit](/articles/best-way-to-set-battery-charge-threshold/) at 80%, automatic Saver at 20% still leaves you a comfortable buffer.

### Fix 4: Switch the Power Mode to Best Power Efficiency

Battery Saver's best friend. Together they stack.

1. Open **Settings** > **System** > **Power & battery**.
2. Find **Power mode** and set it to **Best power efficiency** (on battery — Windows 11 lets you set it per power source).
3. This caps CPU boost behavior and favors efficiency cores, cutting the biggest single power draw in the system.
4. Notice the performance difference: fine for browsing, Office, and video; switch back to **Balanced** or **Best performance** for gaming or heavy compiles.
5. On Windows 10, use the taskbar battery slider: **Best battery life** is the equivalent.
6. Some manufacturer utilities (Lenovo Vantage, MyASUS) have their own power profiles that override this — set them to match, or Windows and the utility will fight.

### Fix 5: Cut the Background Drain Battery Saver Misses

Saver throttles background activity, but these settings cut it further.

1. Go to **Settings** > **Apps** > **Installed apps**, click the three dots on heavy apps, choose **Advanced options**, and set **Background apps permissions** to **Never** for apps you do not need live.
2. Open **Settings** > **System** > **Notifications** and disable notifications for noisy apps — each wake costs power.
3. In **Settings** > **Bluetooth & devices**, turn off Bluetooth when not in use.
4. Reduce screen brightness manually to 40-50% — the display is typically the largest power draw, bigger than the CPU at idle.
5. In **Settings** > **System** > **Power & battery** > **Screen and sleep**, set aggressive timeouts: screen off after 3-5 minutes on battery, sleep after 10.
6. For the full drain-hunting procedure including `powercfg` analysis, see [how to run battery diagnostics](/articles/how-to-run-battery-diagnostics-on-laptop/).

### Fix 6: Fix Battery Saver When It Will Not Turn On

If the toggle is greyed out or does nothing, work through these.

1. **Unplug the charger.** Battery Saver is disabled on AC power by design — this resolves most "greyed out" reports instantly.
2. Check that Windows detects the battery: no battery icon, or a [red X on the icon](/articles/battery-x-icon-red-cross-troubleshooting/), means Saver has nothing to manage.
3. Look for manufacturer power utilities (Dell Power Manager, Lenovo Vantage, MyASUS) set to a performance profile that overrides Windows — align them or uninstall the utility's power component.
4. Check Group Policy (Pro editions): run `gpedit.msc`, navigate to **Computer Configuration** > **Administrative Templates** > **System** > **Power Management**, and ensure nothing forces Saver off.
5. Run Windows Update — power subsystem bugs do get fixed, and the relevant components update through the normal channel documented on the [Windows support site](https://support.microsoft.com/en-us/windows).
6. As a last resort, reset power plans to default: elevated Command Prompt, `powercfg -restoredefaultschemes`, then reboot and reconfigure.

## Closing

Battery Saver will not fix a dying battery, but on a healthy one it is the difference between making it through a flight and hunting for an outlet at 40,000 feet. Set the automatic threshold once, pair it with Best power efficiency, and forget about it — that is the entire trick. The best power setting is the one you never have to think about again.
