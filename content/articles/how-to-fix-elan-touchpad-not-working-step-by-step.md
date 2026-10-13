---
title: "ELAN Touchpad Not Working? Fix It Step by Step"
slug: how-to-fix-elan-touchpad-not-working-step-by-step
date: 2026-09-15
categories: ["drivers"]
tags: ["elan touchpad", "touchpad not working", "elan driver", "precision touchpad", "laptop touchpad"]
description: "ELAN touchpad dead on your laptop? Fix it step by step with function-key checks, ELAN driver reinstalls, and BIOS touchpad settings."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-step-by-step.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows Update often replaces the ELAN driver with a generic Microsoft precision driver — or vice versa — breaking the specific integration your laptop needs. Reinstalling the ELAN driver from your laptop maker's support site restores the correct pairing of driver and hardware."
  - q: "What is the difference between ELAN and precision touchpads?"
    a: "ELAN is the hardware/driver vendor; 'precision touchpad' is Microsoft's standardized driver interface. Some ELAN touchpads run on ELAN's own driver, others on Microsoft's precision driver. Installing the wrong type for your model breaks gestures or kills the pad entirely — use whatever your maker ships."
  - q: "Can I use my laptop without the touchpad while fixing it?"
    a: "Yes. Any USB mouse works immediately with no drivers needed. You can also enable Mouse Keys (Settings, Accessibility, Mouse) to control the cursor from the keyboard numpad in a pinch while you work through the driver fixes. A cheap wired mouse is the most reliable emergency pointer."
  - q: "Why does the touchpad work in BIOS but not Windows?"
    a: "That proves the hardware is fine — the problem is purely the Windows driver stack. Boot into Safe Mode and reinstall the ELAN driver from your maker's support site. If it works in Safe Mode but not normal mode, a startup program is interfering."
---

The cursor will not move. Taps do nothing, two-finger scroll is a memory, and the touchpad might as well be a decorative panel. ELAN touchpads — found across ASUS, Lenovo, Acer, MSI, and many other laptops — have a particular failure pattern tied to their driver model, and generic touchpad advice often misses it.

ELAN touchpads live an interesting double life: some run on ELAN's proprietary driver with its control panel, others on Microsoft's precision touchpad driver. Windows Update loves to swap one for the other, and the wrong driver for your specific model means a dead pad, dead gestures, or a pad that works until the next reboot.

This step-by-step guide covers the ELAN-specific sequence: the Fn-key toggle everyone forgets, the driver-type question, clean ELAN driver installation, and the BIOS and settings checks. Work through these in order — diagnose first, then act.

## Why this happens


- **Touchpad disabled by Fn key:** Most laptops have an Fn-key touchpad toggle; one accidental press kills the pad with no on-screen warning.
- **Wrong driver type installed:** ELAN-proprietary vs. Microsoft precision mismatch after a Windows Update swap.
- **Corrupt ELAN driver:** Update failures corrupt the driver, leaving the pad detected but unresponsive.
- **Touchpad disabled in Settings:** Windows' touchpad toggle can flip off after updates, especially on shared or managed machines.
- **BIOS touchpad mode changed:** Firmware updates can switch the touchpad between Advanced and Basic modes, breaking the Windows driver.
- **External mouse auto-disable:** 'Leave touchpad on when mouse is connected' unchecked means a forgotten USB receiver disables the pad.
- **Palm rejection set too aggressive:** Overzealous palm detection can suppress legitimate touches, feeling like a dead pad.
- **Hardware ribbon cable failure:** The touchpad's internal cable can work loose — usually after drops or battery swelling.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn toggle and Windows touchpad setting


Two toggles, thirty seconds, and they account for a huge share of 'dead touchpad' reports. Always check these before touching drivers.

1. Press the touchpad Fn key (often Fn + F9, or a key with a touchpad icon) and test.
2. Open Settings, Bluetooth & devices, Touchpad — confirm the Touchpad toggle is On.
3. If a USB mouse or wireless receiver is plugged in, unplug it and check 'Leave touchpad on when a mouse is connected.'
4. Test taps, movement, and two-finger scroll separately — partial function narrows the cause. Microsoft documents the full touchpad settings panel on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

### Fix 2: Identify your touchpad in Device Manager


You need to know what Windows thinks your touchpad is before fixing it. The device name reveals whether you are on ELAN's driver or Microsoft's — and whether the device is present at all.

1. Press Windows + X and open Device Manager.
2. Expand Human Interface Devices and Mice and other pointing devices.
3. Look for ELAN Input Device, ELAN touchpad, or I2C HID Device entries.
4. A warning icon means driver trouble; a missing entry (check View, Show hidden devices) suggests BIOS or hardware issues.
5. Note the exact device name — you will match it to the driver download later.

### Fix 3: Reinstall the correct ELAN driver


The core fix: remove the wrong or corrupt driver completely, then install the exact ELAN package your laptop maker ships for your model. Matching the maker's package — not a generic ELAN download — is what makes gestures and palm rejection work properly.

1. Download the touchpad/ELAN driver for your exact model from your maker's support site.
2. In Device Manager, right-click the ELAN/touchpad device and choose Uninstall device with driver removal checked.
3. Restart the laptop.
4. Install the downloaded ELAN driver package and restart again.
5. Open Settings, Touchpad and verify gestures are configurable — that confirms the right driver type.
6. For the Lenovo-specific variant, see our [ELAN touchpad fix for Lenovo](/articles/how-to-fix-elan-touchpad-not-working-on-lenovo-laptop/).

### Fix 4: Roll back a bad driver update


If the touchpad died immediately after an update, the previous driver was working. Rolling back is instant and often permanent — if you then block the bad update.

1. In Device Manager, right-click the touchpad device, Properties, Driver tab.
2. Click Roll Back Driver if available, choose a reason, and restart.
3. If rollback is greyed out, manually install the older ELAN version from your maker's support archive.
4. Use the wushowhide troubleshooter to hide the problematic driver update.
5. Consider disabling automatic driver updates to prevent a repeat.

### Fix 5: Check BIOS touchpad mode


Some laptops expose the touchpad mode in firmware — Advanced (I2C, needs the full driver) versus Basic (PS/2 fallback). A BIOS update can flip this and orphan your Windows driver.

1. Restart and enter BIOS/UEFI (F2, Del, or your maker's key).
2. Look under Advanced or Config for Touchpad, Internal Pointing Device, or similar.
3. Ensure it is Enabled (not Disabled).
4. If a mode option exists (Advanced/Basic), try Advanced first; if the Windows driver fails there, Basic is a functional fallback.
5. Save, exit, and test in Windows.

### Fix 6: Test hardware and adjust sensitivity


The final checks: rule out physical failure and tune the settings that mimic a dead pad. Aggressive palm rejection and tiny dead zones fool a lot of people.

1. In Touchpad settings, set Touchpad sensitivity to Most sensitive and test.
2. Disable any 'disable touchpad when mouse connected' options entirely.
3. Boot a Linux live USB — a working pad there proves Windows/driver fault; a dead pad there suggests hardware.
4. Check for battery swelling under the touchpad area (a spongy or lifted pad) — swelling batteries press on the touchpad from below and this needs immediate service.
5. If hardware is suspected, our [Synaptics touchpad guide](/articles/how-to-fix-synaptics-touchpad-not-working-on-lenovo-laptop/) covers similar diagnostics for the other major touchpad vendor.

## Closing


ELAN touchpad failures are driver-identity problems more than hardware problems: the Fn toggle, the ELAN-vs-precision driver question, and the BIOS mode cover nearly every case. Get the maker's exact ELAN package installed, keep Windows Update from swapping it, and the pad stays responsive. Only a pad dead in Linux too earns a trip to the repair shop.
