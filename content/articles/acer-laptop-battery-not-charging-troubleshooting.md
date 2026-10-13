---
title: "Acer Laptop Battery Not Charging? Troubleshooting Guide"
slug: acer-laptop-battery-not-charging-troubleshooting
date: 2026-09-16
categories: ["battery"]
tags: ["acer battery not charging", "acer aspire", "acer nitro", "battery reset pinhole"]
description: "Acer laptop plugged in but not charging? Use Acer's battery reset pinhole, Acer Care Center checks, and driver fixes to get charging working again."
thumbnail: "/images/thumbs/acer-laptop-battery-not-charging-troubleshooting.webp"
faqs:
  - q: "Where is the battery reset pinhole on my Acer laptop?"
    a: "On most Acer Aspire, Swift, and Nitro models, it's a tiny hole on the bottom panel, usually near the center, marked with a battery icon. Push a straightened paperclip in and hold for 5 seconds while the laptop is off and unplugged to reset the embedded controller."
  - q: "Why does my Acer say 'plugged in, not charging'?"
    a: "This usually means a battery limit feature is active, the driver is stuck, or the charger isn't delivering enough power. Check Acer Care Center's battery settings first, then reinstall the ACPI battery driver, then test the charger."
  - q: "Does Acer Care Center help with battery problems?"
    a: "Yes — Acer Care Center (preinstalled on most Acers) shows battery health status and runs hardware diagnostics. It's the fastest way to check whether Acer itself considers your battery healthy before you start troubleshooting."
  - q: "Should I update the BIOS on my Acer to fix charging?"
    a: "Only if Acer's support page lists a BIOS update that mentions battery or charging fixes for your exact model. Update with the charger connected and don't interrupt it. A BIOS update won't fix a worn-out battery, so check battery health first."
---

Acer laptops have a few brand-specific quirks when it comes to charging problems — most notably the little battery reset pinhole on the bottom panel that most owners never notice. If your Acer says "plugged in, not charging," or the battery percentage refuses to climb, this guide starts with the Acer-specific fixes and then covers the universal ones.

A quick note on Acer's lineup: the Aspire and Swift lines are straightforward ultrabooks where the standard fixes apply cleanly, while the Nitro and Predator gaming lines draw so much power that charger wattage becomes the dominant issue. If you own a Nitro or Predator, pay extra attention to the charger checks — a surprising number of "not charging" reports on those models trace back to someone using a lower-wattage adapter.

## Why this happens

- **The embedded controller is stuck.** Acer's EC manages charging, and it can lock up after power events. Acer built the reset pinhole specifically for this.
- **Acer Care Center battery settings** may have a charge limit enabled that caps charging at 80% for battery longevity.
- **Underpowered or third-party charger.** Acer gaming laptops (Nitro, Predator) are picky — a 65W USB-C charger on a machine that expects a 135W+ barrel adapter won't charge properly.
- **Corrupted ACPI battery driver**, especially after Windows updates — the same driver issue that affects all brands.
- **Worn battery cells** that can no longer accept a charge, common on Acers older than 3–4 years.
- **Loose DC jack or damaged charging port**, particularly on models where the barrel connector takes mechanical stress.
- **BIOS bug** on certain firmware versions that mishandles the charge handshake.

## How to fix it

Work through these in order, starting with Acer's own tools.

### Fix 1: Use the battery reset pinhole

This is Acer's official reset procedure and it fixes a large share of charging glitches.

1. Shut the laptop down completely and unplug the charger and all USB devices.
2. Flip the laptop over and find the small pinhole with a battery icon next to it (usually near the middle of the bottom panel).
3. Straighten a paperclip, push it into the hole, and hold for 5 seconds. You'll feel a faint click.
4. Plug the charger back in, wait a minute, then power on and check whether charging resumes.

### Fix 2: Check Acer Care Center

Acer Care Center is preinstalled on most Acer laptops and gives you the manufacturer's own read on battery health.

1. Open **Acer Care Center** from the Start menu (install it from the Microsoft Store if missing).
2. Go to the battery or system check section and run the battery diagnostic.
3. Look at the reported battery health. If Acer flags it as poor, skip to Fix 8 — the battery needs replacing.
4. Check for any battery charge limit settings and disable them temporarily for testing.

### Fix 3: Reinstall the battery drivers

The standard Windows fix, and it applies to Acers too.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Also uninstall **Microsoft AC Adapter** if present.
4. Shut down, unplug for 30 seconds, reconnect, and boot. Windows reinstalls the drivers.

For a deeper explanation of what these drivers do, see [the red X battery icon fix](/articles/how-to-fix-battery-x-icon-red-cross-step-by-step/), which covers the same driver reset.

### Fix 4: Verify the charger is correct for your model

Acer's gaming lines are especially sensitive to charger wattage.

1. Check the wattage printed on your charger's label and compare it to the requirement on the laptop's bottom sticker.
2. If you're using a USB-C charger on a Nitro or Predator, switch to the original barrel-style Acer adapter — many Acer gaming laptops only charge properly through the dedicated DC jack.
3. Inspect the DC jack for looseness. If the plug wobbles, the jack itself may need repair.

### Fix 5: Test with the battery calibration routine

If the battery charges to a point then stops, the gauge may be misreading.

1. Charge to 100%, then unplug and run the battery down to about 5% through normal use.
2. Shut down, recharge uninterrupted to 100%, and see if the "not charging" message clears.
3. Generate a report with `powercfg /batteryreport` in an admin terminal to confirm the capacity numbers look sane.

### Fix 6: Check the charging LED behavior

Acer's charging LED is a diagnostic tool most people ignore. Its behavior tells you where the failure is:

1. **No LED at all** with the charger plugged in: the charger is dead, the outlet is dead, or the DC jack has failed. Try another outlet and inspect the jack.
2. **LED on but battery not charging**: power is reaching the laptop but the battery circuit isn't engaging — this points to the EC, the driver, or the battery itself. The pinhole reset (Fix 1) is your best bet here.
3. **LED blinking**: on many Acer models this signals a battery fault or an incompatible charger. Note the blink pattern and compare against your model's manual.
4. If the LED behaves normally but Windows insists the battery isn't charging, the issue is on the software side — drivers and Acer Care Center settings.

### Fix 7: Update the BIOS from Acer's support site

1. Find your exact model (e.g., Aspire 5 A515-56) and check Windows Update's optional updates for a firmware entry, or use Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) guidance on firmware updates.
2. Only update if the changelog mentions battery, charging, or EC fixes.
3. Keep the charger connected throughout and don't touch the machine until it reboots on its own.

### Fix 8: Replace the battery

If Acer Care Center reports poor health and the battery report confirms low full charge capacity, order a genuine Acer battery by part number. Acer batteries have a model-specific part number printed on the battery label — match it exactly. Third-party "compatible" packs for Acers are notorious for triggering "battery not detected" errors because of missing authentication chips.

## Closing

Acer gives you two advantages most brands don't: the reset pinhole and Acer Care Center's built-in diagnostics. Use them first — the pinhole reset alone resolves an outsized share of "plugged in, not charging" complaints on Aspire, Swift, and Nitro machines. If the diagnostics say the battery is healthy but it still won't charge, the driver and charger checks will get you the rest of the way there. And if the problem turns out to be general battery wear rather than anything Acer-specific, our guide on [batteries that won't hold a charge](/articles/laptop-battery-won-t-hold-charge-troubleshooting/) picks up where this one leaves off.
