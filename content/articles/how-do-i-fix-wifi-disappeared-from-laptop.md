---
title: "How to Fix WiFi That Vanished From Your Laptop"
slug: how-do-i-fix-wifi-disappeared-from-laptop
date: 2026-10-07
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi option", "wireless adapter", "windows 11", "driver fix"]
description: "WiFi option completely gone from Windows? Restore the missing wireless adapter with this diagnostic flow — from airplane mode to driver repair."
thumbnail: "/images/thumbs/how-do-i-fix-wifi-disappeared-from-laptop.webp"
faqs:
  - q: "Why did the WiFi option disappear from my laptop?"
    a: "The wireless adapter's driver failed to load, so Windows no longer sees any WiFi hardware and hides the option entirely. This usually follows a Windows update that installed an incompatible driver. Reinstalling the correct driver brings the adapter — and the WiFi option — back."
  - q: "How do I get the WiFi icon back on the taskbar?"
    a: "The icon returns automatically once the wireless adapter is working again. Focus on restoring the adapter in Device Manager rather than the icon itself. If the adapter works but the icon is missing, check Settings > System > Notifications > Quick Settings to re-add it."
  - q: "Can airplane mode make WiFi disappear completely?"
    a: "Airplane mode normally just disconnects, but a stuck airplane-mode state combined with a physical wireless switch can make the adapter vanish from Device Manager. Toggle airplane mode off, check any physical WiFi switch, and restart before assuming a driver problem."
  - q: "What if the wireless adapter is missing from Device Manager?"
    a: "First check View > Show hidden devices — a greyed-out adapter means the driver knows about hardware it can't reach. If it's absent even there, check the BIOS for a disabled wireless toggle, then suspect a failed card or loose M.2 connection."
---

There's a meaningful difference between WiFi not working and WiFi being gone. When the WiFi option disappears from Settings and the taskbar entirely, Windows isn't failing to connect — it's failing to see the wireless hardware at all. That distinction focuses the entire repair: you're not fixing a connection, you're resurrecting an adapter.

The causes run from a stuck airplane mode through driver failure to a BIOS-disabled radio. Work the list in order and the adapter comes back.

It helps to think of the wireless adapter as having two separate "existences" in Windows. The first is the hardware device itself, which appears in Device Manager when the driver successfully talks to the card. The second is the WiFi option in Settings and the taskbar, which only appears when Windows' network service can see a working wireless device. A surprising number of "disappeared WiFi" cases are actually a gap between these two: the adapter exists in Device Manager with a warning icon, but the Settings UI hides WiFi because the device isn't functional. That gap is why this guide starts in Device Manager rather than in Settings — the adapter's status there tells you precisely which half of the problem you're dealing with.

## Why this happens

- **Wireless driver failed to load:** An incompatible or corrupted driver means Windows can't initialize the card, so it hides WiFi completely.
- **Airplane mode stuck on:** A wedged airplane-mode state can suppress the adapter at a level Device Manager reflects as missing.
- **Physical WiFi switch off:** Some laptops have a hardware switch or Fn-key toggle that electrically disables the radio.
- **Adapter disabled in BIOS:** A BIOS wireless toggle switched off removes the hardware from the OS entirely.
- **Power management parked the card:** Aggressive power saving can leave the adapter in a state Windows stops enumerating.
- **Windows Update removed the driver:** Major updates occasionally drop the wireless driver package during migration.
- **Corrupted network adapter enumeration:** Damaged registry entries prevent Windows from listing the adapter.
- **Failed wireless card:** A dead M.2 card or loose connection removes the hardware for real.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle airplane mode and check switches

1. Press **Windows + A** and toggle **Airplane mode** on, wait ten seconds, then off.
2. Check for a **physical WiFi switch** on the laptop's edges and any **Fn-key** wireless toggle.
3. Restart the laptop after toggling — a stuck radio state often needs a reboot to clear.
4. If WiFi reappears, the radio was simply switched off; if not, the adapter itself needs attention.

### Fix 2: Inspect Device Manager

1. Open **Device Manager** and look under **Network adapters** for your wireless card.
2. If it's missing, click **View → Show hidden devices** — a greyed-out adapter means the driver can't reach the hardware.
3. Check **Other devices** for an **Unknown device** or **Network Controller** — that's your card with a failed driver.
4. What you find here determines everything downstream: warning icon means driver repair, total absence means BIOS or hardware.

### Fix 3: Scan for hardware changes

1. In **Device Manager**, click **Action → Scan for hardware changes**.
2. Watch whether the wireless adapter reappears, even briefly.
3. If it appears then vanishes, the driver is crashing on load — proceed to driver repair.
4. If nothing appears, continue to the BIOS check before concluding hardware failure.

### Fix 4: Reinstall the wireless driver

1. If the adapter is visible (even with a warning), right-click → **Uninstall device**, checking driver deletion.
2. Restart and let Windows reinstall its inbox driver, then check for the WiFi option.
3. If the adapter was missing entirely, download the manufacturer's wireless driver on another device, transfer via USB, and install.
4. OEM drivers from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support pages include the firmware your card needs. For the update-specific variant, see [WiFi disappeared in Windows 11](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/).

### Fix 5: Check the BIOS wireless toggle

1. Enter **BIOS/UEFI setup** and find the **Wireless**, **WLAN**, or **WiFi** toggle (often under Security or Devices).
2. Make sure it's **enabled** — BIOS updates and IT policies can flip it off silently.
3. Save, exit, and check Device Manager again.
4. A BIOS-disabled radio is invisible to every Windows fix; this check saves hours of pointless driver work.

### Fix 6: Disable Fast Startup and cold boot

1. Turn off **Fast Startup** in **Control Panel → Power Options → Choose what the power buttons do**.
2. Shut down fully, unplug the charger, wait thirty seconds, and power on.
3. A cold boot forces full hardware re-enumeration, which can rediscover an adapter that warm reboots keep missing.
4. On some laptops, holding the power button for a full shutdown (not restart) is what finally brings the card back.

### Fix 7: Reset the network stack

1. Open **Terminal as administrator** and run:
   `netsh winsock reset`
   `netsh int ip reset`
2. Then go to **Settings → Network & internet → Advanced network settings → Network reset** and reset.
3. Restart and check for the WiFi option.
4. This repairs corrupted adapter enumeration without touching drivers — useful when the hardware is present but Windows won't list it.

### Fix 8: Test the hardware

1. Boot a **Linux live USB** — if WiFi appears there, the card is alive and Windows is the problem.
2. If the laptop has a removable bottom cover, check that the **M.2 wireless card** is seated and its antenna wires are connected.
3. Check Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) for wireless known issues tied to your update version.
4. If Linux also finds no wireless hardware, the card has failed — replacements are inexpensive on socketed models. For the no-icon variant of this problem, see [WiFi missing with no option shown](/articles/wifi-disappeared-windows-11-no-wifi-option/).

## Closing

A vanished WiFi option is Windows saying it can't see the radio — so make it see the radio again. Toggle the switches, scan Device Manager, reinstall the driver, check the BIOS, and cold-boot. The Linux live-USB test delivers the final verdict when software fixes run out. In most cases, though, the adapter was never gone — just waiting for the right driver to wake it up. Once it's back, take a moment to prevent the encore: note the working driver version, hide the bad update that caused the disappearance, and remember that the BIOS toggle exists. Vanished WiFi is one of those problems that feels catastrophic and turns out to be a twenty-minute fix — but only if you check the layers in order instead of panicking.
