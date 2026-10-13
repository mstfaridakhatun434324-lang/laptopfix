---
title: "Intel Wi-Fi 6 AX201 Not Working on Acer Laptop: Full Troubleshooting"
slug: how-to-fix-intel-wifi-6-ax201-not-working-on-acer-laptop
date: 2026-09-22
categories: ["drivers"]
tags: ["intel ax201", "wifi not working", "acer laptop", "wifi 6", "wireless driver"]
description: "Intel Wi-Fi 6 AX201 dead or missing on your Acer laptop? Diagnose the adapter, reinstall the right driver, and fix power and BIOS issues step by step."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-on-acer-laptop.webp"
faqs:
  - q: "Why does my Intel AX201 disappear from Device Manager entirely?"
    a: "When the AX201 vanishes completely, the usual causes are a failed driver installation that left the device in an error state, the adapter being disabled at the firmware level, or Windows hiding it after repeated initialization failures. Enabling hidden devices in Device Manager often reveals it with an error code. A full driver reinstall using the Intel package, plus a power drain to reset the hardware, brings it back in most cases."
  - q: "Should I install the Wi-Fi driver from Acer or directly from Intel?"
    a: "Try the Acer support package first, since it is validated for your exact model's antenna configuration and regulatory settings. If Acer's package is outdated and the problem persists, Intel's generic Wi-Fi driver for the AX201 is a safe fallback — the AX201 uses a standard CNVi interface, so Intel's reference driver works on nearly all laptops. Avoid third-party driver updater tools entirely."
  - q: "Can Windows power management break the AX201 connection?"
    a: "Yes, and it is a classic cause of the AX201 working after boot but dropping minutes later. Windows aggressively powers down the adapter to save battery, and the AX201 sometimes fails to wake cleanly, showing as connected with no internet or vanishing until reboot. Disabling power saving on the adapter in Device Manager and in the advanced power plan fixes the dropouts permanently."
  - q: "Does the AX201 need a specific BIOS version to work on Acer laptops?"
    a: "The AX201 connects through Intel's CNVi interface, which depends on chipset and BIOS support. Some Acer models needed a BIOS update to stabilize the CNVi link, especially early production runs. Check Acer's support page for your model — if a BIOS update mentions wireless, connectivity, or CNVi fixes, install it on AC power before chasing the problem further in Windows."
---

The Intel Wi-Fi 6 AX201 is a tiny card with an outsized failure record on laptops: one day it connects at full speed, the next it shows code 10 in Device Manager, vanishes entirely, or connects with no actual internet. On Acer Aspire, Swift, and Nitro models this almost always traces to the driver, Windows power management, or the CNVi interface the card depends on — not to a dead card. Before you buy a replacement adapter, work through the sequence below.

The AX201 is unusual because it is not a fully standalone card: it pairs with Intel's integrated connectivity (CNVi) in the chipset, so both the Wi-Fi driver and the chipset/BIOS side must be healthy. That is why generic "reinstall the driver" advice sometimes fails — the fix may be a BIOS update or a power setting instead. For the OS-focused variant of this repair, see our [AX201 guide for Windows 11 24H2](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/), and if Wi-Fi has disappeared from the system entirely, our [vanished Wi-Fi troubleshooting](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers the broader case.

## Why this happens

- **The Intel wireless driver is corrupted or mismatched**, showing error code 10, 43, or 45 on the AX201 in Device Manager after a Windows update.
- **Windows power management suspends the adapter** and the AX201 fails to resume, dropping the connection minutes after boot.
- **The CNVi interface is unstable** because the chipset driver or BIOS version predates the fixes Intel and Acer released for early AX201 firmware.
- **A failed driver update left the device in a ghost state**, where the adapter is hidden and Windows refuses to reinstall over it cleanly.
- **Airplane mode or the wireless function key got stuck on**, disabling the radio at a level Device Manager does not clearly report.
- **Third-party VPN or security software installed a filter driver** that binds to the Wi-Fi adapter and breaks its initialization.
- **The adapter's regulatory and band settings conflict with the router**, particularly on Wi-Fi 6 networks using WPA3 or 160 MHz channels the driver build does not handle well.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode and the wireless toggle

Rule out the trivial before reinstalling anything.

1. Press Win + A and make sure Airplane mode is off and Wi-Fi is on.
2. Check the function row for a wireless icon (often F3 on Acer) and press Fn plus that key.
3. Open Settings, Network and internet, and confirm Wi-Fi appears as an option.
4. If the Wi-Fi toggle is missing entirely, the adapter is not detected — continue below.

### Fix 2: Reveal the adapter and read its error code

The error code tells you whether this is a driver problem, a power problem, or a hardware problem.

1. Press Win + X, open Device Manager, and expand Network adapters.
2. If the AX201 is absent, open the View menu and select Show hidden devices.
3. Double-click the Intel Wi-Fi 6 AX201 entry and read the Device status box on the General tab.
4. Note the code: 10 and 43 mean driver failure, 45 means disconnected hardware, and no entry at all points to firmware or BIOS.

### Fix 3: Clean-reinstall the Intel Wi-Fi driver

A proper clean reinstall removes the corrupted driver store entries that a simple update leaves behind. Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can identify the exact package your system needs.

1. Download the latest Wi-Fi driver for the AX201 from Intel or from Acer's support page for your model.
2. In Device Manager, right-click the AX201, choose Uninstall device, and tick Delete the driver software for this device.
3. Restart the laptop — do not let Windows install its own driver first if you can avoid it.
4. Run the downloaded installer immediately after boot and restart once more.

### Fix 4: Disable power saving on the adapter

This stops the resume failures that cause connections to die minutes after boot.

1. In Device Manager, right-click the AX201 and open Properties.
2. On the Power Management tab, untick Allow the computer to turn off this device to save power.
3. On the Advanced tab, set Preferred Band and Roaming Aggressiveness to moderate values if the defaults look aggressive.
4. In Power Options, expand Wireless Adapter Settings and set Power Saving Mode to Maximum Performance on both battery and plugged in.

### Fix 5: Reset the network stack

Corrupted Winsock and TCP/IP state can make a healthy adapter behave as if it has no internet.

1. Open an elevated Command Prompt (Win + X, Terminal as administrator).
2. Run `netsh winsock reset` and press Enter.
3. Run `netsh int ip reset` and press Enter.
4. Restart the laptop and reconnect to your network.

### Fix 6: Remove conflicting VPN or filter drivers

VPN clients and some security suites bind filter drivers to the adapter that can block initialization.

1. In Device Manager, open the AX201 Properties and check the Driver tab's Driver Details for third-party filter entries.
2. Temporarily uninstall any VPN client or network security software you added recently.
3. In Settings, Network and internet, Advanced network settings, reset the network entirely.
4. Reinstall the Intel driver from Fix 3 after the reset and test before reinstalling the VPN.

### Fix 7: Update the BIOS and chipset driver

When the CNVi link itself is unstable, no Wi-Fi driver version will fix it — the platform firmware needs the update.

1. Check Acer's support page for your exact model for a newer BIOS mentioning wireless or connectivity fixes.
2. Flash the BIOS on AC power with all programs closed, and do not interrupt it.
3. Install the latest Intel chipset driver package for your model.
4. Reinstall the AX201 Wi-Fi driver once more so it binds cleanly to the updated platform.

## Closing

The AX201 on Acer laptops is fixable in software in the large majority of cases: a clean driver reinstall plus disabled power management resolves most dropouts and code 10 errors, and a BIOS update handles the stubborn CNVi cases. If the adapter still shows code 45 or never appears even with hidden devices shown after all of this, the card or its antenna leads have likely failed — replacement cards are inexpensive, but the antenna wiring is worth checking first.
