---
title: "Studio Effects Not Working in Microsoft Teams? Here's the Fix"
slug: studio-effects-not-working-teams
date: 2026-10-20
categories: ["ai-pc"]
tags: ["studio effects", "microsoft teams", "video calls", "troubleshooting", "ai pc", "windows 11"]
description: "Studio Effects missing or broken in Microsoft Teams meetings? Find out why background blur and eye contact fail on Copilot+ PCs and restore them fast."
thumbnail: "/images/thumbs/studio-effects-not-working-teams.webp"
faqs:
  - q: "Where are Studio Effects settings in Teams?"
    a: "Join or preview a meeting, open Device settings, and look for the camera effects or background effects panel. On Copilot+ PCs, Teams surfaces Windows Studio Effects — background blur, eye contact, automatic framing, and portrait light — directly in the pre-join screen and in-meeting device settings."
  - q: "Why do Studio Effects work in the Camera app but not Teams?"
    a: "Teams maintains its own camera pipeline and sometimes selects a different camera device or an incompatible capture mode. The Windows Camera app talks to Studio Effects directly, so a working Camera app with broken Teams points to Teams' device selection, not the NPU. Re-select the built-in camera in Teams device settings."
  - q: "Do I need Teams Premium for Studio Effects?"
    a: "No. Studio Effects are a Windows feature, not a Teams tier feature. Any Teams client on a Copilot+ PC with a working NPU can use them. If someone tells you to upgrade Teams, they are confusing Studio Effects with Teams Premium extras like intelligent recap."
  - q: "Why does enabling background blur crash my Teams call?"
    a: "A crash on enable means the NPU effects pipeline died — usually a driver problem. Update the NPU driver from your maker's support page and restart. If Teams keeps crashing, disable all effects, rejoin, then enable them one at a time to identify the unstable one."
---

You open Teams expecting the polished Studio Effects look — background blur, eye contact correction, automatic framing — and get a plain, unprocessed feed instead. Or worse, enabling an effect freezes your video mid-meeting. On a Copilot+ PC this is an NPU pipeline problem far more often than a Teams problem, which is actually good news: the fix is in Windows, not in the app.

Teams and Windows share responsibility here. Windows provides the effects through the NPU; Teams has to request them through the right camera path. When either side breaks, the effects vanish. This guide separates the two so you fix the right layer. The same pipeline drives other apps too — if Zoom is the problem child, read our guide on [Studio Effects issues in Zoom meetings](/articles/studio-effects-zoom-meeting-issues/).

Work through the steps below, testing in a Teams test call after each change, and your AI-enhanced video will be back.

## Why this happens

- **Teams selected the wrong camera:** A virtual camera or an old USB device bypasses Studio Effects entirely.
- **NPU pipeline crashed:** The effects run on the NPU; a driver stall kills all effects at once. Our guide on the [NPU not being used by apps](/articles/npu-not-used-by-apps-windows-11/) explains how to reset that pipeline.
- **Teams is outdated:** Older Teams builds predate proper Studio Effects integration on Copilot+ PCs.
- **Effects disabled per-device in Windows:** The toggle lives per camera in Settings, and Teams respects the Windows-level switch.
- **Conflicting Teams background effects:** Teams' own background effects can fight Windows Studio Effects for the same frame.
- **Insufficient NPU headroom:** Running several NPU features at once (framing + blur + eye contact) can overload weaker NPUs and drop effects.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Select the physical camera in Teams

Teams sometimes defaults to a virtual camera or a stale device entry, which bypasses Studio Effects. The physical built-in camera is the only path that carries the effects.

1. In Teams, open Settings > Devices and check the Camera dropdown.
2. Select your built-in camera by its real name — not a virtual camera or screen-share device.
3. Disable or uninstall virtual camera software (OBS Virtual Camera, ManyCam) if you are not using it.
4. Start a test call and check whether the effects options appear.

### Fix 2: Update Teams to the latest build

Studio Effects integration on Copilot+ PCs improved significantly across Teams updates. An old client may simply lack the hooks.

1. In Teams, click your profile picture > Check for updates.
2. Install the update and fully restart Teams (quit from the system tray, not just the window).
3. Clear the Teams cache: close Teams, delete `%appdata%\Microsoft\Teams` contents, and reopen.
4. Test effects in the pre-join preview before joining a real meeting.

### Fix 3: Enable effects in Windows Settings first

Teams respects the Windows-level Studio Effects switches. If they are off for your camera in Settings, Teams cannot turn them on by itself.

1. Open Settings > Bluetooth & devices > Cameras > your built-in camera.
2. Turn on the effects you want (background blur, eye contact, automatic framing).
3. Restart Teams so it re-reads the camera capabilities.
4. In the Teams pre-join screen, open background effects and confirm the Studio Effects options are listed.

### Fix 4: Turn off Teams' own background effects

Teams' built-in background blur competes with Windows Studio Effects for the same frame. Running both causes flicker or kills the Windows effects entirely.

1. In the Teams pre-join or in-meeting background settings, set the background to "None."
2. Let Windows Studio Effects handle blur instead — it runs on the NPU and looks smoother.
3. If you prefer Teams' backgrounds, turn off the Windows-level blur to avoid the conflict.
4. Pick one pipeline and stick with it; mixing them is the most common cause of visual glitches.

### Fix 5: Reset the NPU effects pipeline

When effects are enabled but the video freezes or crashes, the NPU pipeline has stalled. A reset clears it.

1. Disable all Studio Effects in Windows Settings for your camera.
2. Close Teams completely (end the process in Task Manager to be sure).
3. Reopen Teams, re-enable one effect, and test with a preview.
4. Add the remaining effects one at a time. If a specific effect crashes consistently, leave it off and update the NPU driver — background reading on the same root cause: [NPU not used by apps](/articles/npu-not-used-by-apps-windows-11/).

### Fix 6: Reinstall the camera and NPU drivers

If nothing above restores the effects, the driver pair is corrupted. Reinstall both from your manufacturer's support page.

1. Download the camera and NPU drivers for your exact model (for example from [HP Support](https://support.hp.com/us-en)).
2. In Device Manager, uninstall the camera (tick "remove driver") and the NPU device, then restart.
3. Install the downloaded NPU driver first, restart, then the camera driver.
4. Re-enable Studio Effects in Settings and verify in a Teams test call.

## Closing

Teams and Studio Effects break at the seam between the app and Windows: wrong camera, outdated client, conflicting background pipelines, or a stalled NPU. Work the app side first — camera selection, Teams update, one-effects-pipeline rule — then repair the Windows side with a pipeline reset and driver reinstall. Get the seam right and Teams becomes the best showcase your Copilot+ PC's camera has. On-device image features share the same NPU — see [Cocreator in Paint not working](/articles/cocreator-paint-not-working/).
