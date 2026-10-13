---
title: "How to Fix Windows Update Stuck on 'Undoing Changes' in Windows 10"
slug: "how-to-fix-windows-update-undoing-changes-stuck-on-windows-10"
date: 2026-09-18
categories: ["windows-update"]
tags: ["undoing changes", "windows update stuck", "windows 10", "update rollback", "windows update"]
description: "Windows 10 hanging on 'Undoing changes made to your computer'? This guide covers safe waiting times, recovery-environment repairs, and how to stop the rollback loop for good."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-on-windows-10.webp"
faqs:
  - q: "How long is too long for 'Undoing changes' on Windows 10?"
    a: "Give it at least 2 hours on an SSD and up to 4 hours on a mechanical hard drive before intervening — large rollbacks on slow disks are genuinely that slow. The line is crossed when the spinner animation itself freezes and there is no drive activity for over an hour. At that point the rollback is not slow, it is stuck, and the recovery-environment steps below are the correct response."
  - q: "Where is the recovery environment in Windows 10?"
    a: "Windows 10's recovery environment (WinRE) is reached the same way as Windows 11: interrupt the boot twice in a row (power off at the logo), and the third boot opens Automatic Repair. From there choose Troubleshoot and then Advanced options for Startup Repair, System Restore, Uninstall Updates, and Command Prompt. If WinRE never appears, create Windows 10 installation media on another PC and boot from it to reach the same tools."
  - q: "Why does my Windows 10 keep failing the same update?"
    a: "The usual suspects on Windows 10 are a corrupted SoftwareDistribution cache, an outdated servicing stack update (SSU) that must be installed before the cumulative update, third-party antivirus blocking the install, or a driver conflict. Because Windows 10 is in its final years, also check that you are on a supported build — updates for expired builds fail by design."
  - q: "Does System Restore help with a stuck update rollback?"
    a: "Sometimes. If you have a restore point from before the update attempt, System Restore in WinRE can return the system files and registry to that state, bypassing the stuck rollback entirely. It does not affect personal files. It is worth trying before heavier repairs, but it cannot fix a physically failing drive or a deeply corrupted component store — those need CHKDSK and DISM respectively."
---
The 'Undoing changes made to your computer' screen on Windows 10 means exactly what it says: an update failed, and Windows is reversing it. When the reversal works, you wait a while and get your desktop back. When it wedges — the spinner frozen, the drive silent, hours passing — you need the recovery environment and a methodical approach, not panic and random button-pressing.

Windows 10 handles rollbacks a little differently from Windows 11: the servicing stack is older, the troubleshooter lives in the classic Control Panel path as well as Settings, and many Windows 10 laptops still run on mechanical hard drives that make every rollback dramatically slower. Age matters too — a Windows 10 machine that has skipped updates for months faces a much bigger, more failure-prone rollback than a current one.

This guide mirrors the Windows 11 process but with Windows 10's specific menus and an extra emphasis on the servicing stack update, which is the single most common hidden cause of repeated update failures on Windows 10. If your machine runs Windows 11 instead, use our [Windows 11 undoing-changes guide](/articles/how-to-fix-windows-update-undoing-changes-stuck-on-windows-11/) — the recovery steps differ in the details.

## Why this happens

- **Corrupted SoftwareDistribution cache** — Damaged download fragments confuse the rollback engine, which stalls trying to reverse an install it cannot fully parse.

- **Missing servicing stack update (SSU)** — Windows 10 cumulative updates often require a matching SSU first. Without it, the install fails and the rollback inherits the confusion.

- **Third-party antivirus blocking the install** — Security suites that quarantine update payloads cause the install to fail, and their filter drivers can then interfere with the rollback too.

- **Nearly full system drive** — Rollbacks shuffle gigabytes of system files; on a drive with under 10 GB free, the reversal can stall for lack of working space.

- **Failing mechanical hard drive** — Many Windows 10 laptops still use HDDs. Bad sectors in system areas turn a slow rollback into a frozen one.

- **Driver refusing to roll back** — Storage and graphics drivers from third parties sometimes cannot be cleanly reverted, hanging the whole rollback on one component.

- **Interrupted original update** — A power cut or forced shutdown mid-install creates a half-applied state that is far harder to reverse than a clean failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Give it a proper waiting window first

Windows 10 rollbacks on HDDs are slow enough to look stuck when they are not. Establish the facts before intervening.

1. Note the start time and wait at least 2 hours (4 on a mechanical drive).
2. Watch for life signs: HDD activity light, fan noise changes, spinner animation movement.
3. If the spinner is frozen and the drive has been silent for over an hour, move to Fix 2.
4. If there is any activity at all, keep waiting — interrupting a working rollback is the main way these situations get worse.

### Fix 2: Force shutdown and enter the Windows 10 recovery environment

Two interrupted boots trigger Automatic Repair in Windows 10, giving you access to the repair tools without the frozen rollback in the way.

1. Hold the power button until the laptop is fully off.
2. Power on and force off at the Windows logo; repeat once more.
3. On the third boot, Automatic Repair should appear — choose **Advanced options > Troubleshoot**.
4. If it boots to Windows instead, the rollback may have resumed; give it another hour.

### Fix 3: Try System Restore to a pre-update point

Windows 10 usually creates a restore point before updates. Restoring it bypasses the stuck rollback in one move.

1. In **Troubleshoot > Advanced options**, select **System Restore**.
2. Choose the most recent restore point dated before the update attempt.
3. Let the restore complete and restart.
4. If no restore points exist or the restore fails, continue to Fix 4 — nothing is lost by trying.

### Fix 4: Uninstall the latest update from WinRE

Removing the update that started the rollback removes the rollback's entire reason for being — the single most effective intervention.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall latest quality update** first.
3. Restart when it completes and let Windows boot normally.
4. Once at the desktop, pause updates for 7 days (**Settings > Update & Security > Windows Update > Pause updates**) to stop the immediate retry. For persistent retry loops, the [step-by-step undoing-changes walkthrough](/articles/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-step-by-ste/) goes deeper.

### Fix 5: Install the latest servicing stack update manually

This is the Windows 10-specific fix that resolves a huge share of repeat failures: the SSU must be current before cumulative updates will install cleanly.

1. Find your Windows 10 build and the matching SSU KB on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Download and install the SSU .msu, then restart.
3. Now install the pending cumulative update — manually from the catalog if Windows Update still balks.
4. Future cumulative updates should now install without the fail-and-rollback cycle.

### Fix 6: Repair system files from the recovery command prompt

When the servicing stack itself is damaged, repair it offline from WinRE where nothing can interfere.

1. Open **Command Prompt** from **Troubleshoot > Advanced options**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (verify the drive letter with `diskpart > list volume` first).
3. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Exit, restart, and retry the update. Background on both tools is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Clean the update cache and check the drive

Finish by removing the corrupted cache that started the failure and verifying the disk that has to survive the next attempt.

1. Boot normally, open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`, then delete the contents of **C:\Windows\SoftwareDistribution\Download**.
3. Restart the services with `net start wuauserv` and `net start bits`.
4. Run `chkdsk C: /f`, reboot to let it scan, then check for updates with a clean cache on a verified disk.

## Closing

Windows 10's 'Undoing changes' freeze is fixable with the same discipline as on Windows 11 — verify it is truly stuck, repair from the recovery environment, and address the root cause, which on Windows 10 is very often a missing servicing stack update. Do that, and the loop ends.
