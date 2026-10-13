---
title: "How to Fix Faulty Hardware Corrupted Page on an HP Laptop"
slug: how-to-fix-faulty-hardware-corrupted-page-on-hp-laptop
date: 2026-09-16
categories: ["windows-errors"]
tags: ["bsod", "hp", "hardware", "memory"]
description: "Fix FAULTY_HARDWARE_CORRUPTED_PAGE blue screens on HP laptops with HP diagnostics, driver updates, and definitive memory testing."
thumbnail: "/images/thumbs/how-to-fix-faulty-hardware-corrupted-page-on-hp-laptop.webp"
faqs:
  - q: "What does Faulty Hardware Corrupted Page mean on an HP laptop?"
    a: "Windows detected corruption in a memory page that looked like a hardware fault and halted. The name is Windows' first guess, not a diagnosis: drivers cause this exact stop code frequently on HP machines, especially after updates. Treat it as a lead to investigate, starting with the free software checks before assuming hardware failure."
  - q: "Does HP have a built-in diagnostic for this?"
    a: "Yes. HP laptops include UEFI hardware diagnostics: press Esc during boot, then F2 for System Diagnostics, and run the memory and hard drive tests. These are vendor-tuned for your exact hardware and are the best first hardware check on an HP machine before trying third-party tools."
  - q: "Can a Windows update cause this on HP laptops?"
    a: "Yes. HP's support forums regularly see clusters of this error after Windows feature updates install incompatible storage or chipset drivers. If your crashes started within days of an update, update the HP drivers from HP's support site or roll the update back to confirm."
  - q: "Is my data at risk when this BSOD appears?"
    a: "Your files are almost certainly intact; the crash halts the system to prevent corruption, not because corruption already happened. Still, repeated crashes are a warning sign, so back up important data while troubleshooting, especially if diagnostics later point at the drive or RAM."
---

FAULTY_HARDWARE_CORRUPTED_PAGE on an HP laptop is the blue screen that sends people shopping for new RAM before they have run a single test. Slow down. The stop code means Windows found a corrupted memory page that smelled like hardware failure, but drivers produce this identical error all the time, and HP machines have excellent built-in diagnostics to sort hardware from software quickly.

This guide is tailored to HP laptops: it uses HP's own tools where they help, covers the driver patterns HP users hit most, and ends with the definitive memory tests. Work through it in order, and do not skip the built-in diagnostics; they are faster and more accurate for HP hardware than any generic tool.

## Why this happens

- **A driver corrupts a memory page.** Buggy storage, chipset, or graphics drivers are frequent causes despite the error's name.
- **Failing RAM.** Genuinely bad memory is the leading true-hardware cause.
- **Driver mismatch after a Windows update.** New kernel, old HP driver, corrupted pages.
- **Failing hard drive or SSD.** Disk errors during paging corrupt memory pages backed by the page file.
- **Overheating.** Thermal stress on the memory controller causes transient corruption.
- **Corrupted system files.** Damaged kernel memory management produces the same symptoms.
- **Unstable BIOS memory settings.** Rare on HP, but possible after manual changes.

## How to fix it

Work through these in order, testing for stability after each fix before moving on.

### Fix 1: Run HP's built-in hardware diagnostics

Use the vendor-tuned tests first.

1. Shut down the laptop completely.
2. Power on and immediately press **Esc** repeatedly, then press **F2** for System Diagnostics.
3. Run the **Memory Test** (choose the extensive option if offered).
4. Run the **Hard Drive Test** as well.
5. If either fails, note the failure ID; HP support uses it for warranty claims, and you have your hardware answer. Take a photo of the screen showing the failure ID so you have it when contacting support.

### Fix 2: Update HP drivers from HP's site

Replace the drivers most likely to corrupt pages.

1. Visit [HP Support](https://support.hp.com/us-en) and enter your product name or serial number.
2. Download the latest **chipset**, **storage**, **graphics**, and **BIOS** drivers for your model.
3. Install chipset first, then storage, then graphics, restarting between each.
4. Avoid third-party driver updaters; HP's drivers are tested against your exact hardware. These tools are a common source of the mismatched drivers that cause this exact blue screen.
5. Test for a day of normal use, including the activities that previously triggered crashes. If the crashes were random with no pattern, a full day of mixed use is the minimum meaningful test.

### Fix 3: Run Windows Memory Diagnostic

A second opinion on the RAM, from inside Windows.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Press **F1** and select **Extended**, then run at least two passes.
4. If HP's test passed but this reports errors, trust the error and investigate the RAM.
5. If both pass, memory is likely fine and the cause is software.

### Fix 4: Roll back the recent Windows update

Confirm or clear the update's role.

1. Open **Settings** then **Windows Update** then **Update history**.
2. Click **Uninstall updates** and remove the most recent update.
3. Restart and test for several days.
4. If stability returns, update HP drivers fully before reinstalling the update.
5. Pause updates briefly from **Advanced options** while you sort the drivers.

### Fix 5: Check the drive and repair system files

Rule out disk-sourced corruption.

1. Open **Terminal (Admin)** with **Win + X**.
2. Run `chkdsk C: /f /r` and let it complete.
3. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth` if needed.
4. Run `sfc /scannow` once more to confirm.
5. Restart and monitor.

### Fix 6: Reset BIOS to defaults

Clear any unstable firmware settings.

1. Restart and press **F10** to enter BIOS setup on most HP laptops.
2. Load **Setup Defaults** or **Optimized Defaults**.
3. Save and exit.
4. Retest under normal workloads.

### Fix 7: Run MemTest86 for the final word on RAM

When HP's test and Windows' test disagree or crashes persist, this settles it.

1. Create a MemTest86 bootable USB on another PC.
2. Boot the HP laptop from it (use **Esc** then **F9** for the boot menu).
3. Run at least four full passes, ideally overnight.
4. Any error means a bad stick; test sticks individually if you have two.
5. Replace the faulty module with matching specs, or use HP warranty with the failure details. Keep the receipt and note the installation date in case the replacement also fails early.

### Fix 8: Clean-install Windows if hardware tests pass

When every test says the hardware is fine, the installation is the problem.

1. Back up all data.
2. Create installation media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Clean-install, then add only HP vendor drivers, testing stability as you go.
4. If the error survives a clean install with passing hardware tests, escalate to HP support with your diagnostic results. Bring the failure IDs and MemTest86 logs; they dramatically speed up a warranty claim.

For the Windows 10 version of this error, see [faulty hardware corrupted page on Windows 10](/articles/how-to-fix-faulty-hardware-corrupted-page-on-windows-10/), and for the related memory stop code, read [memory management BSOD on Windows 11](/articles/memory-management-bsod-windows-11-fix/).

## Closing

On HP laptops you have an advantage most brands do not: genuinely good built-in diagnostics a keypress away. Run them first, update the HP drivers second, and let MemTest86 deliver the final verdict on RAM only if the easier answers fail. FAULTY_HARDWARE_CORRUPTED_PAGE is a question, not a sentence, and this order answers it with the least wasted money and time. Keep the HP PC Hardware Diagnostics tool installed afterward; it is useful for any future hardware suspicion, not just this error.
