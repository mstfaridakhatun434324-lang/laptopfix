---
title: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows 10: 7 Fixes That Work"
slug: how-to-fix-system-thread-exception-not-handled-on-windows-10
date: 2026-09-15
categories: ["windows-errors"]
tags: ["windows-10", "bsod", "system-thread-exception"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows 10? It is almost always a driver issue. These 7 fixes walk you from Safe Mode to a clean driver set."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled-on-windows-10.webp"
faqs:
  - q: "Is the fix different on Windows 10 versus Windows 11?"
    a: "The underlying cause — usually a bad graphics or chipset driver — is the same, but the menus differ. Windows 10 uses the classic Control Panel paths and the Start menu right-click for admin Command Prompt instead of Windows Terminal. Safe Mode access is also slightly different. This guide uses Windows 10's exact menus so you are never hunting for a Windows 11 screen that does not exist."
  - q: "My Windows 10 laptop is old. Could this be failing hardware?"
    a: "Possible, and more likely than on a new machine — aging RAM and drying thermal paste are real factors on 5+ year old laptops. But drivers are still the most common cause even on old hardware, and they are free to fix. Work the driver fixes first; if crashes survive a clean driver set plus a memory test, then start budgeting for hardware."
  - q: "Should I just upgrade to Windows 11 instead of fixing this?"
    a: "Only if your hardware supports it and you were planning to anyway. An upgrade will not fix a bad driver — Windows 11 will happily carry the same broken driver forward, and the crashes will follow you. Fix the driver problem first on Windows 10; then upgrade from a stable system if you choose to."
  - q: "Where can I find working older drivers for a Windows 10 laptop?"
    a: "Go to your laptop maker's support page, enter the exact model, and download the drivers listed under Windows 10 — they keep the last tested versions archived. Avoid generic driver-updater programs, which often install mismatched builds. If a newer driver started the crashes, roll back from Device Manager > Properties > Driver tab before hunting for older versions."
---

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows 10 means exactly what it says: a background system thread hit an error it could not handle, and Windows stopped everything. On Windows 10 laptops the culprit is a bad driver in the overwhelming majority of cases — most often graphics, sometimes audio or chipset.

This guide uses Windows 10's actual menus and tools. Work through it in order.

## Why this happens

- **A corrupted or outdated graphics driver.** Still the number one cause on Windows 10, especially after a feature update like 22H2 replaces the manufacturer's driver.
- **Old chipset drivers.** Windows 10 feature updates change kernel interfaces; chipset drivers from 2018 do not always keep up.
- **Failing Windows Update driver swaps.** Windows 10's automatic driver updates can silently replace a working OEM driver with a problematic generic one.
- **Corrupted system files.** Years of updates, interrupted installs, and disk wear damage the files threads depend on.
- **Aging RAM.** On older laptops, memory modules degrade; the resulting corruption produces exactly this stop code.
- **Overheating.** Dust-clogged cooling on an old laptop pushes the GPU/CPU into thermal instability that corrupts driver execution.
- **Third-party driver-level software.** Old VPN clients, virtualization tools, and "driver updater" utilities install kernel drivers that throw unhandled exceptions.

## How to fix it

Work through these in order. If Windows 10 will not stay booted, do the early steps from Safe Mode.

### Fix 1: Boot into Safe Mode and identify the bad driver

Safe Mode loads a minimal driver set, which both stabilizes the machine and narrows the suspect list.

1. Hold **Shift** while clicking **Restart** (from the login screen: click the power icon, hold **Shift**, click **Restart**).
2. Go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**, then press **4** for Safe Mode.
3. Once in, right-click **Start** → **Device Manager** and look for yellow warning icons.
4. Note any `.sys` file named on the blue screen: `nvlddmkm.sys` (NVIDIA), `igdkmdnd64.sys` (Intel), `atikmdag.sys` (AMD), `rtkvhd64.sys` (Realtek audio).
5. Press **Win + R**, type `eventvwr`, and check **Windows Logs** → **System** for red errors just before each crash timestamp.

### Fix 2: Clean-reinstall the graphics driver

The highest-value fix. Use Display Driver Uninstaller for a true clean slate — a standard reinstall leaves the broken files in place.

1. Download DDU and the correct latest driver for your GPU from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), Intel, or AMD.
2. Disconnect from the internet so Windows Update cannot interfere mid-process.
3. Boot into Safe Mode, run DDU, select your GPU brand, click **Clean and restart**.
4. Install the downloaded driver, reconnect to the internet, and restart.
5. Test with whatever used to trigger the crash — video playback, games, or external monitor use.

### Fix 3: Update chipset and remaining drivers

Do not stop at graphics — finish the whole driver stack.

1. In **Device Manager** (right-click **Start** → **Device Manager**), expand **System devices** and update chipset entries (right-click → **Update driver** → **Search automatically for updated driver software**).
2. Update **Display adapters**, **Sound, video and game controllers**, and **Network adapters** the same way.
3. Better: visit your laptop manufacturer's support site, enter your model, and install their Windows 10 driver pack — OEM drivers are tested against your exact hardware.
4. Restart after installing and test stability for a day before moving on.

### Fix 4: Stop Windows 10 from replacing your drivers

Windows 10 loves to "help" by overwriting your fixed drivers with its own versions. Prevent that.

1. Press **Win + R**, type `sysdm.cpl`, press **Enter** → **Hardware** tab → **Device Installation Settings**.
2. Select **No (your device might not work as expected)** and click **Save Changes**. This stops automatic driver downloads via Windows Update.
3. Alternatively, use the Group Policy editor (`gpedit.msc` → **Computer Configuration** → **Administrative Templates** → **Windows Components** → **Windows Update** → **Do not include drivers with Windows Updates** → **Enabled**) on Pro editions.
4. Re-verify your driver versions in **Device Manager** after the next Patch Tuesday to confirm nothing was swapped.

### Fix 5: Run SFC and DISM

Years of updates leave cruft; repair the system files properly.

1. Right-click **Start** → **Command Prompt (Admin)** (or **Windows PowerShell (Admin)**) → **Yes**.
2. Run `sfc /scannow` and wait for 100%.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` — needs an internet connection, takes 15-20 minutes.
4. Run `sfc /scannow` again to confirm, then restart.
5. Microsoft documents both tools in their [Windows support articles](https://support.microsoft.com/en-us/windows).

### Fix 6: Test the RAM and clean the cooling

Old laptops have old hardware — verify it before blaming software further.

1. Press **Win + R**, type `mdsched.exe`, press **Enter** → **Restart now and check for problems (recommended)**.
2. If errors appear, reseat the RAM modules (power off, unplug, remove battery if possible) and retest; replace the faulty stick if errors persist.
3. While you are in there: blow dust out of the vents and fans with compressed air. On a 5+ year old laptop, clogged cooling alone can cause these crashes under load.
4. Check temperatures with a free monitor — sustained CPU/GPU temps above 90°C under load warrant new thermal paste (a shop job if you are not comfortable opening the chassis).

### Fix 7: In-place repair install of Windows 10

The final software option: reinstall Windows while keeping your files and apps.

1. Download Microsoft's Windows 10 Media Creation Tool on a working PC (or this one in Safe Mode with Networking).
2. Run it, choose **Upgrade this PC now**, and select **Keep personal files and apps**.
3. The process takes 30-90 minutes with several restarts — do not interrupt it.
4. Afterward, install the manufacturer's drivers first, then let Windows Update run.

## Closing

On Windows 10, SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is a driver problem until proven otherwise — and the DDU clean-reinstall in Fix 2 is the move that resolves most cases I see in the shop. The Windows 10-specific gotcha is Fix 4: this OS will cheerfully replace your fixed drivers behind your back, so lock that down. Work the list patiently, test between changes, and you will get there. For the step-by-step variant of this same repair, see [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED step by step](/articles/how-to-fix-system-thread-exception-not-handled-step-by-step/); for the Windows 11 version, [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on Windows 11](/articles/how-to-fix-system-thread-exception-not-handled-on-windows-11/).
