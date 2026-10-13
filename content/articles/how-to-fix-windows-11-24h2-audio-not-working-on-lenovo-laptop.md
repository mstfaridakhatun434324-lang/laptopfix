---
title: "Fix Windows 11 24H2 Audio Not Working on a Lenovo Laptop"
slug: how-to-fix-windows-11-24h2-audio-not-working-on-lenovo-laptop
date: 2026-09-19
categories: ["windows-update"]
tags: ["audio not working", "windows 11 24h2", "lenovo laptop"]
description: "No sound after the Windows 11 24H2 update on your Lenovo? Fix broken audio drivers, services, and settings with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-audio-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why did the 24H2 update break my Lenovo's audio?"
    a: "Feature updates migrate audio drivers to the new OS build, and the migration sometimes installs a generic driver that does not match Lenovo's audio hardware — particularly models with Realtek chips plus Dolby or Smart Audio enhancements. The result is silence, or a speaker icon with a red X. Reinstalling the Lenovo-validated driver fixes it."
  - q: "Should I use the Windows Update driver or Lenovo's driver?"
    a: "Lenovo's. Windows Update often supplies a generic Realtek driver that lacks the model-specific tuning and enhancement layers. Download the audio driver for your exact model from Lenovo Support or via Lenovo Vantage — it is built for your hardware and far more likely to work."
  - q: "My Bluetooth audio works but speakers don't. What does that mean?"
    a: "That isolates the fault to the internal audio driver or speaker hardware path, not the Windows audio engine — Bluetooth audio uses a completely separate driver stack. Focus on the Realtek/internal audio driver reinstall steps below rather than system-wide audio repairs."
  - q: "Could the 24H2 update have damaged my speakers physically?"
    a: "No. Software updates cannot damage speakers. If audio worked before the update and stopped after, it is a driver or configuration issue in essentially every case. The hardware is fine; the software driving it needs repair. Treat it as a software problem until proven otherwise — which the driver steps below will establish one way or the other."
---

Audio breaking after a Windows 11 24H2 update is a special kind of irritating: everything else works, but your Lenovo sits in silence — or worse, shows the speaker icon with a red X as if mocking you. This is one of the most common post-feature-update complaints on Lenovo laptops, and it has a well-understood cause: the update's driver migration replaces Lenovo's tuned Realtek audio driver with a generic one that does not know how to talk to your specific audio hardware, especially on models with Dolby Atmos or Smart Audio enhancements layered on top.

The fix is almost always driver surgery, not system repair. Windows' audio engine is fine; the driver translating between the engine and your speakers is wrong. This guide walks the driver fix properly — including the clean removal that most people skip — plus the service and settings checks for the minority of cases where the driver is not the culprit. For the broader class of update failures that can accompany this, see [Windows Update failing to install in 24H2](/articles/how-to-fix-windows-update-fails-to-install-in-windows-11-24h2/).

There is a diagnostic shortcut specific to this problem that saves a lot of time: test with headphones or an external speaker before doing anything else. If external audio works while the internal speakers are silent, you have isolated the fault to the internal audio path — its driver, its enhancement layer, or its BIOS setting — and you can skip every system-wide repair with confidence. If nothing produces sound anywhere, the fault is higher up the stack. Two minutes with a pair of earbuds tells you which half of this guide matters.

## Why this happens

- **Generic driver migration:** The 24H2 update installs a basic Microsoft/Realtek driver that lacks Lenovo's hardware-specific configuration.
- **Enhancement layer mismatch:** Dolby or Smart Audio components from the old build conflict with the new generic driver.
- **Driver marked incompatible:** 24H2's stricter validation disables the old Lenovo audio driver without installing a working replacement.
- **Audio service disruption:** The Windows Audio service or its dependencies fail to start properly after the migration.
- **Default device reset:** The update resets the default playback device to a nonexistent or wrong output.
- **Exclusive mode conflicts:** Leftover exclusive-mode settings from the old driver block the new one.
- **BIOS audio settings:** Rarely, the update exposes a BIOS-level audio disablement — check if the driver reinstall fails.
- **Corrupted driver store:** Migration debris in the driver store prevents clean installation of the correct driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the basics — output device and volume

1. Click the speaker icon in the taskbar and verify the correct output (Speakers/Headphones) is selected — updates often switch it.
2. Open **Settings → System → Sound** and confirm the output device, volume level, and that nothing is muted.
3. Run the built-in audio troubleshooter: **Settings → System → Sound → Troubleshoot** — it catches simple misconfigurations fast.

### Fix 2: Restart the audio services

1. Press **Win + R**, type `services.msc`.
2. Restart **Windows Audio** and **Windows Audio Endpoint Builder** (right-click → Restart).
3. If either is stopped, set Startup type to **Automatic** and start it.
4. Test audio. Services that failed to start post-update are a quick win.

### Fix 3: Clean-remove the broken audio driver

1. Open **Device Manager → Sound, video and game controllers**.
2. Right-click the Realtek/audio device → **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. This is the step most guides skip — without it, Windows reinstalls the same broken driver.
4. Reboot. Windows will install a basic driver; test, then proceed to Fix 4 for the proper Lenovo driver.

### Fix 4: Install Lenovo's validated audio driver

1. Open **Lenovo Vantage → System Update**, or visit [Lenovo Support](https://support.lenovo.com/us/en/) with your serial number.
2. Download and install the **Audio driver** for your exact model — this is the tuned package with the correct enhancements.
3. Reboot and test. This resolves the large majority of post-24H2 audio failures on Lenovo. If sound works but quality is poor — crackling or tinny — revisit Fix 5's enhancement settings before assuming the driver is wrong.
4. If Vantage offers a **Dolby** or **Smart Audio** component update too, install it — the enhancement layer must match the driver.

### Fix 5: Disable audio enhancements temporarily

1. **Settings → System → Sound →** select your output → **Advanced** → turn off **Audio enhancements**.
2. Also disable exclusive mode: in the classic Sound control panel → device Properties → Advanced → uncheck "Allow applications to take exclusive control."
3. Test. Enhancement conflicts cause silence or distortion even with the right driver.

### Fix 6: Check for a disabled device in BIOS

1. If Device Manager shows no audio device at all after the clean reinstall, reboot into BIOS (F1/F2 on Lenovo).
2. Look for an **Audio** or **Internal Speaker** toggle under Configuration/Security and ensure it is enabled.
3. Save and boot — the device should now appear for driver installation.

### Fix 7: System restore or repair install for stubborn cases

1. If audio worked before 24H2 and nothing above helps, use **System Restore** to a pre-update point as a diagnostic — if sound returns, the update's migration is definitively at fault.
2. For a permanent fix without losing 24H2, do an in-place repair install from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) ISO, then install Lenovo's audio driver immediately after.
3. Verify with the [Windows Update troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-in-windows-11-24h2/) path if update components seem generally unhealthy.

## Closing

Post-24H2 audio failure on Lenovo is a driver problem wearing a system problem's clothes. The clean removal plus Lenovo-validated reinstall fixes it in the overwhelming majority of cases — the key is removing the broken driver fully instead of installing over it. Keep Lenovo Vantage's driver updates current going forward, and the next feature update will migrate audio cleanly instead of leaving you in silence. Sound is one of those things you only notice when it is gone; a few minutes of driver hygiene keeps it present.
