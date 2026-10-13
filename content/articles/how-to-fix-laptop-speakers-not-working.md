---
title: "How to Fix Laptop Speakers Not Working in Windows 11"
slug: "how-to-fix-laptop-speakers-not-working"
date: "2026-09-26"
categories: ["drivers"]
tags: ["speakers", "audio", "windows 11", "sound", "troubleshooting"]
description: "No sound from your laptop speakers? Work through output settings, audio drivers, and enhancements to restore sound step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-speakers-not-working.webp"
faqs:
  - q: "Why is there no sound coming from my laptop speakers?"
    a: "The most common causes are the wrong output device selected, muted or low volume, a corrupted audio driver, or audio enhancements causing a conflict. Check the volume mixer and default output device first. If those are correct, reinstall the audio driver from the manufacturer's support page."
  - q: "How do I set my laptop speakers as the default device?"
    a: "Right-click the speaker icon in the taskbar and open Sound settings. Under Output, select the laptop's internal speakers. In the classic Sound panel, you can also right-click the speakers on the Playback tab and choose Set as Default Device and Set as Default Communication Device."
  - q: "Can a Windows update break laptop speakers?"
    a: "Yes. Audio driver updates through Windows Update are a frequent cause of sudden silence. If sound stopped right after an update, roll back the audio driver in Device Manager or reinstall the manufacturer's audio driver. Our [audio driver crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) covers the related failure mode."
  - q: "What if headphones work but speakers do not?"
    a: "That usually means the audio hardware and core driver are fine, and the problem is routing or the speaker-specific configuration. Check the default output device, disable audio enhancements, and look for a stuck headphone-jack detection switch. Some laptops need the Realtek control panel to reassign the output correctly."
---

You press play, the progress bar moves, and silence comes out. The video plays fine, the app shows audio levels bouncing, but your laptop speakers produce nothing. It is one of those problems that makes you question everything, because every indicator says sound should be working.

In practice, dead laptop speakers come down to routing (sound going to the wrong device), the audio driver, or enhancements and effects breaking the output chain. Actual dead speaker hardware is rare and usually announces itself with distortion first. Crackling variants are covered in our [speaker crackling guide](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/).

Start with the two-minute output and volume checks, then move to the driver repairs that fix the stubborn cases.

## Why this happens

- **Wrong output device selected:** Windows may be sending audio to a disconnected Bluetooth device or monitor.
- **Muted or zeroed volume:** Per-app mutes in the volume mixer are easy to set accidentally and hard to notice.
- **Corrupted audio driver:** The Realtek or Intel audio driver can break after Windows updates.
- **Audio enhancements conflicting:** Enhancements and spatial sound processing can silence output on some hardware.
- **Headphone jack stuck in plugged state:** A worn jack can fool the laptop into thinking headphones are connected.
- **Disabled audio device:** The speakers can end up disabled in the Sound control panel.
- **BIOS or hardware mute:** Some laptops have a hardware mute tied to function keys or the BIOS.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the output device and volume mixer

Most no-sound cases end here. Windows loves to route audio to whatever device was connected last, including Bluetooth headphones sitting in another room.

1. Click the speaker icon in the taskbar and confirm the output device is the laptop speakers.
2. Open the volume mixer and check that neither the master nor the app is muted.
3. Raise the volume above fifty percent for testing.
4. In Sound settings, run the audio troubleshooter for the speaker device.
5. Disconnect Bluetooth devices temporarily to rule out silent routing.

### Fix 2: Restart the Windows Audio services

The audio stack runs as system services, and they can wedge. Restarting them is the audio equivalent of turning it off and on again, and it takes thirty seconds.

1. Press Windows + R, type services.msc, and press Enter.
2. Find Windows Audio in the list, right-click it, and choose Restart.
3. Do the same for Windows Audio Endpoint Builder.
4. If either service is not running, start it and set its startup type to Automatic.
5. Test sound immediately after both services are running.

### Fix 3: Disable audio enhancements

Enhancements like bass boost and virtual surround process every sound before it reaches the speakers. On some hardware, they corrupt the stream into silence.

1. Open the classic Sound panel and go to the Playback tab.
2. Right-click the speakers, choose Properties, and open the Enhancements tab.
3. Tick Disable all enhancements and click OK.
4. On the Advanced tab, also test with different default format sample rates.
5. Restart the audio app and test again.

### Fix 4: Reinstall the audio driver

When settings are correct but silence persists, the driver is the prime suspect. A clean reinstall from the manufacturer's package fixes corruption that updates leave behind.

1. Open Device Manager and expand Sound, video and game controllers.
2. Right-click the audio device (often Realtek) and choose Uninstall device with driver deletion.
3. Restart the laptop and let Windows reinstall a basic driver.
4. Download the audio driver from your laptop maker's support page and install it.
5. Restart once more and verify sound through the speakers.

### Fix 5: Check the headphone jack for a stuck switch

The headphone jack contains a tiny mechanical switch that tells Windows headphones are plugged in. Lint or wear can jam it, muting the speakers permanently.

1. Look into the headphone jack with a flashlight for lint or debris.
2. Gently clean it with a dry cotton swab or compressed air.
3. Plug headphones in and out several times to exercise the switch.
4. Check the Sound panel to see whether the headphone device appears and disappears correctly.
5. If the jack is physically damaged, a USB audio adapter is a cheap workaround.

### Fix 6: Test with the generic High Definition Audio driver

Manufacturer audio drivers add features but also add failure modes. The generic Microsoft driver is a useful diagnostic: if sound returns with it, the OEM driver was the problem.

1. Open Device Manager and open the audio device's Properties.
2. Choose Update driver, then Browse my computer, then Let me pick.
3. Select High Definition Audio Device from the list and install it.
4. Restart and test the speakers.
5. If sound works, decide whether to keep the generic driver or troubleshoot the OEM one. Guidance for [Realtek-specific issues](/articles/realtek-audio-driver-not-working-windows-11/) can help with the latter.

### Fix 7: Check balance, mono audio, and spatial sound settings

Sometimes the speakers are technically working but the sound is routed strangely: all audio pushed to one channel by a dragged balance slider, mono downmixing enabled in accessibility settings, or spatial sound processing sending the stream nowhere. These settings hide in different panels, so they are easy to miss during normal troubleshooting.

1. Open Settings, then Accessibility, then Audio, and check whether mono audio is turned on.
2. Open the Sound control panel, open the speaker Properties, and check the Levels tab for the balance control.
3. Center the balance sliders if one channel is at zero.
4. On the Spatial sound tab, set the format to Off as a diagnostic test.
5. Retest with stereo content you know well, listening for both channels.
6. Leave spatial sound off unless you specifically use it with compatible content.

## Closing

Silent laptop speakers are usually a routing or driver problem, not dead hardware. The output device check and the driver reinstall resolve the vast majority of cases in minutes. Save the hardware suspicion for when the speakers stay silent across drivers, operating systems, and a known-good external output.
