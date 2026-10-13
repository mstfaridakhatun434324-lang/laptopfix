---
title: "How to Use Startup Repair on a Windows 11 Laptop"
slug: how-to-use-startup-repair-windows-11-on-laptop
date: 2026-09-17
categories: ["windows-errors"]
tags: ["startup repair", "recovery", "Windows 11"]
description: "Windows 11 won't start? Learn how to run Startup Repair from the recovery menu and what to do when it can't fix the problem."
thumbnail: "/images/thumbs/how-to-use-startup-repair-windows-11-on-laptop.webp"
faqs:
  - q: "What does Startup Repair actually fix?"
    a: "It repairs the files Windows needs to boot: the Boot Configuration Data, the master boot record, boot sector code, and core system files. It runs a series of automated diagnostics and applies fixes without you needing to know command-line tools."
  - q: "Will Startup Repair delete my personal files?"
    a: "No. Startup Repair only touches boot and system files — it never deletes documents, photos, or installed programs. It's one of the safest recovery tools in Windows, which is why it's always worth trying first."
  - q: "How long does Startup Repair take?"
    a: "Usually 10 to 20 minutes, though it can run longer on slow hard drives. If it's been going for over an hour with no progress, it's likely stuck — force a shutdown and try the manual Command Prompt repairs instead."
  - q: "What should I do if Startup Repair says it couldn't repair my PC?"
    a: "That message just means the automated fixes weren't enough — it doesn't mean your data is gone. Click Advanced options and move to manual repairs: rebuilding the BCD, running System Restore, or uninstalling the latest update, all available from the same recovery menu."
---
When Windows 11 won't boot — looping, blue-screening, or hanging on the logo — Startup Repair is the tool Microsoft wants you to try first. It's an automated doctor for boot problems: it scans your boot files, registry hives, and disk, then applies the standard fixes on its own. No commands to memorize, no risky choices to make.

That said, knowing *how* to reach it, what it's actually doing, and — critically — what to do when it fails makes the difference between a quick recovery and hours of frustration. This guide covers all three: getting into the Recovery Environment from any state your laptop is in, running Startup Repair properly, and your next moves when the automated repair isn't enough.

## Why this happens

Startup Repair exists because boot failures have a handful of repeat causes it can fix automatically:

- **Corrupted Boot Configuration Data (BCD).** The BCD tells the bootloader where Windows lives and how to start it. Update glitches and bad shutdowns scramble it regularly — and Startup Repair knows how to rebuild it.
- **Damaged boot sector or master boot record.** Malware, disk errors, or failed dual-boot experiments can break the very first code the machine runs. Startup Repair rewrites these cleanly.
- **Missing or corrupt system files.** If critical files like winload.exe are damaged, Startup Repair can restore them from the local recovery image.
- **A bad driver blocking boot.** Startup Repair can't remove drivers, but its diagnostic log tells you when a driver is the blocker — which points you at Safe Mode and driver removal.
- **Disk errors in the system area.** The tool runs a check on the system partition and can fix logical file-system errors that prevent boot.
- **Failed updates leaving the system half-updated.** When an update breaks the boot sequence, Startup Repair sometimes rolls back enough to get you into Windows, where you can uninstall the update properly.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Reach the Windows Recovery Environment

Everything starts here. Pick the method that matches your laptop's current state.

1. **If Windows tries to boot but fails:** force the laptop off by holding the **power button** during the manufacturer's logo, and repeat **three times**. On the fourth boot, Windows opens the **Choose an option** screen automatically.
2. **If you can reach the login screen but not the desktop:** hold **Shift** while clicking the **power icon > Restart** on the login screen.
3. **If Windows boots fine but you want the tools anyway:** go to **Settings > System > Recovery** and click **Restart now** next to **Advanced startup**.
4. **If nothing else works:** boot from a Windows 11 USB installer (created with the [Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11)), choose your language, and click **Repair your computer** instead of Install.

### Fix 2: Run Startup Repair

Now the actual repair — straightforward, but give it the time it needs.

1. On the **Choose an option** screen, select **Troubleshoot > Advanced options > Startup Repair**.
2. If prompted, choose your user account and enter your password. (If you sign in with a PIN normally, use your full Microsoft account password here.)
3. Startup Repair now runs its diagnostics — **do not interrupt it**. You'll see "Diagnosing your PC" and "Attempting repairs." Expect 10–20 minutes.
4. If it succeeds, the laptop restarts into Windows. Log in and immediately do two things: check **Settings > Windows Update > Update history** for a recently failed update, and create a restore point (**System > About > System protection > Create**) while everything works.

### Fix 3: Read the log when it fails

A failed Startup Repair still gives you a diagnosis — you just have to read it.

1. When you see "Startup Repair couldn't repair your PC," click **Advanced options** (don't shut down yet).
2. Go to **Troubleshoot > Advanced options > Command Prompt**.
3. Type `notepad` and press Enter. In Notepad, use **File > Open**, navigate to `C:\Windows\System32\LogFiles\Srt\`, and open **SrtTrail.txt**.
4. Scroll to the bottom and read the **"Root cause found"** section — it names the failing test, like "Boot critical file is corrupt" or a specific driver. That line tells you which of the fixes below to prioritize. This log is also what Microsoft's [support documentation](https://support.microsoft.com/en-us/windows) references for advanced recovery scenarios.

### Fix 4: Rebuild the boot files manually

When Startup Repair can't fix the BCD itself, do it by hand — it takes two minutes.

1. Open **Command Prompt** from **Troubleshoot > Advanced options**.
2. Run these commands one at a time:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If `fixboot` says "Access is denied," use the workaround:
   `bcdedit /export C:\BCD_Backup`
   `attrib C:\boot\bcd -h -r -s`
   `ren C:\boot\bcd bcd.old`
   `bootrec /rebuildbcd`
4. Type `Y` when prompted, then `exit`, and select **Continue** to restart. Manual BCD rebuilds succeed where the automated tool gives up surprisingly often.

### Fix 5: Uninstall the update that broke boot

If the SrtTrail log or your memory points at a recent update, remove it.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall latest quality update** first, let it finish, and restart.
3. If Windows still won't boot, return and choose **Uninstall latest feature update**.
4. Once you're back in Windows, pause updates for two weeks (**Settings > Windows Update > Pause updates**) so the same update doesn't reinstall before it's fixed. If the symptom is a black screen rather than a boot failure after the update, see [black screen after Windows update on 24H2](/articles/how-to-fix-black-screen-after-windows-update-in-windows-11-24h2/).

### Fix 6: Use System Restore

Roll the system files and registry back to when the laptop booted fine.

1. Go to **Troubleshoot > Advanced options > System Restore**.
2. Select a restore point from **before** the boot problems began and run the wizard.
3. The process restarts the laptop automatically when done. Your files are untouched — only system files, drivers, and settings roll back.
4. No restore points available? That means System Protection was disabled. After recovery, enable it at **Settings > System > About > System protection** so you have this safety net next time.

### Fix 7: Check the disk, then reset as a last resort

If nothing has worked, verify the hardware before reinstalling.

1. Open **Command Prompt** from the recovery menu and run `chkdsk C: /f /r`. On large drives this can exceed an hour — keep the charger plugged in.
2. If chkdsk finds extensive bad sectors, back up your data (you can copy files via the Command Prompt or Notepad's file browser) and plan for a drive replacement — no software fix saves a dying drive.
3. If the drive is healthy, go to **Troubleshoot > Reset this PC > Keep my files** and choose **Cloud download** for fresh installation files.
4. After the reset, update drivers from your laptop maker's support site before doing anything else — a clean driver set prevents the most common repeat boot failures. If you'd rather understand the broader landscape of startup failures first, our guide on [automatic repair loops](/articles/what-to-do-if-automatic-repair-loop-windows-11/) covers the loop scenario this tool often encounters.

## Closing

Startup Repair is a genuinely good first responder — it quietly fixes a huge number of boot problems with zero risk to your data. But its real value is as a gateway: even when it fails, it puts you in the Recovery Environment with the log file, the Command Prompt, and every manual tool you need. Learn the three-interrupted-boots trick to reach that environment, and no boot failure will ever leave you feeling helpless again. The only true prerequisite is a working recovery partition — so once you're back in Windows, consider creating a recovery USB drive (**Control Panel > Recovery > Create a recovery drive**) as insurance.
