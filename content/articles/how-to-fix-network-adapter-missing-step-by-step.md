---
title: "Network Adapter Missing? A Step-by-Step Recovery Guide"
slug: how-to-fix-network-adapter-missing-step-by-step
date: 2026-10-04
categories: ["drivers"]
tags: ["network adapter", "wifi missing", "device manager", "driver fix", "windows 11"]
description: "Network adapter vanished from Device Manager? Follow this step-by-step recovery: rescan hardware, reinstall drivers, reset the stack, and check BIOS."
thumbnail: "/images/thumbs/how-to-fix-network-adapter-missing-step-by-step.webp"
faqs:
  - q: "Why did my network adapter disappear from Device Manager?"
    a: "The adapter disappears when Windows can no longer communicate with the hardware: a corrupted driver, a failed Windows update that broke driver registration, the device being disabled in BIOS, or the wireless card physically failing. A driver problem is most likely if it vanished after an update; hardware failure is more likely if it disappeared randomly and stays gone through rescans."
  - q: "How do I get my Wi-Fi adapter to show up again?"
    a: "Start with Action > Scan for hardware changes in Device Manager, then check View > Show hidden devices in case it's greyed out. If it appears with a warning, reinstall its driver. If it's completely absent, reset the network stack, check the BIOS wireless setting, and as a last resort reinstall the driver from the manufacturer's site using another computer and a USB drive."
  - q: "Can a Windows update delete my network adapter?"
    a: "Updates don't delete hardware, but they can corrupt the driver's registration so Windows stops listing the device. This is extremely common after feature updates to Windows 11 24H2. The hardware is still there — reinstalling the manufacturer's wireless driver almost always brings it back. The update-specific recovery is covered in the post-update network adapter guide."
  - q: "What if the adapter is missing even in the BIOS?"
    a: "If the wireless device doesn't appear in the BIOS device list or diagnostics, the card has likely failed or worked loose from its slot. On many laptops the Wi-Fi card is a replaceable M.2 module, making this a cheap fix. Run the manufacturer's built-in hardware diagnostics first to confirm before opening the machine or visiting a repair shop."
---

A missing network adapter is one of the scarier Windows failures because it removes your lifeline: no Wi-Fi, no settings page to fix it with, and no internet to download the driver you probably need. Device Manager shows no wireless device under Network adapters, the Wi-Fi option is gone from Settings, and the taskbar network icon shows a globe or an X. It feels like the hardware evaporated.

In the overwhelming majority of cases, it hasn't. The wireless card is still physically present; Windows has just lost track of it — a corrupted driver registration, a botched update, or a disabled device state. This guide recovers it step by step, ordered so the quick software fixes come before the deeper surgery. Keep a phone handy for downloading drivers if needed, since your laptop is offline.

## Why this happens

- **Corrupted driver registration:** The driver's registry entries get damaged (often during a Windows update), so Windows stops enumerating the device even though the hardware is fine.
- **Failed feature update:** Windows 11 24H2 upgrades are notorious for leaving wireless drivers half-migrated — the [post-update adapter guide](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/) exists precisely because this pattern is so common.
- **Device disabled in BIOS:** A BIOS wireless toggle set to disabled hides the card from Windows entirely — no scan or reinstall will reveal it until the BIOS setting changes.
- **Power management shutoff:** Aggressive power settings can put the adapter into a deep sleep state from which it doesn't wake, making it vanish from Device Manager.
- **Conflicting VPN or filter drivers:** Network filter drivers from VPN clients or security software can break the adapter's binding so badly the device stops enumerating.
- **Fast Startup holding stale state:** Windows Fast Startup can preserve a broken driver state across reboots, making the adapter stay missing no matter how many times you restart.
- **Loose or failed wireless card:** The M.2 Wi-Fi module can work loose from its slot or fail outright — the hardware explanation when all software fixes fail.
- **Corrupted network stack:** Damage to Winsock or the TCP/IP stack can cascade into the adapter failing to initialize at boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Scan for hardware changes and reveal hidden devices

1. Open Device Manager (**Win+X > Device Manager**).
2. Click **Action > Scan for hardware changes** and wait — the adapter sometimes reappears immediately.
3. Click **View > Show hidden devices**. If your Wi-Fi adapter appears greyed out, right-click it and choose **Uninstall device** (ticking driver removal), then scan for hardware changes again.
4. Check under **Other devices** too — the adapter may be listed there as an unknown device awaiting a driver. If it reappears with a yellow warning instead of working cleanly, note the error code: Code 10 or Code 43 means the driver is present but failing to start, a different repair path than a fully missing device — the [Dell adapter recovery guide](/articles/how-to-fix-network-adapter-missing-on-dell-laptop/) covers error-code-specific steps that apply across brands.

### Fix 2: Do a full shutdown to clear Fast Startup state

1. Hold **Shift** and click **Shut down** in the Start menu — this forces a true shutdown, bypassing Fast Startup's hibernation of driver state.
2. Wait 30 seconds, then power on.
3. Check Device Manager again. If the adapter is back, Fast Startup was preserving the broken state — consider disabling it permanently in Control Panel > Power Options > Choose what the power buttons do.

### Fix 3: Reset the network stack

1. Open Terminal as administrator (**Win+X > Terminal (Admin)**).
2. Run `netsh winsock reset` and `netsh int ip reset`, then restart.
3. This rebuilds the network components the adapter depends on at boot. If corruption here was blocking enumeration, the adapter returns after the reboot.

### Fix 4: Reinstall the wireless driver from the manufacturer

1. On another device (your phone works), visit your laptop manufacturer's support site and download the Wi-Fi driver for your exact model.
2. Transfer it via USB drive to the laptop.
3. In Device Manager, if the adapter is visible with a warning, right-click > **Uninstall device** with driver removal ticked. If it's invisible, skip straight to install.
4. Run the downloaded installer, restart, and check Device Manager. Use the [Intel detection tool](https://www.intel.com/content/www/us/en/support/detect.html) from another PC if you need to identify an Intel card's exact driver.

### Fix 5: Remove conflicting filter drivers

1. In Device Manager, expand **Network adapters** (if anything is visible) and check for WAN Miniport or virtual adapters from VPN software.
2. Uninstall your VPN client completely — not just disconnect — and restart.
3. In an admin terminal, run `netcfg -d` to remove all network devices and configurations (you'll need to reinstall the Wi-Fi driver after), then restart. This is aggressive but effective against filter-driver corruption.

### Fix 6: Check the BIOS wireless setting

1. Restart and enter the BIOS (usually **F2** or **Del** during the logo screen).
2. Find the wireless/WLAN device setting and make sure it's **Enabled**.
3. While there, run the built-in hardware diagnostics if your manufacturer provides them — a failed wireless test confirms hardware failure. Save and exit.

### Fix 7: Test with a USB Wi-Fi adapter and inspect hardware

1. Plug in a USB Wi-Fi adapter. If it works, your internal card is the problem — either its driver state is unrecoverable or the card itself failed.
2. If you're comfortable opening the laptop (check warranty first), reseat the M.2 wireless card and its antenna wires.
3. A replacement Intel or MediaTek M.2 card costs little and fixes confirmed hardware failures — match the form factor (usually 2230) and keying. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional guided steps for persistent adapter problems.

## Closing

A missing network adapter is alarming but usually reversible: rescan, true-shutdown, reset the stack, reinstall the manufacturer's driver, and check the BIOS. That sequence recovers the adapter in the vast majority of cases because the hardware is almost always fine — it's Windows' record of the hardware that's broken. Only when the card is invisible to the BIOS itself should you start thinking about replacement hardware.
