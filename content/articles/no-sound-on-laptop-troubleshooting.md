---
title: "No Sound on Your Laptop? The Complete Troubleshooting Guide"
slug: no-sound-on-laptop-troubleshooting
date: 2026-09-14
categories: ["drivers"]
tags: ["no sound", "audio not working", "realtek", "speakers"]
description: "Laptop speakers suddenly silent? Work through output selection, driver fixes, and service restarts to get your audio back."
thumbnail: "/images/thumbs/no-sound-on-laptop-troubleshooting.webp"
faqs:
  - q: "Why is there no sound on my laptop even though nothing is muted?"
    a: "The most common cause is Windows routing audio to the wrong output — a disconnected Bluetooth device, an HDMI monitor, or a USB headset Windows still thinks is attached. Right-click the speaker icon, open Sound settings, and check the Output device dropdown. If it shows anything other than your laptop's speakers, switch it back. Driver updates are the second most common cause."
  - q: "How do I fix no sound after a Windows update?"
    a: "Open Device Manager, expand Sound, video and game controllers, right-click your audio device, and use Roll Back Driver to revert the update — this fixes most post-update audio loss. If rollback isn't available, uninstall the device (checking delete driver software), restart, and install the audio driver from your laptop manufacturer's support page instead of taking the Windows Update version."
  - q: "Should I disable audio enhancements?"
    a: "Yes, as a diagnostic step at minimum. Audio enhancements (Dolby, DTS, Nahimic, Windows' own 'Enhance audio') process the signal through extra driver layers, and when any layer breaks, you get silence or distortion. Turn them off in Settings > System > Sound > your output device. If sound returns, the enhancement layer was the problem — leave it off or update the enhancement software."
  - q: "No audio device is detected at all — what now?"
    a: "If Device Manager shows no audio device even with hidden devices shown, the audio controller may be disabled in BIOS or the driver stack is thoroughly broken. Check BIOS for an onboard-audio/HD-audio enable option, then reinstall the chipset driver (which includes the audio bus) followed by the audio driver from your manufacturer. If the device never appears, suspect hardware failure of the audio codec."
---

Silence from a laptop that played fine yesterday is disorienting — video calls go mute, media plays dead, and the volume slider mocks you at 100. The reassuring fact: total audio loss is a software problem in the large majority of cases, and it usually traces to one of three things — Windows sending sound to the wrong device, a driver update breaking the audio stack, or the Windows Audio service itself stalling.

The diagnostic order matters: verify the output device and volume first (thirty seconds), then the driver (five minutes), then the services and enhancements. For crackling or distorted audio rather than silence, see [fixing crackling sound](/articles/how-to-fix-crackling-sound-on-laptop-after-windows-11-update/); for the Realtek-specific driver mess, see [Realtek audio driver fixes](/articles/realtek-audio-driver-not-working-windows-11/).

## Why this happens

- **Wrong output device selected**: Windows routes audio to a disconnected Bluetooth headset, HDMI monitor, or USB device instead of the speakers.
- **Audio driver updated or corrupted**: Windows Update's audio drivers are a leading cause of sudden silence.
- **Windows Audio service stalled**: The AudioSrv service can hang, especially after sleep/wake cycles, muting everything.
- **Audio enhancements breaking the chain**: Dolby, DTS, Nahimic, or Windows' enhancement layer crashes silently and takes output with it.
- **Exclusive mode conflicts**: An app grabs exclusive control of the audio device and doesn't release it.
- **Muted at a hidden layer**: Per-app volume mixer, browser tab mute, or the manufacturer's utility muted output outside the main slider.
- **Audio disabled in BIOS**: Rare, but BIOS updates can toggle onboard audio off.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the output device and volume layers

The thirty-second check that solves a third of cases.

1. Click the speaker icon in the taskbar (or press **Win + Ctrl + V** — wait, the correct shortcut is clicking the Quick Settings volume icon) and confirm the output device listed is your laptop's **Speakers**, not a Bluetooth device, monitor, or headset.
2. Click the **>** arrow next to the volume slider in Quick Settings to see all outputs and switch to Speakers explicitly.
3. Right-click the speaker icon > **Open volume mixer** and check that neither the system nor your specific app (browser, media player) is muted or at zero — the mixer has per-app sliders the main control doesn't show.
4. Check physical mute: many laptops have a mute F-key or button — press it twice and watch the on-screen indicator.
5. Unplug ALL audio devices — USB headsets, HDMI cables, Bluetooth audio — then retest. Windows clings to removed outputs surprisingly often.

### Fix 2: Run the audio troubleshooter

Let Windows attempt the standard repairs first.

1. Open **Settings** > **System** > **Sound** and scroll to **Advanced**, then click **Troubleshoot common sound problems** (or **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Audio** > **Run**).
2. Select your speakers when asked which device to diagnose.
3. Apply whatever fixes it suggests — it commonly restarts the audio service and resets enhancements.
4. When it finishes, play a test sound immediately: **Settings** > **System** > **Sound** > your speakers > **Test**.
5. If the troubleshooter reports it couldn't identify the problem, continue — manual driver work is next.

### Fix 3: Restart the Windows Audio services

For audio that died after sleep or a long uptime.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click > **Restart**. Do the same for **Windows Audio Endpoint Builder**.
3. Double-click **Windows Audio**, set **Startup type** to **Automatic**, and confirm the service status is **Running**.
4. Also check **Remote Procedure Call (RPC)** is running — the audio service depends on it.
5. Test sound. If audio dies again after every sleep, the root cause is likely the driver (Fix 4), not the service.

### Fix 4: Roll back or reinstall the audio driver

The heavy hitter for post-update silence.

1. Press **Win + X** > **Device Manager** > **Sound, video and game controllers**, right-click your audio device (Realtek, Intel Smart Sound, or similar) > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is available, use it — this reverses the update that most likely killed your sound.
3. If not available: right-click > **Uninstall device**, check **Attempt to remove the driver** if offered, restart, and let Windows install its inbox HD Audio driver. Test — the generic driver is plain but reliable.
4. For the permanent fix, download the audio driver from your manufacturer's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) rather than accepting Realtek generics or Windows Update versions.
5. After installing, play audio from two different sources (a local file and a browser video) to confirm both the system mixer and app layers work.

### Fix 5: Disable audio enhancements

Strip the processing chain down to the raw driver.

1. Open **Settings** > **System** > **Sound**, click your speakers/output device.
2. Turn **Enhance audio** **Off**.
3. Scroll to **Advanced** > **More sound settings** to open the classic dialog, select your speakers > **Properties** > **Enhancements** tab, and check **Disable all enhancements**.
4. On the **Advanced** tab, uncheck both **Exclusive mode** options (**Allow applications to take exclusive control**) — exclusive-mode grabs are a classic silent-killer.
5. Click OK, restart the audio-playing app, and test. If sound returns, re-enable enhancements one at a time to identify the broken layer.

### Fix 6: Check BIOS and the audio controller's presence

When no audio device exists at all.

1. In **Device Manager**, click **View** > **Show hidden devices** and re-expand **Sound, video and game controllers**. A greyed-out audio device means it's disabled — right-click > **Enable device**.
2. If there's truly no audio device, restart into BIOS/UEFI and look for **Onboard Audio**, **HD Audio**, or **Audio Controller** under Advanced/Devices — ensure it's **Enabled**.
3. Back in Windows, reinstall the **chipset driver** first (it provides the bus the audio codec hangs off), then the audio driver from your manufacturer.
4. Check **Settings** > **System** > **Sound** again — the output device list should now include Speakers.
5. If the device never appears anywhere, the audio codec chip itself may have failed — USB audio adapters are a cheap workaround while you arrange repair.

### Fix 7: Repair system files and reset the audio stack

The last software resort.

1. Open an elevated terminal and run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. If sound is still absent, the nuclear-but-safe option: **Settings** > **System** > **Recovery** > **Reset this PC** > **Keep my files** — this reinstalls Windows and the full driver stack while preserving personal files.
3. Before resetting, back up anything irreplaceable anyway — "keep my files" is reliable but not infallible.
4. After the reset, install the manufacturer audio driver before letting Windows Update touch audio.
5. Test thoroughly before reinstalling third-party audio software (equalizers, virtual cables), which are common re-breakers.

## Closing

No-sound troubleshooting rewards the boring order: output device, volume layers, service restart, driver. Most people jump straight to reinstalling drivers and miss that Windows was faithfully playing audio to a Bluetooth headset sitting in a drawer. Check the routing first, fix the driver second, and silence becomes a ten-minute problem.
