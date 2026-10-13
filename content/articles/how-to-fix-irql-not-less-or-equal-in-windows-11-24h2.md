---
title: "How to Fix the IRQL Not Less or Equal Error in Windows 11 24H2"
slug: how-to-fix-irql-not-less-or-equal-in-windows-11-24h2
date: 2026-09-30
categories: ["windows-errors"]
tags: ["irql-not-less-or-equal", "windows-11-24h2", "blue-screen"]
description: "IRQL Not Less or Equal crashing Windows 11 24H2? Find the driver accessing memory illegally and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-irql-not-less-or-equal-in-windows-11-24h2.webp"
faqs:
  - q: "What does IRQL Not Less or Equal mean in simple terms?"
    a: "A driver tried to access a memory address it wasn't allowed to touch at its current priority level (IRQL). Think of it as a driver reaching into memory reserved for more critical operations. Windows catches the violation and crashes. It's one of the most common blue screens and is driver-caused the vast majority of the time."
  - q: "Why is this error so common after the 24H2 update?"
    a: "24H2 tightened memory-access enforcement and updated core driver stacks. Drivers that bent the rules on earlier Windows 11 builds — especially older network, audio, and peripheral drivers — now trip the check reliably. Updating those drivers to 24H2-compatible versions is the fix."
  - q: "Can RAM cause IRQL Not Less or Equal?"
    a: "Yes, though drivers are more common. Faulty RAM corrupts the addresses drivers try to use, producing this stop code with no single driver to blame. If your dumps name different drivers on each crash, or crashes happen at idle with no pattern, test the memory — that's the signature of a hardware cause."
  - q: "The crash names ndis.sys. What does that mean?"
    a: "Ndis.sys is Windows' network driver interface — the crash was detected there, but the actual culprit is almost always your Wi-Fi or Ethernet driver calling into it incorrectly. Update your network adapter driver from Intel, Realtek, or your laptop maker's site rather than trying to fix ndis.sys itself."
---
IRQL Not Less or Equal (0xA) is the blue screen most Windows users meet eventually. In plain terms: a driver tried to touch memory it had no business touching, and Windows stopped the system rather than let the corruption spread. On Windows 11 24H2 it's surged because the update enforces memory-access rules more strictly — drivers that got away with sloppy access before now crash reliably.

The good news is the pattern is well understood: it's a driver problem until proven otherwise, and the crash dump usually names the offender. That "until proven otherwise" matters — the RAM test in Fix 5 exists because hardware causes produce this exact stop code too, and you don't want to spend days updating drivers when a memory stick is the real problem.

Work through the steps below. For the driver-specific variant see [Driver IRQL Not Less or Equal in Windows 11 24H2](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/), and for the general fix there's [IRQL Not Less or Equal on Windows 11](/articles/how-to-fix-driver-irql-not-less-or-equal-on-windows-11/).

## Why this happens

- **Incompatible or buggy driver.** Network, audio, graphics, and USB drivers are the most frequent offenders on 24H2.
- **Driver not updated for 24H2.** Older drivers that worked on 23H2 violate the stricter 24H2 memory rules.
- **Faulty RAM.** Corrupts addresses drivers use, producing crashes with no consistent driver.
- **Corrupted system files.** Damaged Windows components mishandle driver memory requests.
- **Overclocking instability.** Unstable CPU/RAM overclocks cause drivers to misbehave at high IRQL.
- **Conflicting drivers.** Two drivers managing the same device corrupt each other's memory access.

## How to fix it

Work through these in order — the dump names the driver, you fix the driver.

### Fix 1: Identify the driver from the crash dump

Start with evidence, not guesses.

1. Verify dumps: **Win + R** > `sysdm.cpl` > **Advanced** > **Startup and Recovery Settings** > **Small memory dump** selected.
2. After the next crash, grab the newest `.dmp` from `C:\Windows\Minidump`.
3. Open it in **WinDbg Preview** (Microsoft Store, free) and run `!analyze -v`.
4. Note **IMAGE_NAME**. Common readings: `Netwtw10.sys`/`rtwlanu.sys` (Wi-Fi — update network driver), `nvlddmkm.sys` (NVIDIA graphics), `ndis.sys` (network stack — update the underlying adapter driver).
5. If every dump names something different, skip to the RAM test (Fix 5) — that's the hardware signature.

### Fix 2: Update the named driver

Replace the specific offender. A clean uninstall-then-reinstall beats an in-place update here, because it removes corrupted driver binaries that an update would otherwise leave in place.

1. Download the newest driver from the vendor: [Intel](https://www.intel.com/content/www/us/en/support/detect.html) for Wi-Fi/Bluetooth/chipset, [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) for graphics, or your laptop maker's support page.
2. In **Device Manager**, right-click the device, choose **Uninstall device**, tick **Attempt to remove the driver for this device**, and restart.
3. Install the downloaded driver fresh.
4. Test under the conditions that crashed before — gaming, video calls, large downloads.

### Fix 3: Update the other common offenders

If the dump was unclear, update the usual suspects one at a time. Patience here pays off — each update either fixes the crashes or eliminates a suspect, and either outcome moves you forward.

1. **Network adapters** — Wi-Fi first, then Ethernet. These cause more IRQL crashes than any other category on laptops.
2. **Sound, video and game controllers** — audio drivers are a perennial IRQL trigger.
3. **Display adapters** — graphics drivers next.
4. Restart and test between each so you know which one fixed it.

### Fix 4: Roll back a recent driver update

When the timeline implicates an update, reverse it.

1. In **Device Manager**, open the suspect device's **Properties > Driver** tab.
2. Click **Roll Back Driver**, choose a reason, and confirm.
3. Restart and verify stability.
4. To stop Windows Update reinstalling it immediately: **Settings > Windows Update > Advanced options > Optional updates** — don't install the driver version offered there.

### Fix 5: Test your RAM

For inconsistent dumps or random idle crashes. When every crash names a different driver, no single driver is guilty — something is corrupting memory underneath all of them, and that something is usually RAM.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, choose **Restart now and check for problems**.
2. Press **F1** during the test for **Extended** mode with multiple passes.
3. Test sticks individually if errors appear. Replace the faulty one.
4. Mismatched RAM (different brands or speeds) is a standalone cause — a matched kit is the fix.

### Fix 6: Run SFC and DISM

Repair the Windows components drivers interact with.

1. Right-click **Start > Terminal (Admin)**.
2. Run: `sfc /scannow`
3. Then: `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart and retest.

### Fix 7: Disable overclocking and XMP

Remove instability from the equation.

1. Enter BIOS/UEFI setup at boot (**F2**/**Del**).
2. Disable **XMP / EXPO** memory profiles and reset any CPU or GPU overclocks to stock.
3. Save (**F10**), exit, and test for a few days at stock settings.
4. Gaming laptops with factory "turbo" modes: test with those disabled too.

### Fix 8: Check for Windows updates and known issues

Microsoft ships driver-compatibility fixes through Windows Update.

1. Go to **Settings > Windows Update** and install everything pending, then restart.
2. Check Microsoft's Windows support hub for documented 24H2 known issues matching your stop code.
3. If a specific update caused the crashes, you can uninstall it from **Settings > Windows Update > Update history > Uninstall updates** as a temporary measure.

## Closing

IRQL Not Less or Equal on 24H2 is overwhelmingly a driver-compatibility story: the update raised the bar, and older drivers trip over it. Read the dump, update the named driver to a 24H2-ready version, and test the RAM if the dumps won't settle on a single culprit. One driver at a time, verified with real use — that's the whole method, and it works because it treats the crash as evidence instead of a mystery.
