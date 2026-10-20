---
title: "How to Fix Docker Desktop on ARM Windows"
slug: docker-desktop-arm-windows
date: 2026-10-20
categories: ["ai-pc"]
tags: ["docker desktop", "containers", "arm windows", "troubleshooting", "ai pc", "wsl2"]
description: "Docker Desktop failing on your ARM Windows laptop? Learn why installs stall and containers won't start on Snapdragon X, then apply proven fixes that work."
thumbnail: "/images/thumbs/docker-desktop-arm-windows.webp"
faqs:
  - q: "Is there a native Docker Desktop build for ARM Windows?"
    a: "Yes. Docker ships an official ARM64 build of Docker Desktop for Windows on ARM that runs natively on Snapdragon X. Do not install the x64 build — it will refuse to install or limp along under emulation with constant failures."
  - q: "Why does Docker Desktop say virtualization is not enabled?"
    a: "Docker Desktop runs its Linux VM through WSL2, which needs hardware virtualization turned on in UEFI firmware. Many Snapdragon laptops ship with the toggle off. Enable it in firmware, confirm Task Manager shows Virtualization as Enabled, then restart Docker."
  - q: "Can I run x86 container images on an ARM laptop?"
    a: "Technically yes through QEMU emulation, but it is slow and many images crash. Prefer multi-arch images and pull the ARM64 variant explicitly with `--platform linux/arm64`. Rebuild your own images for ARM64 for anything you run regularly."
  - q: "Docker Desktop was working and suddenly stopped starting. What changed?"
    a: "Usually a Windows update, a WSL kernel update, or a corrupted Docker WSL distro. Run `wsl --update` and `wsl --shutdown`, then check Docker Desktop's Troubleshoot menu. A factory reset of Docker Desktop fixes most sudden breakages."
---

Docker Desktop on a Snapdragon X laptop should mean silent, cool-running containers — but many ARM users get an installer that refuses to run, a whale icon stuck on "starting," or containers that crash on boot. The causes are almost always the same handful of issues: the wrong installer architecture, a WSL2 stack that is not ready, or x86 images forced onto an ARM64 kernel.

The good news is that Docker officially supports Windows on ARM with a native ARM64 build that performs well. The bad news is that years of x64-first tutorials still dominate search results, and following them on ARM leads straight into emulation traps. This guide covers the ARM-specific fixes in the right order — installer, virtualization, WSL2 backend, image architecture, and the clean reset.

If you have not set up WSL2 yet, start with our [WSL not working on ARM laptop guide](/articles/wsl-not-working-arm-laptop/), since Docker Desktop depends on that entire stack. And if your ARM laptop doubles as a gaming machine, our [Steam games on ARM laptop guide](/articles/steam-games-arm-laptop/) covers similar emulation pitfalls on the gaming side.

## Why this happens

- **Wrong installer architecture:** The default x64 installer may install under emulation and fail strangely, or refuse outright — always download the ARM64 build.
- **Virtualization disabled in firmware:** Docker's backend is a WSL2 VM — with the UEFI toggle off, the engine can never start, and the errors blame Docker instead of the firmware.
- **WSL2 stack broken underneath:** Docker relies on your WSL installation rather than its own kernel; a stale kernel or corrupted Docker WSL distros stop the engine from starting.
- **x86 images on an ARM64 kernel:** Pulling a `latest` tag that only ships an x86 build forces QEMU emulation — many images crash, hang, or run far slower than expected.
- **Under-provisioned WSL2 resources:** Default WSL2 memory and CPU limits can starve the Docker VM when Windows is busy, causing timeouts during pulls and container starts.
- **Corrupted Docker data after updates:** Windows and Docker updates occasionally corrupt the docker-desktop WSL distros, leaving Docker permanently "starting" until reset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 Docker Desktop build

This is the easiest thing to get wrong, because Docker's download page defaults to the x64 installer for most visitors. The x64 build on ARM either fails its prerequisite checks or installs under Prism emulation, where the backend crashes unpredictably. If your installer filename does not say ARM64, you have the wrong one — uninstall it first, since leftover x64 services conflict with the native build.

1. Uninstall any existing Docker Desktop from Settings, then reboot the laptop.
2. Download the installer labeled for Windows ARM64.
3. Run it and accept the default WSL2 backend option when prompted.
4. Launch Docker Desktop and wait for the engine to reach "Running" before pulling anything.

### Fix 2: Enable virtualization and repair the WSL2 backend

Docker Desktop hangs at startup when the WSL2 layer it sits on is unhealthy — its Linux VM is just a specialized WSL2 distro, so every WSL2 fix applies here. Firmware virtualization must be on, the Virtual Machine Platform feature enabled, and the WSL kernel current. Our full [WSL troubleshooting walkthrough](/articles/wsl-not-working-arm-laptop/) covers the deep cases; the essentials are below. For background on the Windows features involved, see the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Confirm Task Manager's Performance tab shows "Virtualization: Enabled"; if not, enable it in UEFI firmware.
2. Run `wsl --update` in PowerShell, then `wsl --shutdown` for a clean WSL2 restart.
3. In Docker Desktop Settings, under General, confirm "Use the WSL 2 based engine" is checked.
4. Restart Docker Desktop and run `docker version` to confirm client and server both respond.

### Fix 3: Pull ARM64 images and rebuild your own for ARM

This is the fix that transforms Docker on ARM. When you pull an image whose tag only contains an x86 build, Docker either errors out or silently runs it under QEMU emulation — dramatically slower and crash-prone. Multi-arch images contain both variants and Docker picks correctly, but only if the publisher built them. For your own Dockerfiles, the ARM64 platform flag produces native images that run at full speed.

1. Pull explicitly: `docker pull --platform linux/arm64 <image>`.
2. Check available architectures first with `docker buildx imagetools inspect <image>`.
3. Rebuild your own images natively: `docker build --platform linux/arm64 -t <name> .`.
4. In Compose files, add `platform: linux/arm64` under each service so every container resolves to ARM.

### Fix 4: Repair corrupted Docker WSL distros without losing data

Docker Desktop keeps two hidden WSL distros — docker-desktop and docker-desktop-data — and when either corrupts after an update, the app sits at "starting" forever. Reinstalling rarely helps because the installer preserves the corrupted distros. Unregister the engine distro while keeping the data distro, then let Docker recreate it on next launch — your images and volumes live in the data distro, so your work survives. This preserves your images while clearing corruption that reinstalls cannot touch.

1. Quit Docker Desktop fully, then run `wsl --list -v` to see the docker-desktop distros.
2. Run `wsl --unregister docker-desktop`, leaving docker-desktop-data untouched.
3. Start Docker Desktop and let it recreate the engine distro, which takes a few minutes.
4. Verify with `docker ps` and `docker images` that your containers and images survived.

### Fix 5: Factory reset Docker Desktop as a last resort

When nothing else works, a factory reset clears accumulated bad state in one move. Docker Desktop's Troubleshoot menu offers "Clean / Purge data"; a full reset also removes images and volumes. Back up irreplaceable data first — push custom images to a registry, export named volumes. Then reinstall the ARM64 build fresh and reconfigure from a known-good state rather than restoring old settings.

1. Back up irreplaceable data: push custom images to Docker Hub or export volumes you cannot rebuild.
2. In Docker Desktop, click the Troubleshoot (bug) icon and choose "Clean / Purge data".
3. If problems persist, uninstall Docker, delete `%APPDATA%\Docker`, and reinstall the ARM64 build.
4. Re-pull images with `--platform linux/arm64` and confirm the engine reaches "Running".

## Closing

Docker Desktop on ARM works well once three things are true: the native ARM64 build, a healthy WSL2 backend, and ARM64 images instead of emulated x86. The fixes above address them in the order that wastes the least time. Stick to multi-arch images and keep WSL updated, and your Snapdragon laptop becomes a quiet, all-day container machine. If your containers run local AI models, also confirm the [NPU is actually being used by apps in Windows 11](/articles/npu-not-used-by-apps-windows-11/) rather than sitting idle — and if you are shopping for more headroom, our [best Copilot+ PC under $1000](/articles/best-copilot-plus-pc-under-1000/) guide compares machines with the RAM containers love.
