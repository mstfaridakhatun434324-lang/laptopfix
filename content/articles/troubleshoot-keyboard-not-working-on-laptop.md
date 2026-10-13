---
title: "Laptop Keyboard Not Working? Full Troubleshooting Walkthrough"
slug: "troubleshoot-keyboard-not-working-on-laptop"
date: "2026-09-16"
categories: ["drivers"]
tags: ["keyboard not working", "laptop keyboard", "keyboard driver", "windows 11"]
description: "Some or all laptop keys dead? This walkthrough isolates hardware vs. software causes and fixes keyboard failures step by step, from filter keys to ribbon cables."
thumbnail: "/images/thumbs/troubleshoot-keyboard-not-working-on-laptop.webp"
faqs:
  - q: "Why did my laptop keyboard suddenly stop working?"
    a: "The most common sudden causes are accidentally enabled Filter Keys, a corrupted keyboard driver after a Windows update, or a firmware glitch in the embedded controller. Check accessibility settings first, then reinstall the keyboard driver in Device Manager — these two steps resolve most sudden failures."
  - q: "Can a Windows update break my laptop keyboard?"
    a: "Yes. Updates can replace the keyboard filter driver with an incompatible version or leave driver state corrupted. Uninstalling the keyboard devices in Device Manager and restarting — which forces a fresh driver install — is the standard fix for update-related keyboard failures."
  - q: "Why do only some keys on my laptop not work?"
    a: "Partial failure usually means debris under the keys, liquid damage, or a failing keyboard matrix (dead rows or columns of the circuit grid). Try compressed air under the affected keys first. If keys fail in geometric patterns like a full row, the keyboard hardware needs replacement."
  - q: "Should I replace the keyboard or the ribbon cable first?"
    a: "Always reseat the ribbon cable first — it is free and fixes looseness from drops or heat cycling. Only order a replacement keyboard after reseating fails and software causes are ruled out. Make sure to buy the exact part number for your model, as layouts and connectors vary."
---

A dead laptop keyboard is uniquely disruptive — you cannot even type your password comfortably. The first thing to establish is scope: are all keys dead, is it a cluster of keys, or is it specific keys like the function row? Total failure points at drivers, BIOS settings, or the ribbon cable; partial failure points at debris, damage, or a failing keyboard matrix.

The second diagnostic is the external keyboard test. Plug in any USB keyboard: if it works perfectly, Windows itself is fine and the problem is isolated to the laptop's internal keyboard hardware or its driver. If the USB keyboard also misbehaves, you are looking at a Windows-level input problem affecting all keyboards.

Work through these fixes in order. Most keyboard failures are software — filter keys, stale drivers, or a BIOS glitch — and resolve without opening the laptop. If only your function keys are affected, our [function key fix guide](/articles/how-to-fix-function-keys-not-working-reddit/) addresses that case.

## Why this happens

- ****Filter Keys or Sticky Keys enabled**:** Windows accessibility features can make the keyboard appear dead. Filter Keys ignores brief keystrokes; Sticky Keys changes modifier behavior. Both are easy to enable accidentally.
- ****Corrupted keyboard driver**:** The keyboard filter driver can corrupt after updates, leaving the internal keyboard unresponsive while USB keyboards work fine.
- ****BIOS glitch or disabled internal keyboard**:** Some BIOS setups can disable the internal keyboard, and firmware glitches can leave the keyboard controller in a bad state until power is fully drained.
- ****Fast Startup stale driver state**:** Fast Startup hibernates kernel and driver state. A wedged keyboard driver can persist across dozens of normal restarts.
- ****Debris or liquid under the keys**:** Crumbs, dust, and especially liquid spills break the electrical contacts under individual keys or whole rows.
- ****Loose keyboard ribbon cable**:** The internal keyboard connects via a flat ribbon cable that can loosen after drops, heat cycling, or a previous repair.
- ****Failing keyboard matrix**:** The keyboard's circuit matrix can develop dead traces with age. Characteristically, this kills keys in geometric patterns — a row, a column, or a diagonal.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn Off Accessibility Key Filters

Open Settings, Accessibility, Keyboard, and turn off Sticky Keys, Filter Keys, and Toggle Keys. Filter Keys is the classic culprit: with it on, quick taps do not register, which feels exactly like a dead keyboard. This gets enabled accidentally more often than anyone admits — usually by holding Shift too long and accepting the prompt.

Test typing immediately after disabling. If the keyboard springs to life, you are done — no drivers, no disassembly needed.

1. 1. Open Settings, Accessibility, Keyboard.
2. 2. Turn off Sticky Keys, Filter Keys, and Toggle Keys.
3. 3. Open Notepad and test every key.
4. 4. If keys work now, the case is closed.
5. 5. If not, continue to the driver fixes.

### Fix 2: Test With an External Keyboard

Plug in a USB keyboard (or connect a Bluetooth one) and test thoroughly. If the external keyboard works normally, Windows input handling is healthy and the fault is specific to the internal keyboard — its driver, cable, or hardware. If the external keyboard also fails, skip ahead to the Windows-level fixes and the system file check.

This single test saves enormous time by telling you whether to focus on the internal keyboard's driver and cable or on Windows itself.

1. 1. Connect a USB or Bluetooth keyboard.
2. 2. Test typing, modifiers, and special keys.
3. 3. External works but internal does not: focus on internal keyboard driver and cable.
4. 4. Both fail: focus on Windows input stack and system files.
5. 5. Disconnect the external keyboard before continuing driver work.

### Fix 3: Reinstall the Keyboard Driver

In Device Manager, expand Keyboards, right-click every entry (HID Keyboard Device and any vendor entries), and choose Uninstall device. Restart the laptop — Windows reinstalls fresh keyboard drivers during boot. This clears corrupted filter-driver state, the most common software cause of total internal-keyboard failure.

After rebooting, check Device Manager for warning icons. A persistent yellow triangle with a specific error code points at deeper trouble — note the code. You can compare driver versions using our guide on [checking driver versions in Device Manager](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).

1. 1. In Device Manager, expand the Keyboards section.
2. 2. Uninstall every keyboard device listed.
3. 3. Restart the laptop.
4. 4. Verify the keyboard works and check for warning icons.
5. 5. Note any error codes for further diagnosis.

### Fix 4: Drain Residual Power

Shut the laptop down completely, unplug the charger, and if the battery is removable, take it out. Hold the power button down for 30 seconds to drain residual charge from the capacitors, then reconnect power and boot. This hard-resets the embedded controller that manages the keyboard.

For sealed-battery laptops, the button-hold with everything unplugged still works — the goal is a complete power drain, not battery removal per se. This fixes keyboards wedged by firmware glitches that survive normal restarts.

1. 1. Shut down completely and unplug the charger.
2. 2. Remove the battery if it is removable.
3. 3. Hold the power button for 30 seconds.
4. 4. Reconnect power and boot normally.
5. 5. Test the keyboard immediately.

### Fix 5: Disable Fast Startup and Do a Full Shutdown

Open Control Panel, Power Options, 'Choose what the power buttons do,' click 'Change settings that are currently unavailable,' and uncheck 'Turn on fast startup.' Then hold Shift while clicking Shut down for a true cold boot. Fast Startup's hibernated kernel state can preserve a wedged keyboard driver indefinitely.

If the keyboard works after a cold boot but dies after sleep or regular restarts, Fast Startup or a sleep-state driver bug is confirmed — leave Fast Startup off permanently.

1. 1. Open Power Options, 'Choose what the power buttons do.'
2. 2. Uncheck 'Turn on fast startup' and save.
3. 3. Hold Shift while clicking Shut down.
4. 4. Power on and test the keyboard.
5. 5. Leave Fast Startup off if this resolves it.

### Fix 6: Run System File Checker

Open Command Prompt as administrator and run sfc /scannow. Corrupted Windows system files can break the input stack for all keyboards. The scan takes 10-20 minutes; let it finish, then restart. If SFC reports unfixable corruption, follow with DISM /Online /Cleanup-Image /RestoreHealth and run SFC again.

This fix matters most when both internal and external keyboards misbehave, which points above the driver level at Windows itself. Microsoft documents these repair commands in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. Open Command Prompt as administrator.
2. 2. Run sfc /scannow and wait for completion.
3. 3. Restart the laptop.
4. 4. If corruption remains, run DISM /Online /Cleanup-Image /RestoreHealth.
5. 5. Run SFC once more, then restart and test.

### Fix 7: Reseat the Keyboard Ribbon Cable

If software fixes all fail and the external keyboard works, the internal keyboard's ribbon cable is the prime suspect. Power off completely, remove the bottom panel, and locate the wide flat cable running from the keyboard to the motherboard — it is secured by a flip-lock or slide-lock connector. Open the lock, reseat the ribbon fully and squarely, and close the lock.

If reseating does not help, the keyboard unit itself has likely failed. Replacement keyboards are model-specific but usually inexpensive; on many laptops the keyboard is a separate replaceable module, while on some ultrabooks it is riveted to the palm rest and the whole top cover must be replaced.

1. 1. Power off completely and unplug everything.
2. 2. Remove the bottom panel per your service manual.
3. 3. Locate the keyboard ribbon cable and its locking connector.
4. 4. Open the lock, reseat the ribbon squarely, and close the lock.
5. 5. Reassemble, boot, and test. Replace the keyboard if still dead.

## Closing

Keyboard failures follow a clean diagnostic ladder: accessibility settings, external keyboard test, driver reinstall, power drain, system files, and finally the ribbon cable. Most cases resolve in the first three steps — the cable reseat at the end is for the stubborn remainder, and it is a straightforward repair once you have ruled out software.
