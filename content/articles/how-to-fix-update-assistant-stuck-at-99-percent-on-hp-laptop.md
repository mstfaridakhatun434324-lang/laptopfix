---
title: "How to Fix the Update Assistant Stuck at 99% on an HP Laptop"
slug: how-to-fix-update-assistant-stuck-at-99-percent-on-hp-laptop
date: 2026-09-06
categories: ["windows-update"]
tags: ["update assistant stuck at 99", "hp windows 11 update", "windows 11 installation assistant stuck", "feature update stuck"]
description: "Windows 11 Update Assistant frozen at 99% on your HP laptop? Verify it is really stuck, clear the Assistant cache, free disk space, and finish the upgrade."
thumbnail: "/images/thumbs/how-to-fix-update-assistant-stuck-at-99-percent-on-hp-laptop.webp"
faqs:
  - q: "How long should I wait at 99% before giving up?"
    a: "If Task Manager shows disk activity, wait at least 60 minutes — verification of a multi-gigabyte image is slow on hard drives. If there is zero disk activity for over an hour and free space is not changing, it is genuinely hung and safe to close and restart the process."
  - q: "Will closing the Assistant at 99% damage Windows?"
    a: "No. The Assistant stages everything before the install phase, so closing it during download or verification leaves your running system untouched. The worst case is a wasted download and leftover staging files, which the cache-clearing step removes. Your files, apps, and the current Windows build are completely unaffected."
  - q: "Why does the Assistant get stuck but Windows Update works?"
    a: "They use different download and staging paths. The Assistant downloads a full image and verifies it as one unit, which exposes disk and verification issues that Windows Update's chunked delivery avoids. If the Assistant hangs, the Media Creation Tool or Windows Update itself may succeed."
  - q: "Should I delete the $Windows.~BT folder?"
    a: "Yes, when the Assistant is closed. It is just the staging folder — Windows recreates it on the next attempt. Deleting it clears the corrupted partial download that is likely causing the repeat 99% hang. Never delete it while an install is actively running."
---

The Windows 11 Update Assistant freezing at 99% on an hp laptop is a special kind of maddening — hours invested, one percent to go, and nothing happening. The Assistant works differently from Windows Update: it downloads the full feature update image and runs setup from it. The 99% point is where it finalizes the download, verifies integrity, and hands off to the installer — and each of those steps can hang silently. [the Update Assistant stalling on other brands](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-lenovo-laptop/)

hp-specific context: on hp laptops the most common 99% hang is the installer waiting on a driver or firmware handshake — often storage or BIOS related — while the Assistant shows no useful status. The good news is that a 99% hang has not touched your working system yet in most cases; the Assistant stages everything before committing. The fixes below unstick it in order of likelihood.

## Why this happens

- **Corrupted partial download.** A damaged chunk in the multi-GB image fails verification at 99% and the Assistant retries silently. Delete C:\$Windows.~BT with the Assistant closed to clear it.
- **Insufficient disk space for staging.** The final handoff needs several GB of working room beyond the download itself. The handoff stages several GB beyond the download itself.
- **Driver handoff conflict.** The installer phase hits a storage or chipset driver problem right at transition. Storage and chipset drivers are the usual handoff blockers.
- **HP Support Assistant concurrent update lock.** hp's updater holding the servicing stack while the Assistant needs it. End Hp updater processes in Task Manager before launching the Assistant.
- **Antivirus scanning the image.** Real-time scanning of the multi-gigabyte ESD slows verification to a crawl or blocks it. Exclude the staging folder or disable real-time scanning during the run.
- **Corrupted Assistant cache.** The Assistant's own download folder contains stale data from a previous attempt. A fresh binary from Microsoft rules out version bugs.
- **Failing drive sectors.** Read errors during the multi-GB verification read stall the process. chkdsk and SMART data reveal the marginal sectors.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it is actually stuck

Do not kill a working Assistant. The 99%-to-restart transition involves heavy disk work with no progress update. The Assistant downloads a full multi-gigabyte ESD image and verifies its hash at 99% — on a slow drive that verification alone can take 30-40 minutes with no progress movement.

1. Open Task Manager and check disk activity by SetupHost.exe or the Assistant process.
2. If the disk is busy, wait a full 60 minutes before acting.
3. Check free space on C: — if it is shrinking, the Assistant is still staging.
4. Only proceed if disk activity is zero for 60+ minutes.
5. Note how long it has been stuck; you will need this if you escalate.
6. Watch Task Manager for 15 minutes after relaunching to confirm genuine download progress this time.

### Fix 2: Free up disk space

The handoff needs working room. Tight drives stall exactly at 99%. Task Manager is the arbiter: sustained disk activity by SetupHost.exe means working, zero activity for an hour means hung.

1. Ensure at least 20 GB free on C: — 25 GB to be safe.
2. Run Disk Cleanup with system files; remove previous Windows installations.
3. Uninstall large unused apps.
4. Move personal files off the system drive temporarily.
5. Restart the Assistant after freeing space.
6. Confirm C:\$Windows.~BT is being recreated with fresh timestamps, proving the cache clear worked.

### Fix 3: Close HP Support Assistant and other updaters

Remove the concurrent-update deadlock possibility. The Assistant stages everything in C:\$Windows.~BT before the install phase, so closing it at 99% does not touch your running system.

1. Close HP Support Assistant completely, including its background processes in Task Manager.
2. Close any third-party driver updaters.
3. Pause Windows Update's own checks temporarily.
4. Relaunch the Update Assistant alone.
5. Let the Assistant have the servicing stack to itself.
6. Verify free space on C: stays above 20 GB throughout the Assistant's run.

### Fix 4: Temporarily disable antivirus

Real-time scanning of a 5+ GB image can stall verification indefinitely. On Hp laptops, close HP Support Assistant before launching the Assistant — concurrent updaters deadlocking over the servicing stack is a real 99% cause.

1. Disable real-time protection in your third-party antivirus.
2. Relaunch the Update Assistant.
3. If it sails past 99%, the scanner was the bottleneck.
4. Re-enable protection after the update completes.
5. Consider excluding the Assistant's download folder in the future.
6. Once past 99%, let the installer phase run uninterrupted — do not use the laptop heavily during it.

### Fix 5: Clear the Assistant's download cache

Stale or corrupted partial downloads poison every retry. [a feature update parked at 61 percent](/articles/how-to-fix-feature-update-stuck-at-61-percent-step-by-step/) An outdated Assistant binary can mishandle the current feature update; always download a fresh copy from Microsoft rather than reusing an old one.

1. Close the Update Assistant completely.
2. Delete the contents of C:\$Windows.~BT if it exists (this is the Assistant's staging folder).
3. Also clear C:\Windows\SoftwareDistribution\Download.
4. Download a fresh copy of the Update Assistant from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
5. Run the fresh Assistant as administrator.
6. After the upgrade completes, confirm the new build with winver.

### Fix 6: Run the Assistant as administrator

Permission issues at handoff are rare but real. The 99% point is the handoff from download to Windows Setup, which is why driver and firmware issues surface exactly there.

1. Right-click the Update Assistant and choose Run as administrator.
2. Confirm the UAC prompt.
3. Let it run without other heavy applications open.
4. If it still stalls at 99%, the issue is not permissions — continue.
5. Admin rights also help when the staging folder has odd ACLs.
6. Run Windows Update fully on the new build to pull day-one patches.

### Fix 7: Update the BIOS first

Firmware handoff problems clear with a current BIOS. Antivirus real-time scanning of a 5+ GB image slows verification dramatically; excluding the staging folder is a legitimate optimization.

1. Check your BIOS version with msinfo32.
2. Download the latest BIOS for your exact hp model from [HP's support site](https://support.hp.com/us-en).
3. Install with the charger connected; do not interrupt.
4. After the BIOS update, retry the Assistant.
5. This resolves the 99% hangs that are really installer-handoff failures.
6. Re-enable your antivirus and HP Support Assistant automation after the upgrade.

## Closing

A 99% hang in the Update Assistant is a staging problem, not a system problem — your running Windows is untouched, and the fix is about clearing the corrupted download and giving the handoff what it needs. The Media Creation Tool path exists precisely for when the Assistant will not cooperate. For other feature-update stall points, [Windows Update taking too long overall](/articles/how-to-fix-windows-update-taking-too-long-after-windows-11-update/) covers them.
