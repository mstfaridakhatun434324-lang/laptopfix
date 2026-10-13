---
title: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on Windows 11"
slug: how-to-fix-attempted-execute-of-noexecute-memory-on-windows-11
date: 2026-09-23
categories: ["windows-errors"]
tags: ["attempted execute of noexecute memory", "blue screen", "windows 11"]
description: "Fix the ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen on Windows 11: refresh drivers, scan for malware, and test your memory step by step."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-on-windows-11.webp"
faqs:
  - q: "What triggers ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on Windows 11?"
    a: "Stop code 0x000000FC fires when a driver tries to execute code from memory marked non-executable. On Windows 11 the usual triggers are outdated graphics or chipset drivers, a bad driver pushed by Windows Update, failing RAM, or kernel-level software like VPNs and old antivirus products."
  - q: "Does Windows 11 24H2 cause this error?"
    a: "The 24H2 update itself does not cause it, but it can expose drivers that were already marginal — especially graphics and network drivers written for older Windows builds. Updating those drivers to 24H2-compatible versions resolves most cases."
  - q: "How do I know which driver is responsible?"
    a: "Check Event Viewer → Windows Logs → System for BugCheck entries naming a .sys file, or open the minidump in WinDbg. If no file is named, start with the graphics driver — it is the culprit in the majority of cases."
  - q: "Can I fix it without reinstalling Windows?"
    a: "Almost always, yes. Driver updates, SFC/DISM repairs, and memory testing resolve this error in the overwhelming majority of cases. Reinstallation is only needed if system files are damaged beyond what DISM can repair."
---

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (0x000000FC) is Windows 11's Data Execution Prevention catching a driver doing something forbidden: running code from a memory page reserved for data. Windows treats this as a potential exploit and crashes immediately. It feels dramatic, but the cause is mundane far more often than not.

On Windows 11, and especially after the 24H2 update, this crash usually means a driver that has not kept up — graphics first, then chipset and network. The steps below go from quick checks to deeper hardware tests, in the order that resolves most cases fastest.

## Why this happens

- **Graphics driver lagging behind Windows 11:** The number one cause. GPU drivers that predate your Windows build mishandle memory protection under load.
- **A driver pushed by Windows Update:** Windows Update occasionally installs a driver version with a regression. The crash often starts within days of an update.
- **Failing or unstable RAM:** Bad memory corrupts page attributes, making legitimate driver code look like an execution violation.
- **Outdated kernel-level software:** VPN clients, virtual machine tools, and third-party antivirus install drivers that run in protected memory regions.
- **Overclocking:** XMP memory profiles or CPU overclocks that are borderline-stable corrupt execution flow under heavy load.
- **Corrupted system files:** A bad update or sudden power loss can damage kernel components that manage memory protection.
- **Malware:** Uncommon, but code-injection malware triggers exactly this protection. A quick Defender scan rules it out.

## How to fix it

Work through these in order — stop as soon as the crashes end.

### Fix 1: Rule out malware with a full Defender scan

1. Open **Settings → Privacy & security → Windows Security → Virus & threat protection**.
2. Choose **Scan options → Full scan → Scan now** and let it finish.
3. Remove anything found, restart, and test for a day.
4. A clean scan lets you focus on drivers with confidence. If Defender will not run properly, Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover recovery options.

### Fix 2: Clean-install the latest graphics driver

1. Identify your GPU with **Win + R → `dxdiag` → Display tab**.
2. Download the newest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, or via [Intel's tool](https://www.intel.com/content/www/us/en/support/detect.html).
3. Run the installer, choose **Custom**, and tick **Perform a clean installation** (NVIDIA/AMD) to remove all traces of the old driver.
4. Restart. This single step fixes more 0xFC crashes than everything else combined — do not skip the clean-install option.

### Fix 3: Update chipset, Wi-Fi, and Bluetooth drivers

1. Go to your laptop maker's support page (Dell, HP, Lenovo, ASUS, Acer) and download the latest **chipset** driver for your exact model.
2. Install the newest **Wi-Fi** and **Bluetooth** drivers from the same page.
3. Avoid relying on Device Manager's automatic search here — manufacturer packages are newer and better tested.
4. Restart and use the laptop normally for a day. Network drivers are the second most common trigger after graphics.

### Fix 4: Uninstall the last Windows update if crashes just started

1. Open **Settings → Windows Update → Update history → Uninstall updates**.
2. Remove the most recent update and restart.
3. If stability returns, the update's bundled driver was the problem. Pause updates for two weeks, then reinstall — the vendor usually ships a fixed driver quickly.
4. For granular control, download updates manually from the Microsoft Update Catalog so you can skip driver updates while taking security fixes.

### Fix 5: Remove suspect kernel-level software

1. Open **Settings → Apps → Installed apps**, sort by install date.
2. Uninstall VPN clients, virtual machine software, RGB control apps, and any third-party antivirus you installed around the time crashes began.
3. In **Device Manager → View → Show hidden devices**, remove greyed-out remnants of uninstalled software.
4. Restart and test. These programs install drivers that live in exactly the memory regions this error protects.

### Fix 6: Repair system files with SFC and DISM

1. Open **Terminal (Admin)** from the Start right-click menu.
2. Run `sfc /scannow` and wait for completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` once more.
4. Restart. This repairs kernel and system files that a bad update may have corrupted — damage that can mimic a driver fault. If you are seeing several different stop codes, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) helps sort out which to chase first.

### Fix 7: Test memory and reset overclocks

1. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. If errors appear, reseat the RAM (if accessible) and retest; persistent errors mean the module needs replacing.
3. Enter the BIOS and choose **Load Optimized Defaults** to clear XMP or CPU overclocks.
4. Retest under load (a game or stress test). Memory faults and unstable overclocks produce this exact stop code, so this step matters when every driver already looks fine.

### Fix 8: Update the BIOS and reset firmware to defaults

Stale firmware can mismanage memory protection attributes that Windows 11 relies on. A BIOS update plus a settings reset closes that gap.

1. Press **Win + R**, type `msinfo32`, and note the **BIOS Version/Date**.
2. Check your manufacturer's support page for a newer BIOS for your exact model and install it on AC power.
3. Enter the BIOS and choose **Load Optimized Defaults** to clear XMP or CPU overclocks.
4. Save, exit, and retest under the workload that crashed. Firmware-level memory handling affects exactly the protections this stop code enforces.
5. If memory-adjacent crashes persist in other forms, our [memory management guide](/articles/memory-management-bsod-windows-11-fix/) covers the sibling stop code.

## Closing

On Windows 11, ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is a driver problem until proven otherwise — and the proof usually arrives with a clean graphics driver install from the chip vendor. Move through the list methodically: scan for malware, update graphics and chipset drivers from official sources, strip out recent kernel-level software, repair system files, test the RAM, and finish with a BIOS refresh. The crash looks severe because Windows treats it like an exploit attempt, but the fix is routine maintenance in the vast majority of cases.
