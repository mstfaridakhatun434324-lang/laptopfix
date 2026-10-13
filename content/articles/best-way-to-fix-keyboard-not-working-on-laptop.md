---
title: "The Best Way to Fix a Keyboard Not Working on a Laptop"
slug: best-way-to-fix-keyboard-not-working-on-laptop
date: 2026-10-08
categories: ["drivers"]
tags: ["keyboard fix", "laptop keyboard", "keyboard driver", "filter keys", "keys not working"]
description: "The best way to fix a laptop keyboard that's not working: quick Filter Keys check, driver reinstall, BIOS test, and hardware diagnosis."
thumbnail: "/images/thumbs/best-way-to-fix-keyboard-not-working-on-laptop.webp"
faqs:
  - q: "What is the fastest fix for a laptop keyboard not working?"
    a: "Check Filter Keys first — it takes ten seconds and resolves a huge number of cases. Open Settings, Accessibility, Keyboard, and turn Filter Keys off. Holding the right Shift key for eight seconds enables it accidentally, after which the keyboard ignores normal keystrokes and appears completely dead."
  - q: "How do I reinstall my laptop keyboard driver?"
    a: "Open Device Manager, expand Keyboards, right-click Standard PS/2 Keyboard, choose Uninstall device, and restart. Windows reinstalls the driver automatically at boot. This fixes corruption from updates that causes total or partial key failure, and it's safe — the keyboard works during the process via the basic input driver."
  - q: "Why do only some keys work on my laptop keyboard?"
    a: "Partial key failure is usually hardware: a damaged keyboard membrane, a partially seated ribbon cable, or liquid damage affecting specific key traces. Software causes like Filter Keys or drivers typically affect all keys equally. A row or cluster of dead keys points firmly at the membrane or cable."
  - q: "Can a BIOS update fix keyboard problems?"
    a: "Rarely, but it's worth checking your maker's support page for BIOS release notes mentioning keyboard fixes. More useful is the BIOS as a diagnostic: if the keyboard works in BIOS setup, the hardware is fine and the problem is Windows software. If it fails in BIOS too, no software update will help — it's hardware."
---

When a laptop keyboard stops working, the most effective approach isn't trying random fixes — it's running the highest-probability checks first. Years of support data show a clear ranking: accessibility settings (Filter Keys) lead by a wide margin, followed by driver corruption, stuck controller states, and only then physical problems. This guide orders the fixes by that probability so the average user is typing again within minutes.

Start at the top and stop when typing works. Each fix includes its diagnostic logic so you understand why you're doing it, not just what to click.

## Why this happens

- **Filter Keys enabled:** The runaway leader — an accessibility feature that ignores brief keystrokes, activated by holding right Shift for 8 seconds.
- **Keyboard driver corruption:** Update-damaged PS/2 keyboard drivers cause partial or total failure.
- **Embedded controller stuck:** The controller managing the keyboard can crash into an unresponsive state that survives reboots.
- **Conflicting software:** Key remappers, macro tools, and some security software intercept and block keystrokes.
- **Liquid damage:** Spills corrode the membrane progressively — keys die over hours or days, not instantly.
- **Ribbon cable issues:** Loose or damaged cables from drops or prior repairs cause partial or total failure.
- **BIOS-level problems:** Rare firmware bugs or disabled internal devices.
- **Malware:** Keyloggers hooking keystrokes can disrupt normal typing behavior.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off Filter Keys

1. Press **Win + Ctrl + O** to open the On-Screen Keyboard (you'll need it for navigation).
2. Go to **Settings → Accessibility → Keyboard** and turn **Filter keys** OFF.
3. Uncheck **Allow the shortcut key to start Filter Keys** to prevent recurrence.
4. Test typing immediately in Notepad.
5. If this fixed it, you're done — this resolves more keyboard cases than all other fixes combined. The [full keyboard troubleshooting guide](/articles/keyboard-not-working-on-laptop-troubleshooting/) covers the deeper causes for when it doesn't.

### Fix 2: Do the BIOS test to split software from hardware

1. Restart and enter BIOS/UEFI setup (**F2**, **Del**, or **Esc**).
2. Try navigating with arrow keys or typing in any field.
3. **Works in BIOS** = hardware is fine; continue with software fixes below with confidence.
4. **Fails in BIOS** = hardware fault; skip to Fix 7 — software fixes cannot help.
5. This two-minute test is the highest-value diagnostic in keyboard repair. It prevents wasted hours of driver work on broken hardware and vice versa.

### Fix 3: Reinstall the keyboard driver

1. Open **Device Manager** (Win + X) → expand **Keyboards**.
2. Right-click **Standard PS/2 Keyboard** → **Uninstall device**.
3. Restart the laptop — Windows reinstalls the driver during boot.
4. Test every key, including modifiers, function keys, and the number row.
5. If Device Manager showed Code 19 or 39 on the keyboard, corruption was confirmed — the reinstall was the right call. Back up working drivers afterward with the [driver backup method](/articles/best-way-to-backup-drivers-before-update/) so you can restore quickly next time.

### Fix 4: Power-drain the embedded controller

1. Shut down completely and disconnect the charger.
2. Remove the battery if it's removable; if not, just leave the machine unplugged.
3. Hold the power button for **30 seconds**.
4. Reconnect power and boot — test the keyboard at the login screen.
5. The embedded controller manages the keyboard at a firmware level, and its crashed state survives normal restarts. The power drain is the only reset that reaches it.

### Fix 5: Check for software conflicts in Safe Mode

1. Boot into **Safe Mode** (Shift + Restart → Troubleshoot → Startup Settings → press 4).
2. Test typing. Working in Safe Mode = a third-party program or driver is blocking keystrokes in normal mode.
3. Return to normal mode, open **msconfig**, and disable half the startup items; retest. Bisect until you find the culprit.
4. Prime suspects: keyboard remapping tools, macro software, "gaming mode" utilities, and recently installed system tools.
5. Uninstall the offending program fully — don't just disable it, since low-level keyboard hooks can persist.

### Fix 6: Scan for malware

1. Run a **Full scan** in **Windows Security → Virus & threat protection**.
2. Keyloggers and info-stealers hook keyboards at a low level and can cause dropped, doubled, or blocked keystrokes.
3. Follow up with the **Microsoft Safety Scanner** from [Microsoft Support](https://support.microsoft.com/en-us/windows) for a second opinion.
4. After removing threats, reinstall the keyboard driver (Fix 3) — malware-damaged input stacks don't always self-heal.
5. If a keylogger was found, change passwords from a known-clean device.

### Fix 7: Inspect for physical damage

1. Look for spill evidence: sticky keys, stains, or a remembered accident. Power off immediately if a spill is fresh — every minute matters for corrosion.
2. For a cluster of dead keys, suspect the membrane or ribbon cable. Compressed air clears debris; it doesn't fix membrane damage.
3. Test with a USB keyboard — perfect external typing confirms the OS side is healthy and isolates the built-in hardware.
4. On models with serviceable keyboards, reseat the ribbon cable following the service manual — a partially unseated cable causes exactly the partial-failure pattern.
5. Individual dead keys on an otherwise fine keyboard = membrane damage = keyboard replacement, not software.

### Fix 8: Replace the keyboard or adapt

1. Check your model's replacement difficulty and part cost — many business laptops have straightforward keyboard swaps; ultrabooks may need full disassembly.
2. Under warranty? Contact the manufacturer — include your BIOS test result ("fails in BIOS") for fast authorization.
3. Out of warranty and handy? Follow a model-specific video guide; take photos of each screw position.
4. Not handy? A compact wireless keyboard is a fine permanent setup for a desk-bound laptop.
5. Enable **On-Screen Keyboard** (**Win + Ctrl + O**) for login screens and short typing until the repair is done.

## Closing

The best way to fix a laptop keyboard is the ordered way: Filter Keys first (seconds), BIOS test second (minutes, and it tells you which world you're in), driver reinstall and power drain third, hardware inspection last. Most keyboards are back within the first three steps. The ones that aren't have told you — via the BIOS test — exactly what kind of problem you're dealing with.
