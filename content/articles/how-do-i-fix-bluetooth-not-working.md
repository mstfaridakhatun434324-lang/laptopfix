---
title: "Bluetooth Not Working on Your Laptop? Fix It Step by Step"
slug: how-do-i-fix-bluetooth-not-working
date: 2026-09-15
categories: ["drivers"]
tags: ["bluetooth", "bluetooth not working", "wireless", "device manager"]
description: "Bluetooth missing or won't connect on your Windows laptop? Work through toggle checks, service restarts, and driver fixes to restore it."
thumbnail: "/images/thumbs/how-do-i-fix-bluetooth-not-working.webp"
faqs:
  - q: "Why is Bluetooth missing from my Windows 11 settings?"
    a: "A missing Bluetooth toggle almost always means Windows can't see the Bluetooth radio — the driver is missing, corrupt, or the device is disabled. Check Device Manager first: if Bluetooth is absent even with hidden devices shown, reinstall the Bluetooth driver from your laptop manufacturer's support page. If the device appears with a warning, update or roll back its driver. Airplane mode stuck on can also hide the toggle."
  - q: "Bluetooth is on but won't pair with my device. What should I try?"
    a: "Put the accessory in pairing mode first (most need a long-press until an LED blinks), then remove the old pairing from Settings > Bluetooth & devices > Devices and pair fresh. Keep the devices within a meter during pairing, and make sure the accessory isn't still connected to your phone — Bluetooth accessories typically connect to only one host at a time."
  - q: "Can a Windows update break Bluetooth?"
    a: "Yes, very commonly. Windows Update replaces Bluetooth drivers (often Intel wireless drivers) with versions that break pairing, drop connections, or make the adapter vanish from Device Manager entirely. If Bluetooth died right after an update, roll the Bluetooth driver back in Device Manager — it's the fastest fix — then block the bad version with the Show or hide updates troubleshooter."
  - q: "Should I use the manufacturer's Bluetooth driver or Intel's?"
    a: "For Intel wireless cards (AX200/AX201/AX210 and friends), Intel's own driver from the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is usually the best choice — it's current and correctly matched. For MediaTek, Realtek, or Qualcomm Bluetooth, stick with your laptop manufacturer's driver, since those are tuned per model. Either beats the generic Windows Update version."
---

Bluetooth failures come in two flavors, and telling them apart saves a lot of time: the toggle is *missing* (Windows can't see the radio — a driver or hardware problem), or the toggle is there but *pairing fails* (a protocol or interference problem). Missing-toggle cases need driver surgery; pairing cases need procedure fixes. Figure out which one you have before touching anything.

The sequence: confirm Bluetooth exists in Device Manager, fix the driver if it doesn't, then work pairing procedure, services, and power management. If Bluetooth vanished specifically after an update, see [Bluetooth disappeared from Device Manager](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/); if your whole wireless stack is down including Wi-Fi, check [airplane mode stuck on](/articles/how-to-fix-airplane-mode-stuck-on/).

## Why this happens

- **Bluetooth driver replaced or corrupted by Windows Update**: The single most common cause — Intel wireless driver updates frequently break Bluetooth while leaving Wi-Fi working.
- **Bluetooth Support Service stalled**: The background service Bluetooth depends on can hang, especially after sleep/wake.
- **Airplane mode or physical wireless switch engaged**: Kills the radio at a level no Settings toggle can override.
- **USB power management sleeping the adapter**: Internal Bluetooth is usually a USB device; Windows powers it down to save battery.
- **Accessory still paired to another host**: Bluetooth accessories connect to one device at a time — your phone is holding the connection.
- **Stale pairing cache**: Corrupt pairing data on either side blocks reconnection even when everything else works.
- **2.4 GHz Wi-Fi interference**: Bluetooth shares the 2.4 GHz band; heavy Wi-Fi traffic or USB 3.0 interference degrades pairing and audio.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Windows sees the Bluetooth radio

Determine missing-radio vs. pairing-problem in one check.

1. Press **Win + X** > **Device Manager** and look for a **Bluetooth** category. If it's there with your adapter listed and no warnings, your radio is fine — skip to Fix 4.
2. If the Bluetooth category is missing, click **View** > **Show hidden devices**. A greyed-out adapter means it's disabled — right-click > **Enable device**.
3. If there's a yellow warning icon, right-click > **Properties** and read the error — Code 43 or Code 10 means driver trouble (Fix 2).
4. Check **Settings** > **Bluetooth & devices** — if the Bluetooth toggle itself is missing, that confirms Windows sees no radio.
5. Also verify airplane mode is off and there's no physical wireless switch on the laptop's side or front edge.

### Fix 2: Fix the Bluetooth driver

The core repair for missing or broken radios.

1. In **Device Manager**, right-click the Bluetooth adapter > **Properties** > **Driver** tab > **Roll Back Driver** if the problem started after an update.
2. If rollback isn't available: right-click > **Uninstall device**, check **Attempt to remove the driver** if offered, then restart. Windows will reinstall its inbox Bluetooth driver.
3. For Intel wireless cards, install the latest from the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — Intel's Bluetooth and Wi-Fi ship as a pair, so update both.
4. For other vendors (MediaTek, Realtek, Qualcomm), get the driver from your laptop maker's support page — [Dell's support page](https://www.dell.com/support) (or HP's or Lenovo's).
5. After installing, confirm the Bluetooth category is back in Device Manager with no warnings before attempting any pairing.

### Fix 3: Restart Bluetooth services and reset the stack

For radios that exist but misbehave.

1. Press **Win + R**, type `services.msc`, and restart **Bluetooth Audio Gateway Service**, **Bluetooth Support Service**, and **Bluetooth User Support Service** (set each to **Automatic**).
2. Open **Settings** > **Bluetooth & devices** > **Devices**, remove every paired device you no longer use (three dots > **Remove device**) — stale pairings cause conflicts.
3. Toggle Bluetooth off, wait ten seconds, toggle it back on.
4. Run the troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Bluetooth** > **Run**.
5. Restart the laptop — Bluetooth stack resets are one of the few things that genuinely need the reboot.

### Fix 4: Pair correctly — procedure matters

Most "won't pair" cases are procedure, not breakage.

1. Put the accessory in **pairing mode** — this is not the same as just turning it on. Usually a long-press (3–7 seconds) on the power/pair button until an LED blinks rapidly. Check the accessory's manual if unsure.
2. Disconnect the accessory from your phone first — turn the phone's Bluetooth off temporarily. One host at a time.
3. On the laptop: **Settings** > **Bluetooth & devices** > **Add device** > **Bluetooth**, and keep the accessory within a meter during pairing.
4. If the accessory appears but pairing fails, remove any existing entry for it first (**Remove device**), then pair fresh.
5. For PIN prompts on old devices, try `0000` or `1234` — the ancient defaults still work on legacy headsets and keyboards.

### Fix 5: Disable power management on the Bluetooth adapter

Stop Windows from sleeping the radio.

1. In **Device Manager** > **Bluetooth**, right-click your adapter > **Properties** > **Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Also check under **Universal Serial Bus controllers** — internal Bluetooth often appears as a **USB** device there. Open each **USB Root Hub** > **Power Management** and uncheck the same box.
4. In **Power Options** > **advanced settings**, set **USB selective suspend** to **Disabled** for both battery and plugged-in.
5. Test specifically after sleep/wake cycles — that's when power-management Bluetooth deaths show up.

### Fix 6: Reduce 2.4 GHz interference

For connections that pair but stutter, lag, or drop.

1. Move USB 3.0 devices (external drives, docks) away from the laptop's Bluetooth antenna area — USB 3.0 is a notorious 2.4 GHz noise source. Use extension cables if needed.
2. If your router offers 5 GHz Wi-Fi, connect the laptop to 5 GHz — this moves Wi-Fi traffic off Bluetooth's band entirely.
3. Keep the Bluetooth accessory close and line-of-sight during testing; walls and bodies attenuate 2.4 GHz significantly.
4. For audio stutter specifically, check **Settings** > **Bluetooth & devices** > **Devices** > your headphones — disable "hands-free" profiles you don't use, as they force low-quality modes.
5. Microwave ovens operating nearby will nuke Bluetooth temporarily — not a laptop problem, just physics.

### Fix 7: Reset network settings as a last resort

When everything is configured right but nothing works.

1. Open **Settings** > **Network & internet** > **Advanced network settings** > **Network reset** > **Reset now**. This clears all Bluetooth pairings, Wi-Fi networks, and VPNs — you'll set them up again afterward.
2. Restart when prompted and re-pair your most important accessory first as a test.
3. If Bluetooth *still* doesn't appear in Device Manager after a network reset and driver reinstall, the radio hardware itself may have failed (or its internal USB connection loosened).
4. A USB Bluetooth dongle ($10–15) is a perfectly good permanent workaround — disable the internal adapter in Device Manager to avoid conflicts.
5. For internal repair, the wireless card is usually a replaceable M.2 module — a shop can swap it cheaply.

## Closing

Bluetooth troubleshooting is really two jobs: prove Windows can see the radio (driver work), then prove the pairing procedure is right (accessory in pairing mode, old host disconnected). Most people mix the two up and reinstall drivers for what was actually a phone still holding the connection. Check the radio first, pair properly second.
