---
title: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: Fix This Blue Screen Error"
slug: attempted-execute-of-noexecute-memory-blue-screen-error-fix
date: 2026-10-12
categories: ["windows-errors"]
tags: ["bsod", "stop code", "memory", "drivers"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen? It's a memory-protection violation — usually bad RAM, a buggy driver, or malware. Here's the fix."
thumbnail: "/images/thumbs/attempted-execute-of-noexecute-memory-blue-screen-error-fix.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean?"
    a: "Windows marks certain memory regions as non-executable (data only). This stop code means a program or driver tried to run code from one of those regions — a classic sign of a buggy driver, failing RAM corrupting pointers, or malware attempting code injection."
  - q: "Is this error caused by bad RAM?"
    a: "Often, yes. Failing memory corrupts the pointers drivers use, sending execution into non-executable regions. But buggy drivers and malware cause the identical crash, so test memory AND check drivers before buying new RAM."
  - q: "Could this be a virus?"
    a: "It's possible — this exact crash pattern is what happens when malicious code tries to execute from data regions. If the crashes started after downloading something sketchy, run a full Windows Defender offline scan before assuming hardware failure."
  - q: "Will I lose data fixing this?"
    a: "No. Memory tests, driver updates, malware scans, and system file repairs don't touch your files. Back up anyway as good practice, but none of these fixes delete anything."
---

`ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY` is one of the more technical-sounding blue screens, but the idea is simple: modern CPUs mark memory regions as either "you can run code here" or "data only." Something — a driver, failing RAM, or malware — tried to run code from a data-only region, and Windows crashed rather than allow it. The name sounds exotic; the causes are the usual suspects.

Because three very different problems (bad RAM, bad driver, malware) produce this exact crash, the fix order matters: rule out the dangerous and the free stuff first, then test hardware.

Here's a useful mental model while you work: think of this crash as Windows catching someone somewhere they shouldn't be. The "someone" is a thread of execution; the "somewhere" is a memory page marked NX (no-execute). Either the thread was given a wrong address (bad RAM corrupting a pointer, or a driver bug computing a bad jump), or the thread is genuinely hostile (malware). Your job in the fixes below is to figure out which of those three stories fits — and the order is designed so each fix eliminates one suspect cleanly.

## Why this happens

- **Failing RAM corrupting pointers**: The most common hardware cause. Bad memory flips bits in the addresses drivers use, redirecting execution into non-executable regions. The driver is innocent; the RAM lied to it.
- **Buggy or outdated drivers**: A driver with a memory bug can genuinely try to execute from a data region. Graphics and network drivers are frequent offenders, especially after Windows updates.
- **Malware attempting code injection**: Malicious code often tries to run from memory regions marked non-executable — that's exactly what Data Execution Prevention is designed to catch, and this crash is DEP doing its job loudly.
- **Corrupted system files**: Damage to kernel memory-management components can mislabel regions or mishandle execution permissions.
- **Overclocked or unstable memory**: XMP profiles pushed too far, or manual RAM overclocks that were "stable enough" until now, produce exactly this class of error.
- **Failing storage corrupting loaded drivers**: A dying SSD can corrupt driver code as it loads into memory, producing execution faults that look like memory problems.

## How to fix it

Work through these in order — malware scan and memory test come before driver work for a reason.

### Fix 1: Run a full malware scan

Rule out the malicious cause first, since it's the one that gets worse with time.

1. Open **Windows Security** (**Win + S**, type `windows security`, press Enter).
2. Go to **Virus & threat protection** > **Scan options**.
3. Select **Microsoft Defender Offline scan** and click **Scan now**. The laptop restarts into a clean environment outside Windows and scans deeply.
4. Remove anything found, restart normally, and see if crashes stop.
5. If you run third-party antivirus, update it and run its full/boot-time scan too.

### Fix 2: Test your RAM thoroughly

Memory is the top hardware suspect — test it properly, not quickly.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Let Windows Memory Diagnostic complete both passes. Any error — even one — means bad RAM.
3. For a definitive test, run MemTest86 from a USB stick overnight (4+ passes). Windows' built-in test is good; MemTest86 is conclusive.
4. If errors appear and your laptop has removable RAM, test sticks one at a time to identify the bad one. If RAM is soldered, the motherboard needs professional service.

### Fix 3: Reset memory overclocks and XMP

Unstable memory settings produce exactly this crash signature.

1. Restart and enter BIOS/UEFI (**F2**, **Del**, or **Esc** depending on brand).
2. Find memory settings and disable **XMP** / **EXPO** / **DOCP**, or choose **Load Optimized Defaults** (**F9**).
3. Save (**F10**) and test for a few days at stock memory speeds.
4. Only re-enable XMP after a week of stability — and if crashes return, that RAM simply can't hold its rated speed.

### Fix 4: Update your drivers

With malware and RAM addressed, fix the software side.

1. Press **Win + X** and open **Device Manager**.
2. Update **Display adapters**, **Network adapters**, and **System devices** drivers (right-click > **Update driver** > **Search automatically**).
3. Get graphics drivers from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
4. Install all pending Windows updates too — **Settings** > **Windows Update** — since Microsoft ships driver and memory-management fixes in cumulative updates.

### Fix 5: Check which driver the dump blames

If crashes continue, read the evidence.

1. Open `C:\Windows\Minidump` and examine the newest dump per [how to check minidump files on Windows 11](/articles/how-to-check-minidump-files-on-windows-11/).
2. If a specific driver is named, update it, roll it back, or uninstall its software entirely.
3. If dumps blame random different drivers each time, that's the classic fingerprint of bad RAM — go back to Fix 2 and test harder.

### Fix 6: Repair system files

Corrupted kernel components can mishandle execution permissions.

1. Open an elevated **Command Prompt**.
2. Run:

   ```cmd
   DISM /Online /Cleanup-Image /RestoreHealth
   ```

3. Then:

   ```cmd
   sfc /scannow
   ```

4. Restart and monitor.

### Fix 7: Check drive health

A failing drive corrupts what it loads into memory.

1. In an elevated Command Prompt, run:

   ```cmd
   chkdsk C: /f /r
   ```

   Type **Y** and restart to let it scan.

2. Check SSD health with the manufacturer's utility (Samsung Magician, Crucial Storage Executive, WD Dashboard) — look at percentage used and available spare.
3. If the drive is failing, back up immediately and replace it. For the related crash pattern, see [what to do about faulty hardware corrupted page](/articles/what-to-do-if-faulty-hardware-corrupted-page/).

### Fix 8: Verify DEP settings and do a final stability check

Data Execution Prevention is the mechanism behind this crash — make sure it's configured correctly, then prove stability.

1. Press **Win + R**, type `sysdm.cpl`, press Enter, and go to the **Advanced** tab.
2. Under **Performance**, click **Settings**, then the **Data Execution Prevention** tab.
3. Ensure **Turn on DEP for essential Windows programs and services only** is selected (the default). Don't add blanket exceptions for crashing programs — that just hides the symptom.
4. Use the laptop hard for a few days: the workloads that used to crash it, plus sleep/wake cycles. Check `C:\Windows\Minidump` for new dumps — none means the fix held.

## Closing

`ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY` demands a particular discipline: scan for malware, test the RAM properly, then work the drivers. The dump pattern tells you which world you're in — one consistent driver means software, random drivers mean memory. Follow that signal and you'll land on the real cause. For the closely related pool-corruption variant, read [how to fix special pool detected memory corruption](/articles/how-to-fix-special-pool-detected-memory-corruption-after-windows-11-update/).
