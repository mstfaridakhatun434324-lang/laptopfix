---
title: "FAULTY_HARDWARE_CORRUPTED_PAGE: A Step-by-Step Fix Guide"
slug: how-to-fix-faulty-hardware-corrupted-page-step-by-step
date: 2026-09-22
categories: ["windows-errors"]
tags: ["bsod", "stop code", "ram", "hardware"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE blue screen? It's usually failing RAM or a bad driver. Follow this step-by-step guide to test, fix, and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-faulty-hardware-corrupted-page-step-by-step.webp"
faqs:
  - q: "Does FAULTY_HARDWARE_CORRUPTED_PAGE always mean my RAM is broken?"
    a: "Not always, but it's the most common cause. Windows detects that a memory page was corrupted and the pattern usually points to failing RAM. However, a buggy driver writing outside its memory bounds produces the identical crash. Test the memory properly and check drivers before buying replacement RAM."
  - q: "How long does it take to fix this error?"
    a: "Software-side fixes take about 30 to 60 minutes. The definitive memory test (MemTest86) runs overnight — plan for 4 to 8 hours. If the RAM is genuinely bad and your laptop has removable sticks, swapping them takes about 15 minutes once you have the replacements."
  - q: "Can overheating cause this blue screen?"
    a: "Yes. Heat-induced bit errors in RAM become more likely when the memory runs hot for long periods, especially during gaming or heavy workloads. If crashes cluster during intensive use, improving cooling and cleaning dust from vents is a legitimate part of the fix."
  - q: "Will fixing this delete any of my files?"
    a: "No. Memory tests, driver updates, and system file repairs don't touch your personal files. Replacing RAM doesn't affect your SSD at all. Still, keep a current backup — a laptop with flaky memory can corrupt files while it crashes, so backing up first is smart."
---

When Windows throws the `FAULTY_HARDWARE_CORRUPTED_PAGE` blue screen, the name tells you the story: the operating system detected that a page of memory it was actively using had been corrupted, and the pattern looks like a hardware problem. In practice this stop code comes down to failing RAM more often than anything else — but a misbehaving driver can corrupt memory pages the exact same way, and Windows can't always tell the difference.

The tricky part is separating those two causes without spending money on the wrong one. This guide walks you through that in the sensible order: quick software checks first, then a definitive memory test, then what to actually do if your RAM turns out to be the problem.

## Why this happens

- **Failing or degrading RAM**: The most common cause. Individual memory cells go bad over time and flip bits in the pages Windows is using. Windows checksums critical pages, spots the mismatch, and crashes rather than continue with corrupted data.
- **A buggy driver writing out of bounds**: A driver bug can scribble over memory pages that belong to the OS or another driver. The corruption pattern looks exactly like hardware failure, so Windows reports it the same way.
- **Overclocked or unstable memory**: Aggressive XMP/EXPO profiles or manual memory overclocks that were "stable enough" produce intermittent corruption under load — exactly the signature of this stop code.
- **Heat-induced bit errors**: RAM running hot for long stretches (gaming, rendering, poorly ventilated lap use) starts producing errors. Dust-clogged vents make a marginal memory module fail much sooner.
- **Corrupted page file on failing storage**: If Windows' page file sits on bad SSD sectors, pages swapped out to disk come back corrupted. The symptom is a "hardware corrupted page" crash even though the RAM itself is fine.
- **A recent update changed the timing**: A Windows or driver update can alter memory management just enough that a borderline module — one that was quietly producing rare, unnoticed errors — starts tripping the checksum often enough to crash.

## How to fix it

Work through these in order — each step rules out a cause before you spend money on anything.

### Fix 1: Check whether a recent update or driver is the trigger

If the crashes started right after something changed, that something is suspect number one.

1. Open **Settings** > **Windows Update** > **Update history** and look at what's installed in the last two weeks. Note any driver updates.
2. Press **Win + X** and open **Device Manager**. Expand **Display adapters**, **Memory technology devices**, and **IDE ATA/ATAPI controllers** — look for yellow warning icons.
3. If a driver was updated within a day or two of the first crash, right-click the device > **Properties** > **Driver** tab > **Roll Back Driver**.
4. If a Windows update is the suspect, **Settings** > **Windows Update** > **Update history** > **Uninstall updates** lets you remove the most recent one as a test.

### Fix 2: Run Windows Memory Diagnostic

The quick built-in test. It won't catch everything, but it catches obvious failures fast.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The laptop reboots into the memory test automatically.
3. Let both passes complete — don't interrupt it. This takes 10–30 minutes.
4. When Windows boots back, check the result: **Event Viewer** > **Windows Logs** > **System**, filter for source `MemoryDiagnostics-Results`. Any reported error, even one, means the RAM has bad cells.

### Fix 3: Run MemTest86 overnight for a definitive answer

Windows' built-in test is decent; MemTest86 is conclusive. Run this before buying anything.

1. Download MemTest86 (free edition) on a working computer and create a bootable USB with its included tool.
2. Boot your laptop from the USB (usually **F12** or **Esc** at power-on for the boot menu).
3. Let it run at least 4 full passes — typically 4 to 8 hours overnight.
4. Zero errors after 4+ passes means your RAM is almost certainly fine; focus on drivers instead. Any error means the RAM is bad, full stop.

If your crashes happen at startup rather than mid-session, the general [blue screen of death guide for Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers boot-time triage in more detail.

### Fix 4: Reseat the RAM and test sticks one at a time

Loose or oxidized contacts cause exactly this kind of intermittent corruption, and testing sticks individually identifies which one is bad.

1. Shut down, unplug everything, and remove the bottom panel (check your model's manual for the correct screw order).
2. Release the RAM retention clips, remove each stick, and blow out the slots with compressed air.
3. Reseat one stick firmly until both clips click. Boot and use the laptop normally for a day.
4. If it still crashes, swap in the other stick alone. The one that crashes is the bad one.
5. If your laptop has soldered RAM (many ultrabooks do), you can't do this step — skip to Fix 6 and plan for professional service.

### Fix 5: Reset memory to stock speeds in BIOS

An unstable XMP profile is a classic cause of intermittent page corruption.

1. Restart and enter BIOS/UEFI (usually **F2** or **Del** on the manufacturer's splash screen).
2. Find the memory settings — often under **Advanced** > **Memory** or **Ai Tweaker**/**Overclocking**.
3. Disable **XMP**/**EXPO**/**DOCP** or set memory to **Auto**/stock speed.
4. Save and exit (**F10**). Use the laptop for a few days at stock speeds; if the crashes stop, the XMP profile was too aggressive for your modules.

### Fix 6: Update chipset and storage drivers from the manufacturer

Outdated chipset or storage-controller drivers can mishandle memory pages, and the generic Windows ones are often the culprits.

1. Identify your platform: Intel users can run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect and update chipset, graphics, and Wi-Fi drivers automatically.
2. For AMD laptops, grab the chipset and storage drivers from [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html).
3. Also update your SSD firmware — check your laptop maker's support site for a storage firmware utility. A drive with a known firmware bug can corrupt the page file exactly the way this stop code describes.
4. Restart and monitor for a few days of normal use.

### Fix 7: Repair Windows' own memory-management files

Corrupted kernel components can misdetect or mishandle memory pages, producing false "hardware" crashes.

1. Open an elevated Command Prompt: **Win + X** > **Terminal (Admin)**.
2. Run `sfc /scannow` and let it finish — it repairs protected system files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store `sfc` draws from.
4. Restart. If crashes persist after clean memory tests and updated drivers, the pattern strongly suggests genuine hardware failure.

A closely related memory crash with a driver flavor is [DRIVER_IRQL_NOT_LESS_OR_EQUAL](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/) — worth reading if your crashes involve driver names on the blue screen. There's also a [24H2-specific walkthrough for this exact stop code](/articles/how-to-fix-faulty-hardware-corrupted-page-in-windows-11-24h2/) if you recently updated to that build.

## Closing

`FAULTY_HARDWARE_CORRUPTED_PAGE` sounds alarming, but the diagnostic path is straightforward: rule out software triggers, test the memory definitively, and only then spend money. Most people who work through these steps find the answer by Fix 3 or Fix 6 — either a bad stick they can replace for the cost of a RAM module, or a driver update that ends the crashes entirely. If MemTest86 comes back clean and drivers are current, the next stop is a warranty claim, because at that point the fault is real hardware somewhere on the board.
