---
title: "How to Fix WSL Not Working on Snapdragon Laptops (Windows on ARM)"
slug: wsl-not-working-snapdragon-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["wsl", "snapdragon", "windows on arm", "linux", "developer", "troubleshooting"]
description: "WSL failing to install or launch on your Snapdragon X laptop? Follow these step-by-step fixes for virtualization, kernel updates, and ARM Linux distros."
thumbnail: "/images/thumbs/wsl-not-working-snapdragon-laptop.webp"
faqs:
  - q: "Does WSL work on Snapdragon X laptops?"
    a: >
      Yes — WSL2 works on Windows 11 ARM, including Snapdragon X Elite and Plus laptops. You must install an ARM64 Linux distribution (such as Ubuntu ARM) from the Microsoft Store; x86-only distros and containers will not run without emulation workarounds.
  - q: "Why does wsl --install fail with an error on my ARM laptop?"
    a: >
      The usual causes are virtualization being disabled in firmware, a corrupted WSL kernel package, or a pending Windows update that the installer needs. Enable virtualization in BIOS/UEFI first, then run Windows Update before retrying the install.
  - q: "Can I run Docker and x86 Linux tools in WSL on Snapdragon?"
    a: >
      Docker Desktop now ships with ARM64 support for Windows, and most mainstream developer tools have ARM64 Linux builds. x86 Linux binaries can sometimes run through emulation but expect slower performance — for x86 container images, check our [Docker Desktop on ARM Windows](/articles/docker-desktop-arm-windows-issues/) guide.
  - q: "WSL launches but networking does not work. What should I check?"
    a: >
      Networking failures in WSL2 on ARM are often caused by third-party VPN clients or firewalls blocking the virtual switch. Temporarily disable your VPN and any third-party firewall, restart the WSL VM with wsl --shutdown, and test connectivity again.
---

You type `wsl --install` on your brand-new Snapdragon laptop and get an error, or WSL installs but no distro will launch — just a black window, a cryptic error code, or an instant crash back to the terminal.

WSL2 on Windows on ARM runs a real ARM64 Linux kernel inside a lightweight Hyper-V virtual machine. That architecture difference is the root of nearly every failure: virtualization must be enabled in firmware, you need ARM64 (not x64) distro packages, and many familiar Linux tools only exist for x86. The good news is that once the prerequisites are right, WSL on Snapdragon is genuinely good — Ubuntu ARM, Debian ARM, and Fedora ARM all run natively with near-native speed. Similar ARM-only snags bite other subsystems too, like [lock screen widgets failing on Windows 11](/articles/lock-screen-widgets-not-working/) and [Photos generative erase issues](/articles/photos-generative-erase-not-working/) — the pattern is the same: ARM builds need their own attention.

This guide gives you six fixes in order: enable virtualization and confirm the CPU is ready, update Windows and the WSL kernel, install the correct ARM64 distro, repair a broken WSL installation, fix networking and VPN conflicts, and reset WSL fully. Run everything from an elevated terminal.

## Why this happens

- **Virtualization disabled in firmware:** WSL2 requires the Hyper-V hypervisor. If virtualization is off in BIOS/UEFI, `wsl --install` fails immediately with a virtualization error.
- **Wrong distro architecture:** Installing an x64-only Linux distribution (or pulling an x64 package inside Linux) on an ARM machine fails or crawls. ARM needs ARM64 builds of everything.
- **Corrupted WSL kernel update:** WSL2's Linux kernel is delivered through Windows Update or a separate MSI. A failed or half-applied kernel update leaves WSL unable to boot any distro.
- **Pending Windows updates:** The WSL installer depends on OS components that only exist in recent builds. A laptop that skipped updates may lack the WSL platform pieces the installer expects.
- **VPN or firewall blocking the virtual switch:** WSL2 creates a Hyper-V virtual network adapter. Third-party VPN clients and firewalls frequently block or hijack it, killing all Linux networking.
- **Conflicting virtualization software:** Some third-party hypervisors and security products fight the Hyper-V hypervisor, leaving WSL in a state where it installs but never starts.
- **Corrupted distro or WSL state:** A crashed import, a disk-full event, or a forced shutdown can corrupt the distro's virtual disk, producing launch failures that look like install failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable virtualization in firmware and confirm CPU readiness

WSL2 cannot exist without the hypervisor, and the hypervisor cannot exist without firmware-level virtualization. This is the gate everything else passes through.

1. Open Task Manager (**Ctrl + Shift + Esc**), go to the **Performance** tab, select **CPU**, and check that **Virtualization** says **Enabled**.
2. If it says Disabled, restart the laptop and enter BIOS/UEFI (usually **F2** or **Del** during boot; on Snapdragon laptops sometimes **Volume Up + Power**).
3. Find the virtualization setting (often under **Advanced > CPU Configuration**) and enable it, then save and exit.
4. Boot into Windows, open an elevated PowerShell (**Windows key + X > Terminal (Admin)**), and run `systeminfo` — confirm the Hyper-V Requirements section shows **Yes** on all lines.
5. Only when virtualization reports Enabled should you retry any WSL install command.

### Fix 2: Update Windows and install the WSL kernel package

A stale OS build or a missing kernel package breaks the installer in ways that look like ARM problems but are not.

1. Open **Settings > Windows Update** and install every pending update, then restart — WSL components ship inside OS builds.
2. In the elevated terminal, run `wsl --update` to force the WSL kernel package to the latest version.
3. If `wsl --update` fails, download the WSL kernel update package manually from [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) (search "WSL manual install steps") and run the MSI.
4. After updating, run `wsl --status` and confirm it reports a version for both the WSL platform and the kernel.

### Fix 3: Install an ARM64 distro from the Microsoft Store

The distro must match the architecture. This is the single most common real mistake on Snapdragon laptops — grabbing whatever Ubuntu entry looks familiar without checking the architecture.

1. Open the Microsoft Store and search for **Ubuntu** — choose the entry explicitly labeled for ARM or WSL (the standard **Ubuntu** listing ships an ARM64 WSL rootfs on ARM machines).
2. Click **Install**, then launch the distro from the Start menu and let it complete first-run setup (create your UNIX username and password).
3. Inside the distro, run `uname -m` — it must report **aarch64**. If it reports x86_64, you installed the wrong build; uninstall it and pick the ARM entry.
4. Run `sudo apt update && sudo apt upgrade -y` (for Ubuntu/Debian) to bring the ARM64 package set current.
5. Test with `wsl -l -v` from PowerShell — your distro should show version **2**, not 1.

### Fix 4: Repair or reinstall the WSL platform

When `wsl --install` fails outright or distros refuse to launch despite correct prerequisites, the WSL platform itself needs repair.

1. In the elevated terminal, run `wsl --shutdown` to stop all WSL VMs and the background service.
2. Run `DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Windows-Subsystem-Linux` and then `DISM /Online /Enable-Feature /All /FeatureName:VirtualMachinePlatform`, restarting if prompted.
3. If install previously failed with error **0x8007019e** or **0x80370102**, those two DISM commands plus a reboot are the documented fix.
5. Check **Settings > Apps > Installed apps** for a **Windows Subsystem for Linux** entry; if it is present and broken, uninstall it and reinstall from the Microsoft Store.

### Fix 5: Fix WSL networking and VPN conflicts

Distro launches fine but `apt` and `curl` fail, or SSH connections die — classic virtual-switch interference, common with VPN clients on ARM laptops.

1. Fully quit your VPN client (not just disconnect — exit the app) and any third-party firewall, then run `wsl --shutdown` in PowerShell.
2. Relaunch your distro and test with `ping -c 3 8.8.8.8` — if ICMP works but DNS fails, the issue is DNS, not connectivity.
3. For DNS failures, create `/etc/wsl.conf` inside the distro with `[network]` and `generateResolvConf = false`, then write your own `/etc/resolv.conf` with `nameserver 8.8.8.8`.
4. In Windows, open **Control Panel > Network and Internet > Network Connections** and confirm a **vEthernet (WSL)** adapter exists and is enabled.
5. If your VPN is mandatory, check its settings for a **split tunneling** or **allow LAN/virtual adapters** option and add the WSL subnet to the allowed list.

### Fix 6: Unregister and reinstall the distro as a last resort

When a distro's virtual disk is corrupted — usually from a forced shutdown or a full disk — no repair command saves it. A clean reinstall takes minutes and fixes it.

1. Export anything you need first: `wsl --export Ubuntu C:\backup\ubuntu.tar` from PowerShell.
2. Unregister the broken distro with `wsl --unregister Ubuntu` — this deletes its virtual disk, so be sure the export succeeded.
3. Reinstall from the Microsoft Store entry you used in Fix 3 and complete first-run setup.
4. Restore files selectively from the exported tar rather than re-importing the whole disk, since the disk itself may carry the corruption.
5. After reinstall, run `wsl -l -v` to confirm version 2, then reinstall your dev tools using ARM64 packages — see our [Epson printer on ARM laptop](/articles/epson-printer-arm-laptop/) guide for the same ARM64-first habit applied to peripherals.

## Closing

WSL on Snapdragon is fully capable once the three ARM truths are respected: virtualization on in firmware, a current Windows build with the WSL kernel, and ARM64 distros and packages throughout. Most failures trace to one of those three, with VPN interference a distant fourth. The honest limitation to keep in mind: x86 Linux binaries and x86 container images are second-class citizens here — use ARM64 images wherever they exist and you will get the fast, native experience these laptops were designed for. Microsoft's own WSL documentation, reachable through the [Windows support hub](https://support.microsoft.com/en-us/windows), stays current on ARM-specific notes as the platform evolves.
