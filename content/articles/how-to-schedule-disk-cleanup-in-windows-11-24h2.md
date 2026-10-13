---
title: "How to Schedule Disk Cleanup in Windows 11 24H2"
slug: how-to-schedule-disk-cleanup-in-windows-11-24h2
date: 2026-09-03
categories: ["performance"]
tags: ["disk cleanup", "storage", "windows 11 24h2", "automation"]
description: "Stop cleaning your disk by hand. Schedule Disk Cleanup in Windows 11 24H2 with Task Scheduler so junk files never pile up again."
thumbnail: "/images/thumbs/how-to-schedule-disk-cleanup-in-windows-11-24h2.webp"
faqs:
  - q: "Does Windows 11 24H2 still have Disk Cleanup?"
    a: "Yes, the classic cleanmgr.exe still ships with Windows 11 24H2, though Microsoft now steers users toward Storage Sense in Settings. Disk Cleanup remains fully functional and scriptable, which makes it ideal for scheduled unattended cleaning. You can launch it from Run with cleanmgr or find it under Windows Tools in the Start menu."
  - q: "Is it better to use Storage Sense or scheduled Disk Cleanup?"
    a: "Use both. Storage Sense handles day-to-day tidying — temp files, Recycle Bin, and Downloads — on its own schedule. A scheduled Disk Cleanup with the /sagerun switch adds deeper categories like Windows Update Cleanup and Delivery Optimization files that Storage Sense sometimes skips. Together they cover everything without overlap."
  - q: "Will scheduled Disk Cleanup delete anything important?"
    a: "Not if you configure it carefully. The preset you save with /sageset controls exactly which categories get cleaned, and the safe categories — temporary files, Recycle Bin, thumbnails, delivery optimization — contain nothing Windows needs. Avoid selecting 'Windows ESD installation files' unless you are certain you will not need to reset the PC."
  - q: "How often should Disk Cleanup run automatically?"
    a: "Monthly is the sweet spot for most laptops. Weekly runs are overkill and can slow the system while they execute; longer than monthly lets Windows Update leftovers and temp files accumulate into the multi-gigabyte range. Schedule it for a time the laptop is on but idle, like Sunday morning."
---

Disk Cleanup is one of those tools everyone knows about and nobody runs. The junk accumulates — Windows Update leftovers, delivery optimization caches, thumbnail databases, temporary setup files — until the C: drive is mysteriously full and the laptop starts crawling. The fix is not remembering to clean; it is making cleaning automatic.

Windows 11 24H2 gives you two automation paths: the modern Storage Sense and the classic Disk Cleanup on a Task Scheduler trigger. This guide sets up both, with Disk Cleanup running monthly through a saved preset so it cleans exactly the categories you choose, silently, in the background.

## Why this happens

- **Update leftovers accumulate by design:** Every cumulative update keeps the previous version's files for rollback, and Windows only offers to remove them through cleanup tools.
- **Temp folders grow without bound:** Applications write to Temp and never clean up after themselves; a year of installs can leave gigabytes behind.
- **Delivery Optimization caches peer data:** Windows stores downloaded update chunks to share with other PCs on your network, and the cache is only trimmed by cleanup.
- **Nobody runs manual cleanup:** The tool works fine, but it requires remembering, opening it, selecting categories, and waiting — so it never happens.
- **Storage Sense defaults are conservative:** Out of the box, Storage Sense skips some of the largest categories, like Windows Update Cleanup and old device driver packages.
- **The Recycle Bin has no auto-empty:** Deleted files sit in the Recycle Bin indefinitely on default settings, silently holding disk space.
- **Thumbnail and icon caches regenerate endlessly:** These caches corrupt or bloat over time, and only a cleanup pass rebuilds them at a sane size.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check how much junk you are actually carrying

1. Press **Win + R**, type `cleanmgr`, and press Enter. Select your C: drive.
2. Click **Clean up system files** and select C: again — this second scan reveals the big categories like Windows Update Cleanup.
3. Note the total reclaimable space. If it is under 1GB, your problem is elsewhere; if it is several gigabytes, automation will pay off immediately.
4. Cancel out of the dialog for now — do not clean yet. You will configure the automated preset first.

### Fix 2: Create a saved Disk Cleanup preset

1. Press **Win + R** and type `cleanmgr /sageset:1`, then press Enter. This opens Disk Cleanup in preset-configuration mode.
2. Check the safe, high-value categories: **Temporary files**, **Recycle Bin**, **Thumbnails**, **Delivery Optimization Files**, **Windows Update Cleanup**, **Temporary Internet Files**, and **DirectX Shader Cache**.
3. Leave **Windows ESD installation files** and **Downloads** unchecked — the first removes your reset image, the second is your own files.
4. Click **OK**. Windows saves this selection as preset number 1, ready for silent runs.
5. The Microsoft documentation hub at [Microsoft support](https://support.microsoft.com/en-us/windows) has background on each cleanup category if you want to fine-tune the selection.

### Fix 3: Schedule it with Task Scheduler

1. Search for **Task Scheduler** in the Start menu and open it.
2. In the right pane click **Create Basic Task**. Name it **Monthly Disk Cleanup** and add a short description.
3. Set the trigger to **Monthly**, pick a day (the 1st works well), and set the start time to something like **9:00 AM**.
4. For the action, choose **Start a program**, browse to `C:\Windows\System32\cleanmgr.exe`, and in **Add arguments** type `/sagerun:1`.
5. On the final screen, check **Open the Properties dialog**, then on the **General** tab select **Run whether user is logged on or not** and **Run with highest privileges** so it works even on the sign-in screen.

### Fix 4: Enable and configure Storage Sense as the daily layer

1. Go to **Settings → System → Storage** and turn on **Storage Sense**.
2. Click **Storage Sense** to open its settings. Set **Run Storage Sense** to **Every week**.
3. Under Temporary Files, set **Delete files in my recycle bin if they have been there for over** to **30 days**, and do the same for the Downloads folder only if you are comfortable with it.
4. Turn on **Delete previous versions of Windows** if the option appears after a feature update.
5. Storage Sense now handles the small stuff weekly while your scheduled Disk Cleanup handles the deep categories monthly. For a manual deep-clean walkthrough, see our guide to [cleaning temporary files in Windows 11 24H2](/articles/how-to-clean-temporary-files-in-windows-11-24h2/).

### Fix 5: Verify the scheduled task actually runs

1. Back in Task Scheduler, find **Monthly Disk Cleanup** in the Task Scheduler Library.
2. Right-click it → **Run** to execute it immediately as a test. Disk Cleanup should run silently — check that disk space increases afterward.
3. Check the **History** tab of the task after the next scheduled run to confirm it triggered.
4. If it never runs, revisit the task properties: confirm the trigger is enabled, the laptop is not asleep at the scheduled time, and **Wake the computer to run this task** is checked under the **Conditions** tab if needed.

### Fix 6: Keep the automation healthy over time

1. Once a quarter, run `cleanmgr /sageset:1` again and review the categories — new Windows versions occasionally add new cleanup categories worth including.
2. Watch for the **Windows.old** folder after feature updates; Storage Sense's "delete previous versions" setting handles it, but verify it actually disappears after ten days.
3. If disk space stays tight despite automation, the problem is data, not junk — move large media to external storage or cloud rather than cleaning harder.
4. Our companion article on [scheduling vs. manual cleanup trade-offs](/articles/how-to-fix-disk-active-time-100-percent-youtube/) explains when disk pressure is a cleanup problem versus a hardware problem.

## Closing

A scheduled Disk Cleanup plus Storage Sense is a set-and-forget system: monthly deep passes for update leftovers, weekly light passes for temp files, and no more mysterious disk-full warnings. Set it up once, verify it runs, and your C: drive takes care of itself.
