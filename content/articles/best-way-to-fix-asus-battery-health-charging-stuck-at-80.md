---
title: "ASUS Battery Health Charging Stuck at 80? The Best Way to Fix It"
slug: best-way-to-fix-asus-battery-health-charging-stuck-at-80
date: 2026-09-16
categories: ["battery"]
tags: ["asus", "battery health charging", "myasus", "charge limit"]
description: "Your ASUS laptop won't charge past 80% and you want it to? Here's the best way to change it — plus when you should leave the limit alone."
thumbnail: "/images/thumbs/best-way-to-fix-asus-battery-health-charging-stuck-at-80.webp"
faqs:
  - q: "Why won't my ASUS laptop charge past 80%?"
    a: "ASUS Battery Health Charging is set to Balanced mode (80% cap) or Maximum lifespan mode (60% cap). It's a deliberate longevity feature, not a malfunction. Change it in MyASUS > Customization > Battery Health Charging, or in the BIOS, to Full capacity mode when you need 100%."
  - q: "Is it bad to always charge my ASUS to 100%?"
    a: "Not bad, but it wears the battery faster than capping at 80%. Lithium cells degrade faster when held at full charge, especially when warm. If you mostly use the laptop plugged in at a desk, the 80% cap can roughly double the battery's useful lifespan. Use 100% mode when you need maximum runtime away from outlets."
  - q: "I changed the setting in MyASUS but it still stops at 80%. Why?"
    a: "The setting needs a full shutdown (not restart) to apply, and sometimes MyASUS and the BIOS disagree — the BIOS wins. Enter the BIOS (F2 at boot), find the battery health charging option, set it there, then do a complete shutdown and cold boot."
  - q: "Where is Battery Health Charging in the BIOS?"
    a: "Reboot and tap F2 to enter the ASUS BIOS (UEFI). Go to Advanced > ASUS Battery Health Charging (location varies slightly by model). Set it to Full capacity mode, save, exit, then shut down completely and power back on for the change to take effect."
---

First, the reassurance: your ASUS isn't broken. Battery Health Charging is doing exactly what it was designed to do — stopping at 80% (or 60%) to make your battery last years longer. The "stuck at 80" complaint is the feature working. But features should obey you, so if you've tried changing it and it won't budge — or you just want to understand the trade-offs before deciding — this is the complete guide.

The best fix depends on your situation: changing the mode properly (most people), fixing it when the setting won't apply (the stubborn cases), and knowing when to leave the cap on (the smart play).

## Why the cap exists (and why it's "stuck")

- **Balanced mode (80% cap):** The default on many ASUS models. Stops charging at 80% to reduce the voltage stress that ages lithium cells fastest.
- **Maximum lifespan mode (60% cap):** For laptops that live on desks permanently. Maximum longevity, minimum runtime.
- **Full capacity mode (100%):** Charges fully. Use when you need every minute of runtime.
- **Setting applied at firmware level:** MyASUS writes the preference to the EC firmware, which enforces it independently of Windows — that's why Windows reinstalls don't change it.
- **Needs a cold boot to apply:** The EC reads the mode at power-on. A Windows "restart" with Fast Startup doesn't fully reset the EC, so changes appear to not stick.
- **BIOS vs MyASUS conflict:** If set in one place but not the other, behavior follows the BIOS. MyASUS may display the wrong state.

## How to fix it

Pick the path matching your goal.

### Fix 1: Change the mode in MyASUS (the normal way)

This works for most people. The trick is the shutdown afterward.

1. Open **MyASUS** (search Start; install from the Microsoft Store if missing).
2. Go to **Customization** (left sidebar) → **Battery Health Charging**.
3. Select **Full capacity mode** for 100% charging.
4. Click **apply/save** if prompted.
5. Now the critical step: **shut down completely** — **Start > Power > Shut down**. Not restart. Wait 10 seconds, then power on.
6. Plug in and charge. It should now sail past 80% to 100%. If it still stops at 80%, continue to Fix 2 — the BIOS is overriding MyASUS.

### Fix 2: Set it in the BIOS (when MyASUS won't stick)

The BIOS setting is authoritative. Set it here and it stays.

1. Shut down completely. Power on and **tap F2 repeatedly** to enter the ASUS UEFI BIOS.
2. Go to **Advanced** mode if needed (F7 on many models), then find **ASUS Battery Health Charging** — usually under **Advanced** settings.
3. Set it to **Full capacity mode**.
4. Press **F10** to save and exit.
5. When Windows loads, **shut down completely again**, wait 10 seconds, cold boot.
6. Charge and verify it passes 80%. The BIOS-set mode persists across Windows reinstalls and MyASUS reinstalls — this is the durable fix.

### Fix 3: Disable Fast Startup so changes apply

Fast Startup is the silent saboteur of firmware-setting changes.

1. **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. **Uncheck** "Turn on fast startup (recommended)."
4. Click **Save changes**.
5. Redo Fix 1 or Fix 2 — with Fast Startup off, shutdowns are true cold boots and the EC picks up the new mode reliably.
6. You can re-enable Fast Startup later if you like it; just remember to do a full shutdown (or hold **Shift** while clicking Shut down) whenever you change battery modes in the future.

### Fix 4: Reinstall MyASUS cleanly

When MyASUS shows one mode but the laptop does another, the app's state is corrupt.

1. Uninstall **MyASUS** via **Settings > Apps > Installed apps**.
2. Restart the laptop.
3. Reinstall **MyASUS** from the Microsoft Store.
4. Open it, go through first-run device detection (give it a minute to identify your model).
5. Set **Battery Health Charging** to your desired mode in the fresh install.
6. Full shutdown, cold boot, test. If the app still disagrees with reality, trust the BIOS setting (Fix 2) and ignore the app's display.

### Fix 5: Update BIOS and MyASUS components

ASUS fixes Battery Health Charging bugs in firmware updates.

1. Open MyASUS → **System Update** (or **Live Update** on older versions) and install all recommended updates.
2. Check the BIOS version against the latest for your exact model on ASUS support (search your model number).
3. If a BIOS update is available, install it with the charger connected. Don't interrupt the flash.
4. After updating, reconfigure Battery Health Charging (updates reset it — usually to Balanced/80%).
5. Cold boot and verify. Check the BIOS release notes for "battery" mentions — if present, this was likely your root cause.

### Fix 6: Rule out a real charging problem

Make sure the 80% stop is the limiter and not a fault.

1. Set **Full capacity mode** (Fix 2), cold boot, and charge.
2. If it now charges to 100% — it was the limiter. Case closed.
3. If it **still** stops at 80% (or any fixed point) in Full capacity mode, that's not the limiter — run `powercfg /batteryreport` and check the full charge capacity. A battery whose true capacity degraded to ~80% of design will "stop" there because there's nothing more to fill.
4. Also check for overheating during charging — thermal protection can pause charging at any percentage. See [fixing laptop battery overheating](/articles/how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2/).
5. If wear is high, the fix is a new battery, not a settings change. Our guide on [checking design vs full charge capacity](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/) shows how to confirm.

### Fix 7: Choose the right mode for your life (the smart play)

Now that you control it, use it wisely.

1. **Desk-bound 90%+ of the time:** Use **Balanced (80%)** or even **Maximum lifespan (60%)**. Your battery will last years longer, and you never need the runtime.
2. **Mixed use:** **Balanced (80%)** daily; switch to **Full capacity** the night before travel. The mode change + cold boot takes 3 minutes.
3. **Always mobile:** **Full capacity mode**. Runtime matters more than longevity — but expect to replace the battery sooner.
4. **Don't micro-manage:** Constantly toggling modes adds little. Pick the mode matching your dominant usage and change it only for trips.
5. Remember: the 80% cap isn't the enemy. A battery nursed at 80% for three years beats a 100%-charged battery replaced after eighteen months.

## Closing

"Stuck at 80" on an ASUS is a feature with a settings problem, not a hardware problem: set Full capacity mode in the BIOS, cold boot so the EC picks it up, and you're done. And once you're in control, consider leaving the cap on for desk duty — your future self, still on the original battery three years from now, will thank you.

*Related reading: [ASUS battery health charging troubleshooting](/articles/asus-battery-health-charging-stuck-at-80-troubleshooting/), [check design vs full charge capacity](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/)*
