---
title: "Fix Windows Update Stuck on 'Restarting' in Windows 11 24H2"
slug: how-to-fix-windows-update-stuck-on-restarting-in-windows-11-24h2
date: 2026-09-06
categories: ["windows-update"]
tags: ["stuck on restarting", "windows 11 24h2", "update hang", "restart loop"]
description: "Windows 11 24H2 update stuck on the 'Restarting' screen? Learn when to wait, when to intervene, and how to recover safely."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-in-windows-11-24h2.webp"
faqs:
  - q: "How long is too long on the 'Restarting' screen?"
    a: "Up to 30–60 minutes can be normal during a feature update as drivers migrate. Beyond 2 hours with no disk activity (no drive light, no sounds), it is stuck. For a routine cumulative update, anything past 60–90 minutes deserves attention."
  - q: "Is it safe to force-shut-down during 'Restarting'?"
    a: "One forced shutdown is generally safe — Windows is designed to roll back an interrupted update. Hold the power button 10 seconds, wait 30 seconds, then power on. Avoid repeated forced shutdowns, which compound the risk. If the first forced shutdown does not resolve it, use the recovery environment instead of forcing it again."
  - q: "Why does the update get stuck on restarting?"
    a: "The restart phase is when drivers migrate and boot configuration updates. A driver that hangs during migration, a peripheral that will not re-enumerate, or a corrupt staged payload freezes the process with the spinner still turning. The animated spinner is misleading — it proves the UI thread is alive, not that the update is progressing."
  - q: "What if it says 'Undoing changes' after I force a restart?"
    a: "That is the expected rollback — Windows detected the interrupted update and is restoring the previous state. Let it finish; it can take 30+ minutes. Do not interrupt the rollback. Interrupting the rollback is the one action that can turn a recoverable failed update into an unbootable machine."
---

Few screens inspire as much dread as Windows' blue 'Restarting' with its endlessly circling dots — especially when it has been circling for two hours. During a Windows 11 24H2 update, the restart phase is where the real work happens: drivers migrate, the boot environment reconfigures, and the new system comes online. When it stalls here, the machine looks alive but is going nowhere.

The critical skill is distinguishing 'slow' from 'stuck'. Feature updates legitimately spend a long time in this phase, and intervening too early can interrupt a healthy install. But a genuinely frozen restart needs exactly one decisive action — a forced shutdown followed by a proper diagnosis — not hours of hopeful waiting.

This guide gives you the wait/intervene decision rule, the safe recovery sequence, and the fixes that prevent the next update from stalling the same way. If the machine rolled back with an 'undoing changes' message, our ['couldn't complete the updates' troubleshooting guide](/articles/we-couldn-t-complete-the-updates-undoing-changes-troubleshooting/) picks up from there.

## Why this happens

- **Driver migration hang:** A driver that cannot migrate to 24H2 hangs the boot process indefinitely while the spinner keeps animating.
- **Peripheral re-enumeration failure:** Docks, USB devices, or SD cards that fail to re-enumerate during restart block the boot sequence.
- **Corrupt staged update payload:** Damaged files staged for the restart phase fail verification in a loop that never surfaces an error.
- **Boot configuration damage:** A damaged BCD or EFI boot entry leaves the restart with nowhere to go.
- **Disk errors on the system volume:** Bad sectors in the middle of the migration area freeze file operations silently.
- **Third-party boot-level software:** Disk encryption, third-party boot managers, or AV early-launch drivers conflicting with the new boot environment.
- **Power interruption:** A charger disconnect or sleep during the critical phase corrupting the in-progress migration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Apply the wait rule: verify activity before acting

Never force a shutdown on a timer alone. Check for signs of life first.

1. Look for disk activity: drive LED, faint drive sounds, or occasional fan changes.
2. For a feature update, allow up to 2 hours; for a cumulative update, up to 90 minutes.
3. If there is zero activity for over an hour past those windows, proceed to force a shutdown. If there is activity, keep waiting.

### Fix 2: Perform one clean forced shutdown

A single decisive shutdown triggers the automatic rollback machinery. Repeated power-cycling is what causes real damage.

1. Hold the power button for a full 10 seconds until the machine powers off.
2. Unplug all peripherals — docks, USB drives, printers, SD cards.
3. Wait 30 seconds, reconnect only the charger, and power on.
4. Let whatever happens next finish: normal boot, automatic repair, or 'Undoing changes' rollback — do not interrupt it.

### Fix 3: Boot into recovery if it will not start normally

If the forced shutdown leads to a boot loop or black screen, use the recovery environment.

1. Force WinRE: power off during the Windows logo twice in a row; on the third boot, Automatic Repair should appear.
2. In WinRE, try Startup Repair first.
3. If that fails, use System Restore to roll back to a pre-update restore point.
4. As a last resort here, 'Uninstall latest quality/feature update' in WinRE removes the offending update directly.

### Fix 4: Disconnect peripherals and retry the update

Peripherals are the most common cause of restart-phase stalls. Eliminate them before the next attempt.

1. Keep only the charger connected for the entire next update attempt.
2. Remove docks, USB hubs, external drives, printers, and SD cards.
3. Disable Bluetooth devices temporarily.
4. Run the update again and monitor the restart phase.

### Fix 5: Update BIOS and storage drivers before retrying

The restart phase lives or dies on storage and firmware. Bring them current.

1. Install the latest BIOS/UEFI from your laptop manufacturer's support site with the charger connected.
2. Update chipset and storage drivers to the newest vendor-provided versions.
3. Reboot normally to confirm stability, then retry the Windows update.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) also documents the update prerequisites worth checking before a retry.

### Fix 6: Repair the boot configuration

If the machine boots to errors or loops after the stall, the BCD may be damaged.

1. Boot into WinRE → Troubleshoot → Advanced options → Command Prompt.
2. Run `bootrec /fixmbr`, `bootrec /fixboot` (if it errors, use the bcdboot method), `bootrec /rebuildbcd`.
3. Alternatively: `bcdboot C:\Windows /s S: /f UEFI` (adjust drive letters to your EFI partition).
4. Reboot and confirm normal startup before attempting the update again.

### Fix 7: Run the update from a clean boot state

Minimize third-party interference for the retry, especially boot-level software.

1. Uninstall third-party antivirus temporarily; pause third-party disk encryption if you use it.
2. Run `msconfig` → selective startup, disabling non-Microsoft services.
3. Retry the update with peripherals disconnected.
4. If the restart phase completes cleanly this time, re-enable services one group at a time to identify the culprit — and check the [Lenovo undoing-changes guide](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-lenovo-laptop/) if the rollback instead gets stuck.

### Fix 8: Retry with a minimal driver set enabled

Unplugging peripherals removes external drivers from the migration, but internal devices — fingerprint readers, SD controllers, Bluetooth radios — still migrate their drivers during restart. Temporarily disabling them shrinks the migration surface further for the retry.

1. Open Device Manager and disable (do not uninstall) non-essential internal devices: fingerprint reader, SD host controller, Bluetooth, and any imaging devices.
2. Keep display, storage, network, keyboard, and mouse enabled — the system needs those to complete the update.
3. Run the Windows update and monitor the restart phase.
4. After the update completes, re-enable the devices one by one; Windows redetects each normally.
5. If the restart phase now completes, re-enable in small groups to identify which device's driver was the staller.

## Closing

A Windows update stuck on 'Restarting' is a judgment call: verify real activity, wait out the legitimate windows, then intervene exactly once with a clean forced shutdown. Recover through WinRE if needed, strip peripherals and update firmware before retrying, and repair the boot configuration if the stall damaged it. Patience first, then one decisive action — that order keeps a stuck update from becoming a broken machine.
