---
title: "Touchpad Not Working on Windows 11? Fix It Step by Step"
slug: how-to-fix-touchpad-not-working-on-windows-11
date: 2026-09-18
categories: ["drivers"]
tags: ["touchpad", "windows 11", "cursor", "precision touchpad"]
description: "Touchpad dead on Windows 11? Step-by-step fixes in the order that works — from Settings toggles to clean driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-touchpad-not-working-on-windows-11.webp"
faqs:
  - q: "Why did my touchpad stop working after upgrading to Windows 11?"
    a: "The upgrade frequently carries over a Windows 10-era touchpad driver that misbehaves on 11, or Windows Update promptly replaces the manufacturer's driver with a generic one. The Settings layout also moved — the touchpad toggle now lives under Bluetooth & devices. Reinstalling the manufacturer's Windows 11 touchpad driver and verifying the new Settings paths fixes the large majority of cases."
  - q: "Where is the touchpad setting in Windows 11?"
    a: "Settings > Bluetooth & devices > Touchpad. The master toggle is at the top, with cursor speed, sensitivity, taps, scroll, and gestures below. If the entire Touchpad page is missing, Windows isn't detecting a compatible touchpad — that's a driver problem, not a settings problem, and the driver fixes below apply."
  - q: "My touchpad works but gestures don't on Windows 11. Why?"
    a: "The basic cursor driver loaded but the precision gesture stack didn't — almost always because a generic driver replaced the manufacturer's full package. Installing the OEM touchpad driver restores multi-finger gestures. Also verify gestures are enabled under the Touchpad settings page, since upgrades sometimes reset them to off."
  - q: "Can Windows 11's touchscreen settings interfere with the touchpad?"
    a: "Not directly — they're separate input stacks. But if both the touchscreen and touchpad failed simultaneously, suspect the shared Intel Serial IO / I2C bus driver rather than either device's driver. Our touchscreen fix guide covers that shared-bus angle for the combined failure case."
---

Windows 11 moved things around just enough to confuse everyone: the touchpad settings relocated to **Bluetooth & devices**, the driver model tightened, and Windows Update got more aggressive about swapping manufacturer touchpad drivers for its own generic builds. The result is the familiar dead cursor on a brand-new-feeling OS — and a Settings page that sometimes vanishes entirely.

The sequence below is ordered by success rate on Windows 11 specifically. It opens with the relocated settings and the new toggle behaviors (which account for a surprising share of "dead" touchpads), moves into the driver-stack repair that fixes update damage, and closes with the bus-level and hardware checks. Windows 10 users should follow our [Windows 10 touchpad guide](/articles/how-to-fix-touchpad-not-working-on-windows-10/) — the paths differ enough to matter.

## Why this happens

- **Windows Update replaced the manufacturer's driver.** Windows 11 is more aggressive about driver updates than 10 — the generic swap that kills cursors and gestures happens more often.
- **The touchpad toggle moved and got flipped.** The setting's new home under Bluetooth & devices means people don't find it; upgrades and updates can also flip it off silently.
- **Precision vs. manufacturer stack mismatch.** Windows 11 pushes the precision touchpad model hard; on laptops that shipped with a vendor stack (Synaptics/ELAN), the forced mismatch kills the pad.
- **The driver carried over badly from Windows 10.** In-place upgrades keep the old driver, which may enumerate but not function correctly on 11's input stack.
- **Power management on the I2C/SMBus.** The touchpad's bus gets suspended aggressively, producing the "dead after sleep" pattern.
- **The "leave touchpad on" logic with connected mice.** A forgotten wireless receiver disables the pad exactly as designed — and the design is easy to forget.
- **BIOS disabled the internal pointing device.** Firmware updates during the Windows 11 era can flip the toggle, hiding the device from the OS entirely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Windows 11 touchpad settings

The relocated toggles — two minutes, high hit rate.

1. Go to **Settings > Bluetooth & devices > Touchpad** and confirm the **Touchpad** toggle is **On**.
2. If the entire **Touchpad** page is missing from Bluetooth & devices, Windows sees no compatible touchpad — skip to Fix 3 (driver stack); no setting will help.
3. Set **Touchpad sensitivity** to *Medium* or higher, and check **Leave touchpad on when a mouse is connected** while troubleshooting.
4. Expand the **Taps**, **Scroll and zoom**, and **Three-finger/four-finger gestures** sections — re-enable anything an upgrade turned off, and test two-finger scroll specifically.

### Fix 2: Try the function-key toggle

The hardware-level switch that the Settings page can't override.

1. Press your laptop's touchpad toggle — usually **Fn + F5/F7/F9** with the touchpad icon. Wait several seconds and test.
2. If nothing happens, the OEM hotkey software may be missing — check **Settings > Apps** for the manufacturer's hotkey utility and reinstall it from their support site if absent.
3. Some Windows 11 laptops moved the toggle to a dedicated key without Fn — try the key alone too.
4. After toggling, recheck the Settings > Bluetooth & devices > Touchpad page — the software toggle should reflect the hardware state.

### Fix 3: Reinstall the manufacturer's Windows 11 touchpad driver

The anchor fix — and it must be the Windows 11 package, not the Windows 10 one.

1. In **Device Manager**, note the touchpad's current entry under **Human Interface Devices** or **Mice and other pointing devices**.
2. Download the **touchpad driver** for your exact model from the laptop maker's site, explicitly selecting **Windows 11** as the OS — the Windows 10 package is a common source of carried-over breakage.
3. Right-click the touchpad > **Uninstall device**, checking *Attempt to remove the driver for this device* to clear the wrong stack.
4. Install the Windows 11 package as administrator, reboot, and verify the full Touchpad settings page returns with gesture options. The [Synaptics-specific walkthrough](/articles/synaptics-touchpad-not-working-troubleshooting/) covers the dual-stack trap in depth if your laptop uses Synaptics.

### Fix 4: Block Windows from swapping the driver again

Windows 11's driver enthusiasm is the relapse mechanism — address it.

1. After the working manufacturer driver is installed, note its version (**Device Manager > Properties > Driver**) as your known-good baseline.
2. Follow our [driver update control guide](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) to stop Windows Update from replacing manufacturer drivers — the Group Policy method on Pro, the registry method on Home.
3. Use the manufacturer's update utility (Lenovo Vantage, Dell Update, HP Support Assistant, MyASUS) as your driver source going forward.
4. If Windows has already re-broken it once, you'll recognize the pattern instantly next time: cursor dead + gestures gone + wrong driver date = repeat Fix 3.

### Fix 5: Repair the I2C/SMBus foundation

The touchpad's bus driver can fail while the touchpad driver looks fine.

1. In **Device Manager**, expand **System devices** and inspect **Intel Serial IO** I2C/GPIO controllers and SMBus entries for warning icons.
2. Download the **chipset / Serial IO driver** for your model from the manufacturer and install it — this re-enumerates the bus the touchpad lives on.
3. In the touchpad device's **Properties > Power Management** (if the tab exists), uncheck *Allow the computer to turn off this device to save power*.
4. Do a **full shutdown** (Shift + Shut down) to clear Fast Startup's preserved bus state, then cold boot and test.

### Fix 6: Rule out conflicts in a clean boot

Something else may be intercepting input.

1. Run **msconfig**, choose **Selective startup**, disable all non-Microsoft services, and reboot — if the touchpad works, a third-party service is the culprit.
2. Re-enable services in halves to isolate the offender — common ones include old mouse utilities, remote-desktop tools, and "touchpad enhancer" apps.
3. Check **Device Manager > View > Show hidden devices** for ghost pointing devices from previously installed software and uninstall them.
4. Microsoft's [Windows input support pages](https://support.microsoft.com/en-us/windows) document the official troubleshooting sequence as a cross-check.

### Fix 7: Confirm hardware with an outside-OS test

The final verdict.

1. Boot a **Linux live USB** — working touchpad there proves the hardware and convicts Windows software completely. Revisit Fix 3 with a driver-store cleanup (Driver Store Explorer) for a truly clean slate.
2. Dead in Linux and absent from BIOS-level tests = hardware: ribbon cable or touchpad module. Suspect this after drops or palm-rest service.
3. Check whether the failure affects the **touchscreen** too — both dead together implicates the shared bus or a motherboard issue rather than the pad itself.
4. Interim: **Mouse Keys** (**Settings > Accessibility > Mouse**) drives the cursor from the keyboard; a USB mouse restores full usability while you arrange repair.

## Closing

Windows 11 touchpad failures follow the same script as always — the toggle, the swapped driver, the wrong stack — just with new Settings addresses and a more aggressive Windows Update. Find the relocated toggles, install the manufacturer's Windows 11 driver package, and keep the updater from swapping it back. The cursor comes home.
