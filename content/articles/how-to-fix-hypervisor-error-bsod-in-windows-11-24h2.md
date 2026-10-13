---
title: "How to Fix the HYPERVISOR_ERROR Blue Screen on Windows 11 24H2"
slug: how-to-fix-hypervisor-error-bsod-in-windows-11-24h2
date: 2026-09-03
categories: ["windows-errors"]
tags: ["bsod", "hyper-v", "virtualization"]
description: "HYPERVISOR_ERROR blue screen on Windows 11 24H2? Usually a virtualization conflict or bad driver. Here's the step-by-step fix."
thumbnail: "/images/thumbs/how-to-fix-hypervisor-error-bsod-in-windows-11-24h2.webp"
faqs:
  - q: "What is HYPERVISOR_ERROR on Windows 11?"
    a: "It's a blue screen (stop code 0x20001) from Windows' hypervisor layer — the virtualization component underneath Hyper-V, WSL2, Core Isolation, and Android apps. It means the hypervisor detected a fatal inconsistency, usually caused by conflicting virtualization software or a bad driver."
  - q: "Why did this start after updating to 24H2?"
    a: "Windows 11 24H2 tightened virtualization-based security and changed hypervisor behavior. Drivers and third-party virtualization tools (VMware, VirtualBox, some antivirus) that worked on 23H2 can conflict with the new hypervisor, triggering this crash."
  - q: "Do I need virtualization enabled to get this error?"
    a: "Usually yes — the hypervisor only loads when a feature needs it: Hyper-V, WSL2, Memory Integrity (Core Isolation), or Windows Subsystem for Android. If none of those are on and you still crash, check BIOS virtualization settings and firmware."
  - q: "Can I just disable Hyper-V to fix it?"
    a: "Sometimes, but it's a workaround, not a fix — and it breaks WSL2, Docker, and Memory Integrity. Better to update the conflicting driver or software so you can keep virtualization's security benefits. Disable it only as a diagnostic step."
---

`HYPERVISOR_ERROR` is a stop code most people never see — until they update to Windows 11 24H2 and it starts appearing out of nowhere. The hypervisor is the thin virtualization layer sitting between Windows and your hardware, powering Hyper-V, WSL2, Memory Integrity, and Android apps. When it crashes, everything above it goes down.

The 24H2 update made this more common because it changed how the hypervisor interacts with drivers and tightened virtualization-based security. The fix is usually about resolving a conflict, not reinstalling Windows.

## Why this happens

- **Third-party virtualization software conflicts**: VMware Workstation, VirtualBox, or Android emulators fighting Hyper-V for control of the CPU's virtualization extensions.
- **Outdated hypervisor-related drivers**: Storage, network, or chipset drivers that worked on 23H2 but violate 24H2's stricter hypervisor rules.
- **Memory Integrity (HVCI) vs. incompatible driver**: Core Isolation's Memory Integrity uses the hypervisor; an incompatible driver loaded alongside it can crash the hypervisor.
- **BIOS/firmware virtualization bugs**: Outdated BIOS with buggy VT-x/AMD-V or IOMMU handling, especially on laptops that got 24H2 before a firmware update.
- **Corrupted hypervisor binaries**: Damaged `hvix64.exe`/`hvax64.exe` or related system files from a bad update.
- **Antivirus kernel drivers**: Some third-party AV products install hypervisor-level drivers that conflict with 24H2's virtualization security.

## How to fix it

Work through these in order — start with software conflicts, then drivers and firmware.

### Fix 1: Update conflicting virtualization software

If you run VMware, VirtualBox, or an Android emulator, update it first — older versions are the classic 24H2 conflict.

1. Check what you have installed: **Settings** > **Apps** > **Installed apps**, and look for VMware, VirtualBox, BlueStacks, LDPlayer, or similar.
2. Update each to its latest version — vendors shipped 24H2-compatibility fixes, and running the newest build resolves most conflicts.
3. If you don't need a tool anymore, uninstall it and restart.
4. Test for a day of normal use. If crashes stop, you've found it — keep the software updated and don't run two hypervisors' VMs simultaneously.
5. For VirtualBox specifically, make sure you're on version 7.1 or later, which handles Hyper-V coexistence far better.

### Fix 2: Check Memory Integrity and incompatible drivers

Memory Integrity uses the hypervisor, and 24H2 flags incompatible drivers more aggressively.

1. Open **Windows Security** > **Device security** > **Core isolation details**.
2. Note whether **Memory integrity** is on. If Windows shows a list of incompatible drivers, that's a strong lead — update or remove those drivers.
3. As a diagnostic step, you can toggle Memory Integrity off and restart to see if crashes stop. If they do, the problem is a driver incompatible with HVCI — find and update it rather than leaving protection off permanently.
4. Re-enable Memory Integrity after updating the driver and confirm stability.
5. Microsoft documents Memory Integrity requirements on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Update BIOS/firmware

Hypervisor crashes are often rooted in firmware — the hypervisor talks directly to CPU virtualization features.

1. Find your exact model: press **Win + R**, type `msinfo32`, and note **System Model** and **BIOS Version/Date**.
2. Go to your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and check for a newer BIOS.
3. If one exists, download it, plug the laptop into AC power, close all apps, and run the updater. Don't interrupt it.
4. After the update, enter BIOS setup and verify virtualization is enabled: **Intel Virtualization Technology** / **VT-x** or **AMD-V**, plus **VT-d**/**AMD-Vi** (IOMMU) if present.
5. Boot and test. Firmware updates resolve a meaningful share of hypervisor crashes.

### Fix 4: Update chipset and storage drivers

The hypervisor depends on chipset, storage, and network drivers behaving correctly at a low level.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Update drivers under **IDE ATA/ATAPI controllers**, **Storage controllers**, **System devices** (chipset), and **Network adapters**.
3. Better yet, install the full chipset driver package from your laptop manufacturer's support page — Windows Update often misses these.
4. For Intel systems, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) catches chipset and management engine updates reliably.
5. Restart and verify with a few days of normal use including sleep/wake cycles.

### Fix 5: Repair system files and the hypervisor stack

A bad 24H2 upgrade can leave hypervisor components corrupted.

1. Open an elevated Command Prompt (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` first, then `sfc /scannow`.
3. If crashes persist, toggle the Hyper-V platform off and on to reinstall its components: open **Turn Windows features on or off** (**Win + R**, type `optionalfeatures`), uncheck **Hyper-V**, restart, then re-check it and restart again.
4. Also try `bcdedit /set hypervisorlaunchtype auto` from an elevated prompt to ensure the hypervisor is configured to launch correctly, then restart.

### Fix 6: Test with third-party antivirus removed

Some AV products install drivers that operate at hypervisor level and clash with 24H2.

1. If you run third-party antivirus, uninstall it completely (disabling isn't enough — its drivers still load).
2. Restart and let **Microsoft Defender** take over protection.
3. Test stability for a day or two. If crashes stop, check with the AV vendor for a 24H2-compatible version before reinstalling.
4. If you must keep the product, ensure it's the absolute latest version — vendors patched hypervisor conflicts through 2025.

### Fix 7: Reset virtualization features as a last resort

If nothing else works, rebuild the virtualization configuration cleanly.

1. Open **Turn Windows features on or off** (`optionalfeatures`).
2. Uncheck **Hyper-V**, **Virtual Machine Platform**, and **Windows Hypervisor Platform**. Restart.
3. Restart again, re-check the ones you need, and restart once more.
4. If you don't use WSL2, Docker, or VMs at all, you can leave them off — but also disable virtualization in BIOS only if you never plan to use these features, since Memory Integrity benefits from it.
5. As a final option, an in-place upgrade with [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) refreshes the hypervisor stack while keeping files and apps.

If your crashes mention a different stop code alongside virtualization features, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) and the [Driver Verifier IOManager violation fix](/articles/driver-verifier-iomanager-violation-blue-screen-error-fix/) cover adjacent hypervisor-adjacent crashes.

## Closing

HYPERVISOR_ERROR on 24H2 is almost always a conflict story: old virtualization software, an incompatible driver under Memory Integrity, or firmware that predates the update. Update the software, check Memory Integrity's incompatible-driver list, update the BIOS, and refresh chipset drivers — in that order. The hypervisor itself is rarely broken; something next to it usually is.
