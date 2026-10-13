---
title: "Function Keys Not Working? Step-by-Step Repair Guide"
slug: how-to-fix-function-keys-not-working-step-by-step
date: 2026-09-06
categories: ["drivers"]
tags: ["function keys", "fn key not working", "hotkey driver", "keyboard troubleshooting", "windows 11"]
description: "Function keys dead on your laptop? Follow this step-by-step repair guide — Fn lock, BIOS settings, and hotkey driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-function-keys-not-working-step-by-step.webp"
faqs:
  - q: "Why do my function keys do nothing when I press them?"
    a: "The top-row keys depend on two layers: the base keyboard driver handling F1–F12 scancodes, and the manufacturer's hotkey software implementing the Fn combinations for brightness, volume, and Wi-Fi. When Fn combos die but plain F-keys work, the hotkey software is missing or broken — usually removed by an update or killed by an optimizer tool. Reinstalling the maker's hotkey package is the fix."
  - q: "How do I turn Fn lock on or off?"
    a: "Press Fn + Esc on most laptops — an on-screen indicator or LED confirms the toggle. Some models use Fn + Caps Lock or a dedicated Fn Lock key. Fn lock switches the top row between media/brightness shortcuts and classic F1–F12 behavior. If nothing happens when you press the combination, the hotkey software that implements it isn't running — see the driver fixes below."
  - q: "Where is the function key setting in BIOS?"
    a: "Restart and enter BIOS/UEFI (F2, Del, or F10), then look under Advanced, System Configuration, or Keyboard for Function Key Behavior, Action Keys Mode, or Hotkey Mode. This sets the default: multimedia shortcuts versus classic F-keys. BIOS updates sometimes reset it, so recheck this setting whenever function keys misbehave after a firmware update."
  - q: "Do I need manufacturer software for function keys to work?"
    a: "For the Fn combinations — yes. Plain F1–F12 work with Windows' built-in keyboard driver, but brightness, volume, microphone mute, airplane mode, and other Fn combos are implemented by the laptop maker's utility (Lenovo Vantage components, Dell services, HP Hotkey Support, ASUS ATK package, Acer Quick Access). Without that software installed and running, those combos do nothing."
---

When the function keys stop working, the pattern matters more than the symptom. If the plain F1–F12 keys work but the Fn combinations (brightness, volume, Wi-Fi) don't, your keyboard is fine — the manufacturer's hotkey software layer is what's broken. If nothing on the top row works at all, the base keyboard driver or the Fn-lock state is suspect. This guide walks you through the diagnosis and repair step by step, from the instant toggles to the driver reinstall.

You won't need any tools — just your keyboard and about fifteen minutes.

## Why this happens

- **Fn lock in the wrong state.** The keys work but send F1–F12 instead of the Fn functions — the most common "failure."
- **Hotkey utility missing or broken.** The maker's Fn software removed by an update or never reinstalled after a reset.
- **Hotkey service disabled at startup.** Optimizer and debloat tools killing the background service.
- **BIOS function-key behavior reset.** A firmware update flipping the default mode.
- **Base keyboard driver corruption.** The underlying driver not passing key events correctly.
- **Fast Startup skipping initialization.** The hotkey utility failing to load on hybrid boot.
- **Sticky/Filter Keys interference.** Accessibility features swallowing key combinations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Diagnose which layer is broken

Two minutes of testing that directs everything after.

1. Press a top-row key **alone** (e.g., F5) — note what happens (nothing? F5 refresh? brightness change?).
2. Press **Fn + the same key** — note what happens now.
3. If **F-keys work but Fn combos don't**: the hotkey software is broken → Fix 4.
4. If **neither works**: check Fn lock (Fix 2) and the base keyboard driver (Fix 5).
5. If **Fn combos work but plain F-keys don't**: Fn lock is simply on — toggle it off (Fix 2) and you're done.

### Fix 2: Toggle Fn lock and check the key itself

The instant fix for the most common report.

1. Press **Fn + Esc** — watch for an on-screen indicator or LED showing the lock state.
2. Alternatives by brand: **Fn + Caps Lock** (some Lenovos), dedicated **Fn Lock** key, or **Fn + F11** on older models.
3. Test in both states — pick the behavior you prefer as default.
4. If pressing **Fn alone** seems to do nothing, that's normal — Fn is a modifier, like Shift; it only acts in combination.
5. If the Fn key is physically stuck or unresponsive, test with an external USB keyboard to isolate hardware.

### Fix 3: Set the BIOS default behavior

Define what the top row does without holding Fn.

1. Restart, enter **BIOS/UEFI** (F2/Del/F10 — varies by maker).
2. Find **Function Key Behavior**, **Action Keys Mode**, or **Hotkey Mode** under Advanced or System Configuration.
3. Choose **Multimedia keys / Action keys** for brightness/volume without Fn, or **Function keys** for classic F1–F12 default.
4. Save, exit, and test in Windows.
5. Recheck this after every BIOS update — firmware updates reset it to the factory default, which may not be what you had.

### Fix 4: Reinstall the manufacturer's hotkey software

The core fix for dead Fn combinations.

1. Identify your maker's package: **Lenovo** (Vantage + system drivers), **Dell** (SupportAssist/quickset services from [Dell Support](https://www.dell.com/support)), **HP** (HP Hotkey Support from [HP Support](https://support.hp.com/us-en)), **ASUS** (ATK Package / System Control Interface), **Acer** (Quick Access).
2. Uninstall the existing/broken version via **Settings > Apps**, restart.
3. Download the current package for your exact model from the maker's support site and install it.
4. Restart again — these utilities initialize at boot.
5. Test **every** Fn combo: brightness up/down, volume up/down/mute, mic mute, airplane mode, sleep, display output.

### Fix 5: Re-enable the hotkey service and startup entries

The software must actually be running.

1. **Task Manager > Startup apps** — re-enable any disabled entries from your laptop maker (Lenovo ImController, Dell services, HP Hotkey, ASUS ATK, Acer Quick Access).
2. **services.msc** — find the maker's hotkey/function-key service, set **Startup type: Automatic**, and **Start** it.
3. Undo any "debloat" script changes that disabled these — those scripts are a top cause of dead Fn keys.
4. Restart and retest the combos.
5. If the service won't stay running, the installation is corrupt — repeat Fix 4's clean reinstall.

### Fix 6: Reinstall the base keyboard driver

When the top row is dead at the hardware-event level.

1. **Device Manager > Keyboards** — right-click **Standard PS/2 Keyboard** (or HID Keyboard Device) > **Uninstall device**.
2. Restart — Windows reinstalls the baseline driver automatically.
3. Test plain F-keys first: working F-keys + dead Fn combos = hotkey software problem (Fix 4), not this.
4. Check **Settings > Accessibility > Keyboard** — turn **Sticky Keys**, **Filter Keys**, and **Toggle Keys** all **Off**.
5. Disable **Fast Startup** (Power Options > Choose what the power buttons do) and do a full shutdown — hybrid boot sometimes skips hotkey initialization.

Microsoft documents keyboard and startup interactions on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Verify versions, remap as fallback, test hardware

Confirm the repair and cover the edge cases.

1. Verify the installed hotkey package version against the maker's support page — make sure the reinstall actually delivered the current build. Our version-checking guide shows how: [how to check driver version in Device Manager in Windows 11 24H2](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).
2. As a workaround for stubborn cases, **Microsoft PowerToys Keyboard Manager** can remap keys to replicate lost Fn functions (e.g., map unused keys to brightness).
3. Test with an **external USB keyboard** — if its function row works fully, the internal keyboard's Fn layer is the problem, not Windows.
4. Boot into **BIOS** — if Fn combos work there (on models with BIOS hotkey tests), it's definitively software.
5. Single dead keys across all environments = keyboard hardware fault, not a driver issue — but a whole dead Fn row is software until proven otherwise.

For the Windows 10-specific edition: [how to fix function keys not working on Windows 10](/articles/how-to-fix-function-keys-not-working-on-windows-10/). Broader keyboard failures: [how to fix keyboard not working on laptop in Windows 11 24H2](/articles/how-to-fix-keyboard-not-working-on-laptop-in-windows-11-24h2/).

## Closing

Function-key failures are a layer cake: Fn lock state on top, BIOS default next, then the maker's hotkey software and its services, with the base keyboard driver at the bottom. Diagnose which layer with the Fix 1 test, repair that layer, and verify every combo afterwards. The hardware is the suspect only when individual keys die everywhere.
