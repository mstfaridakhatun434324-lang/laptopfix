---
title: "LG Gram Pro AI: Fix Copilot Key and AI Features Not Working"
slug: lg-gram-pro-ai-copilot-not-working
date: 2026-10-21
categories: ["ai-pc"]
tags: ["lg gram pro ai", "copilot not working", "copilot key", "ai pc", "studio effects", "lg glance"]
description: "Fix LG Gram Pro AI Copilot problems — dead Copilot key, broken app, missing AI features — with six ordered technician fixes covering drivers and setup."
thumbnail: "/images/thumbs/lg-gram-pro-ai-copilot-not-working.webp"
faqs:
  - q: "Why does the Copilot key do nothing on my LG Gram Pro AI?"
    a: "The key usually fails because the Copilot app is missing, outdated, or blocked — the key just launches the app, so if the app cannot start, the key appears dead. Reinstalling the Copilot app from the Microsoft Store fixes it in most cases."
  - q: "Does Copilot need the NPU to work on the Gram Pro AI?"
    a: "The Copilot web app runs in the cloud and works without the NPU. But on-device features like Recall, Cocreator, and Studio Effects need the Intel AI Boost driver healthy — a broken NPU driver disables those even when Copilot chat works."
  - q: "Can LG Glance break Copilot or Studio Effects?"
    a: "LG Glance (by Mirametrix) hooks the camera for presence detection, and its camera driver can conflict with Studio Effects. If background effects fail while presence detection works, updating or pausing Glance is worth testing."
  - q: "Will a BIOS update fix Copilot issues?"
    a: "It fixes the AI-feature side — NPU enumeration, Studio Effects, Recall — but not the Copilot key or app itself, which are pure software. Update the BIOS when AI features fail, reinstall the app when the key or chat fails."
---

The LG Gram Pro AI pairs LG's famously light chassis with Intel's Core Ultra platform, and it ships with a dedicated Copilot key right on the keyboard. That key is supposed to summon Microsoft's Copilot instantly — but many owners find it does nothing, opens a broken app, or launches Copilot while none of the on-device AI features (Studio Effects, Recall, Cocreator) actually work.

The confusion comes from Copilot being two different things. The Copilot app is a cloud service that only needs an internet connection; the key simply launches it. The on-device AI features need the NPU, the Intel AI Boost driver, and strict Recall prerequisites. A machine can have working Copilot chat and dead AI features, or vice versa — and each half has its own fix path.

This guide covers both halves in technician order: fix the key and app first, then repair the NPU driver stack underneath, then check the prerequisites that gate the on-device features. Work through the steps in sequence and test after each.

## Why this happens

- **Copilot app missing or broken:** The Copilot key is just a shortcut that launches the app. If the app was uninstalled, never updated, or corrupted, the key appears completely dead.
- **Intel AI Boost driver failed:** On-device features (Studio Effects, Recall, Cocreator) need this driver. Without it, Copilot chat works fine but every NPU-powered feature fails.
- **LG Update Center drivers outdated:** LG ships chipset, camera, and BIOS updates through its own Update Center. Missing these leaves the NPU unenumerated or the camera incompatible with Studio Effects.
- **LG Glance camera conflict:** LG's presence-detection software hooks the camera at driver level, which can clash with Studio Effects' camera pipeline and kill background effects.
- **Recall prerequisites unmet:** Recall needs 40+ TOPS of NPU, BitLocker, Secure Boot, a Microsoft account, and Windows Hello. The Gram Pro AI qualifies on hardware, but any missing software prerequisite blocks it.
- **Driver crash after updates:** A mismatched NPU driver can destabilize the whole machine — if you have seen crashes, check the [NPU blue screen guide](/articles/npu-causes-blue-screen-windows-11/) before continuing, since an unstable driver must be replaced before anything else will work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair the Copilot app and key mapping

Start with the simplest layer: the key does nothing more than launch the Copilot app, so a healthy app usually revives a dead key immediately.

1. Open the **Microsoft Store**, search **Copilot**, and install or update it — then launch it manually to confirm it opens and signs in.
2. Press the Copilot key again. If the app opens now, the key was never the problem.
3. If the key still does nothing, check **Settings > Personalization > Text input** or your keyboard settings for Copilot key remapping options, and reset them to default.
4. As a fallback, pin Copilot to the taskbar — the key is a convenience, not a requirement. For machines where the whole AI feature set failed together, the [Gram AI Copilot issues overview](/articles/lg-gram-ai-copilot-issues/) maps which symptom belongs to which layer.

### Fix 2: Install LG's official driver pack from Update Center

LG validates drivers against the Gram Pro AI's thin-and-light power firmware, so LG's channel beats generic sources for the first attempt. This repairs the chipset and AI Boost drivers together.

1. Open **LG Update Center** (or LG Smart Assistant on newer builds) and install all required driver updates.
2. Prioritize anything labeled chipset, neural processor, AI Boost, camera, or BIOS.
3. Restart when prompted — driver cleanup often completes during boot, so do not skip it.
4. Open Device Manager and confirm **Intel AI Boost** appears cleanly under Neural processors with no warning icon.

### Fix 3: Manually repair the Intel AI Boost driver

If LG's pack did not restore the NPU, install the driver directly. A corrupt AI Boost driver is the single most common reason on-device AI features fail while Copilot chat keeps working.

1. In Device Manager, right-click the NPU (or unknown device), choose **Uninstall device**, and check **"Attempt to remove the driver for this device"**.
2. Restart the laptop, then run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) and install the chipset/AI Boost driver it detects.
3. Restart again and verify the NPU entry is clean in Device Manager.
4. Test an NPU feature directly: open Camera settings and toggle a Studio Effect, or try live captions.

### Fix 4: Resolve the LG Glance camera conflict

When background blur, eye contact, or automatic framing fail but the camera itself works in other apps, LG Glance's camera hook is the prime suspect. Presence detection and Studio Effects fight over the same camera pipeline.

1. Open **LG Glance by Mirametrix** settings and temporarily disable presence detection and camera-based features.
2. Test Studio Effects again in **Settings > Bluetooth & devices > Cameras**.
3. If effects return, update LG Glance to the latest version from LG Update Center, then re-enable its features one by one.
4. If the conflict persists on the newest Glance, leave presence detection off — Studio Effects are the more broadly useful feature on a Copilot+ PC.

### Fix 5: Meet the Recall and on-device AI prerequisites

With the driver healthy, Recall can still refuse to enable if any prerequisite is missing. Check each one explicitly rather than assuming.

1. Verify **Device encryption** is on under Settings > Privacy & security, Secure Boot reads **On** in `msinfo32`, and you are signed in with a Microsoft account with Windows Hello enrolled.
2. Open **Settings > Privacy & security > Recall & snapshots** and enable snapshot saving.
3. If snapshots save but you cannot find anything, adjust how often they are taken — the [Recall snapshot frequency settings](/articles/recall-snapshot-frequency-settings/) guide explains the trade-off between history depth and disk usage.
4. Confirm Cocreator appears in Paint and Studio Effects toggle in quick settings — these prove the NPU path is genuinely working.

### Fix 6: Update the BIOS and reset stuck AI hardware state

A BIOS update fixes NPU enumeration bugs that no driver reinstall can touch, and a cold boot clears firmware stuck after sleep. Do this when the NPU vanishes intermittently or AI features fail only after the laptop sleeps.

1. Install any BIOS update offered in LG Update Center with the charger connected, closing all programs first.
2. After the flash, do a full cold boot: hold **Shift**, click **Shut down**, unplug, hold power 15 seconds, wait 30 seconds, then power on.
3. Verify the NPU in Device Manager and retest Studio Effects and Recall.
4. If problems survive all of this, check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for current known issues, then contact LG support with your symptom log — a persistent failure past clean drivers and current BIOS points at hardware.

## Closing

Copilot key problems are almost always the app, not the keyboard — reinstall it from the Store first. Dead AI features are almost always the Intel AI Boost driver — repair it through LG Update Center, then Intel's assistant as backup. Keep LG Glance in mind when camera effects specifically fail, and verify Recall's prerequisites one by one instead of assuming they are met. With the driver stack clean and the BIOS current, the Gram Pro AI's full Copilot+ feature set comes up reliably.
