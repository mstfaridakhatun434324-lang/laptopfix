---
title: "How to Fix Bad System Config Info on an HP Laptop"
slug: how-to-fix-bad-system-config-info-on-hp-laptop
date: 2026-09-12
categories: ["windows-errors"]
tags: ["blue screen", "HP laptop", "boot error"]
description: "Bad System Config Info blue screen on your HP laptop? This guide walks you through BCD repair and registry fixes to boot again."
thumbnail: "/images/thumbs/how-to-fix-bad-system-config-info-on-hp-laptop.webp"
faqs:
  - q: "What causes Bad System Config Info on HP laptops?"
    a: "Almost always corruption in the Boot Configuration Data (BCD) or in the SYSTEM registry hive — often after a failed Windows update, a bad shutdown, or disk errors. On HP laptops specifically, interrupted HP BIOS/firmware updates delivered through Windows Update are a known trigger."
  - q: "Will fixing Bad System Config Info delete my files?"
    a: "No. The standard repairs — automatic repair, BCD rebuild, and restoring the registry backup — only touch system and boot files. Your documents, photos, and installed programs stay exactly where they are. File loss only enters the picture if you choose a full reset."
  - q: "Why does this error keep coming back after I fix it?"
    a: "Recurrence usually means the underlying cause is still there: a failing hard drive or SSD corrupting files again, or Windows Update reinstalling the same bad update. Run a disk check and, if the drive is old, check its health in HP's hardware diagnostics."
  - q: "Can I fix this without a Windows installation USB?"
    a: "Usually yes. HP laptops can reach the Windows Recovery Environment by interrupting the boot three times in a row, which gives you Startup Repair, Command Prompt, and System Restore without any USB drive. A USB installer is only needed if the recovery partition itself is damaged."
---
Your HP laptop was fine yesterday. Today it greets you with a blue screen reading "BAD_SYSTEM_CONFIG_INFO" and restarts into the same screen, over and over. The name is refreshingly honest: Windows found something wrong in its own configuration — usually the Boot Configuration Data or a registry hive — and it can't start until that's repaired.

This is one of the more repairable blue screens because the damage is confined to configuration files, not your data. HP laptops have a couple of quirks worth knowing — the recovery key combos and HP's built-in diagnostics — and this guide uses both. You'll be working mostly from the Windows Recovery Environment, which you can reach without any USB drive.

## Why this happens

- **Corrupted Boot Configuration Data (BCD).** The BCD tells Windows where and how to boot. A failed update, a power cut during shutdown, or disk errors can scramble it, and without a valid BCD, Windows can't start at all.
- **A damaged SYSTEM registry hive.** Bad System Config Info (stop code 0x74) specifically implicates the registry's SYSTEM hive. Windows keeps an automatic backup of it, which is why one of the fixes below works so reliably.
- **Interrupted HP firmware or driver updates.** HP pushes BIOS and firmware updates through Windows Update on many models. If one of those gets interrupted, the system configuration can be left inconsistent. HP's own [support site](https://support.hp.com/us-en) has model-specific BIOS recovery steps if you suspect this.
- **Failing storage.** Bad sectors on an aging hard drive or a worn SSD corrupt exactly the kind of small system files this error complains about. If the fix works but the error returns in a few weeks, suspect the drive.
- **Faulty RAM.** Less common for this specific stop code, but corrupted memory can garble configuration data as it's being read. Worth testing if nothing else explains it.
- **Botched manual tweaks.** Editing the registry, using aggressive "optimizer" tools, or misusing `bcdedit` can create this error out of thin air. If you were tinkering before it broke, that's your answer.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Let Startup Repair try first

It's automatic, it's safe, and it fixes BCD problems on its own more often than people expect.

1. With the laptop off, press the **power button**, then force it off by holding the button when the HP logo appears. Do this **three times in a row**.
2. On the fourth boot you'll land on **Choose an option**. Select **Troubleshoot > Advanced options > Startup Repair**.
3. Choose your account, enter your password, and let it run — give it up to 20 minutes.
4. If it succeeds, the laptop restarts normally. If it says it couldn't repair your PC, click **Advanced options** and continue below — you'll need the manual approach.

### Fix 2: Rebuild the BCD from Command Prompt

This is the heavy hitter for Bad System Config Info. You're rewriting the boot configuration from scratch.

1. From the recovery screen, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Type `bootrec /scanos` and press Enter to see if Windows finds your installation. Then run:
   `bootrec /fixmbr`
   `bootrec /fixboot`
3. If `fixboot` gives an "Access is denied" error, run these instead:
   `bcdedit /export C:\BCD_Backup`
   `attrib C:\boot\bcd -h -r -s`
   `ren C:\boot\bcd bcd.old`
   `bootrec /rebuildbcd`
4. When asked to add the installation to the boot list, type `Y` and press Enter. Then type `exit`, choose **Continue**, and restart.

### Fix 3: Restore the registry backup

Windows keeps a backup of the registry hives in the RegBack folder. Swapping in the backup fixes hive corruption directly.

1. Open **Command Prompt** from **Troubleshoot > Advanced options** again.
2. Type `C:` and press Enter, then `cd \Windows\System32\config` to reach the registry hives.
3. Back up the current (broken) hives first:
   `ren SYSTEM SYSTEM.bad`
   `ren SOFTWARE SOFTWARE.bad`
4. Now copy in the backups:
   `copy C:\Windows\System32\config\RegBack\SYSTEM C:\Windows\System32\config\`
   `copy C:\Windows\System32\config\RegBack\SOFTWARE C:\Windows\System32\config\`
5. Type `exit`, restart, and see if Windows boots. If the RegBack folder is empty (Windows 10/11 sometimes doesn't populate it), skip to Fix 4.

### Fix 4: Run System Restore from the recovery menu

A restore point from before the corruption returns the registry and system files to a working state.

1. Go to **Troubleshoot > Advanced options > System Restore**.
2. Pick the most recent restore point dated **before** the blue screens started.
3. Click through the wizard and let it finish — the laptop will restart on its own.
4. Your personal files are untouched. If no restore points exist, move on — this just means System Protection was off, and we'll cover prevention at the end.

### Fix 5: Check the disk for errors

If configuration files keep corrupting, the drive itself may be the problem.

1. Open **Command Prompt** from the recovery menu.
2. Run `chkdsk C: /f /r` and press Enter. The `/r` flag finds bad sectors and recovers readable data — on large drives this can take over an hour, so plug in the charger and be patient.
3. After it completes, also run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` to verify system files against the offline Windows installation.
4. Restart normally. If chkdsk reports lots of bad sectors or unreadable segments, back up your files immediately and plan for a drive replacement.

### Fix 6: Run HP's built-in hardware diagnostics

HP laptops ship with UEFI diagnostics that test the drive and memory outside of Windows — perfect for ruling out hardware.

1. Power off completely, then press the **power button** and immediately start tapping **F2** (on some models it's **Esc** then **F2**).
2. In the **HP PC Hardware Diagnostics UEFI** menu, run the **System Tests > Extensive Test**.
3. If the hard drive or memory test fails, note the **failure ID** — HP support will ask for it, and it confirms the blue screen is a hardware problem, not a Windows problem.
4. This same diagnostics screen is useful for the broader family of startup failures; if you later hit a different blue screen, our general [Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) pairs well with these HP-specific steps.

### Fix 7: Reset Windows while keeping your files

When nothing else works, a reset reinstalls Windows cleanly while preserving your personal data.

1. From the recovery screen, choose **Troubleshoot > Reset this PC**.
2. Select **Keep my files**, then choose **Cloud download** if you have decent internet (it fetches fresh files) or **Local reinstall** otherwise.
3. Follow the prompts. Installed programs will be removed, so keep a list of what you'll need to reinstall.
4. After the reset, immediately run **HP Support Assistant** to pull in the correct drivers for your model before Windows Update has a chance to install generic ones.

## Closing

Bad System Config Info sounds terminal but it's usually a 20-minute repair — the BCD rebuild in Fix 2 alone resolves the majority of cases I see. If your HP instead hangs on the restarting screen without blue-screening, our [Windows 11 stuck on restarting screen fix](/articles/windows-11-stuck-on-restarting-screen-fix/) covers that sibling problem. The one thing I'd insist on: after you're back up, find out *why* it corrupted. Run the HP diagnostics, check the drive health, and make sure System Protection is turned on (**System > About > System protection**) so a restore point exists next time. Configuration corruption that happens once is bad luck; configuration corruption that happens twice is a dying drive telling you it's time to replace it.
