---
title: "Laptop Hotspot Not Working? What to Do About It"
slug: "what-to-do-if-hotspot-not-working-on-laptop"
date: "2026-09-26"
categories: ["drivers"]
tags: ["mobile hotspot", "hotspot not working", "wifi sharing", "windows 11"]
description: "Can't turn on mobile hotspot, or devices connect but get no internet? Diagnose and fix Windows laptop hotspot failures with this practical guide."
thumbnail: "/images/thumbs/what-to-do-if-hotspot-not-working-on-laptop.webp"
faqs:
  - q: "Why does my mobile hotspot turn off by itself?"
    a: "The hotspot toggle flipping back off usually means the Wi-Fi driver does not support hosted networks, the radio got disabled, or power management shut the adapter down. Verify hosted-network support with netsh wlan show drivers, update the Wi-Fi driver, and disable adapter power saving."
  - q: "Why do devices connect to my hotspot but get no internet?"
    a: "This is an Internet Connection Sharing problem: the hotspot network is running, but the upstream connection is not actually being shared to it. Open the upstream connection's Properties, Sharing tab, enable sharing, and select the hotspot's virtual adapter — or check that the ICS service is running."
  - q: "Can a VPN break the Windows mobile hotspot?"
    a: "Yes, frequently. VPN clients reroute network traffic and often block the NAT and DHCP functions the hotspot needs. Disconnect the VPN to test; if the hotspot works, configure split tunneling or an exception for the hotspot network rather than disabling the VPN entirely."
  - q: "Why is my laptop hotspot so slow?"
    a: "Hotspot speed is limited by the upstream connection, the Wi-Fi band, and client count. Use the 5 GHz band for speed (2.4 GHz for compatibility), keep the laptop plugged in, limit connected devices, and remember the laptop's single radio is doing double duty — receiving and transmitting simultaneously."
---

Windows mobile hotspot failures split into two distinct problems with different fixes. Problem one: the hotspot toggle is grayed out, flips back off immediately, or throws an error like 'We can't set up mobile hotspot' — the hotspot will not start at all. Problem two: the hotspot starts and devices connect, but they get no internet access — the hotspot runs but does not share.

The underlying machinery is the hosted-network feature of your Wi-Fi adapter plus Windows Internet Connection Sharing. Both depend on the Wi-Fi driver supporting hosted networks, the network adapters being in a clean state, and the sharing configuration pointing at the right connection. When any of those break, the hotspot fails in one of the two ways above.

Identify which problem you have before starting: toggle behavior versus connected-but-no-internet. The fixes below address both, in an order that handles the most common causes first.

## Why this happens

- ****Wi-Fi driver lacks hosted-network support**:** Some driver versions — notably certain Intel and Realtek builds — report hosted-network support as 'No,' which disables the hotspot feature entirely.
- ****Airplane mode or Wi-Fi radio off**:** The hotspot needs the Wi-Fi radio active. Airplane mode or a disabled radio kills the toggle.
- ****Corrupted network adapter state**:** Stale virtual adapters (the 'Local Area Connection* 12' entries) from previous hotspot sessions can wedge the feature.
- ****Internet Connection Sharing misconfigured**:** ICS must share from the correct upstream connection to the hotspot's virtual adapter. Wrong bindings mean connected devices get no internet.
- ****Bluetooth interfering with the radio**:** On some adapters, active Bluetooth disrupts the hosted network, particularly on 5 GHz.
- ****Third-party firewall or VPN blocking sharing**:** VPN clients and strict firewalls often block the NAT and DHCP functions the hotspot depends on.
- ****Power management disabling the adapter**:** If Windows powers down the Wi-Fi adapter, the hotspot collapses — sometimes mid-session.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the Radio and Driver Support

Make sure Wi-Fi is on and airplane mode is off — the hotspot toggle grays out without an active radio. Then verify hosted-network support: open Command Prompt and run netsh wlan show drivers, looking for 'Hosted network supported: Yes.' If it says No, update your Wi-Fi driver from Intel or your laptop maker — newer builds usually restore support.

If your adapter genuinely lacks hosted-network support, no Windows setting will enable the hotspot; a USB Wi-Fi adapter with hosted-network support is the workaround. For related wireless disappearance issues, see our [Wi-Fi adapter fix guide](/articles/best-way-to-fix-wifi-adapter-not-showing-up/).

1. 1. Turn on Wi-Fi and confirm airplane mode is off.
2. 2. Run netsh wlan show drivers in Command Prompt.
3. 3. Check 'Hosted network supported' reads Yes.
4. 4. Update the Wi-Fi driver if it reads No.
5. 5. Consider a USB Wi-Fi adapter if support is permanently absent.

### Fix 2: Clean Up Stale Virtual Adapters

In Device Manager, enable View, Show hidden devices, and expand Network adapters. Delete any grayed-out 'Microsoft Wi-Fi Direct Virtual Adapter' entries and old 'Local Area Connection*' miniport entries — these are leftovers from previous hotspot sessions that wedge new ones. Restart afterward.

Then open an elevated Command Prompt and run netsh wlan stop hostednetwork followed by netsh wlan start hostednetwork to reset the hosted-network state cleanly before retrying the Settings toggle.

1. 1. In Device Manager, show hidden devices.
2. 2. Delete grayed-out virtual Wi-Fi adapters.
3. 3. Restart the laptop.
4. 4. Run netsh wlan stop hostednetwork, then start hostednetwork.
5. 5. Retry the hotspot toggle in Settings.

### Fix 3: Fix Internet Connection Sharing

For connected-but-no-internet: open Control Panel, Network and Internet, Network Connections. Right-click your upstream connection (Ethernet or the Wi-Fi you are sharing from), choose Properties, go to the Sharing tab, and check 'Allow other network users to connect through this computer's Internet connection,' selecting the hotspot's virtual adapter in the dropdown.

If the Sharing tab is missing, the ICS service may be disabled — check services.msc for 'Internet Connection Sharing (ICS)' and set it to Automatic. Misconfigured ICS is the number-one cause of the connected-but-no-internet variant. Our [hotspot-specific guide](/articles/how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2/) covers additional ICS scenarios.

1. 1. Open Network Connections in Control Panel.
2. 2. Open the upstream connection's Properties, Sharing tab.
3. 3. Enable sharing and select the hotspot virtual adapter.
4. 4. Verify the ICS service is set to Automatic in services.msc.
5. 5. Reconnect client devices and test internet access.

### Fix 4: Reset the Network Stack

When the hotspot toggle flips itself off or throws setup errors, reset everything: run netsh winsock reset and netsh int ip reset in an elevated Command Prompt, then use Settings, Network and internet, Advanced network settings, Network reset. Restart when prompted.

This clears corrupted adapter bindings and NAT state in one pass. You will need to re-enter Wi-Fi passwords afterward, but the hotspot configuration rebuilds cleanly from defaults — which is exactly what you want when the old configuration was the problem.

1. 1. Run netsh winsock reset and netsh int ip reset as administrator.
2. 2. Perform a Network reset in Settings.
3. 3. Restart when prompted.
4. 4. Reconnect to your Wi-Fi network.
5. 5. Enable the hotspot and test with a client device.

### Fix 5: Disable VPN, Firewall Interference, and Bluetooth

Temporarily disconnect your VPN — VPN clients reroute all traffic and frequently break hotspot NAT. If the hotspot works with the VPN off, configure split tunneling or an exception rather than leaving the VPN off permanently. Similarly, test with third-party firewall features paused.

Also try turning Bluetooth off during hotspot use. On several Intel and Realtek adapters, active Bluetooth degrades or kills the hosted network, especially on 5 GHz — switching the hotspot to 2.4 GHz in Settings, Network and internet, Mobile hotspot can also help.

1. 1. Disconnect the VPN and test the hotspot.
2. 2. Temporarily pause third-party firewall features.
3. 3. Turn off Bluetooth during hotspot use.
4. 4. Set the hotspot band to 2.4 GHz in Settings.
5. 5. Re-enable protections with proper exceptions afterward.

### Fix 6: Prevent Power Management From Killing the Hotspot

In Device Manager, open your Wi-Fi adapter's properties and uncheck 'Allow the computer to turn off this device to save power' on the Power Management tab. In your power plan's advanced settings, set wireless adapter power saving to Maximum Performance. Hotspots that die after a few minutes — or when the laptop idles — are the signature of this cause.

Also keep the laptop plugged in during hotspot use when possible. On battery, Windows is more aggressive about powering down the radio, and some adapters cannot sustain hosted-network mode on battery power saving at all. Microsoft covers hotspot requirements in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. 1. Disable power-saving on the Wi-Fi adapter in Device Manager.
2. 2. Set wireless power saving to Maximum Performance.
3. 3. Keep the charger connected during hotspot use.
4. 4. Test a sustained hotspot session of 30 minutes.
5. 5. If stable, power management was the cause.

## Closing

Hotspot failures are configuration problems, not mysteries: verify the radio and hosted-network support, clean up stale virtual adapters, fix the ICS binding, and keep VPNs and power management from interfering. The connected-but-no-internet variant is ICS nine times out of ten — check the Sharing tab before anything else.
