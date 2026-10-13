---
title: "Fix Mobile Hotspot That Won't Work on a Laptop in Windows 11 24H2"
slug: how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-01
categories: ["drivers"]
tags: ["mobile hotspot", "windows 11 24h2", "hotspot not working", "wifi sharing", "ics"]
description: "Fix Windows 11 24H2 mobile hotspot failures: hosted network support checks, adapter driver repair, and Internet Connection Sharing resets."
thumbnail: "/images/thumbs/how-to-fix-hotspot-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why is mobile hotspot not working after the 24H2 update?"
    a: "The update frequently breaks the Microsoft Wi-Fi Direct Virtual Adapter driver, disables the wireless driver's hosted-network capability, or corrupts the Internet Connection Sharing bindings. Reinstalling the Wi-Fi driver package and resetting the ICS configuration restores the hotspot in the large majority of cases."
  - q: "How do I check if my Wi-Fi adapter supports hosted networks?"
    a: "Open Command Prompt and run netsh wlan show drivers, then find the Hosted network supported line. Yes means the radio hardware and driver can host a network; No means the adapter or its current driver lacks the capability. Updating to the vendor's driver package sometimes flips a No to Yes."
  - q: "Why do devices connect to my hotspot but get no internet?"
    a: "The hotspot radio path works but Internet Connection Sharing is broken — the upstream internet connection is not being shared with the virtual adapter. Open the upstream connection's Properties, then the Sharing tab, re-enable sharing, and select the hotspot adapter in the dropdown. The phone will get internet immediately after."
  - q: "Does the hotspot need the Wi-Fi to be on or off?"
    a: "The Wi-Fi adapter must be enabled, because the hotspot runs on a virtual adapter built on top of the physical Wi-Fi radio. Windows 11 shares whatever connection is active — Wi-Fi, Ethernet, or cellular — but the radio hardware underneath the virtual adapter has to be powered on for the hotspot to broadcast."
---

Mobile hotspot on Windows 11 24H2 fails in two distinct ways: the hotspot will not turn on at all ("We can't set up mobile hotspot"), or it turns on but connected devices get no internet. The two failures live in different layers — the first is the virtual Wi-Fi adapter and its driver, the second is Internet Connection Sharing. Identifying which one you have aims every fix below, so test both: toggle the hotspot on, then connect a phone and check whether it reaches the internet.

24H2's driver migration is rough on the virtual adapter stack (Microsoft Wi-Fi Direct Virtual Adapter), which is why hotspots that worked for years break overnight. The hardware is fine; the hosted-network plumbing needs repair.

## Why this happens

- **Virtual adapter driver broken:** 24H2 corrupts or replaces the Microsoft Wi-Fi Direct Virtual Adapter driver the hotspot depends on.
- **Hosted network support disabled:** The wireless driver's hosted-network capability gets turned off during migration.
- **Internet Connection Sharing misconfigured:** ICS bindings break, so the hotspot broadcasts but shares no upstream connection.
- **Wi-Fi driver replaced with incompatible version:** A generic driver that lacks hosted-network support replaces the vendor driver.
- **Third-party VPN/firewall interference:** VPN clients and firewalls hijack the network stack and block the hotspot's NAT path.
- **Power management disabling the adapter:** The Wi-Fi adapter sleeps, taking the virtual hotspot adapter down with it.
- **Corrupted hotspot settings:** Stale network name/password profiles and band settings from before the update conflict with the new stack.
- **Adapter hardware lacks hosted support:** Some radios genuinely cannot host a network — rare on modern laptops, but the check is quick.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify hosted network support

1. Open Command Prompt and run `netsh wlan show drivers`.
2. Find **Hosted network supported** — it must say **Yes**.
3. If **No**, update the Wi-Fi driver from your vendor ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) or chip maker ([Intel](https://www.intel.com/content/www/us/en/support/detect.html)) — hosted support is driver-dependent.
4. If it says Yes, the hardware path is fine and the problem is configuration — continue.

### Fix 2: Reinstall the Wi-Fi and virtual adapter drivers

1. In **Device Manager → Network adapters**, right-click your physical Wi-Fi adapter → **Uninstall device** (check **Attempt to remove the driver**).
2. Also uninstall **Microsoft Wi-Fi Direct Virtual Adapter** entries (enable **View → Show hidden devices** to see them — the [hidden devices guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) covers this view).
3. Reboot. Windows rebuilds both the physical and virtual adapters.
4. Install the vendor's Wi-Fi driver package, reboot again, and test the hotspot toggle in **Settings → Network & internet → Mobile hotspot**.

### Fix 3: Reset the hotspot configuration

1. Go to **Settings → Network & internet → Mobile hotspot**.
2. Turn it **Off**, change **Share my internet connection from** to your actual upstream (Wi-Fi or Ethernet), and set **Share over** to **Wi-Fi**.
3. Click **Edit** under Properties and set a new network name and password (8+ characters).
4. Toggle the hotspot on. Stale pre-24H2 profiles with incompatible band settings are a common silent failure. Take a screenshot of the working settings once the hotspot runs — the next Windows feature update may reset them, and the screenshot makes reconfiguration a one-minute job.

### Fix 4: Repair Internet Connection Sharing

1. Open **Control Panel → Network and Internet → Network Connections**.
2. Right-click your upstream connection (the one with internet) → **Properties → Sharing** tab.
3. Check **Allow other network users to connect through this computer's Internet connection** and select the hotspot/virtual adapter in the dropdown.
4. If the Sharing tab is missing, the **Internet Connection Sharing** service may be disabled — start it in `services.msc` and set it to **Manual**.
5. Retest with a phone: connect to the hotspot and browse. ICS repair fixes the "connected, no internet" variant.

### Fix 5: Disable VPN, firewall, and third-party network tools

1. Disconnect any VPN completely (not just pause — quit the client).
2. Temporarily disable third-party firewalls/antivirus network filtering.
3. In an elevated prompt, run `netsh winsock reset` and `netsh int ip reset`, then reboot.
4. Test the hotspot. VPN virtual adapters are notorious for capturing the NAT path the hotspot needs; if the hotspot works with the VPN off, configure split tunneling or an exclusion.

### Fix 6: Disable power management on the Wi-Fi adapter

1. **Device Manager → Network adapters → Wi-Fi adapter → Properties → Power Management** → uncheck **Allow the computer to turn off this device to save power**.
2. In the **Advanced** tab, set **Power Saving Mode** to **Maximum Performance**.
3. Hotspots that work for a few minutes then die are the signature of the adapter sleeping — this fix targets exactly that pattern. Similar wireless power issues are covered in the [Intel Wi-Fi fix guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

### Fix 7: Reset the network stack as a last resort

1. **Settings → Network & internet → Advanced network settings → Network reset → Reset now**.
2. Reboot and reinstall the vendor Wi-Fi driver (the reset reinstalls adapters with generic drivers).
3. Reconfigure the hotspot from scratch (Fix 3) and re-enable ICS (Fix 4).
4. If the hotspot still fails after a full reset with vendor drivers, test with a USB Wi-Fi adapter that supports hosted networks — this isolates whether the internal radio's hosted capability is genuinely broken. Microsoft documents hotspot requirements in [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

Hotspot failures split cleanly: won't turn on means the virtual adapter/driver layer, turns on but no internet means Internet Connection Sharing. Document which fix restored your hotspot — ICS bindings and virtual adapter drivers are the two components most likely to break again in the next feature update. Verify hosted-network support, reinstall the Wi-Fi and virtual adapter drivers, reconfigure the hotspot cleanly, and repair ICS bindings — in that order.
