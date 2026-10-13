---
title: "How to Install a Driver in Compatibility Mode on Windows 10"
slug: how-to-install-driver-in-compatibility-mode-on-windows-10
date: 2026-10-09
categories: ["drivers"]
tags: ["compatibility mode driver", "old driver windows 10", "legacy driver install"]
description: "Need an older driver on Windows 10? Learn how to run any driver installer in compatibility mode so legacy hardware works again."
thumbnail: "/images/thumbs/how-to-install-driver-in-compatibility-mode-on-windows-10.webp"
faqs:
  - q: "What does compatibility mode actually do for a driver installer?"
    a: "It lies to the installer about which Windows version is running, so setup programs that refuse to run on Windows 10 will proceed as if they were on Windows 7 or 8. It also adjusts permissions and display handling. The installed driver itself still runs on Windows 10's kernel."
  - q: "Is it safe to install an old driver in compatibility mode?"
    a: "Generally yes for well-known hardware from reputable vendors, but old drivers can be unstable or lack security fixes. Create a restore point first, and prefer the newest driver your manufacturer offers. Compatibility mode is a bridge for abandoned hardware, not a first choice."
  - q: "Why does the installer say the operating system is not supported?"
    a: "Many legacy installers check the Windows version number before doing anything and quit if it is not on their approved list. Compatibility mode changes the version the installer sees, which bypasses that check without modifying any files If the installer still refuses, try an older compatibility target such as Windows 7, since some installers check for a specific version rather than just a non-Windows-10 one."
  - q: "Can compatibility mode fix a driver that installs but does not work?"
    a: "Sometimes. If the installer placed the right files but configured them for the wrong OS behavior, reinstalling in compatibility mode can set correct registry values. But if the driver fundamentally cannot talk to Windows 10's kernel, no compatibility setting will save it — you need a newer driver."
---

Some hardware never got a proper Windows 10 driver. The printer is from 2014, the scanner vendor went quiet years ago, or the laptop maker only ever published a Windows 7 package — and now the installer quits with "this operating system is not supported." Before you give up on the hardware, try compatibility mode: it convinces the old installer that it is running on an earlier Windows, and it works far more often than people expect.

Compatibility mode does not magically rewrite the driver. It changes what the installer sees — the reported Windows version, certain permissions, display scaling — so legacy setup programs complete their job instead of bailing out. This guide covers running the installer in compatibility mode, forcing the driver through Device Manager, and what to do when the old driver misbehaves afterward.

## Why this happens

- **Vendor abandoned the hardware:** Manufacturers stop updating drivers for old products, so no native Windows 10 package was ever released.
- **Version check in the installer:** Legacy setup programs hard-code a list of supported Windows versions and refuse to run on anything newer.
- **16-bit installer components:** Very old installers contain 16-bit code that cannot execute on 64-bit Windows 10 at all.
- **Unsigned driver blocks:** Old drivers lack the digital signatures Windows 10 requires, so the OS rejects them even if the installer runs.
- **INF targets wrong OS section:** The driver's INF file may only declare install sections for Windows 7 or 8, leaving Windows 10 with nothing to match.
- **UAC and permission assumptions:** Legacy installers expect administrator behavior from the XP/Vista era and fail under modern User Account Control.
- **Removed legacy APIs:** Drivers that depend on Windows APIs removed in Windows 10 cannot function no matter how the installer is launched.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the installer in compatibility mode

This is the core technique and resolves most "not supported on this OS" installer errors.

1. Right-click the driver's setup file (usually `setup.exe`) and choose **Properties**.
2. Open the **Compatibility** tab.
3. Check **Run this program in compatibility mode for** and select **Windows 7** from the dropdown. For very old hardware, try **Windows Vista** or **Windows 8** instead.
4. Also check **Run this program as an administrator** at the bottom.
5. Click **Apply**, then **OK**, and double-click the installer to run it.

If the installer still refuses, try a different compatibility target — some installers specifically want Windows XP (Service Pack 3) or Windows 8. Always create a system restore point before installing legacy drivers, a habit our [driver backup guide](/articles/best-way-to-backup-drivers-before-update/) reinforces for any risky driver work.

### Fix 2: Use the compatibility troubleshooter for stubborn installers

When manual settings fail, Windows' built-in troubleshooter can detect the right combination automatically.

1. Right-click the setup file and choose **Troubleshoot compatibility**.
2. Select **Try recommended settings** and let Windows test-launch the installer.
3. If the program runs, click **Next**, then **Yes, save these settings for this program**.
4. If it does not, choose **Troubleshoot program** instead and answer the questions — especially "the program worked in earlier versions of Windows."

The troubleshooter sometimes picks non-obvious combinations (like 256-color mode or disabled fullscreen optimizations) that manual setup misses.

### Fix 3: Extract the driver and install it through Device Manager

Some installers are too broken for compatibility mode, but the actual driver files inside are fine. Extract and install them directly.

1. Open the installer with an archive tool (many `.exe` installers open in 7-Zip) and extract its contents to a folder, or run the installer with a `/extract` or `/a` switch if the vendor supports it.
2. Open **Device Manager**, find the device, right-click it, and choose **Update driver**.
3. Select **Browse my computer for drivers** and point it at your extracted folder.
4. If Windows says the best driver is already installed, choose **Let me pick from a list**, click **Have Disk**, and select the `.inf` file manually.

This skips the version-checking installer entirely and lets Windows' own driver machinery do the installation. Microsoft documents the manual driver process on the [Windows support site](https://support.microsoft.com/en-us/windows) if you want the official background.

### Fix 4: Temporarily disable driver signature enforcement

Windows 10 blocks unsigned drivers, and nearly all pre-2015 drivers are unsigned. Disable the check just long enough to install.

1. Hold **Shift** while clicking **Restart** (Start > Power > Restart).
2. Go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
3. Press **7** (or **F7**) to choose **Disable driver signature enforcement**.
4. Install your driver now — the check stays off only for this boot session.
5. Restart normally afterward; the installed driver remains in place.

Only do this for drivers you trust from known vendors. Signature enforcement exists to block malware posing as drivers, so never disable it for software from untrusted sources.

### Fix 5: Try the Windows 8.1 driver as a middle ground

If no Windows 10 driver exists but a Windows 8.1 driver does, install that one in compatibility mode — 8.1 drivers are far more likely to work on Windows 10 than Windows 7 ones.

1. Download the newest driver package available for the hardware, preferring Windows 8.1 over 7 or Vista.
2. Run it in compatibility mode for **Windows 8** as described in Fix 1.
3. Test the hardware thoroughly: print a test page, scan a document, or exercise the device's full feature set.

Windows 8.1 shares much more driver architecture with Windows 10 than Windows 7 does, so this middle-ground driver is often rock-solid while the older one crashes.

### Fix 6: Block Windows Update from replacing the legacy driver

Windows Update loves to "helpfully" replace your working legacy driver with a newer generic one that breaks the hardware again.

1. Once the legacy driver works, open **System > Advanced system settings > Hardware tab > Device Installation Settings**.
2. Choose **No (your device might not work as expected)** to stop automatic manufacturer driver downloads.
3. Alternatively, use the **Show or hide updates** troubleshooter to hide the specific driver update.

Our guide to [disabling automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) walks through the Group Policy and registry methods if you want a more permanent block. This step matters: without it, a Tuesday update can silently undo your compatibility-mode victory.

### Fix 7: Accept the limits and find a modern replacement path

If every approach fails — the installer is 16-bit, the driver needs removed kernel APIs, or the device blue-screens Windows 10 — the hardware has genuinely reached end of life.

1. Check whether the device works through a generic class driver: many printers work with Windows' built-in IPP or PCL drivers, and many scanners work via WIA without vendor software.
2. In **Settings > Bluetooth & devices > Printers & scanners**, try **Add device** and let Windows use its inbox driver.
3. For truly dead hardware, a cheap modern USB equivalent often costs less than the hours spent fighting the old driver.

Knowing when to stop is part of troubleshooting. The generic drivers Windows 10 ships with cover a surprising range of legacy peripherals well enough for everyday use.

## Closing

Compatibility mode is the bridge that keeps perfectly good older hardware alive on Windows 10. Run the installer as Windows 7 or 8, fall back to a manual Device Manager install with signature enforcement temporarily off if needed, and then protect your working driver from Windows Update overwrites — that sequence rescues the majority of "unsupported OS" driver situations.
