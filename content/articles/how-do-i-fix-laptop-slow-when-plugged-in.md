---
title: "Why Is My Laptop Slow When Plugged In? Fixes That Work"
slug: how-do-i-fix-laptop-slow-when-plugged-in
date: 2026-09-13
categories: ["performance"]
tags: ["slow laptop", "plugged in", "power settings", "charger", "throttling"]
description: "Laptop fast on battery but slow when plugged in? That's backwards — and fixable. Here's why it happens and the settings that restore full speed on AC power."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-slow-when-plugged-in.webp"
faqs:
  - q: "Why is my laptop slower when plugged in than on battery?"
    a: "It's counterintuitive, but it usually comes down to power settings or the charger. Some laptops apply a low-power or wrong power plan when they detect AC power, a weak or third-party charger can trigger protective throttling, and certain BIOS or vendor utilities mismanage the AC/battery transition. Heat is another factor — charging generates extra heat that can push the CPU into thermal throttling."
  - q: "Can a wrong charger make my laptop slow?"
    a: "Yes. If the charger can't deliver the wattage your laptop expects (for example, a 45W charger on a laptop that wants 90W), many laptops throttle the CPU to stay within the available power. Always use the original charger or a replacement with matching or higher wattage and the correct connector."
  - q: "Should the power plan be different on battery vs plugged in?"
    a: "Windows lets you set separate behaviors, and the plugged-in setting should be equal or more aggressive than the battery setting — typically Best performance or Balanced on AC. If your AC setting is somehow on power saver, you'll get exactly this backwards slowdown."
  - q: "Does charging generate heat that slows the CPU?"
    a: "It can. Charging the battery produces heat inside the chassis, and on thin laptops that extra heat can push CPU temperatures into throttling range during heavy tasks. If the slowdown appears 20-30 minutes after plugging in rather than immediately, heat is a likely contributor."
---

It defies logic: you plug in your laptop expecting full speed, and instead everything gets slower. Apps take longer to open, videos stutter, and the whole machine feels like it's wading through mud — then you unplug it and performance comes back. This "backwards" slowdown is a real and surprisingly common problem, and it almost always comes down to one of three things: power settings applying the wrong profile on AC, a charger that isn't delivering enough power, or heat from charging pushing the CPU into thermal throttling.

The good news is that all three are fixable without new hardware in most cases. The key is figuring out which one applies to you, because the fix for a wrong power plan is a settings change, the fix for a weak charger is using the right adapter, and the fix for heat is cooling management. This guide helps you identify your scenario and apply the right fix.

Start by confirming the pattern: use the laptop on battery for ten minutes doing normal tasks, then plug in and do the same tasks. If the slowdown is immediate upon plugging in, it's settings or the charger. If it builds up over 20-30 minutes, it's heat.

## Why this happens

- **Wrong power plan on AC**: Windows can apply different power modes for battery and plugged-in states; if the AC profile is set to power saver, you get exactly this backwards behavior.
- **Underpowered or third-party charger**: A charger delivering less wattage than the laptop expects triggers protective CPU throttling to stay within the power budget.
- **Faulty charger detection**: A damaged charger cable or connector can make the laptop misread the adapter's capacity and throttle unnecessarily.
- **Charging heat causing thermal throttling**: Battery charging generates internal heat that, combined with CPU heat, pushes temperatures into throttling range.
- **Vendor utility power profiles**: Dell Power Manager, Lenovo Vantage, HP Power Manager, or ASUS Armoury Crate can apply their own AC/battery profiles that override Windows settings.
- **BIOS power settings**: Some BIOS versions have AC-specific performance settings or bugs in how they handle the power-state transition.
- **Battery health issues**: A failing battery can cause the power system to behave erratically when switching between AC and battery power.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check and correct the plugged-in power mode

This is the most common cause and the fastest fix. Windows 11 lets you set separate power modes, and yours may be wrong.

1. Plug in your laptop, then open **Settings > System > Power & battery**.
2. Look at the **Power mode** setting — this shows the mode for your current power state (plugged in).
3. Set it to **Best performance** or at least **Balanced**. If it's on **Best power efficiency** while plugged in, that's your problem.
4. Unplug the laptop and check the setting again — note that Windows remembers separate modes, so set each appropriately.
5. Test performance plugged in after the change.

If the setting keeps reverting, a vendor utility may be overriding it — see Fix 5.

### Fix 2: Verify your charger wattage

An underpowered charger is the second most common cause. Laptops check the adapter's capacity and throttle the CPU if it's insufficient.

1. Check the wattage printed on your original charger brick (e.g., 65W, 90W, 130W).
2. Check the wattage of the charger you're actually using — many people unknowingly use a weaker spare.
3. If you're using USB-C charging, confirm both the charger and cable support the required wattage (a 60W cable on a 100W charger limits you to 60W).
4. Test with the original charger if you have it. If performance returns, replace the weak charger with one matching the original spec.

For more on power plans, see our guide on [changing to the best performance power plan](/articles/how-to-change-power-plan-to-best-performance-on-laptop/).

### Fix 3: Inspect the charger and charging port

A damaged cable or dirty port can cause the laptop to misread the adapter, triggering the same throttling as a weak charger.

1. Inspect the charger cable for kinks, fraying, or damage near the connectors.
2. Check the laptop's charging port for dust, lint, or bent pins — clean gently with compressed air.
3. Try a different wall outlet to rule out power delivery issues.
4. If your laptop shows a "plugged in, not charging" message or unknown adapter warnings in the BIOS, the charger or port likely needs replacement.

### Fix 4: Rule out charging heat

If the slowdown builds gradually after plugging in rather than appearing instantly, heat is the likely mechanism.

1. Plug in and use the laptop normally for 30 minutes, noting when the slowdown begins.
2. Install HWMonitor (free) and watch CPU temperatures — sustained temps above 90-95°C indicate throttling.
3. Ensure vents are clear and the laptop sits on a hard, flat surface (not a bed or couch).
4. Blow dust out of the vents with compressed air.
5. Consider a cooling pad if you regularly do heavy work while charging.

### Fix 5: Check vendor power utilities

Manufacturer utilities can silently override Windows power settings with their own AC/battery profiles.

1. Open your vendor's utility: **Dell Power Manager**, **Lenovo Vantage**, **HP Power Manager**, **ASUS Armoury Crate**, or **Acer Care Center**.
2. Look for thermal or power profiles tied to AC/battery state.
3. Set the plugged-in profile to performance/balanced — not quiet or power saver.
4. If the utility keeps fighting Windows settings, set the utility to defer to Windows or uninstall the power-management component.

### Fix 6: Update BIOS and chipset drivers

BIOS bugs in power-state handling are a known cause of this exact symptom on several laptop lines. Manufacturers do fix them.

1. Find your exact model number.
2. Check the manufacturer's support page for BIOS updates: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
3. Install any BIOS update newer than yours, following the instructions exactly — on AC power, never interrupt it.
4. Update chipset drivers at the same time.

### Fix 7: Reset power plans to defaults

If settings seem tangled — especially after third-party "optimizer" tools — resetting to defaults clears the mess.

1. Open **Command Prompt as administrator**.
2. Run `powercfg -restoredefaultschemes` to reset all power plans.
3. Restart, plug in, and set the power mode to **Best performance** in Settings.
4. Test thoroughly before reinstalling any power-management utilities.

Our deeper walkthrough for this exact symptom — [troubleshooting a laptop slow only when plugged in](/articles/troubleshoot-laptop-slow-when-plugged-in/) — covers additional edge cases. Microsoft's Windows support documentation covers the power settings for your Windows version if you want to dig deeper.

## Closing

A laptop that's slow when plugged in is almost always a configuration problem, not a hardware failure: the wrong power mode on AC, an underpowered charger, or charging heat. Check them in that order — most people find the culprit in the first two steps — and your laptop will finally be faster plugged in, the way it's supposed to be.
