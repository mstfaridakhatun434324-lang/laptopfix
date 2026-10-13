---
title: "Windows 11 24H2 Audio Not Working? Troubleshooting Guide"
slug: windows-11-24h2-audio-not-working-troubleshooting
date: 2026-10-08
categories: ["windows-update"]
tags: ["24h2", "audio not working", "sound driver", "windows 11"]
description: "No sound after the Windows 11 24H2 update? Work through these 7 troubleshooting steps — driver rollbacks, service restarts, and enhancement fixes."
thumbnail: "/images/thumbs/windows-11-24h2-audio-not-working-troubleshooting.webp"
faqs:
  - q: "Why did my sound stop working right after the 24H2 update?"
    a: "The 24H2 update migrates audio drivers to newer versions, and that migration sometimes installs a generic driver that doesn't fully support your laptop's audio hardware, or it enables audio enhancements your hardware can't handle. The result is silence, crackling, or devices that vanish entirely. Rolling back or reinstalling the proper manufacturer driver fixes the large majority of cases."
  - q: "Should I uninstall the 24H2 update to get my sound back?"
    a: "Don't start there. Uninstalling a feature update is disruptive and only buys ten days of relief before it reinstalls. Audio problems after 24H2 are driver-level issues that survive the update itself, so fix the driver: roll it back, reinstall the manufacturer's version, or disable enhancements. Only consider removing the update if every driver-level fix has genuinely failed."
  - q: "My Bluetooth headphones stopped working after 24H2 but speakers are fine. Why?"
    a: "Bluetooth audio uses a separate driver stack from your built-in speakers, and 24H2 sometimes resets Bluetooth audio profiles or breaks the Hands-Free/A2DP profile pairing. Remove the headphones from Bluetooth settings, re-pair them fresh, and check that the Stereo (A2DP) profile — not Hands-Free — is set as the default playback device for music."
  - q: "Can Windows Update itself fix the audio problem?"
    a: "Sometimes. Microsoft ships revised audio drivers through Windows Update after major releases, so checking for updates a few weeks after 24H2 can resolve the issue automatically. But don't rely on it — the driver Windows Update offers may be the same generic one causing the problem. If a manual driver install from your manufacturer is available, prefer that."
---

The 24H2 update finished, you opened a video, and... silence. Or worse, sound that crackles, cuts out, or only works through one device. Audio breakage is one of the most common 24H2 complaints, and it's almost always a driver migration problem: the update swapped your working audio driver for one that doesn't quite fit your hardware.

The fix sequence is well established. You verify it's really a software problem, then work from the simplest driver rollback up through full reinstallation. If your 24H2 install had broader troubles beyond audio, our [24H2 black screen guide](/articles/how-to-fix-windows-11-24h2-black-screen-after-update-step-by-step/) covers the display-driver side of the same migration.

## Why this happens

- **Generic driver replaced the manufacturer driver** — 24H2's migration installs a basic Microsoft audio driver that lacks your hardware's full feature set.
- **Audio enhancements got re-enabled** — Spatial sound or enhancement flags the old driver tolerated now cause silence or distortion.
- **Driver signature or compatibility mismatch** — An old manufacturer driver that 24H2 kept can conflict with the new audio stack.
- **Audio services failed to restart** — The Windows Audio and Audio Endpoint Builder services sometimes don't come back cleanly after the upgrade.
- **Default device got reassigned** — The update can switch the default output to a disconnected HDMI monitor or disabled device.
- **Bluetooth profiles reset** — Paired audio devices lose their A2DP configuration and fall back to the low-quality Hands-Free profile.
- **Third-party audio software conflicts** — Apps like Nahimic, Waves MaxxAudio, or Dolby Access can clash with the migrated driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the basics and check the default device

Half of all "no sound" reports are a wrong default device, not a broken driver. Rule that out in two minutes.

1. Click the volume icon in the taskbar and confirm the output device listed is the one you expect (speakers, not an HDMI monitor).
2. Press Win + R, type `mmsys.cpl`, and check the Playback tab — right-click your device and choose **Set as Default Device**.
3. Test with the **Configure** and **Test** buttons right there in the Sound window.
4. Check that nothing is muted: the volume mixer (right-click the volume icon > Open volume mixer) has per-app mutes people forget.
5. If sound works here, the driver is fine — something just reassigned your default. Skip to Fix 6 to stop it happening again.

### Fix 2: Restart the Windows audio services

If the services didn't restart cleanly after 24H2, audio dies with no obvious error.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click it, and choose **Restart**.
3. Do the same for **Windows Audio Endpoint Builder**.
4. If either service refuses to start, check its dependencies — **Remote Procedure Call (RPC)** and **Windows Audio Endpoint Builder** must be running.
5. Test sound immediately; if it works, the services were the whole problem.

### Fix 3: Roll back the audio driver

The classic fix: 24H2 replaced your working driver, so put the old one back.

1. Open Device Manager (Win + X > Device Manager) and expand **Sound, video and game controllers**.
2. Right-click your audio device (Realtek, Intel SST, or similar) and choose **Properties**.
3. On the **Driver** tab, click **Roll Back Driver** if it's available, and pick the reason "previous driver worked better."
4. Reboot and test. If the button is grayed out, Windows didn't keep the old driver — continue to Fix 4.
5. After rolling back, pause driver updates temporarily so Windows Update doesn't reinstall the problematic one overnight.

### Fix 4: Install the manufacturer's audio driver fresh

When rollback isn't available, a clean install of the proper driver beats the generic one 24H2 installed.

1. Identify your audio hardware in Device Manager (e.g., Realtek ALC, Intel Smart Sound Technology).
2. Download the latest audio driver from your laptop maker's support site — Dell, HP, Lenovo, or ASUS — not a random driver site.
3. In Device Manager, right-click the audio device and choose **Uninstall device**, ticking **Attempt to remove the driver** if offered.
4. Reboot, then install the downloaded manufacturer driver and reboot again.
5. Intel-based laptops can also use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to verify chipset and SST drivers are current.

### Fix 5: Disable audio enhancements and exclusive mode

Enhancements that worked before 24H2 can break audio after the migration — this fix takes thirty seconds.

1. In `mmsys.cpl`, right-click your playback device > **Properties** > **Enhancements** tab, and tick **Disable all enhancements**.
2. On the **Advanced** tab, untick **Allow applications to take exclusive control of this device**.
3. If there's a **Spatial sound** tab, set it to **Off**.
4. Test audio. If this fixes it, re-enable enhancements one at a time to find the offender — or just leave them off.
5. Third-party enhancers (Nahimic, MaxxAudio, Dolby) should be updated or temporarily uninstalled if the problem persists.

### Fix 6: Fix Bluetooth audio profile problems

For Bluetooth devices specifically, the fix is re-pairing with the right profile.

1. Go to Settings > Bluetooth & devices, remove the problematic headphones or speaker, and re-pair it fresh.
2. In `mmsys.cpl` > Playback, make sure the **Stereo** (A2DP) entry is the default — not **Hands-Free AG Audio**, which sounds like a phone call.
3. Disable **Hands-Free Telephony** for the device in Control Panel > Devices and Printers > right-click device > Properties > Services tab.
4. Update your Bluetooth driver from the manufacturer's site — 24H2's migrated Bluetooth stack is a known weak point.
5. If audio stutters rather than disappearing, move the laptop away from USB 3.0 ports and Wi-Fi routers, which interfere with Bluetooth.

### Fix 7: Use System Restore or repair the audio stack

When nothing driver-level works, roll the system state back or repair it.

1. Check for a restore point from before the 24H2 update: search **Recovery** > **Open System Restore**.
2. Restoring to a pre-update point brings back the entire working audio configuration.
3. If no restore point exists, run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` to repair system files the migration may have damaged.
4. As a final software step, check Settings > Windows Update — Microsoft often ships revised audio drivers in the weeks after a feature release, and a [driver update delivered through Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) may resolve it automatically.
5. If audio fails identically in a Linux live USB or the BIOS beep test, it's hardware — contact the manufacturer.

## Closing

Audio loss after 24H2 is annoying but rarely serious: it's a driver migration hiccup, and the rollback-to-manufacturer-driver path fixes it for the vast majority of laptops. Work the list from the two-minute default-device check up through the clean driver install, and resist the urge to uninstall the whole feature update — the driver is the problem, and the driver is fixable. Your sound will be back well before you'd finish reinstalling Windows.
