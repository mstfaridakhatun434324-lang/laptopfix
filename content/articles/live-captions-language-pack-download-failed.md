---
title: "Live Captions Language Pack Download Failed? Here's the Fix"
slug: live-captions-language-pack-download-failed
date: 2026-10-20
categories: ["ai-pc"]
tags: ["live captions", "language pack", "download failed", "troubleshooting", "ai pc", "windows 11"]
description: "Live Captions language pack stuck or failing to download on your Copilot+ PC? Learn why the speech model download fails and get captions working again."
thumbnail: "/images/thumbs/live-captions-language-pack-download-failed.webp"
faqs:
  - q: "Why does the Live Captions language pack keep failing to download?"
    a: "The usual causes are a metered connection blocking the download, insufficient disk space, a stalled Windows Update service, or corrupted speech components. The pack is several hundred megabytes, so any interruption forces a restart of the whole download."
  - q: "How big is the Live Captions language pack?"
    a: "Roughly 300-500MB depending on the language. It is a one-time download per language. Make sure you have at least 2GB free so the download and extraction both have room."
  - q: "Can I use Live Captions without the language pack?"
    a: "No. The pack contains the on-device speech recognition model — without it there is nothing to convert audio to text. The captions feature will prompt you every launch until the download succeeds."
  - q: "Does the download need the NPU working?"
    a: "No, downloading is independent of the NPU. But once installed, advanced features like translation need the NPU healthy. If downloads succeed yet captions misbehave, check the driver side — for example our guide on [Intel NPU driver update failures](/articles/intel-npu-driver-update-failed/)."
---

Live Captions prompts you to download a language pack, you click download, and it spins forever — or fails outright. Without that speech model, captions cannot function at all, so this is a hard blocker. The good news: the failure is almost always in the download plumbing (Windows Update service, disk space, network policy) rather than anything AI-specific.

Copilot+ PCs download the same packs as other Windows 11 machines, but users hit this more often because they enable Live Captions on day one — before Windows Update has finished its own first-run backlog. This guide clears the download path step by step.

Follow the fixes in order and retry the download after each one. Once the pack lands, if captions still misbehave, our [no audio detected guide](/articles/live-captions-no-audio-detected/) picks up where this one ends.

## Why this happens

- **Metered connection blocks downloads:** Windows pauses large downloads on metered Wi-Fi or mobile hotspots.
- **Windows Update service stalled:** The pack downloads through the update stack; a stuck service stalls it too.
- **Insufficient disk space:** The download plus extraction needs over a gigabyte of free space.
- **Corrupted speech components:** A previous partial download left broken files that block retries.
- **Region/language mismatch:** The requested pack does not match an installed Windows language, confusing the downloader.
- **Third-party firewall or VPN interference:** Security software can block the specific endpoints the speech downloader uses.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Switch off the metered connection flag

Windows will not download multi-hundred-megabyte packs over a connection it thinks is metered. This is the most common silent blocker.

1. Open Settings > Network & internet > Wi-Fi (or Ethernet) and select your connection.
2. Turn off "Metered connection" if it is enabled.
3. Return to the Live Captions prompt and retry the download.
4. Keep the laptop on Wi-Fi (not a phone hotspot) until the download finishes.

### Fix 2: Free up disk space

The pack needs room to download and extract. A nearly full drive fails the download without a clear error.

1. Check free space in Settings > System > Storage — aim for at least 2GB free.
2. Run Disk Cleanup and empty the Recycle Bin.
3. Move large personal files to OneDrive or external storage if needed.
4. Retry the language pack download.

### Fix 3: Restart the Windows Update service

The speech pack downloads through the update stack. A stalled update service stalls the pack with it.

1. Open Services (search "services" in Start), find "Windows Update," and restart it.
2. Also restart the "Background Intelligent Transfer Service."
3. Open Settings > Windows Update and check for updates to flush the queue.
4. Retry the Live Captions download.

### Fix 4: Install the pack manually through Settings

Bypassing the captions prompt and installing through the language settings often succeeds where the prompt fails.

1. Go to Settings > Time & language > Language & region.
2. Select your language, click the three dots, and choose Language options.
3. Under Speech, click Download and wait for completion.
4. Open Live Captions — it should now start without prompting.

### Fix 5: Clear corrupted partial downloads

A failed attempt can leave broken files that poison every retry. Clearing them forces a clean download.

1. Open Settings > Time & language > Speech and remove the partially installed pack if listed.
2. Run `sfc /scannow` in an elevated Command Prompt to repair system files.
3. Restart the laptop.
4. Reinstall the pack via Fix 4's manual path. If captions then misbehave, our [no audio detected guide](/articles/live-captions-no-audio-detected/) continues the troubleshooting.

### Fix 6: Check VPN, firewall, and region settings

Security software and region mismatches can block the specific download endpoints.

1. Temporarily disconnect your VPN and retry the download.
2. Check third-party firewall logs for blocked Microsoft endpoints and allow them.
3. Confirm your Windows region (Settings > Time & language > Language & region > Country) matches the language pack you want.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents current language-pack requirements if the mismatch persists.

## Closing

A failed language pack download is a plumbing problem: metered flags, full disks, stalled update services, or corrupted partial files. Clear the path with the steps above, install the pack manually through language settings when the prompt misbehaves, and Live Captions will finally have the model it needs. The download happens once — after that, captions are yours offline, forever. On-device image restyling uses similar AI components — see [Restyle Image in Cocreator not working](/articles/restyle-image-cocreator-not-working/). Once captions work, keep Windows updated so the speech models stay current. Click to Do's AI actions need similar on-device models — see [Click to Do Rewrite not working](/articles/click-to-do-rewrite-not-working/).
