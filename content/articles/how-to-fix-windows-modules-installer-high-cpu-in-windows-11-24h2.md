---
title: "Windows Modules Installer High CPU in Windows 11 24H2: Fix It"
slug: how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2
date: 2026-09-12
categories: ["performance"]
tags: ["windows modules installer", "tiworker", "windows 11 24h2", "high cpu", "trustedinstaller"]
description: "TiWorker.exe pinning CPU on Windows 11 24H2? 24H2-specific servicing behavior and fixes for a stuck Windows Modules Installer Worker."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "Why is TiWorker.exe so busy on 24H2 specifically?"
    a: "The 24H2 upgrade is one of the largest Windows 11 updates, replacing deep OS components, which gives the servicing stack an enormous post-upgrade workload: component migration, WinSxS optimization, and update finalization that can run for many hours. Additionally, 24H2's reworked update stack occasionally leaves servicing in a half-completed state if the upgrade was interrupted. Most 24H2 TiWorker activity is legitimate catch-up work, but multi-day activity signals a stuck state."
  - q: "How is this different from the general Windows 11 TiWorker issue?"
    a: "The mechanics are identical — TiWorker.exe services Windows Update on every version — but 24H2 adds specific wrinkles: the bigger upgrade footprint means longer legitimate servicing, 24H2's new checkpoint update system changes how cumulative updates stage, and early-24H2 servicing bugs required patching. The fixes overlap heavily with the general guide, with extra attention to completing the 24H2 enablement and installing the latest cumulative update."
  - q: "Should I pause updates on 24H2 to stop TiWorker?"
    a: "Pausing is a temporary pressure valve, not a fix — it stops new servicing work but leaves the stuck work stuck, and deferred updates accumulate into a bigger future servicing storm. Use a short pause (a week) only to reclaim the machine while you apply the real fixes: clearing the update cache, repairing the component store, and manually installing the stuck update. Then unpause and let servicing complete normally."
  - q: "Can TiWorker high CPU mean my 24H2 install is corrupted?"
    a: "It can suggest servicing corruption, though rarely a fully corrupted OS. The typical pattern is a damaged component store or a corrupted update download that TiWorker cannot complete, so it retries indefinitely. DISM's RestoreHealth specifically targets this by repairing the component store from known-good sources. If DISM and SFC both fail to repair it, that is stronger evidence of deeper corruption worth a repair install."
---

On Windows 11 24H2, `Windows Modules Installer Worker` (TiWorker.exe) working hard is expected — the 24H2 upgrade is enormous, and the servicing stack needs serious time to migrate components, optimize the WinSxS store, and finalize everything. But there's a line between "big upgrade, big cleanup" and "stuck": legitimate post-24H2 servicing tapers over hours to a day, while a stuck servicing stack burns CPU for days, often with a failed update sitting in Update history as the telltale.

24H2 adds its own wrinkles to the classic TiWorker story: checkpoint cumulative updates that stage differently, early-24H2 servicing bugs that needed patching, and half-completed upgrade states when installs get interrupted. This guide covers the 24H2-specific angles — verifying the upgrade completed cleanly, getting the latest servicing fixes, and unsticking the worker — alongside the proven general fixes. Check **Settings** > **Windows Update** first: pending, failed, or endlessly "installing" updates tell you exactly where TiWorker is stuck. For the version-neutral guide, see [Windows Modules Installer high CPU after an update](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/).

## Why this happens

- **Massive 24H2 post-upgrade servicing**: Component migration and store optimization after the big upgrade.
- **Checkpoint update staging**: 24H2's new update format changing how servicing work is queued.
- **Interrupted 24H2 upgrade**: A disrupted install leaving servicing half-completed.
- **Corrupted update download**: Damaged payload TiWorker retries in a loop.
- **Early-24H2 servicing bugs**: Known issues fixed by later cumulative updates.
- **Damaged component store**: Corruption TiWorker can't work around.
- **Disk slowness amplifying servicing**: Slow or full drives stretching servicing work for hours.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the 24H2 upgrade completed cleanly

Confirm the foundation before fixing the worker.

1. Check **Settings** > **System** > **About** — confirm **Version 24H2** and a sensible **OS build** number.
2. Open **Settings** > **Windows Update** > **Update history** — look for failed or endlessly retrying updates; a failure here is TiWorker's assignment.
3. Check for a pending restart — much servicing finalizes across reboots; restart now if one is waiting.
4. Give legitimate post-upgrade servicing one full plugged-in day — 24H2's footprint genuinely needs it.
5. If TiWorker is still pinned after 48 hours with failed updates in history, it's stuck — continue below.

### Fix 2: Install the latest 24H2 cumulative update

Servicing fixes servicing.

1. Run **Settings** > **Windows Update** > **Check for updates** repeatedly until fully clear — Microsoft patched several 24H2 servicing issues in cumulative updates.
2. If the offered update is the one that's stuck, note its KB number for the manual-install approach in Fix 5.
3. Run the **Windows Update troubleshooter** (**Settings** > **System** > **Troubleshoot** > **Other troubleshooters**) if updates won't install.
4. Check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the KB if Windows Update can't fetch it — a manual download bypasses a broken automatic path.
5. After successfully installing the latest cumulative update, give TiWorker one idle session to complete the newly-unblocked work.

### Fix 3: Clear the servicing cache

The classic fix for TiWorker loops.

1. Open an **elevated Command Prompt**.
2. Stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptSvc`.
3. Rename the caches: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptSvc`.
5. **Check for updates** again — clean caches let the stuck update download and install properly. Keep the `.old` folders for a week before deleting.

### Fix 4: Repair 24H2's component store

Fix what TiWorker services.

1. In an elevated terminal, run `DISM /Online /Cleanup-Image /RestoreHealth` — allow 15–30 minutes; this repairs the store TiWorker works against.
2. Follow with `sfc /scannow` for protected system files.
3. If DISM can't reach Windows Update for repair sources, mount a 24H2 ISO and use `/Source:WIM:X:\sources\install.wim:1` with your mounted drive letter.
4. Restart, then re-check Windows Update — repaired servicing components unstick the looping update.
5. Expect one final TiWorker surge as it completes the previously-blocked work, then a settle — that's success, not failure.

### Fix 5: Manually install the stuck update

Bypass the broken path entirely.

1. Identify the exact KB number from **Update history**'s failed entries.
2. Download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — match your architecture (x64 for most laptops) and the 24H2 designation.
3. Close heavy apps and run the `.msu` — manual installs avoid the download-corruption issues of the automatic path.
4. Reboot when prompted and verify **Update history** shows success.
5. TiWorker should stand down within the hour — if it doesn't, the issue is servicing corruption (Fix 4), not the update itself.

### Fix 6: Mind the disk during servicing

24H2 servicing is disk-heavy.

1. Keep 15%+ free on C: — servicing stages gigabytes; a full drive makes TiWorker crawl (see [freeing disk space](/articles/how-to-free-up-disk-space-on-windows-11/)).
2. Check drive health: `wmic diskdrive get status` should say OK; run `chkdsk C: /scan` for file-system errors.
3. Avoid disk-heavy tasks during active servicing — big copies and game installs compete for the I/O TiWorker needs.
4. On HDDs, defragment after servicing completes — never during.
5. If servicing is healthy but slow, the disk is the bottleneck — an SSD upgrade is the long-term answer.

### Fix 7: Schedule 24H2 servicing sensibly

Make future servicing invisible.

1. Set **Active Hours** to cover your workday so installs happen outside it.
2. After Patch Tuesday, check for updates in the evening and reboot before bed — servicing works overnight.
3. Don't pause updates long-term to avoid TiWorker — deferred updates compound into bigger servicing storms later.
4. Leave **automatic maintenance** (2 AM default) alone — it handles WinSxS cleanup that would otherwise burden TiWorker.
5. Keep the system current — each cumulative update includes servicing-stack improvements that make the next one smoother. Microsoft's [Windows Update support](https://support.microsoft.com/en-us/windows) documents the servicing model.

## Closing

TiWorker.exe high CPU on Windows 11 24H2 is usually the price of a very large upgrade: extended but legitimate servicing that finishes within a day or two. When it doesn't finish, it's a stuck cache, a damaged component store, or a failed update looping — each with a direct fix above. Help the worker finish its job instead of fighting it, and 24H2 settles into the fast, quiet OS it was meant to be.
