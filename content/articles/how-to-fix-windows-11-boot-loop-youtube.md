---
title: "Windows 11 Boot Loop: Stop the Endless Restarts"
slug: how-to-fix-windows-11-boot-loop-youtube
date: 2026-09-06
categories: ["windows-errors"]
tags: ["windows 11 boot loop", "restart loop", "startup repair", "windows 11"]
description: "Windows 11 keeps restarting and never reaches the desktop? Break the boot loop with these proven repairs, easiest first."
thumbnail: "/images/thumbs/how-to-fix-windows-11-boot-loop-youtube.webp"
faqs:
  - q: "Why does Windows 11 keep restarting in a boot loop?"
    a: "Something fails during every boot attempt, so Windows restarts and tries again. The usual causes: corrupt Boot Configuration Data, a failed update that broke boot files, a BIOS storage mode change, a bad driver loading at startup, or a failing drive. The loop is a symptom — the fixes below target each cause in order."
  - q: "Will breaking the boot loop delete my files?"
    a: "No. Rebuilding the BCD, uninstalling updates, Startup Repair, and Safe Mode troubleshooting all preserve personal files. Your data is intact; only the boot process is broken. Avoid 'Reset this PC > Remove everything' unless you've backed up and exhausted the repair options."
  - q: "How do I get to Safe Mode when Windows won't stop restarting?"
    a: "Interrupt the boot three times by holding the power button during the Windows logo — on the third failure Windows opens the Recovery Environment. Go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 4 for Safe Mode. Alternatively, boot from Windows 11 installation media and choose Repair your computer."
  - q: "What if the boot loop started after a Windows update?"
    a: "Uninstall the update from the recovery environment: Troubleshoot > Advanced options > Uninstall Updates > Uninstall the latest quality update. Then pause updates in Settings once you're back in, and check Microsoft's support site for known issues with that update before letting it reinstall."
---

A **boot loop** — Windows starts, fails, restarts, and repeats forever — is disruptive precisely because it denies you the working system you'd use to fix it. But the loop itself runs from the **Recovery Environment**, which gives you every tool you need: Command Prompt for BCD rebuilds, update uninstallation, Startup Repair, and Safe Mode. You don't need installation media for most fixes (though having a Windows 11 USB helps for the worst cases).

Read the loop's behavior before acting. Does it show the manufacturer's logo, then restart? That's early-boot failure (boot files, BIOS settings). Does it reach "Preparing Automatic Repair" and loop from there? That's Windows boot corruption. Does it reach the login screen or desktop briefly? That's a startup driver or program. Each pattern maps to a fix below. For the automatic-repair variant in detail, see [automatic repair loop step by step](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/); for Safe Mode mechanics, [boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/). One reassurance before you start: a boot loop almost never means dead hardware or lost files. The drive is fine in the overwhelming majority of cases — Windows simply cannot complete the handoff from firmware to operating system. Every fix below works from the Recovery Environment, which the loop itself keeps dropping you into, so you are never locked out of the tools you need.

## Why this happens

- **Corrupt Boot Configuration Data (BCD)**: Damaged boot entries fail identically every attempt.
- **Failed or buggy Windows update**: Broken boot files from an interrupted or faulty update.
- **BIOS storage mode changed**: AHCI/RAID flip breaking the storage driver handoff.
- **Bad startup driver**: A driver that crashes during every boot.
- **Corrupt system files**: Damage to `winload.efi` or early-boot components.
- **Failing drive**: Bad sectors on boot-critical files.
- **Fast Startup corruption**: Hybrid shutdown state poisoning every boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reach the Recovery Environment and try Startup Repair

Start where the loop already takes you.

1. Let the loop fail three times, or hold the power button during the Windows logo three times — Windows opens **Automatic Repair**.
2. Click **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Repair**. Let it run fully.
3. If it fixes the issue, boot normally and immediately check **Settings** > **Windows Update** > **Update history** for what changed recently.
4. If it reports failure, continue — manual repairs below succeed where the automatic tool fails.

### Fix 2: Boot into Safe Mode

Determine whether the problem is a startup driver or program.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4**.
2. If Safe Mode boots: the core system is fine — a third-party driver or startup program is the cause. Skip to Fix 5.
3. If Safe Mode also loops: the problem is boot files, storage drivers, or hardware — continue with Fix 3.
4. This one test directs your entire effort, so don't skip it.

### Fix 3: Rebuild the BCD

The definitive fix for boot-entry corruption.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run: `bootrec /fixmbr`, then `bootrec /fixboot`, then `bootrec /scanos`, then `bootrec /rebuildbcd`, one at a time.
3. If `scanos` finds no Windows installations, rebuild manually: `diskpart` > `list vol` (note the FAT32 EFI partition and Windows letter, often **D:**) > `select vol N` > `assign letter=Z:` > `exit` > `bcdboot D:\Windows /s Z: /f UEFI`.
4. Type `exit`, select **Continue**, and boot normally.

### Fix 4: Uninstall the recent update from recovery

For loops that started within days of an update.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. **Uninstall the latest quality update** first; restart and test.
3. Still looping? Return and uninstall the latest **feature** update.
4. Once in Windows, pause updates and verify the update's status on [Microsoft's support site](https://support.microsoft.com/en-us/windows) before reinstalling.

### Fix 5: Clean-boot to find the crashing startup item

For loops that reach the desktop or login before restarting.

1. In Safe Mode (Fix 2), press **Win + R**, type `msconfig`, press Enter.
2. **Services** tab: tick **Hide all Microsoft services**, click **Disable all**.
3. **Startup** tab: open Task Manager, disable all startup items. Restart normally.
4. If the loop stops, re-enable in halves to identify the culprit, then uninstall it. Update the remaining drivers from the manufacturer's site.

### Fix 6: Check the BIOS storage mode and run disk checks

Cover the firmware and hardware layers.

1. Enter **BIOS/UEFI** (**F2**/**Del** at the logo). Find **SATA Mode**/**SATA Operation** — if it was recently changed (or changed by a BIOS update), set it back (usually **AHCI** for most laptops, **RAID** for some Dells).
2. In WinRE Command Prompt, run `chkdsk C: /f /r` (verify the Windows letter with `diskpart` > `list vol` first) and let it complete.
3. Also run offline SFC: `sfc /scannow /offbootdir=D:\ /offwindir=D:\Windows` with your actual Windows letter.
4. Exit and **Continue** to boot. Filesystem damage on boot files causes loops that survive BCD rebuilds.

### Fix 7: Reset Windows keeping files

The clean ending when repairs fail.

1. In WinRE: **Troubleshoot** > **Reset this PC** > **Keep my files**.
2. Choose **Cloud download** if your internet works in recovery (fresher files) or **Local reinstall** otherwise.
3. Let it complete — this reinstalls Windows while preserving personal files, though you'll reinstall applications.
4. After reset, install drivers from the laptop manufacturer's site first, then let Windows Update run — and download the Windows 11 ISO from [Microsoft](https://www.microsoft.com/en-us/software-download/windows11) to create recovery media for next time.

## Closing

Boot loops feel catastrophic but they're among the most fixable Windows failures — the cause is almost always the BCD, a bad update, or a startup driver, and the Recovery Environment hands you the tools for all three. Work the list in order, note which step broke the loop (so you can prevent recurrence), and make that recovery USB afterward: the next boot problem gets much shorter when you're prepared.
