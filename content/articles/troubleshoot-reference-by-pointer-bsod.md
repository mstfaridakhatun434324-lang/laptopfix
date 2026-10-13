---
title: "Troubleshooting the REFERENCE_BY_POINTER Blue Screen in Windows 11"
slug: troubleshoot-reference-by-pointer-bsod
date: 2026-09-10
categories: ["windows-errors"]
tags: ["reference by pointer", "bsod", "stop code 0x18", "driver", "windows 11"]
description: "REFERENCE_BY_POINTER blue screen on Windows 11? Troubleshoot stop code 0x18 — a driver object reference-count bug — with 7 proven fixes."
thumbnail: "/images/thumbs/troubleshoot-reference-by-pointer-bsod.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "Stop code 0x18 means a driver's reference count for an object dropped below zero — drivers increment a counter when they use a kernel object and decrement it when done, and going negative means something decremented too many times. It is a driver bug, almost always in a third-party driver that mishandles object lifetimes."
  - q: "Which drivers cause REFERENCE_BY_POINTER?"
    a: "The usual suspects are antivirus filter drivers, VPN clients, virtual-device software, and older hardware drivers. Because the corruption is in reference counting, Driver Verifier with pool tracking is the definitive way to identify the guilty driver rather than guessing."
  - q: "Is REFERENCE_BY_POINTER a virus?"
    a: "No — it is a programming bug in a driver, not malware behavior. That said, rootkits operate at the driver level and can cause similar crashes, so if the crashes began after installing suspicious software, run a full Microsoft Defender scan to rule that out."
  - q: "Can RAM cause REFERENCE_BY_POINTER?"
    a: "Rarely, but yes — faulty RAM can corrupt the reference-count values in memory, mimicking a driver bug perfectly. If Driver Verifier implicates no driver, or different drivers are blamed across crashes, test your memory with mdsched.exe and MemTest86 before continuing to chase software causes."
---

REFERENCE_BY_POINTER — stop code 0x18 — is one of Windows' more technical-sounding blue screens, but the concept is simple: kernel objects (files, devices, processes) carry a reference count, and drivers are supposed to increment it when they start using an object and decrement it when finished. When a buggy driver decrements too many times, the count goes negative, Windows detects the impossibility, and the system crashes. It's an accounting error in kernel mode, and like all accounting errors, it points at whoever kept the books — a driver.

Because the crash is detected after the bad decrement already happened, the stop screen rarely names the culprit directly. That makes this a Driver Verifier case: Windows' built-in tool that catches the offending driver in the act. The sequence below clears the easy suspects first, then deploys Verifier for the definitive answer.

## Why this happens

- **Buggy third-party drivers.** Antivirus filters, VPN clients, and virtual-device drivers mishandling object reference counts.
- **Outdated drivers on new Windows builds.** Older drivers violating object-lifetime rules that newer Windows checks more strictly.
- **Corrupted driver installations.** Mixed driver files behaving unpredictably in object management.
- **Incompatible security software.** Kernel-level filters from security products are classic 0x18 offenders.
- **Faulty RAM.** Corrupts reference-count values in memory, mimicking driver bugs.
- **Corrupted system files.** Damage to the kernel's object manager producing false corruption signals.
- **Driver conflicts.** Two drivers managing the same device object and double-releasing it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Remove or update security and VPN software

Kernel filters are the top 0x18 suspects — start here.

1. Uninstall third-party antivirus with the vendor's removal tool (a full removal, not just disabling).
2. Remove VPN clients, firewall utilities, and endpoint-protection agents temporarily.
3. Test on Microsoft Defender alone for several days.
4. If crashes stop, reinstall only the latest versions — outdated filter drivers cause most 0x18 cases.
5. Never run two real-time security products at once; their object-management interactions are a known trigger.

### Fix 2: Update all major drivers

Clear the general driver bug backlog.

1. Update **chipset**, **network**, **graphics**, and **storage** drivers from your laptop maker's support page.
2. On Intel systems, run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Clean-install the GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
4. Remove "driver updater" utilities — they install mismatched drivers that cause exactly this class of bug.
5. Restart after each major driver group and test before moving on.

The update-triggered variant has its own guide: [how to fix REFERENCE_BY_POINTER BSOD after a Windows 11 update](/articles/how-to-fix-reference-by-pointer-bsod-after-windows-11-update/).

### Fix 3: Run Driver Verifier to identify the guilty driver

Catch the bad decrement in the act.

1. Create a **system restore point** — mandatory before Verifier.
2. Press **Windows + R**, type `verifier`, press Enter.
3. Choose **Create custom settings**; enable **Special pool**, **Pool tracking**, **Force IRQL checking**.
4. Choose **Select driver names from a list**, sort by **Provider**, check all **non-Microsoft** drivers.
5. **Finish**, restart, and use the laptop normally — Verifier will crash the system naming the driver when it catches the violation.
6. Open the resulting minidump in WinDbg (`!analyze -v`) to confirm the culprit.
7. Boot to **Safe Mode**, run `verifier /reset`, restart, then update or remove the guilty driver.

Target third-party drivers only — verifying Microsoft drivers adds noise and boot-loop risk.

### Fix 4: Remove virtual-device and peripheral software

Virtual drivers are disproportionate 0x18 offenders.

1. Uninstall virtual audio cables, virtual cameras, virtual CD drives, and Android emulators temporarily.
2. Remove RGB/fan-control utilities and "gaming optimizer" tools that install kernel drivers.
3. Disconnect non-essential USB peripherals and uninstall their companion software for testing.
4. If crashes stop, reinstall needed tools one at a time, checking for updates first.
5. Prefer software with recent updates — abandoned peripheral utilities ship the oldest, buggiest drivers.

The 24H2-specific angle is covered in [how to fix REFERENCE_BY_POINTER BSOD in Windows 11 24H2](/articles/how-to-fix-reference-by-pointer-bsod-in-windows-11-24h2/).

### Fix 5: Test your RAM

When Verifier finds nothing, check the hardware.

1. Run `mdsched.exe`, choose **Restart now and check for problems**.
2. Check **Event Viewer > Windows Logs > System > MemoryDiagnostics-Results**.
3. Run MemTest86 overnight for intermittent faults.
4. Load BIOS **Optimized Defaults** to clear unstable timings.
5. If different drivers are blamed on different crashes, treat RAM as the prime suspect regardless of quick-test results.

### Fix 6: Repair system files and update Windows

Fix the kernel's object manager itself.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Install all pending updates in **Settings > Windows Update**.
3. Check the Microsoft Update Catalog for superseding fixes if a specific KB preceded the crashes.
4. Consider an in-place upgrade from the Windows 11 download page (keep files and apps) as a deep repair.
5. Retest before reinstalling third-party drivers — add them back one group at a time.

### Fix 7: Clean-boot isolation for stubborn cases

Eliminate by halves when the culprit hides.

1. `msconfig` → hide Microsoft services → disable the rest; disable all Startup apps; restart.
2. Stress-test; if 0x18 stops, re-enable in halves to find the offender.
3. Prioritize backup tools, disk utilities, and anything installing filter drivers.
4. Update or permanently remove whatever you find.
5. If the clean boot is stable but normal boot crashes even with everything re-enabled one at a time, suspect an interaction between two drivers — keep the minimal set you actually need.

## Closing

REFERENCE_BY_POINTER is a driver-accounting bug, and the fix is accounting-style discipline: clear the usual suspects (security filters, virtual-device drivers), then let Driver Verifier audit the books and name the driver that's cooking them. Most 0x18 cases end with an outdated filter driver being updated or removed — unglamorous, but effective. The trap is guessing: with no driver named on the stop screen, random driver reinstalls are just expensive superstition. Verifier gives you the name; act on it, and the reference counts stay honest.
