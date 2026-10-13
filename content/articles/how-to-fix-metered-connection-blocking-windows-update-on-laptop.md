---
title: "Metered Connection Blocking Windows Update on Your Laptop? Fix It"
slug: how-to-fix-metered-connection-blocking-windows-update-on-laptop
date: 2026-10-04
categories: ["windows-update"]
tags: ["metered connection", "windows update blocked", "wifi settings", "data limit", "bandwidth"]
description: "Windows Update won't download because your connection is metered? Learn how metered connections block updates and how to get updates flowing again."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-on-laptop.webp"
faqs:
  - q: "What exactly does a metered connection block?"
    a: "A metered connection tells Windows to conserve data: most automatic update downloads pause, Store app updates stop, and some background sync is reduced. Critical security updates may still download. Feature updates and driver updates generally wait until you're on an unmetered connection or you manually approve the download."
  - q: "Should I turn off the metered setting permanently?"
    a: "Only if your data is actually unlimited. The metered flag exists to protect capped mobile hotspots and limited data plans from multi-gigabyte surprise downloads. If you're on home Wi-Fi with no cap, turning it off is correct. If you're tethering from a phone, leave it on and download updates manually when needed."
  - q: "Why is my home Wi-Fi marked as metered? I didn't set that."
    a: "Windows sometimes auto-enables the metered flag on connections it identifies as mobile hotspots, and some manufacturer utilities or mobile-data management apps set it too. It can also carry over from a previous network profile. Check the setting directly — it takes ten seconds to verify and fix under Network & internet settings."
  - q: "Can I install one specific update while staying metered?"
    a: "Yes. On the Windows Update page, a metered connection usually shows a 'Download' button for pending updates instead of downloading automatically. Clicking it approves that specific download. You can also toggle 'Download updates over metered connections' on temporarily, install what you need, and turn it back off."
---

You are on a perfectly good Wi-Fi connection, but Windows Update refuses to download anything — or it downloads security patches while ignoring everything else. The culprit is often invisible: your connection is flagged as "metered," and Windows is dutifully conserving data you did not ask it to conserve.

The metered flag is a sensible feature aimed at mobile hotspots and capped data plans. The problem is when it gets set on connections where it does not belong — home Wi-Fi, office networks, or a hotspot you only use occasionally. Then it silently blocks the updates you actually want.

This guide explains what the metered flag blocks, how to check it, and how to get updates flowing — with or without turning it off. Work through these in order — diagnose first, then act.

## Why this happens

- **Metered flag set on the Wi-Fi profile.** Windows pauses most update downloads on metered connections by design.
- **Auto-metered hotspot detection.** Windows automatically flags connections that look like mobile hotspots.
- **Flag carried over from another network.** The metered setting is per-network-profile and can persist unexpectedly.
- **Data limit configured in Windows.** A set data limit makes Windows treat the connection as constrained.
- **Group policy enforcing metered behavior.** Managed or previously-managed machines may have policies restricting updates on metered connections.
- **Third-party data management apps.** Mobile-data utilities from carriers or manufacturers can set the flag.
- **Delivery Optimization paused.** Metered connections also restrict peer-to-peer update sharing, slowing what does download.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether your connection is actually metered

Go to Settings, Network & internet, Wi-Fi, click your connected network's name (or the info icon), and look for "Set as metered connection." For Ethernet, it is under Network & internet, Ethernet, click the connection.

If the toggle is on and you are on unlimited home or office Wi-Fi, that is your blocker — proceed to Fix 2. If it is off and updates still will not download, your problem is elsewhere (cache corruption or service issues), and the [stuck downloading guide for 24H2](/articles/how-to-fix-windows-update-stuck-downloading-in-windows-11-24h2/) is the better next step. Do not skip this check; it takes ten seconds and explains a huge share of "updates won't download" cases.

### Fix 2: Turn off the metered flag on unlimited connections

On that same network settings page, switch "Set as metered connection" off. Then go to Settings, Windows Update, and click "Check for updates" — queued updates should begin downloading within minutes.

Remember the setting is per-network: turning it off for your home Wi-Fi does not affect your phone hotspot profile. If you connect to several networks, check each one you regularly use for updates. This is the correct permanent fix whenever the flagged connection genuinely has unlimited data.

### Fix 3: Download a specific update while staying metered

If you are on a capped connection and want to stay metered, you can still get updates selectively. On the Windows Update page, pending updates show a "Download" button instead of auto-downloading — clicking it approves just that download.

For more control, go to Settings, Windows Update, Advanced options, and toggle "Download updates over metered connections" on temporarily. Install what you need, then turn it back off. This gives you the security patches without opening the floodgates to multi-gigabyte feature updates on a 10 GB data plan.

### Fix 4: Remove or raise the data limit

Windows lets you set a data limit per connection, and hitting it triggers metered-like behavior. Go to Settings, Network & internet, Advanced network settings, Data usage, select your connection, and check whether a limit is set.

If a limit exists that does not match your actual plan, edit or remove it. An outdated 5 GB limit on a now-unlimited connection will throttle updates indefinitely. This setting is easy to forget — it is often set once during initial setup and never revisited. Microsoft documents data usage controls in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 5: Check Delivery Optimization settings

Metered connections restrict Delivery Optimization's peer sharing, but misconfigured optimization settings can compound the problem. Go to Settings, Windows Update, Advanced options, Delivery Optimization, and confirm it is allowed to download from Microsoft's servers directly.

Under Advanced settings, check the bandwidth limits — an absolute cap set very low (or a background percentage near zero) strangles even approved downloads. On a metered connection you want to approve, temporarily raise these limits, then restore them. These caps are per-device and survive network changes, so a limit set months ago could still be biting you.

### Fix 6: Look for group policy or MDM restrictions

On machines that were ever work-managed (or had "management" tools installed), policies may force metered-connection update blocking. Press Win+R, type `gpedit.msc` (Pro editions), and check Computer Configuration, Administrative Templates, Windows Components, Windows Update, "Manage updates offered from Windows Update" for metered-related policies.

For Home edition, check the registry at `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for unexpected values — but do not delete keys unless you are certain they do not belong to active management. If the laptop is currently work-managed, talk to your IT admin instead of fighting policy. If driver updates are part of what is stuck, the [driver update failure loop guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-on-laptop/) covers that angle.

### Fix 7: Reset the network profile as a last resort

If the metered flag keeps re-enabling itself, the network profile is corrupt. Go to Settings, Network & internet, Wi-Fi, "Manage known networks," forget the network, then reconnect fresh — the new profile starts with default (unmetered) settings.

For stubborn cases, reset the whole network stack: Settings, Network & internet, Advanced network settings, Network reset. This reinstalls network adapters and wipes all profiles, so you will re-enter Wi-Fi passwords afterward. It is drastic but definitive for profile-level corruption that keeps resurrecting the metered flag.

## Closing

A metered connection blocking Windows Update is Windows doing exactly what it was told — the fix is making sure it was told correctly. Verify the flag, turn it off where data is unlimited, approve individual downloads where it is not, and check data limits and policies when the flag will not stay off. Ten minutes of settings review beats hours of wondering why updates never arrive.
