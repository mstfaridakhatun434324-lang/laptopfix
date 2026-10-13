---
title: "How to Fix ASUS Battery Health Charging Stuck at 80%"
slug: how-to-fix-asus-battery-health-charging-stuck-at-80-reddit
date: 2026-09-21
categories: ["battery"]
tags: ["asus", "battery health charging", "myasus"]
description: "ASUS laptop refusing to charge past 80%? Fix Battery Health Charging stuck in Balanced mode and restore full capacity charging."
thumbnail: "/images/thumbs/how-to-fix-asus-battery-health-charging-stuck-at-80-reddit.webp"
faqs:
  - q: "What is ASUS Battery Health Charging?"
    a: "It is a feature in the MyASUS app that limits maximum charge to extend battery lifespan: Full Capacity Mode (100%), Balanced Mode (80%), and Maximum Lifespan Mode (60%). Balanced Mode is the default on many models, which is why new ASUS laptops often stop at 80% out of the box."
  - q: "Is charging stuck at 80% on ASUS a bug?"
    a: "Usually not — it is Balanced Mode working as intended. It becomes a bug when you switch to Full Capacity Mode and the laptop still stops at 80%, which points to a MyASUS glitch, a stuck EC setting, or a BIOS-level cap overriding the app."
  - q: "Does limiting charge to 80% really help the battery?"
    a: "Yes. Lithium batteries degrade fastest when held at 100% charge, especially when warm. Capping at 80% can roughly double the number of useful cycles for a laptop that spends most of its life plugged in. Only disable it when you genuinely need maximum runtime."
  - q: "Where is the Battery Health Charging setting if I don't have MyASUS?"
    a: "Some ASUS models expose it in the BIOS under Advanced > Battery Health Charging. If neither MyASUS nor the BIOS has the option, your model may not support the feature — in that case an 80% cap is coming from somewhere else, like a Windows power setting or a faulty gauge."
---

Your ASUS laptop charges to 80% and stops. Dead stop, every time, no matter how long you leave it plugged in. If you just got the laptop, congratulations — nothing is broken. ASUS ships many models with Battery Health Charging set to Balanced Mode, which caps charging at 80% to make the battery last years longer.

The problem starts when you switch it to Full Capacity Mode and it still stops at 80%. That is the actual bug this guide fixes — the setting that will not let go. Work through these in order.

## Why this happens

- **Balanced Mode is enabled in MyASUS.** The default on many ASUS laptops; caps charging at 80% by design.
- **The MyASUS setting did not apply.** The app shows Full Capacity Mode but the embedded controller never got the message.
- **A BIOS-level cap overrides MyASUS.** Some models have a separate Battery Health Charging option in BIOS that wins over the app.
- **MyASUS is outdated or corrupted.** An old or glitched app version fails to communicate the mode change to firmware.
- **The EC setting is stuck.** The embedded controller latched the 80% limit and ignores further changes until reset.
- **The battery gauge needs calibration.** A drifted gauge can coincidentally stop at 80% and look like the limiter.

## How to fix it

Work through these in order — most cases are fixed by correctly applying the mode change.

### Fix 1: Set Full Capacity Mode properly in MyASUS

The setting has to actually stick. Do it deliberately.

1. Open **MyASUS** (install it from the Microsoft Store if missing).
2. Go to **Customization** (on some versions: **Battery Health Charging** under **Device Settings**).
3. Select **Full Capacity Mode**.
4. Keep the charger plugged in and wait 2-3 minutes — the EC needs a moment to accept the change.
5. Unplug the charger for 10 seconds, then plug it back in. This forces the charging circuit to re-evaluate the limit.
6. Watch the battery icon: charging should now continue past 80%.

### Fix 2: Check the BIOS setting

The BIOS option overrides MyASUS. If they disagree, BIOS wins.

1. Restart and press **F2** or **Del** to enter BIOS setup.
2. Look under **Advanced** for **Battery Health Charging**.
3. Set it to **Full Capacity Mode** (or **Disabled**, depending on your BIOS wording — you want no cap).
4. Save and exit (**F10**).
5. Boot into Windows, open MyASUS again, and confirm it also shows Full Capacity Mode.
6. Charge and verify the battery climbs past 80%.

### Fix 3: Update or reinstall MyASUS

A glitchy MyASUS is the most common reason the mode change does not take effect.

1. Open the **Microsoft Store** > **Library** and update **MyASUS** to the latest version.
2. If it is already current, uninstall it: **Settings** > **Apps** > **Installed apps** > **MyASUS** > **Uninstall**.
3. Restart the laptop.
4. Reinstall **MyASUS** fresh from the Microsoft Store.
5. Open it, go to **Customization**, set **Full Capacity Mode**, and test charging.
6. While you are at it, check **System Update** inside MyASUS for pending BIOS and driver updates — install them with the charger connected. If the Microsoft Store refuses to update MyASUS, [Windows support](https://support.microsoft.com/en-us/windows) has Store troubleshooting steps.

### Fix 4: Reset the embedded controller

When the EC latches the 80% limit, no software toggle will move it until the controller resets.

1. Shut down fully: hold **Shift** while clicking **Shut down**.
2. Unplug the charger and all USB devices.
3. Press and hold the power button for 30 seconds.
4. Plug the charger back in and power on.
5. Open MyASUS, confirm **Full Capacity Mode** is selected, and test.
6. Check your model's manual for any model-specific reset variation if the generic reset does not work.

### Fix 5: Calibrate to rule out gauge drift

Make sure the "80%" is real and not a miscalibrated gauge stopping early.

1. With Full Capacity Mode active, charge as far as it goes and leave plugged in for 2 hours.
2. Unplug, set sleep timers to **Never** (**Settings** > **System** > **Power & battery**), and drain the laptop until it shuts down.
3. Leave it off for 3 hours, then charge uninterrupted to maximum.
4. If the stopping point moves after calibration, the gauge was the problem. See our full [battery calibration guide](/articles/how-to-calibrate-laptop-battery-windows-11/).
5. Run `powercfg /batteryreport` and compare design vs full charge capacity to confirm the battery itself is healthy — details in our [battery health check guide](/articles/how-to-check-battery-health-on-windows-11-laptop/).

### Fix 6: Reinstall the ASUS system drivers

The mode change travels through ASUS system drivers. If they are corrupt, the message never arrives.

1. Open **Device Manager**.
2. Expand **System devices** and look for **ASUS System Control Interface** — right-click > **Uninstall device**.
3. Restart; Windows will attempt to reinstall it. If it does not, download the **ASUS System Control Interface** driver for your exact model from ASUS support.
4. Also reinstall the battery driver: **Batteries** > **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device** > **Action** > **Scan for hardware changes**.
5. Open MyASUS, set Full Capacity Mode once more, and test.

### Fix 7: Decide whether you actually want 100%

Honest question worth asking before you fight the limiter too hard.

1. If the laptop mostly sits on your desk plugged in, Balanced Mode at 80% is genuinely better for the battery — it can add years of useful life.
2. Switch to Full Capacity Mode only before travel or long unplugged sessions, then switch back.
3. Our guide on [limiting battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/) covers the lifespan math if you want the details.
4. If you need 100% daily because the battery is old and 80% no longer lasts, the real fix is a battery replacement, not defeating the limiter.

## Closing

An ASUS stuck at 80% is Balanced Mode doing its job until you tell it otherwise — set Full Capacity Mode in both MyASUS and BIOS, and reset the EC if the setting will not stick. And if you mostly use the laptop plugged in, consider leaving the 80% cap on. Your battery will thank you in two years.
