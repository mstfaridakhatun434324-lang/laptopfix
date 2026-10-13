---
title: "How to Fix the HYPERVISOR_ERROR Blue Screen on Windows 10"
slug: how-to-fix-hypervisor-error-bsod-on-windows-10
date: 2026-10-02
categories: ["windows-errors"]
tags: ["blue screen", "hypervisor error", "windows 10"]
description: "HYPERVISOR_ERROR blue screen on Windows 10? It's usually a virtualization or driver conflict. Here's how to fix it step by step, with and without Hyper-V."
thumbnail: "/images/thumbs/how-to-fix-hypervisor-error-bsod-on-windows-10.webp"
faqs:
  - q: "What is HYPERVISOR_ERROR on Windows 10?"
    a: "HYPERVISOR_ERROR means Windows' hypervisor — the layer that manages virtualization — crashed. It appears on machines running Hyper-V, virtual machines, Android emulators, or Windows Sandbox, but also on systems where virtualization features conflict with drivers. It's rarely a sign of failing hardware."
  - q: "Can outdated drivers cause HYPERVISOR_ERROR?"
    a: "Yes, frequently. Storage, network, and chipset drivers that aren't virtualization-aware can crash the hypervisor. Updating drivers from your laptop maker's support site is one of the most effective fixes, especially after a Windows feature update changed the hypervisor underneath them."
  - q: "Do I need Hyper-V enabled to get this error?"
    a: "No. Windows 10 enables hypervisor-backed features silently — Memory Integrity (HVCI), Virtualization-Based Security, and Credential Guard all use the hypervisor without Hyper-V being visibly on. That's why the error can appear on machines where you never knowingly enabled virtualization."
  - q: "Will disabling virtualization in BIOS fix it?"
    a: "It can stop the crashes, but it's a workaround, not a fix — you lose Hyper-V, WSL2, and Memory Integrity. Better to update drivers and repair system files first, and only disable virtualization temporarily for testing."
---
HYPERVISOR_ERROR is one of the more confusing blue screens because it mentions virtualization — yet it strikes plenty of laptops where the owner never installed Hyper-V or a virtual machine. The hypervisor runs quietly underneath several Windows 10 security features, so a driver conflict down there surfaces as this exact stop code.

The fix strategy is straightforward: update the drivers that interact with virtualization, repair the hypervisor's system files, and check the virtualization features themselves. Work top to bottom. If you're on Windows 11 instead, see our [HYPERVISOR_ERROR guide for Windows 11](/articles/how-to-fix-hypervisor-error-bsod-on-windows-11/) — the steps differ slightly.

## Why this happens

- **Outdated chipset, storage, or network drivers:** Drivers that predate Windows 10's virtualization features can issue calls the hypervisor rejects.
- **Corrupted hypervisor system files:** Failed updates can damage the files the hypervisor depends on at boot.
- **Conflicting third-party virtualization:** An old VMware, VirtualBox, or Android emulator install fighting Windows' own hypervisor for control of VT-x/AMD-V.
- **Memory Integrity (HVCI) conflicts:** The Core Isolation feature uses the hypervisor; an incompatible driver loaded under it can crash the whole layer.
- **BIOS virtualization settings mismatch:** VT-x/AMD-V enabled while Hyper-V is half-configured (or vice versa) creates an inconsistent state.
- **Overclocking or aggressive power settings:** Unstable CPU states can corrupt hypervisor memory regions, though this is rarer on laptops.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Update chipset, storage, and network drivers

These are the drivers that talk to the hypervisor most directly.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Expand **System devices** and update the chipset entries; expand **Network adapters** and **IDE ATA/ATAPI controllers** and do the same via **Update driver** > **Search automatically for drivers**.
3. For the best results, get the tested driver pack from your maker: [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
4. Intel users should also run the Intel Driver & Support Assistant for chipset and network drivers.
5. Restart and watch for stability over a few hours of normal use.

### Fix 2: Repair system files with SFC and DISM

If the crashes began after a Windows update, the hypervisor's own files may be damaged.

1. Open an **administrator Command Prompt**.
2. Run `sfc /scannow` and wait for completion.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. These two commands fix the majority of update-related hypervisor corruption.

### Fix 3: Check Memory Integrity and Core Isolation settings

Memory Integrity runs on the hypervisor — an incompatible driver under it is a classic trigger.

1. Open **Settings** > **Privacy & Security** > **Windows Security** > **Device security**.
2. Click **Core isolation details**.
3. Note the state of **Memory integrity**. If it's on and you crash, try turning it **Off** temporarily as a test.
4. If crashes stop with it off, check the **incompatible drivers** list Windows shows — update or remove those specific drivers, then re-enable Memory Integrity.
5. Leaving it off permanently weakens security, so treat this as diagnosis, not the final fix.

### Fix 4: Disable Hyper-V if you don't use it

If nothing on your machine needs virtualization, removing Hyper-V eliminates the crashing layer entirely.

1. Open **Control Panel** > **Programs** > **Turn Windows features on or off**.
2. Uncheck **Hyper-V**, **Virtual Machine Platform**, and **Windows Hypervisor Platform**.
3. Click **OK** and restart when prompted.
4. If you later need WSL2 or virtual machines, re-enable these — but only after confirming the system is stable without them.

### Fix 5: Turn off the hypervisor from the command line

A stronger version of Fix 4 for cases where the feature toggles don't fully stop hypervisor loading.

1. Open an **administrator Command Prompt**.
2. Run `bcdedit /set hypervisorlaunchtype off`.
3. Restart. Windows will boot without launching the hypervisor at all.
4. To reverse it later, run `bcdedit /set hypervisorlaunchtype auto` and restart.
5. Note: this disables Memory Integrity, WSL2, and Hyper-V — use it as a diagnostic step or a temporary workaround while you update drivers.

### Fix 6: Remove or update third-party virtualization software

Old emulator and VM software is a frequent hidden cause.

1. Open **Settings** > **Apps** > **Installed apps** and look for VirtualBox, VMware, BlueStacks, Nox, LDPlayer, or similar.
2. Update them to the latest version — or uninstall them entirely if you don't use them.
3. After uninstalling, restart and check stability before reinstalling anything.
4. If you need an Android emulator, reinstall the newest version only after the system is stable; modern versions cooperate with Hyper-V instead of fighting it.

### Fix 7: Verify BIOS virtualization settings are consistent

A half-enabled virtualization setup confuses the hypervisor at boot.

1. Enter firmware setup (**F2**/**Del** during boot).
2. Find virtualization options — **Intel VT-x**, **Intel Virtualization Technology**, **AMD-V**, or **SVM Mode** — under **Advanced** or **CPU Configuration**.
3. If you use Hyper-V/WSL2, ensure it's **Enabled**. If you disabled all virtualization features in Fix 4/5, you may set it to **Disabled** for consistency.
4. Also check **VT-d** (IOMMU) — toggling it to match your setup resolves crashes on some machines.
5. Save and exit, then test.

## Closing

HYPERVISOR_ERROR sounds exotic, but the fix is refreshingly ordinary: update your chipset, storage, and network drivers, repair system files, and sort out which virtualization features you actually need. Most Windows 10 laptops are fixed by Fix 1 and Fix 2 alone. Resist the urge to permanently disable virtualization as your first move — features like Memory Integrity exist for a reason. Get the drivers right, and you can keep both stability and security. Document which driver version works — it saves hours the next time an update shakes things up. If crashes persist after all seven fixes, read the minidump to identify the specific driver, as described in our [dump file reading guide](/articles/how-to-read-dump-files-with-windbg-on-windows-11/).
