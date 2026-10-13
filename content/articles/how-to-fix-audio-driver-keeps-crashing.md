---
title: "How to Stop Your Audio Driver From Crashing Repeatedly"
slug: "how-to-fix-audio-driver-keeps-crashing"
date: "2026-09-30"
categories: ["drivers"]
tags: ["audio driver", "crashing", "realtek", "windows 11", "sound"]
description: "Audio driver crashing repeatedly? Stop the cycle of silence and restarts with driver cleanups, enhancement fixes, and conflict removal."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing.webp"
faqs:
  - q: "Why does my audio driver keep crashing?"
    a: "The typical causes are a corrupted audio driver installation, conflicts with audio enhancement software, a Windows update that installed an incompatible driver, or a misbehaving app taking exclusive control. A clean driver reinstall from the manufacturer's support page resolves most recurring crashes."
  - q: "How do I stop the audio service from crashing?"
    a: "Restart the Windows Audio services and set them to Automatic startup. Then disable audio enhancements and exclusive mode, which are common crash triggers. If crashes continue, reinstall the audio driver cleanly and remove third-party audio software that hooks into the output chain."
  - q: "Can Discord or games crash my audio driver?"
    a: "Yes. Voice chat apps, game overlays, and streaming software request exclusive audio access and unusual sample rates that can destabilize a fragile driver. If crashes happen only during calls or gaming, disable exclusive mode and test with those apps closed to confirm the conflict."
  - q: "Should I use the manufacturer or Microsoft audio driver?"
    a: "For troubleshooting, test both. The manufacturer's driver enables all features but has more failure modes. The generic High Definition Audio driver is simpler and very stable. If crashes stop with the generic driver, the manufacturer's version was the problem, and you can wait for an updated release."
---

Sound works, then it does not. The audio cuts out mid-video, the speaker icon shows a red X, and a restart brings it back until the next crash. An audio driver that keeps crashing turns your laptop into a machine you cannot trust for calls, meetings, or media.

Recurring audio crashes have a short list of causes: a corrupted driver, enhancement software fighting the driver, exclusive-mode conflicts with apps, or a bad driver version from Windows Update. Each has a specific fix. The related [post-update audio crash guide](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/) covers the update-triggered variant.

Work through these fixes in order. The goal is not just to restore sound once, but to break the crash cycle permanently.

## Why this happens

- **A corrupted audio driver installation:** Partial updates leave mismatched driver files that crash under specific conditions.
- **Audio enhancement software conflicts:** Enhancements from the manufacturer and from Windows can fight each other.
- **Exclusive-mode app conflicts:** Voice and game apps grabbing exclusive control can crash a fragile driver.
- **A bad driver version from Windows Update:** Newer is not always better; regressions in audio drivers are common.
- **Sample rate mismatches:** Apps requesting unusual sample rates can destabilize the driver.
- **Failing Windows Audio services:** The user-mode services the driver depends on can crash independently.
- **Hardware beginning to fail:** Rare, but dying audio codecs produce crashes that no driver fixes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the Windows Audio services properly

When the driver crashes, its supporting services often stay in a broken state. A proper restart of the whole audio service chain clears the immediate failure.

1. Press Windows + R, type services.msc, and press Enter.
2. Restart the Windows Audio service.
3. Restart the Windows Audio Endpoint Builder service.
4. Set both services' startup type to Automatic.
5. Test audio for at least fifteen minutes before declaring victory.

### Fix 2: Disable audio enhancements and exclusive mode

Enhancements and exclusive mode are the two most common crash triggers in the audio pipeline. Disabling both is a fast, reversible test that isolates the driver itself.

1. Open the Sound control panel and open your playback device's Properties.
2. On the Enhancements tab, tick Disable all enhancements.
3. On the Advanced tab, uncheck both exclusive-mode options.
4. Set the default format to 16-bit, 44100 Hz as a conservative baseline.
5. Click OK and test with the apps that previously triggered crashes.

### Fix 3: Cleanly reinstall the audio driver

A standard update over a corrupted install often preserves the corruption. A full uninstall with driver deletion followed by a fresh manufacturer install breaks the cycle.

1. Open Device Manager and expand Sound, video and game controllers.
2. Uninstall the audio device, ticking Delete the driver software.
3. Restart the laptop.
4. Install the audio driver from your laptop maker's support page, not Windows Update.
5. Restart again and monitor for crashes over a full day. If [Realtek-specific faults](/articles/realtek-audio-driver-not-working-windows-11/) persist, their dedicated fixes go deeper.

### Fix 4: Remove third-party audio software

Equalizers, virtual audio cables, and audio routers hook deep into the driver chain. When two of them disagree, the driver is what crashes.

1. Open Settings, then Apps, and list audio-related software.
2. Uninstall equalizers, virtual cables, and audio enhancers you do not need.
3. Keep at most one audio utility and make sure it is current.
4. Restart and test the previously crashing scenario.
5. Reintroduce tools one at a time if you need them, testing stability after each.

### Fix 5: Roll back to a known-good driver version

If crashes began with a specific driver version, the version itself is the bug. Rolling back to the previous release is the correct response, not endlessly reinstalling the broken one.

1. Open the audio device's Properties in Device Manager.
2. On the Driver tab, click Roll Back Driver if available.
3. If greyed out, download the older driver from the manufacturer's archive.
4. Install the older version and block the bad one from reinstalling.
5. Watch for a fixed release before updating again.

### Fix 6: Test with the generic High Definition Audio driver

The generic Microsoft driver is the ultimate isolation test for audio crashes. It lacks features but also lacks the failure modes of complex OEM drivers.

1. In Device Manager, update the audio device driver manually.
2. Choose Let me pick from a list and select High Definition Audio Device.
3. Restart and use the laptop normally for a day or two.
4. If crashes stop, the OEM driver was at fault; report it to the manufacturer.
5. Stay on the generic driver until a fixed OEM version appears.

### Fix 7: Repair system files with SFC and DISM

The audio stack depends on Windows system files that malware, disk errors, or failed updates can damage. When crashes persist across every driver version, the operating system's own audio components may be corrupt, and no driver reinstall will help until the underlying files are repaired.

1. Open an elevated Command Prompt by right-clicking Start and choosing Terminal (Admin).
2. Run sfc /scannow and wait for the scan to complete fully.
3. If it reports corruption it could not fix, run DISM /Online /Cleanup-Image /RestoreHealth.
4. Restart after DISM completes and run the SFC scan once more to confirm.
5. Test audio stability for a full day of normal use before declaring victory.

## Closing

An audio driver that keeps crashing is telling you something specific: corrupted files, a software conflict, or a bad version. The clean reinstall plus enhancement and exclusive-mode cleanup breaks the cycle in the great majority of cases. System file repair with SFC and DISM is the final software step when every driver has been exhausted. Reserve hardware suspicion for crashes that survive all of that, and document which fix worked so the next crash is a five-minute job instead of another long evening of troubleshooting. Keep the working driver installer archived as well.
