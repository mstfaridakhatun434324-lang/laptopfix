---
title: "How to Fix Live Captions Not Working on Phone Link Calls on Your AI PC"
slug: live-captions-phone-link-calls-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["live captions", "phone link", "ai pc", "calls", "accessibility", "troubleshooting"]
description: "Fix live captions missing on Phone Link calls on your AI PC with step-by-step checks for caption settings, audio routing, permissions, and app updates."
thumbnail: "/images/thumbs/live-captions-phone-link-calls-fix.webp"
faqs:
  - q: "Why do live captions work in other apps but not on Phone Link calls?"
    a: "Phone Link routes call audio through a separate Bluetooth and telephony path, so captions depend on that audio stream being shared correctly. If the call audio goes to the wrong device or the caption service cannot hear it, other apps can still caption normally."
  - q: "Do I need an internet connection for live captions on calls?"
    a: "On Copilot+ PCs, live captions can run on-device using the NPU, but Phone Link call captions still need a stable link between the phone and the PC. A weak Bluetooth connection can interrupt captions even when the call itself sounds fine."
  - q: "Will reinstalling Phone Link delete my messages and photos?"
    a: "No. Your messages, photos, and call history sync from your phone, so unlinking and relinking Phone Link does not delete them. You will need to grant permissions again and re-pair the devices."
  - q: "Can privacy settings block live captions on calls?"
    a: "Yes. If microphone access or speech recognition is turned off, Windows cannot generate captions from call audio. Check microphone permissions and the live captions toggle before assuming the feature is broken."
---

You answer a call through Phone Link on your Copilot+ PC, the conversation is clear, but the live captions window stays blank, frozen, or never appears at all. That gap matters most when you rely on captions to follow fast speech or a noisy room, and it turns a helpful accessibility feature into a source of frustration.

Live captions on a call depend on more moving parts than captions in a video app. Windows must capture the call audio stream, route it through the speech engine on your AI PC, and draw the text — while Phone Link keeps the Bluetooth link alive.

This guide walks you through the checks in technician order, from the caption toggle and audio device to Bluetooth, permissions, and a clean Phone Link repair. Work through the fixes in sequence and test with a short call after each one.

## Why this happens

- **Live captions turned off or misconfigured for calls:** The global caption toggle may be on, but the caption window can be minimised, muted, or set to caption only system audio rather than the call stream.
- **Call audio routed to the wrong device:** When Phone Link sends call audio to a headset, speaker, or monitor that Windows is not capturing, the caption engine hears nothing and shows nothing.
- **Microphone or speech permission blocked:** Windows privacy settings, or a disabled online speech recognition option, can stop the caption service from processing audio at all.
- **Bluetooth link unstable or using an old profile:** A weak or outdated Bluetooth connection can carry voice well enough for conversation but drop the clean audio stream captions need.
- **Phone Link or Windows component out of date:** A stale Phone Link app, a missing Windows update, or a corrupted caption language pack breaks the chain between the call and the caption window.
- **Conflicting audio enhancements or apps:** Noise suppression, a third-party audio app, or another caption tool can seize the audio stream and leave live captions with nothing to transcribe.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn live captions on correctly and check the caption window

Start with the obvious, but check it properly: the toggle alone is not enough if the window is hidden, muted, or positioned off-screen.

1. Open **Settings > Accessibility > Captions** and make sure **Live captions** is turned **On**.
2. Press **Windows + Ctrl + L** to open the caption window, then check it is visible, unmuted, and not minimised to the taskbar.
3. In the caption window settings, confirm the caption language matches the language spoken on the call.
4. Make a short test call through Phone Link and watch whether any words appear, even slowly — partial captions point to an audio problem, not a toggle problem.

### Fix 2: Route the call audio to the right device

Captions can only transcribe audio Windows can actually hear.

1. During a call, click the speaker icon in the taskbar and confirm the output device matches where you are actually hearing the call.
2. Open **Settings > System > Sound** and set the same device as the default for both output and communication.
3. In Phone Link, open **Settings > Calls** and confirm call audio is set to route through the PC rather than staying on the phone.
4. Disable audio enhancements for the active device under **Sound > Properties**, then test the call again.

### Fix 3: Grant microphone and speech permissions

Windows treats live captions as a speech feature, so a privacy block anywhere in that chain silences it.

1. Open **Settings > Privacy & security > Microphone** and confirm microphone access is **On** for the system and for Phone Link.
2. Go to **Settings > Privacy & security > Speech** and make sure **Online speech recognition** is enabled.
3. Restart the live captions window with **Windows + Ctrl + L** after changing any permission — the service only picks up new permissions on a fresh start.
4. Test again with a call, speaking a few clear sentences yourself so you can see whether your side captions correctly.

### Fix 4: Repair the Bluetooth connection to your phone

A call can sound acceptable over a marginal Bluetooth link while captions fail, because captions need a steady, uninterrupted stream. Similar connection-state problems affect other synced features, as seen in [Recall search by date range not working](/articles/recall-search-date-range-not-working-fix/) when a service loses track of its underlying data.

1. On the PC, open **Settings > Bluetooth & devices** and remove your phone from the paired devices list.
2. On the phone, forget the PC in its Bluetooth settings as well, so no stale pairing survives.
3. Restart both devices, then re-pair from Phone Link by scanning the code it shows.
4. In Phone Link, grant all requested permissions — calls, contacts, and nearby devices — when prompted.

### Fix 5: Update Phone Link, Windows, and the caption language pack

An outdated component is the next most likely culprit, particularly the caption language pack, which can corrupt silently during an update.

1. Open the Microsoft Store, go to **Library**, and update **Phone Link** to the latest version.
2. Open **Settings > Windows Update** and install all pending updates, then restart the PC.
3. Go to **Settings > Accessibility > Captions > Caption language** and remove and re-add your language to force a fresh language pack download.
4. Check the guidance on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) if an update fails or the language pack refuses to install.

### Fix 6: Reset Phone Link and the caption service as a last resort

If captions still fail after the steps above, a clean reset clears corrupted app state without losing your synced content.

1. Open **Settings > Apps > Installed apps**, find **Phone Link**, and choose **Advanced options > Reset**.
2. Open **Settings > Apps > Installed apps**, find **Live Captions** if listed separately, and reset it the same way.
3. Unlink the phone in Phone Link, restart the PC, then link it again from scratch and grant every permission.
4. Test with a real call rather than a voicemail or recording — only a live call exercises the full caption path.
5. If captions remain blank, check whether a backup and restore cycle disturbed other AI features, as described in [Windows Backup restore problems on AI PCs](/articles/windows-backup-ai-pc-restore-fix/). For a different Copilot+ shortcut problem, the steps in [Copilot keyboard shortcut not working](/articles/copilot-keyboard-shortcut-not-working/) show how a single stuck component can be isolated the same way.

## Closing

Live captions on Phone Link calls fail when the audio route, the permission, or the Bluetooth link breaks — not because the feature itself is unreliable. Check the caption window first, fix the audio device second, and re-pair the phone before you reset anything, and most calls will caption cleanly again.
