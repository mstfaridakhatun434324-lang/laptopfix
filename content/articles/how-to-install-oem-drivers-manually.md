---
title: "How to Install OEM Drivers Manually on a Windows Laptop"
slug: how-to-install-oem-drivers-manually
date: 2026-10-02
categories: ["drivers"]
tags: ["oem drivers", "manual install", "device manager", "inf driver", "dell hp lenovo"]
description: "Install OEM drivers manually on Windows: download the right package from your laptop maker and install via setup or Device Manager's INF method."
thumbnail: "/images/thumbs/how-to-install-oem-drivers-manually.webp"
faqs:
  - q: "What is the difference between an OEM driver and a regular driver?"
    a: "An OEM driver comes from your laptop manufacturer and is tuned for your exact model — its power profiles, thermal behavior, and hardware quirks. A generic driver from the chip maker works but lacks those customizations. For laptops, the OEM version almost always behaves better, especially for graphics, audio, and Wi-Fi."
  - q: "Where do I find OEM drivers for my laptop?"
    a: "On the manufacturer's support site: Dell, HP, Lenovo, ASUS, and Acer all have driver download pages keyed to your model or serial number. Enter the exact model, select your Windows version, and download from the categorized list. Avoid third-party driver sites, which often bundle outdated or modified packages."
  - q: "How do I install a driver that only has INF files and no setup program?"
    a: "Extract the files, open Device Manager, right-click the device, choose Update driver, then 'Browse my computer for drivers,' and point to the extracted folder with subfolders included. Windows matches the INF to the hardware and installs it. This is the standard method for chipset and storage driver packages."
  - q: "Do I need to uninstall the old driver before installing the OEM one?"
    a: "Usually not — a proper OEM installer upgrades in place. Uninstall first only when the current driver is corrupted, when Device Manager shows the device failing, or when switching between very different driver branches. A clean uninstall plus reboot is the reliable fix for stubborn cases, not the default procedure."
---

OEM drivers — the versions your laptop manufacturer publishes for your exact model — are the single most reliable source of drivers for a Windows laptop. They carry the thermal tuning, power profiles, and hardware quirks that generic chip-vendor drivers do not. The catch is that installing them manually is not always a friendly double-click affair: some come as setup programs, others as bare INF files, and a few need special handling.

This guide covers the full manual process. You will learn where to get the right package, how to install both setup-based and INF-only drivers, and how to confirm the install actually took. No third-party updater tools, no guesswork.

## Why this happens

- **Generic drivers lack laptop tuning:** Chip-vendor drivers work, but OEM versions include the power and thermal behavior your specific chassis was validated with.
- **Windows Update serves older builds:** Microsoft's catalog trails the manufacturer's releases by months, leaving known fixes uninstalled.
- **Some OEM drivers have no installer:** Chipset, storage, and sensor packages often ship as INF-only archives that need Device Manager to install.
- **Wrong model, wrong driver:** Manufacturer sites list many similar models; downloading for a sibling model installs drivers that misbehave subtly.
- **Setup programs fail silently:** OEM installers sometimes exit without error but skip components when prerequisites are missing.
- **Driver signature blocks:** Older OEM packages may lack signatures Windows 11 requires, stopping the install with an unhelpful message.
- **Partial upgrades corrupt state:** Installing a new OEM driver over a corrupted old one can inherit the corruption instead of fixing it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your exact model and Windows version

Precision starts here. Press Win + R, type `msinfo32`, and record the System Model and the OS build. Then find the service tag or serial number — on a sticker on the bottom panel, in the BIOS, or in the manufacturer's preinstalled app. Manufacturer download pages match drivers to this identifier, and laptops often have regional variants with different Wi-Fi cards or audio chips under the same marketing name. Downloading for "almost your model" is how you get a Wi-Fi driver for a card you do not have. Write the exact strings down before you open the browser.

### Fix 2: Download the correct package from the manufacturer

Go to the official support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — enter your service tag or model, select your exact Windows version, and open the driver list. Download the package for the component you need, preferring the newest release marked for your OS. Check the release notes: they tell you what the package fixes and whether it needs prerequisites like a BIOS version or the .NET runtime. Save installers to a dedicated folder and verify the download completed — a truncated file is a classic cause of "setup crashes on launch." For an overview of keeping everything current afterward, see our guide on [updating drivers on Windows 11](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 3: Install setup-based drivers as administrator

For packages with a setup.exe, close all other applications, right-click the installer, and choose Run as administrator. Follow the prompts and reboot when asked — do not postpone the reboot and stack another install on top. OEM installers often extract to `C:\Drivers` or a temp folder before running; if setup fails, check that folder for a secondary installer or logs explaining the failure. If the installer complains about a missing prerequisite, install that first rather than forcing it. After the reboot, verify the new version in Device Manager before moving to the next driver. Order matters: chipset first, then graphics, network, and audio.

### Fix 4: Install INF-only packages through Device Manager

Extract the downloaded archive to a folder. Open Device Manager (Win + X), find the target device — it may sit under its category or under Other devices with a warning — right-click it, and choose Update driver. Select "Browse my computer for drivers," navigate to your extracted folder, check "Include subfolders," and click Next. Windows scans the INF files, matches the hardware ID, and installs. If the device was unknown, it should now appear under its proper category with the manufacturer's name. Confirm the driver version and date on the Driver tab match what you downloaded. This method is the standard path for chipset, SATA, and sensor drivers that ship without setup programs.

### Fix 5: Force-install when Windows claims you already have the best driver

Sometimes Device Manager's automatic search insists the current driver is best even when you know the OEM package is newer. Bypass it: in the Update driver wizard choose "Browse my computer," then "Let me pick from a list of available drivers," click Have Disk, browse to the INF file directly, and select it. This forces Windows to use your file instead of its catalog judgment. It is also the fix when a device stubbornly keeps a generic Microsoft driver after you installed the OEM package. Use it deliberately — force-installing the wrong INF can misconfigure a device — but for the correct OEM file it is safe and effective.

### Fix 6: Handle unsigned or blocked driver packages

Older OEM drivers may fail with a signature error on Windows 11. First, right-click the downloaded file, open Properties, and check for an "Unblock" checkbox on the General tab — files downloaded from the web get flagged, and unblocking resolves many install failures. If the package is genuinely unsigned, you can temporarily disable driver signature enforcement to install it, as described in our guide to [disabling driver signature enforcement](/articles/how-to-disable-driver-signature-enforcement-in-windows-11-24h2/). Re-enable enforcement afterward. Treat unsigned drivers as a last resort for discontinued models; on supported machines, the signed package from the manufacturer is always preferable.

### Fix 7: Verify the installation and clean up

After the final reboot, open Device Manager and check every device you touched: correct manufacturer name, expected version and date, no warning icons. Test the hardware — connect to Wi-Fi, play audio, plug in a USB device — because a driver that installs but does not function is not done. Keep the downloaded packages in your folder for a month in case you need to reinstall, and delete the temp extraction folders. If a device still misbehaves after a correct manual install, the fault is likely the hardware or a deeper OS issue, not the install procedure. Microsoft's Windows support hub documents additional device troubleshooting for those cases.

## Closing

Manual OEM driver installation is a precision task, not a difficult one: exact model, official source, right install method for the package type, and verification afterward. Master the two paths — setup programs and INF-via-Device-Manager — and you will never need a third-party driver tool again. Your laptop runs on drivers tuned for its exact hardware, which is exactly how the manufacturer intended it.
