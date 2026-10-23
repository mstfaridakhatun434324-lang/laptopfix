---
title: "How to Fix Hibernation Not Working on Your Snapdragon Laptop"
slug: hibernation-not-working-snapdragon
date: 2026-10-23
categories: ["ai-pc"]
tags: ["hibernation", "snapdragon", "sleep", "power settings", "windows 11 arm", "troubleshooting"]
description: "Fix hibernation that fails or disappears on Snapdragon laptops — rebuild hiberfil.sys, fix power settings, resolve Modern Standby conflicts, update firmware."
thumbnail: "/images/thumbs/hibernation-not-working-snapdragon.webp"
faqs:
  - q: "Why is Hibernate missing from the power menu on my Snapdragon laptop?"
    a: "The Hibernate option is usually hidden because hibernation was never enabled in the power plan, hiberfil.sys is missing, or an update reset the power settings. Running powercfg /hibernate on from an elevated Command Prompt and ticking Hibernate in the Power Options shutdown settings brings it back in most cases."
  - q: "Can I use hibernation if my laptop uses Modern Standby?"
    a: "Yes, the two can coexist. Modern Standby handles short idle periods, while hibernation kicks in after a longer timeout or when battery runs low. Problems start when the firmware or chipset driver mishandles the handoff between the S0 low-power state and the S4 hibernate state — updating the firmware usually fixes that handoff."
  - q: "Does hibernation work the same on ARM as on Intel laptops?"
    a: "Functionally yes, but the plumbing differs. Snapdragon laptops use Qualcomm power-management firmware to write RAM contents to hiberfil.sys, and that firmware path gets less testing than the Intel/AMD one. That is why hibernation breaks more often on ARM after updates, and why OEM chipset drivers matter more here."
  - q: "Will disabling Fast Startup fix hibernation problems?"
    a: "Often, yes. Fast Startup uses the same hiberfil.sys file for hybrid shutdown, and a corrupted hibernation file breaks both. Turning Fast Startup off and rebuilding hiberfil.sys with powercfg resolves a surprising share of hibernate failures on Snapdragon machines."
---

You close the lid expecting the laptop to hibernate, but it only sleeps — and two hours later the battery is dead and the machine is warm inside your bag. Or Hibernate is gone altogether: the power menu lists Sleep, Shut down, and Restart, with no Hibernate in sight. Either way, the feature that should preserve your work with zero battery drain is not doing its job.

On Snapdragon-powered Copilot+ PCs, hibernation lives in an awkward spot. These machines lean on Modern Standby (S0 low-power idle) as their default light sleep, and the hibernation machinery — hiberfil.sys, the S4 sleep state, the Qualcomm firmware that writes gigabytes of RAM to disk — sometimes never gets configured the way it does on Intel and AMD laptops. A Windows update, a missing power component, or a driver regression can silently remove Hibernate from the menu or break the save-to-disk transition itself.

This guide gives you six fixes in technician order: restoring the Hibernate option and the hibernation file first, then resolving the Fast Startup and Modern Standby conflicts, and finally updating the ARM chipset firmware and drivers that perform the actual hibernate transition. Test Hibernate — not Sleep — after each step.

## Why this happens

- **Hibernation disabled in the power plan:** Windows on ARM sometimes ships with hibernation turned off at the powercfg level, which hides the option from every menu. No file, no option, no hibernate.
- **hiberfil.sys missing or corrupted:** The hibernation file at the root of C: holds the RAM image. If it was deleted, shrunk by disk cleanup, or corrupted by a bad shutdown, hibernate fails or refuses to start.
- **Fast Startup fighting for the same file:** Fast Startup is a hybrid shutdown that uses hiberfil.sys too. A broken file or a misbehaving driver can make Fast Startup and hibernation sabotage each other.
- **Modern Standby handoff bugs in firmware:** The firmware must hand the system from S0 low-power idle to S4 hibernate cleanly. Older Snapdragon platform firmware on several Copilot+ models botches this handoff, so the machine wakes instead of hibernating.
- **Outdated Qualcomm chipset drivers:** The power-management driver package handles the hibernate transition on ARM. When Windows Update leaves it stale or replaces it with a generic one, transitions fail silently.
- **Wake timers and devices aborting the transition:** A USB device, network adapter, or scheduled wake timer can fire during the hibernate transition and pull the machine back out — you see a brief black screen, then the lock screen again.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Re-enable hibernation and restore the menu option

Start with the basics: confirm hibernation is enabled at the system level, then make the option visible in the power menus. This is the fix whenever Hibernate simply vanished.

1. Open **Command Prompt as administrator** and run `powercfg /hibernate on` — this recreates hiberfil.sys and enables the S4 state.
2. Run `powercfg /availablesleepstates` and confirm **Hibernate** appears in the list of supported states.
3. Open **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**, then tick the **Hibernate** checkbox under shutdown settings.
4. Check the Start menu power button — Hibernate should now be listed. If heavy creative apps hang the transition later, close them first; the same emulation quirks behind [After Effects not working on ARM laptops](/articles/after-effects-arm-laptop-not-working/) can stall a hibernate request.
5. Try Hibernate once from the menu and watch what happens — note whether it fails, wakes immediately, or works, because that tells you which fix comes next.

### Fix 2: Rebuild a corrupted hiberfil.sys

If Hibernate is present but the machine flashes a black screen and returns to the lock screen — or hibernates but resumes to a crash — the hibernation file itself is likely corrupt. Rebuilding it is safer than any registry tweak.

1. In an elevated Command Prompt, run `powercfg /hibernate off` to delete the existing hiberfil.sys.
2. Confirm your C: drive has free space equal to at least 40% of your RAM — hibernation needs room for the full memory image.
3. Run `powercfg /hibernate on` to create a fresh hiberfil.sys at the default size.
4. Test Hibernate immediately, before changing anything else, so you know the clean file is what fixed it.
5. If it corrupts again within days, leave Fast Startup off (Fix 3) and retest.

### Fix 3: Turn off Fast Startup

Fast Startup and hibernation share hiberfil.sys, and on Snapdragon machines the hybrid-shutdown path is a common source of cross-contamination: a bad Fast Startup shutdown leaves the file in a state that breaks the next hibernate attempt. Disabling it isolates hibernation cleanly.

1. Open **Control Panel > Power Options > Choose what the power buttons do** and click **Change settings that are currently unavailable**.
2. Untick **Turn on fast startup (recommended)** and save changes.
3. Shut the machine down fully, wait ten seconds, and power it back on — a real cold boot, not a hybrid one.
4. Test Hibernate again. If it now works, Fast Startup was the culprit — leave it off (shutdowns take a few seconds longer without it).

### Fix 4: Update the Snapdragon platform firmware and chipset drivers

When hibernate fails at the hardware level — the screen goes black, the machine never fully powers off, or it wakes seconds later — the Qualcomm power-management firmware and chipset drivers are the suspects. This is the same firmware layer behind post-resume glitches, like [Copilot in Word failing after resume](/articles/copilot-in-word-not-working/) until a reboot.

1. Check your current BIOS/firmware version in **Settings > System > About** or the OEM utility, then compare it against the latest firmware on your maker's support page ([Dell](https://www.dell.com/support), HP, or Lenovo).
2. Install any BIOS/UEFI update marked as fixing sleep, hibernate, or Modern Standby behavior — several Snapdragon X models got exactly such fixes in 2025 firmware releases.
3. From the same support page, install the latest Qualcomm chipset / power-management driver package for Windows 11 on ARM; do not rely on the generic driver Windows Update provides.
4. Run Windows Update afterward, and check [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if the OEM page lags behind.
5. Cold-boot the machine after firmware and driver updates, then test a full hibernate-and-resume cycle with the lid closed for five minutes.

### Fix 5: Stop wake timers and devices from aborting hibernate

If the machine starts hibernating but wakes straight back to the lock screen, something is vetoing the transition. Find it with the built-in power diagnostics instead of guessing.

1. In an elevated Command Prompt, run `powercfg /waketimers` and `powercfg /lastwake` after a failed hibernate — these name the timer or device that woke the machine.
2. In **Device Manager**, open **Properties > Power Management** on network adapters, USB hubs, and mice, and untick **Allow this device to wake the computer** for anything you do not need.
3. In **Settings > System > Power & battery**, pause any updater or sync tool that schedules frequent wake timers.
4. HDMI audio endpoints and USB headsets are frequent offenders — and they also cause [Live Captions trouble with HDMI audio](/articles/live-captions-not-working-hdmi-audio/) after resume, so disabling their wake permission fixes two annoyances at once.
5. Retest hibernate with peripherals unplugged; if it works clean, re-enable wake devices one at a time to find the offender.

### Fix 6: Repair the power plans and system files

When every setting looks right but hibernate still fails, the power plan store or core system files may be damaged — often after a failed feature update. A reset of the plans plus a system-file check closes out the software layer.

1. In an elevated Command Prompt, run `powercfg /restoredefaultschemes` to rebuild all power plans from defaults.
2. Re-enable hibernation with `powercfg /hibernate on` afterward, since the reset can turn it off again.
3. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth` if SFC reports damage it cannot fix.
4. Restart, set your preferred plan (Balanced is fine for Snapdragon efficiency), and confirm the Hibernate checkbox is still ticked in the shutdown settings.
5. If hibernate still fails now, check the [Windows support pages](https://support.microsoft.com/en-us/windows) — but an OEM firmware issue (Fix 4) is likelier than anything in Windows at this point.

## Closing

Hibernation failures on Snapdragon laptops are almost never a hardware defect — they are a configuration stack: the hibernate option, the hiberfil.sys file, Fast Startup, the firmware handoff, and wake devices. Work through them in order, and Hibernate becomes as reliable on ARM as it ever was on x86.
