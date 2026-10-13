---
title: "How to Fix BAD_POOL_HEADER in Windows 11 24H2"
slug: how-to-fix-bad-pool-header-in-windows-11-24h2
date: 2026-09-16
categories: ["windows-errors"]
tags: ["bad pool header", "blue screen", "memory pool", "24H2", "driver"]
description: "BAD_POOL_HEADER blue screen on Windows 11 24H2? It's memory pool corruption from a bad driver. Update drivers, use Verifier, fix it here."
thumbnail: "/images/thumbs/how-to-fix-bad-pool-header-in-windows-11-24h2.webp"
faqs:
  - q: "What does BAD_POOL_HEADER mean?"
    a: "Windows' memory pool manager found corruption in a pool header — the metadata tracking a block of kernel memory. A driver wrote outside its allocation or freed memory twice, damaging the header. It's essentially always a third-party driver bug."
  - q: "Why is BAD_POOL_HEADER common after the 24H2 update?"
    a: "Major Windows updates change kernel memory management internals, exposing latent bugs in third-party drivers that happened to work before. Antivirus filter drivers and older network drivers are the typical casualties after 24H2 upgrades."
  - q: "Can RAM cause BAD_POOL_HEADER?"
    a: "Yes, though drivers are more common. Faulty RAM corrupts pool headers exactly like a buggy driver does. If driver updates and Driver Verifier don't resolve it, run MemTest86 to rule out memory."
  - q: "What's the difference between BAD_POOL_HEADER and BAD_POOL_CALLER?"
    a: "BAD_POOL_HEADER means the pool's metadata was found corrupted; BAD_POOL_CALLER means a driver made an invalid pool request (like freeing already-freed memory). Both point to driver memory bugs and share the same troubleshooting approach."
---

**BAD_POOL_HEADER** is the memory pool manager catching corruption. Windows allocates kernel memory in "pools," each tracked by a header. When a driver scribbles past its allocation or double-frees memory, the header gets damaged — and the next time the pool manager touches it, you get this blue screen.

On Windows 11 24H2, this error spiked after upgrades because the updated kernel exposed bugs in drivers that had been silently misbehaving for years. The fix is finding the bad driver. Here's the order that works.

The good news is that pool corruption leaves evidence — minidumps usually implicate the corrupting driver, and Driver Verifier can catch it red-handed when dumps are inconclusive. You don't need to guess; you need the right tools in the right order. And because 24H2 specifically is involved, pay attention to driver versions validated for 24H2 versus older builds. For the broader memory stop-code family, see our [memory management troubleshooting guide](/articles/troubleshoot-stop-code-memory-management/).

## Why this happens

- **Buggy third-party driver:** Antivirus filters, network drivers, and storage drivers with pool-management bugs — the overwhelming majority of cases.
- **24H2 exposing latent driver bugs:** Drivers that worked on 23H2 crashing on 24H2's changed memory manager.
- **Corrupted driver installation:** Mismatched driver files after a failed update.
- **Bad RAM:** Faulty memory corrupting pool headers in ways identical to driver bugs.
- **Overclocked/unstable RAM:** XMP profiles causing bit errors in pool memory.
- **Disk corruption:** Damaged pagefile or system files contributing to pool instability.
- **Hypervisor/virtualization drivers:** VirtualBox, VMware, or Hyper-V network/storage drivers with pool bugs, especially after host OS upgrades.
- **Motherboard utility drivers:** RGB controllers, fan utilities, and "gaming" tools that install kernel drivers with poor memory hygiene.

## How to fix it

Work through these in order.

### Fix 1: Update the high-risk drivers

Pool corruption comes from drivers that allocate heavily — start there. Network drivers top the list because they constantly allocate and free packet buffers, which is exactly where pool bugs hide. Driver-focused crashes with a different signature are covered in our [IRQL driver guide](/articles/how-to-fix-driver-irql-not-less-or-equal/).

1. Update **network drivers** (Wi-Fi + Ethernet) from your laptop maker's support site — network drivers are the #1 pool corruptors.
2. Clean-install the **graphics driver** with DDU in Safe Mode.
3. Update **chipset and storage drivers** from the manufacturer.
4. Restart between each and test with normal use.

### Fix 2: Remove third-party antivirus and filter drivers

The fastest single elimination step for this stop code.

1. Uninstall third-party antivirus, VPN clients, firewall suites, and any "network optimizer" tools completely.
2. Check **Device Manager > View > Show hidden devices** for leftover filter drivers and remove them.
3. Restart and test for 24–48 hours. Windows Security is sufficient protection meanwhile.

### Fix 3: Roll back the 24H2 driver changes

If crashes started with the 24H2 update:

1. In **Device Manager**, check each major device's **Driver** tab for a driver date matching the 24H2 upgrade — roll back (**Roll Back Driver**) the ones that changed.
2. Visit the laptop maker's support site for **24H2-validated** driver versions — manufacturers release updated drivers specifically for new Windows builds.
3. As a broader undo: **Settings > System > Recovery > Go back** (available 10 days after the feature update) returns you to 23H2 if 24H2 is fundamentally incompatible with your driver set.

### Fix 4: Deploy Driver Verifier to name the driver

When updates don't resolve it, catch the corruptor scientifically. Verifier's Special pool option places each allocation on its own page with guard pages around it, so the instant a driver writes out of bounds, the system crashes with the driver's name — no ambiguity.

1. Create a restore point (**System Protection > Create**).
2. Run `verifier.exe` > **Create custom settings** > **Standard settings** + **Special pool** (ideal for pool corruption).
3. **Select driver names from a list** > check all non-Microsoft drivers > **Finish** > restart.
4. Use the PC normally — Verifier will bugcheck with the guilty driver's name when it corrupts the pool.
5. Boot to Safe Mode, run `verifier /reset`, then update/roll back/remove the named driver.

### Fix 5: Analyze minidumps for patterns

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open dumps from `C:\Windows\Minidump`, run `!analyze -v` on several.
3. If the same driver appears across dumps, that's your target — search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a different (older or newer) version.
4. Cross-reference with **Reliability Monitor** to find what changed before the first crash.

### Fix 6: Test RAM with MemTest86

Driver hunt exhausted? Rule out hardware. RAM faults produce bit flips in pool headers that look exactly like driver corruption, so a clean MemTest86 is the only way to close this branch of the investigation.

1. Create a **MemTest86** USB on another PC, boot from it, run one full pass.
2. Zero errors required. Any errors → reseat modules and retest, then replace the bad stick.
3. Also disable **XMP/EXPO** in BIOS and retest — unstable memory profiles cause pool corruption under load.

### Fix 7: Repair system files and reset the page file

1. Admin terminal: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Reset the page file: **Advanced system settings > Performance Settings > Advanced > Change** — set **No paging file**, restart, re-enable automatic management, restart.
3. Run `chkdsk C: /f` to rule out underlying disk damage.

### Fix 8: In-place upgrade for a clean driver baseline

When the corrupting driver can't be identified or replaced individually, an in-place upgrade rebuilds the entire driver and system baseline in one operation.

1. Download the latest Windows 11 24H2 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount it, run **setup.exe**, choose **Keep personal files and apps**.
3. This reinstalls Windows with a fresh driver stack and rebuilt pool manager state.
4. Afterward, install drivers from the laptop maker's site (24H2-validated versions) before letting Windows Update install its own.

## Closing

BAD_POOL_HEADER on 24H2 is a driver-compatibility problem in most cases — the update changed the rules and some driver didn't keep up. Update the network/graphics/chipset drivers to 24H2-validated versions, strip out third-party filter drivers, and let Driver Verifier name the culprit if the obvious steps miss. Keep MemTest86 in reserve for the hardware backstop. Once the corrupting driver is replaced, this stop code stays gone. After the fix, keep an eye on Reliability Monitor for a week — pool corruption that's truly fixed stays fixed, and any recurrence will show you the same driver name, telling you the replacement didn't take.
