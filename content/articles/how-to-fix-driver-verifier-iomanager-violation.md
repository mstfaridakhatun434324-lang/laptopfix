---
title: "How to Fix Driver Verifier IOManager Violation Blue Screen"
slug: how-to-fix-driver-verifier-iomanager-violation
date: 2026-09-19
categories: ["windows-errors"]
tags: ["blue screen", "driver verifier", "driver error"]
description: "Driver Verifier IOManager Violation keeps blue-screening your laptop? Here's how to find the bad driver and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-iomanager-violation.webp"
faqs:
  - q: "What is Driver Verifier IOManager Violation?"
    a: "Stop code 0x000000C9: Microsoft's Driver Verifier tool caught a driver breaking the rules for I/O operations — mishandling IRPs (I/O request packets) or calling I/O routines incorrectly. Verifier intentionally crashes the system to expose the bug rather than letting it corrupt things silently."
  - q: "I never turned on Driver Verifier. Why am I getting this error?"
    a: "Someone or something enabled it — a troubleshooting tutorial you followed, a driver installer, or enterprise management software. Run verifier.exe, choose 'Delete existing settings,' and restart. But still find and fix the flagged driver, because the underlying bug is real."
  - q: "How do I find which driver Verifier flagged?"
    a: "The crash dump names it. Open the minidump in C:\\Windows\\Minidump with a dump viewer, or check Event Viewer > Windows Logs > System for the BugCheck entry. The faulting driver is usually listed right at the top of the stack."
  - q: "Can I just leave Driver Verifier running after fixing the driver?"
    a: "No — turn it off once you're done diagnosing. Verifier deliberately stresses drivers and slows the system; it's a lab tool, not a safety feature. Leaving it on invites more crashes and noticeably worse performance."
---
DRIVER_VERIFIER_IOMANAGER_VIOLATION is a special kind of blue screen: it's not a random failure, it's a *caught* failure. Driver Verifier is a Windows testing tool that watches drivers for rule-breaking, and when it sees a driver mishandle an I/O operation, it deliberately crashes the system with stop code 0x000000C9 and points at the offender. Think of it as a speed camera — the crash is the ticket, and the ticket names the driver.

The most common story I hear: someone followed a "fix blue screens" tutorial months ago that said to enable Driver Verifier, forgot about it, and now gets these crashes out of nowhere. Whether you turned it on yourself or it came on some other way, the playbook is the same: identify the flagged driver, fix or remove it, then turn Verifier off.

## Why this happens

- **Driver Verifier is enabled and doing its job.** This is the prerequisite for the error — without Verifier running, the same driver bug would cause subtler problems (or different crashes) instead of this specific stop code.
- **A driver mishandles I/O request packets.** The flagged driver is completing IRPs twice, freeing them incorrectly, calling I/O routines at the wrong time, or otherwise breaking the I/O manager's rules. Storage, network, and USB drivers are the usual violators.
- **An outdated driver meets a new Windows build.** Drivers written for older Windows versions sometimes use I/O patterns that newer builds police more strictly. Feature updates are a classic trigger for Verifier crashes that didn't happen before.
- **Third-party filter drivers.** Antivirus file-system filters, disk encryption drivers, and backup software install filter drivers that intercept every I/O operation — prime territory for I/O rule violations.
- **Beta or unsigned drivers.** Experimental GPU drivers, developer hardware drivers, and unsigned community drivers haven't been through Microsoft's validation and break the rules more often.
- **Corrupted driver installation.** Sometimes the driver code is fine but its installation is mangled — mixed versions of the .sys file and its supporting files behave unpredictably under Verifier's scrutiny.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Turn off Driver Verifier

Stop the deliberate crashes first so you can work in peace.

1. Boot into **Safe Mode** if normal boot keeps crashing: interrupt the boot three times at the manufacturer's logo to reach **Choose an option**, then **Troubleshoot > Advanced options > Startup Settings > Restart**, and press **4**.
2. Press **Win + R**, type `verifier`, and press Enter.
3. Select **Delete existing settings**, click **Finish**, and restart normally.
4. The crashes should stop immediately — but remember, Verifier was catching a real bug. Don't skip the remaining fixes, or the bad driver will keep misbehaving quietly. (Our deeper dive into the [24H2-specific variant](/articles/how-to-fix-driver-verifier-iomanager-violation-in-windows-11-24h2/) covers cases where a feature update is the trigger.)

### Fix 2: Identify the flagged driver from the crash dump

Before the dumps get overwritten, find out who Verifier caught.

1. Open **Event Viewer** (**Win + R**, type `eventvwr.msc`), go to **Windows Logs > System**, and find the **BugCheck** error entries. The details often name the driver file directly.
2. For the full picture, look in `C:\Windows\Minidump` for `.dmp` files dated at your crashes. Open the newest one with a dump analysis tool — the faulting driver appears at the top of the stack trace.
3. Write down the exact filename (e.g., `rt640x64.sys`, `e1d65x64.sys`, `somefilter.sys`) and Google it with "driver" — you'll quickly learn which hardware or software it belongs to.
4. If the dumps are inconclusive, re-enable Verifier *temporarily* with standard settings on the suspect driver only, reproduce one crash, then disable it again — one more targeted crash for a definitive answer.

### Fix 3: Update the offending driver

A fixed driver version is the cleanest resolution.

1. Identify the hardware from Fix 2, then get the driver from the right source: your laptop manufacturer's support page first ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo's support site), since their versions are validated for your model.
2. For network drivers (extremely common Verifier offenders), check the chip maker's site too — Intel and Realtek both publish newer drivers than most laptop vendors repackage.
3. Install, restart, and use the laptop normally for several days. I/O violations are usually deterministic — if the trigger scenario recurs without a crash, you're fixed.
4. If the manufacturer's driver is old, try the chip maker's latest as a second option — but keep the old installer handy in case you need to roll back.

### Fix 4: Roll back or reinstall the driver

If the crashes started with a driver update, undo it.

1. Open **Device Manager** (**Win + X**), find the device, right-click, choose **Properties > Driver > Roll Back Driver**.
2. If rollback isn't available, choose **Uninstall device**, tick **Attempt to remove the driver for this device**, restart, and let Windows install its inbox driver.
3. Test thoroughly. The inbox driver may lack fancy features but it's the most rule-abiding option available.
4. Block Windows from "helpfully" reinstalling the bad version: in **Device Manager**, after installing your chosen driver, you can use the **Show or hide updates** troubleshooter from [Microsoft support](https://support.microsoft.com/en-us/windows) to hide the problematic driver update.

### Fix 5: Remove the offending filter software

If the flagged driver belongs to antivirus, encryption, or backup software, the software has to go (or be updated).

1. Identify the owning program from the driver name you found in Fix 2.
2. Uninstall it via **Settings > Apps > Installed apps** — and use the vendor's dedicated removal tool if they offer one, since filter drivers often survive normal uninstalls.
3. Restart and confirm stability for a day or two.
4. If you need the software's function, reinstall the *latest* version from the vendor — filter driver bugs get fixed, and the current release likely behaves. Or switch to a competitor whose driver passes Verifier cleanly. Filter-driver conflicts are also a classic trigger for [System Service Exception](/articles/system-service-exception-windows-11-fix/) crashes, if you want to compare symptoms.

### Fix 6: Run SFC and DISM to rule out system corruption

Make sure the violated rules aren't a symptom of corrupted Windows files.

1. Open **Terminal (Admin)** (**Win + X**) and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` (stay connected to the internet).
3. Restart and retest. This rarely *is* the fix for a C9 stop code, but it eliminates a variable — and if system files were corrupt, the driver may have been a victim rather than the culprit.
4. If corruption keeps recurring after repair, run `chkdsk C: /f /r` to check the drive itself.

### Fix 7: Clean-install the driver stack as a last resort

When a driver is tangled beyond updating, wipe the slate.

1. In Safe Mode, uninstall the device *and* its software from **Device Manager** and **Installed apps**, ticking driver removal everywhere it's offered.
2. Use a driver cleanup utility appropriate to the device type (Display Driver Uninstaller for GPUs is the gold standard; network drivers usually clean up fine manually).
3. Restart and install only the single driver version you've chosen — manufacturer's validated version preferred — with no bundled "control center" extras.
4. Verify with a brief, targeted Verifier run: enable it for just that driver, exercise the device (copy files for storage, stream for network), confirm no crash, then delete Verifier settings again. Clean bill of health.

## Closing

The mindset shift that fixes this error fastest: Driver Verifier is not your enemy, it's your informant. It already did the hard diagnostic work by naming the guilty driver in the crash dump — most blue screens don't give you that gift. Read the dump, fix or remove that one driver, turn Verifier off, and move on. And if you ever follow another tutorial that says "enable Driver Verifier to diagnose crashes," set yourself a reminder to turn it off when you're done — future you will appreciate it.
