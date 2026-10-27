---
title: "How to Fix Automatic1111 Install Issues on ARM Windows"
slug: automatic1111-arm-windows-install-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["automatic1111", "stable diffusion webui", "arm windows", "install", "python", "troubleshooting"]
description: "Fix Automatic1111 install issues on ARM Windows with steps for Python, Git, dependency errors, torch backend selection, and launch failures on Snapdragon."
thumbnail: "/images/thumbs/automatic1111-arm-windows-install-fix.webp"
faqs:
  - q: "Does Automatic1111 work on Windows ARM laptops?"
    a: >
      It can, but with caveats. Automatic1111 is built around x64 Python and CUDA workflows, so on ARM laptops it runs through emulation with a DirectML backend. Expect slower installs, more dependency friction, and lower generation speed than on x64 machines.
  - q: "Why does the webui installer fail on ARM?"
    a: >
      The installer assumes x64 wheels for several packages. On ARM, some packages lack prebuilt wheels and must compile or fall back to slower paths, which fails when build tools are missing or when a package has no ARM-compatible version.
  - q: "Do I need Git installed for Automatic1111?"
    a: >
      Yes. The standard install clones the repository with Git, and updates use Git too. Without Git in your PATH, the installer fails at the first step with a Git-not-found error.
  - q: "Is Fooocus easier than Automatic1111 on ARM?"
    a: >
      Generally yes. Fooocus has a simpler install and fewer configuration options, which means fewer ARM-specific failure points. Users who only need image generation often have an easier time with Fooocus on ARM laptops.
---

You try to install Automatic1111's Stable Diffusion WebUI on your Snapdragon laptop and the installer fails — Git not found, a package that will not build, a torch install that finds no GPU, or a web interface that never opens. Automatic1111 was designed for x64 machines with NVIDIA GPUs, so on ARM Windows every assumption in its installer needs checking: the Python architecture, the package wheels, and the GPU backend all differ from the expected setup.

This guide works through the ARM-specific install chain in order, with honest notes about where the ARM path is simply harder than x64 and where a simpler frontend is the better choice.

## Why this happens

- **x64 Python under emulation conflicts:** Running x64 Python through Prism emulation works but complicates package selection, since some wheels are architecture-specific.
- **Missing ARM-compatible wheels:** Some dependencies lack prebuilt ARM64 wheels, so pip tries to build from source and fails without C++ build tools.
- **Git missing from PATH:** The installer clones and updates via Git. Without Git installed and on the PATH, it fails immediately.
- **CUDA torch installed by default:** The default installer path targets CUDA, which does not exist on ARM laptop GPUs. The backend must be switched to DirectML.
- **Visual C++ build tools missing:** Packages that must compile from source need Microsoft C++ Build Tools, which most laptops do not have installed.
- **Launch port or permission issues:** A stale process, a blocked port, or an install folder under a protected path can make a completed install appear dead.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install Git and the right Python first

The installer cannot start without Git, and Python architecture affects everything after. Get both right before cloning anything.

1. Install Git for Windows and confirm `git --version` works in a fresh terminal.
2. Install a Python version in Automatic1111's supported range — check its documentation for the exact version.
3. Confirm Python is on the PATH with `python --version` in a fresh terminal.
4. Decide on the install folder: use a short path without spaces, such as a folder directly under your user directory, to avoid path-length problems.
5. Clone the repository with Git only after both tools check out. Environment setup problems like these also affect [Fooocus installs](/articles/fooocus-ai-laptop-install-fix/) on the same machines.

### Fix 2: Install C++ build tools for source-built packages

When a package lacks an ARM wheel, pip builds it from source. Without build tools, that step fails with a long compiler error that hides the simple cause.

1. Install Microsoft C++ Build Tools with the Desktop development with C++ workload.
2. Restart the terminal after installation so the new tools are on the PATH.
3. Re-run the installer and watch whether the previously failing package now builds.
4. If a specific package still fails, note its name and check whether an ARM-compatible version or a prebuilt wheel exists for it.
5. Consider skipping optional extensions at install time — install the base WebUI first, then add extensions one at a time.

### Fix 3: Force the DirectML backend instead of CUDA

The default torch path targets CUDA. On an ARM laptop GPU, DirectML is the backend that can actually see the hardware.

1. Do not accept a CUDA torch install on an ARM laptop — it will find no GPU.
2. Follow Automatic1111's DirectML launch arguments and install instructions for Windows without NVIDIA hardware.
3. Update the graphics driver from your laptop maker before testing device detection.
4. Launch with the DirectML arguments and check the startup log for the device it selects.
5. If the log still shows CPU only, verify the DirectML torch packages installed correctly and reinstall them explicitly if needed.

### Fix 4: Read the install log and fix the first failing package

Automatic1111's installer prints a long log. The first error is the real one; later errors are usually consequences of it.

1. Run the installer from a terminal so the full log stays visible.
2. Scroll to the first error — a package name, a missing tool, or a network failure — and ignore later cascading errors.
3. Install or repair that specific package or tool, then re-run the installer.
4. If the failure is a network error, disable VPNs and retry on a stable connection.
5. If the failure is a missing wheel for ARM, search the package's issue tracker for an ARM workaround before forcing a different version.

### Fix 5: Resolve launch, port, and permission problems

An install that completes but never opens is usually a launch problem, not an install problem.

1. End any stale Python or WebUI processes in Task Manager before relaunching.
2. Check the launch log for the local address and port, then open exactly that address in your browser.
3. Allow Python through the Windows firewall if prompted.
4. Move the install out of a protected folder like Program Files if permission errors appear — a user folder is safer.
5. Try launching with the listen or share arguments disabled first, since network-facing options add firewall complications.

### Fix 6: Decide whether Automatic1111 is the right tool on ARM

Sometimes the honest fix is a simpler frontend. Automatic1111's power comes with configuration surface that multiplies ARM friction.

1. Test a basic image generation once installed — if it works, even slowly, the install is proven.
2. If generation is unusably slow or extensions keep failing, try Fooocus for the same models with a simpler install.
3. Compare the two honestly: Automatic1111 offers extensions and control; Fooocus offers simplicity and stability on ARM.
4. Keep the working frontend and stop fighting the other one — both generate images from the same models.
5. For further Windows guidance, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows). Related guides include [Stable Diffusion DirectML on NPU](/articles/stable-diffusion-directml-npu-fix/) and [Perplexity on ARM](/articles/perplexity-app-windows-arm-issues-fix/).

## Closing

Automatic1111 on ARM Windows fails where its x64 assumptions break: Git, Python, package wheels, build tools, and the CUDA backend. Install Git and the right Python first, add build tools for source packages, force the DirectML backend, and read the log's first error instead of its last. And if the full WebUI keeps fighting you on ARM, Fooocus delivers the same models with far less friction — the images matter more than the interface. If this fix did not fully resolve the issue, related troubleshooting for [Acer Swift Edge 16 Ai Issues](/articles/acer-swift-edge-16-ai-issues-fix/) and [Click To Do Open With Not Working](/articles/click-to-do-open-with-not-working/) covers neighboring causes that can produce the same symptom on AI laptops.
