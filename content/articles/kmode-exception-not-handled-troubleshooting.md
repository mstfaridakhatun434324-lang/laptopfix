---
title: "KMODE_EXCEPTION_NOT_HANDLED: A Troubleshooting Guide"
slug: kmode-exception-not-handled-troubleshooting
date: 2026-10-05
categories: ["windows-errors"]
tags: ["kmode-exception-not-handled", "bsod", "driver-troubleshooting"]
description: "KMODE_EXCEPTION_NOT_HANDLED means a kernel driver threw an error it could not catch. This troubleshooting guide shows how to find which one."
thumbnail: "/images/thumbs/kmode-exception-not-handled-troubleshooting.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean in plain English?"
    a: "A program running in kernel mode — where drivers live — hit an error it had no handler for, so Windows crashed to protect itself. Stop code 0x1E. The screen often names the offending driver file (like ntfs.sys or a third-party .sys), which is your starting point for the investigation."
  - q: "How is this different from SYSTEM_SERVICE_EXCEPTION?"
    a: "They are cousins. KMODE_EXCEPTION_NOT_HANDLED (0x1E) is an unhandled exception in kernel code, while SYSTEM_SERVICE_EXCEPTION (0x3B) is an exception during a system service call. In practice both point at drivers, and the troubleshooting process is nearly identical — find the named file, update or remove its driver."
  - q: "Can antivirus software cause this error?"
    a: "Yes — antivirus filter drivers run in kernel mode and are frequent culprits, especially after a major Windows update changes kernel interfaces the AV driver was relying on. If crashes started after an update, the AV driver is worth investigating early."
  - q: "How do I read the minidump to find the bad driver?"
    a: "Install WinDbg Preview from the Microsoft Store, open the newest file in C:\\Windows\\Minidump, and run !analyze -v. The IMAGE_NAME line names the driver. A quick web search of that filename tells you which product installed it."
---
KMODE_EXCEPTION_NOT_HANDLED is Windows telling you a kernel-mode driver crashed in a way it could not recover from. The blue screen usually does you the favor of naming the driver file — but that file is a starting point, not always the villain. The 'not handled' part means the driver had no error recovery for whatever went wrong — a null pointer, a bad memory access — so the kernel stopped the machine rather than continue in a corrupted state.

This guide is about methodical troubleshooting: confirming the suspect, ruling out hardware, and fixing the actual cause instead of reinstalling drivers at random and hoping. This guide is about methodical troubleshooting: confirming the suspect, ruling out hardware, and fixing the actual cause instead of reinstalling drivers at random and hoping.

## Why this happens

- **An outdated or buggy third-party driver.** Network, storage controller, and antivirus filter drivers are the usual suspects.
- **Driver conflict after a Windows feature update.** Updates change kernel interfaces; old drivers that bent the rules start breaking.
- **Corrupted driver files on disk.** A damaged .sys file loads half-broken and throws exceptions immediately.
- **Faulty RAM.** Memory corruption makes innocent drivers throw exceptions, and the named file changes between crashes.
- **Overclocking instability.** An unstable CPU or RAM overclock produces exceptions in whatever driver happens to be running.
- **Malware hooking kernel functions.** Rootkits patch kernel code, and their patches throw exceptions when Windows changes underneath them.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Write down the named driver file

The filename on the blue screen is clue number one — capture it before doing anything else. Phone photos work fine here — the filename is usually in the middle of the screen in smaller text beneath the stop code.

1. If the screen names a `.sys` file, write it down exactly.
2. If Windows reboots too fast to read it, disable that behavior first — our guide to [disabling automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) takes thirty seconds.
3. Search the filename online to identify the product. Names like `rtwlanu.sys` (Realtek Wi-Fi) or `avc3.sys` (Bitdefender) point straight at the owner.

### Fix 2: Confirm with the minidump

The screen names one file; the dump confirms whether it is really at fault or just a bystander. Save copies of the dumps to a folder before you start fixing things; if a repair changes which driver is named, that change itself is diagnostic information.

1. Open `C:\Windows\Minidump` and find the dump matching your crash time.
2. Open it in WinDbg Preview and run `!analyze -v`.
3. Compare IMAGE_NAME with the file from the blue screen. If they agree across two or three dumps, you have a solid suspect.
4. If every dump names a different driver, stop chasing drivers — that pattern screams bad RAM. Jump to Fix 5.

### Fix 3: Update, roll back, or remove the suspect driver

Act on the evidence from the dumps. When the suspect is a laptop-maker utility driver — hotkey tools, fan control — check the laptop maker's support site rather than Windows Update, since those drivers only come from the vendor.

1. For hardware drivers, update via **Device Manager** (**Win + X > Device Manager**), then from the manufacturer's site if needed.
2. If the driver was updated just before crashes began, roll it back: **Properties > Driver tab > Roll Back Driver**.
3. For antivirus or VPN drivers, reinstall the product cleanly — or uninstall it temporarily to test. Windows Security covers you in the meantime.
4. Restart and run the workload that triggered the crash. One clean driver change at a time, so you know what fixed it.

### Fix 4: Run Driver Verifier on the suspect (advanced)

Driver Verifier stress-tests a driver and crashes immediately — with a clearer error — when it misbehaves. Verifier makes crashes happen sooner and more often while it is on — that is the point, but do not enable it the night before a deadline.

1. Press **Win + R**, type `verifier`, and press **Enter**.
2. Choose **Create custom settings**, enable all checks except low-resource simulation, then select the suspect driver.
3. Restart and use the PC normally. Verifier-induced crashes name the driver explicitly.
4. Delete the Verifier settings afterward by running `verifier /reset` — do not leave it on permanently.

### Fix 5: Test the RAM

Inconsistent culprits across dumps mean the memory itself is corrupting drivers as they run. If the laptop has soldered RAM and the test fails, document the errors with photos and contact the manufacturer — that is a warranty claim, not a DIY repair.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. If errors are found, test sticks individually to identify the bad one. Sealed laptop? A shop can do this cheaply.
4. Our [memory management troubleshooting walkthrough](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) goes deeper on isolating RAM faults.

### Fix 6: Repair system files and scan for malware

Cover the remaining software causes in one pass — see [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for additional recovery options if these steps do not resolve it. Run the malware scan in Safe Mode with Networking if the full Windows environment is too unstable — the offline scan option handles the worst cases.

1. In an elevated **Command Prompt**, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Run a **Full scan** in **Windows Security > Virus & threat protection > Scan options**.
3. Restart. If crashes persist after a clean driver, clean RAM test, and clean system files, the remaining suspects are the motherboard or CPU — time for professional diagnostics.

### Fix 7: Install all pending Windows updates

Microsoft regularly ships kernel and driver-compatibility fixes that resolve exception-causing conflicts — an update you have been postponing might be the fix.

1. Go to **Settings > Windows Update** and click **Check for updates**.
2. Install everything offered, including the **Optional updates** under **Advanced options**, which is where driver updates hide.
3. Restart even if Windows does not insist — kernel changes only take effect with a full restart.
4. If crashes began immediately after a specific update, uninstall that one update instead (**Update history > Uninstall updates**) and pause updates for a week.

## Closing

Troubleshooting KMODE_EXCEPTION_NOT_HANDLED is a process of elimination, and the minidumps do most of the work for you. Two dumps naming the same driver means a driver problem; dumps naming everything under the sun means a RAM problem. Follow the evidence and you will land on the fix without the usual guesswork. File the dumps away when you are done. If the same stop code ever comes back, a two-minute comparison tells you whether history is repeating itself or something new broke.
