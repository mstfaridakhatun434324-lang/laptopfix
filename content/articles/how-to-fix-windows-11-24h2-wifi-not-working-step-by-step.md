---
title: "Windows 11 24H2 Wi-Fi Not Working? Fix It Step by Step"
slug: how-to-fix-windows-11-24h2-wifi-not-working-step-by-step
date: 2026-10-07
categories: ["windows-update"]
tags: ["windows 11 24h2", "wifi not working", "network adapter", "intel wifi", "troubleshooting"]
description: "No Wi-Fi after the Windows 11 24H2 update? Work through this step-by-step sequence — from quick toggles to clean driver reinstalls — to get wireless back."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-wifi-not-working-step-by-step.webp"
faqs:
  - q: "Why did Wi-Fi break right after installing 24H2?"
    a: "The 24H2 update changed the Wi-Fi driver interface, and older Intel, Realtek, or MediaTek drivers cannot bind to the new stack. The adapter may vanish from Device Manager entirely or appear with a yellow warning. A clean install of a current driver resolves it in most cases."
  - q: "My Wi-Fi adapter is missing from Device Manager. Is the hardware dead?"
    a: "Probably not. A missing adapter after 24H2 almost always means the driver failed to load, not that the chip died. Check View > Show hidden devices in Device Manager — if it appears greyed out, it is a driver problem. A BIOS reset and driver reinstall bring it back in the large majority of cases."
  - q: "Should I use the driver from Windows Update or Intel's site?"
    a: "For post-24H2 Wi-Fi problems, get the driver from Intel's site or your laptop manufacturer's support page. Windows Update's version lags and is often the one that broke. Intel's [driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects your exact adapter and installs the current release."
  - q: "Wi-Fi works but drops every few minutes since 24H2. What's wrong?"
    a: "Frequent drops are usually power management turning the adapter off, a roaming aggressiveness mismatch with your router, or an old driver. Disable 'allow the computer to turn off this device' in the adapter's Power Management tab first — that single checkbox fixes most drop issues."
---

You installed the Windows 11 24H2 update, rebooted, and the Wi-Fi icon is gone — or it is there but no networks appear, or networks appear and connections drop every few minutes. This is one of the best-documented 24H2 regressions on laptops, and it is fixable in the overwhelming majority of cases without new hardware.

The cause is almost always the driver stack change in 24H2: the update replaced how Windows talks to Wi-Fi adapters, and the old driver could not make the jump. The fix sequence below starts with the thirty-second checks and progresses to a full clean driver reinstall. Test your connection after each step and stop when Wi-Fi is stable.

## Why this happens

- **Driver stack interface change:** 24H2 rewrote parts of the WLAN driver interface; pre-24H2 Intel, Realtek, and MediaTek drivers fail to bind to it.
- **Windows Update installed the wrong driver:** The update process sometimes replaces a working OEM driver with a generic one that lacks your adapter's firmware support.
- **Power management regression:** 24H2 can re-enable aggressive adapter power saving that powers the radio down during idle moments, causing drops.
- **Corrupted adapter configuration:** The upgrade migrates network profiles and adapter settings, and corrupted profiles can leave the adapter in a broken state.
- **BIOS/firmware mismatch:** Some adapters need a firmware or BIOS update to work with 24H2's power and bus management.
- **VPN or filter driver conflict:** Old VPN clients install network filter drivers that 24H2's new stack rejects, taking the adapter down with them.
- **Fast Startup stale state:** Hybrid shutdown can restore the Wi-Fi driver into a half-initialized state after the upgrade.
- **Antenna or hardware coincidence:** Rarely, the timing is coincidental — but rule out every software cause before suspecting hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the quick toggles and network troubleshooter

Start with the basics — a surprising number of "dead Wi-Fi" cases after 24H2 are just a toggled radio or a stuck stack.

1. Check the physical Wi-Fi switch or **Fn** key combo on your laptop (common on Lenovo and Dell) — 24H2 can leave the radio soft-disabled.
2. Go to **Settings > Network & internet** and toggle **Wi-Fi** off and back on. Also toggle **Airplane mode** on, wait 10 seconds, and off.
3. Run **Settings > System > Troubleshoot > Other troubleshooters > Network and Internet > Run**.
4. If networks appear now, reconnect and test for ten minutes before moving on.

### Fix 2: Reset the network stack

If the troubleshooter did not help, reset the entire network configuration. This clears corrupted profiles and stack settings the upgrade left behind.

1. Open **Terminal (Admin)**.
2. Run, one at a time: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Alternatively, use **Settings > Network & internet > Advanced network settings > Network reset** and click **Reset now**.
4. Restart the laptop and reconnect to your Wi-Fi network (you will need to re-enter the password).

### Fix 3: Disable adapter power management

If Wi-Fi connects but drops repeatedly — especially after idle periods or sleep — power management is the prime suspect.

1. Open **Device Manager**, expand **Network adapters**, and double-click your Wi-Fi adapter.
2. Open the **Power Management** tab and uncheck **Allow the computer to turn off this device to save power**.
3. On the **Advanced** tab, find **Roaming Aggressiveness** and set it to **Medium** or **Lowest** if drops happen while stationary.
4. Click OK and test stability for at least 30 minutes of normal use.

### Fix 4: Clean-reinstall the Wi-Fi driver

This is the core fix for post-24H2 Wi-Fi failures. A clean install removes the broken driver binding entirely.

1. In **Device Manager**, right-click the Wi-Fi adapter under **Network adapters** and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. If the adapter is missing entirely, click **View > Show hidden devices** first — uninstall the greyed-out entry.
3. Restart the laptop.
4. Install the latest driver from Intel's [driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop maker's support page (Dell, HP, or [Lenovo](https://support.lenovo.com/us/en/)).
5. Restart once more and reconnect. If your adapter is the Intel Wi-Fi 6 AX201 specifically, our [AX201 guide for 24H2](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) goes deeper on that chip's driver versions and firmware quirks.

### Fix 5: Remove conflicting VPN and filter drivers

Old VPN clients are a known 24H2 Wi-Fi killer because their filter drivers are incompatible with the new network stack.

1. In **Device Manager**, expand **Network adapters** and look for virtual adapters from old VPN software.
2. Uninstall the VPN application itself via **Settings > Apps > Installed apps**.
3. In an elevated Terminal, run `netcfg -d` to remove all network devices and filter drivers (this is aggressive — only do it if VPN filters are suspected), then restart.
4. Reinstall only a current, 24H2-compatible version of your VPN if you need one.

### Fix 6: Update the BIOS

Some Wi-Fi adapters — particularly Intel AX-series cards — need newer BIOS firmware to operate correctly under 24H2's power management.

1. Find your current BIOS version with `msinfo32` (System Summary > BIOS Version/Date).
2. Check your manufacturer's support page for a newer BIOS mentioning 24H2 or Windows 11 compatibility.
3. Install it with the charger connected and the laptop on a stable surface — do not interrupt a BIOS flash.
4. After the flash, retest Wi-Fi. This step is also part of the broader [24H2 known-issues fix sequence](/articles/how-to-fix-windows-11-24h2-known-issues-on-lenovo-laptop/) for Lenovo machines.

### Fix 7: Disable Fast Startup and test a clean boot

If Wi-Fi fails after shutdown but works after restart, Fast Startup's hibernated driver state is the culprit.

1. Open **Control Panel > Power Options > Choose what the power buttons do > Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup** and save.
3. Shut down fully, wait ten seconds, and power on.
4. If Wi-Fi now works consistently, leave Fast Startup off — the few extra boot seconds are worth reliable wireless.

If Wi-Fi is only one of several things 24H2 broke, our [24H2 known-issues guide for Lenovo laptops](/articles/how-to-fix-windows-11-24h2-known-issues-on-lenovo-laptop/) covers the full set.

## Closing

Post-24H2 Wi-Fi failures follow a predictable script: the driver could not cross the stack upgrade, and everything from a missing adapter to flaky drops traces back to that. The clean driver reinstall in Fix 4 resolves most cases; power management and VPN filters cover most of the rest. Work the sequence patiently, test after each step, and keep the driver current going forward — Wi-Fi that survives 24H2 stays working as long as the driver stays matched to the OS.
