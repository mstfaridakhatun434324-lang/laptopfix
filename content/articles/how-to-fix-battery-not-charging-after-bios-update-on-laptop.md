---
title: "How to Fix Battery Not Charging After a BIOS Update on a Laptop"
slug: how-to-fix-battery-not-charging-after-bios-update-on-laptop
date: 2026-09-13
categories: ["battery"]
tags: ["bios update", "battery not charging", "firmware"]
description: "Battery stopped charging right after a BIOS update? Fix the firmware, driver, and EC issues that block charging after BIOS flashes."
thumbnail: "/images/thumbs/how-to-fix-battery-not-charging-after-bios-update-on-laptop.webp"
faqs:
  - q: "Can a BIOS update really break battery charging?"
    a: "Yes. A BIOS update rewrites the firmware that controls the embedded controller, which manages charging. It can reset battery settings, corrupt the charge profile, or leave the controller in a stuck state where it refuses to charge. The battery hardware itself is almost never damaged."
  - q: "Should I roll back the BIOS to fix the battery?"
    a: "Only as a last resort. Most manufacturers do not officially support BIOS downgrades, and a failed flash can brick the laptop. Try the EC reset, driver reinstall, and BIOS settings fixes first — they resolve the vast majority of post-update charging failures."
  - q: "The BIOS update got interrupted. Is my laptop bricked?"
    a: "Not necessarily. Many modern laptops have BIOS recovery (Dell BIOS Recovery, HP Sure Start, Lenovo crisis recovery) that can restore firmware from a USB stick even if the laptop will not boot. Check your manufacturer's support site for the recovery procedure for your exact model."
  - q: "How long should I wait before assuming charging is broken after a BIOS update?"
    a: "Give it at least 30 minutes on the charger first. Some BIOS updates trigger a battery calibration or firmware sync that temporarily pauses charging. If the taskbar still says 'plugged in, not charging' after an hour, start troubleshooting."
---

Everything was fine, then you installed a BIOS update, and now the battery icon says "plugged in, not charging" — or the percentage just sits frozen while the charger is connected. The timing is not a coincidence. BIOS updates touch the embedded controller firmware that runs charging, and they frequently reset battery-related settings to defaults.

The reassuring part: your battery is almost certainly fine. This is a firmware and configuration problem, and it is fixable without buying a new battery. Work through these fixes from least invasive to most.

## Why this happens

- **The BIOS reset battery settings to defaults.** Charge thresholds, battery health modes, and conservation settings get wiped and replaced with defaults that can block charging.
- **The embedded controller firmware is in a stuck state.** The EC handles charging logic, and a flash can leave it confused about the battery's state.
- **Windows battery drivers no longer match the firmware.** The ACPI driver expects certain responses from the BIOS; after an update, that handshake can break.
- **A battery disconnect or "ship mode" got triggered.** Some updates enable a battery disconnect feature meant for servicing, which electrically isolates the battery.
- **The update was incomplete or partially applied.** An interrupted flash can leave power management tables half-written.
- **Charge profiles changed.** Newer BIOS versions sometimes change charging behavior — for example, enabling a battery health limiter that caps charging at 80%.

## How to fix it

Work through these in order. Do not re-flash the BIOS until you have tried everything else.

### Fix 1: Wait and watch first

Some BIOS updates run a battery firmware sync that temporarily pauses charging.

1. Keep the charger plugged in for at least 60 minutes.
2. Watch the taskbar battery icon. Note exactly what it says: "plugged in, charging" vs "plugged in, not charging."
3. If the percentage creeps up slowly, let it finish — the controller may just be recalibrating.
4. If nothing changes after an hour, move on to Fix 2.

### Fix 2: Check BIOS battery settings

The update likely reset something in here. This is the most common real cause.

1. Restart and enter BIOS (**F2**, **F10**, **Del**, or **Fn+F2** depending on brand).
2. Look for battery-related sections: **Power**, **Advanced**, or **Battery**.
3. On Dell: check **Power Management** > **Primary Battery Charge Configuration** — set it to **Standard** if it got changed to something restrictive.
4. On Lenovo: check for **Conservation Mode** or battery threshold settings and disable them temporarily.
5. On HP: check **Advanced** > **Power Management Options** > **Battery Health Manager** — set it to **Let HP Manage My Charging** while troubleshooting.
6. Look for any **Battery Disconnect**, **Ship Mode**, or **Disable Built-in Battery** option and make sure it is off.
7. Save, exit, and test charging in Windows.

### Fix 3: Reset the embedded controller

The EC is the chip that actually runs charging. Resetting it clears the stuck state that BIOS flashes often cause.

1. Shut down fully: hold **Shift** while clicking **Shut down** in the Start menu.
2. Unplug the charger and every USB device.
3. If your battery is removable, remove it now.
4. Press and hold the power button for a full 30 seconds.
5. Reinsert the battery (if removable), plug in the charger, and power on.
6. For sealed laptops, use the pinhole EC reset on the bottom if your model has one — a 10-second press with a paperclip. Manufacturer support pages ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) document the exact location.

### Fix 4: Reinstall the battery drivers in Windows

The driver-to-firmware handshake breaks more often than people expect after a BIOS flash.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**. Do the same for **Microsoft ACPI-Compliant Control Method Battery** if there are two entries.
4. Expand **System devices** and look for anything battery or ACPI related that shows a warning icon — uninstall those too.
5. Click **Action** > **Scan for hardware changes**.
6. Restart the laptop with the charger plugged in and check whether charging resumes.
7. If Windows cannot see the battery at all after this, see our guide on a [battery not detected in Windows 11](/articles/laptop-battery-not-detected-windows-11/).

### Fix 5: Load BIOS defaults and reconfigure

A half-migrated settings table from the old BIOS can cause weird charging behavior. Loading defaults wipes it clean.

1. Enter BIOS setup.
2. Find **Load Optimized Defaults**, **Load Setup Defaults**, or press the key shown (often **F9**).
3. Confirm, then save and exit.
4. Boot into Windows and test charging for 15 minutes.
5. If charging works now, go back into BIOS and reapply any settings you actually need (boot order, virtualization, etc.).
6. Check the battery status page in BIOS if available — some firmware shows whether the battery is detected and its health.

### Fix 6: Re-flash the same BIOS version

If the first flash was interrupted or incomplete, re-applying it cleanly can fix power management tables.

1. Download the BIOS installer for your exact model from the manufacturer's official support site only.
2. Close all programs. Plug in the charger — the updater will refuse to run on battery.
3. Run the installer and do not touch the laptop until it completes and reboots on its own.
4. After booting, leave the charger connected for 30 minutes and verify charging.
5. If the manufacturer offers a BIOS recovery USB option, keep that in mind as a fallback — but a normal re-flash fixes most incomplete updates.

### Fix 7: Check for a stuck charge limiter

Newer BIOS versions sometimes enable battery lifespan features by default that look exactly like "not charging."

1. In Windows, open your manufacturer's app (MyASUS, Lenovo Vantage, Dell Power Manager, MSI Center).
2. Look for **Battery Health Charging**, **Conservation Mode**, or **Battery Care Function**.
3. If charging is capped at 60% or 80%, that is the limiter doing its job — set it to **Full capacity mode** to test.
4. Some limiters only engage after the BIOS update turns them on for the first time, which is why charging "broke" right after the flash.
5. Decide whether you want the limiter on long-term — capping at 80% genuinely extends battery lifespan if you mostly use the laptop plugged in. Our guide on [limiting battery charge to 80%](/articles/how-to-limit-battery-charge-to-80/) explains the tradeoffs.

## Closing

A BIOS update does not kill batteries — it resets the firmware settings and controller state that charging depends on. Checking the BIOS battery options, resetting the embedded controller, and reinstalling the Windows battery drivers resolves this for nearly everyone. Only consider a BIOS rollback if the manufacturer explicitly supports it for your model.
