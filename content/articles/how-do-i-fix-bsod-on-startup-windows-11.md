---
title: "Blue Screen on Startup in Windows 11? Here's How to Fix It"
slug: how-do-i-fix-bsod-on-startup-windows-11
date: 2026-09-24
categories: ["windows-errors"]
tags: ["bsod on startup", "blue screen", "windows 11", "boot loop", "stop code"]
description: "Windows 11 blue-screens every time it starts? Here's how to fix a startup BSOD — Safe Mode, driver rollback, Startup Repair, and update removal."
thumbnail: "/images/thumbs/how-do-i-fix-bsod-on-startup-windows-11.webp"
faqs:
  - q: "Why does my laptop blue screen every time it starts?"
    a: "A startup BSOD means something in the boot sequence is crashing the kernel before the desktop loads — almost always a bad driver (storage, display, or chipset), a failed Windows update, or corrupt boot files. Because the crash happens before you can use Windows normally, the fixes have to come from Safe Mode or the recovery environment. Note the stop code on the blue screen; it narrows the suspect list dramatically."
  - q: "How do I get into Safe Mode if Windows keeps blue-screening?"
    a: "Interrupt the boot three times in a row — power off during the logo or spinning dots each time — and Windows will open the recovery environment on the next boot. Go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 4 for Safe Mode. If Safe Mode also blue-screens, use the recovery Command Prompt instead, as described in the steps below."
  - q: "Will fixing a startup BSOD delete my files?"
    a: "No. Every fix in this guide — Safe Mode driver rollbacks, Startup Repair, update uninstalls, SFC scans — targets system files and drivers, never your personal data. Your documents, photos, and files remain untouched. Only a full 'Reset this PC > Remove everything' would delete data, and that's the last resort, clearly marked as such."
  - q: "What if the BSOD only happens on every other boot?"
    a: "Intermittent startup crashes point at Fast Startup resuming a corrupt hibernation state, a driver that only fails on cold boots, or marginal hardware like a dying drive or bad RAM stick. Disable Fast Startup first — it's the most common cause of alternating-boot crashes. If the pattern persists, test your RAM and check the drive health."
---

A blue screen during startup is Windows 11 at its least helpful: the system crashes before you can even reach the desktop, which rules out most of the normal troubleshooting tools. Every boot ends the same way — spinning dots, a flash of blue, a stop code you can barely read, and a restart. It's tempting to assume the worst, but startup BSODs are usually fixable without reinstalling anything.

The key insight: something in the boot sequence is crashing the kernel. That "something" is almost always a driver that loads at startup, a Windows update that just landed, or damaged boot files. Because you can't work inside Windows normally, you work from the two places that still function: Safe Mode (a minimal Windows that skips most drivers) and the Windows Recovery Environment (the repair OS on your hidden recovery partition). This guide takes you through both, in the order that fixes the most cases fastest. For the systematic diagnostic version of this problem, see our [startup BSOD troubleshooting guide](/articles/troubleshoot-bsod-on-startup-windows-11/).

## Why this happens

- **Bad driver loading at boot**: A corrupt or incompatible storage, display, or chipset driver crashes the kernel as soon as it initializes during startup.
- **Failed Windows update**: Updates modify boot-critical files and drivers. An interrupted or buggy update leaves the system crashing on every boot.
- **Corrupt Boot Configuration Data**: Damaged BCD entries can cause the boot to hand off incorrectly and crash.
- **Fast Startup corruption**: The hybrid hibernation file can corrupt, so every "fast" boot resumes a broken state — while full shutdowns boot fine.
- **New hardware or BIOS change**: A BIOS update that flips storage modes (RAID/AHCI), or newly installed hardware with a bad driver, breaks the boot chain.
- **Failing drive**: Bad sectors on files Windows needs during startup produce identical crashes on every boot attempt.
- **Bad RAM**: Faulty memory corrupts kernel data during the intensive driver-loading phase of startup.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the stop code and reach the recovery environment

You need the error's name and a working repair console.

1. On the next blue screen, photograph it with your phone — note the stop code (e.g., DRIVER_POWER_STATE_FAILURE) and any named file (e.g., `ntfs.sys`).
2. Force the recovery environment: power on, then force-power-off during the logo/spinning dots. Repeat three times. On the next boot, WinRE should open.
3. If you land on **Automatic Repair**, click **Advanced options**. You now have the full recovery toolkit.
4. If the PC boots fine after the forced interruptions, suspect Fast Startup corruption — skip to Fix 6 after trying Fix 2.

### Fix 2: Boot into Safe Mode and roll back the suspect driver

Safe Mode skips most third-party drivers — if it boots, a driver is your culprit.

1. In WinRE, go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
2. Once in, open **Device Manager**, find recently updated devices (display adapter, storage controllers), right-click > **Properties** > **Driver** > **Roll Back Driver**.
3. Also check **Settings** > **Apps** > **Installed apps** sorted by date — uninstall anything added just before the crashes.
4. Restart normally. If it boots, update the rolled-back driver properly from your manufacturer's site rather than leaving the old version indefinitely.

### Fix 3: Run Startup Repair from WinRE

Let the automatic tool take its shot before manual repairs.

1. In WinRE, go to **Troubleshoot** > **Advanced options** > **Startup Repair**.
2. Select your account, enter your password, and let it run — five to twenty minutes.
3. If it reports success, reboot and test. If it reports failure, don't stop — click **Advanced options** and continue with Fix 4.
4. A failed Startup Repair still writes a diagnostic log at `C:\Windows\System32\LogFiles\Srt\SrtTrail.txt` (viewable via the recovery Command Prompt with Notepad) — its "root cause" line guides your next step.

### Fix 4: Uninstall the latest Windows update

If the crashes started within a day of Patch Tuesday, the update did it.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first, restart, and test.
3. If crashes persist, go back and try **Uninstall the latest feature update**.
4. Once stable, pause updates in **Settings** > **Windows Update** for a couple of weeks and check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for known issues before re-applying.

### Fix 5: Repair boot files and system files offline

Fix the underlying file damage from the recovery command prompt.

1. In WinRE, open **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run the BCD rebuild sequence: `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /scanos`, `bootrec /rebuildbcd` (adjust drive letters — in recovery, Windows is often D:, verify with `dir`).
3. Run offline SFC: `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (same letter adjustment).
4. Run `chkdsk C: /f /r` and let it complete. Type `exit`, choose **Continue**, and test the boot.

### Fix 6: Disable Fast Startup

The classic fix for crashes that happen on some boots but not others.

1. If you can reach Safe Mode or the desktop intermittently: open **Control Panel** > **Power Options** > **Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and untick **Turn on fast startup (recommended)**.
3. Shut down fully (not restart) and power on — this forces a true cold boot without the hibernation file.
4. If crashes stop, leave Fast Startup off. The boot is a few seconds slower, but it's dramatically more reliable — especially on laptops with finicky drivers.

### Fix 7: Test RAM and drive health

When software fixes fail, verify the hardware Windows boots from.

1. In WinRE's Command Prompt, your earlier `chkdsk` results matter — growing bad-sector counts mean a dying drive; back up immediately.
2. Test RAM: from a working Windows session (Safe Mode counts), run `mdsched.exe` and choose the restart-and-test option.
3. Run your manufacturer's boot diagnostics (**F12** > **Diagnostics** on Dell, **F2** on HP) for a full storage and memory test.
4. Our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers stop-code-specific hardware interpretation if your photographed code points at memory or storage.

### Fix 8: Reset Windows while keeping files

The last resort before suspecting hardware failure.

1. In WinRE: **Troubleshoot** > **Reset this PC** > **Keep my files**.
2. This reinstalls Windows, removes apps and settings, but preserves personal files. It eliminates any driver or system-file cause definitively.
3. If the BSOD survives even this, it's hardware — usually the drive or RAM. Replace the suspect component and reinstall from USB media created with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11).

## Closing

Startup BSODs feel catastrophic because they lock you out of your own tools — but the recovery environment gives you everything you need: Safe Mode to bypass bad drivers, update uninstall to undo Patch Tuesday damage, and offline repair commands for broken boot files. The discipline that matters most is capturing the stop code before you start fixing; it turns a blind search into a targeted repair. Work the list in order, and the overwhelming majority of startup blue screens resolve without touching your files. If yours keeps returning after every fix here, treat it as hardware until proven otherwise — test the drive and RAM before anything else.
