---
title: "Laptop Not Connecting to Wi-Fi 5GHz in Windows 11 24H2: Fixes"
slug: "how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2"
date: "2026-09-04"
categories: ["drivers"]
tags: ["wifi 5ghz not connecting", "windows 11 24h2", "wifi driver", "intel ax211", "5ghz band"]
description: "Laptop won't connect to 5GHz Wi-Fi after the Windows 11 24H2 update? Fix band settings, driver issues, and 24H2-specific wireless regressions with these steps."
thumbnail: "/images/thumbs/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2.webp"
faqs:
  - q: "Why did 5GHz Wi-Fi stop working after the 24H2 update?"
    a: "The 24H2 upgrade can replace your Wi-Fi driver with a build that mishandles 5GHz band negotiation, reset the adapter's preferred-band setting to 2.4GHz, or introduce power-management behavior that drops 5GHz associations. The 2.4GHz band often keeps working, which makes the failure look like a router problem when it is actually the laptop's driver."
  - q: "How do I know if my laptop supports 5GHz?"
    a: "Open Device Manager, find your Wi-Fi adapter under Network adapters, and check its name — 802.11ac, 802.11ax (Wi-Fi 6), or 802.11be (Wi-Fi 7) adapters all support 5GHz. In the adapter's Advanced properties, look for 'Preferred Band' or 'VHT Mode' options; their presence confirms 5GHz capability."
  - q: "Should I separate the 2.4GHz and 5GHz networks on my router?"
    a: "For troubleshooting, yes — temporarily. Combined band-steering SSIDs let the router decide, which hides whether the laptop can use 5GHz at all. Give the bands separate names during diagnosis so you can attempt a direct 5GHz connection; you can recombine them after the laptop is fixed."
  - q: "Can a VPN or security software block 5GHz connections?"
    a: "Rarely the band specifically, but VPN clients and firewall software can break Wi-Fi association generally, and their failure can coincide with an update. If 5GHz fails while 2.4GHz works on the same network, software is unlikely to be the cause — that pattern points to the adapter's band handling, not to a VPN."
---

A peculiar and frustrating symptom: after the Windows 11 24H2 update, your laptop connects to Wi-Fi fine — but only on the slow 2.4GHz band. The 5GHz network either does not appear in the list, appears but refuses to connect, or connects and immediately drops. Everything else about wireless works, which sends most people down the wrong path: rebooting the router, calling the ISP, blaming the walls.

The 2.4GHz-works/5GHz-doesn't pattern is diagnostic gold. It means the radio hardware is alive, the router is broadcasting, and Windows' wireless stack functions — the failure is specifically in 5GHz band handling, which lives in the Wi-Fi driver and its advanced settings. And 24H2 is notorious for disturbing exactly that: driver migration, reset band preferences, and new power behavior. Work through the fixes in order.

## Why this happens

- **Driver migration broke 5GHz negotiation**: 24H2's upgrade installed a Wi-Fi driver build whose 5GHz (VHT/HE) handshake fails with your router.
- **Preferred band reset**: the adapter's "Preferred Band" advanced setting reverted to 2.4GHz or "No preference" with broken steering.
- **VHT/802.11ac mode disabled**: the driver's 5GHz mode toggle got switched off during migration.
- **Aggressive power saving**: 24H2's power defaults let the adapter drop power-hungry 5GHz associations while keeping 2.4GHz.
- **Channel compatibility**: the router's 5GHz channel (especially DFS channels) is one the new driver build handles poorly.
- **Outdated router firmware vs. new driver**: the 24H2-era driver expects behaviors the router's old firmware does not provide.
- **Corrupted wireless profile**: the saved 5GHz network profile cached pre-24H2 security parameters that no longer match.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Forget the network and reconnect fresh

Start by clearing the cached wireless profile. 24H2 migrations corrupt saved profiles just often enough that this two-minute step deserves to go first.

1. Open **Settings > Network & internet > Wi-Fi > Manage known networks**.
2. Select your 5GHz network (or the combined SSID) and click **Forget**.
3. Restart the Wi-Fi adapter: **Settings > Network & internet > Advanced network settings**, disable Wi-Fi, wait 10 seconds, re-enable.
4. Reconnect to the 5GHz network, carefully re-entering the password.
5. If it connects and holds, the profile was corrupt — if your router uses one SSID for both bands, consider temporarily splitting them (see FAQ) to verify the 5GHz band specifically.

### Fix 2: Set the preferred band and VHT mode in adapter properties

The driver's advanced settings directly control band behavior. 24H2 resets these to defaults that deprioritize 5GHz on some adapters.

1. Open Device Manager, expand **Network adapters**, right-click your Wi-Fi adapter, and open **Properties > Advanced**.
2. Find **Preferred Band** and set it to **5GHz** (or "Prefer 5GHz band").
3. Find **VHT Mode** (or "802.11a/b/g Wireless Mode") and ensure 5GHz-capable modes are enabled — set to **VHT** or **802.11ac/ax** as available.
4. Find **Roaming Aggressiveness** and set it to a middle value — extremes can cause band-flapping.
5. Click OK, disable and re-enable the adapter, and attempt the 5GHz connection.

### Fix 3: Install the manufacturer's 24H2-validated Wi-Fi driver

The core fix for 24H2 5GHz regressions: replace the migrated driver with the manufacturer's 24H2-validated wireless package for your exact model.

1. Identify your Wi-Fi chip in Device Manager (e.g., Intel AX211, MediaTek MT7922, Realtek 8852BE).
2. Download the latest Wi-Fi driver from your laptop manufacturer's support page — look for 24H2-era releases.
3. For Intel cards, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) provides the newest validated package.
4. Uninstall the current Wi-Fi driver (ticking driver removal), install the downloaded package, then full shutdown and cold boot.
5. Recheck the Advanced tab settings from Fix 2 — reinstalls reset them — then test 5GHz.

### Fix 4: Disable power saving on the wireless adapter

5GHz operation draws more power than 2.4GHz, and 24H2's power defaults can sacrifice the 5GHz association to save battery — producing the connects-then-drops pattern.

1. In Device Manager, open the Wi-Fi adapter's **Properties > Power Management** and uncheck "Allow the computer to turn off this device to save power."
2. In the **Advanced** tab, set **Power Saving Mode** (or "Transmit Power") to **Maximum Performance**.
3. In **Power Options > Advanced settings**, set **Wireless Adapter Settings > Power Saving Mode** to **Maximum Performance** for both battery and plugged-in.
4. Test the 5GHz connection on AC power first to isolate battery-policy effects.
5. If 5GHz stabilizes, the diagnosis is confirmed — keep maximum performance while plugged in, as with the radio power fixes in [our Bluetooth power-management guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/).

### Fix 5: Change the router's 5GHz channel

Some 24H2 driver builds handle certain 5GHz channels poorly — particularly DFS channels (52–144) that require radar detection. Moving to a clean non-DFS channel sidesteps the incompatibility.

1. Log into your router's admin page and find the 5GHz wireless settings.
2. Change the channel from **Auto** to a fixed non-DFS channel: **36**, **40**, **44**, or **48**.
3. Set channel width to **80MHz** (or 40MHz for testing) rather than 160MHz — narrower widths negotiate more reliably.
4. Save, let the router restart its radio, and attempt the 5GHz connection from the laptop.
5. If it connects solidly, the driver/channel combination was the issue — check for router firmware updates as the long-term fix.

### Fix 6: Update router firmware and check 24H2 cumulative updates

Both ends of the handshake matter. An old router firmware plus a new 24H2 driver is a classic mismatch; meanwhile, Microsoft shipped 24H2 wireless fixes in cumulative updates.

1. Install all pending Windows updates (**Settings > Windows Update**) — note the build number before and after.
2. Check your router manufacturer's site for firmware updates and install them.
3. After both updates, forget the network once more (Fix 1) and reconnect fresh.
4. Test 5GHz stability for a day of normal use before declaring victory.
5. If problems persist, check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for documented 24H2 wireless regressions affecting your adapter — and see [our 24H2 Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/) for the same update's parallel wireless-stack issues.

### Fix 7: Reset the network stack and test the hardware

If driver, settings, channel, and firmware all check out, reset Windows' network stack wholesale — then verify the radio hardware with a live USB.

1. In an elevated Command Prompt, run `netsh winsock reset` and `netsh int ip reset`, then restart.
2. Go to **Settings > Network & internet > Advanced network settings > Network reset** and reset.
3. Reconnect to the 5GHz network fresh after the reset.
4. Boot an Ubuntu live USB and test 5GHz there — if Linux connects fine, the Windows driver stack is the fault; try an older manufacturer driver version.
5. If Linux also fails on 5GHz while 2.4GHz works, the radio's 5GHz chain has a hardware fault — the M.2 wireless card is replaceable on most laptops; as a workaround, a USB Wi-Fi 6 adapter restores full 5GHz immediately.

## Closing

The 2.4GHz-works/5GHz-doesn't pattern after 24H2 is a driver-and-settings problem wearing a router-problem costume. Forget the cached profile, set the preferred band and VHT mode explicitly, install the manufacturer's 24H2-validated Wi-Fi driver, tame the power settings, and check the router's channel — in that order. One of those layers is where 24H2 broke your 5GHz, and the fix at that layer is permanent. And once 5GHz is stable, lock the working driver against Windows Update; the next "helpful" generic driver is how this whole story started.
