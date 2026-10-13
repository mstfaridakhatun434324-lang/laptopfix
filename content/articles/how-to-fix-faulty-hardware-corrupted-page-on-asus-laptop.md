---
title: "How to Fix FAULTY_HARDWARE_CORRUPTED_PAGE on an ASUS Laptop"
slug: how-to-fix-faulty-hardware-corrupted-page-on-asus-laptop
date: 2026-09-17
categories: ["windows-errors"]
tags: ["faulty hardware corrupted page", "bsod", "asus laptop", "ram error", "0x12b"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE keeps blue-screening your ASUS laptop? Here's how to test your RAM, fix drivers, and stop the 0x12B crashes."
thumbnail: "/images/thumbs/how-to-fix-faulty-hardware-corrupted-page-on-asus-laptop.webp"
faqs:
  - q: "Does this error always mean my hardware is broken?"
    a: "Not always. Despite the name, faulty drivers and corrupted system files cause this error just as often as failing RAM or SSDs. The stop code means Windows found corrupted data in a memory page and could not determine whether hardware or software was responsible. Always rule out drivers and run a memory test before assuming you need new hardware."
  - q: "What is stop code 0x12B?"
    a: "0x12B is the hexadecimal code for FAULTY_HARDWARE_CORRUPTED_PAGE. It means the memory manager detected that the contents of a hardware memory page did not match what was expected — data was corrupted somewhere between the RAM, the storage, or the driver handling it. Windows crashes deliberately to prevent that corrupted data from damaging your files."
  - q: "How long does the Windows Memory Diagnostic take?"
    a: "The standard test takes about 20 to 40 minutes on a typical 8 to 16 GB laptop. The extended test can take several hours. Run at least the standard pass first; if it reports errors, you have found your culprit. For a more thorough check, the free MemTest86 tool booted from a USB drive is the gold standard."
  - q: "Can a Windows update cause this error?"
    a: "Yes. Updates can install incompatible drivers — especially storage controller, chipset, and graphics drivers — that corrupt memory pages and trigger this exact stop code. If the crashes started within days of an update, rolling back the driver or uninstalling the update is one of the first things to try."
---
FAULTY_HARDWARE_CORRUPTED_PAGE is one of those blue screens whose name sends people straight to the repair shop, wallet in hand. But here is what experience teaches: the word "hardware" in the name is misleading. I have fixed this error with a simple driver update far more often than with a RAM replacement.

That said, you should take it seriously and diagnose it properly, because sometimes it really is the memory or SSD. Let's find out which one you are dealing with.

## Why this happens

- **Failing RAM:** A memory stick with bad cells corrupts data as Windows reads and writes it — the textbook cause of this stop code.
- **Buggy or outdated drivers:** Storage, chipset, and graphics drivers handle memory pages constantly; a defective one corrupts them and triggers the crash.
- **A Windows update that replaced a working driver:** Update-installed drivers are a notorious trigger, especially Intel Rapid Storage and older NVIDIA/AMD graphics drivers.
- **Corrupted system files:** Damaged Windows components can mismanage memory pages and produce the same symptom as bad hardware.
- **Failing SSD or hard drive:** Corruption on the page file or system files stored on a dying drive surfaces as corrupted memory pages.
- **Overclocking or aggressive XMP profiles:** ASUS laptops with performance tuning enabled can push RAM beyond stable speeds, causing intermittent corruption.
- **Overheating:** Sustained high temperatures make marginal RAM and VRMs unstable, producing corruption that looks like hardware failure.

## How to fix it

Work through these in order, starting at Fix 1. The memory test in Fix 1 is the single most informative step — do not skip it.

### Fix 1: Test your RAM with Windows Memory Diagnostic

This is the definitive first test. It tells you whether your RAM is actually the problem.

1. Save your work, then press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The laptop reboots into the memory test automatically.
3. Let the standard test complete (20-40 minutes). Do not use the laptop during the test.
4. When Windows boots back up, check the result: press **Win + X**, open **Event Viewer**, go to **Windows Logs > System**, and filter for source **MemoryDiagnostics-Results**.
5. If errors are reported, your RAM is faulty — skip to Fix 7 for next steps. If no errors, continue with Fix 2.

Memory-related crashes share symptoms with other stop codes, so if you also see general memory errors, our [MEMORY_MANAGEMENT BSOD guide](/articles/memory-management-bsod-windows-11-fix/) is worth reading alongside this one.

### Fix 2: Update chipset, storage, and graphics drivers

Bad drivers are the most common non-hardware cause, so update the three driver families that touch memory pages the most.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers** — right-click each entry, choose **Update driver > Search automatically for drivers**.
3. Do the same under **Display adapters** for your GPU.
4. Then visit ASUS's official support downloads for your exact model — the official driver source — and install the latest chipset driver package, which Windows Update often misses.
5. Restart and use the laptop normally for a day or two to confirm the crashes stop.

### Fix 3: Roll back a driver if crashes started after an update

If the blue screens began within days of a Windows or driver update, the new driver is suspect number one.

1. In **Device Manager**, right-click the recently updated device (check **Events** tab under Properties for the install date) and open **Properties**.
2. On the **Driver** tab, click **Roll Back Driver**, pick a reason, and confirm.
3. Alternatively, go to **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent driver or quality update.
4. Restart and monitor. For update-triggered variants of this crash, also see [how to fix FAULTY_HARDWARE_CORRUPTED_PAGE after a Windows 11 update](/articles/how-to-fix-faulty-hardware-corrupted-page-after-windows-11-update/).

### Fix 4: Repair system files and check the disk

Corrupted Windows files and disk errors both produce this stop code.

1. Open an elevated terminal: **Win + X > Terminal (Admin)**.
2. Run `sfc /scannow` and wait for it to finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store SFC draws from.
4. Next, check the drive: `chkdsk C: /f` — type **Y** when asked to schedule it, then restart.
5. After all three complete, test the system under normal use.

### Fix 5: Reset the page file to system-managed

A manually sized or corrupted page file can feed bad data back into memory.

1. Press **Win + R**, type `sysdm.cpl`, press Enter, and open the **Advanced** tab.
2. Under **Performance**, click **Settings**, go to the **Advanced** tab, and under **Virtual memory** click **Change**.
3. Check **Automatically manage paging file size for all drives** and click **OK** on every dialog.
4. Restart the laptop. Windows rebuilds the page file cleanly on boot.

### Fix 6: Disable fast startup and memory overclocking

Fast Startup's hibernation file and aggressive RAM timings both cause intermittent page corruption.

1. Go to **Settings > System > Power & battery**, click **Additional power settings** (or search **Control Panel > Power Options**), then **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**. Save and restart.
3. If you enabled XMP/DOCP or ASUS performance profiles in the BIOS/UEFI, reboot into firmware (**Settings > System > Recovery > Advanced startup > Troubleshoot > UEFI Firmware Settings**) and restore memory settings to default/Auto.

### Fix 7: Reseat or replace the RAM

If the memory diagnostic reported errors, the hardware verdict is in.

1. Power off, unplug, and (on models with a removable back panel) open the laptop following your ASUS model's service manual.
2. Remove the RAM sticks, blow out the slots with compressed air, and reseat them firmly until the clips snap.
3. If errors persist, test one stick at a time to identify the bad module, then replace it with a matching DDR4/DDR5 SODIMM of the correct speed.
4. If the RAM is soldered (common on ultrabooks like the Zenbook line), this is a warranty or service-center job — back up your data first.

Official ASUS warranty and service options are listed on ASUS's support site, and general Windows crash guidance is on the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows).

## Closing

Do not let the word "hardware" in FAULTY_HARDWARE_CORRUPTED_PAGE panic you into buying new RAM on day one. Run the memory diagnostic, update your chipset, storage, and graphics drivers, and repair your system files — that sequence resolves the clear majority of these crashes. Only when the memory test itself reports errors should you open the laptop or head to a service center, and at that point you will know exactly what needs replacing instead of guessing.
