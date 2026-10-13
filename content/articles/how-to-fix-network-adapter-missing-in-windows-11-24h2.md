---
title: "Network Adapter Missing in Windows 11 24H2? 7 Fixes That Work"
slug: how-to-fix-network-adapter-missing-in-windows-11-24h2
date: 2026-09-02
categories: ["drivers"]
tags: ["network adapter", "windows 11", "24h2", "wifi", "ethernet"]
description: "Network adapter vanished after the Windows 11 24H2 update? 7 fixes to restore missing Wi-Fi and Ethernet adapters — BIOS checks to clean reinstalls."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-in-windows-11-24h2.webp"
faqs:
  - q: "Why did the 24H2 update make my network adapter disappear?"
    a: "The 24H2 update overhauls networking components and driver handling. It can install an incompatible network driver that fails to initialize (so Windows hides the adapter), corrupt the driver store migration, or disable the adapter in a way that persists across reboots. Both Wi-Fi and Ethernet adapters are affected, though Wi-Fi disappearances are reported more often."
  - q: "Is my network card dead if it's missing after 24H2?"
    a: "Almost certainly not. A hardware failure coinciding exactly with a major update would be a remarkable coincidence. The 24H2 update is well documented to hide working adapters through driver and configuration issues. Work through the software fixes first — adapter hardware is the culprit in only a tiny fraction of post-24H2 disappearance cases."
  - q: "Why does the adapter show in BIOS but not in Windows?"
    a: "That confirms the hardware is fine and the problem is entirely within Windows — the BIOS sees the physical chip, but Windows' driver or device enumeration is failing. This is actually the best-case diagnostic outcome: it means a driver reinstall or network reset will fix it, with no hardware involvement whatsoever."
  - q: "Can I use a USB Wi-Fi adapter as a temporary workaround?"
    a: "Yes, and it's a smart move while troubleshooting. A USB Wi-Fi adapter uses its own driver and hardware, completely bypassing the broken internal adapter. It gets you back online immediately, which also lets you download the correct drivers for the internal adapter. Just install the USB adapter's driver from its included disc or the manufacturer's site."
---

The 24H2 update finished installing, you rebooted, and the internet is gone — not just disconnected, but the network adapter itself has vanished from Device Manager. No Wi-Fi networks listed, no Ethernet adapter, and the network icon shows a disconnected globe. When a network adapter goes missing after the Windows 11 24H2 update, the hardware is fine; the update broke Windows' ability to see it.

24H2 made significant changes to how Windows handles network drivers, and the migration doesn't always go cleanly. The seven fixes below progress from the quick visibility checks to the driver surgery that resolves stubborn cases. If your adapter is visible but Wi-Fi specifically disappeared from Settings, our [Wi-Fi disappeared guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers that narrower problem.

## Why this happens

- **24H2 installed an incompatible network driver** — the new driver fails to initialize, so Windows hides the adapter.
- **The driver migration corrupted during the update** — half-migrated driver files can't enumerate the hardware.
- **The adapter was disabled and the state persisted** — 24H2's device handling can lock in a disabled state across reboots.
- **Network stack components were damaged** — corrupted Winsock/TCP/IP prevents adapter initialization.
- **The adapter is hidden, not gone** — it's sitting in Device Manager as a hidden or unknown device.
- **BIOS wireless toggle got flipped** — 24H2-adjacent firmware updates sometimes disable WLAN in BIOS.
- **Fast Startup preserved a wedged hardware state** — the adapter never cold-boots to reinitialize.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices in Device Manager

The adapter may not be gone at all — just hidden. Device Manager hides devices Windows considers disconnected, and a 24H2-mangled adapter frequently lands in that category. Flip on "Show hidden devices" and expand Network adapters: a grayed-out adapter can be re-enabled with a right-click. Check **Other devices** too — an unknown device there is often your network card awaiting a driver. Our [hidden devices guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) walks through this in detail.

1. Open **Device Manager**, click **View**, and select **Show hidden devices**.
2. Expand **Network adapters** — right-click any grayed-out adapter and choose **Enable device**.
3. Expand **Other devices** and look for an **Unknown device** with a network-ish hardware ID.
4. If the adapter appears with a yellow warning, note the error code before continuing.

### Fix 2: Run the network troubleshooter

Windows 11's network troubleshooter (now under Settings > System > Troubleshoot) can detect disabled adapters, restart network services, and reset components automatically. It's worth the two minutes before manual work — 24H2-related adapter issues are common enough that the troubleshooter has specific handling for several of them. Let it complete fully and apply its recommendations.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Network and Internet** troubleshooter.
3. Apply any fix it suggests, including adapter resets or driver reinstalls.
4. Restart and check whether the adapter reappears in Device Manager.

### Fix 3: Reset the network stack from an elevated prompt

24H2's networking overhaul leaves corrupted Winsock and TCP/IP components on some systems, and a damaged stack prevents adapters from initializing — which makes them vanish. The classic netsh reset sequence rebuilds these components from scratch. Run each command in order from an administrator Command Prompt, then restart. Microsoft documents these commands at [Windows support](https://support.microsoft.com/en-us/windows).

1. Open **Command Prompt as administrator**.
2. Run `netsh winsock reset` then `netsh int ip reset`, pressing Enter after each.
3. Run `ipconfig /release`, `ipconfig /renew`, and `ipconfig /flushdns`.
4. Restart the laptop and check Device Manager for the adapter.

### Fix 4: Do a full network reset in Settings

Windows 11's built-in network reset reinstalls all network adapters and returns every networking component to factory defaults. It's more thorough than the command-line reset because it also clears saved networks, VPN profiles, and adapter configurations that might be wedged. You'll need your Wi-Fi password afterward — that's the tradeoff for a truly clean slate.

1. Go to **Settings > Network & internet > Advanced network settings**.
2. Click **Network reset** and then **Reset now**.
3. Confirm, and let the laptop restart automatically.
4. After reboot, reconnect to your Wi-Fi network and test.

### Fix 5: Reinstall the network driver from your manufacturer

If the adapter appears as unknown or with an error code, it needs its proper driver — and 24H2's generic replacement is what broke it. Download the Wi-Fi (and Ethernet, if affected) driver for your exact model from Dell, HP, Lenovo, or ASUS support. Use another device and a USB drive if you have no connectivity. Uninstall the broken driver with the "delete driver software" option first so Windows can't reinstall the same bad one.

1. Download the network drivers for your exact model from the manufacturer's support site.
2. In **Device Manager**, right-click the adapter/unknown device, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart, then install the manufacturer's driver package.
4. Restart once more and verify the adapter appears with no warning icon.

### Fix 6: Check the BIOS wireless/Ethernet toggles

Some systems pair the 24H2 update with a firmware update that flips network toggles in BIOS. Restart, enter BIOS setup (F2, Del, or F10 depending on brand), and verify that WLAN and onboard LAN are enabled. When disabled here, the hardware is invisible to Windows — no driver will ever bring it back. Save with the usual key (often F10) and boot into Windows.

1. Restart and enter **BIOS setup** (try F2, Del, or F10 at the logo).
2. Find wireless/LAN settings under **Advanced** or **Onboard Devices**.
3. Set **WLAN** and **Onboard LAN** to **Enabled**.
4. Save, exit, boot into Windows, and check Device Manager.

### Fix 7: Perform a full shutdown power drain

Fast Startup can preserve a wedged adapter state indefinitely across normal restarts. A full shutdown with the power drained forces the network hardware to cold-initialize on the next boot — which clears the stuck states that survive everything else. This is especially effective when the adapter disappeared suddenly mid-use rather than right after the update.

1. Hold **Shift** while clicking **Start > Power > Shut down**.
2. Unplug the AC adapter; remove the battery if it's removable.
3. Hold the power button for 30 seconds, then wait another 30.
4. Reconnect power, boot up, and verify the adapter in Device Manager.

## Closing

A network adapter missing after 24H2 is Windows losing track of working hardware — the update's driver migration is the culprit, not your network card. The hidden-device check and network reset catch the easy cases; the manufacturer driver reinstall handles the stubborn ones. And keep a cheap USB Wi-Fi adapter in a drawer: it's the fastest way to stay online while you fix the internal one.
