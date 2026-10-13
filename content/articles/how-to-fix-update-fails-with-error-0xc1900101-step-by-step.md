---
title: "Error 0xC1900101: The Step-by-Step Fix That Actually Works"
slug: how-to-fix-update-fails-with-error-0xc1900101-step-by-step
date: 2026-09-29
categories: ["windows-update"]
tags: ["0xc1900101", "step by step", "driver conflict", "feature update"]
description: "0xC1900101 killing your Windows upgrade? Follow this strict step-by-step: read the phase code, fix the driver, simplify, and retry successfully."
thumbnail: "/images/thumbs/how-to-fix-update-fails-with-error-0xc1900101-step-by-step.webp"
faqs:
  - q: "What is the very first step for 0xC1900101?"
    a: "Read the full error code including the phase suffix — 0x20017, 0x30018, 0x4000D, or 0x40017. The suffix tells you which upgrade phase the driver failed in, which narrows the suspect list from 'every driver' to one category. Screenshot or write down the complete code before doing anything else — you will reference it throughout."
  - q: "Do I need to follow the steps in order?"
    a: "Yes — the order is the method. Each step eliminates a cause category, so skipping ahead means retrying the upgrade with the blocker still in place. The sequence is designed so that by the final retry, every known 0xC1900101 cause has been addressed."
  - q: "How many times should I retry the upgrade?"
    a: "Exactly once per completed step-group. Blind repeated retries without changes never fix 0xC1900101 — the same driver fails the same way every time. One informed retry after the driver work is worth ten blind ones. If a retry fails with a different phase suffix, treat it as a new problem and re-run the sequence for that phase."
  - q: "What if I complete all steps and it still fails?"
    a: "Then the setup logs name the specific driver — Fix 6 shows how to read them. A log-identified driver fix resolves the cases that survive the general playbook, because you are no longer guessing. At that point the logs are authoritative — generic fixes have done all they can, and specificity wins."
---

Error 0xC1900101 rewards method and punishes improvisation. The people who fix it fastest are not the ones who try the most things — they are the ones who work a strict sequence: identify the phase, address the driver class that phase implicates, simplify the system, and retry exactly once. Every shortcut — retrying without changes, updating random drivers, reinstalling Windows in frustration — wastes the afternoon the method would have saved.

This is that sequence, written as numbered steps with no branching and no guesswork. It assumes a failed feature update rolled back with 0xC1900101 in the history. Follow it top to bottom, do not skip, and the upgrade goes through.

Method matters more than effort with this error, and here is why. Every blind retry of the upgrade replays the identical driver failure, consuming an hour to teach you nothing. Every skipped step leaves a suspect unexamined, so the eventual retry fails for a reason you already could have fixed. The sequence in this guide is ordered by probability and dependency: the most likely causes first, the diagnostic steps positioned where their results change what you do next. Trust the order and the upgrade goes through.

## Why this happens

- **A driver incompatible with the target build.** The core mechanism: one driver cannot migrate, and Setup aborts rather than risk an unbootable system.
- **The wrong driver class for the failure phase.** Storage drivers kill Safe OS phase; display and peripheral drivers kill First and Second Boot.
- **Filter drivers from security software.** Antivirus and encryption drivers that hook the kernel resist migration.
- **Stale driver packages from old installs.** Orphaned driver versions confusing the migration's version resolution.
- **Firmware too old for the new build.** BIOS/UEFI lacking interfaces the migrated drivers require.
- **External hardware adding migration load.** Each attached device contributes drivers the upgrader must migrate.
- **Damaged servicing state from prior attempts.** Partial migrations poisoning subsequent retries.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Step 1: Record the full error code

Everything downstream depends on this.

1. Open **Settings** > **Windows Update** > **Update history**.
1. Write down the complete code, e.g. 0xC1900101 – 0x20017.
1. The suffix is the phase: 0x20017 Safe OS, 0x30018 First Boot, 0x4000D/0x40017 Second Boot.
1. Do not proceed until you have it — guessing the phase wastes every later step.

### Fix 2: Step 2: Update the phase-implicated drivers

Target the driver class, not random drivers.

1. For 0x20017: update chipset and storage drivers from your laptop maker's support site.
1. For 0x30018/0x4000D/0x40017: update graphics and network drivers.
1. Get graphics from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or the [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html).
1. Restart after each driver install — stacked installs without reboots cause their own failures.

### Fix 3: Step 3: Remove filter-driver software

Eliminate the kernel-hook suspects completely.

1. Uninstall third-party antivirus entirely (not just disable).
1. Uninstall VPN clients, disk encryption tools, and system optimizers.
1. Remove old hardware utilities with kernel components.
1. These are uninstalled, not disabled — filter drivers load at boot regardless of the app's running state.

### Fix 4: Step 4: Simplify hardware and clean-boot

Reduce the migration's workload to the minimum.

1. Unplug all external devices except power and essential input.
1. Run `msconfig`: selective startup, disable non-Microsoft services.
1. Disable all startup items in Task Manager.
1. Restart into this minimal state before the retry.

### Fix 5: Step 5: Repair and prepare the system

Cover the environmental prerequisites.

1. Free 30 GB on C:.
1. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`.
1. Clear the SoftwareDistribution cache.
1. Update the BIOS from the maker's site if a newer version exists — on AC power.
1. For the broader repeat-failure playbook beyond 0xC1900101, see [cumulative update fails every time on Windows 11](/articles/how-to-fix-cumulative-update-fails-every-time-on-windows-11/).

### Fix 6: Step 6: Read the logs if a retry fails

The diagnostic of last resort that almost always names the driver.

1. Retry the upgrade once after Steps 1–5.
1. If it fails, open `C:\$Windows.~BT\Sources\Panther\setupact.log`.
1. Search for failure entries near the rollback time, or run Microsoft's `setupdiag`.
1. Update, roll back, or uninstall the implicated driver, then retry — this targeted fix has the highest success rate in the sequence.

### Fix 7: Step 7: The ISO-path final retry

Different orchestration for upgrades that defeat Windows Update.

1. Download the Windows 11 ISO from Microsoft's official Windows 11 download site.
1. Mount the ISO, run setup.exe, choose keep files and apps.
1. Complete the upgrade on AC power with the simplified system from Step 4.
1. If even this fails, the logs from Step 6 hold the answer — do not retry blindly again. The [HP-focused 0xC1900101 guide](/articles/how-to-fix-update-fails-with-error-0xc1900101-on-hp-laptop/) covers brand-specific driver angles, and Microsoft's support pages document the phase codes.

### Fix 8: Verify driver versions after the successful upgrade

Confirm the fix stuck and document the working set.

1. After the upgrade completes, open Device Manager and spot-check the drivers you updated.
1. Confirm versions and dates match what you installed — not older inbox versions.
1. Reinstall your antivirus and utilities one at a time, testing stability between each.
1. Create a restore point named after the working configuration; future updates will thank you.

## Closing

0xC1900101 is a procedure problem as much as a driver problem: the fix works when the steps are worked in order and fails when they are cherry-picked. Record the phase, update the implicated drivers, strip the filter drivers, simplify, repair, and retry once. Follow the sequence and the upgrade that failed repeatedly installs cleanly — that is what the method is for. The method generalizes beyond this one error. Phase-aware diagnosis, most-likely-cause ordering, and one informed retry per change is how technicians approach every failed upgrade, from 0x800F codes to stalled percentages. Learn the sequence once and it pays off on every future feature update your machine attempts.
