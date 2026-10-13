---
title: "Windows Update Stuck on Restarting Screen: Step-by-Step Fix"
slug: how-to-fix-windows-update-stuck-on-restarting-screen-step-by-step
date: 2026-10-08
categories: ["windows-update"]
tags:
  - windows update
  - restarting screen
  - update stuck
  - step-by-step
  - winre
description: "Step-by-step fix for Windows Update stuck on the Restarting screen: triage, safe forced shutdown, WinRE repairs, and prevention for every laptop brand."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-step-by-step.webp"
faqs:
  - q: "What is the difference between stuck on Restarting and stuck on shutting down?"
    a: >
      They are different phases: Restarting hangs occur during the reboot sequence while Windows applies update phases between shutdown and startup; shutdown hangs occur while Windows tries to power off. The triage is similar, but Restarting hangs more often involve driver unload problems and Fast Startup, while shutdown hangs lean toward pending operations and services refusing to stop.
  - q: "Can I press keys or move the mouse during the Restarting screen?"
    a: >
      Yes — input is harmless. The screen ignores most input by design, but pressing Caps Lock as a responsiveness test is genuinely useful diagnostics. What you must avoid is holding the power button until you have completed the triage waiting period, since interrupting a working update is the main way this turns into real damage.
  - q: "Why does System Restore help with a stuck update?"
    a: >
      System Restore reverts system files, drivers, and registry to a snapshot from before the update ran, while leaving your personal files alone. If the hang was caused by the update's changes — a bad driver, a corrupted component — the restore erases those changes at the system level, which update removal sometimes cannot do as cleanly.
  - q: "How do I stop this from happening every Patch Tuesday?"
    a: >
      The prevention trio: keep 20+ GB free on C:, keep chipset/storage/graphics drivers current from your laptop maker, and disable Fast Startup. Additionally, install updates when you can monitor them rather than at shutdown, so a hang gets triaged immediately instead of discovered hours later.
---

The Restarting screen with its endless spinning dots is Windows Update's most stressful failure mode, because it gives you no error, no percentage, and no way to know whether the machine is working or wedged. Every laptop brand hits it, and the recovery is the same everywhere — which is why this brand-neutral master guide exists.

The structure here is a decision tree, not a grab bag. First you triage: is it slow or stuck? Then you act with the minimum force required: a safe forced shutdown only when truly idle. Then you repair from the Recovery Environment in escalating order, and finally you change the settings that let it happen again.

Follow the steps exactly. Skipping the triage step is how people corrupt healthy updates.

## Why this happens

- **Legitimate slow finalization:** the Restarting phase does real work — driver finalization, component cleanup — that takes time on slower machines.
- **Driver blocking the reboot transition:** a driver that will not unload cleanly wedges the restart indefinitely.
- **Fast Startup hybrid state conflict:** hibernated kernel state clashes with the update's cold-boot expectations.
- **Corrupted update payload looping:** a damaged download retries one operation forever behind the static screen.
- **Peripheral stalling hardware re-enumeration:** USB devices and docks hang the restart's hardware phase.
- **Full system drive:** staging needs room; a cramped C: drive stalls the restart phase.
- **Firmware verification delays:** OEM firmware checks extend the reboot and can interact with interrupted updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Triage: slow or stuck?

This decision determines everything downstream. Get it right with objective signals, not gut feeling. A working update and a wedged one look identical from the couch — the only honest witnesses are the drive light, the fan, the heat from the vents, and the Caps Lock test. Collect all four before you decide, because forcing a shutdown on a working update is the single most damaging thing you can do in this entire guide.

1. Note the time the Restarting screen appeared; allow 60 minutes (SSD) or 90 (HDD).
2. Check drive activity light, fan noise, and vent heat — ongoing activity means ongoing work.
3. Test Caps Lock light toggling as a responsiveness probe.
4. Frozen dots plus zero activity for 30 minutes equals stuck — proceed. Anything else equals wait.

### Fix 2: Force a safe shutdown and minimal boot

For a truly stuck machine, power it off cleanly and remove variables before the next boot. Every peripheral you unplug is one fewer driver in the restart path and one fewer suspect if the hang repeats — a minimal boot gives you the cleanest possible signal about whether the problem is the update or the hardware around it.

1. Unplug all peripherals: USB devices, docks, monitors, SD cards.
2. Hold power 10 seconds until fully off, wait 30 seconds.
3. Boot with only the charger connected and observe.
4. If Windows resumes the update or rolls back, let it finish — do not interrupt the recovery.

### Fix 3: Enter WinRE and run Startup Repair

The Recovery Environment is your workshop when Windows cannot boot itself. Reach it by interrupting startup three times at the logo.

1. On the Choose an option screen, go to Troubleshoot > Advanced options > Startup Repair.
2. Let it run through its diagnosis and any reboots.
3. If Windows boots afterward, pause updates for 7 days immediately.
4. If it reports failure or the hang returns, continue.

### Fix 4: Uninstall the offending update from WinRE

Surgical removal: take out the update that caused the hang without touching anything else. WinRE's uninstall feature exists precisely for this scenario — it reverses the update's system changes from outside the operating system, where the hung update cannot fight back. Your personal files, installed programs, and settings are untouched; only the update's payload is rolled back.

1. In WinRE: Troubleshoot > Advanced options > Uninstall Updates.
2. Start with Uninstall latest quality update; use the feature-update option only if the hang began right after a feature update.
3. Wait for completion and reboot.
4. Confirm clean startup, then research the KB before re-approving it — a [manual install from the catalog](https://www.catalog.update.microsoft.com/) sometimes succeeds where the automatic attempt wedged.

### Fix 5: System Restore to a pre-update point

When update removal is unavailable or fails, roll the system state back to before the update ran.

1. In WinRE: Troubleshoot > Advanced options > System Restore.
2. Pick a restore point dated before the problematic update.
3. Let it complete — personal files are preserved; system files and drivers revert.
4. Reboot and verify, then address the update cautiously.

### Fix 6: Disable Fast Startup and update drivers

Prevention: remove the two most common recurrence causes in one pass.

1. In Windows: Control Panel > Power Options > Choose what the power buttons do > Change unavailable settings > untick Turn on fast startup.
2. Update chipset, storage, and graphics drivers from your laptop maker's support site.
3. Free C: to at least 20 GB via Storage cleanup.
4. These three changes prevent the large majority of repeat Restarting hangs.

### Fix 7: Reset update components and repair the image

The deep cleanup for machines where the hang damaged the update machinery itself.

1. Elevated Command Prompt: net stop wuauserv, net stop bits, net stop cryptsvc.
2. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
3. Restart the services, then run DISM /Online /Cleanup-Image /RestoreHealth and sfc /scannow.
4. Reboot and run one full update cycle to confirm health. For HP-specific firmware angles, see [stuck on Restarting on HP](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-on-hp-laptop/); for hangs at shutdown instead of restart, read [Update and shut down stuck on 24H2](/articles/how-to-fix-update-and-shut-down-stuck-on-laptop-in-windows-11-24h2/).

## Closing

The Restarting hang is a triage problem first: objective signals tell you whether to wait or act, and acting means the minimum effective force. WinRE's repair ladder — Startup Repair, update removal, System Restore — resolves nearly every case without data loss, and disabling Fast Startup keeps it from coming back. Print this decision tree mentally once and every future hang becomes a calm ten-minute triage instead of a panicked evening.
