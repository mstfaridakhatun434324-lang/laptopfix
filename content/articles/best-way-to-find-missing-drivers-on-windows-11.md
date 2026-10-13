---
title: "The Best Way to Find Missing Drivers on Windows 11"
slug: best-way-to-find-missing-drivers-on-windows-11
date: 2026-09-20
categories: ["drivers"]
tags: ["missing drivers", "windows 11", "unknown device", "driver update", "device manager"]
description: "Missing drivers on Windows 11? Use Device Manager, Windows Update optional updates, and manufacturer tools to identify and install every missing driver."
thumbnail: "/images/thumbs/best-way-to-find-missing-drivers-on-windows-11.webp"
faqs:
  - q: "How do I know which drivers are missing on Windows 11?"
    a: "Open Device Manager and look for entries with yellow warning triangles, especially under Other devices labeled Unknown device. Then check Settings, Windows Update, Advanced options, Optional updates, where Windows lists drivers it found but did not install. Between those two views you can identify nearly every missing driver on the system."
  - q: "Is it safe to install all drivers from Windows Update optional updates?"
    a: "Mostly yes, but with caution. Optional driver updates from Microsoft are tested, yet they occasionally install generic versions that lack manufacturer features or break working hardware. Install them one category at a time, starting with anything flagged as missing, and skip graphics and network drivers if your current ones work fine."
  - q: "What is the hardware ID and how does it help find drivers?"
    a: "Every device carries a hardware ID like PCI\\VEN_8086&DEV_..., where VEN identifies the vendor and DEV the device. Copying this ID into Device Manager's Details tab and searching it reveals exactly what the unknown device is, which lets you download the precise driver instead of guessing from vague names like Unknown device."
  - q: "Should I use third-party driver updater programs?"
    a: "No. Third-party driver updaters are a frequent source of wrong, outdated, or bundled-junk drivers, and some are outright malware vectors. Stick to Windows Update, your laptop manufacturer's support page, and component makers like Intel, NVIDIA, and AMD. Those three sources cover every legitimate driver you will ever need."
---

A fresh Windows 11 install — or a major update gone sideways — can leave your laptop with missing drivers: unknown devices in Device Manager, hardware that doesn't work, and features like the fingerprint reader or special keys sitting dead. The challenge isn't installing drivers; it's figuring out *which* drivers are missing when Windows just shrugs and labels things "Unknown device."

This guide gives you a systematic identification method. You'll learn to read Device Manager's clues, extract hardware IDs that name the mystery device precisely, and pull the right driver from the right source. No guessing, no shady driver-updater tools.

## Why this happens

- **Clean installs lack vendor drivers:** A fresh Windows 11 install includes generic drivers but not the manufacturer-specific packages for hotkeys, card readers, and sensors.
- **Feature updates drop incompatible drivers:** Major Windows updates can remove drivers they deem incompatible, leaving the hardware driverless afterward.
- **Optional updates never installed:** Windows finds many drivers but files them under Optional updates, which users routinely ignore — so the drivers sit there unfetched.
- **Manufacturer utilities missing:** Control apps for RGB, fan curves, and battery limits aren't drivers exactly, but their absence makes hardware appear broken.
- **Chipset driver not installed:** Without the chipset package, whole device categories (SMBus, GPIO, serial IO) show as unknown because Windows can't classify them.
- **BIOS handoff failures:** Some devices only enumerate correctly if the BIOS exposes them properly; a BIOS quirk can leave hardware permanently "unknown."
- **Ghost entries masking the real device:** Stale hidden entries can prevent Windows from detecting the actual hardware cleanly, perpetuating the "missing" status.
- **Wrong Windows edition or build:** Very new hardware on an older Windows 11 build may simply have no inbox driver available, showing as unknown until the OS is updated.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Survey Device Manager for the damage

1. Press **Win + X** and open **Device Manager**.
2. Expand every category and note all entries with yellow warning triangles, plus the **Other devices** category where unknown hardware collects.
3. Count the unknowns — one or two is a quick fix; a dozen after a clean install means you should install the chipset package first (Fix 4).
4. For each unknown, right-click → **Properties** and check the **Device status** box for clues like "The drivers for this device are not installed (Code 28)."
5. Take a screenshot or write down the list. A clear inventory keeps you from chasing the same device twice, and [checking driver versions](/articles/best-way-to-check-driver-version-in-device-manager/) later confirms each fix landed.

### Fix 2: Check Windows Update optional updates first

1. Open **Settings → Windows Update → Advanced options → Optional updates**.
2. Expand **Driver updates** and review the list — Windows has already matched these to your hardware.
3. Select the drivers for your unknown devices and click **Download & install**.
4. Restart after installation and recheck Device Manager.
5. This resolves the easy cases (common network, audio, and Bluetooth chips) in minutes. For anything Windows can't identify, continue to hardware ID detective work. Keeping [drivers current through Windows Update](/articles/best-way-to-update-drivers-on-windows-11/) afterward prevents repeat gaps.

### Fix 3: Identify unknown devices by hardware ID

1. In Device Manager, right-click an unknown device → **Properties → Details** tab.
2. Change the property dropdown to **Hardware Ids** and copy the top value (e.g., `PCI\VEN_8086&DEV_9D71`).
3. The **VEN** code names the vendor (8086 = Intel, 10DE = NVIDIA, 1022 = AMD) and **DEV** names the device.
4. Search the web for the full ID string — device databases will tell you exactly what the hardware is (e.g., "Intel Serial IO I2C Host Controller").
5. With the true name known, download the driver from the vendor or laptop maker instead of guessing. This technique also cracks [unknown device](/articles/best-way-to-fix-unknown-device-in-device-manager/) cases that resist every automatic method.

### Fix 4: Install the chipset driver package early

1. Go to your laptop maker's support page ([Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en)) and download the **chipset driver** for your exact model and Windows 11.
2. Install it and restart. The chipset package contains the drivers that let Windows classify SMBus controllers, GPIO, serial IO, and management engines.
3. Recheck Device Manager — on a fresh install, the chipset package alone often clears half the unknown entries.
4. Intel users can alternatively use [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect the right chipset components.
5. Treat the chipset driver as foundation work: installing device-specific drivers before it can fail because Windows doesn't yet understand the bus the device sits on.

### Fix 5: Pull drivers from the manufacturer's support page by model

1. Find your exact model number (sticker on the bottom, or **System Information** → System Model).
2. Visit Dell Support or HP Support (linked in Fix 4 above), enter the model, and open **Drivers & Downloads**.
3. Filter by **Windows 11** and work through the categories matching your unknowns: network, audio, card reader, sensors, and input devices.
4. Install in this order: chipset, then network (so you have connectivity), then everything else.
5. Manufacturer packages include the customizations generic drivers lack — hotkey behavior, power profiles, and hardware-specific features. For machines without internet, the [offline driver install method](/articles/best-way-to-install-drivers-without-internet/) covers the USB-transfer workflow.

### Fix 6: Use component-maker tools for graphics and wireless

4. These tools identify hardware Windows couldn't and install the full feature driver, not just a basic display or network stub. Use the Intel, NVIDIA, or AMD download pages linked earlier in this guide.

### Fix 7: Clear ghosts and force re-detection

1. In Device Manager, enable **View → Show hidden devices**.
2. Uninstall greyed-out ghosts of the hardware you're trying to fix.
3. Click **Action → Scan for hardware changes** to trigger fresh detection.
4. If Windows now prompts for a driver or auto-installs one, the ghost was blocking detection.
5. For devices that appear and vanish (docks, USB hardware), this cleanup is often the difference between "missing" and "working." The [OEM manual install guide](/articles/best-way-to-install-oem-drivers-manually/) picks up from here when you have an INF file but Windows won't take it.

### Fix 8: Update Windows itself, then install vendor utilities

1. Run **Settings → Windows Update** and install all pending updates — newer builds carry inbox drivers for newer hardware.
2. After the OS is current, recheck for remaining unknowns; some clear up with the build update alone.
3. Install the manufacturer's system utilities (Dell SupportAssist, HP Support Assistant, Lenovo Vantage, MyASUS) — these detect missing drivers for your exact model automatically.
4. These utilities also install the control apps for special keys, lighting, and battery features that aren't drivers but complete the hardware experience.
5. Do a final Device Manager sweep. A clean tree with no warnings is the goal; anything left at this point deserves the hardware-ID treatment from Fix 3 or a [manual OEM install](/articles/best-way-to-install-oem-drivers-manually/).

## Closing

Finding missing drivers on Windows 11 is detective work, not guesswork: inventory the unknowns, let optional updates handle the easy ones, identify the rest by hardware ID, and source drivers from the manufacturer and component makers in that order. Avoid third-party driver updaters entirely — they create more missing-driver situations than they solve. Once the tree is clean, keep it that way with regular optional-update checks.
