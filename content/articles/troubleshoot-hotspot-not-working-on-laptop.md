---
title: "Mobile Hotspot Not Working on Your Laptop? How to Fix It"
slug: troubleshoot-hotspot-not-working-on-laptop
date: "2026-09-13"
categories: ["drivers"]
tags: ["mobile hotspot", "wifi hotspot", "tethering", "internet sharing", "hotspot fix"]
description: "Can't turn on the mobile hotspot on your Windows laptop? Learn how to fix hotspot problems — driver support, band settings, power management, and sharing services."
thumbnail: "/images/thumbs/troubleshoot-hotspot-not-working-on-laptop.webp"
faqs:
- q: "Why can't I turn on the mobile hotspot on my laptop?"
  a: "The most common reasons are the wireless driver not supporting hosted networks, the WiFi adapter being disabled, or the hotspot toggle failing due to corrupted network settings. Windows 10 and 11 require the WiFi driver to support the hosted-network feature — older or generic drivers often do not. Checking driver capability first, then reinstalling the manufacturer's wireless driver, resolves the toggle failure in most cases."
- q: "Why do devices connect to my hotspot but get no internet?"
  a: "This means the hotspot radio works but internet sharing is broken — usually the Internet Connection Sharing service is misconfigured, the firewall is blocking the shared connection, or the laptop's own internet dropped. Verify the laptop itself has working internet first, then check that sharing is enabled on the correct connection in the adapter settings, and temporarily test with the firewall off to isolate blocking."
- q: "Should my hotspot use 2.4GHz or 5GHz?"
  a: "Use 5GHz when nearby devices support it — it is faster and less congested. Use 2.4GHz for older devices or better wall penetration and range. If devices cannot see your hotspot at all, they may only support 2.4GHz while your hotspot broadcasts 5GHz; switching the hotspot band in Settings usually makes it visible immediately. Some adapters only support one band for hosting, which Settings will indicate."
- q: "Can power saving break my laptop's hotspot?"
  a: "Yes. When the wireless adapter's power management switches the card off to save energy, an active hotspot drops with it — connected devices lose internet without warning. Disabling power saving on the wireless adapter in Device Manager is the permanent fix. This is one of the most common causes of hotspots that work for a while and then mysteriously die."
---

Your phone needs internet, the café WiFi is unusable, and your laptop's mobile hotspot — which worked last month — now refuses to turn on. Or it turns on, devices connect, and nothing loads. The mobile hotspot is one of Windows' most convenient features and one of its most fragile, because it asks the wireless adapter to do two jobs at once: stay connected upstream and broadcast downstream.

Hotspot failures split into two clear types: the toggle will not enable (a driver or settings problem), and the toggle enables but clients get no internet (a sharing or firewall problem). Knowing which you have aims the fix immediately. Both types are software problems in the large majority of cases — the wireless card hardware is rarely at fault.

Work through the fixes below in order, starting with the toggle checks.

## Why this happens

- **Wireless driver lacks hosted-network support**: Generic or outdated drivers do not implement the hotspot feature.
- **WiFi adapter disabled or power-managed**: A sleeping or disabled card cannot broadcast.
- **Corrupted network settings**: Damaged profiles and stack configuration break the hotspot toggle.
- **Wrong hotspot band**: 5GHz-only broadcast is invisible to 2.4GHz-only devices.
- **Internet Connection Sharing misconfigured**: Sharing enabled on the wrong adapter, or disabled entirely.
- **Firewall blocking shared traffic**: Third-party firewalls often block the hotspot subnet.
- **Windows services stopped**: The ICS and WLAN services the hotspot depends on are not running.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle, restart, and check the basics

Hotspot state can wedge just like any wireless feature — the toggle says on, but the underlying hosted network never started. A clean toggle cycle plus a restart clears the wedged state. While you are at it, confirm the laptop itself has working internet; a hotspot cannot share a connection the laptop does not have.

1. Go to Settings, Network and internet, Mobile hotspot, and turn it off.
2. Restart the laptop fully.
3. Turn the hotspot back on and check for an error message — note its exact wording.
4. Confirm the laptop's own internet works (browse a page on the laptop itself).
5. Try connecting a client device and observe: does it see the hotspot, connect, or get internet?

### Fix 2: Verify the driver supports hosted networks

Windows can only host a hotspot if the wireless driver implements the feature. Older drivers, generic Microsoft drivers, and some USB WiFi adapters lack it — in which case the toggle fails with an error about the hosted network. Checking capability takes one command and definitively answers whether the driver is the problem.

1. Open Terminal or Command Prompt as administrator.
2. Run `netsh wlan show drivers` and look for "Hosted network supported."
3. If it says No, the driver cannot host — update to the manufacturer's wireless driver.
4. Download the WiFi driver from your laptop maker's support page (for Intel cards, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) works too).
5. Install, restart, and rerun the command to confirm support now shows Yes.

### Fix 3: Reinstall the wireless driver

When the driver claims hosted-network support but the toggle still fails, the driver installation is corrupt. A clean reinstall — full removal, then the manufacturer's package — restores the hosted-network components. This also fixes hotspots that enable but drop clients within minutes.

1. Open Device Manager and expand "Network adapters."
2. Right-click the wireless adapter, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Restart the laptop.
4. Install the manufacturer's wireless driver and restart again.
5. Enable the hotspot and test with a client device for several minutes.

### Fix 4: Switch the hotspot band

A hotspot broadcasting on 5GHz is invisible to devices with 2.4GHz-only radios — older phones, many IoT gadgets, some laptops. The client "cannot find" a hotspot that is working perfectly. Switching the hotspot to 2.4GHz (or trying 5GHz if 2.4 is congested) resolves visibility complaints instantly.

1. Go to Settings, Network and internet, Mobile hotspot.
2. Open the hotspot properties and find the network band setting.
3. Change it to 2.4GHz and save.
4. On the client device, rescan for networks — the hotspot should now appear.
5. If 2.4GHz is slow or congested, switch back to 5GHz for capable devices afterward.

### Fix 5: Disable power saving on the wireless adapter

A hotspot that works for a while then dies — clients suddenly disconnected, toggle still "on" — is the signature of adapter power management. Windows puts the card to sleep to save energy, killing the broadcast. The fix is permanent and costs negligible battery: tell Windows never to power down the adapter.

1. In Device Manager, right-click the wireless adapter and open Properties.
2. On the Power Management tab, untick "Allow the computer to turn off this device to save power."
3. On the Advanced tab, set power-saving properties to "Maximum Performance."
4. Click OK and restart.
5. Run the hotspot for an extended session to confirm it stays up.

### Fix 6: Repair Internet Connection Sharing and the firewall

When clients connect to the hotspot but get no internet, the radio works and sharing is broken. Internet Connection Sharing must be enabled on the upstream connection (your WiFi or Ethernet), and the firewall must allow the hotspot subnet. Checking both covers the sharing path end to end.

1. Open `ncpa.cpl` (Win + R), right-click your internet connection (WiFi or Ethernet), and open Properties.
2. On the Sharing tab, tick "Allow other network users to connect through this computer's Internet connection."
3. In the dropdown, select the hotspot's virtual adapter if listed.
4. Temporarily disable any third-party firewall and test — if internet flows, add an exception for the hotspot subnet.
5. In services.msc, confirm "Internet Connection Sharing" is running and set to Automatic (Manual trigger is normal on some builds).

### Fix 7: Reset the network stack

When the toggle fails with unhelpful errors after all the above, the network configuration itself is corrupt — damaged profiles, broken virtual adapters, poisoned stack state. The network reset reinstalls every adapter and rebuilds all settings from defaults. It deletes saved WiFi passwords, so note them first. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the reset alongside other network recovery options.

1. Note your WiFi passwords — the reset deletes saved networks.
2. Go to Settings, Network and internet, Advanced network settings, "Network reset."
3. Click "Reset now" and let the PC restart.
4. Reinstall the manufacturer's wireless driver after the reset for the cleanest state.
5. Reconfigure the hotspot (name, password, band) and test with a client.

If the underlying WiFi itself is broken rather than just the hotspot, fix that first — the [ASUS laptop WiFi guide](/articles/how-to-fix-wifi-not-working-on-asus-laptop/) and the [WiFi adapter not showing up guide](/articles/wifi-adapter-not-showing-up-troubleshooting/) cover those foundations.

## Closing

Hotspot failures are either toggle failures (driver capability, corrupt driver, wedged state) or sharing failures (ICS, firewall, band mismatch). Verify hosted-network support, reinstall the manufacturer's wireless driver, disable adapter power saving, and check the sharing path. Worked in that order, these steps restore the hotspot on nearly every laptop — the wireless card hardware is almost never the problem.
