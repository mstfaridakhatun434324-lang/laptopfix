---
title: "Windows Update Stuck on Restarting Screen: Full Troubleshooting Guide"
slug: "windows-update-stuck-on-restarting-screen-troubleshooting"
date: 2026-09-01
categories: ["windows-update"]
tags: ["windows update", "restarting screen", "troubleshooting", "boot loop", "laptop"]
description: "A complete troubleshooting walkthrough for Windows Update frozen on the Restarting screen: diagnosis, recovery environment repairs, and prevention."
thumbnail: "/images/thumbs/windows-update-stuck-on-restarting-screen-troubleshooting.webp"
faqs:
  - q: "What’s the difference between shutdown-side and boot-side hangs?"
    a: >
      Shutdown-side: the ‘Restarting’ screen with spinning dots never goes
      black — drivers or services won’t stop. Boot-side: the screen goes
      black, the logo appears, then it hangs — the update’s boot phases or
      driver migration failed. The distinction directs your repair:
      shutdown-side hangs respond to driver triage in Safe Mode, while
      boot-side hangs need WinRE tools like Startup Repair, System
      Restore, or BCD rebuilds.
  - q: "How do I get into the Recovery Environment?"
    a: >
      Interrupt the boot twice by holding the power button during the
      Windows logo. On the third boot, Automatic Repair launches WinRE,
      where Troubleshoot > Advanced options holds the repair tools. The
      timing matters: press and hold power as soon as the logo or spinning
      dots appear, before Windows loads. After two interrupted boots, the
      firmware hands control to the recovery partition automatically.
  - q: "Will System Restore delete my files?"
    a: >
      No. System Restore reverts system files, drivers, and registry to
      the restore point but leaves your personal files alone. It is one of
      the safest recovery options available. Your documents, photos, and
      downloads are explicitly excluded from restore operations. It can
      remove recently installed programs and drivers — which is often
      exactly what you want when a bad update caused the problem — but
      your data stays put.
  - q: "When should I reset instead of repairing?"
    a: >
      When DISM/SFC from WinRE cannot complete, Startup Repair fails
      repeatedly, and no restore point exists. Reset-with-files-kept is
      the middle ground before a full clean install. The reset reinstalls
      Windows while preserving your personal files, giving you a fresh
      system without the nuclear option. Try it when you have exhausted
      the targeted repairs but want to avoid manually backing up and
      reinstalling everything.
---

This is the full troubleshooting reference for a Windows laptop frozen on the ‘Restarting’ screen during or after Windows Update — the companion to the quick-fix guide, going deeper into diagnosis and the Windows Recovery Environment. If you have already waited, force-restarted, and the machine still will not get past the screen, this is where you work next.

Troubleshooting this properly means answering one question first: is the machine failing to shut down, or failing to come back up? A shutdown-side hang (dots spin forever, never goes black) points at drivers and services refusing to stop. A boot-side hang (screen goes black, then stuck on Restarting or the logo) points at the update’s boot phases or driver migration. The distinction decides which recovery tools you reach for.

Below is the complete sequence: observation, forced recovery into WinRE, startup repair, command-line servicing repairs, driver triage, and the last-resort options — each with the exact steps. If you are dealing with a related symptom instead, see [the best-practice fix order for a stuck restarting screen](/articles/best-way-to-fix-windows-update-stuck-on-restarting-screen/) and [Windows Update stuck while downloading on Acer](/articles/how-to-fix-windows-update-stuck-downloading-on-acer-laptop/).

This guide picks up where the quick fixes leave off: you have waited, you have force-restarted, and the machine still will not get past the screen. Proper troubleshooting now means answering one question — is it failing to shut down, or failing to come back up? — because that single distinction decides whether you triage drivers in Safe Mode or rebuild boot structures in the Recovery Environment. Everything below follows from that diagnosis.

## Why this happens

- **Driver refusing to unload at shutdown** shutdown-side hangs come from drivers that will not stop.

- **Failed driver migration at boot** boot-side hangs come from the new driver set failing to start.

- **Corrupt boot configuration data** the update’s boot changes left BCD inconsistent.

- **Damaged servicing state** half-committed update phases confuse the boot sequence.

- **Failing storage** a dying drive stalls on the heavy I/O of update finalization.

- **Peripheral driver deadlock** USB device drivers deadlock the restart handoff.

- **Interrupted earlier update** a previous forced shutdown left the update half-applied.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Classify the hang: shutdown-side or boot-side

The diagnosis that directs everything else. Write down which type you observe before doing anything else; every fix below branches on this diagnosis, and guessing wrong wastes real time.

1. Force-power-off, unplug USB devices, and power on while watching carefully.

2. If it hangs on ‘Restarting’ with spinning dots and never goes black: shutdown-side.

3. If it goes black, shows the logo, then hangs: boot-side.

4. Note which one — the fixes below split on this.

### Fix 2: Enter the Windows Recovery Environment

WinRE is your workshop when Windows will not boot normally. If the recovery screen never appears after three interrupted boots, create Windows 11 media on another PC — you will need it for the later steps anyway.

1. Force-power-off during boot twice in a row to trigger Automatic Repair.

2. On the recovery screen choose Troubleshoot > Advanced options.

3. You now have Startup Repair, System Restore, and Command Prompt available.

### Fix 3: Run Startup Repair and System Restore

The two gentlest WinRE fixes. Try Startup Repair first even when you doubt it will work; it is fast, safe, and occasionally fixes exactly the boot damage an update leaves behind.

1. First try Startup Repair and let it complete.

2. If that fails, open System Restore and roll back to a restore point from before the update.

3. Restart and observe whether the hang is gone.

### Fix 4: Repair servicing from the WinRE command prompt

For damaged update state blocking boot. Drive letters shift in WinRE, so double-check with diskpart before running commands — targeting the wrong volume is the main way this step goes wrong.

1. In WinRE, open Command Prompt.

2. Identify the Windows drive letter (often D: in WinRE) with: diskpart, list volume, exit.

3. Run: DISM /Image:D:\ /Cleanup-Image /RestoreHealth (adjust the letter).

4. Then: sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows.

5. Restart and test.

### Fix 5: Rebuild the boot configuration data

For boot-side hangs with BCD damage. On modern UEFI systems the bcdboot method is more reliable than the legacy bootrec commands, so prefer it when the laptop uses UEFI firmware.

1. In the WinRE Command Prompt, run: bootrec /fixmbr, bootrec /fixboot, bootrec /rebuildbcd.

2. On UEFI systems, if fixboot reports access denied, use the bcdboot method: bcdboot D:\Windows (adjust letter).

3. Restart and test.

### Fix 6: Triage drivers in Safe Mode

Find the driver behind shutdown-side hangs. Roll back only the drivers dated around the failed update; wholesale driver removal creates new problems while solving nothing.

1. Boot to Safe Mode via Startup Settings.

2. Open Device Manager and look for warning icons.

3. Roll back or uninstall recently updated drivers — display and network first.

4. Restart normally and retry the update with minimal drivers.

### Fix 7: Reset the PC or clean install as last resort

When servicing damage is beyond repair. Choose ‘Keep my files’ for the reset first — it resolves most servicing wreckage while preserving your data, leaving the clean install as the true last resort.

1. In WinRE: Troubleshoot > Reset this PC, keeping files first.

2. If the reset fails, create Windows 11 media from [Microsoft’s download page](https://www.microsoft.com/en-us/software-download/windows11) on another PC.

3. Back up data via the WinRE Command Prompt (xcopy to USB), then clean install.

## Closing

A stuck Restarting screen is diagnosable: classify the hang, use WinRE’s repair tools in order, and reserve the reset for true servicing wreckage. Most machines never need the last resort — Startup Repair, a restore point, or a driver rollback gets them booting again. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
