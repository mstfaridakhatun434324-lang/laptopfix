---
title: "No Sound? How to Fix Realtek Audio Not Working in Windows 11 24H2"
slug: how-to-fix-realtek-audio-not-working-in-windows-11-24h2
date: 2026-09-02
categories: ["drivers"]
tags: ["realtek audio", "windows 11 24h2", "no sound", "audio driver"]
description: "Realtek audio stopped working after the Windows 11 24H2 update? Follow this step-by-step guide to restore sound on your laptop, from driver rollback to a clean reinstall."
thumbnail: "/images/thumbs/how-to-fix-realtek-audio-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my Realtek audio break after the 24H2 update?"
    a: "The 24H2 update frequently replaces your vendor-tuned Realtek driver with a generic Microsoft audio driver, or installs a mismatched Realtek version that cannot talk to the audio codec. The speakers then show as working in Device Manager while producing no sound. Reinstalling the manufacturer's Realtek package fixes the mismatch in most cases."
  - q: "Should I use the driver from Windows Update or my laptop maker?"
    a: "Use your laptop maker's Realtek driver. Vendor packages include customizations for your specific speakers, microphone array, and audio enhancements that generic drivers lack. Windows Update drivers often fix one machine and break another. Grab the package from Lenovo, Dell, HP, ASUS, or Acer support for your exact model."
  - q: "My microphone stopped working too — is that related?"
    a: "Usually yes. The Realtek driver handles both output and input on most laptops, so a broken driver silences speakers and the microphone together. Fixing the driver with the steps below typically restores both. If the mic stays dead after sound returns, see our guide on [Realtek microphone problems on Windows 11](/articles/how-to-fix-realtek-microphone-not-working-on-windows-11/)."
  - q: "Do I need to restart after reinstalling the audio driver?"
    a: "Yes, always restart after an audio driver change. The Windows Audio service binds to the driver at boot, and a restart clears stale driver state from memory. Skipping the restart is one of the most common reasons a reinstall appears to fail even though the driver is actually fixed."
---

No sound, no error, no obvious reason. You installed the Windows 11 24H2 update, and now your laptop speakers are silent — YouTube plays mutely, system sounds are gone, and the volume slider moves without doing anything. The speaker icon shows no red X, Device Manager reports the Realtek device as working properly, and yet: silence.

This disconnect between "driver looks fine" and "no audio" is the signature of the 24H2 Realtek problem. The update replaces your vendor-tuned Realtek HD Audio driver with a generic Microsoft one, or installs a Realtek build that does not match your laptop's audio codec. The device enumerates, Windows thinks audio is fine, and no sound ever reaches the speakers. The repair is methodical driver work — rollback first, clean reinstall second, vendor package third — and it restores sound in the vast majority of cases.

## Why this happens

- **24H2 replaced the vendor driver with a generic one.** The Microsoft generic HD Audio driver enumerates the device but cannot drive your codec correctly.
- **Mismatched Realtek build installed.** Windows Update pulled a Realtek version built for a different codec revision.
- **Old audio enhancements conflicting.** Surviving APO effects (Dolby, Waves, Nahimic) from the old install crash the new driver.
- **Audio service stuck in a bad state.** The Windows Audio service is wedged after the update and never binds to the new driver.
- **Default output device changed.** 24H2 can switch the default output to a disconnected HDMI or Bluetooth device.
- **Exclusive mode or sample-rate mismatch.** Apps holding the audio device in exclusive mode block all other sound.
- **Corrupted driver store entry.** A half-installed driver from an interrupted update breaks the whole stack.
- **BIOS or EC audio initialization change.** Rare, but firmware updates bundled with 24H2 can alter codec power sequencing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the correct output device is selected

Before touching drivers, rule out the trivial cause. Click the speaker icon in the taskbar, then click the arrow next to the volume slider to see output devices. Select your laptop's **Speakers (Realtek Audio)** explicitly. The 24H2 update loves to switch the default to a phantom HDMI monitor output or an old Bluetooth headset. Play a test sound. If sound returns, you are done in thirty seconds — no driver work required.

### Fix 2: Restart the Windows Audio services

Press **Windows + R**, type `services.msc`, and press Enter. Find **Windows Audio**, right-click it, and choose **Restart**. Do the same for **Windows Audio Endpoint Builder**. Then open Task Manager, go to **Processes**, find **audiodg.exe** (the audio device graph), and end the task — it restarts automatically. This clears the wedged audio pipeline that 24H2 updates commonly leave behind, and it is the fix when sound worked briefly after the update and then died.

### Fix 3: Roll back the Realtek driver

Open **Device Manager**, expand **Sound, video and game controllers**, right-click **Realtek Audio** (it may be listed as Realtek High Definition Audio), and open **Properties > Driver**. If **Roll Back Driver** is available, click it and choose the "previous version worked better" reason. Restart. This restores the pre-24H2 driver in about a minute. If rollback is greyed out — common when Windows Update did a full driver replacement rather than an upgrade — continue to the clean reinstall.

### Fix 4: Clean-reinstall the Realtek driver

In Device Manager, right-click the Realtek device and choose **Uninstall device**, checking **Attempt to remove the driver for this device** if offered. This deletes the broken driver package from the driver store. Restart — Windows will install its generic driver on boot. Test the sound. If the generic driver produces sound, the Realtek package was the problem, and you can either keep the generic driver or install the vendor package for full features. If there is still no sound, continue — the issue runs deeper.

### Fix 5: Install the manufacturer's Realtek package

Go to your laptop maker's support site — [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), or [HP support](https://support.hp.com/us-en) — find your exact model, and download its **Realtek audio driver** for Windows 11. Run the installer and restart. Vendor packages include the codec-specific tuning and the audio enhancement software (MaxxAudio, Dolby, Nahimic) your speakers were designed around. This is the definitive fix for most 24H2 Realtek failures. If the driver itself is present but misbehaving in other ways, our [Realtek audio driver troubleshooting guide](/articles/realtek-audio-driver-not-working-windows-11/) covers additional failure modes. If Windows Update keeps replacing it, you can pause updates or use the "show or hide updates" troubleshooter to block the bad driver version.

### Fix 6: Disable audio enhancements and exclusive mode

Right-click the speaker icon, choose **Sound settings**, scroll to your output device, and open **Properties**. Under **Enhancements**, check **Disable all enhancements**. Then go to the classic **Sound** control panel (search "sound" in the taskbar), open the device's properties, and on the **Advanced** tab uncheck **Allow applications to take exclusive control of this device**. Stale enhancement APOs from the old driver install are a classic cause of silence with a "working" driver, and exclusive-mode grabs by conferencing apps block everything else. Test after each change. If audio cuts out or the driver crashes repeatedly rather than staying silent, see our guide on [audio drivers that keep crashing on Windows 11](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/).

### Fix 7: Check for a BIOS update and do a full power drain

If nothing in software helps, check the manufacturer's support site for a **BIOS update** — audio codec initialization is handled by firmware, and vendors ship fixes for post-24H2 audio issues. Flash it with the charger connected. As a last resort, shut down, unplug, remove the battery if possible, and hold the power button for 30 seconds to reset the embedded controller that sequences power to the codec. If the speakers work in the BIOS or with a Linux live USB but never in Windows, the problem is definitely driver-side — repeat Fix 5. If they work nowhere, the codec or speaker wiring may need service.

## Closing

Realtek audio failures after the 24H2 update look mysterious but follow a pattern: the update broke the driver stack, and rebuilding it restores sound. Work the sequence — output device, audio services, rollback, clean reinstall, vendor package — and restart after every driver change. Once sound is back, keep the vendor driver pinned and be cautious about letting Windows Update replace audio drivers automatically.
