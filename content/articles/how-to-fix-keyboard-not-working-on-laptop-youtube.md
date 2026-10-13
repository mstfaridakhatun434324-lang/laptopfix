---
title: "How to Fix a Keyboard Not Working on a Windows Laptop"
slug: how-to-fix-keyboard-not-working-on-laptop-youtube
date: 2026-09-16
categories: ["drivers"]
tags: ["keyboard not working", "laptop keyboard", "keyboard driver", "windows 11"]
description: "Fix a laptop keyboard not working on Windows: unlock filter keys, repair the keyboard driver, and get typing again without an external keyboard."
thumbnail: "/images/thumbs/how-to-fix-keyboard-not-working-on-laptop-youtube.webp"
faqs:
  - q: "Why did my laptop keyboard suddenly stop typing?"
    a: "The most common causes are Filter Keys being enabled accidentally, a corrupted keyboard driver, or the keyboard being disabled in Device Manager. Liquid damage and loose ribbon cables cause physical failures, but software causes are far more common and fixable in minutes. Start with the software checks before suspecting hardware."
  - q: "Some keys work but others do not. Is that a driver problem?"
    a: "Usually not — partial key failure points to hardware. A dead row or cluster of keys typically means a damaged keyboard membrane or a partially seated ribbon cable. Driver problems tend to kill the entire keyboard at once. Try an external USB keyboard to confirm the system itself accepts input normally."
  - q: "Can I use my laptop if the keyboard is dead?"
    a: "Yes. Plug in any USB keyboard as an immediate workaround, or use the On-Screen Keyboard by pressing Win plus Ctrl plus O. The on-screen keyboard lets you log in and perform all the driver fixes in this guide without any physical keyboard at all."
  - q: "Will reinstalling Windows fix a dead keyboard?"
    a: "Only if the cause is software, and a driver reinstall achieves the same result with far less disruption. Test the keyboard in BIOS first — if it works there, Windows is the problem and driver repair will fix it. If it fails in BIOS too, no software reinstall will help because the hardware itself is at fault."
---

A laptop keyboard that stops responding turns a portable computer into a very expensive paperweight — you cannot log in, cannot search for fixes, and cannot do much of anything. Before panic sets in, know this: total keyboard failure on Windows is a software problem more often than people expect, and the software causes are quick to check even with no working keys.

This guide is built for the no-keyboard situation. Every step can be done with a mouse, touchpad, or the On-Screen Keyboard (**Win + Ctrl + O**), and it moves from the instant fixes — accessibility settings that silently hijack typing — through driver repair to the hardware verdict.

## Why this happens

- **Filter Keys enabled:** Holding the Shift key too long enables this accessibility feature, which then ignores brief keystrokes.
- **Corrupted keyboard driver:** The standard PS/2 keyboard driver can corrupt after updates, killing all input at once.
- **Keyboard disabled in Device Manager:** The device can be disabled at the driver level, which no settings toggle will reverse.
- **Stuck modifier key:** A physically or logically stuck Ctrl, Alt, or Win key makes every keystroke behave like a shortcut.
- **Conflicting software:** Keyboard macro tools, remote desktop clients, and some security software can intercept keystrokes.
- **Fast Startup driver state:** Windows' Fast Startup can resume a broken keyboard driver state across reboots.
- **BIOS-level issue:** Rare, but a BIOS misconfiguration or failed firmware update can disable the internal keyboard.
- **Physical failure:** Liquid spills, worn membranes, and loose ribbon cables kill keys or the whole board — the hardware end of the spectrum.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off Filter Keys and Sticky Keys

1. Open **Settings → Accessibility → Keyboard** using your mouse or On-Screen Keyboard.
2. Turn **off** Sticky Keys, Filter Keys, and Toggle Keys.
3. Under Filter Keys specifically, make sure the shortcut (holding Shift for 8 seconds) is disabled so it cannot retrigger.
4. Test typing immediately — accidentally enabled Filter Keys is the single most common cause of "keyboard suddenly stopped working," and it mimics hardware failure convincingly.

### Fix 2: Test with an external keyboard and in BIOS

1. Plug in any USB keyboard. If it types normally, Windows is healthy and the problem is isolated to the internal keyboard's driver or hardware.
2. Restart and press **F2**, **F10**, or **Del** to enter BIOS — try typing there.
3. If the internal keyboard works in BIOS but not Windows, you have a confirmed software problem — continue with the driver fixes.
4. If it fails in BIOS too, skip to the hardware checks at the end; no Windows fix will revive a keyboard that BIOS cannot see.

### Fix 3: Reinstall the keyboard driver

1. Open **Device Manager → Keyboards**, right-click **Standard PS/2 Keyboard**, and choose **Uninstall device**.
2. Restart the laptop — Windows reinstalls the driver automatically during boot.
3. If the keyboard is missing from Device Manager entirely, click **Action → Scan for hardware changes**.
4. A fresh driver resolves the corruption cases that follow Windows updates, the same class of failure behind [touchpad driver problems](/articles/how-to-fix-keyboard-not-working-on-laptop-on-windows-10/) on many laptops.

### Fix 4: Disable Fast Startup

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **"Change settings that are currently unavailable"** and uncheck **"Turn on fast startup"**.
3. Shut down fully (not restart) and power back on.
4. Fast Startup resumes the kernel driver state from disk — if the keyboard driver was broken when that state was saved, every "restart" faithfully restores the broken state until you do a true cold boot.

### Fix 5: Check for stuck modifier keys

1. Open the On-Screen Keyboard (**Win + Ctrl + O**) and watch the Ctrl, Alt, Shift, and Win keys as you tap each physical modifier.
2. If an on-screen modifier appears highlighted without being pressed, its physical key is stuck — press it firmly several times or clean around it.
3. Remove any key remapping or macro software temporarily (AutoHotkey, gaming utilities, remote desktop tools).
4. Test in a plain text editor like Notepad to rule out application-specific interception.

### Fix 6: Run the keyboard troubleshooter and check for malware

1. Open **Settings → System → Troubleshoot → Other troubleshooters → Keyboard → Run**.
2. Apply any fixes it recommends and restart.
3. Run a full scan with Windows Security — certain malware intercepts keystrokes, and a dead keyboard can occasionally be a symptom rather than a driver fault. Microsoft's guidance on [Windows security and recovery](https://support.microsoft.com/en-us/windows) covers scan options if the built-in tools seem compromised.

### Fix 7: Update BIOS and chipset drivers

1. Visit your laptop maker's support site and check for **BIOS** and **chipset/IO driver** updates for your exact model.
2. Install with the charger connected; the keyboard controller firmware sometimes ships inside BIOS updates.
3. After updating, enter BIOS and choose **Load Setup Defaults** to clear any misconfiguration.
4. This step is particularly relevant when the keyboard failed immediately after a firmware update.

### Fix 8: Evaluate the hardware

1. If specific key clusters are dead while others work, the keyboard membrane is damaged — replacement is the fix, and on many laptops the keyboard is a separate, inexpensive part.
2. If the whole keyboard is dead including in BIOS, the ribbon cable may have worked loose (common after drops) or the controller failed.
3. Check whether your model allows easy keyboard replacement — many business laptops have it held by a few screws, while ultrabooks may need professional service. Related input-device diagnostics for [touchpads](/articles/how-to-fix-elan-touchpad-not-working-in-windows-11-24h2/) use the same BIOS-test logic to separate hardware from software.

## Closing

A dead laptop keyboard is alarming but very often a settings or driver issue: Filter Keys silently enabled, a corrupted PS/2 driver, or Fast Startup resurrecting a broken state. The BIOS test is your compass — working in BIOS means Windows can be fixed, and failing in BIOS means it is time to talk about hardware. Either way, you now know exactly which path you are on.
