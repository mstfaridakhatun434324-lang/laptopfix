---
title: "How to Fix a Metered Connection Blocking Windows Update on Windows 11"
slug: "how-to-fix-metered-connection-blocking-windows-update-on-windows-11"
date: 2026-10-08
categories: ["windows-update"]
tags: ["metered connection", "windows update", "windows 11", "wi-fi settings"]
description: "Metered connection blocking Windows Update on Windows 11? Learn how to toggle the setting, allow updates over metered networks, and stop the block for good."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-on-windows-11.webp"
faqs:
  - q: "Why is my home Wi-Fi marked as metered when I never set it?"
    a: "Windows sometimes enables metering automatically when you first connect through a phone hotspot or when a data limit gets configured, and the flag is stored per network name. If your home SSID ever matched a hotspot name or the setting was toggled accidentally, it persists. Open the Wi-Fi network’s properties and switch Metered connection to Off — the change applies immediately to that saved network profile."
  - q: "Will turning off metered connection use a lot of mobile data?"
    a: "Yes, potentially. With metering off, Windows downloads quality updates, driver updates, and eventually feature updates in the background, which can consume several gigabytes per month. Only disable metering on genuinely unlimited connections. On capped hotspots, leave metering on and instead enable Download updates over metered connections so only essential updates download."
  - q: "Can I update Windows while keeping the metered flag on?"
    a: "Yes. Go to Settings, then Windows Update, then Advanced options, and turn on Download updates over metered connections. Security and quality updates will then download despite the metered flag. Feature updates may still be held back until you join an unmetered network, which is usually the behavior you want on a capped connection."
  - q: "Does metered connection block Microsoft Store app updates too?"
    a: "Yes, the Microsoft Store respects the metered flag and pauses automatic app updates on metered networks. The Store has its own related toggle under its Settings, but the system-level metered flag is the main gate. Turning metering off — or allowing the specific downloads you want — unblocks both Windows Update and Store updates together."
---

Your Windows 11 laptop refuses to download updates, and under Settings > Windows Update you see a quiet note that updates are paused or limited because of a metered connection. You are on your home Wi-Fi with unlimited data — so why does Windows think you are on a capped mobile hotspot?

Windows 11 lets any network be flagged as metered, and the flag sticks to the network profile: connect to a phone hotspot once with metering on, and Windows remembers that network as metered forever. The fix takes thirty seconds once you know where the toggle lives, but there is also a deeper setting that controls whether updates download over metered connections at all. If your other machine runs the older OS, the [Windows 10 metered-connection fix](/articles/how-to-fix-metered-connection-blocking-windows-update-on-windows-10/) covers its slightly different screens.

## Why this happens

- **Wi-Fi network flagged as metered:** The most common cause: the current Wi-Fi profile has “Metered connection” switched on, often set long ago for a hotspot and forgotten.
- **Ethernet connection metered by policy:** Windows 11 allows Ethernet to be metered too; some users enable it while tethering via USB and it stays on for the wired profile.
- **Metered flag remembered per network:** Windows stores the metered setting per SSID, so a network you marked metered months ago still blocks updates every time you join it.
- **Data limit configured on the connection:** Setting a data limit in Settings > Network automatically treats the connection as metered once the limit logic engages.
- **Group Policy restricting metered downloads:** On Pro editions, a policy can forbid all updates over metered connections, overriding the per-network toggle.
- **VPN or virtual adapter inheriting metered status:** Some VPN virtual adapters report themselves as metered, and Windows applies update restrictions while the VPN is active.
- **Updates paused, misread as a metered block:** A paused update state and a metered block look similar in the UI; users sometimes chase the metered setting when the real issue is a pause timer.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Turn off the metered flag on your current network

This is the fix in the majority of cases. The toggle lives on the network profile page, one level deeper than most people look — under the Wi-Fi network’s own properties, not the general network settings.

1. Open Settings > Network & internet > Wi-Fi.
2. Click your connected network name to open its properties.
3. Find “Metered connection” and switch it to Off.
4. Return to Windows Update and click “Check for updates” — downloads should start immediately.

### Fix 2: Check Ethernet and remembered networks too

If you use a dock or USB tethering, the active profile might be Ethernet rather than Wi-Fi. And if the block follows you to a specific network, that SSID’s saved profile is the culprit.

1. Go to Settings > Network & internet > Ethernet, open the connected network, and set Metered connection to Off.
2. For a recurring network: Settings > Network & internet > Wi-Fi > Manage known networks.
3. Open the problem SSID and switch its Metered connection toggle to Off.
4. Reconnect to the network so the new profile applies.

### Fix 3: Allow updates over metered connections anyway

If you genuinely use capped data but still want critical updates, Windows 11 can download updates over metered connections without unflagging the network. This is the right choice for metered hotspots you cannot unflag.

1. Open Settings > Windows Update > Advanced options.
2. Turn on “Download updates over metered connections”.
3. Note this covers quality and security updates; feature updates may still wait for unmetered Wi-Fi.
4. Monitor data usage afterward in Settings > Network & internet > Data usage.

### Fix 4: Remove any data limit on the connection

A configured data limit makes Windows treat the connection as metered-adjacent even with the toggle off. Clearing the limit removes the restriction cleanly.

1. Go to Settings > Network & internet > Advanced network settings > Data usage.
2. Select the limited connection and click “Remove limit”.
3. Confirm removal and re-check the Metered connection toggle is Off.
4. Retry Windows Update.

### Fix 5: Check Group Policy on Windows 11 Pro

A domain or previously applied policy can force metered restrictions regardless of your toggles. This is common on laptops that were once company-managed.

1. Press Win + R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration > Administrative Templates > Windows Components > Delivery Optimization.
3. Check “Download mode” and related metered-download policies for anything set to Enabled restrictively.
4. Set unwanted policies to Not Configured, run gpupdate /force, and test updates.

### Fix 6: Distinguish a real pause from a metered block

If updates say “paused” with a resume date, no metered toggle will help — you are looking at the pause feature, not a connection block. Clearing the pause is a separate one-click fix.

1. Open Settings > Windows Update and look for “Updates paused until” text.
2. Click “Resume updates” if a pause is active.
3. Also check Advanced options for the “Pause updates” toggle and any active-hours anomalies.
4. With the pause cleared and metering off, run Check for updates.

### Fix 7: Cap Delivery Optimization bandwidth on metered networks

If you allow updates over a metered connection, the next worry is Windows consuming the entire data allowance in one background session. Windows 11’s Delivery Optimization settings let you cap both foreground and background download bandwidth, so essential security updates trickle in without devouring a capped plan. Combined with the per-network metered flag and the [24H2-specific metered guidance](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/), this gives you fine-grained control: updates flow, but on your terms and within your data budget.

1. Open Settings > Windows Update > Advanced options > Delivery Optimization.
2. Open “Advanced options” and enable bandwidth limits.
3. Set “Limit how much bandwidth is used for downloading updates in the background” to a small percentage (10–20 percent).
4. Set an absolute monthly upload limit as well, so your connection is not used to serve updates to others.
5. Monitor actual usage under Settings > Network & internet > Data usage for a week and adjust.

## Closing

A metered connection block is Windows doing exactly what it was told to do — the fix is telling it otherwise. Switch the flag off on the network profile, or explicitly allow updates over metered connections if the cap is real. Either way, one settings change ends the block, and your updates resume on the next check.
