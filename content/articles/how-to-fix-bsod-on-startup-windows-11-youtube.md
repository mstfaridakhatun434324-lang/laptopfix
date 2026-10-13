---
title: "How to Fix a Blue Screen on Startup in Windows 11"
slug: how-to-fix-bsod-on-startup-windows-11-youtube
date: 2026-09-11
categories: ["windows-errors"]
tags: ["bsod on startup", "boot blue screen", "windows 11", "startup repair", "safe mode"]
description: "Blue screen every time Windows 11 starts? Diagnose the startup BSOD: Safe Mode, driver rollback, WinRE repairs, and the exact fix order."
thumbnail: "/images/thumbs/how-to-fix-bsod-on-startup-windows-11-youtube.webp"
faqs:
  - q: "Why does Windows 11 blue screen on every startup?"
    a: "Something loading at boot is crashing — usually a recently updated driver, a bad Windows update, corrupted boot files, or failing hardware (RAM/drive). Because it happens during startup, the trigger is in the boot path: drivers, services, or the boot configuration itself."
  - q: "How do I troubleshoot if I can't reach the desktop?"
    a: "Use the Windows Recovery Environment: interrupt boot three times to reach Automatic Repair, then Advanced options > Troubleshoot. From there you get Safe Mode, Command Prompt, System Restore, and update uninstall — everything needed without the desktop."
  - q: "What's the first thing to try for a startup BSOD?"
    a: "Safe Mode. If Safe Mode boots, the problem is a third-party driver or startup program — roll back recent drivers and disable startup items. If Safe Mode also crashes, the problem is deeper: boot files, system files, or hardware."
  - q: "Can a Windows update cause a startup blue screen?"
    a: "Yes, it's one of the top causes. Updates install new drivers and modify boot components. If the BSODs started right after an update, uninstall the latest quality update from WinRE — it takes two minutes and fixes a large share of cases."
---

A blue screen on *every* startup is different from a random crash — the culprit loads at boot, which actually narrows the suspect list nicely. It's a driver, a startup service, a Windows update, the boot configuration, or hardware. The diagnostic question that splits the whole troubleshooting tree in two: **does Safe Mode boot?**

Yes → software loading at startup (driver/update/program). No → boot files, core system files, or hardware. Everything below follows from that one test.

Before you start, also note exactly *when* the blue screen appears: during the spinning dots (early boot — points at boot files or a storage driver), at the login screen (points at display drivers or startup services), or a minute after login (points at startup programs or a scheduled task). That timing, plus the stop code, narrows things dramatically. And think about what changed recently — a Windows update, a new driver, new software, or new hardware. In my experience, the cause is almost always the most recent change.

## Why this happens

- **Recently updated driver crashing at load:** Graphics, storage, or network drivers that blue-screen the moment Windows initializes them.
- **Bad Windows update:** An update that damaged boot components or installed an incompatible driver.
- **Corrupted boot configuration (BCD):** Damaged boot data from failed updates or disk errors.
- **Startup program or service conflict:** Third-party software loading at boot and crashing the system.
- **Failing RAM or drive:** Hardware faults that manifest as soon as the system is stressed at boot.
- **Overheating at boot:** Clogged cooling causing thermal crashes within minutes of power-on.
- **Fast Startup corruption:** A damaged hibernation file from hybrid shutdown can crash the boot before Windows fully loads — disabling hibernation with `powercfg /h off` from WinRE clears it.

## How to fix it

Work through these in order.

### Fix 1: Get into WinRE

You need the recovery environment for everything below.

1. Power on; when the logo appears, hold power to force off. Repeat **three times**.
2. On the next boot, **Automatic Repair** loads. Click **Advanced options > Troubleshoot**.
3. From here: **Startup Settings** (for Safe Mode), **Command Prompt**, **System Restore**, **Uninstall Updates**, **Startup Repair**. If you're cycling through Automatic Repair specifically, our [automatic repair loop fix](/articles/how-to-fix-automatic-repair-loop-windows-11/) is the targeted guide.

### Fix 2: Test Safe Mode — the great divider

This single test divides every startup-BSOD case into two clear branches, so run it before changing anything.

1. **Troubleshoot > Advanced options > Startup Settings > Restart**, press **4** for Safe Mode.
2. **If Safe Mode boots:** the problem is a third-party driver or startup item → go to Fix 3.
3. **If Safe Mode also blue-screens:** the problem is boot files, core Windows files, or hardware → skip to Fix 5.
4. Note the stop code shown on the blue screen in either case — it focuses the remaining steps.

### Fix 3: Roll back drivers and disable startup items (Safe Mode works)

Safe Mode gives you a working desktop with minimal drivers — the perfect environment to undo whatever broke the normal boot. We'll roll back suspect drivers and silence startup software in one pass.

1. In Safe Mode, open **Device Manager** and check **Display adapters**, **Network adapters**, and **Storage controllers** for recently updated drivers — roll back (**Properties > Driver > Roll Back Driver**) or uninstall and reinstall from the manufacturer's site.
2. Open **Task Manager > Startup apps** and disable everything non-Microsoft.
3. Run **msconfig**, go to the **Services** tab, check **Hide all Microsoft services**, and disable the rest.
4. Restart normally. If it boots, re-enable services and startup items in small groups to find the offender.

### Fix 4: Uninstall the latest Windows update

If the startup BSODs began after an update:

1. In WinRE: **Troubleshoot > Advanced options > Uninstall Updates**.
2. Remove the **latest quality update** first, restart, test.
3. Then the **latest feature update** if needed.
4. Once stable, pause updates briefly and check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a revised version later.

### Fix 5: Repair boot files (Safe Mode fails)

When Safe Mode can't boot either, the damage is below the driver layer — in the boot configuration or core system files. These commands rebuild that foundation from WinRE.

In WinRE Command Prompt:

1. `bootrec /fixmbr`, then `bootrec /fixboot` (use the diskpart + `bcdboot` workaround on "Access is denied").
2. `bootrec /scanos` and `bootrec /rebuildbcd` (answer **Y**).
3. Restart and test. Our [boot loop guide](/articles/how-to-fix-windows-11-boot-loop-step-by-step/) covers this in more depth.

### Fix 6: Run offline SFC, DISM, and chkdsk

Still in WinRE Command Prompt (verify the Windows drive letter with `diskpart` > `list vol` first). This is the deep-repair pass: system files, the component store, and the disk surface, in that order — don't batch them blindly; knowing which step fixed it matters.

1. `sfc /scannow /offbootdir=X:\ /offwindir=X:\Windows`.
2. `DISM /Image:X:\ /Cleanup-Image /RestoreHealth`.
3. `chkdsk X: /r` for the disk itself.
4. Restart and test after each major step.

### Fix 7: System Restore from WinRE

1. **Troubleshoot > Advanced options > System Restore**.
2. Pick the most recent point before the startup BSODs began.
3. Complete and restart. This rolls back drivers, updates, and registry together — ideal for "it worked yesterday" cases.

### Fix 8: Test hardware, then reset as final resort

If every software repair has failed, it's time to question the hardware — and keep the nuclear option in reserve.

1. Run **Windows Memory Diagnostic** (`mdsched.exe`) or **MemTest86**, and your manufacturer's drive diagnostics — startup crashes under load point at RAM or storage.
2. Check thermals: if the laptop is hot within minutes of boot, clean the cooling system.
3. Final software option: **Troubleshoot > Reset this PC > Keep my files**.
4. If hardware tests fail, replace the faulty component — no software repair overcomes it.

## Closing

Startup BSODs are solvable because the suspect pool is small: test Safe Mode first, and let the answer direct you to drivers/startup software (Safe Mode works) or boot files/system files/hardware (Safe Mode fails). Work that split honestly instead of reinstalling drivers at random, and most startup blue screens resolve within the hour. Keep a Windows 11 USB installer handy afterward — it's the fastest way back into WinRE the next time boot goes wrong. And once you're stable, create a restore point and note which driver or update caused the trouble — if it happens again in six months, you'll know exactly where to look instead of starting from scratch.
