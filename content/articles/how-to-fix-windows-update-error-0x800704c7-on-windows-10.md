---
title: "Fix Error 0x800704C7 on Windows 10: Stop the Cancellations"
slug: how-to-fix-windows-update-error-0x800704c7-on-windows-10
date: 2026-09-09
categories: ["windows-update"]
tags: ["windows update", "0x800704c7", "windows 10", "cancelled update", "interrupted"]
description: "Windows 10 keeps cancelling updates with error 0x800704C7? Identify the interrupter — power, software, or policy — and complete the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800704c7-on-windows-10.webp"
faqs:
  - q: "What does 0x800704C7 mean on Windows 10?"
    a: "The update operation was cancelled. The canceller can be you (closing the lid, shutting down), your software (antivirus, optimizers killing the installer), the system (sleep, scheduled restart), or a policy blocking the operation. This guide eliminates them in order from most visible to most hidden."
  - q: "Why does the update cancel at the same point every time?"
    a: "A consistent cancellation point suggests a systematic cause: a scheduled task firing, a policy triggering, or the installer hitting the same conflicting process each run. Note the timing — it is the best clue you have. Write down the time of each failure; the pattern is the diagnosis."
  - q: "Can Windows 10 cancel updates by itself?"
    a: "Yes. Sleep and hibernate transitions, active-hours restarts, and the servicing stack aborting on conflicting operations can all cancel updates without any user action. The fixes below address each. An observed, undisturbed update attempt reveals which of these is responsible."
  - q: "Is my system damaged by repeated cancellations?"
    a: "No — cancelled updates roll back transactionally. But the update client's state can degrade after many aborted attempts, which is why the component reset is in the list. For the related stuck-rollback scenario, see our [undoing changes guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/)."
---

Windows 10 error 0x800704C7 is the system's way of saying the update was cancelled — and then leaving you to figure out by whom. The honest answer is that cancellation has many authors. Sometimes it is you, closing the lid at the wrong moment. Sometimes it is your antivirus, protectively murdering the installer. Sometimes it is Windows itself, sliding into sleep mid-operation or rebooting on a schedule you forgot you set.

Because the causes are so varied, the repair proceeds by elimination, from the most observable to the most hidden. Power and sleep behavior first — you can see those. Then third-party software — you can test those by disabling them. Then scheduled tasks and policies — the invisible ones. Each layer you clear either fixes it or narrows the field, and the pattern of when the cancellation strikes is evidence throughout.

Keep notes as you go: when it cancels, what was running, whether the laptop was on battery. The pattern is the diagnosis.

## Why this happens

- **Lid closed or sleep**: Power transitions interrupting the installer.
- **Shutdown during install**: User or scheduled shutdowns landing mid-operation.
- **Antivirus kills**: Security software terminating installer processes.
- **Optimizer interference**: Cleaners stopping update services aggressively.
- **Scheduled reboots**: Task Scheduler or maintenance windows rebooting mid-update.
- **Policy blocks**: Leftover management policies cancelling disallowed updates.
- **Damaged client state**: Repeated aborts corrupting the update client's expectations.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Control power during the update

Laptops are mobile, and mobility interrupts updates. Before suspecting software, make the power environment update-proof — this alone resolves the cases where the lid or the battery was the canceller.

1. Connect the charger and keep it connected for the entire update.
2. In Settings > System > Power & sleep, set both screen and sleep to Never temporarily.
3. In Control Panel > Power Options > Choose what closing the lid does, set both to Do nothing.
4. Retry the update with these settings active.

### Fix 2: Run one observed update attempt

Watch the failure happen. An observed cancellation gives you timing, phase, and any popups or toasts that an unattended run hides — all of which identify the canceller.

1. Close every application and disconnect non-essential peripherals.
2. Go to Settings > Update & Security > Windows Update and start the download and install manually.
3. Stay present and note the exact moment and phase of cancellation.
4. Check Event Viewer > Windows Logs > System around that timestamp for the cancelling event.

### Fix 3: Disable third-party interferers temporarily

Antivirus suites, system optimizers, and driver utilities are the classic invisible cancellers. A controlled test with them disabled either exonerates or convicts them in one attempt.

1. Disable your third-party antivirus (real-time and behavioral shields) and any optimizer/cleaner.
2. Immediately retry the update while they are off.
3. If it completes, update the security suite to its latest build and whitelist the Windows Update processes.
4. Turn protection back on afterward — never leave it off as a workaround.

### Fix 4: Hunt down scheduled interruptions

A reboot scheduled for 3 AM cancels a 2:55 AM install just as thoroughly as a user shutdown. These schedulers are invisible during the day, which is why the cancellation feels mysterious.

1. Open Task Scheduler and review tasks with reboot, shutdown, or maintenance actions.
2. Check Settings > Update & Security > Windows Update > Change active hours and set them generously.
3. Look at any UPS or power management software for timed shutdown actions.
4. Neutralize what you find, then retry the update during a guaranteed-quiet window.

### Fix 5: Run the troubleshooter

By this point the update client may be bruised from repeated cancellations. The troubleshooter repairs the client-side damage so the next attempt starts healthy.

1. Go to Settings > Update & Security > Troubleshoot > Additional troubleshooters.
2. Run the Windows Update troubleshooter, applying all suggested fixes.
3. Restart with Start > Power > Restart.
4. Attempt the update again.

### Fix 6: Reset components to clear aborted state

Cancelled operations leave half-written state that makes the next attempt stumble in the same place. Resetting the components wipes that history clean.

1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
2. Rename the SoftwareDistribution and catroot2 folders with .old suffixes.
3. Restart the four services.
4. Reboot and run the update fresh.

### Fix 7: Repair system files and check policies

The final layer covers damage and prohibition: corrupted servicing files that abort operations, and policies that forbid them. Both are checked here before the last-resort repair install.

1. Run DISM /Online /Cleanup-Image /RestoreHealth followed by sfc /scannow in an elevated prompt.
2. In regedit, inspect HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate and the Installer key for blocking values from old management.
3. See [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for guidance on any policy you do not recognize.
4. If cancellations persist with everything cleared, perform an in-place upgrade repair to rebuild the servicing stack.

### Fix 8: Trace the cancellation, then update in Safe Mode

Pair detective work with a workaround. The System log reveals what cancelled the update, and Safe Mode with Networking — free of third-party drivers and startup programs — lets the update install even before you have dealt with the canceller.

1. In Event Viewer > Windows Logs > System, note the exact cancellation time and read the surrounding events for the cause.
2. Open msconfig, go to the Boot tab, tick Safe boot with Network, and restart.
3. In Safe Mode, run Windows Update and install everything pending.
4. Return to msconfig, untick Safe boot, restart normally, then clean-boot to identify the canceller.

## Closing

On Windows 10, 0x800704C7 is rarely a mystery once you watch it happen — the canceller almost always shows itself in the timing. Power discipline and a quiet, observed attempt resolve most cases; the software and policy layers catch the rest. Make updates a deliberate event — plugged in, awake, undisturbed — and cancellations stop being a recurring character in your update history. Related: the [Windows 11 0x800704C7 guide](/articles/how-to-fix-windows-update-error-0x800704c7-on-windows-11/) and our [24H2 failure recovery plan](/articles/best-way-to-fix-feature-update-to-windows-11-24h2-failed/) for interrupted upgrades.
