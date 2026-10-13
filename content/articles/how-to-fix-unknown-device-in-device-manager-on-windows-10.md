---
title: "How to Fix an Unknown Device in Device Manager on Windows 10"
slug: how-to-fix-unknown-device-in-device-manager-on-windows-10
date: 2026-10-12
categories: ["drivers"]
tags: ["unknown device windows 10", "device manager error", "install missing driver"]
description: "Unknown Device showing in Device Manager on Windows 10? Identify the hardware with its hardware ID and install the correct driver step by step."
thumbnail: "/images/thumbs/how-to-fix-unknown-device-in-device-manager-on-windows-10.webp"
faqs:
  - q: "Why do I have Unknown Devices after installing Windows 10?"
    a: "A fresh Windows 10 install only includes base drivers, so OEM-specific hardware like card readers, sensors, and chipset components show as unknown. Installing the chipset driver package from your laptop manufacturer identifies most of them in one step After the chipset package, check Windows Update's optional updates for any remaining devices, since those often carry the sensor and card-reader drivers the chipset installer skips."
  - q: "What is the hardware ID and how do I use it?"
    a: "The hardware ID is a code like PCI\\VEN_8086&DEV_9D3A that uniquely identifies the chip. Find it in the device's Properties under the Details tab, then search the VEN and DEV values on the manufacturer's support site to find the exact matching driver."
  - q: "Can I just disable the Unknown Device?"
    a: "You can, but disabling hides the symptom without restoring the hardware's function. If the device is something you use — a card reader, fingerprint sensor, or chipset component — installing the proper driver is the better fix. Only disable it if the hardware is genuinely unused."
  - q: "Will Windows Update eventually fix Unknown Devices on its own?"
    a: "Sometimes, but not reliably. Windows Update finds drivers for common hardware but often misses OEM-specific components. Checking optional driver updates helps, but manually installing the manufacturer's chipset package is faster and more thorough Manual installation from the manufacturer's site remains the dependable path, because you choose the exact driver instead of hoping the update catalog has it."
---

That yellow-flagged "Unknown Device" in Device Manager on Windows 10 means Windows can see a piece of hardware but has no idea what it is. The component is physically present and probably fine — what is missing is the driver that introduces it to the operating system. This is extremely common after clean installs of Windows 10, where only Microsoft's base drivers are present.

The reliable fix is a two-part process: identify the mystery hardware using its hardware ID, then install the matching driver from the manufacturer. Below is the full procedure, from quick automatic attempts to manual driver installation for the stubborn cases.

## Why this happens

- **Fresh Windows 10 install:** Clean installs lack OEM drivers, so proprietary components like SD readers, sensors, and hotkey controllers appear as unknown.
- **Missing chipset driver package:** Without the Intel or AMD chipset software, several motherboard devices cannot be enumerated by name.
- **Driver removed by cleanup tools:** Overzealous driver cleaners and "PC optimizer" apps sometimes delete OEM driver packages.
- **BIOS update changed hardware reporting:** New firmware can alter device IDs, orphaning the previously matched driver.
- **Device disabled in BIOS:** Hardware switched off in firmware (an unused camera or card reader) shows as unknown instead of absent.
- **Interrupted Windows Update:** A failed feature update can leave driver installations half-completed, producing unknown entries.
- **Wrong architecture driver installed:** A 32-bit driver package on 64-bit Windows (or vice versa) fails to bind, leaving the device unidentified.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the hardware ID to identify the device

Never guess drivers. The hardware ID tells you exactly what the chip is.

1. Press **Win + X** and open **Device Manager**.
2. Right-click the **Unknown Device** and select **Properties**.
3. Go to the **Details** tab, set **Property** to **Hardware Ids**, and copy the top value (for example, `PCI\VEN_8086&DEV_9D3A`).
4. The `VEN_` portion identifies the manufacturer (8086 = Intel, 10DE = NVIDIA, 1022 = AMD) and `DEV_` identifies the chip.
5. Search the full string or the VEN/DEV pair on your laptop maker's support site to find the matching driver.

Keep this ID handy — every fix below depends on knowing what you are actually installing a driver for.

### Fix 2: Install the OEM chipset driver package

One installer clears most unknown devices on laptops.

1. Find your exact model number from the sticker on the laptop or **Settings > System > About**.
2. Go to the support site for your brand: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Download the **Chipset** driver for Windows 10 and run it.
4. Restart and recheck Device Manager.

Chipset packages enumerate the serial I/O controllers, management engine, and platform devices that account for the majority of unknown entries. If you maintain drivers regularly, our [driver backup guide](/articles/best-way-to-backup-drivers-before-update/) is worth reading before any major driver surgery.

### Fix 3: Try automatic driver search and optional updates

Quick and worth trying before manual work.

1. Right-click the Unknown Device, choose **Update driver**, then **Search automatically for drivers**.
2. Then open **Settings > Update & Security > Windows Update > View optional updates** and install any driver updates listed.
3. Restart and check Device Manager again.

Optional updates frequently contain the vendor drivers that automatic search misses on the first pass.

### Fix 4: Install the driver manually via Have Disk

When you have the right driver files but Windows will not auto-match them, force it.

1. Download and extract the driver package for the identified hardware.
2. In Device Manager, right-click the Unknown Device and choose **Update driver > Browse my computer for drivers**.
3. Click **Let me pick from a list of available drivers**, then **Have Disk**, and browse to the `.inf` file.
4. Complete the wizard and restart.

Manual installation bypasses Windows' matching heuristics, which is exactly what you need when the driver is correct but the catalog data confuses the automatic picker.

### Fix 5: Uninstall the ghost entry and rescan

Corrupted entries sometimes block correct identification until removed.

1. Right-click the Unknown Device and choose **Uninstall device**, checking **Delete the driver software for this device** if offered.
2. Click **Action > Scan for hardware changes** in the Device Manager menu.
3. Windows re-detects the hardware fresh — then install the correct driver using Fix 2 or Fix 4.

This mirrors the technique used for [unrecognized USB devices](/articles/best-way-to-fix-usb-device-not-recognized/), where a stale driver association is the root problem.

### Fix 6: Check BIOS for disabled hardware

Firmware-disabled devices enumerate as unknown.

1. Reboot into BIOS/UEFI (**F2**, **Del**, or **F10** at startup).
2. Under **Advanced** or **System Configuration**, look for toggles for the card reader, camera, fingerprint reader, or wireless devices.
3. Enable anything you use, save, and boot into Windows.
4. Install the driver for the newly enumerated device.

If the device is hardware you never use, leaving it disabled in BIOS is cleaner than fighting its driver.

### Fix 7: Stop Windows Update from breaking it again

Once the device is identified and working, protect the driver.

1. After a working driver is installed, consider pausing driver updates so Windows Update does not replace it with a generic version.
2. Use **System > Advanced system settings > Hardware > Device Installation Settings** and select **No**.
3. For a surgical approach, hide only the offending driver update with the show/hide updates troubleshooter.

Microsoft's official driver guidance on the Windows support site explains these settings in more detail. Locking in the working driver prevents the unknown-device warning from returning after the next Patch Tuesday.

## Closing

Unknown Devices on Windows 10 are a driver-identification problem, not a hardware failure. Read the hardware ID, install the manufacturer's chipset package (which clears most cases at once), and manually match any stragglers with Have Disk. Once everything is named and working, lock the drivers down so updates do not undo your work.
