---
title: "WiFi Adapter Not Showing Up? How Do I Fix It on Windows"
slug: how-do-i-fix-wifi-adapter-not-showing-up
date: 2026-09-18
categories: ["drivers"]
tags: ["wifi adapter missing", "wireless disappeared", "device manager", "no wifi option", "windows 11"]
description: "Your WiFi adapter vanished from Windows completely? Here's how to bring it back — from hidden-device checks to BIOS, drivers, and hardware tests."
thumbnail: "/images/thumbs/how-do-i-fix-wifi-adapter-not-showing-up.webp"
faqs:
  - q: "My WiFi option disappeared from Settings entirely. What happened?"
    a: "When the WiFi toggle vanishes from Settings, Windows cannot see the wireless adapter hardware. This is different from WiFi being turned off — the device itself is not enumerating. The most common causes are a failed wireless driver after an update, the adapter disabled in BIOS, or the Radio Management Service crashing. Checking Device Manager with hidden devices shown is the first diagnostic step."
  - q: "How do I reinstall a WiFi adapter that isn't listed anywhere?"
    a: "You cannot reinstall what Windows cannot see, so first restore visibility: enable hidden devices in Device Manager, check the BIOS wireless setting, and disable Fast Startup. Once the adapter appears — even with a warning icon — you can uninstall it and install the correct OEM driver. If it never appears in BIOS either, suspect hardware failure."
  - q: "Why does my WiFi adapter keep disappearing after every Windows update?"
    a: "Windows Update repeatedly replaces your OEM wireless driver with its own version, and on some Intel, Realtek, and MediaTek cards the Microsoft driver fails to initialize the hardware properly. The permanent fix is to install the OEM driver and then block automatic driver updates through Device Installation Settings or Group Policy so the working driver survives future updates."
  - q: "Is the WiFi card dead if it's missing from BIOS?"
    a: "Most likely, yes — or it has a connection problem. If the BIOS device list shows no wireless adapter, the operating system has nothing to work with. Before concluding it is dead, try a full power drain (unplug, hold power 30 seconds) and reseat the card if your laptop allows access. If it is soldered to the board, a USB WiFi adapter is the practical workaround."
---

When the WiFi adapter doesn't show up anywhere — not in Settings, not in Device Manager, not even as an unknown device — you're dealing with a detection failure, not a configuration problem. Windows can't configure hardware it can't see. The frustration is real: one day WiFi works, a Windows update installs overnight, and the next morning the entire wireless section of Settings is simply gone.

The good news is that this is fixable in the majority of cases, and the diagnostic path is logical. You work from the top of the stack down: Windows' device view, then the driver layer, then BIOS, then hardware. At each level you're asking one question — "can the system see the adapter here?" — and the answer tells you exactly where the break is.

## Why this happens

- **Windows Update replaced the wireless driver:** The single most common cause. The new driver fails to initialize the card, so it never enumerates.
- **Adapter disabled in BIOS/UEFI:** A BIOS-level wireless toggle turned off means the hardware is invisible to every operating system.
- **Device disabled in Device Manager:** Disabled devices hide from the normal view; the adapter is present but suppressed.
- **Fast Startup preserving a broken device state:** Hybrid shutdown caches hardware state, and a bad state survives reboots indefinitely.
- **Corrupted driver store entries:** Half-installed or conflicting driver packages can block enumeration entirely.
- **Radio Management Service failure:** When this service crashes, Windows may fail to surface wireless devices at all.
- **Loose or failed M.2 wireless card:** Physical connection problems or a dead card remove it from the PCIe bus.
- **Chipset driver issues:** The platform controller needs correct drivers to enumerate PCIe devices including the WiFi card.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices in Device Manager

1. Press **Win + X** and open **Device Manager**.
2. Click **View → Show hidden devices** — this is the step most people miss.
3. Expand **Network adapters**. Look for a grayed-out wireless adapter (disabled) or anything under **Other devices / Unknown devices** (driver problem).
4. If you find it grayed out, right-click → **Enable device**. If it has a yellow bang, right-click → **Update driver** or **Uninstall device** followed by **Scan for hardware changes**.

### Fix 2: Check the BIOS wireless setting

1. Restart the laptop, pressing **F2** or **Del** repeatedly to enter BIOS/UEFI setup.
2. Navigate to the **Advanced**, **Devices**, or **Security** tab and find the **Wireless**, **WLAN**, or **WiFi** option.
3. Make sure it is set to **Enabled**. Some BIOS versions bury this under "Onboard Devices" — check every tab.
4. Save changes and exit. If the adapter was BIOS-disabled, Windows will detect it on this boot and begin driver installation.

### Fix 3: Kill Fast Startup and do a full power drain

1. Open **Control Panel → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable** and uncheck **Turn on fast startup**.
3. Shut down fully, unplug the AC adapter, and hold the power button for **30 seconds**.
4. Plug back in and power on. This forces complete hardware re-enumeration, clearing states that survive normal reboots — the same technique that fixes [stuck airplane mode](/articles/how-to-fix-airplane-mode-stuck-on-reddit/).

### Fix 4: Reinstall the wireless driver cleanly

1. On another device, download the WiFi driver for your exact laptop model from the manufacturer's support page.
2. Transfer it via USB, then in Device Manager (hidden devices shown), uninstall every wireless-related entry, checking **"Delete the driver software for this device."**
3. Install the downloaded driver package and reboot.
4. For Intel cards specifically, the [Intel WiFi 6 AX201 repair guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) covers card-specific quirks that generic reinstalls miss.

### Fix 5: Restart the Radio Management Service

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Locate **Radio Management Service**. Set **Startup type** to **Automatic** and click **Start** (or **Restart** if already running).
3. Also verify the **WLAN AutoConfig** service is running — both are required for wireless to function.
4. Open **Settings → Network & internet** and check whether the WiFi section has returned.

### Fix 6: Reset the network stack completely

1. Open **Terminal as Administrator** and run these in order: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /flushdns`.
2. Go to **Settings → Network & internet → Advanced network settings → Network reset** and click **Reset now**.
3. Restart when prompted. The reset reinstalls all network adapters and returns networking components to factory state.
4. Reconnect to your WiFi network afterward — you'll need the password again.

### Fix 7: Block Windows from breaking the driver again

1. Once WiFi works, open **System → About → Advanced system settings → Hardware → Device Installation Settings** and choose **No**.
2. On Windows Pro, enable **"Do not include drivers with Windows Updates"** in Group Policy under Computer Configuration → Administrative Templates → Windows Components → Windows Update.
3. This is what makes the fix permanent. Without it, the next update can reinstall the bad driver and you'll be back to square one — a cycle documented in the [missing network adapter guide](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/).
4. For authoritative background on managing drivers, the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) keeps Intel wireless drivers current without Windows Update's interference.

### Fix 8: Test hardware with a USB adapter and reseat the card

1. Plug in a USB WiFi dongle. If it works, your Windows networking is healthy and the internal card is the isolated problem.
2. If the internal card is socketed (not soldered), power off, open the bottom panel, and reseat the M.2 card and its antenna leads.
3. If reseating fails and the card is absent from BIOS, replace the card — Intel AX210/AX211 cards are inexpensive upgrades for many laptops.
4. For soldered-down wireless, the USB adapter becomes the permanent solution; choose a reputable dual-band model.

## Closing

A missing WiFi adapter is a detection problem with a logical fix order: reveal it, enable it in BIOS, clear the cached state, reinstall the driver, and lock the driver in place. Work the list and the adapter comes back — or you'll have proof it's hardware.
