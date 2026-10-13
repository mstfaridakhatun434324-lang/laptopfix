---
title: "WiFi Adapter Not Showing Up in Device Manager: Troubleshoot It"
slug: troubleshoot-wifi-adapter-not-showing-up
date: 2026-09-17
categories: ["drivers"]
tags: ["wifi adapter", "not showing up", "device manager", "missing adapter", "wireless"]
description: "WiFi adapter missing from Device Manager entirely? Troubleshoot hidden devices, BIOS settings, driver reinstalls, and hardware failure."
thumbnail: "/images/thumbs/troubleshoot-wifi-adapter-not-showing-up.webp"
faqs:
  - q: "Why is my WiFi adapter completely missing from Device Manager?"
    a: "A missing adapter means Windows cannot see the hardware at all. The usual causes are a disabled adapter in BIOS, a crashed wireless driver that failed enumeration, the adapter being disabled in Device Manager's hidden view, or actual hardware failure. The key diagnostic is checking BIOS: if the adapter appears there, it is a software problem."
  - q: "Can Windows Update make the WiFi adapter disappear?"
    a: "Yes, this is one of the most reported causes. A Windows update can install an incompatible wireless driver or corrupt the existing one badly enough that the device fails to enumerate. Reinstalling the correct OEM driver — or rolling back to the previous version — typically brings the adapter back immediately."
  - q: "What is the difference between a missing adapter and a disabled adapter?"
    a: "A disabled adapter appears in Device Manager (possibly under hidden devices) with a down-arrow icon and can be re-enabled with a right-click. A missing adapter does not appear at all, even with hidden devices shown. Disabled is a settings issue; missing means Windows cannot detect the hardware, which points to BIOS, driver, or hardware failure."
  - q: "Will a USB WiFi adapter work if my internal one is dead?"
    a: "Yes, and it is the fastest workaround. A USB WiFi dongle is independent of the internal card and works even if the internal adapter has failed completely. It is also the definitive diagnostic: if the USB adapter works fine, your Windows networking stack is healthy and the problem is isolated to the internal card."
---

There is a meaningful difference between WiFi "not working" and the WiFi adapter "not showing up." When the adapter is missing from Device Manager entirely — not disabled, not warning-flagged, just gone — Windows cannot see the hardware at all. That narrows the suspects considerably: BIOS configuration, a catastrophically broken driver, or dead hardware.

The diagnostic path here is about visibility at each layer: BIOS, Device Manager's hidden view, and driver state. Each layer you check eliminates a category of causes.

## Why this happens

- **Adapter disabled in BIOS:** Many laptops have a BIOS toggle for the wireless card. If off, the OS never sees it.
- **Driver corruption after Windows Update:** A bad driver can fail device enumeration so completely the adapter vanishes.
- **Adapter disabled in Device Manager:** It may be present but hidden — disabled devices don't show unless you enable hidden-device view.
- **Fast Startup hiding the device:** Hybrid shutdown can leave the wireless card in a state where it doesn't enumerate on boot.
- **Hardware failure of the WiFi module:** The M.2 or soldered wireless card can die, especially after liquid damage or drops.
- **Loose antenna or card connection:** On laptops with socketed WiFi cards, the card can work loose.
- **Chipset driver problems:** The PCIe bus the WiFi card sits on needs working chipset drivers to enumerate devices.
- **Airplane mode hardware lock:** A stuck hardware radio kill switch can suppress the adapter's appearance.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Show hidden devices in Device Manager

1. Open **Device Manager**, click **View → Show hidden devices**.
2. Expand **Network adapters** and look for your wireless adapter — it may appear grayed out (disabled) or under **Unknown devices**.
3. If grayed out, right-click → **Enable device**.
4. If it appears with a yellow warning, right-click → **Uninstall device**, then **Action → Scan for hardware changes**. This is the same first check used when the [network adapter goes missing after updates](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/).

### Fix 2: Check BIOS for the wireless adapter

1. Restart and enter **BIOS/UEFI** (F2/Del during boot).
2. Look for **Wireless**, **WLAN**, or **WiFi** under Advanced, Devices, or Security tabs.
3. Ensure it is **Enabled**. If it was disabled, enable it, save, and boot into Windows.
4. While in BIOS, check whether the adapter is listed in the system information page — its presence here proves the hardware is alive.

### Fix 3: Power-cycle to clear Fast Startup state

1. Go to **Control Panel → Power Options → Choose what the power buttons do** → disable **Fast Startup**.
2. Shut down completely (not restart), unplug the charger, and hold the power button for 30 seconds.
3. Power on and check Device Manager again. Fast Startup preserves device states across boots, and a full power cycle forces fresh hardware enumeration.
4. This resolves the cases where the adapter "disappears" after sleep or hibernation specifically.

### Fix 4: Reinstall the wireless driver from scratch

1. Download the WiFi driver for your exact model from the manufacturer's support page before you start (you may need another device, since you have no WiFi).
2. In Device Manager (with hidden devices shown), uninstall anything wireless-related, checking "delete the driver software."
3. Run the downloaded installer and reboot.
4. If the adapter appears now, the old driver was corrupt beyond enumeration — the [Intel AX201 fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) covers the most common card specifically.

### Fix 5: Reset the network stack and BIOS to defaults

1. In an admin Terminal, run `netsh winsock reset` and `netsh int ip reset`, then restart.
2. Enter BIOS and choose **Load Optimized Defaults** or **Reset to default** — a misconfigured BIOS can suppress devices.
3. Save and boot, then check Device Manager once more.
4. Also try **Settings → Network & internet → Advanced network settings → Network reset** as a complementary step.

### Fix 6: Test with a USB WiFi adapter

1. Plug in any USB WiFi dongle. If Windows detects it and it connects, your OS networking stack is fine.
2. This isolates the problem to the internal card specifically — driver, BIOS, or hardware.
3. Keep the dongle as your workaround while you pursue the internal fix; there is no shame in a $15 solution.
4. If even the USB adapter fails to appear, the problem is system-wide — consider the [general WiFi repair sequence](/articles/wifi-disappeared-windows-11-no-wifi-option/) and ultimately a Windows repair install.

### Fix 7: Inspect or replace the internal WiFi card

1. If the adapter is absent from BIOS too, power off, open the laptop, and reseat the M.2 WiFi card and its antenna wires (black and white/gray wires — note which goes where).
2. If reseating doesn't help, replacement Intel AX-series cards are inexpensive and widely compatible — check your model's whitelist first, as some Lenovo/HP laptops restrict cards.
3. On laptops with soldered WiFi (many ultrabooks), board-level repair or the USB dongle are the realistic options.
4. Check warranty status before opening anything — wireless card replacement is usually covered. For driver sourcing, the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) identifies the right package automatically.

### Fix 8: Verify system services and consider an in-place upgrade

1. Confirm these services are running and Automatic: **WLAN AutoConfig**, **WWAN AutoConfig**, **Network Connections**, and **Radio Management Service**.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Terminal to repair corrupted networking system files.
3. Check **Event Viewer → System** for network adapter errors at boot time — specific error codes here identify whether it's a driver load failure or a deeper problem.
4. As the last software resort, do an **in-place upgrade**: run the Windows installer from a USB and choose to keep files and apps. This rebuilds Windows' driver and network stacks without wiping your data, and it resolves the cases where the adapter is visible in BIOS but invisible to every other repair.

## Closing

A missing WiFi adapter is a visibility problem: check the hidden-device view, then BIOS, then the driver, then the hardware. Most cases resolve at the driver layer — but now you know exactly how to prove it either way.
