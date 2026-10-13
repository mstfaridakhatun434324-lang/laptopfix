---
title: "How Do I Fix My Synaptics Touchpad? A Practical Step-by-Step"
slug: how-do-i-fix-synaptics-touchpad-not-working
date: 2026-09-06
categories: ["drivers"]
tags: ["synaptics touchpad", "touchpad fix", "cursor not moving", "gestures", "laptop mouse"]
description: "Synaptics touchpad not responding? Answer the diagnostic questions in order and apply the matching fix — from toggles to driver surgery."
thumbnail: "/images/thumbs/how-do-i-fix-synaptics-touchpad-not-working.webp"
faqs:
  - q: "How do I turn my Synaptics touchpad back on?"
    a: "First try the keyboard toggle — usually Fn plus F5, F7, or F9 (look for the touchpad icon). Then check Settings → Bluetooth & devices → Touchpad and make sure the toggle is on. If both are on and it's still dead, open Device Manager → 'Mice and other pointing devices' and re-enable the Synaptics entry if it shows a down arrow. These three toggles cover the vast majority of 'suddenly off' cases."
  - q: "Why does my touchpad work but gestures don't?"
    a: "Gestures need the correct driver type for your hardware. If Windows Update installed a generic PS/2 mouse driver over your Synaptics or Precision driver, the cursor moves but two-finger scroll and multi-finger gestures vanish. Reinstall the touchpad driver from your laptop maker's support site for your exact model, then verify the full gesture options appear in Touchpad settings."
  - q: "How do I know if my touchpad problem is hardware or software?"
    a: "Restart into your BIOS/UEFI setup screen: if the touchpad moves the cursor there, the hardware is fine and Windows software is at fault. If it's dead in BIOS too, it's hardware — usually the ribbon cable or the pad itself. This single test saves enormous time by telling you whether software fixes are even worth attempting."
  - q: "Can I use my laptop without the touchpad while fixing it?"
    a: "Absolutely — plug in any USB mouse and it works immediately with no setup. You can also enable Mouse Keys (Settings → Accessibility → Mouse → Mouse Keys) to move the cursor with the number pad in a pinch. For longer-term use, a small wireless mouse is inexpensive, and Bluetooth mice pair without using a USB port."
---

Your Synaptics touchpad stopped working, and you want it fixed — not a lecture. So here's the deal: answer the questions below in order, do the matching fix, and stop when the cursor moves. Most people are done by question three. This is the hands-on companion to our broader [Synaptics troubleshooting guide](/articles/what-to-do-if-synaptics-touchpad-not-working/) — use that one for background, this one for action.
Question zero, before we start: do you have a USB mouse handy? Plug it in now. Everything below is ten times easier with a working pointer, and there's no shame in it — technicians do exactly the same thing. If you don't have one, Windows' Mouse Keys (number pad as mouse) will get you through in a pinch.
The questions are ordered by how often each cause occurs, based on what actually walks into repair shops. Don't skip ahead to driver surgery before checking the toggles — the number of 'dead' touchpads fixed by one function-key press would embarrass us all. Lenovo owners with stubborn cases should also check our [Lenovo Synaptics guide](/articles/how-to-fix-synaptics-touchpad-not-working-on-lenovo-laptop/).

## Why this happens

- **Accidental function-key disable.** The number-one walk-in cause — one keypress, no on-screen notice on some models.
- **Settings toggle flipped.** Updates and utilities turn the Touchpad setting off silently.
- **'Disable when mouse connected' trap.** Plugging in a USB mouse auto-disables the pad; unplugging doesn't always re-enable it.
- **Driver replaced by Windows Update.** Working Synaptics driver swapped for a generic that half-supports the hardware.
- **Wrong driver type.** Synaptics vs. Precision mismatch kills gestures or the whole pad.
- **Palm rejection set too aggressively.** The pad works but ignores your fingers — feels dead, isn't.
- **BIOS-level disable.** 'Internal Pointing Device' switched off in firmware.
- **Ribbon cable or pad hardware failure.** The genuine hardware ending — least common, most final.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Answer: did you hit the touchpad toggle key?

The classic. One keypress kills the pad with no warning on many laptops — and it's the fix in a huge share of cases.

1. Find the touchpad icon on your function keys (F5/F7/F9 are common) — it looks like a rectangle with a finger.
2. Press Fn + that key (some laptops need just the key alone).
3. Watch for an on-screen indicator; test the pad immediately.
4. Try it twice — toggles can be out of sync with the actual state.
5. If the cursor moves, you're done. Go enjoy your laptop.

### Fix 2: Answer: is the Touchpad setting actually on?

Windows updates flip this toggle more often than anyone admits. Ten seconds to check.

1. Settings → Bluetooth & devices → Touchpad.
2. Ensure the main Touchpad toggle is ON.
3. If a USB mouse is plugged in, uncheck 'Leave touchpad on when a mouse is connected' is NOT the issue — actually, toggle it: unplug the mouse entirely for testing.
4. Set 'Touchpad sensitivity' to 'Most sensitive' to rule out palm-rejection weirdness.
5. Test the pad with the mouse unplugged.

### Fix 3: Answer: does Device Manager see it, and is it enabled?

Now we're checking Windows' own view of the hardware — disabled, driver-broken, or missing tells you the next move.

1. Open Device Manager (Windows + X).
2. Expand 'Mice and other pointing devices' AND 'Human Interface Devices'.
3. Down arrow on the Synaptics/ELAN entry → right-click → Enable device → test.
4. Yellow warning → right-click → Properties → read the error, then continue to the driver fix.
5. Missing entirely → View → 'Show hidden devices'; if still absent, skip to the BIOS/hardware fix.

### Fix 4: Answer: does it work in BIOS?

The great divider — this answer tells you whether to keep fixing software or start thinking hardware.

1. Restart and enter BIOS/UEFI setup (F2/Del/Esc — varies by maker).
2. Try moving the cursor on the touchpad in the BIOS screen.
3. Works in BIOS → hardware is fine; your problem is 100% Windows software — continue to the driver fix.
4. Dead in BIOS → hardware fault (ribbon cable or pad) — skip to the hardware fix; no driver will save it.
5. Write down the result — you'll need it if this goes to a repair shop.

### Fix 5: Fix the driver: remove wrong, install right

For every 'works in BIOS, dead in Windows' case — the driver is wrong, corrupted, or mismatched in type. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the Device Manager driver workflow if you want an official second reference.

1. Download the touchpad driver from YOUR laptop maker's support site for your exact model (not from Synaptics directly).
2. Device Manager → right-click the touchpad → Uninstall device → check 'Attempt to remove the driver for this device.'
3. Restart, then install the downloaded OEM driver.
4. Open Settings → Touchpad and confirm the full gesture panel appears (scroll, three-finger options).
5. If gestures are still missing, the wrong driver type installed — check whether your model uses Precision drivers and let Windows install those instead.

### Fix 6: Fix gestures-only breakage

Cursor moves, gestures don't — this is a driver-type or settings problem, never hardware.

1. Confirm the Touchpad settings page shows gesture sections; if it shows only basic options, return to the driver fix.
2. Scroll to the bottom → 'Reset' under 'Reset touchpad settings and gestures.'
3. Re-enable two-finger scroll and test immediately.
4. Re-enable three/four-finger gestures one at a time, testing each.
5. Disable third-party mouse/gesture utilities temporarily — they hijack gesture handling.

### Fix 7: The hardware ending: BIOS toggle, cable, replacement

For 'dead in BIOS' verdicts and everything software couldn't fix.

1. Enter BIOS → find 'Internal Pointing Device' / 'Touchpad' → ensure Enabled → save and retest.
2. Install the latest chipset driver — the pad connects via chipset-managed buses.
3. If comfortable: power off, open the bottom panel, reseat the touchpad's ribbon cable (flip the ZIF latch, reseat, relatch).
4. Test with a Linux live USB — working there means Windows is still the problem; dead there confirms hardware.
5. Confirmed dead + out of warranty → a compact wireless mouse is the pragmatic fix; in-warranty → file the claim. Our [touchscreen input guide](/articles/how-to-fix-touchscreen-not-working-on-laptop-in-windows-11-24h2/) covers related input diagnostics if other inputs act up too.

## Closing

Seven questions, seven fixes, and most touchpads are back by question three. The method is the message: check toggles, check Device Manager, test in BIOS, fix the driver — in that order, every time, and you'll never waste an afternoon on a one-keypress problem again.
