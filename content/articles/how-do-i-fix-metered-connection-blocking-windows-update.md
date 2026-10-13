---
title: "Metered Connection Blocking Windows Update? Unblock It Safely"
slug: how-do-i-fix-metered-connection-blocking-windows-update
date: 2026-09-10
categories: ["windows-update"]
tags: ["metered connection", "windows update blocked", "windows 11", "windows 10", "update settings"]
description: "Windows Update won't download because your connection is metered? Learn how metered connections block updates and how to allow critical updates without burning your data."
thumbnail: "/images/thumbs/how-do-i-fix-metered-connection-blocking-windows-update.webp"
faqs:
  - q: "What is a metered connection in Windows?"
    a: "It is a flag you can set on any network connection telling Windows that data is limited or expensive — like a mobile hotspot or capped broadband. Windows then restricts background data use, including pausing most Windows Update downloads, to protect your data allowance."
  - q: "Will turning off metered connection use a lot of data?"
    a: "It can. Cumulative updates run several hundred megabytes and feature updates several gigabytes — meaningful on a capped plan. On a truly limited connection, turn metered off temporarily, install the critical security updates, then turn it back on. That targeted approach protects both your security and your data allowance."
  - q: "Do security updates download on metered connections?"
    a: "By default, Windows still downloads critical security updates on metered connections but holds back most other updates — drivers, optionals, and feature updates wait. There is also a dedicated setting under Windows Update's Advanced options to allow all updates over metered connections, if you would rather trade data for completeness."
  - q: "Why is my home Wi-Fi marked as metered?"
    a: "Usually because someone enabled it and forgot, or Windows auto-flagged a mobile hotspot. Some users enable it deliberately to pause updates, then months later wonder why nothing updates. Open Settings, Network & internet, select the network, and toggle metered off if the connection is actually unlimited — the mystery usually ends there."
---

The metered connection flag is one of Windows' most misunderstood features. It exists to protect you — on a mobile hotspot or capped plan, you do not want Windows silently downloading gigabytes. But when the flag is set on the wrong connection, or set and forgotten, it looks exactly like Windows Update is broken: downloads stall, updates sit at "pending download" forever, and optional updates never arrive. Before diagnosing a broken update pipeline, check whether Windows is simply obeying your (possibly accidental) instructions.

This guide covers both sides: unblocking updates when the metered flag is wrong, and managing updates sensibly when the metered flag is right. The deeper troubleshooting companion is [troubleshooting metered connection issues](/articles/troubleshoot-metered-connection-blocking-windows-update/).

The metered flag's history explains why it causes so much confusion. It was designed for the mobile-broadband era, when Windows laptops commonly tethered through phones with tiny data caps. Today it survives as a general "go easy on data" signal that affects far more than updates \u2014 Store apps, OneDrive sync, and background tasks all throttle back. When you see update weirdness, check the flag, but remember it is a system-wide data diet, not an update-specific switch \u2014 and the [optional updates guide](/articles/how-do-i-fix-optional-updates-not-installing-windows-11/) explains why optionals are always the first casualties of that diet.

## Why this happens

- **Metered flag set accidentally:** The most common case — the toggle got enabled at some point and forgotten, silently throttling updates ever since.
- **Hotspot auto-detection:** Windows sometimes marks phone hotspots as metered automatically, which is correct behavior that surprises people.
- **Deliberate blocking, forgotten:** Users enable metered connections specifically to pause updates, then months later wonder why nothing updates.
- **Per-network setting:** The flag is per-network, so your home Wi-Fi can be unmetered while your hotspot is metered — confusion arises when switching between them.
- **Optional updates deprioritized:** Even with the right settings, optional and driver updates are the first things held back on metered links.
- **Delivery Optimization throttling:** Metered connections also restrict peer-to-peer update sharing, slowing downloads that do proceed.
- **Group Policy overrides:** On managed machines, policy can force metered behavior regardless of the toggle.
- **Data cap anxiety:** The legitimate reason the flag exists — real data limits that make unrestricted updates genuinely expensive.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check and correct the metered flag

1. Go to Settings, Network & internet, then Wi-Fi (or Ethernet) and click your connected network.
2. Find the "Metered connection" toggle. If your connection is actually unlimited, turn it off.
3. Return to Windows Update and check for updates — previously blocked downloads should start.
4. If the connection genuinely is limited, leave the flag on and use Fix 2 instead.

### Fix 2: Allow updates over metered connections selectively

1. In Settings, Windows Update, Advanced options, find "Download updates over metered connections" and turn it on.
2. This permits update downloads while keeping other metered data-saving behaviors intact.
3. For finer control, leave it off but manually click "Download" on critical updates — Windows lets you override per-update on metered connections.

### Fix 3: Use the manual download override

1. On a metered connection, Windows Update shows a "Download" button next to pending updates instead of auto-downloading.
2. Click it for the updates you want — typically the cumulative security update first.
3. Let it complete on AC power. This gives you update control without disabling the metered protection entirely.

### Fix 4: Clear the stalled queue

Blocked downloads sometimes leave the queue in a confused state even after the flag is fixed.

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv` and `net stop bits`.
3. Delete the contents of C:\Windows\SoftwareDistribution.
4. Restart the services, reboot, and check for updates.

### Fix 5: Check for policy overrides

1. On Pro editions, open gpedit.msc and look under Computer Configuration, Administrative Templates, Windows Components, Windows Update for metered-related policies.
2. On managed devices, these may be set by IT — do not fight them locally; the data policy exists for a reason.
3. Verify the registry value at `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\DefaultMediaCost` reflects your actual network costs if the UI toggle seems ignored.

### Fix 6: Manage data wisely on truly limited connections

1. Use the manual install route: download the monthly cumulative update once from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) on an unlimited connection (work, library, café), then install offline at home.
2. Disable Delivery Optimization uploads (Settings, Windows Update, Advanced options, Delivery Optimization) so your laptop does not share updates with others on your capped link.
3. Schedule a monthly "update session" on unlimited Wi-Fi rather than fighting the metered flag daily.

### Fix 7: Verify updates flow and document your setup

1. After changing the flag, run a full update check and confirm downloads proceed.
2. Note which networks are metered and why — a sticky note in the laptop bag beats rediscovering this in six months.
3. For official documentation of metered behavior, see the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Audit which apps respect the metered flag

The flag affects more than Windows Update \u2014 check the blast radius.

1. In Settings, Network & internet, review which apps have background data restrictions tied to the metered state.
2. Check OneDrive sync settings and Microsoft Store auto-updates \u2014 both pause on metered connections by design.
3. If an app you need is blocked, most offer their own "allow on metered" override independent of Windows Update.
4. Understanding the full picture prevents the next confusion, when something other than updates mysteriously stops on your hotspot.

## Closing

Metered connection blocking is Windows doing what you told it to \u2014 the fix is usually a toggle, not a repair, and the audit in Fix 8 shows you everything else the flag touches. The real skill is matching the setting to reality: unlimited connections unmetered, limited ones metered with manual overrides for security updates, and a monthly offline-install routine for capped links. Get that mapping right and updates flow where they should while your data cap stays safe where it matters.
