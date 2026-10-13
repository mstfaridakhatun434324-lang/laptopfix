---
title: "BAD_SYSTEM_CONFIG_INFO Blue Screen: How to Fix It"
slug: bad-system-config-info-blue-screen-error-fix
date: 2026-09-01
categories: ["windows-errors"]
tags: ["BAD_SYSTEM_CONFIG_INFO", "registry errors", "boot repair"]
description: "Fix the BAD_SYSTEM_CONFIG_INFO blue screen on Windows: repair the BCD and registry, fix boot files, and recover from this startup crash."
thumbnail: "/images/thumbs/bad-system-config-info-blue-screen-error-fix.webp"
faqs:
  - q: "What does BAD_SYSTEM_CONFIG_INFO mean?"
    a: "It means Windows found its system configuration — the registry hives or Boot Configuration Data — damaged or inconsistent at startup. Stop code 0x74 appears when the SYSTEM hive can't load or the BCD points at invalid settings. It's a startup problem, not a running-system problem, so the fixes live in the recovery environment."
  - q: "What usually causes BAD_SYSTEM_CONFIG_INFO?"
    a: "The top causes are a corrupted SYSTEM registry hive (often from a bad shutdown or failed update), a damaged BCD store, disk errors on the system partition, and failed RAM corrupting registry data as it loads. Overzealous 'registry cleaner' tools are a notorious trigger — they delete keys Windows needs to boot."
  - q: "Will fixing this delete my files?"
    a: "No. Every repair in this guide — Startup Repair, bootrec, registry restoration, System Restore — preserves your personal files. They target boot configuration and system hives only. Your documents sit untouched on the drive throughout. Only a clean install would erase files, and that's the last resort."
  - q: "Can bad RAM cause BAD_SYSTEM_CONFIG_INFO?"
    a: "Yes. If RAM corrupts the registry hive as Windows loads it into memory, you get exactly this error even though the hive on disk is fine. If registry repairs don't stick — the error returns after a successful fix — test your RAM with Windows Memory Diagnostic or MemTest86 before assuming the disk is at fault."
---

BAD_SYSTEM_CONFIG_INFO (stop code `0x74`) strikes at startup: Windows tries to load its system configuration and finds it broken. The usual victims are the SYSTEM registry hive and the Boot Configuration Data (BCD) — corrupt either one and Windows can't even get to the login screen. It looks catastrophic, but the configuration is repairable without touching your personal files.

Because this is a boot-time failure, all the fixes happen in the recovery environment or from installation media — you can't fix it from inside Windows because Windows won't start. Work them in order from automatic to manual, and don't skip the hardware checks at the end: recurring config corruption is often the first symptom of a dying drive or bad RAM. If your machine loops at boot generally, our [boot loop repair guide](/articles/how-to-fix-windows-11-boot-loop-step-by-step/) covers the wider territory.

## Why this happens

- Corrupted SYSTEM registry hive from a bad shutdown, power loss, or failed update.
- Damaged BCD store pointing the bootloader at invalid configuration.
- Disk errors or bad sectors in the registry hive's location on the system partition.
- "Registry cleaner" utilities deleting keys Windows needs to start.
- Faulty RAM corrupting the hive as it loads into memory.
- A failed Windows update leaving registry and boot files mismatched.
- Dual-boot tools or boot managers overwriting the BCD with invalid entries.

## How to fix it

Work through these in order from the recovery environment.

### Fix 1: Run Startup Repair

Let Windows attempt the automatic fix first — it handles simple BCD damage.

1. Boot into recovery: interrupt startup three times, or boot from Windows 11 installation media and choose **Repair your computer**.
2. Go to **Troubleshoot > Advanced options > Startup Repair**.
3. Select your Windows installation and let it run (5–15 minutes).
4. If it succeeds, boot normally and immediately back up your files.
5. If it fails, continue — the manual fixes below handle what Startup Repair can't.

### Fix 2: Rebuild the BCD

A damaged Boot Configuration Data store is the most common fixable cause.

1. From **Advanced options**, open **Command Prompt**.
2. Run `bootrec /fixmbr` and press Enter.
3. Run `bootrec /fixboot` — if "Access denied," run `bootsect /nt60 sys` first.
4. Run `bootrec /rebuildbcd`; type `Y` when it finds your Windows installation.
5. Type `exit`, choose **Continue**, and attempt a normal boot.

### Fix 3: Restore the registry from backup

Windows keeps automatic registry backups you can restore from recovery.

1. In the recovery **Command Prompt**, navigate to `C:\Windows\System32\config`.
2. Check for the **RegBack** folder: `dir C:\Windows\System32\config\RegBack`.
3. If it contains hive files, back up the current ones: `copy SYSTEM SYSTEM.bad` (repeat for SOFTWARE, SAM, SECURITY, DEFAULT).
4. Copy the backups over: `copy C:\Windows\System32\config\RegBack\SYSTEM C:\Windows\System32\config\`.
5. Type `exit` and boot — if the hive was the problem, Windows starts.

### Fix 4: Run System Restore from recovery

A restore point from before the corruption began undoes the damage cleanly.

1. From **Advanced options**, choose **System Restore**.
2. Select a point dated **before** the crashes started.
3. Let the restore complete — personal files are unaffected.
4. Boot normally and verify stability.
5. Our [System Restore guide](/articles/best-way-to-use-system-restore-on-windows-11/) explains how to keep protection enabled so points exist next time.

### Fix 5: Check the disk for errors

Bad sectors in the hive's neighborhood cause recurring corruption.

1. In the recovery **Command Prompt**, run `chkdsk C: /f /r`.
2. Let it complete — the `/r` pass takes a while on large drives.
3. If chkdsk finds and repairs bad sectors, retry the boot.
4. Check SMART status afterwards: `wmic diskdrive get status` should report **OK**.
5. Recurring bad sectors mean the drive is failing — replace it before reinstalling anything.

### Fix 6: Test the RAM

If registry fixes work once but the error returns, suspect memory corrupting the hive at load.

1. From recovery, choose **Windows Memory Diagnostic** (under **Advanced options** on some systems) or boot **MemTest86** from USB.
2. Let at least 2 full passes complete.
3. Reseat RAM modules if errors appear on previously good sticks.
4. Replace failing sticks with matching specs.
5. Retest the boot after confirming clean RAM — the registry repairs from Fix 3 may now stick.

### Fix 7: Repair system files offline

Corruption beyond the registry may need the full offline repair treatment.

1. In the recovery **Command Prompt**, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
2. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
3. Type `exit` and attempt a normal boot.
4. Microsoft documents offline repair on its [Windows support hub](https://support.microsoft.com/en-us/windows).
5. If SFC reports unfixable damage, the installation media's repair install is next.

### Fix 8: Reset Windows as the final option

When configuration damage resists all repairs, start the system state fresh.

1. Create Windows 11 installation media from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) on another PC.
2. Boot from it, choose **Repair your computer > Troubleshoot > Reset this PC**.
3. Choose **Keep my files** to preserve personal data.
4. Prefer **Cloud download** for the cleanest system files.
5. After the reset, never run registry cleaners again — they're a leading cause of this exact error.

## Closing

BAD_SYSTEM_CONFIG_INFO is Windows telling you its startup configuration is broken — and the recovery environment gives you everything needed to fix it: Startup Repair, bootrec, registry restoration, and System Restore. Work the list in order, verify the disk and RAM if corruption keeps returning, and you'll be booting cleanly again without losing a single file. Once you're back in, enable System Protection so the next configuration mishap is a simple rollback. And retire any registry cleaner for good — the few megabytes it "saves" aren't worth another 0x74 at boot time. Your registry doesn't need cleaning; it needs leaving alone by well-meaning utilities that promise speed and deliver boot failures instead, every single time without fail.
