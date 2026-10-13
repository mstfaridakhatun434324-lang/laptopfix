---
title: "How to Fix a Windows 11 Boot Loop, Step by Step"
slug: how-to-fix-windows-11-boot-loop-step-by-step
date: 2026-09-29
categories: ["windows-errors"]
tags: ["boot loop", "Windows 11", "startup repair"]
description: "Fix a Windows 11 boot loop step by step: interrupt the cycle, run Startup Repair, rebuild boot files with bootrec, and get your laptop starting normally."
thumbnail: "/images/thumbs/how-to-fix-windows-11-boot-loop-step-by-step.webp"
faqs:
  - q: "What causes a Windows 11 boot loop?"
    a: "The most common causes are a failed Windows update that left boot files mismatched, corrupted BCD (Boot Configuration Data), a bad driver installed at startup, or disk errors on the system partition. Less often, failing storage hardware or a dying CMOS battery on older laptops can trigger repeated failed boots."
  - q: "Will I lose my files if my laptop is stuck in a boot loop?"
    a: "Almost certainly not. A boot loop means Windows can't finish starting, but your files remain on the drive untouched. All the repair steps in this guide — Startup Repair, bootrec commands, System Restore — preserve your data. Only a clean install would erase files, and that is the absolute last resort."
  - q: "How do I get into recovery mode if Windows won't boot?"
    a: "Force it: power off the laptop mid-boot three times in a row (hold the power button when you see the Windows logo or spinning dots). On the third boot, Windows enters the Automatic Repair screen. From there, choose Advanced options to reach Startup Repair, Command Prompt, and System Restore."
  - q: "How long does fixing a boot loop usually take?"
    a: "Most boot loops are fixed within 30 to 60 minutes using Startup Repair or the bootrec commands below. If those fail, System Restore adds another 20 minutes. Only deep cases requiring an in-place upgrade or clean install stretch past two hours. Work the steps in order and stop as soon as booting succeeds."
---

A boot loop is Windows trying — and failing — to start, over and over: logo, spinning dots, black screen, restart, repeat. It's alarming, but it's one of the most fixable problems in Windows because the recovery environment gives you a full toolbox even when Windows itself won't load.

This guide walks the loop down from the simplest interruptions to boot-file surgery, in the order a technician would try them. If your loop involves blue screens on every attempt, our [guide to fixing BSODs on startup](/articles/how-to-fix-bsod-on-startup-windows-11-on-dell-laptop/) covers the crash-specific side.

## Why this happens

- A Windows update that failed midway, leaving boot files from two different builds mixed together.
- Corrupted BCD (Boot Configuration Data) — the file that tells the bootloader where Windows lives.
- A newly installed driver that crashes during the boot sequence.
- Disk errors or bad sectors on the system partition damaging startup files.
- Third-party disk encryption or antivirus interfering with the boot chain.
- Failing SSD/HDD hardware that can't reliably serve boot files.

## How to fix it

Work through these in order. Stop and boot normally after each fix — there's no need to continue once Windows starts.

### Fix 1: Force the Automatic Repair screen

Windows hides its recovery tools behind failed boots. Trigger them deliberately.

1. Power on the laptop and wait for the Windows logo or spinning dots.
2. Hold the **power button** for 10 seconds to force a shutdown.
3. Repeat steps 1–2 two more times (three interrupted boots total).
4. On the next boot, Windows shows **Automatic Repair / Preparing Automatic Repair**.
5. Click **Advanced options** to reach the full recovery toolkit.

### Fix 2: Run Startup Repair

Startup Repair automatically diagnoses and fixes common boot-file problems.

1. From the recovery menu, choose **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows installation if prompted.
3. Let the tool run — it takes 5 to 15 minutes.
4. If it reports it couldn't repair the PC, don't panic: continue to the manual fixes below.
5. If it succeeds, Windows boots normally — restart once more to confirm stability.

### Fix 3: Boot into Safe Mode and remove the trigger

If a recent driver or update caused the loop, Safe Mode lets you remove it.

1. From **Advanced options**, go to **Startup Settings > Restart**.
2. Press **4** for Safe Mode.
3. If Safe Mode boots, open **Settings > Windows Update > Update history > Uninstall updates** and remove the latest update.
4. Also open **Device Manager** and roll back any driver updated just before the loop began.
5. Restart normally. If [Safe Mode itself won't start](/articles/how-to-fix-windows-11-safe-mode-not-working/), move to the offline command-line fixes.

### Fix 4: Rebuild the boot files with bootrec

Corrupted BCD is the classic boot-loop cause, and these commands rebuild it from scratch.

1. From **Advanced options**, open **Command Prompt**.
2. Run `bootrec /fixmbr` and press Enter.
3. Run `bootrec /fixboot` — if you get "Access denied," run `bootsect /nt60 sys` first, then retry.
4. Run `bootrec /rebuildbcd` and type `Y` when it finds your Windows installation.
5. Type `exit`, choose **Continue**, and boot normally.

### Fix 5: Repair system files and check the disk offline

Boot files can be fine while the system files they load are corrupt.

1. In the recovery **Command Prompt**, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
2. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f /r` to scan for disk errors (this can take over an hour).
4. Type `exit` and choose **Continue** to attempt a normal boot.
5. If Windows starts, immediately back up your important files before doing anything else.

### Fix 6: Use System Restore from recovery

If the loop started recently, rolling the system back to a working restore point is fast and safe.

1. From **Advanced options**, choose **System Restore**.
2. Pick a restore point dated **before** the boot loop began.
3. Confirm and let the restore complete — your personal files are not affected.
4. Boot normally and verify stability.
5. If no restore points exist, enable System Protection afterwards via **System Properties > System Protection** so you have them next time.

### Fix 7: Perform an in-place upgrade or reset

When boot files and system files both resist repair, reinstall Windows over itself.

1. Create Windows 11 installation media on another PC from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Boot from the USB and choose **Repair your computer** first for one more Startup Repair attempt.
3. If that fails, from recovery choose **Troubleshoot > Reset this PC > Keep my files**.
4. Prefer **Cloud download** for the freshest files.
5. After the reset completes, reinstall drivers from your manufacturer's support site — for example, Microsoft documents the broader recovery options on its [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Run your maker's hardware diagnostics

If no software fix breaks the loop, the drive itself may be failing — and every major brand ships a built-in test.

1. Restart and press your brand's diagnostics key: **F12** on Dell, **F2** on HP, **F10** on Lenovo, or **F9** on ASUS.
2. Choose the **storage/drive** test and run the thorough (not quick) scan.
3. If the drive fails, replace it — no software repair can fix failing flash or platters.
4. While you're in there, run the **memory** test too; bad RAM can also stall the boot.
5. With new hardware installed, reinstall Windows from the [official media](https://www.microsoft.com/en-us/software-download/windows11) and restore your backup.

## Closing

Boot loops look dire but resolve cleanly in the vast majority of cases: three forced shutdowns get you into recovery, Startup Repair or `bootrec` fixes the boot files, and System Restore covers the rest. Only reach for a reset when the targeted repairs fail. And once you're booting again, turn on System Protection — the next loop, if there ever is one, becomes a ten-minute rollback.
