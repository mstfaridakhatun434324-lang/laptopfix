---
title: "Windows 11 Automatic Repair Loop on a Lenovo Laptop: 7 Ways Out"
slug: how-to-fix-automatic-repair-loop-windows-11-on-lenovo-laptop
date: 2026-09-08
categories: ["windows-errors"]
tags: ["lenovo", "automatic-repair", "boot-loop"]
description: "Lenovo laptop stuck in an Automatic Repair loop on Windows 11? These 7 methods break the cycle — from bootrec commands to a clean reset."
thumbnail: "/images/thumbs/how-to-fix-automatic-repair-loop-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "What causes the Automatic Repair loop on Lenovo laptops?"
    a: "Windows fails to boot twice in a row, so it launches Automatic Repair — which also fails, and the cycle repeats. Common triggers on Lenovo machines include corrupted boot configuration data after a Windows update, a failing drive, a bad Lenovo BIOS update, or a driver that crashes during early boot. The SrtTrail.txt log it generates usually just says the repair could not fix the problem."
  - q: "Will I lose my files fixing the repair loop?"
    a: "The first six fixes in this guide do not touch your personal files — they repair boot records, run disk checks, and restore system files. Only the last resort, Reset This PC, can remove data, and even then you get a 'keep my files' option. If your data is critical and nothing else works, remove the drive and back it up via another computer before resetting."
  - q: "How do I get to the recovery options on a Lenovo?"
    a: "The loop itself usually drops you at the blue 'Automatic Repair' screen — click Advanced options there. If not, force it: power on, and as soon as the Lenovo logo appears, hold the power button to force off. Repeat three times; on the fourth boot Windows enters the recovery environment. Lenovo's Novo button (the small pinhole button beside the power button on many models) also boots directly to a recovery menu."
  - q: "What is the Novo button and how do I use it?"
    a: "The Novo button is a small recessed button on the side or near the power button of most Lenovo laptops. Power off the laptop, press it with a paperclip, and it opens the Novo Button Menu with direct options for BIOS setup, boot menu, and System Recovery. Choosing System Recovery takes you straight to the recovery tools without fighting the repair loop."
---

Few Windows problems feel as hopeless as the Automatic Repair loop: your Lenovo shows "Preparing Automatic Repair," fails, restarts, and does it all over again. The screen even generates a log file called SrtTrail.txt that essentially says "I tried, I failed." But the loop is breakable — it is almost always corrupted boot data, not a dead laptop.

Here are the seven ways out, ordered from least to most invasive.

## Why this happens

- **Corrupted Boot Configuration Data (BCD).** A Windows update or improper shutdown damages the boot records, so Windows cannot find its own startup files.
- **A failing hard drive or SSD.** If the drive cannot reliably read boot files, every repair attempt fails the same way.
- **Corrupted system files.** Damaged kernel or driver files crash the boot process before the desktop loads.
- **A bad driver update.** A storage or chipset driver that crashes during early boot triggers the loop on every restart.
- **Interrupted Windows updates.** Updates that were force-powered-off mid-install leave the system in a half-upgraded, unbootable state.
- **Lenovo BIOS/firmware issues.** A failed BIOS update or a BIOS setting change (like switching SATA mode) can make the boot drive invisible to Windows.
- **Malware or disk encryption conflicts.** Rare, but rootkits and misconfigured BitLocker can block the boot chain.

## How to fix it

Work through these in order. You will be working in the Windows Recovery Environment (WinRE) for most of them.

### Fix 1: Break the loop and try a plain restart

Sometimes the loop is a one-time glitch that a proper cold boot clears.

1. On the **Automatic Repair** screen, click **Advanced options** → **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**.
2. When the menu appears, press **4** for Safe Mode. If Safe Mode boots, the problem is a driver or startup program — skip to Fix 5.
3. If Safe Mode also fails, return to the recovery menus and continue below.
4. Alternatively, from the Automatic Repair screen choose **Turn off your PC**, unplug everything (including the charger), hold the power button 30 seconds, then plug in and boot. This clears bad hibernation and fast-startup state.

### Fix 2: Rebuild the boot records with bootrec

Corrupted boot data is the most common cause, and these commands rebuild it.

1. From the recovery menus, go to **Troubleshoot** → **Advanced options** → **Command Prompt**.
2. Run these commands one at a time, pressing **Enter** after each:
   `bootrec /fixmbr`
   `bootrec /fixboot` (if this gives "Access denied," continue anyway)
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If `rebuildbcd` finds Windows installations, type `Y` to add them to the boot list.
4. Type `exit`, choose **Continue** to restart, and see if Windows boots.

### Fix 3: Run chkdsk and SFC from the recovery prompt

If the drive or system files are damaged, repair them before rebuilding anything else.

1. In the recovery **Command Prompt**, run `chkdsk C: /f /r`. Note: in WinRE the system drive is sometimes lettered D: — run `diskpart`, then `list volume` to confirm which letter holds Windows.
2. Let chkdsk finish completely; on large drives this takes a while.
3. Then run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter if yours differs).
4. Restart with **Continue** and test.

### Fix 4: Disable Automatic Repair and test a normal boot

Counterintuitive, but disabling the repair itself sometimes lets Windows boot — the repair was the thing failing, not Windows.

1. In the recovery **Command Prompt**, run `bcdedit /set {default} recoveryenabled no`.
2. Also try `bcdedit /set {default} bootstatuspolicy ignoreallfailures`.
3. Type `exit` and choose **Continue**. Windows will now attempt a straight boot instead of detouring into repair.
4. If Windows boots, immediately back up your data, then re-enable repair later with `bcdedit /set {default} recoveryenabled yes` once the system is stable.

### Fix 5: Uninstall the latest update or driver from WinRE

If the loop started right after an update, roll it back without needing to boot.

1. Go to **Troubleshoot** → **Advanced options** → **Uninstall Updates**.
2. Try **Uninstall latest quality update** first, restart, and test.
3. If the loop persists, go back and try **Uninstall latest feature update**.
4. For driver-caused loops: boot into Safe Mode (Fix 1), open **Device Manager**, and roll back the most recently updated driver (right-click → **Properties** → **Driver** → **Roll Back Driver**).
5. Lenovo-specific: check [Lenovo Support](https://support.lenovo.com/us/en/) for a BIOS update or rollback for your exact model — a failed Lenovo BIOS flash is a known loop trigger on some ThinkPad and IdeaPad lines.

### Fix 6: Use System Restore

If restore points exist, this rolls back system files, drivers, and registry to a working state without touching personal files.

1. Go to **Troubleshoot** → **Advanced options** → **System Restore**.
2. Pick the most recent restore point dated before the loop started.
3. Let it complete — the laptop will restart several times.
4. If no restore points exist, this option will say so; move on to Fix 7. (After you recover, turn on System Protection so you have points next time: **Control Panel** → **Recovery** → **Configure System Restore**.)

### Fix 7: Reset This PC

The last resort. It reinstalls Windows and breaks any loop, at the cost of your apps (and optionally your files).

1. Go to **Troubleshoot** → **Reset this PC**.
2. Choose **Keep my files** first — this removes apps and settings but preserves personal data.
3. If that fails or the loop returns, repeat with **Remove everything** for a truly clean slate (back up first if at all possible).
4. After the reset, install drivers from [Lenovo Support](https://support.lenovo.com/us/en/) using your serial number before running Windows Update, so Lenovo's tuned drivers land first.

## Closing

The Automatic Repair loop looks catastrophic but it is usually just broken boot data — Fix 2's `bootrec` sequence alone gets a huge share of Lenovo laptops booting again. The key mistake to avoid is letting the loop run for hours hoping it resolves itself; it will not, and on a failing drive those repeated read attempts can make things worse. Break the cycle, work the fixes in order, and back up the moment you get back in. If the loop's log file mentions SrtTrail.txt specifically, our [SrtTrail.txt error guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-in-windows-11-24h2/) digs into that log, and ASUS owners should see the [ASUS automatic repair loop](/articles/how-to-fix-automatic-repair-loop-windows-11-on-asus-laptop/) variant.
