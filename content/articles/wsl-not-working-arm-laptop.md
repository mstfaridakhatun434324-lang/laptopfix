---
title: "How to Fix WSL Not Working on Your ARM Laptop"
slug: wsl-not-working-arm-laptop
date: 2026-10-20
categories: ["ai-pc"]
tags: ["wsl", "windows subsystem for linux", "arm laptop", "troubleshooting", "ai pc", "snapdragon x"]
description: "WSL won't start on your Snapdragon X laptop? Find out why Ubuntu fails on ARM Windows 11, then fix virtualization, kernel, and distro errors step by step."
thumbnail: "/images/thumbs/wsl-not-working-arm-laptop.webp"
faqs:
  - q: "Does WSL actually work on Snapdragon X laptops?"
    a: "Yes. WSL2 runs natively on ARM64 Windows 11, and Microsoft ships an ARM64 Linux kernel for it. Most failures come from disabled virtualization, missing Windows features, or installing an x64 distro instead of the ARM64 one — all fixable below."
  - q: "Which Linux distro should I install on ARM Windows?"
    a: "Pick one with an official ARM64 build. Ubuntu, Debian, and Kali all publish ARM64 versions, and `wsl --install -d Ubuntu` fetches the right one automatically. Avoid importing x64 rootfs tarballs — they will not boot on an ARM kernel."
  - q: "Why do I get error 0x80370102 when launching WSL?"
    a: "That code means WSL2 cannot reach hardware virtualization. It is usually disabled in UEFI firmware, blocked by Memory integrity, or broken by a stale Hyper-V configuration. Fix 4 below walks through each cause in order."
  - q: "Can I run x86 Linux programs inside WSL on ARM?"
    a: "Mostly no. WSL on ARM runs an ARM64 kernel, so x86 binaries need slow, flaky emulation via box64 or qemu-user. Install the ARM64 builds of your tools instead — Node, Python, Go, Rust, and Docker all ship them."
---

You bought a Snapdragon X laptop for its battery life and AI muscle, typed `wsl --install`, and hit a wall — an error code, a hung install, or a distro that refuses to launch. It is a frustrating first impression, because WSL2 genuinely runs on ARM64 Windows 11: Microsoft ships an ARM64 Linux kernel, and Ubuntu and Debian both publish ARM64 builds. The feature is not broken on your machine; it is misconfigured at one of several layers.

The confusion is understandable. WSL2 on ARM looks identical to WSL2 on Intel from the command line, so the same commands fail cryptically when the virtualization stack underneath is not ready. Students hit this constantly — WSL is a big reason people choose an [AI laptop for college work](/articles/ai-laptop-for-college-students-guide/) — and the error messages rarely say what is actually wrong.

Work through the checks below in order: firmware, Windows features, the WSL kernel, the 0x80370102 error, and distro architecture. If WSL is a stepping stone to containers, our [Docker Desktop on ARM Windows guide](/articles/docker-desktop-arm-windows/) covers the container side of the same stack.

## Why this happens

- **Virtualization disabled in firmware:** WSL2 is a lightweight virtual machine, and some Snapdragon laptops ship with the UEFI virtualization toggle off — every launch fails until it is enabled.
- **Missing Windows features:** WSL2 needs "Windows Subsystem for Linux" and "Virtual Machine Platform." Fresh installs and debloated images often lack one or both.
- **Stale or corrupt WSL kernel:** The ARM64 kernel ships separately from Windows Update; a bad one causes hangs and "operation timed out" errors on launch.
- **x64 distro on an ARM64 kernel:** Manually importing an x64 rootfs is a classic ARM mistake — the ARM64 kernel cannot execute it, so the distro dies silently.
- **Hypervisor conflicts (0x80370102):** Memory integrity or stale Hyper-V settings can block WSL2 from reaching the hardware, producing the most common error code on ARM laptops.
- **Corrupted distro registration:** Interrupted installs leave half-registered distros — the same class of update damage that makes an [NPU disappear after a Windows update](/articles/npu-disappeared-after-windows-update/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable virtualization in UEFI firmware

WSL2 cannot run without hardware virtualization, and many Snapdragon X laptops ship with the firmware toggle off or reset by a BIOS update. It is the single most common root cause on ARM, yet people skip it because everything else looks fine. The toggle hides under different names — Dell, HP, and Lenovo each label it differently — but it is always near the virtualization or security settings.

1. Shut down fully, power on, and press the firmware key (usually F2, F10, or Del) to enter UEFI setup.
2. Find "Virtualization Technology" or similar under Advanced or Security and set it to Enabled.
3. Save, exit, and boot back into Windows.
4. In Task Manager's Performance tab, confirm the CPU shows "Virtualization: Enabled."

### Fix 2: Turn on the WSL and Virtual Machine Platform features

Even with firmware virtualization on, WSL2 needs two Windows optional features that are not always present after a reset or a manufacturer's custom image. Without the Virtual Machine Platform in particular, `wsl --install` appears to succeed and then the distro fails at first launch. The GUI toggle is reliable, and DISM covers cases where the dialog will not open.

1. Open "Turn Windows features on or off" from the Start menu.
2. Check "Windows Subsystem for Linux" and "Virtual Machine Platform," then click OK.
3. If the dialog will not open, enable both features with DISM in an elevated PowerShell instead.
4. Restart, then run `wsl --status` to confirm WSL2 is the default version.

### Fix 3: Update WSL and its ARM64 kernel package

Microsoft updates WSL independently of Windows Update, and the ARM64 kernel can go stale or corrupt on its own. Symptoms include WSL hanging on launch, "operation timed out" messages, and distros that worked yesterday but will not start today. The `wsl --update` command pulls the latest kernel and components in one step. If the updater itself is broken, the Microsoft Store build of WSL cleanly replaces the inbox installation.

1. Run `wsl --update` in PowerShell or Terminal and wait for it to finish.
2. Run `wsl --shutdown` to stop any stuck instances.
3. Launch your distro with `wsl -d Ubuntu` (or your distro's name).
4. If the update fails, install "Windows Subsystem for Linux" from the Microsoft Store and reboot.

### Fix 4: Resolve error 0x80370102 (virtualization unreachable)

Error 0x80370102 is the signature WSL failure on ARM, and it almost never means what it says — the "required feature" is usually installed but blocked from reaching the hypervisor. On Snapdragon machines the usual suspects are Memory integrity fighting the WSL virtual machine and a stale Hyper-V launch configuration. Work through these in order, testing WSL after each change so you know which one was responsible. Once the kernel is current, Memory integrity and WSL coexist without issues.

1. In Windows Security, go to Device security, then Core isolation, and toggle Memory integrity off temporarily.
2. In an elevated PowerShell, run `bcdedit /set hypervisorlaunchtype auto`, then restart.
3. Run `wsl --update` followed by `wsl --shutdown` to rule out a mismatched kernel.
4. Re-enable Memory integrity afterward if your policy requires it, then retest WSL.

### Fix 5: Install a true ARM64 distro, not an x64 image

This mistake is invisible until you know to look for it: a manually imported x64 rootfs will never boot on an ARM64 kernel, and no error explains the architecture mismatch clearly. The Microsoft Store and `wsl --install -d` detect your architecture automatically and fetch ARM64 builds, which is why the official path is the safest. After switching, package managers work natively at full speed instead of failing with "exec format error." Reinstall your dev tools afterward so everything is an ARM64 binary.

1. Back up anything valuable, then remove the broken distro with `wsl --unregister <DistroName>`.
2. Install fresh with `wsl --install -d Ubuntu` and complete the first-run setup.
3. Inside the distro, run `uname -m` and confirm it prints `aarch64`.
4. Reinstall your tools from the package manager; see the [Windows support hub](https://support.microsoft.com/en-us/windows) if Store installs keep failing.

## Closing

WSL on a Snapdragon X laptop is fully capable once the stack underneath is correct — firmware virtualization on, both Windows features enabled, a current ARM64 kernel, and a genuine ARM64 distro. Nine times out of ten the failure is one of those four, not defective hardware or a missing ARM feature. Work the fixes in order, verify with `wsl --status` and `uname -m`, and you will have a native-speed Linux environment that sips battery instead of draining it.
