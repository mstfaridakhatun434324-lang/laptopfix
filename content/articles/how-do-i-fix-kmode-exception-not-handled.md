---
title: "KMODE_EXCEPTION_NOT_HANDLED: Fix It Step by Step"
slug: how-do-i-fix-kmode-exception-not-handled
date: 2026-09-07
categories: ["windows-errors"]
tags: ["kmode_exception_not_handled", "bsod", "drivers", "stop code"]
description: "KMODE_EXCEPTION_NOT_HANDLED blue screen? A kernel-mode driver threw an unhandled exception. Here's how to identify the driver and fix it."
thumbnail: "/images/thumbs/how-do-i-fix-kmode-exception-not-handled.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean?"
    a: "A program running in kernel mode — almost always a driver — encountered an exception (like accessing invalid memory) that it didn't handle. In user mode, an unhandled exception just crashes the app; in kernel mode, there's no containing it, so Windows crashes the whole system. The stop screen usually names the faulting driver file."
  - q: "The blue screen names a driver file — what do I do with that?"
    a: "That's the best-case scenario: the name tells you exactly which driver to fix. Search the filename to identify its software, then update it from the manufacturer, roll it back if recently updated, or uninstall the parent program if you don't need it. The dump usually confirms the same file."
  - q: "Can RAM cause KMODE_EXCEPTION_NOT_HANDLED?"
    a: "Yes, as a secondary cause — failing RAM corrupts driver code or data, causing exceptions the driver didn't cause by itself. If the blamed driver changes between crashes, test memory. If the same driver is blamed every time, it's the driver."
  - q: "Why does this happen after Windows updates?"
    a: "Updates deliver new driver versions that may contain bugs, and kernel changes can expose latent bugs in existing drivers. The pattern 'fine for months, crashing after Patch Tuesday' is classic for this stop code — roll back the updated driver first."
---

`KMODE_EXCEPTION_NOT_HANDLED` is refreshingly direct as blue screens go: a kernel-mode program — in practice, always a driver — hit an exception it didn't handle, and since kernel mode has no safety net, the system stopped. The good news is that this stop code *usually names the culprit right on the blue screen* in the form of a driver filename (like `ntfs.sys` or a third-party `.sys`). When it does, your job is mostly translation: filename → software → update, roll back, or remove.

When the screen doesn't name a file, the dump will — so the workflow below always includes dump analysis as the fallback. The fix families are short: the named driver, a recent update that delivered it, or (when blame is inconsistent) RAM corrupting drivers. For the heap-corruption cousin, see [kernel mode heap corruption diagnosis](/articles/what-to-do-if-kernel-mode-heap-corruption/), and for kernel integrity violations, [KERNEL_SECURITY_CHECK_FAILURE](/articles/how-to-fix-kernel-security-check-failure/).

## Why this happens

- **Buggy device driver**: The primary cause — the driver throws an unhandled exception during normal operation.
- **Driver updated by Windows Update**: A new driver version with a regression, delivered automatically.
- **Corrupted driver files**: Partial updates or disk damage leaving the driver in a broken state.
- **Conflicting drivers**: Two drivers for the same hardware or hooking the same path, one throwing the other into an exception.
- **Failing RAM**: Corrupts driver code/data, producing exceptions with inconsistent blame.
- **Overclocked system instability**: Marginal clocks cause the computational errors that surface as driver exceptions.
- **Malware masquerading as a driver**: Rootkits install as drivers; their bugs crash the kernel the same way.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the driver name from the stop screen

The screen often hands you the answer — capture it.

1. The next time it crashes, photograph or write down the full stop code *and* any filename shown (usually at the bottom: "What failed: something.sys").
2. If you missed it, check **Event Viewer** > **Windows Logs** > **System** > filter **BugCheck** — the details often include the faulting module.
3. Search the filename to identify its software: `ntfs.sys`/`storahci.sys` (Windows storage — see Fix 6), `nvlddmkm.sys` (NVIDIA), `Netwtw10.sys` (Intel Wi-Fi), `rt640x64.sys` (Realtek network), etc.
4. With the driver identified, jump to the targeted fix: update (Fix 2), roll back (Fix 3), or remove (Fix 4).

### Fix 2: Update the faulting driver from the manufacturer

The standard fix when the driver is simply buggy or outdated.

1. Identify the device in **Device Manager** (**Win + X**) corresponding to the driver.
2. Download the latest driver from the hardware vendor or your laptop maker's support page — Dell, HP, Lenovo — not from a driver-updater tool.
3. For graphics: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), [Intel](https://www.intel.com/content/www/us/en/support/detect.html) — choose clean installation.
4. Restart and test with the workload that triggered the crash.
5. If the manufacturer's driver is older than the crashing one, that's fine — stability beats version numbers.

### Fix 3: Roll back a recently updated driver

When the timeline implicates an update.

1. **Device Manager** > right-click the device > **Properties** > **Driver** tab > **Roll Back Driver**.
2. If Windows Update delivered it, also consider hiding that driver update so it doesn't reinstall (use the show/hide updates troubleshooter from Microsoft support).
3. Alternatively, uninstall the device (checking **Attempt to remove the driver**) and restart — Windows installs its inbox driver, which is the stable baseline for testing.
4. Test for several days before accepting any new driver version for that device.

### Fix 4: Uninstall the parent software

Sometimes the driver isn't worth keeping.

1. If the faulting driver belongs to software you don't need — old VPN clients, RGB utilities, "game boosters," printer software for printers you no longer own — uninstall the software completely.
2. Use the vendor's removal tool for security software; filter drivers survive normal uninstalls.
3. Restart and verify the driver file is gone from `C:\Windows\System32\drivers`.
4. This is the cleanest fix when it applies — no driver, no crash, no maintenance.

### Fix 5: Analyze the dump when no driver is named

Let the dump supply what the screen didn't.

1. Confirm minidumps: `sysdm.cpl` > **Advanced** > **Startup and Recovery** > **Small memory dump**.
2. Analyze the newest dump per our [dump analysis guide](/articles/how-to-analyze-bsod-dump-files-on-laptop/) — WinDbg's `!analyze -v` names the faulting module and the exception type.
3. The exception code matters: `0xC0000005` (access violation) is the classic driver bug; the faulting IP pinpoints the driver.
4. Apply Fix 2–4 to whatever the dump names. If dumps blame different drivers each time, proceed to Fix 6's memory test.

### Fix 6: Test RAM and reset clocks

Cover hardware when blame is inconsistent.

1. **Win + R** > `mdsched.exe` > **Restart now and check for problems**; follow with MemTest86 overnight for a definitive result.
2. Reset BIOS to optimized defaults — clear overclocks, undervolts, XMP/EXPO.
3. Run a full offline malware scan (**Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan**) — rootkit-drivers are a real, if uncommon, cause.
4. Check drive health (`chkdsk C: /f` + manufacturer SSD utility) — disk corruption damages driver files.

### Fix 7: Repair system files and stabilize

The foundation pass and the monitoring period.

1. Elevated prompt: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` — repairs Windows' own drivers (`ntfs.sys` and friends) when they're the named fault.
2. Install all pending Windows updates.
3. If a Windows *system* driver (ntoskrnl-adjacent) is consistently blamed with no third-party driver in the stack, an in-place upgrade repair from the Windows 11 ISO rebuilds them cleanly.
4. Monitor for a week. A single recurrence after all fixes warrants another dump analysis — patterns change as drivers update.

## Closing

KMODE_EXCEPTION_NOT_HANDLED is the most actionable stop code in Windows because it usually names its own cause — read the filename, fix that driver, done. The discipline is in the follow-through: get the driver from the manufacturer, block the bad version from returning, and let the dump arbitrate when the screen is silent. Most cases close in under an hour once you stop treating it as a mystery and start treating it as a driver work order.
