---
title: "How to Fix the Bad System Config Info Stop Code in Windows 11 24H2"
slug: how-to-fix-bad-system-config-info-in-windows-11-24h2
date: 2026-09-13
categories: ["windows-errors"]
tags: ["bad-system-config-info", "windows-11-24h2", "blue-screen"]
description: "Stuck on Bad System Config Info in Windows 11 24H2? Learn how to repair the boot configuration and registry to boot your laptop again."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-in-windows-11-24h2.webp"
faqs:
  - q: "What does the Bad System Config Info stop code mean?"
    a: "It means Windows found corrupted system configuration data while starting up — usually a damaged BCD boot store or corrupted registry hives. The system stops before the login screen to prevent further damage. The fix involves repairing the boot files and, if needed, restoring the registry from a restore point or repair image."
  - q: "Can a bad RAM stick cause Bad System Config Info?"
    a: "Yes, faulty RAM is a known trigger. Memory errors corrupt configuration data as it's loaded, producing this stop code intermittently. If the error comes and goes, or moves to different stop codes, run Windows Memory Diagnostic before assuming the boot files are the problem."
  - q: "Will I lose my files fixing this error?"
    a: "Not with the repair steps here. Rebuilding the BCD, running SFC, and using System Restore keep your personal files. A reset with 'Keep my files' also preserves them, though it removes installed programs. Only a full 'Remove everything' reset or clean install wipes the drive."
  - q: "Why does Bad System Config Info appear after the 24H2 update?"
    a: "The 24H2 update makes deep changes to boot components. If the update was interrupted by a power loss or a disk error, the BCD or registry hives can end up half-written. See also [Bad System Config Info after a Windows 11 update](/articles/how-to-fix-bad-system-config-info-after-windows-11-update/) for update-specific recovery steps."
---
Bad System Config Info is a classic blue screen that usually appears right when Windows 11 24H2 is supposed to finish loading. The screen tells you your PC ran into a problem, gives you the stop code, and restarts into the same loop. It means the system's configuration data — the boot records and registry hives Windows reads at startup — is damaged.

This error often appears after a feature update, a botched driver install, or an aggressive registry cleaner. On laptops it can also follow a hard shutdown — closing the lid during an update or draining the battery mid-install leaves boot data in an inconsistent state.

The good news: because the damage is in configuration data rather than your files, the repairs below usually restore the system without data loss. Every fix here is non-destructive, and you'll only consider a reset after the repair options are exhausted. If the error appeared right after a feature update, also see [Bad System Config Info after a Windows 11 update](/articles/how-to-fix-bad-system-config-info-after-windows-11-update/) for update-specific recovery steps. Take them step by step, testing a normal boot after each one.

## Why this happens

- **Corrupted BCD boot store.** The Boot Configuration Data file tells Windows where and how to start. Damage here triggers this stop code reliably.
- **Damaged registry hives.** The SYSTEM and SOFTWARE hives hold startup configuration. Corruption from a power loss or disk error breaks the boot sequence.
- **Faulty RAM.** Bad memory corrupts configuration data as it's read into RAM, causing this error to appear and disappear randomly.
- **Interrupted Windows update.** The 24H2 update rewrites boot components; an interruption leaves them half-written.
- **Aggressive registry cleaners or "optimizers."** Third-party tools that "clean" the registry can delete keys Windows needs to boot.
- **Failing hard drive or SSD.** Bad sectors landing on boot files produce configuration errors that look identical to software corruption.

## How to fix it

Work through these in order. You'll need Windows Recovery Environment (WinRE) — it should appear automatically after two failed boots.

### Fix 1: Boot into WinRE and run Startup Repair

Let Windows attempt the automatic fix first.

1. After two failed boot attempts, the **Automatic Repair** screen should appear. Click **Advanced options**.
2. Go to **Troubleshoot > Advanced options > Startup Repair**.
3. Select your Windows installation if prompted and let the repair run.
4. Restart and check whether the stop code is gone.

### Fix 2: Rebuild the BCD boot store

This is the most reliable fix for this particular stop code, because the Boot Configuration Data is the most common thing this error actually refers to. Rebuilding it recreates the pointers Windows needs to find its own files at startup, without touching your documents or programs.

1. From WinRE, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run these commands one by one:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
3. If `rebuildbcd` finds your Windows installation, type **Y** when asked to add it to the boot list.
4. On UEFI systems also run:
   `bcdboot C:\Windows`
   (If WinRE assigned a different drive letter, use `diskpart` and `list volume` first to confirm which letter holds Windows.)
5. Type `exit`, restart, and try booting.

### Fix 3: Run an offline SFC and DISM scan

Repair corrupted system files from outside Windows.

1. Open **Command Prompt** from WinRE's **Advanced options**.
2. Confirm your Windows drive letter with `diskpart` then `list volume` then `exit`.
3. Run the offline system file check:
   `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`
4. Then run DISM against the offline image:
   `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`
5. Restart when both complete.

### Fix 4: Use System Restore to roll back the registry

A restore point replaces the damaged registry hives with working copies. System Restore is particularly effective here because it restores the SYSTEM and SOFTWARE hives as a matched pair, which is exactly the configuration data this stop code complains about.

1. From WinRE go to **Troubleshoot > Advanced options > System Restore**.
2. Choose the most recent restore point created before the problem began.
3. Let the restore complete — this replaces system files and registry settings but keeps your personal files.
4. Restart and verify the system boots.

### Fix 5: Check your RAM with Windows Memory Diagnostic

If the error is intermittent or you recently changed RAM, test the memory.

1. From WinRE's **Command Prompt**, type `mdsched.exe` and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the standard test complete (about 10–15 minutes). For a deeper check, our guide to [running the Memory Diagnostic tool in Windows 11 24H2](/articles/how-to-run-memory-diagnostic-tool-in-windows-11-24h2/) explains the extended options.
4. If errors are found, reseat or replace the faulty RAM stick — software fixes can't repair bad memory.

### Fix 6: Check the disk for errors

Bad sectors on the system drive can corrupt boot data repeatedly.

1. From WinRE's **Command Prompt**, identify your Windows drive letter as before.
2. Run:
   `chkdsk C: /f /r`
   (Replace C: with the correct letter. The `/r` scan can take over an hour on large drives.)
3. If chkdsk reports unrecoverable bad sectors on a spinning hard drive, plan to replace the drive — the error will keep coming back.

### Fix 7: Reset Windows as a last resort

When boot records, system files, and hardware all check out, reset the installation.

1. From WinRE go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files** first. This reinstalls Windows 11 24H2, removes your apps, but keeps personal data.
3. If that fails too, choose **Remove everything** — but only after trying to copy important files using the Command Prompt (`notepad.exe` > **File > Open** gives you a file browser to copy files to a USB drive).
4. For a fully fresh start, download installation media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and from [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) you can review official recovery options.

## Closing

Bad System Config Info in Windows 11 24H2 looks scary but is very fixable: the BCD rebuild in Fix 2 and the System Restore in Fix 4 resolve the great majority of cases. If the error keeps returning after successful repairs, treat it as a hardware signal — run the memory and disk checks, because configuration data doesn't corrupt itself twice without a cause.
