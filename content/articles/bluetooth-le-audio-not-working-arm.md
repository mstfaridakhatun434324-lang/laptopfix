---
title: "Bluetooth LE Audio Not Working on ARM Laptops: How to Fix It"
slug: bluetooth-le-audio-not-working-arm
date: 2026-10-23
categories: ["ai-pc"]
tags: ["bluetooth le audio", "lc3", "auracast", "arm laptop", "audio fix", "troubleshooting"]
description: "Fix Bluetooth LE Audio not working on ARM laptops: enable LE Audio in Windows, update Bluetooth drivers, and repair pairing step by step for LC3 audio."
thumbnail: "/images/thumbs/bluetooth-le-audio-not-working-arm.webp"
faqs:
  - q: "What is Bluetooth LE Audio and why should I care?"
    a: "LE Audio is the modern Bluetooth audio standard built on the LC3 codec. It delivers better sound quality than classic SBC at lower bitrates, uses less battery, and enables features like Auracast broadcast audio. Your earbuds and your laptop must both support it."
  - q: "Why do my earbuds connect but LE Audio won't enable?"
    a: "Both the earbuds and the laptop's Bluetooth stack must support LE Audio, and Windows 11 must have it toggled on for the device. A missing toggle usually means the Bluetooth driver is outdated or the earbuds' firmware predates LE Audio support."
  - q: "Can I use LE Audio and the microphone at the same time?"
    a: "Yes — that's one of LE Audio's big advantages over classic Bluetooth, which drops to terrible HFP quality when the mic is active. With LE Audio, voice calls keep high-quality audio in both directions."
  - q: "Will LE Audio work with my old Bluetooth headphones?"
    a: "No. LE Audio requires hardware support on both ends. Older headphones that only speak classic Bluetooth (A2DP/SBC) will keep working in classic mode — they just can't use the new LC3 codec."
---

Your new earbuds promise LE Audio with the LC3 codec, your ARM laptop's spec sheet lists Bluetooth 5.3 or 5.4, but Windows stubbornly connects in classic mode — or the "LE Audio" toggle is missing entirely. The two devices are speaking different Bluetooth generations, and something in the middle is not translating.

LE Audio is genuinely worth the trouble: better sound at lower power, proper microphone quality during calls, and Auracast broadcast support. But it demands an unbroken chain — earbud firmware, laptop Bluetooth radio, driver, and Windows toggle — and ARM laptops have a few extra driver quirks in that chain.

This guide walks you through six fixes in order: compatibility checks first, then Windows settings, then driver repair and clean re-pairing.

## Why this happens

- **Earbuds lack LE Audio firmware:** Many earbuds shipped before their LE Audio firmware update, or need a companion phone app to enable it. The hardware supports it; the installed firmware does not.
- **Bluetooth driver outdated:** LE Audio support arrived in Bluetooth drivers over time. An older Qualcomm or Intel Bluetooth driver on your ARM laptop may simply not expose the LE Audio toggle.
- **LE Audio toggle off in Windows:** Windows 11 has a per-device LE Audio setting. If it defaulted off — or was never offered during pairing — the connection stays in classic mode.
- **Paired in the wrong mode:** Some earbuds pair first in classic mode and need to be removed and re-paired after enabling LE Audio on the earbud side before Windows offers the LC3 path.
- **Bluetooth radio too old:** LE Audio needs Bluetooth 5.2 or newer on the laptop. Older radios cannot do it regardless of drivers — check your laptop's spec sheet.
- **Interference or distance breaking the LC3 link:** LE Audio's low-power link is more sensitive to interference. A connection that keeps dropping back to classic mode may be a radio environment problem, not a settings problem.
- **Virtual-device conflicts:** Virtual audio or camera devices from conferencing tools can confuse Windows' audio endpoint selection — the same class of virtual-device interference behind [OBS virtual camera conflicts](/articles/studio-effects-obs-virtual-camera-conflict/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm both ends support LE Audio

LE Audio is a handshake — if either side cannot do it, there is nothing to fix in Windows. Verify the hardware before changing settings.

1. Check your earbuds' spec sheet or companion app for "LE Audio" or "LC3" support — look specifically for a firmware update that adds it, and install it via the earbuds' phone app.
2. Check your laptop's Bluetooth version: open **Device Manager > Bluetooth**, right-click the Bluetooth radio, open **Properties > Advanced**, and look for LMP version — 5.2 or higher (LMP 11+) supports LE Audio.
3. If the laptop's radio is Bluetooth 5.0 or older, LE Audio is impossible on this hardware — a USB Bluetooth 5.3+ dongle is the only path forward.
4. Confirm you are running Windows 11 22H2 or newer (**Settings > System > About**), since LE Audio support in Windows arrived with those builds.
5. Only continue when both ends check out — every fix below assumes capable hardware on both sides.

### Fix 2: Enable LE Audio in Windows Bluetooth settings

With capable hardware, the Windows toggle is the next gate. It is per-device and easy to miss.

1. Open **Settings > Bluetooth & devices**, find your earbuds in the device list, and click the three dots or the device entry for **More options**.
2. Look for an **LE Audio** toggle or a "Use LE Audio when available" option and switch it **On**.
3. If no toggle appears, remove the device (**Remove device**), put the earbuds back in pairing mode, and re-pair — Windows sometimes only offers the toggle on a fresh pairing.
4. After enabling, disconnect and reconnect the earbuds, then play audio and check **Settings > System > Sound** to confirm the earbuds show as the output with the LE Audio path active.
5. Test a voice call as well — LE Audio's real payoff is microphone quality, so confirm the mic input also routes through the LE Audio device rather than a legacy hands-free profile.

### Fix 3: Update the Bluetooth driver from the OEM

A missing LE Audio toggle with capable hardware almost always means the Bluetooth driver predates LE Audio support. The OEM's driver package — not Windows Update's generic one — is what you need.

1. Download the Bluetooth driver for your exact model from [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), or [Dell](https://www.dell.com/support/) — check the release notes for LE Audio or LC3 mentions.
2. In Device Manager, expand **Bluetooth**, right-click the Bluetooth radio device, choose **Uninstall device** (do not check driver removal unless the OEM instructions say so), and restart.
3. Run the OEM Bluetooth installer as administrator and restart again when prompted.
4. Re-pair the earbuds fresh (remove the old pairing first), then check for the LE Audio toggle from Fix 2.
5. If the OEM driver is already current and the toggle is still missing, check the earbud maker's support pages — some earbuds need a specific firmware version before Windows will offer LE Audio.

### Fix 4: Clean re-pairing with a Bluetooth stack reset

Corrupted pairing state can lock Windows into classic mode even with the right drivers. A full reset of the Bluetooth stack clears it — the same "clear the stale state" logic that fixes [model inference errors in local AI apps](/articles/huggingface-model-npu-inference-error/).

1. In **Settings > Bluetooth & devices**, remove the earbuds with **Remove device**, then turn Bluetooth off.
2. Open **Device Manager > Bluetooth**, right-click the radio, choose **Disable device**, wait 10 seconds, and **Enable device** again.
3. Turn Bluetooth back on in Settings and put the earbuds in pairing mode (usually a long-press on the case button — check the earbud manual).
4. Pair fresh, then immediately check for and enable the LE Audio toggle before doing anything else.
5. If pairing fails repeatedly, also remove the earbuds from any paired phone nearby — some earbuds refuse a second pairing while connected elsewhere.

### Fix 5: Reduce interference and fix dropouts

An LE Audio link that connects but stutters or falls back to classic mode is usually a radio environment problem. The LC3 link runs at lower power and notices interference that classic Bluetooth shrugs off.

1. Move the earbuds and laptop closer together for testing — within a meter, line of sight — to isolate interference from configuration.
2. Move away from USB 3 docks and hubs: USB 3.0 is a notorious 2.4GHz interferer, and many docks sit right next to the laptop's Bluetooth antenna.
3. In **Device Manager**, open the Bluetooth radio's **Properties > Power Management** and uncheck **"Allow the computer to turn off this device to save power"**.
4. Turn off Wi-Fi temporarily as a test — if LE Audio stabilizes with Wi-Fi off, the laptop's Wi-Fi/Bluetooth coexistence needs the driver update from Fix 3, and you may need to prefer 5GHz Wi-Fi to leave 2.4GHz cleaner.
5. If dropouts persist only in one location (office, café), that environment is the problem — LE Audio will still beat classic mode everywhere else.

### Fix 6: Reset the earbuds and check for Auracast separately

When one specific earbud pair refuses LE Audio while others work, the earbuds themselves hold the bad state. A factory reset of the earbuds is the last software step before suspecting hardware.

1. Factory-reset the earbuds using the manufacturer's procedure (usually holding both touch panels or the case button for 10+ seconds — check the manual, as it varies).
2. Update the earbuds' firmware to the latest version through their companion phone app before pairing with the laptop again.
3. Re-pair with the laptop and enable the LE Audio toggle fresh.
4. If you bought the earbuds for Auracast broadcast audio specifically, note that Auracast is a separate feature from point-to-point LE Audio — check **Settings > Bluetooth & devices** for broadcast/Auracast options after the LE Audio link works.
5. If LE Audio works with other earbuds on this laptop but never with this pair — even after reset and firmware updates — the earbuds' LE Audio implementation is at fault; contact the earbud maker. And if you are testing audio while gaming, remember that unrelated game-launch problems like [Fortnite failing to launch on ARM](/articles/fortnite-arm-laptop-not-launching/) are a separate track from Bluetooth audio.

## Closing

Bluetooth LE Audio on ARM laptops fails at one of four gates: earbud firmware, laptop Bluetooth driver, the Windows per-device toggle, or stale pairing state. Verify both ends support it, update the OEM Bluetooth driver, re-pair cleanly, and enable the toggle — the LC3 link is worth the ten minutes it takes to get right.
