---
title: "DirectStorage Not Working on ARM Laptops: How to Fix It"
slug: directstorage-not-working-arm-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["directstorage", "nvme ssd", "gaming", "arm laptop", "gpu decompression", "troubleshooting"]
description: "Fix DirectStorage not working on ARM laptops: verify NVMe and driver requirements, enable GPU decompression, and fix game loading issues step by step."
thumbnail: "/images/thumbs/directstorage-not-working-arm-laptop.webp"
faqs:
  - q: "What is DirectStorage and why does it matter?"
    a: "DirectStorage lets games load assets straight from the NVMe SSD to the GPU, bypassing the CPU bottleneck. It dramatically cuts loading times and enables seamless open worlds — but it needs an NVMe SSD, a compatible GPU driver, and game support."
  - q: "Does DirectStorage work on ARM laptops?"
    a: "Yes, when the requirements are met: Windows 11, an NVMe SSD, and a GPU driver with DirectStorage support (Adreno, Radeon, or Intel Arc drivers on AI laptops). The game itself must also implement DirectStorage."
  - q: "How do I check if DirectStorage is active in a game?"
    a: "Most games don't show an indicator. The practical test is loading times: with DirectStorage working, supported games load in seconds. Some games log DirectStorage initialization in their config or log files."
  - q: "Can DirectStorage work on a SATA SSD?"
    a: "Partially — Windows 11 supports a limited DirectStorage path on slower drives, but the real benefits need NVMe. On a SATA drive you won't see the dramatic loading improvements."
---

Your game supports DirectStorage, your ARM laptop has an NVMe SSD, but loading times are still slow — or the game warns that DirectStorage is unavailable. The feature has a strict requirements chain (OS, SSD, GPU driver, game implementation), and ARM laptops add driver-maturity wrinkles to the GPU end of that chain.

DirectStorage is worth fixing: on a proper setup it turns 30-second loads into 5-second ones. This guide walks the requirements chain in order — verifying each link, fixing the broken ones — across six sections.

## Why this happens

- **Game installed on the wrong drive:** DirectStorage needs the game on an NVMe SSD. Installed on a SATA drive, SD card, or external USB drive, the feature silently disables itself.
- **GPU driver lacks DirectStorage support:** The Adreno/Radeon/Arc driver must support GPU decompression. An outdated or generic driver (Microsoft Basic Display Adapter) has no DirectStorage path.
- **Game doesn't actually use DirectStorage:** Marketing claims aside, the game build must implement it. Some games advertise "DirectStorage ready" for a future patch.
- **Windows 11 version too old:** Full DirectStorage (especially GPU decompression) needs recent Windows 11 builds. An unupdated system caps the feature.
- **NVMe driver or configuration issues:** The storage stack must deliver full NVMe performance — a degraded NVMe driver or a drive in the wrong mode throttles the throughput DirectStorage needs.
- **Shader/asset pipeline conflicts:** Corrupted shader caches or game file issues can make a DirectStorage-enabled game fall back to slow loading without any error message.
- **Security software interfering with I/O:** Overzealous antivirus or enterprise endpoint tools (the same class as [VPN client conflicts](/articles/cisco-anyconnect-arm64-windows/)) can intercept the high-throughput I/O path DirectStorage relies on.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the game is on an NVMe SSD

The most common "DirectStorage not working" cause is also the simplest: the game isn't on a qualifying drive.

1. Open **Settings > System > Storage > Advanced storage settings > Disks & volumes** and identify which physical disk is NVMe (it says so in the properties).
2. Check where the game is installed (Steam: right-click game > Properties > Installed Files > Browse; Xbox app: check the install drive in settings).
3. If the game is on a SATA SSD, HDD, or external drive, move it: in Steam use **Properties > Installed Files > Move install folder**; for Xbox/MS Store games, reinstall choosing the NVMe drive.
4. Verify the NVMe drive is healthy and fast: run CrystalDiskMark (ARM64-compatible) — you should see sequential reads in the GB/s range, not MB/s.
5. Retest the game's loading times. If they are now dramatically faster, the drive was the entire issue.

### Fix 2: Update the GPU driver to a DirectStorage-capable version

GPU decompression is the heart of DirectStorage 1.1+, and it lives in the graphics driver. A stale or generic driver kills it.

1. Check your current GPU driver: **Device Manager > Display adapters > Properties > Driver** — note the date and version.
2. Download the latest graphics driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — or from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) / [AMD](https://www.amd.com/en/support/download/drivers.html) for your platform.
3. Clean-install it: uninstall the old driver with driver removal checked, restart, install the new package as administrator, restart again.
4. Confirm in **Task Manager > Performance > GPU** that the real GPU (not Basic Display Adapter) is active with proper driver version.
5. If you are on Snapdragon/Adreno specifically, check the OEM's release notes for DirectStorage or GPU-decompression mentions — Adreno DirectStorage support matured across driver releases.

### Fix 3: Update Windows and verify the DirectStorage runtime

The OS side of DirectStorage ships with Windows 11 and updates over time. An outdated build caps the feature set.

1. Open **Settings > Windows Update** and install all pending updates — then check for updates again until fully current.
2. Verify you are on a recent Windows 11 build (**Settings > System > About** — 23H2 or newer at minimum; newer is better for DirectStorage).
3. The DirectStorage runtime itself updates via the Microsoft Store and Windows Update — no manual install needed, but it must not be blocked (check Store updates aren't paused).
4. Run `dxdiag` and check the Display tab notes for DirectStorage-related capabilities or errors.
5. Restart after all updates and retest the game — OS-level fixes only take effect after a reboot.

### Fix 4: Verify the game actually supports DirectStorage

Not every game that should support it does, and support varies by patch version. Confirm before chasing system fixes.

1. Check the game's official patch notes or support pages for DirectStorage mentions — look for the specific version that added it.
2. Update the game fully — a pending patch may be the one containing DirectStorage support.
3. Check the game's graphics/settings menu for a DirectStorage toggle — some games let you enable/disable it explicitly.
4. Look in the game's install folder for log files mentioning DirectStorage initialization — a log line saying it fell back to legacy loading tells you the game tried and failed (a system issue) versus never tried (a game issue).
5. If the game simply doesn't implement DirectStorage yet, no system fix helps — the feature arrives with the game's patch, not your troubleshooting.

### Fix 5: Clear shader caches and verify game files

Corrupted cached data can silently disable the fast path. Clearing caches forces a clean rebuild of the asset pipeline.

1. In the game's launcher (Steam, Epic, Xbox app), run **Verify integrity of game files** — corrupted assets can break the DirectStorage path without visible errors.
2. Clear the GPU shader cache: **Settings > System > Storage > Temporary files** — check **DirectX Shader Cache** and remove it. The game rebuilds it on next launch (first load will be slow; subsequent loads show the real improvement).
3. Check your GPU control panel (Intel Graphics Software, AMD Adrenalin) for shader cache settings and reset them to defaults.
4. Temporarily disable third-party antivirus real-time scanning for the game folder as a test — if loads speed up, add a permanent exclusion for the game directory.
5. The same "clear stale state" logic applies broadly on AI PCs — from [driver troubleshooting via PowerShell](/articles/powershell-7-arm-windows-issues/) to security attestation hiccups ([Pluton attestation](/articles/pluton-tpm-attestation-failed/)) — stale state is a universal suspect.

### Fix 6: Check NVMe health and system-level bottlenecks

If everything above is correct and loads are still slow, the storage subsystem itself may be underperforming.

1. Check SSD health with CrystalDiskInfo — look at SMART status and the drive's temperature (thermal throttling tanks NVMe speeds).
2. Ensure the NVMe driver is the OEM's (Device Manager > Storage controllers) — the generic Windows NVMe driver works but the OEM's is often faster.
3. Close background disk hogs during gaming: check Task Manager's Disk column for processes hammering the SSD while the game loads.
4. If the laptop has multiple NVMe slots, confirm the game drive is in the fastest slot (check the manual — secondary slots are sometimes slower).
5. As a final check, benchmark with CrystalDiskMark and compare against the drive's rated speeds — if the drive itself underperforms its spec significantly, the SSD may be failing regardless of DirectStorage.

## Closing

DirectStorage on ARM laptops fails at one of four gates: the game isn't on NVMe, the GPU driver predates decompression support, Windows is outdated, or the game doesn't implement it yet. Walk the chain in order — drive, driver, OS, game — clear the shader cache, and the multi-GB/s loading path opens up.
