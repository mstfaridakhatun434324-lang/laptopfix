---
title: "Audio Driver Keeps Crashing on Windows 10: 7 Reliable Fixes"
slug: "how-to-fix-audio-driver-keeps-crashing-on-windows-10"
date: "2026-09-25"
categories: ["drivers"]
tags: ["audio driver", "realtek", "sound crash", "windows 10", "no sound"]
description: "Audio cutting out repeatedly on Windows 10? Discover why the sound driver crashes and apply seven reliable fixes to keep your laptop's audio stable."
thumbnail: "/images/thumbs/how-to-fix-audio-driver-keeps-crashing-on-windows-10.webp"
faqs:
  - q: "Why does sound keep cutting out on my Windows 10 laptop?"
    a: "Intermittent cutouts usually mean the audio driver is crashing and restarting rather than a speaker fault. Typical triggers on Windows 10 are Windows Update replacing the OEM Realtek driver with a generic version, corrupted driver files from a failed update, conflicting enhancement software, and power management suspending the audio codec. The pattern of sound dying until reboot is the signature of driver instability."
  - q: "How can I tell if the problem is the driver or the speakers?"
    a: "Plug in USB or Bluetooth headphones: if they play perfectly while the internal speakers cut out, the speakers or internal codec path are suspect. If all outputs cut out together, the audio driver or Windows audio services are at fault. Also check Event Viewer under Windows Logs, System, for errors from the audio driver source around the time sound died."
  - q: "Does disabling audio enhancements really help?"
    a: "Yes, it is one of the most effective single steps. Enhancement layers from Realtek, Waves, Dolby, or Nahimic insert processing between Windows and the driver, and version mismatches crash the chain. Disabling all enhancements isolates whether the base driver is stable. If sound stays up with enhancements off, update the enhancement software or leave it disabled."
  - q: "Will a Windows 10 reinstall fix audio driver crashes?"
    a: "It usually does, because a clean install removes corrupted drivers, conflicting software, and damaged system files in one sweep. But it is the most disruptive option and rarely necessary — installing the correct OEM driver, disabling enhancements, and blocking driver replacements resolves the same problems with far less effort. Reserve reinstallation for cases where crashes survive every targeted fix."
---

On Windows 10, audio driver crashes have a familiar rhythm: music plays fine, then silence — the speaker icon may show an error, or everything looks normal but no sound comes out until you restart. Then it happens again tomorrow. This cycle points squarely at the audio driver failing under real-world conditions, not at broken speakers.

Windows 10's long support life means many laptops have accumulated years of driver updates, enhancement software, and OS patches layered on top of each other — a perfect recipe for the conflicts that crash audio drivers. The approach here is subtractive: strip the stack back to a known-good driver, remove the conflicting layers, and lock the configuration so it stays fixed.

## Why this happens

- **Years of layered driver updates:** Successive updates leave conflicting driver remnants that destabilize the audio stack.
- **Generic driver from Windows Update:** The basic Microsoft audio driver lacks the codec-specific tuning the laptop needs.
- **Enhancement software version drift:** Audio effects apps updated independently of the driver cause processing-chain crashes.
- **Corrupted driver files:** Failed or interrupted updates leave the driver in a half-working state.
- **Power management suspending the codec:** The audio chip powers down during idle and crashes on resume.
- **Application exclusive-mode conflicts:** Programs seizing exclusive audio control destabilize fragile drivers.
- **Damaged Windows audio services:** Corruption in the Audio and Endpoint Builder services mimics driver failure.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Do a full clean reinstall of the OEM audio driver
Download the audio driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Open Device Manager, expand "Sound, video and game controllers," uninstall the audio device with driver deletion ticked, and also uninstall any enhancement entries (Waves, Dolby, Nahimic). Reboot, install the downloaded package, and reboot again. Years of layered updates are wiped out in one pass, and the matched driver-app set starts clean. Our [Realtek-specific guide](/articles/how-to-fix-realtek-audio-not-working-on-windows-10/) walks through driver sourcing.

### Fix 2: Strip all audio enhancements
Open the classic Sound panel (right-click the speaker icon, Sounds), open your playback device Properties, and on the Enhancements tab tick "Disable all enhancements." On the Advanced tab, uncheck both Exclusive Mode boxes and set the default format to 24-bit, 48000 Hz. Enhancement layers are the top crash trigger on aging Windows 10 installs because they get updated — or abandoned — independently of the driver. Run the laptop for a full day like this; stability here proves the base driver is sound.

### Fix 3: Stop Windows Update from swapping the driver
Open System Properties, Advanced system settings, Hardware tab, Device Installation Settings, and choose "No." Windows 10 is particularly aggressive about replacing audio drivers during its twice-yearly feature updates, and each replacement risks reintroducing the crash. With this set, your manually installed OEM driver stays put. See our guide on [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates/) for the registry method that survives feature upgrades.

### Fix 4: Repair the Windows audio services and system files
In `services.msc`, restart "Windows Audio" and "Windows Audio Endpoint Builder" and set both to Automatic. Then run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt. On long-lived Windows 10 installs, system file corruption accumulates and the audio stack is often where it surfaces. This repair pass is non-destructive and rules out OS-level damage before you blame the driver further.

### Fix 5: Disable codec power management
In Device Manager, open the audio device's Properties and uncheck power-saving on the Power Management tab. In Power Options advanced settings, disable USB selective suspend and set PCI Express link state power management to Off while testing. The signature symptom — sound dies after a period of silence, fine after reboot — is the codec failing to wake from suspension. If disabling power management ends the crashes, you have found a firmware-level quirk to simply leave disabled.

### Fix 6: Isolate the conflicting application with clean boot
Run `msconfig`, hide Microsoft services, disable everything else, and disable startup items. Reboot and test audio stability over normal use. Re-enable in halves until crashes return. On Windows 10 the usual offenders are old EQ utilities, virtual audio cables from streaming setups, and conferencing tools with aggressive audio hooks. Remove or update whatever you find — and note that our [speaker troubleshooting guide](/articles/how-to-fix-laptop-speakers-not-working-on-windows-10/) covers output-specific variants of this problem.

### Fix 7: Roll back the last update or refresh Windows
If crashes started with a specific Windows update, uninstall it from Update history as a diagnostic test. If the driver tab offers "Roll Back Driver," use it. When every targeted fix fails, use "Reset this PC" keeping your files — it rebuilds the driver stack and system files while preserving data. Persistent crashes across a fresh stack with all outputs affected point to a failing audio codec, which means professional board-level repair. Microsoft's audio diagnostics at Windows support can help document the fault.

## Closing
Windows 10 audio crashes are usually archaeology: layers of old drivers, abandoned enhancement apps, and update damage piled onto a codec that just wants its original driver. A clean OEM reinstall, enhancements stripped, and driver replacement blocked gives the audio stack the fresh start it needs — and keeps it there. On a long-lived Windows 10 install, stability is a maintenance habit: audit your audio stack once or twice a year — check that the OEM driver is still installed, that no new enhancement app has attached itself, and that Device Installation Settings still blocks driver replacement. Before each of Windows 10's remaining cumulative updates, note whether audio is healthy so you can identify the culprit immediately if sound breaks afterward. Uninstall audio utilities you no longer use; every abandoned EQ, virtual cable, or recorder left in the stack is a future conflict. If the laptop is eventually upgraded to Windows 11, do a clean driver pass afterward rather than trusting migrated drivers — the migrated Realtek stack is the single most common source of post-upgrade audio crashes. And keep a USB audio adapter in a drawer: it costs little, bypasses the entire internal audio chain, and turns any future audio crisis into a non-event while you fix the real cause.
