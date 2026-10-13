---
title: "Fix a Laptop Keyboard That Stopped Working in Windows 11 24H2"
slug: how-to-fix-keyboard-not-working-on-laptop-in-windows-11-24h2
date: 2026-10-03
categories: ["drivers"]
tags: ["keyboard not working", "windows 11 24h2", "laptop keyboard", "hid keyboard", "driver fix"]
description: "Fix a laptop keyboard that died after Windows 11 24H2: filter key traps, HID driver repair, BIOS checks, and hardware isolation tests."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my laptop keyboard not working after the 24H2 update?"
    a: "The update can corrupt the HID keyboard driver stack, enable Filter Keys during migration so keystrokes get swallowed, or replace the embedded controller interface driver with an incompatible version. The quick proof is the BIOS typing test: if keys work in BIOS, the hardware is healthy and the failure is entirely in Windows software."
  - q: "How do I type if my laptop keyboard is completely dead?"
    a: "Press Win plus Ctrl plus O to open the on-screen keyboard, which gives you full typing capability with the mouse or touchscreen. A USB keyboard also works instantly when plugged in. Either option lets you open Device Manager, edit settings, and run every driver fix in this guide without the built-in keyboard."
  - q: "What does reinstalling the HID keyboard driver do?"
    a: "Uninstalling the Standard PS/2 Keyboard device forces Windows to discard the broken device node and build a fresh one with a clean driver on reboot. It clears corrupted state, bad filter bindings, and failed migration flags in one move, which is why it resolves more post-update keyboard deaths than any settings tweak."
  - q: "Could a Windows update really break a keyboard permanently?"
    a: "No. Windows updates cannot physically damage keyboard hardware — they only change drivers and settings. If the keyboard types in BIOS or from a Linux live USB, the failure is software and fully reversible. Only a keyboard that is dead in BIOS, in Linux, and after a ribbon reseat points to genuine hardware failure."
---

A laptop keyboard that goes dead after the Windows 11 24H2 update is alarming because it removes your primary input — but the single most important diagnostic takes thirty seconds: reboot into BIOS and try typing there. If keys register in BIOS, your keyboard hardware is healthy and Windows 24H2 broke the software path. That is the case the vast majority of the time, and it is completely fixable.

The keyboard talks to Windows through the HID stack and the embedded controller, and 24H2's driver migration touches both. The sequence below starts with the traps that cost nothing to check — Filter Keys, the function-lock state — and escalates through driver repair to the hardware-isolation tests that tell you whether a repair shop is actually needed.

## Why this happens

- **HID keyboard driver corruption:** The 24H2 migration can leave the Standard PS/2 Keyboard device node in a failed state with a yellow warning or error code.
- **Filter Keys got enabled:** Accessibility settings sometimes flip on during the update, making the keyboard appear dead because keystrokes are being filtered out.
- **Embedded controller driver mismatch:** The EC firmware interface driver that relays keystrokes can be replaced with an incompatible version during the update.
- **Fast Startup holds a broken state:** Hybrid shutdown preserves the failed keyboard device state across reboots, so normal restarts never clear it.
- **UpperFilters/LowerFilters registry corruption:** Third-party software (macro tools, keyboard utilities) leaves filter drivers that break under the new OS build.
- **BIOS keyboard setting reset:** Some 24H2-coupled firmware updates reset internal keyboard or legacy USB settings.
- **Power management disabling the device:** Windows may allow the system to power off the keyboard device to save power, and it fails to wake.
- **Actual hardware failure:** Liquid damage, ribbon cable faults, or controller failure — ruled in only after the software steps fail and BIOS typing fails too.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open the on-screen keyboard and check Filter Keys

1. Press **Win + Ctrl + O** to open the on-screen keyboard — your temporary input.
2. Go to **Settings → Accessibility → Keyboard** and turn **off** Filter Keys, Sticky Keys, and Toggle Keys.
3. In the same page, turn off **Underline access key shortcuts** if on — irrelevant, but confirms you are in the right place.
4. Test typing. Filter Keys with a long "ignore brief keystrokes" delay is the classic "keyboard suddenly dead after update" impostor.

### Fix 2: Do the BIOS typing test

1. Reboot and enter BIOS (F2, Del, or F10 — varies by brand).
2. Try typing in any BIOS text field, or navigate menus with arrow keys.
3. If typing works in BIOS, the hardware is fine — commit to the software fixes below with confidence.
4. If typing fails in BIOS too, skip to Fix 7 — you are looking at a hardware problem and no Windows driver will fix it.

### Fix 3: Reinstall the HID keyboard driver

1. Open **Device Manager** and expand **Keyboards**.
2. Right-click **Standard PS/2 Keyboard** → **Uninstall device**. (Do not check driver deletion on the first pass.)
3. Reboot. Windows redetects the keyboard and installs a clean driver instance.
4. If it still fails, repeat but this time check **Attempt to remove the driver for this device**, then reboot and let Windows fetch a fresh copy. If the keyboard entry appears as an unknown device rather than a keyboard, follow the [unknown-device diagnosis](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) before reinstalling. This mirrors the [ghost-device cleanup technique](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) used for other stuck devices.

### Fix 4: Force a true shutdown and disable Fast Startup

1. Hold **Shift** while clicking **Shut down** for a full power-off.
2. Power on and test. The EC re-initializes from cold, clearing stuck controller states.
3. For a permanent fix, disable Fast Startup: **Control Panel → Power Options → Choose what the power buttons do → Change settings currently unavailable** → uncheck **Turn on fast startup**.

### Fix 5: Clean up keyboard filter drivers in the registry

1. Open **regedit** and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e96b-e325-11ce-bfc1-08002be10318}` (the keyboard class key).
2. Look at **UpperFilters** — it should contain only `kbdclass`. If third-party entries (macro software, keyboard utilities) are present, note them, then delete the extra values.
3. Do the same check for suspicious entries under the mouse class key if you use keyboard-mouse combo software.
4. Reboot. Corrupted filter drivers are a notorious cause of "keyboard dead after feature update."

### Fix 6: Run the keyboard troubleshooter and check power management

1. Go to **Settings → System → Troubleshoot → Other troubleshooters → Keyboard → Run**.
2. In Device Manager, right-click the keyboard → **Properties → Power Management** and uncheck **Allow the computer to turn off this device to save power** if the tab exists.
3. Also check **Human Interface Devices** for any HID keyboard entries with warning icons and reinstall those too.
4. Microsoft documents the troubleshooter flow in [Windows support](https://support.microsoft.com/en-us/windows) if the built-in tool reports an error you do not recognize.

### Fix 7: Isolate hardware failure definitively

1. Boot from a Linux live USB — if the keyboard works there, Windows is the problem, period.
2. Test an external USB keyboard. If USB works but internal does not (and BIOS typing failed), the internal keyboard or its ribbon cable is faulty.
3. On some models, reseating the keyboard ribbon cable (remove bottom panel, disconnect and reconnect the ZIF cable) fixes it — only attempt if you are comfortable opening the chassis.
4. Otherwise, it is a keyboard replacement or service-center job. Internal laptop keyboards are usually inexpensive parts; labor is the main cost.

## Closing

Work the isolation logic and the problem classifies itself: typing works in BIOS means Windows broke it, and Windows can unbreak it — usually by reinstalling the HID driver, clearing Filter Keys, or removing a bad filter driver. Only when the keyboard is dead in BIOS, in a live USB environment, and after a ribbon reseat do you spend money on hardware. Most 24H2 keyboard deaths never get that far.
