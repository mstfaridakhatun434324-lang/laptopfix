---
title: "Windows 11 Update Error 0x800704C7: Unblock the Cancelled Update"
slug: how-to-fix-windows-update-error-0x800704c7-on-windows-11
date: 2026-09-08
categories: ["windows-update"]
tags: ["windows update", "0x800704c7", "windows 11", "cancelled", "operation cancelled"]
description: "Error 0x800704C7 means the update was cancelled — by you, by software, or by policy. Find who cancelled it and get the update through."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800704c7-on-windows-11.webp"
faqs:
  - q: "What does error 0x800704C7 mean in Windows Update?"
    a: "The operation was cancelled — ERROR_CANCELLED. Something stopped the update mid-flight: you may have cancelled it, a third-party program may have interfered, a policy may forbid it, or the system may have aborted it during shutdown or sleep."
  - q: "I did not cancel anything. Why 0x800704C7?"
    a: "Cancellation is not always yours. Antivirus suites, system optimizers, aggressive debloaters, and even Windows shutting down for a scheduled restart can cancel update operations. The code records that it stopped, not who stopped it. Event Viewer usually names the actual canceller within a minute's logs."
  - q: "Can sleep mode cause 0x800704C7?"
    a: "Yes. Laptops that sleep or hibernate mid-update can abort the operation when power state changes interrupt the installer. Keep the laptop awake and plugged in during updates to eliminate this cause. Set sleep to Never temporarily and keep the charger connected during updates."
  - q: "Will the cancelled update damage my system?"
    a: "No. Windows Update is transactional — a cancelled operation rolls back to the pre-update state. The risk is not damage but the update never completing, leaving you unpatched. If large upgrades are the ones cancelling, our [24H2 failure guide](/articles/best-way-to-fix-feature-update-to-windows-11-24h2-failed/) covers the heavy cases."
---

Error 0x800704C7 is Windows 11's cancelled stamp: the update started, something stopped it, and the system recorded the interruption. The word cancelled makes people assume they clicked something — sometimes true, often not. In practice, the canceller is frequently invisible: a security suite killing the installer process, a scheduled shutdown landing mid-update, the laptop sleeping at the wrong moment, or a policy quietly forbidding the operation.

The repair is therefore an investigation into who or what keeps stopping the work. You will rule out the accidental causes first (power, sleep, shutdowns), then the software causes (antivirus, optimizers), then the policy causes — and finally repair any damage the repeated cancellations left in the update client itself.

Think of it as detective work with a simple question: who keeps cancelling my updates?

## Why this happens

- **User cancellation**: Clicking cancel, or shutting down during the install phase.
- **Sleep or hibernate interruption**: Power state changes aborting the installer mid-operation.
- **Antivirus interference**: Security suites killing update processes they misjudge.
- **System optimizer meddling**: Cleaners or debloaters stopping update services mid-run.
- **Scheduled restarts**: Maintenance or third-party schedulers rebooting during updates.
- **Policy restrictions**: Group or registry policies cancelling disallowed operations.
- **Corrupt client state**: Damage from repeated cancellations making new attempts abort early.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Keep the laptop awake and plugged in

Eliminate the accidental cancellations first. Updates that die when the lid closes or the battery sags are not a software problem — they are a power problem, and the fix is trivial.

1. Plug in the charger — never run updates on battery alone.
2. Go to Settings > System > Power & battery and set Screen and sleep timeouts to Never temporarily.
3. Close the lid action: set it to Do nothing in Control Panel > Power Options while updating.
4. Retry the update with the laptop awake, plugged in, and undisturbed.

### Fix 2: Retry the update manually and watch it

A surprising number of 0x800704C7 cases are one-off interruptions. A deliberate, observed retry — with nothing else running — either succeeds or reveals the actual canceller in action.

1. Close all applications and pause cloud syncs.
2. In Settings > Windows Update, click Check for updates and then Download & install.
3. Stay with the laptop; note exactly when and how it stops, and any program that pops up.
4. If it completes, the original was a fluke — if it cancels again, you now have a timestamp to investigate.

### Fix 3: Pause third-party security and optimizers

Security suites and system optimizers are the most common invisible cancellers. They see installer processes doing unusual things and kill them protectively — including Windows' own updaters.

1. Temporarily disable your third-party antivirus and any system optimizer or cleaner.
2. Retry the update immediately while they are down.
3. If it succeeds, the suite was the canceller: update it to the latest version and add Windows Update processes to its exclusions.
4. Re-enable protection afterward — the test is diagnostic, not a permanent state.

### Fix 4: Check for shutdown and restart schedulers

Something rebooting the laptop on a schedule — Windows' own active-hours violations, a third-party scheduler, or a UPS signaling shutdown — cancels updates reliably and invisibly.

1. Check Settings > Windows Update > Advanced options > Active hours and set them to cover your real usage.
2. Open Task Scheduler (taskschd.msc) and look for tasks that reboot or shut down the machine.
3. Check any UPS software for aggressive low-battery shutdown thresholds.
4. Disable or reschedule the offenders, then retry the update.

### Fix 5: Run the Windows Update troubleshooter

Repeated cancellations can leave the update client in a damaged state where new attempts abort immediately. The troubleshooter repairs that fallout and resets the client's expectations.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter and apply every fix.
3. Restart the laptop.
4. Attempt the update again with the machine awake and plugged in.

### Fix 6: Reset the update components

Half-cancelled operations leave partial state that confuses subsequent attempts. Clearing the caches gives the next attempt a clean transactional starting point.

1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
2. Rename SoftwareDistribution to SoftwareDistribution.old and catroot2 to catroot2.old.
3. Restart the four services and reboot.
4. Run the update from the clean state.

### Fix 7: Check policies that may forbid the update

On formerly managed machines, leftover policies can cancel operations the policy disallows. If the cancellations feel systematic rather than random, look here.

1. Run gpedit.msc (Pro editions) and review Computer Configuration > Administrative Templates > Windows Components > Windows Update for restrictive settings — set unknowns to Not configured.
2. In regedit, check HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate for blocking values.
3. Consult [Microsoft's support hub](https://support.microsoft.com/en-us/windows) if a specific policy's effect is unclear.
4. Reboot and retry after cleaning.

### Fix 8: Trace the canceller, then update in Safe Mode

When the canceller stays hidden, combine detection with evasion. Event Viewer names the culprit from the system logs, while Safe Mode with Networking strips out third-party drivers and services so the update can complete regardless of who was stopping it.

1. Open Event Viewer > Windows Logs > System and examine the minute around the cancellation for sleep transitions, service stops, or errors.
2. The entries adjacent to the failure usually name the canceller — address that component directly.
3. Hold Shift while clicking Restart, then choose Troubleshoot > Advanced options > Startup Settings > Restart.
4. Press 5 for Safe Mode with Networking, then run Windows Update and install the pending update.
5. Reboot normally afterward and use msconfig to identify and remove the interfering program.

## Closing

Error 0x800704C7 asks a simple question — who cancelled this? — and the answer is usually mundane: a sleeping laptop, a protective antivirus, a scheduled reboot. Remove the canceller and the update that kept dying suddenly completes without drama. If cancellations persist with no visible cause, the policy and component checks at the end of the list are where the invisible cancellers hide. Related: the [Windows 10 0x800704C7 guide](/articles/how-to-fix-windows-update-error-0x800704c7-on-windows-10/) and our [24H2 troubleshooting deep-dive](/articles/feature-update-to-windows-11-24h2-failed-troubleshooting/) for cancellations during feature upgrades.
