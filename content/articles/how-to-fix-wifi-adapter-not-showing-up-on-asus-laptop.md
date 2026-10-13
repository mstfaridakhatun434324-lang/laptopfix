---
title: "Wi-Fi Adapter Not Showing Up on an ASUS Laptop? 7 Fixes That Work"
slug: how-to-fix-wifi-adapter-not-showing-up-on-asus-laptop
date: 2026-10-12
categories: ["drivers"]
tags: ["wifi", "network adapter", "asus", "device manager", "wireless"]
description: "Wi-Fi adapter missing from Device Manager on your ASUS laptop? 7 fixes to bring it back — BIOS toggles, driver reinstalls, and hardware checks."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-on-asus-laptop.webp"
faqs:
  - q: "Why is the Wi-Fi adapter missing from Device Manager on my ASUS laptop?"
    a: "Windows has lost contact with the wireless hardware. The usual causes on ASUS laptops: the wireless card is disabled in the BIOS, the driver is so corrupted Windows can't enumerate the device, or a Windows update installed an incompatible driver that fails to initialize. Less commonly, the M.2 wireless card has worked loose or failed physically."
  - q: "How do I enable Wi-Fi in the ASUS BIOS?"
    a: "Restart and press F2 or Del during the ASUS logo to enter BIOS setup. Look under the Advanced tab for onboard device or wireless configuration and make sure the WLAN controller is enabled. Save with F10 and boot into Windows — the adapter should reappear in Device Manager immediately if the BIOS toggle was the problem."
  - q: "My ASUS has a Wi-Fi hotkey. Could that hide the adapter?"
    a: "Yes. ASUS laptops use Fn + F2 (or a dedicated wireless key) to toggle the radio at firmware level. If it's stuck off, Windows sees no wireless hardware and the adapter vanishes from Device Manager. Press the combination, wait ten seconds, and check whether the adapter reappears before attempting any driver fixes."
  - q: "What if the adapter appears with an error code instead of missing?"
    a: "That's a simpler problem — Windows sees the hardware, so it's purely a driver issue. Note the error code in the device's Properties (Code 10, 31, and 43 are common), then uninstall the device and install the wireless driver from ASUS support for your exact model. Hardware failure is very unlikely when the device is visible."
---

No Wi-Fi icon, no wireless networks, and when you open Device Manager the wireless adapter isn't listed anywhere — not under Network adapters, not with a warning, nowhere. On an ASUS laptop, a completely missing Wi-Fi adapter means Windows can't see the wireless hardware at all, which puts the problem at the BIOS, driver, or hardware level rather than in your network settings.

This differs from Wi-Fi that's visible but won't connect: a missing adapter can't be fixed by forgetting networks or resetting passwords. The seven fixes below work from the most common causes — a disabled radio or hidden device — down to the hardware checks. Dell owners facing the same symptom can follow our [Dell Wi-Fi adapter guide](/articles/how-to-fix-wifi-adapter-not-showing-up-on-dell-laptop/), which covers Dell-specific BIOS paths.

## Why this happens

- **The wireless radio is toggled off** — ASUS Fn-key combos disable the radio at firmware level, hiding the hardware.
- **Wireless is disabled in the BIOS** — BIOS updates or resets can flip the WLAN toggle off silently.
- **The driver is corrupted beyond enumeration** — Windows can't identify the device, so it hides it instead of showing an error.
- **A Windows update broke the driver** — the new driver fails to initialize the card, and Windows drops it from the list.
- **Fast Startup froze a bad hardware state** — hybrid shutdown preserves the wedged wireless state across reboots.
- **The adapter is hidden, not gone** — it's in Device Manager as a hidden or unknown device where you haven't looked.
- **The M.2 card loosened or failed** — physical causes are rare but real, especially after drops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle the ASUS wireless hotkey

ASUS maps the wireless toggle to **Fn + F2** on most models (some use a dedicated key with an antenna icon). When this is off, the radio is disabled at firmware level and Windows sees no wireless hardware — exactly your symptom. Press the combination, wait ten seconds, and check Device Manager. Also look for a wireless LED on the chassis that indicates the radio state.

1. Press **Fn + F2** (or your model's wireless key) and wait 10 seconds.
2. Watch for a wireless indicator LED to light up on the laptop.
3. Open **Device Manager** and check **Network adapters** for the wireless device.
4. If nothing changes, try the toggle once more — some models need two presses.

### Fix 2: Show hidden devices in Device Manager

Windows hides devices it considers disconnected, and a wireless adapter in a failed state often ends up hidden rather than truly gone. Enabling "Show hidden devices" reveals grayed-out adapters you can re-enable with a right-click. Also scan **Other devices** for an unknown device — that's frequently the Wi-Fi card with a missing driver. Our [hidden devices guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) details this technique.

1. In **Device Manager**, click **View > Show hidden devices**.
2. Expand **Network adapters** and look for a grayed-out wireless adapter — right-click and **Enable** it.
3. Check **Other devices** for an **Unknown device** that could be the Wi-Fi card.
4. If found as unknown, proceed to install the ASUS wireless driver for it.

### Fix 3: Enable WLAN in the ASUS BIOS

If the hotkey didn't help, check the BIOS directly. Restart, press **F2** or **Del** at the ASUS logo, and look under the **Advanced** tab for wireless or onboard-device settings. Make sure the WLAN controller is enabled. BIOS updates and CMOS resets sometimes disable it without any visible warning in Windows — the adapter just vanishes.

1. Restart and press **F2** (or **Del**) at the ASUS logo to enter BIOS setup.
2. Go to the **Advanced** tab and find **Onboard Devices Configuration** or similar.
3. Ensure the **WLAN** / wireless controller is set to **Enabled**.
4. Press **F10** to save and exit, then check Device Manager after booting.

### Fix 4: Force a full shutdown to clear the hardware state

Fast Startup's hybrid shutdown preserves hardware states, so a wedged wireless card stays wedged through normal restarts. A full shutdown — Shift + Shut down — plus a power drain forces every device to cold-boot and reinitialize. This fixes the cases where the adapter disappeared suddenly with no update involved, which usually signals a stuck hardware state.

1. Hold **Shift** while clicking **Start > Power > Shut down**.
2. Unplug the AC adapter and wait a full 60 seconds.
3. Hold the power button for 30 seconds to drain residual charge.
4. Reconnect power, boot, and check Device Manager for the adapter.

### Fix 5: Install the ASUS wireless driver manually

If the adapter shows as an unknown device or with a warning icon, feed it the correct driver. Download the wireless driver for your exact ASUS model from ASUS support — look for Intel, Realtek, or MediaTek wireless depending on your card. Install it via Device Manager's "Browse my computer" option pointed at the extracted driver, or run the setup executable. For Intel-based cards, our [Intel Wi-Fi fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) has chipset-specific steps.

1. Download the Wi-Fi driver for your exact ASUS model from ASUS support.
2. In **Device Manager**, right-click the unknown/flagged device and choose **Update driver**.
3. Choose **Browse my computer for drivers** and point to the downloaded files.
4. Restart and confirm the adapter appears under Network adapters with no warning.

### Fix 6: Reset the network stack

When the adapter is visible but Windows' networking components are damaged, the adapter can fail initialization and drop out of the list. An elevated Command Prompt reset of Winsock and TCP/IP rebuilds these components cleanly. Run the commands in order, restart, and check whether the adapter initializes properly on the fresh stack. Microsoft documents these commands at [Windows support](https://support.microsoft.com/en-us/windows).

1. Open **Command Prompt as administrator**.
2. Run `netsh winsock reset` and press Enter, then `netsh int ip reset`.
3. Follow with `ipconfig /release`, `ipconfig /renew`, and `ipconfig /flushdns`.
4. Restart the laptop and verify the Wi-Fi adapter is present and working.

### Fix 7: Reseat the wireless card

If software has failed completely, the M.2 wireless card may be loose or dead. On ASUS models with a service panel, power off, remove the bottom cover screws, and locate the M.2 card — disconnect the two antenna cables (noting their labels), remove the retaining screw, reseat the card firmly, and reconnect everything. If reseating doesn't help, the card itself has likely failed; a replacement Intel AX210 is inexpensive and fits the same slot.

1. Power off, unplug, and remove the bottom panel of the ASUS laptop.
2. Find the M.2 wireless card; disconnect antenna cables, noting which is 1 and 2.
3. Remove the screw, reseat the card firmly, reconnect antennas to their labels.
4. Reassemble, boot, and install the ASUS wireless driver if needed.

## Closing

A vanished Wi-Fi adapter on an ASUS is Windows losing sight of the wireless hardware — usually because the radio toggle, BIOS setting, or driver broke the connection. The firmware toggles and hidden-device check in the early fixes resolve most cases without touching a screwdriver. Save the hardware inspection for last; it's rarely needed, but when it is, reseating the M.2 card is a ten-minute job.
