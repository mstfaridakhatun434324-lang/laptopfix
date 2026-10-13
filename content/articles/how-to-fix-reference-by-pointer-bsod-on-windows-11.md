---
title: "How to Fix the REFERENCE_BY_POINTER BSOD on Windows 11"
slug: how-to-fix-reference-by-pointer-bsod-on-windows-11
date: 2026-10-07
categories: ["windows-errors"]
tags: ["bsod", "drivers", "windows-11"]
description: "REFERENCE_BY_POINTER blue screen on Windows 11? It's a driver reference-counting bug — here's how to identify the driver and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-on-windows-11.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "Windows tracks shared objects with reference counts, and this stop code means a driver decremented a count below zero — a programming bug in the driver. It's almost exclusively a driver problem, not hardware. The faulting driver is often named on the blue screen or in the crash dump."
  - q: "Which drivers cause REFERENCE_BY_POINTER?"
    a: "Historically, antivirus filter drivers, network drivers, and storage filter drivers are the most common offenders. Any driver that manages object lifetimes can have this bug, but security software and recently updated drivers deserve the first look."
  - q: "Can Windows Update trigger REFERENCE_BY_POINTER?"
    a: "Yes. Updates frequently replace network, storage, and security drivers. If the new version has a reference-counting bug — or conflicts with a leftover component of the old version — these crashes start immediately after the update."
  - q: "Is REFERENCE_BY_POINTER dangerous for my files?"
    a: "The crash itself doesn't damage files, but repeated unexpected shutdowns can corrupt open documents and, over time, the file system. Fix it promptly, save work frequently until then, and run chkdsk after the crashes stop to verify file-system integrity."
---
REFERENCE_BY_POINTER is one of the more technical-sounding blue screens, but the translation is simple: a driver made an accounting error with system memory objects, and Windows crashed rather than let the corruption spread. The good news buried in that: it's almost always a driver bug, which means it's fixable without replacing hardware.

The challenge is identifying which driver. Here's the methodical way to do it.

It's worth understanding why this particular stop code is so driver-specific. Reference counts are entirely a software bookkeeping concept — hardware faults corrupt data, but they don't decrement counters. That's why technicians treat REFERENCE_BY_POINTER as a near-certain driver bug from the start, and why the investigation focuses on recently installed or updated drivers, security software, and anything else that installed a kernel-mode component around the time the crashes began.

## Why this happens

- **Buggy third-party driver** — a driver decrements an object reference count too many times; antivirus and network filter drivers are the classic offenders.
- **Driver updated by Windows Update** — the new version introduced (or exposed) the bug.
- **Conflicting driver remnants** — old and new driver components from different versions interacting badly.
- **Corrupted driver files** — disk errors or a bad install damaged the driver binary.
- **Failing RAM** — rare for this stop code, but memory corruption can mimic reference-count bugs.
- **Rootkits or malware drivers** — malicious kernel drivers are often badly written and trigger exactly this.
- **Beta or unsigned drivers** — pre-release drivers haven't been through full validation.

## How to fix it

Work through these in order. The goal of the first half is identification; the second half is elimination.

### Fix 1: Read the crash dump to name the driver

Don't guess when Windows recorded the answer.

1. After a crash, open **Event Viewer** (**Windows + R** > `eventvwr.msc`) > **Windows Logs** > **System** and find the **BugCheck** entry — note the parameters and any named file.
2. For the full picture, install **WinDbg Preview** from the Microsoft Store.
3. In WinDbg: **File** > **Start debugging** > **Open dump file** > navigate to C:\\Windows\\Minidump and open the newest .dmp file.
4. In the command box at the bottom, type `!analyze -v` and press Enter. Read the **MODULE_NAME** / **IMAGE_NAME** lines — that's your suspect.
5. If the dump consistently names the same third-party driver, skip to Fix 3 for that driver. If it names ntoskrnl.exe with varying blame, continue with Fix 2.

### Fix 2: Deploy Driver Verifier against third-party drivers

Force the buggy driver to reveal itself.

1. Press **Windows + R**, type `verifier.exe`, press Enter.
2. Select **Create standard settings** > **Next** > **Select driver names from a list**.
3. Sort by **Provider** and tick every driver NOT from Microsoft — focus on antivirus, network, audio, and storage filter drivers.
4. Click **Finish** and restart. Use the laptop normally; Verifier will crash the system quickly when the bad driver misbehaves, and the blue screen will name it.
5. After identifying it, boot into Safe Mode and run `verifier /reset` in an admin Command Prompt to disable Verifier — don't leave it running indefinitely.

### Fix 3: Update, roll back, or remove the identified driver

Now act on what you found.

1. In **Device Manager** (**Windows + X**), locate the device for the named driver.
2. **Properties** > **Driver** tab: if the problem started recently, **Roll Back Driver**; otherwise **Update driver** > **Search automatically for drivers**.
3. Better: download the latest driver from the hardware maker's site (not Windows Update) and install it manually.
4. If the driver belongs to software you don't need (old VPN client, abandoned utility), uninstall the whole program via **Settings** > **Apps** > **Installed apps**.
5. Restart and test for several days — reference-count bugs can be intermittent.

### Fix 4: Remove antivirus and security filter drivers

If the dump is inconclusive, start with the most likely category.

1. Uninstall your third-party antivirus completely via **Settings** > **Apps** > **Installed apps**. Disabling isn't enough — the filter driver loads anyway.
2. Restart and run on Microsoft Defender for a test period of 3–5 days.
3. If crashes stop, the antivirus driver was the cause. Check the vendor's site for a version certified for your exact Windows 11 build before reinstalling — or stay with Defender.
4. Apply the same logic to VPN clients, endpoint protection, and "anti-cheat" drivers from games you no longer play.

### Fix 5: Run a malware scan

Rule out malicious kernel drivers.

1. In **Windows Security** (**Settings** > **Privacy & security** > **Windows Security** > **Virus & threat protection**), run a **Full scan**.
2. Then run **Microsoft Defender Offline scan** (under **Scan options**) — it reboots into a clean environment that catches rootkits hiding from normal scans.
3. Remove anything found, restart, and monitor. Malware drivers are a real (if uncommon) source of this stop code.

### Fix 6: Repair system files and verify the disk

Clean up collateral damage.

1. Open **Terminal (Admin)** and run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
   then `sfc /scannow`.
2. Run `chkdsk C: /f` to verify the file system — repeated crashes can corrupt the very driver files you're trying to fix.
3. Restart and test.

### Fix 7: Test RAM and reset if needed

The last checks for a stubborn case.

1. Run `mdsched.exe` (Windows + R) > **Restart now and check for problems**. Clean result? Good — this stop code is rarely RAM, but it's cheap to rule out.
2. If everything passes and crashes persist, the pragmatic move is **Settings** > **System** > **Recovery** > **Reset PC** > **Keep my files** > **Cloud download** — a fresh driver set eliminates buried conflicts.
3. After the reset, install drivers from your laptop maker's site one at a time, testing between each, so a returning crash immediately identifies its source.

## Closing

REFERENCE_BY_POINTER looks intimidating but it's one of the most "honest" blue screens — a driver did the math wrong, and Windows kept receipts in the crash dump. Read the dump, verify with Driver Verifier, and remove or replace the offender. Antivirus and network filter drivers are guilty more often than not. For the step-by-step checklist version, see [REFERENCE_BY_POINTER step by step](/articles/how-to-fix-reference-by-pointer-bsod-step-by-step/), and for crashes that began specifically with a Windows update, [REFERENCE_BY_POINTER after a Windows 11 update](/articles/how-to-fix-reference-by-pointer-bsod-after-windows-11-update/) targets that scenario. Microsoft's [troubleshooting reference](https://support.microsoft.com/en-us/windows) documents the official dump-analysis workflow if you want to go deeper.
