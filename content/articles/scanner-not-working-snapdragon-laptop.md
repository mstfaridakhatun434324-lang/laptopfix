---
title: "Scanner Not Working on Snapdragon Laptop? 6 Fixes to Try"
slug: scanner-not-working-snapdragon-laptop
date: 2026-10-21
categories: ["ai-pc"]
tags: ["scanner not working", "snapdragon laptop", "wia driver", "twain arm64", "windows scan", "copilot+ pc"]
description: "Get your scanner working on a Snapdragon laptop with six step-by-step fixes: WIA and TWAIN ARM64 drivers, service resets, plus USB and network repair."
thumbnail: "/images/thumbs/scanner-not-working-snapdragon-laptop.webp"
faqs:
  - q: "Why is my scanner not detected on my Snapdragon laptop?"
    a: "Detection failures are usually driver-architecture problems: the scanner's software installed an x64-only WIA or TWAIN driver that ARM64 Windows cannot load. USB power or cable issues are the second most common cause."
  - q: "Does Windows Scan work on ARM laptops?"
    a: "Yes. The built-in Windows Scan app is native ARM64 and works with any scanner that exposes a proper WIA driver. If Windows Scan sees the scanner but the vendor app does not, the vendor's software is the problem, not your laptop."
  - q: "Can I use an old USB scanner with a Copilot+ PC?"
    a: "Often yes, if Windows includes an inbox WIA driver for that model or the vendor released an ARM64 package. Very old scanners whose vendors never updated drivers may only work through basic WIA scanning without the vendor's extra features."
  - q: "Do network scanners work better on Snapdragon laptops?"
    a: "They sidestep USB driver issues entirely. A network scanner using WSD or eSCL/AirScan protocols usually works with zero vendor software — the built-in Windows Scan app picks it up automatically."
---

Your scanner worked fine on your old laptop, but on your new Snapdragon machine it is invisible: Windows Scan finds nothing, the vendor app throws an error, or scans start and freeze halfway. Scanner trouble on ARM laptops is frustrating because everything looks connected — the real failure hides in driver architecture.

Scanning on Windows runs through two driver interfaces, WIA and TWAIN, and both must be ARM64-native on your Copilot+ PC. Vendor installer packages built years ago for x64 often install their ARM-incompatible pieces silently, leaving a scanner that powers on but never talks to Windows.

This guide gives you six fixes in technician order: verify the connection, fix the driver layer, then repair the software. Work through them in sequence and test a scan after each step.

## Why this happens

- **x64-only WIA/TWAIN drivers**: The vendor's installer drops 64-bit Intel scanner drivers that ARM64 Windows cannot load — the scanner is physically fine but logically absent.
- **Broken Windows Image Acquisition service**: The WIA service (stisvc) that brokers all scanning can stall or corrupt, making every scanner vanish at once.
- **USB power or enumeration failure**: Underpowered USB ports, hubs, or aggressive USB power saving prevent the scanner from enumerating properly on ARM laptops.
- **Vendor software incompatibility**: The scanner utility app itself may be an old x86 program with components that fail under Prism emulation, even when the driver is fine.
- **Network discovery blocked**: For Wi-Fi scanners, firewall rules or disabled network discovery block the WSD/eSCL protocols Windows Scan relies on.
- **Stale driver store entries**: Half-removed scanner drivers from previous installs conflict with the new install, a pattern also seen with [missing drivers after ARM upgrades](/articles/drivers-missing-windows-arm/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out the cable, port, and power basics

Before touching drivers, confirm the scanner is actually reaching Windows. ARM laptops with aggressive USB power saving can starve a scanner of power, and a surprising number of "driver problems" are really connection problems.

1. Plug the scanner directly into the laptop — no hub, no dock — using the shortest USB cable you have, preferably the one that came with it.
2. Open **Device Manager** and look under **Imaging devices**; if the scanner appears with a warning icon, note the error code before continuing.
3. In **Settings > Bluetooth & devices > USB**, turn off any battery-saver USB options temporarily, then unplug and replug the scanner.
4. If Device Manager now shows it cleanly, try Windows Scan — a stable direct connection fixes more cases than people expect.

### Fix 2: Restart the Windows Image Acquisition service

WIA is the broker between Windows and every scanner. When stisvc hangs, no scanner is detected regardless of drivers — and a restart takes thirty seconds, making it the cheapest meaningful fix on this list.

1. Press Win+R, type `services.msc`, and find **Windows Image Acquisition (WIA)** in the list.
2. Right-click it, choose **Restart** (or **Start** if it is stopped), and set **Startup type** to **Automatic** in its properties.
3. Also restart the **Shell Hardware Detection** service, which handles device arrival notifications.
4. Open Windows Scan and check whether the scanner now appears — if it does, a stalled service was the entire problem.

### Fix 3: Install the correct ARM64 scanner driver

If WIA is healthy but the scanner still does not appear, the driver layer is wrong. Vendor "universal" installers sometimes skip ARM64 components, so verify and install deliberately rather than trusting the default setup. Canon all-in-one owners should start with the [Canon printer driver guide for Arm64 Windows](/articles/canon-printer-driver-arm64-windows/) — the scanner driver usually ships in the same package.

1. In Device Manager, right-click the scanner under Imaging devices, choose **Update driver > Browse my computer**, and let Windows search — inbox WIA drivers cover many models natively.
2. If that fails, visit the vendor's support site and search your exact model plus "ARM64" or "Windows 11 ARM" — download only a package that explicitly lists ARM64 support.
3. Run the installer as administrator with the scanner connected and powered on, then restart the laptop.
4. Verify in Device Manager that the device shows no warning; if the vendor offers only x64 software, the scanner may be limited to basic WIA scanning without its bonus features.

### Fix 4: Use Windows Scan instead of the vendor app

Vendor scanning utilities are often the weakest link — old x86 code, bundled toolbars, background services that fail under emulation. The built-in Windows Scan app is native ARM64 and talks directly to WIA, bypassing all of it.

1. Open the **Windows Scan** app from the Start menu (install it free from the Microsoft Store if it is missing).
2. Select your scanner from the dropdown — if it appears here but not in the vendor app, the vendor software is the problem.
3. Run a test scan at 300 DPI; if it completes, make Windows Scan your default and uninstall the vendor utility.
4. For document workflows needing OCR or multi-page PDF, pair Windows Scan with a native ARM64 app rather than fighting the vendor's emulator-hostile suite — similar to how isolating [OEM-specific NPU issues](/articles/dell-xps-14-snapdragon-npu-issues/) beats fighting vendor bloatware.

### Fix 5: Fix network discovery for Wi-Fi scanners

Network scanners do not need vendor drivers at all — they use standard protocols. If your Wi-Fi scanner is invisible, Windows is almost certainly blocking discovery rather than missing a driver.

1. Go to **Settings > Network & internet > Advanced network settings > Advanced sharing settings** and turn on **Network discovery** and **File and printer sharing** for your current profile.
2. Check that the laptop and scanner are on the same Wi-Fi band (both on 5 GHz or both on 2.4 GHz) — band mismatches break discovery on some routers.
3. Temporarily disable any third-party firewall to test; if the scanner appears, add an exception for WSD/eSCL traffic instead of leaving the firewall off.
4. In Windows Scan, the scanner should now list itself — network scanning then works driver-free, permanently sidestepping ARM driver concerns.

### Fix 6: Clean the driver store and reinstall from scratch

When a scanner worked once and then broke — or when remnants of an old model conflict with the new one — the driver store holds the damage. A full purge and clean reinstall is the definitive fix. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the driver-store cleanup commands if you want the official reference.

1. Disconnect the scanner, open **Device Manager**, and under Imaging devices right-click the scanner and choose **Uninstall device**, checking **"Attempt to remove the driver for this device"**.
2. In **Print Management** (`printmanagement.msc`) or Device Manager's driver store view, remove any leftover scanner driver packages for that vendor.
3. Restart, reconnect the scanner, and install only the verified ARM64 package from Fix 3 — declining any optional "full feature software" bundles.
4. Test with Windows Scan first, then the vendor app if you need it. For stubborn low-level installs, the manual [INF-based driver install technique](/articles/manually-install-intel-npu-driver-inf/) demonstrates the same careful approach applied to another device class.

## Closing

Scanner problems on Snapdragon laptops look like hardware failures but are nearly always software: the wrong driver architecture, a stalled WIA service, or a vendor app that never learned ARM. Work the connection first, then the service, then the driver — and lean on the native Windows Scan app whenever the vendor's suite fights you. Once the right ARM64 pieces are in place, scanning on a Copilot+ PC is as reliable as it ever was on Intel.
