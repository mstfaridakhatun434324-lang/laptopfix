---
title: "How to Fix ELAN Touchpad Not Working on Windows 11"
slug: how-to-fix-elan-touchpad-not-working-on-windows-11
date: 2026-10-02
categories: ["drivers"]
tags: ["elan touchpad", "touchpad not working", "windows 11", "elan driver", "precision touchpad"]
description: "ELAN touchpad not working on Windows 11? Fix dead cursors, missing gestures, and driver errors with 7 proven ELAN repairs."
thumbnail: "/images/thumbs/how-to-fix-elan-touchpad-not-working-on-windows-11.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows 11 update?"
    a: "Windows 11 feature updates commonly replace the manufacturer's ELAN driver with a generic Microsoft precision-touchpad driver that does not speak the ELAN hardware's dialect, leaving the cursor dead or gestures broken. The fix is reinstalling the ELAN driver package from your laptop maker's support site. This affects Acer, ASUS, Lenovo, and MSI machines that ship with ELAN touchpad hardware."
  - q: "How do I know if my touchpad is ELAN or Synaptics?"
    a: "Open Device Manager, expand Human Interface Devices or Mice and other pointing devices, and look for entries containing ELAN or Synaptics in the name. You can also check Settings, Bluetooth and devices, Touchpad — ELAN hardware often shows an ELAN tab in the legacy Mouse control panel. Download only the driver matching your actual hardware; the wrong vendor's package will not install or will break the device."
  - q: "Should I switch my ELAN touchpad to a precision touchpad driver?"
    a: "If your laptop maker offers a precision touchpad driver for your model, it usually improves gesture smoothness and gives you Windows' native touchpad settings. But forcing a precision driver onto ELAN hardware it was not built for can kill the touchpad entirely. Only use a precision driver package your manufacturer published for your exact model."
  - q: "My ELAN touchpad works but gestures don't — what's wrong?"
    a: "The cursor moving while gestures fail means the basic PS/2-compatible driver loaded but the ELAN gesture driver did not. Reinstall the full ELAN Smart-Pad or ELAN Input Device driver package from your laptop maker's site, not just the base driver Windows offers. Also check the ELAN control panel — individual gestures can be toggled off there."
---

An ELAN touchpad failure is unmistakable: the cursor freezes, two-finger scroll vanishes, or the touchpad settings page in Windows looks empty. ELAN Microelectronics makes the touchpad hardware in a huge swath of Acer, ASUS, Lenovo, and MSI laptops, and its driver is fussier than most — Windows 11 updates love to replace it with a generic driver that leaves the hardware half-dead.

The repairs below are ordered from the instant checks (is it just toggled off?) through the driver reinstall that fixes most cases, to the BIOS and hardware verdicts. Keep a USB mouse handy — you'll need it for navigation while the touchpad is down.

## Why this happens

- **Windows Update replaced the ELAN driver.** A generic precision driver that doesn't match the ELAN hardware.
- **Touchpad disabled via Fn key or settings.** Accidentally toggled off — embarrassingly common.
- **ELAN service or startup entry killed.** "Debloat" tools disabling the ELAN service the gestures depend on.
- **Corrupt ELAN driver installation.** Partial update leaving the driver in a broken state.
- **BIOS touchpad mode changed.** Advanced vs. Basic mode mismatch after a BIOS update or reset.
- **Fast Startup driver conflict.** The ELAN driver failing to initialize on hybrid boot.
- **Dead touchpad hardware.** Ribbon cable or sensor failure — the last resort diagnosis.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the touchpad toggle

Thirty seconds that fix an embarrassing number of "dead" touchpads.

1. Look for the touchpad **Fn key** — usually Fn+F7, Fn+F9, or a key with a touchpad icon — and press it.
2. Go to **Settings > Bluetooth & devices > Touchpad** and make sure the **Touchpad** toggle is **On**.
3. While there, check **"Leave touchpad on when a mouse is connected"** if you use both.
4. If the Touchpad settings page is missing entirely, Windows isn't seeing the hardware — skip to Fix 4.
5. Restart the laptop after toggling — the ELAN driver sometimes needs a boot to pick up the state change.

### Fix 2: Re-enable the ELAN device in Device Manager

The device may simply be disabled at the driver level.

1. Open **Device Manager** (Windows + X).
2. Look under **Human Interface Devices** and **Mice and other pointing devices** for **ELAN Input Device**, **ELAN Smart-Pad**, or similar.
3. If it shows a down-arrow icon, right-click and choose **Enable device**.
4. If it's missing entirely, click **View > Show hidden devices** — a grayed-out ELAN entry means the driver isn't loading (Fix 4).
5. Check for an **ELAN** tab in the legacy **Mouse** control panel (search "mouse" in Start) — its presence confirms the ELAN driver is at least partially alive.

### Fix 3: Restart the ELAN service

The gestures and advanced features depend on ELAN's background service.

1. Press **Windows + R**, type `services.msc`, press Enter.
2. Look for **ELAN Service** (sometimes "ETDService").
3. Set **Startup type** to **Automatic** and **Start** it if it's stopped.
4. Check **Task Manager > Startup apps** — re-enable any **ELAN** or **ETDCtrl** entry that an optimizer disabled.
5. Restart and test two-finger scroll and gestures, not just cursor movement.

### Fix 4: Reinstall the ELAN driver from your laptop maker

The core fix — replace the generic driver with the manufacturer's ELAN package.

1. Go to your laptop maker's support site (Acer, ASUS, Lenovo, MSI) and find the **touchpad/ELAN driver** for your exact model and Windows 11.
2. In **Device Manager**, right-click the ELAN device, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart — Windows will load a basic fallback.
4. Run the manufacturer's ELAN installer as administrator, then restart again.
5. Verify: **Settings > Bluetooth & devices > Touchpad** should now show full gesture options, and the ELAN tab should appear in the Mouse control panel.

If your machine actually has Synaptics hardware instead, the equivalent repair is covered in [how to fix Synaptics touchpad not working in Windows 11 24H2](/articles/how-to-fix-synaptics-touchpad-not-working-in-windows-11-24h2/).

### Fix 5: Check the BIOS touchpad setting

A BIOS update or reset can flip the touchpad into a mode Windows 11 mishandles.

1. Restart and enter **BIOS/UEFI** (usually F2 or Del during boot).
2. Look under **Advanced** or **Main** for **Touchpad** or **Internal Pointing Device**.
3. If it offers **Advanced** vs. **Basic** modes, try **Advanced** first (full feature set), then **Basic** if Advanced fails — Basic presents the touchpad as a simple PS/2 mouse that always works.
4. Save and exit, boot into Windows, and let the driver redetect.
5. If you recently updated the BIOS, also reinstall the ELAN driver (Fix 4) — BIOS updates sometimes change the hardware ID the driver matches against.

### Fix 6: Disable Fast Startup

Fast Startup's hybrid boot can prevent the ELAN driver initializing properly.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup**, click Save changes.
4. Shut down completely (not restart), then power on.
5. If the touchpad now works on cold boot but not on restart, Fast Startup was the culprit — leave it off; the boot-time cost on an SSD is a few seconds.

Microsoft documents startup and driver behavior on [Windows support](https://support.microsoft.com/en-us/windows) if you want the official background.

### Fix 7: Test in BIOS and conclude hardware

The definitive hardware test takes two minutes.

1. Restart into **BIOS/UEFI** — most BIOS screens support the touchpad for navigation.
2. If the cursor moves in BIOS but not in Windows, it's 100% a software/driver problem — repeat Fix 4 with a different driver version (try the Windows 10 package in compatibility mode).
3. If the touchpad is dead in BIOS too, the hardware has failed — usually the ribbon cable connecting the touchpad to the motherboard, sometimes the sensor itself.
4. Reseating the ribbon cable is a 15-minute job for a repair shop; touchpad replacement parts are model-specific and cheap.
5. As a workaround, a USB mouse or Windows' **Mouse Keys** (Settings > Accessibility > Mouse) keeps the laptop usable meanwhile.

## Closing

ELAN touchpad failures on Windows 11 are a driver story in the overwhelming majority of cases — the Fn-key toggle and the manufacturer driver reinstall resolve them. Work the sequence, keep that USB mouse nearby, and only conclude hardware failure after the BIOS test proves the touchpad dead outside of Windows. Touchscreen issues follow a similar driver logic — see [how to fix touchscreen not working on laptop in Windows 11 24H2](/articles/how-to-fix-touchscreen-not-working-on-laptop-in-windows-11-24h2/).
