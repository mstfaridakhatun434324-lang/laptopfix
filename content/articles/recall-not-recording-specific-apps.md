---
title: "How to Fix Recall Not Recording Specific Apps"
slug: recall-not-recording-specific-apps
date: 2026-10-21
categories: ["ai-pc"]
tags: ["recall not recording", "recall missing apps", "recall exclusions", "windows recall", "ai pc", "windows 11"]
description: "Recall skipping certain apps? Learn why Recall excludes some programs and follow six fixes to restore full snapshot coverage of your Windows 11 activity."
thumbnail: "/images/thumbs/recall-not-recording-specific-apps.webp"
faqs:
  - q: "Why is Recall not recording some of my apps?"
    a: "Recall deliberately skips private browsing windows, DRM-protected video, and apps you excluded in Settings. If an ordinary app is missing, it is usually on your exclusion list, running elevated, or affected by a capture glitch."
  - q: "Does Recall record incognito or private browsing?"
    a: "No, by design. Recall never captures InPrivate, Incognito, or other private browsing windows, and there is no setting to change that. This is a privacy guarantee, not a bug."
  - q: "Can I make Recall record an excluded app again?"
    a: "Yes. Remove it from the exclusion list in Settings > Privacy & security > Recall & snapshots. New snapshots will include the app going forward; previously skipped periods stay blank."
  - q: "Why are some apps blank even when not excluded?"
    a: "Apps showing DRM-protected content (some streaming video) render black to screen capture by design. Elevated (run-as-administrator) apps can also escape capture depending on system configuration."
---

Recall's timeline is impressively complete — until you search for something you definitely did and find a blank stretch. One specific app never appears in snapshots, while everything around it is captured fine. The timeline has a hole shaped exactly like that program.

Some of this is by design: Recall will never capture private browsing, and DRM-protected content renders black. But when an ordinary app — your code editor, a desktop program, a game — goes missing from snapshots, it is an exclusion, a privilege mismatch, or a capture glitch, and all three are fixable.

This guide gives you six fixes in order: check the exclusion list, understand the by-design skips, fix privilege and settings issues, and repair the capture pipeline. Work through them in sequence and test by using the app for a few minutes, then checking Recall.

## Why this happens

- **The app is on your exclusion list:** Recall lets you exclude apps and websites. An app added months ago — or added by a settings sync — stays excluded silently until you remove it.
- **Private browsing or DRM content:** Browsers' private windows and DRM-protected video are never captured, by design. No setting overrides this.
- **App running elevated:** Programs launched as administrator run at a higher integrity level than the capture service, and Recall may skip their windows.
- **Fullscreen exclusive mode:** Some games and media apps in exclusive fullscreen bypass the desktop compositor that Recall snapshots, leaving gaps.
- **Filter or website exclusion too broad:** Excluding a website can also exclude the browser window state around it, and overly broad app filters catch more than intended.
- **Capture pipeline glitch for that app:** Occasionally the snapshot service fails on specific window types — often after a graphics driver update — while capturing everything else normally.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Recall's app and website exclusion list

The exclusion list is the most common cause and the fastest check. Many users exclude an app during setup and forget, or a synced setting carries exclusions across devices.

1. Open **Settings > Privacy & security > Recall & snapshots** and find the **excluded apps and websites** section.
2. Look through the full list for your missing app — check carefully, as entries may show the process name rather than the friendly title.
3. Remove the app from the exclusion list.
4. Use the app normally for 5–10 minutes, then search Recall — new snapshots should now include it. Old gaps remain blank; only future activity is captured.

### Fix 2: Confirm the app is not a by-design skip

Before troubleshooting further, make sure you are not fighting intentional privacy behavior. Recall's guarantees are not configurable, and no fix will change them.

1. If the missing content is a private/Incognito browser window, that is by design — Recall never captures private browsing, full stop.
2. If it is streaming video showing a black rectangle, that is DRM protection doing its job; the rest of the app window should still capture.
3. If the app handles passwords, banking, or other sensitive input, check whether it marks its windows as non-capturable — some security-conscious apps do.
4. If none of these apply to your ordinary missing app, continue — the cause is a real configuration issue.

### Fix 3: Stop running the app as administrator

Elevated apps run above the capture service's integrity level, which is a classic reason one specific program vanishes from snapshots while everything else records fine.

1. Close the app completely, including any tray icon.
2. Right-click its shortcut, open **Properties > Compatibility**, and uncheck **Run this program as an administrator**.
3. Also check **Properties > Shortcut > Advanced** and uncheck **Run as administrator** there.
4. Relaunch the app normally, use it for a few minutes, and verify it now appears in Recall snapshots.

### Fix 4: Switch fullscreen apps to borderless windowed mode

Exclusive fullscreen apps can bypass the compositor path Recall uses for snapshots. Borderless windowed mode looks identical but captures reliably.

1. Open the app or game's display/video settings.
2. Change the display mode from **Fullscreen** (exclusive) to **Borderless Windowed** or **Windowed Fullscreen**.
3. Apply, use the app for several minutes, then check Recall for new snapshots of it.
4. If Click to Do's email actions also misbehave in the same app, the [Click to Do send-email fix](/articles/click-to-do-send-email-not-working/) covers the related integration.

### Fix 5: Update the graphics driver and restart the capture pipeline

A graphics driver update — or a stale one — can break snapshot capture for specific window types while leaving the rest of Recall working. Refreshing the driver and the pipeline clears it.

1. Update your graphics driver from your laptop maker or the GPU vendor's official tool, such as [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx).
2. In Recall settings, toggle **Save snapshots** off, restart the PC, and toggle it back on.
3. If the app's audio features also act up — for example voice input doing nothing — the [press-to-talk fix](/articles/copilot-press-to-talk-not-working/) covers the parallel permission-style failure.
4. Test the app again for 10 minutes and check whether snapshots now include it.

### Fix 6: Check for an unknown or failing NPU device

Recall's snapshot analysis depends on the NPU pipeline. If the NPU device is broken or unrecognized, capture can degrade in strange, app-specific ways rather than failing outright.

1. Open Device Manager and look at the NPU entry. An [unknown device](/articles/npu-unknown-device-in-device-manager/) or warning icon means the hardware layer needs repair first.
2. Reinstall the NPU/chipset driver from your laptop maker's support page and restart.
3. Confirm Task Manager > Performance shows a healthy **NPU** tab.
4. Re-test the missing app. If snapshots now capture it, the app was never the problem — the degraded AI pipeline was dropping its windows.

## Closing

Recall skipping specific apps is usually an exclusion you forgot, an elevated process, or exclusive fullscreen — all fixable in minutes. The by-design skips (private browsing, DRM) are the only ones you cannot change, and that is intentional. Clear the exclusions, run apps unelevated, prefer borderless windowed, and your timeline will stop having holes.
