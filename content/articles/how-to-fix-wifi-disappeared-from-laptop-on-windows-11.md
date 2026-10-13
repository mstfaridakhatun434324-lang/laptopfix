---
title: "How to Fix Wi-Fi Disappeared From Your Laptop on Windows 11"
slug: "how-to-fix-wifi-disappeared-from-laptop-on-windows-11"
date: "2026-09-19"
categories: ["drivers"]
tags: ["wifi disappeared", "wireless adapter missing", "windows 11", "network driver", "no wifi"]
description: "Wi-Fi option completely gone on Windows 11? Restore it with adapter checks, driver reinstalls, network resets, and BIOS verification — step by step."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop-on-windows-11.webp"
faqs:
  - q: "Why did the Wi-Fi option completely vanish from Windows 11?"
    a: "The Wi-Fi option disappears when Windows can no longer see the wireless adapter, which happens when its driver crashes, gets replaced by an incompatible Windows Update, or the adapter is disabled in Device Manager or BIOS. Less commonly, the WLAN AutoConfig service stops or the card itself fails. Because the cause ranges from a toggled setting to dead hardware, work through the diagnostic steps in order rather than guessing."
  - q: "My Wi-Fi disappeared after a Windows 11 update. How do I undo it?"
    a: "Open Device Manager, find your wireless adapter under Network adapters, open its Properties, and use the Driver tab's Roll Back Driver button if available. If rollback is greyed out, uninstall the device with driver removal ticked, restart, and install the driver from your laptop maker's support site. Then disable automatic driver updates so Windows does not reinstall the bad version overnight."
  - q: "The Wi-Fi adapter is missing even in Device Manager. Is the card dead?"
    a: "Not necessarily. First enable hidden devices in Device Manager, then check the BIOS to confirm the wireless device is enabled. A missing adapter with hidden devices shown and Wi-Fi enabled in BIOS, persisting after a driver reinstall and a full power drain, is when hardware failure becomes likely. Test with a Linux live USB before concluding the card is dead."
  - q: "Can airplane mode permanently remove the Wi-Fi option?"
    a: "No, airplane mode only disables the radio temporarily; turning it off should restore Wi-Fi. If the Wi-Fi option stays missing after airplane mode is off, something else is wrong — usually the driver or the adapter's enabled state. However, a stuck airplane mode toggle (often after a failed update) can mimic this, so toggling it on and off once is still a worthwhile first check."
---

When Wi-Fi disappears from Windows 11 entirely — no icon in the taskbar, no Wi-Fi page in Settings, no adapter in Device Manager — it feels like the hardware evaporated. In practice, the wireless card is almost always still physically present; Windows has just lost the ability to see it. The causes form a clear ladder from trivial (airplane mode, disabled adapter) to serious (dead card), and this guide climbs it one rung at a time so you find your problem quickly.

Grab an alternate internet source before you start if possible — a phone USB tether works perfectly — because several fixes involve downloading drivers.

## Why this happens

- **Driver replaced or corrupted by Windows Update:** The most common cause; an incompatible wireless driver leaves the adapter unrecognized.
- **Adapter disabled in Device Manager:** The device can end up disabled by troubleshooting tools, policies, or failed updates.
- **Wireless disabled in BIOS:** The firmware toggle hides the card from Windows completely.
- **WLAN AutoConfig service stopped:** Without this service, Windows shows no Wi-Fi option even with a healthy adapter.
- **Airplane mode stuck on:** A failed update can leave the radio locked off with no visible toggle.
- **Power management disabling the card:** Aggressive power saving can take the adapter offline permanently until reset.
- **Corrupted network stack:** Damaged Winsock or TCP/IP data can prevent the Wi-Fi UI from appearing.
- **Failed wireless card:** Electrical failure of the M.2 module — uncommon, but the end of the diagnostic road.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode, the function key, and Settings

Rule out the radio being simply switched off.

1. Click the taskbar network/volume/battery area and confirm airplane mode is off; toggle it on and off once to unstick it.
2. Press your laptop's wireless function key (often F12 with an antenna icon) and watch for an indicator light.
3. Open Settings > Network & internet and look for a Wi-Fi entry — note whether the page is missing or just shows no networks.
4. Run Settings > System > Troubleshoot > Other troubleshooters > Network and Internet.
5. If the troubleshooter says no wireless adapter was found, continue — that confirms the adapter-level problem.

### Fix 2: Inspect Device Manager thoroughly

Find out exactly what state the adapter is in.

1. Press Win + X and open Device Manager.
2. Expand Network adapters and look for your wireless card (Intel, MediaTek, Realtek, or Qualcomm).
3. If it is absent, click View > Show hidden devices and look for greyed-out entries.
4. A greyed-out adapter means disabled or driverless — right-click and choose Enable device.
5. A yellow warning icon means a driver problem — double-click it and note the error code.
6. Complete absence, even hidden, means the OS cannot see the hardware at all — check the BIOS next.

### Fix 3: Restart the WLAN AutoConfig service

This service is the backbone of Wi-Fi in Windows; without it, no Wi-Fi UI appears.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find "WLAN AutoConfig", double-click it, and set Startup type to Automatic.
3. Click Start if it is stopped; if it is running, click Restart.
4. Also check that "Network Connections" and "Network List Service" are running.
5. Reopen Settings > Network & internet and see whether Wi-Fi has returned.
6. If the service will not stay running, note the error — it usually indicates the driver problem addressed below.

### Fix 4: Reinstall the wireless driver

The highest-success fix for vanished Wi-Fi: purge the broken driver completely.

1. In Device Manager, right-click the wireless adapter (or its hidden/greyed entry) and choose Uninstall device.
2. Tick "Attempt to remove the driver for this device" so Windows cannot reinstall the broken version.
3. Restart the laptop — Windows will detect the card and install its inbox driver.
4. Check whether Wi-Fi returns with the inbox driver before doing anything else.
5. If it does, install the manufacturer's driver package over it for full features and stability.
6. For the [Windows 10 variant of Wi-Fi 6 issues](/articles/how-to-fix-wifi-6-not-working-on-laptop-on-windows-10/), the same purge-and-reinstall logic applies.

### Fix 5: Install the manufacturer's driver package

The inbox driver proves the hardware works; the manufacturer's driver makes it work well.

1. Identify your exact laptop model (check the sticker on the bottom or run `msinfo32`).
2. On another device, download the wireless driver from the manufacturer's support site.
3. Transfer it via USB and install, choosing a clean install if offered.
4. Restart and confirm the adapter appears normally in Device Manager with no warnings.
5. Intel card owners can alternatively use the official [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for the latest generic package.
6. After a working driver is in place, consider disabling automatic [driver updates](/articles/how-to-disable-automatic-driver-updates-on-windows-11/) so Windows Update cannot break it again.

### Fix 6: Reset the network stack

When the adapter is healthy but the Wi-Fi UI still will not appear, reset Windows' networking.

1. Open Command Prompt as administrator.
2. Run `netsh winsock reset` and `netsh int ip reset`, then `ipconfig /flushdns`.
3. Alternatively, go to Settings > Network & internet > Advanced network settings > Network reset and click "Reset now".
4. Restart the laptop — the reset completes on reboot and clears all saved networks.
5. Reconnect to your Wi-Fi and verify the option persists after a restart.
6. Microsoft documents these resets on their [Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 7: Check the BIOS and disable Fast Startup

Confirm the firmware is not hiding the card, and clear any locked power state.

1. Restart into the BIOS (F2, F10, Del, or a manufacturer key) and find the wireless device setting.
2. Make sure WLAN/Wi-Fi is enabled; load setup defaults if the options are unclear.
3. In Windows, go to Control Panel > Power Options > Choose what the power buttons do, and uncheck "Turn on fast startup".
4. Shut down fully, unplug for 30 seconds, then boot fresh.
5. Check Device Manager again — cards hidden by BIOS or locked power states reappear here.

### Fix 8: Test the hardware directly

With software exhausted, determine whether the card itself has failed.

1. Boot an Ubuntu live USB and check whether Wi-Fi networks appear.
2. Wi-Fi works in Linux but not Windows: the hardware is fine — consider a Windows repair install.
3. Missing in both: the M.2 wireless card has likely failed.
4. If your model has a socketed card and warranty allows, reseat it and check the antenna leads.
5. Otherwise, a USB Wi-Fi adapter restores connectivity for a few dollars — the same workaround applies to [adapters not detected on other brands](/articles/how-to-fix-wifi-adapter-not-showing-up-on-acer-laptop/).

## Closing

Wi-Fi disappearing from Windows 11 is a visibility problem, not usually a hardware problem — the ladder runs from airplane mode through services, drivers, BIOS, and only finally the card itself. Most cases resolve at the driver reinstall step, and the single best prevention is keeping the manufacturer's wireless driver installed while blocking Windows Update from replacing it. Work the list in order, and your Wi-Fi will almost certainly be back before you reach the hardware step.
