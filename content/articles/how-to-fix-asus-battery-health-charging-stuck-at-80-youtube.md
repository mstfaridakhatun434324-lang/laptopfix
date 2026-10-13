---
title: "How to Fix ASUS Battery Health Charging Stuck at 80% (Video Walkthrough)"
slug: how-to-fix-asus-battery-health-charging-stuck-at-80-youtube
date: 2026-09-02
categories: ["battery"]
tags: ["asus", "battery health charging", "stuck at 80", "myasus"]
description: "ASUS laptop refusing to charge past 80%? That's Battery Health Charging doing its job — or glitching. 6 fixes to control it."
thumbnail: "/images/thumbs/how-to-fix-asus-battery-health-charging-stuck-at-80-youtube.webp"
faqs:
  - q: "Why won't my ASUS charge past 80 percent?"
    a: "Battery Health Charging in MyASUS is limiting it — the Balanced or Maximum Lifespan mode caps charging at 80% (or 60%) to extend battery life. Switch to Full Capacity Mode if you need 100%. If it's already on full capacity and still stuck, the setting has glitched and needs a reset."
  - q: "Is charging to only 80% bad for my laptop?"
    a: "No — it's protective. Lithium batteries degrade slowest when kept between 20 and 80 percent. ASUS added this feature specifically to make batteries last years longer. Only switch to 100% when you need maximum unplugged runtime."
  - q: "I set Full Capacity Mode but it still stops at 80. Why?"
    a: "The setting didn't actually apply — a known MyASUS glitch. Toggle to a different mode, apply, reboot, then set Full Capacity Mode again. If that fails, reinstall MyASUS, since a corrupt install can leave the EC stuck on the old limit."
  - q: "Where is Battery Health Charging in MyASUS?"
    a: "Open MyASUS, go to Customization (or Battery Health Charging on newer versions), and look for the charging mode selector with three options: Full Capacity Mode, Balanced Mode, and Maximum Lifespan Mode."
---
Your ASUS charges to 80 percent and stops. Dead. No matter how long it sits plugged in, it won't budge past 80. Before you panic, know this: on an ASUS, that's usually a feature working as designed, not a fault. ASUS's Battery Health Charging deliberately caps charging to prolong battery life — and it's easy to forget it's on, or to have it turn itself on during an update.

But sometimes it genuinely glitches: you set Full Capacity Mode and the laptop still refuses to pass 80. This guide covers both — understanding the feature, and fixing it when it misbehaves. The distinction matters because the "fix" for a feature working as designed is just changing a setting, while the fix for a glitched setting involves reinstalling software and resetting firmware. We'll start with the setting, then move to the glitches.

## Why this happens

- **Balanced Mode is active.** MyASUS's Balanced Mode caps charging at 80 percent by design. Many ASUS laptops ship with it enabled, or updates re-enable it.
- **Maximum Lifespan Mode is active.** The most aggressive mode caps at 60 percent — if you're stuck even lower than 80, this is why.
- **The mode setting glitched.** MyASUS can display "Full Capacity Mode" while the embedded controller still enforces the old 80 percent cap — the UI and the hardware disagree.
- **A Windows or MyASUS update reset it.** Updates frequently revert the charging mode to Balanced without telling you.
- **MyASUS is corrupt or outdated.** A broken install can't communicate mode changes to the EC, so the cap stays frozen regardless of what you click.
- **The EC latched the limit.** The embedded controller can get stuck enforcing a cap even after the software setting changes, until it's reset. This is the hardest variant to diagnose because every screen in Windows insists the limit is off while the hardware quietly enforces it.

## How to fix it

Work through these in order. Fix 1 is the intended control — the rest are for when it's misbehaving.

### Fix 1: Set the charging mode in MyASUS

This is the official control. Check it first.

1. Open **MyASUS** > **Customization** > **Battery Health Charging** (location varies slightly by version).
2. You'll see three modes: **Full Capacity Mode** (100%), **Balanced Mode** (80%), **Maximum Lifespan Mode** (60%).
3. Select **Full Capacity Mode** and click **Apply**. Unplug and replug the charger.
4. Charge for 30 minutes and confirm it passes 80. If you actually want the longevity benefit, Balanced Mode at 80% is the sweet spot — learn [how to limit charging to 80 percent properly](/articles/how-to-limit-battery-charge-to-80/) across brands. Note that the mode change can take a few minutes and a charger replug to take effect; if it still shows the old cap immediately, wait before assuming it's broken.

### Fix 2: Force the stuck setting to rewrite

When the UI says Full Capacity but the hardware says 80, force them back in sync.

1. In MyASUS, switch to **Maximum Lifespan Mode** (60%), apply, and wait one minute.
2. Switch to **Balanced Mode** (80%), apply, and wait one minute.
3. Now switch to **Full Capacity Mode**, apply, and **restart** the laptop (full restart, not sleep).
4. After reboot, charge uninterrupted and watch whether it climbs past 80. The mode-cycling forces the EC to accept each new value instead of ignoring the change.

### Fix 3: Reinstall MyASUS

A corrupt MyASUS install is the most common reason the mode won't change.

1. Uninstall **MyASUS** via **Settings** > **Apps** > **Installed apps**.
2. Restart the laptop.
3. Reinstall **MyASUS** fresh from the Microsoft Store.
4. Open it, set **Full Capacity Mode**, apply, restart once more, and test charging. Also update **Armoury Crate** if installed — it shares power components with MyASUS.

### Fix 4: Reset the embedded controller

When the EC itself is latched on the 80 percent cap, software toggles can't reach it.

1. Shut down fully and unplug the charger.
2. Hold the power button for 30 seconds to drain residual power and reset the EC.
3. Reconnect the charger, boot, and set your desired mode in MyASUS again.
4. Charge and verify. If the cap was EC-latched, it clears on the first boot after reset.

### Fix 5: Check for a second limiter fighting MyASUS

Two charge limiters means neither works predictably.

1. Check **Armoury Crate** for any battery or charging limit settings that might conflict.
2. Look in **Settings** > **Apps** for third-party battery tools and uninstall any you don't need.
3. In **Task Manager** > **Startup apps**, disable leftover battery helpers.
4. With only MyASUS managing charging, set the mode once more and test. Conflicting tools are also a prime suspect when [battery percentages jump around](/articles/how-to-fix-battery-percentage-jumps-up-and-down-step-by-step/).

### Fix 6: Update BIOS and the ASUS system drivers

The EC firmware that enforces the cap gets bug fixes like everything else.

1. Open **MyASUS** > **System Update** (or **Live Update**) and install all **BIOS** and system driver updates.
2. Alternatively, download them from ASUS support for your exact model.
3. Run the BIOS update on AC power with everything closed; don't interrupt it.
4. After reboot, set Full Capacity Mode one final time and confirm charging passes 80 percent. If it still won't budge after all six fixes, the battery's own protection circuit may be limiting charge — contact ASUS support, especially under warranty. Bring your purchase date and serial number; ASUS support will typically ask for a battery report, which you can generate in advance with `powercfg /batteryreport` to speed things up.

## Closing

An ASUS stuck at 80 percent is Battery Health Charging doing exactly what it was designed to do — until it isn't. Check the mode, force a rewrite if it's glitched, and keep MyASUS healthy. And honestly? If you mostly use the laptop plugged in, leaving it at 80 percent is doing your battery a favor. The 20 percent of runtime you give up buys you a battery that still holds a real charge two or three years from now, which is a trade most desk-bound users should happily take.
