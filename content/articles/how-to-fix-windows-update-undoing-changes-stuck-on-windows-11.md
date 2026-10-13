---
title: "How to Fix Windows Update Stuck on 'Undoing Changes' in Windows 11"
slug: "how-to-fix-windows-update-undoing-changes-stuck-on-windows-11"
date: 2026-09-17
categories: ["windows-update"]
tags: ["undoing changes", "windows update stuck", "windows 11", "update rollback", "windows update"]
description: "Stuck on 'Undoing changes made to your computer' in Windows 11? Learn how long to wait, how to break the loop safely, and how to stop it happening again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-on-windows-11.webp"
faqs:
  - q: "How long should 'Undoing changes' take in Windows 11?"
    a: "On a healthy system with an SSD, the rollback usually completes within 15 to 45 minutes. On older laptops with mechanical hard drives, or when a large feature update is being rolled back, it can legitimately take 2 to 3 hours. If the spinner has been going for more than 4 hours with no disk activity — no drive light, no fan changes — the rollback is genuinely stuck and it is time to intervene with the steps below."
  - q: "Is it safe to force-shutdown during 'Undoing changes'?"
    a: "It is a last resort, not a first step. Interrupting a rollback can leave the system in a half-rolled-back state, but Windows is designed to resume or restart the rollback on next boot in most cases. If the screen has been frozen for hours with zero disk activity, a forced shutdown followed by booting into the recovery environment is the accepted procedure — far safer than leaving it looping for days."
  - q: "Why does Windows keep undoing the same update?"
    a: "Because the update keeps failing for the same unresolved reason — a conflicting driver, insufficient disk space, or a corrupted component store — and Windows Update keeps retrying it on schedule. Each attempt installs, fails, and rolls back. Breaking the cycle means fixing the underlying failure (usually with DISM/SFC and a manual install) or hiding the problematic update so it stops being offered."
  - q: "Will I lose my files if the update rollback gets stuck?"
    a: "Your personal files are safe. The rollback only reverses system changes made by the failed update; it does not touch Documents, photos, or other user data. The risk in a stuck rollback is to Windows itself — a corrupted system state requiring repair — not to your files. Still, this is a good reminder to keep backups current before any major update."
---
Few Windows screens inspire as much dread as 'Undoing changes made to your computer' with a spinner that never stops. It means an update failed and Windows is rolling it back — a process that should take under an hour but sometimes wedges itself into an endless loop on Windows 11, especially after big feature updates on laptops with slow disks.

The rollback is actually Windows protecting you: rather than boot into a half-updated system, it reverses the failed update to the last known-good state. The problem is purely that the reversal itself can stall — on a corrupted update cache, a damaged servicing stack, or a driver that refuses to roll back cleanly. The fixes below are ordered from 'wait it out correctly' to 'surgical repair,' so you intervene at the right level.

First, the patience test: if the spinner has been running less than two hours and your drive activity light is blinking, let it finish — interrupting a working rollback causes the very damage you are trying to avoid. If it is truly frozen, start at Fix 1. For the specific case where the update fails and rolls back every single cycle, our guide to ['we couldn't complete the updates' on Windows 11](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-windows-11/) covers the failure side of the loop.

## Why this happens

- **Corrupted update cache** — Damaged files in SoftwareDistribution confuse the rollback logic, which cannot cleanly reverse an install it cannot fully read.

- **Damaged servicing stack** — If the component store was already inconsistent before the update, the rollback has no clean baseline to return to and stalls mid-reversal.

- **Driver that will not roll back** — Some third-party drivers (graphics, storage) resist being reverted; the rollback waits on them indefinitely.

- **Insufficient disk space** — Rollbacks need scratch space to shuffle files. A nearly full drive can freeze the reversal partway through.

- **Interrupted original install** — A power loss or forced shutdown during the update leaves a half-installed state that is inherently harder to roll back than a clean failure.

- **Failing hard drive** — Bad sectors in the middle of system files turn a routine rollback into an unreadable-file nightmare, stalling the process.

- **Pending operations from earlier updates** — A backlog of unprocessed servicing operations compounds the current rollback, multiplying the work and the failure points.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait properly — then confirm it is truly stuck

Before touching anything, establish whether the rollback is working slowly or actually frozen. Most 'stuck' reports are just slow rollbacks on mechanical drives.

1. Note the time and watch for at least 2 hours (3 on an HDD) before concluding anything.
2. Check for signs of life: drive activity light blinking, fan speed changes, or the spinner animation still moving smoothly.
3. If the spinner is frozen solid and there has been zero drive activity for over an hour, proceed to Fix 2.
4. If it is still churning, leave it alone — patience is the fix.

### Fix 2: Force a shutdown and boot into the recovery environment

When the rollback is genuinely frozen, break the loop by powering off and entering WinRE, where you can repair without the stuck rollback in the way.

1. Hold the power button for 10 seconds until the laptop fully powers off.
2. Power on, and as soon as the manufacturer's logo appears, hold power again to force off — repeat twice to trigger Automatic Repair.
3. On the third boot, Windows should enter the recovery environment: choose **Troubleshoot > Advanced options**.
4. If Windows boots normally instead, the rollback may have resumed — give it another hour before repeating.

### Fix 3: Use Startup Repair from WinRE

Startup Repair can fix the boot and servicing state that the frozen rollback left behind, often enough to let Windows boot normally.

1. In **Troubleshoot > Advanced options**, select **Startup Repair**.
2. Choose your Windows installation and let the tool run — it takes 5-15 minutes.
3. If it reports it could not repair, do not worry; continue to Fix 4.
4. Restart and see whether Windows boots to the desktop or resumes the rollback cleanly.

### Fix 4: Uninstall the latest quality update from WinRE

Removing the update that triggered the whole mess eliminates the rollback's reason to exist. This is the highest-success intervention for the loop.

1. In **Troubleshoot > Advanced options**, choose **Uninstall Updates**.
2. Select **Uninstall latest quality update** first (feature updates only if the quality uninstall does not help).
3. Let the uninstall complete and restart.
4. Windows should now boot normally. Immediately pause updates for 7 days (**Settings > Windows Update > Pause updates**) to prevent instant recurrence — detailed rollback-loop guidance is in our [undoing-changes troubleshooting guide](/articles/windows-update-says-undoing-changes-made-to-your-computer-troubleshooting/).

### Fix 5: Run SFC and DISM from the recovery command prompt

If the system boots but updates still fail, repair the servicing stack from WinRE's command prompt, where the stuck update cannot interfere.

1. In **Troubleshoot > Advanced options**, open **Command Prompt**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter if WinRE mounted Windows elsewhere).
3. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Type `exit`, restart, and attempt the update again — or install it manually per Fix 6.

### Fix 6: Install the update manually to break the retry loop

Windows Update will keep offering the same failing update. Installing it as a standalone package — or deliberately skipping it — breaks the install-fail-rollback cycle.

1. Boot normally, open **Settings > Windows Update > Update history**, and note the KB number.
2. Download that KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install the .msu directly.
3. If the manual install also fails, hide the update with the 'Show or hide updates' troubleshooter (see the [Windows support hub](https://support.microsoft.com/en-us/windows)) and wait for the next cumulative release.
4. Unpause updates once the problematic KB is handled.

### Fix 7: Free disk space and check drive health

Rollbacks stall on full or failing drives. Eliminate both so the next attempt — and any future rollback — has room and reliable media.

1. Boot normally and ensure at least 20 GB free on C: using **Settings > System > Storage** cleanup tools.
2. Open an elevated Command Prompt and run `chkdsk C: /f` to fix filesystem errors.
3. Check drive health in **Settings > System > Storage > Advanced storage settings > Disks & volumes > Properties** for warnings.
4. If the drive reports bad health, back up immediately and replace it — no software fix survives a dying disk.

## Closing

A stuck 'Undoing changes' screen feels catastrophic but is almost always recoverable: confirm it is truly frozen, break into the recovery environment, uninstall the offending update, and repair the servicing stack. Then fix the underlying failure so the loop never restarts.
