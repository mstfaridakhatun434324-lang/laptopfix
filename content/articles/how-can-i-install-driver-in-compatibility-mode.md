---
title: "How to Install a Driver in Compatibility Mode on Windows"
slug: how-can-i-install-driver-in-compatibility-mode
date: 2026-10-11
categories: ["drivers"]
tags: ["compatibility mode", "driver install", "legacy driver", "windows 11"]
description: "Need an old driver to run on Windows 11? How to install drivers in compatibility mode safely, and when this trick actually works."
thumbnail: "/images/thumbs/how-can-i-install-driver-in-compatibility-mode.webp"
faqs:
  - q: "What does compatibility mode actually do to a driver installer?"
    a: "It lies to the installer about which Windows version is running. The setup program checks the OS version before proceeding, and compatibility mode reports an older version like Windows 8 or 7 so the version check passes. It doesn't change the driver code itself — if the driver fundamentally can't run on a modern kernel, compatibility mode won't save it."
  - q: "Is installing a driver in compatibility mode safe?"
    a: "Generally yes if the driver comes from the hardware manufacturer and you have a restore point. The risk is real but small: an incompatible kernel driver can cause blue screens. Always create a system restore point first, and avoid compatibility mode for antivirus, disk encryption, or storage controller drivers, where a bad install can block booting."
  - q: "Why won't my old printer or scanner driver install on Windows 11?"
    a: "Most old installer packages include an explicit OS version check that fails on Windows 11, even when the driver itself would work fine. Compatibility mode exists precisely for this case. It also helps with installers that look for features removed from modern Windows, like the old driver store layout."
  - q: "What should I try if compatibility mode doesn't fix the driver?"
    a: "Extract the driver's .inf files and install them manually through Device Manager, which skips the installer's version check entirely. Check the Microsoft Update Catalog for a newer signed version of the same driver, or look for a community-modified driver package. As a last resort, run the device through a virtual machine with the older OS."
---

Some hardware outlives its software. The printer, scanner, audio interface, or specialty controller that worked perfectly on Windows 7 or 8 now refuses to install on Windows 10 or 11 — not because the driver is broken, but because the installer was programmed to reject any operating system it doesn't recognize. Compatibility mode is Windows' built-in answer to exactly that problem: it convinces the installer it's running on the older OS, letting the version check pass.

It's worth understanding what compatibility mode can and cannot do. It changes the environment the installer sees — reported OS version, some legacy API behaviors — but it does not rewrite the driver. A user-mode driver for a printer will usually sail through. A kernel-mode driver written for the Windows 7 driver model may install and then blue-screen, because the kernel underneath really is different. Used with that understanding (and a restore point), it's one of the most useful legacy-hardware tricks in Windows.

This guide covers the two ways to apply it — the compatibility troubleshooter and the manual properties setting — plus the manual `.inf` fallback for installers that still refuse, and the safety rails that keep a legacy driver from taking down your system. If you need the raw driver files first, our guides to [downloading Dell drivers for Windows 11](/articles/how-can-i-download-dell-drivers-for-windows-11/) and [downloading Lenovo drivers for Windows 11](/articles/how-to-download-lenovo-drivers-for-windows-11/) cover the official sources.

## Why this happens

- **Installers hard-code OS version checks.** A setup program from 2014 checks "is this Windows 7 or 8?" and aborts — when it sees Windows 11, even if the driver payload would run fine.
- **Manufacturers abandoned the hardware.** When a vendor stops updating drivers, the last released installer is frozen in time with its old version checks intact.
- **The driver model changed.** Windows 10 and 11 tightened driver signing and deprecated some legacy interfaces; older installers trip over these even when a compatible driver exists inside the package.
- **16-bit installer stubs still linger.** Some very old packages wrap their setup in 16-bit code that 64-bit Windows can't execute at all — compatibility mode can't fix this one.
- **Unsigned drivers are blocked.** 64-bit Windows requires driver signatures; old installers that bundle unsigned drivers fail regardless of compatibility settings.
- **The installer expects removed components.** Legacy frameworks or control-panel applets the installer depends on may not exist anymore, causing silent or cryptic failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Create a restore point first

Non-negotiable before installing any legacy driver. This is your undo button.

1. Press **Win + S**, type **Create a restore point**, and open it.
2. Select your system drive, click **Create**, and name it something like "Before legacy driver install."
3. Wait for confirmation. If anything goes wrong later, **System Restore** from this same dialog rolls the driver state back.
4. Keep the driver's original installer file somewhere safe — you'll want it if you need to retry with different settings.

### Fix 2: Run the Program Compatibility Troubleshooter

The guided path — Windows picks the settings for you.

1. Right-click the driver installer (the `.exe` or `.msi`) and choose **Troubleshoot compatibility** — on Windows 11, it's under **Show more options** in the right-click menu.
2. Select **Try recommended settings**. Windows will typically suggest an older OS version based on the installer's metadata.
3. Click **Test the program** — the installer launches with the compatibility shim applied. Proceed through the installation.
4. When asked whether the fix worked, answer honestly: **Yes** saves the settings for next time; **No** lets you try different modes manually (Fix 3).

### Fix 3: Set compatibility mode manually

When the troubleshooter guesses wrong, set the mode yourself — this is the precise, repeatable method.

1. Right-click the installer > **Properties** > **Compatibility** tab.
2. Check **Run this program in compatibility mode for** and choose the OS the driver was built for — **Windows 8** first for most 2012–2015 hardware, **Windows 7** for older gear. Pick the newest OS the driver officially supported.
3. Also check **Run this program as an administrator** — driver installers need elevated rights, and this removes a whole class of permission failures.
4. Click **OK**, double-click the installer, and proceed. If it still fails, retry with the next-older OS in the list; don't jump straight to Windows XP or 95, which apply heavier shims.

### Fix 4: Extract and install the .inf manually

Some installers fail no matter the shim — often it's the installer wrapper, not the driver. Bypass it entirely.

1. Extract the installer with a tool like 7-Zip (right-click > **7-Zip > Extract**) — many `.exe` installers are just self-extracting archives containing `.inf`, `.sys`, and `.cat` files.
2. Open **Device Manager**, find the device (it may sit under **Other devices** as an unknown device), right-click > **Update driver** > **Browse my computer for drivers**.
3. Point it at the extracted folder containing the `.inf` file and click Next. Device Manager installs the driver directly, skipping the version check that blocked the installer.
4. If Windows warns the driver is unsigned, you'll need to temporarily disable driver signature enforcement from the advanced startup menu — do this only for hardware you trust, and re-enable afterward.

### Fix 5: Check the Microsoft Update Catalog for a newer signed build

Before fighting a 2013 installer, check whether Microsoft already hosts a working driver for your hardware.

1. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for your device name or hardware ID (from Device Manager > device **Properties > Details > Hardware Ids**).
2. If a newer driver package exists, download the `.cab`, extract it, and install via Device Manager as in Fix 4.
3. Catalog drivers are Microsoft-signed and version-checked against modern Windows — they install cleanly where vendor abandonware fails.
4. This is especially productive for network adapters, printers, and card readers, which Microsoft often re-packages long after vendors stop.

### Fix 6: Disable memory integrity temporarily for legacy drivers

Windows 11's Memory Integrity (HVCI) blocks drivers that use incompatible techniques — a common silent killer for old kernel drivers.

1. Go to **Settings > Privacy & security > Windows Security > Device security > Core isolation**.
2. Toggle **Memory integrity** off and restart.
3. Retry the driver installation (Fix 3 or 4).
4. Once the driver works, try re-enabling Memory integrity — if the driver breaks again, you've found an incompatibility you'll have to live with, and you should weigh the security tradeoff carefully. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the current core-isolation behavior if you need the official details.

### Fix 7: Know when to stop — the virtual machine escape hatch

Some drivers will never run on a modern kernel, and recognizing that saves hours.

1. If the driver installs but causes **blue screens** (especially `DRIVER_IRQL_NOT_LESS_OR_EQUAL` referencing the driver's `.sys` file), it's fundamentally incompatible — uninstall it in Safe Mode and restore your restore point.
2. For must-have legacy hardware (old scanners, lab equipment, industrial controllers), run the device through a **virtual machine** with the older Windows version installed, passing the USB device through to the VM.
3. VirtualBox and Hyper-V both support USB passthrough; the VM's older OS runs the original driver natively with zero shims.
4. This is the professional answer for irreplaceable hardware — stable, repeatable, and it keeps the legacy driver quarantined away from your main system's kernel.

## Closing

Compatibility mode is a version-check bypass, not a time machine: it rescues drivers whose only sin is an outdated installer, and it can't resurrect drivers the modern kernel genuinely can't host. Start with the troubleshooter, set the mode manually when it guesses wrong, fall back to raw `.inf` installation, and keep a restore point under everything. Used that way, it keeps perfectly good hardware earning its keep years after the manufacturer moved on.
