---
title: "File Explorer Slow on an HP Laptop? Windows 11 Fixes"
slug: how-to-fix-file-explorer-slow-windows-11-on-hp-laptop
date: 2026-10-03
categories: ["performance"]
tags: ["file explorer slow", "hp laptop", "windows 11", "shell extensions", "explorer fix"]
description: "File Explorer lagging on your HP laptop running Windows 11? Fix slow folders, green loading bars, and delays with HP-specific and general solutions."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-slow-windows-11-on-hp-laptop.webp"
faqs:
  - q: "Why is File Explorer especially slow on HP laptops?"
    a: "HP ships several preinstalled utilities — HP Support Assistant, HP System Event Utility, McAfee trials, Dropbox promotions — that install Explorer shell extensions and background services. These hook into every folder render and right-click, adding latency on top of normal Explorer work. A new HP laptop often has five or more third-party extensions active before you install anything yourself."
  - q: "Should I uninstall HP bloatware to speed up Explorer?"
    a: "Selectively, yes. Remove the trial antivirus (replace with Defender or your chosen product), promotional apps, and duplicate utilities, but keep HP Support Assistant and core drivers — they handle BIOS and driver updates for your specific model. Use Settings > Apps > Installed apps and remove obvious trials and promos; when in doubt, disable its startup entry instead of uninstalling."
  - q: "Does HP's preinstalled antivirus slow down File Explorer?"
    a: "Yes, noticeably. Trial security suites (commonly McAfee on HP) add real-time scanning hooks and Explorer context-menu extensions that delay every folder open and file operation. If the trial expired, its half-active state is even worse. Either subscribe, or fully uninstall it with the vendor's removal tool and let Windows Defender take over cleanly."
  - q: "Will updating HP drivers fix slow File Explorer?"
    a: "It can, particularly storage and chipset drivers — an outdated Intel RST or chipset driver makes all disk I/O slower, and Explorer is disk-heavy. Get drivers from [HP Support](https://support.hp.com/us-en) for your exact model rather than relying solely on Windows Update. BIOS updates from HP have also resolved Explorer-adjacent slowness tied to power management."
---

HP laptops have a particular flavor of File Explorer slowness. Out of the box they carry HP utilities, trial antivirus, and promotional apps that all inject themselves into Explorer — shell extensions, icon overlays, background services — so folders that open instantly on a clean Windows install can crawl on a new HP. Add the usual Windows 11 Explorer issues on top and it's a perfect storm.

The fix has two halves: the HP-specific cleanup (bloatware, trial AV, drivers from HP's site) and the general Explorer repairs that apply to every Windows 11 machine. Do both and Explorer gets dramatically snappier. For right-click-specific delays, our [right-click menu guide](/articles/how-to-fix-right-click-menu-slow-windows-11-on-laptop/) goes deeper.

## Why this happens

- **HP bloatware shell extensions**: Preinstalled utilities register context-menu and overlay handlers that run on every folder render.
- **Trial antivirus hooks**: McAfee/trial suites add real-time scan interception plus Explorer extensions — heavy on every file operation.
- **Outdated HP chipset/storage drivers**: The drivers Windows installed generically underperform HP's tuned versions, slowing all disk I/O.
- **Thumbnail cache issues**: Corrupt or oversized thumbnail databases stall media folders regardless of brand.
- **OneDrive on-demand fetching**: Cloud placeholders make Explorer wait on downloads before rendering folders.
- **Quick Access dead paths**: HP's factory image sometimes pins promotional or dead locations that Explorer tries to resolve.
- **Search indexer competition**: The indexer rebuilding (common after HP's first big update wave) fights Explorer for disk.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean up HP bloatware and trial software

Remove what's slowing Explorer before tuning anything else.

1. Open **Settings** > **Apps** > **Installed apps** and sort by install date — the HP factory apps cluster at the beginning.
2. Uninstall: trial antivirus (McAfee/Norton trials), WildTangent games, Dropbox/ExpressVPN promotions, Booking.com or Amazon "apps," and any duplicate utilities (two photo apps, two music apps).
3. Keep: **HP Support Assistant**, **HP System Event Utility**, **HP PC Hardware Diagnostics**, and anything with "driver" in the name — these service your hardware.
4. After uninstalling a trial antivirus, run that vendor's **removal tool** (McAfee MCPR, Norton Remove and Reinstall) — the standard uninstaller leaves filter drivers that keep slowing file operations.
5. Reboot, then open Task Manager > **Startup apps** and disable remaining HP entries you don't need at boot (HP Analytics, HP Notifications).
6. Get replacement protection sorted: Windows Defender activates automatically once the trial is fully gone — verify in **Windows Security**.

### Fix 2: Update drivers from HP Support

Generic Windows drivers underperform on HP hardware.

1. Go to [HP Support](https://support.hp.com/us-en), enter your exact model (find it on the bottom sticker or via HP Support Assistant).
2. Download and install the latest **chipset**, **Intel Rapid Storage Technology (RST)**, and **graphics** drivers — install chipset first, reboot, then the rest.
3. Check the **BIOS** section: HP BIOS updates frequently fix power-management and storage-controller behavior that manifests as general sluggishness. Follow HP's instructions exactly — keep the charger connected during a BIOS flash.
4. In **Device Manager**, confirm no yellow warning icons remain after updating.
5. Retest Explorer in a large folder — storage driver updates alone often produce a visible speedup on HP machines that were running generic drivers.

### Fix 3: Restart Explorer and fix Quick Access

The quick universal wins.

1. Press `Ctrl + Shift + Esc`, find **Windows Explorer**, right-click > **Restart**.
2. Open **Folder Options** (search in Start) > **General** tab > click **Clear** next to "Clear File Explorer history."
3. Change **Open File Explorer to:** from **Home** to **This PC** — Home's Quick Access is Explorer's slowest view, and HP images often pin dead promotional paths there.
4. In the **View** tab of Folder Options, uncheck **Show sync provider notifications** to stop per-file cloud status queries.
5. Unpin anything in Quick Access pointing to removed drives, dead network shares, or HP promotional folders — right-click each > **Unpin from Quick Access**.

### Fix 4: Disable third-party shell extensions

The extensions from HP's bundle and your own apps stall every render.

1. Download **ShellExView** (NirSoft) and run as administrator.
2. Filter to non-Microsoft **Context Menu** handlers — disable HP utility entries, cloud storage entries, and archiver entries you don't use daily (red disable button).
3. Restart Explorer (Task Manager) after each batch and test folder speed.
4. Pay special attention to **Icon Overlay** handlers — HP utilities plus OneDrive/Dropbox can exceed Windows' 15-overlay limit, causing rendering stalls. Disable overlays for services you rarely use.
5. When speed returns, check the vendor's site for an updated version of the offending extension before re-enabling — or leave it disabled if you never used that feature.

### Fix 5: Rebuild thumbnails and fix OneDrive behavior

Media folders and cloud folders are the usual slow spots.

1. **Settings** > **System** > **Storage** > **Temporary files** > check **Thumbnails** > **Remove files**. Let one photo folder regenerate as a test.
2. For OneDrive: click the cloud icon > gear > **Settings** > **Sync and backup** — for folders you open constantly, right-click them in Explorer > **Always keep on this device** so Explorer never waits on downloads.
3. As a diagnostic, **Pause syncing** for 2 hours — if Explorer flies, cloud fetching was the bottleneck.
4. Reduce indexed locations if the indexer is mid-rebuild: **Settings** > **Privacy & security** > **Searching Windows** > **Advanced indexing options** > **Modify**.
5. If search results are also broken, see [Windows Search repair](/articles/how-to-fix-windows-search-not-working-on-windows-11/).

### Fix 6: Check disk health and free space

HP laptops with small SSDs fill up fast, and full drives slow everything.

1. **Settings** > **System** > **Storage** — if C: is over 85% full, free space now: **Temporary files**, then uninstall big unused apps.
2. Run **HP PC Hardware Diagnostics** (preinstalled, or via Esc-boot menu) > **Component Tests** > **Hard Drive** — HP's own test is tuned for your drive.
3. In an elevated terminal, `wmic diskdrive get status` should report OK for all drives.
4. Aim to keep 15–20% free; below 10%, Explorer, paging, and updates all degrade.
5. Our [disk space guide](/articles/how-to-free-up-disk-space-on-windows-11/) covers the bigger cleanups if the built-in tools aren't enough.

### Fix 7: Repair Windows components

For Explorer broken at the system level.

1. In an elevated terminal: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then reboot.
2. Install all pending updates: **Settings** > **Windows Update** — and check HP Support Assistant for HP-specific updates Windows Update doesn't carry.
3. If slowness started with a specific update, uninstall it (**Update history** > **Uninstall updates**) and pause updates for a week while a fix ships.
4. Last resort: an in-place repair install using [Windows 11 media](https://www.microsoft.com/en-us/software-download/windows11) — keeps files and apps while refreshing Explorer and all system components.
5. Document your exact HP model and what you tried — HP's support forums and technicians solve model-specific Explorer issues faster with that info upfront.

## Closing

Slow File Explorer on an HP laptop is usually the factory software load plus one general Windows issue. Strip the trialware and promotional extensions, update drivers from HP's site, clear Quick Access and thumbnails, and tame OneDrive — and Explorer on your HP will feel like the clean install it never quite was.
