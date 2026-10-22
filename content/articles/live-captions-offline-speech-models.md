---
title: "How to Download Live Captions Offline Speech Models on Windows 11"
slug: live-captions-offline-speech-models
date: 2026-10-22
categories: ["ai-pc"]
tags: ["live-captions", "speech-models", "offline-download", "windows-11", "copilot-plus-pc", "npu"]
description: "Live Captions needs offline speech models to run on your Copilot+ NPU. Learn how to download them correctly and fix downloads that stall, fail, or vanish."
thumbnail: "/images/thumbs/live-captions-offline-speech-models.webp"
faqs:
  - q: "Why does Live Captions need to download speech models?"
    a: "On Copilot+ PCs, Live Captions runs entirely on-device through the NPU for privacy and speed. The speech recognition and translation models must be downloaded once first — after that, captions work fully offline with no internet required."
  - q: "How big are the Live Captions speech model downloads?"
    a: "Each language's speech model is a few hundred megabytes, and translation models add more. A couple of languages can take over a gigabyte, so download them on Wi-Fi with enough free disk space before you need captions."
  - q: "Can Live Captions work without an internet connection?"
    a: "Yes — after the models are downloaded. That is the whole point of the on-device design. If captions demand a download every time you go offline, the model install is incomplete or corrupt; see our [language pack download fix](/articles/live-captions-language-pack-download-failed/)."
  - q: "Do I need a Microsoft account to download speech models?"
    a: "No. Speech model downloads come through Windows' built-in language and caption components, not the Store account system. If a download asks you to sign in, you are in the wrong place — use the caption settings gear instead."
---

Live Captions on a Copilot+ PC is an offline feature by design: speech recognition runs on the NPU inside your laptop, not in the cloud. But before that privacy-friendly magic works, Windows must download the speech models — one per language — and those downloads fail more often than they should.

A stalled download leaves you with a caption window stuck on "preparing" or a language that simply never becomes available. Worse, a corrupt partial download can break captions entirely, producing the speech-model errors that send people searching for answers. If you are seeing explicit model errors, our [language pack download repair](/articles/live-captions-language-pack-download-failed/) targets those; this guide covers the download process end to end.

Below is the right way to get the models onto your machine, and repairs for every stage where the download can stall, fail, or silently corrupt.

## Why this happens

- **Metered or unstable connection:** Windows pauses large optional downloads on metered networks.
- **Insufficient disk space:** Each model needs hundreds of MB; a full drive aborts the download silently.
- **Interrupted first download:** Closing the caption window mid-download leaves a corrupt partial model.
- **Stuck Windows Update components:** Caption models ride the same delivery plumbing as optional updates.
- **Corrupt model cache:** Old or partial model files block fresh downloads until cleared.
- **VPN or proxy interference:** Some VPNs and corporate proxies throttle or block Microsoft's model CDN.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Download speech models the correct way

Many failures come from starting the download in the wrong place. The caption settings gear is the reliable entry point.

1. Open the Live Captions window and click the settings gear, then Language.
2. Choose Add a language and select the language you need captions in.
3. Keep the caption window open and the laptop awake until the download completes.
4. Do not switch to a metered connection or VPN during the download.
5. When the language appears in the list, play audio to confirm captions actually work offline.

### Fix 2: Unblock downloads on metered connections

Windows treats speech models as optional content and will not fetch them over a metered connection — the download just sits there.

1. Open Settings > Network & internet > Wi-Fi and check if the connection is marked metered.
2. Turn off the metered setting, or connect to a different, non-metered network.
3. In caption settings, remove the stalled language and re-add it to restart the download.
4. Alternatively, keep metered on but go to Settings > Windows Update > Advanced options and allow downloads over metered connections.
5. Retry the download and confirm it progresses instead of hanging at 0%.

### Fix 3: Free disk space and clear partial models

A drive with little free space aborts model downloads without a clear error. Clearing the partial files lets the next attempt start clean.

1. Check free space on C: — keep at least 2 GB free for a couple of language models.
2. Run Disk Cleanup or Storage Sense to reclaim space if needed.
3. Remove the half-installed language from caption settings.
4. Restart the laptop so any locked partial model files are released.
5. Re-add the language and download again on stable Wi-Fi.

### Fix 4: Repair the Windows Update delivery plumbing

Speech models download through the same components as optional Windows updates. When that pipeline jams, caption models jam with it.

1. Open Settings > Windows Update and install every pending update, then restart.
2. Run the Windows Update troubleshooter from Settings > System > Troubleshoot > Other troubleshooters.
3. If updates themselves fail, reset the update components (stop the wuauserv and bits services, rename SoftwareDistribution, restart).
4. Try the caption model download again after the pipeline is healthy.
5. You can also verify a clean Windows image via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) if the system itself seems damaged.

### Fix 5: Bypass VPNs and proxies during the download

Corporate VPNs, proxies, and aggressive firewalls can throttle or block the CDN that hosts the models — the download crawls or resets.

1. Disconnect the VPN temporarily and retry the download on a direct connection.
2. If you use a manual proxy, disable it in Settings > Network & internet > Proxy for the download.
3. Pause third-party firewall or "privacy" apps that filter HTTPS traffic.
4. Download the model, then re-enable your VPN or proxy afterwards — captions themselves need no network at all.
5. If a corporate network blocks the download permanently, download at home and the models stay installed.

### Fix 6: Verify the models actually run offline

A download that "completed" is not proven until captions work with the network off. Testing this now saves a nasty surprise on a plane.

1. With models installed, turn on Airplane mode or disconnect Wi-Fi.
2. Open Live Captions and play a local video or speak into the microphone.
3. Confirm captions appear promptly — this proves the NPU is using the local models.
4. If captions demand a download again, the install is corrupt: remove the language, restart, and re-download (Fix 1).
5. Note that running captions inside a VM will not use the NPU at all — our [NPU unavailable in virtual machine guide](/articles/npu-not-available-virtual-machine/) explains why, and [Arm64EC app issues](/articles/arm64ec-apps-explained-fix/) covers mixed-architecture quirks on Arm laptops.

## Closing

Offline speech models are what make Live Captions on a Copilot+ PC private, fast, and airplane-proof — but only if the one-time download actually completes. Do it deliberately: stable non-metered Wi-Fi, plenty of disk space, the caption window left open, and no VPN in the way. If a download misbehaves, the culprit is almost always the delivery plumbing (metered settings, Windows Update, proxies) rather than the model itself. Get the models on board once, verify they work in Airplane mode, and captions are yours anywhere, no connection required. Treat speech models like any other system component: download once on good Wi-Fi, verify offline, and leave them alone — they will quietly do their job for months.
