---
title: "How to Fix a Feature Update Stuck at 61% on an ASUS Laptop"
slug: how-to-fix-feature-update-stuck-at-61-percent-on-asus-laptop
date: 2026-09-04
categories: ["windows-update"]
tags: ["windows 11 feature update stuck", "update stuck at 61 percent", "asus windows update", "feature update troubleshooting"]
description: "ASUS laptop frozen at 61% during a Windows 11 feature update? Unstick the driver-migration phase with cache resets, BIOS refreshes, and MyASUS conflict checks."
thumbnail: "/images/thumbs/how-to-fix-feature-update-stuck-at-61-percent-on-asus-laptop.webp"
faqs:
  - q: "Does a 61% stall mean my SSD is failing?"
    a: "Not necessarily — software causes are far more common. But if the stall repeats after you've flushed the cache, refreshed the BIOS, and freed space, run chkdsk and check the SMART data. Repeated stalls at the exact same percentage with a healthy software stack are one of the early warning signs of a dying drive."
  - q: "Why does it always stop at exactly 61%?"
    a: "Because 61% marks the boundary between the file-copy phase and the driver migration phase. The installer reports progress in chunks, so every driver-related problem surfaces at the same number. It's not a coincidence or a progress-bar bug — it's where driver validation begins."
  - q: "Should I disconnect USB devices before retrying?"
    a: "Yes. USB docks, printers, external drives, and some headsets install drivers the migration phase must process, and flaky peripheral drivers are a well-known 61% trigger. Update with only the charger connected, then reattach devices one at a time afterward — reconnecting slowly reveals which device's driver was jamming the migration."
  - q: "Can a BIOS update really fix a stuck feature update?"
    a: "Yes, on ASUS hardware specifically. ASUS has shipped BIOS updates whose changelogs explicitly mention Windows 11 feature update compatibility. If your BIOS is more than a year old, updating it from ASUS support is one of the highest-value fixes for a 61% stall."
---

If your ASUS laptop has been displaying 61% for what feels like an eternity, you're looking at the classic feature-update stall point. Installers report progress in phases, and the handoff from file copy to driver migration lands right around 61%. Anything that forces the installer to re-examine drivers — a stale storage driver, a half-installed peripheral driver, an antivirus filter driver — can freeze the counter there. [a feature update stuck at 61 percent, step by step](/articles/how-to-fix-feature-update-stuck-at-61-percent-step-by-step/)

One ASUS-specific detail worth knowing: MyASUS and Windows Update don't always coordinate. I've seen ASUS laptops where MyASUS queued a BIOS or Intel chipset update at the exact moment Windows began a feature update, and the installer sat at 61% until the conflict was resolved. The fixes below are ordered to catch that kind of collision first, then clear the usual blockers.

## Why this happens

- **An outdated BIOS or chipset firmware.** ASUS has released BIOS updates specifically to unblock Windows 11 feature updates; old firmware can trip driver validation.
- **A MyASUS driver conflict.** ASUS's own updater pushing a driver mid-upgrade fights Windows over the same device stack and freezes progress.
- **Third-party antivirus filter drivers.** Kernel-level filters from security suites hook file operations the installer needs — a classic 61% trigger.
- **Failing storage sectors.** If the staging area on the SSD or HDD has bad sectors, the installer retries reads indefinitely at the same percentage.
- **A corrupted component store.** A damaged WinSxS store fails the integrity checks the installer runs right around this phase.
- **Peripheral driver chaos.** USB docks, printers, and external drives attached during the upgrade add drivers the migration phase must process.
- **A pending servicing stack update.** Installing the servicing stack update separately first sometimes clears a 61% stall on the feature update itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Flush the Windows Update cache

A corrupted SoftwareDistribution folder is one of the most common reasons the counter freezes at 61%. Clearing it forces Windows to download clean payload data.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, then net stop bits, then net stop cryptsvc (one per line).
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
4. Rename C:\Windows\System32\catroot2 to catroot2.old.
5. Restart the three services with net start wuauserv, net start bits, net start cryptsvc, then check for updates again.

### Fix 2: Refresh the BIOS and chipset from ASUS support

ASUS regularly publishes BIOS and chipset updates that fix feature-update compatibility. Outdated firmware is a leading cause of the 61% stall on ASUS hardware.

1. Visit the ASUS support site and enter your exact model or service tag.
2. Download the latest BIOS and Intel/AMD chipset driver listed for Windows 11.
3. Install the chipset driver first, then the BIOS update, with the charger connected.
4. Don't interrupt the BIOS flash for any reason.
5. After the BIOS update completes, retry the feature update from Settings.

### Fix 3: Quiet MyASUS and third-party driver updaters

MyASUS can queue driver installs that collide with the Windows feature update. Pausing it removes the tug-of-war over the device stack.

1. Open MyASUS and pause or disable automatic driver updates.
2. Also pause any third-party driver updater utilities.
3. In Settings, then Windows Update, then Advanced options, switch off "Receive updates for other Microsoft products" temporarily.
4. Retry the feature update with only Windows Update running.
5. Re-enable MyASUS updates after the feature update finishes.

### Fix 4: Strip out third-party antivirus temporarily

Antivirus filter drivers operate at kernel level and can block the file operations the installer performs during driver migration. Windows Defender is enough protection during the upgrade window.

1. Download your antivirus vendor's complete removal tool (not just the uninstaller).
2. Disconnect from the internet only if you're comfortable doing so, then run the removal tool.
3. Restart and retry the feature update.
4. Reinstall your antivirus after the update completes successfully.
5. If the update succeeds, the filter driver was the blocker — consider a lighter security setup.

### Fix 5: Repair the system image with SFC and DISM

If the component store is damaged, the integrity checks at 61% fail silently and the installer stalls. These two built-in tools repair it.

1. Open Command Prompt as administrator.
2. Run: sfc /scannow and wait for it to finish.
3. Then run: DISM /Online /Cleanup-Image /RestoreHealth.
4. Restart the laptop when both complete.
5. Retry the feature update; if it still stalls at 61%, the store wasn't the issue.

### Fix 6: Install the feature update through the Update Assistant

When Windows Update itself is the problem, Microsoft's Update Assistant takes a different code path that often sails past the stall. [feature updates taking too long in general](/articles/how-to-fix-windows-update-taking-too-long-in-windows-11-24h2/)

1. Download the Windows 11 Installation Assistant from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it as administrator and let it check compatibility.
3. Choose to keep personal files and apps when prompted.
4. Let it download and install — this can take 1 to 3 hours, which is normal.
5. If the Assistant also stalls, use the same page to create installation media for an in-place upgrade instead.

### Fix 7: Examine the drive for errors

Bad sectors in the staging area cause endless read retries at the same percentage. A quick health check rules the drive in or out.

1. Open Command Prompt as administrator and run: chkdsk C: /f /r.
2. Agree to run it at the next restart, then reboot and let it complete.
3. For a deeper read, check the drive's SMART data with ASUS's diagnostics or CrystalDiskInfo.
4. If the drive shows reallocated sectors or fails the test, replace it before retrying the update.
5. A healthy drive result means the stall is software, not hardware.

## Closing

Most ASUS laptops clear the 61% stall once the conflicting driver or outdated firmware is out of the way. Work the list top to bottom, verify disk activity before declaring each attempt stuck, and use the Update Assistant path when Windows Update itself seems to be the problem. For related stall patterns, our guide to [the Update Assistant hanging at 99 percent](/articles/how-to-fix-update-assistant-stuck-at-99-percent-on-dell-laptop/) covers the next most common scenarios.
