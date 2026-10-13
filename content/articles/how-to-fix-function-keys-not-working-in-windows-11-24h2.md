---
title: "How to Fix Function Keys Not Working in Windows 11 24H2"
slug: how-to-fix-function-keys-not-working-in-windows-11-24h2
date: 2026-09-30
categories: ["drivers"]
tags: ["function keys", "windows 11 24h2", "hotkeys", "keyboard driver"]
description: "Function keys dead after Windows 11 24H2? Fix Fn key behavior, hotkey drivers, and BIOS settings so your media and brightness keys work again."
thumbnail: "/images/thumbs/how-to-fix-function-keys-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my function keys stop working after the Windows 11 24H2 update?"
    a: "The 24H2 update can replace your laptop maker's hotkey utility driver with a generic version that does not understand the Fn key layer. On many models the update also resets the BIOS Fn behavior setting. Reinstalling the manufacturer's hotkey software and checking the BIOS Fn lock mode fixes this on most machines."
  - q: "What is the difference between Fn keys and F1-F12 behavior?"
    a: "Modern laptops default the top row to media actions like volume and brightness, requiring the Fn key plus F1-F12 for traditional function keys. BIOS and utilities can invert this. If your keys do the wrong action rather than nothing, the Fn lock mode flipped — not a driver failure."
  - q: "Do I need the manufacturer's hotkey utility installed?"
    a: "Usually yes. Basic keys may work with Windows alone, but brightness, airplane mode, keyboard backlight, and performance-mode keys typically need the maker's hotkey or system utility package. Dell, HP, and Lenovo each ship one, and 24H2 sometimes silently removes it."
  - q: "Can a BIOS update break the function keys?"
    a: "It can reset their configuration. BIOS updates often restore default Fn key behavior, which may differ from what you had. Check the BIOS Advanced or Keyboard settings after any BIOS update and set the Fn key behavior back to your preference."
---

When function keys stop working after the Windows 11 24H2 update, the failure is rarely the keyboard itself. The physical keys are fine; what broke is the software layer that translates Fn combinations into brightness changes, volume adjustments, and airplane-mode toggles. On most laptops that layer is a manufacturer hotkey driver plus a BIOS setting, and 24H2 has a habit of disturbing both.

Start by identifying exactly what is broken. Do the keys do nothing at all, or do they do the wrong thing (F1-F12 instead of media actions, or vice versa)? "Nothing" points to a missing hotkey driver; "wrong action" points to Fn lock mode. That distinction saves you half the troubleshooting below.
A useful mental model: your function keys live in three layers — the physical key, the BIOS/EC firmware that interprets Fn combinations, and the Windows hotkey utility that turns them into actions like brightness changes. The 24H2 update can disturb the top two layers without touching the key itself. The fixes below check each layer in turn, which is faster than reinstalling drivers at random and hoping.

## Why this happens

- **Hotkey driver replaced by 24H2:** The update installs a generic keyboard driver over the manufacturer's hotkey package, killing Fn-layer functions.
- **Fn lock mode reset:** 24H2 or a companion BIOS update flips the default between media keys and F1-F12 behavior.
- **Manufacturer utility uninstalled:** The update can remove the hotkey/system utility (Dell QuickSet, HP Hotkey Support, Lenovo Hotkeys) without warning.
- **BIOS Fn setting changed:** BIOS updates bundled with 24H2 rollouts reset the Function Key Behavior option to factory default.
- **Windows Mobility Center conflicts:** Stale Mobility Center policies can override brightness and media key handling after the update.
- **Fast Startup caching old driver state:** Hybrid shutdown preserves the broken driver state across reboots, making the problem look permanent.
- **Filter driver corruption:** Upper/lower filter drivers in the keyboard stack can corrupt during the update, blocking all special-key processing.
- **Actual keyboard hardware fault:** Rare and usually partial — a dead Fn key alone, while every other key works, suggests hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn lock state first

1. Look for an **Fn lock** indicator — many laptops show it on the Fn key itself (a small lock LED) or via an on-screen display when you press **Fn + Esc**.
2. Press **Fn + Esc** to toggle Fn lock and test the keys again.
3. Also try holding **Fn** while pressing a function key to see if the alternate action works.
4. If toggling changes the behavior, this was configuration, not breakage — set your preferred default in the BIOS (Fix 3) and move on.

### Fix 2: Reinstall the manufacturer's hotkey software

1. Identify your maker's package: Dell QuickSet/Command, HP Hotkey Support, Lenovo Hotkey Features Integration, ASUS ATK Package.
2. Download the latest version for Windows 11 from the official support site — [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) as appropriate.
3. Uninstall the existing hotkey utility from **Settings → Apps** first, restart, then install the fresh package.
4. Test all Fn combinations. Missing utilities are the single most common cause after 24H2.
5. If the utility installs but keys still fail, check whether the touchpad or other input devices also misbehave — input devices share driver infrastructure, and our [Synaptics touchpad repair guide](/articles/synaptics-touchpad-not-working-troubleshooting/) covers the shared-stack issues that can affect keyboards too.

### Fix 3: Set Fn behavior in the BIOS

1. Restart into the BIOS (**F2**, **F10**, **Del**, or the Novo button depending on brand).
2. Find **Advanced → Function Key Behavior** (Dell), **System Configuration → Action Keys Mode** (HP), or **Config → Keyboard/Mouse → Fn and Ctrl Key swap** area (Lenovo).
3. Set it to your preference: **Multimedia Key** for media-first behavior or **Function Key** for F1-F12-first.
4. Save and exit, then verify in Windows.

### Fix 4: Reinstall the keyboard driver cleanly

1. Open **Device Manager → Keyboards**, right-click the HID/PS2 keyboard → **Uninstall device** (do not tick driver removal unless a custom driver is listed).
2. Restart — Windows reinstalls the standard keyboard driver automatically.
3. If special keys still fail, install the chipset driver package from your maker, since keyboard controller logic often rides with it. This is the same clean-driver discipline used for [audio driver crashes](/articles/how-to-fix-audio-driver-keeps-crashing-on-lenovo-laptop/).
4. Reinstall the hotkey utility from Fix 2 after the driver refresh.
5. After the refresh, open **Settings → Bluetooth & devices** and confirm Windows sees the keyboard as the maker's device rather than a generic HID keyboard — a generic label means the custom driver didn't bind and special keys won't work.

### Fix 5: Do a full shutdown to clear Fast Startup state

1. Hold **Shift** while clicking **Shut down** for a full power-off.
2. Power on and immediately test the Fn keys before opening any applications.
3. If they work now but broke again later, disable Fast Startup in **Control Panel → Power Options → Choose what the power buttons do**.
4. Fast Startup preserving a half-loaded hotkey driver is a classic cause of "fixed until reboot" symptoms.

### Fix 6: Check for filter driver corruption

1. Open **Registry Editor** and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e96b-e325-11ce-bfc1-08002be10318}`.
2. Look at the **UpperFilters** value — it should typically contain only `kbdclass`. Third-party entries from old utilities can break the stack.
3. Back up the key (**File → Export**), then remove non-standard entries with care.
4. Restart and test. When in doubt, skip this fix — registry edits are the riskiest step here.

### Fix 7: Test with an external keyboard and check hardware

1. Plug in a USB keyboard and test its function keys — if they work, Windows is fine and the laptop keyboard is the suspect.
2. Test the built-in Fn key alone in the BIOS menus, which bypass Windows entirely.
3. If Fn is dead even in BIOS, the key or keyboard ribbon cable is the fault — reseating the cable or replacing the keyboard is the fix.
4. For a single dead key on an otherwise fine keyboard, remapping software can serve as a workaround while you arrange a repair.

## Closing

Function keys that die with Windows 11 24H2 are a driver-and-settings problem far more often than a hardware one. Reinstall the maker's hotkey package, set Fn behavior in the BIOS, and clear Fast Startup state — those three steps restore the keys on the overwhelming majority of affected laptops. Note which hotkey package version worked; the next feature update may try to replace it again.
