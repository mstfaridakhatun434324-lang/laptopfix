---
title: "\"Your PC Ran Into a Problem\"? Here's How to Fix It on Windows 11"
slug: how-do-i-fix-your-pc-ran-into-a-problem
date: 2026-10-01
categories: ["windows-errors"]
tags: ["your pc ran into a problem", "blue screen", "windows 11", "stop code", "crash"]
description: "Stuck on 'Your PC ran into a problem and needs to restart'? Here's how to fix it — from reading the stop code to driver, update, and hardware checks."
thumbnail: "/images/thumbs/how-do-i-fix-your-pc-ran-into-a-problem.webp"
faqs:
  - q: "What does 'Your PC ran into a problem' actually mean?"
    a: "It's Windows 11's friendly face for a blue screen crash — technically a bug check. The kernel hit an error it couldn't recover from: a faulty driver, corrupt system files, bad RAM, or failing hardware. The screen shows a stop code (like CRITICAL_PROCESS_DIED) and sometimes a failing file name. That code is the starting point for every fix below; photograph the screen before it restarts."
  - q: "Will I lose my files when this happens?"
    a: "The crash itself doesn't delete files — it's a system halt, not a disk wipe. Your documents and photos are almost certainly intact. The fixes in this guide (driver rollbacks, Startup Repair, update removal, system file scans) all preserve personal data. Only a full reset with 'Remove everything' would delete files, and that's presented as an explicit last resort."
  - q: "Why does it happen randomly and not all the time?"
    a: "Intermittent crashes usually mean a driver bug triggered by specific conditions (sleep/wake, heavy load, a particular device), marginal hardware like a RAM stick with occasional errors, or overheating that only peaks under load. Note what you were doing each time it crashed — the pattern is diagnostic. Random-looking crashes are rarely actually random."
  - q: "How do I stop it from restarting so fast I can't read the error?"
    a: "Disable automatic restart on system failure. In the recovery environment: Troubleshoot > Advanced options > Startup Settings > Restart, then press 9. Once Windows boots, set it permanently in System Properties > Advanced > Startup and Recovery by unticking 'Automatically restart'. The blue screen will then wait for you to read and photograph it."
---

"Your PC ran into a problem and needs to restart." It's the most unhelpful helpful message in computing — it tells you something broke while telling you nothing about what. Behind that sad emoticon is a full technical crash report: a stop code, sometimes a culprit file, and a memory dump with the complete story. Your job is to extract that information and act on it.

This screen appears for the same reasons as any blue screen: a driver crashed the kernel, system files are corrupt, RAM is faulty, or hardware is failing. The fixes don't depend on the friendly wording — they depend on the stop code hiding in the small print. So step one is always the same: read the screen properly. Then work the standard crash-triage order below: recent changes first, drivers second, system files third, hardware last. For the deep-dive on any specific stop code, our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the most common ones individually.

## Why this happens

- **Faulty or outdated driver**: The single most common cause — a driver bug crashes the kernel, and Windows halts to protect itself.
- **Bad Windows update**: Updates replace drivers and system files; a buggy one can start crashes the morning after installation.
- **Corrupt system files**: Disk errors or interrupted updates damage core Windows files until something critical fails.
- **Failing RAM**: Bad memory corrupts kernel data structures, producing crashes that name innocent drivers.
- **Overheating**: A CPU or GPU exceeding safe temperatures becomes unstable and crashes under load.
- **Failing drive**: Bad sectors on system files or the paging file cause crashes that worsen over time.
- **New hardware or peripherals**: A new device with a broken driver, or a failing USB device, can crash the system on connection or during use.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the screen and capture the stop code

Everything downstream depends on this thirty-second step.

1. The next time the screen appears, photograph it with your phone. Capture the stop code in capital letters (e.g., SYSTEM_SERVICE_EXCEPTION), any file named below it (e.g., `ntfs.sys`), and the QR code.
2. If the screen restarts too fast to read, disable automatic restart: force the recovery environment with three interrupted boots, go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, press **9**.
3. Note what you were doing when it crashed — gaming, waking from sleep, plugging in a device, or nothing at all. Write down the last three crashes' circumstances.
4. Look up the stop code's meaning — the name plus the activity pattern usually points at a subsystem (storage, network, graphics, memory).

### Fix 2: Undo whatever changed most recently

Crashes that start after a change are usually caused by the change.

1. Open **Settings** > **Windows Update** > **Update history**. If a quality or driver update landed just before the crashes started, uninstall it (**Uninstall updates**) and test.
2. Open **Device Manager**, check recently updated devices, and use **Roll Back Driver** where available.
3. Think about software: new antivirus, VPN, game anti-cheat, or "optimizer" installed recently? Uninstall it and test — these install kernel drivers that crash systems.
4. If you added new hardware (RAM, SSD, dock, USB device), remove it and test. New-hardware crashes are almost always the new hardware's driver.

### Fix 3: Boot into Safe Mode to confirm it's software

Safe Mode loads a minimal driver set — stability there implicates third-party drivers.

1. Force WinRE (three interrupted boots), then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **4**.
2. If Safe Mode is stable, the problem is a third-party driver or startup program — proceed to clean-boot isolation in Fix 4.
3. If Safe Mode also crashes, suspect core system files or hardware — skip to Fix 5.
4. While in Safe Mode, you can also run the system file repairs (Fix 5) with fewer running processes interfering.

### Fix 4: Clean-boot to find the culprit

Binary-search your software until the crasher reveals itself.

1. Press **Windows + R**, type `msconfig`, go to the **Services** tab, tick **Hide all Microsoft services**, click **Disable all**.
2. In **Task Manager** > **Startup apps**, disable everything non-Microsoft. Restart normally.
3. If crashes stop, re-enable services in halves, rebooting and testing each time, until crashes return. The last group contains the culprit.
4. Update, replace, or remove the offending software. Common winners of this contest: third-party antivirus filters, VPN clients, RGB control software, and motherboard "utility" suites.

### Fix 5: Repair system files and check the disk

Fix the OS itself when software isolation doesn't name a culprit.

1. Open **Windows Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth` — wait for full completion.
2. Run `sfc /scannow`, then restart.
3. Run `chkdsk C: /f` (schedule at reboot if asked) to rule out file-system damage.
4. If SFC finds corruption it can't repair even after DISM, note it — that's unusual and worth an in-place upgrade repair install rather than repeated scans. Microsoft documents these utilities on their [support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Check temperatures and test the RAM

Rule out the two hardware causes that masquerade as software.

1. Install HWMonitor and check CPU/GPU temperatures under load. Sustained readings above 90–95°C on a laptop mean thermal instability — clean the vents and fans.
2. Run Windows Memory Diagnostic: **Windows + R** > `mdsched.exe` > **Restart now and check for problems**.
3. For certainty, run MemTest86 overnight from a USB stick — it catches marginal RAM faults the quick test misses.
4. Bad RAM is the great impersonator: it corrupts random drivers, producing a different stop code every crash. Multiple different stop codes across crashes is the classic RAM signature.

### Fix 7: Update drivers properly from the manufacturer

When rollbacks aren't the answer, clean updates are.

1. Get chipset, storage, network, and graphics drivers from your laptop maker's support page — [Dell](https://www.dell.com/support), HP, Lenovo — not just Windows Update.
2. For graphics, do a clean install: use DDU in Safe Mode to remove the old driver, then install the fresh download from NVIDIA, AMD, or Intel.
3. Update the BIOS too if yours is old — firmware fixes resolve entire categories of crashes.
4. Update one driver category at a time and test between them, so you know which one mattered.

### Fix 8: Reset Windows as the final software verdict

When everything points at software but nothing names it, start the software over.

1. Back up your files (they should be preserved, but back up anyway — it's the last resort for a reason).
2. Go to **Settings** > **System** > **Recovery** > **Reset this PC**. Try **Keep my files** first.
3. If crashes persist after a reset, it's hardware — the drive and RAM are the prime suspects. Test or replace them.
4. If even the reset fails to complete, the drive is likely the problem — replace it and clean-install from USB media created with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11). For crashes that specifically loop at boot, our [automatic repair guide](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) covers the boot-specific recovery path.

## Closing

"Your PC ran into a problem" is Windows being polite about a kernel crash — and politeness aside, it's one of the most diagnosable problems you can have. Photograph the stop code, undo recent changes, confirm with Safe Mode, isolate with a clean boot, repair the system files, and test the hardware, in that order. Most cases end at step two or three: a bad update, a bad driver, a piece of software that didn't belong in the kernel. The crashes feel random until you log them; once you log them, the pattern usually points straight at the cause.
