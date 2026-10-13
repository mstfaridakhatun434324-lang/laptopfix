---
title: "How to Stop a Windows Update in Progress in Windows 11 24H2"
slug: how-to-stop-windows-update-in-progress-in-windows-11-24h2
date: 2026-09-09
categories: ["windows-update"]
tags: ["stop windows update", "cancel update", "windows 11 24h2", "pause updates"]
description: "Need to stop a Windows update mid-install on 24H2? Learn the safe methods — pausing, stopping services — and when it's risky."
thumbnail: "/images/thumbs/how-to-stop-windows-update-in-progress-in-windows-11-24h2.webp"
faqs:
  - q: "Is it safe to stop a Windows update while it is installing?"
    a: "It depends on the phase. Stopping a download is completely safe. Interrupting the actual installation phase — especially during the restart when Windows says not to turn off the computer — risks corrupting system files and leaving the update half-applied. If the install phase has started, the safest choice is almost always to let it finish."
  - q: "What is the difference between pausing and stopping updates?"
    a: "Pausing tells Windows Update not to download or install anything new for a set period, up to five weeks, and it is fully supported and safe. Stopping means forcibly halting an update already in progress, which is what carries risk. Whenever possible, use pause to prevent future updates rather than stopping one mid-flight."
  - q: "Can I stop an update that is stuck at a percentage?"
    a: "Yes, but first verify it is actually stuck — no disk activity for over an hour — rather than just slow. A stuck download can be stopped safely by halting the update services and clearing the cache. A stuck install percentage during the restart phase is riskier; only force it off if you are certain it has been dead for hours."
  - q: "Will stopping an update damage my laptop?"
    a: "Stopping a download will not. Forcibly powering off during the install or restart phase can corrupt the component store, though Windows is designed to roll back to the pre-update state in most cases. The realistic worst case is needing to run DISM and SFC repairs or reinstall the update — annoying, but recoverable."
---

Sometimes you need to stop a Windows update mid-flight: it started at the worst possible moment, it is eating your bandwidth before a presentation, or it has been stuck at the same percentage for three hours and you have a deadline. Windows 11 24H2 gives you legitimate, safe ways to halt the process — and a few dangerous ones you should understand before using.

The key distinction is phase. An update in the download phase can be stopped with zero consequences. An update in the install phase — particularly during the "do not turn off your computer" restart — should be left alone unless it is genuinely, verifiably stuck. This guide covers both, in order of safety.

Windows Update's design assumes the machine is always available, always connected, and never in the middle of anything important — which describes no real laptop ever. The controls below exist because Microsoft knows this: pause, metered connections, and active-hours settings are not hacks, they are the intended interface for humans with schedules. Learning them is not fighting the system; it is using the system as designed, instead of letting a background service dictate your day.

## Why this happens

- **You need the laptop now.** Updates that start automatically rarely consult your schedule.
- **Bandwidth emergency.** A multi-gigabyte feature update saturating a metered or shared connection.
- **The update appears stuck** at a percentage with no disk activity for hours.
- **You want to defer a problematic update** you have heard causes issues on your hardware.
- **Battery risk.** An update started on battery with the charger nowhere nearby.
- **You need to troubleshoot** — stopping a looping update to regain control of the system.
- **Preventing an unwanted feature update** from installing while you keep security patches flowing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pause updates — the safe, official method

1. Open **Settings** > **Windows Update**.
2. Next to **Pause updates**, choose a duration from the dropdown — up to 5 weeks.
3. This stops all new downloads and installs immediately and safely, including anything queued.
4. Use this whenever your goal is "not now" rather than "stop this exact update." It is the method Microsoft supports. Details on the [Windows Update support page](https://support.microsoft.com/en-us/windows).

### Fix 2: Stop an in-progress download via services

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Right-click **Windows Update** and choose **Stop**. Also stop **Background Intelligent Transfer Service (BITS)**.
3. The download halts immediately with no risk — partial downloads are simply discarded or resumed later.
4. To prevent it restarting, set both services to **Disabled** temporarily (right-click > Properties > Startup type), and remember to set them back to **Manual**/**Automatic** later.

### Fix 3: Clear the stalled download so it does not resume

1. With the services stopped (Fix 2), open File Explorer and delete everything in `C:\Windows\SoftwareDistribution\Download`.
2. Restart the **Windows Update** and **BITS** services.
3. The update will have to download fresh if you ever allow it — the stuck partial download is gone.
4. Combine with pausing (Fix 1) if you want it to stay gone for a while. More on download problems: [fixing stuck downloads](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).

### Fix 4: Use a metered connection to block downloads

1. Go to **Settings** > **Network & internet** > **Wi-Fi** (or **Ethernet**), click your connection.
2. Turn on **Metered connection**.
3. Windows will not download most updates over a metered connection — this is a persistent, passive block.
4. Note that some critical security updates may still come through; for full control, combine with pausing. Related: [metered connection blocking fixes](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/).

### Fix 5: Force-stop a genuinely stuck install (risky — last resort)

1. Confirm it is truly stuck: zero disk activity for over an hour, percentage frozen, fans idle.
2. Hold the **power button** for ten seconds to force the laptop off. Wait thirty seconds.
3. Power on — Windows will usually detect the interrupted update and roll back to the pre-update state automatically.
4. After rollback completes, immediately pause updates (Fix 1) so it does not start again before you are ready.

### Fix 6: Recover if the forced stop caused problems

1. After the rollback, open an elevated Command Prompt and run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
2. Then run:
   `sfc /scannow`
3. Restart and check **Settings** > **Windows Update** > **Update history** for the update's status.
4. If the component store was damaged by the interruption, these two repairs fix it in most cases. For a full rebuild, see [resetting update components](/articles/how-to-reset-windows-update-components-in-windows-11-24h2/).

### Fix 7: Prevent the specific update from returning

1. Once stable, use Microsoft's **Show or Hide Updates** troubleshooter to hide the problematic update.
2. Or keep updates paused until you have time to deal with it properly.
3. When ready, install it deliberately: charger connected, peripherals disconnected, no deadline looming.
4. For feature updates specifically, the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) lets you run the upgrade on your own schedule via the Installation Assistant.

### Fix 8: Pin your feature-update target version

To stop feature updates (like 24H2/25H2) while keeping security patches flowing, pin Windows to your current feature version via the registry.

1. Press **Windows key + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` (create the key if missing).
2. Create a DWORD value named `TargetReleaseVersion` set to `1`.
3. Create a string value named `TargetReleaseVersionInfo` set to your current version (check with `winver`, e.g. `24H2`).
4. Restart. Windows Update will now offer security updates for your pinned version but not feature upgrades — revisit the setting when you are ready to move.

## Closing

Stopping a Windows update is safe when you stop a download and risky when you interrupt an install — know which phase you are in before you act. Pause updates for the "not now" cases, stop services and clear the cache for stuck downloads, and reserve the forced shutdown for updates that are verifiably dead. Then deal with the update on your terms, not its. The goal is not to never update — unpatched machines are how botnets grow — but to update on your schedule, with the charger in and the deadline past. Pause deliberately, pin the version if needed, and install big updates like appointments: planned, prepared, and uninterrupted.
