---
title: "How to Fix IRQL_NOT_LESS_OR_EQUAL on an HP Laptop"
slug: how-to-fix-irql-not-less-or-equal-on-hp-laptop
date: 2026-10-06
categories: ["windows-errors"]
tags: ["blue screen", "IRQL", "driver error", "HP laptop", "stop code"]
description: "IRQL_NOT_LESS_OR_EQUAL on your HP laptop is almost always a bad driver or faulty RAM. Here's the exact troubleshooting order that works."
thumbnail: "/images/thumbs/how-to-fix-irql-not-less-or-equal-on-hp-laptop.webp"
faqs:
  - q: "What causes IRQL_NOT_LESS_OR_EQUAL on HP laptops?"
    a: "A driver (or occasionally faulty RAM) tried to access memory it shouldn't. On HP laptops the usual suspects are network drivers, the Intel graphics driver, or a Windows update that replaced a working HP driver with a generic one. Overclocking utilities and third-party antivirus drivers can also trigger it."
  - q: "Is IRQL_NOT_LESS_OR_EQUAL a hardware problem?"
    a: "Usually no — about 80% of cases are driver or software related. But if the crashes persist after you've updated or rolled back every driver, test your RAM with Windows Memory Diagnostic. Bad RAM modules cause this exact stop code and are common in older laptops."
  - q: "How do I find which driver caused the crash?"
    a: "Check C:\\Windows\\Minidump for .dmp files and open them with BlueScreenView (free) or WinDbg. The 'Caused By Driver' field usually names the file, e.g., ntoskrnl.exe with a network driver. That tells you exactly which driver to update or roll back."
  - q: "Can HP's own tools help diagnose this?"
    a: "Yes. HP PC Hardware Diagnostics (press Esc at boot, then F2) tests RAM, the drive, and the motherboard. HP Support Assistant can also pull the correct drivers for your exact model, which beats installing generic drivers from chip makers."
---

The **IRQL_NOT_LESS_OR_EQUAL** blue screen is one of the most common stop codes on HP laptops, and the name sounds scarier than the problem actually is. In plain terms: a driver tried to use a chunk of memory it wasn't allowed to touch, and Windows pulled the emergency brake.

On HP machines this is overwhelmingly a driver issue — Windows Update loves to swap HP's tuned drivers for generic ones. The troubleshooting below goes from the quick wins to the deeper checks. If you're seeing a different memory-related stop code, our [memory management BSOD guide](/articles/how-to-fix-memory-management-bsod-in-windows-11-24h2/) covers the RAM-heavy side of things.

## Why this happens

- **Faulty or mismatched driver:** A network, graphics, or storage driver with a bug, or a generic Windows driver replacing HP's version after an update.
- **Bad RAM:** A failing memory module corrupts data that a driver is reading, producing this exact stop code.
- **Overclocking or aggressive power settings:** HP Omen/OMEN Gaming Hub overclocks and some "performance booster" utilities push hardware into unstable territory.
- **Corrupted system files:** Damaged Windows kernel files (ntoskrnl.exe) can make a healthy driver look guilty.
- **Third-party antivirus or VPN drivers:** Kernel-level security and network filter drivers from security suites are a classic trigger.
- **Overheating:** Less common, but sustained heat can cause memory errors that manifest as IRQL crashes during gaming or heavy loads.

## How to fix it

Work through these in order — most HP laptops are fixed by Fix 2 or Fix 3.

### Fix 1: Identify the guilty driver from the dump file

Don't guess — the crash dump usually names the culprit.

1. If you can boot (even into Safe Mode), open **File Explorer** and go to `C:\Windows\Minidump`.
2. Download and run **BlueScreenView** (free from NirSoft) or install **WinDbg Preview** from the Microsoft Store.
3. Open the most recent `.dmp` file and look at **Caused By Driver** — a filename like `Netwtw10.sys` (Intel Wi-Fi), `nvlddmkm.sys` (NVIDIA), or `rtwlane.sys` (Realtek) tells you exactly what to update.
4. If every dump blames `ntoskrnl.exe` with no specific driver, that's the signature of bad RAM — skip ahead to Fix 5.

### Fix 2: Update drivers from HP, not just Windows Update

Generic drivers from Windows Update are the #1 cause of this error on HP hardware.

1. Open **Settings > Windows Update** and install everything pending first, then restart.
2. Go to [HP Support](https://support.hp.com/us-en), enter your exact model number (on the bottom sticker), and download the latest **chipset, network (Wi-Fi + Ethernet), and graphics** drivers.
3. Install them one at a time, restarting between each, then use the laptop normally to see if the crashes stop.

HP's driver packages are tested against your specific motherboard revision, which is why they beat the generic versions Windows pulls automatically.

### Fix 3: Roll back the driver that just changed

If the crashes started right after an update, undo it.

1. Boot into **Safe Mode** if normal boot crashes (hold **Shift** while clicking **Restart**, then **Troubleshoot > Advanced options > Startup Settings**).
2. Open **Device Manager** (right-click **Start**), find the suspect device (start with **Network adapters** and **Display adapters**), right-click it, and choose **Properties**.
3. On the **Driver** tab, click **Roll Back Driver** and pick a reason. If the button is grayed out, choose **Uninstall device**, then restart — Windows will reinstall the previous driver version.

### Fix 4: Run SFC and DISM to repair system files

Corrupted kernel files can cause phantom IRQL errors.

1. Open **Terminal (Admin)** or **Command Prompt (Admin)** — right-click **Start** and choose it.
2. Run `sfc /scannow` and wait for it to finish (10–20 minutes).
3. If it found problems it couldn't fix, run `DISM /Online /Cleanup-Image /RestoreHealth`, then run `sfc /scannow` once more.
4. Restart and test.

### Fix 5: Test your RAM

Bad memory is the leading hardware cause of this stop code.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The test runs before Windows loads.
3. If it reports errors, you've found it: one of your RAM sticks is bad. On most HP laptops you can reseat or replace the SODIMM modules yourself; if the RAM is soldered, it's a warranty/HP service job.
4. For a deeper test, run **MemTest86** from a bootable USB overnight — one full pass with zero errors is the bar for "RAM is fine."

### Fix 6: Run HP's built-in hardware diagnostics

HP ships excellent diagnostics — use them before assuming Windows is at fault.

1. Restart and press **Esc** repeatedly, then press **F2** for **System Diagnostics**.
2. Run the **Component Tests** for memory, hard drive/SSD, and the processor (the extensive memory test takes a while — worth it).
3. If any component fails, note the 24-digit failure ID and contact HP support or your repair shop with it.

You can also run these checks from inside Windows with **HP Support Assistant**, which you can grab from the [HP support site](https://support.hp.com/us-en).

### Fix 7: Remove kernel-level third-party software

Antivirus, VPNs, and "game booster" tools install drivers that run at the same privilege level as Windows itself.

1. Temporarily uninstall your third-party antivirus (Windows Security/Defender is fine on its own) and any VPN client.
2. Uninstall HP OMEN Gaming Hub overclocking profiles or third-party tools like MSI Afterburner if you use them.
3. Restart and use the laptop for a day. If the crashes stop, reinstall the software one piece at a time — or leave the offender off.

### Fix 8: Clean-install the graphics driver

Graphics drivers are a frequent IRQL trigger, especially on HP laptops with both Intel and NVIDIA/AMD graphics.

1. Download **Display Driver Uninstaller (DDU)** and the latest graphics driver for your model from [HP Support](https://support.hp.com/us-en).
2. Boot into **Safe Mode**, run DDU, and choose **Clean and restart**.
3. Install the HP-provided graphics driver (not the newest one from NVIDIA/AMD unless HP's is outdated and the problem persists).

## Closing

On HP laptops, IRQL_NOT_LESS_OR_EQUAL is a driver problem far more often than a hardware problem — and the fix is usually "put HP's driver back." Start with the dump file to aim your efforts, update or roll back the named driver, and only start suspecting RAM if the crashes survive a full driver refresh. If HP's own diagnostics flag a component, don't keep fighting it in software — a failing stick of RAM or SSD will keep producing [stop code crashes](/articles/troubleshoot-stop-code-memory-management/) no matter how many drivers you reinstall.
