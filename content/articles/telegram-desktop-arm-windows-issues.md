---
title: "How to Fix Telegram Desktop Issues on ARM Windows"
slug: telegram-desktop-arm-windows-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["telegram", "arm windows", "desktop app", "snapdragon", "messaging"]
description: "Telegram Desktop crashing, not syncing, or running slow on your Snapdragon laptop? Fix Telegram on ARM Windows with these build, cache, and GPU steps."
thumbnail: "/images/thumbs/telegram-desktop-arm-windows-issues.webp"
faqs:
  - q: "Is there a native ARM64 version of Telegram Desktop?"
    a: >
      Yes. Telegram Desktop ships native ARM64 builds for Windows on ARM — download from desktop.telegram.org on the Snapdragon laptop. The Microsoft Store version also serves the right architecture. Emulated x64 installs are the main cause of slowness.
  - q: "Why is Telegram not syncing messages on my ARM laptop?"
    a: >
      Sync failures are almost always network-related, not ARM-related: a proxy or VPN interfering, the app being throttled in the background, or a corrupted local database. Check the connection settings in Telegram before suspecting the architecture.
  - q: "Will reinstalling Telegram delete my chats?"
    a: >
      No. Telegram is cloud-based — all chats, media, and contacts live on Telegram's servers and restore when you sign in again. Only local settings and cached files are removed by a reinstall.
  - q: "Why do Telegram calls have no audio on Windows on ARM?"
    a: >
      Call audio issues are device-selection problems in the vast majority of cases: Telegram picking the wrong microphone or speaker. Open Telegram Settings > Advanced > Call settings and set the devices explicitly rather than leaving them automatic.
---

Telegram is supposed to be the fast, light messenger — the one that syncs instantly and sips resources. On your Snapdragon laptop, though, it launches slowly, chats take a second to render, calls have no audio, or the app just crashes. For an app famous for speed, this is embarrassing.

Telegram Desktop does have native ARM64 builds, so the architecture story here is better than most apps. The real culprits are usually the emulated install hanging around, a corrupted local database, GPU acceleration quirks, proxy/VPN interference with Telegram's MTProto connections, or audio device selection in calls.

This guide gives you six fixes in order: get the native build, fix sync and connection, clear the corrupted data, tune the GPU path, fix call audio, and handle notifications. VPN-related messaging failures share roots with [VPN not working on Windows on ARM](/articles/vpn-not-working-windows-on-arm/), so check that pairing.

## Why this happens

- **Emulated x64 build still installed:** Old installs from before ARM64 builds matured run under Prism emulation — slower and buggier than native.
- **Proxy or VPN interfering:** Telegram's MTProto protocol is sensitive to proxies and VPNs; a misconfigured one causes endless "connecting" states.
- **Corrupted local database:** Telegram caches chats locally — a damaged database causes crashes, missing messages, and UI lag.
- **Hardware acceleration quirks:** The client's GPU-accelerated UI can glitch on Adreno graphics with certain drivers.
- **Wrong audio devices in calls:** Telegram's automatic device selection picks wrong endpoints on ARM laptops with multiple audio devices.
- **Background throttling:** Power management throttling Telegram's background process delays message sync and notifications.
- **Outdated build:** ARM64-specific fixes ship in Telegram's frequent updates — old builds carry fixed bugs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build

Verify the build first — an emulated Telegram explains slowness, heat, and random crashes in one stroke, and no settings tweak compensates for emulation.

1. In Task Manager's **Details** tab, check whether Telegram.exe is flagged as emulated while running.
2. If emulated, quit Telegram fully (tray icon > Quit).
3. Uninstall it from **Settings > Apps > Installed apps**.
4. Download from desktop.telegram.org on the laptop, or install from the **Microsoft Store** — both serve ARM64 on Snapdragon machines.
5. Sign in with your phone number — chats, media, and contacts restore from the cloud. Test scrolling and search speed immediately.

### Fix 2: Fix connection and sync problems

"Connecting..." forever, messages that send from your phone but never appear on desktop, channels not updating — these are network-path issues, and Telegram gives you direct controls for them.

1. In Telegram **Settings > Advanced > Connection type**, check whether a proxy is configured — if you did not set one, set it to use system proxy or disable it.
2. Temporarily disconnect your VPN and test sync — if messages flood in, the VPN is interfering with MTProto.
3. Try toggling **Use IPv6** in the connection settings if your network has broken IPv6.
4. In **Settings > Advanced**, check **Connection** diagnostics for blocked data centers.
5. If one network works and another does not (home vs. office), the network is filtering Telegram — try the built-in MTProto proxy options or a different network. Printer-driver-class ARM issues show the same "works here, not there" pattern: [Brother printer driver on ARM](/articles/brother-printer-driver-arm-windows/).

### Fix 3: Clear Telegram's corrupted local data

Crashes on launch, chats that will not open, media that never loads — the local database or cache is corrupt. Because Telegram is cloud-based, clearing local data is completely safe.

1. Fully quit Telegram.
2. Press **Win + R**, type `%APPDATA%`, and rename **Telegram Desktop** to **Telegram Desktop.bak**.
3. Relaunch Telegram and sign in with your phone number — everything restores from the cloud.
4. Let it sync fully (watch the progress) before judging performance — the initial sync is heavy.
5. If stable after a few days, delete the `.bak` folder. Your chats were never at risk; they live on Telegram's servers.

### Fix 4: Tune the GPU and animation settings

UI lag, stuttering animations, and graphical glitches are the GPU path arguing with the Adreno driver. Telegram's settings let you calm it down without losing the native feel.

1. In Telegram **Settings > Advanced**, find the **Hardware acceleration** / ANGLE graphics backend option and try toggling it.
2. Disable **Large emoji** animations and sticker autoplay in **Settings > Chat Settings** if the chat view stutters.
3. Update the graphics driver via **Settings > Windows Update > Optional updates**.
4. Test scrolling through a media-heavy channel — that is the heaviest UI workload Telegram has.
5. Keep the combination that scrolls smoothly; retest after driver updates. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document driver update paths.

### Fix 5: Fix voice and video call audio

Call audio failures — silence, one-way audio, robotic voice — are device selection and audio-path issues, the same family as every other VoIP app on ARM. They are not Telegram bugs.

1. In Telegram, start a call, open the call settings, and set microphone and speaker explicitly — never leave them on automatic.
2. In Windows **Sound settings**, set devices to **16-bit, 48000 Hz** and disable exclusive mode.
3. Test with the **Echo test** / call settings preview before calling a real person.
4. If audio is robotic, disable any "noise suppression" enhancements in the Windows device properties for your mic.
5. Test with wired audio — if wired works and Bluetooth does not, the Bluetooth stack is the problem, not Telegram. Work/school Copilot chat toggles break in a similar device-context way: [Copilot chat work/web toggle missing](/articles/copilot-chat-work-web-toggle-missing/).

### Fix 6: Fix notifications and background sync

Messages arrive on your phone instantly but the desktop app is silent or hours late. That is background throttling or notification settings, not sync — the messages are there when you open the app.

1. In Windows **Settings > System > Notifications**, confirm Telegram is allowed to send notifications.
2. In **Settings > System > Power & battery**, set Telegram's background activity to allow unrestricted background work.
3. In Telegram **Settings > Notifications**, verify desktop notifications are enabled for the chat types you care about.
4. Disable **battery saver** interference: add Telegram as an exception if your laptop maker includes aggressive background killers.
5. Keep Telegram running (minimized, not quit) — a fully quit app cannot notify you, and cold-start sync will always lag behind your phone.

## Closing

Telegram on Snapdragon laptops is fast and reliable once it is the native ARM64 build with a clean local database — emulation and corrupted caches cause most complaints, with proxy/VPN interference covering the sync mysteries. Because everything lives in Telegram's cloud, you can be aggressive with the local fixes: nothing you delete in Fix 3 can lose a chat. Do the six steps and Telegram goes back to feeling instant.
