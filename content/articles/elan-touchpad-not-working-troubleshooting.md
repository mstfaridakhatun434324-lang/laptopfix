---
title: "ELAN Touchpad Not Working? Troubleshoot It Like a Technician"
slug: elan-touchpad-not-working-troubleshooting
date: 2026-09-11
categories: ["drivers"]
tags: ["elan", "touchpad", "trackpad", "input driver", "troubleshooting"]
description: "ELAN touchpad dead, laggy, or missing gestures? Diagnose whether it's the driver, a setting, or Windows Update — and restore full touchpad function."
thumbnail: "/images/thumbs/elan-touchpad-not-working-troubleshooting.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows Update commonly replaces the manufacturer's ELAN driver with a generic Microsoft one, or installs an incompatible ELAN version. The generic driver provides basic mouse movement but kills multi-touch gestures and sometimes the touchpad entirely. Reinstalling the laptop maker's ELAN driver package is the fix."
  - q: "My touchpad works but gestures don't. Is the driver broken?"
    a: "Not broken — just generic. Basic movement comes from the fallback PS/2-compatible driver, while gestures need the full ELAN precision driver. If movement works but two-finger scroll and gestures don't, you need the proper ELAN driver, not a hardware repair."
  - q: "Can the touchpad be disabled in BIOS?"
    a: "Yes — many laptops have a touchpad toggle in BIOS/UEFI, and some have Fn-key shortcuts that disable it. If the touchpad is completely dead and missing from Device Manager, check both the Fn key and BIOS before assuming hardware failure."
  - q: "Does an external mouse disable the ELAN touchpad?"
    a: "There's a Windows setting for exactly that: 'Leave touchpad on when a mouse is connected.' If your touchpad dies whenever you plug in a mouse, uncheck the auto-disable option in Settings > Bluetooth & devices > Touchpad rather than troubleshooting the driver."
---

ELAN touchpads are in millions of laptops — ASUS, Lenovo, Acer, MSI, and others — and they fail in distinctive ways: completely dead after updates, alive but gesture-less, erratic cursor jumps, or a touchpad that works until you plug in a mouse. The pattern tells you which layer broke: driver, setting, or hardware. This guide reads those patterns in order.

One useful framing: the ELAN driver is really two drivers in one — a basic fallback that moves the cursor, and the full precision driver that enables gestures. Knowing which one is active explains most symptoms instantly.

## Why this happens

- **Windows Update replaced the ELAN driver.** The classic cause. The generic replacement moves the cursor but kills gestures — or kills the touchpad entirely on some models.
- **The touchpad is disabled by Fn key or setting.** An accidental **Fn + F-key** press disables the touchpad with no on-screen warning on some laptops.
- **"Disable when mouse is connected" is on.** Plugging in a USB mouse silently kills the touchpad by design.
- **Corrupted ELAN driver install.** Partial updates leave the driver in a state where Device Manager shows errors or the touchpad behaves erratically.
- **Precision touchpad vs. ELAN driver conflict.** Windows 10/11 prefers Microsoft precision drivers; fighting between precision and ELAN drivers produces erratic behavior. Compare [Synaptics' version of this conflict](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/).
- **BIOS-level disable.** A firmware toggle can switch the touchpad off below the OS level.
- **Hardware failure.** Loose ribbon cable or dead touchpad module — the last suspect, presenting as total death across operating systems.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the Fn key and the mouse-connected setting

The 60-second fixes.

1. Press **Fn + the touchpad key** (look for a touchpad icon on F5–F9 typically). Try it twice — some laptops toggle with no indicator.
2. Go to **Settings** > **Bluetooth & devices** > **Touchpad**. Make sure the **Touchpad** toggle is **On**.
3. Expand the touchpad settings and **uncheck** "Leave touchpad on when a mouse is connected" — actually, verify its state: if you want the touchpad to work alongside a mouse, this box must be **checked**.
4. Unplug all external mice and retest. If the touchpad springs to life, the auto-disable setting was the cause.

### Fix 2: Determine which driver is actually active

Diagnosis that directs everything downstream.

1. Open **Device Manager** > **Human Interface Devices** and **Mice and other pointing devices**. Look for **ELAN Input Device** or similar.
2. If you see only **PS/2 Compatible Mouse** and no ELAN entry, the fallback driver is active — gestures are impossible until the real driver is installed (Fix 3).
3. If the ELAN device shows a **yellow warning**, note the error code and proceed to Fix 3.
4. If no touchpad device appears at all, check **View** > **Show hidden devices**, then check BIOS (Fix 5).

### Fix 3: Reinstall the manufacturer's ELAN driver

The core repair.

1. Download the **touchpad/ELAN driver** for your exact model from the laptop manufacturer's support page — not from ELAN directly, not from Windows Update.
2. In Device Manager, right-click the ELAN device (or the PS/2 fallback) > **Uninstall device**, checking "Attempt to remove the driver" if offered.
3. Restart the laptop.
4. Install the downloaded driver **as administrator**. Restart again when prompted.
5. Verify in Device Manager that the ELAN device is present without warnings, then test gestures: two-finger scroll, three-finger swipe.

### Fix 4: Configure gestures and sensitivity properly

For touchpads that work but misbehave.

1. Go to **Settings** > **Bluetooth & devices** > **Touchpad**. Set **Touchpad sensitivity** to **Medium** or **High** if the cursor feels dead, **Low** if it jumps erratically from palm contact.
2. Review the **Gestures** sections — enable two-finger scroll, three-finger actions, and tap settings to your preference. Driver reinstalls reset these.
3. If the cursor jumps while typing, increase the **palm rejection** / touchpad sensitivity threshold, or enable "disable touchpad while typing" if your driver offers it.
4. Test on a clean, dry surface — moisture and dirt on the touchpad cause genuinely erratic behavior that no driver fixes.

### Fix 5: Check BIOS and reset to defaults

For touchpads invisible to Windows.

1. Reboot into **BIOS/UEFI**. Find the **Touchpad**, **Internal Pointing Device**, or similar setting and set it to **Enabled**.
2. While there, note whether there's a **precision touchpad mode** toggle — some BIOS versions let you choose between ELAN and precision modes.
3. Save and boot into Windows. Check Device Manager again.
4. If the touchpad appears in BIOS diagnostics (many laptops have a built-in hardware test) but not in Windows, it's purely a Windows driver problem — revisit Fix 3 with different driver versions.

### Fix 6: Block Windows Update from breaking it again

ELAN drivers are repeat victims of driver replacement.

1. Once working, set **Device Installation Settings** to **No** (System > About > Advanced system settings > Hardware).
2. Use the **Show or hide updates** troubleshooter to hide touchpad driver updates.
3. Note the working driver version from Device Manager's Driver tab for future comparison.
4. Our companion guide on [keeping the ELAN driver stable](/articles/how-to-fix-elan-touchpad-not-working-in-windows-11-24h2/) covers additional persistence techniques.

### Fix 7: Verify hardware as the last step

Only after software is exhausted.

1. Boot a **Linux live USB** and test the touchpad. Working in Linux = Windows driver issue, full stop.
2. Dead in Linux too? If comfortable, open the laptop and reseat the touchpad's ribbon cable — they can work loose, especially after drops.
3. Check for a swollen battery pressing upward on the touchpad — a common cause of physical touchpad death and a safety issue requiring immediate battery replacement.
4. Touchpad module replacement is usually inexpensive as a part; the labor depends on how buried it is in your model.

The official [Windows support pages](https://support.microsoft.com/en-us/windows) cover touchpad settings basics that complement these driver steps.

## Closing

ELAN touchpad failures follow a script: accidental disable, then driver replacement by Windows Update, then configuration. Check the Fn key and the mouse-connected setting, identify which driver is actually active, reinstall the manufacturer's ELAN package, configure gestures, and then lock Windows Update out of "fixing" it again. The touchpad is almost certainly fine — it's the software around it that needs putting back in order.
