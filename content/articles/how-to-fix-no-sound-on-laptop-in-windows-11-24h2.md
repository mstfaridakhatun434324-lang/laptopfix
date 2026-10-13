---
title: "Fix Total Audio Loss on Windows 11 24H2"
slug: how-to-fix-no-sound-on-laptop-in-windows-11-24h2
date: 2026-09-06
categories: ["drivers"]
tags: ["no sound", "audio", "windows 11 24h2", "realtek", "troubleshooting"]
description: "No sound at all on Windows 11 24H2? Restore laptop audio with these driver, service, and settings fixes for complete silence."
thumbnail: "/images/thumbs/how-to-fix-no-sound-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why did sound stop working after the Windows 11 24H2 update?"
    a: "The 24H2 update replaces audio drivers and resets the audio stack, which breaks the driver binding for many Realtek and Intel audio devices. Reinstalling the manufacturer's audio driver and restarting the Windows Audio service restores sound in most cases. Run the built-in audio troubleshooter first; it automates the service restart and basic driver checks."
  - q: "What does the red X on the speaker icon mean?"
    a: "It means Windows cannot find a working audio output device — the audio driver has failed, the device is disabled, or the audio service is stopped. Device Manager will show the audio device with a warning icon or missing entirely, pointing to a driver problem."
  - q: "Can BIOS settings cause no sound in Windows?"
    a: "Rarely, but yes. If the onboard audio controller is disabled in the BIOS, Windows has no audio hardware to drive. This sometimes happens after a BIOS update resets settings. Re-enabling HD Audio in the BIOS brings the device back. The option is usually under Advanced or Integrated Peripherals, labeled HD Audio or Onboard Audio."
  - q: "Why do I have sound in some apps but not others?"
    a: "Per-app volume settings in the Windows volume mixer can mute individual applications while the system sounds fine. Right-click the speaker icon, open the volume mixer, and check that the silent app is not muted or set to zero volume. Browsers in particular have per-tab mute states that persist independently of the system mixer."
---

Total silence from a laptop is disorienting — no system sounds, no video audio, no meeting chatter, just a speaker icon that may or may not show a red X. On Windows 11 24H2 this failure surged because the update reworks audio driver handling, and plenty of machines came out the other side with a broken audio stack.

Complete audio loss has a narrower set of causes than partial problems. It is almost always one of four things: the audio driver is broken or missing, the Windows Audio service is stopped, the output device is disabled or misrouted, or the audio hardware is disabled at firmware level. Each has a fast, decisive test.

Work through these fixes in order. They move from the thirty-second checks to driver surgery, and they will either restore your sound or prove the audio hardware has failed.

The 24H2 update deserves a specific callout: it migrates audio drivers to a new driver framework, and on some systems that migration silently fails — the old driver is removed but the new binding never completes. Device Manager may even show the audio device as working while no sound plays. That is why the clean driver reinstall below deletes the driver software rather than just updating it; the binding has to be rebuilt from zero.

## Why this happens

- **Audio driver broken by the 24H2 update:** The update's driver migration leaves many Realtek and Intel audio devices with a non-functional driver binding.
- **Windows Audio service stopped:** If the Audiosrv service is not running, no application can produce sound regardless of drivers.
- **Output device disabled or wrong default:** The correct device may be disabled while Windows routes audio to a disconnected HDMI or Bluetooth device.
- **Corrupted audio enhancements:** Third-party enhancements and spatial sound processing can crash the audio engine on 24H2.
- **BIOS onboard audio disabled:** A firmware reset can disable the HD audio controller, removing the hardware from Windows entirely.
- **Conflicting audio drivers:** Multiple audio driver packages fighting over the same device can leave it in a failed state.
- **Hardware failure of the audio codec:** Rare, but the onboard codec chip can fail, usually after liquid damage or a power surge.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows audio troubleshooter

The built-in troubleshooter detects the common 24H2 audio breakages automatically and is worth the two minutes.

1. Open **Settings > System > Sound** and scroll to **Advanced**.
2. Click **Troubleshoot** next to **Output** and follow the prompts.
3. Let it apply any recommended fixes, including driver reinstalls.
4. Test audio before moving on — it resolves the simple cases outright.

### Fix 2: Check the output device and volume mixer

Windows may be playing sound perfectly — just to the wrong device. Verify routing before touching drivers.

1. Open **Settings > System > Sound** and confirm the correct speakers are selected under **Output**.
2. Click the speaker icon in the taskbar and check the volume is up and not muted.
3. Right-click the speaker icon, open **Volume mixer**, and confirm no app is muted.
4. If the correct device is missing from the list, continue to the driver fixes. Related routing issues affect [USB headsets](/articles/how-to-fix-usb-headset-not-working-on-windows-11/) the same way.

### Fix 3: Restart the Windows Audio services

A stopped audio service produces total silence with healthy drivers. Restarting it is instant when it works.

1. Press **Win + R**, type **services.msc**, and press Enter.
2. Find **Windows Audio**, right-click, and choose **Restart**.
3. Do the same for **Windows Audio Endpoint Builder**.
4. Set both services' **Startup type** to **Automatic** and test sound.

### Fix 4: Reinstall the audio driver

This is the core fix for 24H2 audio loss. The update breaks the driver binding, and a clean reinstall rebuilds it.

1. Open **Device Manager** and expand **Sound, video and game controllers**.
2. Right-click the Realtek or Intel audio device and choose **Uninstall device**, checking **Delete the driver software**.
3. Restart — Windows reinstalls a base driver. Test sound.
4. If the base driver works, install the latest audio driver from your laptop vendor for full functionality. For audio that cuts in and out rather than vanishing, see the [audio crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/).

### Fix 5: Disable audio enhancements

Enhancement processing crashes the audio engine on some 24H2 systems. Disabling it restores the raw audio path.

1. Right-click the speaker icon, choose **Sounds**, and open the **Playback** tab.
2. Double-click your speakers, go to the **Enhancements** tab, and check **Disable all enhancements**.
3. On the **Advanced** tab, uncheck **Allow applications to take exclusive control**.
4. Click OK and test. Microsoft documents audio troubleshooting steps on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Check for disabled devices and BIOS audio

A disabled device at either the Windows or firmware level is invisible to every fix above.

1. In the Sound control panel's Playback tab, right-click empty space and enable **Show Disabled Devices**, then enable your speakers.
2. Restart into the BIOS and confirm **Onboard Audio** or **HD Audio** is **Enabled**.
3. Save and boot into Windows, then recheck Device Manager for the audio device.
4. If the device now appears, install its driver.

### Fix 7: Test with a USB audio device

A USB headset or USB sound card bypasses the onboard codec entirely, proving whether the hardware is dead.

1. Plug in any USB audio device and set it as the default output.
2. If USB audio works, the onboard codec or its driver path has failed — the driver reinstall above is your best shot.
3. If even USB audio fails, the Windows audio stack itself is corrupt; consider an in-place repair install.
4. Persistent codec failure after driver repair means a hardware fault needing service.

### Fix 8: Use System Restore to undo the breakage

If sound died immediately after an update and nothing else works, rolling the system back is faster than further surgery.

1. Search for **Create a restore point**, open System Protection, and click **System Restore**.
2. Choose a restore point dated **before** the sound stopped working.
3. Complete the wizard and let the system restart.
4. If sound returns, pause Windows updates briefly and research the specific update before allowing it again.

## Closing

Total audio loss on 24H2 is a driver or service problem in the vast majority of cases — the update breaks the binding, and reinstalling the driver plus restarting the audio service rebuilds it. Only when USB audio also fails, or the device is absent from both Device Manager and the BIOS, should you conclude the hardware is at fault.
