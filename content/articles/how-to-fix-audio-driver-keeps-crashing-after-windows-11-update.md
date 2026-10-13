---
title: "How to Fix an Audio Driver That Keeps Crashing After a Windows 11 Update"
slug: how-to-fix-audio-driver-keeps-crashing-after-windows-11-update
date: 2026-09-14
categories: ["drivers"]
tags: ["audio driver crashing", "sound keeps cutting out", "realtek crash", "windows 11 update"]
description: "Audio driver crashing over and over after a Windows 11 update? Six fixes that stabilize Realtek and Intel audio, from service repair to full driver replacement."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update.webp"
faqs:
  - q: "What's the difference between crackling audio and a crashing audio driver?"
    a: "Crackling is degraded-but-continuous audio — the driver runs but produces artifacts. A crashing driver stops entirely: sound cuts out completely, the speaker icon may show a red X, and Device Manager may show the device disappearing or gaining a warning icon. Crashes point to driver instability or service failures, while crackling points to format or enhancement mismatches. The fixes overlap but the emphasis differs — crashes need driver replacement, not just settings tweaks."
  - q: "Why does the audio work for a few minutes after reboot, then die?"
    a: "That's the signature of a driver that loads correctly but crashes under sustained use — usually a memory leak, a power-management suspend that never wakes properly, or a conflict with another driver that loads later in the boot sequence. The temporary recovery after reboot is diagnostic gold: it proves the hardware and base driver work, and the failure is triggered by runtime conditions you can isolate."
  - q: "Can Windows Update keep reinstalling the bad driver after I fix it?"
    a: "Yes, and it's the most common reason this problem 'comes back.' Windows Update's automatic driver updates will happily replace your stable vendor driver with the newer-but-broken build again. After fixing the crash, exclude drivers from Windows Update via the registry policy or Group Policy, and manage audio driver updates through your laptop vendor's utility instead."
  - q: "Should I disable the audio device in BIOS as a workaround?"
    a: "Only as a last resort for a machine you need usable today — disabling onboard audio in BIOS stops the crashes but leaves you with no sound at all. A USB audio adapter is a better stopgap: it bypasses the broken onboard audio stack entirely for a few dollars while you work the real fix. Don't accept silence as the solution when the driver is fixable."
---

Sound works for ten minutes after boot, then dies. Or the speaker icon sprouts a red X at random. Or Device Manager shows your audio device vanishing and reappearing like it's haunted. An audio driver that keeps crashing after a Windows 11 update is different from merely bad-sounding audio — the driver itself is failing, and Windows is restarting it (or failing to) in a loop.

The pattern matters diagnostically. Works-after-reboot-then-dies means the driver loads fine but can't sustain operation — think power management, memory leaks, or a conflict with something that loads later. Dies instantly and never works means the driver build itself is wrong for your hardware. Either way, the update is the prime suspect: it replaced a working audio stack with one that isn't stable on your machine. We'll stabilize it from the services layer up through full driver replacement. If the symptom is distortion rather than dropouts, the [speaker crackling guide](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/) is the better fit — and if the mic is the casualty, see the [microphone fix guide](/articles/how-to-fix-microphone-not-working-on-laptop-in-windows-11-24h2/).

## Why this happens

- **The new audio driver build is unstable on your hardware.** The update's driver has a bug — often in power management or stream handling — that crashes it under normal use.
- **The Windows Audio services are failing.** The driver depends on the Windows Audio and Audio Endpoint Builder services; if the update corrupted their configuration, the driver can't stay up.
- **Power management suspends the audio device permanently.** The driver puts the codec to sleep to save power and a bug prevents wake — the classic works-after-reboot-then-dies pattern.
- **A conflicting driver loads after boot.** Bluetooth audio drivers, virtual audio cables, or conferencing app drivers can destabilize the primary audio driver once they initialize.
- **Leftover components from the old driver.** The update replaced the driver but left the old control panel app or APO (audio processing object) behind, and the version mismatch crashes the stack.
- **Corrupted system files in the audio pipeline.** The update damaged shared audio components (like AudioDG or the endpoint builder database) that every audio driver depends on.
- **The Intel SST bus driver is the actual crasher.** On Intel laptops the audio codec rides the Smart Sound Technology bus; when the SST driver crashes it takes audio down with it, while the codec driver looks innocent.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Windows Audio services properly

Stabilize the service layer the driver depends on.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click > **Restart**. Do the same for **Windows Audio Endpoint Builder**.
3. Double-click each service and set **Startup type** to **Automatic**.
4. Open the **Dependencies** tab of Windows Audio and confirm its dependency services are running too. Test for an hour.

### Fix 2: Disable power management on the audio device

Stop the sleep-that-never-wakes cycle.

1. Device Manager > **Sound, video and game controllers** > right-click your audio device > **Properties**.
2. On the **Power Management** tab (if present), uncheck **Allow the computer to turn off this device to save power**.
3. Also check **System devices** > **Intel(R) Smart Sound Technology** entries for the same tab and uncheck it there.
4. Additionally: **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** > **USB settings** > **USB selective suspend** > **Disabled** — this catches USB audio devices.

### Fix 3: Roll back or replace the audio driver

The update's driver build is the prime suspect — remove it.

1. Device Manager > right-click the audio device > **Properties** > **Driver** tab > **Roll Back Driver** if available.
2. If rollback isn't offered, **Uninstall device** with **Attempt to remove the driver for this device** checked, then restart.
3. Download the audio driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) and install it clean.
4. Restart and run audio for a sustained period — a full workday of use is the real test.

### Fix 4: Remove conflicting audio software

Strip the audio stack to its essentials.

1. **Settings** > **Apps** > **Installed apps** — look for virtual audio devices, old conferencing apps, audio enhancers, and duplicate Realtek control panels.
2. Uninstall anything audio-related you don't actively use, especially software installed around the time the crashes started.
3. In Device Manager > **Sound, video and game controllers**, disable (don't uninstall yet) any virtual or secondary audio devices for testing.
4. If stability returns, re-enable them one at a time to identify the conflict.

### Fix 5: Repair system files and the audio endpoint database

Fix corruption beneath the driver.

1. Open **Terminal (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart after both complete.
3. If crashes persist, the endpoint database may be corrupt: stop the **Windows Audio** service, delete the contents of `C:\Windows\System32\DriverStore\` — no, safer path: in **Sound settings** > **More sound settings**, remove all unused playback/recording devices, then restart the service.
4. Re-run the **Playing Audio** troubleshooter (**Settings** > **System** > **Sound** > **Troubleshoot**) to rebuild clean endpoint state.

### Fix 6: Update the Intel SST driver and block future replacements

Fix the bus driver and protect the result.

1. Device Manager > **System devices** > update every **Intel(R) Smart Sound Technology** entry (**Update driver** > **Search automatically**, or the vendor's chipset package).
2. Check for a BIOS update from your vendor mentioning audio or SST stability — install it if the notes match your symptom.
3. Once stable, exclude drivers from Windows Update (registry: `ExcludeWUDriversInQualityUpdate` = 1) so the broken build can't return.
4. Document your working driver version (see the [driver version check guide](/articles/how-to-check-driver-version-in-device-manager-in-windows-11-24h2/)) so you can spot future unwanted replacements instantly.

## Closing

A crashing audio driver is the update's driver build failing your hardware — and the fix is to stop using that build. Restart the services, kill the power-management suspends, replace the driver with the vendor's stable version, and then bar Windows Update from swapping it back. The crashes that arrived with the update leave with the driver that caused them.
