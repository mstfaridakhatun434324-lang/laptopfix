---
title: "Fix Windows 11 24H2 Audio Not Working on an HP Laptop"
slug: how-to-fix-windows-11-24h2-audio-not-working-on-hp-laptop
date: 2026-09-23
categories: ["windows-update"]
tags: ["24h2 audio", "no sound", "hp laptop", "audio driver"]
description: "No sound after the 24H2 update on your HP laptop? Usually a driver or audio-service issue. Here are 7 fixes to get sound working again."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why did my HP laptop lose sound after the 24H2 update?"
    a: "The 24H2 update replaces or migrates audio drivers, and on HP laptops the Realtek or Conexant driver sometimes fails to migrate cleanly — leaving the system with a generic driver that produces no sound, or with the audio service in a broken state. HP-specific audio enhancements and the Bang and Olufsen tuning software can also conflict with the new driver model. Reinstalling the correct HP audio driver fixes most cases."
  - q: "My speakers show as working but there is no sound. What is wrong?"
    a: "This classic symptom means the audio pipeline is running but output is routed nowhere or muted at a hidden layer. Check the volume mixer for per-app mutes, verify the correct output device is selected in quick settings, and look at the Realtek or HP audio control panel for a muted master channel. If all levels look fine, the driver is likely outputting to a disconnected jack — reinstalling it resets the routing."
  - q: "Should I use the HP audio driver or the Windows generic one?"
    a: "Use HP's driver from their official support site. The generic Windows High Definition Audio driver will produce basic sound, but it lacks HP's speaker tuning, the correct jack detection, and microphone array support — so audio quality and features suffer. Install HP's driver first; fall back to the generic driver only temporarily while troubleshooting."
  - q: "Will reinstalling the audio driver delete my settings?"
    a: "It resets audio settings to defaults — equalizer tweaks, custom enhancements, and per-app volume levels will be lost. Your files and everything else are untouched. If you have carefully tuned audio settings, screenshot them before reinstalling so you can restore them afterward. The tradeoff is worth it: a clean driver install resolves the deep corruption that settings tweaks cannot."
---

Sound disappearing right after the Windows 11 24H2 update is a special kind of annoying — everything else works, but your HP laptop has gone mute. No error message, no warning; the speaker icon might even show everything as normal while nothing comes out. This is one of the most common 24H2 regressions on HP hardware, and it is almost always a driver migration problem rather than broken speakers.

Here is what happens: during the feature update, Windows migrates your audio drivers to the new OS build. On HP laptops — which use Realtek or Conexant audio chips plus HP's own audio tuning software — that migration frequently goes wrong. The result is a driver that loads without errors but produces no sound, an audio service stuck in a bad state, or output routed to a phantom device. The speakers themselves are fine; the software path to them is broken. These fixes rebuild that path step by step.

## Why this happens

- **Failed audio driver migration.** The 24H2 installer replaces the HP audio driver with an incompatible version or a broken generic one.
- **Audio service stuck.** The Windows Audio service can end up in a hung state after the update, blocking all sound output.
- **Output routed to the wrong device.** The update can switch the default output to HDMI, a disconnected Bluetooth device, or a phantom jack.
- **HP audio enhancements conflict.** Bang & Olufsen tuning and Realtek enhancements can clash with the migrated driver.
- **Muted at a hidden layer.** Per-app or device-level mutes in the volume mixer survive the update and silence everything.
- **BIOS audio settings changed.** Rare, but 24H2-related firmware updates on some HP models reset onboard audio settings.
- **Corrupted driver store.** Damage to the driver repository means even reinstalls pull broken files until it is cleaned.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious output routing first

Half of all "no sound" cases are routing problems, not driver problems. Rule them out in two minutes.

1. Click the volume icon in the taskbar (or press **Win + A**) and check which output device is selected — make sure it says **Speakers (Realtek Audio)** or similar, not HDMI or a Bluetooth device.
2. Right-click the volume icon, choose **Open volume mixer**, and verify neither the master nor your app is muted or set to zero.
3. Play a test sound: right-click the volume icon, choose **Sound settings**, and click your output device — use the **Test** option if available.
4. Unplug any headphones, USB headsets, or HDMI cables, then retest. If sound returns, the issue was a stuck jack-detection state — continue to Fix 3 for the permanent fix.

### Fix 2: Restart the Windows Audio services

If routing is correct but there is still silence, the audio service stack may be hung from the update.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Windows Audio**, right-click it, and choose **Restart**. Do the same for **Windows Audio Endpoint Builder**.
3. If either service refuses to start, check its dependencies: **Remote Procedure Call (RPC)** and **Multimedia Class Scheduler** must be running.
4. Retest sound. If the services keep stopping on their own, the driver underneath is crashing — move to Fix 3.

### Fix 3: Reinstall the HP audio driver from the official source

This is the fix that resolves most 24H2 audio failures: remove the broken migrated driver and install HP's correct one.

1. Go to [HP's official support site](https://support.hp.com/us-en), enter your model or serial number, and download the latest **audio driver** (Realtek or Conexant) for Windows 11.
2. Open **Device Manager**, expand **Sound, video and game controllers**, right-click your audio device, and choose **Uninstall device** — check **Attempt to remove the driver for this device**.
3. Restart the laptop, then install the driver you downloaded from HP. Restart once more.
4. Retest. If HP's driver still produces no sound, try the generic driver temporarily: in Device Manager, choose **Update driver > Browse my computer > Let me pick**, and select **High Definition Audio Device** — if that works, the HP driver package itself needs a newer release.

### Fix 4: Disable audio enhancements

HP's audio enhancements and the Realtek control panel effects can conflict with the 24H2 driver model, silently killing output.

1. Right-click the volume icon and choose **Sound settings**, then click your output device.
2. Under **Enhance audio**, turn the toggle **Off**.
3. In the same device properties, check the **Advanced** tab and uncheck **Allow applications to take exclusive control of this device** temporarily.
4. If you have the Realtek Audio Console or HP Audio Control app, open it and disable all effects and equalizer presets, then retest.

### Fix 5: Run the audio troubleshooter

Microsoft's troubleshooter checks the full audio path — services, drivers, and routing — and fixes common misconfigurations automatically.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Audio** and follow the prompts, selecting your speakers when asked which device to diagnose.
3. Apply every fix it suggests, then restart.
4. If the troubleshooter reports it cannot identify the problem, continue to Fix 6 — the issue is deeper than configuration.

### Fix 6: Check BIOS and update it if needed

On some HP models, the audio codec is gated by BIOS settings, and 24H2-era firmware updates occasionally reset them.

1. Restart and press **F10** (or **Esc** then **F10**) to enter BIOS setup.
2. Look for onboard audio or integrated peripherals settings and confirm the internal audio device is **Enabled**.
3. While you are there, note the BIOS version and compare it against the latest on [HP's support site](https://support.hp.com/us-en) — install the update if yours is older, keeping the charger plugged in.
4. Save, exit, and retest sound in Windows.

### Fix 7: Reset audio via a clean driver store cleanup

For the stubborn cases where reinstalls keep pulling the same broken driver, clean the driver store first.

1. In Device Manager, uninstall the audio device again with **Attempt to remove the driver for this device** checked.
2. Open Command Prompt as administrator and run `pnputil /enum-drivers` to list third-party drivers; find the audio driver's published name (e.g., `oem123.inf`).
3. Run `pnputil /delete-driver oem123.inf /uninstall` (using the actual name) to purge it from the store.
4. Restart and install the fresh HP driver from Fix 3. As a last resort, an in-place upgrade with the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) rebuilds the entire driver stack while keeping your files.

## Closing

No sound after 24H2 on an HP laptop is a software routing or driver problem in the vast majority of cases — not dead speakers. Check the output routing, restart the audio services, and reinstall HP's official audio driver; that sequence restores sound for nearly everyone. If the update also left your machine sluggish overall, see our guide to fixing a [slow laptop after the 24H2 update](/articles/best-way-to-fix-laptop-slow-after-windows-11-24h2-update/); and once audio is back, keeping drivers current via our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) prevents the next feature update from muting you again.
