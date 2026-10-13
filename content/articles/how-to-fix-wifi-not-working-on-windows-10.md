---
title: "WiFi Not Working on Windows 10? Fix It Step by Step"
slug: how-to-fix-wifi-not-working-on-windows-10
date: 2026-09-06
categories: ["drivers"]
tags: ["windows 10", "wifi", "wireless adapter", "troubleshooting", "network"]
description: "No WiFi on Windows 10 — adapter missing, won't connect, or drops constantly? Diagnose and repair it with this ordered fix sequence."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-on-windows-10.webp"
faqs:
  - q: "Why did my WiFi stop working after a Windows 10 update?"
    a: "Windows 10 feature updates frequently replace working WiFi drivers with older inbox versions, reset power management settings, or corrupt network profiles. If WiFi died immediately after an update, rolling back the WiFi driver in Device Manager is the fastest fix, followed by a network reset if needed."
  - q: "My WiFi adapter is missing from Device Manager. What now?"
    a: "A missing adapter means Windows can't see the hardware at all. Try Action > Scan for hardware changes first, then do a full power cycle (shutdown, unplug, hold power 30 seconds) to reset the card's firmware. If it never reappears, check BIOS for a wireless toggle, then suspect hardware."
  - q: "WiFi works on my phone but not my Windows 10 laptop. Is it the router?"
    a: "Almost certainly not — if other devices connect fine, the router is working and the problem is local to the laptop. Focus on the laptop's WiFi driver, its power management settings, and corrupted network profiles rather than rebooting the router repeatedly."
  - q: "Should I still be on Windows 10 for WiFi troubleshooting?"
    a: "Windows 10 remains fully usable, but Microsoft's free support has ended, so driver updates increasingly target Windows 11. If your laptop supports it, upgrading to Windows 11 often resolves chronic WiFi issues by bringing a newer driver stack — grab the installer from Microsoft's official download page."
---

Windows 10 WiFi failures come in three flavors: the adapter vanishes entirely, the adapter is present but won't connect, or it connects and then drops. Each flavor has its own most-likely cause, and the fixes are different enough that diagnosing first — before reinstalling anything — saves real time. This guide is organized around that diagnosis.

One important note: Windows 10's free support lifecycle has ended, which means WiFi drivers increasingly ship optimized for Windows 11. Keep that in mind as a background factor while you work through these steps.

## Why this happens

- **A Windows 10 update replaced the WiFi driver.** Feature updates are notorious for swapping a working vendor driver for an older generic one. This is cause number one for sudden WiFi death.
- **Power management put the card to sleep permanently.** "Allow the computer to turn off this device to save power" plus Windows 10's aggressive USB/PCIe power saving can wedge the adapter in an off state.
- **Corrupted network profile or stack.** A damaged saved network profile or corrupted TCP/IP stack produces "can't connect" errors even with perfect signal.
- **The WLAN AutoConfig service stopped.** If this Windows service isn't running, WiFi simply doesn't function — no networks appear at all.
- **Airplane mode or a hardware radio kill switch.** Physical WiFi switches and Fn-key toggles still exist on many Windows 10-era laptops, and they're easy to bump. See [stuck airplane mode](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/).
- **Antivirus or VPN software blocking the adapter.** Security suites and VPN clients install filter drivers that can break WiFi entirely when they malfunction.
- **Failing WiFi card hardware.** Less common, but cards do die — usually presenting as intermittent drops that get progressively worse.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the radio switches and airplane mode

The two-minute check that embarrasses everyone eventually.

1. Look for a physical **WiFi switch** on the laptop's sides or front edge and make sure it's on.
2. Press **Fn + the WiFi key** (often F2, F3, or F12 with a radio-tower icon) and watch for an on-screen indicator.
3. Open **Action Center** (click the notification icon) and make sure **Airplane mode** is off and **Wi-Fi** is on.
4. Go to **Settings** > **Network & Internet** > **Wi-Fi** and confirm the Wi-Fi toggle is on and your network appears in the list.
5. If no networks appear at all but the toggle is on, the problem is driver-level — continue to Fix 3.

### Fix 2: Restart the WLAN service and network components

When the software plumbing has stalled.

1. Press **Win + R**, type `services.msc`, and find **WLAN AutoConfig**. Make sure its status is **Running** and startup type is **Automatic**. If not, start it and set it to Automatic.
2. In an admin Command Prompt, run: `netsh winsock reset` and `netsh int ip reset`, then restart.
3. After rebooting, **forget** your WiFi network (Settings > Network & Internet > Wi-Fi > Manage known networks > Forget) and reconnect fresh.
4. If you use a VPN, temporarily uninstall it — VPN filter drivers are a classic silent WiFi killer on Windows 10.

### Fix 3: Fix the WiFi driver

The core repair for most Windows 10 WiFi failures.

1. Open **Device Manager** (Win + X) > **Network adapters**. Find your WiFi adapter.
2. If it has a yellow warning, right-click > **Properties** > **Driver** tab > **Roll Back Driver** if available.
3. Whether or not rollback works: right-click > **Uninstall device**, check "Delete the driver software for this device" if offered, then restart.
4. Download the WiFi driver for your exact model from the manufacturer's support site and install it manually — don't rely on Windows Update's version.
5. For Intel cards, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) finds the correct current driver automatically.

### Fix 4: Disable power management on the adapter

Stops the "WiFi dies after sleep" and random-drop patterns.

1. In **Device Manager**, right-click the WiFi adapter > **Properties** > **Power Management** tab. Uncheck "Allow the computer to turn off this device to save power."
2. Go to **Control Panel** > **Power Options** > **Change plan settings** > **Change advanced power settings** > **Wireless Adapter Settings** > **Power Saving Mode** — set both On battery and Plugged in to **Maximum Performance**.
3. In the adapter's **Advanced** tab, set **Roaming Aggressiveness** to **Lowest** as a stability test.
4. Test through a full sleep/wake cycle before declaring victory.

### Fix 5: Use Windows 10's built-in troubleshooters and network reset

The built-in tools earn their keep here.

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters** > **Internet Connections** and **Network Adapter**. Run both and apply any fixes offered.
2. If they don't resolve it, use the bigger hammer: **Settings** > **Network & Internet** > **Status** > **Network reset**. This reinstalls all network adapters and resets everything to defaults.
3. Restart when prompted, then reconnect to WiFi from scratch.
4. Note: network reset also removes saved VPN connections and virtual switches — back up VPN configs first if you use them.

### Fix 6: Check for software conflicts

Third-party software that hooks the network stack.

1. Temporarily disable (not just exit) your **antivirus/firewall** and test WiFi. If it works, add an exclusion or switch products — don't run without protection permanently.
2. Uninstall any **VPN clients**, **network optimizers**, or **"WiFi booster"** utilities, then test. Reinstall only the ones you actually need, one at a time.
3. Check **Device Manager** > **View** > **Show hidden devices** > **Network adapters** for ghost or duplicate adapters from old VPN installs — uninstall the ghosts.
4. Our [Ethernet troubleshooting guide](/articles/how-to-fix-ethernet-not-working-on-laptop-on-windows-10/) covers the wired side if both radios are misbehaving.

### Fix 7: Consider the hardware and the OS upgrade path

When software is exhausted.

1. Boot a **Linux live USB** and test WiFi. Stable in Linux = Windows driver problem (revisit Fix 3 with different driver versions). Dead in Linux = hardware.
2. If the card is a removable M.2 module, reseating it (or replacing it with a newer card) is a cheap fix — check your model's service manual.
3. Seriously consider upgrading to **Windows 11** if your hardware supports it: download it from [Microsoft's official page](https://www.microsoft.com/en-us/software-download/windows11). The newer driver stack resolves entire categories of Windows 10 WiFi bugs, and you'll get security updates again.
4. As an immediate workaround, a USB WiFi adapter restores connectivity for very little money.

The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) can also supply specific driver versions when the manufacturer's site lags behind.

## Closing

Windows 10 WiFi failures are overwhelmingly driver and power-management problems wearing different disguises: check the physical switches, restart the WLAN plumbing, rebuild the driver from the manufacturer's package, kill the power-saving settings, and reset the network stack. That sequence resolves the large majority of cases. And if your laptop qualifies for Windows 11, the upgrade is worth considering — not just for WiFi, but because the old OS is no longer getting the fixes that keep wireless working.
