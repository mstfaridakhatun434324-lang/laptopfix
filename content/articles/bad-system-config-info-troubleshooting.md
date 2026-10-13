---
title: "Troubleshooting BAD_SYSTEM_CONFIG_INFO Boot Errors in Windows 11"
slug: bad-system-config-info-troubleshooting
date: 2026-09-06
categories: ["windows-errors"]
tags: ["bad system config info", "boot error", "bcd repair", "stop code 0x74", "winre"]
description: "Windows 11 won't boot with BAD_SYSTEM_CONFIG_INFO? Troubleshoot stop code 0x74 with BCD repairs, registry restoration, and disk checks."
thumbnail: "/images/thumbs/bad-system-config-info-troubleshooting.webp"
faqs:
  - q: "What does BAD_SYSTEM_CONFIG_INFO mean on boot?"
    a: "Stop code 0x74 means Windows cannot assemble a valid system configuration during startup — the Boot Configuration Data store or the system registry hives are corrupted. The boot loader reads these before anything else, so the failure happens before the login screen, often dropping you into the Recovery Environment."
  - q: "Will troubleshooting BAD_SYSTEM_CONFIG_INFO delete my files?"
    a: "No. BCD rebuilds, registry restores, Startup Repair, CHKDSK, and System Restore all preserve personal files. These repairs target boot metadata and system state only. File loss only enters the picture with a full reset or clean install, which are last resorts."
  - q: "How do I open Command Prompt if Windows won't start?"
    a: "Boot into the Windows Recovery Environment: let the laptop fail to start three times, or boot from Windows 11 installation media and choose Repair your computer. Then go to Troubleshoot, Advanced options, Command Prompt. You get full offline access to your drives from there."
  - q: "What if bootrec commands don't fix it?"
    a: "Then the registry hives are likely damaged rather than the BCD — restore them from RegBack or a System Restore point. If those are unavailable, run offline SFC and CHKDSK to fix underlying corruption, then rebuild the BCD again on the repaired filesystem."
---

BAD_SYSTEM_CONFIG_INFO — stop code 0x74 — is a boot-time failure: Windows can't put together the configuration it needs to start. Two structures carry that configuration: the Boot Configuration Data (BCD) store, which tells the loader where Windows lives and how to start it, and the system registry hives, which describe drivers, services, and hardware. Corrupt either one and the boot process stalls before the login screen, usually depositing you in the Windows Recovery Environment.

The good news is that this is a metadata problem, not a data problem — your files are almost certainly intact. The troubleshooting below starts in WinRE and works from the least invasive repair (Startup Repair) through manual BCD and registry surgery, ending with the heavy options you'll probably never need.

## Why this happens

- **Corrupted BCD store.** The most common cause — the loader's instructions are damaged or point at the wrong partition.
- **Damaged SYSTEM registry hive.** The registry's system branch is read at boot; corruption halts configuration assembly.
- **Interrupted updates or installs.** Power loss mid-update leaves boot files half-written.
- **Disk errors in the boot partition.** Bad sectors silently corrupting the BCD or hives over time.
- **Partition changes.** Resizing, cloning, or disk-management tools desyncing the BCD from the real layout.
- **Failed driver or encryption installs.** Boot-start drivers (storage, BitLocker) installed badly.
- **Aggressive "cleaner" tools.** Registry cleaners and boot optimizers damaging the hives they promise to fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Startup Repair

Let the automatic tool take the first shot.

1. In WinRE, go to **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows installation and wait — allow up to 20 minutes.
3. If it succeeds, boot normally and immediately create a restore point.
4. If it fails, note the log location it reports (usually `SrtTrail.txt`) for clues.
5. Move on — manual repair below fixes what the automatic tool misses.

If the log mentions SrtTrail, our [SrtTrail.txt blue screen error guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-on-windows-11/) covers that specific failure in depth.

### Fix 2: Rebuild the BCD manually

The definitive fix for BCD corruption.

1. In WinRE: **Troubleshoot > Advanced options > Command Prompt**.
2. Run `bootrec /scanos` — it should find your Windows installation.
3. Run `bootrec /fixmbr`, then `bootrec /fixboot` (ignore "Access is denied" on UEFI; continue).
4. Run `bootrec /rebuildbcd` and answer **Y** to add the installation.
5. If rebuildbcd finds nothing: `bcdedit /export C:\BCD_Backup`, `attrib c:\boot\bcd -h -r -s`, `ren c:\boot\bcd bcd.old`, then `bootrec /rebuildbcd` again.
6. Type `exit`, remove installation media, and restart.

The post-update variant of this error has its own walkthrough: [how to fix BAD_SYSTEM_CONFIG_INFO after a Windows 11 update](/articles/how-to-fix-bad-system-config-info-after-windows-11-update/).

### Fix 3: Restore the registry hives

For when the BCD is healthy but the registry isn't.

1. From the WinRE Command Prompt, find your Windows drive letter: `diskpart` > `list volume` > `exit` (it may be D: or E: here).
2. Back up current hives: `cd /d D:\Windows\System32\config`, then `ren SYSTEM SYSTEM.bad` and `ren SOFTWARE SOFTWARE.bad`.
3. Try the automatic backup: `copy D:\Windows\System32\config\RegBack\* D:\Windows\System32\config\`.
4. If RegBack is empty (common on Windows 11 — automatic registry backup is disabled by default), skip to Fix 4's System Restore instead.
5. Restart and test; if it boots, delete the `.bad` backups after a week of stability.

### Fix 4: Use System Restore from WinRE

Restore points contain full registry snapshots.

1. In WinRE: **Troubleshoot > Advanced options > System Restore**.
2. Pick a restore point from **before** the boot failures started.
3. Let it complete and restart — personal files are preserved.
4. Once booted, open **System Properties > System Protection** and confirm protection is enabled for C:.
5. Create a manual restore point immediately so you have a fresh fallback.

### Fix 5: Run offline CHKDSK and SFC

Repair the filesystem damage that keeps breaking boot data.

1. From the WinRE Command Prompt: `chkdsk C: /f /r` (use the correct letter from Fix 3).
2. Allow the full scan — bad sectors in the boot area explain recurring 0x74 crashes.
3. Then run offline SFC: `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
4. Rebuild the BCD once more after the repairs (Fix 2) — clean filesystem, clean boot data.
5. If chkdsk keeps finding new bad sectors, clone the drive to a replacement SSD promptly.

### Fix 6: Uninstall the triggering update

If the failure followed an update, remove it.

1. In WinRE: **Troubleshoot > Advanced options > Uninstall Updates**.
2. Remove the **latest quality update** first, then test booting.
3. If still failing, remove the **latest feature update**.
4. After booting, pause updates for 7 days in **Settings > Windows Update** to prevent immediate reinstallation.
5. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) later for a revised version of the problematic KB.

### Fix 7: Reset Windows, keeping files

The final option when boot metadata is unrecoverable.

1. In WinRE: **Troubleshoot > Reset this PC > Keep my files**.
2. Choose **Cloud download** if your connection allows — it fetches clean source files.
3. Back up critical files first via Command Prompt (`xcopy`) if you have any doubt about the reset.
4. After the reset, install drivers only from your manufacturer's support page.
5. Enable System Protection and create a restore point before installing anything else.

## Closing

BAD_SYSTEM_CONFIG_INFO is a boot-metadata problem wearing a scary blue-screen costume. Work it in order — Startup Repair, manual BCD rebuild, registry restoration, System Restore — and the overwhelming majority of cases resolve without touching your files. The key insight is that 0x74 is almost never about Windows being "broken" in some deep way; it's about the small set of files the loader reads first. Fix those files, verify the disk beneath them is healthy, and the laptop boots like nothing ever happened. Then set up System Protection, because the next time this happens, you'll fix it in five minutes from a restore point.
