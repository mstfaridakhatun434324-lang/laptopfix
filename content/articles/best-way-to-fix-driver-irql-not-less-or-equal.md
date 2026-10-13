---
title: "Best Fixes for the Driver IRQL Not Less or Equal Error"
slug: best-way-to-fix-driver-irql-not-less-or-equal
date: 2026-09-06
categories: ["windows-errors"]
tags: ["blue screen", "driver fix", "IRQL"]
description: "Ranked by effectiveness: the fixes that actually stop DRIVER_IRQL_NOT_LESS_OR_EQUAL crashes, starting with the one that works most often."
thumbnail: "/images/thumbs/best-way-to-fix-driver-irql-not-less-or-equal.webp"
faqs:
  - q: "What is the fastest fix for this blue screen?"
    a: "Updating the specific crashing driver from your laptop manufacturer's support page. The blue screen usually names the .sys file, which tells you the device. A targeted driver update resolves the majority of cases in under 30 minutes, without touching anything else on the system."
  - q: "Should I use a driver updater program?"
    a: "No. Third-party driver updaters are a frequent cause of this exact blue screen — they install mismatched or untested driver versions. Get drivers from the laptop manufacturer, the chip maker (Intel, NVIDIA, AMD), or Windows Update, in that order of preference."
  - q: "Why does the error keep coming back after I fix it?"
    a: "Because Windows Update reinstalls the problematic driver version over your working one. After fixing it, note the working driver version and use the 'Show or hide updates' troubleshooter or a temporary update pause to block the bad version from returning."
  - q: "Is a clean Windows install the best fix?"
    a: "Rarely. A clean install with the same faulty driver — which Windows Update will promptly reinstall — reproduces the problem. Targeted driver replacement fixes the actual cause in a fraction of the time. Reserve clean installs for cases where file corruption is proven."
---
Not all fixes are equal. For **DRIVER_IRQL_NOT_LESS_OR_EQUAL**, some remedies work most of the time, some work sometimes, and some are folklore. This article ranks them by real-world effectiveness so you start with what is most likely to end your crashes and stop as soon as the blue screens stop.

The ranking below comes from the nature of the error: it is a driver bug about 80% of the time, a Windows Update driver swap about 10%, and hardware or deep corruption the rest. Work the list top-down.

## Why this happens

- **An outdated or buggy device driver:** The runaway leader. Wi-Fi, graphics, and storage drivers cause most cases.
- **Windows Update installing the wrong driver:** A generic driver replacing a working manufacturer-tuned one.
- **Conflicting security or VPN software:** Filter drivers destabilizing the device driver beneath them.
- **Corrupt driver files:** Bad sectors or interrupted installs leaving driver binaries half-written.
- **Failing RAM:** Memory errors that corrupt driver operations and blame innocent drivers.
- **Unstable overclocks or overheating:** Hardware instability surfacing inside driver code.
- **Damaged Windows driver frameworks:** Corruption in shared files like `ndis.sys` breaking every driver built on them.
- **Recently added peripherals:** A new USB device, dock, or adapter whose driver has an IRQL-handling bug can start the crashes the day it is plugged in.

## How to fix it

Work through these in order — the ranking is the point.

### Fix 1: Update the crashing driver from the manufacturer (works most often)

Read the `.sys` filename on the blue screen, then replace exactly that driver with the manufacturer-tested version.

1. Identify the device from the filename: `Netwtw10.sys`/`rtwlanu.sys` means Wi-Fi, `nvlddmkm.sys` means NVIDIA graphics, `atikmdag.sys` means AMD graphics, `storahci.sys` means storage.
2. Download the driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/). For Intel wireless/chipset, the Intel Driver & Support Assistant is the fastest reliable source.
3. Install it over the old driver, reboot, and reproduce the crash conditions. This single step ends the problem for most people.

### Fix 2: Roll back the driver Windows Update just installed

If crashes began within days of an update, the "update" is the prime suspect.

1. Open **Device Manager** (**Win + X**), right-click the device, and open **Properties > Driver**.
2. Click **Roll Back Driver** and confirm.
3. Reboot and test thoroughly under your normal daily workload, including the exact specific scenario that used to crash every time. Then prevent recurrence: **Settings > Windows Update** lets you pause updates for several weeks, and Microsoft's support site documents the troubleshooter that hides a specific driver update permanently so the bad version cannot return.

### Fix 3: Clean-reinstall the driver (when update alone fails)

Sometimes the old driver's remnants are the problem, and an in-place update preserves them.

1. In **Device Manager**, right-click the device and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Reboot — Windows will load a basic driver.
3. Install the fresh manufacturer driver from Fix 1. For graphics cards, use DDU (Display Driver Uninstaller) in Safe Mode for a truly clean slate before installing the new GPU driver. DDU removes registry entries, folders, and services the standard uninstaller leaves behind — the leftover fragments are exactly what cause a "clean" reinstall to keep crashing.

### Fix 4: Remove conflicting filter-driver software

When the dump blames `ndis.sys` or crashes persist across driver versions, something layered on top is interfering.

1. Uninstall third-party antivirus temporarily — Windows Security covers you during the test.
2. Remove VPN clients, virtual adapters, and "driver updater" utilities.
3. Test for a day or two between each removal so you know which one mattered. If you want the full conflict-hunting method, our [driver IRQL troubleshooting guide](/articles/driver-irql-not-less-or-equal-troubleshooting/) walks through isolating filter drivers with msconfig.

### Fix 5: Repair system files and reset the network stack

For network-driver crashes especially, corrupt shared components are worth fixing.

1. Elevated Command Prompt: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
2. For `ndis.sys` crashes, also run `netsh winsock reset`, `netsh int ip reset`, and `ipconfig /flushdns`, then reboot.
3. This is quick, safe, and resolves the cases where the driver itself is fine but its foundation is cracked.

### Fix 6: Test the memory

If different crashes blame different drivers, stop blaming drivers.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Review results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
3. Reseat or replace faulty RAM. Random-driver blame is the signature symptom of bad memory — see [memory-management-bsod-windows-11-fix](/articles/memory-management-bsod-windows-11-fix/) for the deeper memory workup.

### Fix 7: Check thermals and reset overclocks

Hardware instability is uncommon here but real, especially on gaming laptops. Before assuming the worst, remember that heat-related IRQL crashes follow a pattern: they appear after sustained load and vanish after cooldown. If your crashes match that rhythm, thermals deserve attention before drivers get a second round of blame.

1. Reset BIOS to **Optimized Defaults**; disable XMP and any undervolting tools temporarily.
2. Monitor GPU/CPU temperatures under load — sustained extreme heat corrupts driver operations.
3. Remove recently added USB hardware and docks to rule out immature drivers for new devices.

## Closing

Ranked by what works: update the named driver from the manufacturer, roll back bad updates, clean-reinstall stubborn drivers, clear out conflicting software, repair system files, test memory, and check thermals. Start at the top and stop when the crashes stop — most people never get past Fix 2. And when the same crash returns months later after another update cycle, you will already know the drill: check what changed most recently, because with this stop code, the newest change is guilty until proven innocent.
