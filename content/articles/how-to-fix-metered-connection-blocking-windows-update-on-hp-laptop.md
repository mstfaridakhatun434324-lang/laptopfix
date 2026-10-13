---
title: "Metered Connection Blocking Windows Update on an HP Laptop (Fix)"
slug: how-to-fix-metered-connection-blocking-windows-update-on-hp-laptop
date: 2026-09-21
categories: ["windows-update"]
tags:
  - metered connection
  - windows update
  - hp laptop
  - wi-fi
  - troubleshooting
description: "Windows Update refuses to download on your HP laptop because of a metered connection? Here is how to fix the setting and get updates flowing again."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-on-hp-laptop.webp"
faqs:
  - q: "Why does Windows think my home Wi-Fi is a metered connection?"
    a: >
      Windows sometimes carries the metered flag over from a mobile hotspot profile, especially if the hotspot and home network share similar settings, or the flag was set once and never cleared. Forgetting and rejoining the network creates a clean profile. The flag can also be pushed by management policy on work laptops, in which case Settings will show it greyed out.
  - q: "Will turning off metered connection use a lot of data?"
    a: >
      On an unlimited home connection, no — turning it off simply lets Windows behave normally. On a genuinely limited connection, keep it on and use the Download updates over metered connections toggle selectively for critical updates. You can also set active hours and pause updates for up to five weeks to control timing.
  - q: "Does metered connection block HP driver updates too?"
    a: >
      Yes, mostly. Both Windows Update driver offerings and HP Support Assistant respect the metered flag and will defer downloads. If you need an HP driver urgently on a metered network, download it directly from HP Support on another device or allow the download explicitly — HP's site does not care about the Windows flag.
  - q: "Can my employer prevent me from turning off metered connection?"
    a: >
      Yes. On domain-joined or Intune-managed HP laptops, IT policy can enforce metered behavior and grey out the toggle. In that case do not try registry workarounds — they may violate company policy and get reverted anyway. Ask your IT helpdesk to push the updates, or connect to the corporate network where updates are managed centrally.
---

You open Windows Update on your HP laptop and instead of downloading, it sits there saying updates are paused because you are on a metered connection — even though you are on your own home Wi-Fi with unlimited data. Or the metered flag is genuinely on, and you need this month's security update anyway.

Metered connections are Windows' way of protecting limited data plans: on a metered network, most updates simply do not download. The feature is sensible on a 4G hotspot and infuriating when Windows mislabels your home network as metered, which happens more often than HP owners expect.

This HP-focused guide shows how to check and clear the metered flag on Wi-Fi and Ethernet, how to allow updates over metered connections when you truly need them, and how HP's own tools fit into the picture.

## Why this happens

- **Wi-Fi marked as metered by mistake:** Windows sometimes inherits the metered flag from a hotspot profile or a previous network with the same name, and it sticks to your home Wi-Fi incorrectly.
- **Metered flag set on purpose for a hotspot:** if you tether through your phone, Windows correctly marks it metered — and then keeps the flag when you reconnect later.
- **Ethernet marked as metered:** less common, but Windows allows metered Ethernet too, and some HP docking setups end up flagged after driver reinstalls.
- **Data limit configured on the connection:** Windows 11 lets you set a data limit, which implies metered behavior and pauses updates when the limit is reached.
- **HP Support Assistant updating over the flagged network:** HP's own updater respects the metered flag, so HP driver updates stall alongside Windows updates.
- **Group policy enforcing metered behavior:** on work-managed HP laptops, IT policy may force metered handling that you cannot toggle from Settings.
- **Corrupted network profile:** a damaged Wi-Fi profile can report metered status incorrectly and resist normal toggling until the profile is forgotten and recreated.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off the metered flag on your Wi-Fi network

Nine times out of ten, this is the entire fix. The toggle lives one level deeper than most people look, under the specific network's properties.

1. Open Settings > Network & internet > Wi-Fi and click your connected network's name.
2. Find Metered connection and toggle it Off.
3. Go to Settings > Windows Update and click Check for updates — downloads should start.
4. If the toggle is greyed out, your laptop is managed by an organization; skip to Fix 6.

### Fix 2: Check Ethernet and other adapters too

Laptops on docks or USB-C Ethernet adapters can be metered on the wired side while Wi-Fi looks fine. Windows evaluates the active connection, so check whichever one is actually in use.

1. Go to Settings > Network & internet > Ethernet and click your adapter.
2. Set Metered connection to Off here as well.
3. If you use a USB-C dock's Ethernet, check it while docked — the flag is per-adapter.
4. Recheck Windows Update after clearing every active adapter.

### Fix 3: Allow updates over metered connections when you need them

Sometimes the network genuinely is metered — a hotel Wi-Fi or phone tether — but you still need a critical security update. Windows lets you permit updates explicitly without unflagging the network.

1. Go to Settings > Windows Update > Advanced options.
2. Enable Download updates over metered connections.
3. Click Check for updates to pull the pending updates now.
4. Turn the option back off afterward if data is precious — and consider updating HP drivers through [HP Support](https://support.hp.com/us-en) over an unmetered network later.

### Fix 4: Remove any data limit on the connection

A configured data limit triggers the same update-pausing behavior as a metered flag, and it survives toggling the metered switch. Check both.

1. Go to Settings > Network & internet > Advanced network settings > Data usage.
2. Select your network and check whether a limit is set.
3. Remove the limit or raise it well above your actual usage.
4. Return to Windows Update and retry the download.

### Fix 5: Forget and rejoin the Wi-Fi network

When the metered flag is stuck due to a corrupted network profile, no toggle will move it. Forgetting the network deletes the damaged profile so Windows builds a clean one.

1. Go to Settings > Network & internet > Wi-Fi > Manage known networks.
2. Select your network and click Forget.
3. Reconnect by choosing the network and entering the password again.
4. Verify the metered toggle is Off on the fresh profile, then check for updates.

### Fix 6: Use HP Support Assistant for HP drivers separately

HP driver updates can be fetched independently of Windows Update, which is useful when policy or data caps keep the metered flag on. HP's tool manages its own downloads.

1. Open HP Support Assistant (install it from the Microsoft Store if missing).
2. Run a check for updates and install HP-recommended drivers and BIOS updates.
3. For anything the assistant does not cover, browse drivers by model on [HP Support](https://support.hp.com/us-en).
4. This keeps your HP-specific drivers current even while Windows Update stays paused.

### Fix 7: Install the urgent update manually from the catalog

When you need one specific update now and the metered machinery will not cooperate, bypass it entirely with a manual install.

1. Note the KB number from Settings > Windows Update > Update history.
2. Download the matching package for your architecture from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Double-click the .msu to install, then reboot.
4. Confirm it appears in update history afterward.

## Closing

A metered connection blocking Windows Update on an HP laptop is a settings problem, not an update problem: clear the flag on the active adapter, remove stray data limits, and updates flow again. Keep the flag on for genuine hotspots to protect your data, and use HP Support Assistant for HP drivers when Windows Update must stay paused. If updates still misbehave after the flag is cleared, our [step-by-step metered connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-step-by-step/) covers the registry and policy routes, and the [troubleshooter guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-step-by-step/) helps when the update engine itself is stuck.
