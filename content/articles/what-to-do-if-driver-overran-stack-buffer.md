---
title: "What to Do If You Get Driver Overran Stack Buffer Blue Screen"
slug: what-to-do-if-driver-overran-stack-buffer
date: 2026-09-20
categories: ["windows-errors"]
tags: ["driver overran stack buffer", "BSOD", "driver bug"]
description: "Driver Overran Stack Buffer means a driver corrupted kernel memory. Find the bad driver, remove it safely, and end the crashes."
thumbnail: "/images/thumbs/what-to-do-if-driver-overran-stack-buffer.webp"
faqs:
  - q: "What does Driver Overran Stack Buffer mean?"
    a: "It means a driver wrote more data than its allocated memory buffer could hold — a buffer overflow in kernel mode — corrupting adjacent memory. Windows detects the corruption and crashes deliberately to prevent further damage. The cause is virtually always a buggy driver, most commonly a recently updated or newly installed one, rather than failing hardware."
  - q: "Which drivers cause this blue screen most often?"
    a: "Network drivers (Wi-Fi and Ethernet), graphics drivers, and USB or peripheral drivers top the list. Third-party antivirus filter drivers and VPN clients also show up regularly. The pattern to look for is timing: whichever driver was installed or updated just before the crashes began is the prime suspect."
  - q: "Can I fix it without knowing which driver is bad?"
    a: "Yes, with a systematic approach. Boot into Safe Mode, roll back or uninstall recently updated drivers one category at a time (network first, then graphics, then the rest), and test between changes. If that does not isolate it, analyzing the minidump with WinDbg names the exact driver, removing all guesswork."
  - q: "Is Driver Overran Stack Buffer a virus?"
    a: "No, it is a legitimate Windows stop code indicating a driver bug. However, rootkits and some malware operate as malicious drivers and can trigger kernel corruption that looks similar. If the crashes coincide with other suspicious behavior, run a full scan with Microsoft Defender and Malwarebytes after stabilizing the system."
---

Driver Overran Stack Buffer is Windows catching a driver red-handed. A "stack buffer" is a chunk of memory a driver is allowed to use, and "overran" means the driver wrote past the end of it, stomping on neighboring memory. In user programs that is a crash; in a kernel driver, Windows halts the entire system to contain the damage. The name sounds technical, but the fix is practical: find the bad driver and replace it.

The good news is the suspect pool is small. This stop code is overwhelmingly caused by one recently changed driver, and the crashes usually started right after something was installed or updated. Think back to what changed — that memory is your best diagnostic tool.

## Why this happens

- **Recently updated buggy driver.** New driver versions occasionally ship with buffer-handling bugs.
- **Newly installed hardware or its driver.** Fresh peripherals bring fresh driver code, sometimes faulty.
- **Corrupted driver files.** Disk errors or bad installs damage a previously fine driver.
- **Conflicting drivers.** Two drivers for overlapping hardware corrupting shared memory regions.
- **Third-party antivirus or VPN filter drivers.** Kernel-level filters with memory bugs.
- **Malware operating as a driver.** Rare, but malicious kernel drivers corrupt memory similarly.

## How to fix it

Work through these in order, testing stability after each change.

### Fix 1: Identify what changed before the crashes

Your memory is the fastest diagnostic here.

1. Think back: did you install a new program, update a driver, add hardware, or install a Windows update just before crashes began?
2. Open **Settings > Windows Update > Update history** and check for driver updates around the start date.
3. Open **Settings > Apps > Installed apps**, sort by install date, and note recent additions.
4. The most recent change is your prime suspect — target it in the fixes below.

### Fix 2: Roll back the suspect driver

If a driver update preceded the crashes, undo it.

1. Open **Device Manager** (`Win + X`).
2. Find the device tied to your suspect (network adapter, display adapter, or the new hardware).
3. Right-click, **Properties > Driver tab > Roll Back Driver**, pick a reason, and confirm.
4. Restart and use the laptop normally to verify the crashes stop.
5. To prevent Windows Update from reinstalling the bad version, pause driver updates or use the manufacturer's older stable release.

### Fix 3: Update the driver from the manufacturer

If no recent update is the cause, the installed driver may simply be buggy or corrupted.

1. In **Device Manager**, note the exact device model.
2. Download the latest driver from the source: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or the laptop maker ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
3. For network drivers especially, prefer the laptop manufacturer's version — generic ones sometimes mismatch.
4. Install, restart, and test.

### Fix 4: Remove the driver from Safe Mode

If the driver crashes Windows on every boot:

1. Force WinRE (three interrupted boots), then **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4** for Safe Mode.
2. In Safe Mode open **Device Manager**, right-click the suspect device, and choose **Uninstall device** — check **Attempt to remove the driver software** if offered.
3. Restart normally; Windows will load a basic inbox driver.
4. Install the known-good manufacturer driver afterward.

### Fix 5: Uninstall recently added software with kernel components

Antivirus, VPN clients, and system utilities install filter drivers.

1. In Safe Mode (or normal mode if stable enough), open **Settings > Apps**.
2. Uninstall any antivirus, VPN, or "system optimizer" installed around the time crashes started.
3. Restart and test — Windows' built-in Defender covers you in the meantime.
4. Reinstall the software later only from the vendor's current release if you need it.

### Fix 6: Analyze the minidump to confirm the driver

Get the exact filename instead of guessing.

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open the newest dump in `C:\Windows\Minidump` and run `!analyze -v`.
3. The **IMAGE_NAME** line names the faulting driver file.
4. Search that filename to identify its vendor, then update, roll back, or remove that specific driver.

Our [minidump analysis guide](/articles/how-to-check-minidump-files-on-windows-11/) walks through this in detail.

### Fix 7: Run SFC/DISM and scan for malware

Cover the remaining bases.

1. Open **Terminal (Admin)** and run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Run a full scan with **Windows Security > Virus & threat protection > Scan options > Full scan**.
3. Consider a second-opinion scan with Malwarebytes free.
4. Restart and monitor.

Related driver-crash stop codes with similar fixes: [KMODE Exception Not Handled](/articles/how-to-fix-kmode-exception-not-handled-on-lenovo-laptop/) and our [driver-overran guide for post-update cases](/articles/how-to-fix-driver-overran-stack-buffer-after-windows-11-update/).

### Fix 8: Update the BIOS and chipset firmware

Low-level firmware bugs can corrupt the memory operations drivers rely on.

1. Check the current BIOS version in **System Information** (`msinfo32`).
2. Install the latest BIOS from the laptop manufacturer's support site with the charger connected.
3. Install the latest chipset driver package from the same site — chipset firmware updates fix memory-handling bugs that individual driver updates cannot.
4. Load BIOS defaults after the update, then reinstall the suspect driver from Fix 3 fresh.
5. Test stability for a day before declaring victory.

## Closing

Driver Overran Stack Buffer is refreshingly straightforward as blue screens go: a driver wrote where it should not have, and your job is to find it and replace it. Start with what changed most recently — the timeline rarely lies — roll back or update that driver from the manufacturer's site, and use the minidump to confirm when guessing is not enough. Once the buggy driver is gone, this stop code goes with it and stays gone. If you manage several machines, note which driver version caused it; the same bad release tends to strike more than once.
