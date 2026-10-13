---
title: "Windows Update Says 'Undoing Changes Made to Your Computer'? What to Do Next"
slug: what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer
date: 2026-10-02
categories: ["windows-update"]
tags: ["undoing changes", "update rollback", "windows update failed", "windows 11", "update recovery"]
description: "Seeing 'Undoing changes made to your computer' after a failed update? Here's what it means, how long to wait, and the exact steps to recover safely."
thumbnail: "/images/thumbs/what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer.webp"
faqs:
  - q: "What does 'Undoing changes made to your computer' actually mean?"
    a: "It means a Windows update failed during installation and Windows is automatically rolling back to the previous working state. It's restoring the old versions of system files, drivers, and registry settings from backups it made before the update started. The message is Windows telling you the safety net caught a failure."
  - q: "How long should I wait on the 'Undoing changes' screen?"
    a: "Wait at least two hours on an SSD-equipped laptop and three hours on one with a hard drive. Rollbacks restore thousands of files and can look frozen while working hard. Only intervene if the spinner is completely frozen and there's been no disk activity for a full hour."
  - q: "Will the failed update try to install again?"
    a: "Yes — Windows Update will offer it again, usually within a day. If the underlying cause isn't fixed, it will fail and roll back identically. Pause updates for a couple of weeks after a rollback, fix the root cause using the steps below, then let it retry."
  - q: "Can I find out why the update failed?"
    a: "Yes. After the rollback completes, go to Settings > Windows Update > Update history and look for the failed entry with its error code. The code (like 0x800F0922 or 0xC1900101) identifies the failure category and tells you which fix to apply first."
---

"Undoing changes made to your computer" is one of Windows' better messages, even if it doesn't feel like it when you're staring at it. It's telling you the truth: an update went wrong, and Windows caught it. Before the update started, Windows snapshotted the system files it was about to replace. When the installation failed its integrity checks, Windows began restoring those snapshots — undoing the changes — so you don't end up with a half-updated, unbootable mess. The rollback is the safety net doing its job.

That said, "the safety net is working" is cold comfort when the screen has been up for two hours. This guide covers the full playbook: how long to wait, how to tell a working rollback from a frozen one, how to find out why the update failed, and how to fix the root cause so the retry succeeds instead of rolling back again. If your rollback is specifically stuck rather than just slow, the brand-specific guides for [Lenovo](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-lenovo-laptop/), [Dell](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-dell-laptop/), [Acer](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-acer-laptop/), and [ASUS](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-asus-laptop/) laptops cover hardware-specific recovery tools.

## Why this happens

- **The update package failed integrity checks**: Windows verifies every file as it installs; a single corrupted or mismatched file triggers the full rollback.
- **A driver conflicted mid-install**: The new build tried to migrate a driver that refused to cooperate, failing the installation phase.
- **Insufficient disk space**: The update ran out of room while staging files, a failure Windows detects and reverses.
- **Third-party software blocked system changes**: Antivirus or "system protection" tools prevented the update from replacing protected files.
- **The component store was already damaged**: Pre-existing corruption meant the update couldn't build on the current system state.
- **Firmware incompatibility**: An outdated BIOS/UEFI clashed with what the new build expected from the hardware.
- **Power or interruption during install**: A dead battery or forced shutdown mid-installation guarantees a rollback on next boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish — with a firm deadline

The single biggest mistake is interrupting a working rollback. Give it a real chance before touching anything.

1. Make sure the laptop is **plugged into AC power** — a dead battery mid-rollback is the worst outcome.
2. Start a timer: **2 hours** for SSDs, **3 hours** for hard drives.
3. Look for signs of life: drive activity sounds, fan cycling, spinner animating.
4. Do not press anything, do not hold the power button, do not unplug.
5. If it completes, you'll land at the login screen — proceed to Fix 2 to find out why it failed.
6. If the deadline passes with zero activity, move to Fix 5 for the stuck-rollback procedure.

### Fix 2: Identify the failed update and its error code

Once you're back in Windows, the first job is intelligence-gathering. The error code turns a mystery into a diagnosis.

1. Go to **Settings > Windows Update > Update history**.
2. Find the failed update — it will show "Failed to install" with a date.
3. Click it or note the **error code** (e.g., 0x800F0922, 0xC1900101, 0x80070002).
4. Common meanings: 0x800F0922 often involves .NET or secure boot issues; 0xC1900101 is driver-related (see our [0xC1900101 guide](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/)); 0x80070002 points to corrupt download cache.
5. Write down the KB number too — you'll need it for manual download fallbacks.

### Fix 3: Free disk space and clear the update cache

Two of the most common rollback causes — low space and corrupt downloads — are fixed together in about five minutes.

1. Open **Settings > System > Storage** and check free space on C: — you want at least **20 GB** free for a feature update, 10 GB for cumulative.
2. Click **Temporary files**, check the big categories (especially Windows Update Cleanup), and remove them.
3. Open **Command Prompt as administrator** and run:
   - `net stop wuauserv`
   - `net stop bits`
4. Delete all files inside `C:\Windows\SoftwareDistribution\Download`.
5. Run `net start wuauserv` and `net start bits`.
6. Retry the update from **Settings > Windows Update**.

### Fix 4: Temporarily disable third-party antivirus and clean boot

Kernel-level security software is a classic rollback trigger because it guards the exact system files the update must replace. A clean boot isolates this cleanly.

1. Open **System Configuration** (Win + R, type `msconfig`).
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. On the **Startup** tab, click **Open Task Manager** and disable all startup items.
4. Restart — you're now in a clean boot state.
5. Temporarily disable your third-party antivirus (Windows Defender stays on and is update-friendly).
6. Run Windows Update and install the failed update.
7. After success, re-enable services and startup items via msconfig.

### Fix 5: Break a genuinely stuck rollback safely

If the rollback itself is frozen — spinner dead, no disk activity for over an hour past your deadline — it's safe to intervene. Windows journals rollback progress and resumes from checkpoints.

1. Hold the **power button** 10 seconds to force shutdown.
2. Unplug all USB devices and docks.
3. Power on and watch: most systems resume "Undoing changes" and finish within 30 minutes.
4. If it boots to the desktop, the rollback completed — continue with Fix 6.
5. If it loops back to the stuck screen, interrupt boot three times to reach **Automatic Repair**, then use **Troubleshoot > Advanced options > Startup Repair**.
6. Microsoft's [Windows Update support page](https://support.microsoft.com/en-us/windows) documents these recovery paths if you need official confirmation of the steps.

### Fix 6: Repair the component store before retrying

A damaged component store dooms every retry to the same rollback. DISM rebuilds it.

1. Open **Command Prompt as administrator**.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` (15–30 minutes, needs internet).
3. Follow with `sfc /scannow`.
4. Restart the laptop.
5. Update your BIOS/UEFI from the manufacturer's support site (Dell, HP, or Lenovo) — since outdated firmware is a repeat rollback cause.
6. Only then retry the failed update.

### Fix 7: Pause updates strategically while you fix the root cause

Letting Windows retry a doomed update every day just wastes time and risks another multi-hour rollback. Pause deliberately.

1. In **Settings > Windows Update**, choose **Pause updates** and select 2–3 weeks.
2. Use the pause window to work through driver updates, BIOS updates, and disk checks.
3. If the failing update is a feature update you don't need urgently, you can also hide it: download Microsoft's "Show or hide updates" troubleshooter to block that specific KB.
4. Unpause after fixing the root cause and let the update install cleanly.
5. If rollbacks persist after all of this, an in-place upgrade (mount a Windows 11 ISO, run setup, keep files and apps) rebuilds the system cleanly — the same technique in our [clean-install update error guide](/articles/how-to-fix-windows-update-error-after-clean-install-in-windows-11-24h2/).

## Closing

"Undoing changes" is Windows cleaning up after a failed update — the right response is patience first, diagnosis second, and targeted repair third. Find the error code, fix what it points to (space, cache, drivers, firmware, component store), and the retry will succeed where the first attempt rolled back. The rollback screen is annoying, but it's proof the safety net works; the goal now is to make sure it never needs to catch you again.
