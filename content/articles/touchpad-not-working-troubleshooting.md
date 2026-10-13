---
title: "Touchpad Not Working? A Complete Troubleshooting Guide"
slug: touchpad-not-working-troubleshooting
date: 2026-09-15
categories: ["drivers"]
tags: ["touchpad", "not working", "troubleshooting", "laptop"]
description: "Touchpad completely dead on your laptop? Troubleshoot hardware toggles, BIOS, drivers, and settings in the right order with this guide."
thumbnail: "/images/thumbs/touchpad-not-working-troubleshooting.webp"
faqs:
  - q: "Why did my touchpad suddenly stop working?"
    a: "The most common sudden causes are an accidental Fn-key toggle press, a Windows update replacing the touchpad driver, or the touchpad toggle in Windows Settings getting flipped. All three are quick to check and fix. Actual hardware failure is much less common and usually follows a drop, spill, or repair — sudden death without any of those is almost always software."
  - q: "How can I tell if my touchpad problem is hardware or software?"
    a: "Check Device Manager and the BIOS. If the touchpad appears in Device Manager (even with an error), the hardware is communicating and the problem is software. If it is absent from both Device Manager and the BIOS, and the BIOS toggle is enabled, suspect the ribbon cable or the touchpad module itself. The Fn-key and Settings checks rule out the trivial causes first."
  - q: "Why does my touchpad work in BIOS but not in Windows?"
    a: "That is actually good news — it proves the hardware works and the problem is entirely within Windows: the driver, a disabled setting, or conflicting software. Focus on reinstalling the manufacturer's touchpad driver, checking the Windows touchpad toggle, and testing in Safe Mode to find conflicting programs."
  - q: "Should I just use an external mouse instead of fixing the touchpad?"
    a: "An external mouse is a fine temporary workaround, but a dead touchpad often signals a driver or system issue worth fixing properly — the same bad update that killed the touchpad may affect other devices. Work through the software fixes; they take about twenty minutes and permanently resolve most cases."
---

A dead touchpad makes a laptop feel broken in a way few other failures do. But before you panic or buy an external mouse, run the numbers: the overwhelming majority of touchpad failures are software — a toggled Fn key, a flipped Settings switch, or a driver replaced by Windows Update. Hardware failure is real but rare, and it almost always has a backstory (a drop, a spill, a recent disassembly).

The diagnostic approach here is elimination from the outside in: physical toggles first (fastest), then Windows settings, then drivers, then BIOS, then hardware. Each step takes a few minutes, and you stop the moment the cursor moves again. This guide is brand-agnostic and covers ELAN, Synaptics, and Microsoft Precision touchpads. For ELAN-specific issues, see our [ELAN touchpad fix guide](/articles/how-to-fix-elan-touchpad-not-working/), and for Synaptics hardware, the [Synaptics touchpad guide](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/).

## Why this happens

- **Fn-key toggle accidentally pressed.** The most common cause — a single keypress disables the pad at the hardware level.
- **Touchpad disabled in Windows Settings.** The Settings toggle can be flipped by updates, scripts, or accidental clicks.
- **Driver replaced by Windows Update.** Generic drivers lack touchpad functionality or break existing installs.
- **Touchpad disabled in BIOS.** Firmware settings can turn the pad off where Windows cannot override it.
- **"Disable when mouse plugged in" enabled.** A common setting that surprises users who dock and undock.
- **Conflicting third-party software.** Touchpad utilities and some security software intercept input.
- **Loose ribbon cable or failed module.** Hardware causes, usually with a physical backstory.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn-key toggle

The thirty-second check that fixes a huge share of cases.

1. Find the touchpad icon on your function keys — commonly **F5**, **F6**, **F7**, or **F9**, showing a touchpad with a line through it.
2. Press **Fn + that key**. On some laptops the toggle works without Fn — try both.
3. Test the touchpad after each press. If it springs to life, that was the entire problem.
4. If your laptop has a dedicated touchpad indicator light, watch it change as you toggle.

### Fix 2: Enable the touchpad in Windows Settings

The software switch that mirrors the hardware one.

1. Open **Settings > Bluetooth & devices > Touchpad** and make sure the **Touchpad** toggle is **On**.
2. If the Touchpad page is missing entirely, Windows has no touchpad driver loaded — skip ahead to Fix 4.
3. Set **Touchpad sensitivity** to **Medium** or higher while testing; minimum sensitivity can feel like a dead pad.
4. Expand **Taps** and **Scroll and zoom** to confirm gestures are enabled — a pad that moves but does not scroll or tap is a driver/gesture issue, not a dead pad.

### Fix 3: Check "disable when external mouse is connected"

A setting that bites laptop dockers.

1. In **Settings > Bluetooth & devices > Touchpad**, expand the touchpad section and look for **Leave touchpad on when a mouse is connected** — check it.
2. On older Windows 10 systems, check **Settings > Devices > Touchpad** for the same option, or **Control Panel > Mouse** for a manufacturer tab (ELAN/Synaptics) with a "disable internal pointing device when external USB pointing device is attached" checkbox.
3. Unplug any USB or Bluetooth mouse and retest — if the pad works with the mouse disconnected, this setting was the cause.

### Fix 4: Reinstall the touchpad driver

The core software fix.

1. Open Device Manager and expand **Mice and other pointing devices** and **Human Interface Devices**. Note exactly what is listed — **ELAN**, **Synaptics**, **I2C HID Device**, or generic **PS/2 Compatible Mouse**.
2. Right-click the touchpad-related entries and choose **Uninstall device**, checking **Attempt to remove the driver** where offered.
3. Restart the laptop. Windows will attempt to reinstall — then immediately install the touchpad driver from your laptop manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for your exact model.
4. Verify the proper device name (not generic PS/2) appears in Device Manager and the full Touchpad settings page returns.

### Fix 5: Verify the touchpad in BIOS

Rule out a firmware-level disable.

1. Restart and enter the BIOS (**F2**, **Delete**, **Esc** — varies by brand).
2. Find **Touchpad**, **Internal Pointing Device**, or **PS/2 Mouse** under Advanced or Devices and set it to **Enabled**.
3. Save and exit. If the BIOS has a touchpad test or diagnostics page, run it — a pass here proves the hardware.
4. If the BIOS shows it enabled and Windows still sees nothing, continue to Fix 6.

### Fix 6: Test in Safe Mode and clean boot

Isolate software interference.

1. Boot into **Safe Mode** (hold **Shift** while clicking Restart, then **Troubleshoot > Advanced options > Startup Settings**) and test the touchpad with the basic driver.
2. If it works in Safe Mode, return to normal mode and perform a **clean boot** (**msconfig**, hide Microsoft services, disable all) to find the conflicting program.
3. Pay special attention to third-party touchpad tools, remote desktop software, and accessibility utilities that remap input.
4. Re-enable services in halves to narrow down the culprit efficiently.

### Fix 7: Check the hardware

When software is fully exonerated.

1. If the touchpad is absent from Device Manager (including hidden devices) and the BIOS, and the BIOS toggle is enabled, the ribbon cable is the prime suspect.
2. Think about recent history: drops, spills, or a recent opening of the laptop for another repair all point at the cable or connector.
3. On out-of-warranty machines, reseating the touchpad ribbon cable is a documented repair for many models — look up your model's service manual first, as the connectors are delicate.
4. If you are not comfortable opening the laptop, a repair shop can diagnose this quickly — and in the meantime, a wireless mouse keeps the machine fully usable.

## Closing

Touchpad troubleshooting is a triumph of checking the obvious first: the Fn key and the Settings toggle resolve an almost embarrassing proportion of "dead touchpad" reports. Beyond that, the driver reinstall is the workhorse fix, especially after Windows updates. The BIOS and Safe Mode steps exist to give you certainty — certainty that it is software (fixable in minutes) or hardware (a cable or module, fixable with parts). Either way, you stop guessing and start knowing, which is the entire point.
