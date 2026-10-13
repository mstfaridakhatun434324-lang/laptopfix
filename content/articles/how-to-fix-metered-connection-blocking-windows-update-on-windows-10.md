---
title: "How to Fix a Metered Connection Blocking Windows Update on Windows 10"
slug: "how-to-fix-metered-connection-blocking-windows-update-on-windows-10"
date: 2026-10-09
categories: ["windows-update"]
tags: ["metered connection", "windows update", "windows 10", "network settings"]
description: "Metered connection blocking Windows Update on Windows 10? Find the hidden toggle, allow updates over metered networks, and get downloads moving again."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-on-windows-10.webp"
faqs:
  - q: "Where is the metered connection setting on Windows 10?"
    a: "Open Settings, go to Network and Internet, then Wi-Fi, and click your connected network. The “Set as metered connection” toggle lives there. If you connect through Ethernet instead, go to Network and Internet, then Ethernet, click the connection, and check the same toggle. The setting is per network profile, so check each connection type you actually use for updates."
  - q: "Why does Windows 10 keep treating my Wi-Fi as metered?"
    a: "Windows 10’s metered flag is stored per network name, so if you once enabled it for a hotspot or a network with the same SSID, it stays on every time you reconnect. Open the network’s properties and turn the toggle off. Also check for a configured data limit under Data usage, which can re-impose metered-like behavior even with the main toggle off."
  - q: "Can I force updates to download on a metered connection?"
    a: "Yes, with a trade-off. Under Settings, Update and Security, Windows Update, Advanced options, enable the option to download updates over metered connections. Quality and security updates will download normally. Be aware this can consume significant mobile data, so only use it when you accept the data cost or need a critical security fix urgently."
  - q: "Do privacy tools cause this metered block?"
    a: "Many debloat and privacy scripts set the metered flag (or the underlying registry value) to curb telemetry, and they rarely mention that Windows Update gets blocked too. If you ran such a tool, re-check the metered toggle on your networks after every script update, or undo the specific metered-related change rather than re-running the whole script blindly."
---

Your Windows 10 laptop sits on “Checking for updates” forever, or downloads crawl and die — and buried in the settings is the reason: Windows thinks your connection is metered. On Windows 10 the toggle is even easier to overlook than on Windows 11, living one click deeper inside each network’s properties page.

The underlying idea is the same across versions: a metered flag tells Windows to conserve data by deferring updates. But Windows 10 remembers the flag per network, applies it to Ethernet and USB tethering profiles too, and several popular tweaking tools set it silently. The [Windows 11 version of this fix](/articles/how-to-fix-metered-connection-blocking-windows-update-on-windows-11/) covers the newer Settings layout if that is the machine giving you trouble.

## Why this happens

- **Wi-Fi profile set as metered:** The classic cause: the active Wi-Fi connection has “Set as metered connection” enabled, carried over from hotspot use.
- **Metered flag on the Ethernet adapter:** Windows 10 (version 1703 and later) supports metered Ethernet; USB tethering setups often leave it enabled on the wired profile.
- **Per-network memory of the setting:** The metered flag is saved per known network, so rejoining a previously metered SSID silently re-blocks updates.
- **Data usage limit configured:** A data limit set under Network & Internet > Data usage makes Windows treat the connection as metered.
- **Registry metered override from tweaking tools:** Privacy and debloat tools sometimes set the metered flag via registry to block telemetry, with Windows Update blocked as collateral.
- **VPN adapter reporting metered:** Certain VPN clients create virtual adapters flagged as metered, and Windows honors the restriction while connected.
- **Delivery Optimization throttled by the same flag:** Metering also throttles peer-to-peer update sharing, so even partially allowed updates crawl on metered links.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Switch off the metered toggle on Wi-Fi

On Windows 10 the toggle sits on the Wi-Fi network’s own page — Settings > Network & Internet > Wi-Fi, then the network name. It is easy to miss because the main Wi-Fi page shows no hint that the connected network is metered.

1. Open Settings > Network & Internet > Wi-Fi.
2. Click your connected network name.
3. Turn off “Set as metered connection”.
4. Go to Update & Security > Windows Update and click Check for updates.

### Fix 2: Check the Ethernet and tethering profiles

Tetherers get bitten twice: the Wi-Fi hotspot profile and the USB-tethering Ethernet profile each carry their own flag. If updates work on home Wi-Fi but never on tethering, the tethering profile is the one still metered.

1. Open Settings > Network & Internet > Ethernet and click your wired connection.
2. Turn off “Set as metered connection” there too.
3. If you tether via phone USB, check the adapter Windows created for tethering as well.
4. Retry Windows Update after each profile is corrected.

### Fix 3: Allow updates over metered connections selectively

When the connection genuinely is capped — a hotel hotspot or a limited phone plan — unflagging it is the wrong move. Windows 10 lets you punch a narrow exception for updates instead, which is the safer compromise.

1. Open Settings > Update & Security > Windows Update > Advanced options.
2. Enable “Download updates over metered connections” (wording varies slightly by Windows 10 build).
3. Understand the cost: cumulative updates can exceed 1 GB, drivers add more.
4. Use this only on connections where you accept the data usage.

### Fix 4: Remove stale data limits

Data limits and metering are linked: a limit implies a cap, and Windows treats capped connections conservatively. Removing a stale limit (set for a trip months ago, for instance) often clears the block by itself.

1. Go to Settings > Network & Internet > Data usage.
2. Select the connection and remove any configured data limit.
3. Return to the network’s properties and confirm the metered toggle is Off.
4. Check for updates again.

### Fix 5: Clear Group Policy or registry overrides

Laptops that passed through corporate management or aggressive tweaking tools may carry policies that hard-block updates on metered links. These override the friendly toggles, so they must be cleared at the source.

1. Press Win + R, type gpedit.msc (Pro) and check Windows Update > “Do not connect to any Windows Update Internet locations” and Delivery Optimization policies.
2. On Home, open Registry Editor and inspect HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate for unexpected values.
3. Delete or reset values you did not set yourself (export the key first as backup).
4. Run gpupdate /force, restart, and test.

### Fix 6: Test with the VPN disconnected

Some VPN virtual adapters report a metered cost to Windows, triggering the block only while the tunnel is up. Testing with the VPN disconnected isolates the cause in seconds.

1. Disconnect the VPN and test Windows Update on the bare connection.
2. In the VPN client’s settings, look for virtual-adapter or “metered” options and disable them.
3. As a workaround, download the needed update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) while on VPN, then install offline.
4. For persistent issues, check the [Windows Update support hub](https://support.microsoft.com/en-us/windows) for VPN-related known issues.

### Fix 7: Schedule updates around capped data with active hours and pauses

On Windows 10 with a capped connection, the smartest play is often scheduling rather than blocking: let security updates download during an off-peak window when your plan offers unmetered data (many mobile plans zero-rate overnight traffic), and keep metering protection during expensive hours. Windows 10’s active hours and the 7-day pause control give you the levers, and the [Dell metered-connection walkthrough](/articles/how-to-fix-metered-connection-blocking-windows-update-on-dell-laptop/) shows the same scheduling approach applied on Dell hardware with its own connection utilities.

1. Open Settings > Update & Security > Windows Update > Change active hours and set them to your expensive-data window.
2. Use “Pause updates for 7 days” ahead of travel or billing-cycle boundaries.
3. When on genuinely free Wi-Fi, click “Resume updates” and let everything download at once.
4. Re-pause before returning to the capped connection.
5. Review Data usage monthly to confirm the schedule matches your plan’s free windows.

## Closing

On Windows 10 the metered block hides in the network profile properties — one toggle per connection. Flip it off where data is unlimited, or use the dedicated “download over metered” setting where it is not. Either choice takes under a minute and ends the standoff between your laptop and Windows Update.
