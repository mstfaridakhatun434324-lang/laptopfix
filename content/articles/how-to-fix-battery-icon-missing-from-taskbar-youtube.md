---
title: "How to Get the Battery Icon Back on the Windows Taskbar"
slug: how-to-fix-battery-icon-missing-from-taskbar-youtube
date: 2026-09-16
categories: ["battery"]
tags: ["battery icon missing", "taskbar", "system tray", "windows 11"]
description: "Battery icon vanished from your taskbar? Here's how to bring it back — from quick settings toggles to the deeper fixes when it won't reappear."
thumbnail: "/images/thumbs/how-to-fix-battery-icon-missing-from-taskbar-youtube.webp"
faqs:
  - q: "Why did my battery icon disappear from the taskbar?"
    a: "Usually it's just hidden: Windows 11 lets you toggle system tray icons off, and updates sometimes reset the toggle. Less commonly, a corrupted battery driver or a File Explorer glitch removes it. The icon is almost never gone because of a hardware problem."
  - q: "Where is the battery icon setting in Windows 11?"
    a: "Go to Settings > Personalization > Taskbar > System tray icons (or Other system tray icons on some builds) and make sure Power is toggled on. You can also click the battery/network/volume cluster in the taskbar to open Quick Settings, where the battery status always appears."
  - q: "What if the Power toggle is greyed out?"
    a: "A greyed-out Power toggle usually means Windows can't detect the battery — the icon hides itself when there's no battery to report. Reinstall the Microsoft ACPI-Compliant Control Method Battery driver in Device Manager and restart; the toggle typically becomes available again."
  - q: "Does a missing battery icon mean my battery is broken?"
    a: "No. The icon is just a display element. If the laptop still runs on battery power when unplugged, the battery is fine and this is purely a display or driver issue."
---

You glance at the taskbar to check your charge and the battery icon is just... gone. No percentage, no charging indicator, nothing. The laptop works fine otherwise, which makes it more annoying — you know the battery is there, Windows just won't show it.

This is overwhelmingly a settings or display issue, not a battery problem. The icon can be toggled off, hidden by an update, or suppressed when Windows temporarily can't see the battery. Let's bring it back.

## Why this happens

- **The Power tray icon is toggled off** — in Taskbar settings, easy to flip accidentally.
- **A Windows update reset taskbar settings** — feature updates sometimes revert icon toggles.
- **File Explorer glitch** — the shell didn't load the icon properly at startup.
- **Corrupted battery driver** — Windows hides the icon when it can't read battery status.
- **Tablet mode / display quirks** — icon hidden in certain display configurations.
- **Corrupted system files** — rare, but broken shell components can drop tray icons.

## How to fix it

Work through these in order — the toggle fixes it for most people.

### Fix 1: Toggle the Power icon back on

The setting moved around between Windows builds, so check both locations:

1. Go to **Settings > Personalization > Taskbar**.
2. Expand **System tray icons** (labeled **Other system tray icons** on some builds).
3. Make sure **Power** is toggled **On**.
4. If it's already on, toggle it **Off**, wait a few seconds, then toggle it back **On**.

Check the taskbar immediately — the battery icon should reappear in the system tray area.

### Fix 2: Check Quick Settings

Even with the tray icon off, your battery status is one click away: click the network/volume/battery cluster in the bottom-right corner (or press **Win + A**) to open **Quick Settings**. The battery percentage and charging state always show there. This doesn't fix the missing icon, but it confirms Windows can see the battery — if Quick Settings shows the battery fine, you know it's purely a tray display issue.

On some builds, the relevant toggle lives under **Settings > Personalization > Taskbar > Other system tray icons** instead — Microsoft renamed this section more than once, so if you don't see "System tray icons," look for the "Other" variant. The Power switch does the same job in both places.

### Fix 3: Restart File Explorer

If the toggle is on but the icon still won't show, the shell may have glitched:

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Find **Windows Explorer** in the Processes list.
3. Right-click it and choose **Restart**.

Your taskbar will briefly disappear and reload. Check whether the battery icon returns. This fixes cases where the icon vanished after waking from sleep or after an update.

### Fix 4: Reinstall the battery driver

When Windows can't read the battery, it hides the icon — and a greyed-out Power toggle is the telltale sign:

1. Press **Win + X**, open **Device Manager**, expand **Batteries**.
2. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**.
3. Restart the laptop.

After the reboot, Windows redetects the battery and the Power toggle in Taskbar settings should become available again. If Windows genuinely can't see the battery, our [battery not detected guide](/articles/laptop-battery-not-detected-windows-11/) covers the deeper fixes.

### Fix 5: Run the system file checker

If the icon area itself seems broken (other icons missing too, or the taskbar misbehaving):

1. Open Command Prompt **as administrator**.
2. Run `sfc /scannow` and let it complete — this repairs corrupted Windows system files.
3. If it reports unfixable corruption, follow with `DISM /Online /Cleanup-Image /RestoreHealth`, then run `sfc /scannow` again.
4. Restart.

This is the heavy artillery for shell problems; most missing-icon cases won't need it, but it's the right step when multiple tray icons are affected. The DISM command downloads clean replacement files from Windows Update, so make sure you're online when you run it — on a metered connection, temporarily allow the download or run it while on Wi-Fi you trust.

### Fix 6: Check for Windows updates

Microsoft occasionally breaks and then fixes tray icons in cumulative updates:

1. Go to **Settings > Windows Update** and install all pending updates.
2. Restart even if it doesn't prompt you — some shell fixes only apply on a full restart.

If the icon disappeared immediately after an update, the next cumulative update often restores it — but don't just wait; the driver and Explorer steps above usually fix it now.

It's also worth checking whether you're signed in with a temporary profile, which can happen after a failed update — temporary profiles load with default taskbar settings and your icon customizations vanish. If your desktop wallpaper and files look wrong too, that's the giveaway; signing out and back in (or restarting) usually restores your real profile and your icons with it.

### Fix 7: Create a battery shortcut as a workaround

If the tray icon stubbornly refuses to return, pin battery status somewhere visible:

1. Go to **Settings > System > Power & battery** and keep an eye on the percentage there.
2. Right-click the desktop > **New > Shortcut** and enter `ms-settings:batterysaver` — name it "Battery" and keep it handy.

It's not as elegant as the tray icon, but it gives you one-click battery status while you work on the underlying issue. For ongoing battery monitoring, [generating a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) gives you far more detail than any icon anyway.

## Closing

A missing battery icon is almost never a battery problem — it's a toggled setting, a shell hiccup, or a driver that needs reinstalling. The Taskbar settings toggle resolves the vast majority of cases in under a minute. If the Power toggle is greyed out, that's Windows telling you it can't see the battery, and the driver reinstall is your next move. Either way, your battery is almost certainly fine; it's just the messenger that went missing.

If you find yourself toggling the icon back on after every major Windows update, you're not imagining it — feature updates do occasionally reset taskbar preferences. It takes ten seconds to flip back on, and now you know exactly where the switch lives, so it stops being a mystery and becomes a minor routine.
