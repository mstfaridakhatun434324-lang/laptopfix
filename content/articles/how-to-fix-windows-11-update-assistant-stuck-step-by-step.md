---
title: "Windows 11 Update Assistant Stuck: A Step-by-Step Fix"
slug: how-to-fix-windows-11-update-assistant-stuck-step-by-step
date: 2026-09-29
categories: ["windows-update"]
tags: ["update assistant", "installation assistant", "stuck install", "windows 11"]
description: "Update Assistant frozen mid-upgrade? This step-by-step walkthrough takes you from diagnosis to a completed install — safely, in order."
thumbnail: "/images/thumbs/how-to-fix-windows-11-update-assistant-stuck-step-by-step.webp"
faqs:
  - q: "What is the first thing I should do when the Update Assistant freezes?"
    a: "Nothing, for 90 minutes. Seriously — the assistant's install phase legitimately sits at one percentage for a long time while migrating drivers and files, and interrupting a healthy install causes the very corruption you are trying to avoid. Watch the disk activity light: blinking means working, dark for over an hour means stuck. Only after confirming a true stall should you begin the recovery steps."
  - q: "Can I safely restart my laptop if the assistant is stuck installing?"
    a: "One controlled restart is the accepted recovery when the assistant is genuinely frozen with no disk activity. Windows will usually roll back to your previous build or resume the install on reboot. What you must avoid is repeated force-restarts — a single restart is recovery, but power-cycling five times in a panic is how boot configurations get corrupted."
  - q: "Why does the assistant get stuck at 99%?"
    a: "The high-90s percentages are the final driver migration and first-boot configuration phase, where the installer validates every migrated driver and writes the new boot configuration. A single incompatible driver — often storage, display, or a manufacturer utility driver — can park the installer here indefinitely. Updating drivers before retrying, as covered in the steps below, clears the vast majority of 99% stalls."
  - q: "The assistant finished but Windows Update still shows the old version. What happened?"
    a: "The assistant likely rolled back silently. Check Settings, then System, then About to confirm your build number — if it shows the old build, the install failed and reverted. Look in Windows Update history for the failure record and its error code, then work through the preparation steps below before running the assistant again. A second attempt without fixing the blocker fails the same way."
---

When the Windows 11 Installation Assistant freezes, the screen gives you almost nothing to work with: a percentage that does not move, a status line that does not change, and no error to search for. This walkthrough is the complete step-by-step recovery — diagnose the stall, recover safely, prepare the machine properly, and run the upgrade to completion. Follow the steps in order; each one assumes the previous ones are done.

The assistant (downloaded from Microsoft as Windows11InstallationAssistant.exe) upgrades your PC to the latest Windows 11 feature build outside the normal Windows Update flow. It downloads a multi-gigabyte payload, verifies it, installs in phases with automatic restarts, and finishes with first-boot configuration. Stalls happen in any of those phases, and the recovery differs by phase — which is why step 1 is diagnosis, not action.

## Why this happens

- **Corrupted download payload.** A bad chunk in the multi-gigabyte download fails verification and the assistant loops retrying it.
- **Driver migration deadlock.** An incompatible storage, display, or manufacturer driver parks the installer during the high-percentage phase.
- **Insufficient disk space.** The assistant stages the full payload plus working files; cramped disks stall it silently.
- **Antivirus or security suite blocking.** Real-time protection intercepting the installer's file operations mid-phase.
- **Conflicting manufacturer utilities.** OEM updaters and control apps locking files the installer must replace.
- **Pending Windows Update operations.** A half-finished Settings-based update deadlocking the assistant's install phase.
- **Failing storage hardware.** Bad sectors or a dying drive that cannot sustain the heavy staging I/O.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stall — wait and watch the disk

Never interrupt the assistant on suspicion alone. Confirm a genuine stall first.

1. Note the exact percentage and status text, then wait 90 minutes without touching the machine.
2. Watch the storage activity LED (or listen for drive sounds). Sustained blinking means the assistant is working — keep waiting.
3. Try **Ctrl + Alt + Delete** once. If the system responds, Windows is alive underneath.
4. Only when the percentage is unchanged, the disk is dark, and the screen ignores input for a full hour do you have a true stall — proceed to Fix 2.

### Fix 2: Recover with one controlled restart

A single restart lets Windows roll back or resume. Do it once, deliberately.

1. If the assistant is still in the **download** phase, simply close it (or end its Task Manager process) — download-phase interruption is harmless.
2. If it is in the **install** phase and truly frozen, hold the power button 10 seconds to shut down, wait 30 seconds, and power on.
3. Windows will either resume the install, roll back with "Undoing changes made to your computer" (wait it out — it can take an hour), or boot normally to the old build. If the rollback itself hangs, see our guide to the [undoing changes loop](/articles/best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer/).
4. Once booted, verify your build at **Settings > System > About** so you know exactly where you stand.

### Fix 3: Clean up the failed attempt's leftovers

Partial payloads and staging folders from the failed run will poison the retry. Remove them.

1. Open File Explorer, enable **View > Show > Hidden items**, and delete the `$Windows.~BT` and `$Windows.~WS` folders on C:.
2. Run Disk Cleanup as administrator and check **Temporary Windows installation files** and **Windows Update Cleanup**.
3. In an administrator Command Prompt, reset the update cache too: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, then rename SoftwareDistribution and catroot2 with the `ren` commands, then restart the services.
4. Empty the Recycle Bin and confirm at least 20 GB free on C: at **Settings > System > Storage**.

### Fix 4: Update drivers and firmware before retrying

Most install-phase stalls are driver migration failures. Update the drivers so there is nothing to choke on.

1. Visit your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and install the latest **chipset**, **storage**, **graphics**, and **BIOS** packages for your model.
2. Install one at a time with restarts; do BIOS last with the charger connected.
3. Open Device Manager and confirm no yellow warning icons.
4. Our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) has the full safe order if you want the detailed version.

### Fix 5: Disable interfering software for the install window

Security suites and OEM utilities are the other major install-phase blockers. Quiet them temporarily.

1. Temporarily disable third-party antivirus real-time protection (and HP Wolf Security / Lenovo Vantage guards if present).
2. In `services.msc`, stop manufacturer updater services (Dell SupportAssist, HP Support Assistant, Lenovo System Update) and set them to Manual for now.
3. Disconnect all USB peripherals except the charger — docks and external drives cause redetection hangs.
4. Set sleep to **Never** temporarily at **Settings > System > Power & battery** so the machine cannot doze mid-install.

### Fix 6: Run the assistant again — properly this time

With the machine prepared, the retry has the best possible conditions.

1. Download a fresh copy of the Installation Assistant from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) — do not reuse the old executable.
2. Right-click it and choose **Run as administrator**.
3. Let it run start to finish without using the laptop for anything else: 60–120 minutes on an SSD, longer on older drives. Several automatic restarts are normal.
4. If it stalls at the same percentage again, the blocker survived preparation — note the percentage and skip to Fix 7 instead of retrying blindly.

### Fix 7: Use the ISO method when the assistant will not cooperate

The ISO upgrade performs the identical install through a more fault-tolerant path.

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Double-click the ISO to mount it, open it, and run `setup.exe` as administrator.
3. Choose **Keep personal files and apps** when prompted.
4. Let the install complete (30–90 minutes, several restarts), then check **Settings > Windows Update** for follow-up cumulative updates. Re-enable your antivirus and manufacturer utilities afterward.

## Closing

The step-by-step discipline is what makes this work: confirm the stall before interrupting, clean up the failed attempt, update drivers, quiet the interfering software, and only then retry. Most assistant stalls never survive proper preparation. If you prefer the phase-by-phase diagnosis for a specific brand, our HP-focused guide to the [Update Assistant stuck on HP](/articles/how-to-fix-windows-11-update-assistant-stuck-on-hp-laptop/) covers the manufacturer-specific angles; and once the new build is running, our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) keeps the next feature update from stalling the same way.
