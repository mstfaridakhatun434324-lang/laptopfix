---
title: "How to Install Drivers Without Internet on Windows 10"
slug: how-to-install-drivers-without-internet-on-windows-10
date: 2026-09-10
categories: ["drivers"]
tags: ["drivers", "offline", "windows 10", "no internet", "usb"]
description: "No internet on your Windows 10 laptop? Learn to install drivers offline — USB transfers, built-in driver store, Snappy Driver Installer, and phone tethering."
thumbnail: "/images/thumbs/how-to-install-drivers-without-internet-on-windows-10.webp"
faqs:
  - q: "How do I get drivers onto a laptop with no internet at all?"
    a: "Use a second device with internet: download the drivers from the laptop manufacturer's support site onto a USB flash drive, then run the installers on the offline laptop. Prioritize the network driver first — once networking works, you can download everything else directly. A phone with USB tethering also works as a temporary internet source for downloading drivers."
  - q: "Can Windows 10 install drivers without any downloads?"
    a: "Sometimes. Windows 10 ships with a built-in driver store containing basic drivers for common hardware — Device Manager's 'update driver' can install these offline. These built-in drivers get devices working at a basic level (display works, network may work) but lack manufacturer tuning. They're a starting point, not the final solution."
  - q: "What is Snappy Driver Installer and does it work offline?"
    a: "Snappy Driver Installer (SDI) is a free tool that installs drivers from massive offline driver packs — you download the packs once on a connected machine, copy them to USB, and SDI installs from local files with no internet needed. It's the go-to tool for machines with completely broken networking, though you should install selectively rather than bulk-updating everything."
  - q: "Can I use my phone to get the laptop online temporarily?"
    a: "Yes — USB tethering is the easiest bridge. Connect your phone to the laptop with a USB cable, enable USB tethering in the phone's hotspot settings, and Windows 10 usually recognizes it as a network adapter without needing drivers. This gives you just enough internet to download the proper drivers, after which you can disconnect the phone."
---

The network driver is broken, so you can't get online — and you can't get online to fix the network driver. It's the classic chicken-and-egg of Windows troubleshooting. Whether it's a fresh install with missing drivers or an update that killed networking, installing drivers on a Windows 10 laptop with no internet is entirely doable — you just need a bridge to get the files across.

The strategy is simple: prepare on a connected device, transfer via USB, install in the right order. This guide covers every offline method from the obvious (USB drive) to the clever (phone tethering, offline driver packs). If you want to try a dedicated offline driver tool, our [Snappy Driver Installer guide](/articles/how-to-use-snappy-driver-installer-in-windows-11-24h2/) covers that in depth — the concepts apply to Windows 10 too.

## Why this happens

- **Fresh Windows installs lack network drivers** — clean installs often miss the exact Wi-Fi or Ethernet driver.
- **An update broke the network driver** — you had internet until the update replaced a working driver.
- **The driver was uninstalled accidentally** — cleanup tools or manual uninstalls remove the network driver.
- **New hardware needs drivers Windows doesn't include** — replacement Wi-Fi cards or USB adapters need their own drivers.
- **Corrupted driver store** — damaged driver files prevent even built-in drivers from loading.
- **No second device seems available** — the real blocker is often not knowing the phone-tethering trick.
- **Manufacturer bloatware was removed aggressively** — debloating tools sometimes take network utilities with them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Try USB tethering from your phone

The fastest bridge: connect your phone to the laptop with a USB cable and enable USB tethering (Android: Settings > Network > Hotspot > USB tethering; iPhone: Personal Hotspot with the cable connected). Windows 10 recognizes most phones as a network device without extra drivers, giving you instant internet over the phone's data connection. Download your proper drivers, then disconnect — ten minutes of phone data solves the whole problem.

1. Connect your phone to the laptop with a USB cable.
2. On the phone, enable **USB tethering** (Android) or **Personal Hotspot** (iPhone).
3. Wait for Windows 10 to detect the new network connection.
4. Use this connection to download drivers from the manufacturer's site.

### Fix 2: Check Windows' built-in driver store first

Before going the USB route, check whether Windows already has a usable driver sitting in its local store. Open Device Manager, right-click the network device (or unknown device), choose Update driver > **Browse my computer for drivers** > **Let me pick from a list** — Windows shows compatible drivers from its built-in store. These are basic but often enough to get networking alive, after which you can download the proper manufacturer driver.

1. Open **Device Manager** and find the network device or unknown device.
2. Right-click it, choose **Update driver > Browse my computer for drivers**.
3. Select **Let me pick from a list of available drivers**.
4. Choose the matching driver, install it, and test connectivity.

### Fix 3: Download drivers on another device via USB

The reliable classic: on any connected device (another PC, a library computer, a friend's laptop), visit your laptop manufacturer's support site, enter your model or Service Tag, and download the network drivers — Ethernet and Wi-Fi — to a USB flash drive. Copy them to the offline laptop and run the installers. Prioritize network drivers above all else; once online, the rest is easy.

1. On a connected device, go to your laptop manufacturer's support site.
2. Enter your model and download the **network** (Ethernet + Wi-Fi) drivers to a USB drive.
3. Plug the USB drive into the offline laptop and run the installers.
4. Connect to the internet, then download the remaining drivers directly.

### Fix 4: Use the manufacturer's offline driver package

Dell, HP, and Lenovo offer full driver packs or "driver CAB" downloads containing every driver for a model in one package — designed exactly for offline deployment. Download the CAB or full package on a connected machine, transfer via USB, and either run the included installer or point Device Manager at the extracted folder. This gets every device — not just networking — in one pass. For installing from extracted files, our [compatibility mode guide](/articles/how-to-install-driver-in-compatibility-mode-in-windows-11-24h2/) covers manual installation techniques.

1. On a connected PC, download your model's **driver pack/CAB** from the manufacturer.
2. Transfer it to the offline laptop via USB drive.
3. Extract it and run the included setup, or point Device Manager at the folder.
4. Restart and verify all devices in Device Manager show no warnings.

### Fix 5: Deploy Snappy Driver Installer offline

For machines with multiple unknown devices, Snappy Driver Installer with offline packs is the heavy artillery. Download SDI and the driver packs you need on a connected computer, copy the whole SDI folder to a USB drive, and run it on the offline laptop — it matches hardware IDs to its local packs with zero internet. Install selectively (network first), one driver at a time, with a restore point created beforehand.

1. On a connected PC, download **Snappy Driver Installer** and the needed driver packs.
2. Copy the entire SDI folder to a USB drive.
3. On the offline laptop, run SDI as administrator from the USB drive.
4. Install the network driver first, then other devices one at a time.

### Fix 6: Extract drivers from the Windows installation media

Your Windows 10 installation USB or ISO contains a driver store with basic drivers for common hardware. If you have the install media, you can point Device Manager at it: choose "Browse my computer for drivers" and navigate to the media's driver folders. This is a fallback when nothing else is available — the drivers are generic but functional enough to bootstrap networking.

1. Insert your Windows 10 installation USB (or mount the ISO).
2. In **Device Manager**, right-click the device and choose **Update driver**.
3. Select **Browse my computer for drivers** and point to the USB drive.
4. Let Windows search the media; install whatever compatible driver it finds.

### Fix 7: Prevent repeat offline crises

Once you're back online, future-proof yourself. Download your laptop's full driver set from the manufacturer and archive it on a USB drive labeled with the model — network drivers especially. Create a system restore point while everything works. Consider keeping a bootable Windows USB with the network drivers copied onto it. Microsoft documents driver management basics at [Windows support](https://support.microsoft.com/en-us/windows) for reference.

1. Download the full driver set for your model from the manufacturer.
2. Save it to a labeled USB drive, including network drivers prominently.
3. Create a **system restore point** named "All drivers working."
4. Store the USB somewhere you'll find it — taped inside a drawer beats a random folder.

## Closing

No internet is an inconvenience, not a dead end — the drivers exist, they just need a ride to your laptop. Phone tethering is the quickest bridge; the USB-drive method is the most reliable; offline packs handle the worst cases. And the real lesson is Fix 7: a fifteen-minute archiving session now prevents the next chicken-and-egg crisis entirely.
