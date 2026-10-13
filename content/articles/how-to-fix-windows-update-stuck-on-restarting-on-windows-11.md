---
title: "Windows Update Stuck on 'Restarting' in Windows 11: How to Fix It"
slug: how-to-fix-windows-update-stuck-on-restarting-on-windows-11
date: 2026-10-07
categories: ["windows-update"]
tags: ["stuck on restarting", "windows update", "windows 11", "boot hang", "restart loop"]
description: "Windows 11 stuck on the 'Restarting' screen after an update? Diagnose the hang, recover safely, and fix the driver or service causing it."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-on-windows-11.webp"
faqs:
  - q: "How long should the Restarting screen last during an update?"
    a: "A normal update restart takes a few minutes, occasionally up to 30 minutes for large feature updates on slow drives. Give it a full hour before intervening. The Restarting screen shows no progress details, so a slow install phase looks identical to a hang — the disk activity light is your truth-teller. Blinking means work is happening; an hour of darkness means a genuine stall."
  - q: "Is it safe to force restart when stuck on Restarting?"
    a: "Yes, after the full wait window with zero disk activity. The update phase that was running will either resume or roll back on the next boot — Windows is designed for this. Hold the power button for ten seconds, wait 30 seconds, and power on. Do not interrupt the boot that follows; let Windows complete whatever recovery it starts."
  - q: "What causes the Restarting screen to hang after an update?"
    a: "The usual suspects are a driver that fails to unload during the restart transition, a Windows service that will not stop, Fast Startup replaying a bad state, or the update's install phase stalling mid-restart. External peripherals with misbehaving drivers also hang the restart handshake. The event logs after recovery usually name the exact culprit."
  - q: "Will this keep happening with every update?"
    a: "Not if you fix the underlying cause. A one-time hang can come from a transient driver glitch, but repeat hangs point to a specific driver, service, or Fast Startup conflict that needs addressing. The steps in this guide — driver updates, Fast Startup disable, event log diagnosis — convert a recurring hang into a one-time event."
---

The update installed, Windows asked for a restart, and now the screen says 'Restarting' with the spinning dots — for an hour, then two. This is the limbo state of Windows Update: the old session will not fully stop, the new one cannot fully start, and the screen gives you no information about which side is stuck.
The restart transition is one of the most driver-intensive moments in Windows. Every driver must unload cleanly, every service must stop, the kernel hands off, and then everything reverses on the way back up. A single driver that refuses to unload, a service that hangs on stop, or an update phase that stalled mid-restart will freeze the whole sequence at the 'Restarting' screen. External peripherals add their own handshake delays to the mix.
The recovery below is ordered: verify the hang, force the restart safely, diagnose from the event logs, fix the identified cause, and prevent recurrence. If the machine boots but then hangs differently, the generic [stuck-on-restarting fix](/articles/windows-11-stuck-on-restarting-screen-fix/) covers the boot-side variant, and for machines that rolled back instead the [undoing-changes guide](/articles/how-do-i-fix-windows-update-says-undoing-changes-made-to-your-computer/) is the companion piece.

## Why this happens

- **A driver refuses to unload.** Storage or network drivers that mishandle the restart transition hang the sequence.
- **A service will not stop.** A hung service blocks the shutdown half of the restart indefinitely.
- **The update's install phase stalled.** The restart-triggered install phase froze mid-operation with no timeout.
- **Fast Startup replays a bad state.** The hybrid shutdown cache can trap the machine in a broken restart loop.
- **An external peripheral hangs the handshake.** Docks and USB devices with bad drivers stall the restart negotiation.
- **Corrupted update files.** Damaged payloads make the restart-phase installer retry forever.
- **Low disk space.** The restart-phase staging needs working room that is not there.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the hang with the activity light

The Restarting screen hides all progress. The disk activity light reveals whether the machine is working or frozen.

1. Note the time the Restarting screen appeared, then wait one full hour.
2. Watch the disk activity light continuously: blinking means the restart is progressing.
3. Listen for fan and drive noise as a secondary indicator of activity.
4. Proceed only after a full hour with zero light activity and an unchanged screen.

### Fix 2: Force the restart safely

A verified hang will not clear on its own. Forcing the restart is safe — Windows resumes or rolls back the update on the next boot.

1. Hold the power button for 10 seconds until the machine powers off.
2. Disconnect all external devices, docks, and USB peripherals.
3. Wait 30 seconds, then power on and do not interrupt the boot sequence.
4. Let Windows complete any 'working on updates' or rollback screens that appear.

### Fix 3: Read the event logs for the culprit

After recovery, the logs record what hung. This turns the next fix from guesswork into a targeted repair.

1. Open Event Viewer and check Windows Logs > System around the time of the hang.
2. Look for Service Control Manager errors naming a service that failed to stop in time.
3. Check for driver warnings from storage or network drivers in the same window.
4. Note the exact service or driver name — it is the target of the next fixes.

### Fix 4: Update or replace the hanging driver

Driver unload hangs are the most common identified cause. Refresh the driver the logs implicated.

1. Open Device Manager and locate the device from the event log findings.
2. Update its driver from the laptop or component manufacturer's support site.
3. If the driver was recently updated, use Roll Back Driver to revert it.
4. Check the official [Microsoft support guidance](https://support.microsoft.com/en-us/windows) for known bad driver versions.

### Fix 5: Disable Fast Startup

Fast Startup's hybrid state is a documented source of restart hangs. A full shutdown gives the restart a clean foundation.

1. Open Control Panel > Power Options > Choose what the power buttons do.
2. Click 'Change settings that are currently unavailable.'
3. Uncheck 'Turn on fast startup' and save changes.
4. Restart once normally so the change takes effect.

### Fix 6: Reset the update cache

If the hang came from a stalled update phase rather than a driver, corrupted cache files are the suspect.

1. In an elevated Command Prompt, run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands and reboot.
4. Retry the update and watch the restart phase closely.

### Fix 7: Prevent recurrence with clean restart habits

A few habits keep the restart transition reliable for future updates.

1. Disconnect docks and non-essential USB devices before major updates.
2. Keep drivers current — set a quarterly reminder to check the manufacturer's site.
3. Check [Dell's support site](https://www.dell.com/support) or your vendor's equivalent for BIOS updates that improve restart behavior.
4. Leave Fast Startup off if your machine has hung at restart more than once.

### Fix 8: Test the restart with a clean boot

If hangs recur, a clean boot isolates whether a third-party service is the hanging party. It is the definitive test for service-caused restart hangs.

1. Press Win+R, type `msconfig`, and press Enter.
2. On the Services tab, check 'Hide all Microsoft services', then click Disable all.
3. On the Startup tab, open Task Manager and disable all startup items, then reboot.
4. If restarts are now clean, re-enable services in halves until the culprit returns — then leave it disabled or update it.

## Closing

The 'Restarting' hang is a transition problem: something would not let go on the way down, or would not start on the way up. Verify the hang, force the restart, read the logs to name the culprit, and fix that specific driver or service. One targeted repair beats ten blind retries, and the next update's restart will be the uneventful one it should have been.
