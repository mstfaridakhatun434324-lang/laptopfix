---
title: "Synaptics Touchpad Not Working? Restore Your Laptop's Touchpad"
slug: what-to-do-if-synaptics-touchpad-not-working
date: 2026-10-08
categories: ["drivers"]
tags: ["synaptics touchpad", "touchpad not working", "precision touchpad", "windows 11", "mouse driver"]
description: "Synaptics touchpad not working on your laptop? Fix dead cursors, missing gestures, and driver conflicts with these step-by-step solutions."
thumbnail: "/images/thumbs/what-to-do-if-synaptics-touchpad-not-working.webp"
faqs:
  - q: "Why did my Synaptics touchpad suddenly stop working?"
    a: "The most common triggers are a Windows update replacing the Synaptics driver with a generic one, the touchpad being disabled via function key or settings, or the driver crashing. Less commonly, the ribbon cable connecting the touchpad works loose. Check the function-key toggle and Touchpad settings first — they resolve a surprising share of 'sudden' failures."
  - q: "How do I re-enable a disabled Synaptics touchpad?"
    a: "Open Settings → Bluetooth & devices → Touchpad and make sure the Touchpad toggle is on. Also try the keyboard toggle (usually Fn + F5/F7/F9, look for the touchpad icon). In Device Manager, check 'Mice and other pointing devices' or 'Human Interface Devices' for a disabled Synaptics entry and re-enable it. Some laptops also have a BIOS toggle for the internal pointing device."
  - q: "Should I use the Synaptics driver or Windows Precision drivers?"
    a: "If your laptop shipped with Synaptics drivers and its custom gestures, keep the manufacturer's Synaptics package for full feature support. If it shipped as a Precision touchpad (most modern laptops), Windows' built-in Precision drivers are better — smoother and more consistent. Problems arise when Windows Update cross-installs the wrong type; match what the laptop originally used."
  - q: "What if the touchpad works in BIOS but not in Windows?"
    a: "That cleanly isolates the problem to Windows software — the hardware and its connection are fine. The cause is almost always the driver: wrong driver type installed, corrupted installation, or a conflicting update. Boot into Safe Mode to confirm (touchpad usually works there with basic drivers), then clean-reinstall the correct touchpad driver from your laptop maker's site."
---

The cursor won't move. No scroll, no gestures, no clicks — your laptop's touchpad is a dead slab of glass. Before you resign yourself to a USB mouse forever, know that touchpad failures are overwhelmingly software: a disabled toggle, a driver Windows Update swapped, or a settings conflict. Hardware failure is actually the least likely cause.
Synaptics touchpads add one wrinkle: the eternal confusion between Synaptics' own drivers and Microsoft's Precision Touchpad drivers. Installing the wrong type (or letting Windows Update do it for you) breaks gestures and sometimes the whole pad. This guide sorts that out along with every other common cause. For the OS-level settings side, our [touchscreen troubleshooting](/articles/how-to-fix-touchscreen-not-working-on-laptop-in-windows-11-24h2/) covers related input-device diagnostics.
If your touchpad works but gestures specifically are broken, that's almost always a driver-type mismatch — jump to Fix 4. And if you use a Lenovo, Dell, or HP, grab the touchpad driver from your maker's site rather than Synaptics directly; the OEM packages include model-specific tuning. Our [Synaptics model-specific guide](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/) has more on that.

## Why this happens

- **Touchpad disabled by function key.** The Fn-key toggle is easy to hit accidentally and gives zero on-screen feedback on some models.
- **Touchpad toggle off in Settings.** Windows updates and some utilities flip the Settings toggle without asking.
- **Wrong driver type installed.** Synaptics driver on Precision hardware (or vice versa) breaks gestures or the entire pad.
- **Windows Update driver replacement.** Update swaps the working OEM touchpad driver for a generic or mismatched one.
- **Corrupted driver installation.** Partial updates leave the touchpad driver in a half-installed state.
- **BIOS toggle disabled.** Some laptops have an 'Internal Pointing Device' BIOS setting that updates can reset.
- **Palm-rejection / sensitivity misconfiguration.** Overaggressive palm detection makes the pad feel dead while it's technically working.
- **Loose ribbon cable.** The touchpad's ZIF ribbon connector can work loose after drops or servicing — hardware, but worth knowing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the function-key toggle and Settings

Two toggles, ten seconds each — and they account for a huge fraction of 'dead touchpad' reports.

1. Press the touchpad function key (look for the touchpad icon on F5, F7, or F9 — often combined with Fn) and test.
2. Open Settings → Bluetooth & devices → Touchpad → ensure the Touchpad toggle is ON.
3. Uncheck 'Leave touchpad on when a mouse is connected' temporarily if a USB mouse is plugged in — this setting disables the pad.
4. Increase the touchpad sensitivity to 'Most sensitive' as a test against overzealous palm rejection.
5. Check Cursor speed too — a speed set near zero can make the pad feel dead.

### Fix 2: Verify the touchpad in Device Manager

This reveals whether Windows sees the hardware and whether the driver is healthy, disabled, or missing.

1. Open Device Manager (Windows + X).
2. Expand 'Mice and other pointing devices' and 'Human Interface Devices' — look for Synaptics, ELAN, or Precision entries.
3. A down-arrow icon means disabled: right-click → Enable device.
4. A yellow warning icon means driver trouble: right-click → Properties and note the error code.
5. If the touchpad is absent entirely, click View → 'Show hidden devices'; a ghosted entry suggests hardware or BIOS-level disablement.

### Fix 3: Test in BIOS and Safe Mode to isolate hardware

This two-minute test definitively separates hardware failure from Windows software problems.

1. Restart into BIOS/UEFI setup — if the touchpad moves the cursor there, the hardware and cable are fine.
2. Boot into Safe Mode (Settings → Recovery → Advanced startup) and test the pad with basic drivers.
3. Works in BIOS/Safe Mode but not normal Windows = driver or software conflict. Proceed with driver fixes.
4. Dead everywhere including BIOS = hardware: ribbon cable or the pad itself — check warranty or a repair shop.
5. Note the result before continuing; it determines whether software fixes are even worth attempting.

### Fix 4: Install the correct touchpad driver type

The crux of Synaptics issues: match the driver to what the laptop shipped with, from the laptop maker's site.

1. Check your laptop maker's support page for your exact model — download their touchpad driver (Synaptics, ELAN, or Precision as specified).
2. In Device Manager, right-click the touchpad → Uninstall device, checking 'Attempt to remove the driver for this device.'
3. Restart, then install the downloaded OEM driver package.
4. If your laptop is a Precision-touchpad model, you can often just let Windows install its built-in Precision driver — verify in Settings → Touchpad that gesture options appear.
5. After installing, open the touchpad settings and re-enable your preferred gestures — driver swaps reset them. Lenovo owners can cross-check with our [Lenovo-specific Synaptics guide](/articles/how-to-fix-synaptics-touchpad-not-working-on-lenovo-laptop/).

### Fix 5: Fix gestures and scrolling specifically

When the cursor moves but two-finger scroll and gestures don't, the driver type or gesture config is wrong — not the hardware.

1. Confirm Settings → Bluetooth & devices → Touchpad shows the full gestures panel (scroll, three-finger, four-finger sections).
2. If only basic options appear, the wrong driver type is installed — return to Fix 4 and match the OEM driver.
3. Reset gestures: scroll to the bottom of Touchpad settings and click 'Reset' under 'Reset touchpad settings and gestures.'
4. Re-enable each gesture individually and test — sometimes one corrupt gesture profile poisons the set.
5. Check for conflicting mouse utilities (some gaming mouse software hijacks gesture handling) and disable them temporarily.

### Fix 6: Check BIOS settings and update chipset drivers

Firmware-level disables and stale chipset drivers can wedge the touchpad below the OS.

1. Enter BIOS/UEFI and look for 'Internal Pointing Device' or 'Touchpad' — ensure it's Enabled.
2. Install the latest chipset driver from your laptop maker's support site — the touchpad often connects via I2C/SMBus managed by the chipset.
3. Check for a BIOS update mentioning touchpad or input fixes.
4. After any BIOS change, boot to Windows and recheck Device Manager for the touchpad entry.
5. If a recent BIOS update caused the failure, the maker's support site may offer a rollback BIOS — use with care.

### Fix 7: Rule out interference and hardware failure

Last checks before concluding it's the ribbon cable or pad hardware.

1. Unplug all USB devices — a faulty USB device can flood the input subsystem on some models.
2. Boot with no external mouse connected to eliminate the 'disable touchpad when mouse present' logic entirely.
3. If comfortable opening the laptop, reseat the touchpad's ZIF ribbon cable (release the latch, reseat, relatch) — a common fix after drops.
4. Test with a Linux live USB: working there proves Windows software is at fault; dead there proves hardware.
5. If hardware is confirmed dead and warranty has expired, USB or Bluetooth mice are the pragmatic permanent workaround — check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for accessibility alternatives like Mouse Keys.

## Closing

Touchpad failures are rarely the pad itself — they're toggles, driver-type mismatches, or Windows Update surprises. Check the easy toggles, confirm hardware in BIOS, install the maker's exact driver, and your cursor will be gliding again.
