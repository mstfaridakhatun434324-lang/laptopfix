---
title: "What to Do If You Get Stop Code Memory Management"
slug: what-to-do-if-stop-code-memory-management
date: 2026-09-10
categories: ["windows-errors"]
tags: ["memory management", "BSOD", "RAM"]
description: "Stop code Memory Management means Windows found corruption in RAM handling. Test your memory, fix drivers, and stop this blue screen for good."
thumbnail: "/images/thumbs/what-to-do-if-stop-code-memory-management.webp"
faqs:
  - q: "What does stop code Memory Management mean?"
    a: "It means Windows detected serious corruption in how memory is being managed — a driver wrote to memory it should not have touched, RAM returned bad data, or the memory manager's own structures got damaged. Windows halts with this stop code to prevent the corruption from spreading to your files. The cause splits roughly between faulty RAM, bad drivers, and corrupted system files."
  - q: "Is Memory Management always bad RAM?"
    a: "No, and that is the most common misconception about this stop code. Faulty drivers — especially graphics and storage drivers — are at least as common a cause as bad memory. Run the memory tests first because they give a definitive answer, but if the RAM passes, focus on drivers and system file repair rather than buying new memory."
  - q: "Can outdated drivers cause Memory Management BSOD?"
    a: "Yes. Drivers that mishandle memory allocations or write past their buffers corrupt the memory manager's bookkeeping, and Windows responds with this exact stop code. The biggest offenders are display drivers, storage controller drivers, and network drivers. Updating them from the manufacturer's site — not just Windows Update — resolves a large share of these crashes."
  - q: "How do I stop Memory Management blue screens permanently?"
    a: "Test the RAM with MemTest86 and replace any failing module, update all major drivers from manufacturer sources, run SFC and DISM to repair system files, and disable unstable overclocks. If crashes continue after all of that on a laptop with soldered RAM, have the machine serviced — the memory controller or board may be at fault."
---

Stop code Memory Management is Windows catching corruption in its own memory bookkeeping and pulling the emergency brake. It can strike at random — browsing, gaming, waking from sleep — and the randomness is the clue: something is corrupting memory in ways that only sometimes become visible. The name points at RAM, and sometimes it really is the RAM, but drivers cause this stop code just as often.

The way to handle it is elimination. Test the memory properly (one definitive test beats a week of guessing), then clean up drivers, then repair Windows itself. Most people find the answer in the first three fixes below.

## Why this happens

- **Failing RAM modules.** Degraded memory cells return corrupted data that the memory manager cannot trust.
- **Buggy graphics, storage, or network drivers.** Drivers that corrupt memory pools trigger this stop code directly.
- **Corrupted system files.** Damaged memory-management components inside Windows itself.
- **Unstable overclock or XMP profile.** Aggressive timings corrupt data in transit through RAM.
- **Disk errors.** Corrupted pagefile or system files on a failing drive manifest as memory errors.
- **Conflicting software.** Some antivirus and "RAM optimizer" tools interfere with memory management.

## How to fix it

Work through these in order, using the laptop normally between steps to check stability.

### Fix 1: Run Windows Memory Diagnostic

A quick first pass at the most feared cause.

1. Press `Win + R`, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems (recommended)**.
3. Let the **Standard** test complete — do not interrupt it.
4. After rebooting, open **Event Viewer > Windows Logs > System** and filter for **MemoryDiagnostics-Results** to read the verdict.
5. Errors here mean bad RAM — jump to Fix 6. A clean result means continuing below, but consider Fix 2 for certainty.

### Fix 2: Confirm with MemTest86

The Windows test can miss intermittent faults; MemTest86 rarely does.

1. On another PC, create a bootable MemTest86 USB drive.
2. Boot your laptop from it via the boot menu (**F12**/**F9**/**Esc** depending on brand).
3. Run at least **two full passes** (several hours for 16 GB).
4. Any errors confirm faulty RAM. Test sticks individually to isolate the bad one.
5. Clean results point firmly at drivers or software — continue below with confidence.

### Fix 3: Update your major drivers from manufacturer sources

This fixes the largest share of non-RAM cases.

1. Open **Device Manager** (`Win + X`).
2. Update **Display adapters** first — but do it properly: download from [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) rather than relying on Windows Update.
3. Update **Storage controllers**, **IDE ATA/ATAPI controllers**, and **Network adapters** the same way.
4. Get the chipset driver from your laptop maker: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
5. Restart and use the laptop normally for a day to verify.

### Fix 4: Run SFC and DISM

Repair the Windows memory-management components themselves.

1. Open **Terminal (Admin)** from `Win + X`.
2. Run `sfc /scannow` and let it finish.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart the laptop.

### Fix 5: Disable overclocking and Fast Startup

Both can produce or preserve memory corruption.

1. Enter the BIOS (**F2**/**Del** at boot) and disable **XMP**/**EXPO** profiles and any CPU overclock; load optimized defaults.
2. In Windows, open **Control Panel > Power Options > Choose what the power buttons do**.
3. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
4. Shut down fully once (not restart), then power on and test.

### Fix 6: Reseat or replace the RAM

For confirmed memory faults on laptops with removable RAM:

1. Power off, unplug, and remove the charger and battery if removable.
2. Open the bottom panel and reseat each RAM stick — remove it fully and click it firmly back in.
3. Test with one stick at a time to isolate the faulty module.
4. Replace the bad stick with matching spec RAM (type, speed, voltage).
5. On ultrabooks with soldered RAM, a confirmed fault means a warranty or board-level repair — contact the manufacturer.

Related RAM-linked crashes are covered in our guides to [PFN List Corrupt](/articles/how-to-fix-pfn-list-corrupt-after-windows-11-update/) and the [Memory Management BSOD fix](/articles/memory-management-bsod-windows-11-fix/).

### Fix 7: Check the drive and pagefile

Disk-level corruption can masquerade as memory errors.

1. Open **Command Prompt (Admin)** and run `chkdsk C: /f`, scheduling it for restart if asked.
2. After the check, open **Settings > System > About > Advanced system settings > Performance Settings > Advanced > Virtual memory**.
3. If the pagefile was manually set to a odd size, switch it back to **Automatically manage paging file size for all drives**.
4. Restart and monitor.

### Fix 8: Update the BIOS and check for known Windows issues

Firmware and OS-level bugs occasionally produce this stop code on specific hardware.

1. Check your BIOS version with `msinfo32` and compare it to the latest on the manufacturer's support site.
2. Update the BIOS if you are behind — keep the charger connected and do not interrupt the flash.
3. After updating, load BIOS defaults to clear any stale settings.
4. Check Microsoft's Windows release health dashboard (via [Microsoft Support](https://support.microsoft.com/en-us/windows)) for known memory-management issues with your current build — if one is documented, the fix may be a specific cumulative update rather than anything on your machine.

## Closing

Stop code Memory Management rewards a methodical approach: test the RAM definitively, update drivers from the real manufacturer sources, repair system files, and kill unstable overclocks. That sequence finds the actual cause instead of throwing parts at the problem. If MemTest86 gives your memory a clean bill of health and fresh drivers do not help, look hard at the drive and consider a clean Windows install before concluding the hardware is at fault — software causes are simply more common than dead RAM.
