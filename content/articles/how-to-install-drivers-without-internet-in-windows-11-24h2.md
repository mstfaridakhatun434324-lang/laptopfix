---
title: "Install Drivers Without Internet on Windows 11 24H2: The Offline Playbook"
slug: how-to-install-drivers-without-internet-in-windows-11-24h2
date: 2026-09-16
categories: ["drivers"]
tags: ["offline drivers", "no internet", "windows 11 24h2", "driver install"]
description: "Install drivers with no internet on Windows 11 24H2: prepare an offline driver kit on USB, use Device Manager with local files, and handle unsigned or missing drivers."
thumbnail: "/images/thumbs/how-to-install-drivers-without-internet-in-windows-11-24h2.webp"
faqs:
  - q: "How can I get drivers onto a laptop that has no internet at all?"
    a: "Use a second device with internet access — a phone, another computer, or a library PC — to download the driver packages from the laptop vendor's support site onto a USB flash drive. Then plug the drive into the offline laptop and install from the local files. Vendor packages are self-contained installers and need no internet once downloaded."
  - q: "Can Device Manager install drivers from a USB stick?"
    a: "Yes. In Device Manager, right-click the device, choose Update driver, then Browse my computer for drivers, and point it at the folder on the USB stick containing the extracted driver files. Check Include subfolders so Windows searches the whole tree. This works for individual devices when you have raw driver files rather than a setup executable."
  - q: "What if Windows 11 blocks the driver because it is unsigned?"
    a: "Windows 11 24H2 requires signed drivers by default, and bypassing that check reduces security, so treat it as a last resort for trusted vendor drivers only. The proper fix is to download the signed package from the vendor rather than a random repack. If you must proceed, the advanced startup option to disable driver signature enforcement applies for one boot only."
  - q: "Should I use a third-party offline driver updater tool?"
    a: "Be cautious. Many such tools bundle adware or install wrong drivers, and on a fresh offline install the risk is not worth it. The vendor's own driver packages for your exact model are safer and matched to your hardware. Use third-party tools only from sources you fully trust, and prefer the manual Device Manager method described here."
---

A fresh Windows 11 24H2 install with no network driver is a special kind of stranded: the laptop works, Windows is activated, but without internet you cannot fetch the very drivers that would get you online. The usual fix-it flow of letting Windows Update handle drivers is unavailable, and every tutorial assumes a connection you do not have. The way out is preparation done on a second device, and it is simpler than it sounds.

Every driver you need exists as a downloadable package on your laptop vendor's support site, and those packages are designed to install from local files with no internet at all. The trick is knowing which drivers matter most — network first, then chipset, then everything else — and having a method for the cases where a vendor package is missing or a device needs manual pointing at raw driver files.

This playbook covers the full offline workflow: building a driver kit on USB using another device, installing in the right order, using Device Manager against local folders, and handling the stubborn cases like unsigned drivers and unknown devices.

## Why this happens

- **No network driver after a clean install:** Windows 11 24H2 includes many drivers but not every Wi-Fi or Ethernet controller, especially newer 2.5 GbE chips and recent Intel and MediaTek wireless cards. Without the network driver, nothing else can be fetched.
- **Windows Update unreachable:** The normal driver pipeline — Windows Update plus the vendor's update utility — needs connectivity. Offline, you are the update mechanism.
- **Wrong driver order causes failures:** Chipset and serial IO drivers must go in before device-specific drivers. Installing a touchpad or card-reader driver on top of a missing chipset stack produces phantom errors.
- **Raw files versus installers:** Vendors ship both self-extracting setup executables and bare INF driver files. Knowing which one you have determines whether you double-click or use Device Manager's browse option.
- **Signature enforcement blocks old drivers:** 24H2 enforces driver signatures strictly. An old but correct driver that lacks a valid signature will be refused until you address it properly.
- **Unknown devices with no names:** Without drivers, Device Manager shows cryptic unknown devices. Their hardware IDs are the Rosetta Stone for identifying what each one actually is — once you can look them up.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Build the offline driver kit on a second device

Preparation is the whole battle. Ten minutes on a phone or a friend's computer saves hours of frustration on the offline laptop.

1. Identify your exact laptop model from the sticker on the bottom or the BIOS.
1. On the second device, open the vendor's support site and download the network (Wi-Fi and Ethernet), chipset, serial IO, graphics, and audio drivers for Windows 11 24H2.
1. Copy everything onto a USB flash drive, keeping each driver in its own clearly named folder.

### Fix 2: Install the network driver first

Connectivity unlocks everything else, so the network driver goes first even before the chipset in a true offline emergency — you can fix ordering issues afterward once Windows Update is reachable.

1. Plug in the USB stick and run the Wi-Fi or Ethernet setup executable from the vendor package.
1. Restart if prompted, then confirm the adapter appears in Device Manager without warnings.
1. Connect to the internet immediately and let Windows Update pull the remaining drivers — but verify what it installs against the [driver update basics](/articles/how-to-update-drivers-on-windows-11-laptop/) so a bad automatic driver does not undo your work.

### Fix 3: Install chipset and platform drivers in order

With the network working — or if you are staying fully offline — install the foundation drivers before the peripherals.

1. Run the chipset driver package first and restart.
1. Follow with serial IO, Intel Management Engine or AMD chipset components, then graphics.
1. Install audio, card reader, touchpad, and remaining devices last.
1. Restart after each major package; stacked installs without reboots are the top cause of mysterious offline-install failures.

### Fix 4: Point Device Manager at local driver folders

For devices that came as bare INF files or that a setup executable skipped, Device Manager can install directly from the USB stick.

1. In Device Manager, right-click the device and choose Update driver.
1. Select Browse my computer for drivers and point it at the driver's folder on the USB stick.
1. Check Include subfolders and click Next. Windows searches the folder tree for a matching signed driver.
1. Repeat per device. To confirm you installed the right versions afterward, see [checking driver versions](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/).

### Fix 5: Identify unknown devices by hardware ID

When Device Manager shows unknown devices with no useful name, the hardware ID reveals the vendor and device so you can fetch the exact driver on your next trip to an internet-connected machine.

1. Right-click the unknown device, open Properties, and go to the Details tab.
1. Select Hardware Ids from the dropdown and note the VEN and DEV codes.
1. Look these up on a connected device using the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) search, which indexes drivers by hardware ID.
1. Download the matching package to your USB kit and install it via Device Manager.

### Fix 6: Handle unsigned or refused drivers correctly

If Windows refuses a driver over signatures, do not reach for random repacks from forums. The safe path is the signed vendor package; the bypass is a last resort.

1. First, re-download the driver from the vendor to make sure you have the signed release, not a stripped copy.
1. If the vendor only offers an unsigned legacy driver you trust, use Advanced Startup to disable driver signature enforcement for one boot and install within that session.
1. Re-enable enforcement afterward by simply restarting normally. For a clean OS baseline underneath it all, the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) provides official installation media.

## Closing

Installing drivers offline is purely a logistics problem, not a technical one: get the right packages onto a USB stick using any connected device, install network first, then build upward from the chipset. Once the network driver lands, the crisis is over and Windows Update can take the baton. Keep that USB kit somewhere safe — it turns every future clean install from a day-long ordeal into a thirty-minute routine.
