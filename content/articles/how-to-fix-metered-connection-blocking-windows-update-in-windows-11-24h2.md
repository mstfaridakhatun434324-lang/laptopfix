---
title: "Metered Connection Blocking Windows Update on Windows 11 24H2? Here's the Fix"
slug: how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2
date: 2026-09-27
categories: ["windows-update"]
tags: ["metered connection", "windows update", "windows 11 24h2", "wifi settings", "update blocked"]
description: "Windows 11 24H2 refuses to download updates on a metered connection? Learn why it happens and how to allow updates safely without burning through your data."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2.webp"
faqs:
  - q: "Why does Windows 11 block updates on a metered connection?"
    a: "A metered connection tells Windows the network has a data cap or charges per megabyte. To protect you from surprise bills, Windows 11 pauses most update downloads — including cumulative updates and some driver updates — until you're on an unmetered network or you explicitly override the setting."
  - q: "Is it safe to let updates download over a metered connection?"
    a: "It depends on your data budget. Security updates are small and worth the megabytes, but a feature update or 24H2 enablement package can be several gigabytes. If you override the setting, do it on Wi-Fi you trust and pause again afterward, or schedule the download when you have spare data."
  - q: "Will turning off the metered setting affect anything else?"
    a: "Yes — apps like OneDrive, Microsoft Store, and some sync services also throttle themselves on metered connections to save data. Clearing the metered flag restores their normal background behavior, which can raise data usage. If you only want updates, allow them per-update instead of disabling metering entirely."
  - q: "The metered toggle is greyed out. How do I change it?"
    a: "On some managed or mobile-broadband connections Windows locks the toggle. Try Settings > Network & internet > your connection and check for a policy message. On cellular, you can also allow updates over metered connections directly in Windows Update > Advanced options without touching the metered flag itself."
---

Nothing is more confusing than a laptop that says updates are available but stubbornly refuses to download a single byte. You click Download, the progress ring spins for a moment, and then... nothing. Or worse, Windows Update cheerfully reports "You're up to date" when you know you aren't. If your Wi-Fi network is marked as metered, that is not a bug — it is Windows 11 doing exactly what you (or someone) told it to do: treat this network like expensive mobile data and download as little as possible.

The metered connection feature made sense in the era of strict data caps, but it causes real problems in 2026. Hotspot tethering from a phone with an unlimited plan gets flagged as metered. A home router with a captive portal or a USB tethering setup can trigger it too. And on Windows 11 24H2, Microsoft tightened the behavior: more update types now respect the metered flag than in older builds. The good news is that you have fine-grained control — you can let critical updates through without throwing the data-saving doors wide open.

## Why this happens

- **The Wi-Fi network is flagged as metered**: Someone (maybe you, months ago) toggled "Metered connection" on for this network, and Windows remembers it per network profile.
- **Cellular and tethered connections default to metered**: Mobile broadband and phone hotspots are automatically treated as metered to protect your data plan.
- **24H2 expanded what respects the metered flag**: Feature updates, driver updates, and Microsoft Store app updates all pause on metered connections in 24H2.
- **A VPN or proxy changed the network profile**: Some VPN adapters register as new metered connections, silently blocking updates while connected.
- **Group Policy enforces metered behavior**: On work or school laptops, an administrator policy may force updates to wait for unmetered networks.
- **Windows Update's own metered toggle is off**: Even on an unmetered network, the separate "Download updates over metered connections" switch in Advanced options may be disabled.
- **Corrupt network profile data**: Rarely, a damaged Wi-Fi profile keeps the metered flag stuck even after you toggle it off.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the metered flag is the actual culprit

Before changing anything, verify that metering is what's blocking the download. Open **Settings > Windows Update** and look for a message like "Updates are paused because this device is on a metered connection" or a banner under the Download button. Then go to **Settings > Network & internet > Wi-Fi**, click your connected network, and check whether **Metered connection** is toggled on. If it is, you've found your blocker. If it isn't, the problem is elsewhere — [our guide to the update service not running](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/) covers the next most likely cause.

1. Open **Settings** with **Win + I**.
2. Go to **Windows Update** and read any banner text carefully.
3. Go to **Network & internet > Wi-Fi** and click your network name.
4. Note whether **Metered connection** is on.

### Fix 2: Turn off the metered flag for trusted networks

If the network is your home Wi-Fi with no real data cap, the simplest fix is to clear the flag. Windows applies metering per network, so turning it off for your home network won't affect your phone hotspot.

1. Go to **Settings > Network & internet > Wi-Fi**.
2. Click the connected network (or the **i** icon next to it).
3. Toggle **Metered connection** to **Off**.
4. Return to **Settings > Windows Update** and click **Check for updates**.
5. Downloads should begin within a minute or two.

### Fix 3: Allow updates over metered connections without disabling metering

If you genuinely have a data cap but still want security patches, Windows 11 lets you permit updates specifically while keeping everything else throttled. This is the surgical option.

1. Go to **Settings > Windows Update > Advanced options**.
2. Find **Download updates over metered connections** and toggle it **On**.
3. Below it, review **Notify me when a restart is required** so big updates don't surprise you.
4. Click **Check for updates** on the main Windows Update page.
5. After critical updates install, consider toggling this back off if data is tight.

### Fix 4: Fix cellular and hotspot connections that default to metered

Phone hotspots and USB tethering almost always register as metered. If your phone plan is unlimited, you can clear the flag the same way — but check your carrier's hotspot allowance first, because many "unlimited" plans throttle hotspot data after 30–50 GB.

1. Connect to the hotspot, then open **Settings > Network & internet**.
2. Click **Wi-Fi** (hotspot) or **Mobile** (USB tethering) and open the connection properties.
3. Toggle **Metered connection** to **Off**.
4. Alternatively, leave metering on and enable **Download updates over metered connections** in Windows Update > Advanced options.
5. Monitor usage in **Settings > Network & internet > Advanced network settings > Data usage** so a 5 GB cumulative update doesn't eat your allowance.

### Fix 5: Check for Group Policy or MDM restrictions

On a work or school laptop, an administrator may have locked the metered behavior. You'll know because the toggle is greyed out or a "Some settings are managed by your organization" message appears.

1. Look for the managed-by-organization notice in **Settings > Windows Update**.
2. Press **Win + R**, type `gpedit.msc`, and press Enter (Pro editions only).
3. Navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
4. Check **Do not allow update deferral policies** and related metered-download policies.
5. If you don't control the policy, contact your IT administrator — overriding it locally will just get reapplied.
6. For personal laptops showing the message incorrectly, see Microsoft's guidance on [Windows Update settings](https://support.microsoft.com/en-us/windows).

### Fix 6: Reset the network profile if the flag is stuck

Sometimes the toggle flips off but Windows keeps treating the network as metered because the stored profile is corrupt. Forgetting the network and reconnecting rebuilds the profile cleanly.

1. Go to **Settings > Network & internet > Wi-Fi > Manage known networks**.
2. Click your network and choose **Forget**.
3. Reconnect by selecting the network and entering the password again.
4. Recheck the **Metered connection** toggle — it should now default to off.
5. If the problem persists on Ethernet, check **Settings > Network & internet > Ethernet** — wired connections can be flagged metered too, especially on USB Ethernet adapters.

### Fix 7: Download the update manually as a fallback

If you need the update now and don't want to change any metering behavior — say you're on a hotel network with a strict cap — grab the specific update package directly. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) lets you download individual cumulative updates and install them offline.

1. In **Settings > Windows Update > Update history**, note the KB number of the failing update.
2. Visit the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB number.
3. Download the package matching your architecture (x64 for most laptops).
4. Run the `.msu` file to install it manually — this bypasses the metered restriction entirely.
5. For bigger feature updates, the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) offers the Installation Assistant as an alternative.

## Closing

Metered connection blocking is Windows 11 protecting your data bill — annoying when the "cap" is imaginary, but easy to tame once you know the two switches involved. Clear the flag on networks you trust, or allow updates over metered connections when you want patches without giving every app a free pass. If updates still won't download after metering is sorted, the blockage is deeper in the update pipeline — [driver updates failing repeatedly](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) is the next guide to check, since stuck driver packages often masquerade as a download problem.
