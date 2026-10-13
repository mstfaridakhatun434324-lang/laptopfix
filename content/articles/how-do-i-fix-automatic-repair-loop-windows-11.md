---
title: "How Do I Fix the Automatic Repair Loop in Windows 11?"
slug: how-do-i-fix-automatic-repair-loop-windows-11
date: 2026-09-06
categories: ["windows-errors"]
tags: ["automatic repair loop", "boot loop", "winre", "startup repair", "windows 11"]
description: "Stuck in the Windows 11 Automatic Repair loop? Break the cycle, rebuild boot files, and get back to your desktop with these proven steps."
thumbnail: "/images/thumbs/how-do-i-fix-automatic-repair-loop-windows-11.webp"
faqs:
  - q: "Why is my PC stuck in an Automatic Repair loop?"
    a: "Windows fails to boot, launches Automatic Repair, the repair fails, and the PC reboots — only to fail again. The loop persists because the underlying cause (corrupt boot files, bad driver, disk errors, failed update) is never actually fixed by the automated repair."
  - q: "Will I lose my files if I fix the repair loop?"
    a: "Not with the standard fixes. Rebuilding the BCD, running chkdsk, uninstalling updates, and System Restore all preserve personal files. Only a clean install would erase them, and that's the last resort."
  - q: "How do I stop the loop so I can troubleshoot?"
    a: "From WinRE's Command Prompt, run bcdedit /set {default} recoveryenabled No. This stops Windows from launching Automatic Repair on every failed boot, so you see the real error and can work on it directly."
  - q: "What if Advanced options won't open?"
    a: "Boot from a Windows 11 USB installer (made with the Media Creation Tool on another PC) and choose Repair your computer. That gives you the full recovery environment independent of the broken installation."
---

The Automatic Repair loop is Windows trying to be helpful and failing at it: your PC can't boot, so it runs Automatic Repair; the repair can't fix the problem, so the PC reboots; the boot fails again... and around you go. I've seen people stuck in this for days because they keep clicking "Restart" hoping for a different result.

The way out is to **stop letting it repair and start fixing the actual problem.** That means getting into the recovery environment's Command Prompt and working the real causes: boot files, disk errors, bad updates, broken drivers. Here's the full sequence.

A quick warning about what NOT to do: don't keep clicking "Restart" hoping it'll fix itself — every loop iteration is another failed boot attempt that changes nothing. And don't jump to "Reset this PC" as step one; it's effective but wipes your applications, and most loops are fixed by the far less destructive steps below. Work the list in order and you'll keep everything. If your loop specifically references the SrtTrail.txt log, our [SrtTrail.txt quick-fix guide](/articles/best-way-to-fix-srttrail-txt-blue-screen-error/) targets that exact variant.

## Why this happens

- **Corrupted boot files (BCD):** Windows can't assemble the boot, and Startup Repair can't rebuild what it can't parse.
- **Disk errors:** Bad sectors or file system damage on the boot partition that repair can't work around.
- **Failed Windows update:** A half-applied update with inconsistent boot components.
- **Incompatible driver:** A newly installed driver (often storage or display) that crashes the boot.
- **Corrupted registry hives:** Damaged SYSTEM hive blocking boot.
- **Recently installed software with boot drivers:** Disk encryption or backup tools whose drivers crash the boot.
- **Failing drive hardware:** Physical degradation that makes every repair attempt fail the same way.

## How to fix it

Work through these in order.

### Fix 1: Break the loop

First, stop the merry-go-round. Disabling the automatic repair trigger doesn't fix anything by itself — but it converts an infinite loop into a visible error you can actually diagnose, which is the prerequisite for every real fix.

1. On the Automatic Repair screen, click **Advanced options** (not Restart).
2. Go to **Troubleshoot > Advanced options > Command Prompt**.
3. Type `bcdedit /set {default} recoveryenabled No` and press Enter.
4. Type `exit` and choose **Continue**. Windows will now attempt a normal boot and show you the real error instead of looping. Note the stop code or message — it tells you which fix to prioritize.

### Fix 2: Boot into Safe Mode

If normal boot shows a blue screen but Safe Mode works, it's a driver or startup software issue.

1. Interrupt boot three times to return to WinRE, then **Troubleshoot > Advanced options > Startup Settings > Restart**.
2. Press **4** for Safe Mode.
3. In Safe Mode, open **Device Manager** and roll back any recently updated driver, then uninstall recently installed programs.
4. Restart normally and test.

### Fix 3: Rebuild the BCD and MBR

The core fix for boot-file corruption. These commands rewrite the master boot record, the boot sector, and the boot configuration database — the three structures Windows needs to find and start itself. Run them in order; each builds on the last.

1. In WinRE Command Prompt, run `bootrec /fixmbr`.
2. Run `bootrec /fixboot`. On "Access is denied": `diskpart` > `list vol` > find the FAT32 EFI partition > `sel vol N` > `assign letter=S:` > `exit` > `bcdboot C:\Windows /s S: /f UEFI` (verify the Windows drive letter first with `dir C:` — in WinRE it's often D:).
3. Run `bootrec /scanos` then `bootrec /rebuildbcd`, answering **Y**.
4. Restart and test.

### Fix 4: Run chkdsk on the system drive

Disk corruption underlies many loops.

1. In WinRE Command Prompt, confirm the Windows drive letter (`diskpart` > `list vol`).
2. Run `chkdsk X: /r` (your letter). Let the full scan finish — it can take a long time on big drives.
3. If it repairs errors, restart and test. If it finds unrecoverable sectors, back up your files now (use `robocopy X:\Users\<you> E:\backup /E` to a USB drive) — the drive may be failing.

### Fix 5: Uninstall the latest Windows updates

If the loop started right after an update:

1. In WinRE: **Troubleshoot > Advanced options > Uninstall Updates**.
2. Remove the **latest quality update** first, restart, test.
3. If still looping, remove the **latest feature update**.
4. Once booting, pause updates for a couple of weeks to avoid immediate reinstallation of the bad one.

### Fix 6: Run offline SFC and DISM

When boot files look fine but Windows still won't start, the system files themselves are damaged. These commands repair them against the offline Windows image.

1. In WinRE Command Prompt: `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows` (your drive letter).
2. Then `DISM /Image:X:\ /Cleanup-Image /RestoreHealth`.
3. If a stuck update is suspected: `DISM /Image:X:\ /Cleanup-Image /RevertPendingActions`.
4. Restart and test.

### Fix 7: System Restore

1. In WinRE: **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point from before the loop began.
3. Complete and restart. Files untouched; drivers, updates, and registry roll back.

For background on restore points and when they save you, see [using System Restore on Windows 11](/articles/how-to-use-system-restore-on-windows-11-on-laptop/).

### Fix 8: Reset Windows (keep files), then clean install if needed

The final software option before suspecting hardware. A reset reinstalls Windows fresh while keeping your personal files — you'll reinstall apps, but the loop will be gone.

1. In WinRE: **Troubleshoot > Reset this PC > Keep my files > Local reinstall**.
2. If the reset fails (damaged recovery image), create USB media with the [Windows 11 Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) on another PC, back up your files from WinRE Command Prompt, and clean-install.
3. After any reinstall, install chipset/storage drivers from your manufacturer's site before letting Windows Update run wild.

## Closing

The Automatic Repair loop ends when you stop repairing and start fixing: disable the auto-repair trigger, rebuild the boot data, check the disk, and undo the last change (update or driver). That sequence resolves the large majority of loops without data loss. If the loop returns after a fix, suspect the drive — run the manufacturer's full diagnostics, because hardware that keeps corrupting boot files will keep producing the same loop no matter how many times you rebuild them. One more tip: after you escape the loop, immediately create a restore point and a recovery USB. Loops are much less scary the second time when you have both ready — and the restore point gives you a one-click undo for whatever caused it.
