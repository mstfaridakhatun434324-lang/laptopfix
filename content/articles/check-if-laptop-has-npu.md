---
title: "How to Check If Your Laptop Has an NPU (Windows 11)"
slug: check-if-laptop-has-npu
date: 2026-10-19
categories: ["ai-pc"]
tags: ["check npu", "npu", "windows 11", "device manager", "task manager"]
description: "How to check if your laptop has an NPU? Four reliable ways to confirm AI hardware in Windows 11, from Task Manager to manufacturer specs."
thumbnail: "/images/thumbs/check-if-laptop-has-npu.webp"
faqs:
  - q: "Do all new laptops have an NPU?"
    a: "No. NPUs appear in Intel Core Ultra, AMD Ryzen AI, and Qualcomm Snapdragon X chips — roughly 2024 onward. Most budget laptops, older models, and many gaming laptops still lack one."
  - q: "Can I add an NPU to a laptop that doesn't have one?"
    a: "No. The NPU is integrated into the processor silicon; it cannot be added, upgraded, or installed separately. AI features on such machines run on CPU or GPU instead."
  - q: "Does having an NPU mean my laptop is a Copilot+ PC?"
    a: "Not necessarily. Copilot+ requires 40+ NPU TOPS plus 16GB RAM and 256GB storage. Many NPU-equipped laptops (like first-gen Core Ultra with 11 TOPS) fall short of the bar."
  - q: "Why does the store say 'AI laptop' but I find no NPU?"
    a: "Marketing stretches the term — some 'AI laptops' just run AI software on CPU/GPU. The methods in this guide verify actual NPU silicon rather than trusting the box."
---

"AI laptop" is printed on a lot of boxes that contain no AI chip at all. Before troubleshooting NPU problems — or feeling smug about Copilot+ features — verify the silicon is actually in your machine. Windows 11 gives you four reliable ways to check, from a ten-second glance to definitive proof.

If you have already confirmed an NPU and it is misbehaving, our [NPU detection troubleshooting](/articles/npu-not-detected-windows-11/) picks up where this guide ends.

## Why this happens

- **Marketing inflation:** "AI" branding appears on machines whose AI runs entirely on CPU.
- **No single Windows indicator:** Windows scatters NPU evidence across Task Manager, Device Manager, and Settings.
- **Processor name soup:** Intel, AMD, and Qualcomm naming makes it hard to tell which chips include NPUs.
- **Copilot+ vs NPU conflation:** Having an NPU and being a Copilot+ PC are related but different things.
- **OEM spec pages bury it:** NPU specs hide in footnotes or "AI performance" sections.

## How to fix it

Work through these in order — quickest first.

### Method 1: Task Manager (10 seconds)

The fastest visual check.

1. Press Ctrl + Shift + Esc.
2. Click the Performance tab.
3. Look for "NPU" in the left-hand list alongside CPU, Memory, Disk, GPU.
4. Present and active? You have a working NPU. Absent? Continue checking — it might be a driver issue rather than missing hardware.
5. Note: a missing entry here alone does not prove no NPU; confirm with Method 2.

### Method 2: Device Manager (definitive for Windows)

Windows' hardware inventory does not lie about what it sees.

1. Press Win + X, choose Device Manager.
2. Look for a "Neural processors" category — its presence confirms Windows sees NPU hardware with a driver.
3. Expand it: you should see Intel AI Boost, AMD NPU, or Qualcomm Hexagon entries.
4. No category? Check "Other devices" for unknown entries that might be a driverless NPU.
5. Still nothing? Move to Method 3 — the definitive hardware answer.

### Method 3: Identify your processor (definitive for silicon)

The chip model settles it regardless of software state.

1. Press Win + R, type `msinfo32`, Enter — read the Processor line exactly.
2. **Has NPU:** Intel Core Ultra (100/200 series), AMD Ryzen AI 300 / 8000 series, Qualcomm Snapdragon X Plus/Elite.
3. **No NPU:** Intel Core i3/i5/i7/i9 13th/14th gen and older, AMD Ryzen 7000/5000 series (non-AI), most Celeron/Pentium.
4. Search the exact model on the vendor's ARK/spec page — NPU TOPS is listed for equipped chips.
5. This method is immune to driver problems: if the chip qualifies, the NPU exists physically.

### Method 4: Manufacturer spec page (purchase verification)

For confirming before you buy — or settling arguments.

1. Find your exact model number (sticker on the bottom or `msinfo32`, System Model).
2. Open the maker's spec page and search for "NPU," "TOPS," "AI Boost," or "XDNA."
3. Look for a TOPS figure — its presence confirms an NPU; its absence strongly suggests none.
4. Cross-check with Method 3's chip identification — the two should agree.
5. For Copilot+ status specifically, see [how to check Copilot+ PC status](/articles/how-to-check-if-laptop-is-copilot-plus-pc/).

### When the checks disagree

Mixed signals have specific meanings — read them correctly.

1. **Chip qualifies but Task Manager/Device Manager show nothing:** Classic driver or BIOS issue. The NPU exists; Windows cannot see it. Work through [NPU detection fixes](/articles/npu-not-detected-windows-11/) — start with the BIOS toggle, then the OEM driver.
2. **Device Manager shows it, Task Manager does not:** Usually a Task Manager display glitch or a disabled device. Enable the device in Device Manager and restart Task Manager.
3. **Spec page claims NPU, chip lookup says otherwise:** Trust the chip lookup. Retailers and even some OEM pages copy marketing text across model variants sloppily.
4. **NPU appears after a Windows update:** The driver was missing, not the hardware — Windows finally fetched it. Confirm it stays across reboots before celebrating.

### What to do with the answer

Turn the verdict into action.

1. **NPU confirmed, working:** You are set — explore which [AI features](/articles/npu-not-used-by-apps-windows-11/) actually use it.
2. **NPU confirmed, not detected:** Driver or BIOS issue — our [detection fixes](/articles/npu-not-detected-windows-11/) apply.
3. **No NPU:** AI features run on CPU/GPU; do not chase NPU troubleshooting guides.
4. **No NPU but want Copilot+:** That requires new hardware — see whether [upgrading makes sense](/articles/upgrade-laptop-to-copilot-plus-pc/) for you.

## Closing

Four methods, one truth: Task Manager for speed, Device Manager for Windows' view, the processor model for silicon certainty, and the spec page for purchase proof. Most "missing NPU" mysteries dissolve at Method 3 — either the chip never had one, or it does and the problem is software. When it is software, the usual suspects are version mismatches like [24H2 driver incompatibility](/articles/npu-driver-incompatible-windows-11-24h2/) or a corrupted stack needing a [clean driver reinstall](/articles/reinstall-npu-driver-clean-install/). Knowing which saves hours of misdirected troubleshooting, and it is the required first step before attempting any driver or BIOS fix.
