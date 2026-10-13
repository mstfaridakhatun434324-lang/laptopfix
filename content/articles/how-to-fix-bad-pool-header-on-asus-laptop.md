---
title: "How to Fix the BAD_POOL_HEADER Blue Screen on an ASUS Laptop"
slug: how-to-fix-bad-pool-header-on-asus-laptop
date: 2026-10-05
categories: ["windows-errors"]
tags: ["bsod", "bad-pool-header", "asus-laptop"]
description: "BAD_POOL_HEADER crashing your ASUS laptop? Fix the driver, memory, and Armoury Crate causes with this guide."
thumbnail: "/images/thumbs/how-to-fix-bad-pool-header-on-asus-laptop.webp"
faqs:
  - q: "What does BAD_POOL_HEADER mean on an ASUS laptop?"
    a: "It means Windows found corruption in a kernel memory pool header — a driver wrote to memory it didn't own, or RAM returned corrupt data. It's the same stop code on every brand; ASUS models just tend to trigger it via Armoury Crate drivers, bad updates, or failing memory."
  - q: "Can Armoury Crate cause BAD_POOL_HEADER?"
    a: "Yes — Armoury Crate installs several low-level drivers for lighting, fan, and power control, and buggy versions have caused pool corruption crashes. Updating or cleanly reinstalling Armoury Crate is worth trying if crashes started around an Armoury update."
  - q: "How do I know if it's RAM or a driver?"
    a: "Test drivers first (free, fast): update or remove suspects and see if crashes stop. Then run the Windows Memory Diagnostic. If the laptop is stable in Safe Mode, it's a driver; if it crashes in Safe Mode too, lean toward hardware."
  - q: "Will updating the BIOS help?"
    a: "Sometimes. ASUS BIOS updates fix memory-compatibility and power-management bugs that can manifest as pool corruption. Update the BIOS from ASUS support if your version is old — but only as one step among the driver and memory checks, not the first resort."
---
# How to Fix the BAD_POOL_HEADER Blue Screen on an ASUS Laptop

**BAD_POOL_HEADER** means Windows caught something corrupting kernel memory — usually a driver writing where it shouldn't, sometimes faulty RAM. On ASUS laptops there's an extra usual suspect beyond the generic ones: **Armoury Crate** and its bundle of low-level drivers, which have a track record of causing exactly this stop code when they go bad.

The approach is the same as for any BAD_POOL_HEADER: drivers first, memory second, everything else after. If you own an Acer or Dell with the same crash, the general [memory management BSOD guide](/articles/memory-management-bsod-windows-11-fix/) and the [special pool corruption guide](/articles/how-to-fix-special-pool-detected-memory-corruption-on-windows-11/) cover the shared ground.

## Why this happens

- **Buggy third-party drivers:** Antivirus filters, old peripheral drivers, and ASUS's own Armoury Crate drivers top the list.
- **Faulty RAM:** Bad memory cells corrupt pool headers just like a bad driver would.
- **Corrupted system files:** Damaged memory-manager components mishandle pool allocations.
- **Disk errors:** Bad sectors corrupting drivers as they load mimic driver bugs.
- **Unstable memory settings:** XMP/DOCP profiles or manual tweaks on ASUS ROG and TUF models destabilize the memory subsystem.
- **Conflicting utilities:** Multiple hardware-control apps (Armoury Crate plus a third-party fan tool) fighting over the same embedded controller.

## How to fix it

Work through these in order. ASUS-specific steps are noted where they matter.

### Fix 1: Boot into Safe Mode and assess

Get stable ground and determine whether it's a third-party driver at all.

1. Interrupt boot three times at the ASUS logo to reach Recovery, then **Troubleshoot > Advanced options > Startup Settings > Restart**, pressing **4** for Safe Mode.
2. If the laptop is stable in Safe Mode, a third-party driver is the cause — continue.
3. If it crashes in Safe Mode too, prioritize the memory test (Fix 3) and disk check (Fix 5).
4. While in Safe Mode, note any software installed or updated just before crashes began — dates matter a lot for identifying the culprit.

### Fix 2: Update or reinstall Armoury Crate

On ASUS laptops, do this before generic driver hunting — it's the brand-specific smoking gun.

1. Open **Armoury Crate** and install all pending updates, or download the latest version from ASUS support for your model.
2. If crashes started right after an Armoury Crate update, uninstall it completely (use the official **Armoury Crate Uninstall Tool** from ASUS — regular uninstall leaves drivers behind).
3. Restart and test without Armoury Crate for a day or two.
4. If crashes stop, reinstall the latest Armoury Crate fresh — the old install's drivers were the problem.
5. While you're at it, remove any other hardware-control utilities (fan controllers, RGB apps) that might conflict with it.

### Fix 3: Run the Windows Memory Diagnostic

Bad RAM is the other headline cause — test it early.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. After reboot, check **Event Viewer > Windows Logs > System** for the MemoryDiagnostics-Results entry.
3. Errors mean reseating modules and testing sticks individually (on models with accessible RAM).
4. Replace any failing stick. For a deeper memory-testing walkthrough, see our [Memory Management BSOD guide](/articles/memory-management-bsod-windows-11-fix/).

### Fix 4: Update core drivers from ASUS

Refresh the driver stack with versions validated for your exact model.

1. Go to ASUS support, enter your model, and download the latest **chipset**, **storage**, and **network** drivers. The **MyASUS** app can also fetch these, but verify versions against the support site since MyASUS sometimes lags.
2. In **Device Manager**, update each category; if a device shows a yellow warning, uninstall it (tick **Attempt to remove the driver**) and install the ASUS download fresh.
3. Skip "driver updater" utilities entirely — they cause more BAD_POOL_HEADER cases than they fix.
4. Uninstall recently added antivirus, VPN, or virtual-drive software, whose filter drivers are classic pool-corruption sources.

### Fix 5: Check the drive for errors

Storage corruption that damages drivers on load looks like a driver bug.

1. Open an admin Command Prompt and run `chkdsk C: /f /r`, pressing **Y** to schedule at reboot.
2. Restart and let the full scan finish.
3. Check the SSD's SMART health with the manufacturer's toolbox afterward.
4. Back up and replace any drive with reallocated sectors or a failing status — and run `sfc /scannow` plus `DISM /Online /Cleanup-Image /RestoreHealth` from an admin Terminal to repair any system files the disk errors damaged. Microsoft documents both tools on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Reset BIOS settings and memory profiles

Unstable memory timings corrupt pools under load.

1. Restart and press **F2** or **Del** to enter the ASUS BIOS/UEFI.
2. Load optimized defaults (**F5** on most ASUS boards).
3. If you enabled **DOCP/XMP**, disable it for now — re-enable only after days of stability.
4. Save and exit, then test. ROG laptops with manual tuning should return every voltage and timing to stock during diagnosis.

### Fix 7: Update the BIOS, then reset Windows if needed

The last two resorts, in order.

1. Download the latest BIOS for your model from ASUS support and install it with the charger connected — never interrupt a BIOS flash.
2. If crashes survive everything above, use **Settings > System > Recovery > Reset this PC** with **Keep my files**.
3. After the reset, install drivers only from ASUS, add Armoury Crate last, and test between installs so a returning crash identifies the culprit immediately.

## Closing

On ASUS laptops, BAD_POOL_HEADER deserves an Armoury Crate check before anything else — it's the brand-specific cause the generic guides miss. Beyond that, it's the standard playbook: drivers, memory, disk, BIOS. Work it methodically and you'll not only stop the crashes but know exactly which component was responsible, which is what keeps it from coming back next month to interrupt your work again without any warning at all.
