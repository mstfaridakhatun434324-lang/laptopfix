---
title: "Can You Upgrade RAM on a Copilot+ PC? The Honest Answer"
slug: copilot-plus-pc-ram-upgrade-possible
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot+ pc", "ram upgrade", "memory", "hardware", "ai pc", "windows 11"]
description: "Wondering if you can add RAM to your Copilot+ PC? Learn which AI laptops have soldered memory, which are upgradeable, and what to buy instead if yours is not."
thumbnail: "/images/thumbs/copilot-plus-pc-ram-upgrade-possible.webp"
faqs:
  - q: "Can you upgrade RAM on a Copilot+ PC?"
    a: "On almost every Copilot+ PC, no. Snapdragon X, Intel Core Ultra, and AMD Ryzen AI laptops all use soldered LPDDR5X memory for speed and power efficiency. There are no SODIMM slots to fill. A small number of Intel and AMD AI laptops from Lenovo and others still use removable SODIMM or LPCAMM2 modules — check your specific model's service manual."
  - q: "Why is the RAM soldered on Copilot+ PCs?"
    a: "LPDDR5X memory is soldered close to the processor to reach very high bandwidth at low power, which AI workloads and the NPU depend on. Removable SODIMM slots are slower, bulkier, and use more energy, so ultra-thin AI laptops dropped them to hit the battery and performance targets Copilot+ requires."
  - q: "What can I do if my Copilot+ PC does not have enough RAM?"
    a: "You cannot add more, so optimize what you have: close background apps, disable unneeded startup programs, use browser tab sleeping, and keep virtual memory enabled. When buying your next AI PC, choose 32GB up front if you run VMs, large datasets, or heavy creative apps — 16GB is the practical floor."
  - q: "Is 16GB RAM enough for AI features on a Copilot+ PC?"
    a: "For Recall, Live Captions, Click to Do, and Studio Effects, yes — 16GB is the Copilot+ minimum and handles the built-in AI features fine. It gets tight with Chrome plus a VM plus Photoshop open at once. If the NPU is part of your workflow concern, also check our guide on the [NPU not being detected](/articles/npu-not-detected-windows-11/)."
---

You bought a Copilot+ PC with 16GB of RAM, opened Task Manager, and watched memory creep past 80% during normal work. Naturally you want to add more — but AI laptops play by different hardware rules than the upgradable machines of the past. This guide gives you the straight answer for every Copilot+ platform, plus what to do when the answer is no.

Here is the short version: nearly all Copilot+ PCs have soldered RAM that cannot be upgraded after purchase. Snapdragon X laptops, Surface devices, and most Intel Core Ultra and AMD Ryzen AI machines ship with LPDDR5X memory welded to the board. If storage is also on your mind, our [Copilot+ PC SSD upgrade guide](/articles/copilot-plus-pc-ssd-upgrade-guide/) covers which models let you expand the drive.

The longer version matters, because a few models break the rule — and knowing your options before you open the machine saves you from a wasted purchase.

## Why this happens

- **LPDDR5X is soldered by design:** The memory standard Copilot+ PCs use only exists in soldered packages; there is no removable LPDDR5X SODIMM.
- **Bandwidth and power targets:** Soldered memory sits millimeters from the CPU/NPU, enabling the bandwidth AI features need at a power budget removable slots cannot match.
- **Thinness goals:** Removing the SODIMM slot saves several millimeters of chassis height, a trade most ultraportable buyers accept.
- **No user-serviceable panel on most models:** Even where a service manual exists, opening the chassis on many AI laptops risks the warranty.
- **LPCAMM2 is the rare exception:** A few 2024-2025 Lenovo and ASUS AI laptops use removable LPCAMM2 modules — the only upgradeable path in this class.
- **Buyers underestimated AI memory use:** Recall snapshots and on-device models quietly raise baseline RAM usage, making 16GB feel tighter than on non-AI laptops.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Check for the rare removable-memory exception

Before assuming the worst, verify your exact model. A small number of AI laptops genuinely allow memory upgrades, and yours might be one of them.

1. Find your full model in Settings > System > About and search for its service manual.
2. Look for "LPCAMM2" or "SODIMM" in the memory section — those words mean a removable module.
3. Known exceptions include some Lenovo ThinkPad P1 / T-series AI models and a few ASUS ProArt machines.
4. If the manual says "soldered" or "onboard," stop here — no upgrade exists, and opening the machine risks the warranty for nothing.

### Fix 2: Trim startup programs to free real RAM

Every auto-starting app reserves memory before you do anything. Cutting the list is the fastest way to reclaim gigabytes on a fixed-memory machine.

1. Open Task Manager > Startup apps and sort by status.
2. Disable anything you do not need within the first minutes of a session (updaters, launchers, chat apps).
3. Restart and compare memory usage in Task Manager > Performance > Memory.
4. Keep a short list of what you disabled in case you miss one later.

### Fix 3: Tame the browser, the biggest RAM hog

Browsers are where most Copilot+ PC owners lose their memory. A few tab-management habits recover more RAM than any utility.

1. Turn on tab sleeping/freezing in Edge or Chrome settings so idle tabs release memory.
2. Install an extension that suspends inactive tabs if your browser lacks the feature natively.
3. Close tabs you are "saving for later" into a reading list or bookmarks instead.
4. If you run two browsers, consolidate to one — each adds hundreds of megabytes of overhead.

### Fix 4: Disable Recall if you do not use it

Recall's snapshot and indexing service consumes memory in the background. If you never search your timeline, that RAM is better spent on your actual work.

1. Go to Settings > Privacy & security > Recall & snapshots.
2. Turn off "Save snapshots" to stop the service from running.
3. Restart and check Task Manager for the freed memory.
4. Note that disabling Recall also helps boot time — see our [slow boot fix guide](/articles/copilot-plus-pc-slow-boot-fix/) for the full picture.

### Fix 5: Keep virtual memory enabled and healthy

With fixed physical RAM, Windows leans on the page file. Disabling it — a popular "tweak" — makes low-memory crashes more likely, not less.

1. Open System > About > Advanced system settings > Performance Settings > Advanced > Virtual memory.
2. Make sure it is set to "Automatically manage paging file size for all drives."
3. Keep at least 15-20% of your SSD free so the page file has room to breathe.
4. Do not follow guides that tell you to disable the page file on 16GB machines — that advice predates AI workloads.

### Fix 6: Plan the next purchase around memory

If you are constantly at 90%+ memory, the real fix is buying right next time. Memory pressure also stresses the NPU pipeline, so check that your AI hardware is healthy with our guide on the [NPU not being detected](/articles/npu-not-detected-windows-11/).

1. Honestly audit your workload: VMs, 4K editing, and large datasets need 32GB.
2. When shopping, treat 16GB as the floor and 32GB as the sweet spot for AI PCs.
3. Remember that storage is sometimes upgradeable even when RAM is not — our [SSD upgrade guide](/articles/copilot-plus-pc-ssd-upgrade-guide/) covers which models qualify. Microsoft documents memory requirements for AI features on the [Windows support hub](https://support.microsoft.com/en-us/windows).
4. Sell or trade the current machine while it still holds value rather than suffering for two more years.

## Closing

For nearly every Copilot+ PC, the RAM you bought is the RAM you keep — soldered LPDDR5X is the price of thin, efficient AI laptops. That is not the end of the story: trimming startup apps, taming the browser, disabling unused Recall, and keeping virtual memory healthy can recover several gigabytes of headroom. And the next time you buy, choose 32GB up front — on an AI PC, memory is a purchase-time decision, not an upgrade. Printer setup is another frequent ARM-laptop headache — see our [Epson printer guide for ARM laptops](/articles/epson-printer-arm-laptop/).
