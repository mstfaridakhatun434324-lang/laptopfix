---
title: "\"Reset This PC\" Failed on ARM Laptops: How to Fix It"
slug: reset-this-pc-arm-laptop-failed
date: 2026-10-23
categories: ["ai-pc"]
tags: ["reset this pc", "windows recovery", "arm laptop", "recovery failed", "winre", "troubleshooting"]
description: "Fix 'Reset this PC' failing on ARM laptops: repair the Windows Recovery Environment, use cloud download, and rebuild recovery media step by step."
thumbnail: "/images/thumbs/reset-this-pc-arm-laptop.webp"
faqs:
  - q: "Why does Reset this PC fail on my ARM laptop?"
    a: "The usual causes are a corrupted or missing Windows Recovery Environment (WinRE), damaged system files the reset needs, insufficient disk space, or a recovery image that doesn't match the installed Windows build. Repairing WinRE fixes most failures."
  - q: "Will I lose my files if the reset fails halfway?"
    a: "A failed reset normally rolls back to your previous Windows state without deleting files, but there are no guarantees. Back up your important files to an external drive before attempting the reset again."
  - q: "What's the difference between cloud download and local reinstall?"
    a: "Cloud download fetches a fresh Windows image from Microsoft (needs 4GB+ download), while local reinstall reuses files already on your disk. On ARM laptops, cloud download is more reliable because it bypasses corrupted local recovery files."
  - q: "Can I reset an ARM laptop without the recovery partition?"
    a: "Yes — cloud download doesn't need the local recovery image at all. If the recovery partition is damaged or missing, cloud download is your path forward, provided you have a stable internet connection."
---

You decided to start fresh, clicked through Reset this PC, waited — and got "There was a problem resetting your PC" with no changes made. On ARM laptops this failure is more common than on x64 machines, because the reset process depends on the Windows Recovery Environment and a recovery image that must match your ARM64 Windows build exactly.

The reset is not magic: it boots into WinRE, wipes or refreshes the system partition, and reinstalls Windows from either local files or a cloud download. When any piece of that machinery is damaged — WinRE itself, the system image, or the disk space it needs — the whole operation aborts.

This guide gives you six fixes in order: checking the recovery environment first, then repairing it, then alternative reset paths. Back up your files before you begin — a failed reset usually rolls back safely, but "usually" is not a backup strategy.

## Why this happens

- **Windows Recovery Environment (WinRE) corrupted or disabled:** Reset this PC runs inside WinRE. If WinRE is damaged, missing, or disabled, the reset cannot even start its work.
- **Corrupted system files:** The reset process verifies system integrity before proceeding. Deep corruption in the component store causes it to abort rather than install a broken system.
- **Insufficient free disk space:** Both local and cloud resets need working room — typically 10GB+ free. A nearly-full drive kills the reset early.
- **Recovery image mismatch:** The local recovery image must match the installed Windows build. After major updates (like 25H2), a stale recovery image can refuse to apply.
- **Third-party disk encryption or security software:** Some encryption tools and aggressive security suites lock the partitions WinRE needs to modify, causing the reset to fail at the disk-layout stage.
- **Failing storage:** Bad sectors in the system or recovery partitions produce read errors mid-reset. If resets fail repeatedly at the same percentage, suspect the SSD.
- **App-level corruption misread as system failure:** Sometimes what feels like a broken system is really a broken app layer — the same distinction that matters when [the Xbox app misbehaves on ARM](/articles/xbox-app-arm-windows-not-working/). A reset is a heavy hammer; make sure you need it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify and re-enable the Windows Recovery Environment

A disabled or broken WinRE is the number one cause. Checking its status takes a minute and tells you exactly where you stand.

1. Open **Terminal as administrator** and run `reagentc /info` — look for "Windows RE status: Enabled" and a valid recovery location.
2. If it shows Disabled, run `reagentc /enable` and then `reagentc /info` again to confirm it is now Enabled.
3. If enabling fails with an error about a missing image, the WinRE image itself is damaged — note this and continue to Fix 2, which rebuilds it.
4. Free up disk space regardless: aim for at least 15GB free on C: (empty the Recycle Bin, run Disk Cleanup, move large personal files to external storage).
5. Retry Reset this PC from **Settings > System > Recovery**. If WinRE was the only problem, the reset now proceeds.

### Fix 2: Repair system files with SFC and DISM

Corruption in the component store makes the reset abort during its verification phase. Repairing it first gives the reset clean material to work with.

1. Open **Terminal as administrator** and run `sfc /scannow` — let it complete fully, which can take 15-30 minutes.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store from Windows Update. On ARM laptops this downloads ARM64 repair files automatically.
3. If DISM fails, retry it with a stable internet connection — it needs to reach Microsoft's servers for clean file copies.
4. Run `sfc /scannow` once more after DISM completes to confirm everything now verifies clean.
5. Retry the reset. If it still fails at the same point, the recovery image itself (not the live system) is likely the problem — continue to Fix 3.

### Fix 3: Use cloud download instead of local reinstall

Cloud download sidesteps every local recovery-file problem by fetching a fresh ARM64 Windows image from Microsoft. On ARM laptops it is the more reliable path.

1. Go to **Settings > System > Recovery > Reset PC** and start the reset flow again.
2. When asked, choose **Cloud download** instead of **Local reinstall** — you will need a stable internet connection and about 4-5GB of download.
3. Choose **Keep my files** or **Remove everything** as needed (back up first either way).
4. Let the download and installation run without interruption — do not let the laptop sleep; plug in the charger.
5. If cloud download also fails, the problem is likely WinRE itself or the disk — continue to Fix 4. For the full cloud-download troubleshooting path, see [cloud download recovery on ARM laptops](/articles/cloud-download-recovery-arm-laptop/).

### Fix 4: Rebuild WinRE manually

When WinRE's image file is damaged, `reagentc /enable` cannot fix it — you need to restore a clean WinRE image and re-register it.

1. In admin Terminal, run `reagentc /disable` to detach the broken recovery environment.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` again to ensure the component store (which contains a clean WinRE copy) is healthy.
3. Re-enable with `reagentc /enable` and verify with `reagentc /info` — the status should now show Enabled with a valid location.
4. If it still fails, your Windows installation media approach from Fix 5 is the fallback — a WinRE rebuild needs source files that a deeply damaged system may lack.
5. Once WinRE shows Enabled, retry Reset this PC with cloud download.

### Fix 5: Reset from bootable ARM64 installation media

When the on-disk recovery machinery is beyond repair, external media bypasses it entirely. You need ARM64-specific media — x64 media will not boot on a Snapdragon laptop.

1. On another computer, download the Windows 11 ARM64 ISO from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create a bootable USB with Rufus (select the ARM64 ISO — Rufus handles ARM64 media correctly) or the Media Creation Tool's ARM64 path.
3. Boot the laptop from the USB (interrupt boot with the boot-menu key — often F12 — or change boot order in UEFI).
4. Choose **Repair your computer > Troubleshoot > Reset this PC** from the media's recovery environment, or do a clean install from the media if the reset option is unavailable.
5. After reinstalling, immediately run Windows Update to pull the latest ARM64 drivers, then reinstall your apps. This is the "nuclear option" that works when nothing on the disk can be trusted.

### Fix 6: Check disk health and rule out hardware failure

Resets that fail at the same percentage every time — or WinRE repairs that never stick — point at the SSD itself. Confirm before doing anything drastic.

1. Open admin Terminal and run `chkdsk C: /f /r` — schedule it for the next restart if prompted, then restart and let the full scan complete.
2. Check the SSD's SMART health: open **Terminal** and run `wmic diskdrive get status` — anything other than "OK" is a red flag.
3. Your maker's diagnostics (Lenovo Vantage, HP Support Assistant, Dell SupportAssist) include storage tests — run the full storage diagnostic.
4. If the SSD is failing, back up immediately and contact your maker's support about a drive replacement — no software fix repairs bad flash.
5. If the disk is healthy and resets still fail after all software fixes, consider that the goal may not need a reset at all: targeted repairs — like fixing [NPU benchmark anomalies](/articles/how-to-benchmark-npu-windows-11/) or [app-specific glitches](/articles/copilot-canvas-not-working/) — often resolve the underlying complaint with far less disruption.

## Closing

"Reset this PC" failures on ARM laptops are recovery-machinery failures, not mysteries: a broken WinRE, corrupted system files, or a stale local image. Verify WinRE with `reagentc`, repair the component store with DISM, prefer cloud download, and fall back to ARM64 installation media — one of those four resolves nearly every case.
