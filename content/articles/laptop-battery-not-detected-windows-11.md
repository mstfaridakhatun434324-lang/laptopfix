---
title: "Fix: Laptop Battery Not Detected in Windows 11"
slug: laptop-battery-not-detected-windows-11
date: 2026-09-04
categories: ["battery"]
tags: ["battery not detected", "windows 11", "device manager"]
description: "Windows 11 says no battery is detected? Fix it with a power reset, battery driver reinstall, and BIOS checks — most cases solved without opening the laptop."
thumbnail: "/images/thumbs/laptop-battery-not-detected-windows-11.webp"
faqs:
  - q: "Why does Windows 11 say no battery is detected when the battery is inside?"
    a: "Usually the battery controller stopped responding to Windows — a driver glitch, a failed handshake after an update, or the battery entering a protection state after deep discharge. The battery is physically present; Windows just can't see it."
  - q: "Will reinstalling the battery driver delete anything?"
    a: "No. Uninstalling the Microsoft ACPI-Compliant Control Method Battery driver only removes the software interface. Windows reinstalls it automatically on reboot, and your files and settings are untouched."
  - q: "Can a Windows update cause the battery to disappear?"
    a: "Yes, this is one of the most common triggers. Updates can replace the battery driver with an incompatible version or interrupt the battery controller during firmware changes. A driver reinstall and power reset usually bring it back."
  - q: "How do I know if it's a dead battery versus a software problem?"
    a: "If the laptop runs on the charger but the battery never appears even in BIOS, and the battery is over 3 years old or swollen, suspect hardware. If it appeared before an update or a deep discharge, suspect software first."
---
"No battery is detected" — and yet the battery is right there inside your laptop. The icon shows an X, the laptop only works plugged in, and unplugging it kills the machine instantly. It's alarming, but in most cases Windows has simply lost contact with the battery controller, not the battery itself.

The battery talks to Windows through a driver and a hardware handshake. When that conversation breaks — after an update, a deep discharge, or a static glitch — Windows reports no battery at all. The fixes below re-establish that connection, from the simplest power reset up to a BIOS check.

## Why this happens

- **The battery driver glitched or got replaced.** Windows updates sometimes install a battery driver version that doesn't handshake correctly with your specific battery controller.
- **The battery entered protection mode.** After a very deep discharge, some battery controllers shut down communication until they receive a proper charge cycle.
- **A power reset is needed.** Residual charge in the motherboard's capacitors can leave the battery controller in a confused state that survives normal reboots.
- **The battery isn't seated properly.** On laptops with removable batteries, a slightly loose pack breaks the data pins' contact even though power pins still work.
- **BIOS can't see it either.** If the battery is invisible in BIOS setup, the problem is below Windows — firmware, connector, or a genuinely dead battery.
- **Physical battery failure.** Rare as a first cause, but real: a failed cell or controller board makes the battery electrically silent.

## How to fix it

Work through these in order. Stop when the battery reappears.

### Fix 1: Do a full power reset

This clears the confused state in the battery controller and motherboard.

1. Shut down the laptop completely (not sleep, not hibernate — **Start** > **Power** > **Shut down**).
2. Unplug the charger.
3. If the battery is removable, take it out. If it's internal, skip this.
4. Press and hold the power button for **30 seconds** to drain residual charge.
5. Reinsert the battery (if removed), plug in the charger, and power on.

### Fix 2: Reinstall the battery drivers

The classic fix for "no battery detected" after a Windows update.

1. Press **Windows key + X** and open **Device Manager**.
2. Expand **Batteries**. You'll usually see **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**. Check nothing else — just confirm.
4. Repeat for any other entries under **Batteries** except the AC Adapter.
5. Restart the laptop. Windows reinstalls the drivers automatically during boot.
6. Check the taskbar — the battery icon should return within a minute of login.

Once the battery reappears but sits at 0% or refuses to charge, you've moved past detection into a different fault — our [battery-not-charging guide](/articles/how-to-fix-laptop-battery-not-charging-after-windows-11-24h2-update/) picks up exactly there.

### Fix 3: Run the Windows power troubleshooter

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Run the **Power** troubleshooter and apply any fixes it suggests.
3. Restart and check whether the battery is detected. This catches misconfigured power policies that can hide the battery.

### Fix 4: Check BIOS for the battery

This tells you whether Windows or the hardware is at fault.

1. Restart and enter BIOS setup (usually **F2**, **F10**, **Del**, or **Esc** during boot — varies by brand).
2. Look for a **Battery**, **Power**, or **System Information** tab.
3. If BIOS shows the battery (charge level, health), the hardware is fine — the problem is Windows-side, so repeat Fix 2 and consider a Windows update rollback.
4. If BIOS also shows no battery, the issue is hardware or firmware — continue to the next fixes. Similar no-detection cases after updates are covered in the [no battery detected after Windows update guide](/articles/how-to-fix-no-battery-detected-after-windows-update-on-windows-11/).

### Fix 5: Update the BIOS and chipset drivers

An outdated BIOS may not initialize the battery controller correctly on newer Windows builds.

1. Find your exact model on your manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)).
2. Download the latest **BIOS** and **chipset** drivers for your model.
3. Install the chipset driver first, then the BIOS update — with the charger plugged in and the laptop undisturbed.
4. After the BIOS update completes and the laptop restarts, check for the battery icon.

### Fix 6: Reseat the battery connector (internal batteries)

Only if you're comfortable opening the laptop — otherwise skip to Fix 7.

1. Power off, unplug, and remove the bottom panel screws (keep them organized).
2. Disconnect the battery's ribbon or plug connector from the motherboard, wait 30 seconds, and reconnect it firmly.
3. Reassemble and boot. A loose data connection is a surprisingly common cause on laptops that have been serviced or dropped.

### Fix 7: Test with a known-good battery or get service

1. If you have access to a compatible battery (same model), swap it in. If Windows detects the spare, your battery's controller board has failed.
2. Check for swelling — a puffed battery is a safety issue, not a software one. Stop using it and get it replaced.
3. If the laptop is under warranty, contact the manufacturer with your serial number; batteries are often covered for the first year. Microsoft documents hardware troubleshooting steps on the [Windows support site](https://support.microsoft.com/en-us/windows) as well.

### Fix 8: Load BIOS defaults to re-enable battery detection

A misconfigured BIOS setting can hide the battery from the entire system.

1. Enter BIOS setup (**F2**, **Del**, **F10**, or **Esc** during boot — varies by brand).
2. Find the **Load Optimized Defaults** or **Load Setup Defaults** option (usually on the **Exit** tab or via **F9**).
3. Apply it, then **Save and Exit**. The laptop will reboot with factory firmware settings.
4. Check Device Manager after boot — on some models, a disabled battery controller or power-management feature in BIOS is what made Windows report "no battery detected" all along.
5. If the battery appears now, re-enter BIOS and reconfigure only the settings you actually need (boot order, virtualization) rather than changing power options blindly.

## Closing

"No battery detected" is usually Windows losing the handshake, not a dead battery — a power reset and driver reinstall bring most of them back. If BIOS can't see the battery either, you've ruled out Windows and it's time to think hardware: reseat, swap, or service. Either way, the layered approach means you always know which half of the system to blame.
