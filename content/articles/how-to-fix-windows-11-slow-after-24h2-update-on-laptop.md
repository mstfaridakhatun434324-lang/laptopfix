---
title: "Windows 11 Slow After the 24H2 Update? Speed It Back Up"
slug: how-to-fix-windows-11-slow-after-24h2-update-on-laptop
date: 2026-09-25
categories: ["performance"]
tags: ["windows 11 24h2", "slow after update", "feature update", "performance", "laptop"]
description: "Your laptop crawls after installing Windows 11 24H2? Post-update slowness has specific, fixable causes — background re-indexing, driver mismatches, and leftover update files."
thumbnail: "/images/thumbs/how-to-fix-windows-11-slow-after-24h2-update-on-laptop.webp"
faqs:
  - q: "Why is Windows 11 slower right after the 24H2 update?"
    a: "The first 24–72 hours after a feature update are genuinely busy: Windows re-indexes your files for search, Defender runs full baseline scans, the .NET framework re-optimizes assemblies, and update cleanup runs in the background. This activity settles on its own. If slowness persists beyond three or four days of normal use, it's no longer 'settling in' — it's a driver mismatch or leftover problem this guide fixes."
  - q: "Should I roll back the 24H2 update if my laptop is slow?"
    a: "Rollback is a last resort, not a first step. You have only 10 days after installing 24H2 to roll back via Settings > System > Recovery > Go back, and rolling back reintroduces the security issues the update fixed. In most cases the slowness comes from outdated drivers or background tasks that the fixes here resolve — try them first, and only consider rollback if the machine is unusable and nothing helps."
  - q: "Do I need to update drivers after the 24H2 update?"
    a: "Yes — this is the single most important post-24H2 step. Feature updates replace core OS components that drivers hook into, and drivers written for 23H2 can misbehave badly under 24H2. Prioritize graphics, chipset, Wi-Fi, and audio drivers from your laptop maker's support site or the chip vendor. Windows Update's driver offerings lag months behind, so check the manufacturer directly."
  - q: "Can I delete the Windows.old folder after 24H2?"
    a: "Yes, once you're confident you won't roll back. Windows.old holds your previous installation and can consume 15–30 GB. Use Disk Cleanup > Clean up system files > Previous Windows installation(s) rather than deleting the folder manually. Only do this after a week or two of stable use past the 10-day rollback window — before that, keep it as your escape hatch."
---

Feature updates are the biggest single change Windows ever undergoes short of a reinstall, and 24H2 is no exception: new kernel components, a reworked scheduler, and updated driver frameworks. It's completely normal for a laptop to feel sluggish for a day or two afterward while background tasks finish. But when the slowness stretches into week two, something specific is wrong — and it's almost always one of three things: drivers that 24H2 left behind, background processes stuck in a loop, or gigabytes of update debris clogging the drive.

The rule for post-update slowness: give it 72 hours of plugged-in use first. Still slow after that? Work this guide in order. For general slowness unrelated to the update, see [how to speed up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/); for game-specific issues after 24H2, read our [game stuttering guide](/articles/how-to-fix-windows-11-stuttering-in-games-step-by-step/).

## Why this happens

- **Post-update background tasks**: search re-indexing, Defender baseline scans, and .NET optimization saturate CPU and disk for days after the install.
- **Driver mismatches**: 23H2-era graphics, Wi-Fi, and chipset drivers misbehaving under 24H2's changed internals.
- **Windows.old and update debris**: 15–30 GB of leftover files eating disk space — critical on 256 GB drives.
- **Reset power and visual settings**: 24H2 sometimes flips power plans, transparency, and animation settings back to defaults.
- **Re-enabled startup apps and services**: updates occasionally re-enable OEM utilities and services you'd previously disabled.
- **Corrupt update components**: a partially failed update leaves the servicing stack in a loop, retrying forever.
- **Old BIOS/UEFI firmware**: 24H2's power management expects firmware cooperation that very old BIOS versions don't provide.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let it finish, then confirm it's actually stuck

Don't "fix" normal settling behavior.

1. Keep the laptop plugged in and powered on (not sleeping) for a few evenings — background tasks only run when the machine is awake and idle.
2. Open **Task Manager > Processes** sorted by CPU and Disk: legitimate settling shows *Windows Search Indexer*, *Antimalware Service Executable*, and *.NET optimization* activity that tapers over days.
3. Check **Settings > Windows Update** — make sure 24H2 shows as fully installed with no "pending restart" or failed updates.
4. If the same processes are still pegged after 4+ days, it's stuck, not settling — continue below.
5. Note your baseline: is everything slow, or just specific things (games, boot, browsing)? Specific slowness narrows the suspect list fast.

### Fix 2: Update every major driver for 24H2

This fixes more post-24H2 slowness than everything else combined.

1. Start with graphics: Intel users run Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html); NVIDIA and AMD users should grab the latest driver from their vendor's official download page — vendor releases fix 24H2 issues months before Windows Update offers them.
2. Update the chipset driver from your laptop maker's support site (Dell, HP, Lenovo, ASUS) — search your exact model, not a generic download.
3. Update Wi-Fi and Bluetooth drivers the same way — 24H2 changed the networking stack, and old Wi-Fi drivers cause stuttering and freezes, not just slow internet.
4. Update audio drivers (Realtek/Conexant) — mismatched audio drivers are a sneaky cause of system-wide micro-stutters after feature updates.
5. Reboot after each major driver, not all at once — if one driver was the culprit, you'll know which.

### Fix 3: Clean up update debris and reclaim disk space

A full drive is a slow drive, and 24H2 leaves a big footprint.

1. Search Start for **Disk Cleanup**, run it, click **Clean up system files**, and check **Previous Windows installation(s)**, **Windows Update Cleanup**, **Delivery Optimization Files**, and **Temporary files**.
2. Only remove Previous Windows installations after you're past the 10-day rollback window and the system is stable — it's your escape hatch until then.
3. Check free space afterward: Windows needs 15–20% free on the system drive for paging, indexing, and updates to work smoothly.
4. Empty the **SoftwareDistribution\Download** folder indirectly via Disk Cleanup (never delete it manually while the Update service runs).
5. If the drive is still nearly full, move personal files to external storage — no tweak compensates for a 99%-full SSD.

### Fix 4: Re-check settings 24H2 may have reset

Feature updates love flipping your customizations back.

1. **Settings > System > Power & battery > Power mode**: confirm it's still on **Best performance** (or Balanced) — 24H2 sometimes resets this to a power-saver-leaning default.
2. **Settings > Personalization > Colors**: re-disable **Transparency effects** if you'd turned them off — they cost GPU cycles on integrated graphics.
3. **Settings > Accessibility > Visual effects**: turn off **Animation effects** for an instant snappiness gain on weaker hardware.
4. **Task Manager > Startup apps**: re-disable anything the update re-enabled — OEM updaters and trial software love to resurrect themselves.
5. **Settings > System > Notifications > Additional settings**: re-disable tips and suggestions if they came back (they often do).

### Fix 5: Repair the update components

For updates stuck in a retry loop, burning CPU forever.

1. Open an elevated terminal and run: `net stop wuauserv`, `net stop bits`, then rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`, then `net start wuauserv`, `net start bits`.
2. Go to **Settings > Windows Update** and check for updates — this forces a clean re-scan with fresh metadata.
3. Run the troubleshooter: **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**.
4. In an elevated terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` to repair any component-store damage the update left.
5. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for any known 24H2 issues matching your symptoms before going further.

### Fix 6: Update the BIOS and reset firmware settings

24H2's power management is pickier about firmware than 23H2 was.

1. Check your BIOS version: `msinfo32` > BIOS Version/Date.
2. Compare against your laptop maker's support site for your exact model — install any update mentioning Windows 11 24H2, stability, or power management.
3. Flash **on AC power, battery charged, with nothing else running** — interrupted BIOS updates brick machines.
4. After updating, enter BIOS setup and **load optimized defaults** — stale settings carried across updates cause subtle instability.
5. Back in Windows, verify **Sleep** and **Modern Standby** behave — test a sleep/wake cycle, since firmware issues often show up there first.

### Fix 7: The clean options — in-place upgrade, then reset

When targeted fixes fail, escalate in order of destructiveness.

1. First try an **in-place upgrade**: download the Windows 11 installer from the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and run setup, choosing **Keep personal files and apps** — this reinstalls Windows over itself, fixing deep corruption.
2. If that's not enough, **Settings > System > Recovery > Reset this PC** with **Keep my files** — a fresh Windows with your data intact.
3. Back up irreplaceable files before either step — "keep my files" is reliable but not infallible.
4. After a reset, install drivers from the maker *before* letting Windows Update have its way — this avoids the exact driver mismatch that started the problem.
5. Only consider **Go back** (rollback to 23H2) within the 10-day window if the machine is unusable — and understand you're trading performance for unpatched security issues.

## Closing

Post-24H2 slowness is a phase, not a fate: let the background work finish, update every driver like you mean it, clean up the debris, and re-apply the settings the update reset. In the overwhelming majority of cases the laptop comes out of it faster than it went in — 24H2's scheduler improvements are real, once the drivers catch up.
