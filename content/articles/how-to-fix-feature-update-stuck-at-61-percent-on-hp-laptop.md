---
title: "Feature Update Stuck at 61 Percent on an HP Laptop? Fix It"
slug: how-to-fix-feature-update-stuck-at-61-percent-on-hp-laptop
date: 2026-10-01
categories: ["windows-update"]
tags: ["feature update stuck", "61 percent", "hp laptop", "update stuck"]
description: "Feature update frozen at 61% on your HP laptop? That is the driver migration phase stalling. Here is the HP-specific unstick sequence."
thumbnail: "/images/thumbs/how-to-fix-feature-update-stuck-at-61-percent-on-hp-laptop.webp"
faqs:
  - q: "Why 61 percent specifically on HP laptops?"
    a: "61% sits in the driver migration phase, and HP laptops carry a heavy driver load — storage controllers, card readers, fingerprint sensors, and HP utility drivers. If any one of them resists migration, the phase stalls at the percentage where that driver is processed."
  - q: "How long should I wait at 61% on an HP?"
    a: "Two to four hours on AC power with the machine idle — longer if the HP still has a mechanical hard drive. Migration is genuinely slow. Act only after hours of zero percentage movement with idle disk activity in Task Manager."
  - q: "Will forcing a restart at 61% damage my HP?"
    a: "Unlikely. At 61% the update has not committed to the new build — it is still migrating into a scratch area. A forced shutdown triggers an automatic rollback to your current Windows, which is the designed recovery path for exactly this situation."
  - q: "Which HP driver most often causes the 61% stall?"
    a: "Storage controller and chipset drivers lead the statistics, followed by HP's peripheral drivers (card reader, fingerprint sensor). Updating those from HP support before retrying resolves most 61% stalls on HP hardware. HP's support site lists driver updates by model, so match the download to your exact machine."
---

Your HP laptop's feature update climbs to 61 percent and stops. Not slows — stops. Hours pass, the spinner spins, the number never moves. HP owners report this stall more than most, and there is a reason: 61 percent is the driver migration phase, and HP machines migrate more drivers than average — storage, chipset, card reader, fingerprint sensor, and a layer of HP utility drivers on top.

The stall point is actually good news disguised as bad: at 61 percent the update has not yet committed to the new Windows build, so your recovery options are safe and your current system is intact underneath. This guide gives you the HP-specific unstick sequence — what to update, what to unplug, when to force the restart, and how to make the retry succeed.

HP adds a firmware wrinkle worth knowing. HP's Sure Start and BIOS-level device controls can present hardware to Windows in ways the migration does not expect — a card reader disabled in BIOS but present in the driver store, for example. The migrator tries to reconcile the firmware view with the driver view and stalls. Aligning the two — either enabling the device in BIOS or uninstalling its driver — removes the contradiction. When the 61 percent stall resists every OS-level fix, the answer is usually one level down, in firmware.

## Why this happens

- **HP storage or chipset driver resisting migration.** The top HP-specific cause — the migrator cannot carry the driver forward.
- **HP peripheral drivers stalling the phase.** Card reader, fingerprint sensor, and webcam drivers from old HP packages.
- **HP utility kernel drivers.** Support Assistant and security utilities with deep hooks.
- **Third-party antivirus filters.** Security drivers refusing the migration handoff.
- **External devices multiplying migration work.** Docks, printers, and USB devices each adding drivers to migrate.
- **Corrupted state from a previous 61% attempt.** Partial migration data confusing the retry.
- **Insufficient working space.** The migration scratch area needs gigabytes beyond the download.
- **A firmware-driver contradiction.** BIOS-disabled devices with installed drivers create a mismatch the migration phase cannot reconcile, stalling at 61 percent.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait correctly, then confirm the stall

Do not intervene in a working migration.

1. Plug into AC power and leave the HP idle for 2 to 4 hours.
1. Check Task Manager disk activity periodically — activity means progress.
1. Confirm the percentage is truly frozen, not creeping.
1. Only proceed when hours pass with zero movement and idle disk.

### Fix 2: Unplug everything non-essential

Reduce the migration workload immediately.

1. Disconnect docks, printers, USB drives, and external monitors.
1. Remove SD cards; disconnect Bluetooth devices.
1. Leave only power connected.
1. Wait one more hour — simplified hardware unblocks many 61% stalls.

### Fix 3: Force the restart and let it roll back

The safe intervention for a confirmed stall.

1. Hold the power button 10 seconds to force off.
1. Power on and let the automatic rollback complete (30–60 minutes).
1. Log in and verify the previous build in **Settings** > **System** > **About**.
1. Your system is intact — the failed attempt's migration data is discarded.
1. If the machine hangs on reboot instead of rolling back, see [update stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).

### Fix 4: Update HP drivers before retrying

The fix that prevents the second stall.

1. Visit [HP support](https://support.hp.com/us-en), enter your model, update chipset and storage drivers first.
1. Update peripheral drivers: card reader, fingerprint sensor, webcam.
1. Update or reinstall **HP Support Assistant**.
1. Temporarily uninstall third-party antivirus — filter drivers are prime 61% suspects.

### Fix 5: Clear the failed attempt and repair

Give the retry a clean foundation.

1. Stop the update services and rename `SoftwareDistribution` and `catroot2`.
1. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow`.
1. Ensure 30 GB free on C:.
1. Restart — the retry now starts without the previous attempt's corrupted state.

### Fix 6: Retry the feature update properly

The attempt engineered to succeed.

1. Unplug externals, disable antivirus, close all apps.
1. Run the update on AC power and leave the machine alone.
1. Monitor the first hour — past 61% means the driver fix worked.
1. If it stalls at 61% again, the blocking driver is still unidentified: check `C:\$Windows.~BT\Sources\Panther\setupact.log`.

### Fix 7: Use the step-by-step 61% playbook for persistent stalls

When HP-specific fixes are not enough.

1. Follow the generic [61% step-by-step guide](/articles/how-to-fix-feature-update-stuck-at-61-percent-step-by-step/) for the full driver-hunt procedure.
1. Consider the Installation Assistant as an alternate orchestration.
1. As a final measure, the in-place upgrade via ISO bypasses Windows Update's orchestration.
1. Document the blocking driver once found — HP's [support site](https://support.hp.com/us-en) may have a newer revision that migrates cleanly.

### Fix 8: Align BIOS device settings with installed drivers

Removes firmware-driver contradictions that stall migration.

1. Enter BIOS with **F10** during HP boot and review the device configuration.
1. Enable devices you use; for devices disabled here, uninstall their drivers in Windows.
1. Pay special attention to the card reader, fingerprint sensor, and webcam entries.
1. Save, boot normally, and retry — a consistent hardware view migrates cleanly.

## Closing

The 61 percent stall on HP laptops is driver migration waiting on a driver that will not migrate — usually storage, chipset, or an HP peripheral driver. Wait it out properly, roll back safely, update the HP driver stack, clear the failed attempt, and retry lean. The percentage that haunted you becomes the one you sail past, and that is the whole trick: fix the driver, and the migration finishes itself. Note which device was the blocker and keep its driver current; migration stalls are recurrent by nature, and the same device tends to cause the next one if neglected. Patience remains part of the method even after the fix: the retry migration on a healthy driver set still takes time, and interrupting it recreates the exact corrupted state you just cleared. Give the retry the same unhurried window you gave the diagnosis. The 61 percent mark passes without drama when the drivers are right — and watching it sail past is one of the more satisfying moments in Windows troubleshooting.
