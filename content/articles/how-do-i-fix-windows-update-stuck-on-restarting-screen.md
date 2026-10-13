---
title: "Windows Update Stuck on the Restarting Screen? Get Your Laptop Booting Again"
slug: how-do-i-fix-windows-update-stuck-on-restarting-screen
date: 2026-10-12
categories: ["windows-update"]
tags: ["stuck on restarting", "windows 11 24h2", "boot loop", "force restart", "troubleshooting"]
description: "Fix Windows Update stuck on the restarting screen: safe hard-reset protocol, recovery options, and how to finish or roll back the interrupted update."
thumbnail: "/images/thumbs/how-do-i-fix-windows-update-stuck-on-restarting-screen.webp"
faqs:
  - q: "How long should I wait on the restarting screen before acting?"
    a: "Wait at least 30 to 45 minutes if the drive activity light is blinking or you hear disk activity. Laptop updates on slow drives can legitimately take that long. If the screen is frozen with no activity for a full hour, the update has genuinely stalled. Use a phone timer rather than guessing — perceived waiting time stretches dramatically when you are staring at spinning dots."
  - q: "Is it safe to force-shut-down during the restarting screen?"
    a: "It carries some risk, but after an hour of zero activity it is the standard recovery step. Windows is designed to roll back an interrupted update. The danger is highest during the actual file-replacement phase, which is why waiting first matters."
  - q: "Why does my laptop get stuck on restarting after every update?"
    a: "Recurring stalls point to a driver that hangs during shutdown, a corrupted update cache, or a disk with bad sectors in the servicing area. Fix the underlying cause after recovering, or every Patch Tuesday will repeat the ordeal. The Event Viewer system log usually names the hanging driver, turning a recurring mystery into a ten-minute targeted fix."
  - q: "What if the laptop won't boot at all after I force it off?"
    a: "Boot into the Windows Recovery Environment by interrupting startup three times, then use Startup Repair or System Restore. If those fail, the Go Back option can uninstall the interrupted update and return the previous working build. The Recovery Environment exists precisely for this situation, and the Go Back option can remove the interrupted update when nothing else works."
---

The spinning dots on "Restarting" are supposed to last a minute or two. When they last an hour — the fan humming, the screen unchanged, your stomach sinking — Windows Update has stalled during the reboot phase. This is one of the most stressful update failures because the machine looks dead and every instinct says to yank the power. Do not act on that instinct yet. There is a correct order here: verify the stall, reset safely, recover, then fix the root cause so it never repeats.

This guide gives you the technician's protocol for a stuck restarting screen on a Windows 11 laptop: when to wait, when to force the shutdown, how to recover if it will not boot, and the permanent fixes for repeat offenders.

## Why this happens

- **Driver hanging at shutdown:** A misbehaving storage, graphics, or network driver refuses to unload, and Windows waits on it indefinitely during the restart phase.
- **Corrupted update cache:** Damaged files in the SoftwareDistribution folder make the servicing engine loop instead of progressing through the install phases.
- **Disk errors in the servicing area:** Bad sectors where update files are staged cause the installer to retry silently forever.
- **Third-party antivirus hooks:** Deep system hooks from security software can deadlock the shutdown sequence when the kernel is being replaced.
- **Fast Startup conflicts:** The hybrid shutdown state can collide with the update's reboot requirements, leaving the machine in a half-restart limbo.
- **Low-level firmware stalls:** An outdated BIOS/UEFI or storage controller firmware can hang the actual hardware reset the OS requests.
- **Interrupted earlier update:** A previous update that never finished leaves the servicing stack in a half-applied state, and the next restart inherits the mess.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall before touching anything

1. Look for the drive activity light or listen for disk sounds. Blinking or churning means work is still happening — keep waiting.
2. Give it a full 30–45 minutes from the moment the screen froze. Slow laptop hard drives and large feature updates genuinely need this long.
3. Note the exact state: spinning dots frozen versus dots still animating tells a technician whether the kernel or the UI layer is stuck.
4. Only proceed to a forced shutdown after a full hour with zero signs of activity. Patience here prevents a recoverable stall from becoming a corrupted install.

### Fix 2: Perform a safe forced shutdown

1. Press and hold the power button for a full 10 seconds until the machine powers off completely — the screen goes black and the fan stops.
2. Unplug the charger and, on laptops with removable batteries, remove the battery for 30 seconds to drain residual power.
3. Wait another 30 seconds, reconnect power, and press the power button once.
4. In most cases Windows detects the interrupted update and either resumes it or automatically rolls it back — let it finish whatever it starts without interrupting again.

### Fix 3: Use the Recovery Environment if it will not boot

1. If the laptop loops or will not start, force it off, then power on and force it off again during the Windows logo — repeat three times to trigger the Recovery Environment.
2. Choose **Troubleshoot > Advanced options > Startup Repair** and let it run.
3. If Startup Repair fails, go back and try **System Restore** to a point before the update.
4. As a last resort in the same menu, **Go back to the previous version** uninstalls the interrupted update entirely. Microsoft documents these paths at [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 4: Update the driver that hangs shutdown

1. Once booted, open **Event Viewer > Windows Logs > System** and filter for errors around the time of the stuck restart — look for driver names in the shutdown sequence.
2. Graphics and storage controller drivers are the usual suspects; update them from the vendor ([NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or your laptop maker).
3. If a specific driver update from Windows Update is the culprit, our guide to [driver updates failing in Windows Update](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) shows how to block the bad version.
4. Restart normally (no update pending) to confirm shutdowns are clean before the next Patch Tuesday.

### Fix 5: Clear the corrupted update cache

1. Open an elevated Command Prompt and stop the update services: `net stop wuauserv` and `net stop bits`.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`.
3. Restart the services with `net start wuauserv` and `net start bits`, then check for updates — the cache rebuilds fresh.
4. A clean cache eliminates the damaged staged files that caused the stall loop.

### Fix 6: Check the disk for errors in the servicing area

1. In an elevated Command Prompt, run `chkdsk C: /f /r` and accept the prompt to run at next restart.
2. Restart and let the full check complete — on large drives this takes a while, but bad sectors in the update staging area are a classic repeat-stall cause.
3. If chkdsk finds and repairs bad sectors, also run `sfc /scannow` to verify system file integrity afterward.
4. Consider checking the drive's SMART health; a failing drive will keep producing update stalls until it is replaced.

### Fix 7: Disable Fast Startup and update the BIOS

1. Open **Control Panel > Power Options > Choose what the power buttons do** and uncheck **Turn on fast startup**.
2. Visit your laptop maker's support site and check for a BIOS/UEFI update newer than your installed version — firmware-level restart hangs are fixed this way.
3. Install the BIOS update on AC power with the battery charged, following the maker's instructions exactly.
4. Re-enable Fast Startup afterward only if you want it; many technicians leave it off on machines with a history of restart stalls. If the machine later shows a [black screen after an update](/articles/best-way-to-fix-black-screen-after-windows-update/), that guide picks up where this one leaves off.

## Closing

A stuck restarting screen feels like a dead laptop, but it is almost always recoverable: wait, force-shut-down once, recover through the Recovery Environment if needed, and then fix the driver, cache, or disk issue that caused it. Do the root-cause work this time and the next update's restart will be the boring sixty-second affair it was always supposed to be.
