---
title: "REFERENCE_BY_POINTER Blue Screen? Here's What to Do"
slug: what-to-do-if-reference-by-pointer-bsod
date: 2026-09-19
categories: ["windows-errors"]
tags: ["reference by pointer", "bsod", "blue screen", "windows 11", "driver"]
description: "REFERENCE_BY_POINTER (stop code 0x18) means a driver mishandled an object reference count. Here's what to do, from driver updates to memory testing."
thumbnail: "/images/thumbs/what-to-do-if-reference-by-pointer-bsod.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "It's stop code 0x18, and it means a kernel-mode driver called ObReferenceObject or ObDereferenceObject incorrectly, corrupting an object's reference count. In plain terms: a driver told Windows 'I'm done with this system object' too many times, or referenced something improperly. When the count goes wrong, Windows crashes to protect itself. The faulty driver is almost always third-party — antivirus filters, old hardware drivers, or virtualization tools."
  - q: "Is REFERENCE_BY_POINTER caused by bad RAM?"
    a: "Rarely, but it can't be ruled out. This stop code is overwhelmingly a driver bug — faulty RAM more typically produces MEMORY_MANAGEMENT or PAGE_FAULT_IN_NONPAGED_AREA. Still, if you've updated or removed every suspect driver and the crashes continue, run Windows Memory Diagnostic to eliminate RAM. A single failing stick can corrupt the exact kernel structures this stop code involves."
  - q: "Which drivers most often cause this blue screen?"
    a: "Antivirus and security filter drivers are the classic offenders, followed by old storage controller drivers, outdated chipset drivers, virtual machine drivers (VirtualBox, VMware), and VPN network filter drivers. Anything that installs a kernel-mode filter — software that inspects files, network traffic, or disk I/O — is a prime suspect. Check the crash dump for the named driver."
  - q: "Can I just disable the driver causing it?"
    a: "Sometimes, as a diagnostic step. If the dump names a non-essential driver — a VPN filter, an old printer driver, a game anti-cheat — disabling or uninstalling its software stops the crashes and confirms the diagnosis. For essential drivers like storage controllers, don't disable; update or replace them instead. Never leave a storage or security driver disabled permanently without a replacement plan."
---

REFERENCE_BY_POINTER is one of the more cryptic blue screens in Windows 11. Stop code 0x18 doesn't describe a failed device or a bad sector — it describes a bookkeeping error deep in the Windows kernel. A driver mishandled the reference count of a system object, and Windows crashed rather than continue with corrupted internal state. The good news: because it's almost always a specific third-party driver misbehaving, it's usually fixable without hardware replacement.

The challenge is identification. Unlike VIDEO_TDR_FAILURE, which names your GPU driver, REFERENCE_BY_POINTER doesn't always point at the culprit on the blue screen itself. The name of the offending driver is usually buried in the crash dump file. So the first thing to do is capture that information — then the fix is typically a driver update, rollback, or removal. Work the steps below in order and you'll either fix it or prove it's hardware.

## Why this happens

- **Buggy third-party filter driver**: Antivirus, backup, and disk-utility software installs kernel filters that intercept system operations. A bug in reference counting here is the classic cause.
- **Outdated storage controller driver**: Old AHCI/RAID or NVMe drivers mishandling I/O completion can trigger this stop code during heavy disk activity.
- **Virtualization drivers**: VirtualBox, VMware, and Hyper-V-adjacent tools install kernel drivers that manipulate objects aggressively — version mismatches cause reference bugs.
- **VPN or network filter drivers**: VPN clients install network filter drivers; a buggy one can corrupt object references during connection setup and teardown.
- **Corrupt driver installation**: Even a normally good driver can cause this if its files are damaged by disk errors or a failed update.
- **Failing RAM corrupting kernel structures**: Rare, but faulty memory can flip bits in the exact reference-count fields this stop code monitors.
- **Overclocking instability**: An unstable CPU or memory overclock can corrupt kernel data structures, producing driver-blaming stop codes that are really hardware instability.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the culprit from the crash dump

Don't guess — read the dump. The driver name is usually right there.

1. Install WinDbg Preview from the Microsoft Store, or use BlueScreenView for a quicker read.
2. Open the latest dump from `C:\Windows\Minidump\` and look at the `MODULE_NAME` / `IMAGE_NAME` fields and the stack trace.
3. Note the driver filename — e.g., something like `avgntflt.sys` (antivirus filter) or `vboxdrv.sys` (VirtualBox). That names your suspect.
4. If reading dumps is new to you, our [WinDbg walkthrough](/articles/how-to-read-dump-files-with-windbg-in-windows-11-24h2/) covers the process step by step.

### Fix 2: Update or remove the suspect driver

Once you have a name, act on it.

1. If the driver belongs to antivirus or security software, update that software to the latest version first — vendors patch these bugs regularly.
2. If it's already current, temporarily uninstall the software entirely and test for a few days. No crashes means confirmed — then try a competing product or an older version.
3. For hardware drivers (storage, chipset), get the update from your laptop manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo — rather than generic Windows Update versions.
4. For virtualization tools, update to the latest release; if crashes persist, disable the virtual network adapters you don't use.

### Fix 3: Roll back recent driver and software changes

If the crashes started after a specific change, undo it.

1. Open **Device Manager**, find recently updated devices, and use **Properties** > **Driver** > **Roll Back Driver** where available.
2. Check **Settings** > **Apps** > **Installed apps**, sorted by install date — uninstall anything added just before the crashes began, especially security tools, VPNs, and disk utilities.
3. Check **Settings** > **Windows Update** > **Update history** — if a driver update arrived via Windows Update at the wrong time, roll it back and use the manufacturer's driver instead.

### Fix 4: Run Driver Verifier to catch the offender

If the dump is inconclusive, make Windows catch the driver in the act.

1. Press **Windows + R**, type `verifier`, and press Enter.
2. Choose **Create standard settings**, then **Automatically select unsigned drivers** (or manually select the suspects from Fix 1).
3. Restart. Verifier stresses drivers — the system will crash faster and the dump will name the offender precisely. This is diagnostic, not a fix.
4. After capturing the dump, boot into Safe Mode and run `verifier /reset` to turn it off — never leave Verifier running permanently, as it degrades performance.

### Fix 5: Test your RAM

Rule out the hardware explanation before going deeper into software.

1. Press **Windows + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Let the full test complete. Any reported errors mean bad RAM — replace the faulty stick.
3. For a more thorough test, run MemTest86 from a bootable USB overnight. Our [memory-focused blue screen guide](/articles/memory-management-bsod-windows-11-fix/) explains how RAM faults disguise themselves as driver crashes.

### Fix 6: Disable overclocks and check system stability

Unstable overclocks corrupt kernel structures and produce exactly this class of stop code.

1. Enter BIOS/UEFI and load optimized defaults — disable CPU overclocking, XMP memory profiles, and any "performance enhancement" multi-core settings.
2. If you use Intel XTU or Ryzen Master, reset those to stock too.
3. Test for several days at stock settings. If crashes stop, your overclock was the cause — re-tune more conservatively if you want the performance back.

### Fix 7: Repair system files and check the disk

Corrupt system files can make good drivers look guilty.

1. Open **Windows Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow` and restart.
3. Run `chkdsk C: /f` (schedule at reboot if asked) to rule out file system damage corrupting driver files.
4. If you need a refresher on these tools, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents them officially.

### Fix 8: Clean-boot to isolate software conflicts

When dumps and Verifier still don't name a culprit, isolate by elimination.

1. Press **Windows + R**, type `msconfig`, go to the **Services** tab, tick **Hide all Microsoft services**, and click **Disable all**.
2. In **Task Manager** > **Startup apps**, disable everything non-Microsoft, then restart.
3. If crashes stop, re-enable services in halves until the crashes return — the last group enabled contains your culprit.
4. Once identified, update, replace, or permanently remove the offending software.

## Closing

REFERENCE_BY_POINTER rewards a detective's mindset: the stop code tells you a driver broke the kernel's bookkeeping, the dump usually names the driver, and the fix is almost always updating or removing that one piece of software. Resist the urge to reinstall Windows at the first sight of it — that's the slowest possible way to fix a single bad driver. Work the identification steps first, and you'll usually have a name, a fix, and a stable system within the hour. If your dumps instead keep naming memory-corruption patterns, our [memory management guide](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) takes over from there.
