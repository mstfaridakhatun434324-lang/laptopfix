---
title: "How to Increase Virtual Memory on a Windows Laptop (Paging File Guide)"
slug: how-to-increase-virtual-memory-on-laptop
date: 2026-09-11
categories: ["performance"]
tags: ["virtual memory", "paging file", "ram", "windows 11", "pagefile.sys"]
description: "Running out of RAM? Increasing virtual memory (the paging file) gives your Windows laptop breathing room. Here's how to size and configure it correctly."
thumbnail: "/images/thumbs/how-to-increase-virtual-memory-on-laptop.webp"
faqs:
  - q: "What is virtual memory and how does it help?"
    a: "Virtual memory is disk space that Windows uses as an extension of RAM. When physical memory fills up, Windows moves less-used data to the paging file (pagefile.sys) on your drive, freeing RAM for active tasks. Increasing it prevents out-of-memory crashes and stuttering when you exceed your physical RAM, though it's slower than real RAM."
  - q: "How much virtual memory should I set?"
    a: "The classic guidance is 1.5 times your physical RAM for the maximum size, with the initial size equal to your RAM amount. For a laptop with 8GB of RAM, that means an initial size of 8192 MB and a maximum of 12288 MB. On modern systems with SSDs, letting Windows manage it automatically is often fine unless you're hitting memory limits."
  - q: "Does increasing virtual memory make my laptop faster?"
    a: "It doesn't make anything faster — it prevents slowdowns and crashes when RAM runs out. Virtual memory on an SSD is much slower than physical RAM, so it's a safety net, not a performance upgrade. If you constantly exceed your RAM, the real fix is adding more physical memory or reducing what's running."
  - q: "Should I disable the paging file if I have lots of RAM?"
    a: "No. Even with 16GB or 32GB of RAM, Windows and some applications expect a paging file to exist. Disabling it entirely can cause strange crashes and prevents proper crash dumps for troubleshooting. If you want to reduce it, set a small fixed size (like 2-4GB) rather than disabling it completely."
---

When your laptop has 8GB of RAM and you're running a browser with twenty tabs, a video call, and a couple of apps, something has to give. That something is virtual memory — disk space Windows uses as overflow when physical RAM fills up. Windows manages this automatically by default, and for most people the defaults are fine. But if you're hitting "your computer is low on memory" warnings, seeing constant disk thrashing, or running memory-hungry workloads on a laptop with limited RAM, manually tuning the paging file can make the difference between a usable machine and constant crashes.

Virtual memory isn't magic. Data in the paging file lives on your drive, which is orders of magnitude slower than RAM — even on a fast SSD. Increasing virtual memory won't make your laptop faster; it gives Windows more headroom before it starts refusing to open programs or killing processes. Think of it as widening the emergency lane, not adding horsepower. The real performance fix for chronic memory pressure is more physical RAM, but when that's not an option (soldered memory, budget constraints), a properly sized paging file is the next best thing.

This guide shows you how to check your current virtual memory, size it correctly for your system, and configure it manually — plus when to leave the automatic management alone.

## Why this happens

- **Physical RAM is fully used**: When RAM fills up, Windows must page data to disk. An undersized paging file means it runs out of overflow space too.
- **Automatic management set too small**: On systems with small SSDs, Windows sometimes sets a conservative paging file that doesn't cover peak usage.
- **Memory-hungry applications**: Browsers, video editors, virtual machines, and games can each consume gigabytes, quickly exceeding modest RAM.
- **Memory leaks**: A buggy app that never releases memory gradually fills both RAM and the paging file until the system chokes.
- **Paging file on a slow drive**: If the paging file sits on an old HDD instead of the SSD, every page fault is painfully slow.
- **Multiple paging files misconfigured**: Manually-set paging files on multiple drives with wrong sizes can confuse Windows' memory management.
- **Disabled paging file**: Some "optimization" guides wrongly advise disabling the paging file, which causes out-of-memory errors even with free RAM.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check your current memory and paging file usage

Before changing anything, confirm that virtual memory is actually your problem and see how Windows currently has it configured.

1. Open Task Manager (**Ctrl + Shift + Esc**) and go to the **Performance > Memory** tab.
2. Note your total RAM and how much is typically in use during your normal workload.
3. The **Committed** value shows RAM + paging file usage versus the total commit limit. If committed regularly approaches the limit, you need a bigger paging file.
4. To see the current paging file settings: press **Win + R**, type `sysdm.cpl`, press Enter, go to the **Advanced** tab, and click **Settings** under Performance, then the **Advanced** tab, then **Change** under Virtual memory.

If committed memory stays well under the limit and you're still slow, the problem is elsewhere — see our guide on [how to speed up a Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/).

### Fix 2: Calculate the right paging file size

Sizing matters. Too small and you still crash; excessively large wastes SSD space and can mask memory leaks.

1. Note your physical RAM in MB (8GB = 8192 MB, 16GB = 16384 MB).
2. Set the **Initial size** to 1x your RAM (8192 MB for 8GB).
3. Set the **Maximum size** to 1.5x–2x your RAM (12288–16384 MB for 8GB).
4. If you have 16GB+ of RAM and rarely max it out, a fixed 4096 MB paging file is plenty as a safety net.
5. For systems with very small SSDs, don't go below 2048 MB — Windows needs minimum headroom for stability.

### Fix 3: Set a custom paging file size

Now apply the numbers you calculated. This is the core procedure.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab, click **Settings** under Performance.
3. In Performance Options, go to the **Advanced** tab and click **Change** under Virtual memory.
4. Uncheck **Automatically manage paging file size for all drives**.
5. Select your system drive (usually C:), choose **Custom size**.
6. Enter your **Initial size** and **Maximum size** in MB, then click **Set**.
7. Click OK through all dialogs and **restart** your laptop — the change requires a reboot.

### Fix 4: Put the paging file on your fastest drive

If your laptop has both an SSD and an HDD, the paging file should live on the SSD. Paging to a spinning hard drive is dramatically slower and you'll feel every page fault.

1. Open the Virtual Memory settings as described in Fix 3.
2. Select the HDD drive, choose **No paging file**, and click **Set**.
3. Select the SSD drive, choose **Custom size** or **System managed size**, and click **Set**.
4. Restart your laptop.

If you only have one drive, skip this — Windows already has it in the only possible place.

### Fix 5: Reduce memory pressure instead of just adding paging space

A bigger paging file treats the symptom. Reducing actual memory consumption treats the cause, and your laptop will feel faster for it.

1. In Task Manager's **Processes** tab, sort by **Memory** to find the biggest consumers.
2. Close browser tabs you don't need — each one can use hundreds of MB. See our guide on [fixing Chrome high CPU and memory use](/articles/what-to-do-if-chrome-high-cpu-windows-11/).
3. Disable unnecessary startup apps in Task Manager's **Startup apps** tab.
4. Consider our broader cleanup guide: [how to disable background apps on a laptop](/articles/how-to-disable-background-apps-on-laptop/).

### Fix 6: Check for memory leaks

If memory usage climbs steadily over hours until the system crawls, a leaky app — not the paging file size — is the real problem.

1. Restart your laptop and note the **Committed** memory in Task Manager's Performance tab.
2. Use the laptop normally for a few hours without restarting.
3. If committed memory has grown enormously with the same apps open, sort Processes by Memory to find the growing process.
4. Update or replace the leaky application. Our guide on [fixing memory leaks in Windows 11](/articles/how-to-fix-memory-leak-windows-11-reddit/) covers this in depth.

### Fix 7: Consider a RAM upgrade

If you constantly exceed physical RAM despite cleanup, no paging file tuning will make the laptop feel fast. Check whether your model supports a memory upgrade.

1. Check your laptop's specs — many laptops have soldered RAM that can't be upgraded, but many still have an open SO-DIMM slot.
2. Use the [Intel driver and support assistant](https://www.intel.com/content/www/us/en/support/detect.html) or your manufacturer's tool to identify your chipset and model.
3. Check the manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), Lenovo) for the maximum supported memory and compatible modules.
4. A jump from 8GB to 16GB transforms everyday multitasking on most laptops.

## Closing

Increasing virtual memory is a legitimate fix for out-of-memory crashes and stuttering on RAM-limited laptops — set a sensible custom size, keep it on your fastest drive, and restart. But remember what it is: emergency overflow, not extra speed. If you're paging heavily every day, reducing memory waste and adding physical RAM will do far more for how your laptop feels.
