---
title: "The Best Way to Fix a Laptop Hotspot That Won't Work"
slug: best-way-to-fix-hotspot-not-working-on-laptop
date: 2026-09-03
categories: ["drivers"]
tags: ["mobile hotspot", "wifi hotspot", "tethering", "network adapter"]
description: "Can't share your laptop's internet as a hotspot? The fastest fix sequence for mobile hotspot failures on Windows 10 and 11."
thumbnail: "/images/thumbs/best-way-to-fix-hotspot-not-working-on-laptop.webp"
faqs:
  - q: "Why does my mobile hotspot turn on but devices can't connect?"
    a: "The hotspot radio is broadcasting, but the hosted-network or ICS layer behind it is broken. The usual culprits are a Wi-Fi driver that doesn't support hosted networks, the Internet Connection Sharing service being disabled, or a third-party firewall blocking client traffic. Updating the Wi-Fi driver and resetting the network stack resolves most of these cases."
  - q: "Why does Windows say 'we can't set up mobile hotspot'?"
    a: "That error means the Wi-Fi adapter reported it can't create a hosted network — almost always a driver limitation or a disabled adapter. Check that Wi-Fi is turned on (the hotspot needs the radio even when sharing a wired connection), update the wireless driver from the manufacturer, and confirm the adapter supports hosted networks with a quick command-line check."
  - q: "Can I share my laptop's Wi-Fi connection over hotspot at the same time?"
    a: "Yes, if your Wi-Fi adapter supports it — most modern Intel and Realtek adapters do. The adapter connects to the upstream Wi-Fi and simultaneously broadcasts the hotspot SSID. Older or budget adapters lack this dual-mode capability, in which case you can only share a wired Ethernet connection, not re-share Wi-Fi."
  - q: "Does using mobile hotspot require a special driver?"
    a: "No special driver — just a current, manufacturer-provided Wi-Fi driver. Windows' generic Wi-Fi drivers sometimes lack hosted-network support even when the hardware has it. Installing the wireless driver from your laptop maker's site (Intel, Realtek, or MediaTek as equipped) is the single most effective hotspot fix."
---

The mobile hotspot toggle is on, your phone sees the network name, and then… nothing. Or devices connect but get no internet. Or Windows refuses outright with "we can't set up mobile hotspot." Sharing your laptop's connection should be a two-click feature, and when it fails it fails in confusing ways — because a hotspot is really three systems cooperating: the Wi-Fi radio, the hosted-network driver layer, and Internet Connection Sharing.

This is the priority-ordered fix sequence: the steps with the highest success rate first, so most people stop early. It starts with the radio and driver (where the vast majority of hotspot failures live), moves through Windows' sharing services and stack resets, and ends with the adapter-level checks for stubborn cases. If your failure began after a Windows feature update, the focused [hotspot fix for Windows 11 24H2](/articles/how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2/) covers the update-specific breakage.

## Why this happens

- **The Wi-Fi driver doesn't support hosted networks.** Generic or outdated drivers often lack the hosted-network capability the hotspot needs — the toggle appears, but setup fails.
- **Wi-Fi is turned off.** The hotspot needs the wireless radio even when sharing a wired connection; with Wi-Fi off, there's nothing to broadcast with.
- **Internet Connection Sharing (ICS) is disabled or broken.** The service that routes client traffic can be stopped by updates, "optimizer" tools, or corrupted configuration.
- **A VPN or third-party firewall is intercepting traffic.** These sit between the hotspot and the internet and commonly block client devices while the laptop itself browses fine.
- **The network stack is corrupted.** Winsock and TCP/IP corruption breaks the NAT layer the hotspot depends on, producing "connected, no internet" on clients.
- **Power management suspended the adapter.** The Wi-Fi card powers down under load or on battery, dropping all hotspot clients at once.
- **The adapter genuinely lacks hotspot capability.** Rare on modern laptops, but some budget wireless cards can't do hosted networks at all — no software fixes hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the hosted-network capability

Thirty seconds to learn whether the hardware can even do this.

1. Open an **elevated Command Prompt** (Win + X > Terminal (Admin)).
2. Run: `netsh wlan show drivers` and look for **Hosted network supported: Yes**.
3. If it says **No**, update the Wi-Fi driver from your laptop manufacturer's site (Fix 2) and check again — many adapters gain the capability with the proper OEM driver.
4. If it still says No after the OEM driver, the adapter hardware lacks support; a USB Wi-Fi adapter with hotspot support ($15–20) is the practical answer.

### Fix 2: Install the manufacturer's Wi-Fi driver

The single highest-success hotspot fix. Windows' generic wireless driver is the usual culprit.

1. Identify your wireless card: **Device Manager > Network adapters** (typically *Intel Wi-Fi 6 AX201/AX211*, *Realtek*, or *MediaTek*).
2. Download the Wi-Fi driver for your exact model from the laptop maker's support site — or use Intel's detection tool at the [Intel driver support page](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards.
3. In Device Manager, right-click the Wi-Fi adapter > **Uninstall device** (check *Attempt to remove the driver*), then install the downloaded package as administrator and reboot.
4. Re-run `netsh wlan show drivers` — hosted network support should now read Yes. Retry the hotspot.

### Fix 3: Turn Wi-Fi on and reset the hotspot configuration

The simple state fixes that resolve a surprising share of cases.

1. Make sure **Wi-Fi is turned on** — **Settings > Network & internet > Wi-Fi** — even if you're sharing a wired Ethernet connection. The hotspot broadcasts over the Wi-Fi radio. If the Wi-Fi option itself is missing from Settings, fix that first with our [Wi-Fi disappeared guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) — the hotspot can't work until the adapter is back.
2. Go to **Settings > Network & internet > Mobile hotspot**, turn it **Off**, then change the **Network name** and **password** (this forces Windows to regenerate the hosted profile), then turn it back **On**.
3. Under **Share my internet connection from**, select the correct source — **Wi-Fi** or **Ethernet** — matching how the laptop itself gets online.
4. Forget the hotspot network on your phone/other device and reconnect fresh; stale saved profiles with old passwords cause silent connection failures.

### Fix 4: Restart ICS and reset the network stack

When clients connect but get no internet, the sharing layer is the suspect.

1. Press **Win + R**, type `services.msc`, and find **Internet Connection Sharing (ICS)** — set its Startup type to **Automatic** and start it if it's stopped.
2. In an elevated Command Prompt, run:
   `netsh winsock reset`
   `netsh int ip reset`
   then restart the laptop.
3. After reboot, turn the hotspot off and on once to rebuild its NAT configuration cleanly.
4. If a third-party firewall or VPN is installed, temporarily disable it and test — if the hotspot works with it off, add an exception or configure split tunneling rather than leaving protection down.

### Fix 5: Disable power management on the Wi-Fi adapter

For hotspots that work briefly then drop all clients.

1. **Device Manager > Network adapters** > right-click your Wi-Fi adapter > **Properties > Power Management** > uncheck *Allow the computer to turn off this device to save power*.
2. In **Settings > System > Power & battery**, set the power mode to **Best performance** while testing — aggressive battery saver throttles the radio.
3. On the adapter's **Advanced** tab, look for **Power Saving Mode** or **Roaming Aggressiveness** and set them to **Maximum Performance** / lowest roaming while using the hotspot.
4. Keep the laptop plugged in during hotspot use; on battery, Windows may still throttle the radio regardless of settings.

### Fix 6: Use the 5 GHz band and check client limits

Congestion and band issues masquerade as hotspot failure.

1. In **Mobile hotspot** settings, set **Network band** to **5 GHz** if your adapter and client devices support it — the 2.4 GHz band in apartment buildings is often too congested for a usable hotspot.
2. If clients can't see the 5 GHz network, their own Wi-Fi may be 2.4 GHz-only — switch back and accept the slower band.
3. Windows allows up to 8 simultaneous hotspot clients; if you're at the limit, new devices fail silently. Disconnect idle devices.
4. Move the client devices closer for testing — hotspot range from a laptop radio is shorter than from a router, and weak signal looks like "no internet."

### Fix 7: Rebuild the hotspot via command line

When the Settings UI is wedged, the command-line path bypasses it.

1. In an elevated Command Prompt, tear down the current hosted network:
   `netsh wlan stop hostednetwork`
2. Reconfigure it manually:
   `netsh wlan set hostednetwork mode=allow ssid=YourName key=YourPassword123`
3. Start it:
   `netsh wlan start hostednetwork`
4. Then enable sharing manually: `ncpa.cpl` > right-click your internet source adapter > **Properties > Sharing** > check *Allow other network users to connect*, selecting the hosted connection. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the current hotspot UI if the command-line and UI behaviors diverge after an update.

## Closing

Hotspot failures are driver failures in disguise more often than not — the manufacturer's Wi-Fi driver restores hosted-network support that Windows' generic driver never had, and everything downstream (ICS, the stack, the band settings) only matters once the radio can actually host. Get the right driver in, keep the radio awake, and the two-click feature goes back to being two clicks.
