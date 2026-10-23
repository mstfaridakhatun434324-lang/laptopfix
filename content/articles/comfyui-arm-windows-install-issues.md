---
title: "How to Fix ComfyUI Install Issues on Windows 11 ARM (Copilot+ PCs)"
slug: comfyui-arm-windows-install-issues
date: 2026-10-23
categories: ["ai-pc"]
tags: ["comfyui", "windows on arm", "copilot+ pc", "python", "stable diffusion", "directml"]
description: "Fix ComfyUI install failures on Windows 11 ARM: ARM64-native Python, DirectML PyTorch builds, skipping x64-only packages, and launch flags for Copilot+ PCs."
thumbnail: "/images/thumbs/comfyui-arm-windows-install-issues.webp"
faqs:
  - q: "Why does pip say it can't find torch on my ARM laptop?"
    a: "Because the official install command points pip at CUDA builds of PyTorch, which do not exist for Windows on ARM64. Install a DirectML-capable PyTorch build using an ARM64-native Python 3.11 instead, and skip the CUDA wheel line from the README entirely."
  - q: "Can I use the official ComfyUI portable build on a Copilot+ PC?"
    a: "The portable build targets x64 PCs with NVIDIA GPUs, so on ARM it runs under emulation at best and usually fails. A manual install with ARM64-native Python and a DirectML backend is the reliable path on Snapdragon laptops."
  - q: "Do I need xformers for ComfyUI on ARM?"
    a: "No. xformers has no ARM64 Windows wheels, so the install dies on it. ComfyUI runs fine without xformers — remove it from requirements.txt and let the default attention implementation handle the work."
  - q: "Why is my first image generation so slow?"
    a: "DirectML compiles shaders on first use, which can take several minutes on the first run — that is normal, not a failure. Later generations are much faster. If every run stays slow, confirm you launched with the DirectML flag and not the CPU fallback."
---

You followed the ComfyUI install guide, ran the pip commands, and instead of a working Stable Diffusion UI you got a wall of red text — "Could not find a version that satisfies the requirement torch" or an installer that crashes halfway through. On an NVIDIA machine the official steps just work; on a Snapdragon Copilot+ laptop they break almost immediately, and the errors rarely explain why.

The reason is architectural. ComfyUI's official Windows instructions and portable build target x64 PCs with NVIDIA GPUs — they pull CUDA builds of PyTorch that do not exist for Windows on ARM64. Your Copilot+ PC is a different machine: it needs ARM64-native Python, a DirectML-capable PyTorch build instead of CUDA wheels, and launch flags that skip x64-only extras like xformers. Nothing is broken about your laptop; the recipe was written for a different kitchen.

This guide rebuilds the install for ARM the way a technician would: six fixes in order, from the Python interpreter and virtual environment, through the correct PyTorch and DirectML installation order, to model folders and launch flags. Work through them in sequence and check the server output after each step — the same methodical approach behind other [slow ARM app installs](/articles/epic-games-launcher-arm-windows-slow/) on this platform.

## Why this happens

- **CUDA PyTorch wheels do not exist for ARM64:** the official README points pip at CUDA torch builds with no ARM64 equivalent, so pip fails with "could not find a version" errors.
- **x64 Python instead of ARM64 Python:** the x64 interpreter under emulation gets every native package lookup wrong, and performance collapses even on successful installs.
- **Wrong Python version:** ComfyUI's dependency chain is validated against specific Python releases; a too-new interpreter breaks pinned packages.
- **xformers and other x64-only extras:** the requirements pull packages with no ARM64 wheels; the install dies on them unless deliberately skipped.
- **Missing Visual C++ build tools:** packages compiling from source on ARM64 need the MSVC build tools — without them the compile fails cryptically.
- **Corrupted virtual environment:** a half-failed first install leaves mixed packages behind, and rerunning pip in the same broken venv repeats the failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install ARM64-native Python 3.11 and start clean

Everything downstream depends on the interpreter: an x64 Python on an ARM laptop makes every wheel lookup wrong and tanks performance even when something installs. Download the Windows ARM64 build of Python 3.11, tick "Add python.exe to PATH" during setup, and delete any virtual environment left over from a failed attempt. This gives pip a native foundation where ARM64 wheels resolve correctly — and honestly, a surprising share of ComfyUI-on-ARM failures end right here, at the interpreter choice nobody questioned.

1. Install the ARM64 build of Python 3.11 with "Add python.exe to PATH" checked.
2. Delete the old `venv` folder — or the whole ComfyUI folder — to remove corrupted state.
3. In a fresh Command Prompt, run `python -c "import platform; print(platform.machine())"` and confirm it prints ARM64.
4. Place ComfyUI in a short path without spaces, for example `C:\ComfyUI`.
5. Create a fresh venv with `python -m venv venv` and activate it before installing anything.

### Fix 2: Install a DirectML-capable PyTorch build for ARM64

The stock install command from the ComfyUI README pulls CUDA wheels and dies on ARM64 — that single line is the most common point of failure. On Copilot+ PCs the supported GPU path is DirectML, so install a PyTorch build with DirectML support before anything else touches the environment. That DirectML and driver stack also powers [Studio Effects features like teleprompter eye contact](/articles/studio-effects-teleprompter-eye-contact/) — if both are flaky, the Adreno and NPU drivers are the common suspect, not your technique.

1. With the venv activated, install the DirectML backend first (for example `pip install torch-directml`).
2. Verify it imports: `python -c "import torch_directml; print(torch_directml.is_available())"` should print True.
3. Never run the README’s CUDA torch install line — it is the x64 NVIDIA recipe.
4. On "no matching distribution," recheck Fix 1: an x64 Python is probably active.
5. Upgrade pip first (`python -m pip install --upgrade pip`); old versions misread ARM64 wheel tags.

### Fix 3: Install requirements with x64-only extras skipped

ComfyUI’s requirements.txt includes packages with no ARM64 wheels — xformers being the famous one — so a straight `pip install -r requirements.txt` dies on them. Edit the requirements to exclude those extras, then install and watch for “Building wheel” lines, which signal source compiles needing the C++ build tools. Skipping xformers costs nothing functional here; it only accelerates attention on NVIDIA cards you do not have. If a package still fails, install it individually once the build tools are in place.

1. Open `requirements.txt` and comment out the xformers line — ComfyUI runs fine without it.
2. Run `pip install -r requirements.txt` and note any package that fails.
3. Install the Microsoft C++ Build Tools (Desktop development with C++) if a package fails to build.
4. Ensure pip pulls `onnxruntime-directml` rather than CPU-only onnxruntime if your workflow needs DirectML.
5. Note anything you skipped; revisit it in Fix 6 if generation errors point back here.

### Fix 4: Put models and custom nodes in the right folders

A successful dependency install can still greet you with an empty UI when the folder layout is wrong. ComfyUI looks in strict paths — `ComfyUI\models\checkpoints` for base models, with matching subfolders for LoRAs, VAEs, and ControlNet — and a checkpoint dropped in the root folder is simply invisible. Custom nodes cloned into the wrong directory also fail to load silently, which looks exactly like an install failure from the browser’s point of view, so verify the layout before reinstalling anything.

1. Place checkpoints in `ComfyUI\models\checkpoints\`, creating the folder if missing.
2. Put LoRAs, VAEs, and ControlNet models in their matching subfolders under `models\`.
3. Clone custom nodes into `ComfyUI\custom_nodes\`, then run any `install.py` the node ships with.
4. Restart the server and read the console log — it names loaded checkpoints and failed imports.
5. Refresh http://127.0.0.1:8188 and confirm the checkpoint dropdown is populated.

### Fix 5: Launch with ARM-safe flags

Default launch assumptions target NVIDIA: xformers flags, CUDA memory settings, and preview methods that can crash or crawl on DirectML. Launch with the DirectML flag so ComfyUI uses the right backend, set the VRAM mode to match your unified memory, and strip out any CUDA-specific flags copied from x64 tutorials. This is the same class of silent misconfiguration behind [Night Light not working on ARM laptops](/articles/night-light-not-working-arm-laptop/) — platform defaults quietly doing the wrong thing on this architecture until you override them.

1. Launch with `python main.py --directml --preview-method auto` from the activated venv.
2. Add `--lowvram` on 16 GB or less; `--normalvram` is the sweet spot with more memory.
3. Remove any `--xformers`, `--force-fp16`, or CUDA-only flags copied from NVIDIA guides.
4. Expect a slow first generation — DirectML compiles shaders on first use, which is normal.
5. On out-of-memory errors, drop batch size to 1 and use tiled VAE settings.

### Fix 6: Fix startup, browser, and permission problems

Sometimes the server is fine but nothing appears in the browser, or Windows interferes with the stack. Antivirus software loves quarantining Python executables inside venvs, firewalls block the local port, and a previously crashed server can hold port 8188 open so the new instance silently fails to bind. These are environmental issues, not ComfyUI bugs. If the DirectML backend itself misbehaves after a clean install, update the Adreno graphics driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support before blaming the app.

1. On "Address already in use," kill the zombie python.exe in Task Manager and relaunch.
2. Try http://127.0.0.1:8188 explicitly — "localhost" can fail on some setups.
3. Add the ComfyUI folder as a Windows Security exclusion if files get quarantined mid-install.
4. Allow Python through the firewall prompt when it appears; blocking it kills the server UI.
5. Run Command Prompt as a normal user daily — admin installs tangle venv permissions.

## Closing

Once the right interpreter, the DirectML PyTorch build, and ARM-safe launch flags are in place, ComfyUI on a Copilot+ PC is just ComfyUI — slower than a discrete NVIDIA card on large models, but fully usable for everyday generation. Keep the venv isolated per project, pin the combination that works, and resist copying x64 CUDA tutorials verbatim.
