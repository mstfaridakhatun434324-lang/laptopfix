---
title: "KERNEL_SECURITY_CHECK_FAILURE: What to Do When You See It"
slug: what-to-do-if-kernel-security-check-failure
date: 2026-10-02
categories: ["windows-errors"]
tags: ["kernel-security-check-failure", "bsod", "stop-code"]
description: "KERNEL_SECURITY_CHECK_FAILURE means a driver corrupted kernel data structures. Here is exactly what to do, in the order a technician would do it."
thumbnail: "/images/thumbs/what-to-do-if-kernel-security-check-failure.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE actually mean?"
    a: "Stop code 0x139 fires when Windows detects corruption in a kernel data structure — typically a linked list a driver was manipulating. Windows deliberately crashes to stop the corruption from spreading. The named file on the screen, if any, is usually the driver that was active when the corruption was discovered, not necessarily the one that caused it."
  - q: "Can RAM cause KERNEL_SECURITY_CHECK_FAILURE?"
    a: "Yes, and it is one of the top causes. Bad memory corrupts the kernel structures Windows is checking, producing exactly this stop code. If your crashes name different drivers each time or happen at random, test the RAM before chasing drivers — a memory test takes 30 minutes and settles the question."
  - q: "Is this error caused by a virus?"
    a: "Rarely, but rootkits do tamper with kernel structures, so it is worth one full scan. In practice, third-party drivers — especially antivirus filter drivers, VPN clients, and overclocking utilities — are far more common causes than malware. Scan once, then focus on drivers."
  - q: "Will updating Windows fix KERNEL_SECURITY_CHECK_FAILURE?"
    a: "Sometimes. Microsoft ships driver-compatibility fixes and kernel hardening in cumulative updates, and an update can resolve a known conflict. But if a specific third-party driver is corrupting structures, no Windows update will fix it — you have to identify and update or remove that driver."
---
KERNEL_SECURITY_CHECK_FAILURE sounds like a security incident, but it is really Windows catching a driver misbehaving. The kernel keeps internal lists and structures, and when it finds one corrupted, it pulls the emergency brake — the blue screen — rather than let the corruption spread. The 'security' in the name refers to the kernel verifying the integrity of its own data, not to antivirus or hacking — although the name understandably sends people down the wrong path at first.

The fix is detective work, not guesswork. The steps below isolate whether it is RAM, a specific driver, or system corruption, and they are ordered so the most likely causes get checked first. You will need about an hour, an administrator account, and ideally the ability to read a minidump — though the steps explain that part as you go, no prior debugging experience required.

## Why this happens

- **A third-party driver corrupting kernel lists.** Antivirus filters, VPN clients, and RGB/overclocking tools are repeat offenders.
- **Faulty RAM.** Bad memory flips bits in kernel structures, triggering the check randomly with different drivers named each time.
- **Corrupted system files.** Damage to Windows' own kernel components makes legitimate operations trip the security check.
- **Overclocked CPU or RAM.** Unstable overclocks corrupt data in transit, and the kernel's integrity checks catch it.
- **A failing storage drive.** Corrupted pages read from a dying drive poison the kernel structures built from them.
- **Incompatible driver after a Windows update.** Feature updates change kernel internals, and an old driver that manipulated them can start corrupting structures.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Run a full memory test first

Because bad RAM mimics every other cause of this error, testing it first saves hours of driver chasing. This matters more than usual for 0x139 because the error is literally a corruption check — bad RAM fails it directly, while every driver-focused step afterward assumes the RAM is good.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Select **Restart now and check for problems** and let the test run.
3. If it finds hardware problems, reseat your RAM sticks (or have a shop do it on a sealed laptop) and retest.
4. If crashes name a different driver every time and the quick test passes, run MemTest86 overnight — the built-in test misses marginal sticks. Our [memory management fix guide](/articles/memory-management-bsod-windows-11-fix/) covers deeper RAM diagnosis.

### Fix 2: Identify the crashing driver from the minidump

Windows saves a crash dump every time. Reading it names the suspect instead of guessing. Two dumps that agree give you a suspect worth acting on; a single dump is only a hint, since the driver present at discovery is often innocent.

1. Open **File Explorer** and go to `C:\Windows\Minidump`.
2. Note the newest `.dmp` file's date matches your crash.
3. Install WinDbg Preview from the Microsoft Store, open the dump, and run `!analyze -v` in the command box.
4. Look for the MODULE_NAME and IMAGE_NAME lines — that is your suspect driver. Search its filename online to identify the product it belongs to.

### Fix 3: Update or remove the suspect driver

Once you have a name, act on it directly. Change only the suspect driver between tests — if you update five drivers at once and the crashes stop, you will never know which one was guilty.

1. In **Device Manager** (**Win + X > Device Manager**), locate the device tied to the driver.
2. Right-click and choose **Update driver > Search automatically for drivers**.
3. If it is already current, visit the manufacturer's site for a newer version — or roll back via **Properties > Driver > Roll Back Driver** if the trouble started after an update.
4. For antivirus or VPN filter drivers, try a clean reinstall of that product, or temporarily uninstall it to test. Details on reading these screens are in our [blue screen of death walkthrough](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 4: Scan for malware once

Rule out the scary cause quickly so you can focus on drivers. Rootkits are the one malware class that genuinely causes this stop code, and only an offline scan reliably catches them, since they hide from scanners running inside the infected Windows.

1. Open **Windows Security** from the Start menu.
2. Go to **Virus & threat protection > Scan options** and run a **Full scan**.
3. If it finds and removes something, restart and monitor for a day — rootkits that hook the kernel can cause exactly this stop code.

### Fix 5: Repair system files

Corruption in Windows' own kernel files produces this error from perfectly innocent drivers. Run these even when a driver looks guilty — corrupted system files and a bad driver often arrive together via the same bad update, and fixing only one leaves the other.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` and wait for completion.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and use the machine normally — this pair fixes a surprising number of 0x139 crashes.

### Fix 6: Reset any overclocking to stock

Unstable overclocks corrupt kernel data in ways that look exactly like a bad driver. Memory overclocks deserve special attention here: XMP instability corrupts kernel lists in exactly the pattern 0x139 detects, so test at stock speeds, not just defaults that quietly re-enable XMP.

1. Enter your BIOS/UEFI (usually **F2** or **Del** during boot) and load optimized defaults.
2. In Windows, disable any overclocking or tuning utilities (Afterburner, Ryzen Master, Intel XTU, motherboard apps).
3. If you enabled XMP/EXPO for RAM, try disabling it temporarily to test stability at stock speeds.

### Fix 7: Check the drive's health

A dying SSD or HDD feeding corrupted data into the kernel is the last hardware suspect. When the drive is the cause, the corruption pattern looks random — different drivers named, crashes during disk-heavy work — which is why this check comes after the RAM test rather than before it.

1. Open an elevated **Command Prompt** and run `chkdsk C: /f`.
2. Check SMART data with your drive maker's tool or `wmic diskdrive get status` — anything other than OK means replace the drive.
3. If the drive is healthy and crashes persist after all the above, an in-place Windows repair (download from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and choose **Keep personal files and apps**) is the final step.

## Closing

KERNEL_SECURITY_CHECK_FAILURE is Windows doing its job — catching corruption before it snowballs. Your job is to find what is corrupting things, and nine times out of ten it is either bad RAM or one misbehaving third-party driver. The memory test and the minidump will tell you which within the hour. Keep the minidumps from your crashes even after fixing it — if the error ever returns, comparing old and new dumps tells you immediately whether it is the same cause or something new.
