---
title: "How to Fix TiWorker High CPU in Windows 11 24H2"
slug: how-to-fix-tiworker-high-cpu-in-windows-11-24h2
date: 2026-10-12
categories: ["performance"]
tags: ["tiworker", "high cpu", "windows 11 24h2", "servicing"]
description: "TiWorker.exe stuck at high CPU on Windows 11 24H2? Fix 24H2's servicing quirks: checkpoint updates, component store repair, and stuck cumulative updates."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-in-windows-11-24h2.webp"
faqs:
  - q: "What is TiWorker.exe on Windows 11 24H2?"
    a: "TiWorker.exe (Windows Modules Installer Worker) is the servicing engine that installs Windows updates and manages system components. On 24H2 it also handles the newer checkpoint cumulative update format — smaller incremental updates built on checkpoints. Sustained high CPU means it's installing updates, cleaning up the component store, or stuck on a corrupted update — the fixes below distinguish and resolve each case."
  - q: "Are checkpoint updates related to TiWorker CPU problems?"
    a: "They can be. 24H2 introduced checkpoint cumulative updates, where each month's update builds on a checkpoint rather than the original release. If a checkpoint is damaged or missing, TiWorker works much harder — downloading larger payloads and reconciling components. A corrupted checkpoint state is a 24H2-specific cause of prolonged TiWorker activity that the older 'just reset SoftwareDistribution' advice doesn't fully address."
  - q: "How is this different from general Windows Modules Installer issues?"
    a: "The core engine is the same as on other Windows versions, but 24H2's servicing stack has its own quirks: checkpoint update mechanics, a larger component store (WinSxS) from the 24H2 upgrade itself, and 24H2-specific known issues documented per-KB. Our general [Windows Modules Installer guide](/articles/how-do-i-fix-windows-modules-installer-high-cpu/) covers the version-agnostic fixes; this guide targets what's unique to 24H2."
  - q: "Should I disable Windows Update to stop TiWorker?"
    a: "No — disabling updates trades a temporary CPU annoyance for missing security patches, and Windows re-enables the service anyway. The correct approach is fixing the stuck state so TiWorker finishes and idles: repair the component store, clear corrupted update metadata, and let updates complete during scheduled maintenance. A healthy 24H2 system sees TiWorker only briefly during update days."
---

`TiWorker.exe` grinding at high CPU for hours on Windows 11 24H2 has a flavor all its own. The engine is the familiar Windows Modules Installer Worker, but 24H2 changed the servicing game with **checkpoint cumulative updates** — and the 24H2 upgrade itself left many systems with a bloated component store and servicing quirks the old fixes don't fully address. If TiWorker spikes briefly on update days, that's normal. If it never settles, or returns every boot, you're dealing with 24H2-specific servicing problems. (For the version-agnostic TiWorker playbook, see our [general guide](/articles/how-do-i-fix-windows-modules-installer-high-cpu/).) For update-download-side issues, [Service Host update loops](/articles/how-to-fix-service-host-high-cpu-on-asus-laptop/) covers the wuauserv container.

## Why this happens

- **Checkpoint update reconciliation**: Damaged checkpoint state forcing full-payload downloads and heavy component merging.
- **Bloated WinSxS from the 24H2 upgrade**: The feature update leaves a large component store TiWorker must maintain.
- **Stuck 24H2 cumulative update**: A specific KB failing to install and retrying.
- **Corrupt component store**: Damage in the servicing stack TiWorker installs from.
- **Post-upgrade cleanup pending**: 24H2's own cleanup tasks running for days after the upgrade.
- **Driver updates bundled with cumulative updates**: 24H2 pushing driver updates that conflict and roll back repeatedly.
- **Insufficient disk space for servicing**: Checkpoint mechanics need more scratch space than old-style updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check 24H2 update status and TiWorker behavior

Establish whether it's working, stuck, or cleaning up.

1. Go to **Settings** > **Windows Update** > **Update history** — note the most recent **cumulative update for 24H2** and whether any show **"Failed to install"** with an error code.
2. In **Task Manager** > **Details**, watch **TiWorker.exe** for 30 minutes: declining CPU = progressing; flat high CPU = stuck; high CPU with heavy disk writes = component store work.
3. Check free space on C: — 24H2 servicing wants **20GB+** free; cramped drives stall checkpoint operations specifically.
4. Open `C:\Windows\Logs\CBS\CBS.log` and check recent timestamps — active progress entries vs. repeating identical errors tells you working vs. stuck.
5. Confirm you're actually on 24H2: `winver` should show **Version 24H2** — servicing advice differs meaningfully from 23H2.

### Fix 2: Run the 24H2 update troubleshooter and targeted resets

The automated pass, 24H2-aware.

1. **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Windows Update** > **Run** — let it complete and reboot if asked.
2. If a specific KB keeps failing, note its number (e.g., KB504XXXX) and check Microsoft's known-issues documentation for 24H2 — some 24H2 KBs had servicing bugs fixed by later out-of-band updates.
3. Reset the update cache the thorough way: elevated prompt, `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`, rename `C:\Windows\SoftwareDistribution` to `.old`, restart the services.
4. After the reset, **Check for updates** and let it run to completion — don't interrupt; checkpoint downloads resume poorly.
5. If Windows Update itself is broken, download the failing KB directly from the [Update Catalog](https://www.catalog.update.microsoft.com/) and install the standalone `.msu` — this bypasses the damaged metadata path.

### Fix 3: Repair the component store (DISM, 24H2 thorough)

The servicing stack TiWorker depends on.

1. Elevated Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth` — on 24H2 this also repairs checkpoint-related component data. Allow 20–40 minutes.
2. Follow with `sfc /scannow` to repair protected files from the restored store.
3. For deeper store issues: `DISM /Online /Cleanup-Image /StartComponentCleanup` — cleans superseded components, shrinking the WinSxS TiWorker maintains.
4. The aggressive variant: `DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase` — makes all current updates permanent (you can't uninstall them afterward) but maximally slims the store. Use only when the system is stable otherwise.
5. Reboot, check for updates, and monitor TiWorker — a healthy store lets pending updates install cleanly instead of looping.

### Fix 4: Clean up post-24H2-upgrade residue

The upgrade's leftovers keep TiWorker busy.

1. Run **Disk Cleanup** (`cleanmgr`) > **Clean up system files** > check **"Previous Windows installation(s)"** and **"Windows Update Cleanup"** — the 24H2 upgrade leaves tens of GB that servicing keeps tripping over. (Only remove previous installations if you're past the 10-day rollback window and committed to 24H2.)
2. In **Settings** > **System** > **Storage** > **Temporary files**, clear **Delivery Optimization Files** and **Windows upgrade log files**.
3. Check **Settings** > **Windows Update** > **Advanced options** > **Optional updates** — 24H2 often queues driver updates here that conflict; install them one at a time, skipping any that repeatedly fail.
4. If **"Windows.old"** exists and cleanup won't remove it, delete via Disk Cleanup only — never manually delete Windows.old while servicing references it.
5. After cleanup, give TiWorker one full idle session to finish reconciling the slimmer store, then confirm it idles.

### Fix 5: Address 24H2-specific driver and firmware interactions

24H2's driver servicing has its own failure modes.

1. Open **Device Manager** and look for devices with warning icons appearing after 24H2 updates — 24H2's bundled driver updates occasionally install wrong drivers (notably Wi-Fi and audio).
2. For any suspect: **Properties** > **Driver** > **Roll Back Driver**, or manually install the maker's 24H2-verified driver — Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel components, or the NVIDIA/AMD direct downloads for graphics.
3. Update the **BIOS/firmware** to a 24H2-era release from your laptop maker — 24H2 tightened some hardware requirements, and old firmware causes servicing-detected "incompatibilities" that TiWorker retries.
4. In **Windows Update** > **Advanced options**, consider pausing **driver updates via Windows Update** (Pro: Group Policy > "Do not include drivers with Windows Updates") if driver churn is the loop source — manage drivers manually instead.
5. Re-measure TiWorker after driver stabilization — driver install/rollback cycles are some of its heaviest legitimate work.

### Fix 6: In-place upgrade as the servicing reset

When the servicing stack itself is beyond DISM.

1. Download the **Windows 11 24H2 ISO** from the [software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run **setup.exe**, choose **Keep personal files and apps** — this reinstalls Windows over itself, rebuilding the entire servicing stack, checkpoint state, and component store.
3. The process takes 1–3 hours with several reboots — TiWorker will be legitimately busy during it; that's expected.
4. Afterward, run Windows Update to completion — the fresh servicing stack should process updates cleanly.
5. Monitor for a week: TiWorker should now appear only during actual update installations. If it still loops on a clean servicing stack, suspect hardware (failing drive stretching installs — check S.M.A.R.T.) or a genuinely problematic KB to skip.

## Closing

TiWorker on 24H2 is the same engine with new servicing mechanics — checkpoint updates, a bigger component store, and 24H2-specific KB quirks. Work the 24H2-aware sequence: troubleshooter and cache reset, DISM with component cleanup, post-upgrade residue removal, driver stabilization — and the in-place upgrade when the stack itself is broken. Then TiWorker goes back to brief, boring appearances on update days.
