---
title: "Fix an ELAN Touchpad That Stopped Working on Windows 11"
slug: how-do-i-fix-elan-touchpad-not-working
date: 2026-10-08
categories: ["drivers"]
tags: ["elan touchpad", "touchpad not working", "windows 11", "elan driver"]
description: "ELAN touchpad not working on your Windows laptop? Diagnose driver, BIOS, and hardware causes with this step-by-step technician's repair guide."
thumbnail: "/images/thumbs/how-do-i-fix-elan-touchpad-not-working.webp"
faqs:
  - q: "Why did my ELAN touchpad stop working after a Windows update?"
    a: "Windows Update frequently replaces the manufacturer's ELAN driver with a generic Microsoft driver that the ELAN hardware doesn't fully understand. The touchpad may vanish from Device Manager or stop responding to gestures. Reinstalling the laptop maker's original ELAN driver, which you can find through their support page, usually restores normal function."
  - q: "How do I know if the ELAN touchpad is disabled in BIOS?"
    a: "Restart the laptop and enter the BIOS setup, usually by pressing F2, Del, or the brand-specific key at boot. Look under Advanced or Integrated Peripherals for an Internal Pointing Device or Touchpad setting. If it shows Disabled, switch it to Enabled, save, and exit. The touchpad should respond once Windows loads again."
  - q: "Should I use the ELAN driver from Windows Update or my laptop maker?"
    a: "Use the laptop maker's driver first. It is tuned for your exact touchpad firmware and includes the ELAN control panel with gesture settings. Only fall back to the Windows Update driver if the maker's version is years out of date and causes crashes. For most users, the manufacturer's package is the more reliable choice."
  - q: "Can a dead touchpad mean the ribbon cable is loose?"
    a: "Yes. The touchpad connects to the motherboard through a thin ribbon cable that can work loose over time, especially after drops or battery swelling. If Device Manager shows no touchpad device at all and no driver fix helps, a loose or damaged cable is a strong suspect — and that requires opening the chassis or a repair shop visit."
---

An ELAN touchpad that suddenly stops working is deeply frustrating, because the device is your primary input. Most of the time the hardware is perfectly fine — the problem sits in the driver stack, a BIOS toggle, or a Windows setting that quietly disabled the device. Working through this methodically will tell you which one in about thirty minutes.

The technician's approach is simple: confirm whether Windows sees the device at all, check whether it is enabled in every layer (BIOS, Windows, function key), then repair the driver stack from least invasive to most. Start with Device Manager — that single check splits the problem in half: a missing device points to BIOS or hardware, while a present-but-broken device points to drivers or settings. Related reading: [Synaptics touchpads on Windows 11](/articles/how-to-fix-synaptics-touchpad-not-working-on-windows-11/) and [updating drivers on Windows 11](/articles/how-to-update-drivers-on-windows-11-laptop/).

## Why this happens

- **Windows Update replaced the ELAN driver:** A generic "PS/2 Compatible Mouse" or Microsoft precision driver gets installed over the ELAN package, and gestures plus basic movement break.
- **Touchpad disabled by function key:** Most laptops have an Fn + F-key combo (often F5, F7, or F9) that toggles the touchpad. It is easy to trigger accidentally.
- **BIOS toggle set to Disabled:** Some BIOS setups include an Internal Pointing Device option. A BIOS reset or update can flip it off.
- **ELAN driver service crashed or corrupted:** The ETDService background process can fail after a crash or incomplete update, leaving the hardware silent.
- **Fast Startup holding a bad state:** Hybrid shutdown preserves a broken driver state across restarts, so the touchpad stays dead through reboots.
- **Ribbon cable loose or damaged:** The flat cable between touchpad and motherboard works loose after impacts, or gets pinched by a swelling battery.
- **Conflicting third-party drivers:** Touchpad "enhancer" utilities and some remote-desktop tools install filter drivers that fight the ELAN stack.
- **Registry or group policy blocking the device:** Corporate-managed laptops sometimes have policies that disable internal pointing devices for security reasons.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether Windows sees the touchpad

Press Win + X and open Device Manager. Expand "Mice and other pointing devices" and "Human Interface Devices." Look for anything named ELAN, ELAN Input Device, or ELAN PS/2 Port Smart-Pad. If it is there with a yellow warning icon, right-click it, choose Properties, and read the device status — the error code tells you exactly where to focus. If it is missing entirely, note that and move to the BIOS check in Fix 2 before touching drivers.

1. Open Device Manager with Win + X, then M.
2. Expand Mice and other pointing devices and Human Interface Devices.
3. Look for ELAN entries and note any yellow warning icons.
4. Double-click the device and read the Device status text on the General tab.
5. Write down any error code (Code 10, Code 24, Code 39) for later steps.

### Fix 2: Rule out the BIOS and the function key

Restart the laptop and enter BIOS setup with the brand's key (F2 on many Acers and ASUS models, F10 on HP, Enter then F1 on Lenovo). Find the touchpad or Internal Pointing Device setting and make sure it reads Enabled. Save and exit. Then, back in Windows, try the touchpad toggle hotkey — hold Fn and press the key with the touchpad icon, usually on the top function row. Watch for an on-screen notification confirming the touchpad state changes.

1. Restart and press the BIOS key (F2, Del, F10, or Enter+F1) repeatedly.
2. Navigate to Advanced or Integrated Peripherals settings.
3. Set Internal Pointing Device or Touchpad to Enabled.
4. Save with F10 and boot into Windows.
5. Press Fn + the touchpad icon key and watch for the status popup.

### Fix 3: Disable Fast Startup to clear the stuck driver state

Fast Startup preserves kernel and driver state across shutdowns, so a corrupted ELAN driver session survives every hybrid shutdown. Disable it to force a true cold boot before working through the steps below.

1. Open Control Panel and go to Power Options.
2. Click "Choose what the power buttons do" in the left pane.
3. Click "Change settings that are currently unavailable."
4. Uncheck "Turn on fast startup (recommended)" and save changes.
5. Shut down completely, wait ten seconds, then power on.

### Fix 4: Reinstall the ELAN driver from the laptop maker

This is the fix that works most often. Download the touchpad driver package from your laptop manufacturer's support site — for example, [Dell's support portal](https://www.dell.com/support) or [HP's support page](https://support.hp.com/us-en) — matching your exact model. In Device Manager, right-click the ELAN device, choose Uninstall device, and tick "Attempt to remove the driver for this device" if offered. Reboot, then install the downloaded package and reboot again.

1. Download the touchpad driver for your exact model from the maker's support site.
2. In Device Manager, right-click the ELAN device and choose Uninstall device.
3. Tick "Attempt to remove the driver for this device" and confirm.
4. Restart the laptop.
5. Run the downloaded driver installer and restart once more.

### Fix 5: Block Windows from overwriting the working driver

If the touchpad breaks again after every Windows Update, use the "Show or hide updates" troubleshooter or set the device installation policy to stop automatic driver updates for that device. A practical middle ground: pause Windows updates for a week after getting the touchpad working, and install the maker's driver package again if an update replaces it. [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents how to manage optional driver updates.

1. Press Win + R, type `gpedit.msc`, and press Enter (Windows 11 Pro).
2. Go to Computer Configuration, Administrative Templates, Windows Components, Windows Update, Manage updates offered from Windows Update.
3. Enable "Do not include drivers with Windows Updates."
4. Alternatively, use Settings, Windows Update, Advanced options to pause updates temporarily.

### Fix 6: Restart the ELAN service and check for filter conflicts

Open Services (Win + R, `services.msc`) and find ETDService or ELAN Service. If it is stopped, start it and set Startup type to Automatic. Then check Device Manager's View menu, enable "Show hidden devices," and look for duplicate or ghost touchpad entries — uninstall any grayed-out duplicates. Also uninstall any third-party touchpad utilities you do not recognize, since their filter drivers can intercept ELAN input.

1. Open Services with Win + R and `services.msc`.
2. Locate ETDService, start it, and set it to Automatic.
3. In Device Manager, enable View, Show hidden devices.
4. Uninstall any grayed-out duplicate ELAN entries.
5. Remove unfamiliar touchpad "enhancer" programs from Settings, Apps.

### Fix 7: Test with a USB mouse and inspect for hardware faults

Plug in a USB mouse to keep working while you diagnose. Then check for physical causes: does the touchpad area feel raised or spongy (a swelling battery pushes from underneath and can disconnect the cable)? Is there any sign of liquid damage? If Device Manager never shows the ELAN device even with BIOS enabled and the maker's driver installed, the ribbon cable or the touchpad module itself is the likely culprit. At that point, opening the chassis to reseat the cable — or visiting a repair shop — is the remaining option. You can compare symptoms with the [24H2-specific ELAN fix guide](/articles/how-to-fix-elan-touchpad-not-working-in-windows-11-24h2/).

1. Connect a USB mouse so you can keep navigating.
2. Power off and feel the touchpad surface for swelling or looseness.
3. Check the palm rest for liquid residue or warping.
4. If no device appears in Device Manager at all, suspect the ribbon cable.
5. Reseat the cable yourself only if comfortable opening the chassis; otherwise book a repair.

## Closing

Most dead ELAN touchpads come back with a clean driver reinstall or a flipped BIOS toggle — genuine hardware failure is the minority case. Work the fixes in order, keep the working driver version noted somewhere safe, and consider pausing driver updates from Windows Update if the problem keeps recurring after updates. If nothing here revives the touchpad, you have solid evidence for a hardware repair instead of another round of software guesses.
