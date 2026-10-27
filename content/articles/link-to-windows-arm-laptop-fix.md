---
title: "How to Fix Link to Windows App Issues on Your ARM Laptop"
slug: link-to-windows-arm-laptop-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["link to windows", "phone link", "arm laptop", "android", "pairing", "troubleshooting"]
description: "Fix Link to Windows app issues on your ARM laptop with steps for pairing failure fixes, companion app problems, permissions, and sync that stops working."
thumbnail: "/images/thumbs/link-to-windows-arm-laptop-fix.webp"
faqs:
  - q: "What is the difference between Phone Link and Link to Windows?"
    a: >
      They are two halves of the same system. Link to Windows is the companion app on your Android phone, and Phone Link is the app on your Windows laptop. They pair together to sync notifications, messages, photos, and calls.
  - q: "Why does Link to Windows fail to pair on ARM laptops?"
    a: >
      Pairing failures on ARM laptops usually come from the same causes as on any Windows PC — network mismatches, revoked permissions, outdated apps, or stale pairing state — plus occasional ARM-specific app issues in the Windows Phone Link app itself.
  - q: "Does Link to Windows work with iPhones?"
    a: >
      iPhones use a different pairing flow through Bluetooth and the Link to Windows iOS integration, with fewer features than Android. The pairing and permission steps still apply, but photo sync and app mirroring remain Android-only.
  - q: "Why does the companion app keep disconnecting?"
    a: >
      Android battery optimization killing the app in the background is the leading cause. Exempting Link to Windows from battery optimization usually stops the repeated disconnections.
---

Link to Windows will not pair with your ARM laptop, or it paired once and now shows disconnected, or it connects but syncs nothing. The system has two apps — the companion on your phone and Phone Link on the laptop — plus Bluetooth, Wi-Fi, permissions, and a Microsoft account. A failure anywhere in that chain looks the same on the laptop: an empty Phone Link window and no sync.

ARM laptops add one wrinkle: the Windows Phone Link app can have its own emulation-related quirks, but the phone side causes most failures regardless of processor. This guide works the phone side first, the laptop side second, and the pairing itself last.

## Why this happens

- **Battery optimization killing the companion app:** Android aggressively kills background apps, and Link to Windows is a frequent victim. Once killed, sync stops until you reopen the phone app.
- **Permissions revoked after an update:** Notification access, contacts, photos, and SMS permissions can be reset by phone updates or privacy cleanups, breaking specific features silently.
- **Different Wi-Fi networks or accounts:** Pairing and discovery require both devices on the same network and the same Microsoft account. A mismatch blocks pairing entirely.
- **Outdated Phone Link or companion app:** Version differences between the two apps cause pairing failures that look like connection problems.
- **Stale pairing state on one side:** A half-removed pairing leaves both apps believing they are linked while nothing syncs.
- **Bluetooth or network interruption:** Calls need Bluetooth and the rest needs Wi-Fi. A failure in either transport stalls the features that depend on it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix the phone companion app first

The phone side causes most Link to Windows failures, so it comes before any laptop troubleshooting.

1. Open the Link to Windows app on your phone and confirm it shows your laptop as linked.
2. On Android, verify notification access, contacts, photos, SMS, and calls permissions are all granted — re-grant any that are missing.
3. Turn off battery optimization for Link to Windows so Android stops killing it in the background.
4. Leave the app open in the foreground for a minute to force a sync attempt.
5. If the app shows no linked laptop, continue to the re-pairing fix. If it shows linked but nothing syncs, the laptop side or the network is the problem — continue below. Related phone-side issues affect [Phone Link sync](/articles/phone-link-ai-laptop-not-syncing-fix/) on the same machines.

### Fix 2: Verify network, Bluetooth, and account alignment

Discovery and pairing depend on alignment between the two devices. Check all three before deeper fixes.

1. Confirm both devices are on the same Wi-Fi network.
2. Confirm Bluetooth is on for both devices and the phone is within range of the laptop.
3. Confirm both apps are signed into the same Microsoft account.
4. Toggle Wi-Fi and Bluetooth off and on on both devices, then wait a minute for rediscovery.
5. Restart both devices if discovery still fails — a fresh cycle resolves many stale states.

### Fix 3: Update both apps and Windows

Version mismatches are a silent pairing killer. Update everything before assuming a deeper fault.

1. On the laptop, update Phone Link from the Microsoft Store.
2. On the phone, update Link to Windows from the Play Store or App Store.
3. On the laptop, install pending Windows updates from **Settings > Windows Update**.
4. Restart both devices after updating.
5. Open both apps and check whether pairing or sync resumes.

### Fix 4: Repair Phone Link on the ARM laptop

When the phone side is healthy, the Windows app may hold the corrupted state — including ARM-specific app quirks.

1. Open **Settings > Apps > Installed apps**, find Phone Link, and open **Advanced options**.
2. Click **Repair**, then test sync.
3. If repair does not help, click **Reset** to clear pairing state, then re-pair with the QR code flow.
4. During re-pairing, grant every permission the phone requests — skipping one creates partial sync later.
5. If Phone Link itself crashes or behaves oddly on the ARM laptop, uninstall and reinstall it from the Store, since a fresh install clears emulation-related corruption.

### Fix 5: Remove the pairing completely and start fresh

A stale pairing can survive individual repairs. Removing it from both sides is the clean reset.

1. In Phone Link on the laptop, remove the phone from the device list.
2. On the phone, remove the laptop from the linked devices in the companion app.
3. Clear the companion app's cache on Android, or reinstall it if no cache option exists.
4. Restart both devices, then pair fresh by scanning the QR code in Phone Link.
5. Test each feature after pairing — notifications, messages, photos, calls — so you know exactly what works.

### Fix 6: Check network blocks and managed-device policies

If a clean pairing still fails, the network or a device policy is blocking the connection.

1. Try a different Wi-Fi network or a phone hotspot to rule out router-level blocking.
2. Temporarily disable third-party firewalls on the laptop and test again.
3. Confirm the Microsoft account is in good standing by signing into it in a browser.
4. Check whether a work or school policy restricts Phone Link on a managed laptop — managed devices sometimes block it.
5. If pairing still fails on a clean network with a clean pairing, contact Microsoft support with both app versions and any error shown. For general Windows help, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) and [Zoom on ARM](/articles/zoom-app-arm-laptop-issues-fix/) for other ARM app issues.

## Closing

Link to Windows failures on ARM laptops are usually phone-side problems — battery optimization, revoked permissions, or a stale pairing — not ARM problems. Fix the companion app first, verify the shared network and account second, and re-pair cleanly before blaming the laptop. That sequence restores pairing and sync for nearly every setup, on ARM and x64 alike. If this fix did not fully resolve the issue, related troubleshooting for [Dell Inspiron 14 7445 Ai Issues](/articles/dell-inspiron-14-7445-ai-issues-fix/) and [Cocreator Prompt No Image](/articles/cocreator-prompt-no-image/) covers neighboring causes that can produce the same symptom on AI laptops.
