---
title: "How to Fix BAD_SYSTEM_CONFIG_INFO on a Lenovo Laptop"
slug: how-to-fix-bad-system-config-info-on-lenovo-laptop
date: 2026-09-20
categories: ["windows-errors"]
tags: ["bsod", "boot failure", "lenovo"]
description: "BAD_SYSTEM_CONFIG_INFO blue screen on your Lenovo laptop? Corrupt registry or BCD. Here's how to repair it and boot again."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-on-lenovo-laptop.webp"
faqs:
  - q: "What does BAD_SYSTEM_CONFIG_INFO mean?"
    a: "Windows found corruption in the system registry hive or the Boot Configuration Data (BCD) — the configuration Windows needs to start (stop code 0x74). It's usually caused by a bad update, disk errors, or a corrupted registry from a failed driver install."
  - q: "Will I lose my files?"
    a: "The registry and BCD repairs below don't touch personal files. Only a clean install would. If you're worried, back up your user folder from the recovery command prompt with robocopy before starting."
  - q: "Why is this common on Lenovo laptops?"
    a: "It's not Lenovo-specific, but Lenovo's rapid-boot and firmware utilities (like Lenovo Vantage driver updates) occasionally leave the BCD or registry in a bad state after interrupted updates. The fixes are the same on any brand."
  - q: "Can I fix this without installation media?"
    a: "Often yes — Lenovo's Novo button (the small pinhole button beside the power button) boots directly into the recovery environment, giving you Command Prompt and Startup Repair without any USB media."
---

`BAD_SYSTEM_CONFIG_INFO` (stop code 0x74) means Windows tried to load its core configuration — the SYSTEM registry hive or the boot configuration — and found it corrupted. Without valid configuration, Windows can't start, so you get this blue screen, often in a boot loop.

Lenovo laptops have a handy advantage here: the **Novo button** (a small recessed button next to the power button, pressed with a paperclip) boots straight into the Novo Button Menu with **System Recovery** — no installation media needed. The fixes below use it.

## Why this happens

- **Corrupt SYSTEM registry hive**: Damage to the registry's core hive from disk errors, bad updates, or interrupted writes.
- **Corrupt Boot Configuration Data**: BCD damage from failed updates or disk errors.
- **Failing storage drive**: Bad sectors in the registry or boot partition.
- **Bad RAM**: Memory corruption during registry writes produces a corrupt hive on disk.
- **Interrupted Windows update**: Power loss mid-update leaving configuration half-written.
- **Faulty driver installation**: A driver installer corrupting registry keys during setup.

## How to fix it

Work through these in order — Lenovo's Novo button gets you into recovery.

### Fix 1: Enter recovery with the Novo button

Lenovo's shortcut to the recovery environment.

1. Power off the laptop completely.
2. Find the **Novo button** — a small pinhole button on the side or next to the power button. Press it with a straightened paperclip.
3. The **Novo Button Menu** appears. Select **System Recovery**.
4. The laptop boots into the Windows recovery environment.
5. If your model lacks a Novo button, use the standard method: interrupt boot three times with the power button to trigger Automatic Repair.
6. From here, **Troubleshoot** > **Advanced options** gives you **Command Prompt**, **Startup Repair**, and **System Restore**.

### Fix 2: Run Startup Repair

Let Windows attempt the automatic fix first — it occasionally resolves BCD issues on its own.

1. Go to **Troubleshoot** > **Advanced options** > **Startup Repair**.
2. Select your Windows installation and let it run (up to 30 minutes).
3. If it succeeds, great. If it reports failure, continue — the manual fixes below are more thorough.
4. If Startup Repair loops, see our [Automatic Repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-youtube/) — and the [Lenovo-specific repair loop guide](/articles/how-to-fix-automatic-repair-loop-windows-11-on-lenovo-laptop/).

### Fix 3: Rebuild the BCD

BCD corruption is a top cause — rebuild it from the command prompt.

1. Open **Command Prompt** from **Troubleshoot** > **Advanced options**.
2. Run:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
3. If prompted about a Windows installation, type `Y` to add it.
4. If `fixboot` returns "Access denied," use diskpart: `diskpart` > `list vol` > identify the FAT32 EFI partition > `sel vol <n>` > `assign letter=Z:` > `exit` > `bcdboot C:\Windows /s Z: /f UEFI`.
5. Reboot with `wpeutil reboot` and test.

### Fix 4: Restore the registry from backup

Windows keeps automatic registry backups — restore the SYSTEM hive.

1. In the recovery **Command Prompt**, find your Windows drive letter (it may not be C: — use `diskpart` > `list vol` > `exit` and check with `dir`).
2. Navigate to the backup: `cd /d X:\Windows\System32\config\RegBack` (replace X:).
3. Check the backup isn't empty: `dir` — the files should have meaningful sizes and recent dates. If they're 0 bytes, skip this fix.
4. Back up the current hives first: `copy X:\Windows\System32\config\SYSTEM X:\Windows\System32\config\SYSTEM.bad`
5. Copy the backup over: `copy SYSTEM X:\Windows\System32\config\SYSTEM` (confirm overwrite).
6. Reboot and test. If Windows boots, immediately create a restore point and check the drive (Fix 6) — registry corruption often signals disk problems.
7. If the RegBack folder is empty or the restore doesn't help, don't copy hives from another PC — registry hives are machine-specific and transplanting them causes worse problems. Move on to Fix 5 instead.

### Fix 5: Run offline SFC and DISM

Repair corrupted system files including registry-adjacent components.

1. In the recovery **Command Prompt** (with the correct drive letter X: from Fix 4):
   `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows`
2. Then: `DISM /Image:X:\ /Cleanup-Image /RestoreHealth`
3. Reboot with `wpeutil reboot`.
4. If DISM needs a source, mount [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) and point `/Source:` at its `install.wim`.

### Fix 6: Check the drive and RAM

Registry corruption recurs if the hardware is at fault.

1. Run `chkdsk X: /f /r` (your Windows drive letter) — look for bad sectors in the summary.
2. Run Lenovo's built-in diagnostics: reboot, press **F10** (or use the Novo menu > **BIOS Setup** > diagnostics tab on some models), or download Lenovo diagnostics from [Lenovo support](https://support.lenovo.com/us/en/).
3. Test RAM: from a working Windows session later, run `mdsched.exe`. Bad RAM corrupts registry writes — if chkdsk is clean but corruption recurs, test memory.
4. If the drive is failing, back up now: `robocopy X:\Users\YourName E:\Backup /E` to an external drive, then replace the SSD.
5. Microsoft documents startup repair options on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: System Restore or reset

If the registry and BCD are beyond manual repair, roll back.

1. **Troubleshoot** > **Advanced options** > **System Restore** — pick a point from before the crashes.
2. If no restore points exist, **Troubleshoot** > **Reset this PC** > **Keep my files**.
3. Last resort: **Remove everything** for a clean install (back up first via Fix 6's robocopy).
4. After recovery, update the BIOS from [Lenovo support](https://support.lenovo.com/us/en/) and enable **System Protection** (**Win + R** > `sysdm.cpl` > **System Protection** tab) so restore points exist next time.

## Closing

BAD_SYSTEM_CONFIG_INFO on a Lenovo is a configuration corruption problem — registry hive or BCD — and Lenovo's Novo button gets you into the recovery tools faster than any other brand. Rebuild the BCD, restore the registry from backup, repair system files offline, and check the drive so it doesn't happen again. The configuration is repairable; your files were never in danger, and with System Protection enabled afterward, you'll have a restore point ready if it ever recurs.
