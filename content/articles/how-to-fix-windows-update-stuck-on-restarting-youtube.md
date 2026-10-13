---
title: "Windows Update Stuck on Restarting? The Video-Tutorial Fix, Done Right"
slug: how-to-fix-windows-update-stuck-on-restarting-youtube
date: 2026-09-18
categories: ["windows-update"]
tags: ["stuck on restarting", "video tutorial", "force restart", "recovery", "windows 11"]
description: "The complete, safe fix for Windows Update stuck on the restarting screen — everything the video tutorials show, plus what they leave out."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-youtube.webp"
faqs:
  - q: "The video I watched says to just hold the power button. Is that safe?"
    a: "After waiting a full hour with no disk activity, yes — it is the standard recovery step and Windows is designed to roll back interrupted updates. What the videos often skip is the waiting period, which is what separates a safe forced shutdown from a risky one. Windows tracks servicing transactions precisely so an interrupted update can roll back, but only if the interruption happens after the stall is genuine."
  - q: "Why do some tutorials say to remove the battery?"
    a: "Removing the battery (or holding the power button 30 seconds with the charger unplugged) drains residual power and clears stuck hardware states that a normal forced shutdown can leave behind. It is a legitimate extra step for machines that will not POST after the forced shutdown."
  - q: "My video tutorial's commands did nothing. Why?"
    a: "Many tutorials show commands for a different failure — cache resets fix download problems, not restart freezes. A restarting-screen freeze is a shutdown-phase problem, so the fix sequence here targets drivers, servicing transactions, and boot state instead. Matching the repair to the failure phase — download, install, or restart — is what separates effective troubleshooting from ritual command-pasting."
  - q: "How do I know the fix actually worked and won't recur?"
    a: "The update completes and the machine restarts cleanly twice afterward with no update pending. For recurrence, the real test is the next Patch Tuesday — which is why this guide ends with the preventive steps the videos never mention. The preventive steps at the end of this guide — current drivers, free space, Fast Startup off — are what make the fix stick rather than just work once."
---

If you searched for this problem on YouTube, you have seen the pattern: a three-minute video, dramatic music, "hold the power button," and ten comments saying it worked next to ten saying it bricked their laptop. The power-button step is not wrong — but it is step three of a seven-step fix, and the videos skip the diagnosis, the waiting rule, the recovery path, and the root-cause repair. This article is the video-tutorial fix done right: everything the good videos show, sequenced properly, with everything they leave out filled in.

Follow it top to bottom. No skipping to the power button.

A note on how to use this guide: each fix is labeled with what the videos usually show versus what they skip. If you already tried the video version and it failed, you probably did the right step in the wrong sequence — start from Fix 1 anyway, because the sequence is the fix as much as any individual step.

## Why this happens

- **Driver hanging at shutdown:** A driver that will not unload blocks the restart phase indefinitely — the most common true cause.
- **Servicing transaction jam:** The update engine cannot commit its changes and retries silently instead of failing.
- **Corrupted update cache:** Damaged staged files make the installer loop through the restart phase.
- **Fast Startup state pollution:** Hybrid shutdown preserves the frozen driver state across "restarts."
- **Antivirus deadlock:** Kernel hooks from security software deadlock against the update installer during reboot.
- **Disk errors:** Bad sectors in the servicing area cause silent infinite retries.
- **Firmware stalls:** Outdated BIOS mishandling the hardware reset the OS requests.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The waiting rule the videos skip

1. Check for drive activity — blinking light, disk sounds, fan changes. Activity means work is happening.
2. If there is activity, wait: large updates on slow laptop drives legitimately take 45–60 minutes on this screen.
3. Only when there has been zero activity for a full hour is the stall confirmed.
4. This single step is what separates the success stories from the "it bricked my laptop" comments — patience first, power button second.

### Fix 2: The safe forced shutdown, done completely

1. Hold the power button for a full 10 seconds until the machine is fully off — screen black, fan stopped, lights out.
2. Unplug the charger. If the battery is removable, take it out; if not, hold the power button 30 seconds with the charger unplugged to drain residual power.
3. Wait 30 seconds, reconnect power, and press power once — a single clean press, not repeated mashing.
4. Let Windows do whatever it starts — resume, rollback, or boot normally — without interrupting it again.

### Fix 3: When it will not boot — the recovery path

1. Interrupt startup three times (force off during the Windows logo) to trigger the Recovery Environment.
2. Try **Troubleshoot > Advanced options > Startup Repair** first.
3. If that fails, **System Restore** to a point before the update.
4. Last resort: **Go back to the previous version** uninstalls the interrupted update. These are the options the videos gesture at but never explain — Microsoft documents them at [Windows support](https://support.microsoft.com/en-us/windows). If none of the recovery options appear, the recovery partition itself may be damaged — in that case boot from Windows installation media and use its repair options instead of the on-disk recovery.

### Fix 4: Find the driver that caused it

1. Once booted, open **Event Viewer > Windows Logs > System** and examine the minutes before the freeze.
2. Look for driver names in shutdown-sequence errors — graphics and storage drivers lead the statistics.
3. Update the suspect driver from the vendor, not from a random video description link.
4. If a [Windows Update driver offer](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) was the culprit, block that version after installing the vendor's.

### Fix 5: Clear the cache that fed the loop

1. Elevated Command Prompt: `net stop wuauserv`, `net stop bits`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
3. `net start wuauserv`, `net start bits`, then check for updates for a fresh payload.
4. The cache-reset commands are what most tutorials actually demonstrate — but they fix download problems, and they belong here only as cleanup after the real cause is addressed.

### Fix 6: Kill Fast Startup and check the disk

1. **Control Panel > Power Options > Choose what the power buttons do** — uncheck **Turn on fast startup**.
2. Run `powercfg /h off` then `powercfg /h on` to regenerate a clean hibernation file.
3. Run `chkdsk C: /f` scheduled at reboot to rule out servicing-area disk errors.
4. Test a plain restart with no update pending — it should complete in under two minutes. If restarts still hang, the problem is systemic, like the cases in our [restarting-screen guide](/articles/best-way-to-fix-windows-update-stuck-on-restarting-screen/).

### Fix 7: Update the BIOS and verify

1. Check the laptop maker's support site for a BIOS newer than yours — firmware-level restart hangs are fixed in BIOS updates.
2. Flash on AC power following the maker's instructions exactly.
3. After the flash, perform two normal restarts to confirm the shutdown path is clean.
4. Reinstall the update that originally froze, watching the restart phase — this is the verification the videos never show.

### Fix 8: The prevention checklist

1. Keep graphics and storage drivers current from vendors — the two driver families behind most restart freezes.
2. Maintain 20 GB free on C: so servicing never stalls for space.
3. Restart (not shut down) the laptop weekly so pending operations never accumulate.
4. Leave Fast Startup off if this machine has frozen before — the seconds it saves are not worth a repeat. And if a future update leaves a [black screen](/articles/best-way-to-fix-black-screen-after-windows-update/) instead of a freeze, that guide takes over.

## Closing

The video tutorials are not wrong about the power button — they are just incomplete. Wait an hour, shut down safely, recover through WinRE if needed, find the driver, clear the cache, fix the boot state, verify twice. That is the whole fix, in the order that makes each step safe. Next time the restarting screen freezes, you will not need a video at all.
