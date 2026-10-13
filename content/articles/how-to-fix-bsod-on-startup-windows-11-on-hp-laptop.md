---
title: "How to Fix a BSOD on Startup in Windows 11 on an HP Laptop"
slug: how-to-fix-bsod-on-startup-windows-11-on-hp-laptop
date: 2026-09-28
categories: ["windows-errors"]
tags: ["bsod", "startup", "hp"]
description: "HP laptop blue-screening every time Windows 11 starts? Here's how to break the crash loop and fix the underlying cause step by step."
thumbnail: "/images/thumbs/how-to-fix-bsod-on-startup-windows-11-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop blue screen every time Windows 11 starts?"
    a: "Something in the startup chain is faulting: a bad driver loading at boot, a corrupted Windows update, failing RAM or storage, or a startup program with a broken driver. Because it crashes before you can use Windows, you fix it from the Recovery Environment or Safe Mode instead of the normal desktop."
  - q: "How do I stop the automatic restart so I can read the error?"
    a: "In the Recovery Environment go to Troubleshoot > Advanced options > Startup Settings > Restart, then press 9 to disable automatic restart after failure. The blue screen will stay visible so you can photograph the stop code. You can also disable it from Safe Mode via System Properties > Advanced > Startup and Recovery settings."
  - q: "Will HP's built-in diagnostics help with startup blue screens?"
    a: "Yes. HP laptops include UEFI diagnostics — press Esc at power-on, then F2 for System Diagnostics. Run the full component tests for memory and storage. If hardware passes, the problem is software (drivers, updates, corruption), which narrows your fix list considerably."
  - q: "Can I fix a startup BSOD without reinstalling Windows?"
    a: "Usually, yes. Safe Mode driver rollbacks, uninstalling the last update from recovery, Startup Repair, and SFC/DISM repairs resolve most startup blue screens. Reinstallation is the last resort, and even then you can choose the option that keeps your files."
---
There's a special frustration to a laptop that blue-screens before you even reach the desktop. You power on your HP, the Windows logo appears, and instead of the login screen you get the sad face — every single time. You can't open Settings, can't uninstall anything, can't even Google the error from the machine itself.

The way out is to stop trying to fix it from inside Windows and instead work from the Recovery Environment — the repair toolkit Windows keeps for exactly this situation. Here's the full playbook, in the order a technician would actually use it.

## Why this happens

- **Faulty driver loading at boot** — graphics, Wi-Fi, or storage drivers that load during startup crash the kernel before the desktop appears. HP's driver updates via Windows Update are a frequent source.
- **Corrupted Windows update** — a quality or feature update that installed badly leaves the boot chain inconsistent.
- **Failing RAM** — memory faults during the heavy I/O of startup produce crashes that look like driver problems.
- **Failing SSD** — bad sectors in boot-critical files cause different stop codes on different boots.
- **Corrupted boot configuration** — the BCD store or EFI boot files are damaged, so Windows starts loading the wrong way and faults.
- **Startup software with kernel drivers** — third-party antivirus, VPN clients, or "tuning" utilities whose drivers load at boot and immediately crash.
- **Fast Startup hibernation corruption** — the hibernation file Windows uses to boot faster gets corrupted and poisons every startup.

## How to fix it

Work through these in order. Steps 1–3 get you into the repair environment; the real fixes start at step 4.

### Fix 1: Reach the Windows Recovery Environment

You can't fix what you can't reach, so get into WinRE first.

1. Power on the laptop. As soon as the HP logo with the spinning dots appears, press and hold the power button for about 5 seconds to force it off.
2. Repeat this two more times — power on, force off during the spinner.
3. On the fourth power-on, Windows should display **Preparing Automatic Repair** and then the **Choose an option** screen. You're in.
4. If this never triggers, create Windows 11 installation media on another PC, boot from it (tap **Esc** at power-on for the HP boot menu, select the USB), and click **Repair your computer** on the setup screen.

### Fix 2: Disable automatic restart to read the stop code

Knowing the exact error focuses everything that follows.

1. On the **Choose an option** screen, select **Troubleshoot** > **Advanced options** > **Startup Settings**, then click **Restart**.
2. When the numbered menu appears, press **9** — **Disable automatic restart after failure**.
3. The laptop will now boot and, when it crashes, the blue screen will stay up instead of rebooting. Photograph it with your phone — note the stop code (like DRIVER_IRQL_NOT_LESS_OR_EQUAL) and any named file (like ntoskrnl.exe or a .sys driver).
4. The named driver is your prime suspect: a Wi-Fi driver name means wireless, nvlddmkm.sys means NVIDIA graphics, and so on.

### Fix 3: Try Safe Mode

Safe Mode skips most third-party drivers — if it boots, the culprit is almost certainly a driver or startup program.

1. Back in **Startup Settings** (Troubleshoot > Advanced options > Startup Settings > Restart), press **4** for Safe Mode or **5** for Safe Mode with Networking.
2. If Safe Mode loads, press **Windows + X** > **Device Manager** and look for devices with yellow warning icons — update or roll back those drivers first.
3. Also open **Settings** > **Apps** > **Startup** and disable everything non-essential, then restart normally to test.
4. If even Safe Mode blue-screens, the problem is deeper — a core Windows driver, system file corruption, or hardware — so continue to the next fixes.

### Fix 4: Run HP's built-in hardware diagnostics

Rule hardware in or out early; it changes the whole strategy.

1. Power off completely, power on, and immediately tap **Esc** repeatedly, then press **F2** for **System Diagnostics** (HP PC Hardware Diagnostics UEFI).
2. Run the **System Tests** > **Extensive Test** — it checks CPU, memory, and storage thoroughly. This takes a while; let it finish.
3. If any component fails, note the failure ID — [HP's support site](https://support.hp.com/us-en) can look it up, and it's what a repair shop needs.
4. If everything passes, you can confidently focus on drivers and Windows itself.

### Fix 5: Uninstall the latest update from recovery

If the crashes started after Patch Tuesday or a feature update, remove it.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Start with **Uninstall latest quality update**, then restart and test.
3. Still crashing? Return and choose **Uninstall latest feature update** to roll back the bigger upgrade.
4. Once stable, open **Settings** > **Windows Update** and use **Pause updates** for 2–3 weeks to avoid immediate reinstallation of the bad update.

### Fix 6: Repair system files and the boot records

Corruption in Windows' own files or boot data causes startup crashes that look like driver faults.

1. In WinRE: **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. First repair the boot files:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
3. Then check system files against the offline Windows install (adjust the drive letter — verify with `diskpart` > `list vol` first):
   `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`
4. Follow with the DISM image repair:
   `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`
5. Type `exit`, select **Continue**, and test a normal boot.

### Fix 7: Disable Fast Startup from recovery

A corrupted hibernation file can crash every single boot.

1. If you can reach Safe Mode with Command Prompt, run:
   `powercfg /h off`
   This disables hibernation — and Fast Startup with it, since Fast Startup depends on hibernation.
2. Restart and test. If boots are now stable, the hibernation file was the problem.
3. You can re-enable it later with `powercfg /h on` once everything is stable, though many technicians leave it off on laptops that had this issue.

### Fix 8: Reset Windows while keeping files

When nothing else works, a fresh Windows over your existing install usually does.

1. Back up anything critical first if you can reach Safe Mode or the command prompt (you can copy files to a USB drive using `xcopy` or File Explorer in Safe Mode).
2. In WinRE: **Troubleshoot** > **Reset this PC** > **Keep my files**, then choose **Cloud download** for the cleanest reinstall.
3. After the reset completes, install drivers from HP's support site for your exact model before running Windows Update.
4. Reinstall applications one at a time over a few days — if the crashes return after a specific app, you've found a software conflict.

## Closing

A startup blue screen on an HP laptop is a puzzle, but it's a solvable one: get into recovery, read the actual stop code, test the hardware with HP's own diagnostics, and then work the software side — updates, drivers, boot records — in order. Most of these resolve without touching your files. For crashes that happen after you successfully log in rather than during boot, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) applies, and if you want to stop the reboot loop just to read the error, see [how to disable automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/). Microsoft's own [blue screen troubleshooting page](https://support.microsoft.com/en-us/windows) is also worth bookmarking for stop-code lookups.
