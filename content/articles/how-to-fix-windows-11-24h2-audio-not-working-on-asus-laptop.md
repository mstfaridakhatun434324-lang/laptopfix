---
title: "No Sound After Windows 11 24H2 on an ASUS Laptop: Getting Audio Back"
slug: how-to-fix-windows-11-24h2-audio-not-working-on-asus-laptop
date: 2026-09-03
categories: ["windows-update"]
tags: ["24h2", "audio not working", "asus laptop", "sound fix"]
description: "Windows 11 24H2 killed your ASUS laptop's sound? Fix missing or distorted audio with the right driver sequence, Realtek resets, and Windows audio service repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why did 24H2 break audio on my ASUS specifically?"
    a: "The 24H2 update replaces the audio driver stack and re-enumerates audio endpoints. On ASUS laptops the new generic driver sometimes fails to talk to ASUS's customized Realtek implementation, so the device shows up but produces no sound — or vanishes entirely. The fix is almost always driver-layer, not hardware."
  - q: "Should I update or roll back the audio driver?"
    a: "Update first, and only roll back if the newest driver still fails. Get the driver from ASUS's support site for your exact model rather than relying on Windows Update, because ASUS's package includes the tuning components the generic Realtek driver lacks. Rollback is the fallback when every newer driver misbehaves."
  - q: "Does 24H2 affect Bluetooth audio too?"
    a: "Sometimes, but Bluetooth audio failures have different causes — usually the Bluetooth stack or the audio enhancement pipeline. If your speakers are dead but Bluetooth headphones work, focus on the Realtek driver fixes below. If both are dead, start with the Windows audio service checks instead."
  - q: "Will a system restore fix the audio?"
    a: "A restore point from before the 24H2 update would restore the old driver stack and bring sound back, yes. But it is a temporary win — Windows will reinstall 24H2 eventually. Better to fix the driver problem now so the update can stay installed permanently."
---

Few post-update problems are as immediately noticeable as silence. You install Windows 11 24H2 on your ASUS laptop, everything looks fine, and then — no system sounds, no video audio, nothing. The speakers have not broken. In nearly every case, the update disturbed the audio driver layer, and the sound is one driver sequence away from returning.

ASUS laptops complicate this slightly because ASUS ships customized Realtek audio packages with extra processing components. The generic driver Windows 11 24H2 prefers does not always include those components, so the driver loads but produces nothing. Follow the order below; the fix that restores sound for most ASUS owners is Fix 3, but run the quick checks first so you know what you are dealing with. If Windows Update itself is [failing to deliver driver updates](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/), fix that first — it can be the root cause.

## Why this happens

- **Driver replaced by 24H2:** The update swapped your ASUS-tuned audio driver for a generic one that cannot drive the speakers.
- **Audio endpoint re-enumeration failed:** 24H2 re-registers audio devices, and the registration can complete with a broken endpoint mapping.
- **ASUS audio console removed:** The update sometimes drops the Realtek Audio Console or ASUS tuning app, disabling the processing chain.
- **Audio service failed to start:** The Windows Audio and AudioEndpointBuilder services did not come up cleanly after the update.
- **Enhancement pipeline broken:** Audio enhancements tied to the old driver version now point at components that no longer exist.
- **Exclusive-mode conflicts:** An app grabbed the audio device in exclusive mode under the new driver and never released it.
- **BIOS/UEFI audio setting drift:** Rare, but some ASUS firmware exposes audio controller toggles that can reset during major updates.
- **Output device defaulted wrong:** The default playback device silently switched to a monitor or disconnected output.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the simple stuff first

Rule out the embarrassing causes in two minutes before touching drivers.

1. Press the volume keys and check the system tray — make sure nothing is muted.
2. Right-click the speaker icon, open **Sound settings**, and confirm the correct output device is selected.
3. Click the output device and run the **Test** button — if the test tone plays, the problem is app-level, not driver-level.
4. Try a different app (browser vs. media player) to see whether the silence is universal.
5. Plug in headphones: if headphones work but speakers do not, the speaker driver path is broken — continue below.

### Fix 2: Restart the Windows audio services

The audio services sometimes fail to initialize after a feature update.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find **Windows Audio** — if it is not running, right-click and choose **Start**.
3. Find **Windows Audio Endpoint Builder** and start it the same way if needed.
4. Right-click each service, choose **Properties**, and set **Startup type** to **Automatic**.
5. Restart the laptop and test the sound.

### Fix 3: Install the ASUS audio driver for your exact model

This is the fix that resolves most ASUS post-24H2 audio deaths.

1. Find your exact model number (check the sticker on the bottom or MyASUS).
2. Go to the ASUS support site and search for your model.
3. Download the audio driver package listed for Windows 11 — prefer the newest version.
4. Uninstall the current audio driver first: Device Manager > **Sound, video and game controllers** > right-click the Realtek device > **Uninstall device** (do not check "delete driver" unless you have the new package ready).
5. Install the ASUS package, restart, and test.

### Fix 4: Disable audio enhancements

Broken enhancement hooks from the old driver can silence the new one. Intel's driver detection tool at [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html) can also update the chipset-side audio bus drivers that feed the codec.

1. Open **Sound settings** and select your output device.
2. Open **Device properties > Additional device properties** (or the equivalent link).
3. Go to the **Enhancements** tab and check **Disable all enhancements**.
4. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device**.
5. Apply, restart the affected app, and test.

### Fix 5: Run the audio troubleshooter

Microsoft's troubleshooter handles endpoint registration problems reasonably well. See the [Windows support hub](https://support.microsoft.com/en-us/windows) for the guided walkthrough.

1. Go to **Settings > System > Sound**.
2. Scroll to **Advanced** and click **Output devices > Troubleshoot** (or **Other troubleshooters > Audio**).
3. Let it run and apply its recommended fixes.
4. Restart the laptop afterward.
5. Test with the built-in test tone first.

### Fix 6: Roll back the audio driver

If the newest driver is the problem, the previous one still works.

1. Open Device Manager and find your audio device under **Sound, video and game controllers**.
2. Right-click it, choose **Properties**, and open the **Driver** tab.
3. Click **Roll Back Driver** and pick the reason "previous driver worked better."
4. Restart the laptop.
5. Once sound is back, consider pausing driver updates briefly via [optional update settings](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop/) so 24H2 does not immediately replace the driver again.

### Fix 7: Reinstall the audio stack with a clean slate

For stubborn cases where no driver version produces sound.

1. In Device Manager, uninstall every device under **Sound, video and game controllers** and **Audio inputs and outputs**.
2. Check the box to delete the driver software for each one.
3. Restart — Windows will install basic High Definition Audio drivers.
4. Test: if sound works with the basic driver, install the ASUS package from Fix 3 on top.
5. If even the basic driver is silent, suspect a hardware or firmware issue and contact ASUS support.

## Closing

Post-24H2 audio loss on ASUS laptops is a driver-layer problem in the overwhelming majority of cases, and the ASUS-provided driver package is the correct answer more often than anything Windows Update offers on its own. Work the list in order, verify sound after each step with the built-in test tone, and resist the urge to reinstall Windows — the speakers are fine, and so is the hardware underneath them.
