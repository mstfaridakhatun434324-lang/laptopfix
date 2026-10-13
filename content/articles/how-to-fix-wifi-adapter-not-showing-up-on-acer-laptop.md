---
title: "How to Fix Wi-Fi Adapter Not Showing Up on an Acer Laptop"
slug: "how-to-fix-wifi-adapter-not-showing-up-on-acer-laptop"
date: "2026-09-24"
categories: ["drivers"]
tags: ["wifi adapter missing", "acer laptop", "wireless not detected", "windows 11", "network driver"]
description: "Wi-Fi adapter not detected on your Acer laptop? Bring it back with hidden-device scans, driver reinstalls, BIOS checks, and Acer-specific troubleshooting."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-on-acer-laptop.webp"
faqs:
  - q: "Why is there no network adapter at all in Device Manager on my Acer?"
    a: "When no wireless adapter appears even with hidden devices shown, Windows cannot see the hardware. The usual causes are the adapter being disabled in the BIOS, a driver that failed so badly Windows cannot enumerate the device, or the WLAN service being broken. On Acer laptops specifically, check the BIOS wireless setting and the function-key radio toggle first — both can hide the adapter completely."
  - q: "My Acer shows only Ethernet and Bluetooth, no Wi-Fi. What does that mean?"
    a: "Ethernet working while Wi-Fi is absent means the problem is specific to the wireless adapter, not general networking. Bluetooth appearing is actually a useful clue: on combo cards, Bluetooth enumerates separately, so its presence suggests the card has power and the Wi-Fi-specific driver is the failure point. Reinstall the wireless driver from Acer's support site for your exact model."
  - q: "Can the Acer BIOS disable the Wi-Fi adapter?"
    a: "Yes. Acer BIOS setups (usually entered with F2) include wireless device settings on many models, particularly Aspire and Nitro lines. If wireless is disabled there, no Windows troubleshooting will help — the card is invisible to the OS. Enable it, save, and exit. Also check for a physical wireless switch on older Acer models, which does the same thing at the hardware level."
  - q: "How do I download Acer Wi-Fi drivers without internet?"
    a: "Use another device — a phone, tablet, or second computer — to visit Acer's support site, enter your serial number or model, and download the wireless LAN driver. Transfer it on a USB stick. Alternatively, enable USB tethering on your phone to give the laptop temporary internet, then download the driver directly. Phone tethering is usually the faster option."
---

On Acer laptops — Aspire, Swift, Nitro, and Predator models alike — the Wi-Fi adapter sometimes stops showing up entirely: not in Settings, not in the taskbar, and not even in Device Manager's Network adapters section. Because Acer uses wireless cards from Intel, MediaTek, Realtek, and Qualcomm across its lineup, the fix is rarely Acer-specific — but the diagnostic path has a few Acer-flavored steps worth knowing, from the F2 BIOS to Acer Care Center's driver updates.

Work through this guide in order. The early steps take seconds and catch the most common causes; the later ones dig into drivers and firmware.

## Why this happens

- **Adapter disabled in Device Manager:** The wireless device can end up disabled, hiding it from normal Device Manager views.
- **Wireless disabled in Acer BIOS:** The firmware toggle removes the card from the OS entirely.
- **Driver failure after Windows Update:** An incompatible wireless driver can fail enumeration so badly the device does not list at all.
- **Function-key radio toggle:** Acer's Fn + F3 (on many models) toggles the wireless radio; it is easy to hit accidentally.
- **WLAN AutoConfig service failure:** Without this service, Windows may not display wireless adapters properly.
- **Corrupted driver store:** Failed updates leave fragments that block the adapter from enumerating.
- **Fast Startup locking device state:** The hibernation snapshot preserves a broken enumeration across reboots.
- **Dead wireless card:** Electrical failure of the M.2 module — the final possibility after software is ruled out.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the radio toggle and airplane mode

Start with the physical and OS-level radio switches.

1. Press Fn + F3 (the wireless key on most Acer laptops) and watch for the Wi-Fi indicator light.
2. Click the taskbar system tray and make sure airplane mode is off — toggle it on and off once to unstick it.
3. Open Settings > Network & internet and note whether a Wi-Fi section exists at all.
4. Run the Network troubleshooter from Settings > System > Troubleshoot > Other troubleshooters.
5. If the troubleshooter reports no wireless adapter found, the adapter-level diagnosis below is the right path.

### Fix 2: Scan Device Manager with hidden devices shown

Find out whether Windows sees the hardware in any form.

1. Press Win + X, open Device Manager, and click View > Show hidden devices.
2. Expand Network adapters and look for any wireless entry — Intel, MediaTek, Realtek, Qualcomm, or a greyed-out unknown device.
3. Also check "Other devices" for unknown devices with yellow warnings — your adapter may be listed there without a driver.
4. If you find a greyed-out wireless adapter, right-click it and choose Enable device.
5. Right-click your computer name at the top and choose "Scan for hardware changes" to force re-detection.
6. Note exactly what you find — it determines whether this is a disabled device, a driverless device, or an invisible one.

### Fix 3: Restart WLAN AutoConfig and related services

A broken wireless service can suppress the adapter's appearance.

1. Press Win + R, type `services.msc`, and press Enter.
2. Set "WLAN AutoConfig" to Automatic and start (or restart) it.
3. Verify "Network Connections", "Network List Service", and "Internet Connection Sharing" are running.
4. Reopen Device Manager and rescan for hardware changes.
5. Check Settings > Network & internet for a returning Wi-Fi section.
6. If services refuse to start, the underlying driver is usually the cause — continue below.

### Fix 4: Reinstall the wireless driver from Acer

Acer-tuned drivers are the correct replacement for whatever Windows Update installed.

1. Identify your exact Acer model and serial number (sticker on the bottom or `msinfo32`).
2. On another device, visit Acer's support site, enter your model, and download the Wireless LAN driver.
3. Transfer it via USB, or use phone USB tethering for direct download on the laptop.
4. In Device Manager, uninstall any wireless or unknown-device entries with driver removal ticked.
5. Install the Acer driver package and restart.
6. Verify the adapter appears in Device Manager without warnings and that networks are visible.
7. For broader context on vanished Wi-Fi, our [Windows 11 Wi-Fi disappeared guide](/articles/how-to-fix-wifi-disappeared-from-laptop-on-windows-11/) covers the OS-level steps in parallel.

### Fix 5: Update via Acer Care Center

Acer's own utility can find the right driver without manual model hunting.

1. Open Acer Care Center (preinstalled on most Acer laptops; downloadable from Acer's site if missing).
2. Go to the update or driver section and check for wireless driver updates.
3. Install what it offers and restart when prompted.
4. This is particularly useful when you are unsure which wireless card your Acer contains — the tool detects it automatically.
5. After updating, confirm the adapter is present and stable across a sleep-wake cycle.

### Fix 6: Check the Acer BIOS wireless setting

If the adapter is invisible even as a hidden or unknown device, the BIOS may be hiding it.

1. Restart and press F2 repeatedly to enter the Acer BIOS setup.
2. Navigate to the Main or Advanced tab and look for wireless, WLAN, or network device settings.
3. Make sure the wireless device is enabled — enable it if disabled, then save and exit.
4. While in the BIOS, note whether any wireless hardware is listed in the information page.
5. Boot into Windows and rescan Device Manager for hardware changes.
6. Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) covers the OS-side network adapter steps that follow.

### Fix 7: Disable Fast Startup and drain residual power

Clear any locked hardware state that survives normal reboots.

1. Open Control Panel > Power Options > Choose what the power buttons do.
2. Click "Change settings that are currently unavailable" and uncheck "Turn on fast startup".
3. Shut down fully, unplug the charger, and hold the power button for 15 seconds.
4. On models with a battery reset pinhole (many Acers have one on the bottom), press it with a paperclip for 5 seconds.
5. Power on and check Device Manager — adapters stuck in failed power states often reappear after this.
6. A [Code 10 error](/articles/how-to-fix-wifi-driver-code-10-error-on-lenovo-laptop/) is the next thing to look for if the adapter appears but will not start.

### Fix 8: Test the hardware with a live USB

Confirm whether the wireless card itself is alive.

1. Create an Ubuntu live USB on another computer and boot the Acer from it.
2. Check the Wi-Fi settings for available networks and the adapter's presence.
3. Wi-Fi works in Linux: the card is fine — focus on Windows drivers or consider a repair install.
4. No Wi-Fi in Linux either: the M.2 card has likely failed electrically.
5. On many Acer models the wireless card is socketed and replaceable — check your warranty before opening the machine; otherwise a USB Wi-Fi adapter is the simple workaround.
6. Intel card owners can keep drivers fresh with the official [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) once the adapter is visible again.

## Closing

A Wi-Fi adapter that will not show up on an Acer laptop is a visibility problem with a clear diagnostic ladder: radio toggles, hidden devices, services, Acer's own driver, the BIOS, power state, and finally hardware. Most cases end at the driver reinstall — Acer's tuned wireless package plus a rescan brings the adapter back. And once it is back, keep that Acer driver installed and stop Windows Update from swapping it, so the adapter stays visible for good.
