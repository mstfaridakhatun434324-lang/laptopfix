---
title: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: A Practical Fix Guide"
slug: how-to-fix-attempted-execute-of-noexecute-memory-youtube
date: 2026-09-05
categories: ["windows-errors"]
tags: ["windows 11", "blue screen", "memory", "drivers"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen? Here's what it means in plain English and the practical steps to stop it."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-youtube.webp"
faqs:
  - q: "What does ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY mean in simple terms?"
    a: "Windows marks some memory regions as non-executable — data can live there, but code may not run from there. This error means something tried to run code from such a region. It's a security tripwire: either a driver has a bug, or malicious code tried to execute. On home laptops, a buggy driver is the cause the vast majority of the time."
  - q: "Is this blue screen caused by a virus?"
    a: "Rarely, but it's worth checking. The no-execute protection (DEP/NX) exists partly to stop malware, so a scan is sensible. In practice, though, this stop code on Windows 11 laptops comes from faulty drivers — especially graphics, audio, and storage drivers — far more often than from malware."
  - q: "Why did it start after a Windows update?"
    a: "Updates replace drivers and change memory management behavior. A driver that previously stayed inside its allowed memory regions can start straying after an update changes timing or addresses. Rolling back the recently updated driver is the fastest fix in these cases."
  - q: "How do I find which driver caused it?"
    a: "Check C:\\Windows\\Minidump with BlueScreenView — it highlights the faulting driver. The stop code is 0x000000FC. Once you have the driver filename, update or roll back that specific driver in Device Manager rather than updating everything blindly."
---

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: A Practical Fix Guide

If you landed here after a YouTube tutorial sent you searching, welcome — you're in the right place, and you don't need to watch another 12-minute video with a robot voice. ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is a mouthful, but the idea is simple: Windows caught something trying to run program code from a memory area marked "data only," and crashed to stop it. Think of it as a bouncer catching someone climbing through the kitchen window instead of using the door.

On Windows 11 laptops, the "someone" is almost always a buggy driver, not a hacker. This guide gives you the practical fix sequence — find the driver, fix the driver — without the fluff. If you're collecting stop codes, our main [Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the whole family.

## Why this happens

- **A driver tried to execute non-executable memory.** Buggy drivers sometimes jump to wrong addresses; DEP (Data Execution Prevention) catches it and Windows bugchecks.
- **A Windows update changed memory layout.** Address changes can expose latent driver bugs that previously went unnoticed.
- **Corrupted driver files.** A half-updated driver can contain garbage addresses that point into no-execute regions.
- **Failing RAM.** Bad memory cells corrupt pointers, sending execution off into data regions.
- **Malware attempting code injection.** Rare on patched home systems, but the NX protection exists for exactly this — worth one scan.
- **Overclocked or unstable memory.** Bad timings corrupt the addresses drivers compute, with the same result.

## How to fix it

Work through these in order. Identifying the driver first saves the most time.

### Fix 1: Identify the faulting driver from the dump

Don't guess — read the crash dump.

1. Get to a stable state (Safe Mode if needed) and confirm dumps exist in `C:\Windows\Minidump`.
2. Run BlueScreenView and look for stop code `0x000000FC`.
3. Note the driver highlighted in red — that's the one that attempted the illegal execution.
4. Search the filename with your laptop model to identify the device it belongs to. If several different drivers appear across multiple dumps, that's a hint the real problem is RAM or another shared cause rather than any single driver — jump to Fix 5 in that case. Consistent blame on one driver, crash after crash, means you've found your target.

### Fix 2: Update the suspect driver properly

A fixed driver stays inside its own memory.

1. Open **Device Manager** (**Win + X > Device Manager**), find the device, right-click, and choose **Update driver > Search automatically for drivers**.
2. If Windows finds nothing, download the driver from your laptop maker's support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — use your exact model.
3. For Intel wireless or Bluetooth drivers, Intel's Driver & Support Assistant tool finds the right version automatically.
4. Reboot and use the laptop normally for a day to confirm the crashes stop.

### Fix 3: Roll back if the crash followed an update

New driver + new crash = rollback.

1. In **Device Manager**, open the suspect device's **Properties > Driver** tab.
2. Click **Roll Back Driver**, pick a reason, and confirm.
3. Also check **Settings > Windows Update > Update history > Driver updates** to see what arrived recently.
4. If the system is otherwise stable on the old driver, hide the bad version with Microsoft's "Show or hide updates" troubleshooter so it isn't reinstalled.

### Fix 4: Run a malware scan

Quick, free, and rules out the scary explanation.

1. Open **Windows Security** (**Win + S**, type `Windows Security`), go to **Virus & threat protection**.
2. Click **Scan options**, choose **Microsoft Defender Offline scan**, and click **Scan now** — the laptop reboots into a clean environment for the scan.
3. Remove anything found, then reboot normally.
4. A clean scan plus continued crashes confirms it's a driver issue, not malware — proceed with the remaining fixes.

### Fix 5: Test your RAM

Bad memory corrupts pointers, which looks exactly like this error.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Use **Extended** mode (press **F1** during the test) for a thorough check.
3. Read results afterward in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
4. Errors mean the RAM is bad — reseat the modules or replace the faulty stick. Memory-focused crashes are also covered in our [memory management BSOD guide](/articles/memory-management-bsod-windows-11-fix/).

### Fix 6: Verify DEP is enabled and repair system files

Make sure the protection itself is intact, and fix any corrupted components.

1. Open an elevated **Command Prompt** and check DEP status with:
   `wmic OS Get DataExecutionPrevention_SupportPolicy`
   A value of `2` or `3` means it's on (OptIn/OptOut). If it's `0` (AlwaysOff), re-enable with:
   `bcdedit /set nx OptIn`
2. Then run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Reboot. If a tutorial ever told you to disable DEP/NX to "fix" crashes, re-enable it — disabling a security tripwire to hide crashes is never the answer.

### Fix 7: Reset BIOS memory settings

Unstable RAM timings are a quiet cause of pointer corruption.

1. Enter BIOS (**F2**/**Del** during the logo, varies by maker).
2. Disable **XMP**/**EXPO** or any memory overclocking, and **Load Optimized Defaults**.
3. Save and exit, then monitor for a day or two.
4. If crashes persist after all fixes, compare with the closely related [special pool memory corruption fix](/articles/how-to-fix-special-pool-detected-memory-corruption-on-lenovo-laptop/) — the two errors share root causes. Microsoft documents bugcheck codes further in its Windows support documentation.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY sounds like a cyberattack, but it's usually just a driver that wandered where it shouldn't. Read the dump, fix that driver, give the RAM a quick test, and run one offline malware scan for peace of mind. Do those four things and the bouncer can go back to standing quietly by the door instead of shutting down the whole club — no YouTube rabbit hole required.
