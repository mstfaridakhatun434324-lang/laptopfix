---
title: "Windows 11 Stuck in Automatic Repair Loop? Here's the Fix"
slug: automatic-repair-loop-windows-11-troubleshooting
date: 2026-09-07
categories: ["windows-errors"]
tags: ["automatic repair", "boot loop", "windows 11", "startup repair"]
description: "Windows 11 keeps saying 'Preparing Automatic Repair' and never boots? Here's how to break the loop — from quick fixes to full repairs."
thumbnail: "/images/thumbs/automatic-repair-loop-windows-11-troubleshooting.webp"
faqs:
  - q: "Why is Windows 11 stuck in an Automatic Repair loop?"
    a: "Windows failed to boot, launched Automatic Repair, the repair failed, and now it repeats forever. Common triggers: a bad update, corrupt boot files (BCD), a changed BIOS storage mode, or a failing drive that the repair tool can't fix."
  - q: "Will I lose my files breaking the loop?"
    a: "No — the fixes below repair boot data and system files without touching personal files. Only a full 'Reset this PC > Remove everything' would delete data, and that's presented as a last resort, not a first step."
  - q: "What if Automatic Repair says it couldn't repair my PC?"
    a: "That's expected — the built-in repair is limited. The manual fixes below (BCD rebuild, startup repair from installation media, update rollback) succeed where the automatic tool fails. Don't give up at that message."
  - q: "How do I stop the loop from happening again?"
    a: "Fix the root cause: if it was a bad update, pause updates until it's resolved; if it was a drive issue, replace the drive; if a BIOS setting changed, correct it. Also disable automatic restart-on-failure temporarily so you can see the real error next time."
---

The Automatic Repair loop is uniquely frustrating: your laptop shows "Preparing Automatic Repair," thinks for a while, announces it couldn't repair your PC, restarts — and does it all again. Forever. The loop itself isn't the problem; it's a symptom. Something is preventing Windows from booting, and the automatic tool isn't equipped to fix it. The manual fixes below are.

Before diving in: your files are almost certainly fine. This is a boot problem, not a data problem. Work through the fixes in order — they go from the quickest wins to the deeper repairs. If your loop shows a specific stop code on the blue screen first, our [blue screen troubleshooting guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) helps identify it; the loop-breaking steps here apply regardless.

## Why this happens

- **Corrupt Boot Configuration Data (BCD)**: The most common cause. The BCD tells Windows how to start; when it's damaged, every boot attempt fails and triggers the repair loop.
- **A failed Windows update**: Updates modify boot files. An interrupted or buggy update leaves the boot chain broken — the repair tool can't fix what the update broke.
- **BIOS storage mode changed**: A BIOS update or reset flipping between RAID and AHCI makes Windows unable to find its drive, failing every boot identically.
- **Failing drive**: Bad sectors on boot-critical files cause consistent boot failure. Automatic Repair can't repair physically damaged storage.
- **Corrupted system files**: Damage to core Windows files that load early in boot.
- **Recently installed drivers**: A bad storage or chipset driver installed just before the loop started.
- **Fast Startup state corruption**: The hybrid-shutdown hibernation file can become corrupt, breaking every "fast" boot in an identical way.

## How to fix it

Work through these in order — start inside the recovery environment you're already landing in.

### Fix 1: Break the loop and boot into Safe Mode

First, escape the cycle so you can work.

1. On the "Automatic Repair couldn't repair your PC" screen, click **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
2. Press **4** for Safe Mode. If Windows boots in Safe Mode, the problem is a driver or startup program — skip to Fix 6.
3. If Safe Mode also fails, return to **Advanced options** > **Command Prompt** and continue with Fix 2.

### Fix 2: Rebuild the BCD

The core fix for most repair loops.

1. From **Advanced options**, open **Command Prompt**.
2. Run these commands one at a time:
   - `bootrec /fixmbr`
   - `bootrec /fixboot`
   - `bootrec /scanos`
   - `bootrec /rebuildbcd`
3. If `rebuildbcd` reports zero Windows installations found, do the manual rebuild:
   - `diskpart` → `list vol` → find the FAT32 **EFI** partition, `select vol N`, `assign letter=Z:`, `exit`
   - `bcdboot C:\Windows /s Z: /f UEFI` (verify your Windows drive letter first with `dir C:` — in recovery it may be **D:**)
4. Type `exit`, choose **Continue**, and boot.

### Fix 3: Disable automatic restart and early-launch anti-malware

Sometimes the loop is sustained by settings rather than corruption.

1. From **Advanced options** > **Startup Settings** > **Restart**, press **9** to **Disable automatic restart after failure** — this at least shows you the real stop code instead of looping.
2. Separately, try **8** to **Disable driver signature enforcement** — if a recent driver is the problem, this can get you booted.
3. If either gets you into Windows, immediately update or roll back the suspect driver.

### Fix 4: Uninstall the latest update from recovery

If the loop started within a day of an update, this is likely your fix.

1. Go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Try **Uninstall the latest quality update** first, then restart.
3. If still looping, go back and try **Uninstall the latest feature update**.
4. Once booted, pause updates (**Settings** > **Windows Update** > **Pause updates**) and check [Microsoft's support site](https://support.microsoft.com/en-us/windows) for known issues with that update.

### Fix 5: Run offline SFC and chkdsk

Repair system files and check the disk without needing Windows to boot.

1. Open **Command Prompt** from **Advanced options**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter to your Windows drive).
3. Run `chkdsk C: /f /r` (same letter adjustment) and let the full scan complete.
4. Type `exit` and choose **Continue**.

If chkdsk finds many bad sectors, suspect the drive — continue to Fix 7 before celebrating.

### Fix 6: Disable Fast Startup and clean-boot

If you can boot into Safe Mode (Fix 1), these steps address the common software causes.

1. In Safe Mode, open **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable** and untick **Turn on fast startup**.
2. Press **Windows + R**, type `msconfig`, go to the **Services** tab, tick **Hide all Microsoft services**, and click **Disable all**.
3. In **Task Manager** > **Startup apps**, disable everything non-Microsoft.
4. Restart normally. If it boots, re-enable services in groups to find the culprit.

### Fix 7: Check the drive health

A loop that survives BCD rebuilds and update rollbacks points at hardware.

1. Boot your laptop manufacturer's diagnostics (usually **F12** > **Diagnostics**, or **F2** for HP's hardware diagnostics) and run the full drive test.
2. Alternatively, from the recovery **Command Prompt**, the chkdsk results from Fix 5 tell the story — growing bad-sector counts mean a dying drive.
3. If the drive is failing: back up immediately (connect the drive to another PC or boot a live Linux USB), replace the drive, and reinstall Windows. Your files are recoverable as long as you act before total failure.

### Fix 8: Reset Windows (keep your files)

The last resort that preserves your data.

1. From **Advanced options**, go to **Troubleshoot** > **Reset this PC**.
2. Choose **Keep my files**. This reinstalls Windows, removes apps and settings, but preserves personal files.
3. If even this fails, the drive is almost certainly the problem — replace it and do a clean install from USB media created with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11).

## Closing

The Automatic Repair loop feels like a dead end, but it's really just Windows admitting its automatic tool isn't enough — the manual BCD rebuild in Fix 2 alone breaks the loop in most cases. The important discipline is fixing the root cause afterward, not just the boot: a loop caused by a bad update will recur when the update reinstalls, and a loop caused by a dying drive will recur until the drive is replaced. Break the loop, then make sure it stays broken. For the related case where Windows boots but immediately blue-screens, our [Safe Mode troubleshooting guide](/articles/best-way-to-fix-windows-11-safe-mode-not-working/) picks up where this one leaves off.
