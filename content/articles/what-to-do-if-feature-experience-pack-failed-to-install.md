---
title: "Feature Experience Pack Failed to Install? Here Is What to Do"
slug: what-to-do-if-feature-experience-pack-failed-to-install
date: 2026-09-06
categories: ["windows-update"]
tags:
  - "feature experience pack"
  - "windows update"
  - "install failed"
  - "windows 11"
description: "The Windows Feature Experience Pack delivers taskbar, shell, and app improvements through Windows Update. If it fails to install, these steps diagnose the cause and get it applied."
thumbnail: "/images/thumbs/what-to-do-if-feature-experience-pack-failed-to-install.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It is a package of updates to Windows shell features — parts of the taskbar, Start menu, Settings app, and built-in apps — delivered through Windows Update independently of full feature updates. It lets Microsoft ship user-experience improvements to Windows 10 and 11 without waiting for the annual release."
  - q: "Why would the Feature Experience Pack fail to install?"
    a: "The usual reasons mirror other update failures: a corrupted update cache, damaged servicing-stack files, insufficient disk space, or a conflict with a pending feature update. Because it touches shell components, third-party shell modifications like Start menu replacements can also block it."
  - q: "Can I just ignore a failed Feature Experience Pack?"
    a: "You can, temporarily — your laptop keeps working. But the pack often bundles fixes for shell bugs and Settings crashes, and repeatedly failing updates can jam the queue for other updates. It is better to fix it once than to let it fail every Patch Tuesday."
  - q: "Will reinstalling the pack reset my taskbar customizations?"
    a: "No. The Feature Experience Pack updates system components, not your personal layout. Pinned apps, taskbar alignment, and Start menu pins survive the install. If you use a third-party Start menu tool, update that tool afterward for compatibility. Your desktop background, themes, and accessibility settings are equally unaffected by the pack."
---

Of all the updates Windows offers, the Feature Experience Pack has the most forgettable name and the most annoying failure mode: it fails quietly, retries forever, and clutters your update history with red entries. You may not even know what it does — but its repeated failures can block or delay the updates that actually matter.

The pack updates pieces of the Windows shell: the taskbar, parts of the Start experience, the Settings app, and bundled apps. When it fails, the cause is usually mundane — a corrupted cache, a servicing hiccup, or a conflict with shell customizations — rather than anything exotic.

Below is the practical sequence for getting it installed: verify what is failing, clear the way, repair the engine, and install the pack cleanly. If you also see driver updates failing alongside it, our guide on [failing driver updates](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/) addresses that parallel problem.

## Why this happens

- **Corrupted update cache:** the pack's downloaded files are damaged, so its installer fails verification every retry.

- **Servicing stack damage:** the underlying install machinery has corrupt files, which hits small packs as readily as big ones.

- **Pending feature update conflict:** the pack sometimes cannot install while a feature update is staged or partially downloaded.

- **Third-party shell tools:** Start menu replacements and taskbar modifiers hook the same components the pack updates, causing conflicts.

- **Insufficient disk space:** even small packs need working room, and laptops with nearly full drives fail them.

- **Stuck update database entries:** the DataStore recorded a partial install, and every retry trips over the stale record.

- **Metered connection throttling:** the pack may download incompletely over metered connections and then fail at install.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm exactly what is failing

Windows Update history distinguishes the Feature Experience Pack from cumulative and driver updates. Confirming the failing entry is really the pack keeps you from fixing the wrong thing.

1. Open Settings, Windows Update, then Update history.
2. Expand the failed entries and look for Windows Feature Experience Pack with its version number.
3. Note the error code shown — 0x80070002, 0x80070003, and 0x80240034 are the usual suspects.
4. Check whether other updates are also failing or if the pack is alone.
5. If everything is failing, treat it as an engine problem and continue through all fixes.

### Fix 2: Clear the update cache

A damaged download is the top cause of pack failures. Clearing the cache forces a fresh, intact download of the pack on the next check.

1. Open Terminal (Admin) from the Start right-click menu.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Restart the services with the matching `net start` commands and reboot.
5. Run Check for updates and let the pack re-download completely.

### Fix 3: Temporarily disable shell customization tools

Start menu replacements, taskbar tweakers, and Explorer add-ons hook the exact components the pack modifies. Disabling them for one install attempt removes a genuine and common conflict.

1. Open Task Manager, Startup apps, and disable any Start menu or taskbar customization tools.
2. Check Settings, Apps, Installed apps for shell modification utilities and close them fully.
3. Restart the laptop so no hooks remain loaded in Explorer.
4. Run Windows Update and let the Feature Experience Pack install.
5. Re-enable your tools afterward and check the vendor for a compatibility update.

### Fix 4: Run SFC and DISM

When the pack fails with file-not-found style codes, the servicing stack or system files are damaged. These two scans restore them from known-good sources.

1. In Terminal (Admin), run `sfc /scannow` to completion.
2. Restart, then run `DISM /Online /Cleanup-Image /RestoreHealth` in a new admin terminal.
3. Allow up to 30 minutes for DISM on a laptop; do not interrupt it.
4. Restart once more after both scans finish.
5. Retry the Feature Experience Pack install from Windows Update.

### Fix 5: Install the pack via the Update Catalog

The standalone installer sidesteps whatever is broken in the automatic pipeline. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) for the pack's KB number and install it directly.

1. Find the pack's KB number in update history or on Microsoft's release notes.
2. Search that KB on the Microsoft Update Catalog.
3. Download the x64 package (or ARM64 for Snapdragon laptops).
4. Run the .msu and let it install, then restart when prompted.
5. Verify the pack version updated under Settings, System, About.

### Fix 6: Free disk space and check the connection

Boring causes deserve checking: a nearly full drive or a metered connection that truncates downloads will fail the pack every time, and both are two-minute checks.

1. Confirm at least 10-15 GB free on C: via Settings, System, Storage.
2. Run Disk Cleanup with system files to clear Windows Update Cleanup.
3. Check Settings, Network and internet — turn off Metered connection on your Wi-Fi.
4. Connect the charger; some installs defer on battery.
5. Retry the update on a stable, unmetered connection.

### Fix 7: Use the Windows 11 Installation Assistant as a last resort

If the pack will not install because a feature update is stuck staged behind it, moving the whole OS forward with the [Windows 11 Installation Assistant](https://www.microsoft.com/en-us/software-download/windows11) often resolves the pack as a side effect.

1. Back up important files first.
2. Download the Installation Assistant from Microsoft's Windows 11 download page.
3. Run it and let it upgrade Windows to the latest build.
4. After the upgrade completes, run Windows Update normally.
5. Confirm the Feature Experience Pack now shows as installed in update history.

## Closing

A failing Feature Experience Pack is rarely a crisis, but it is never worth ignoring — it clutters your history and can jam the queue. Identify the failing entry, clear the cache, park your shell tools for one install, and repair the servicing stack if needed. The pack is small; the fix should be too. If the pack failure came with a restart hang, see our [guide to updates stuck on the restarting screen](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/).
