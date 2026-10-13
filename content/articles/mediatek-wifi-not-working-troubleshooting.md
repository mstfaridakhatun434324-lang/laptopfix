---
title: "MediaTek WiFi Not Working? Complete Troubleshooting Guide"
slug: mediatek-wifi-not-working-troubleshooting
date: 2026-09-05
categories: ["drivers"]
tags: ["mediatek", "wifi driver", "wireless", "mt7921", "troubleshooting"]
description: "MediaTek WiFi card dropping, vanishing, or refusing to connect? Fix the MT7921/MT7922 and related adapters with driver, power, and firmware steps."
thumbnail: "/images/thumbs/mediatek-wifi-not-working-troubleshooting.webp"
faqs:
  - q: "Why is MediaTek WiFi so problematic on Windows laptops?"
    a: "MediaTek's MT7921 and MT7922 cards shipped in huge numbers of budget and mid-range laptops, and their early Windows drivers had genuine stability bugs — drops, vanishing adapters, and poor roaming. Later driver revisions fixed most issues, so the single most impactful step is getting off the old inbox driver onto a current one."
  - q: "My MediaTek WiFi disappears from Device Manager. Is the card dead?"
    a: "Usually not. The disappearing act is the card's most infamous driver bug — the adapter crashes and Windows removes it. A full power cycle (shutdown, unplug, hold power 30 seconds) plus a driver update to a recent version resolves it in most cases. True hardware death is rare."
  - q: "Should I replace my MediaTek card with an Intel one?"
    a: "If your laptop has a socketed (non-soldered) WiFi card and the MediaTek adapter keeps failing after driver updates, swapping to an Intel AX210 is a popular and effective upgrade. Check that your BIOS doesn't whitelist WiFi cards first, and confirm the card is removable — many thin laptops solder it down."
  - q: "Does the MediaTek Bluetooth share the WiFi problem?"
    a: "Yes — MediaTek combo cards run WiFi and Bluetooth on one chip, so a crashing WiFi driver often takes Bluetooth down with it. If both die together, that's actually diagnostic confirmation pointing at the combo driver rather than two separate failures."
---

MediaTek WiFi cards — the MT7921 (WiFi 6) and MT7922 (WiFi 6E) especially — earned a rough reputation in Windows laptops. Vanishing adapters, random disconnects, connections that work for an hour then die, Bluetooth dying in sympathy. The reputation was earned by early drivers, but here's the thing most guides miss: later drivers fixed the majority of these problems, and most "broken" MediaTek cards just need the right driver and power settings.

This guide is the complete MediaTek-specific sequence, from the quick power-cycle trick that revives vanished adapters to the driver versions that actually work.

## Why this happens

- **Old or inbox driver.** The driver Windows ships for MediaTek cards is often years behind. Early MT7921 drivers had the disconnect and vanish bugs baked in.
- **Aggressive power management.** Windows powers down the WiFi card to save battery, and MediaTek's early drivers often failed to wake it back up — producing the classic "WiFi died after sleep" pattern.
- **Driver crash taking down the adapter.** The card's firmware can crash under certain traffic patterns; when it does, Windows removes the device from Device Manager entirely.
- **Roaming aggressiveness bugs.** Some driver versions handle access-point handoffs badly, dropping connections when moving between rooms or on mesh networks.
- **Windows Update driver replacement.** A working driver gets replaced by an older "inbox" version during feature updates, resurrecting bugs you thought were fixed. Compare the [Intel AX201's similar update problems](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).
- **BIOS/firmware incompatibility.** Some laptop BIOS versions don't initialize the MediaTek card cleanly, particularly after BIOS updates.
- **Actual hardware failure.** The least common cause — but cards do die, and antennas do come loose.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The full power-cycle revive

For vanished or dead adapters, this is step zero.

1. Shut the laptop down completely. Unplug the charger and all USB devices.
2. Press and hold the power button for **30 seconds**. This drains residual power and forces the WiFi card's firmware to fully reset.
3. If your laptop has a removable battery, take it out during this step.
4. Plug back in, boot up, and check Device Manager > Network adapters for the MediaTek card.
5. This revive works because the card's firmware can wedge in a state that survives normal reboots — only a full power drain clears it.

### Fix 2: Disable WiFi power management

Stops the "dies after sleep/idle" pattern.

1. In **Device Manager**, right-click the MediaTek WiFi adapter > **Properties** > **Power Management** tab. Uncheck "Allow the computer to turn off this device to save power."
2. Go to the **Advanced** tab. Set **Power Saving Mode** (or **Power Output**) to **Maximum Performance**.
3. In **Settings** > **System** > **Power & battery**, set power mode to **Best performance** while testing.
4. In **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** > **Wireless Adapter Settings** > **Power Saving Mode**, set both battery and plugged-in to **Maximum Performance**.
5. Test through a sleep/wake cycle and an hour of idle time.

### Fix 3: Install the correct current driver

The highest-yield permanent fix.

1. Identify your exact card: Device Manager > Network adapters > right-click MediaTek adapter > **Properties** > **Details** tab > **Hardware Ids**. Note whether it's MT7921, MT7922, or MT7925.
2. Get the driver from your **laptop manufacturer's support page** first — for Lenovo machines, [Lenovo support](https://support.lenovo.com/us/en/) often carries tested MediaTek driver packages.
3. If the manufacturer driver is old, get a newer one from MediaTek's site or a newer driver package from another laptop maker using the same card (Dell's and Lenovo's MediaTek packages are often interchangeable for the same chip).
4. In Device Manager, **Uninstall device** with driver removal checked, restart, then install the downloaded driver as administrator.
5. Verify the installed version in the Driver tab and write it down — you'll want to know if Windows Update replaces it later.

### Fix 4: Tune the adapter's advanced settings

Driver defaults aren't always the most stable.

1. In the adapter's **Advanced** tab, find **Roaming Aggressiveness** and set it to **Lowest** or **1**. This stops the drop-prone handoff behavior on most home networks.
2. Set **Preferred Band** to **Prefer 5GHz** (or your fastest stable band) to keep the card from bouncing between bands.
3. If you see **802.11a/b/g Wireless Mode** or **VHT Mode**, try disabling the newest modes (set to 802.11ac instead of ax) as a stability test — if drops stop, the ax-mode firmware is your problem and a driver update is the real fix.
4. Disable **Wake on Magic Packet** and **Wake on Pattern Match** unless you use Wake-on-LAN — these keep the card in twilight states that cause resume failures.

### Fix 5: Reset the network stack and forget the network

Clears corrupted profiles that mimic driver faults.

1. In **Settings** > **Network & internet** > **Wi-Fi**, **forget** your network, then reconnect from scratch with the password.
2. Run in an admin Terminal: `netsh winsock reset`, `netsh int ip reset`, then restart.
3. If problems persist, use **Settings** > **Network & internet** > **Advanced network settings** > **Network reset**.
4. After reconnecting, check whether drops correlate with specific times or locations — microwave ovens, for example, murder 2.4GHz.

### Fix 6: Update BIOS and block driver downgrades

Firmware-level stability and protecting your working driver.

1. Check your laptop maker's support page for a **BIOS update** — several vendors released BIOS fixes specifically for MediaTek card initialization.
2. After installing the working driver, set **Device Installation Settings** to **No** so Windows Update doesn't replace it with an older inbox driver.
3. Use the **Show or hide updates** troubleshooter to hide WiFi driver updates.
4. If [airplane mode gets stuck on](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/) after these changes, that's a separate radio-management issue — address it independently.

### Fix 7: Consider the hardware verdict or a card swap

When drivers can't save it.

1. Boot a **Linux live USB** and test WiFi there. Linux's MediaTek drivers are solid — if WiFi is stable in Linux, it's purely a Windows driver problem; if it fails in Linux too, it's hardware.
2. Check whether your card is socketed: look up your model's service manual. If it's an M.2 2230 card, an **Intel AX210** swap is a well-trodden upgrade path.
3. Verify there's no BIOS WiFi whitelist (most modern laptops don't have one, but check forums for your model).
4. As a stopgap, a USB WiFi adapter gets you online immediately while you decide.

General wireless troubleshooting is also documented on the official [Windows support pages](https://support.microsoft.com/en-us/windows).

## Closing

MediaTek WiFi's bad reputation is mostly a driver-age problem wearing a hardware costume. The full power-cycle revive brings vanished cards back, killing power management stops the sleep-deaths, and a current driver — protected from Windows Update downgrades — fixes the drops for the large majority of cards. Work the sequence, and only start shopping for an Intel replacement after Linux has confirmed the hardware is truly at fault.
