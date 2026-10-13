---
title: "How to Fix BAD_SYSTEM_CONFIG_INFO, Step by Step"
slug: how-to-fix-bad-system-config-info-step-by-step
date: 2026-09-04
categories: ["windows-errors"]
tags: ["bad system config info", "blue screen", "registry", "BCD", "step by step"]
description: "BAD_SYSTEM_CONFIG_INFO blue screen? It's usually registry or BCD corruption. Follow this exact step-by-step repair from WinRE to recovery."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-step-by-step.webp"
faqs:
  - q: "What causes BAD_SYSTEM_CONFIG_INFO?"
    a: "Corruption in the Windows registry (especially the SYSTEM hive) or the Boot Configuration Data — often after a failed update, a power cut during writes, disk errors, or a bad driver installation. Incorrect manual BCD edits and some 'registry cleaner' tools can also trigger it."
  - q: "Can I fix BAD_SYSTEM_CONFIG_INFO without reinstalling Windows?"
    a: "Yes, in most cases. Rebuilding the BCD, restoring registry hives, and running offline SFC resolve it without touching your files or apps. Reinstallation is only needed if the registry backups are also damaged."
  - q: "Why did this happen after a Windows update?"
    a: "Updates write heavily to the registry and boot configuration. If the update was interrupted (power loss, forced shutdown) or hit disk errors mid-write, the registry hives or BCD can be left corrupted — producing this exact stop code on the next boot."
  - q: "How do I open Command Prompt if Windows won't boot?"
    a: "Interrupt the boot three times to reach Automatic Repair, then Advanced options > Troubleshoot > Advanced options > Command Prompt. Or boot from a Windows USB installer and choose Repair your computer > Troubleshoot > Command Prompt."
---

**BAD_SYSTEM_CONFIG_INFO** means Windows found its own configuration — the registry, the boot data, or both — damaged beyond what it can work around. It usually appears at boot, which means you'll be doing the repair from the Windows Recovery Environment. That's fine; every step below is designed for exactly that situation.

Follow the steps in order and don't skip the verification steps — they tell you whether each fix actually took. Your files are safe through all of this; we're repairing configuration, not touching data.

## Why this happens

- **Corrupted SYSTEM registry hive:** The most common cause — the registry's SYSTEM hive damaged by an interrupted update, power loss, or disk error.
- **Damaged Boot Configuration Data:** BCD corruption from failed updates or disk problems.
- **Bad RAM corrupting writes:** Faulty memory corrupting registry data as it's written to disk.
- **Disk errors:** Bad sectors landing on registry hive files or the BCD store.
- **Registry cleaner tools:** Aggressive third-party "optimizers" deleting or mangling registry keys.
- **Failed driver installation:** A driver setup that crashed mid-install, leaving the driver/service registry keys inconsistent.

## How to fix it

Work through these in order — each step is one precise procedure.

### Fix 1: Boot into WinRE and open Command Prompt

Step 1 — get to the repair environment:

1. Power on the laptop. When the logo appears, hold the power button to force it off.
2. Repeat twice more (three interrupted boots). On the next start, **Automatic Repair** appears.
3. Click **Advanced options**, then **Troubleshoot**, then **Advanced options**, then **Command Prompt**.
4. Select your admin account and enter the password if prompted.

Step 2 — confirm your drive letters (they shift in WinRE):

1. Type `diskpart` and press Enter, then type `list vol` and press Enter.
2. Note which letter holds Windows (look for the large NTFS volume labeled or containing Windows) — it's often D: or E: here, not C:. I'll call it `X:` below; substitute yours.
3. Type `exit` to leave diskpart.

### Fix 2: Rebuild the BCD store

Step 1 — repair the boot records:

1. Type `bootrec /fixmbr` and press Enter. Wait for "completed successfully."
2. Type `bootrec /fixboot` and press Enter. If you see "Access is denied," run: `diskpart` > `list vol` > identify the FAT32 EFI partition > `sel vol N` > `assign letter=S:` > `exit` > `bcdboot X:\Windows /s S: /f UEFI`.

Step 2 — rebuild the boot list:

1. Type `bootrec /scanos` and press Enter — note whether it finds your Windows installation.
2. Type `bootrec /rebuildbcd` and press Enter. If prompted, type `Y` and press Enter for each installation found.
3. Type `exit`, choose **Continue**, and restart. If Windows boots, stop here.

### Fix 3: Restore the registry hives from RegBack

Step 1 — check whether backups exist:

1. Reopen the WinRE Command Prompt (Fix 1).
2. Type `dir X:\Windows\System32\config\RegBack` and press Enter.
3. If the files (DEFAULT, SAM, SECURITY, SOFTWARE, SYSTEM) show **0 bytes**, the backups are empty — skip to Fix 4. If they have real sizes, continue.

Step 2 — back up the current (corrupt) hives:

1. Type `cd X:\Windows\System32\config` and press Enter.
2. Type `md backup-corrupt` and press Enter, then `copy SYSTEM backup-corrupt\` and repeat for SOFTWARE, SAM, SECURITY, DEFAULT.

Step 3 — restore the backups:

1. Type `copy X:\Windows\System32\config\RegBack\SYSTEM SYSTEM` and press Enter (confirm overwrite with **Y**).
2. Repeat for SOFTWARE, SAM, SECURITY, and DEFAULT.
3. Type `exit`, restart, and test. This is the step that fixes most BAD_SYSTEM_CONFIG_INFO cases with registry damage.

### Fix 4: Run offline SFC and DISM

Step 1 — system file check against the offline Windows:

1. In WinRE Command Prompt, type `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows` and press Enter.
2. Wait for completion (10–20 minutes). Note whether it repaired anything.

Step 2 — component store repair if needed:

1. Type `DISM /Image:X:\ /Cleanup-Image /RestoreHealth` and press Enter.
2. If a half-applied update is suspected, also run `DISM /Image:X:\ /Cleanup-Image /RevertPendingActions`.
3. Restart and test.

### Fix 5: Check the disk

Corruption that keeps coming back means the disk is the real problem.

1. In WinRE Command Prompt, type `chkdsk X: /r` and press Enter.
2. Let the full scan complete — do not interrupt it.
3. If it finds and repairs errors, restart and test. If it reports bad sectors it couldn't recover, back up your files immediately (via `robocopy` to USB from this same Command Prompt) and plan a drive replacement.

### Fix 6: Test the RAM

Registry corruption with no disk errors and no update incident points at memory.

1. From WinRE: **Troubleshoot > Advanced options > Startup Settings > Restart** isn't needed — instead, boot normally if you can, or use another PC to make a **MemTest86** USB.
2. Run one full MemTest86 pass. Any errors = replace/reseat the RAM (see our [memory corruption guide](/articles/troubleshoot-stop-code-memory-management/) for the full procedure).
3. Reseat SODIMM modules first and retest — loose RAM causes real corruption.

### Fix 7: System Restore from WinRE

If a restore point predates the damage:

1. **Troubleshoot > Advanced options > System Restore**.
2. Select the most recent point from before the first BAD_SYSTEM_CONFIG_INFO crash.
3. Complete the wizard and restart. Personal files are unaffected.

### Fix 8: Reset Windows keeping files

The final software option:

1. **Troubleshoot > Reset this PC > Keep my files > Local reinstall**.
2. This rebuilds Windows, the registry, and the BCD from scratch while preserving personal files. Reinstall your applications afterward.
3. If the reset fails due to a damaged recovery image, use USB media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) for a clean install — back up files first via Command Prompt.

## Closing

BAD_SYSTEM_CONFIG_INFO is a configuration repair job, not a data disaster. The step-by-step order that works: confirm drive letters, rebuild the BCD, restore registry hives from RegBack, run offline SFC/DISM, then check disk and RAM if corruption recurs. Most cases resolve at Fix 2 or Fix 3. If you find yourself fixing this twice, look hard at the disk and RAM — recurring configuration corruption is a hardware symptom wearing a software mask. For the wider family of memory-related stop codes that bad RAM produces, see our [stop-code memory management guide](/articles/troubleshoot-stop-code-memory-management/). If the BAD_SYSTEM_CONFIG_INFO stop code is appearing specifically on Windows 11, our [BAD_SYSTEM_CONFIG_INFO guide for Windows 11](/articles/bad-system-config-info-bsod-windows-11/) covers the OS-specific wrinkles on this same repair.
