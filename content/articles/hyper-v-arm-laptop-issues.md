---
title: "How to Fix Hyper-V Issues on ARM Laptops (Windows 11)"
slug: hyper-v-arm-laptop-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["hyper-v", "arm", "virtualization", "windows 11", "vm", "troubleshooting"]
description: "Hyper-V VMs failing to start or running slowly on your ARM laptop? Follow these step-by-step fixes for virtualization, ARM64 guests, and Hyper-V setup."
thumbnail: "/images/thumbs/hyper-v-arm-laptop-issues.webp"
faqs:
  - q: "Does Hyper-V work on Snapdragon ARM laptops?"
    a: >
      Yes — Hyper-V is fully supported on Windows 11 Pro and Enterprise for ARM64. The key difference from x86 is that ARM VMs must run ARM64 guest operating systems; you cannot virtualize x64 Windows or x64 Linux on these laptops.
  - q: "Why does my VM fail to start with a virtualization error?"
    a: >
      The most common cause is virtualization being disabled in firmware, or the hypervisor launch type being set to Off by a tweaking tool. Enable virtualization in BIOS/UEFI and confirm hypervisorlaunchtype is Auto with bcdedit.
  - q: "Can I run Windows 11 x64 inside Hyper-V on an ARM laptop?"
    a: >
      No — Hyper-V on ARM can only run ARM64 guest operating systems. For an x64 Windows guest you would need full CPU emulation, which Hyper-V does not provide. Use a Windows 11 ARM64 ISO for your guests.
  - q: "My ARM VM is very slow. How do I speed it up?"
    a: >
      Give the VM at least 4 GB of RAM and 4 virtual processors, store its virtual disk on the internal SSD, and make sure you installed an ARM64 guest OS — an emulated or mismatched guest will always crawl. Driver issues on the host can also starve VMs, so check that [Intel AI Boost drivers install cleanly](/articles/intel-ai-boost-driver-not-installing/) if you are on Intel hardware.
---

You created a virtual machine in Hyper-V on your Snapdragon laptop and it refuses to start — or it starts but runs so slowly it is unusable, or the Hyper-V Manager itself throws errors about the virtualization service. On Intel this was routine; on ARM the same clicks produce different failures.

Hyper-V on ARM64 is real Hyper-V, but the guest world is smaller: every VM must run an ARM64 operating system — Windows 11 ARM64, Ubuntu ARM64, Debian ARM64. There is no x64 guest support, no nesting an x64 world inside. Most failures come from that architecture mismatch, from firmware virtualization being off, or from the Hyper-V platform being incompletely enabled. Teams-heavy users sometimes notice virtualization-adjacent AI features misbehaving too — see [Copilot Teams meeting recap not working](/articles/copilot-teams-meeting-recap-not-working/) and [Paint Cocreator not working](/articles/paint-cocreator-not-working/) for the same "check the platform first" pattern applied to AI features.

This guide gives you six fixes in order: enable firmware virtualization and the Hyper-V platform, use ARM64 guest media, fix VM start failures, tune VM performance, repair the Hyper-V service, and resolve conflicts with other hypervisors. All commands run elevated.

## Why this happens

- **Virtualization disabled in firmware:** The Hyper-V hypervisor cannot load without it. VMs fail to start with virtualization errors, and the Hyper-V Manager may report the service as unavailable.
- **x64 guest OS on an ARM host:** Hyper-V on ARM cannot emulate x64. An x64 ISO will fail to boot or install — this is the single most common "VM won't start" cause on Snapdragon laptops.
- **Hyper-V platform incompletely enabled:** The Hyper-V Manager console can be installed without the underlying hypervisor platform, producing a manager that opens but cannot run anything.
- **Hypervisor launch type disabled:** Tweaking tools and some games set `hypervisorlaunchtype` to Off for marginal performance, silently breaking all Hyper-V functionality until reverted.
- **Under-provisioned VM resources:** Default VM settings (2 GB RAM, 2 vCPUs) starve modern ARM64 guests, especially Windows 11 ARM64 — the VM boots but crawls.
- **Conflicting third-party hypervisor:** VirtualBox, VMware Workstation, and some security products install drivers that conflict with Hyper-V's hypervisor on ARM.
- **Corrupted Hyper-V configuration:** Failed updates or interrupted VM operations can corrupt the Hyper-V service configuration, producing start failures with no clear error.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable firmware virtualization and the Hyper-V platform

Nothing works without the hypervisor. Verify the firmware switch and the Windows features together.

1. Open Task Manager (**Ctrl + Shift + Esc**), go to **Performance > CPU**, and confirm **Virtualization** reads **Enabled**.
2. If Disabled, reboot into BIOS/UEFI and enable virtualization, then save and exit.
3. Press **Windows key + R**, type `optionalfeatures`, press Enter, and check **Hyper-V** (both Management Tools and Platform), **Virtual Machine Platform**, and **Windows Hypervisor Platform**.
4. Click OK and restart — the hypervisor activates at boot.
5. After reboot, open an elevated PowerShell and run `Get-Service vmms` — the Hyper-V Virtual Machine Management service should show **Running**.

### Fix 2: Use ARM64 guest operating systems only

If your VM was built from an x64 ISO, no platform fix will save it. Rebuild with ARM64 media.

1. Delete or discard the non-booting VM — an x64 guest on ARM Hyper-V will never work, regardless of settings.
2. Download a **Windows 11 ARM64** ISO (from Microsoft's download page via a registered device) or an **Ubuntu/Debian ARM64** ISO for Linux guests.
3. In Hyper-V Manager, create a **Generation 2** VM and attach the ARM64 ISO.
4. During guest setup, confirm the installer boots — an ARM64 ISO on ARM Hyper-V boots normally; an x64 ISO fails immediately at boot.
5. After installation, install the guest integration services (automatic for Windows ARM64 guests) to enable proper mouse, display, and networking.

### Fix 3: Fix VM start failures and hypervisor launch type

The platform is enabled and the guest is ARM64, but the VM still will not start — check the hypervisor launch configuration.

1. In an elevated PowerShell, run `bcdedit` and find `hypervisorlaunchtype` — it must read **Auto**.
2. If it reads **Off**, run `bcdedit /set hypervisorlaunchtype auto` and reboot.
3. Check **Event Viewer > Applications and Services Logs > Microsoft > Windows > Hyper-V-VMMS** for the specific start failure and its error code.
4. If the error mentions saved state corruption, right-click the VM in Hyper-V Manager and choose **Delete Saved State**, then start fresh.
5. For error **0x80070057** or similar, re-run `DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V-All` from an elevated prompt and reboot.

### Fix 4: Tune the VM for usable performance

An ARM64 VM that boots but crawls is almost always under-provisioned. Give it real resources.

1. Shut down the VM, right-click it in Hyper-V Manager, and open **Settings**.
2. Under **Memory**, assign at least **4096 MB** (8192 MB for a Windows 11 ARM64 guest used as a daily driver).
3. Under **Processor**, assign at least **4 virtual processors** — 2 vCPUs starves modern guests.
4. Under **Hard Drive**, confirm the VHDX lives on the internal SSD, not a slow external drive or SD card.
5. Start the VM and check Task Manager inside the guest — CPU should idle low; sustained 100% at idle means the guest OS is wrong-architecture or its drivers failed.

### Fix 5: Repair the Hyper-V service and configuration

When the Hyper-V Manager itself errors or the vmms service will not stay running, the service configuration needs repair.

1. In an elevated PowerShell, run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
2. Restart the Hyper-V services: `Restart-Service vmms`, `Restart-Service vmcompute` — both should return to Running without errors.
3. If vmms fails to start, check that no third-party antivirus is blocking hypervisor drivers, and temporarily disable its virtualization features to test.
4. Re-register the Hyper-V platform: uncheck Hyper-V in `optionalfeatures`, reboot, re-check it, reboot again.
5. After the re-enable cycle, recreate a small test VM with an ARM64 ISO to confirm the platform is healthy before rebuilding production VMs.

### Fix 6: Resolve conflicts with other virtualization software

Two hypervisors cannot own the CPU. If another product is installed, it may be blocking Hyper-V.

1. Uninstall VirtualBox, VMware Workstation, or any other desktop hypervisor you do not actively need — their kernel drivers can conflict on ARM.
2. Check security software for **hardware-assisted virtualization** or **hypervisor-protected** features and disable them temporarily to test.
3. Some Android emulators install their own hypervisor drivers — update them to versions that cooperate with Hyper-V, or uninstall them.
4. After removing the conflicting product, reboot and verify `hypervisorlaunchtype` is still **Auto**, then retest your Hyper-V VM.
5. If you must keep the other product, check its documentation for a Hyper-V compatibility mode — many now run on top of the Windows hypervisor instead of fighting it.

## Closing

Hyper-V on ARM laptops is production-capable with one non-negotiable rule: ARM64 guests only. Get firmware virtualization on, the platform fully enabled, and the guest architecture right, and the rest is standard VM administration — memory, vCPUs, fast storage. The honest limit is the guest ecosystem: if the OS or appliance you need exists only for x64, no Hyper-V setting on a Snapdragon laptop will run it. For platform-level questions, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the ARM64 Hyper-V requirements as they evolve.
