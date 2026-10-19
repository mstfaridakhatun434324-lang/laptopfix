---
title: "Copilot+ PC Requirements: Does Your Laptop Qualify?"
slug: copilot-plus-pc-requirements
date: 2026-10-19
categories: ["ai-pc"]
tags: ["copilot plus pc", "requirements", "npu", "specs", "windows 11"]
description: "What are the official Copilot+ PC requirements? See the exact NPU, RAM, storage, and Windows specs your laptop needs to qualify."
thumbnail: "/images/thumbs/copilot-plus-pc-requirements.webp"
faqs:
  - q: "What is the minimum NPU for a Copilot+ PC?"
    a: >
      40 TOPS (trillion operations per second). This is the headline requirement and the one most older laptops fail. The NPU must be a dedicated neural processor — a fast CPU or GPU alone does not count.
  - q: "Is 8 GB of RAM enough for Copilot+ PC?"
    a: >
      No. Microsoft requires 16 GB of RAM minimum. On-device AI models are memory-hungry, and 8 GB machines cannot run the Copilot+ feature set reliably.
  - q: "Do I need Windows 11 Pro for Copilot+ features?"
    a: >
      No. Windows 11 Home qualifies. The Copilot+ features work on both Home and Pro as long as the hardware requirements are met and the Windows build is current.
  - q: "Can a desktop PC be a Copilot+ PC?"
    a: >
      The certification originally targeted laptops, but the hardware requirements apply equally to desktops. A desktop with a qualifying NPU, 16 GB RAM, and Windows 11 can run the same Copilot+ features.
---

"Copilot+ PC" sounds like marketing, but behind the label sits a precise hardware specification from Microsoft. If your laptop meets every requirement, you get the full AI feature set: Recall, Click to Do, Live Captions with translation, and Windows Studio Effects, all accelerated on-device. Miss even one requirement and those features stay locked, no matter how new the machine feels.

The requirements exist for a technical reason. On-device AI models need a fast neural processor, plenty of memory to hold model weights, and a current OS with the right frameworks. This is not an arbitrary gate to sell new laptops — a 2021 ultrabook genuinely cannot run these workloads. To check your own machine against this list, use our guide on [how to check if your laptop is a Copilot+ PC](/articles/how-to-check-if-laptop-is-copilot-plus-pc/); for the broader compatibility question, see [is my laptop AI PC compatible](/articles/is-my-laptop-ai-pc-compatible/).

Here are the official requirements, what each one means, and how to verify it.

## Why this happens

- **NPU threshold:** 40 TOPS is far above what pre-2024 laptop NPUs delivered, which is why most existing laptops fail.
- **RAM floor:** AI models resident in memory need the 16 GB minimum; 8 GB machines page constantly and stutter.
- **Storage minimum:** 256 GB ensures room for model files, Recall snapshots, and the OS.
- **OS requirement:** Only Windows 11 has the AI frameworks (DirectML updates, NPU drivers stack) these features need.
- **OEM enablement:** The manufacturer must ship proper NPU drivers — qualifying hardware with broken drivers still fails in practice.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the NPU delivers 40+ TOPS
This is the requirement that eliminates most laptops.

1. Open Device Manager and expand "Neural processors" to find your NPU's exact name.
2. Look up that chip on the manufacturer's official spec page: Intel ARK for Intel AI Boost, AMD's site for Ryzen AI, Qualcomm's site for Hexagon/Snapdragon.
3. Confirm the NPU TOPS figure is 40 or higher. Examples that pass: Snapdragon X Elite/Plus (45), Intel Core Ultra 200V series (up to 48), AMD Ryzen AI 300 series (50+).
4. Examples that fail: Intel Core Ultra 100 series NPU (~11 TOPS), Apple-style "neural engines" on non-qualifying chips, and any laptop with no NPU at all.
5. If your NPU is under 40 TOPS, no other fix matters — the hardware cannot be certified.
6. Record the figure; you will reference it whenever AI features misbehave.

### Fix 2: Confirm 16 GB RAM and 256 GB storage
The less glamorous requirements, but equally mandatory.

1. Open Task Manager > Performance > Memory and read the total. It must be 16 GB or more.
2. In Settings > System > Storage, verify at least 256 GB total capacity.
3. Check Settings > System > About to confirm Windows 11 (not 10) is installed.
4. If RAM is the only shortfall and your laptop has SODIMM slots, a RAM upgrade is straightforward and relatively cheap.
5. If storage is short, you cannot easily fix soldered storage — but most modern laptops already ship with 512 GB or more.
6. All three hardware checks plus Windows 11 must pass simultaneously for the badge.

### Fix 3: Update Windows to a Copilot+ enabled build
Qualifying hardware on an old Windows build still will not unlock the features.

1. Go to Settings > Windows Update and install everything pending.
2. Copilot+ features rolled out across 2024-2025 builds; you need a recent 24H2 (or later) build.
3. After updating, restart and check Settings for the AI features section.
4. If features are still missing on qualifying hardware, check that your region supports them — some are region-gated.
5. Use Microsoft's official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) if Windows Update is stuck, or the [Update Catalog](https://www.catalog.update.microsoft.com/) for specific KB packages.
6. Keep the system updated going forward; NPU driver and AI framework updates ride along with Windows Update.

### Fix 4: Install the correct NPU driver from your OEM
Microsoft's requirement assumes a working driver stack. Generic drivers often underperform.

1. Go to your laptop maker's support site (Dell, HP, Lenovo, ASUS, Acer, Samsung, Microsoft) and find your exact model.
2. Download the chipset/NPU driver package — look for Intel AI Boost, AMD Ryzen AI, or Qualcomm Hexagon drivers.
3. Install the OEM driver even if Device Manager shows no error; OEM versions are tuned for your firmware.
4. Restart and verify in Task Manager > Performance that the NPU appears and shows activity.
5. If the NPU is missing from Device Manager entirely, our guide on neural processors missing from Device Manager covers the deeper fix.
6. Never rely solely on Windows Update for NPU drivers on brand-new platforms — OEM packages lead by months.

### Fix 5: Understand what "upgrade" can and cannot do
Many readers land here hoping to upgrade their current laptop into compliance.

1. RAM: upgradeable on many models — check your manual for SODIMM slots versus soldered RAM.
2. Storage: sometimes upgradeable, but soldered on thin-and-lights.
3. NPU: never upgradeable. It is part of the processor silicon. No upgrade, dock, or eGPU adds a qualifying NPU.
4. OS: Windows 10 machines can usually upgrade to Windows 11 for free if the CPU is supported.
5. Bottom line: if the NPU fails, the only path to Copilot+ is a new laptop. Our guide on [upgrading a laptop to a Copilot+ PC](/articles/upgrade-laptop-to-copilot-plus-pc/) is blunt about this.
6. If everything passes, enable the features and enjoy — and check [how much RAM an AI PC really needs](/articles/how-much-ram-for-ai-pc/) if you are deciding between 16 GB and 32 GB configurations.

## Closing

The Copilot+ requirements are refreshingly concrete: 40+ TOPS NPU, 16 GB RAM, 256 GB storage, Windows 11. No mystery, no fine print — just specs you can verify in ten minutes. If your laptop clears all four, the AI features are yours to use. If the NPU falls short, no settings change will bridge the gap, and knowing that saves you from chasing fixes for features your hardware was never meant to run.
