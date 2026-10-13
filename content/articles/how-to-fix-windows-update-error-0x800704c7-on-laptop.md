---
title: "Windows Update Error 0x800704c7 on Laptop: Fix Guide"
slug: how-to-fix-windows-update-error-0x800704c7-on-laptop
date: 2026-09-25
categories: ["windows-update"]
tags: ["windows update error 0x800704c7", "error_cancelled", "update cancelled error", "windows update keeps cancelling"]
description: "Error 0x800704c7 means the update operation was cancelled. Find what cancelled it, remove the interference, and complete the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800704c7-on-laptop.webp"
faqs:
  - q: "What does error 0x800704c7 mean?"
    a: "It means ERROR_CANCELLED: the update operation was cancelled before it could complete. The cancellation can come from the user, from antivirus software terminating the installer, from a conflicting program, or from a service stopping unexpectedly mid-operation. The pattern of when it cancels usually identifies the culprit."
  - q: "Can antivirus cancel a Windows Update?"
    a: "Yes. Antivirus products occasionally identify update payload behavior as suspicious and terminate the installer process. This is one of the more common causes of 0x800704c7, and temporarily disabling real-time protection is the standard diagnostic test. If the update then completes, you have found your canceller."
  - q: "Why would Windows cancel its own update?"
    a: "Usually it does not; something else cancels it. The exceptions are servicing conflicts, where the servicing stack aborts an operation that conflicts with another, and user action, such as shutting down or running a cleaner at the worst possible moment."
  - q: "Is it safe to retry immediately after 0x800704c7?"
    a: "Yes, retrying is safe. The cancellation happens before changes are committed in most cases, so the system is left as it was. Clear the suspected interference first, such as antivirus or cleaners, then retry the update normally. The system keeps no record of the cancelled attempt beyond the history entry."
---

Error 0x800704c7 is the update that never got to finish because something cancelled it. The code is the system's ERROR_CANCELLED, and it is refreshingly non-technical: an operation started, and before it completed, a cancellation arrived.

The interesting question is always who sent the cancellation. Sometimes it was you — a shutdown, a restart, or a cleanup tool run at exactly the wrong moment. More often on laptops it is a third party: antivirus software terminating the installer, a system utility killing the update service, or a conflicting program aborting the shared servicing operation.

The fix is therefore a whodunit. Identify the canceller, remove it from the scene, and the update proceeds uninterrupted.

Cancellation is an action, and actions have actors. Error 0x800704c7 means something acted to stop your update, and on a laptop the actor is rarely you. Antivirus software, scheduled cleaners, and conflicting installers are the usual suspects, each with a recognizable pattern. The steps below identify the actor by its pattern and remove it from the scene.

## Why this happens

- **Antivirus terminating the installer.** Security software occasionally kills the update process mid-operation, triggering the cancelled status.

- **User shutdown or restart mid-update.** Powering off during the install phase cancels the operation, sometimes leaving this code in history.

- **Cleanup tools run during updates.** Disk cleaners that purge the update cache while an install is active abort the operation.

- **Conflicting program aborting servicing.** Another installer or servicing tool cancelling the shared operation cancels everything attached to it.

- **Update services stopping unexpectedly.** If wuauserv or BITS crashes mid-operation, the operation reports as cancelled.

- **Corrupt update cache.** Damaged state can make the pipeline abort its own operations.

- **Third-party system utilities.** Tweakers and optimizers that meddle with services can cancel update operations as a side effect.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Simply retry the update

If the cancellation was a one-off — an accidental shutdown, a transient AV hiccup — a clean retry succeeds. Do not overthink the first attempt. Watch the retry rather than walking away; if it cancels at exactly the same percentage each time, the canceller is deterministic and the later steps will find it.

1. Open Settings, then Windows Update.
2. Click Check for updates or Retry and let it run to completion without interruption.
3. Avoid shutting down or running cleaners until it finishes.

### Fix 2: Fix 2: Temporarily disable third-party antivirus

AV termination of the installer is the leading third-party cause. Disabling real-time protection for the duration of the update removes the prime suspect. Some antivirus products have a dedicated tamper-protection switch that must be disabled before real-time protection will actually turn off; check for it if the disable seems to have no effect.

1. Disable your third-party antivirus real-time protection.
2. Run the update to completion.
3. Re-enable protection immediately. Windows Security covers you in the meantime.

### Fix 3: Fix 3: Close cleaners and system utilities

Disk cleaners, tweakers, and optimizers should not run during updates. Close them fully, including their background tray processes, before retrying. Do not forget scheduled tasks; a cleaner set to run hourly in Task Scheduler can strike mid-update even with its main window closed.

1. Exit any disk cleaner, optimizer, or tweaking utility completely.
2. Check Task Manager's background processes for their services and stop them.
3. Retry the update with the field clear.

### Fix 4: Fix 4: Verify the update services are healthy

If the services keep stopping on their own, the operations they host keep getting cancelled. Check that the key services are running and set correctly. In the service properties, check the Recovery tab too; a service set to restart aggressively on failure can create a cancel-and-retry loop.

1. Press Win + R, type `services.msc`, and press Enter.
2. Confirm Windows Update, Background Intelligent Transfer Service, and Cryptographic Services are running.
3. Set any that are stopped to start, using Manual or Automatic startup types as appropriate.

### Fix 5: Fix 5: Clean-boot and retry

A clean boot silences every third-party canceller at once. If the update completes clean-booted, something in your normal startup was doing the cancelling. If the update completes clean-booted, the most efficient identification method is binary search: re-enable half the services, test, and halve again.

1. In `msconfig`, hide all Microsoft services and disable the rest.
2. Disable all startup items in Task Manager, restart, and run the update.
3. Re-enable in halves afterward to identify the canceller.

### Fix 6: Fix 6: Clear the update cache

A damaged cache can cause the pipeline to abort its own operations. Clearing it gives the retry pristine state to work with. After clearing the cache, the first check rebuilds the database; give it several minutes before concluding the retry also failed.

1. Open Terminal as administrator, then run `net stop wuauserv` and `net stop bits`.
2. Delete everything in C:\Windows\SoftwareDistribution\Download.
3. Run `net start wuauserv` and `net start bits`, then retry.

If the retry keeps getting cancelled at the same point, sidestep the pipeline entirely — our [manual update install guide](/articles/how-to-manually-install-windows-update-on-windows-11/) shows how to fetch the package from the Catalog and install it by hand.

### Fix 7: Fix 7: Uninstall the failed update, then reinstall

If the code is attached to a specific update that keeps cancelling, remove that update's partial state and let it install fresh. When uninstalling, remove only the update tied to the failure; bulk-removing updates widens the servicing surface and can introduce new problems.

1. Open Settings, then Windows Update, then Update history, then Uninstall updates.
2. Remove the most recent update matching the failure, restart, and check for updates.
3. For persistent installer-side failures, our [0x80070643 installer guide](/articles/how-to-fix-windows-update-error-0x80070643-on-laptop/) covers the deeper repairs, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the official process.

## Closing

Error 0x800704c7 is an interruption, not a breakage: something cancelled the operation, and removing the interrupter lets it finish. Antivirus and ill-timed cleanups are the usual suspects on laptops. Once the field is clear, updates complete normally. If the failure moves into the installer itself, see our [0x80070643 walkthrough](/articles/how-to-fix-windows-update-error-0x80070643-on-laptop/), and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the official troubleshooting sequence.
