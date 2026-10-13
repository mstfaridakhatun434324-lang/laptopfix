---
title: "How to Fix a Wi-Fi Adapter Not Showing Up on Windows 11 24H2"
slug: how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2
date: 2026-09-07
categories: ["drivers"]
tags: ["wifi adapter not showing", "wifi missing windows 11", "wireless driver fix"]
description: "Wi-Fi adapter not showing up on Windows 11 24H2? Bring back the missing wireless adapter with driver reinstalls, BIOS checks, and hardware resets."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my Wi-Fi adapter disappear after the 24H2 update?"
    a: "The 24H2 update sometimes installs an incompatible wireless driver or fails the driver migration entirely, leaving the adapter undetected. In other cases the adapter is present but hidden in Device Manager. Reinstalling the manufacturer's wireless driver resolves most disappearances Download the driver on another device and transfer it via USB if the laptop has no connectivity, since you cannot fetch it on the affected machine."
  - q: "How do I know if the adapter is disabled or actually missing?"
    a: "Open Device Manager and click View > Show hidden devices. If the Wi-Fi adapter appears grayed out, it is disabled or disconnected — right-click and enable it. If it does not appear even as hidden, Windows cannot see the hardware at all, pointing to a driver, BIOS, or hardware issue."
  - q: "Can a BIOS setting hide the Wi-Fi adapter?"
    a: "Yes. Many laptops have a BIOS toggle for the wireless LAN device, and BIOS updates sometimes reset it to disabled. Entering the BIOS setup and re-enabling wireless is a quick check that resolves a surprising number of missing-adapter cases."
  - q: "Is a missing Wi-Fi adapter a hardware failure?"
    a: "Not usually. True hardware failure is the last resort diagnosis. Most missing adapters are driver migrations gone wrong, BIOS toggles, or power-management states. Only suspect the physical card after exhausting the software fixes and a BIOS check Work through driver reinstallation, BIOS toggles, and power settings first; the physical card is the last thing to blame, not the first."
---

No Wi-Fi icon, no networks list, and no wireless adapter in Device Manager — on Windows 11 24H2 this "vanished adapter" problem strands you without internet on the very machine you need to research the fix. The adapter has not necessarily failed; 24H2's driver migration is notoriously rough on wireless drivers from Intel, MediaTek, and Realtek, and the adapter often just needs to be re-detected and re-driven.

The diagnostic path is: confirm whether Windows sees the hardware at all, then work from driver reinstallation through BIOS checks to hardware resets. Each step below narrows the cause, so follow them in order.

## Why this happens

- **Failed driver migration in 24H2:** The update does not carry the wireless driver across correctly, leaving the adapter driverless and hidden.
- **Incompatible generic driver installed:** 24H2 substitutes a basic driver that cannot initialize the specific wireless chip.
- **Adapter disabled in Device Manager:** The migration leaves the adapter in a disabled state that hides it from the network UI.
- **Wireless disabled in BIOS:** A BIOS toggle for the WLAN device gets switched off, sometimes by the update process itself.
- **Power management deep-sleep:** Aggressive power settings put the adapter in a state Windows cannot wake it from.
- **Loose M.2 wireless card:** Physical jolts can unseat the M.2 Wi-Fi card or detach its antenna leads.
- **Fast startup caching a bad state:** The hibernation-based fast startup preserves a broken adapter state across reboots.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices and re-enable the adapter

First, find out whether the adapter is hidden rather than gone.

1. Open **Device Manager** and click **View > Show hidden devices**.
2. Expand **Network adapters** and look for your Wi-Fi adapter — it may appear grayed out.
3. If you find it grayed out, right-click and choose **Enable device**.
4. If it appears with a warning icon, note the error code (Code 10, Code 43) — it guides the driver fixes below.

A grayed-out adapter that enables successfully means the problem was just a disabled state, and your Wi-Fi should return immediately.

### Fix 2: Reinstall the wireless driver from the manufacturer

The core fix for 24H2 migration failures.

1. Identify your wireless chip: Intel, MediaTek, Realtek, or Qualcomm. The hidden Device Manager entry or your laptop's spec sheet tells you.
2. On another device, download the wireless driver for your exact laptop model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/) — or the Intel Driver & Support Assistant for Intel cards. Transfer it via USB.
3. In Device Manager, right-click the adapter (show hidden devices first), choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
4. Run the downloaded installer and restart.

Vendor-matched drivers initialize the specific radio correctly where 24H2's generic driver fails. If Wi-Fi appears but will not stay connected, our [Wi-Fi 6 troubleshooting guide](/articles/best-way-to-fix-wifi-6-not-working-on-laptop/) covers the next layer of issues.

### Fix 3: Run the network reset

When the adapter exists but the network stack around it is broken, reset everything.

1. Go to **Settings > Network & internet > Advanced network settings > Network reset**.
2. Click **Reset now** and confirm. The laptop restarts.
3. After booting, check Device Manager for the adapter and rejoin your Wi-Fi network.

Network reset reinstalls all adapters and clears corrupted configuration. Have your Wi-Fi password ready — saved networks are wiped.

### Fix 4: Check the BIOS wireless toggle

Firmware can hide the adapter from Windows entirely.

1. Restart and enter BIOS/UEFI setup (**F2**, **Del**, or **F12**).
2. Look under **Advanced**, **System Configuration**, or **Devices** for **Wireless LAN**, **WLAN**, or **Wi-Fi** toggles.
3. Ensure wireless is **Enabled**, save, and boot into Windows.
4. Recheck Device Manager.

While in the BIOS, note whether a recent BIOS update occurred — if the adapter vanished right after one, the update likely flipped the toggle. Also see our guide on [Wi-Fi completely disappearing](/articles/best-way-to-fix-wifi-disappeared-from-laptop/) for the UI-side symptoms.

### Fix 5: Disable fast startup and power-manage the adapter

Stale cached states and power saving both hide adapters.

1. Go to **Control Panel > Power Options > Choose what the power buttons do**, click **Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
2. In Device Manager, open the Wi-Fi adapter's **Properties > Power Management** tab and uncheck **Allow the computer to turn off this device to save power**.
3. Shut down fully (not restart), wait 10 seconds, and power on.

The full shutdown with fast startup off forces Windows to re-enumerate hardware from scratch instead of restoring a cached broken state.

### Fix 6: Reseat the M.2 wireless card (if comfortable)

For adapters that survive every software fix, check the physical card.

1. Power off, unplug, and remove the bottom panel (check your model's service manual — some laptops have warranty seals).
2. Locate the M.2 wireless card, remove its retaining screw, and reseat it firmly. Reattach the antenna leads (black and white wires) if loose.
3. Reassemble and boot.

Only attempt this if you are comfortable with laptop internals and your warranty allows it. A card that was slightly unseated explains an adapter that vanished suddenly after a drop or bump.

### Fix 7: Test with a USB Wi-Fi adapter to isolate hardware failure

The final diagnostic: determine whether the internal card is dead.

1. Plug in any USB Wi-Fi adapter. If it works immediately, Windows' wireless stack is fine and the internal card is the problem.
2. If the internal card is under warranty, contact the manufacturer for a replacement — M.2 Wi-Fi cards are inexpensive and usually user-replaceable.
3. As a permanent workaround, a nano USB Wi-Fi adapter costs little and works reliably.

If even the USB adapter fails, the issue is system-wide — consider the Windows Update catalog for alternative driver versions or, as a last resort, an in-place Windows repair install.

## Closing

A Wi-Fi adapter that does not show up on Windows 11 24H2 is usually a driver migration casualty, not dead hardware. Reveal hidden devices, reinstall the manufacturer's wireless driver, check the BIOS toggle, and kill fast startup — that sequence restores the adapter on the overwhelming majority of laptops, no new hardware required.
