---
title: "How to Fix Click to Do Not Working With a Stylus Pen"
slug: click-to-do-stylus-pen-not-working-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["click to do", "stylus pen", "surface pen", "touchscreen", "copilot+ pc", "windows 11"]
description: "Fix Click to Do not working with a stylus pen on your Copilot+ PC with checks for pen pairing, Windows Ink settings, selection gestures, and driver repair."
thumbnail: "/images/thumbs/click-to-do-stylus-pen-not-working-fix.webp"
faqs:
  - q: "Why does Click to Do work with touch but not with my pen?"
    a: "Pen input travels a different path in Windows than finger touch: it goes through Windows Ink and pen-specific drivers. If pen pairing, Ink settings, or the pen driver fails, Click to Do can work fine by touch while ignoring the pen entirely."
  - q: "Does Click to Do support every stylus?"
    a: "Click to Do works best with the pen designed for your PC, such as a Surface Slim Pen on a Surface device. Third-party pens that lack Windows Ink support may select text but fail to trigger the Click to Do gesture reliably."
  - q: "Can a low pen battery break Click to Do?"
    a: "Yes. A low or dead pen battery causes missed clicks, failed selections, and gestures that Windows never registers. Replace or charge the pen battery first before assuming a software fault."
  - q: "Will resetting pen settings delete my notes?"
    a: "No. Pen and Windows Ink settings do not store your notes; those live in your note app or OneNote. Resetting pen settings only changes how the pen behaves, not what you have written."
---

Click to Do works perfectly with your finger or mouse — but with the stylus pen, the gesture does nothing. You circle text, press the pen button, hold and tap, and the menu never appears, even though the pen writes normally elsewhere. The pen is not broken; the path Click to Do listens on is different for pen input.

Pen input goes through Windows Ink, pairing, and button handling that finger touch skips. A dead battery, lost pairing, Ink setting, or pen driver can break the Click to Do gesture while leaving handwriting untouched.

This guide isolates the pen layer first, then the gesture, then the drivers. Test with the pen after each fix in Notepad, so you know which step restored it.

## Why this happens

- **Pen battery low or dead:** Weak pen batteries cause dropped clicks and incomplete selections, so Windows never sees a complete Click to Do gesture.
- **Pen Bluetooth pairing lost:** On pens that pair over Bluetooth, a dropped pairing kills button shortcuts and gesture recognition while basic inking still works.
- **Windows Ink settings changed:** Ink workspace settings, pen button assignments, or "ignore touch when using pen" options can redirect or swallow the gesture Click to Do expects.
- **Wrong selection gesture with the pen:** Click to Do needs a proper text selection followed by its activation gesture; circling, scribbling, or a single pen tap does not count as a selection.
- **Pen driver or firmware outdated:** A stale pen, touchscreen, or Bluetooth driver can break pen-button events after a Windows update while touch and mouse keep working.
- **App does not support pen-based Click to Do:** Some apps accept pen handwriting but do not expose pen selections to Click to Do in the same way as touch or mouse selections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Charge the pen and test basic pen input

A pen that writes can still be too weak for gestures, which need a clean, complete click event. Start with power and basic input before touching any setting.

1. Charge the pen fully, or replace its battery — on a Surface Slim Pen, place it in its charging slot or on its charger until the light confirms a full charge.
2. Open a blank page in a note app, write a sentence, then select it by dragging the pen across the words.
3. Tap the pen once and confirm the tap registers as a click, not as an ink dot.
4. Open Notepad, type a sentence, select it with the pen, and try the gesture: hold the **Windows key** and tap the selection with the pen.
5. If the gesture now works, low power was the cause. If basic pen taps also fail, the pen hardware or pairing is at fault — continue below. See also [Copilot actions not working](/articles/copilot-actions-not-working/).

### Fix 2: Re-pair the pen over Bluetooth

Bluetooth pens keep two connections: the digitiser for writing, and Bluetooth for buttons and shortcuts. The second can drop while the first works, which exactly matches "writes fine, Click to Do dead."

1. Open **Settings > Bluetooth & devices** and check whether your pen appears as **Connected** — if it shows **Paired** only, or is missing, it needs re-pairing.
2. Remove the pen from the device list, then put the pen in pairing mode by holding its top button until the light blinks.
3. Click **Add device > Bluetooth** in Settings and select the pen when it appears, waiting for the **Connected** status.
4. Open **Settings > Bluetooth & devices > Pen & Windows Ink** and confirm the pen is recognised there too.
5. Test the Click to Do gesture in Notepad with the pen again — a fresh pairing restores button and gesture events that a stale pairing silently drops.

### Fix 3: Check Pen and Windows Ink settings

Windows Ink controls what the pen button does and how Windows treats pen versus touch input. A setting changed by an update can redirect the exact gesture Click to Do needs.

1. Open **Settings > Bluetooth & devices > Pen & Windows Ink**.
2. Confirm **"Ignore touch input when I'm using my pen"** is set the way you want — try toggling it off temporarily, since it can interfere with mixed pen-and-keyboard gestures.
3. Review the pen button shortcuts: make sure the top button and barrel button are not assigned to an app that swallows the click.
4. Enable **"Show visual effects"** and **"Show cursor"** for the pen temporarily, so you can see whether Windows registers your pen taps at all.
5. Test the gesture in Notepad again. If it works with touch ignored off, leave that setting off for Click to Do use. A related selection-path problem is covered in [Click to Do File Explorer preview](/articles/click-to-do-file-explorer-preview-fix/), where the app surface decides which gestures reach Click to Do.

### Fix 4: Learn the exact pen selection gesture for Click to Do

Many pen failures are not failures at all — they are the wrong gesture. Click to Do needs a real text selection first, and circling text or tapping once does not count.

1. In Notepad, type a full sentence, then press the pen tip at the start of the sentence and drag slowly to the end, watching the highlight follow the pen.
2. Lift the pen, then hold the **Windows key** on the keyboard with your other hand and tap inside the highlighted text with the pen.
3. Wait two seconds — the menu can take a moment to appear on pen input, longer than on mouse input.
4. If that works, practise the same two-handed gesture in your real app; the keyboard hand is part of the gesture, and a pen-only attempt will not trigger it.
5. If your pen has a barrel button, try holding it while tapping the selection as an alternative — but do not rely on circling or lasso gestures, which Click to Do does not use for text selection.

### Fix 5: Update pen, touchscreen, and Bluetooth drivers

Updating the whole input stack restores the agreement.

1. Open **Device Manager** and expand **Human Interface Devices**, **Bluetooth**, and **Mice and other pointing devices**, looking for pen or touchscreen entries.
2. Right-click each pen, touchscreen, and Bluetooth entry and choose **Update driver > Search automatically for drivers**.
3. Also download the latest pen and firmware package for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — PC-maker packages include pen firmware that Windows Update does not.
4. Restart the PC after installing, re-pair the pen if prompted, and test the Click to Do gesture in Notepad.
5. If a driver update made things worse, roll back just that driver in Device Manager via **Properties > Driver > Roll Back Driver**, then test again. Driver-sensitive AI workloads on the same hardware are discussed in [TensorFlow DirectML on AI laptops](/articles/tensorflow-directml-ai-laptop-fix/), where one stale driver breaks a whole class of features.

### Fix 6: Test in a second app and reset pen settings

If the pen works in Notepad but not in your main app, the app is the limiter. If it fails everywhere, a pen-settings reset clears corrupted Ink state that driver updates leave behind.

1. Test the pen gesture in Notepad, then in Edge, then in your usual app, noting where it works and where it fails.
2. If it works in Notepad and Edge but not in one app, update that app and check its pen settings — some apps disable pen gestures by default.
3. If it fails everywhere, go to **Settings > Bluetooth & devices > Pen & Windows Ink**, restore the defaults, and restart.
4. Remove and re-pair the pen once more after the reset, since the reset can drop the pairing.
5. As a final test, try a different compatible pen if one is available — if it works, your original pen's button hardware is faulty and needs replacement.

## Closing

Click to Do failing only with a pen is a pen-path problem: battery, Bluetooth pairing, Ink settings, the selection gesture, or a stale pen driver. Charge the pen, re-pair it, practise the two-handed gesture, and update the input drivers.
