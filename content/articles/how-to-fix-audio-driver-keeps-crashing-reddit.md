---
title: "Audio Driver Keeps Crashing? Fixes That Stick"
slug: how-to-fix-audio-driver-keeps-crashing-reddit
date: 2026-09-10
categories: ["drivers"]
tags: ["audio driver", "crashing", "realtek", "sound stutter"]
description: "Audio driver crashing repeatedly? Stop the cycle with the community-tested fixes for unstable Realtek and Intel audio drivers."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-reddit.webp"
faqs:
  - q: "Why does my audio driver keep crashing over and over?"
    a: "Recurring audio crashes come from an unstable driver build, conflicting audio software fighting over the same device, or corrupted driver-store entries that survive reinstalls. The crash loop persists because each 'fix' — like letting Device Manager reinstall the same broken driver — restores the identical faulty state. Breaking the cycle requires a clean removal plus the manufacturer's known-good package."
  - q: "How can I tell if it's the driver crashing or something else?"
    a: "Open Event Viewer > Windows Logs > System and filter for errors mentioning your audio driver's .sys file or 'Windows Audio' around the crash times. Driver crashes also show a pattern: sound dies, the speaker icon may show a red X briefly, and audio returns after the driver restarts — sometimes with a pop. App-specific silence without those signs points at the app, not the driver."
  - q: "Will disabling audio enhancements stop the crashes?"
    a: "Often yes, at least as a diagnostic. The enhancement APOs run inside the audio driver's process space, so a buggy enhancement crashes the driver with it. If disabling all enhancements stops the crashes, you've isolated the fault to the APO layer — then reinstall the OEM driver package to get a healthy enhancement chain back."
  - q: "Should I use the driver from Windows Update or the manufacturer?"
    a: "The manufacturer, every time, for crashing audio. Windows Update's generic audio drivers are the most common source of instability reports — they lack the model-specific validation and often mismatch the enhancement components. Download the audio package from your laptop maker's support site for your exact model."
---

Sound dies mid-video. Or the audio stutters into a robotic buzz, the speaker icon flashes, and everything goes silent until the driver restarts itself — only to crash again ten minutes later. An audio driver stuck in a crash loop is one of the most maddening Windows problems because each crash looks like a one-off, and the usual advice ("update your drivers") is often what caused it.

The forum threads on this all converge on the same insight: a crashing audio driver is almost never fixed by installing *another* driver on top of the broken one. The crash state lives in corrupted driver-store entries, mismatched enhancement components, and conflicting audio software — and it survives ordinary reinstalls. The fixes below are ordered to break the cycle for real: diagnose the crash, strip the bad state completely, then install one known-good manufacturer package.

For the update-specific variant, see our [audio crash fix for Windows 11 24H2](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/).

## Why this happens

- **A buggy or mismatched driver build.** The top cause: a driver version with a real defect, or a generic Windows driver mismatched with the laptop's audio hardware and enhancement chain.
- **Conflicting audio software.** Virtual audio cables, Voicemeeter, old conferencing drivers, and "audio enhancer" tools hook the same device — conflicts crash the driver.
- **Corrupted enhancement (APO) registrations.** The audio processing objects run in the driver's space; a corrupt APO takes the driver down with it, repeatedly.
- **Corrupted driver-store entries.** Leftover driver packages from previous installs get re-applied on every reinstall, reintroducing the same broken state.
- **Power management cutting the codec.** Aggressive power saving on the audio controller causes suspend/resume crashes — the classic "crashes when the laptop sleeps" pattern.
- **Failing audio hardware.** Rare, but a dying codec produces driver crashes that no software fix touches — suspect after all software avenues are exhausted and crashes happen in Linux too.
- **Overzealous "optimizer" tools.** Debloat utilities that disable audio services or strip driver components create an unstable hybrid that crashes under load.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's the driver crashing (Event Viewer)

Don't guess — read the crash log. Two minutes.

1. Press **Win + X** > **Event Viewer** > **Windows Logs** > **System**.
2. Look for **Error** entries around your crash times mentioning your audio driver (e.g., `rtkvhd64.sys`, `IntcAzAud.sys`) or the **Windows Audio** service stopping unexpectedly.
3. Note the faulting module name — if it's consistently the audio `.sys` file, it's the driver. If it's an app's `.dll`, the app is the problem, not the driver.
4. Also check **Reliability Monitor** (**Win + S** > *reliability*) — it shows the crash history as a timeline, making the pattern (and its start date) obvious. A start date matching a Windows update is a strong lead.

### Fix 2: Disable all audio enhancements

The fastest circuit-breaker — isolates the APO layer in one toggle.

1. Right-click the speaker icon > **Sound settings** > **More sound settings** > **Playback** > double-click your output device.
2. On the **Enhancements** tab, check **Disable all enhancements**. Apply and use the laptop normally for a few hours.
3. If the crashes stop, the fault is in the enhancement chain — proceed to Fix 3 for the permanent repair (a clean OEM driver with healthy APOs).
4. If crashes continue with enhancements off, the driver core itself is unstable — skip to Fix 4's clean removal.

### Fix 3: Remove conflicting audio software

Strip the contenders fighting over the audio device.

1. **Settings > Apps > Installed apps** — uninstall virtual audio tools (VB-Cable, Voicemeeter), old "sound booster" apps, and conferencing software you no longer use.
2. In **Device Manager > View > Show hidden devices**, expand **Sound, video and game controllers** and uninstall grayed-out ghost audio devices from previously removed hardware.
3. Check **Task Manager > Startup** for audio-related utilities (Nahimic, Sonic Studio, MaxxAudio updaters from the wrong vendor) and disable anything that doesn't match your laptop's brand.
4. Reboot and test for several hours before reinstalling anything — stability here confirms the conflict theory. Related enhancement-stack issues are covered in our [MaxxAudio fix guide](/articles/how-to-fix-waves-maxxaudio-not-working-in-windows-11-24h2/).

### Fix 4: Clean-remove the driver from the driver store

Ordinary uninstalls leave the broken package in the store, where Windows happily reinstalls it. Remove it properly.

1. Download the **correct audio driver** for your exact model from the laptop maker's support site first — you'll need it offline.
2. Install the free **Driver Store Explorer (RAPR)** tool, run as administrator, and delete all driver packages related to your audio device (Realtek, Intel Smart Sound, Conexant — audio only, touch nothing else).
3. In **Device Manager**, uninstall the audio device with *Attempt to remove the driver for this device* checked.
4. Reboot — Windows will either have no audio driver (fine) or a bare inbox one. Now install the manufacturer's package as administrator and reboot again.

### Fix 5: Install the manufacturer's known-good package (and stay there)

One validated driver, protected from "updates."

1. Install the OEM audio package downloaded in Fix 4. Prefer a version from the maker's site over the absolute newest — if the release notes don't mention your issue, the currently posted stable version is the right choice.
2. After installing, verify stability for a day with enhancements **enabled** (the OEM package should have a healthy APO chain).
3. Then block Windows from replacing it: see our guide on [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) — this is what stops the crash cycle from restarting next Patch Tuesday.
4. If the OEM package itself crashes, try one version older from the maker's archive — occasionally the newest OEM release is the buggy one, and the forums will tell you which version is stable.

### Fix 6: Tame power management on the audio controller

For crashes tied to sleep, idle, or battery.

1. In **Device Manager**, find the audio controller under **System devices** (e.g., *Intel Smart Sound Technology*) > **Properties > Power Management** > uncheck *Allow the computer to turn off this device*.
2. In **Power Options > Advanced**, set **PCI Express > Link State Power Management** to **Off** (or Moderate, not Maximum) — aggressive PCIe power saving crashes audio codecs on some platforms.
3. Test specifically around sleep/wake cycles — put the laptop to sleep and wake it several times with audio playing.
4. Keep the laptop plugged in during testing to separate battery-saver behavior from genuine driver instability.

### Fix 7: Rule out hardware with a live environment

When software is fully exhausted.

1. Boot a **Linux live USB** and play audio for an extended session — hours, not minutes, since these crashes are intermittent.
2. Crashes in Linux too = the audio codec or motherboard audio circuit is failing. No Windows driver will fix that.
3. Check whether crashes correlate with **heat** — audio codecs near hot components can fail thermally; monitor temperatures during the crash window.
4. Practical paths: in-warranty = manufacturer repair with your Event Viewer logs as evidence; out-of-warranty = a USB sound card ($15–25) bypasses the internal codec entirely and is a perfectly good permanent solution. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the official audio-troubleshooting sequence as a final cross-check.

## Closing

A crashing audio driver keeps crashing because the broken state keeps getting reinstalled — the same bad package from the driver store, the same conflicting software, the same generic update. Break the loop deliberately: confirm the crash in Event Viewer, strip the driver store clean, remove the conflicts, and install exactly one manufacturer-validated package. Stability, once restored this way, tends to stay restored.
