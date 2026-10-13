---
title: "Acer Laptop Battery Not Charging? Step-by-Step Fix"
slug: how-to-fix-acer-laptop-battery-not-charging-step-by-step
date: 2026-09-12
categories: ["battery"]
tags: ["acer", "battery not charging", "care center", "troubleshooting"]
description: "Acer laptop plugged in but not charging? From the battery reset pinhole to Acer Care Center settings, here are the Acer-specific fixes in order."
thumbnail: "/images/thumbs/how-to-fix-acer-laptop-battery-not-charging-step-by-step.webp"
faqs:
  - q: "Where is the battery reset button on an Acer laptop?"
    a: "Most modern Acer laptops (Aspire, Swift, Nitro, Predator) have a battery reset pinhole on the bottom panel — a tiny hole, sometimes labeled with a battery icon. With the charger unplugged, push a straightened paperclip in and hold for 15-30 seconds. This disconnects the internal battery at the EC level and clears charging faults."
  - q: "Why does my Acer say 'plugged in, not charging'?"
    a: "Common Acer-specific causes: the battery reset pinhole needs pressing after a deep discharge, Acer Care Center's battery charge limit is set to 80%, the charger wattage doesn't match (especially on Nitro/Predator gaming models), or the standard Windows battery driver is corrupt. Work through them in that order."
  - q: "Does Acer Care Center limit battery charging?"
    a: "Yes — Acer Care Center has a Battery Health option that can cap charging at 80% to extend lifespan. If your battery stops at 80% and won't go higher, check Acer Care Center > Battery > Battery Health before assuming hardware failure. Switch it back to full charge mode when you need maximum runtime."
  - q: "My Acer Nitro/Predator won't charge while gaming. Is that normal?"
    a: "It can be, if you're using an underpowered charger. Gaming Niros and Predators ship with 135W-280W adapters; a 90W universal charger can't run the GPU and charge simultaneously. Always use the original wattage adapter for gaming models — the battery may even drain slowly under full load with a weak charger, which is expected behavior."
---

Acer's charging problems have a distinctive flavor: the battery reset pinhole, Acer Care Center's charge limiter, and gaming models that are extremely picky about adapter wattage. If you've tried generic Windows fixes without luck, the Acer-specific steps below are probably what you were missing.

One important note up front: on Acer gaming laptops (Nitro, Predator), "not charging" while gaming with the wrong adapter is often working-as-designed. Check your adapter wattage before anything else.

## Why this happens

- **EC latched after deep discharge:** Acer's embedded controller commonly latches into a no-charge state after the battery drains to absolute zero. The pinhole reset is the designed fix.
- **Acer Care Center charge limit:** The Battery Health feature caps charging at 80%. Users enable it, forget, and later read it as a fault.
- **Wrong adapter wattage:** Especially on Nitro/Predator — a 90W charger on a 180W machine can't charge under load. Acer's barrel adapters also have thin center pins that break.
- **Corrupt Windows battery driver:** The usual ACPI driver issue; worth ruling out on Acers too.
- **BIOS battery calibration drift:** The gauge drifts and the controller refuses charge because it misreads the battery state.
- **DC jack wear:** Acer's slim barrel jacks loosen over time, causing intermittent charging that looks like a battery problem.
- **Failed battery:** Genuine end-of-life, verifiable via battery report wear numbers.

## How to fix it

Work through these in order — Acer's pinhole reset first, since it's the brand's signature fix.

### Fix 1: Use the battery reset pinhole

This is Acer's built-in EC reset, and it resolves a huge share of Acer charging issues.

1. Shut down the laptop completely and **unplug the charger**.
2. Flip the laptop over and find the **battery reset pinhole** — a tiny hole on the bottom panel, sometimes marked with a battery symbol. (On some Aspire models it's near the center; on Nitro/Predator it's often toward the rear.)
3. Straighten a paperclip and push it gently into the hole until you feel a click. **Hold for 15-30 seconds.**
4. Remove the paperclip, plug the charger back in, and wait 10 seconds before powering on.
5. Watch the charging LED: it should show normal charging behavior now. Let it charge for 15 minutes undisturbed.
6. If the pinhole doesn't exist on your model (some older Acers), do the manual equivalent: unplug, hold the power button for 30 seconds, replug.

### Fix 2: Verify the adapter wattage and condition

Acer gaming laptops are wattage-sensitive; even non-gaming models need the right adapter.

1. Check the original adapter's wattage printed on the brick. Nitro/Predator models typically need **135W, 180W, or 280W** — a standard 65W/90W universal adapter will not properly charge them.
2. If you're using a third-party or universal adapter, compare its wattage to the original. Underpowered = slow/no charging under load.
3. Inspect the barrel plug, especially the thin center pin — Acer pins bend and snap. A damaged pin means no charging even from a "working" brick.
4. Plug directly into a wall outlet, not a power strip, and confirm the brick's LED (if it has one) is lit.
5. For USB-C charging Acers (Swift series): use a PD charger matching the original wattage (usually 45W or 65W) with a 100W-rated cable. See our guide on [slow USB-C PD charging](/articles/how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-11/) if that's your situation.

### Fix 3: Check Acer Care Center battery settings

The 80% cap catches everyone at least once.

1. Open **Acer Care Center** (search Start; download from Acer's site or the Microsoft Store if missing).
2. Go to the **Battery** section and check **Battery Health** / charge limit settings.
3. If it's set to limit charging (often labeled as an 80% health mode), switch it to **full charge** mode temporarily and test.
4. Note: on some models this setting only appears when the charger is connected.
5. If Care Center won't open or shows no battery section, reinstall it from Acer's support site for your exact model — but honestly, the feature is optional; the pinhole and driver fixes matter more.

### Fix 4: Reinstall the battery drivers

Standard Windows-side reset.

1. Right-click **Start** → **Device Manager** → expand **Batteries**.
2. Uninstall **Microsoft ACPI-Compliant Control Method Battery** (and **Microsoft AC Adapter** if present).
3. Shut down fully, unplug for 30 seconds, plug back in, power on.
4. Windows reinstalls the drivers automatically.
5. Open an admin Command Prompt, run `powercfg /batteryreport`, and check whether Windows now shows the battery charging. Our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/) explains how to read the charge status rows.

### Fix 5: Update BIOS and drivers from Acer

Acer fixes charging/EC behavior in BIOS updates.

1. Go to Acer Support, enter your serial number or model (Aspire 5 A515-5x, Nitro 5 AN515-xx, etc. — the full model matters).
2. Download the latest **BIOS**, **chipset**, and **Intel/AMD power management** drivers.
3. Install chipset drivers first, then BIOS, with the charger plugged in and battery above 30%.
4. Don't touch the laptop during the BIOS flash until it reboots itself.
5. After updating, redo the pinhole reset (Fix 1) — BIOS updates can leave the EC in a confused state that the pinhole clears.
6. Recheck Acer Care Center settings afterward, since BIOS updates can reset them.

### Fix 6: Inspect the DC jack and test systematically

Rule out the physical connection.

1. With the charger plugged in, gently wiggle the barrel connector. Steady LED = good jack. Flickering = loose jack.
2. Look inside the jack for debris or bent contacts; check the plug for a bent center pin.
3. Test with the battery removed if your Acer has a removable battery (increasingly rare, but some Aspire models still do): run on AC alone to confirm the adapter and motherboard are fine.
4. For internal batteries: if the laptop runs fine on AC but won't charge the battery, and the pinhole + drivers + BIOS didn't help, you're likely looking at battery failure (Fix 7) or a motherboard charging circuit issue.
5. Don't use a laptop that only charges when the plug is held at an angle — intermittent arcing damages the motherboard over time.

### Fix 7: Check battery health and replace if needed

Get the numbers before spending money.

1. Run `powercfg /batteryreport` from an admin terminal.
2. Compare **Design Capacity** vs **Full Charge Capacity**. Over 40% wear with charging problems = replacement time.
3. Get the exact battery model number from the battery label (visible if you open the bottom panel) or Acer's support page for your model.
4. Buy genuine Acer or a reputable OEM-equivalent — cheap marketplace batteries are the #1 source of recurring "not charging" complaints on Acers.
5. Check warranty: Acer batteries are typically covered 1 year. Use the serial number lookup on Acer's support site before buying.
6. Internal battery replacement on most Aspire/Swift models is 8-12 screws and one connector — very DIY-friendly. Nitro/Predator models are similar but have more cables to mind. If you're not comfortable, a local shop charges modestly for this.

## Closing

Acer charging issues bow to Acer-specific fixes: the pinhole reset for EC latch-ups, the correct-wattage adapter (especially on Nitro/Predator), and Acer Care Center's charge limiter. Run those before assuming the battery is dead, and check the actual wear numbers before spending money on a replacement.

*Related reading: [generate a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/), [USB-C PD charger slow](/articles/how-to-fix-usb-c-pd-charger-charging-slowly-on-windows-11/)*
