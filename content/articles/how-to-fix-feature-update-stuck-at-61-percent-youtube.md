---
title: "Feature Update Frozen at 61%? Get Windows Moving Again"
slug: how-to-fix-feature-update-stuck-at-61-percent-youtube
date: 2026-09-22
categories: ["windows-update"]
tags: ["feature update", "stuck at 61", "windows 11", "update frozen"]
description: "Your Windows feature update has been sitting at 61% for hours? That's a classic stall point — here's what causes it and the proven sequence to unstick it safely."
thumbnail: "/images/thumbs/how-to-fix-feature-update-stuck-at-61-percent-youtube.webp"
faqs:
  - q: "Why does a feature update get stuck at exactly 61 percent?"
    a: "The 61% mark typically falls during the driver and device migration phase of the second boot stage, where Windows moves drivers and hardware settings into the new OS image. If a driver hangs during migration — often storage, display, or USB controller drivers — progress freezes at this exact point on many systems."
  - q: "How long should I wait before assuming the update is stuck?"
    a: "Give it at least two to three hours of zero progress before intervening, longer on older laptops with spinning hard drives. Feature updates legitimately slow down during migration phases. Only treat it as stuck if the percentage and the spinning dots are completely frozen for hours with no disk activity."
  - q: "Is it safe to force restart a feature update stuck at 61%?"
    a: "A single forced restart is generally recoverable because Windows keeps a rollback copy of the previous installation. The update will usually roll back automatically. What you should never do is interrupt it repeatedly or power off during the 'undoing changes' rollback phase that follows."
  - q: "Can low disk space cause a feature update to freeze at 61%?"
    a: "Yes — feature updates need substantial free space for staging files, driver backups, and the rollback image. With less than about 20GB free on the system drive, the migration phase can stall. Freeing space before retrying the update prevents many 61% freezes."
---

# Feature Update Frozen at 61%? Get Windows Moving Again

Few things test your patience like a Windows feature update that parks itself at 61% and refuses to budge. The dots keep spinning, the percentage doesn't move, and after two hours you're wondering whether your laptop is actually doing anything or just pretending. This particular number isn't random — 61% lands right in the driver migration phase, which is where updates most often get tangled up with a misbehaving driver.

The encouraging part: a stall at 61% is one of the most recoverable update failures there is. Windows keeps your old installation intact until the very end, so even a forced intervention usually ends with a clean rollback rather than a broken system. Follow the sequence below and you'll either get the update installed or land safely back on your working Windows, ready to try again properly.

## Why this happens

- **A driver hanging during migration.** Storage, display, or USB drivers that don't respond during the device migration phase freeze progress at 61%.
- **Insufficient free disk space.** The migration phase stages drivers and rollback data; under ~20GB free, it can stall silently.
- **Conflicting third-party antivirus.** Kernel-level security drivers can block the migration of other drivers, deadlocking the phase.
- **A failing or slow disk.** Bad sectors in the staging area cause endless retries that look like a freeze.
- **Connected peripherals confusing setup.** USB drives, docks, and printers add devices the migrator must process — one bad device stalls them all.
- **Corrupted update download.** A damaged feature update payload passes initial checks but fails mid-migration.
- **BIOS/firmware incompatibility.** Older firmware on some laptops conflicts with the new OS build's expectations during device handoff.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm It's Truly Stuck Before Touching Anything

Impatience causes more damage here than the stall itself. Verify first.

1. Watch the screen for a full 30 minutes — check for any disk activity light or faint drive sounds.
2. Open Task Manager with Ctrl + Shift + Esc if you can reach the desktop (some stalls still allow this) and look for disk activity under the Performance tab.
3. If the percentage hasn't moved in 2–3 hours AND there's zero disk activity, it's genuinely stuck.
4. Note the exact percentage and time — useful if you later need to [uninstall a problematic update](/articles/how-to-uninstall-problematic-update-on-windows-11/) or describe the issue to support.
5. Take a breath: Windows maintains a complete rollback image, so a failed update at this stage is designed to be reversible.

### Fix 2: Force a Restart and Let It Roll Back

One controlled forced restart is the standard recovery from a migration-phase stall.

1. Hold the power button for 10 seconds until the laptop shuts off completely.
2. Wait 30 seconds, then power it back on.
3. Windows should detect the failed update and display "Undoing changes made to your computer" — this rollback can take 30–90 minutes.
4. Do NOT interrupt the rollback. Let it finish completely, even if it seems slow.
5. Once back on your desktop, verify in **Settings > Windows Update > Update history** that the feature update shows as failed — this confirms a clean rollback.

### Fix 3: Disconnect All Peripherals and Update Drivers First

Since 61% is the driver migration phase, reducing the driver workload is the highest-value preparation for the retry.

1. Unplug every USB device except your charger — docks, external drives, printers, wireless receivers, everything.
2. If you use a laptop dock, undock and run the update on the bare laptop.
3. Open **Device Manager**, expand each category, and update critical drivers: display adapter, storage controllers, network adapters, and USB controllers.
4. Check your manufacturer's support page for a BIOS update — Acer, Dell, HP, and Lenovo all publish BIOS fixes that resolve migration stalls. The [Dell support hub](https://www.dell.com/support) and [HP support portal](https://support.hp.com/us-en) are good starting points for driver packs.
5. If your GPU uses NVIDIA or AMD drivers, grab the latest directly from the GPU maker's official driver download page rather than relying on old bundled versions.

### Fix 4: Free Up Disk Space and Run the Update Troubleshooter

Give the next attempt the room and the clean state it needs.

1. Open **Settings > System > Storage** and free at least 20–25GB on the system drive — empty the Recycle Bin, remove temp files, uninstall apps you don't use.
2. Run **Disk Cleanup** (search for it in Start) and check **Previous Windows installations** and **Temporary Windows installation files** — these can free 10–30GB.
3. Run the Windows Update troubleshooter from **Settings > System > Troubleshoot > Other troubleshooters**.
4. Restart the laptop after cleanup so no installer locks remain.
5. Retry the feature update only after space is confirmed free — the troubleshooter plus free space resolves a large share of repeat stalls.

### Fix 5: Temporarily Remove Third-Party Antivirus

Security drivers are frequent culprits in migration-phase deadlocks.

1. If you run third-party antivirus, uninstall it (not just disable — kernel drivers load at boot either way) using its official removal tool.
2. Windows Defender activates automatically and is fully compatible with feature updates.
3. Disable any third-party firewall or VPN client too, as their virtual adapters add migration work.
4. Retry the feature update with only Defender running.
5. Reinstall your preferred security suite after the update completes successfully.

### Fix 6: Install the Update via the Installation Assistant

If Windows Update keeps stalling at the same point, the [Update Assistant](https://www.microsoft.com/en-us/software-download/windows11) uses a different, more resilient installation path.

1. Back up important files first — external drive or cloud, your choice.
2. Download the Windows 11 Installation Assistant from Microsoft's software download page.
3. Run it with peripherals still disconnected and antivirus still removed.
4. The assistant downloads a fresh copy of the update, bypassing any corrupted cached payload.
5. Monitor progress — the assistant's migration phase is identical, but the clean payload and prepared drivers usually carry it through. If it stalls the same way, see our guide on [media creation tool errors](/articles/how-to-fix-media-creation-tool-error-0x80070002-in-windows-11-24h2/) for the USB-install alternative.

### Fix 7: Check Disk Health Before the Final Attempt

A disk with bad sectors will stall migration every single time, no matter how clean everything else is.

1. Open an elevated Command Prompt.
2. Run `chkdsk C: /f /r` and agree to run it at next restart.
3. Restart and let the full check complete — this can take an hour or more on large drives.
4. Check the results: if chkdsk reports bad sectors, back up immediately and consider replacing the drive before retrying the feature update.
5. If the disk is healthy and the update still stalls, note the failure code in update history — some stalls at this stage are the known [99% variant](/articles/how-to-fix-update-assistant-stuck-at-99-percent-youtube/) wearing a different mask, and the diagnostic steps there apply too.

## Closing

A feature update stuck at 61% feels alarming, but it's a well-understood failure: a driver or disk hiccup during the migration phase, caught by a system designed to roll back safely. Disconnect the peripherals, update the drivers, clear the space, and retry through the Installation Assistant — that combination unsticks the overwhelming majority of 61% freezes.
