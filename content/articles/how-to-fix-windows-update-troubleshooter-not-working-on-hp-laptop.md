---
title: "Windows Update Troubleshooter Not Working on HP Laptop (Fix)"
slug: how-to-fix-windows-update-troubleshooter-not-working-on-hp-laptop
date: 2026-09-25
categories: ["windows-update"]
tags:
  - troubleshooter
  - windows update
  - hp laptop
  - hp support assistant
  - troubleshooting
description: "The Windows Update troubleshooter will not run or finds nothing on your HP laptop? Here is how to fix the troubleshooter itself, plus HP-specific alternatives."
thumbnail: "/images/thumbs/how-to-fix-windows-update-troubleshooter-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why did the Windows Update troubleshooter disappear from Control Panel?"
    a: >
      Microsoft retired the old msdt-based troubleshooters and moved them into Settings > System > Troubleshoot, powered by the Get Help app. Old Control Panel links and msdt commands for Windows Update no longer work on current builds. Always launch the troubleshooter from Settings now — anything else is a dead shortcut.
  - q: "The troubleshooter says it found nothing but updates still fail. Now what?"
    a: >
      The built-in troubleshooter only checks common, shallow issues. Move to manual steps: reset the SoftwareDistribution cache, run DISM and SFC to repair the system image, and check the specific error code in Update history. On HP laptops, also run HP Support Assistant, which catches HP-specific driver and firmware problems Microsoft's tool misses.
  - q: "Is HP Support Assistant a replacement for the Windows troubleshooter?"
    a: >
      Partially. HP Support Assistant excels at HP driver, BIOS, and hardware diagnostics — areas where the Microsoft troubleshooter is blind. But it does not repair Windows Update's own cache or services. Use both: HP's tool for HP hardware and drivers, Microsoft's framework (or the manual resets in this guide) for the update engine itself.
  - q: "Can I reinstall the Windows Update troubleshooter?"
    a: >
      There is no separate installer — it is part of Windows. Repairing the Get Help app and running DISM/SFC effectively restores it. If it remains broken after those repairs, the underlying Windows installation is likely damaged enough to warrant an in-place upgrade repair (reinstalling Windows over itself while keeping files and apps), which restores all built-in diagnostics.
---

The troubleshooter is supposed to be the easy button: click Run, wait, done. So it is doubly frustrating when the Windows Update troubleshooter itself refuses to run, crashes instantly, or cheerfully reports it found nothing while updates keep failing on your HP laptop.

On HP machines there are two layers to this problem. The first is the troubleshooter's own health — on recent Windows 11 builds the old msdt-based troubleshooters were retired in favor of the Get Help app, and the transition left some systems with a troubleshooter that cannot start. The second is HP's parallel universe: HP Support Assistant has its own diagnostics that often succeed where Microsoft's tool fails.

This guide repairs the troubleshooter first, then shows you the HP-specific paths that get updates working even when Microsoft's tool will not cooperate.

## Why this happens

- **Retired msdt troubleshooters on new builds:** Microsoft moved troubleshooters into the Get Help app; old shortcuts and scripts that call msdt now fail silently.
- **Corrupted troubleshooter packages:** the built-in diagnostic packages can be damaged by failed updates, so the tool crashes on launch.
- **Windows Update services stopped:** the troubleshooter needs wuauserv and bits running to diagnose them — if both are dead, it errors out.
- **Missing Get Help app:** on some installs the Get Help app that now hosts troubleshooters is missing or broken.
- **HP system files interfering:** HP's own update services occasionally conflict with the diagnostic's service restarts.
- **Permission problems:** running the troubleshooter without elevation on a restricted account can make it fail immediately.
- **Underlying corruption the tool cannot see:** if the component store is damaged, the troubleshooter may run fine and report nothing while updates still fail.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the troubleshooter the modern way

First, make sure you are launching the current version, not a dead msdt shortcut. The path changed and old bookmarks lie.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Click Run next to Windows Update — not a desktop shortcut or old Control Panel link.
3. If it asks to open the Get Help app, allow it and follow its prompts.
4. If the Run button does nothing at all, continue to Fix 2.

### Fix 2: Restart the update services manually

A troubleshooter cannot diagnose services that will not start. Waking them by hand often unblocks both the tool and the updates.

1. Open Services (Win + R > services.msc) as administrator.
2. Find Windows Update, double-click it, set Startup type to Manual, and click Start.
3. Do the same for Background Intelligent Transfer Service.
4. Return to Settings and run the Windows Update troubleshooter again.

### Fix 3: Repair the Get Help app

Since troubleshooters now live inside Get Help, a broken Get Help means broken troubleshooters. Repairing the app restores the whole framework, including the Windows Update troubleshooter and its siblings for network, audio, and power — so this one repair often fixes several flaky diagnostics at once.

1. Go to Settings > Apps > Installed apps and find Get Help (Microsoft GetHelp).
2. Click the three dots > Advanced options, then click Repair.
3. If Repair does not help, click Reset — this clears the app's data without affecting your files.
4. Run the Windows Update troubleshooter again from Settings.

### Fix 4: Use HP Support Assistant diagnostics instead

HP's own tool diagnoses update and driver problems with full knowledge of HP hardware, and it does not depend on Microsoft's troubleshooter framework at all.

1. Open HP Support Assistant from the Start menu (or install it from the Microsoft Store).
2. Go to the dashboard and run the Tune-up or diagnostic scan.
3. Install any HP-recommended driver, firmware, and BIOS updates it finds.
4. If an HP update fails, note the exact error — HP's [official support site](https://support.hp.com/us-en) has model-specific fixes for each code.

### Fix 5: Reset the Windows Update components by hand

When the troubleshooter cannot run, do its job manually: the standard cache reset fixes the majority of what the tool would have fixed.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Run: net start wuauserv, net start bits, net start cryptsvc, then check for updates.

### Fix 6: Repair system files with DISM and SFC

A troubleshooter that crashes on launch often points to damaged system files underneath. Repair the image and the tool frequently comes back to life.

1. Open Command Prompt as administrator.
2. Run: DISM /Online /Cleanup-Image /RestoreHealth and wait for completion.
3. Run: sfc /scannow and reboot afterward.
4. Try the troubleshooter once more — and run Windows Update to confirm the original problem is gone.

### Fix 7: Use the HP hardware diagnostics for deeper issues

If updates fail with hardware-flavored errors even after all software repairs, rule out the hardware with HP's built-in tests before going further.

1. Reboot and tap Esc, then F2 to open HP PC Hardware Diagnostics.
2. Run the System Tests > Extensive Test on storage and memory.
3. If hardware passes, return to Windows and retry updates with a clean cache.
4. If hardware fails, contact HP support with the failure ID — no software fix will help.

## Closing

When the troubleshooter itself is broken on an HP laptop, work the two tracks: repair Microsoft's framework through the Get Help app and manual service resets, and lean on HP Support Assistant for the HP-specific side. Between them, very few update problems survive. For the generic version of this repair that applies to any brand, see our [step-by-step troubleshooter fix](/articles/how-to-fix-windows-update-troubleshooter-not-working-step-by-step/), and if failed updates left you with display issues, the [HP black screen guide](/articles/how-to-fix-black-screen-after-windows-update-on-hp-laptop/) is next. Keep HP Support Assistant installed and updated — it is the fastest first step the next time updates misbehave on this machine.
