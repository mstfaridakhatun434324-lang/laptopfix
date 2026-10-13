---
title: "How to Break Out of the Automatic Repair Loop in Windows 11"
slug: how-to-fix-automatic-repair-loop-windows-11-reddit
date: 2026-10-01
categories: ["windows-errors"]
tags: ["boot-error", "repair-loop", "windows-11"]
description: "Stuck in the Windows 11 Automatic Repair loop? These are the fixes that actually work, gathered from real cases — no reinstall required for most."
thumbnail: "/images/thumbs/how-to-fix-automatic-repair-loop-windows-11-reddit.webp"
faqs:
  - q: "What is the Automatic Repair loop in Windows 11?"
    a: "It's when Windows fails to boot, launches Automatic Repair, the repair fails, and the machine reboots straight back into the same cycle. You'll see 'Preparing Automatic Repair' then 'Diagnosing your PC' endlessly. The underlying cause is usually boot file corruption, a bad update, or disk errors — not a dead PC."
  - q: "Will I lose my files if I fix the Automatic Repair loop?"
    a: "The fixes themselves — Startup Repair, bootrec commands, SFC scans, uninstalling updates — don't touch your personal files. Only a full 'Remove everything' reset would delete data, and that's presented as an explicit choice. If you're nervous, back up from the recovery command prompt before doing anything."
  - q: "Why does Automatic Repair keep failing?"
    a: "Automatic Repair is a blunt tool: it fixes common bootloader problems but can't handle corrupted system files, bad updates, or disk errors on its own. When it fails, it usually means the problem is one layer deeper — which is exactly what the manual steps in this guide address."
  - q: "How long should I let Automatic Repair run before giving up?"
    a: "Give it one full attempt — if it's still 'Diagnosing your PC' after 30–45 minutes with no progress, it's stuck. Force shutdown and move to the manual fixes. Repeatedly letting it loop for hours doesn't help; the manual command-prompt repairs do what the automated tool can't."
---
If you've searched Reddit for this problem, you already know the scene: "Preparing Automatic Repair" → "Diagnosing your PC" → a failed repair → reboot → right back to "Preparing Automatic Repair." It's maddening because the machine looks like it's trying to help, but it's just running in circles.

The collective wisdom from thousands of these threads boils down to this: Automatic Repair is a decent first attempt but a terrible loop to stay in. The real fixes are manual, they're done from the recovery command prompt, and they work in the majority of cases without reinstalling anything. Here's the order that actually gets people out.

## Why this happens

- **Corrupted boot configuration data (BCD)** — the most common cause; the bootloader's map of where Windows lives is damaged.
- **Failed or partial Windows update** — an update that didn't finish leaves system files in a half-written state that can't boot.
- **Disk errors** — bad sectors or file-system corruption in boot-critical areas.
- **Corrupted system files** — damaged Windows files that the boot process needs before the desktop loads.
- **Driver conflict introduced at boot** — a newly installed driver that faults during startup, triggering the repair cycle.
- **SrtTrail.txt log loop** — the specific log file (C:\\Windows\\System32\\Logfiles\\Srt\\SrtTrail.txt) fills or corrupts, and some users find deleting it breaks the cycle.
- **Recent hardware change** — a new SSD, RAM stick, or BIOS setting change that Windows can't reconcile at boot.

## How to fix it

Work through these in order. You'll be operating from the blue **Choose an option** screen — if the loop never shows it, force it with three interrupted boots (power off during the Windows spinner, three times).

### Fix 1: Let Startup Repair have one proper try, then move on

Give the automated tool its chance — once.

1. On the **Choose an option** screen, select **Troubleshoot** > **Advanced options** > **Startup Repair**.
2. Let it run to completion, even if it takes 15–20 minutes.
3. If it reports it couldn't repair the PC, don't run it again and again — click **Advanced options** and proceed to the manual fixes below. The loop ends when you stop feeding it.

### Fix 2: Boot into Safe Mode

If Safe Mode works, the core of Windows is intact and the problem is a driver or startup item.

1. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
2. Press **4** for Safe Mode.
3. If it boots, open **Device Manager** (**Windows + X**) and roll back any driver updated in the last few days — especially display, storage, and network drivers.
4. Open **Settings** > **Apps** > **Startup** and disable non-essential startup apps.
5. Restart normally. If the loop is broken, reinstall drivers one at a time from your laptop maker's site to find the bad one.

### Fix 3: Rebuild the BCD from the command prompt

This is the fix Reddit threads cite most often, and for good reason.

1. Go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run these commands in order:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /scanos`
   `bootrec /rebuildbcd`
3. If `bootrec /fixboot` returns "Access is denied," use the EFI workaround: run `diskpart`, then `list vol`, find the FAT32 EFI partition, `select vol N`, `assign letter=Z:`, `exit`, then run `bcdboot C:\Windows /s Z: /f UEFI` (confirm C: is your Windows drive with `dir C:` first).
4. Type `exit` and choose **Continue** to restart.

### Fix 4: Run chkdsk and SFC on the offline system

Fix the disk and the system files in one pass.

1. In the recovery **Command Prompt**, first identify your Windows drive letter — it's often D: or E: in recovery, not C:. Run `diskpart`, `list vol`, `exit` to check.
2. Run `chkdsk X: /f /r` (replace X: with your Windows drive) and let it complete — this repairs file-system errors and bad sectors.
3. Then run the offline system file check:
   `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows`
4. If SFC can't fix everything, run:
   `DISM /Image:X:\ /Cleanup-Image /RestoreHealth`
5. Restart and test.

### Fix 5: Delete the SrtTrail.txt log (the Reddit classic)

This odd fix has broken the loop for countless people.

1. In the recovery **Command Prompt**, run:
   `del C:\Windows\System32\Logfiles\Srt\SrtTrail.txt`
   (Adjust the drive letter to match your Windows drive from Fix 4.)
2. Some users also report success renaming it instead: `ren SrtTrail.txt SrtTrail.old`.
3. Restart. The theory: a corrupted or oversized repair log was itself blocking the repair process. It sounds strange, but the success reports are hard to argue with.

### Fix 6: Uninstall the latest update

If the loop started within a day of an update, that update is guilty until proven innocent.

1. Go to **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall latest quality update**, restart, and test.
3. Still looping? Go back and choose **Uninstall latest feature update**.
4. Once you're booting, pause updates (**Settings** > **Windows Update** > **Pause updates**) for a few weeks to avoid reinstalling the same bad update immediately.

### Fix 7: System Restore to before the loop began

If you have restore points, this is the gentlest full rollback.

1. Go to **Troubleshoot** > **Advanced options** > **System Restore**.
2. Pick the most recent restore point dated before the loop started.
3. Let it complete — this reverts system files, drivers, and registry to that point without touching your personal files.
4. Restart and confirm normal booting, then investigate what changed (usually an update or driver install) so it doesn't recur.

### Fix 8: Reset Windows keeping your files

The last resort before a clean install — and it usually works.

1. Go to **Troubleshoot** > **Reset this PC** > **Keep my files**.
2. Choose **Cloud download** so you get a fresh Windows image rather than reusing the damaged local one.
3. After the reset, install chipset and storage drivers from your laptop manufacturer's support site first, then let Windows Update run.
4. If even the reset fails, the drive itself is likely failing — check its SMART status from the command prompt with `wmic diskdrive get status` and plan a replacement.

## Closing

The Automatic Repair loop feels like a dead end, but it's really just Windows asking for manual help: rebuild the boot data, repair the disk and system files, remove the bad update, and the loop breaks. The vast majority of cases on Reddit resolve at Fix 3 or Fix 4 without anyone losing a file. If your loop is tied to a specific stop code like INACCESSIBLE_BOOT_DEVICE, our [step-by-step guide for that error](/articles/how-to-fix-inaccessible-boot-device-step-by-step/) goes deeper, and the [SrtTrail.txt blue screen guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-step-by-step/) covers the log-file angle in full. Microsoft's [recovery documentation](https://support.microsoft.com/en-us/windows) is the official reference if you want to read further.
