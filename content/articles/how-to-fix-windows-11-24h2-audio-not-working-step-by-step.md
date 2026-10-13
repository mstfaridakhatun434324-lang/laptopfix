---
title: "How to Fix Windows 11 24H2 Audio Not Working: Step-by-Step"
slug: how-to-fix-windows-11-24h2-audio-not-working-step-by-step
date: 2026-09-10
categories: ["windows-update"]
tags: ["24h2 audio not working", "no sound after update", "audio driver", "windows 11"]
description: "No sound after the Windows 11 24H2 update? Follow this step-by-step audio repair, from quick checks to full driver reinstallation."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-step-by-step.webp"
faqs:
  - q: "Why did the 24H2 update break my audio?"
    a: "Feature updates migrate audio drivers to the new build, and 24H2's migration sometimes installs a generic driver that does not match your laptop's audio hardware, disables enhancements the old driver needed, or leaves the old driver half-removed. The hardware is fine — the software driving it is in a broken intermediate state."
  - q: "Should I roll back 24H2 to fix audio?"
    a: "No — rollback is overkill for an audio problem. Audio issues after 24H2 are fixed by driver repair in the vast majority of cases, which takes twenty minutes versus the disruption of a full build rollback. Only consider rolling back if the audio failure is one symptom among many serious post-update problems."
  - q: "Will reinstalling the audio driver delete my settings?"
    a: "It resets audio device settings to defaults — volume levels, enhancements, and spatial sound settings for that device. Your files and everything else are untouched. Note your custom settings first if you had elaborate audio configurations, so you can reapply them after the driver is working."
  - q: "What if there is no audio device listed at all?"
    a: "Then the driver is missing entirely or the hardware is disabled. Check Device Manager with hidden devices shown, look in the BIOS for an audio toggle, and reinstall the chipset driver — audio controllers depend on it. A completely absent audio device after 24H2 is almost always a driver stack problem, not dead hardware."
---

The 24H2 update finishes, you play a video, and there is no sound. Or the sound is distorted, or the speakers work but the headphone jack does not. Audio breakage is one of the most common post-feature-update complaints because the update touches the entire audio driver stack — and on laptops with vendor-customized audio (Realtek with Waves MaxxAudio, Dolby, or similar), the migration frequently lands in a broken state.

This is a step-by-step repair in strict order. Each step is quick, safe, and either fixes the problem or narrows it down. Do not skip ahead to driver surgery before checking the simple stuff — a surprising share of "no audio after 24H2" reports end at step two.

Laptop audio is a stack of fragile agreements: Windows talks to the audio driver, the driver talks to the codec chip, and a vendor enhancement layer (MaxxAudio, Dolby, DTS) sits in the middle adjusting everything. A feature update renegotiates all of those agreements at once, and 24H2 is particularly aggressive about replacing the driver at the bottom of the stack. When one layer ends up speaking a different version than the others, the result is silence — or worse, sound that is technically present but distorted beyond recognition.

## Why this happens

- **Wrong audio driver migrated.** 24H2 installed a generic High Definition Audio driver instead of your laptop's customized Realtek/Conexant driver.
- **Audio enhancements broken.** The old driver's enhancement layer (MaxxAudio, Dolby) is incompatible with the new driver and mutes or distorts output.
- **Default output device changed.** The update switched the default to a disconnected HDMI or Bluetooth device.
- **Audio service failed to start** properly on the new build.
- **Exclusive mode or format mismatch** — the new driver negotiates a sample rate the hardware path cannot handle.
- **Driver half-migrated**, with old and new driver files conflicting.
- **BIOS or chipset driver outdated** relative to what 24H2's audio stack expects.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious — volume, mute, and output device

1. Click the **volume icon** in the taskbar and confirm the volume is up and not muted.
2. Click the **arrow** next to the volume slider (or go to **Settings** > **System** > **Sound**) and verify the correct output device is selected — not a disconnected monitor or old Bluetooth device.
3. Play the test tone in **Settings** > **System** > **Sound** > your output device.
4. If the wrong device was selected, you are done. Updates change the default output more often than anyone expects.

### Fix 2: Run the audio troubleshooter

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** and run **Audio**.
2. Answer its questions honestly — it checks services, devices, and enhancements automatically.
3. Apply its recommended fixes and test again.
4. The troubleshooter resolves service and configuration issues quickly. If the troubleshooter itself reports it cannot run, see [fixing a broken update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/). Microsoft documents the audio pipeline on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 3: Restart the Windows Audio services

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click, and choose **Restart**. Do the same for **Windows Audio Endpoint Builder**.
3. Set both services' **Startup type** to **Automatic** if they are not already.
4. Test audio. Services that failed to start cleanly on the new build are a classic 24H2 issue.

### Fix 4: Disable audio enhancements

1. Go to **Settings** > **System** > **Sound**, click your output device, and open its properties.
2. Turn off **Audio enhancements** (or set to Off/Device Default Effects).
3. In the same panel, try changing the **Format** (sample rate) to 24-bit, 48000 Hz if the current setting produces distortion.
4. Vendor enhancement layers broken by the driver migration are a top cause of silence and distortion — disabling them is both a fix and a diagnostic.

### Fix 5: Roll back the audio driver

1. Open **Device Manager**, expand **Sound, video and game controllers**.
2. Right-click your audio device (Realtek, Conexant, or similar), choose **Properties** > **Driver** tab.
3. Click **Roll Back Driver** if available and follow the prompts, then restart.
4. This restores the pre-24H2 driver that was working. If rollback is grayed out, continue to the next fix. For related driver-update failures, see [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/).

### Fix 6: Uninstall and reinstall the audio driver cleanly

1. In **Device Manager**, right-click the audio device and choose **Uninstall device**. Check **Attempt to remove the driver for this device**.
2. Restart the laptop — Windows will install a basic driver on boot. Test audio with it.
3. For the full vendor driver, download it from your laptop maker's support site, or update the chipset and audio stack via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
4. Install the vendor driver, restart, and test again. A clean reinstall resolves the half-migrated driver states that rollback cannot.

### Fix 7: Check BIOS settings and update the chipset driver

1. Restart into the BIOS/UEFI (usually **F2** or **Del** during boot) and confirm the onboard audio/HD Audio controller is **Enabled**.
2. While there, note your BIOS version — check the maker's support site for a newer one mentioning audio or 24H2 compatibility.
3. Back in Windows, install the latest **chipset driver** for your laptop — the audio controller hangs off the chipset, and 24H2's audio stack is sensitive to old chipset drivers.
4. Restart and do a final audio test across speakers, headphones, and Bluetooth to confirm everything works.

### Fix 8: Roll the audio stack back with System Restore

If driver surgery has not worked, restore the entire system state — drivers, services, and configuration — to before 24H2 touched it.

1. Search for **Create a restore point**, open **System Protection**, and click **System Restore**.
2. Choose a restore point dated before the 24H2 update (the update usually creates one automatically).
3. Complete the restore and restart — your files are untouched, but the audio stack returns to its working state.
4. Before retrying 24H2, update the audio and chipset drivers first so the migration starts from healthy components.

## Closing

Audio failure after 24H2 is a driver migration problem, not a hardware problem, and it yields to methodical repair: verify output selection, restart the audio services, kill broken enhancements, then roll back or cleanly reinstall the driver. Work the steps in order and the sound comes back — usually well before you reach the BIOS. Audio failures feel personal — a silent laptop is a broken laptop in daily use — but they are among the most fixable post-update problems. The stack is small, the layers are knowable, and one of the eight fixes above restores it in nearly every case. Test with speakers, headphones, and Bluetooth before declaring victory.
