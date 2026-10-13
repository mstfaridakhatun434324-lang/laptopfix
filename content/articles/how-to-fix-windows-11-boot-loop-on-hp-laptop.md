---
title: "Fixing a Windows 11 Boot Loop on an HP Laptop"
slug: how-to-fix-windows-11-boot-loop-on-hp-laptop
date: 2026-09-17
categories: ["windows-errors"]
tags: ["boot loop", "windows 11", "HP laptop"]
description: "HP laptop stuck restarting over and over? Break the Windows 11 boot loop with HP diagnostics, startup repair, and boot rebuilds."
thumbnail: "/images/thumbs/how-to-fix-windows-11-boot-loop-on-hp-laptop.webp"
faqs:
  - q: "What causes a boot loop on an HP laptop?"
    a: "Usually a failed Windows update, corrupt boot configuration data, a bad driver loading at startup, or a failing drive. On HP machines, interrupted BIOS updates or HP-specific driver conflicts are additional triggers. The loop itself — restart, fail, restart — is Windows' automatic recovery retrying and failing."
  - q: "Will I lose my files breaking the boot loop?"
    a: "The standard fixes — Startup Repair, Safe Mode driver removal, System Restore, and boot-record rebuilds — all preserve your files. Only a clean install wipes data. If the drive is failing, back up from the recovery environment before attempting repairs."
  - q: "How do I get into recovery if it keeps restarting?"
    a: "Interrupt the boot three times by holding the power button during the HP logo — Windows will enter Automatic Repair on its own. Alternatively, press Esc at power-on for HP's Startup Menu, then F11 for System Recovery, which boots HP's recovery environment directly."
  - q: "What if it's stuck on the HP logo specifically?"
    a: "A loop that never reaches the Windows spinner usually means a BIOS/firmware or hardware problem rather than a Windows problem. Run HP PC Hardware Diagnostics from the Startup Menu (Esc > F2) first — if hardware passes, the issue is the Windows boot chain."
---
An HP laptop caught in a **boot loop** — HP logo, spinning dots, black screen, restart, repeat — is stuck because something in the startup sequence fails every time, and Windows' automatic retry just runs the same failure again. Breaking the loop means getting into the recovery environment and fixing whatever is crashing the boot.

HP machines give you two doors into recovery: Windows' own Automatic Repair and HP's built-in System Recovery. This guide uses both, starting with the least destructive options.

## Why this happens

- **Failed or interrupted Windows update:** An update that installed halfway leaves the system unbootable.
- **Corrupt Boot Configuration Data (BCD):** The boot menu's instructions damaged by disk errors or bad updates.
- **Bad driver loading at startup:** A newly installed driver that crashes during boot, triggering the restart.
- **Failing drive:** Bad sectors in boot or system files causing consistent boot failure.
- **Corrupt system files:** Damage to the kernel or critical boot drivers.
- **Interrupted BIOS update:** On HP, a failed firmware update can loop at the logo before Windows even loads.
- **Fast Startup corruption:** A damaged hibernation file breaking the hybrid boot sequence.

## How to fix it

Work through these in order. Stop when the laptop boots normally.

### Fix 1: Reach the recovery environment

You cannot fix the loop from inside the loop — get out first.

1. **Method A:** Hold the power button to force-shutdown during the HP logo or Windows spinner. Repeat three times. On the fourth boot, Windows enters **Automatic Repair**.
2. **Method B (HP-specific):** Power on and immediately press **Esc** repeatedly for the Startup Menu, then **F11** for System Recovery.
3. Once in the recovery environment, you have Startup Repair, Safe Mode, Command Prompt, System Restore, and Reset options. Do not choose Reset yet.

### Fix 2: Run Startup Repair

Let the automatic tool try first — it fixes common boot-record and boot-file problems.

1. In the recovery environment: **Troubleshoot > Advanced options > Startup Repair**.
2. Select your Windows 11 installation and let it run. It checks the BCD, boot files, and disk for boot-blocking issues.
3. If it succeeds, the laptop boots. If it fails, note the log path (`SrtTrail.txt`) — our guide on [what to do when SrtTrail.txt keeps failing](/articles/what-to-do-if-srttrail-txt-blue-screen-error/) covers that specific dead end.

### Fix 3: Boot into Safe Mode and remove the bad driver

If Startup Repair cannot fix it, a driver loading at boot is the likely culprit.

1. From recovery: **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. If Safe Mode boots, open **Device Manager** and look for the driver installed just before the loop began — right-click it and choose **Uninstall device** (tick **Attempt to remove the driver**).
3. Also open **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent update.
4. Reboot normally. Safe Mode bypasses most third-party drivers, so reaching it proves the core system is intact.

### Fix 4: Run HP hardware diagnostics

Rule out a failing drive or memory — the loop could be hardware. This step earns its place early in the sequence: every software repair below assumes working hardware, and ten minutes of diagnostics now prevents an afternoon of futile boot rebuilds on a dying drive.

1. Power on, press **Esc** for the Startup Menu, then **F2** for **HP PC Hardware Diagnostics**.
2. Run the **System Extensive Test** (or at minimum the **Hard Drive Extensive Test** and **Memory Test**).
3. If the drive fails, back up from the recovery Command Prompt and replace the drive. If memory fails, reseat or replace the sticks. Get HP's full diagnostic suite from [HP Support](https://support.hp.com/us-en) if needed.

### Fix 5: Rebuild the boot configuration

Corrupt BCD is a classic loop cause and is directly repairable.

1. From recovery: **Troubleshoot > Advanced options > Command Prompt**.
2. Run in order:
   - `bootrec /fixmbr`
   - `bootrec /fixboot` (if "Access denied," continue — the next commands usually succeed anyway)
   - `bootrec /rebuildbcd`
3. If `rebuildbcd` finds no Windows installations, run `bcdboot C:\Windows` (adjust the drive letter if your Windows partition differs — use `diskpart` then `list volume` to check).
4. Type `exit`, choose **Continue**, and test the boot.

### Fix 6: Use System Restore

Roll back to before the loop began.

1. From recovery: **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point dated before the looping started.
3. This reverses driver installs, updates, and system changes without touching personal files. If no restore points exist, enable System Protection after you recover so you have this option next time.

### Fix 7: Repair system files and check the disk from recovery

Deep corruption needs the offline tools.

1. In the recovery Command Prompt, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust C: to your Windows drive).
2. Run `chkdsk C: /f /r` and let it complete — boot loops from disk errors need the `/r` pass.
3. Reboot and test. If the loop persists with clean files and a healthy disk, the remaining options are reset or clean install.

### Fix 8: Reset Windows (Keep my files) as the last resort

When the boot chain cannot be repaired, replace the installation.

1. From recovery: **Troubleshoot > Reset this PC > Keep my files**, choosing **Cloud download** if Wi-Fi is available.
2. After the reset, install drivers from [HP Support](https://support.hp.com/us-en) for your exact model before anything else.
3. If even the reset fails, the drive is likely the problem — replace it and install Windows fresh from a [Microsoft installation image](https://www.microsoft.com/en-us/software-download/windows11).

## Closing

A boot loop on an HP laptop is a broken startup sequence, and the recovery environment gives you every tool to fix it: Startup Repair, Safe Mode driver removal, HP's own hardware diagnostics, BCD rebuilds, and System Restore. Work the list in order and the loop breaks — usually long before a reset is needed. If the machine hangs on the "Restarting" screen rather than fully rebooting, see our [stuck on restarting screen guide](/articles/windows-11-stuck-on-restarting-screen-fix/) for that specific variant.
