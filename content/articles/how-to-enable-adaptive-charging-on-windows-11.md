---
title: "How to Enable Adaptive Charging on Windows 11 (Smart Charging)"
slug: how-to-enable-adaptive-charging-on-windows-11
date: 2026-10-11
categories: ["battery"]
tags: ["adaptive charging", "smart charging", "windows 11"]
description: "Windows 11 has built-in Smart Charging to protect your battery. Here's how to enable it, how it works, and what to do if it's missing."
thumbnail: "/images/thumbs/how-to-enable-adaptive-charging-on-windows-11.webp"
faqs:
  - q: "What is Smart Charging in Windows 11?"
    a: "Smart Charging is Windows 11's built-in adaptive charging feature. It learns your daily routine, holds the battery below 100% during long plugged-in periods, and finishes charging just before you typically unplug. This reduces the time cells spend at stressful full charge, measurably extending battery lifespan."
  - q: "How do I turn on Smart Charging in Windows 11?"
    a: "Go to Settings > System > Power & battery, expand the Battery section, and look for Smart charging. If your device supports it, you can toggle it there. Note it's hardware-dependent — not every laptop shows this option, in which case your manufacturer's app (Lenovo Vantage, Dell Power Manager, MyASUS) provides the equivalent."
  - q: "Why don't I see Smart Charging in my Windows 11 settings?"
    a: "Smart Charging requires specific firmware support from the manufacturer — Microsoft enables it per device model. If it's missing, your laptop's vendor utility almost certainly has the same feature under a different name (charge threshold, conservation mode, battery protection). Check there instead."
  - q: "Will Smart Charging leave me with less battery when I need it?"
    a: "That's the clever part: it learns when you unplug and completes the charge beforehand. If your routine changes unexpectedly, you can always toggle it off temporarily for a full immediate charge. Most users never notice it except in longer battery lifespan."
---
# How to Enable Adaptive Charging on Windows 11 (Smart Charging)

Windows 11 finally brought battery smarts into the OS itself with Smart Charging — no vendor app required. It watches your routine, holds the battery below full while you're docked, and tops it up just before you grab the laptop and go. Less time at 100% means a battery that stays healthy years longer.

But there's a catch: not every laptop shows the option, and the vendor apps still matter. This guide covers enabling Microsoft's Smart Charging, what to do when it's missing, and how the manufacturer alternatives compare.

## Why this happens

- **Smart Charging is hardware-gated.** Microsoft enables it per device model based on firmware support — many laptops don't have the toggle at all.
- **It's off or paused by default on some devices.** Even supported laptops sometimes need it switched on manually.
- **Vendor apps override it.** Lenovo Vantage or Dell Power Manager thresholds take precedence and can mask Smart Charging's behavior.
- **The algorithm needs learning time.** For the first few days it may seem to do nothing while it studies your routine.
- **Confusion with vendor features.** "Adaptive charging," "Smart Charging," "conservation mode," and "battery protection" all do similar things with different names.
- **Windows 10 habits carry over.** Upgraders look for the feature in the wrong place or assume their vendor app is now redundant.

## How to fix it

Work through these in order, from quickest to deepest. Most people find the answer by Fix 3.

### Fix 1: Enable Smart Charging in Settings

Check whether your device supports Microsoft's built-in version.

1. Open **Settings > System > Power & battery**.
2. Expand the **Battery** section.
3. Look for **Smart charging** — if present, toggle it **On**.
4. Read the status text: it tells you whether it's actively managing the charge or still learning.
5. Leave it on for a few days of normal routine so the algorithm learns your unplug times.

### Fix 2: Understand What It's Doing

Smart Charging behaves differently from a fixed limit — knowing the pattern avoids confusion.

1. During long plugged-in periods, the battery may hold at a reduced level (often around 80%).
2. Before your typical unplug time, it completes the charge to 100%.
3. If your schedule changes, it adapts within a few days.
4. You can toggle it off any time you need an immediate guaranteed full charge (before travel, for example).
5. It never harms the battery — holding below full is always gentler than sitting at 100%.

### Fix 3: Use the Manufacturer's Equivalent (Most Laptops)

If Smart Charging is missing from Settings, your vendor app has the same capability — this covers the majority of Windows 11 laptops.

1. **Lenovo:** **Vantage > Device > Power** — set a **Battery Charge Threshold** (stop at 80%) for adaptive-like behavior.
2. **Dell:** **Dell Power Manager > Battery Settings** — choose **Adaptive** mode, which learns your pattern like Smart Charging.
3. **ASUS:** **MyASUS > Battery Health Charging** — **Balanced Mode** caps at 80%.
4. **HP:** BIOS (**F10**) **> Advanced > Power Management > Battery Health Manager** — **Let HP Manage My Charging**.
5. **Samsung:** **Samsung Settings > Battery protection** — caps at 85%.
6. Don't run both Smart Charging and a vendor limit simultaneously — pick one to avoid conflicts.

The complete reference: [how to set a battery charge threshold on your laptop](/articles/how-to-set-battery-charge-threshold-on-laptop/).

### Fix 4: Check for Conflicts Between Settings

Two charge managers fighting causes weird behavior — battery stuck, limits ignored, or constant toggling.

1. If Smart Charging is on in Windows Settings, turn off vendor charge thresholds.
2. If you prefer the vendor app's control, turn Smart Charging off in Settings.
3. Check BIOS for a third layer — some laptops enforce thresholds in UEFI too.
4. After changing, unplug/replug the charger so the new policy takes effect.
5. Observe for a day: the battery should follow exactly one policy.

### Fix 5: Give the Algorithm Time to Learn

Adaptive features look broken during the learning period. Don't judge too early.

1. Use the laptop on your normal schedule for 3–5 days with the feature enabled.
2. Keep a consistent routine if possible — regular unplug times train it faster.
3. Check the vendor app or Settings status text for "learning" vs. "active" indications.
4. After the learning period, verify: long docked periods should hold below 100%, with full charge before typical unplug times.
5. If it never adapts after a week, the feature may not be properly supported on your model — use a fixed 80% threshold instead.

### Fix 6: Update Everything That Touches Power

Smart Charging depends on firmware and drivers being current.

1. Run **Windows Update** (**Settings > Windows Update**) and install all pending updates.
2. Update your vendor app from the **Microsoft Store**.
3. Check the manufacturer's support site for **BIOS** updates mentioning battery or charging.
4. After a Windows feature update (like 24H2), re-verify your charging settings — updates can reset them.
5. If Smart Charging disappeared after an update, check for a new BIOS — Microsoft sometimes re-gates the feature on firmware versions.

### Fix 7: The Manual Fallback

If no adaptive option exists anywhere on your laptop, approximate it by habit.

1. When docked, unplug at around **80%**; plug back in at **40%**.
2. Before travel, charge to 100% — occasional full charges are fine.
3. For overnight: if the laptop is full, unplug before bed.
4. Enable **Battery saver** at 20% in **Settings > System > Power & battery** as a safety net.
5. It's manual, but the chemistry rewards the 40–80% range regardless of who manages it.

For the Windows 10 version of this setup, see [how to enable adaptive charging on Windows 10](/articles/how-to-enable-adaptive-charging-on-windows-10/).

## Closing

Windows 11's Smart Charging is the easiest battery-longevity win available — one toggle, and your battery spends hundreds fewer hours at stressful full charge. If your laptop doesn't offer it, the vendor equivalent does the same job under a different name. Either way, the principle is identical: keep the battery out of the 100% red zone when you don't need it, and let it fill up when you do. Your future self, still getting decent runtime in year four, will thank you.

## Verify your results

After a week, check the pattern: docked periods holding below full, complete charges before your usual unplug time. Run `powercfg /batteryreport` monthly to watch full-charge capacity — with adaptive charging active, the decline should be noticeably slower. The [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) is useful if you ever need to repair Windows itself, and [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) keeps chipset drivers current for proper power management.
