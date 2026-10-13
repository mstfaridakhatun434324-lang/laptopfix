---
title: "How to Fix the HYPERVISOR_ERROR Blue Screen on Windows 11"
slug: how-to-fix-hypervisor-error-bsod-on-windows-11
date: 2026-09-01
categories: ["windows-errors"]
tags: ["blue screen", "hypervisor error", "windows 11"]
description: "HYPERVISOR_ERROR blue screen on Windows 11? It's a virtualization-layer crash, usually driver-related. Here's the step-by-step fix for laptops."
thumbnail: "/images/thumbs/how-to-fix-hypervisor-error-bsod-on-windows-11.webp"
faqs:
  - q: "What is HYPERVISOR_ERROR on Windows 11?"
    a: "It means the hypervisor — the virtualization layer under Windows 11 — crashed. Windows 11 uses the hypervisor for Memory Integrity, Virtualization-Based Security, and WSL2, so the error can appear even if you never installed Hyper-V. Faulty drivers interacting with virtualization are the most common trigger."
  - q: "How is this different from the Windows 10 version?"
    a: "The causes are nearly identical, but Windows 11 enables hypervisor-backed security (like Memory Integrity and VBS) by default on more machines, so the error appears more often without any virtualization software installed. See our Windows 10 guide if you're on the older OS."
  - q: "Can RAM problems cause HYPERVISOR_ERROR?"
    a: "Occasionally. The hypervisor manages memory regions, so faulty RAM can corrupt them. But drivers are far more likely — test RAM with Windows Memory Diagnostic (mdsched.exe) to rule it out definitively, then focus on chipset, storage, and network drivers."
  - q: "Should I just disable virtualization to stop the crashes?"
    a: "As a temporary test, yes; as a permanent fix, preferably not. Disabling the hypervisor also disables Memory Integrity and WSL2, weakening security. The better path is updating the conflicting drivers so you can keep virtualization-based protection enabled."
---
HYPERVISOR_ERROR on Windows 11 is the hypervisor crashing underneath the operating system — and since Windows 11 leans on the hypervisor for security features like Memory Integrity and Virtualization-Based Security, this error shows up even on laptops where nobody ever touched Hyper-V. The trigger is almost always a driver that doesn't play well with virtualization.

Work through these in order, from driver updates to hypervisor configuration. If you're on Windows 10, use our [HYPERVISOR_ERROR guide for Windows 10](/articles/how-to-fix-hypervisor-error-bsod-on-windows-10/) instead — the menus differ slightly.

## Why this happens

- **Incompatible chipset/storage/network drivers:** Old drivers issuing calls the hypervisor rejects.
- **Memory Integrity conflicts:** An incompatible driver loaded under Core Isolation's Memory Integrity crashes the hypervisor layer.
- **Corrupted hypervisor files:** Failed updates damaging boot-critical virtualization components.
- **Third-party virtualization software:** Outdated emulators or VM tools fighting Windows' hypervisor for CPU virtualization extensions.
- **BIOS virtualization misconfiguration:** VT-x/AMD-V settings inconsistent with Windows' expectations.
- **Faulty RAM:** Corrupting hypervisor-managed memory regions (less common but real).
- **Overzealous "debloating":** Scripts that rip out virtualization components can leave the hypervisor half-configured.
- **Stale hypervisor launch configuration:** A corrupted BCD hypervisor entry can crash the hypervisor before Windows even finishes booting.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Update chipset, storage, and network drivers

The drivers that interact with the hypervisor most — update them first.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Update **System devices** (chipset), **IDE ATA/ATAPI controllers** (storage), and **Network adapters** via **Update driver** > **Search automatically for drivers**.
3. Install the manufacturer-tested pack from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
4. Run the Intel Driver & Support Assistant for Intel chipset, Wi-Fi, and Bluetooth drivers.
5. Restart and test for a full day of normal use before declaring victory.

### Fix 2: Repair system files

Fixes corrupted hypervisor and boot components from failed updates.

1. Open an **administrator Command Prompt** (or Terminal as admin).
2. Run `sfc /scannow` and wait.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. If crashes began after a Windows update, this pair resolves most cases.

### Fix 3: Test with Memory Integrity toggled

Memory Integrity runs on the hypervisor — it's both a common trigger and a useful diagnostic.

1. Open **Settings** > **Privacy & Security** > **Windows Security** > **Device security** > **Core isolation details**.
2. If **Memory integrity** is on, turn it **Off** and restart as a test.
3. Crashes stop? Check the **incompatible drivers** list Windows displays — update or remove those exact drivers.
4. Then turn Memory Integrity back **On** and restart. Keeping it on matters for security; the goal is compatible drivers, not a disabled feature.

### Fix 4: Update or remove third-party virtualization software

Old emulators and VM tools are frequent hidden causes on Windows 11.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Update VirtualBox, VMware Workstation, BlueStacks, or similar to the latest version — or uninstall if unused.
3. Restart and verify stability before reinstalling anything.
4. Modern versions are Hyper-V-compatible; ancient ones try to seize VT-x exclusively and crash the hypervisor.

### Fix 5: Check Windows features configuration

Ensure the virtualization stack is consistently enabled or disabled — not half-and-half.

1. Open **Control Panel** > **Programs** > **Turn Windows features on or off**.
2. If you use WSL2 or VMs: ensure **Virtual Machine Platform** and **Windows Hypervisor Platform** are checked.
3. If you use nothing virtualization-related: uncheck **Hyper-V**, **Virtual Machine Platform**, and **Windows Hypervisor Platform**, click OK, restart.
4. Mixed states (platform on, Hyper-V off, etc.) are fine as long as they're intentional — the problem is leftover partial configurations from debloat scripts.

### Fix 6: Test RAM with Windows Memory Diagnostic

Rules out the hardware cause definitively.

1. Press **Win + R**, type `mdsched.exe`, press Enter.
2. Choose **Restart now and check for problems** (use Extended mode via F1 for thoroughness).
3. Check results in **Event Viewer** > **Windows Logs** > **System** for **MemoryDiagnostics-Results**.
4. Errors → reseat or replace RAM. Clean → continue.

### Fix 7: Verify BIOS virtualization settings

A consistent firmware configuration prevents hypervisor boot conflicts.

1. Enter firmware setup (**F2**/**Del**/**Esc** at boot, varies by brand).
2. Under **Advanced** or **CPU Configuration**, confirm **Intel Virtualization Technology** (VT-x) or **AMD SVM Mode** is **Enabled** if you use any virtualization features.
3. Check **VT-d**/**AMD-Vi** (IOMMU) — enable it if you use Hyper-V/WSL2; toggling it resolves crashes on some laptops either way.
4. Save and exit, then test.

### Fix 8: Disable hypervisor auto-launch as a diagnostic

If nothing else helps, stop the hypervisor from launching to confirm it's the crashing layer.

1. Open an **administrator Command Prompt**.
2. Run `bcdedit /set hypervisorlaunchtype off` and restart.
3. If crashes stop entirely, the hypervisor layer is confirmed as the fault domain — focus remaining effort on its drivers (chipset, storage, network) rather than general troubleshooting.
4. To restore, run `bcdedit /set hypervisorlaunchtype auto` and restart.
5. Remember this disables Memory Integrity and WSL2, so treat it as diagnosis, then fix the real driver problem and re-enable.

## Closing

HYPERVISOR_ERROR on Windows 11 is a driver problem wearing a virtualization costume in the vast majority of cases. Update the chipset, storage, and network drivers from your laptop maker's site, repair system files, and use Memory Integrity's incompatible-driver list as your detective — it literally names the offenders. Keep virtualization enabled if you can; the security features built on it are worth the troubleshooting effort. And if you've worked through all seven fixes, read the minidump — our [dump-reading guide](/articles/how-to-read-dump-files-with-windbg-on-windows-11/) shows how — because the faulting driver name ends the guessing game for good. Document what fixed it — the next hypervisor crash will be much shorter. Stability and virtualization can coexist; it just takes the right drivers.
