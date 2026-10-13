---
title: "How to Fix an Acer Laptop Battery That Won't Charge"
slug: how-to-fix-acer-laptop-battery-not-charging
date: 2026-09-19
categories: ["battery"]
tags: ["Acer", "battery not charging", "troubleshooting"]
description: "Acer laptop battery not charging? These Acer-specific fixes cover the battery reset pinhole, Acer Care Center settings, and driver resets."
thumbnail: "/images/thumbs/how-to-fix-acer-laptop-battery-not-charging.webp"
faqs:
  - q: "What is the battery reset pinhole on Acer laptops?"
    a: "Many Acer laptops have a small pinhole on the bottom labeled with a battery icon. Pressing a straightened paperclip into it for 5–15 seconds disconnects the internal battery, performing a hard reset of the charging circuit without opening the laptop."
  - q: "Why does my Acer say plugged in but not charging?"
    a: "Common causes include Acer's battery charge limit being enabled in Acer Care Center, a stuck embedded controller (fixed with the pinhole reset or a power drain), a worn battery, or a corrupted ACPI battery driver after a Windows update."
  - q: "Does Acer have a battery charge limit feature?"
    a: "Yes. Acer Care Center includes a battery charge limit option (often capped at 80%) designed to extend battery lifespan. If enabled, the laptop intentionally stops charging at the limit, which looks like a fault if you forgot it was on."
  - q: "How do I update my Acer battery drivers?"
    a: "Open Device Manager, expand Batteries, uninstall the Microsoft ACPI-Compliant Control Method Battery device, then use Action and Scan for hardware changes to reinstall it. For chipset and power management drivers, download them from Acer's official support page for your exact model."
---

Acer laptops that refuse to charge usually suffer from one of a handful of Acer-specific quirks: the battery reset pinhole that nobody knows about, a charge limit quietly enabled in Acer Care Center, or the classic stuck charging controller. The brand-neutral steps matter too, but start with the Acer-specific ones — they resolve most cases.

Before diving in, it helps to know whether you are dealing with a dead battery or a charging fault. Our general [battery not charging troubleshooting guide](/articles/laptop-battery-not-charging-troubleshooting/) walks through that distinction if you are unsure.

## Why this happens

- **Acer's battery charge limit is on.** Acer Care Center can cap charging at 80% to prolong battery life. If it was enabled — sometimes by default after a reinstall — the battery stops at the cap and never reaches 100%.
- **Stuck embedded controller.** Acer's charging controller can lock up after a deep discharge or a power surge, refusing to charge until it is hard-reset.
- **Worn or failed battery.** Acer batteries last roughly 300–500 cycles. A battery at end of life may show "plugged in, not charging" because its controller refuses unsafe charging.
- **Corrupted ACPI battery driver.** Windows updates occasionally break the battery driver, blocking communication between Windows and the charging hardware.
- **Faulty or underpowered adapter.** A damaged charger, a loose DC jack, or a third-party adapter with the wrong wattage can power the laptop without charging the battery.
- **BIOS needs an update.** Acer releases BIOS updates that fix charging bugs on specific models — worth checking if the hardware otherwise tests fine.

## How to fix it

Work through these in order, starting with the Acer-specific resets.

### Fix 1: Use the battery reset pinhole

This is Acer's built-in hard reset for the battery circuit, and it fixes a large share of Acer charging problems.

1. Shut the laptop down completely and unplug the AC adapter and all peripherals.
2. Flip the laptop over and look for a small pinhole on the bottom panel, usually marked with a battery icon.
3. Straighten a paperclip and gently press it into the pinhole. Hold for **5–15 seconds** — you may feel a slight click.
4. Remove the paperclip, plug the AC adapter back in, and wait 30 seconds before powering on.
5. Check the battery icon. If it now shows charging, the embedded controller was stuck and the reset cleared it.

### Fix 2: Check Acer Care Center's battery charge limit

Acer's own utility may be deliberately capping your charge.

1. Open **Acer Care Center** from the Start menu (download it from the Microsoft Store or Acer's site if it is missing).
2. Go to the **Battery** or **Checkup** section and look for **Battery Charge Limit** or a similar option.
3. If the limit is enabled (commonly 80%), the battery will stop there by design. Disable it temporarily to test whether charging resumes to 100%.
4. If you keep the laptop docked most of the time, leaving the limit on is actually good for long-term battery health — just know it is the reason the battery "won't charge past 80%."

### Fix 3: Do a full power drain reset

If your model lacks the pinhole, a manual power drain achieves the same reset.

1. Shut down the laptop and disconnect the AC adapter and all USB devices.
2. If the battery is removable, slide it out. If it is internal, leave it in place.
3. Press and hold the power button for a full **30 seconds**.
4. Reconnect the adapter (and battery), then power on and check charging status.

### Fix 4: Reinstall the battery driver

A corrupted driver after a Windows update is a common and quick fix.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
3. Click **Action** in the menu bar, then **Scan for hardware changes** to reinstall the driver automatically.
4. Restart the laptop with the charger connected and observe the battery icon for a few minutes. For additional background on Windows battery management, Microsoft's [support pages](https://support.microsoft.com/en-us/windows) are worth a read.

### Fix 5: Test the adapter and charging port

Rule out the power supply before blaming the laptop.

1. Inspect the charger's cable along its full length for kinks, cuts, or a loose strain relief near the brick.
2. Wiggle the plug gently in the laptop's charging port — if charging cuts in and out, the DC jack is loose or worn.
3. Check the charger's label: the output voltage must match the laptop's requirement (usually 19V for Acer), and the wattage should meet or exceed the original.
4. If possible, test with another Acer-compatible adapter of the correct wattage. For adapter-specific diagnosis, see our guide to [charger not detected troubleshooting](/articles/laptop-charger-not-detected-troubleshooting/).

### Fix 6: Update the BIOS from Acer's support site

Acer publishes BIOS updates that address charging behavior on many models.

1. Find your exact model number on the bottom sticker (for example, Aspire 5 A515-56).
2. Go to Acer's support website, enter the model, and open **Drivers and Manuals**.
3. Download the latest **BIOS/Firmware** update for your model.
4. With the AC adapter plugged in and all programs closed, run the updater and do not interrupt it.
5. The system restarts automatically. Verify charging afterward.

### Fix 7: Check battery health and replace if worn out

If everything else passes, the battery itself may be finished.

1. Open an administrator **Terminal** (**Win + X**, then **Terminal (Admin)**) and run `powercfg /batteryreport`.
2. Open the generated report and compare **Full Charge Capacity** to **Design Capacity**.
3. If the battery holds less than 60% of its design capacity, or the cycle count is very high, replacement is the sensible move.
4. Order a battery matching the exact part number on the old battery's label. After swapping, run a full charge-discharge cycle to [calibrate the new battery](/articles/how-to-calibrate-laptop-battery-windows-11/).

## Closing

Acer charging issues are rarely mysterious once you know the brand's quirks: try the pinhole reset, check Acer Care Center's charge limit, and reinstall the battery driver before you spend money on parts. Those three steps resolve the majority of cases. If the battery report shows heavy wear, though, no reset will bring the capacity back — a genuine replacement battery is the honest fix, and your Acer will be back to full-day runtime.
