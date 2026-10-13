---
title: "Blue Screen After a Windows 11 Update? Proven Fixes"
slug: how-to-fix-blue-screen-after-windows-11-update
date: 2026-09-29
categories: ["windows-errors"]
tags: ["blue screen", "windows 11 update", "bsod"]
description: "Blue screening right after a Windows 11 update? Learn why updates break drivers, how to roll back the bad update, and how to get your laptop stable again."
thumbnail: "/images/thumbs/how-to-fix-blue-screen-after-windows-11-update.webp"
faqs:
  - q: "Why does my laptop blue screen after every Windows 11 update?"
    a: "Feature and cumulative updates replace core drivers and system files. If your laptop has an old graphics, storage, or chipset driver that conflicts with the new Windows build, the system crashes. Recurring crashes after every update usually mean one stale driver — often the display or storage driver — needs updating from your laptop maker's site."
  - q: "Can I uninstall the Windows 11 update that caused the blue screen?"
    a: "Yes. Go to Settings > Windows Update > Update history > Uninstall updates, select the most recent update, and uninstall it. Windows also auto-rolls back a feature update within 10 days via Settings > System > Recovery > Go back. Uninstalling buys you time to update the conflicting driver before reinstalling the update."
  - q: "Should I pause Windows updates after a bad one?"
    a: "Temporarily, yes. Pausing for 1–2 weeks lets Microsoft or your laptop maker ship a fix. Go to Settings > Windows Update and pause updates, but don't leave them paused forever — security updates matter. Use the pause to update drivers, then resume."
  - q: "What if the blue screen happens during the update itself?"
    a: "Interruptions during an update can corrupt the installation. Let automatic repair try first; if it fails, boot from Windows 11 installation media, choose Repair your computer, and use Startup Repair or System Restore. If the update keeps failing at the same percentage, check the error code and fix the underlying driver or disk issue first."
---
Few things are more frustrating than a Windows 11 update that was supposed to make your laptop better — and instead leaves it blue screening on every boot. The update itself is rarely "broken." What usually happens is the new Windows build clashes with an old driver on your machine, and the system crashes before you can even log in.

The fix path depends on whether you can still reach Windows. If you can boot (even into Safe Mode), start at Fix 1. If the laptop won't boot at all, jump to the recovery fixes near the end, which use the Windows recovery environment — our [automatic repair loop guide](/articles/how-do-i-fix-automatic-repair-loop-windows-11/) covers that scenario in depth. For black screens with no error message rather than blue ones, see [black screen troubleshooting after a Windows update](/articles/black-screen-after-windows-update-troubleshooting/).

## Why this happens

- **Driver conflict with the new build:** Feature updates change kernel behavior; old display, Wi-Fi, storage, or chipset drivers that worked before can crash the new build on load.
- **Interrupted or partially applied update:** A power cut or forced shutdown mid-update leaves system files in a half-written state.
- **Low disk space during the update:** The update needs room to stage files; a nearly full drive produces corrupted installs and boot crashes.
- **Incompatible third-party antivirus or disk tools:** Kernel-level security software sometimes blocks new system files, causing boot loops.
- **Corrupted update components:** A damaged Windows Update cache can repeatedly install a broken version of the same update.
- **Firmware/BIOS mismatch:** Very old BIOS versions on some laptops conflict with newer Windows 11 builds, especially around power management and virtualization.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Boot into Safe Mode and note the stop code

Safe Mode loads only essential drivers, which usually bypasses the crashing one — and the stop code tells you where to look next.

1. Force the recovery environment: power on, and as soon as the Windows logo appears, hold the power button to shut down. Repeat twice; on the third boot you'll get **Automatic Repair**.
2. Choose **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
3. If it boots fine in Safe Mode, a third-party driver is almost certainly the cause.
4. Write down the exact **stop code** from the blue screen (e.g., DRIVER_POWER_STATE_FAILURE, SYSTEM_SERVICE_EXCEPTION) — you'll match fixes to it below.

### Fix 2: Uninstall the problematic update

If the timeline is clear — update installed, crashes began — remove it.

1. In Safe Mode (or normal Windows), open **Settings** > **Windows Update** > **Update history**.
2. Click **Uninstall updates**.
3. Select the most recent **cumulative or feature update** and click **Uninstall**.
4. Restart normally. If the crashes stop, you've confirmed the culprit.
5. Before reinstalling it later, update the driver that conflicts (Fix 3), then reinstall the update.

### Fix 3: Update your display, storage, and chipset drivers

These three driver families cause the overwhelming majority of post-update blue screens.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Expand **Display adapters**, right-click your GPU, and choose **Update driver** > **Search automatically for drivers**.
3. Do the same under **IDE ATA/ATAPI controllers** (storage) and **System devices** (chipset).
4. Better still, download the latest drivers directly from your laptop maker: [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/). Their driver packs are tested against Windows 11 builds.
5. Use the Intel Driver & Support Assistant for Intel chipset, Wi-Fi, and graphics drivers.
6. Restart and reinstall the Windows update that caused the trouble.

### Fix 4: Run SFC and DISM to repair update damage

Partially applied updates leave corrupted system files behind. These two commands repair them.

1. Open an **administrator Command Prompt**.
2. Run `sfc /scannow` and let it complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. If Windows Update was failing to even complete, this often unblocks it.

### Fix 5: Reset the Windows Update components

A corrupted update cache will keep reinstalling the same broken payload.

1. Open an **administrator Command Prompt**.
2. Run these commands one by one, pressing Enter after each:
   `net stop wuauserv`
   `net stop bits`
   `net stop cryptsvc`
3. Then run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Check **Settings** > **Windows Update** and try the update again.

### Fix 6: Use System Restore or Startup Repair from recovery

If you can't reach Windows at all, roll the system back from the recovery environment.

1. Boot into the recovery environment using the forced-shutdown method from Fix 1.
2. Go to **Troubleshoot** > **Advanced options** > **System Restore** and pick a restore point from before the update.
3. If no restore point exists, try **Startup Repair** from the same menu.
4. As a deeper fix, open **Command Prompt** in recovery and run `bootrec /fixmbr`, `bootrec /fixboot`, and `bootrec /rebuildbcd` to repair boot data the update may have damaged.

### Fix 7: Free up disk space and temporarily remove peripherals

Cramped drives and external devices cause a surprising share of update failures.

1. In Safe Mode, open **Settings** > **System** > **Storage** and run **Cleanup recommendations** — aim for at least 20 GB free.
2. Disconnect all USB devices except keyboard and mouse: docks, external drives, printers, and USB hubs can all interfere with the update process.
3. Temporarily uninstall third-party antivirus (keep Windows Security on) — kernel-level AV is a known update crasher.
4. Try the update or normal boot again.

## Closing

A blue screen after a Windows 11 update is almost never the end of the road — it's a driver conflict or a damaged update in disguise, and uninstalling the update plus refreshing your core drivers fixes it for most laptops. The key lesson: keep your display, storage, and chipset drivers current from your laptop maker's site, and give yourself 20 GB of breathing room before big updates. Once you're stable, reinstall the update — running an unpatched system to avoid crashes trades one problem for a worse one. If the same update keeps failing, check Microsoft's Windows support hub for known issues with that specific KB number.
