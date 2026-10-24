---
title: "How to Fix a Scanner Not Working on an ARM Laptop"
slug: scanner-not-working-arm-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["scanner not working", "arm laptop", "snapdragon laptop", "wia driver", "windows 11"]
description: "Scanner not detected on your ARM laptop? Learn why scanner drivers fail on Snapdragon PCs and how to get scanning working with fixes that actually stick."
thumbnail: "/images/thumbs/scanner-not-working-arm-laptop.webp"
faqs:
  - q: "Why won't my scanner work on my Snapdragon laptop?"
    a: >
      Scanner drivers are kernel-mode software, and kernel drivers must be written specifically for ARM64 — they can't be emulated like apps. If the manufacturer never released an ARM64 driver, Windows 11 can't talk to the scanner over USB. Newer models often have one; older ones usually never will.
  - q: "Can Windows Scan work without a manufacturer driver?"
    a: >
      No — Windows Scan uses the same driver stack, so it can't bypass a missing ARM64 driver. But network scanning is different: if your all-in-one has Wi-Fi, scan through its built-in web page with no Windows driver at all, as covered in Fix 5.
  - q: "How do I check whether an ARM64 scanner driver exists?"
    a: >
      Search your exact model on the manufacturer's support page and look for a Windows 11 ARM64 driver entry. If only x64 drivers are listed, there is no ARM support. In Device Manager, an unknown device with a yellow warning after connecting the scanner points to the same conclusion.
  - q: "Will an old scanner ever get an ARM64 driver?"
    a: >
      Honestly, probably not — manufacturers rarely back-port drivers to discontinued models. If your scanner is several years old and has no ARM64 driver today, plan around it. The network-scan workaround in Fix 5 is the realistic path forward.
---

You plug the scanner in, Windows plays its connection sound, and then nothing happens. The device never appears in Windows Scan, the manufacturer's utility reports no scanner found, and Device Manager shows a yellow warning triangle. If you recently moved from an Intel laptop to a Snapdragon ARM machine, this is a rude surprise: hardware that worked for years suddenly acts dead. It isn't your cable — the problem runs deeper, and knowing why saves hours of pointless reinstalls. Much like [Telegram Desktop issues on ARM Windows](/articles/telegram-desktop-arm-windows-issues/), the root cause is an architecture gap, not a broken device.

Here is the uncomfortable truth: scanner drivers are kernel-mode drivers, and kernel code cannot be emulated. Windows 11 on ARM runs x64 apps through its Prism emulator, but anything that talks directly to hardware must be compiled natively for ARM64 — no exceptions. Without an ARM64 driver from the manufacturer, Windows cannot drive the scanner over USB. It is the same class of problem as [missing Windows Copilot Runtime components](/articles/windows-copilot-runtime-components-missing/): an expected software layer is simply absent, and the fix must work around that absence.

This guide is honest about what can and cannot be fixed. First we'll confirm the diagnosis in Device Manager so you stop chasing settings that were never the problem. Then we'll hunt for an ARM64 driver if one exists, try Windows' built-in scan stack, and set up network scanning that sidesteps the driver entirely. It shares troubleshooting DNA with [Cocreator issues in Photos](/articles/photos-cocreator-not-working/): ARM machines missing a software piece their Intel cousins take for granted, where diagnosis must come before action.

## Why this happens

- **Kernel drivers can't be emulated:** Apps run under Prism emulation, but drivers execute inside the Windows kernel, where only native ARM64 code is allowed.
- **Manufacturers skipped ARM64 for old models:** New drivers cost money, and discontinued scanners almost never get ports to new architectures.
- **WIA and TWAIN both need the driver:** Windows Scan (WIA) and pro apps (TWAIN) both funnel through the same missing driver.
- **Windows Update can't conjure drivers:** It only offers drivers the manufacturer submitted; if none exists for ARM64, none will appear.
- **The USB sound misleads you:** Windows detects the device's USB identity fine — it's the functional driver binding that fails.
- **All-in-ones have a split personality:** The printer half may work via a universal driver while the scanner half stays dead, since they use separate stacks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the real problem in Device Manager

Prove this is a driver-architecture issue, not a dead cable or port. Five minutes here prevents hours of wasted effort.

1. Connect the scanner, then open Device Manager (right-click Start > Device Manager).
2. Check "Imaging devices" and "Other devices" for your scanner or an unknown device with a yellow triangle.
3. Right-click it > Properties > Details, and note the Hardware Ids (VID/PID) for later searching.
4. Read the Device status message — "drivers for this device are not installed" confirms the diagnosis.
5. Try one different USB port and cable to rule out trivial causes, then move on.

### Fix 2: Install the manufacturer's ARM64 driver (if one exists)

Some newer scanners do have ARM64 drivers buried on the support page. This is the only true fix when it applies — check carefully before assuming the worst.

1. Find your scanner's exact model number on its label.
2. Search the model on the manufacturer's support site and open its driver downloads.
3. Look specifically for a Windows 11 ARM64 driver — x64-only listings mean no ARM support.
4. Download the ARM64 package, disconnect the scanner, run the installer, and reboot.
5. Reconnect the scanner; the yellow triangle should be gone and Windows Scan should detect it.

### Fix 3: Try Windows' built-in scan stack

Windows 11 ships generic WIA infrastructure that supports many scanners — provided a basic driver binding exists. One attempt costs nothing.

1. Install the free "Windows Scan" app from the Microsoft Store if needed.
2. Connect the scanner and open Windows Scan to see if it appears in the Scanner list.
3. If it appears, run a low-resolution test scan to confirm the full path works.
4. If Windows Scan can't see it either, the driver gap is confirmed — no built-in path will help.

### Fix 4: Check Windows Update's optional drivers

Sometimes a manufacturer submits an ARM64 driver to Microsoft without advertising it. The optional-drivers list is the one place it might quietly appear.

1. Go to Settings > Windows Update > Advanced options > Optional updates.
2. Expand "Driver updates" and look for your scanner brand or model.
3. If found, install it, reboot, and test with Windows Scan again.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents this optional-updates flow if you get stuck.
5. If nothing scanner-related appears, close this door and move to the network workaround.

### Fix 5: Set up network scanning (the real workaround)

If your all-in-one has Wi-Fi or Ethernet, scanning over the network needs no Windows driver at all — the device's firmware does the work and your laptop just receives a file. This keeps most abandoned all-in-ones alive on ARM.

1. Connect the all-in-one to Wi-Fi using its front-panel network setup menu.
2. Print a network configuration page from the device to get its IP address.
3. Type that IP into your laptop's browser — most devices serve a web page with a Scan tab.
4. Use web scan to save documents as PDF or JPEG downloads, no driver involved.

### Fix 6: Share a scanner from another PC (or plan a replacement)

A USB-only scanner with no network option and no ARM64 driver will never work on the ARM laptop directly. But you still have practical options short of throwing it away.

1. If any Intel/AMD Windows PC is in the house, connect the scanner there and share it over the network.
2. Scan on the older PC and move files via OneDrive, a USB stick, or your home network.
3. When buying a replacement, verify ARM64 driver support on the driver page before purchasing.
4. The [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), and [Lenovo](https://support.lenovo.com/us/en) support pages show which bundled all-in-one drivers include ARM64 builds.

## Closing

A scanner that won't work on an ARM laptop feels like betrayal by trusted hardware, but it's really an industry gap: kernel drivers can't be emulated, and older devices never got ARM64 ports. Diagnose it once in Device Manager, grab an ARM64 driver if your model has one, and otherwise lean on network scanning — the workaround that genuinely works. The scanner isn't broken; the software bridge to it was simply never built.
