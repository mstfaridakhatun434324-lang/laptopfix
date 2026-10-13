---
title: "How to Fix Windows Update Stuck on ‘Restarting’ on a Dell Laptop"
slug: how-to-fix-windows-update-stuck-on-restarting-on-dell-laptop
date: 2026-09-16
categories: ["windows-update"]
tags: ["windows update stuck on restarting", "dell laptop restarting loop", "restarting screen frozen", "fast startup fix"]
description: "Dell laptop stuck on the Restarting screen during Windows Update? Shut down safely, disable Fast Startup, and remove the driver blocking shutdown."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-on-dell-laptop.webp"
faqs:
  - q: "Why does this only happen during updates?"
    a: "Updates force the full restart that unmasks a shutdown problem which was always there. The hanging driver or service predates the update — you simply never saw it, because everyday restarts may have been fast startups (not full shutdowns) or because you rarely restart at all."
  - q: "Can a USB device really block a restart?"
    a: "Absolutely. When a device's driver declines the shutdown request, Windows waits for it instead of forcing the issue — and that wait can last indefinitely. Docks, external drives, and certain USB audio devices top the suspect list. The one-minute test — unplug everything and restart — exposes this cause instantly."
  - q: "Will disabling Fast Startup slow my boot a lot?"
    a: "Hardly. With an SSD the difference is a couple of seconds. Fast Startup's hybrid shutdown is behind a disproportionate share of restart hangs, driver resume glitches, and dual-boot headaches — the seconds it saves are not worth the instability on machines it affects. Almost nobody notices the change afterward."
  - q: "What if it hangs on Restarting even without updates?"
    a: "Then the update was never the cause — some driver or service on your system is the culprit. Use the clean-boot procedure to isolate it, refresh drivers from Dell support, and scan the drive for errors. The update merely delivered the restart that exposed a pre-existing shutdown defect; repairing the underlying hang fixes updates as a side effect."
---

A Dell laptop frozen on the Restarting screen mid-update has not actually begun installing — it is still trying to shut down cleanly. That is good news: forcing the machine off now interrupts a shutdown, not an install, so the corruption risk is far lower than most people fear. Windows anticipates this situation and usually resumes or rolls back gracefully. [how other brands handle the stuck-restarting problem](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-on-lenovo-laptop/)

One Dell-specific pattern deserves attention: SupportAssist and Dell power-management services sometimes keep shutdown-blocking handles open — particularly when SupportAssist was installing a driver the moment the restart began. The forced-shutdown procedure plus the SupportAssist check below resolve a large share of these cases without touching Windows itself.

## Why this happens

- **The update engine wedged mid-transaction.** Windows Update itself froze while shutting down. The troubleshooter dissolves the wedged update transaction.
- **A device stonewalling shutdown.** A USB device whose driver refuses to let go. Docks and external drives are the classic device blockers.
- **A corrupted shutdown transaction.** Damaged servicing state unable to complete the handoff. Half-finished servicing transactions also sabotage clean shutdowns.
- **A third-party antivirus hook.** Security software meddling with shutdown calls. Pause protection for testing instead of uninstalling.
- **A struggling drive.** Sluggish storage stretches shutdown past its timeouts. chkdsk C: /f plus a SMART check answers the drive question.
- **A backlog of pending file operations.** An enormous queue of pending renames slowing shutdown to a crawl. Only touch pending.xml after reboots fail to drain it.
- **A BIOS power-management defect.** Firmware mishandling the restart signal under update conditions. Dell BIOS changelogs sometimes reference restart or power-behavior fixes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off Fast Startup

Hybrid shutdown manufactures restart hangs. SupportAssist background services occasionally keep shutdown-blocking handles open — most often when SupportAssist was mid-driver-install as the restart began.

1. In Control Panel, open Power Options, then "Choose what the power buttons do".
2. Select "Change settings that are currently unavailable".
3. Clear the "Turn on fast startup" checkbox.
4. Save, then verify with an ordinary restart.
5. Leave it off permanently — the seconds it saves are not worth the trouble it causes.
6. Reconnect peripherals individually with a restart between each to pinpoint the blocking device.

### Fix 2: Clear out stuck SupportAssist operations

Release any Dell service gripping the shutdown. Fast Startup's hybrid shutdown underlies a large share of restart hangs, so disabling it works as both repair and diagnostic.

1. Open SupportAssist and hunt for driver or BIOS operations still in progress.
2. Allow them to finish, or cancel whichever are stuck.
3. Before the next update restart, end Dell-branded background processes in Task Manager.
4. During update cycles, consider setting SupportAssist updates to manual.
5. Restart normally and confirm shutdown completes.
6. Verify Fast Startup is still off after rebooting — certain updates turn it back on quietly.

### Fix 3: Bring drivers current from Dell support

Swap out the drivers likeliest to stall shutdown. A USB device whose driver refuses to let go can block shutdown indefinitely — the unplug-everything test proves it in one reboot.

1. From [Dell's support site](https://www.dell.com/support), grab the newest chipset, storage, and network drivers.
2. Install them while the charger is connected.
3. Reboot after each major driver.
4. Flash a newer BIOS too if one is available.
5. Modern drivers unload cleanly; outdated ones are the clingers.
6. Before the next update attempt, confirm SupportAssist reports no stuck operations.

### Fix 4: Dissolve the wedged update state

Have the update troubleshooter dissolve the stuck update transaction. The engine can jam mid-transaction while shutting down; the troubleshooter aims at exactly that condition.

1. Navigate to Settings > System > Troubleshoot > Other troubleshooters.
2. Launch the Windows Update troubleshooter.
3. Apply all its recommendations, then restart.
4. Retry the update from a clean-boot state.
5. That removes the half-transacted update possibly re-hanging shutdown.
6. Retry the update from the clean state, timing the restart phase.

### Fix 5: Update from a clean boot

Determine whether a third-party service is the blocker. A clean boot (msconfig with non-Microsoft services disabled) implicates third-party services when the hang reproduces.

1. Press Win + R, enter msconfig, and press Enter.
2. Under the Services tab, check "Hide all Microsoft services", then choose Disable all.
3. Under the Startup tab, open Task Manager and switch off every startup item.
4. Restart and run the update from this minimal state.
5. If the restart succeeds, re-enable services in batches to corner the blocker.
6. Search Event Viewer for shutdown warnings naming the hanging component.

### Fix 6: Examine the drive for errors

A failing drive stretches shutdown beyond its timeouts. After a hang, the System event log's event ID 1074 and 6006 entries reveal what Windows was waiting for.

1. In an elevated Command Prompt, run chkdsk C: /f.
2. Schedule it for the next restart and allow it to finish.
3. Review SMART data with Dell diagnostics.
4. Replace a failing drive — shutdown hangs are an early symptom.
5. Do not shrug off repeated chkdsk findings.
6. If you clean-booted, re-enable services in halves to find the blocker faster.

### Fix 7: Uninstall the update from WinRE if it loops

When every restart hangs, remove the update that triggered it. If restarts hang with nothing pending, the update is innocent — treat it as a general shutdown defect.

1. Interrupt two consecutive boots to force WinRE.
2. Choose Troubleshoot > Advanced options > Uninstall Updates.
3. Remove the latest quality update, then restart.
4. Confirm normal restarts work before reinstalling anything.
5. Research the KB for documented restart-hang reports before attempting it again.
6. Write down the culprit — restart hangs recur with every update until the driver or service is repaired.

## Closing

A restart hang during updates is almost always a pre-existing shutdown flaw the update merely exposed. Repair the hanging driver or service once and every future update benefits. When the hang follows you outside update season, treat it as a system issue first — and for install-phase hangs, see [the undoing-changes loop guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-after-windows-11-update/).
