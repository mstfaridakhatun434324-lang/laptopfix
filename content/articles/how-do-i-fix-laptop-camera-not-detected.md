---
title: "How Do I Fix a Laptop Camera Not Detected? — Hardware Detection Guide"
slug: how-do-i-fix-laptop-camera-not-detected
date: 2026-09-02
categories: ["drivers"]
tags: ["camera not detected", "webcam missing", "device manager", "camera driver", "code 45"]
description: "Laptop camera not detected at all — missing from Device Manager and every app? Trace the detection chain from BIOS to driver to hardware."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-camera-not-detected.webp"
faqs:
  - q: "What is the difference between camera not working and camera not detected?"
    a: "Not working means the system sees the camera but it fails — black screens, errors in apps, or a warning icon in Device Manager. Not detected means the system does not see the camera at all: no entry in Device Manager even with hidden devices shown. Not detected is a deeper problem in the detection chain — BIOS, USB enumeration, or hardware — while not working is usually permissions or driver state. The distinction determines which fixes apply."
  - q: "Why would a built-in camera suddenly stop being detected?"
    a: "The most common triggers are Windows updates that break the camera driver stack, BIOS updates that reset the camera to disabled, and the camera's internal USB connection failing to enumerate after sleep. Physical causes include hinge-cable damage from years of opening and closing the lid. Because laptop cameras connect internally via USB, any USB enumeration problem can make the camera vanish exactly like an unplugged external webcam would."
  - q: "Can I still use video calls if the built-in camera is not detected?"
    a: "Yes. A USB webcam bypasses the internal camera entirely and works immediately — plug it in and select it in your video app. Your phone can also serve as a webcam through apps like DroidCam or the manufacturer's phone-link features. These workarounds are worth setting up before an important call rather than troubleshooting the internal camera under time pressure; you can fix the built-in camera afterward at leisure."
  - q: "Does a factory reset fix a camera that is not detected?"
    a: "Rarely, and it is overkill. If the camera is not detected because of driver corruption, a targeted driver reinstall achieves the same result in minutes. If it is not detected because of a BIOS setting or hardware failure, a factory reset changes nothing — the camera will still be missing after hours of reinstalling. Only consider a reset after you have checked BIOS, reinstalled drivers, and tested with a live USB environment, and even then it seldom helps detection issues."
---

"Camera not detected" is the deeper, scarier cousin of "camera not working." No app lists it. Device Manager shows nothing, even with hidden devices revealed. It is as if the camera was never installed. This guide treats it as what it is: a detection-chain problem. Somewhere between the camera module, the BIOS, the USB bus, and Windows, the signal is getting lost — and each link has a specific test.

Laptop cameras are USB devices internally. That single fact explains most detection failures: everything that can make a USB device vanish — enumeration bugs, power states, disabled ports — can make your built-in camera vanish too.

## Why this happens

- **Camera disabled in BIOS:** Many business laptops have a BIOS-level camera toggle. BIOS updates reset it to disabled without warning.
- **USB enumeration failure:** The camera connects via an internal USB bus. Enumeration bugs after sleep or updates make it vanish like an unplugged device.
- **Corrupted camera driver stack:** A broken driver can prevent the device from enumerating at all, not just from working — Device Manager shows nothing, not even an error.
- **Windows update breaking the USB video class driver:** Feature updates occasionally damage the shared USB Video Class driver that all laptop cameras depend on.
- **Hinge cable damage:** The camera cable runs through the display hinge, flexing thousands of times. A broken conductor kills detection completely and permanently.
- **Camera module failure:** The module itself can die — rare, but it happens, usually after liquid exposure or physical trauma to the lid.
- **Fast Startup preserving bad state:** Hybrid shutdown preserves USB device state across "shutdowns," so an enumeration failure survives what looks like a full power cycle.
- **Conflicting camera software:** Virtual camera drivers and old webcam utilities can interfere with enumeration of the physical device.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check BIOS for the camera toggle

The firmware gate that overrides everything else.

1. Restart and enter BIOS/UEFI setup (usually **F2** or **Del**).
2. Look under **Security** (often **I/O Port Access** on HP/Lenovo business machines) or **Devices** for **Integrated Camera** or **Webcam**.
3. Make sure it is **Enabled**. If a recent BIOS update preceded the problem, also choose **Load Optimized Defaults** first, then re-enable the camera.
4. Save, exit, and check Device Manager again. A camera that appears after this was never broken — firmware had it switched off. Permission-level camera issues, by contrast, are covered in our [camera not working guide](/articles/what-to-do-if-laptop-camera-not-working/).

### Fix 2: Force USB re-enumeration with a true power cycle

Clear the stuck USB state that hides the camera.

1. Shut down fully — then disable **Fast Startup** first if you have not already (**Control Panel → Power Options → Choose what the power buttons do**), because it otherwise defeats this fix.
2. Unplug the charger, hold the power button for 30 seconds to drain residual power, then boot.
3. Open **Device Manager → Action → Scan for hardware changes** and watch the **Cameras** / **Imaging devices** section.
4. If the camera appears, the problem was enumeration state. If it appears with an error code, continue to Fix 4 — you have moved from "not detected" to "detected but broken," which is progress.

### Fix 3: Reveal hidden devices and clear ghost entries

Stale device records can block fresh detection.

1. In Device Manager, enable **View → Show hidden devices**.
2. Expand **Cameras**, **Imaging devices**, and **Universal Serial Bus controllers**. Look for grayed-out camera entries or **Unknown USB Device** entries.
3. Right-click any ghost camera entries and choose **Uninstall device**. Also uninstall grayed-out **USB Composite Device** entries that might be the camera's parent.
4. **Action → Scan for hardware changes**. Windows now attempts a clean enumeration without the stale records interfering.

### Fix 4: Rebuild the camera driver stack

When the driver itself prevents detection.

1. Download the camera driver for your exact model from the manufacturer's support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. In Device Manager, uninstall every camera-related entry found (including hidden ones), checking **Delete the driver software** where offered.
3. Restart, then install the downloaded driver package before opening any camera app.
4. Check **Device Manager → Cameras** for a clean entry with no warning icon. If Windows immediately replaces your driver with its own on reboot, temporarily disconnect from the internet during the install, then block the driver update.

### Fix 5: Repair the USB Video Class driver

The shared driver all laptop cameras depend on.

1. In Device Manager, expand **Universal Serial Bus controllers** and look for **USB Composite Device** entries — the camera usually hides behind one.
2. Right-click each composite device → **Properties → Details → Hardware Ids** to identify which one is the camera (look for `USB\VID_` entries matching camera vendors).
3. If the camera's parent shows a warning, uninstall it (not delete) and scan for hardware changes — Windows rebuilds the USB Video Class binding.
4. As a broader repair, run **Settings → Windows Update** and install all optional driver updates, then re-check. Corrupted system USB drivers sometimes need the full update pass to heal.

### Fix 6: Test with a live environment and check the hinge

Separate software from hardware definitively.

1. Boot a Linux live USB and check whether the camera appears (most live environments list it in settings or via `lsusb`). Visible in Linux means Windows is the problem — revisit Fixes 2–5.
2. Invisible in Linux too means hardware or BIOS. Re-verify the BIOS toggle from Fix 1 very carefully — some BIOS versions hide the camera setting in non-obvious menus.
3. Consider the hinge: does the camera ever flicker into detection when you move the lid? Intermittent detection tied to lid position is the signature of a damaged hinge cable.
4. For hinge-cable failure, the repair is a cable or display-assembly replacement — a shop job on most modern thin laptops. Meanwhile, a USB webcam restores full video-call capability immediately, as detailed in our [camera troubleshooting guide](/articles/troubleshoot-laptop-camera-not-detected/).

### Fix 7: Remove conflicting software and reset the camera app

Last software layer before accepting a hardware verdict.

1. Uninstall virtual camera software (OBS Virtual Camera, Snap Camera, XSplit) and old webcam utilities — their filter drivers can suppress the physical device.
2. Reset the Windows Camera app: **Settings → Apps → Installed apps → Camera → Advanced options → Reset**.
3. Check **Settings → Privacy & security → Camera** — while permissions do not affect detection, a corrupted permission state combined with driver issues occasionally confuses the stack. Toggle camera access off and on.
4. If the camera remains invisible in Device Manager, hidden view, Linux, and BIOS-verified-enabled, the module or its cable has failed. Document everything you tried — it saves diagnostic time at the repair shop.

## Closing

"Not detected" sounds terminal, but it is usually a gate that is closed rather than a device that is dead: a BIOS toggle, a stuck USB enumeration, or a corrupted driver stack. The diagnostic that matters most is cross-environment visibility — if Linux sees it, Windows can be fixed; if nothing sees it, the hinge cable is the prime suspect. Either way, you now know exactly which kind of problem you have, and that is more than half the battle.
