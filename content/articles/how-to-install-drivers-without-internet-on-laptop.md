---
title: "How to Install Drivers on a Laptop With No Internet"
slug: how-to-install-drivers-without-internet-on-laptop
date: 2026-10-09
categories: ["drivers"]
tags: ["install drivers offline", "no internet", "driver installation", "usb drivers", "device manager"]
description: "No internet on your laptop? Learn how to install drivers offline using another PC, USB drives, Device Manager INF installs, and DISM driver injection."
thumbnail: "/images/thumbs/how-to-install-drivers-without-internet-on-laptop.webp"
faqs:
  - q: "How do I get drivers onto a laptop with no internet at all?"
    a: "Use a second internet-connected device — a phone, another PC, or a library computer. Download the driver packages from your laptop maker's support site onto a USB flash drive, then run the installers on the offline laptop. For network drivers specifically, this is the standard recovery path technicians use."
  - q: "Can I use my phone to get internet on the laptop temporarily?"
    a: "Yes. USB tethering shares your phone's mobile data with the laptop over a cable, and Windows usually recognizes it without special drivers. This gives you just enough connectivity to download the real network drivers, after which you can disable tethering and install everything properly."
  - q: "What order should I install drivers in?"
    a: "Install chipset drivers first, then storage controllers, then graphics, then network (Ethernet and Wi-Fi), then audio, then everything else like card readers and fingerprint sensors. The chipset package lays the foundation the other drivers build on, so it always goes first."
  - q: "Will Windows install any drivers on its own without internet?"
    a: "Windows includes a library of generic inbox drivers on the installation media. These cover basic display, storage, and some network hardware — enough to boot and show a desktop. But they are basic: no Wi-Fi on many newer cards, no proper graphics acceleration, and no laptop-specific features until you add the real drivers."
---

The cruelest catch-22 in PC repair: you need the network driver to get internet, and you need internet to get the network driver. It usually strikes after a fresh Windows install, when Device Manager shows a row of yellow warning icons and the Wi-Fi adapter is simply gone. The laptop works — it just cannot talk to anything.

Here is the good news: this is a solved problem with a well-worn playbook. Professional technicians deal with offline driver installation constantly, and every method below uses only free tools plus one USB flash drive and a second internet-connected device (even a phone counts).

This guide covers the full offline driver workflow: preparing your driver package on another device, installing via setup executables and manual INF installation, injecting drivers with DISM for stubborn cases, and the correct installation order. Follow it once and the catch-22 disappears for good.

## Why this happens


- **Fresh Windows install without network drivers:** Windows setup media includes generic drivers, but many modern Wi-Fi and Ethernet chips need manufacturer drivers that are not in the box.
- **Driver wiped by a bad update:** A failed or rolled-back driver update can leave the network adapter in a broken state with no working version cached locally.
- **Wrong driver architecture:** Installing 32-bit drivers on 64-bit Windows (or vice versa) silently fails and leaves the device unclaimed.
- **Missing chipset driver:** Without the chipset package, Windows may not even enumerate some devices correctly, hiding them from Device Manager.
- **Corrupted driver store:** The local driver repository (DriverStore) can corrupt during interrupted updates, so Windows cannot reinstall even drivers it once had.
- **BIOS/firmware too old for the OS:** Very old firmware sometimes misreports hardware IDs to a new Windows version, so even correct drivers refuse to bind.
- **Secure Boot blocking unsigned drivers:** Some third-party driver packages lack proper signatures and get blocked on systems with Secure Boot enforced.
- **USB ports themselves driverless:** On rare fresh installs, even USB needs a driver first — in that case, burn the drivers to a DVD or use an SD card the BIOS can see.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Prepare a driver pack on another device


Everything starts here. You need one internet-connected device and one USB flash drive. The goal is a folder containing every driver your offline laptop needs, downloaded from the authoritative source — your laptop maker's support page.

1. On the connected device, find your laptop's exact model number (check the sticker under the offline laptop or its original box).
2. Visit your maker's support site — [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) — and open the drivers page for your model.
3. Download at minimum: chipset, graphics, Ethernet, Wi-Fi, and audio drivers for your Windows version and architecture (64-bit for nearly all modern laptops).
4. Copy everything to a USB flash drive in clearly named folders (Chipset, WiFi, Audio, and so on).
5. Safely eject the drive and plug it into the offline laptop.

### Fix 2: Install in the correct order


Driver installation order matters more than people think. The chipset driver teaches Windows how to talk to the motherboard; everything else builds on that foundation. Installing graphics before chipset is a classic cause of mysterious follow-on failures.

1. Run the chipset installer first and restart when prompted.
2. Next install storage/RAID drivers if your maker lists any.
3. Install the graphics driver and restart.
4. Install Ethernet, then Wi-Fi drivers. Check whether the network icon comes alive.
5. Install audio, Bluetooth, card reader, fingerprint, and remaining drivers.
6. Restart once more at the end and verify Device Manager shows no warning icons.

### Fix 3: Use USB tethering as a temporary bridge


If you have a smartphone with mobile data, you can give the laptop temporary internet in about a minute. USB tethering uses generic drivers Windows already has, so it works even when Wi-Fi and Ethernet are dead.

1. Connect your phone to the laptop with a USB cable.
2. On Android: Settings, Network & internet, Hotspot & tethering, enable USB tethering. On iPhone: enable Personal Hotspot, then connect via USB.
3. Windows should detect a new wired network connection within a minute.
4. Use this connection to download drivers directly on the laptop — or run Windows Update once to pull network drivers.
5. Disable tethering when done and install the proper drivers offline if you prefer stable versions.

### Fix 4: Install drivers manually through Device Manager


Some downloads are raw driver files (.inf) rather than setup programs — especially Wi-Fi and Bluetooth packages. Device Manager can install these directly by pointing it at the extracted folder. This is also the method for forcing a specific driver version.

1. Extract the downloaded driver ZIP to a folder on the USB drive.
2. On the offline laptop, open Device Manager (Windows + X).
3. Right-click the device with the warning icon and choose Update driver.
4. Select Browse my computer for drivers.
5. Point it at the extracted folder, check Include subfolders, and click Next.
6. Windows will install the matching .inf. Repeat for each unknown device.
7. For a deeper walkthrough of manual techniques, see our guide to [installing OEM drivers manually](/articles/how-to-install-oem-drivers-manually-on-windows-11/).

### Fix 5: Inject drivers offline with DISM


For advanced cases — like adding network drivers to a Windows installation image before setup, or servicing an offline Windows — the DISM command-line tool injects drivers directly into the driver store. Technicians use this to pre-load network drivers so the catch-22 never happens.

1. On a working PC, extract all needed drivers to a folder, for example D:\Drivers.
2. Open an elevated Command Prompt.
3. To add drivers to the running offline system from WinPE or recovery: first identify the Windows drive letter, then run DISM /Image:C:\ /Add-Driver /Driver:D:\Drivers /Recurse.
4. To service an install image before setup: mount the install.wim, run DISM /Image:C:\mount /Add-Driver /Driver:D:\Drivers /Recurse, then commit.
5. Boot or reboot and verify the devices appear in Device Manager.
6. This method bypasses setup executables entirely — useful when installers refuse to run.

### Fix 6: Restore from a driver backup if you made one


If you exported your drivers before the problem — with DISM's driver export or a backup tool — restoration is a single command. This is the fastest offline recovery path and the reason technicians preach backups before every major change.

1. Plug in the drive containing your backup (a folder of .inf-based drivers).
2. Open an elevated Command Prompt.
3. Run pnputil /add-driver X:\DriverBackup\*.inf /subdirs /install (replace X with your drive letter).
4. Windows installs every driver in the backup into the driver store.
5. Restart and confirm Device Manager is clean.
6. No backup? Make one now while everything works — our [driver backup guide](/articles/how-to-backup-drivers-before-update-on-windows-11/) shows the exact commands.

### Fix 7: Verify everything and get back online safely


The final pass: confirm each device is healthy, get the laptop on the network with proper drivers, and set yourself up so this never happens again. Ten minutes of verification now prevents a repeat of the whole ordeal.

1. Open Device Manager and confirm no yellow warning icons remain under any category.
2. Connect to Wi-Fi or Ethernet and confirm stable connectivity for several minutes.
3. Run Windows Update once — with real network drivers in place, it can now fetch anything still missing.
4. Immediately create a driver backup with DISM or pnputil and store it on a USB drive you keep labeled.
5. Consider keeping a copy of your network drivers permanently on that USB stick — it is the single most useful emergency tool a laptop owner can own.

## Closing


Installing drivers without internet looks intimidating until you have done it once — then it is just a routine: driver pack on USB, install chipset first, work down the list, verify in Device Manager. The real lesson is the backup. A fifteen-minute driver export today is the difference between a quick restore and another afternoon of catch-22 next time something breaks.
