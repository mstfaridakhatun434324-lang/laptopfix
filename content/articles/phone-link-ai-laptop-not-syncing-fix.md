---
title: "How to Fix Phone Link Not Syncing on Your AI Laptop"
slug: phone-link-ai-laptop-not-syncing-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["phone link", "sync", "android", "iphone", "link to windows", "troubleshooting"]
description: "Fix Phone Link not syncing on your AI laptop with steps for pairing, app permissions, Bluetooth, network, and account issues that stop messages and photos."
thumbnail: "/images/thumbs/phone-link-ai-laptop-not-syncing-fix.webp"
faqs:
  - q: "What does Phone Link sync?"
    a: >
      Phone Link syncs notifications, messages, photos, calls, and app mirroring between your phone and your Windows laptop, depending on whether you use Android or iPhone and which features your phone supports.
  - q: "Why did Phone Link stop syncing suddenly?"
    a: >
      The usual causes are a revoked permission on the phone, a Bluetooth or Wi-Fi interruption, an app update that reset the connection, or the phone's battery optimization killing the companion app in the background.
  - q: "Does Phone Link need Bluetooth and Wi-Fi?"
    a: >
      Yes. Phone Link uses Bluetooth for calls and proximity, and Wi-Fi for photos, messages, and app streaming. Both connections must be healthy, and both devices should be on the same Wi-Fi network for the best experience.
  - q: "Can I use Phone Link with an iPhone?"
    a: >
      Yes, with a reduced feature set compared to Android — messages, notifications, and calls work, but photo sync and app mirroring are Android-only features. The troubleshooting steps for pairing and permissions still apply.
---

Phone Link was syncing your messages and photos yesterday, and today nothing arrives — or it never synced at all after pairing. Phone Link is a two-device system: the Windows app, the phone companion app, Bluetooth, Wi-Fi, permissions on both sides, and a Microsoft account sign-in all have to agree. A failure on either device looks identical on the laptop: an empty or stale Phone Link window.

The fastest way to fix it is to find which side broke. This guide isolates the phone side, the laptop side, and the connection between them, in that order.

## Why this happens

- **Companion app killed by battery optimization:** Android battery optimization frequently kills the Link to Windows app in the background, stopping sync until you open the phone app again.
- **Permissions revoked on the phone:** Notification access, contacts, photos, or SMS permissions can be revoked by an update or a privacy cleanup, silently breaking specific sync features.
- **Bluetooth or Wi-Fi interruption:** Calls need Bluetooth, photos and messages need Wi-Fi. A dropped connection on either side stalls the features that depend on it.
- **Different networks or accounts:** Devices on different Wi-Fi networks, or signed into different Microsoft accounts, fail to discover and sync with each other.
- **Outdated Phone Link or companion app:** Version mismatches between the Windows app and the phone app cause pairing and sync failures that look like connection problems.
- **Corrupted pairing state:** A half-completed pairing or a stale device entry can leave both apps thinking they are connected while nothing syncs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the phone companion app and its permissions

Most Phone Link sync failures live on the phone, not the laptop. Start there.

1. Open the Link to Windows app on your Android phone, or the Link to Windows settings on iPhone, and confirm it shows as connected.
2. On Android, check that notification access, contacts, photos, SMS, and calls permissions are all granted — re-grant any that are missing.
3. Turn off battery optimization for the Link to Windows app so Android does not kill it in the background.
4. Open the companion app and leave it in the foreground for a minute to force a sync attempt.
5. If the phone app shows disconnected, continue to the re-pairing fix below. Related phone-connection problems affect [Link to Windows on ARM](/articles/link-to-windows-arm-laptop-fix/) laptops.

### Fix 2: Verify both devices share a network and account

Discovery failures are often just mismatched networks or accounts, and they are quick to check.

1. Confirm both devices are on the same Wi-Fi network and that Bluetooth is on for both.
2. Confirm both are signed into the same Microsoft account in Phone Link and the companion app.
3. Move the phone closer to the laptop to rule out Bluetooth range problems.
4. Toggle Bluetooth off and on on both devices, then wait a minute for rediscovery.
5. If the laptop still does not see the phone, restart both devices — a fresh discovery cycle resolves many stale pairings.

### Fix 3: Update both apps

Version mismatches cause failures that no permission fix can solve. Update both sides before deeper troubleshooting.

1. On the laptop, open the Microsoft Store and update Phone Link to the latest version.
2. On the phone, update the Link to Windows app from the Play Store or App Store.
3. Open **Settings > Windows Update** on the laptop and install pending updates, since Phone Link depends on Windows components.
4. Restart both devices after updating.
5. Open Phone Link on the laptop and the companion app on the phone, and check whether sync resumes.

### Fix 4: Repair the Phone Link app on Windows

When the phone side checks out, the Windows app itself may hold corrupted pairing state.

1. Open **Settings > Apps > Installed apps**, find Phone Link, and open **Advanced options**.
2. Click **Repair**, then test sync.
3. If repair does not help, click **Reset** — this clears the pairing state and you will need to re-pair.
4. After a reset, pair again by scanning the QR code shown in Phone Link with the phone companion app.
5. Grant all permissions during the fresh pairing, since skipping one now creates a partial sync later.

### Fix 5: Re-pair from scratch and clean stale devices

A corrupted pairing can survive repairs on both sides. A clean re-pair removes it completely.

1. In Phone Link on the laptop, remove the phone from the device list.
2. On the phone, remove the laptop from the linked devices list in the companion app.
3. Clear the companion app's cache on Android, or reinstall it on iPhone if it offers no cache option.
4. Restart both devices, then pair fresh with the QR code flow.
5. Test each feature in turn — notifications, messages, photos, calls — so you know exactly which ones sync after the clean pairing.

### Fix 6: Check firewall, network, and account blocks

If a clean pairing still does not sync, something in the network or account layer is blocking the connection.

1. Temporarily disable third-party firewalls on the laptop and test sync.
2. Try a different Wi-Fi network or a phone hotspot to rule out router-level blocking.
3. Confirm the Microsoft account is not locked or restricted by signing into it in a browser.
4. Check whether a work or school account policy restricts Phone Link — managed devices sometimes block it by policy.
5. If sync still fails after a clean pairing on a clean network, contact Microsoft support with both app versions and the pairing error, if any. For general Windows help, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) and related [Windows Backup restore fixes](/articles/windows-backup-ai-pc-restore-fix/).

## Closing

Phone Link sync failures are usually phone-side problems: a killed companion app, a revoked permission, or a stale pairing. Check the phone's permissions and battery settings first, verify the shared network and account second, and re-pair cleanly before blaming the laptop. Worked through in order, these fixes restore sync for nearly every Phone Link setup. If this fix did not fully resolve the issue, related troubleshooting for [Hp Probook 440 Ai Laptop Issues](/articles/hp-probook-440-ai-laptop-issues-fix/) and [Click To Do Screenshot History](/articles/click-to-do-screenshot-history-fix/) covers neighboring causes that can produce the same symptom on AI laptops.
