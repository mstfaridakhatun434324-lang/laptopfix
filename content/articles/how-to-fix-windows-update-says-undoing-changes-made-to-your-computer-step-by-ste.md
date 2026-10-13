---
title: "Undoing Changes Made to Your Computer: Step-by-Step Fix (All Versions)"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-step-by-ste
date: 2026-09-01
categories: ["windows-update"]
tags: ["undoing changes step by step", "windows update fix", "update rollback fix", "step by step", "windows 10 windows 11"]
description: "A universal step-by-step checklist for 'Undoing changes made to your computer' on Windows 10 and 11 — escape, diagnose, fix, verify."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-step-by-ste.webp"
faqs:
  - q: "How long does the full step-by-step fix take?"
    a: "Budget two to three hours wall-clock, most of it waiting: the rollback itself, DISM/SFC scans, and the update retry all take time. Active hands-on work is about 30 minutes spread across the steps. Do not start at midnight before a deadline — begin when you can let the laptop work undisturbed, plugged in."
  - q: "Do I need to be an administrator for these steps?"
    a: "Yes for most of them. Stopping services, clearing the update cache, running DISM/SFC, and installing updates all require elevation. Sign in with an administrator account before starting; a standard account will stall at the first elevated prompt. If this is a work laptop, you may need IT for the admin steps."
  - q: "What should I do if a step fails or shows an error?"
    a: "Write down the exact error and continue to the next step rather than stopping — later steps (especially DISM/SFC and the in-place upgrade) often repair whatever blocked the earlier one. The checklist is ordered so each step either fixes the problem or narrows it; a failed step is still diagnostic information, not a dead end."
  - q: "How do I know the fix actually worked?"
    a: "The proof is the previously failing update installing cleanly with no rollback, followed by one more successful Patch Tuesday. Do not declare victory after the troubleshooter alone — complete the verification step at the end. A fix is only a fix when the update that kept failing now completes."
---

When Windows gets stuck **undoing changes**, you do not need ten browser tabs of conflicting advice — you need one checklist, in order, that works on both **Windows 10 and Windows 11**. This is that checklist: escape the stuck screen, diagnose the cause, apply the fixes in sequence, and verify the update finally installs.

Each step tells you exactly what to do, what success looks like, and when to move on. Check steps off as you go; the order matters because early steps are safe and fast while later steps are thorough and slow. Most loops break by step 6.

Before starting: plug in, connect to stable internet, and sign in as an administrator. For version-specific deep dives, see the [Windows 11 complete guide](/articles/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-windows/) or the [24H2 guide](/articles/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-in-windows/).

## Why this happens

- **Corrupted update cache:** Damaged downloaded files failing verification during install.
- **Damaged servicing stack:** Broken component store failing every update the same way.
- **Driver migration failures:** A driver the new build cannot carry over, aborting the install.
- **Low disk space:** Insufficient room for the install plus its rollback safety net.
- **Stuck update services:** Windows Update or BITS wedged in a bad state.
- **Third-party interference:** Antivirus, encryption, or utilities blocking update operations.
- **Firmware or hardware gates:** Failed compatibility checks or a struggling drive underneath.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1: Get past the stuck screen

If the "Undoing changes" screen has been up less than two hours, wait — plugged in, untouched. Past three hours with no disk activity, force power off, wait 30 seconds, power on, and let Windows finish booting or resume the rollback. Success looks like: you reach the desktop. Once there, open Windows Update → Update history and write down the failed KB number and error code — you will need both.

1. Wait two hours on the rollback screen if it has been less than that.
2. Truly stuck: force off, wait 30 seconds, power on.
3. Reach the desktop; open Update history.
4. Write down the failed KB number and the full error code.

### Fix 2: Step 2: Run the update troubleshooter

Settings → System (Win11) or Update & Security (Win10) → Troubleshoot → Windows Update → Run. Apply every fix it offers and restart when asked. Success looks like: the troubleshooter reports problems fixed. Then check for updates once — if the update now installs, you are done; if it fails again with the same code, continue. This step resolves the simple stuck-service cases in minutes.

1. Run the Windows Update troubleshooter; apply all suggested fixes.
2. Restart if prompted.
3. Check for updates and retry once.
4. Same failure: continue — the simple cases are ruled out.

### Fix 3: Step 3: Clear the update cache completely

Open an admin prompt: `net stop wuauserv`, `net stop bits` (also cryptSvc and msiserver on Win10). Delete everything inside `C:\Windows\SoftwareDistribution\Download` — or rename the whole SoftwareDistribution folder to .old for the thorough version. Then `net start` the services again and check for updates. Success looks like: updates re-download from zero and the pending list rebuilds. Corrupted downloads are the most common single cause; this step ends them.

1. Stop the update services (wuauserv, BITS, plus cryptSvc/msiserver on Win10).
2. Delete the Download cache contents (or rename SoftwareDistribution to .old).
3. Restart the services.
4. Check for updates; retry the failed update once.

### Fix 4: Step 4: Free space and repair the servicing stack

Run Disk Cleanup as administrator → Clean up system files → check everything update-related; confirm 20 GB+ free on C:. Then admin prompt: `DISM /Online /Cleanup-Image /RestoreHealth`, wait for completion, then `sfc /scannow`. Success looks like: both tools report no corruption (or "repaired successfully"). Restart afterward. This step fixes the "fails identically every time" pattern at its root.

1. Free 20 GB+ with elevated Disk Cleanup.
2. Run DISM restore-health to completion.
3. Run `sfc /scannow`; restart.
4. Retry the update once; note any change in behavior.

### Fix 5: Step 5: Update drivers and remove interference

Update chipset, storage, display, network, and biometric drivers from your laptop maker support page. Temporarily disable third-party antivirus real-time protection and pause disk encryption. Disconnect external USB devices. Then retry the update once. Success looks like: the update progresses past its previous failure point. If it now succeeds, re-enable protection immediately and update the security product so the next cycle does not repeat this.

1. Update all maker-validated drivers.
2. Temporarily disable AV and pause encryption; unplug USB extras.
3. Retry the update exactly once.
4. Success: re-enable everything and update the security tools.

### Fix 6: Step 6: Install the update manually

Download the exact KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and run the .msu. Success looks like: the installer completes and prompts for restart, and the restart finishes without the "Undoing changes" screen. If the manual install fails with the same code, the problem is definitively system state — continue to step 7. If it succeeds, the automatic pipeline was at fault; future updates will tell you if that persists.

1. Find the KB number in Update history.
2. Download the .msu from the Update Catalog.
3. Install manually; restart when prompted.
4. Watch the restart: no rollback screen means progress.

### Fix 7: Step 7: Repair Windows in place, then verify

Back up personal files. Run the Windows installer for your version (Windows 11: [Microsoft software download](https://www.microsoft.com/en-us/software-download/windows11); Windows 10: the Media Creation Tool) → Upgrade → keep files and apps, plugged in. After it completes, immediately install the previously failing update. Success looks like: the update installs cleanly, and the next Patch Tuesday also installs without rollback. That two-update confirmation is your proof the loop is broken — checklist complete.

1. Back up files; run the in-place upgrade keeping files and apps.
2. Install the previously failing update immediately after.
3. Confirm it completes with no rollback.
4. Monitor the next Patch Tuesday as final verification.

## Closing

That is the whole checklist: escape the screen, troubleshoot, clear the cache, repair servicing, fix drivers and interference, install manually, repair in place, and verify with two successful updates. Followed in order, these steps break every "Undoing changes" loop that software can cause — and the verification step proves it before you close the tab.
