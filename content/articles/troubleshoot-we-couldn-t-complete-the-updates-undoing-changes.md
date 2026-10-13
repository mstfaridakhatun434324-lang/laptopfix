---
title: "Troubleshoot 'We Couldn't Complete the Updates, Undoing Changes'"
slug: troubleshoot-we-couldn-t-complete-the-updates-undoing-changes
date: 2026-09-16
categories: ["windows-update"]
tags: ["couldn't complete updates", "undoing changes", "update rollback"]
description: "Seeing 'We couldn't complete the updates, undoing changes'? Diagnose why the install failed and stop the rollback loop with this ordered repair plan."
thumbnail: "/images/thumbs/troubleshoot-we-couldn-t-complete-the-updates-undoing-changes.webp"
faqs:
  - q: "What does 'We couldn't complete the updates' actually mean?"
    a: "It means Windows installed the update, ran its post-install validation, and the result failed the checks — so it automatically reversed everything. The message is the rollback notification, not the error itself. The real cause is logged separately, which is why the diagnostic steps below matter more than the message text."
  - q: "How is this different from 'Undoing changes made to your computer'?"
    a: "They are two screens of the same process. 'We couldn't complete the updates' is the failure announcement; 'Undoing changes' is the rollback in progress. You will usually see the first briefly, then the second for much longer. Both point at the same underlying install failure."
  - q: "Will this loop happen every time I shut down?"
    a: "It can, because Windows retries the failed update on the next restart or shutdown cycle. The loop continues until the blocker is fixed or the update is paused. Breaking it requires the WinRE steps below or pausing updates while you repair the root cause."
  - q: "Can I find out exactly why my update failed?"
    a: "Yes. After you are back in Windows, check Settings, then Windows Update, then Update history for the error code, and open Event Viewer, then Windows Logs, then Setup for the detailed failure entries. The CBS.log file also records servicing failures verbosely for advanced diagnosis."
---

"We couldn't complete the updates, undoing changes" is Windows Update's autopsy report: the install was attempted, something failed validation, and the system is now reversing the attempt to protect itself. It is one of the most-searched Windows errors because it arrives with zero useful detail — no code on the screen, no explanation, just the rollback.

The message itself is not the problem to solve; the failed install behind it is. Every instance of this loop has a specific cause — a driver that would not cooperate, a corrupted package, a damaged servicing stack — and the rollback will keep happening on every boot until that cause is addressed. This guide gives you the complete troubleshooting arc: escape the immediate loop, diagnose the actual failure, fix it, and verify. The community-sourced variant — [Reddit's top solutions for the stuck rollback](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-reddit/) — is a good companion read.

The most valuable thing you can do while staring at this screen is reframe it: the message is not reporting a disaster, it is reporting a successful safety maneuver. The disaster version of this story is an update that installs badly and does not roll back — corrupted system, no boot, data at risk. You got the good version. The rollback is Windows choosing the safe failure mode, and safe failure modes are fixable. Everything after this paragraph is about making sure the next attempt does not need the safety net.

## Why this happens

- **Post-install validation failure:** Windows applies the update, checks the result, finds it inconsistent, and rolls back. The validation is strict by design.
- **Incompatible driver:** The update changes system components a current driver depends on; the driver fails to load, validation fails, rollback begins.
- **Corrupted update package:** Damaged download that passes initial checks but produces a broken install.
- **Servicing stack corruption:** The install engine itself is damaged, so even a perfect package installs incorrectly.
- **Disk space exhaustion mid-install:** The install runs out of staging room partway through and cannot complete.
- **Antivirus file interception:** Security software modifies files during the install window, so the final state fails validation.
- **Pending operations conflict:** Leftover pending operations from a previous attempt collide with the new install.
- **Hardware faults:** Failing RAM or storage corrupting data during the write-heavy install phase.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish, then pause updates

1. When the rollback screen appears, let it complete — interrupting it risks an unbootable system.
2. Once in Windows, immediately go to **Settings → Windows Update → Pause updates** (1–2 weeks).
3. This stops the retry loop and gives you a stable system to diagnose from. Dell owners should also review the [Dell-specific undoing-changes guide](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-dell-laptop/) for manufacturer driver steps that complement this general sequence.

### Fix 2: Extract the real error code

1. Go to **Settings → Windows Update → Update history** and find the failed update's error code (e.g., 0x80070002, 0x800f0922).
2. Open **Event Viewer → Windows Logs → Setup** and look for error entries timestamped at the failure — they often name the failing component.
3. For deep detail, check `C:\Windows\Logs\CBS\CBS.log` around the failure time.
4. The code and component name direct the rest of your repair. If the code is 0xC1900101, the fault is driver migration — prioritize Fix 5's driver updates. If it is 0x80070002 or 0x80070003, prioritize Fix 4's cache reset. Matching the fix to the code is what makes this fast.

### Fix 3: Break the loop from WinRE if you cannot reach Windows

1. If the loop prevents booting normally, force WinRE: interrupt boot three times at the Windows logo.
2. **Troubleshoot → Advanced options → Uninstall Updates → Uninstall latest quality update**.
3. Reboot — the failed package is gone and the loop breaks.
4. Alternatively use **System Restore** to a pre-update point.

### Fix 4: Clear the cache and reset components

1. Elevated Terminal: stop `wuauserv`, `bits`, `cryptsvc`.
2. Rename `SoftwareDistribution` and `catroot2` with `.old` suffixes.
3. Restart the services and reboot. This eliminates corrupted-package causes.

### Fix 5: Update drivers and repair the servicing stack

1. Update storage, chipset, and graphics drivers from the manufacturer's site — driver incompatibility is the top validation-failure cause.
2. Elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then reboot.
3. These two steps together address the most common root causes behind the message. Run them even when the failure looks driver-related — servicing damage and driver faults frequently coexist, and the repair is cheap insurance.

### Fix 6: Check disk space and hardware health

1. Free at least **15 GB** on C:.
2. `wmic diskdrive get status` should report "OK" for all drives.
3. Run Windows Memory Diagnostic (**Win + R** → `mdsched.exe`) if failures are erratic — bad RAM corrupts installs unpredictably.

### Fix 7: Retry surgically, then repair-install if needed

1. Unpause updates and install the update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) using the KB number.
2. If it fails again with the same code, run an in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) ISO, keeping files and apps.
3. Verify in **Update history** that the update shows installed — the loop is over.

## Closing

"We couldn't complete the updates" is a symptom; the failed validation behind it is the disease. Pause the loop, read the actual error code, and work the repair sequence — cache, drivers, servicing stack — and the message stops appearing. The in-place repair install is your definitive backstop. Treat every recurrence as new diagnostic information rather than the same old annoyance, and you will converge on the fix quickly. The screen loses its power to alarm you once you understand it is simply Windows doing its job. Keep this guide's five-move sequence handy — it works for every future instance of this error, not just this one.
