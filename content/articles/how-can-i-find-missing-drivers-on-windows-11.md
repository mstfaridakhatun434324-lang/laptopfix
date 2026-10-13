---
title: "How to Find Missing Drivers on Windows 11 (The Right Way)"
slug: how-can-i-find-missing-drivers-on-windows-11
date: 2026-09-15
categories: ["drivers"]
tags: ["missing drivers", "find drivers windows 11", "unknown device", "device manager"]
description: "Unknown devices in Device Manager? Learn how to find missing drivers on Windows 11 using hardware IDs and official sources — never shady driver tools."
thumbnail: "/images/thumbs/how-can-i-find-missing-drivers-on-windows-11.webp"
faqs:
  - q: "How do I find which drivers are missing in Windows 11?"
    a: "Open Device Manager and look under 'Other devices' for entries labeled Unknown device, or any device with a yellow warning icon. Each flagged entry is a missing or broken driver. Right-click the device, open Properties > Details > Hardware Ids, and copy the VEN/DEV codes — those identify the exact hardware so you can find the correct driver."
  - q: "Is Windows Update enough to find missing drivers?"
    a: "Sometimes, but not reliably. Windows Update carries a large driver library and will install generic drivers for common hardware, but it often lacks the laptop maker's tuned versions and may miss obscure devices entirely. Use Windows Update as the first attempt, then go to the laptop maker's support page for your exact model for the drivers it misses."
  - q: "Are third-party driver updater tools safe?"
    a: "Generally no. Most free driver updaters bundle adware, install wrong or outdated drivers, and charge for the 'fix.' Some have been outright malware vectors. The safe sources are Windows Update, the laptop maker's support page, and the chip maker's site (Intel, AMD, NVIDIA, Realtek). Those three cover every legitimate driver need without the risk."
  - q: "What do I do with an Unknown device I cannot identify?"
    a: "Copy its Hardware IDs from Device Manager and search the PCI vendor/device codes on a lookup site like pcilookup.com, or paste them into a web search. The VEN code identifies the manufacturer and DEV identifies the chip. Once identified, download the driver from the chip maker or laptop maker — never from a random driver-download site."
---

Fresh Windows installs, major updates, and secondhand laptops all produce the same sight: Device Manager showing 'Unknown device' entries or yellow-flagged hardware with no working driver. The machine runs, but something — the fingerprint reader, the SD slot, a sensor — sits idle for want of software. Finding the right driver is a research task, not a guessing task, and there is a correct order that avoids the malware-ridden driver-updater industry entirely.

The method is simple: let Windows try first, then identify each remaining device by its hardware ID, then fetch the driver from the laptop maker or the chip maker. No third-party tools, no sketchy download sites, no registry cleaners with driver features.

## Why this happens

- **Fresh Windows install** without the laptop maker's driver bundle.
- **Major Windows update** dropping support for an older driver.
- **Unknown devices** never had a driver installed at all.
- **Driver files corrupted** by a failed update or disk error.
- **Device disabled at the BIOS level**, so no driver can bind.
- **Wrong-architecture driver** (x86 on x64) failing to install.
- **Chipset driver missing**, hiding devices behind unrecognized controllers.
- **Third-party 'driver cleaner' tools** deleting drivers they should not touch.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let Windows Update try first

Open Settings > Windows Update and check for updates, then look under Advanced options > Optional updates > Driver updates. Windows carries drivers for thousands of devices and will often resolve the obvious ones — network, audio, basic chipset — on its own. Install everything offered, reboot, and recheck Device Manager. Whatever remains flagged after this is what needs manual identification. This step is free, safe, and resolves the easy half of most missing-driver lists.

1. Open Settings > Windows Update and check for updates.
2. Install all driver updates under Optional updates.
3. Reboot and reopen Device Manager.
4. Note which devices remain flagged or unknown.

### Fix 2: Identify each unknown device by hardware ID

For every remaining unknown device, right-click > Properties > Details tab > change the dropdown to Hardware Ids. Copy the top ID — it looks like PCI\VEN_8086&DEV_... The VEN portion is the vendor (8086 = Intel), DEV is the specific chip. Search these codes on pcilookup.com or in a web search to name the device. This turns 'Unknown device' into 'Intel Serial IO I2C Host Controller' or whatever it actually is, which tells you exactly which driver to hunt. Microsoft documents Device Manager in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open the unknown device's Properties > Details > Hardware Ids.
2. Copy the VEN and DEV codes from the top ID.
3. Look them up to identify the exact hardware.
4. Write down each device's real name and vendor.

### Fix 3: Install the laptop maker's driver bundle

With devices identified, go to the laptop maker's support page, enter your exact model, and download the driver bundle for Windows 11. Install in this order: chipset first (it unhides devices behind unrecognized controllers), then storage/serial-IO, then graphics, network, audio, and the rest. The chipset driver alone often clears half the unknown devices, because many 'unknown' entries are chipset-integrated controllers. The [chipset install guide](/articles/how-to-install-chipset-drivers-in-windows-11-24h2/) walks through the most important package.

1. Find your exact model on the laptop maker's support page.
2. Download the Windows 11 driver bundle.
3. Install the chipset driver first, then the rest.
4. Reboot and recheck Device Manager after each group.

### Fix 4: Get chip-maker drivers for what the OEM lacks

If the laptop maker abandoned your model (no Windows 11 drivers listed), go to the chip maker directly: Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) auto-identifies Intel wireless, Bluetooth, and graphics; AMD and NVIDIA serve their own GPU drivers; Realtek hosts audio and card-reader drivers. Match the device name from your hardware-ID research to the chip maker's download. These reference drivers are newer than abandoned OEM packages and usually work, though they lack model-specific tuning.

1. Identify the chip vendor from your hardware-ID research.
2. Download from the chip maker's official site or detection tool.
3. Install and reboot.
4. Verify the device clears in Device Manager.

### Fix 5: Search the Microsoft Update Catalog by hardware ID

For stubborn devices, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you search by the hardware ID or device name directly. Enter the VEN/DEV string or the device name, pick the newest x64 package for Windows 11, download the CAB, and install it via Device Manager (Update driver > Browse > point at the extracted files). The Catalog hosts WHQL-signed drivers Microsoft validated, making it the safest manual source after the OEM and chip maker.

1. Search the Update Catalog for the hardware ID or device name.
2. Download the newest x64 Windows 11 package.
3. Install via Device Manager > Update driver > Browse.
4. Reboot and confirm the device is working.

### Fix 6: Check the BIOS for disabled devices

If a device remains unknown through every driver attempt, verify it is actually enabled. Reboot into the BIOS and check for toggles covering the device class — wireless, Bluetooth, camera, fingerprint reader, and serial-IO controllers are commonly switchable. A device disabled in the BIOS appears as unknown-or-absent no matter what driver you install. Enable it, boot, and let Windows detect it fresh. If the BIOS shows no such device at all, consider that the hardware may be absent or failed.

1. Enter the BIOS and look for the device-class toggle.
2. Enable the device and save.
3. Boot and let Windows detect it.
4. Install the driver for the newly detected device.

### Fix 7: Avoid driver updaters and verify stability

With all devices resolved, resist the urge to 'optimize' with a third-party driver updater — they are the leading cause of freshly broken driver stacks, and you just finished repairing one. Instead, verify stability: use the machine for a day, confirm sleep/wake cycles work, and check Device Manager once more. Then consider blocking Windows' automatic driver updates so a background update cannot re-break the stack you just built — the [driver-update control guide](/articles/best-way-to-disable-automatic-driver-updates/) covers that. Keep the driver installers you downloaded; they are your recovery kit.

1. Do not install any third-party driver updater tools.
2. Use the machine for a day, testing sleep/wake.
3. Re-verify Device Manager shows no warnings.
4. Archive the driver installers for future recovery.

## Closing

Finding missing drivers is detective work with a fixed procedure: Windows Update first, hardware-ID identification second, the laptop maker's bundle third, the chip maker and the Update Catalog for the stubborn remainder. The hardware ID is the key insight — a VEN/DEV string turns every 'Unknown device' into a named chip with a known vendor and a downloadable driver. The discipline that matters most is sourcing: maker, chip maker, Microsoft, in that order, and never a driver-updater utility. Do it right once and the Device Manager stays clean; do it with sketchy tools and you will be doing it again next month, this time with adware on top.
