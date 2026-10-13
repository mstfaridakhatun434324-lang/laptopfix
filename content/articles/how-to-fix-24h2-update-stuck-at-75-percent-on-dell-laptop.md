---
title: "Fix 24H2 Update Stuck at 75% on a Dell Laptop"
slug: how-to-fix-24h2-update-stuck-at-75-percent-on-dell-laptop
date: 2026-09-15
categories: ["windows-update"]
tags: ["windows 11 24h2", "update stuck", "dell laptop", "windows update"]
description: "Windows 11 24H2 stuck at 75% on your Dell laptop? That percentage is where driver migration happens. Here are 7 proven fixes to unstick it safely."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-on-dell-laptop.webp"
faqs:
  - q: "Is it safe to restart my Dell laptop when the 24H2 update is stuck at 75%?"
    a: "It depends on how long it has been still. If the percentage has not moved for over an hour and the drive light is dark, a single restart is usually safe because Windows rolls back automatically. Do not force power off repeatedly, since interrupted writes during the driver phase are what corrupt the update and cause boot loops."
  - q: "How long should I wait before I call 75% a real stall?"
    a: "Wait at least 90 minutes to two hours. The 75% mark is where Windows migrates drivers and rewrites the boot configuration, which looks frozen on the screen even while the disk is busy. Check the storage activity light or listen for disk activity first; a stall is only real when there is no disk activity for over an hour."
  - q: "Why do Dell laptops stall at 75% more than other brands?"
    a: "Dell machines carry a heavier preinstalled driver stack — SupportAssist hooks, Dell Update services, audio and thermal drivers — and the 24H2 installer migrates every one of them at around the 75% mark. One incompatible or corrupted Dell driver can park the whole installer, so cleaning up drivers before the upgrade prevents most Dell stalls."
  - q: "Will these fixes work if the update already rolled back once?"
    a: "Yes. A rollback actually protects your data, and it gives you a clean starting point. Run the driver cleanup, free up disk space, and reset the update cache, then try the install again. Repeated rollbacks at the same percentage usually point to a single failing driver, which a clean installation of the latest Dell drivers resolves."
---

A Windows 11 24H2 feature update freezing at exactly 75 percent is a pattern Dell laptop owners know well. The progress bar climbs steadily, then parks at three-quarters and refuses to move — no error message, no blue screen, just a number that sits there mocking you. I have seen this stall last overnight on XPS, Inspiron, and Latitude machines alike, and the cause is almost always the same: 75% is where the installer migrates drivers and rewrites the boot environment, and something in that phase is refusing to complete.

The important thing to understand is that 75% is not a random number. Feature update progress maps to distinct phases — file copy, driver migration, feature installation, and first-boot configuration — and the driver migration phase clusters right around the three-quarter mark. Dell laptops ship with a deep stack of manufacturer drivers (thermal controls, audio, SupportAssist services, BIOS-level hooks), and the 24H2 installer must validate and migrate every one of them. If a single driver is corrupted, incompatible, or actively blocking the migration, the installer waits. And waits.

## Why this happens

- **A corrupted Dell driver blocks migration.** Storage controller, chipset, or audio drivers with damaged files cannot be migrated, and the installer halts rather than skip them.
- **Insufficient free disk space.** Feature updates need roughly 20 GB of free space to stage files. Below that, the driver phase starves and stalls at 75%.
- **Antivirus or encryption software interferes.** Third-party AV and full-disk encryption can block the installer from rewriting drivers or the boot configuration.
- **A damaged SoftwareDistribution cache.** Corrupted partial downloads from a previous attempt make the installer retry the same files forever.
- **Conflicting USB peripherals.** External drives, docks, and even some webcams have caused 24H2 installs to hang during hardware redetection.
- **BIOS/firmware out of date.** Older Dell BIOS versions can conflict with 24H2's changed driver signing and power-management behavior.
- **Corrupted system files.** Damage to the component store (WinSxS) from an earlier interrupted update means the installer cannot assemble the new OS image.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is really stuck before touching anything

First, make sure you are not interrupting a healthy install. Feature updates can sit at one percentage for over an hour while the disk works hard in the background.

1. Wait at least 90 minutes at 75% before concluding it is stuck.
2. Check for disk activity: the storage LED should blink, or hold your ear near the machine for faint drive chatter. Activity means it is still working — leave it alone.
3. If there is no disk activity for a full hour, press **Ctrl + Alt + Delete** once and see if the screen responds. A frozen screen plus a dead drive light means a genuine stall — move to Fix 2.
4. Unplug all USB devices except the charger and keyboard/mouse receiver, then give it another 30 minutes — a peripheral redetection hang sometimes resolves itself once the device is gone.

### Fix 2: Roll back safely and prepare the machine

If the screen is frozen and the drive is quiet, a controlled restart lets Windows roll back to Windows 11's previous state. A rollback keeps your files and apps intact.

1. Hold the power button for 10 seconds until the Dell shuts off, wait 30 seconds, then power it back on.
2. Windows should detect the failed update and begin "Undoing changes made to your computer" — this can take 30 to 60 minutes. Do not interrupt it. If the rollback itself hangs, our guide to the [undoing changes loop](/articles/best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer/) covers the recovery steps.
3. Once you are back on the desktop, open **Settings > System > Storage** and confirm at least 20 GB free on C:. If not, run Disk Cleanup (including system files) before doing anything else.
4. Restart once more and verify the machine boots normally — a stable rollback is the foundation every later fix builds on.

### Fix 3: Update Dell drivers from the official source

Stale or corrupted Dell drivers are the single most common cause of the 75% stall, so bring them current before retrying.

1. Go to [Dell's official support page](https://www.dell.com/support), enter your service tag (on the sticker under the laptop), and open the Drivers section.
2. Download and install the latest **chipset**, **storage (Intel RST / NVMe)**, **audio**, and **BIOS** packages — install BIOS last, and keep the charger plugged in during it.
3. If Dell's site lists an "Urgent" driver update for Windows 11 24H2 compatibility, install it first.
4. Restart the laptop, then open Device Manager and confirm no device shows a yellow warning icon. For a fuller walkthrough of keeping drivers current, see our guide to [updating drivers on Windows 11](/articles/best-way-to-update-drivers-on-windows-11/).

### Fix 4: Clear the Windows Update cache

If a previous attempt left damaged partial downloads, the installer can get stuck re-reading them. Clearing the cache forces a clean download.

1. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
2. Run these commands to stop the update services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`. Then go to **Settings > Windows Update** and check for updates — the download starts fresh.

### Fix 5: Temporarily remove third-party security software

Antivirus and disk-encryption tools are notorious for blocking driver migration at 75%.

1. If you run a third-party antivirus (Norton, McAfee, Avast, etc.), open it and choose the temporary disable option — 24H2's migration phase is when it matters.
2. If you use a third-party encryption product on the system drive, decrypt the drive or suspend protection before upgrading; Windows' own BitLocker can usually stay on.
3. Retry the 24H2 update from **Settings > Windows Update** with the security software still paused.
4. After the update completes, re-enable your antivirus and encryption immediately. Do not browse unprotected any longer than the install takes.

### Fix 6: Repair the component store with DISM and SFC

A damaged WinSxS store means the installer cannot assemble the new OS image — exactly the kind of silent failure that parks at 75%.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and let it finish (15 to 30 minutes; it pulls clean files from Windows Update).
2. When DISM completes, run `sfc /scannow` and wait for the verification to reach 100%.
3. If SFC reports it found and fixed corruption, restart the laptop before retrying the update.
4. If DISM fails with a source error, follow our deeper guide on fixing [running DISM RestoreHealth](/articles/how-to-run-dism-restore-health-on-windows-11/), which covers pointing DISM at a Windows ISO for repair files.

### Fix 7: Install 24H2 with the Update Assistant instead

If Windows Update itself keeps stalling, Microsoft's Update Assistant takes a different code path and often sails past the percentage where Settings-based updates hang.

1. Download the Windows 11 Installation Assistant from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Disconnect all USB peripherals, keep the charger plugged in, and run the assistant as administrator.
3. Let it run to completion — it typically takes 60 to 120 minutes, with several automatic restarts. Do not open other apps during the process.
4. After 24H2 installs, check **Settings > Windows Update** for the follow-up cumulative updates that the feature release needs.

## Closing

A 24H2 install parked at 75% on a Dell laptop is almost always a driver-migration problem, not a dying machine — and driver-migration problems are fixable with preparation, not panic. Updating Dell's drivers, clearing the cache, and repairing the component store resolve the overwhelming majority of stalls. If the update later succeeds but your screen goes dark afterward, see our guide to the [black screen after Windows update](/articles/black-screen-after-windows-update-troubleshooting/); and once everything is running, consider setting a [battery charge limit](/articles/how-to-limit-battery-charge-to-80/) since 24H2's background indexing can chew through battery on the first few days after a feature upgrade.
