---
title: "Feature Experience Pack Failed to Install? How to Fix It Fast"
slug: how-do-i-fix-feature-experience-pack-failed-to-install
date: 2026-09-26
categories: ["windows-update"]
tags: ["feature experience pack", "install failed", "windows update", "windows 11", "fix"]
description: "The Feature Experience Pack fails on every update check? Diagnose the real blocker and get it installed with these 7 practical fixes."
thumbnail: "/images/thumbs/how-do-i-fix-feature-experience-pack-failed-to-install.webp"
faqs:
  - q: "Do I actually need the Feature Experience Pack?"
    a: "Strictly speaking, no — it delivers minor feature improvements, not security patches, so your laptop runs fine without it. But its repeated failure is a warning light for your update pipeline: the same corruption blocking this small package will eventually block critical security updates. Fix the cause now while the stakes are low."
  - q: "Why does the pack fail with error 0x800f081f?"
    a: "That code means the installer could not find required source files — usually because the component store is damaged or the downloaded package is corrupt. The DISM repair in this guide rebuilds the store, and the cache reset forces a fresh download. Together they resolve nearly all 0x800f081f failures on small packages."
  - q: "The pack fails even after a cache reset. What next?"
    a: "Move to the component store repair with DISM, then try the manual install from the Microsoft Update Catalog. If the standalone package also fails, the installation machinery itself is damaged and needs the DISM/SFC repair sequence. A bad pack release from Microsoft is the remaining possibility — check the catalog for a revised version."
  - q: "Can antivirus software block the Feature Experience Pack?"
    a: "Yes. Third-party antivirus products occasionally interfere with the pack's installer, especially its shell components. Temporarily disabling real-time protection during the install is a safe diagnostic — if the pack installs with protection off, add exclusions for the update working folders or consider whether Windows Security alone suffices."
---

Every update check ends the same way: the Windows Feature Experience Pack downloads, attempts to install, fails with a cryptic error, and waits to try again next time. It is a small package — minor features, not security fixes — so the temptation is to ignore it. Do not. A package this small failing repeatedly means something in your update pipeline is wrong, and whatever is wrong will eventually graduate to blocking the security updates that protect your machine. The pack is the canary; this guide clears the mine.

The failure causes are compact, matching the package: a corrupted download stuck in the cache, a damaged component store, a pending restart blocking installs, antivirus interference, or occasionally a genuinely bad release from Microsoft. Each has a direct fix, and because the package is tiny, you can iterate quickly — most people get through the whole sequence in under an hour. Start at the top and work down.

## Why this happens

- **Corrupted cached download.** The pack's files in the update cache are damaged and fail verification every retry.
- **Damaged component store.** The installer cannot stage the package against a broken store.
- **Pending restart blocking installs.** Another update awaiting reboot holds the installer hostage.
- **Third-party antivirus interference.** Security software blocking the pack's shell-component install.
- **Corrupted system files.** Broader damage affecting Windows Update's installer components.
- **Defective pack release.** A bad version from Microsoft, later revised or pulled.
- **Stuck update services.** The wuauserv/bits/cryptsvc trio in a wedged state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart properly and retry

Clear the most common blocker — a pending restart — before doing anything clever.

1. Save everything and choose **Restart** (not Shut down — with fast startup on, shutdown does not clear pending update states).
2. After reboot, open **Settings > Windows Update** and click **Check for updates**.
3. Watch the Feature Experience Pack attempt its install.
4. If it succeeds, you are done — the blocker was a pending operation. If it fails again with the same code, continue; the problem is in the package or the pipeline. Do not be discouraged by one failed retry: pending-state blocks are the most common cause precisely because they are invisible, and a proper restart eliminates them cleanly without any deeper repair.

### Fix 2: Run the Windows Update troubleshooter

The automated pass handles corrupted download states and wedged services.

1. Open **Settings > System > Troubleshoot > Other troubleshooters** and **Run** Windows Update.
2. Apply every fix it offers, then restart.
3. Check for updates again.
4. If the troubleshooter claims success but the pack still fails, the corruption is in the cached package itself — Fix 4's manual cache reset is the next step. When the troubleshooter itself will not cooperate, see our [troubleshooter repair guide](/articles/troubleshoot-windows-update-troubleshooter-not-working/).

### Fix 3: Restart the update services cleanly

Sometimes the services are simply wedged — a clean restart unsticks them.

1. Open Command Prompt as administrator.
2. Run:
   ```
   net stop wuauserv
   net stop bits
   net stop cryptsvc
   ```
3. Then:
   ```
   net start wuauserv
   net start bits
   net start cryptsvc
   ```
4. Check for updates. This is the lightest intervention and resolves service-state stalls — if the pack was failing because a service hung mid-operation, this clears it.

### Fix 4: Reset the update cache for a fresh download

A damaged cached copy fails identically forever. Force a clean download.

1. In an elevated prompt, stop the services as in Fix 3.
2. Rename the cache folders:
   ```
   ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
   ren C:\Windows\System32\catroot2 catroot2.old
   ```
3. Restart the services and check for updates — the pack downloads fresh and usually installs first try.
4. This is also the core repair in our [Windows 11 update database error guide](/articles/how-to-fix-windows-update-database-error-on-windows-11/) — the same cache mechanics cause both symptoms.

### Fix 5: Disable third-party antivirus during the install

Rule out security software interference with a quick controlled test.

1. Turn off **real-time protection** in your third-party antivirus (temporarily).
2. Run the update check and let the pack install.
3. Re-enable protection immediately.
4. If the pack installed with protection off, the antivirus was the blocker — add exclusions for `C:\Windows\SoftwareDistribution` and the servicing paths, or evaluate whether Windows Security meets your needs on its own.

### Fix 6: Install the pack manually from the catalog

Take Windows Update out of the equation with the standalone installer.

1. Note the pack's KB number from **Settings > Windows Update > Update history**.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), download the x64 package for your build, and run it as administrator.
3. Restart when prompted and verify in update history.
4. A successful manual install proves the package is healthy and the automated pipeline was at fault. Also check the catalog listing for a **revised version** — if Microsoft reissued the pack, the manual download gets you the fixed one directly. Keep the downloaded installer file for a couple of weeks; if the pack ever fails again, you can reinstall it instantly without another download.

### Fix 7: Repair the component store with DISM and SFC

If even the manual install fails, the installation machinery needs rebuilding.

1. In an elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` — 15–30 minutes, uninterrupted.
2. Run `sfc /scannow` to 100% completion.
3. Restart, then retry — automated first, manual catalog install as backup.
4. Once the pack installs, run a final update check to confirm the pipeline is healthy overall. For persistent infrastructure-level issues, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the deeper recovery options.

## Closing

The Feature Experience Pack fails for small, fixable reasons — a pending restart, a corrupted cache, antivirus interference, or a damaged component store — and each fix takes minutes because the package is tiny. Work the sequence, get the pack installed, and treat its failure as the early warning it is: a healthy pipeline now means your security updates will land without drama later.
