---
title: "How to Fix SYSTEM_SERVICE_EXCEPTION on an HP Laptop"
slug: how-to-fix-system-service-exception-on-hp-laptop
date: 2026-10-09
categories: ["windows-errors"]
tags: ["bsod", "system service exception", "hp laptop", "drivers"]
description: "SYSTEM_SERVICE_EXCEPTION blue screen on your HP laptop? Usually a driver or HP utility gone wrong. Here's the exact fix order that works."
thumbnail: "/images/thumbs/how-to-fix-system-service-exception-on-hp-laptop.webp"
faqs:
  - q: "What causes SYSTEM_SERVICE_EXCEPTION on HP laptops?"
    a: "Almost always a driver — HP's own utility software, Realtek audio drivers, outdated Intel chipset or storage drivers, or a recently installed third-party app. Faulty RAM is possible but far less common; suspect drivers first."
  - q: "Will updating my HP drivers fix it?"
    a: "Very often, yes. HP Support Assistant and the HP drivers page deliver firmware and driver updates that fix known crash causes. Update the chipset, storage (IRST), audio, and graphics drivers, plus the BIOS if HP lists one newer than yours."
  - q: "Can I fix this without reinstalling Windows?"
    a: "Yes in most cases. Driver updates, removing conflicting HP utilities, SFC/DISM repairs, and a memory test resolve the large majority of SYSTEM_SERVICE_EXCEPTION crashes without a reinstall. Reinstallation is a last resort."
  - q: "How do I know which driver crashed?"
    a: "Open Event Viewer and check Windows Logs > System for the critical error entry around the crash time — it often names the failing driver file (like rtwlanu.sys). A memory dump analyzed with WinDbg gives the definitive answer."
---

`SYSTEM_SERVICE_EXCEPTION` is one of the most common blue screens on HP laptops, and it almost always points to one thing: a driver misbehaving. That could be a driver Windows Update just replaced, an HP utility loading at startup, or a third-party driver that hasn't kept up with a recent Windows 11 update. Windows is telling you a system service ran into something it couldn't handle.

HP laptops have a few quirks that make this error show up more often than on other brands — bundled HP support utilities, custom audio drivers, and OEM-specific storage drivers. The good news is that means the fix path is well-mapped: work through the fixes below in order, and resist the urge to jump straight to a Windows reinstall.

## Why this happens

- **HP Support Assistant or other HP utilities crashing at driver level**: HP bundles several background utilities with its laptops. When one of these loads a kernel-mode component that conflicts with a Windows update, you get this blue screen on boot or shortly after login.
- **Realtek or Conexant audio drivers**: HP laptops commonly ship with customized Realtek or Conexant audio drivers. These are frequent SYSTEM_SERVICE_EXCEPTION culprits, especially after a Windows feature update replaces part of the driver stack.
- **Outdated Intel Rapid Storage Technology (IRST) driver**: The IRST storage driver is a classic cause of this exact stop code. HP sometimes ships an older IRST version that breaks when Windows updates the storage stack underneath it.
- **Windows Update-installed driver replacements**: Windows Update silently replaces manufacturer drivers with its own generic versions. These replacements sometimes conflict with HP-specific hardware, producing this crash within a day or two of an update.
- **Recently installed third-party drivers or software**: VPN clients, antivirus products, and RGB or peripheral utilities install kernel drivers. One bad update to any of them is enough to trigger 0x3B.
- **Failing RAM (less common)**: Memory corruption can make a perfectly good driver crash. It's rarer than driver causes, but worth testing once driver fixes haven't helped.
- **Corrupted system files**: A failed or interrupted Windows update can damage the files this system service depends on.

## How to fix it

Work through these in order — cheapest, most likely fixes first.

### Fix 1: Boot into Safe Mode and identify recent changes

Start by getting into a stable state so you can work. If Windows boots far enough, Safe Mode loads only the essential drivers, which usually avoids the crash.

1. Hold **Shift** while clicking **Power** > **Restart** from the sign-in screen (or the Start menu if you can get there).
2. Choose **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need internet).
4. Once in Safe Mode, open **Settings** > **Windows Update** > **Update history** and check whether an update or driver landed in the last few days — that timing is your biggest clue.

If you can't reach Safe Mode through the sign-in screen, force it: power off the laptop mid-boot three times in a row to trigger Automatic Repair, then follow **Troubleshoot** > **Advanced options** > **Startup Settings**.

### Fix 2: Update drivers with HP Support Assistant

HP's own tool is the fastest way to get drivers that are actually tested against your model, as detailed in our [HP driver update guide](/articles/system-service-exception-windows-11-fix/).

1. In Safe Mode with Networking (or normal mode if stable), open **HP Support Assistant** from the Start menu. If it's missing, install it from [HP's support site](https://support.hp.com/us-en).
2. Go to **My devices**, select your laptop, and click **Updates**.
3. Install every available update — prioritize **BIOS**, **chipset**, **Intel RST / storage**, **audio**, and **graphics** updates.
4. Restart normally and watch for the crash. A BIOS update alone resolves this error on a surprising number of HP models, since it often fixes firmware-level timing the driver was tripping on.

Keep the charger plugged in during the BIOS flash and don't touch the keyboard while it runs.

### Fix 3: Roll back or update the audio driver

HP's customized Realtek or Conexant audio driver is the single most common driver cause of this stop code on HP machines.

1. Press **Windows + X** and open **Device Manager**.
2. Expand **Sound, video and game controllers**, right-click your audio device, and choose **Properties**.
3. Go to the **Driver** tab. If the crash started right after a driver change, click **Roll Back Driver**.
4. If rollback isn't available, click **Update driver** > **Search automatically for drivers** — or better, grab the audio driver from HP's support page for your exact model.
5. As a test: if the crash happens on boot, try disabling the audio device in Device Manager (right-click > **Disable device**) and restart. If the crashes stop, you've found your culprit and the fix is a clean audio driver install.

### Fix 4: Update the Intel RST storage driver

The IRST driver sits in the storage path, and a stale version crashes the whole system service when Windows touches the disk in a way it doesn't expect.

1. In **Device Manager**, expand **Storage controllers** and note your IRST driver version under **Properties** > **Driver**.
2. Visit [HP's support site](https://support.hp.com/us-en), enter your model, and download the latest **Intel Rapid Storage Technology driver**.
3. Install it (reboot when prompted). Alternatively, the Intel driver tool at [Intel's support page](https://www.intel.com/content/www/us/en/support/detect.html) can detect and update chipset and storage drivers automatically.
4. Restart and use the laptop normally for a day. Storage-driver crashes often appear under disk load, so copy some large files around to stress it.

### Fix 5: Uninstall recently added third-party software

VPN clients, third-party antivirus, and system "optimizers" install kernel drivers that are notorious for 0x3B crashes.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Sort by install date and look at anything added in the week before the crashes started.
3. Uninstall suspects one at a time — start with VPNs, third-party security software, and anything claiming to "boost" or "clean" your PC.
4. After each uninstall, restart and test. If removing something fixes it, reinstall only if you truly need it, and grab the latest version from the vendor.

Windows Defender is a full antivirus on its own, so removing a third-party one doesn't leave you unprotected.

### Fix 6: Run SFC and DISM to repair system files

If an update damaged system files, this repair pass fixes them without touching your data.

1. Press **Windows + X** and open **Terminal (Admin)** (or **Command Prompt (Admin)**).
2. Run: `sfc /scannow` and wait for it to finish (15-30 minutes).
3. Then run: `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store SFC draws from.
4. Run `sfc /scannow` once more, then restart.

These commands are safe — they never touch your personal files.

### Fix 7: Test your RAM with Windows Memory Diagnostic

Once drivers and files are ruled out, check the hardware.

1. Press **Windows + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The test runs before Windows loads (10-30 minutes).
3. When Windows boots back up, check the result in **Event Viewer** > **Windows Logs** > **System**, filtering for source **MemoryDiagnostics-Results**.

HP also ships its own test: reboot and tap **Esc** repeatedly, then choose **F2** for **HP PC Hardware Diagnostics UEFI** and run the **Memory Test** — it's more thorough than Windows' built-in one. If either test finds errors, the fix is a RAM replacement (contact HP support if the laptop is under warranty; don't open a sealed chassis yourself if it would void coverage).

## Closing

SYSTEM_SERVICE_EXCEPTION on an HP laptop is a driver problem roughly nine times out of ten, and the HP-specific updates in Fixes 2-4 resolve most cases within an hour. If you've worked through all seven fixes and the crashes persist — especially if the memory test shows errors or the crash happens with every audio device disabled — you're likely looking at a hardware fault, and that's when an HP support ticket or warranty claim becomes the right move rather than more software troubleshooting. (Our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers every boot method.)
