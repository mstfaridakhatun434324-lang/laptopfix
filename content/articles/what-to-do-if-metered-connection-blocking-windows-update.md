---
title: "Metered Connection Blocking Windows Update? What to Do"
slug: what-to-do-if-metered-connection-blocking-windows-update
date: 2026-09-26
categories: ["windows-update"]
tags: ["windows update", "metered connection", "wifi", "windows 11"]
description: "Windows Update stuck because your connection is metered? Learn what the metered flag does and how to let updates through without wasting data."
thumbnail: "/images/thumbs/what-to-do-if-metered-connection-blocking-windows-update.webp"
faqs:
  - q: "What does a metered connection actually block?"
    a: "A metered flag tells Windows the network has a data cap or per-megabyte cost, so it pauses most automatic downloads: Windows feature and cumulative updates, driver updates, Store app updates, and many background syncs. Priority security updates may still trickle through. The block is intentional data-saving behavior, not a malfunction — which is why it produces no error message."
  - q: "Will turning off metered connection use a lot of data?"
    a: "It can, because Windows will immediately start downloading everything it deferred — potentially gigabytes of queued updates. If you are on a capped plan, a better approach is to enable the Download updates over metered connections option selectively, or download only the latest cumulative update manually from the Microsoft Update Catalog over an unmetered connection."
  - q: "Why is my home Wi-Fi marked as metered?"
    a: "Usually because it was enabled once and forgotten — perhaps when the network was a phone hotspot with the same name, or during a fresh install that defaulted to metered. The flag is stored per network profile and never expires on its own. Checking the toggle in the network's properties takes seconds and is worth doing whenever updates mysteriously stall."
  - q: "Can I keep metering on but still get security updates?"
    a: "Yes. Windows 11 lets you keep the metered flag while separately allowing update downloads over metered connections, so you stay patched without fully opening background data. Alternatively, manually install just the latest cumulative update from the Microsoft Update Catalog — one download covers all security fixes to date, which is the most data-efficient option of all."
---

Everything looks fine — Wi-Fi connected, signal strong — yet Windows Update refuses to download anything, or only trickles out tiny updates while the big ones sit waiting. The culprit is often a single toggle you may not remember enabling: the metered connection flag, which tells Windows to treat your network like expensive mobile data and hold back anything non-essential.

This is Windows working as designed, not a bug — but the design assumes you know the flag is set. Laptop users hit this constantly: hotel Wi-Fi you flagged as metered months ago, a phone hotspot that inherited the setting, or a fresh install that defaulted to metered. Here is what the flag actually blocks, and how to get your updates moving again without burning through a data cap.

A quick way to confirm the metered flag is your problem: open Windows Update and look at the messaging. On a metered connection, Windows often shows updates as available but paused, or downloads only tiny definition updates while everything substantial waits. If that matches what you see, the fixes below will have you downloading within minutes.

## Why this happens

- **Metered flag pauses most downloads:** On a metered connection, Windows Update downloads only priority updates. Feature updates, driver updates, and most cumulative payloads wait indefinitely until the flag clears.
- **The setting persists per network:** Metering is stored per Wi-Fi network profile. A network you flagged as metered once stays metered forever, long after you have forgotten doing it.
- **Hotspots inherit metered status:** Windows often auto-marks mobile hotspots as metered. If you tether regularly, every one of those sessions blocks updates by default.
- **Some installs default to metered:** Certain fresh installs and mobile-broadband connections enable metering automatically, so a new laptop may block its own updates from day one.
- **Store and app updates also pause:** The metered flag affects Microsoft Store updates too, so the symptom can look broader than Windows Update alone — nothing on the system wants to download.
- **Group policy can enforce metering:** On managed or formerly managed laptops, a policy may force the metered behavior regardless of the toggle's visible state.
- **Confusion with the pause feature:** Users sometimes mistake a metered block for a paused update schedule. Both produce a quiet, non-downloading Windows Update page, but the fixes are completely different.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find and disable the metered flag

This is the fix in the majority of cases. The toggle lives in the network profile settings, and switching it off lets queued updates start downloading within moments — no restart required. The 24H2-specific version of this issue is detailed in [metered connection blocking Windows Update on 24H2](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/).

1. Open Settings, Network and internet, Wi-Fi.
2. Click the connected network's name to open its properties.
3. Set Metered connection to Off.
4. Return to Windows Update and click Check for updates; queued downloads should begin.

### Fix 2: Allow updates over metered connections selectively

If you genuinely need metering — say, a capped hotspot — you can keep the flag on while permitting update downloads. Windows 11 exposes this as a separate option, giving you control without fully opening the floodgates. Driver downloads suffer most under metering; [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) addresses those specifically.

1. Open Settings, Windows Update, Advanced options.
2. Enable Download updates over metered connections.
3. Leave the network itself flagged as metered so other apps stay throttled.
4. Monitor data usage in Settings, Network and internet, Data usage to stay within your cap.

### Fix 3: Download the critical update manually

When data is truly precious, skip the bulk download queue and install only what matters. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) lets you fetch individual updates — such as the latest cumulative package — and install them directly without enabling background downloads.

1. Identify the most important pending update in Windows Update.
2. Search for its KB number on the Microsoft Update Catalog.
3. Download it over an unmetered connection if possible, then install offline.
4. This keeps the laptop patched while the metered queue stays paused.

### Fix 4: Check for policy-enforced metering

If the toggle is off but updates still behave as metered, a policy may be overriding it. This happens on laptops with a managed past, where the old configuration still whispers instructions to Windows Update.

1. Check Settings, Windows Update for any message about settings managed by your organization.
2. In Registry Editor, inspect HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate for stale entries.
3. Remove obsolete policy keys left by former management software.
4. Restart and retest the update behavior.

### Fix 5: Reset the network profile

A corrupted network profile can misreport its metered state. Forgetting the network and reconnecting rebuilds the profile from scratch with default (unmetered) settings.

1. Open Settings, Network and internet, Wi-Fi, Manage known networks.
2. Select the network and click Forget.
3. Reconnect by selecting the network and entering the password.
4. Verify the metered toggle is off on the fresh profile, then check for updates.

### Fix 6: Use Delivery Optimization on a trusted LAN

If several PCs share one unmetered connection, Delivery Optimization lets them share downloaded update payloads locally — one download serves the whole household, which is ideal when only one machine has unmetered access.

1. On the unmetered PC, open Settings, Windows Update, Advanced options, Delivery Optimization.
2. Enable Allow downloads from other PCs and choose devices on the local network.
3. Enable the same setting on the metered laptop.
4. The laptop can then pull update payloads from the local PC instead of the internet.

## Closing

A metered connection blocking Windows Update is Windows protecting your data cap — usually long after you stopped needing the protection. Flip the toggle off, allow updates over metered connections selectively, or hand-pick critical updates from the catalog when data is scarce. Either way, the mystery stall resolves the moment you address the flag that caused it.
