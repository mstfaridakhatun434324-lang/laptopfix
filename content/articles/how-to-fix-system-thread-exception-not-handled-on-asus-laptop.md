---
title: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on an ASUS Laptop — Fixed Step by Step"
slug: how-to-fix-system-thread-exception-not-handled-on-asus-laptop
date: 2026-09-03
categories: ["windows-errors"]
tags: ["asus", "bsod", "system-thread-exception"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED blue screen on your ASUS laptop? Usually a graphics driver. Follow these 7 steps to fix it properly."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled-on-asus-laptop.webp"
faqs:
  - q: "Which driver causes SYSTEM_THREAD_EXCEPTION_NOT_HANDLED most often?"
    a: "On ASUS laptops it is the graphics driver more than anything else — nvlddmkm.sys for NVIDIA GPUs, igdkmdnd64.sys or igdkmdn64.sys for Intel graphics, and atikmdag.sys for AMD. The error text on the blue screen sometimes names the file in parentheses. Audio drivers (rtkvhd64.sys) and ASUS's own ATK/Armoury Crate drivers are the next most common culprits."
  - q: "Can I fix this without losing my files?"
    a: "Yes. Every fix in this guide preserves your files — we are updating or reinstalling drivers, repairing system files, and adjusting settings. Only the last-resort options like a Windows reset touch your data, and even then you can choose to keep personal files. Still, if the laptop boots at all, back up anything irreplaceable before you start."
  - q: "Why does it happen on ASUS laptops specifically after updates?"
    a: "ASUS ships custom-tuned drivers through MyASUS and Armoury Crate. A Windows 11 update can silently replace those tuned drivers with generic versions, or the update changes a system component the ASUS driver was not expecting. The result is a system thread that throws an exception the kernel cannot handle — hence the blue screen, often right after login."
  - q: "Could ASUS Live Update or MyASUS drivers be the cause?"
    a: "Yes, on ASUS laptops the prime suspects are often the NVIDIA graphics driver, the ASUS System Control Interface, or drivers pushed by MyASUS Live Update. Uninstall the graphics driver with Display Driver Uninstaller in Safe Mode, then reinstall only the version listed on the ASUS support page for your exact model instead of the latest generic release."
---

Few things are as annoying as a laptop that blue-screens with SYSTEM_THREAD_EXCEPTION_NOT_HANDLED right when you are trying to get work done. On ASUS machines — VivoBook, ZenBook, ROG, TUF — this error is a driver problem far more often than a hardware problem, and the graphics driver is suspect number one.

The catch is that you may not be able to stay booted long enough to fix it normally. This guide covers both situations: fixing it from the desktop, and fixing it from Safe Mode when Windows will not stay up.

## Why this happens

- **A broken graphics driver.** The most common cause by far. A Windows update replaced your ASUS-tuned GPU driver with a generic or mismatched version, or the driver install itself corrupted.
- **Conflicting ASUS utility drivers.** ATK Package, Armoury Crate services, and MyASUS components install kernel drivers that can clash after major Windows updates.
- **Outdated BIOS or chipset firmware.** Older ASUS BIOS versions mishandle power-state transitions the new Windows build expects, crashing system threads.
- **Corrupted system files.** Interrupted updates damage the kernel components that manage system threads.
- **Faulty RAM.** Less common, but memory errors can corrupt thread execution and produce exactly this stop code.
- **Overclocked or overheating GPU.** ROG and TUF owners who tweaked GPU settings in Armoury Crate can push the card into instability that shows up as this error.
- **Fast Startup saving a bad driver state.** The hybrid shutdown can preserve a crashed driver state across reboots, making the blue screen repeat every boot.

## How to fix it

Work through these in order. If Windows will not stay booted, start in Safe Mode (hold **Shift** while clicking **Restart** → **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart** → press **4**).

### Fix 1: Boot into Safe Mode and note the failing driver

Before changing anything, identify the culprit. The blue screen often names it.

1. When the blue screen appears, look for a file name in parentheses under the stop code, like `nvlddmkm.sys` or `rtkvhd64.sys`. Photograph it with your phone.
2. Boot into Safe Mode as described above. Safe Mode loads only basic drivers, so the crashing driver stays dormant.
3. Open **Device Manager** (**Win + X** → **Device Manager**) and look for devices with yellow warning icons — these are your prime suspects.
4. If no file was shown, check the minidump later; for now, proceed with the graphics driver, which is the cause in most ASUS cases I see.

### Fix 2: Clean-reinstall the graphics driver

A plain driver update often is not enough — you need the old files fully removed first.

1. In Safe Mode (or normal mode if stable), download Display Driver Uninstaller (DDU) and the correct GPU driver: NVIDIA owners get it from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), Intel owners from the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Disconnect from the internet so Windows Update cannot reinstall a driver mid-process.
3. Run DDU, choose **GPU** and your brand, then click **Clean and restart**.
4. After the reboot, install the driver you downloaded. For ASUS laptops, the MyASUS version is fine, but the direct NVIDIA/Intel/AMD release is usually newer.
5. Reconnect to the internet and restart once more.

### Fix 3: Update ASUS system drivers via MyASUS

ASUS-specific drivers — chipset, ATK, audio — need the ASUS versions, not generic ones.

1. Open **MyASUS** from the Start menu (install it from the Microsoft Store if missing).
2. Go to **System Update** or **Live Update** and install every pending driver and BIOS update.
3. Pay special attention to **chipset**, **audio**, and **ATK Package** entries.
4. Restart when prompted, even if the laptop seems fine — driver installs finalize on reboot.
5. If Armoury Crate is installed, open it and check for its own updates too; stale Armoury Crate services crash system threads on ROG/TUF models.

### Fix 4: Run SFC and DISM from Safe Mode

Corrupted system files keep the error alive even after driver fixes.

1. Open **Terminal (Admin)** from Safe Mode (**Win + X** → **Terminal (Admin)**).
2. Run `sfc /scannow` and let it finish completely.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` — this needs internet, so use Safe Mode with Networking (press **5** instead of **4** at the Startup Settings screen) if required.
4. Run `sfc /scannow` a second time to verify, then reboot normally.

### Fix 5: Disable Fast Startup and reset GPU tweaks

If the crash happens on every cold boot but not on restarts, Fast Startup is preserving a bad state. And if you ever touched GPU settings, undo them.

1. Press **Win + R**, type `powercfg.cpl`, press **Enter** → **Choose what the power buttons do** → **Change settings that are currently unavailable** → uncheck **Turn on fast startup (recommended)** → **Save changes**.
2. Open **Armoury Crate** → **GPU** or **Manual mode** and reset any overclock or custom fan/voltage curves to defaults.
3. In **Device Manager**, expand **Display adapters**, right-click your GPU → **Properties** → **Power Management**, and make sure nothing unusual is set.
4. Shut down fully, wait 10 seconds, and power on.

### Fix 6: Test the memory

If driver work has not helped, rule out bad RAM before assuming the motherboard is at fault.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, and choose **Restart now and check for problems**.
2. Let the full pass complete. Errors here mean a RAM problem, not a driver problem.
3. On models with removable RAM, power off, reseat the modules, and retest. If errors persist on one stick, remove it and run on the other to isolate the bad module.
4. Many thin ASUS models have soldered RAM — errors there mean a warranty or repair-shop conversation.

### Fix 7: Update the BIOS and do an in-place repair

The last two moves: firmware, then a repair install that keeps everything.

1. In MyASUS or on the ASUS support site, check your BIOS version against the latest for your exact model and update if behind (AC adapter plugged in, do not interrupt).
2. If crashes continue, create [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11), run setup from inside Windows, and choose **Upgrade this PC now** with **Keep personal files and apps**.
3. This reinstalls Windows core files while preserving your data and programs — it fixes deep corruption that SFC cannot reach.
4. After the repair, reinstall the ASUS drivers from MyASUS before anything else.

## Closing

On ASUS laptops, SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is a driver story nine times out of ten, and the graphics driver is the usual villain. The DDU clean-reinstall in Fix 2 resolves more of these cases than everything else combined, so do not skip it in favor of a quick Device Manager update. Work the list in order, test stability for a day between major changes, and you will have it nailed down. If your crashes mention a verifier driver instead, see our guide on [DRIVER_VERIFIER_IOMANAGER_VIOLATION on ASUS](/articles/how-to-fix-driver-verifier-iomanager-violation-on-asus-laptop/) — and if the screen goes black rather than blue, the [black screen after update](/articles/how-to-fix-black-screen-after-windows-update-on-asus-laptop/) guide is the right next stop.
