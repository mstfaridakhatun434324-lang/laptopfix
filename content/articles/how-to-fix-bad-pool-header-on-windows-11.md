---
title: "Bad Pool Header on Windows 11? How to Fix It"
slug: how-to-fix-bad-pool-header-on-windows-11
date: 2026-09-30
categories: ["windows-errors"]
tags: ["bad pool header", "bsod", "windows 11", "driver"]
description: "The BAD_POOL_HEADER blue screen on Windows 11 is usually a driver or RAM issue. Here's the Windows 11-specific fix sequence that resolves it."
thumbnail: "/images/thumbs/how-to-fix-bad-pool-header-on-windows-11.webp"
faqs:
  - q: "What does Bad Pool Header mean on Windows 11?"
    a: "Windows 11's memory manager caught an invalid request to the memory pool — typically a driver freeing memory twice or accessing freed memory. Stop code 0x00000019. The mechanism is identical to Windows 10, but Windows 11's faster driver-update cadence means recently auto-updated drivers are suspects more often. Check what updated just before the crashes began."
  - q: "How do I find the bad driver on Windows 11?"
    a: "Open Event Viewer (Windows + X, Event Viewer), go to Windows Logs, System, and find BugCheck entries — the parameters sometimes implicate a driver. Better: analyze C:\\Windows\\Minidump with BlueScreenView, or enable Driver Verifier with special pool on non-Microsoft drivers to catch the corruptor with a more specific stop code."
  - q: "Windows 11 updated my driver automatically and now I crash. What do I do?"
    a: "Roll it back: Device Manager, right-click the device, Properties, Driver tab, Roll Back Driver. Then block that version with the 'Show or hide updates' troubleshooter so Windows 11 doesn't reinstall it. Windows 11 is more aggressive about driver updates than 10, so this rollback-and-block pattern is an essential skill."
  - q: "Could my RAM be causing Bad Pool Header on Windows 11?"
    a: "Yes — it's the second most common cause after drivers. Run Windows Memory Diagnostic (Windows + R, mdsched.exe), and follow up with MemTest86 overnight for certainty. Also check whether XMP/DOCP memory profiles are enabled in the BIOS; Windows 11 gaming laptops with aggressive memory timings produce this stop code when the timings go marginal."
---

BAD_POOL_HEADER (stop code 0x00000019) on Windows 11 is the same memory-pool violation as on Windows 10, but the Windows 11 context changes the suspect lineup. Windows 11 updates drivers more aggressively — including silently, overnight — so "nothing changed" often means "Windows Update changed a driver while you slept." The error still means the memory manager caught an invalid pool request (double-frees and use-after-free by drivers being the classics), and it's still usually a driver, with bad RAM as the runner-up.

This guide uses Windows 11's actual Settings paths and accounts for its update behavior, including the crucial skill of blocking a bad driver version after rolling it back. For the Windows 10 version of this fix, see our [Windows 10 Bad Pool Header guide](/articles/how-to-fix-bad-pool-header-on-windows-10/); for pool corruption's close cousin, see our [special pool corruption guide](/articles/how-to-fix-special-pool-detected-memory-corruption-on-windows-11/); for general blue screen method, our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Why this happens

- **Auto-updated drivers**: Windows 11 silently installing buggy driver versions overnight.
- **Antivirus filter drivers**: Kernel security drivers mishandling pool allocations after updates.
- **Failing RAM**: Hardware corruption of pool structures.
- **XMP/DOCP memory instability**: Aggressive timings going marginal over time.
- **Corrupt system files**: Damaged memory-management components.
- **Interrupted Windows 11 updates**: Half-applied updates corrupting kernel components.
- **Disk errors**: Bad sectors corrupting drivers or the page file.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what changed — especially overnight

Windows 11's update behavior makes this step essential.

1. **Settings** > **Windows Update** > **Update history** — check both Windows updates and driver updates with dates just before the crashes.
2. **Device Manager** > suspect devices > **Properties** > **Driver** > note the driver date — a driver dated yesterday that you didn't install yourself is Windows Update's doing.
3. **Event Viewer** > **Windows Logs** > **System** > **BugCheck** entries give you the crash timeline to correlate.
4. If a driver update aligns with crash onset, skip straight to Fix 3 (rollback) — you've found it.

### Fix 2: Boot into Safe Mode to confirm the driver theory

Validate before changing drivers.

1. **Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **4**.
2. Stable in Safe Mode → third-party driver confirmed. Crashes in Safe Mode → prioritize RAM testing (Fix 5) and system repair (Fix 4).
3. In Safe Mode, you can uninstall suspect drivers via **Device Manager** safely.
4. Remember: this method exits Safe Mode on plain restart — no setting to undo.

### Fix 3: Roll back and block the bad driver

The Windows 11-specific core skill.

1. **Device Manager** > device > **Properties** > **Driver** > **Roll Back Driver** (or uninstall with driver removal, then install the previous version manually).
2. Block reinstallation: run Microsoft's "Show or hide updates" troubleshooter and hide the driver update — otherwise Windows 11 reinstalls the crasher within days.
3. Alternatively, **Group Policy** > **Do not include drivers with Windows Updates** to stop all automatic driver updates; manage drivers manually from vendor sites instead.
4. Verify the block survived the next Patch Tuesday by rechecking the driver date in **Device Manager**.

### Fix 4: Repair system files and update Windows 11

Fix the OS layer with Windows 11's tools.

1. **Terminal (Admin)**: `sfc /scannow` → `DISM /Online /Cleanup-Image /RestoreHealth` → SFC again.
2. **Settings** > **Windows Update** > install all pending updates — Microsoft patches pool-management bugs in cumulative updates; check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for the KB details.
3. If a specific update caused the crashes, uninstall it (**Update history** > **Uninstall updates**) and pause updates while stabilizing.
4. For a stuck or damaged update system, the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) provides clean installation media for repair installs.

### Fix 5: Test the RAM and memory settings

The hardware half of the diagnosis.

1. **Windows + R** > `mdsched.exe` > **Restart now and check for problems**.
2. MemTest86 overnight (4+ passes, zero errors) for the definitive answer.
3. Enter the BIOS/UEFI and check memory profiles — disable XMP/DOCP and retest at stock JEDEC speeds; re-enable only if stock proves stable and you want to isolate the profile as the cause.
4. Reseat sticks, test individually on errors, replace failures.

### Fix 6: Remove antivirus filter drivers temporarily

A common Windows 11-specific trigger.

1. Uninstall third-party antivirus using the vendor's complete removal tool — Windows 11's tightened kernel integration makes filter-driver bugs more visible.
2. **Windows Security** (built in) activates automatically and is sufficient during the test period.
3. Test 48 hours. Crashes gone → reinstall the latest antivirus version (vendors patch these quickly) or switch products.
4. Never leave the system without active protection beyond the test window.

### Fix 7: Check the disk and do a repair install if needed

Close out storage causes and deep corruption.

1. Elevated terminal: `chkdsk C: /f /r` (schedule at restart) — bad sectors corrupt pool-adjacent structures.
2. Manufacturer diagnostics (**F12** > **Diagnostics** on Dell, **F2** on HP) for a full drive test.
3. If software fixes fail but hardware tests pass: in-place upgrade repair — mount the Windows 11 ISO, run setup, keep files and apps. This rebuilds all system components cleanly.
4. Persistent crashes after a repair install with clean drivers = hardware fault needing professional diagnosis.

## Closing

On Windows 11, BAD_POOL_HEADER is most often a driver story with an update twist — the OS's enthusiasm for driver updates means the culprit frequently arrived uninvited. The durable fix is rollback plus blocking, not just rollback; without the block, you're scheduling a rematch. After that, the standard discipline applies: verify RAM, repair system files, and confirm stability over days rather than hours. Keep a note of your stable driver versions — on Windows 11, that's not paranoia, it's maintenance. For the Windows 10 edition of this problem, our [Windows 10 guide](/articles/how-to-fix-bad-pool-header-on-windows-10/) covers the same error in that OS's context. As a final preventive step, consider changing how Windows 11 handles drivers on your machine permanently: disabling automatic driver updates via Group Policy and managing graphics, network, and chipset drivers manually from vendor sites puts you back in control of what changes and when. It costs a few minutes each month to check for updates yourself, and it buys immunity from the entire category of "Windows updated my driver overnight and now I blue-screen." Pair that with an annual RAM health check on aging laptops, and BAD_POOL_HEADER becomes a problem you solved once rather than a problem you manage forever.
