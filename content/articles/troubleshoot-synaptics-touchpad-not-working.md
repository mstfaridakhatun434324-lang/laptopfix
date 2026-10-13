---
title: "Synaptics Touchpad Not Working? Troubleshooting Steps That Work"
slug: troubleshoot-synaptics-touchpad-not-working
date: "2026-10-13"
categories: ["drivers"]
tags: ["synaptics touchpad", "touchpad driver", "cursor frozen", "precision touchpad", "mouse pad not working"]
description: "Synaptics touchpad not working on your Windows laptop? Follow these troubleshooting steps to re-enable the touchpad, fix the driver, and restore gestures."
thumbnail: "/images/thumbs/troubleshoot-synaptics-touchpad-not-working.webp"
faqs:
- q: "Why did my Synaptics touchpad suddenly stop working?"
  a: "The most common causes are the touchpad being disabled via the Fn-key toggle or Windows settings, a Windows update replacing the Synaptics driver with a generic one, or the driver becoming corrupted. Because the touchpad depends on both a software enable switch and a working driver, checking the toggle first and then reinstalling the manufacturer's driver resolves the issue in the large majority of cases."
- q: "How do I re-enable my touchpad if the Fn key does not work?"
  a: "Open Settings, go to Bluetooth and devices, then Touchpad, and make sure the touchpad switch is on. Also check the legacy Mouse properties under Additional mouse settings for a Synaptics or ClickPad tab with its own enable button. If both are on and the pad is still dead, the driver is the problem — reinstall it from your laptop manufacturer's support page."
- q: "Should I use the Synaptics driver or Microsoft's precision driver?"
  a: "Use whichever your laptop manufacturer ships for your model. Some laptops are designed for the Synaptics driver with its control panel, while others use Microsoft's precision touchpad driver built into Windows. Installing the wrong one causes missing gestures or a dead pad. Your manufacturer's support page lists the correct touchpad driver for your exact model — that is the one to install."
- q: "Can I fix the touchpad without a mouse?"
  a: "Yes. Use the keyboard: press the Windows key to open Start, type settings, and navigate with Tab, arrows, and Enter. Enable Mouse Keys (Alt + left Shift + Num Lock) to control the cursor with the number pad, or press Win + Ctrl + O for the on-screen keyboard. These built-in tools let you reach Device Manager and Settings to perform every fix in this guide."
---

The cursor sits frozen in the middle of the screen. Taps do nothing, two-finger scroll is a memory, and you are navigating Windows with keyboard shortcuts like it is 1995. Touchpad failures feel catastrophic because the touchpad is the primary input on a laptop — but like most laptop input problems, the cause is usually a switch that got flipped or a driver that broke, not dead hardware.

Synaptics touchpads are especially prone to one specific failure mode: Windows Update replaces the manufacturer's Synaptics driver with a generic Microsoft one (or vice versa), and the pad either dies completely or loses gestures. The second classic is the Fn-key toggle — one accidental keypress disables the pad, and nothing on screen explains why the cursor stopped moving.

This guide covers both, in order: the enable switches first (fastest), then the driver repairs, then the deeper checks. You can do all of it with keyboard alone if needed.

## Why this happens

- **Touchpad disabled via Fn key or setting**: An accidental Fn-key press or settings change switches the pad off silently.
- **Driver replaced by Windows Update**: Update swaps the Synaptics driver for a generic one that does not initialize the pad.
- **Corrupted Synaptics driver**: Failed updates leave a half-installed driver the pad cannot use.
- **Wrong driver type installed**: Synaptics-driver laptops given the precision driver (or reverse) lose function.
- **BIOS toggle disabled**: Some laptops have a firmware-level touchpad switch, reset by BIOS updates.
- **Conflicting external mouse software**: Mouse utilities can auto-disable the touchpad when a USB mouse is present — and fail to re-enable it.
- **Hardware failure**: Least common; a damaged touchpad cable (often after palmrest repairs) kills the pad electrically.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the touchpad toggle — Fn key and Windows setting

Before anything else, verify the pad is actually enabled. Laptops have two independent switches: a function-key toggle (usually Fn + F5/F7 or a key with a touchpad icon, sometimes with an LED) and the Windows touchpad switch. Either one off means a dead pad with zero error messages. This check resolves a remarkable number of "sudden" failures.

1. Press the touchpad Fn-key combination on your keyboard (look for the touchpad icon).
2. Open Settings, Bluetooth and devices, Touchpad, and confirm the toggle is On.
3. Untick "Leave touchpad on when a mouse is connected" temporarily for testing.
4. Disconnect any USB mouse and test the pad.
5. If the pad works now, the mystery was a switch — consider disabling the Fn toggle shortcut if your BIOS allows it.

### Fix 2: Enable the pad in the legacy mouse properties

Some Synaptics installations keep a second, older enable switch in the classic Mouse control panel — a Synaptics or ClickPad tab with its own device list and enable button. The Windows 11 touchpad toggle and this legacy switch can disagree, leaving the pad disabled despite the modern setting showing On. Checking both covers the disagreement.

1. In the Touchpad settings page, click "Additional mouse settings" (under Related settings).
2. Look for a Synaptics, ClickPad, or Device Settings tab.
3. Select the touchpad device in the list and click "Enable" if it is disabled.
4. Click Apply and test the pad immediately.
5. While here, check the tapping and gesture options are configured as you like.

### Fix 3: Reinstall the Synaptics driver from the manufacturer

When the pad is enabled everywhere but still dead — or Device Manager shows it with a warning or as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/) — the driver is corrupt or mismatched. Installing the touchpad driver from your laptop maker's support page restores the exact driver build the hardware expects, including the control panel and gestures.

1. Open Device Manager and expand "Human Interface Devices" and "Mice and other pointing devices."
2. Right-click the Synaptics entry, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Restart the laptop and test — Windows may install a working driver automatically.
4. If not, download the touchpad driver from your maker's support page (for Lenovo models, [Lenovo Support](https://support.lenovo.com/us/en/) lists it under Mouse/Touchpad) and install it.
5. Restart once more and verify tapping, scrolling, and gestures all work.

### Fix 4: Roll back the driver after a Windows update

If the touchpad died immediately after an update, the previous driver was working and the new one is not — so go back. Driver rollback restores the exact previous version in seconds, no download needed. This is the fastest fix when the timeline points at an update, and it works even when you cannot get online to download anything.

1. In Device Manager, right-click the Synaptics touchpad and choose Properties.
2. Open the Driver tab and click "Roll Back Driver" (if available).
3. Select a reason, confirm, and restart when prompted.
4. Test the touchpad after reboot.
5. To stop Windows from breaking it again, pause driver updates via Windows Update settings.

### Fix 5: Check the BIOS touchpad toggle

A firmware-level disable overrides everything in Windows — no driver, no setting, no rollback can enable a pad the BIOS has switched off. BIOS updates sometimes reset this toggle, which explains touchpads that die "for no reason" overnight. The check takes two minutes and is definitive.

1. Restart and enter BIOS/UEFI setup.
2. Look under Advanced, Devices, or Main for "Touchpad," "Internal Pointing Device," or similar.
3. Set it to Enabled (not "Advanced" mode if that option misbehaves — try both).
4. Save and exit, then boot into Windows.
5. Test the pad before changing any Windows settings.

### Fix 6: Rule out software conflicts with a clean boot

Mouse utilities, remote-desktop tools, and some accessibility software hook into the input stack and can suppress the touchpad. If the pad works in Safe Mode but not normally, something installed is interfering. Safe Mode loads a minimal driver set, making it a clean test environment for exactly this question.

1. Boot into Safe Mode (hold Shift while clicking Restart, then Troubleshoot, Advanced, Startup Settings).
2. Test the touchpad in Safe Mode.
3. If it works there, return to normal mode and run `msconfig` for a clean boot.
4. Re-enable startup services in halves to isolate the conflicting program.
5. Uninstall or reconfigure the offender — often a third-party mouse or gesture utility.

### Fix 7: Test the hardware and consider professional repair

If the pad is dead in BIOS-level diagnostics, absent from Device Manager even with hidden devices shown, and unresponsive in a Linux live environment, the hardware has failed — usually the touchpad cable, which routes through the palmrest hinge area and wears over time. Manufacturer diagnostics (often F12 at boot) include a touchpad test that bypasses Windows entirely.

1. Run your manufacturer's built-in diagnostics and execute the touchpad/mouse test.
2. Boot a Linux live USB and test the pad there as a second opinion.
3. If both fail, the touchpad cable or pad itself needs replacement.
4. Check warranty status — touchpad replacement is a standard, usually affordable repair.
5. As a stopgap, a small wireless mouse restores full usability for very little money. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document additional input troubleshooting if needed.

Keyboard trouble often arrives with touchpad trouble after the same update — our guide to [fixing a laptop keyboard not working](/articles/how-do-i-fix-keyboard-not-working-on-laptop/) covers the companion repair.

## Closing

A dead Synaptics touchpad is usually a flipped switch or a driver Windows Update replaced — check the Fn toggle and Windows setting first, then reinstall or roll back the manufacturer's driver. Only when the pad is invisible to BIOS diagnostics and Linux alike should you suspect the cable or the pad itself.
