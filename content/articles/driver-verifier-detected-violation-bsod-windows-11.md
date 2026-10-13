---
title: "DRIVER_VERIFIER_DETECTED_VIOLATION BSOD in Windows 11: What It Means and How to Fix It"
slug: driver-verifier-detected-violation-bsod-windows-11
date: 2026-10-09
categories: ["windows-errors"]
tags: ["bsod", "driver-verifier", "drivers"]
description: "Seeing DRIVER_VERIFIER_DETECTED_VIOLATION in Windows 11? It means Driver Verifier caught a bad driver — here's how to identify it and fix it."
thumbnail: "/images/thumbs/driver-verifier-detected-violation-bsod-windows-11.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_DETECTED_VIOLATION?"
    a: "Driver Verifier is a Windows testing tool that stresses drivers to expose bugs. When it's active and a driver breaks the rules — bad memory access, wrong IRQL usage, pool corruption — Verifier deliberately blue-screens with this stop code and names the offending driver. It's a diagnostic crash, not a random failure."
  - q: "Why is Driver Verifier running on my laptop? I never enabled it."
    a: "Someone or something enabled it: a technician troubleshooting your machine, a driver installer, enterprise management software, or you following an earlier troubleshooting guide and forgetting to turn it off. It's also occasionally left on after manufacturer diagnostics. Run verifier /query in an admin Command Prompt to check its status."
  - q: "Should I just turn off Driver Verifier to stop the crashes?"
    a: "Turning it off stops the crashes, but the underlying driver bug remains — Verifier was only exposing it. The right approach: note which driver Verifier blamed, fix or replace that driver, then disable Verifier. Disabling it without fixing the driver leaves a real bug in your system."
  - q: "How do I turn off Driver Verifier in Windows 11?"
    a: "Open an admin Command Prompt or Terminal and run verifier /reset, then restart. If Windows won't boot because Verifier crashes it immediately, boot into Safe Mode (Verifier doesn't load all drivers there the same way) or use the recovery command prompt to run verifier /reset."
---
DRIVER_VERIFIER_DETECTED_VIOLATION is a strange blue screen because it's not really an accident — it's Windows catching a driver red-handed. Driver Verifier is a built-in stress-test tool: when enabled, it watches drivers aggressively, and the moment one breaks the rules, it crashes the system on purpose and points at the guilty driver.

So if you're seeing this stop code, two things are true: Verifier is (or was) turned on, and at least one driver on your system has a genuine bug. Here's how to handle both facts properly.

## Why this happens

- **Verifier was left enabled** — after troubleshooting, diagnostics, or a repair shop visit, and now it crashes on a driver bug that would otherwise go unnoticed.
- **A genuinely buggy driver** — the whole point of Verifier; the named driver has a real defect (bad memory handling, IRQL violations, pool misuse).
- **Outdated driver under stricter scrutiny** — old drivers often violate rules that Verifier enforces, even if they "worked" for years without it.
- **Verifier settings too aggressive** — enabling every check on every driver produces crashes from minor issues and massive slowdowns.
- **Driver conflict exposed** — two drivers interacting badly in a way normal operation never triggers.
- **Corrupted driver binary** — disk corruption damaging a driver that Verifier then catches misbehaving.

## How to fix it

Work through these in order. The sequence matters: identify, fix the driver, then disable Verifier.

### Fix 1: Note which driver Verifier blamed

The blue screen is telling you the answer — capture it.

1. Photograph the blue screen. DRIVER_VERIFIER_DETECTED_VIOLATION screens typically name the faulting driver file (e.g., `rtwlanu.sys`, `nvlddmkm.sys`, some `*.sys` name).
2. After rebooting, confirm in **Event Viewer** (**Windows + R** > `eventvwr.msc`) > **Windows Logs** > **System** — the BugCheck entry records the stop code parameters.
3. For full detail, open the minidump in **WinDbg Preview** (Microsoft Store): **File** > **Open dump file** > C:\\Windows\\Minidump > newest file, then `!analyze -v`. The blamed driver is listed explicitly.
4. Write the driver name down — every fix below targets it.

### Fix 2: Check Verifier's current configuration

See what was enabled and why it might be overreacting.

1. Open **Terminal (Admin)** (**Windows + X**) and run:
   `verifier /query`
   This shows which drivers are under verification and which checks are active.
2. If every driver on the system is selected with all checks on, that's an overly aggressive setup — likely to crash on trivial issues and slow the machine noticeably.
3. Don't reset it yet — first fix the driver (Fixes 3–4), so you don't lose the diagnostic information. You'll disable Verifier at the end.

### Fix 3: Update or replace the blamed driver

Fix the actual bug Verifier found.

1. Identify the device: search the driver filename — `rtwlanu.sys`/`Netwtw` = Wi-Fi, `nvlddmkm.sys` = NVIDIA, `amdkmdag.sys` = AMD, `rtkvhd64.sys` = Realtek audio, and so on.
2. In **Device Manager** (**Windows + X**), find the device, **Properties** > **Driver** tab.
3. Download the newest driver from the hardware maker's site or your laptop manufacturer's support page — not just Windows Update.
4. Install it. If the newest driver still trips Verifier, try the previous version (**Roll Back Driver**) — sometimes the latest release is the buggy one.
5. If the driver belongs to software you don't need, uninstall the parent program entirely.

### Fix 4: Remove the usual Verifier tripwires

Certain software categories trip Verifier constantly.

1. Uninstall third-party antivirus completely (**Settings** > **Apps** > **Installed apps**) — its filter drivers are frequent Verifier victims. Test on Microsoft Defender.
2. Uninstall VPN clients, "driver updater" utilities, and system "optimizers" — all install kernel drivers of varying quality.
3. Remove old hardware's leftover drivers: in **Device Manager** > **View** > **Show hidden devices**, uninstall grayed-out devices you no longer own.
4. Restart and observe — with the tripwires gone, Verifier often goes quiet.

### Fix 5: Repair system files and the driver store

Rule out corruption as the reason a driver misbehaves.

1. In **Terminal (Admin)**:
   `DISM /Online /Cleanup-Image /RestoreHealth`
   then `sfc /scannow`.
2. Run `chkdsk C: /f` to verify the file system holding the driver files.
3. Restart. If Verifier still blames the same driver after this, the bug is in the driver's code, not corruption — replacement is the answer.

### Fix 6: Narrow Verifier to confirm, then disable it

Use Verifier as the diagnostic tool it is — then put it away.

1. If you want confirmation the fix worked: run `verifier.exe`, choose **Create standard settings** > **Select driver names from a list**, tick ONLY the previously-blamed driver, **Finish**, restart, and use the laptop for a day. No crash = fixed.
2. Whether you test or not, disable Verifier when done: admin Terminal > `verifier /reset` > restart.
3. Verify it's off: `verifier /query` should report no drivers being verified.
4. Never leave Verifier running permanently — it slows the system and will eventually crash on some minor driver infraction.

### Fix 7: If Windows won't boot with Verifier on

Emergency path when Verifier crashes every boot.

1. Force Automatic Repair (three interrupted boots), then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4** for Safe Mode.
2. In Safe Mode, open an admin Command Prompt and run `verifier /reset`, then restart normally.
3. If Safe Mode also crashes, use **Troubleshoot** > **Advanced options** > **Command Prompt** in recovery and run `verifier /reset` there (you may need to target the offline system — try `verifier /reset` first; it usually works from WinRE).
4. Once booted, identify the driver from the last minidump and replace it before considering re-enabling Verifier.

## Closing

DRIVER_VERIFIER_DETECTED_VIOLATION means the diagnostic tool did its job — it found a driver with a real bug and named it. Thank it, fix or replace that driver, and then turn Verifier off with `verifier /reset`. The mistake to avoid is treating the symptom (disabling Verifier) while ignoring the disease (the buggy driver still in your kernel). For the focused repair walkthrough, see [driver verifier detected violation in Windows 11 24H2](/articles/how-to-fix-driver-verifier-detected-violation-in-windows-11-24h2/), and for the methodical best-practice sequence, [the best way to fix DRIVER_VERIFIER_DETECTED_VIOLATION](/articles/best-way-to-fix-driver-verifier-detected-violation/). Microsoft's [driver verifier documentation](https://support.microsoft.com/en-us/windows) explains the tool's settings if you want to use it deliberately for future troubleshooting.
