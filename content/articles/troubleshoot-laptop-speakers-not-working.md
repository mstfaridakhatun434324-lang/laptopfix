---
title: "Laptop Speakers Not Working? Troubleshoot Every Cause"
slug: troubleshoot-laptop-speakers-not-working
date: 2026-09-21
categories: ["drivers"]
tags: ["laptop speakers", "no sound", "speakers not working", "audio troubleshooting", "realtek"]
description: "No sound from your laptop speakers? Work through every cause systematically — from muted outputs to driver reinstalls to hardware failure."
thumbnail: "/images/thumbs/troubleshoot-laptop-speakers-not-working.webp"
faqs:
  - q: "Why do my headphones work but laptop speakers don't?"
    a: "Headphones and internal speakers use separate output paths in the audio driver. When headphones work but speakers don't, the audio system is fundamentally healthy — the problem is isolated to the speaker output: wrong default device selection, disabled speakers in Sound settings, a driver quirk affecting only the speaker path, or failed speaker hardware. This is actually good news because it narrows the diagnosis enormously."
  - q: "How do I know if my laptop speakers are physically broken?"
    a: "Physical failure signs include: no sound from speakers across Windows, Safe Mode, and BIOS beep tests; crackling or distortion at all volumes that a driver reinstall doesn't fix; and speakers that cut in and out when you move the lid or press near the speaker grilles. If speakers fail identically in a Linux live USB, it's hardware."
  - q: "Can Windows updates break laptop speakers?"
    a: "Yes — audio driver updates are a frequent culprit. Windows Update may install a generic audio driver that doesn't properly drive your laptop's specific speaker configuration, resulting in silence or terrible quality. Rolling back to the OEM driver from the laptop manufacturer's support page is the standard fix."
  - q: "Why is there a red X on my speaker icon?"
    a: "A red X means Windows detects no working audio output device at all. The audio driver has failed to load, the audio device is disabled in Device Manager or BIOS, or the Windows Audio service isn't running. Start by checking Device Manager for the audio device and the Services panel for Windows Audio."
---

No sound from laptop speakers is a top-ten Windows complaint, and it has an unusually wide range of causes — which is exactly why random guessing fails. The symptom is identical whether the fix is a two-second unmute or a driver reinstall. Systematic troubleshooting is the only approach that works without wasting an afternoon.

The diagnostic logic is simple: verify sound should play, verify it's routed to the speakers, verify the driver is healthy, then suspect hardware. Each step below moves one level deeper, and you'll usually find the break long before the hardware tests.

## Why this happens

- **Wrong default playback device:** Sound is routing to HDMI, Bluetooth, or a disconnected USB device instead of the speakers.
- **Speakers muted or volume at zero:** Per-app or per-device mute states that aren't obvious from the taskbar icon.
- **Audio driver corrupted:** The driver loads but can't drive the speaker output path correctly.
- **Windows Audio service stopped:** The core audio service crashed or failed to start, silencing everything.
- **Speakers disabled in Sound settings:** The device is present but manually disabled, hiding it from normal view.
- **Driver update broke speaker configuration:** Generic drivers lacking OEM speaker tuning produce silence or garbage.
- **BIOS audio disabled:** The onboard audio codec is switched off at firmware level.
- **Failed speaker hardware:** Blown speakers or damaged wiring, usually after drops or liquid exposure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious — volume, mute, and output device

1. Click the taskbar speaker icon and confirm volume is up and not muted — then click the **arrow next to the volume slider** to see the output device list.
2. Select **Speakers** (your internal audio device), not HDMI, not Bluetooth, not a USB device.
3. Open **Settings → System → Sound → Volume mixer** and check that your app and the system sounds aren't individually muted.
4. Play the Windows test sound. If the volume meter animates but you hear nothing, sound is routing somewhere wrong or the speakers aren't responding — continue.

### Fix 2: Run the audio troubleshooter

1. Go to **Settings → System → Sound** and click **Troubleshoot** under the output section, or run it from **Settings → System → Troubleshoot → Other troubleshooters → Audio**.
2. Let it complete and apply any fixes, then restart even if it reports no problems.
3. The troubleshooter restarts audio services and resets device states — quick, harmless, and occasionally sufficient.
4. If it says "audio device is disabled," that's your answer: continue to Fix 3.

### Fix 3: Enable the speakers in Sound settings

1. Press **Win + R**, type `mmsys.cpl`, and press Enter to open the classic Sound panel.
2. Right-click in the empty space of the Playback tab and check **Show Disabled Devices** and **Show Disconnected Devices**.
3. If your speakers appear grayed out, right-click → **Enable**, then right-click again → **Set as Default Device**.
4. Test again. Disabled-by-accident speakers are embarrassingly common after driver updates shuffle device lists.

### Fix 4: Restart the Windows Audio services

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click → **Restart**. Do the same for **Windows Audio Endpoint Builder**.
3. Set both **Startup type** to **Automatic** if they aren't already.
4. If the services won't stay running, that's a deeper system problem — run `sfc /scannow` in an admin Terminal to check for corrupted system files.

### Fix 5: Clean-reinstall the OEM audio driver

1. Download the audio driver for your exact model from the manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. In **Device Manager → Sound, video and game controllers**, uninstall the audio device, checking "delete the driver software."
3. Install the downloaded package as Administrator and reboot.
4. This is the fix for most post-update speaker failures, where Windows replaced tuned OEM audio with a generic driver — the same root cause behind [crackling speakers](/articles/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update/).

### Fix 6: Test with headphones and check the jack sensor

1. Plug in wired headphones. If they produce sound, the audio pipeline works and only the speaker path is broken.
2. Unplug and check whether Windows switches back to speakers — a stuck headphone-jack sensor can make Windows believe headphones are still connected, permanently muting the speakers.
3. Blow compressed air into the headphone jack and plug/unplug a few times to free a stuck sensor switch.
4. In the Realtek control panel, look for jack detection settings and disable front-panel jack detection as a test.

### Fix 7: Check BIOS and test outside Windows

1. Enter **BIOS/UEFI** and verify onboard audio is **Enabled**.
2. Boot a Linux live USB and test the speakers there. Sound in Linux with silence in Windows proves a Windows driver problem beyond doubt.
3. Silence in Linux too means hardware failure — the speakers, their wiring, or the codec chip.
4. Also test the built-in speaker test if your BIOS has one (many Dell/Lenovo diagnostics include it) — this bypasses the OS entirely. The [Realtek driver guide](/articles/realtek-audio-driver-not-working-windows-11/) covers driver-side depth if Linux points back at Windows.

### Fix 8: Diagnose speaker hardware failure

1. Listen closely at high volume for any faint crackle or buzz from the speaker grilles — any sign of life means the wiring works and the driver is the issue.
2. Press gently around the speaker areas while playing audio; sound that cuts in and out indicates loose wiring.
3. Check for distortion at all volumes that survives driver reinstalls — blown speakers distort consistently.
4. Speaker replacement on most laptops is straightforward (bottom panel, a few screws, one connector) and parts are cheap — but run the manufacturer's built-in hardware diagnostics before ordering.

## Closing

Speaker silence is a routing problem until proven otherwise: right device, enabled, unmuted, healthy driver. Walk the chain in order and the sound comes back — or you'll know with certainty that the speakers themselves need replacing. Either outcome is a win: a working fix, or a confident hardware diagnosis instead of endless guessing.
