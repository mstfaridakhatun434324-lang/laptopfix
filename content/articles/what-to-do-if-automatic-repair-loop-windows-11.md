---
title: "What to Do If Your Windows 11 Laptop Is Stuck in an Automatic Repair Loop"
slug: what-to-do-if-automatic-repair-loop-windows-11
date: 2026-10-03
categories: ["windows-errors"]
tags: ["automatic repair", "boot loop", "recovery"]
description: "Stuck on 'Preparing Automatic Repair' forever? Break the Windows 11 automatic repair loop and fix the underlying boot problem."
thumbnail: "/images/thumbs/what-to-do-if-automatic-repair-loop-windows-11.webp"
faqs:
  - q: "What is the Automatic Repair loop?"
    a: "It's when Windows fails to boot, launches Automatic Repair to fix itself, the repair fails, and the laptop restarts — only to fail booting again and relaunch the repair, forever. You typically see 'Preparing Automatic Repair' then 'Diagnosing your PC' on every cycle."
  - q: "Will I lose my files in an Automatic Repair loop?"
    a: "No — the loop itself doesn't touch your files, and neither do the fixes here (Startup Repair alternatives, BCD rebuild, System Restore, update uninstall). Your data is only at risk if the underlying cause is a failing drive, which is why checking the disk is part of this guide."
  - q: "How do I get out of the loop to actually fix things?"
    a: "On the 'Automatic Repair couldn't repair your PC' screen, click Advanced options — that takes you to the full Recovery Environment with Command Prompt, System Restore, and Startup Settings. Everything in this guide starts from there."
  - q: "Why does Automatic Repair keep failing?"
    a: "Because the automated tool only handles common boot-file problems. If your issue is a bad driver, a corrupted registry hive, a failed update, or disk errors beyond its scope, it fails the same way every cycle. The manual fixes below cover what the automation can't."
---
The Automatic Repair loop is Windows trying its best and failing in public: your laptop can't boot, so it launches "Preparing Automatic Repair," spends a while "Diagnosing your PC," announces it couldn't repair anything, and restarts — straight back into the same failure. It's supposed to be a safety net. When the net itself has a hole, you need the manual tools.

Here's the thing most people miss: the loop screen is actually your way *in*. That "Automatic Repair couldn't repair your PC" message comes with an **Advanced options** button, and behind that button is the full Recovery Environment — Command Prompt, System Restore, Safe Mode, all of it. The loop isn't a dead end; it's a doorway. Let's walk through it.

## Why this happens

- **Corrupted Boot Configuration Data.** The most common cause. The BCD tells Windows how to boot; when it's damaged, every boot fails identically, and Automatic Repair's automated BCD fix doesn't always catch it.
- **A failed Windows update.** Updates that break the boot sequence trigger the loop on the very next restart. The repair tool can't uninstall updates on its own, so it fails while the fix sits one menu away.
- **Corrupted system files or registry hives.** Damage to the SYSTEM hive or critical boot files defeats the automated repair but yields to manual tools like System Restore or a hive restore.
- **Disk errors.** Bad sectors in the boot area cause the same failure every cycle. Automatic Repair runs a limited disk check; deeper corruption needs manual chkdsk.
- **A bad driver.** Automatic Repair can't remove drivers. If a driver update broke boot, the repair fails forever until you boot into Safe Mode and remove the driver yourself.
- **Fast Startup caching a failed state.** The hibernation-based fast boot replays the broken startup on every attempt, and the repair environment doesn't always clear that cache.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Enter Advanced options and try Safe Mode

Break out of the loop's cycle and confirm Windows can still start minimally.

1. On the **Automatic Repair couldn't repair your PC** screen, click **Advanced options**.
2. Go to **Troubleshoot > Advanced options > Startup Settings** and click **Restart**.
3. After reboot, press **4** for **Safe Mode**. If Windows loads in Safe Mode, your core system is intact — the problem is a driver, update, or startup item, not fundamental corruption.
4. If Safe Mode works, skip to Fix 4 (driver/update removal). If even Safe Mode loops back to repair, continue with Fix 2 — the damage is deeper. Safe Mode details are in our [dedicated Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/) if you need them.

### Fix 2: Rebuild the BCD manually

The automated repair's most common blind spot, fixed by hand in two minutes.

1. From **Advanced options**, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
3. If `fixboot` returns "Access is denied," run the workaround:
   `bcdedit /export C:\BCD_Backup`
   `attrib C:\boot\bcd -h -r -s`
   `ren C:\boot\bcd bcd.old`
   `bootrec /rebuildbcd`
4. Type `Y` to add the installation, then `exit` and choose **Continue**. A manual BCD rebuild succeeds where the automation failed more often than you'd expect.

### Fix 3: Disable Automatic Repair's auto-launch and Fast Startup

Stop the loop from re-triggering while you work, and clear the cached bad boot.

1. In the recovery **Command Prompt**, disable the auto-repair trigger:
   `bcdedit /set {default} recoveryenabled No`
   This stops Windows from launching Automatic Repair on the next failed boot — instead you'll get the Advanced options menu directly, which is more useful.
2. Still in the prompt, disable Fast Startup in the offline registry:
   `reg load HKLM\TempHive C:\Windows\System32\config\SYSTEM`
   `reg add "HKLM\TempHive\ControlSet001\Control\Session Manager\Power" /v HiberbootEnabled /t REG_DWORD /d 0 /f`
   `reg unload HKLM\TempHive`
3. Type `exit`, choose **Continue**, and restart. With the cached boot state cleared, Windows attempts a genuine clean boot.
4. Note: re-enable recovery later with `bcdedit /set {default} recoveryenabled Yes` once the system is healthy — the safety net is worth having.

### Fix 4: Uninstall the latest update

If the loop started after an update, remove the update.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall latest quality update** first. Let it finish, then **Continue** to restart.
3. If the loop persists, return and choose **Uninstall latest feature update**.
4. Once booting normally, pause updates for two weeks (**Settings > Windows Update > Pause updates**) to prevent immediate reinstallation. Update-caused loops are also covered from the general angle in our [Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 5: Run System Restore

Roll back to before the loop began.

1. Go to **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point dated **before** the looping started — the wizard shows descriptions and dates.
3. Let it complete; the laptop restarts automatically. System Restore rewinds system files, drivers, and registry together, which covers most non-hardware loop causes in one move.
4. Your personal files are untouched. If no restore points exist, enable System Protection once you're back in (**Settings > System > About > System protection**) so this option exists next time.

### Fix 6: Check the disk with chkdsk

Rule out the hardware cause that makes loops recur.

1. Open the recovery **Command Prompt** and run `chkdsk C: /f /r`.
2. Let it run fully — the `/r` flag on a large drive can take over an hour. Keep the charger connected.
3. Review the summary: a few repaired errors is fine; widespread bad sectors means the drive is failing and the loop will return until the drive is replaced.
4. Also run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` afterward to verify system files on the repaired disk. Microsoft's [recovery documentation](https://support.microsoft.com/en-us/windows) describes these offline repair options in full.

### Fix 7: Reset Windows while keeping files

The last resort that preserves your data.

1. Go to **Troubleshoot > Reset this PC > Keep my files**.
2. Choose **Cloud download** (fresh files from Microsoft) if your internet is decent, otherwise **Local reinstall**.
3. Follow the prompts. Installed applications are removed, but documents, photos, and other personal files stay.
4. After the reset, install drivers from your laptop manufacturer's site before running Windows Update broadly — and create a restore point immediately while everything works, so a future loop has a one-click exit.

## Closing

The Automatic Repair loop is frustrating because the tool that's supposed to save you is the thing that's stuck — but remember, it's stuck *at the doorway*, not in a locked room. The Advanced options button is always there, and behind it are the manual tools that fix what the automation can't. In practice, the BCD rebuild (Fix 2) and the update uninstall (Fix 4) resolve the large majority of loops. And once you're out, the two habits that prevent a repeat: keep System Protection on (so restore points exist) and don't let the disk fill to the brim — both are free, and both turn the next boot failure from a loop into a footnote.
