---
title: "How Do I Fix Laptop Speakers Not Working on Windows 11?"
slug: how-do-i-fix-laptop-speakers-not-working
date: 2026-09-24
categories: ["drivers"]
tags: ["laptop speakers", "no sound windows 11", "speaker fix", "audio output", "realtek"]
description: "Speakers silent on Windows 11? This focused guide walks through output selection, driver repair, and hardware checks until sound returns."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-speakers-not-working.webp"
faqs:
  - q: "Why is there no sound on my Windows 11 laptop?"
    a: "The most common causes on Windows 11 are: the wrong output device selected (HDMI or Bluetooth instead of speakers), the speakers disabled in Sound settings, a corrupted audio driver after an update, or the Windows Audio service failing. Work through output selection first — it resolves the issue in a surprising number of cases — then move to driver repair."
  - q: "How do I set my laptop speakers as the default device in Windows 11?"
    a: "Go to Settings → System → Sound, and under Output select your Speakers device. For the classic control panel, run mmsys.cpl, right-click the Playback tab background, enable Show Disabled Devices, then right-click your speakers → Set as Default Device. The classic panel is more reliable for revealing hidden or disabled devices."
  - q: "Why do my speakers work in BIOS but not in Windows?"
    a: "BIOS beep tests bypass Windows entirely, so sound in BIOS proves the speakers and amplifier hardware work. The problem is then 100% in Windows: the audio driver, the Windows Audio service, or output routing. Focus all effort on driver reinstallation and service checks — no hardware repair is needed."
  - q: "Do I need the manufacturer's audio driver or is Windows' enough?"
    a: "For basic sound, Windows' generic driver suffices. But laptop speakers are tuned with OEM-specific processing — without the manufacturer's Realtek package, audio often sounds thin, quiet, or distorted, and features like MaxxAudio or DTS disappear. For proper speaker sound, always install the OEM audio driver."
---

Windows 11 changed enough audio plumbing — new Settings layouts, the quick-settings volume flyout, per-app volume handling — that speaker problems have their own flavor on this OS. The underlying causes are the classics (routing, drivers, services), but the places you check them moved. This guide is Windows 11-specific: every path, every panel, every quirk.

The approach is the same disciplined chain: confirm sound is being produced, confirm it's routed to the speakers, confirm the driver is healthy, then consider hardware. On Windows 11, the routing step deserves extra attention because the OS is aggressive about switching outputs.

## Why this happens

- **Windows 11 auto-switched the output:** Plugging in HDMI or Bluetooth once can permanently reroute audio away from speakers.
- **Speakers disabled after driver update:** Updates reshuffle the device list and sometimes leave speakers disabled.
- **Generic driver replaced OEM audio:** Windows Update's driver lacks the speaker tuning, producing silence or awful sound.
- **Windows Audio service failure:** The service crashes or hangs, particularly after updates or sleep/wake cycles.
- **Per-app mute in volume mixer:** Individual apps muted in the new Windows 11 volume mixer while system sounds work.
- **Spatial sound / enhancement conflicts:** Windows Sonic or third-party spatial processing crashing the output pipeline.
- **Fast Startup audio state corruption:** The audio subsystem resumes in a broken state from hybrid shutdown.
- **Hardware failure:** Blown speakers or damaged connections, usually with a history of drops or distortion first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Select the speakers in Windows 11's sound settings

1. Click the **volume icon** in the taskbar, then click the **arrow (>)** next to the volume slider to open the output switcher.
2. Select **Speakers** — explicitly, even if it looks selected already. Reselecting forces the routing to rebuild.
3. Go to **Settings → System → Sound** and confirm the Output device shows your speakers.
4. Play audio and watch the volume meter under Output — if it animates, Windows is producing sound and the problem is downstream (driver or hardware).

### Fix 2: Use the classic Sound panel to find hidden devices

1. Press **Win + R**, type `mmsys.cpl`, press Enter.
2. Right-click empty space in the Playback tab → check **Show Disabled Devices** and **Show Disconnected Devices**.
3. Right-click your speakers → **Enable** if disabled, then **Set as Default Device** and **Set as Default Communication Device**.
4. Click **Properties → Advanced** and test different default formats; set **24 bit, 48000 Hz** for maximum compatibility.

### Fix 3: Check the Windows 11 volume mixer thoroughly

1. Go to **Settings → System → Sound → Volume mixer**.
2. Verify the **system volume** is up and each app's individual slider is up and unmuted.
3. Note the **output device dropdown per app** — Windows 11 lets each app use a different output. An app set to a disconnected device plays silence.
4. Reset any app showing an unexpected output device back to Default.

### Fix 4: Restart audio services and disable Fast Startup

1. Press **Win + R**, type `services.msc`: restart **Windows Audio** and **Windows Audio Endpoint Builder**, both set to **Automatic**.
2. Disable **Fast Startup** (Control Panel → Power Options → Choose what the power buttons do) to stop corrupted audio states surviving shutdowns.
3. Shut down fully, wait 10 seconds, power on, and retest.
4. Fast Startup is a notorious source of "worked yesterday, silent today" audio issues on Windows 11.

### Fix 5: Reinstall the OEM audio driver

1. Download your model's audio driver from the manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. In **Device Manager → Sound, video and game controllers**, uninstall the audio device with "delete the driver software" checked.
3. Install the OEM package as Administrator, reboot, and test with the built-in Camera-app-free approach: just play a YouTube video.
4. OEM drivers restore the speaker tuning profiles that generic drivers lack — the difference is often dramatic, as noted in the broader [speaker troubleshooting guide](/articles/troubleshoot-laptop-speakers-not-working/).

### Fix 6: Disable enhancements and spatial sound

1. In **Settings → System → Sound**, select your speakers and set **Audio enhancements** to **Off** as a test.
2. Set **Spatial sound** to **Off** — Windows Sonic and Dolby processing can break the output chain on some drivers.
3. If sound returns, the enhancement pipeline was crashing; keep it off until an OEM driver update, or leave it off permanently.
4. This mirrors the diagnostic used for [audio drivers that keep crashing](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/), since the root cause is often identical.

### Fix 7: Test hardware outside Windows

1. Restart and run your manufacturer's **built-in diagnostics** (F12 boot menu on Dell, F2 on Lenovo) — most include a speaker test that bypasses Windows.
2. Alternatively, boot a Linux live USB and play audio. Sound in Linux = Windows problem confirmed. Silence = hardware.
3. Listen for faint buzzing or crackling from the speaker grilles at max volume — any noise means the amplifier works.
4. Check for a stuck headphone jack sensor: plug/unplug wired headphones several times and blow out the jack.

### Fix 8: Update BIOS and check for hardware failure

1. Check the manufacturer's support page for **BIOS updates** mentioning audio fixes — the audio codec is initialized by firmware.
2. If speakers distort at all volumes even after clean OEM driver installs, the speakers are likely blown — replacement parts are cheap and the repair is usually just a bottom-panel removal.
3. Document the failure (photos of Device Manager, notes on tests) before contacting support — it speeds warranty claims enormously.
4. If you need to escalate beyond these steps, your laptop manufacturer's support site documents the official audio troubleshooting flow for your exact model.

## Closing

Windows 11 speaker silence is a routing problem first, a driver problem second, and a hardware problem a distant third. Reselect the output, reveal hidden devices, reinstall the OEM driver — sound returns in the large majority of cases right there. If you went through the full sequence, you now also have a tested recovery playbook: the next time an update silences the speakers, you'll know within minutes whether it's routing or drivers, instead of starting the diagnosis over.
