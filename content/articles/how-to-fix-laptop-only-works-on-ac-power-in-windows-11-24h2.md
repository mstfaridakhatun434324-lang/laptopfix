---
title: "How to Fix a Laptop That Only Works on AC Power in Windows 11 24H2"
slug: how-to-fix-laptop-only-works-on-ac-power-in-windows-11-24h2
date: 2026-09-12
categories: ["battery"]
tags: ["ac power", "windows 11 24h2", "battery not detected"]
description: "Laptop dies the second you unplug it on Windows 11 24H2? Fix batteries that won't hold a charge or won't engage at all."
thumbnail: "/images/thumbs/how-to-fix-laptop-only-works-on-ac-power-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my laptop turn off immediately when I unplug the charger?"
    a: "The battery is either fully dead, disconnected internally, or Windows 24H2 is not communicating with it. A dead battery cell, a battery that the system has stopped detecting after an update, or a BIOS that disabled the battery can all cause instant shutdown on unplug."
  - q: "Can a Windows 11 24H2 update kill my battery?"
    a: "The update itself does not damage the battery hardware, but it can corrupt the battery driver, reset the charge controller firmware state, or change power management behavior so the battery no longer engages. These are all software problems and can be fixed without replacing the battery."
  - q: "How do I know if my battery is dead or just not detected?"
    a: "Open Device Manager and look under Batteries. If you see the Microsoft ACPI-Compliant Control Method Battery listed but the laptop still dies on unplug, the battery is likely worn out. If the battery entry is missing entirely, it is a detection problem — driver, BIOS, or hardware connection — not necessarily a dead battery."
  - q: "Is it safe to keep using a laptop that only works on AC power?"
    a: "Yes, as long as the charger is the correct wattage. The laptop runs normally on AC power. The main risk is losing unsaved work during a power cut, since there is no battery backup. Replace or repair the battery when you need portability back."
---

The moment you pull the charger out, the laptop dies like someone yanked the power cord from a desktop. No shutdown, no warning — just black. Plug it back in and it boots fine. If that is your Windows 11 24H2 laptop right now, the battery has effectively checked out of the equation.

This is different from fast drain. Here the battery contributes nothing at all: zero seconds of runtime. The good news is that after the 24H2 update this is often a detection or driver problem, not a dead battery. The fixes below start with software and end with hardware, so you only open the laptop if you have to.

## Why this happens

- **The battery driver failed after the 24H2 update.** The update can corrupt or mismatch the ACPI battery driver, so Windows ignores the battery entirely.
- **The battery is genuinely worn out.** A battery at the end of its life can read 0% available and deliver no current, even while Windows shows it as "present."
- **The battery got disabled in BIOS or UEFI.** Some firmware has a battery disable option used during servicing, and an update can leave it toggled off.
- **The internal battery cable is loose or corroded.** Drops, heat cycles, and age loosen the connector between the battery and the motherboard.
- **The charge controller is stuck.** The embedded controller that manages charging can lock up and refuse to switch to battery power.
- **The wrong charger is masking the problem.** An underpowered charger can run the laptop on AC while never charging the battery, making it look like the battery is dead.
- **Battery firmware needs re-enumeration.** Sometimes the battery simply needs to be redetected by the system, like any other piece of hardware.

## How to fix it

Work through these in order — most 24H2 cases are solved by the first three fixes.

### Fix 1: Check what Windows actually sees

Before touching anything, get the facts. A battery report tells you whether the battery exists as far as Windows is concerned.

1. Right-click **Start** and open **Terminal (Admin)**.
2. Run `powercfg /batteryreport` and note the file path it prints.
3. Open the HTML report in your browser.
4. Check **Design Capacity** vs **Full Charge Capacity**. If full charge capacity is under 20% of design, the battery is worn out.
5. Look at **Battery capacity history** — a sudden cliff right around the 24H2 update date points to a software issue, not wear. Our guide on [checking battery health on Windows 11](/articles/how-to-check-battery-health-on-windows-11-laptop/) walks through reading every section of this report.

### Fix 2: Reinstall the ACPI battery driver

This is the number one fix for the post-24H2 version of this problem.

1. Shut the laptop down and unplug the charger.
2. If the battery is removable, take it out for 30 seconds. If it is internal, skip this step.
3. Plug in the charger, boot into Windows.
4. Press **Win + X** and open **Device Manager**.
5. Expand **Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery**, and choose **Uninstall device**.
6. Click **Action** > **Scan for hardware changes** to reinstall it.
7. Restart the laptop, unplug the charger, and see if it stays alive.
8. If the Batteries section was completely empty, see our guide on a [battery not detected in Windows 11](/articles/laptop-battery-not-detected-windows-11/).

### Fix 3: Perform an embedded controller reset

The embedded controller (EC) manages the battery hardware. A hard reset clears its stuck state.

1. Shut the laptop down completely (hold **Shift** while clicking **Shut down** to bypass fast startup).
2. Unplug the charger and all USB devices.
3. If the battery is removable, remove it. Press and hold the power button for 30 seconds.
4. Reinsert the battery, plug in the charger, and power on.
5. For sealed laptops, many brands have a pinhole reset button on the bottom — press it with a paperclip for 10 seconds. Check your manual: [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) list the exact procedure per model.

### Fix 4: Verify the battery is enabled in BIOS

A BIOS update or reset can disable the battery without any visible warning in Windows.

1. Restart and press the BIOS key during boot (**F2** for Dell, **F10** for HP, **F1** or **Fn+F2** for Lenovo, **Del** for ASUS).
2. Look under **Advanced**, **Power**, or **Battery** sections for anything like "Battery," "Internal Battery," or "Battery Disconnect."
3. Make sure the battery is enabled. Some Lenovo models have a "Disable built-in battery" option used for servicing — it must be off for normal use.
4. Save and exit. Boot into Windows and unplug the charger to test.
5. While in BIOS, check the battery status page if your firmware has one — it often shows the real health percentage.

### Fix 5: Rule out the charger

An underpowered or failing charger creates exactly this symptom: enough juice to run, not enough to charge.

1. Check the wattage printed on the charger brick (e.g., 65W, 90W, 130W).
2. Compare it to what your laptop requires — printed on the bottom panel or in the manual.
3. If you are using a USB-C charger, make sure it supports Power Delivery at your laptop's required wattage. A 45W phone charger will not charge a 65W laptop properly.
4. Borrow the original charger or a known-good equivalent and test for an hour.
5. Watch the taskbar battery icon: it should say "plugged in, charging," not just "plugged in." If it never charges, the charger or the charging circuit is suspect.

### Fix 6: Update the BIOS and chipset drivers

The 24H2 update can expose firmware bugs in older BIOS versions that break battery handoff.

1. Find your exact model number on the bottom of the laptop.
2. Download the latest BIOS from the manufacturer's support site — never from a random driver site.
3. Run the BIOS update **with the charger plugged in** and do not interrupt it.
4. After the BIOS update, also install the latest chipset driver package from the same site.
5. Boot into Windows, let it sit on the charger for 30 minutes, then unplug and test.
6. If the BIOS update itself caused charging trouble instead, see our guide on [battery not charging after a BIOS update](/articles/how-to-fix-battery-not-charging-after-bios-update-in-windows-11-24h2/).

### Fix 7: Test with a full discharge-recharge cycle

Sometimes the battery gauge is so far off that the controller refuses to engage the battery. A full cycle can recalibrate it.

1. With the charger plugged in, go to **Settings** > **System** > **Power & battery** and set **Screen and sleep** timeouts to **Never** temporarily.
2. Unplug the charger. If the laptop dies instantly, this fix does not apply — skip to Fix 8.
3. If it stays on but the percentage drops oddly fast, let it run until it sleeps or hibernates on its own.
4. Leave it off and unplugged for 2 hours, then charge it uninterrupted to 100%.
5. Repeat once more. If runtime improves, the gauge was miscalibrated. For a proper calibration routine, see [how to calibrate a laptop battery on Windows 11](/articles/how-to-calibrate-laptop-battery-windows-11/).

### Fix 8: Check the physical battery connection

If software fixes all failed, the battery may be physically disconnected.

1. Shut down, unplug everything, and remove the back panel (you will need a small Phillips screwdriver; check a teardown video for your exact model).
2. Find the battery connector on the motherboard — a wide multi-pin plug with a cable to the battery pack.
3. Unplug it, inspect for corrosion or bent pins, then firmly reseat it.
4. Look at the battery itself: any swelling, warping, or a sweet chemical smell means stop — a swollen battery is a fire risk and must be replaced, not reseated.
5. Reassemble and test on battery power.

## Closing

For most people on 24H2, reinstalling the ACPI battery driver or resetting the embedded controller brings the battery back to life. If none of the software fixes work and the battery report shows a collapsed full charge capacity, the battery itself is done — a replacement battery for most models costs far less than a new laptop.
