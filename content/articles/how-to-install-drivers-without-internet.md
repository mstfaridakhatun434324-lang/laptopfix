---
title: "How to Install Drivers on a Laptop Without Internet"
slug: "how-to-install-drivers-without-internet"
date: "2026-09-20"
categories: ["drivers"]
tags: ["drivers", "offline install", "windows 11", "device manager", "usb"]
description: "No internet on your laptop? Learn how to download drivers on another device, transfer them via USB, and install them offline step by step."
thumbnail: "/images/thumbs/how-to-install-drivers-without-internet.webp"
faqs:
  - q: "How can I get drivers if my laptop has no internet?"
    a: "Use a second device with internet access: a phone, another computer, or a library PC. Download the drivers from your laptop manufacturer's support page onto a USB flash drive, then run the installers on the offline laptop. Always match the exact laptop model and Windows version."
  - q: "Can I install drivers from a USB drive?"
    a: "Yes. Copy the driver installer files or extracted driver folders to a USB drive, plug it into the offline laptop, and run the installers. For drivers without an installer, use Device Manager's manual driver update and point it at the folder containing the .inf files."
  - q: "What driver should I install first on an offline laptop?"
    a: "Install the network driver first: Wi-Fi or Ethernet. Once networking works, the laptop can fetch the remaining drivers itself through Windows Update or the manufacturer's update utility, which saves enormous manual effort. Chipset drivers come second, since graphics, audio, and other drivers sometimes depend on chipset components being present."
  - q: "Can Windows install drivers without internet?"
    a: "Windows includes a built-in driver store with basic drivers for common hardware, which is why a fresh install often has working display and USB. But Wi-Fi, Bluetooth, and specialized hardware usually need manufacturer drivers that are not in the built-in store, so plan to supply those yourself."
---

A fresh Windows install with no network driver is a special kind of stranded: the one thing you need to get drivers is the internet, and the internet is the thing you cannot reach. It happens after clean installs, when a Wi-Fi driver breaks, or when you are setting up a laptop somewhere with no connectivity at all.

The way out is gloriously low-tech: a second device with internet, a USB flash drive, and the manufacturer's support page. You download the drivers elsewhere, carry them over on the drive, and install them locally. Knowing how to [update drivers properly](/articles/how-to-update-drivers-on-windows-11-laptop/) helps once you are back online, and the same approach rescues a [missing display adapter](/articles/how-to-fix-display-adapter-missing-after-windows-11-update/).

This guide covers the full offline workflow: identifying what you need, downloading it elsewhere, transferring it, and installing it without a network connection.

## Why this happens

- **The network driver is missing:** Without Wi-Fi or Ethernet drivers, the laptop cannot reach Windows Update or any download site.
- **Windows' built-in driver store is incomplete:** Generic drivers cover common hardware but rarely include your exact Wi-Fi or Bluetooth chip.
- **A clean install wiped the manufacturer's drivers:** Fresh Windows media contains Microsoft drivers, not the OEM-tuned versions.
- **The driver was uninstalled during troubleshooting:** Removing a broken network driver to fix it can leave you offline if the reinstall fails.
- **No second device was prepared:** Most people discover the problem only after the laptop is already offline.
- **Wrong driver version downloaded:** Grabbing a driver for the wrong model or Windows version wastes the one transfer you have.
- **Secure Boot or signature issues:** Extremely old unsigned drivers may be blocked on modern systems.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which drivers you need

Blindly downloading every driver wastes time and USB space. A quick inventory on the offline laptop tells you precisely what is missing.

1. On the offline laptop, open Device Manager.
2. Expand each category and note every device with a yellow warning or listed as Unknown device.
3. Pay special attention to Network adapters: Wi-Fi and Ethernet are your priority.
4. Write down the exact laptop model from the sticker on the bottom or the BIOS.
5. Note the Windows version and whether it is 64-bit, since drivers are version-specific.

### Fix 2: Download the drivers on a second device

Any internet-connected device works: a phone, a friend's laptop, or a public computer. The manufacturer's support page is the safest source.

1. On the connected device, go to your laptop maker's support page.
2. Enter the exact model number and select the correct Windows version.
3. Download the network drivers first, then chipset, graphics, audio, and Bluetooth.
4. Save everything to a folder on a USB flash drive with at least 8 GB free.
5. Keep the original file names so you can tell the drivers apart later.

### Fix 3: Transfer the drivers via USB drive

The USB drive is your sneakernet. Copy the whole driver folder over, and verify the files actually made it before you walk away from the internet-connected machine.

1. Plug the USB drive into the connected device and copy the driver folder.
2. Safely eject the drive and plug it into the offline laptop.
3. Open the drive and confirm all the installer files are present and nonzero in size.
4. Copy the folder to the laptop's desktop for faster access during installation.
5. If the laptop lacks USB-A ports, use a USB-C adapter or a phone as a USB drive.

### Fix 4: Install the network driver first

Networking unlocks everything else. Once Wi-Fi or Ethernet works, Windows Update can fetch the remaining drivers automatically, turning a manual marathon into a short sprint.

1. Open the driver folder and run the Wi-Fi or Ethernet installer first.
2. Follow the prompts and restart the laptop when asked.
3. Connect to a network and confirm internet access works.
4. Run Windows Update to pull in the remaining drivers automatically.
5. Return to the manual installers only for anything Windows Update misses.

### Fix 5: Install remaining drivers with their setup programs

Most manufacturer drivers come as self-contained installers. Run them in a sensible order so dependencies resolve cleanly.

1. Install the chipset driver next, then restart.
2. Install graphics, audio, and Bluetooth drivers one at a time.
3. Restart between major driver installs when prompted.
4. Check Device Manager after each round for remaining warning icons.
5. Leave optional utilities and bloatware unchecked during installation.

### Fix 6: Manually install drivers that have no setup program

Some drivers ship as bare .inf files with no installer. Device Manager can install these directly by pointing it at the extracted folder.

1. Extract the driver archive to a folder on the laptop if it is zipped.
2. Open Device Manager and right-click the unknown or warning-marked device.
3. Choose Update driver, then Browse my computer for drivers.
4. Point the browser at the extracted folder and enable Include subfolders.
5. Click Next and let Windows install from the .inf files, then restart.

### Fix 7: Verify everything and create an offline driver backup

Once the laptop is healthy, take ten minutes to prevent a repeat. A driver backup on a USB drive turns the next offline emergency into a non-event.

1. Open Device Manager and confirm no devices show warnings.
2. Test Wi-Fi, Bluetooth, audio, and the webcam.
3. Copy the working driver installers to a labeled USB drive for safekeeping.
4. Consider exporting drivers with a tool like Double Driver while the system is healthy.
5. Store the backup somewhere you will actually find it next time.

## Closing

An offline laptop is only stranded until you bridge the gap with a USB drive and a second internet-connected device. Download the network driver first, get online, and let Windows Update finish the job. Keep a driver backup afterward, and you will never be stuck in this particular trap again.
