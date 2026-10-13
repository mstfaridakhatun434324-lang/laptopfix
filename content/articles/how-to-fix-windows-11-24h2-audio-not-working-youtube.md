---
title: "No Sound After the Windows 11 24H2 Update? Fix Your Audio Now"
slug: how-to-fix-windows-11-24h2-audio-not-working-youtube
date: 2026-09-24
categories: ["windows-update"]
tags: ["audio not working", "24h2", "no sound", "windows 11", "driver"]
description: "24H2 killed your laptop's audio? From driver rollbacks to sample-rate fixes, here's the ordered sequence that restores sound."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-youtube.webp"
faqs:
  - q: "Why does the 24H2 update break audio that worked fine before?"
    a: "24H2 changes the audio stack and replaces audio drivers during the upgrade. If the new inbox driver conflicts with your hardware (common with Intel Smart Sound Technology and certain Realtek codecs), or the migration corrupts the driver state, output devices vanish or go silent. It's a driver-migration failure, not broken speakers."
  - q: "My audio device disappeared from Device Manager after 24H2 — is the hardware dead?"
    a: "No — a missing device in Device Manager after an upgrade almost always means the driver failed to migrate, not hardware failure. The hardware is fine; Windows just has no working driver bound to it. Reinstalling the manufacturer's audio driver brings it back in nearly all cases."
  - q: "Should I use Windows Update or the manufacturer for the audio driver fix?"
    a: "The manufacturer, every time. Windows Update's audio drivers lag behind and may reinstall the same problematic version. Get the 24H2-era driver from Dell/HP/Lenovo support (or Intel/Realtek directly) for your exact model — those are tested against the new audio stack."
  - q: "Can a Windows update really cause crackling and distortion rather than silence?"
    a: "Yes — that's actually the more common 24H2 audio bug. Sample-rate mismatches and audio-enhancement incompatibilities in the new stack produce crackling, popping, or robotic distortion while the device otherwise 'works.' The enhancement toggle and format changes in the fixes below target exactly this."
---

You updated to 24H2, rebooted, hit play — and silence. Or worse: crackling, popping, robotic distortion where your audio used to be. The speakers worked yesterday; the update changed the software between you and them. This is one of 24H2's most reported regressions, and it's fixable in the large majority of cases without rolling back the entire update.

The culprits are specific: Intel Smart Sound Technology (SST) driver conflicts, Realtek codec migration failures, audio enhancements that break under the new stack, and sample-rate mismatches. The sequence below goes from the 30-second checks to full driver replacement, in the order that resolves most cases fastest. For the broader 24H2 issue landscape, see [24H2 known issues step by step](/articles/how-to-fix-windows-11-24h2-known-issues-step-by-step/).

Quick triage first: right-click the speaker icon → check that the correct output device is selected and volume is up. Upgrades sometimes switch the default to a phantom HDMI device. If that's all it was, you're done in ten seconds.

## Why this happens

- **Intel SST driver conflict**: The most documented 24H2 audio bug — specific SST driver versions clash with the new stack. Intel's Driver and Support Assistant delivers the fixed SST driver directly.
- **Realtek driver migration failure**: The upgrade replaced a working Realtek driver with a broken inbox version. The manufacturer's Realtek package — not the inbox one — is the tested fix.
- **Audio enhancements incompatible**: Enhancement DSP that worked on 23H2 distorts or silences under 24H2. Disabling enhancements is also the fastest test for distinguishing crackling from silence.
- **Sample-rate mismatch**: The new stack defaults to a format the driver mishandles, producing crackling. Dropping to 16-bit 44100 Hz resolves the format-specific variants.
- **Default device switched**: The upgrade reassigns default output to a disconnected HDMI or dock device. This ten-second check resolves a real share of dead-audio reports.
- **Audio service startup failure**: Windows Audio services occasionally fail to start post-upgrade. Setting both audio services to Automatic prevents the recurrence.
- **BIOS/firmware audio hooks**: Some laptops need a BIOS update for 24H2-era audio routing. BIOS changelogs mentioning audio are worth reading before flashing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check output device, volume, and the audio troubleshooter

The embarrassingly simple fixes first — they resolve a real share of cases. The embarrassingly simple fixes first — they resolve a real share of cases.

1. Click the speaker icon → verify the correct output device (not a phantom HDMI) is selected and volume is up.
2. Settings → System → Sound → confirm the right device under Output.
3. Settings → System → Troubleshoot → Other troubleshooters → run **Playing Audio**.
4. If the troubleshooter reports fixed, test with a video — many 'dead audio' cases end here.
5. Check the per-app volume mixer too — upgrades sometimes mute individual apps while the master stays up.

### Fix 2: Restart the Windows Audio services

Post-upgrade service startup failures are quick to clear. Post-upgrade service startup failures are quick to clear.

1. Win + R → `services.msc`.
2. Restart **Windows Audio** and **Windows Audio Endpoint Builder** (right-click → Restart).
3. Set both Startup types to **Automatic** if they aren't.
4. Test audio. If it works now, the upgrade simply failed to start them — a reboot or two usually makes it stick.
5. If the services were set to Manual, something changed them — check for tuning software that touches services.

### Fix 3: Disable audio enhancements

The top fix for crackling/distortion specifically. The top fix for crackling and distortion specifically.

1. Settings → System → Sound → click your output device → **Advanced**.
2. Turn **Audio enhancements** OFF.
3. Also try changing the format (e.g., 24-bit 48000 Hz → 16-bit 44100 Hz) — some 24H2 bugs are format-specific.
4. Test. Enhancement-related distortion typically vanishes immediately.
5. Test each format change for a full minute — some distortion only appears after the buffer pattern settles. Crackling that survives the enhancement toggle has a few more causes — sample-rate handling, DPC latency, speaker wear — covered in our [crackling sound guide for 24H2](/articles/how-to-fix-crackling-sound-on-laptop-in-windows-11-24h2/).

### Fix 4: Roll back or update the audio driver (manufacturer version)

The core fix for driver-migration failures. The core fix for driver-migration failures.

1. Device Manager → Sound, video and game controllers → right-click your audio device → Properties → Driver → **Roll Back Driver** (if available).
2. If rollback isn't available or doesn't help: download the latest audio driver from your laptop manufacturer's support site for your exact model.
3. Install it, reboot, and retest.
4. Intel-based systems: also check Intel SST drivers via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
5. Download the driver before uninstalling anything — you do not want to hunt for it on a silent machine.

### Fix 5: Fully remove and reinstall the audio stack

When rollback/update leaves a corrupted hybrid state. When rollback and update leave a corrupted hybrid state.

1. Device Manager → uninstall the audio device, checking **Delete the driver software** if offered.
2. Also uninstall Intel Smart Sound Technology entries under System devices if present (same delete-driver option).
3. Reboot — Windows installs its inbox drivers.
4. Then install the manufacturer's latest audio + SST drivers over the inbox ones. Test after each layer.
5. Reboot between each layer — stacked driver installs without reboots create the hybrid states you are trying to escape.

### Fix 6: Check BIOS updates and 24H2-specific patches

Some audio regressions need firmware or a follow-up KB, not just drivers. Some audio regressions need firmware or a follow-up KB, not just drivers.

1. Check your manufacturer's support site for a BIOS update mentioning 24H2 or audio fixes.
2. Check the 24H2 known-issues dashboard for audio items marked Resolved — install the named KB from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Keep Windows Update current; audio-stack fixes ship in cumulative updates.
4. Retest after each layer — firmware and KB fixes resolve the stubborn cases.
5. BIOS updates that mention audio often fix the Intel SST handshake specifically — read the changelog.

### Fix 7: Roll back 24H2 as the last resort

If the audio hardware worked on 23H2 and nothing above restores it. If the audio hardware worked on 23H2 and nothing above restores it.

1. Settings → System → Recovery → **Go back** (within 10 days of the upgrade).
2. Your files are preserved; the system returns to 23H2 with working audio.
3. Pause feature updates while waiting for the documented audio fix.
4. Retry 24H2 after the dashboard marks your audio issue Resolved — with fresh manufacturer drivers ready. Broader context: [24H2 known issues](/articles/how-to-fix-windows-11-24h2-known-issues-step-by-step/).
5. After rollback, export your working driver versions — they are your known-good baseline for the next 24H2 attempt.

## Closing

24H2 audio failures are driver-stack failures, and driver-stack failures yield to method: correct output device, restarted services, disabled enhancements, manufacturer drivers, full stack reinstall, then firmware and KBs. Silence after an update is a software problem with a software fix — work the ladder and the sound comes back. Related guides: [24H2 known issues step by step](/articles/how-to-fix-windows-11-24h2-known-issues-step-by-step/) and [24H2 known issues](/articles/how-to-fix-windows-11-24h2-known-issues-step-by-step/).
