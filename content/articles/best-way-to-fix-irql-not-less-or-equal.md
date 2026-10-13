---
title: "The Best Way to Fix IRQL_NOT_LESS_OR_EQUAL on Windows 11"
slug: best-way-to-fix-irql-not-less-or-equal
date: 2026-09-08
categories: ["windows-errors"]
tags: ["irql not less or equal", "bsod fix", "driver update", "windows 11", "stop code 0x0a"]
description: "The most reliable way to fix IRQL_NOT_LESS_OR_EQUAL on Windows 11: identify the driver, update the right stack, and verify with dumps."
thumbnail: "/images/thumbs/best-way-to-fix-irql-not-less-or-equal.webp"
faqs:
  - q: "What is the fastest fix for IRQL_NOT_LESS_OR_EQUAL?"
    a: "Update the driver named on the blue screen — on laptops that is the Wi-Fi driver more often than anything else. Download it from your laptop maker's support page, uninstall the old driver completely, install the fresh one, and restart. That single targeted update resolves the majority of 0x0A crashes without touching anything else."
  - q: "Should I use Driver Verifier for IRQL_NOT_LESS_OR_EQUAL?"
    a: "Only if the basic fixes fail. Driver Verifier stresses drivers until the buggy one crashes with its name attached, which is definitive — but it makes the system deliberately unstable during testing. Create a restore point first, verify only non-Microsoft drivers, and run verifier /reset in Safe Mode when done."
  - q: "Can I fix IRQL_NOT_LESS_OR_EQUAL without Safe Mode?"
    a: "Usually yes. Driver updates, rollbacks, SFC scans, and memory diagnostics all run fine in normal Windows. You only need Safe Mode if crashes are so frequent you cannot stay booted long enough to work, or to reset Driver Verifier after it does its job."
  - q: "Why does the blamed driver keep changing?"
    a: "When each crash names a different .sys file, the real culprit is usually faulty RAM corrupting whatever driver happens to be active, or occasionally an unstable overclock. Stop chasing drivers and test your memory — inconsistent blame is the classic signature of a hardware problem underneath."
---

IRQL_NOT_LESS_OR_EQUAL (0x0A) is the blue screen Windows users meet most often, and the "best way" to fix it is less about any single trick than about refusing to guess. The stop screen usually hands you the answer — a `.sys` filename in parentheses — and the reliable repair is a short, ordered procedure: identify that driver, determine whether to update or roll it back, verify the fix with the actual crash dumps, and only then widen the search to memory and system files. Shotgun driver reinstalls and registry cleaners just add noise.

This guide is the distilled version of that procedure — the order a technician uses when the goal is fixing it once, correctly, instead of fixing it five times. If you haven't read the broader diagnosis yet, our [IRQL_NOT_LESS_OR_EQUAL troubleshooting guide](/articles/irql-not-less-or-equal-troubleshooting/) covers the full background.

## Why this happens

- **A single buggy driver.** Most 0x0A crashes trace to one driver violating interrupt-level memory rules — the file named on the stop screen.
- **Wi-Fi driver bugs.** On laptops, wireless drivers (Intel, Realtek, MediaTek) are the top offender by a wide margin.
- **A driver update gone wrong.** New driver revisions occasionally ship with IRQL bugs; the crash starts the day after the update.
- **Windows update changing the rules.** A new kernel build can expose bugs in older drivers that previously got away with violations.
- **Faulty RAM.** Corrupts driver addresses, producing 0x0A crashes with a different blamed file each time.
- **Graphics driver instability.** GPU drivers run at high IRQL; bugs crash the system under 3D load.
- **Kernel filter conflicts.** Antivirus, VPN, and firewall drivers fighting over the same IRQL territory.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the stop screen and target the named driver

Precision beats volume — fix the driver Windows already blamed.

1. Photograph or write down the `.sys` filename on the blue screen before it restarts.
2. If it restarts too fast, disable auto-restart: `sysdm.cpl > Advanced > Startup and Recovery > uncheck Automatically restart`.
3. Map the file: `ndis.sys`/`Netwtw*.sys` = network, `nvlddmkm.sys` = NVIDIA, `atikmdag.sys` = AMD, `rtwlane.sys` = Realtek Wi-Fi.
4. In **Device Manager**, open that device's **Properties > Driver** and note the version and date.
5. Decide: crash started after a driver change → **Roll Back Driver**; driver is old and nothing changed → update it.

The driver-specific deep dive is at [how to fix DRIVER_IRQL_NOT_LESS_OR_EQUAL in Windows 11 24H2](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/).

### Fix 2: Do a true clean reinstall of that driver

"Update" often leaves the broken files in place — remove them first.

1. Download the newest driver for your exact model from the manufacturer's support page — Dell, HP, or Lenovo support sites all carry model-specific builds.
2. In **Device Manager**, right-click the device > **Uninstall device**, checking **Attempt to remove the driver for this device**.
3. Restart — Windows will load a basic fallback driver.
4. Install the downloaded driver, restart again.
5. For Intel wireless specifically, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the newest Wi-Fi/Bluetooth builds reliably.

A half-removed driver is worse than an old one; the uninstall-with-removal step is what makes this a clean reinstall rather than a wishful update.

### Fix 3: Handle the post-update case correctly

When a Windows update started the crashes, the response is specific.

1. Open **Settings > Windows Update > Update history** and check for driver updates around the crash start date.
2. Roll back the driver Windows installed (**Device Manager > Properties > Driver > Roll Back Driver**).
3. If no rollback is available, manually install the previous version from your maker's support page.
4. To stop Windows re-installing the bad driver: **Settings > Windows Update > Advanced options > Optional updates** — don't approve it, or use the "Show or hide updates" troubleshooter to block it.
5. Report the bad driver via Feedback Hub with the stop code — that's how Microsoft pulls broken driver updates.

The update-triggered variant is covered step-by-step in [how to fix IRQL_NOT_LESS_OR_EQUAL after a Windows 11 update](/articles/how-to-fix-irql-not-less-or-equal-after-windows-11-update/).

### Fix 4: Clean-install the graphics stack

Don't neglect the second-most-common 0x0A source.

1. Download the latest GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
2. Choose **Custom installation > Perform a clean installation** (NVIDIA) or **Factory Reset** (AMD).
3. For persistent cases, use Display Driver Uninstaller in Safe Mode first, then install fresh.
4. Skip beta/"game ready day-one" drivers if stability is the priority.
5. Stress with the workload that crashed — graphics IRQL faults need 3D load to reproduce.

### Fix 5: Verify with the minidump, not with hope

Confirm the fix against actual crash evidence.

1. Ensure dumps are enabled: `sysdm.cpl > Advanced > Startup and Recovery > Small memory dump`.
2. After the next crash (or the most recent one), open `C:\Windows\Minidump\*.dmp` in WinDbg Preview, run `!analyze -v`.
3. Check that `IMAGE_NAME` matches the driver you fixed — if it names a *different* driver, you fixed the wrong one; repeat Fix 1–2 for the new name.
4. If dumps consistently blame `ntoskrnl.exe` with varying stacks, suspect RAM (Fix 6), not drivers.
5. No new dumps after a week of normal use = fixed. Dumps are the receipt; everything else is a claim.

### Fix 6: Test memory when blame is inconsistent

Hardware produces the pattern drivers can't explain.

1. Run `mdsched.exe` → **Restart now and check for problems** → check **MemoryDiagnostics-Results** in Event Viewer.
2. Run MemTest86 overnight for intermittent faults a quick test misses.
3. Load BIOS **Optimized Defaults** to clear unstable memory or CPU timings.
4. Test RAM sticks individually where removable.
5. Replace failing modules with the manufacturer-specified part — mismatched replacements restart the whole cycle.

### Fix 7: Repair the OS foundation last

When drivers and RAM are both clean, fix what they run on.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Install all pending Windows updates, including optional ones.
3. Strip third-party antivirus/VPN/optimizer tools temporarily and test on Defender alone.
4. If crashes persist through all of this, an in-place upgrade from the Windows 11 download page (keep files and apps) rebuilds the kernel cleanly.
5. Still crashing after that, with clean memory tests? That's a warranty conversation — you've eliminated software.

## Closing

The best way to fix IRQL_NOT_LESS_OR_EQUAL isn't the most fixes — it's the right order: read the blamed driver, clean-reinstall exactly that driver, verify against the minidump, and widen to memory and the OS only when the evidence points there. Most 0x0A crashes surrender at Fix 2, a clean Wi-Fi or graphics driver install that takes twenty minutes. The people who fight this stop code for weeks are the ones who skipped the stop screen, guessed at drivers, and never opened a dump file. Don't be them — let the blue screen tell you who did it, then act on it.
