---
title: "How to Fix Edge Video Enhance Not Working on Windows 11"
slug: edge-video-enhance-not-working
date: 2026-10-24
categories: ["ai-pc"]
tags: ["edge", "video enhance", "windows 11", "gpu", "troubleshooting", "ai pc"]
description: "Edge Video Enhance is grayed out or doing nothing on your Windows 11 laptop? Follow these step-by-step fixes for GPU requirements, Edge flags, and settings."
thumbnail: "/images/thumbs/edge-video-enhance-not-working.webp"
faqs:
  - q: "Why is Video Enhance grayed out in Edge settings?"
    a: >
      The most common reason is that your GPU does not meet the minimum requirement — Microsoft requires an NVIDIA RTX 20-series or newer, or an AMD RX 5700 or newer, and a display powered by the discrete GPU. On many laptops, the integrated GPU drives the internal display, which disables the option entirely.
  - q: "Does Edge Video Enhance use my GPU?"
    a: >
      Yes — Video Enhance uses the GPU for AI-based video super resolution, not the CPU or NPU. It renders enhanced video at up to 720p using your graphics card, which is why gaming and media laptops see it work while NPU-only office laptops may not. For a deeper look at which chip does what, see our comparison of [CPU vs GPU vs NPU image generation](/articles/cpu-vs-gpu-vs-npu-image-generation/).
  - q: "Why does Enhanced video not work on some websites?"
    a: >
      Video Enhance only processes video below 720p and skips content protected by digital rights management, such as most paid streaming services. Try a test clip on a non-DRM site like YouTube at 480p to confirm the feature is working.
  - q: "Does Video Enhance drain laptop battery?"
    a: >
      Yes, it increases GPU load and can drain the battery faster while playing video on battery power. If you value battery life, leave it on but consider disabling it when unplugged, or plug in while watching enhanced video.
---

You are watching a 480p video in Edge and it looks exactly as blurry as before — the Video Enhance toggle does nothing, or worse, the option is grayed out and you cannot even turn it on. You know the feature exists because you have seen the sparkle icon on someone else's laptop, but your AI PC seems immune to it.

Video Enhance is Microsoft's AI-powered video super resolution built into Edge: it uses your GPU's machine-learning hardware to sharpen low-resolution video in real time, right in the browser. But it is picky. It demands a specific class of GPU, a recent Edge build, the right display wiring, and the right kind of video — miss any one condition and it silently does nothing. Most failures come down to hardware eligibility, a stalled Edge update, or protected video that the feature is not allowed to touch. Accessibility users sometimes hit similar AI-feature gray-outs, as covered in our guide to [accessibility AI features not working](/articles/accessibility-ai-features-not-working/), and budget AI laptops have their own quirks — the [Acer Swift Go 14 AI issues](/articles/acer-swift-go-14-ai-issues/) guide covers those.

This guide walks you through six fixes in technician order: verify GPU eligibility first, then Edge version and the enhancement setting, then the hidden flags, then driver updates, then test with eligible video, and finally reset Edge.

## Why this happens

- **GPU below the minimum requirement:** Video Enhance needs an NVIDIA RTX 20-series or newer, or an AMD RX 5700 or newer. Older GTX cards, Intel integrated graphics, and ARM/Qualcomm laptops do not qualify — the toggle stays grayed out permanently.
- **Display wired to the wrong GPU:** On many laptops the internal display is driven by the integrated GPU while the discrete GPU idles. Video Enhance requires the enhancing GPU to own the display pipeline, so hybrid-GPU laptops often fail this silently.
- **Outdated Edge version:** The feature arrived in Edge 109 and has been refined since. A browser that has not updated in months may show the setting but never engage it.
- **Enhancement not enabled in settings:** The master switch lives at edge://settings/system under "Enhance videos in Microsoft Edge". If it is off, the sparkle icon and all enhancement stop working.
- **DRM-protected or high-resolution video:** Netflix, Disney+, and similar services use protected video paths that Edge is not allowed to process, and anything already at 720p or higher is skipped by design.
- **Outdated or corrupted GPU drivers:** Even with qualifying hardware, a stale NVIDIA or AMD driver can break the AI pipeline Edge relies on — updating the driver is a frequent fix.
- **Broken Edge flags or profile:** The feature is gated behind experimental flags (notably the Video Super Resolution flag). A bad flag state or a corrupted profile can leave the UI present but non-functional.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your GPU actually qualifies

Before touching anything, verify your hardware meets Microsoft's bar — otherwise every other fix is wasted effort. This diagnosis takes two minutes.

1. Press **Windows key + R**, type `dxdiag`, and press Enter to open the DirectX Diagnostic Tool.
2. On the Display tab, note the GPU name — look for NVIDIA RTX 20xx/30xx/40xx or AMD RX 5700 or newer.
3. If you see only an Intel integrated GPU or a GTX 10-series/16-series card, your hardware does not support Video Enhance — stop here and leave the feature off.
4. On laptops with two GPUs, note which one is listed as the primary display device on Display 1 — if it is the integrated GPU, this is your likely blocker.
5. Continue to the next fix with your GPU model in mind.

### Fix 2: Update Edge and enable the enhancement setting

A surprising number of failures are just an old browser or a toggled-off master switch. Rule out both in one pass.

1. Open Edge, click the three-dot menu, and go to **Help and feedback > About Microsoft Edge** to force an update check.
2. Let Edge install any update and click **Restart** when prompted.
3. Type `edge://settings/system` in the address bar and press Enter.
4. Find **Enhance videos in Microsoft Edge** and switch it on — also set the dropdown to **All videos** if it is limited to a stricter mode.
5. Play a 480p video on YouTube and hover over it to check whether the sparkle/HD icon appears.

### Fix 3: Enable the Video Super Resolution flag

Edge still gates parts of this feature behind experimental flags. A flag stuck in the wrong state — or one never enabled — is a common silent killer.

1. Type `edge://flags` in the Edge address bar and press Enter.
2. Search for **Video Super Resolution** and set it to **Enabled**.
3. Also search for **Enhance videos** related entries and enable any that are present in your Edge build.
4. Click **Restart** at the bottom of the flags page to relaunch Edge with the new flags.
5. Re-open `edge://settings/system` to confirm the enhance toggle is still on, then test video playback again.

### Fix 4: Update your GPU driver from the official source

A stale driver breaks the AI acceleration Edge depends on, even on qualifying cards. Update from the manufacturer's official tool, not from Windows Update alone.

1. Identify your GPU brand from the dxdiag step in Fix 1.
2. For NVIDIA, use the [official NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx) and install the latest Game Ready or Studio driver for your card.
3. For AMD, grab the latest driver from [AMD's official support site](https://www.amd.com/en/support/download/drivers.html).
4. During installation, choose the **clean install** option if offered, then restart your laptop.
5. Re-open Edge and test a sub-720p video — driver refreshes fix roughly half of "it just does nothing" cases.

### Fix 5: Test with eligible video and rule out DRM

If the hardware and settings are right, the video itself may be the problem. Verify with content the feature is allowed to enhance.

1. Open YouTube in Edge and search for a video that offers a 480p quality option.
2. Click the settings gear in the player and force **Quality > 480p** so you are below the 720p enhancement ceiling.
3. Hover over the video and look for the sparkle/HD Video Enhance icon in the Edge video overlay.
4. Do NOT test with Netflix, Disney+, Prime Video, or similar — their protected DRM video path blocks enhancement by design.
5. If the icon appears on YouTube but not on your favorite site, the feature is working correctly and the site's content is simply ineligible.

### Fix 6: Reset Edge settings and repair the profile

When everything looks right but enhancement still refuses to engage, a damaged profile or settings store is the likely culprit. This is the last resort before accepting a hardware limitation.

1. In Edge, open **Settings > Reset settings** and click **Restore settings to their default values**.
2. Confirm the reset — this disables extensions and clears temp data but keeps bookmarks, history, and passwords.
3. After the reset, re-enable the enhance toggle at `edge://settings/system` and the flags from Fix 3.
4. If it still fails, create a test profile: click the profile icon, choose **Add profile**, sign in, and test Video Enhance there.
5. If the new profile works, the old one is corrupted — migrate your bookmarks to the new profile.

## Closing

Video Enhance is a genuine GPU-gated feature, so the honest starting point is hardware: if your laptop lacks an RTX 20-series or RX 5700-class GPU, no amount of settings surgery will turn it on. For qualifying machines, though, the fix chain — Edge update, enable the toggle, set the flags, update the GPU driver, test with eligible non-DRM video — resolves the vast majority of cases. If you work through all six and it still sits grayed out on a qualifying laptop, your OEM's display wiring or driver is the likely blocker, and [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) can help you escalate through your laptop maker's support channel. For everything else AI on your machine, keep exploring — these NPU and GPU features are new enough that everyone hits a setup snag somewhere.
