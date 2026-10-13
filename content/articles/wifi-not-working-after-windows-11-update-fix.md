---
title: "Wi-Fi Not Working After a Windows 11 Update? 7 Fixes That Work"
slug: wifi-not-working-after-windows-11-update-fix
date: 2026-10-06
categories: ["drivers"]
tags: ["wifi", "network", "windows update", "drivers"]
description: "Wi-Fi stopped working right after a Windows 11 update? Here are 7 fixes — from rolling back the network driver to resetting the TCP/IP stack."
thumbnail: "/images/thumbs/wifi-not-working-after-windows-11-update-fix.webp"
faqs:
  - q: "Why does Wi-Fi break after a Windows 11 update?"
    a: "Windows Update sometimes installs a newer wireless driver that does not work properly with your specific adapter, or it resets network settings your old configuration relied on. In some cases the update process itself corrupts the TCP/IP stack or the Winsock catalog. The result: the adapter looks fine but cannot connect, or it disappears from the Wi-Fi list entirely."
  - q: "Should I uninstall the Windows update to fix my Wi-Fi?"
    a: "Try that only as a last resort. Most post-update Wi-Fi failures are driver or configuration problems, and rolling back the driver or resetting the network stack usually fixes them without touching the update itself. Uninstall the update only if every other fix has failed and the connection was working perfectly immediately before that update installed."
  - q: "Will resetting the network remove my saved Wi-Fi passwords?"
    a: "Yes. A full network reset erases saved networks and passwords, along with VPN profiles, custom DNS, and static IP settings. Your laptop will set up networking like it is brand new, so keep your router password handy. That is why it is worth trying the driver fixes and a simple forget-and-rejoin before doing a full reset."
  - q: "What should I do if none of these fixes restore Wi-Fi?"
    a: "Check Device Manager for an error code on the wireless adapter — a Code 10 or Code 43 points to a driver conflict you can research specifically. Look for a BIOS or firmware update from your laptop maker, since those occasionally restore hardware that a Windows update broke. If nothing software-related helps, a cheap USB Wi-Fi adapter will confirm whether the built-in adapter itself has failed."
---

You finished installing a Windows 11 update, restarted your laptop — and now the Wi-Fi icon shows a globe with a warning triangle instead of connected bars. Either no wireless networks appear at all, or the laptop connects but has no internet. It is frustrating, but it is also one of the most common things a Windows update breaks.

The hardware is almost certainly fine. Updates typically swap in a new wireless driver, reset adapter settings, or damage the network stack — all software problems you can reverse in minutes. Work through the seven fixes below in order, from the quickest to the most involved, and stop as soon as your connection is back.

## Why this happens

- **The update installed an incompatible wireless driver** — Windows Update sometimes pushes a generic or newer driver that does not match your adapter.
- **The update reset adapter or power-management settings** — a changed power plan can let Windows turn the adapter off to save battery.
- **The TCP/IP stack or Winsock catalog was corrupted** — interrupted installs can damage the core networking components Windows depends on.
- **A VPN client, virtual adapter, or firewall rule is blocking traffic** — third-party network software often conflicts with new update builds.
- **The update itself is faulty or only partially installed** — a stalled update can leave network services misconfigured (see our guide on [Windows Update stuck at 100%](/articles/windows-update-stuck-at-100-percent-fix/)).

## How to fix it

Start with Fix 1 and move down the list — the early fixes solve most cases.

### Fix 1: Restart fully and toggle Airplane mode

Airplane mode forces Windows to power-cycle the wireless radio and reload the network stack. Combined with a full shutdown rather than a quick restart, this clears stale adapter states left behind by the update.

1. Open **Settings > Network & internet** and turn the **Airplane mode** toggle On.
2. Shut the laptop down fully — hold **Shift** while clicking **Shut down** — wait 30 seconds, then power it back on.
3. Return to **Settings > Network & internet** and turn Airplane mode Off.
4. Click **Wi-Fi > Show available networks** and check whether your network appears.

### Fix 2: Roll back the Wi-Fi driver

If the update installed a new driver, rolling back restores the previous version that was working. This single fix resolves the majority of post-update Wi-Fi failures. Driver swaps can break other hardware too — if your HP laptop's touchpad also stopped working after the same update, see our [touchpad fix guide](/articles/touchpad-not-working-hp-laptop-windows-11-fix/).

1. Right-click **Start** and choose **Device Manager**.
2. Expand **Network adapters**, right-click your wireless adapter (for example, Intel Wi-Fi 6 AX201 or Realtek 8821CE Wireless LAN), and choose **Properties**.
3. Open the **Driver** tab. If **Roll Back Driver** is clickable, click it, select a reason such as "Previous version of the driver seemed more reliable", and confirm.
4. Restart the laptop and test Wi-Fi.

### Fix 3: Reinstall the network adapter

If rollback is not available or did not help, uninstalling the adapter forces Windows to reinstall it cleanly from its driver store on the next boot.

1. In **Device Manager > Network adapters**, right-click the wireless adapter and choose **Uninstall device**.
2. Leave "Attempt to remove the driver for this device" **unchecked** — you want Windows to keep a copy.
3. Click **Uninstall**, then restart the laptop. Windows reinstalls the adapter automatically during boot.

If Windows can't find a working driver on its own, download the latest Wi-Fi driver for your adapter from [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — most laptop Wi-Fi chips are Intel — using another device, then install it via USB.

### Fix 4: Run the Network troubleshooter

The built-in troubleshooter can reset adapter configurations and repair common DNS, DHCP, and gateway problems through one guided flow.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Next to **Network and Internet**, click **Run**.
3. Follow the on-screen prompts, apply any fixes it suggests, then restart and test the connection.

### Fix 5: Reset the TCP/IP stack and Winsock

When the stack itself is corrupted, these commands rebuild it from scratch. You will need an administrator Command Prompt.

1. Right-click **Start**, choose **Terminal (Admin)**, and accept the UAC prompt.
2. Type `netsh winsock reset` and press Enter.
3. Type `netsh int ip reset` and press Enter.
4. Type `ipconfig /release`, press Enter, then type `ipconfig /renew` and press Enter.
5. Restart the laptop and reconnect to Wi-Fi.

### Fix 6: Forget the network and rejoin it

Updates can corrupt the saved profile for a network — its security settings, stored credentials, or IP lease. Forgetting it and rejoining builds a fresh profile.

1. Open **Settings > Network & internet > Wi-Fi** and click **Manage known networks**.
2. Find your network, click **Forget**.
3. Click **Show available networks**, select your network, enter the password, and connect.

### Fix 7: Uninstall the problematic update (last resort)

If Wi-Fi worked right up until a specific update and nothing else helped, removing that update can confirm it is the culprit. Note that Windows may reinstall it later.

1. Open **Settings > Windows Update > Update history > Uninstall updates**.
2. Find the most recent update by its install date, select it, and click **Uninstall**.
3. Restart when prompted. If Wi-Fi returns, pause updates (**Settings > Windows Update > Pause updates**) for a few weeks while the vendor ships a corrected driver.

Most post-update Wi-Fi problems trace back to the driver, and Fix 2 or Fix 3 alone resolves the majority of cases. If the adapter still misbehaves, download the driver directly from your laptop maker's support page rather than relying on the Windows Update version. And if this update broke more than Wi-Fi, a stuck installation may be behind it — our guide on [Windows Update stuck at 100%](/articles/windows-update-stuck-at-100-percent-fix/) covers that side of the problem. If the adapter vanishes from Device Manager entirely, a BIOS update from your laptop maker sometimes restores it.
