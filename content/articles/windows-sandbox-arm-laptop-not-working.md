---
title: "How to Fix Windows Sandbox Not Working on ARM Laptops"
slug: windows-sandbox-arm-laptop-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["windows sandbox", "arm", "virtualization", "windows 11", "security", "troubleshooting"]
description: "Windows Sandbox won't start or crashes on your ARM laptop? Follow these step-by-step fixes for virtualization, feature enablement, and Hyper-V conflicts."
thumbnail: "/images/thumbs/windows-sandbox-arm-laptop-not-working.webp"
faqs:
  - q: "Does Windows Sandbox work on Snapdragon ARM laptops?"
    a: >
      Yes, Windows Sandbox is supported on Windows 11 Pro and Enterprise for ARM64. It is not available on Windows 11 Home at all — that edition lacks the feature regardless of CPU — so check your edition first if the feature is missing entirely.
  - q: "Why does Sandbox fail with error 0x80070057?"
    a: >
      That error usually points to the virtualization platform being incomplete — virtualization disabled in firmware, the Virtual Machine Platform feature missing, or a conflicting hypervisor. Enable virtualization in BIOS/UEFI and turn on the required Windows features.
  - q: "Windows Sandbox opens then immediately closes. What is wrong?"
    a: >
      Instant-close behavior is often caused by corrupted Sandbox components, insufficient memory, or a third-party security product interfering with the hypervisor. Repair the feature with DISM, free up RAM, and temporarily disable third-party antivirus to test.
  - q: "Can I use Windows Sandbox while Hyper-V virtual machines are running?"
    a: >
      Yes — Sandbox and Hyper-V VMs coexist on the same hypervisor. Problems arise only when a third-party hypervisor or a nested-virtualization setup conflicts with Hyper-V. If you need to disable the NPU while debugging virtualization, see [how to disable the NPU in Device Manager](/articles/how-to-disable-npu-device-manager/).
---

You need to test a suspicious download, so you launch Windows Sandbox — and get an error code, a hang at the splash screen, or a Sandbox window that opens and vanishes in two seconds. On your old Intel laptop it just worked. On this ARM machine it feels like the feature was never really finished.

Windows Sandbox is a lightweight, disposable Hyper-V-based desktop for running untrusted software safely. On ARM64 it exists, but with tighter prerequisites: Windows 11 Pro or Enterprise (Home is excluded entirely), virtualization enabled in firmware, the right Windows features switched on, and enough free memory. Most failures are one of three things: the edition does not include Sandbox, the virtualization platform is incomplete, or something is fighting the hypervisor. The same firmware-virtualization gate also blocks other features — [dynamic lighting not working on Windows 11](/articles/dynamic-lighting-not-working-windows-11/) and [Photos restyle image issues](/articles/photos-restyle-image-missing/) are unrelated features, but their fixes share the same "check the platform first" discipline.

This guide gives you six fixes in order: confirm edition and firmware virtualization, enable the required Windows features, repair the virtualization platform, resolve hypervisor conflicts, address memory and resource problems, and reset the Sandbox components. Work from an elevated terminal throughout.

## Why this happens

- **Windows 11 Home edition:** Sandbox is a Pro/Enterprise feature. On Home it simply does not exist — no feature toggle, no error, just absence.
- **Virtualization disabled in firmware:** Like all Hyper-V-based features, Sandbox needs firmware-level virtualization. Without it, enabling the feature fails or launches crash immediately.
- **Missing Windows features:** Sandbox depends on the Virtual Machine Platform and Hyper-V hypervisor components. A clean install or a debloated image may lack them.
- **Third-party hypervisor conflict:** Some third-party virtualization and security products install their own hypervisor or block Hyper-V, which breaks Sandbox at launch.
- **Insufficient free memory:** Sandbox needs several hundred MB of free RAM plus room for its dynamic memory. A laptop with 90% memory in use can fail to start the Sandbox VM.
- **Corrupted Sandbox components:** Failed Windows updates or interrupted feature enablement can leave the Sandbox binaries half-installed — the feature shows as enabled but cannot launch.
- **Nested virtualization or VBS policy:** Certain enterprise virtualization-based security policies and nested setups on ARM can prevent the Sandbox VM from initializing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your edition and firmware virtualization

Sandbox has hard prerequisites. Check them before changing anything — half of all "not working" reports end at this step.

1. Open **Settings > System > About** and check the **Edition** line — you need **Windows 11 Pro** or **Enterprise**. If it says Home, Sandbox is unavailable; upgrading the edition is the only path.
2. Open Task Manager (**Ctrl + Shift + Esc**), go to **Performance > CPU**, and confirm **Virtualization** reads **Enabled**.
3. If Disabled, reboot into BIOS/UEFI (**F2** or **Del** at boot) and enable virtualization under the CPU or Advanced settings, then save and exit.
4. Back in Windows, open an elevated PowerShell and run `systeminfo` — every line under **Hyper-V Requirements** should say **Yes**.
5. Only proceed when edition is Pro/Enterprise and virtualization is Enabled.

### Fix 2: Enable the Windows Sandbox and platform features

Even on Pro, the features may simply be off — especially on fresh installs or OEM images that trimmed optional components.

1. Press **Windows key + R**, type `optionalfeatures`, and press Enter.
2. Check **Windows Sandbox**, **Virtual Machine Platform**, and **Windows Hypervisor Platform**, then click **OK**.
3. Let Windows apply the changes and **restart** when prompted — the hypervisor only activates at boot.
4. After rebooting, search the Start menu for **Windows Sandbox** to confirm the app entry now exists.
5. Launch it once and note what happens — a first launch can take a minute while components initialize; only treat a clear error as a failure.

### Fix 3: Repair the virtualization platform with DISM

If the features show as enabled but Sandbox still fails, the underlying platform may be damaged. Repair it from the command line.

1. Open an elevated PowerShell (**Windows key + X > Terminal (Admin)**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to complete — this repairs the component store.
3. Then run `sfc /scannow` to fix corrupted system files that Sandbox depends on.
4. Re-run the feature enablement: `DISM /Online /Enable-Feature /All /FeatureName:Containers-DisposableClientVM` and restart.
5. Launch Windows Sandbox again and record any new error code — changed errors mean the repair moved you forward.

### Fix 4: Remove hypervisor conflicts

Third-party software that installs its own hypervisor or blocks Hyper-V will break Sandbox silently. Identify and neutralize the conflict.

1. Uninstall or fully exit any third-party virtualization products you do not need (some install kernel drivers that persist after closing the app).
2. Check your antivirus: temporarily disable any **hardware virtualization** or **hypervisor protection** feature it offers, then retest Sandbox.
3. In an elevated PowerShell, run `bcdedit` and look for `hypervisorlaunchtype` — it should be **Auto**. If it says **Off**, run `bcdedit /set hypervisorlaunchtype auto` and reboot.
4. Some "game booster" and system-tweak tools disable the hypervisor for marginal performance gains — check their settings and revert.
5. After each change, reboot and retry Sandbox; hypervisor state only changes at boot time.

### Fix 5: Free memory and check resource pressure

Sandbox's VM needs real free RAM. On an 8 GB laptop with a heavy workload, there may simply not be enough.

1. Open Task Manager and check memory usage on the **Performance** tab — if you are above 85%, close heavy apps before launching Sandbox.
2. Disable unnecessary startup apps under **Task Manager > Startup apps** to free baseline memory.
3. Make sure at least 4 GB of disk space is free on the system drive — Sandbox stages temporary files during launch.
4. If you run Sandbox with networking-heavy or large apps inside, launch it clean first (no startup scripts) to isolate resource issues from app issues.
5. On 8 GB machines, accept the honest limit: Sandbox plus a full desktop workload may simply exceed available RAM — close what you can.

### Fix 6: Reset Sandbox components fully

When the feature is enabled, the platform is healthy, and it still will not launch, a full reset of the Sandbox components is the last resort.

1. In `optionalfeatures`, **uncheck** Windows Sandbox, click OK, and restart.
2. After reboot, run `DISM /Online /Cleanup-Image /RestoreHealth` once more to clear any damaged state.
3. Re-check Windows Sandbox in `optionalfeatures`, click OK, and restart again.
4. Launch Sandbox and let the first initialization complete without interruption — do not force-close it.
5. If it still fails, check **Event Viewer > Applications and Services Logs > Microsoft > Windows > Containers** for the specific failure, and search that error code on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Windows Sandbox on ARM is a real, working feature — but only on Pro/Enterprise, only with firmware virtualization on, and only with the platform features properly enabled. Work the prerequisites in order and the fix usually reveals itself early. The honest boundaries: Home edition simply does not include it, and 8 GB laptops may struggle to host it alongside a full workload. For anything the Sandbox log cannot explain, the Containers event log plus Microsoft's support documentation will get you the rest of the way.
