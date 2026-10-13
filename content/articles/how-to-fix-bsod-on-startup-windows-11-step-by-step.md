---
title: "How to Fix a BSOD on Startup in Windows 11 — Step by Step"
slug: how-to-fix-bsod-on-startup-windows-11-step-by-step
date: 2026-09-01
categories: ["windows-errors"]
tags: ["bsod", "startup", "windows-11"]
description: "Windows 11 blue-screening before the desktop? This step-by-step checklist takes you from recovery mode to a stable boot."
thumbnail: "/images/thumbs/how-to-fix-bsod-on-startup-windows-11-step-by-step.webp"
faqs:
  - q: "What should I do first when Windows 11 blue-screens on startup?"
    a: "Get into the Windows Recovery Environment: force it with three interrupted boots (power off during the Windows spinner three times). From there you can use Startup Repair, Safe Mode, System Restore, and the command prompt — the full toolkit for fixing boot-time crashes without reinstalling."
  - q: "How do I find out which stop code I'm getting?"
    a: "Disable automatic restart so the blue screen stays visible: in recovery go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 9. Photograph the screen — the stop code and any named driver file tell you exactly where to focus."
  - q: "Can a startup BSOD be fixed without losing files?"
    a: "Yes, in the large majority of cases. Startup Repair, Safe Mode driver rollbacks, update uninstalls, bootrec repairs, and System Restore all preserve personal files. Only a 'Remove everything' reset or clean install erases data, and those are last resorts."
  - q: "When should I suspect hardware for a startup blue screen?"
    a: "When software fixes fail systematically: crashes in Safe Mode too, memory diagnostic errors, a drive failing SMART checks, or different stop codes on every boot. Run the built-in diagnostics (Windows Memory Diagnostic, chkdsk, manufacturer UEFI diagnostics) before concluding it's hardware."
---
A blue screen during startup is uniquely stressful: you can't get into Windows to fix Windows. But Windows keeps a separate repair environment precisely for this situation, and there's a well-worn path from "crashes before the desktop" to "boots fine." This is that path, as a checklist. Work it top to bottom, and don't skip steps — each one eliminates a whole category of causes, so even the steps that don't fix your machine are telling you something useful about what the problem isn't.

## Why this happens

- **Driver that loads at boot is faulty** — display, storage, or network drivers crashing the kernel before login.
- **Corrupted Windows update** — a half-installed update breaking the boot chain.
- **Damaged boot configuration data (BCD)** — the bootloader pointing at the wrong place.
- **Corrupted system files** — core Windows files damaged by disk errors or failed updates.
- **Failing RAM** — memory faults during the I/O-heavy startup process.
- **Failing drive** — bad sectors in boot-critical files.
- **Startup program with a kernel driver** — antivirus or utilities crashing at boot.
- **Fast Startup / hibernation corruption** — a poisoned hibernation file crashing every boot.

## How to fix it

Work through these in order. Check off each step — the order is deliberate, cheapest and most likely first.

### Fix 1: Enter the Windows Recovery Environment

1. Power on the laptop. When the Windows logo with spinning dots appears, hold the power button ~5 seconds to force shutdown.
2. Repeat step 1 two more times (three interrupted boots total).
3. On the fourth boot, **Preparing Automatic Repair** should appear, followed by the blue **Choose an option** screen.
4. If it doesn't appear after several tries, the on-disk recovery partition may be damaged — create Windows 11 installation media on another PC using the [official download page](https://www.microsoft.com/en-us/software-download/windows11), boot from the USB (via the boot menu key: F12 on Dell/Lenovo, Esc on HP), and click **Repair your computer** on the setup screen instead of Install. This loads the same recovery toolkit from USB.
5. Bookmark this screen mentally — every fix below starts here.

### Fix 2: Try Startup Repair

1. Select **Troubleshoot** > **Advanced options** > **Startup Repair**.
2. Choose your Windows installation if prompted, enter your password if asked.
3. Let it run to completion — give it up to 20 minutes.
4. If it fixes the problem, great — but still read Fix 3 to identify what broke, so it doesn't recur.
5. If it reports failure, click **Advanced options** and continue — one attempt is enough.

### Fix 3: Disable automatic restart and read the stop code

1. **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
2. Press **9** (**Disable automatic restart after failure**).
3. The next crash will freeze on the blue screen instead of rebooting — photograph the stop code and any named `.sys` file.
4. The named file identifies the subsystem: graphics driver, network driver, storage driver, or core Windows file. Let it guide which fix you prioritize below.

### Fix 4: Boot into Safe Mode

1. Return to **Startup Settings** (**Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**).
2. Press **4** for Safe Mode (or **5** with Networking if you need to download drivers).
3. If Safe Mode boots: open **Device Manager** (**Windows + X**), find devices with yellow warnings, and roll back or update those drivers. Then open **Settings** > **Apps** > **Startup** and disable non-essential items.
4. Restart normally and test. If Safe Mode also blue-screens, the fault is in core Windows or hardware — continue to Fix 5.

### Fix 5: Undo recent changes — uninstall updates or use System Restore

1. **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Choose **Uninstall latest quality update** first. Restart, test.
3. Still crashing? Return and **Uninstall latest feature update**.
4. If updates aren't the issue, try **Troubleshoot** > **Advanced options** > **System Restore** instead: select a restore point dated before the crashes began and complete the wizard. This reverts drivers, system files, and registry without touching personal files.
5. If the machine boots after either step, pause updates (**Settings** > **Windows Update** > **Pause updates**) for a few weeks, and investigate what changed (update? new driver? new software?) to prevent recurrence.

### Fix 6: Repair boot records and system files from the command prompt

1. **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Find your Windows drive letter: `diskpart` > `list vol` > `exit` (it's often D: in recovery — call it X: below).
3. Rebuild boot data:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
4. Check the disk and system files:
   `chkdsk X: /f /r`
   `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows`
5. Type `exit`, choose **Continue**, test boot.

### Fix 7: Disable Fast Startup and test hardware

1. If you can reach Safe Mode's command prompt, run `powercfg /h off` to kill Fast Startup and its hibernation file, then restart.
2. Run **Windows Memory Diagnostic**: in recovery command prompt you can't easily, so if you reach Safe Mode, run `mdsched.exe` > **Restart now and check for problems**.
3. Run your manufacturer's UEFI diagnostics (F2/Del/Esc at boot, depending on brand) for CPU, memory, and drive tests.
4. From the recovery command prompt, `wmic diskdrive get status` should say **OK**.

### Fix 8: Reset Windows keeping your files

1. **Troubleshoot** > **Reset this PC** > **Keep my files** > **Cloud download**.
2. After the reset, install your laptop maker's chipset and storage drivers first, then run Windows Update.
3. Reinstall apps gradually — if crashes return after a specific app, you've found a conflict.
4. If even this fails, the drive is likely failing — replace it.

## Closing

Startup blue screens feel like a locked door, but the Recovery Environment is the key — and this checklist is the order a technician works through once inside. Most cases resolve at Startup Repair, Safe Mode driver rollback, or update removal, with files intact. For brand-specific recovery paths, see our [HP startup BSOD guide](/articles/how-to-fix-bsod-on-startup-windows-11-on-hp-laptop/), and to stop the reboot loop long enough to read the error, [disable automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/). Microsoft's [recovery options documentation](https://support.microsoft.com/en-us/windows) covers the official WinRE reference.
