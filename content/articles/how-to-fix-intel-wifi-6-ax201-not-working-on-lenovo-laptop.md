---
title: "Intel Wi-Fi 6 AX201 Not Working on a Lenovo Laptop? Fix It Fast"
slug: how-to-fix-intel-wifi-6-ax201-not-working-on-lenovo-laptop
date: 2026-09-13
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "lenovo", "wireless driver"]
description: "Fix the Intel Wi-Fi 6 AX201 on a Lenovo laptop: resolve the Code 10 error, reinstall the correct Intel wireless driver, and fix Lenovo-specific power and BIOS issues."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "What does Code 10 mean on the Intel AX201 adapter?"
    a: "Code 10 means Windows could not start the device, and on the AX201 it almost always traces to a driver mismatch rather than dead hardware. The adapter needs the Intel Wi-Fi 6 AX201 160MHz driver package matched to your Windows build. Uninstalling the device with the driver software deleted and reinstalling the correct package from Intel or Lenovo clears it in most cases."
  - q: "Why does my AX201 work after restart but die after sleep?"
    a: "This is the classic Modern Standby power-management failure. Windows powers down the AX201 during sleep and the driver fails to reinitialize it on wake, leaving the adapter missing or error-flagged until a reboot. Disabling the allow-the-computer-to-turn-off-this-device option on the adapter and updating to the newest Intel driver usually ends the cycle."
  - q: "Should I use Lenovo's Wi-Fi driver or Intel's generic one?"
    a: "Start with Lenovo's driver for your exact model, because Lenovo validates it against the machine's BIOS and power firmware. If Lenovo's package is more than a year old and problems persist, Intel's generic AX201 driver from the Driver and Support Assistant is the next step. Keep whichever version proves stable for a full week of sleep-wake cycles."
  - q: "Can a BIOS update fix an AX201 that is not detected at all?"
    a: "Yes. The AX201 is a CNVio2 card that depends on the Intel chipset and BIOS working together; on some Lenovo models a BIOS update specifically addresses wireless card enumeration. If the adapter is missing from Device Manager even with hidden devices shown, check Lenovo's support page for a BIOS newer than your current one before assuming the card is dead."
---

The Intel Wi-Fi 6 AX201 is one of the most common wireless cards in Lenovo laptops, and when it stops working the symptoms are unmistakable: the Wi-Fi icon vanishes from the taskbar, Device Manager shows the adapter with a yellow warning or not at all, and the troubleshooter reports that Windows could not start the device. Lenovo machines add their own twist with Vantage-managed power profiles and BIOS-level wireless controls that can silently disable the card.

The AX201 is a CNVio2 module, which means part of its logic lives in the Intel chipset rather than on the card itself. That design makes it sensitive to driver-and-chipset mismatches in a way older cards were not. A Windows feature update that replaces the Intel driver with a slightly wrong version is the single most common trigger, and it produces the famous Code 10 error that survives ordinary reboots.

Fixing it means matching the right driver to the right Windows build, stopping Windows from power-managing the card into oblivion, and checking the Lenovo-specific layers — BIOS wireless settings, the physical wireless switch or Fn key, and Vantage power modes. The steps below are ordered from quickest to most involved.

## Why this happens

- **Driver mismatch after a Windows update:** The AX201 needs the exact Intel Wi-Fi 6 AX201 160MHz driver for your Windows build. A feature update can install a close-but-wrong version that throws Code 10 and refuses to start.
- **Aggressive power management:** Windows may power down the AX201 to save battery and then fail to wake it. The adapter disappears after sleep and only returns after a full restart.
- **Lenovo BIOS wireless disable:** Lenovo BIOS has a Wireless LAN setting that can disable the card at the hardware level. A BIOS update or reset can flip it without any visible warning in Windows.
- **Airplane mode or Fn-key radio kill:** Lenovo laptops toggle the wireless radio with Fn+F8 or a similar key. The radio can be off while Windows insists everything is fine, because the kill happens below the OS.
- **Corrupted driver store:** A failed driver update can leave a corrupted AX201 driver package in the Windows driver store, so every reinstall pulls the same broken files back in.
- **CNVio2 chipset dependency:** Because the AX201 offloads work to the Intel chipset, an outdated chipset driver or BIOS can break enumeration even when the Wi-Fi driver itself is perfect.
- **Antenna or card seating (rare):** On machines where the card is socketed, a loose M.2 card or a pinched antenna lead after a repair can cause intermittent or total failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the radio kill switch and airplane mode first

Eliminate the trivial causes before touching drivers. Lenovo's radio toggle works below the operating system, so Windows can report the adapter healthy while the radio is physically off.

1. Press Fn+F8 (or the key with the wireless tower icon) and watch for an on-screen radio indicator.
1. Open Quick Settings and confirm Airplane mode is off.
1. If the adapter appears in Device Manager but shows no networks, toggle the radio off and on once more — the state can desync after sleep.

### Fix 2: Reset the adapter with a clean driver reinstall

A plain uninstall leaves the broken driver package in the store, so Windows reinstalls the same broken files. Deleting the driver software forces a genuinely fresh copy.

1. Open Device Manager, expand Network adapters, and right-click Intel Wi-Fi 6 AX201 160MHz.
1. Choose Uninstall device and check Delete the driver software for this device.
1. Restart the laptop. Windows installs a base driver from its local store.
1. Test Wi-Fi. If it works, let Windows Update offer the newer driver; if Code 10 returns, continue to the manual install below.

### Fix 3: Install the correct Intel driver manually

The definitive fix for Code 10 is the right driver package, installed deliberately rather than left to Windows Update's guesswork. Lenovo's package is validated for your model; Intel's generic package is newer.

1. Download the Wi-Fi driver for your exact Lenovo model from [Lenovo support](https://support.lenovo.com/us/en/).
1. If Lenovo's package is old, get the latest AX201 driver from Intel's [Driver and Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) instead.
1. Run the installer, restart, and confirm the adapter starts without a warning in Device Manager.

### Fix 4: Disable power management on the AX201

This single checkbox ends the majority of sleep-related AX201 failures. Windows is allowed to cut power to the card, and on many Lenovo firmware revisions the card never comes back cleanly.

1. In Device Manager, right-click the AX201 and open Properties.
1. On the Power Management tab, uncheck Allow the computer to turn off this device to save power.
1. On the Advanced tab, set Power Saving Mode to Maximum Performance while testing.
1. Put the laptop to sleep, wake it, and confirm Wi-Fi reconnects on its own.

### Fix 5: Check the BIOS wireless setting

If the adapter is missing entirely — even with hidden devices shown — the BIOS may have it disabled. This check takes two minutes and rules out a whole class of problems.

1. Restart into the BIOS with F2 or the Novo button.
1. Under Security or Devices, find Wireless LAN and confirm it is Enabled.
1. While there, note the BIOS version and compare it with the newest on Lenovo's support page; update if yours is older and mentions wireless or CNVio fixes.

### Fix 6: Reset the network stack

When the driver is healthy but connections still fail or the adapter misbehaves, corrupted network configuration is the likely culprit. A stack reset returns everything to defaults without touching your files.

1. Open an elevated Command Prompt and run netsh winsock reset followed by netsh int ip reset.
1. Run ipconfig /flushdns, then restart the laptop.
1. Reconnect to your Wi-Fi network and re-enter the password. If the whole Wi-Fi option had vanished rather than just failing, our [Wi-Fi disappeared guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) covers the missing-adapter path in depth.

### Fix 7: Update the chipset driver and BIOS as a pair

Because the AX201 is a CNVio2 card, its fate is tied to the Intel chipset driver and the system BIOS. Updating only the Wi-Fi driver while the chipset driver is two years old leaves the underlying enumeration broken.

1. Install the latest Intel Chipset driver from Lenovo's support page for your model.
1. Apply the newest BIOS, keeping the charger connected throughout.
1. After the BIOS flash completes and Windows boots, verify the AX201 enumerates and connects. For networks that connect but only on the slower band, see [5 GHz connection fixes](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).

## Closing

The AX201 looks fragile when it throws Code 10, but it is almost never dead — it is just extraordinarily picky about driver versions and power states. Match the driver to your Windows build, take power management away from Windows, and keep the BIOS and chipset current. Do that, and the card that vanished after every sleep will quietly become the reliable Wi-Fi 6 connection it was designed to be.
