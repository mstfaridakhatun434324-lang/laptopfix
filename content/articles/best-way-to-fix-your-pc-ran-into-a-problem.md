---
title: "Best Way to Fix 'Your PC Ran Into a Problem' Blue Screen"
slug: best-way-to-fix-your-pc-ran-into-a-problem
date: 2026-10-06
categories: ["windows-errors"]
tags: ["blue screen", "troubleshooting", "windows 11"]
description: "The best fix order for 'Your PC ran into a problem': capture the stop code, update drivers, remove bad updates, and repair Windows step by step."
thumbnail: "/images/thumbs/best-way-to-fix-your-pc-ran-into-a-problem.webp"
faqs:
  - q: "What's the first thing to do when I see this blue screen?"
    a: "Read and photograph the stop code at the bottom of the screen before it disappears. That code — something like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL — is the single most useful piece of information for fixing the problem. Everything else, from driver updates to memory tests, follows from what that code tells you."
  - q: "How can I see what caused past blue screens?"
    a: "Open Reliability Monitor by pressing Win + R and typing perfmon /rel — it shows a timeline with red X marks on crash days; clicking one reveals the stop code and faulting module. Event Viewer under Windows Logs > System also keeps BugCheck entries. These tools let you diagnose crashes that already happened, even if you didn't photograph the screen."
  - q: "Should I be worried if it only happened once?"
    a: "A single blue screen after a driver or Windows update is often a one-time glitch during the transition — make a note of the stop code and carry on. Worry when it repeats, even infrequently. Recurring crashes never fix themselves; they indicate a driver, update, or hardware problem that needs the steps below."
  - q: "Can this blue screen damage my files?"
    a: "The crash itself doesn't damage files — it's Windows stopping to prevent damage. Unsaved work is lost, but saved files are safe. The underlying cause (like a failing drive) could threaten files independently, which is why backups matter. Fix the crash with the steps below and keep a backup routine, and your data is fine."
---

"Your PC ran into a problem and needs to restart" is Windows' generic crash screen, and generic crashes need a prioritized approach — not random Googling. After years of fixing these, the order below is what actually works: capture the evidence, fix the most likely causes first, and only then dig deeper.

This is the "best way" because it front-loads the fixes with the highest success rate. Follow it top to bottom.

## Why this happens

- **Buggy driver.** Responsible for the majority of all blue screens, with graphics and network drivers leading.
- **Problematic Windows update.** An update conflicting with existing drivers or installing corruptly.
- **Failing memory.** Bad RAM crashing random processes at random times.
- **Corrupted system files.** Damaged Windows components failing under normal use.
- **Overheating.** Thermal problems crashing the system under load.
- **New hardware.** Recently added devices with immature drivers.
- **Disk corruption.** Failing storage damaging critical files.
- **Unstable power.** A dying charger or loose battery connection causing brownouts during peak draw.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as the crashes stop.

### Fix 1: Capture the stop code

Everything downstream depends on this one piece of information.

1. Disable the auto-restart so the screen stays visible: **Win + R**, type `sysdm.cpl`, go to **Advanced > Settings** under Startup and Recovery, and uncheck **Automatically restart**. (See our [auto-restart guide](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/) for the illustrated version.)
2. The next time it crashes, photograph the screen — capture the stop code and any named file.
3. Look up the stop code: it maps directly to a cause family (memory, driver, disk, licensing).
4. If crashes already happened, open **Reliability Monitor** (`perfmon /rel`) and click the red X marks to see past stop codes.
5. Write the code down somewhere — you'll reference it through every step below.

### Fix 2: Update the high-risk drivers

Graphics, network, chipset, storage — in that order of suspicion.

1. Press **Win + X** and open **Device Manager**.
2. Update the display adapter first: right-click, **Update driver > Search automatically for drivers** — or better, clean-install from the GPU maker's site.
3. Update network adapters, then storage controllers the same way.
4. Install the chipset package from your laptop maker's support page.
5. Restart and live with it for a few days; single data points don't prove anything with intermittent crashes.

### Fix 3: Remove the most recent Windows update

Timing is the best diagnostic tool you have. Crashes starting days after an update point straight at it.

1. Open **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the latest quality update and restart.
3. If that doesn't help, remove the latest driver update shown in the history too.
4. Pause updates for one to two weeks once stable.
5. Use the pause productively: check your laptop maker's site for revised drivers that address the conflict.

### Fix 4: Repair Windows system files and the disk

Eliminate corruption as a variable with the built-in repair tools.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Run `sfc /scannow` until it completes.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Run `chkdsk C: /f`, scheduling it with `Y` and restarting if asked.
5. After booting, run SFC once more — a clean second pass confirms the repairs held.

### Fix 5: Test memory and cooling

Hardware faults produce the same screens as software bugs, so verify them.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Review results in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
3. Run HWMonitor during heavy use and check for sustained temperatures above 90 degrees Celsius.
4. Clean vents with compressed air; confirm the laptop sits on a hard, flat surface.
5. Replace failing RAM — and retest with any XMP/DOCP profile disabled, since overclocked memory fails these tests deceptively.

### Fix 6: Clean boot to isolate software

Determine whether third-party software is involved at all.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then **Disable all**.
3. In **Task Manager > Startup apps**, disable all non-Microsoft entries.
4. Restart and use the laptop for several days.
5. If stable, re-enable in small groups until crashes return, then update or remove the culprit.

### Fix 7: Roll back with System Restore

If you have a restore point from before the crashes, this is the fastest complete fix.

1. Press **Win + S**, type `Create a restore point`, and open it.
2. Click **System Restore**, choose a pre-crash point, and review affected programs.
3. Complete the wizard without interrupting the restart.
4. Verify stability over several days of normal use.
5. Turn on System Protection if it was disabled, so the safety net exists next time.

### Fix 8: Reset Windows and reassess

The final software step before concluding it's hardware.

1. Back up your files to external storage or the cloud.
2. Go to **Settings > System > Recovery > Reset PC**, choose **Keep my files**, and use **Cloud download**.
3. After setup, install only maker-provided drivers and test before adding other software.
4. Reintroduce programs gradually — one every day or two.
5. If crashes persist on a clean system with current drivers and passing hardware tests, get the hardware professionally diagnosed.

## Closing

The "best way" to fix this blue screen isn't a single trick — it's the order: evidence first, then the highest-probability fixes (drivers, updates), then system repair, then hardware verification. Skipping straight to drastic measures wastes time and risks your data, so resist the urge. Most people never need to go past Fix 4, and those who do usually find the definitive answer in the memory test or the clean boot. For the stop-code-first approach to the same problem, see our companion guide on ['Your PC ran into a problem' on Windows 11](/articles/your-pc-ran-into-a-problem-bsod-windows-11/), and Microsoft's [official blue screen help](https://support.microsoft.com/en-us/windows) covers anything out of the ordinary.
