---
title: "Wi-Fi Disappeared From Your Laptop? Here's How to Fix It"
slug: how-to-fix-wifi-disappeared-from-laptop-reddit
date: 2026-10-04
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi option", "wifi icon missing", "windows 11 wifi gone"]
description: "Wi-Fi option completely gone from your laptop? This is the full checklist Reddit threads recommend: driver fixes, network resets, and BIOS checks."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop-reddit.webp"
faqs:
  - q: "Why is there no Wi-Fi option at all in Settings?"
    a: "When the Wi-Fi entry is missing from Settings and Quick Settings entirely, Windows cannot see a working wireless adapter. The cause is usually a failed, disabled, or missing driver — the adapter may show a warning in Device Manager or be hidden there. Less often, the card is disabled in the BIOS or has failed physically."
  - q: "Why do Reddit threads always suggest a network reset first?"
    a: "Because the built-in Network reset (Settings > Network & internet > Advanced network settings) reinstalls every network adapter and resets all networking components in one shot. It resolves a huge share of disappeared-Wi-Fi cases caused by corrupted adapter states, and it takes five minutes with no downloads required."
  - q: "Can airplane mode make Wi-Fi disappear completely?"
    a: "A stuck airplane mode can hide the Wi-Fi toggle and the network list, which looks identical to a driver failure. Check Quick Settings and the physical wireless switch or Fn key on your laptop. If airplane mode refuses to turn off, that is a separate fault — fix the airplane mode lock first, then reassess."
  - q: "My Wi-Fi vanished right after a Windows update. What happened?"
    a: "Windows Update likely replaced your wireless driver with an incompatible version or left the old one in a broken state. The fix is to roll back the driver in Device Manager, or download the current driver from the laptop or card maker's site. Blocking driver updates via Windows Update afterward prevents a repeat."
---

This is one of the most posted-about laptop problems on Reddit: you open your laptop and the Wi-Fi option is simply gone. Not disconnected — gone. No toggle in Quick Settings, no Wi-Fi page in Settings, sometimes not even an adapter in Device Manager. It feels catastrophic, but in the overwhelming majority of cases it is a software problem with a straightforward fix.

The threads converge on the same checklist, and it works: verify the radio is not switched off, reset the network stack, fix the driver, and check the BIOS. The order matters — the quick wins come first because they resolve most cases, and the deeper driver surgery is only needed when the easy steps fail.

Follow the steps below in order. Each fix includes how to tell whether it worked, so you know when to move on.

## Why this happens

- **Wireless driver failed or was replaced by Windows Update**, leaving the adapter unable to start.
- **Adapter disabled in Device Manager** or stuck in a corrupted state after sleep or hibernation.
- **Airplane mode stuck on**, hiding the Wi-Fi toggle and network list entirely.
- **Physical wireless switch or Fn key** toggled off — common on business laptops with a side switch.
- **Network stack corruption** — Winsock or TCP/IP damage that takes the adapter down with it.
- **Wi-Fi card disabled in the BIOS**, sometimes flipped by a firmware update or IT policy.
- **Failed wireless card hardware**, the least common cause but the one to check when nothing else works.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode and the physical switch

Open Quick Settings (Win + A) and make sure airplane mode is off. Then check your laptop for a physical wireless switch — usually on the side or front edge — and the Fn wireless key (often Fn + F2 or a radio-tower icon). A surprising number of 'disappeared Wi-Fi' cases end here. If airplane mode is stuck on and will not toggle off, fix that first before continuing.

1. Press Win + A and turn airplane mode off.
2. Check for a physical wireless switch on the laptop's edges.
3. Press the Fn + wireless function key once.
4. Wait 30 seconds and check whether the Wi-Fi toggle returns.

### Fix 2: Run the Windows network reset

The built-in network reset reinstalls all network adapters and returns every networking component to defaults. It is the highest-yield single step for vanished Wi-Fi. Microsoft documents it in the [Windows support hub](https://support.microsoft.com/en-us/windows). Note that it forgets saved Wi-Fi passwords, so have yours handy.

1. Open Settings > Network & internet > Advanced network settings.
2. Click Network reset, then Reset now, and confirm.
3. Restart when prompted and wait for Windows to reinstall the adapters.
4. Check whether the Wi-Fi option has returned.

### Fix 3: Re-enable and reinstall the Wi-Fi adapter driver

Open Device Manager (Win + X) and expand Network adapters. If the wireless adapter is present but greyed out, right-click and enable it. If it shows a warning, uninstall it — ticking the box to delete the driver — then restart so Windows reinstalls it. If the adapter is missing entirely, click View > Show hidden devices; a greyed-out entry there confirms Windows sees the hardware but cannot start it. The [missing Wi-Fi option guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers additional Device Manager scenarios.

1. Open Device Manager and expand Network adapters.
2. Enable the adapter if greyed out; uninstall it (deleting the driver) if it shows a warning.
3. Restart the laptop and let Windows reinstall the driver.
4. If the adapter was hidden, note whether it now appears normally.

### Fix 4: Install the driver from the manufacturer

If Windows' own reinstall does not bring Wi-Fi back, get the driver from the source: your laptop maker's support page for your exact model, or Intel/Realtek/Mediatek for the card itself. Install the chipset driver first on Intel machines, then the wireless driver. This fixes the cases where Windows Update installed a driver that cannot initialize the card.

1. Identify your wireless card model in Device Manager or the laptop specs.
2. Download the latest driver from the laptop maker or card maker.
3. Install the chipset driver first if it is an Intel-based laptop, then the Wi-Fi driver.
4. Reboot and verify the Wi-Fi toggle returns.

### Fix 5: Reset the network stack from the terminal

When the adapter is present but no networks appear, corrupted Winsock or TCP/IP catalogs are often responsible. These commands rebuild them from scratch. Run them from an elevated terminal, restart, and give Windows a minute after boot to re-enumerate the adapter.

1. Open Terminal (Admin) from Win + X.
2. Run `netsh winsock reset` and `netsh int ip reset`.
3. Run `ipconfig /flushdns` and restart the laptop.
4. Check Quick Settings for the Wi-Fi toggle after reboot.

### Fix 6: Check the BIOS for a disabled wireless card

Reboot into the BIOS (F2, Del, or F10 depending on brand) and look for wireless, WLAN, or Wi-Fi settings. If the card is disabled there, no Windows fix can help — enable it, save, and boot. If the adapter still does not appear in Device Manager afterward, compare against the [adapter-not-showing checklist](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) for the deeper hardware tests.

1. Reboot into the BIOS setup.
2. Find the wireless / WLAN setting and set it to Enabled.
3. Save and exit, then boot into Windows.
4. Confirm the adapter appears in Device Manager.

### Fix 7: Test the hardware

If the adapter is invisible in Device Manager (even with hidden devices shown) and absent from the BIOS, the card may have failed or worked loose. Boot a Linux live USB: Wi-Fi working there proves the hardware is fine and the problem is Windows. No Wi-Fi anywhere means hardware — reseat the card if it is socketed and warranty allows, or use a USB Wi-Fi adapter as a workaround.

1. Boot a Linux live USB and test Wi-Fi there.
2. If socketed and warranty permits, reseat the wireless card.
3. Try a USB Wi-Fi adapter to confirm the OS side works.
4. Arrange a wireless card replacement if the hardware is dead.

## Closing

Disappeared Wi-Fi looks dramatic but is usually a ten-minute fix: the radio switch, the network reset, or a driver reinstall covers the vast majority of cases. The key discipline is checking in order — physical switches before software, software before BIOS, BIOS before hardware — so you do not replace a card that only needed a driver. Keep the manufacturer's driver handy afterward, because Windows Update is the most common repeat offender.
