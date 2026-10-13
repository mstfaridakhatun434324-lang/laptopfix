---
title: "How to Fix the Feature Experience Pack Failing to Install on an Asus Laptop"
slug: how-to-fix-feature-experience-pack-failed-to-install-on-asus-laptop
date: 2026-10-01
categories: ["windows-update"]
tags: ["feature experience pack", "windows update", "asus", "install failed", "windows 11"]
description: "Feature Experience Pack won't install on your Asus? Clear the cache, calm Armoury Crate conflicts, and install it manually."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-on-asus-laptop.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It is a small Microsoft package that updates Windows shell features — the snipping experience, input panels, clipboard history, and related components — independently of full Windows builds. It arrives through Windows Update. When it fails to install, those features simply remain on their older versions; nothing breaks and no security coverage is lost."
  - q: "Why does it fail on Asus laptops?"
    a: "Usually for the same generic reasons it fails anywhere: a corrupted update cache, a stalled update service, or a software conflict. On Asus machines the extra suspects are Armoury Crate and MyAsus background services, which occasionally hold locks on shell components or interfere with small package installs. Outdated Asus utilities cause more conflicts than current ones."
  - q: "Can I just ignore a failing Feature Experience Pack?"
    a: "Yes, safely — it contains no security patches, so ignoring it leaves no vulnerability. The caveat is that the underlying cause, like a corrupted cache or stalled service, can also block important updates. Fix the pipeline using the steps below even if you do not care about the pack itself, or at minimum verify your cumulative updates still install."
  - q: "How do I install the pack manually?"
    a: "Find its KB number in Settings, then Windows Update, then Update history. Search that KB number on the Microsoft Update Catalog, download the x64 package, and run it. Manual installation bypasses the Windows Update pipeline entirely and succeeds in most cases where the automatic attempt keeps failing."
---
The Windows Feature Experience Pack is a minor update with a major talent for failing repeatedly. It is a small package — shell feature refinements for things like the snipping tool and input panels — delivered through Windows Update. On Asus laptops it sometimes refuses to install: failed in update history, retried periodically, failed again. Everything else works, which makes it tempting to ignore.

Ignore the pack if you like — it carries no security fixes. But fix the pipeline anyway, because whatever is blocking this tiny package can block bigger updates too. On Asus machines the usual suspects are the generic ones (corrupted cache, stalled service) plus Asus-specific ones: Armoury Crate and MyAsus background services occasionally interfere with shell component updates, especially when outdated.

It helps to know what you are dealing with before you start troubleshooting. The Feature Experience Pack is versioned independently of Windows itself — you can check your installed version under Settings > System > About, where it appears as its own line item. When the pack fails, that version line simply stays where it is. Nothing degrades, nothing breaks; the system just misses out on minor refinements until the install succeeds. The fixes below run from simplest to most thorough. Work through them in order.

## Why this happens

- **The update cache is corrupted.** Damaged downloads fail verification — the top cause for small packages.
- **The update service is stalled.** A hung wuauserv blocks even tiny installs.
- **Armoury Crate or MyAsus conflicts.** Asus background services can lock shell components the pack updates.
- **Pending operations block it.** An earlier update awaiting restart holds the queue.
- **Corrupted system files.** Damage to the shell components being updated fails installer checks.
- **Antivirus interference.** Real-time protection can block the pack's file replacements.
- **The package was superseded.** A newer version replaced it, and Windows fails the old one instead of skipping it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry cleanly

Clear transient glitches first.

1. Do a full **Restart** — not a hybrid shutdown.
2. After booting, open **Settings > Windows Update** and click **Check for updates** before launching other programs.
3. If the pack installs, done. If it fails identically, continue.

### Fix 2: Update Asus utilities and note the KB number

Rule out Asus-side conflicts and get specific.

1. Open **MyAsus** and **Armoury Crate** and install all their pending updates — outdated Asus utilities cause more conflicts than current ones.
2. In **Settings > Windows Update > Update history**, note the failed pack's KB number.
3. Search the KB on [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues.
4. Retry the update check after the Asus utilities are current.

### Fix 3: Clear the update cache

The highest-probability fix for repeatedly failing small packages. Because the pack is tiny, its entire download is a single small payload — and if that payload is corrupted, every automatic retry fails at the verification step before installation even begins.

1. In an elevated Command Prompt: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`. Confirm each service reports stopped.
2. Rename: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Check for updates — the pack re-downloads fresh and usually installs. This single fix resolves more pack failures than all the others combined.

### Fix 4: Run the Windows Update troubleshooter

Automated repair for service and registration issues.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Windows Update** troubleshooter; apply its repairs.
3. Restart.
4. Retry the update.

### Fix 5: Quiet Asus background services temporarily

Expose whether an Asus utility is holding a lock.

1. In Task Manager's **Startup apps**, temporarily disable non-essential Asus utilities.
2. Temporarily disable third-party antivirus real-time protection.
3. Restart and retry the update immediately after boot, before utilities reload.
4. Re-enable protection afterward. If the pack installed, re-enable utilities one at a time to find the conflicting one.

### Fix 6: Install the pack manually from the Update Catalog

Bypass the pipeline entirely. The manual installer does not use the Windows Update download cache or services at all, so whatever was jamming the automatic attempt is irrelevant to this path.

1. On the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number from Fix 2.
2. Download the x64 package and run it. The installer is small and finishes in a minute or two.
3. Restart if prompted.
4. Verify the pack shows as installed in update history, and check Settings > System > About to confirm the Feature Experience Pack version line has advanced.

### Fix 7: Repair system files or hide the update

The final options for stubborn cases. If the pack fails after a clean cache, current Asus utilities, and a manual install attempt, the issue is likely damaged system files — or a pack version that simply does not agree with your configuration.

1. In an elevated Command Prompt: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`. Allow up to 30 minutes for DISM.
2. Restart and try the update once more, preferably via the manual catalog installer.
3. If it still fails while everything else updates fine, hide it with the show/hide updates troubleshooter — safe, since it has no security content.
4. Revisit in a month or two; reissued packs typically install cleanly, and the underlying pipeline will have had more chances to heal itself.

## Closing

The Feature Experience Pack failure on Asus laptops is a small problem with small fixes: clear the cache, update the Asus utilities, and install manually if needed. The one thing not to do is nothing — verify the underlying pipeline is healthy so the same cause does not start blocking security updates. For the same pack failure on other brands, see the [Acer pack guide](/articles/how-to-fix-feature-experience-pack-failed-to-install-on-acer-laptop/) and the [Dell pack guide](/articles/how-to-fix-feature-experience-pack-failed-to-install-on-dell-laptop/), or the [step-by-step pack repair](/articles/how-to-fix-feature-experience-pack-failed-to-install-step-by-step/) for the deepest walkthrough.
