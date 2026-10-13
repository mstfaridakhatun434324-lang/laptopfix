---
title: "Windows Update Stuck on the Restarting Screen in Windows 11 24H2? Fix It"
slug: how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2
date: 2026-10-01
categories: ["windows-update"]
tags: ["stuck on restarting", "windows 11 24h2", "update stuck", "restart loop", "windows update"]
description: "Your laptop has shown 'Restarting' for an hour after a Windows 11 24H2 update? Here's how to tell if it's working, when to intervene, and how to recover."
thumbnail: "/images/thumbs/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2.webp"
faqs:
  - q: "How long can the 'Restarting' screen legitimately take?"
    a: "After a major 24H2 update, the restarting phase can take 20 to 45 minutes on an SSD and over an hour on a hard drive, especially when driver migrations run. Give it at least 90 minutes before concluding it's stuck. A frozen spinner with no disk activity for a full hour is the real signal of a hang."
  - q: "Is it safe to force-shut-down during the 'Restarting' screen?"
    a: "It's a calculated risk. If the screen has been frozen with no disk activity for over an hour, a forced shutdown is usually safe — Windows resumes the update from a checkpoint on reboot. The danger is interrupting an update that's actually writing files, which is why you should verify inactivity first by listening for drive sounds."
  - q: "Why does my laptop get stuck on 'Restarting' after every update?"
    a: "Recurring hangs point to a driver that won't unload (often storage, display, or network drivers), Fast Startup holding a corrupt hibernation state, or a peripheral confusing the shutdown sequence. Updating drivers and disabling Fast Startup, covered below, break the cycle for most repeat cases."
  - q: "What if it boots to a black screen after I force a restart?"
    a: "A black screen after interrupting the restart usually means the update is still finalizing — wait 15 minutes. If it persists, force a shutdown, boot into recovery with three interrupted boots, and use Startup Repair. Our [black screen after update guide](/articles/how-to-fix-black-screen-after-windows-update-in-windows-11-24h2/) walks through the full recovery."
---

The update downloaded. It installed. It asked for a restart, you clicked Restart now, and the screen went to that familiar blue "Restarting" with the spinning dots. Twenty minutes later, it's still there. An hour later, still there. The dots may even still be animating, which is the cruelest part — it looks alive, but nothing is happening. This is one of the most common Windows 11 24H2 complaints, and it's also one of the most misunderstood: a long "Restarting" screen is often normal, and the difference between "slow" and "stuck" matters because intervening at the wrong moment is what actually breaks things.

The restart phase is when Windows does its most delicate work: swapping system files that were in use, migrating drivers, and updating the boot configuration. On 24H2, with its larger cumulative payloads and driver migration steps, this phase legitimately takes longer than it did on 23H2. The fixes below start with telling slow from stuck, then move through safe recovery and the preventive steps that stop it happening every Patch Tuesday.

## Why this happens

- **Driver migration takes a long time**: 24H2 updates migrate storage and display drivers during restart; old or bulky driver packages stall this phase.
- **A driver refuses to unload**: A misbehaving driver (commonly network, audio, or USB) blocks the shutdown sequence indefinitely.
- **Fast Startup holds a corrupt state**: The hybrid shutdown file can conflict with the update's restart, freezing the handoff.
- **Connected peripherals stall shutdown**: USB drives, docks, and printers can hold the shutdown sequence waiting for a response that never comes.
- **Disk errors slow file operations**: Bad sectors encountered while swapping system files turn a 10-minute restart into an hour-long crawl.
- **Pending file operations queue up**: Multiple stacked updates create a long chain of file replacements processed during the single restart.
- **Antivirus hooks the shutdown**: Kernel-level security software inspecting every file operation during the update multiplies the time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it's slow or truly stuck

This diagnosis step prevents 90% of self-inflicted damage. Most "stuck" restarts are just slow ones, and force-restarting a working update is how boot loops are born.

1. Note the time and give it a full **90 minutes** on an SSD, **2 hours** on a hard drive, from the moment the Restarting screen appeared.
2. Listen closely: hard drive chatter or an SSD's faint activity, plus occasional fan speed changes, means work is happening.
3. Watch the spinner: smooth animation suggests the system is responsive; a completely frozen spinner for 30+ minutes suggests a hang.
4. Check the power LED and drive activity light if your laptop has one — blinking means progress.
5. Only proceed to Fix 2 if there's been zero sign of activity for a full hour.

### Fix 2: Force a restart and let Windows resume

If you've confirmed a genuine hang, a forced shutdown is the right move. Windows 11 checkpoints update progress, so it resumes rather than starting over.

1. Hold the **power button** for 10 seconds until the laptop powers off.
2. **Unplug all USB devices**, docks, and external drives — peripherals are a leading cause of restart hangs.
3. Wait 30 seconds, then power on.
4. Windows will typically show "Working on updates" and complete within 10–30 minutes.
5. If it boots normally to the desktop, open **Settings > Windows Update > Update history** to confirm the update installed.

### Fix 3: Disable Fast Startup to fix the restart handoff

Fast Startup's hybrid shutdown is a frequent culprit in restart hangs because the update's restart collides with the saved kernel state. Disabling it makes restarts clean.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left pane.
3. Click **Change settings that are currently unavailable**.
4. **Uncheck** "Turn on fast startup (recommended)".
5. Click **Save changes** and restart normally to test.
6. Leave it off if restart hangs were recurring — the boot-time cost is a few seconds on an SSD.

### Fix 4: Update drivers before the next update round

A driver that can't unload cleanly will hang every restart. Proactively updating the usual suspects — chipset, storage, graphics, network — prevents the next hang. Our [driver update guide](/articles/how-to-update-drivers-on-windows-11-laptop/) covers the full process.

1. Open **Device Manager** (Win + X > Device Manager).
2. Expand **IDE ATA/ATAPI controllers**, **Storage controllers**, **Display adapters**, and **Network adapters**.
3. Right-click each and choose **Update driver > Search automatically for drivers**.
4. Better: visit your laptop maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) and install the latest chipset and storage drivers for your exact model.
5. For NVIDIA or AMD graphics, use the GPU maker's official driver download page rather than Windows Update's versions.

### Fix 5: Run Startup Repair from the recovery environment

If the forced restart lands you in a boot loop or back on the stuck screen, the update may have damaged the boot chain. Startup Repair fixes it automatically.

1. Force-shutdown during boot **three times in a row** to trigger **Automatic Repair**.
2. On the recovery screen, go to **Troubleshoot > Advanced options > Startup Repair**.
3. Let it run — it checks boot files, the BCD, and disk errors.
4. If it reports it couldn't repair, choose **Advanced options > Command Prompt** and run `chkdsk C: /f /r` (confirm the drive letter first).
5. After repairs, choose **Continue** to boot into Windows.

### Fix 6: Check the disk for errors slowing everything down

Restart phases that take hours on a healthy SSD often trace back to a drive developing bad sectors. The update's file-swapping hammers the exact areas going bad.

1. Open **Command Prompt as administrator**.
2. Run `chkdsk C: /f` — agree to schedule it at next restart if prompted.
3. For a deeper scan, run `chkdsk C: /r` (takes longer, finds bad sectors).
4. Check the drive's SMART health: open **Command Prompt** and run `wmic diskdrive get status` — anything other than "OK" means replace the drive.
5. On a failing drive, back up immediately; no software tweak fixes dying storage.

### Fix 7: Uninstall the problematic update and pause

If the same update hangs the restart every time, stop installing it. A pattern of identical hangs means that specific package conflicts with your hardware.

1. Boot into **Safe Mode** (interrupt boot 3x > Troubleshoot > Advanced options > Startup Settings > Restart > press 4).
2. Go to **Settings > Windows Update > Update history > Uninstall updates** and remove the latest cumulative update.
3. Back on Windows Update, **pause updates** for 2 weeks.
4. Use the pause to update BIOS and drivers from your manufacturer's site.
5. Unpause and retry — Microsoft often ships a revised package within weeks for widespread hang reports. If rollbacks follow instead of hangs, our [Lenovo "undoing changes" walkthrough](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-lenovo-laptop/) covers that sibling symptom.

## Closing

The "Restarting" screen tests your patience by design — 24H2 does genuinely heavy work during that phase. The discipline is: verify it's actually stuck (no activity for an hour) before forcing anything, then fix the underlying cause rather than just surviving each hang. Updated drivers, Fast Startup disabled, and peripherals unplugged during update restarts eliminate the vast majority of repeat cases.
