---
title: "How to Fix DPC_WATCHDOG_VIOLATION on Windows 10"
slug: how-to-fix-dpc-watchdog-violation-on-windows-10
date: 2026-09-13
categories: ["windows-errors"]
tags: ["bsod", "dpc watchdog violation", "windows 10", "drivers"]
description: "Fix DPC_WATCHDOG_VIOLATION on Windows 10 with 7 steps — replace the SATA driver, update SSD firmware, disable Fast Startup, and repair system files."
thumbnail: "/images/thumbs/how-to-fix-dpc-watchdog-violation-on-windows-10.webp"
faqs:
  - q: "What causes DPC_WATCHDOG_VIOLATION on Windows 10?"
    a: "A device driver exceeded the time Windows allows for a deferred procedure call, so the watchdog crashed the system. On Windows 10 the classic trigger is the default SATA AHCI driver (storahci.sys) — replacing it with the manufacturer's driver fixes a huge share of cases."
  - q: "Why does it happen when my laptop wakes from sleep?"
    a: "Because power-state transitions are where drivers most often stall. The Wi-Fi or storage driver fails to wake promptly, misses its deadline, and the watchdog fires. Updating those two drivers and disabling Fast Startup usually ends the wake-from-sleep crashes."
  - q: "Is this error related to the hard drive failing?"
    a: "It can be, but a driver or firmware issue is far more likely. Run chkdsk and your SSD maker's health tool as part of troubleshooting. If the drive is healthy, the problem is in the driver stack, not the hardware."
  - q: "Should I upgrade to Windows 11 to fix it?"
    a: "No — upgrading to escape a driver bug usually just carries the bug along, since Windows 11 will install the same class of drivers. Fix the driver on Windows 10 first; then upgrade on your own schedule, not the error's."
---

**DPC_WATCHDOG_VIOLATION** (0x133) means a driver took too long to finish a task and Windows crashed instead of freezing forever. On Windows 10 this blue screen has a famous prime suspect: the generic **SATA AHCI controller driver** that Windows installs by default. Swapping it for the proper manufacturer driver is the fix that has resolved this error for countless people, and it is where this guide starts.

Windows 10's driver ecosystem is mature, which is actually good news — the correct drivers exist for nearly everything, and the failure patterns are well documented. If you are on Windows 11 instead, see our [DPC_WATCHDOG_VIOLATION guide for Windows 11](/articles/how-to-fix-dpc-watchdog-violation-on-windows-11/) — same error, slightly different driver landscape.

Pay attention to *when* the crashes happen, because the timing is diagnostic. Crashes within a minute of waking from sleep point squarely at the Wi-Fi or storage driver failing its power-state transition. Crashes during large file copies or game installs point at the storage driver under sustained load. Crashes that seem truly random, with no pattern at all, are the ones where you should suspect the SSD firmware or the RAM — the components whose failures do not follow a schedule. Matching the pattern to the fix saves you from updating drivers at random and hoping.

## Why this happens

- **Generic SATA AHCI driver.** Windows 10's built-in storahci.sys works, but on many laptops it mishandles power transitions. The chipset maker's driver (Intel RST, AMD SATA) almost always behaves better.
- **Outdated SSD firmware.** The drive itself can stall on certain commands; firmware updates fix the drive-side half of the problem.
- **Wi-Fi driver stalling on wake.** Extremely common pattern: crash happens seconds after opening the lid. The wireless driver is the usual suspect.
- **Fast Startup.** Windows 10's Fast Startup is enabled by default and preserves driver state across shutdowns — including broken driver state.
- **Old graphics driver.** Less common than storage, but GPU drivers that hang during display power transitions trip the same watchdog.
- **Failing drive or bad RAM.** The hardware causes to rule out once drivers check out.

## How to fix it

Work through these in order — Fix 1 is the classic for a reason.

### Fix 1: Replace the SATA AHCI controller driver

This single change fixes more Windows 10 DPC_WATCHDOG_VIOLATION cases than everything else combined.

1. Press **Win + X** and open **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers**.
3. Right-click **Standard SATA AHCI Controller** and choose **Update driver > Browse my computer for drivers > Let me pick from a list of available drivers on my computer**.
4. If your chipset maker's driver is listed (e.g., **Intel(R) Chipset SATA/PCIe RST Premium Controller**), select it and click **Next**.
5. If only the standard driver is listed, download the Intel RST or AMD SATA driver first: use [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) or AMD's driver download page, install it, then repeat the steps above.
6. Restart. This change alone ends the crashes for most people.

### Fix 2: Update the SSD firmware

1. In **Device Manager > Disk drives**, note your exact SSD model.
2. Install the manufacturer's toolbox (Samsung Magician, Crucial Storage Executive, WD Dashboard, Kingston SSD Manager) and check for firmware updates.
3. Apply any available firmware update — keep the charger plugged in and do not interrupt it.
4. Run the toolbox's health check while you are there to rule out a dying drive.

### Fix 3: Update the Wi-Fi driver and test the wake pattern

1. In **Device Manager > Network adapters**, right-click your wireless adapter and choose **Update driver > Search automatically for drivers**.
2. Then check **Settings > Update & Security > Windows Update > View optional updates** for a newer Wi-Fi driver.
3. If crashes happen on wake-from-sleep, also try this test: before closing the lid, disconnect from Wi-Fi manually. If the crash stops happening, you have confirmed the wireless driver — get the newest version from your laptop maker's support site.

### Fix 4: Disable Fast Startup

1. Open **Control Panel > Hardware and Sound > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Shut down fully (not restart), wait 10 seconds, and power on — this clears the hibernated kernel state.

### Fix 5: Update the graphics driver

1. Identify your GPU in **Device Manager > Display adapters**.
2. For NVIDIA, do a clean install from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx). For AMD, use AMD's driver download page. For Intel integrated graphics, check Intel's driver detection tool (linked in Fix 1).
3. During NVIDIA/AMD installation, choose the **clean/custom install** option to remove old driver remnants.

### Fix 6: Repair system files and check the disk

1. Open an elevated Command Prompt (**Win + X > Command Prompt (Admin)** or **Windows PowerShell (Admin)**).
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Run `chkdsk C: /f /r`, type **Y**, and restart to let it scan.
4. Test the RAM too: **Win + R** → `mdsched.exe` → **Restart now and check for problems**. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents these tools if you want more background.

### Fix 7: Adjust the power plan's PCI Express setting

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** on your active plan, then **Change advanced power settings**.
3. Expand **PCI Express > Link State Power Management** and set it to **Off** (on battery too, while testing).
4. Click **OK** and restart. Aggressive link power management is a documented trigger for storage-related watchdog crashes.

## Closing

On Windows 10, **DPC_WATCHDOG_VIOLATION** is a solved problem in the vast majority of cases: replace the generic SATA driver with the manufacturer's version, update the SSD firmware, and turn off Fast Startup. Those three steps clear it up for most laptops. HP owners should also check the [HP-tuned version of this guide](/articles/how-to-fix-dpc-watchdog-violation-on-hp-laptop/), which covers the HP Support Assistant driver-conflict angle. The error looks random and scary, but it is really just one driver missing its deadline — find the driver, fix the driver, and the blue screens stop.
