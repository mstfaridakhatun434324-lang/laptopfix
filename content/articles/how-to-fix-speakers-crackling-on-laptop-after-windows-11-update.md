---
title: "How to Fix Speakers Crackling on a Laptop After a Windows 11 Update"
slug: how-to-fix-speakers-crackling-on-laptop-after-windows-11-update
date: 2026-09-06
categories: ["drivers"]
tags: ["speakers crackling", "audio fix", "windows 11 update", "realtek audio"]
description: "Speakers started crackling, popping, or distorting right after a Windows 11 update? Seven proven fixes, from driver rollback to audio enhancement tweaks."
thumbnail: "/images/thumbs/how-to-fix-speakers-crackling-on-laptop-after-windows-11-update.webp"
faqs:
  - q: "Why did my speakers start crackling immediately after the Windows 11 update?"
    a: "Feature and cumulative updates frequently replace the laptop vendor's tuned audio driver with a newer generic one from Microsoft or the chip maker. The new driver may not match your laptop's specific speaker hardware, causing timing errors in the audio stream that you hear as crackles and pops. In most cases the hardware is fine — the wrong driver build is running, and rolling back or reinstalling the vendor's version clears it."
  - q: "Could crackling speakers mean my laptop's hardware is damaged?"
    a: "It can, but software causes are far more common right after an update. Test with wired headphones: if the headphones sound clean while the speakers crackle, the speaker hardware or its amplifier path is suspect. If both crackle, the driver or audio stack is the problem. If the crackling predates the update and grows worse at high volume, blown speakers become more likely."
  - q: "Should I use the driver from Windows Update or from my laptop maker?"
    a: "Use your laptop maker's driver first. Vendors like Dell, HP, and Lenovo customize Realtek and Intel audio drivers with speaker-tuning profiles specific to their models, and the generic driver Windows Update offers lacks that tuning — which is exactly why crackling often appears after an update. Only switch to the chip maker's latest driver if the vendor's version is unavailable or known to be broken."
  - q: "Will disabling audio enhancements affect sound quality?"
    a: "Disabling enhancements removes effects like virtual surround and loudness equalization, so the sound becomes flatter — but it eliminates the most common source of driver-induced crackling. Many users can't tell the difference in everyday use, and a flat, clean signal is always better than an 'enhanced' crackling one. You can re-enable effects one at a time afterward to find the offending one."
---

The update finished, the laptop rebooted, and now every YouTube video sounds like it's playing through a bag of chips. Crackling, popping, and intermittent distortion that wasn't there yesterday is one of the most common audio complaints after a Windows 11 update — and it's almost always a driver problem, not dying speakers. The timing is the giveaway: hardware doesn't fail on Microsoft's patch schedule.

What's happening under the hood is that the update swapped your audio driver stack. Windows 11's 24H2 updates are aggressive about pushing driver revisions through Windows Update, and the replacement driver often lacks the speaker-specific tuning your laptop vendor baked into the original. The result is buffer underruns and mismatched sample rates that surface as crackle. The good news: because the root cause is software, it's fixable without opening the laptop. Work through these fixes in order; most people are done by Fix 3. If the driver itself keeps dying rather than just distorting, see the guide on the [audio driver crashing repeatedly after a Windows 11 update](/articles/how-to-fix-audio-driver-keeps-crashing-after-windows-11-update/).

## Why this happens

- **Windows Update installed a generic audio driver.** The update replaced your vendor-tuned Realtek/Intel SST driver with a newer generic build that doesn't match your laptop's speaker profile, causing stream timing errors.
- **Audio enhancements conflict with the new driver.** Effects like loudness equalization and spatial sound that worked with the old driver now clash with the replacement, producing distortion.
- **The sample rate mismatched.** The new driver defaulted to a sample rate or bit depth (e.g., 16-bit 44100 Hz) that your speaker pipeline handles poorly, introducing audible artifacts.
- **Exclusive mode applications fight the driver.** Apps that take exclusive control of the audio device can now glitch against the updated driver, producing pops when they grab or release the stream.
- **The old driver's configuration survived the swap.** Leftover registry settings and enhancement profiles from the previous driver are applied to the new driver, which interprets them differently.
- **Power management throttles the audio device.** The update may have re-enabled aggressive power saving on the audio controller, starving it of CPU time during playback.
- **A partial update left mismatched components.** The audio driver updated but its companion service or control-panel app (like the Realtek Audio Console) didn't, creating version skew in the stack.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Roll back the audio driver

Since the update caused it, the fastest cure is the previous driver.

1. Press **Win + X** > **Device Manager** > **Sound, video and game controllers**.
2. Right-click your audio device (e.g., **Realtek(R) Audio** or **Intel Smart Sound Technology**) > **Properties**.
3. Open the **Driver** tab and click **Roll Back Driver**. Choose **Previous version of the driver worked better** and confirm.
4. Restart and test. If crackling stops, tell Windows Update not to replace it again (see Fix 7).

### Fix 2: Disable audio enhancements

Enhancements are the single most common crackle source after a driver swap.

1. Right-click the speaker icon in the taskbar > **Sound settings** > **More sound settings**.
2. On the **Playback** tab, double-click **Speakers** (your default output).
3. Open the **Enhancements** tab and check **Disable all enhancements**.
4. On the **Advanced** tab, uncheck **Allow applications to take exclusive control of this device**.
5. Click **Apply** and test playback. If it's clean, the driver was fine — the effects were the problem.

### Fix 3: Install the vendor's audio driver

Get the driver your laptop maker tuned for your exact speakers.

1. Find your laptop's exact model and go to the vendor's support page — [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or the [Lenovo Support site](https://support.lenovo.com/us/en/).
2. Download the audio driver listed for your model (Realtek, Intel SST, or Cirrus Logic depending on hardware).
3. In Device Manager, right-click the audio device > **Uninstall device**, and check **Attempt to remove the driver for this device** to purge the crackling build.
4. Restart, then install the downloaded vendor driver and restart again.

### Fix 4: Change the default format

A mismatched sample rate produces exactly the crackle-and-pop signature.

1. In the **Speakers Properties** window (Fix 2, steps 1–2), open the **Advanced** tab.
2. In **Default Format**, try **24-bit, 48000 Hz (Studio Quality)** first, then **16-bit, 44100 Hz (CD Quality)** if the crackle persists.
3. Click **Test** after each change and **Apply** when you find the clean setting.
4. Avoid the highest options (192 kHz); they increase the load on the audio path and can reintroduce glitches.

### Fix 5: Update the Intel Smart Sound Technology driver

On Intel-based laptops, the SST bus driver — not the codec — is often the real culprit.

1. In Device Manager, expand **System devices** and find **Intel(R) Smart Sound Technology** entries.
2. Right-click each > **Update driver** > **Search automatically for drivers**.
3. If Windows finds nothing, get the SST driver from your laptop vendor's support page (it's usually bundled with the chipset or audio package).
4. Restart after installation and test. SST timing errors masquerade as speaker crackle.

### Fix 6: Run the audio troubleshooter and restart audio services

Let Windows repair its own stack before you go deeper.

1. Go to **Settings** > **System** > **Sound** > **Troubleshoot** (under Advanced).
2. Run the **Playing Audio** troubleshooter and apply any recommended fixes.
3. Press **Win + R**, type `services.msc`, and restart **Windows Audio** and **Windows Audio Endpoint Builder**.
4. Test playback. The troubleshooter sometimes resets the enhancement and format settings that the update mangled.

### Fix 7: Block Windows Update from replacing the audio driver

Once you have a clean driver, keep it.

1. Press **Win + R**, type `gpedit.msc` (Pro editions) or use the registry on Home: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`, create DWORD **ExcludeWUDriversInQualityUpdate** = 1.
2. Alternatively, in Device Manager note your working driver version, and if an update breaks it again, roll back immediately via Fix 1.
3. Also check the vendor's support app (e.g., Dell Update, HP Support Assistant) — let it manage driver updates instead of Windows Update. If headphones are also affected, work through the [headphone detection guide](/articles/how-to-fix-laptop-not-detecting-headphones-in-windows-11-24h2/) after the crackle is gone.

## Closing

Post-update speaker crackling is annoying precisely because it feels like hardware damage — but in the overwhelming majority of cases it's a driver mismatch introduced by the update, and it's fully reversible. Roll back, disable enhancements, and reinstall the vendor's tuned driver; that trio resolves nearly every case. Once the sound is clean, take two minutes to block future driver replacements so the next update can't bring the crackle back.
