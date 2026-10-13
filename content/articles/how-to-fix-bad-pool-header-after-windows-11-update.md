---
title: "How to Fix BAD_POOL_HEADER After a Windows 11 Update"
slug: how-to-fix-bad-pool-header-after-windows-11-update
date: 2026-10-02
categories: ["windows-errors"]
tags: ["bsod", "memory", "windows-update"]
description: "BAD_POOL_HEADER blue screen after updating Windows 11? It's a memory-pool bug — here's how to find the bad driver and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-bad-pool-header-after-windows-11-update.webp"
faqs:
  - q: "What does BAD_POOL_HEADER mean in Windows 11?"
    a: "Windows manages memory in 'pools,' and this stop code means a driver or process corrupted a pool header — the bookkeeping data Windows uses to track memory allocations. It's almost always a buggy driver writing where it shouldn't, and it frequently appears right after a Windows update swaps driver versions."
  - q: "Why did BAD_POOL_HEADER start after a Windows update?"
    a: "Feature and quality updates replace drivers — network, storage, audio, and antivirus filter drivers especially. If the new version has a memory-management bug, or if it conflicts with a leftover piece of the old driver, pool corruption crashes begin immediately after the update."
  - q: "Can RAM cause BAD_POOL_HEADER?"
    a: "Yes. Faulty RAM corrupts pool data in ways that look exactly like a driver bug. If driver updates and rollbacks don't stop the crashes, run Windows Memory Diagnostic (mdsched.exe) or MemTest86 — bad memory is the second most common cause after drivers."
  - q: "How do I find which driver causes BAD_POOL_HEADER?"
    a: "Enable Driver Verifier for third-party drivers (run verifier.exe, choose standard settings for non-Microsoft drivers), reboot, and let it crash — Verifier forces the buggy driver to blue-screen immediately with its name visible. Alternatively, analyze the minidump in WinDbg with the !analyze -v command."
---
You installed a Windows 11 update, restarted, and now the blue screens have started — BAD_POOL_HEADER, over and over. The timing isn't a coincidence. Updates shuffle drivers around, and when a new driver version mismanages memory, this is the stop code you get.

The fix is a driver hunt: find which driver the update broke or replaced, and either roll it back, update it properly, or remove it. Here's the systematic way to do it.

## Why this happens

- **Buggy driver installed by the update** — Windows Update replaced a stable driver (often network, audio, or storage) with a version that corrupts memory pools.
- **Driver conflict after the update** — remnants of the old driver clash with the new one, especially with antivirus filter drivers and VPN clients.
- **Corrupted driver files** — the update's driver payload didn't install cleanly, leaving half-written driver binaries.
- **Faulty RAM** — physical memory errors corrupt pool headers; the update timing can be coincidental.
- **Failing storage** — disk errors corrupt the paging file or driver files loaded from disk.
- **Third-party antivirus filter drivers** — these hook deep into memory management and are notorious BAD_POOL_HEADER sources after OS updates change the rules underneath them.
- **Overclocked or unstable memory settings** — XMP profiles or manual RAM tuning that was borderline-stable can tip over after an update changes memory handling.

## How to fix it

Work through these in order. Start with the update-related steps since the timing points there.

### Fix 1: Roll back the driver Windows Update changed

The fastest win when crashes track an update.

1. Press **Windows + X** > **Device Manager**.
2. Think about what the update touched — but start with the usual suspects: expand **Network adapters**, **Sound, video and game controllers**, and **Storage controllers**.
3. Right-click each recently-touched device > **Properties** > **Driver** tab, and check the **Driver Date** — anything dated within the last few days is suspect.
4. Click **Roll Back Driver** where available, choosing "a previous version worked better" as the reason.
5. Restart and use the laptop for a day. If crashes stop, block that driver from reinstalling: **Settings** > **Windows Update** > **Advanced options** > **Optional updates** — don't install the driver version that broke things.

### Fix 2: Uninstall the problematic Windows update

If rollbacks don't help, remove the update itself.

1. Go to **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Sort by installed date and uninstall the most recent quality update, then restart and test for a day or two.
3. If crashes continue, uninstall the most recent driver updates listed there too.
4. Once stable, pause updates for 2–3 weeks (**Windows Update** > **Pause updates**) to avoid the immediate return of the bad payload.

### Fix 3: Update drivers properly from the manufacturer

Replace Windows Update's generic drivers with the real ones.

1. Identify your laptop's exact model (**Windows + R** > `msinfo32` > **System Model**).
2. Download fresh drivers from the manufacturer's support site: chipset, network (Wi-Fi and Ethernet), audio, and storage — these are the BAD_POOL_HEADER usual suspects.
3. Install them one at a time, restarting between each, and test for crashes after each install. This isolates which driver was the problem.
4. For Intel network and Bluetooth, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) provides current, stable versions directly.

### Fix 4: Use Driver Verifier to catch the culprit

Driver Verifier stresses drivers until the buggy one crashes with its name showing.

1. Press **Windows + R**, type `verifier.exe`, and press Enter.
2. Choose **Create standard settings**, then **Automatically select unsigned drivers** — or **Select driver names from a list** and tick all non-Microsoft drivers.
3. Click **Finish** and restart. Use the laptop normally; Verifier will force a blue screen quickly when the bad driver misbehaves, and this time the screen names it.
4. Once you have the driver name, boot into Safe Mode (**Settings** > **System** > **Recovery** > **Advanced startup**), open an admin Command Prompt, and run `verifier /reset` to turn Verifier off.
5. Then update, roll back, or uninstall the named driver.

### Fix 5: Test the RAM

Rule out hardware memory faults.

1. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. For a thorough test, run MemTest86 from a USB drive (boot via the F12/Esc boot menu) for at least one full pass — ideally overnight for multiple passes.
3. If errors appear, reseat the RAM modules (power off, unplug, remove bottom panel, pop sticks out and back in firmly).
4. Retest with one stick at a time if you have two — replace the stick that errors. Also try disabling XMP in the BIOS (**F2** at boot > memory settings) to rule out unstable memory overclocking.

### Fix 6: Remove third-party antivirus temporarily

Antivirus filter drivers are a classic BAD_POOL_HEADER source after OS updates.

1. Uninstall your third-party antivirus via **Settings** > **Apps** > **Installed apps** — don't just disable it, since filter drivers load even when "disabled."
2. Restart and test for a few days with Windows Security (Microsoft Defender) handling protection — it's fully capable as a temporary or permanent replacement.
3. If crashes stop, check the antivirus vendor's site for an updated version explicitly supporting your Windows 11 build before reinstalling.
4. VPN clients with network filter drivers deserve the same treatment — uninstall and test.

### Fix 7: Repair system files and check the disk

Clean up any corruption the update left behind.

1. Open **Terminal (Admin)** (**Windows + X**) and run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
2. When it finishes, run `sfc /scannow`.
3. Then check the disk: `chkdsk C: /f` (schedule at restart if prompted).
4. Restart and monitor. If BAD_POOL_HEADER persists after all of this, the remaining suspects are the motherboard or a deeply buried driver — at which point a **Reset this PC** (**Settings** > **System** > **Recovery**) with cloud download is the pragmatic next step.

## Closing

BAD_POOL_HEADER after a Windows 11 update is the OS telling you a driver fumbled memory management — and the update is what handed it the ball. Roll back what the update changed, get proper manufacturer drivers, and let Driver Verifier name the culprit if you're stuck. Hardware memory faults are the backup theory, so don't skip the RAM test. For the step-by-step checklist version of this same repair path, see [BAD_POOL_HEADER step by step](/articles/how-to-fix-bad-pool-header-step-by-step/), and if your crashes involve pool corruption with a different name, [special pool detected memory corruption](/articles/how-to-fix-special-pool-detected-memory-corruption-step-by-step/) covers its close cousin.
