---
title: "How to Install Drivers Without Internet on Windows 11"
slug: "how-to-install-drivers-without-internet-on-windows-11"
date: "2026-09-20"
categories: ["drivers"]
tags: ["install drivers offline", "no internet", "usb driver install", "windows 11", "driver package"]
description: "No internet on your Windows 11 laptop? Learn how to download drivers on another device, transfer via USB, and install network, chipset, and graphics drivers offline."
thumbnail: "/images/thumbs/how-to-install-drivers-without-internet-on-windows-11.webp"
faqs:
  - q: "How do I get drivers onto a laptop with no internet at all?"
    a: "Use a second device with internet — a phone, tablet, library computer, or friend's PC — to download the driver packages from your laptop manufacturer's support site, then transfer them on a USB flash drive. Phone USB tethering is even simpler: it shares your phone's data connection over USB, giving the laptop temporary internet to download drivers directly. Both methods work reliably."
  - q: "Which drivers should I install first when offline?"
    a: "Install in this order: chipset, then network (Ethernet and Wi-Fi), then graphics, then audio and everything else. The chipset driver lets Windows properly recognize the motherboard's devices, and the network driver restores internet access, after which Windows Update can fetch the rest automatically. Installing graphics before the chipset can occasionally cause detection issues."
  - q: "Can I use my phone to download drivers for my laptop?"
    a: "Yes, two ways. First, download the driver files on your phone's browser and transfer them to the laptop with a USB cable. Second, enable USB tethering on the phone (usually under Settings > Network or Hotspot), connect it to the laptop, and Windows will use the phone's mobile data as its internet connection — then just download drivers normally on the laptop. Tethering uses mobile data, so watch your allowance."
  - q: "What if I don't know which drivers my laptop needs?"
    a: "Open Device Manager and look for devices with yellow warning icons or listed as unknown — those need drivers. Even easier: find your exact laptop model on the manufacturer's support site, which lists every driver your machine needs in one place. Download the full set for your model onto USB in one trip, and you will have everything regardless of what Device Manager shows."
---

A fresh Windows 11 install — or a broken network driver — can leave a laptop with no internet and no obvious way to get drivers. It feels like a chicken-and-egg problem, but it is very solvable: you just need a second internet-connected device and a USB stick, or a phone with tethering. This guide covers every practical method, the correct installation order, and how to verify everything landed properly.

The key insight: you do not need internet on the laptop itself. Driver files are just files — download them anywhere, carry them over on USB, and install them locally. Plan for one trip: grab the full driver set for your model in a single download session.

## Why this happens

- **Fresh Windows install without network drivers:** Clean installs often lack the specific Ethernet or Wi-Fi driver the laptop needs.
- **Broken network driver:** The driver bringing you here may be the very one that is broken, cutting off the normal download path.
- **Windows Update cannot reach the machine:** With no network, the automatic driver pipeline is unavailable.
- **Unknown devices after reinstall:** Chipset and platform drivers missing means Windows cannot even identify some hardware.
- **No second PC assumed:** Most guides assume you can just download drivers, ignoring the offline scenario.
- **Wrong driver architecture:** Downloading 32-bit drivers for a 64-bit system (or vice versa) wastes the one transfer you have.
- **Driver install order matters:** Installing graphics before chipset can cause detection problems that look like bad drivers.
- **USB transfer pitfalls:** Corrupted downloads or wrong model packages only reveal themselves at install time, far from internet.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your exact laptop model

Getting the model right is the foundation — wrong-model drivers cause the worst headaches.

1. Check the sticker on the laptop's bottom for the full model name and serial number.
2. If Windows boots, press Win + R, type `msinfo32`, and note the System Model and System SKU.
3. Write down the model exactly — "Pavilion 15-eg2000" and "Pavilion 15-eg2001" can use different drivers.
4. Note whether Windows is 64-bit (Settings > System > About > System type) — virtually all modern laptops are.
5. Keep this information on your phone or paper for the download step.

### Fix 2: Use phone USB tethering (fastest method)

If your phone has mobile data, this gives the laptop real internet in under a minute.

1. Connect your phone to the laptop with a USB cable.
2. On Android: Settings > Network & internet > Hotspot & tethering > enable USB tethering. On iPhone: enable Personal Hotspot, then connect via USB.
3. Windows 11 should detect a new network connection automatically — check the taskbar network icon.
4. If it does not appear, open Device Manager and check for a new "Remote NDIS" adapter; install any driver Windows requests.
5. Once online, download drivers directly on the laptop from the manufacturer's site.
6. Watch your mobile data usage — driver packages can total several hundred megabytes.

### Fix 3: Download the full driver set on another device

When tethering is not an option, do one careful download session elsewhere.

1. On any internet-connected device, go to your laptop maker's support site and enter your exact model.
2. Download at minimum: chipset, Ethernet/LAN, Wi-Fi, Bluetooth, and graphics drivers for Windows 11 64-bit.
3. Ideally, also grab audio, touchpad, and card-reader drivers to complete the set in one trip.
4. Save everything into a clearly labeled folder on a USB flash drive (8 GB or larger is plenty).
5. Verify the downloads completed — check file sizes against the site's listed sizes before leaving internet behind.
6. Microsoft's [Update Catalog](https://www.catalog.update.microsoft.com/) is a backup source for individual driver files if the maker's site is hard to use on a phone.

### Fix 4: Transfer and organize on the laptop

Set up for a smooth offline installation session.

1. Plug the USB drive into the laptop and copy the entire driver folder to the desktop or Documents — installing from the local disk is more reliable than from the USB stick.
2. Create subfolders by category (chipset, network, graphics, audio) if the downloads are not already organized.
3. Extract any ZIP archives now — installers cannot run from inside unextracted zips.
4. Note which files are actual installers (setup.exe) versus raw driver folders (containing .inf files) — both are usable, as Fix 6 explains.
5. Disconnect the USB drive once copied, to avoid accidentally running installers twice.

### Fix 5: Install in the correct order

Order matters — chipset first, network second, everything else after.

1. Install the chipset driver first and restart when prompted — this lets Windows properly enumerate motherboard devices.
2. Install the Ethernet/LAN driver next, then the Wi-Fi driver; restart after each if asked.
3. Test for internet access — with network drivers in, you may be online, and Windows Update can take over from here.
4. Install the graphics driver, then audio, touchpad, Bluetooth, and remaining drivers.
5. Restart once more at the end even if no installer demands it.
6. If a driver refuses to install normally, the [compatibility-mode method](/articles/how-to-install-driver-in-compatibility-mode-on-windows-11/) often gets older packages working on Windows 11.

### Fix 6: Install raw (.inf) drivers manually

Some downloads are driver files without an installer — install them through Device Manager.

1. Open Device Manager and find the device with a yellow warning (or the unknown device).
2. Right-click it, choose "Update driver", then "Browse my computer for drivers".
3. Click Browse, navigate to the folder containing the .inf files, and make sure "Include subfolders" is ticked.
4. Click Next — Windows will find and install the matching driver from the .inf.
5. If Windows says the best driver is already installed but the device still malfunctions, choose "Let me pick from a list" and force the specific .inf version.
6. Restart after installing critical drivers (chipset, network, graphics).

### Fix 7: Verify every device is healthy

Confirm the offline install actually covered everything.

1. Open Device Manager and expand every category, looking for yellow warnings or "Unknown device" entries.
2. For any remaining unknown device, right-click > Properties > Details tab > select Hardware Ids, and note the VEN/DEV codes.
3. Those codes identify the exact hardware — search them on your phone to find the right driver for a second USB trip if needed.
4. Open Settings > Windows Update and run a check — with network restored, it will fill any gaps automatically.
5. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents the Device Manager verification steps officially.

### Fix 8: Prepare an offline driver backup for next time

Never be stranded again — build a driver kit while everything works.

1. Once all drivers are installed and verified, copy the entire driver folder to a safe place — a second USB stick or cloud storage.
2. Consider exporting installed drivers with the command `dism /online /export-driver /destination:D:\DriverBackup` (run as administrator).
3. Label the backup with the laptop model and date.
4. After any future clean install, you can bulk-install from this backup via Device Manager or `pnputil /add-driver D:\DriverBackup\*.inf /subdirs /install`.
5. The [Windows 10 offline-driver guide](/articles/how-to-install-drivers-without-internet-on-windows-10/) covers the same backup strategy for older systems.

## Closing

Installing drivers without internet is purely a logistics problem: identify the model, download the set elsewhere, transfer via USB, and install in the right order. Phone USB tethering shortcuts the whole process when mobile data is available. And once you are back online, take ten minutes to build the driver backup in Fix 8 — future you, staring at a fresh install with no network, will be grateful.
