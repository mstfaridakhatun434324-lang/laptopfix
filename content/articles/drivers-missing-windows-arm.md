---
title: "Drivers Missing on Windows on ARM? How to Find and Fix Them"
slug: drivers-missing-windows-arm
date: 2026-10-19
categories: ["ai-pc"]
tags: ["windows on arm", "drivers", "snapdragon", "device manager", "troubleshooting"]
description: "Drivers missing on Windows on ARM? Learn why some devices show errors in Device Manager and how to get working ARM64 drivers for all your hardware. Start here."
thumbnail: "/images/thumbs/drivers-missing-windows-arm.webp"
faqs:
  - q: "Why does Device Manager show unknown devices on my Snapdragon laptop?"
    a: >
      Unknown devices usually mean Windows couldn't find an ARM64 driver for that hardware. This happens with older peripherals, specialty dongles, and some internal components when the OEM hasn't published an ARM64 driver package. The hardware is fine — the driver simply doesn't exist in ARM64 form.
  - q: "Can I install x64 drivers on Windows on ARM?"
    a: >
      No. Drivers run in the Windows kernel, which cannot be emulated — only native ARM64 drivers load. An x64 driver installer will either refuse to install or install files that Windows can't use. You must find an ARM64-specific driver from the manufacturer.
  - q: "Do printers work on Snapdragon laptops?"
    a: >
      Most modern printers work through universal print drivers (IPP/Mopria) built into Windows 11. Problems arise with old printers that need manufacturer-specific x86 driver software — those utilities won't install on ARM. Check if your printer supports driverless IPP printing.
  - q: "Where do I get ARM64 drivers for my laptop's own hardware?"
    a: >
      From your laptop maker's support page, always. Dell, HP, Lenovo, Microsoft, Samsung, and ASUS all publish ARM64 driver packs for their Snapdragon models. Windows Update also delivers many of them automatically — run it before hunting manually.
---

Open Device Manager on a Snapdragon laptop and you might spot yellow warning triangles on devices you expected to "just work" — a fingerprint reader, an old printer, a USB audio interface, or a specialty dongle. On an x86 laptop you'd download the driver and move on. On Windows on ARM, the story is different: drivers live in the Windows kernel, and the kernel cannot be emulated. If no ARM64 driver exists for that device, no amount of compatibility mode will conjure one.

This is the single hardest limit of Windows on ARM, and it's worth understanding before you waste an afternoon. Applications can be emulated — when they're slow, our guide on [x86 apps running slow on Snapdragon](/articles/x86-app-slow-on-snapdragon/) covers that — but drivers must be native ARM64, full stop. An x64 driver is simply a machine language the kernel can't speak.

The practical picture is better than it sounds: every major laptop maker ships complete ARM64 driver packs for their Snapdragon models, and Windows Update handles most of it silently. The pain concentrates on peripherals — especially older ones — and niche hardware. This guide shows how to identify exactly which driver is missing, where to find a real ARM64 replacement, and what to do when none exists. If you're also unsure whether your programs themselves are native, see [how to check if an app is ARM native](/articles/how-to-check-if-app-is-arm-native/).

## Why this happens

- **Kernel code can't be emulated:** Prism translates user-mode apps, but drivers run in kernel mode where emulation is impossible. Only ARM64-compiled drivers load.
- **Manufacturers deprioritize ARM64:** Smaller hardware vendors never bothered compiling ARM64 drivers for older products, leaving them permanently unsupported.
- **Installer wrappers are x86:** Even when an ARM64 driver exists, the vendor's installer program is often x86-only and crashes — while the actual driver files inside would work fine.
- **Windows Update gaps:** Microsoft's driver catalog covers mainstream hardware well but misses specialty devices, leaving them as "Unknown device" entries.
- **OEM packs lag behind:** Laptop makers bundle ARM64 drivers for built-in hardware, but their support pages update slower than Windows itself, creating temporary mismatches.
- **Legacy bus drivers:** Old FireWire, PCMCIA-era, and 32-bit-only device classes have no ARM64 path at all — the entire driver stack was never ported.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which device is missing its driver

Guessing wastes time. Device Manager tells you precisely what's wrong if you read it properly, including the hardware IDs you need to search for drivers.

1. Press Win + X and open Device Manager.
2. Expand each category and note every device with a yellow triangle or listed under "Other devices."
3. Right-click a problem device > Properties > Details tab > change the dropdown to "Hardware Ids."
4. Copy the top hardware ID (e.g., USB\VID_1234&PID_5678) — this is your search key.
5. Note whether the device is built into the laptop (OEM's responsibility) or a peripheral (peripheral maker's responsibility).

### Fix 2: Get built-in hardware drivers from your OEM

For anything soldered into the laptop — fingerprint reader, cameras, Wi-Fi, audio — the laptop maker is the only correct source. Generic drivers from chip vendors are a fallback, not the first choice.

1. Go to your maker's support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/), or Microsoft/Samsung/ASUS equivalents.
2. Enter your exact model and select Windows 11 on ARM as the OS if there's a choice.
3. Download the driver pack or the specific missing driver (chipset, biometric, camera, audio).
4. Run the installer as administrator and reboot when prompted.
5. Re-check Device Manager — the yellow triangle should be gone.

### Fix 3: Run Windows Update's optional driver updates

Microsoft quietly ships a large ARM64 driver catalog through Windows Update, including drivers your OEM hasn't packaged yet. Many "unknown device" entries resolve here with zero effort.

1. Open Settings > Windows Update > Advanced options > Optional updates.
2. Expand "Driver updates" and check everything listed.
3. Click Download & install, then restart the laptop.
4. After rebooting, open Device Manager and verify the problem devices cleared.
5. Repeat once more — Windows sometimes stages driver updates across two passes.

### Fix 4: Extract drivers from x86 installers manually

Here's a trick technicians use: the vendor's setup program may be x86-only and crash, but the ARM64 .inf and .sys files are often sitting inside it. You can install them by hand.

1. Download the vendor's driver package (even if the installer is x86-only).
2. Extract it with 7-Zip or WinRAR instead of running the setup.exe.
3. In Device Manager, right-click the problem device > Update driver > "Browse my computer for drivers."
4. Point it at the extracted folder (check "Include subfolders").
5. If Windows finds a compatible ARM64 .inf, it installs just the driver — no broken installer needed.

### Fix 5: Use class drivers and universal alternatives

When no vendor ARM64 driver exists, Windows' built-in class drivers cover entire device categories. Printers, audio, storage, and network adapters usually have a generic path.

1. For printers: remove the old printer, then re-add it via Settings > Bluetooth & devices > Printers — choose the IPP/Mopria universal driver.
2. For USB audio: let Windows install its generic USB Audio class driver instead of the vendor suite.
3. For network dongles: the built-in USB NDIS driver handles most adapters.
4. Test full functionality; class drivers cover core features but may skip vendor extras (custom EQ, button mapping).

### Fix 6: Replace or work around permanently unsupported hardware

Some devices will never get ARM64 drivers — typically hardware from vendors that exited the market or 32-bit-only designs. Recognize the dead end and route around it.

1. Check the vendor's site once for any ARM64 or "Windows 11 ARM" driver — if none, stop hunting.
2. Look for a newer replacement device with explicit ARM64/Windows 11 support.
3. For must-keep legacy hardware, consider a cheap x86 mini-PC or print server as a bridge (e.g., share the old printer over the network).
4. Check Microsoft's official guidance on [Windows on ARM support](https://support.microsoft.com/en-us/windows) for the current compatibility picture.
5. When buying new peripherals for a Snapdragon laptop, verify "ARM64 driver available" before purchasing.

## Closing

Missing drivers on Windows on ARM almost always trace back to one fact: kernel drivers can't be emulated, so an ARM64 driver must exist. Work the chain — Device Manager diagnosis, OEM pack, Windows Update optional drivers, manual .inf extraction, then class drivers — and you'll resolve the large majority of cases. For the stubborn remainder, usually old peripherals from vendors who never shipped ARM64 support, replacement beats endless hunting. If a device works but its companion software misbehaves, that's usually an app problem rather than a driver one — see [apps not working on Snapdragon X laptops](/articles/app-not-working-snapdragon-x-laptop/). If a built-in laptop device (camera, Wi-Fi, fingerprint reader) stays broken after the OEM's own driver pack, that's a warranty conversation, not a driver hunt.
