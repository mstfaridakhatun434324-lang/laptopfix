---
title: "How to Fix Sleep and Wake Problems on Your Copilot+ PC"
slug: copilot-plus-pc-sleep-wake-problems
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot+ pc", "sleep", "wake", "windows 11", "troubleshooting", "ai pc"]
description: "Copilot+ PC won't sleep, wakes randomly, or won't wake up? Learn the causes behind sleep and wake problems on AI laptops and fix them step by step today."
thumbnail: "/images/thumbs/copilot-plus-pc-sleep-wake-problems.webp"
faqs:
  - q: "Why does my Copilot+ PC wake up by itself at night?"
    a: "Scheduled tasks, Windows Update, and devices allowed to wake the machine are the usual culprits. Run `powercfg /waketimers` in an admin Terminal to see exactly what is scheduled to wake your laptop, then disable or reschedule the offenders."
  - q: "Is it bad to just close the lid instead of shutting down?"
    a: "Not if sleep works correctly — modern standby is designed for exactly that. But if your laptop runs hot or drains battery in the bag, sleep is broken and you should shut down until it is fixed."
  - q: "Why won't my Copilot+ PC wake from sleep with the keyboard or mouse?"
    a: "The device probably is not allowed to wake the computer, or a driver failed to reinitialize it. In Device Manager, open the device's Power Management tab and enable 'Allow this device to wake the computer.'"
  - q: "Does hibernate work better than sleep on Copilot+ PCs?"
    a: "Often, yes. Hibernate writes memory to disk and powers fully off, sidestepping the driver bugs that plague modern standby. It wakes slower but is far more reliable on machines with immature sleep drivers."
---

You close the lid, slide the laptop into your bag, and an hour later the bag feels warm — the machine never actually slept. Or the opposite: you open the lid and stare at a black screen that refuses to wake, forcing a hard power-button hold. Sleep and wake problems are among the most reported issues on Copilot+ PCs, and they are uniquely frustrating because they strike when you are not even using the machine.

The root of most of it is modern standby. Copilot+ PCs use a phone-like low-power idle state instead of the old S3 sleep, so drivers, firmware, and background tasks must cooperate perfectly — and on new platforms like Snapdragon X and Intel Core Ultra Series 2, that cooperation is still a work in progress. Wake failures also cascade into other symptoms, like docks that stop responding after resume (see [Copilot+ PC Thunderbolt dock not working](/articles/copilot-plus-pc-thunderbolt-dock-not-working/)).

This guide covers the full range: machines that will not sleep, machines that wake on their own, and machines that will not wake up. Work through the fixes in order and you will find which layer is broken.

## Why this happens

- **Modern standby driver bugs:** The low-power idle state depends on every driver entering and exiting sleep cleanly. One misbehaving driver on a new Copilot+ platform can block sleep or crash the resume.
- **Devices allowed to wake the machine:** Network adapters, mice, and scheduled tasks can wake the laptop at 3 AM. Wake-on-LAN left enabled is a classic overnight waker.
- **Fast startup interfering with shutdown:** The hibernated kernel state can carry a broken driver configuration across "shutdowns," making every boot inherit the problem.
- **Lid-close action misconfigured:** Updates sometimes reset the lid-close action to "Do nothing," leaving the machine fully awake in your bag.
- **Firmware bugs on new platforms:** Early BIOS versions on first-wave Copilot+ laptops had sleep-state bugs fixed only by later firmware updates.
- **Background tasks keeping the machine awake:** Windows Update, indexing, and apps with active media or network requests can hold sleep off indefinitely.
- **Driver errors surfacing after resume:** Drivers that fail to reinitialize — graphics, NPU, USB — cause black screens on wake, similar to the [NPU driver error code 43](/articles/npu-driver-error-code-43/) failures some owners see.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find out what is waking or blocking sleep

Windows can tell you exactly what woke the machine last — start with evidence, not guesses.

1. Open Terminal as administrator and run `powercfg /lastwake` to see what caused the most recent wake.
2. Run `powercfg /waketimers` to list scheduled timers that can wake the laptop.
3. Run `powercfg /requests` while the machine refuses to sleep to see which driver or program is holding a power request.
4. In Device Manager, check your network adapter and mouse Properties > Power Management, and uncheck "Allow this device to wake the computer" for anything you do not want waking the machine.
5. In Task Scheduler, find the offending task and uncheck "Wake the computer to run this task" on its Conditions tab.

### Fix 2: Verify the lid and power-button actions

It sounds too simple to be the cause, but updates really do reset these settings.

1. Open Control Panel > Power Options > "Choose what closing the lid does."
2. Set "When I close the lid" to Sleep for both battery and plugged in.
3. Confirm sleep timeouts under Settings > System > Power & battery > "Screen, sleep, & hibernate timeouts."
4. Close the lid for two minutes, open it, and check whether the machine slept — listen for fans and check if it is warm.

### Fix 3: Disable fast startup

Fast startup's hibernated kernel can preserve a broken power state across every shutdown.

1. Open Control Panel > Power Options > "Choose what the power buttons do."
2. Click "Change settings that are currently unavailable."
3. Uncheck "Turn on fast startup" and save changes.
4. Shut down fully (not restart), wait ten seconds, and power on fresh.
5. Test sleep and wake for a day; if problems vanish, leave fast startup off permanently — the boot-time cost on modern SSDs is negligible.

### Fix 4: Update BIOS and chipset drivers

Sleep-state bugs on new platforms are frequently fixed in firmware, not Windows.

1. Check your current BIOS version: press Win + R, type `msinfo32`, and read the BIOS Version/Date line.
2. Visit your laptop maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)) and compare against the latest BIOS for your exact model.
3. Install the BIOS update with the charger plugged in and the battery above 50 percent — never interrupt it.
4. Install the latest chipset and power-management drivers from the same support page.
5. Reboot, then retest lid-close sleep and overnight behavior before changing anything else.

### Fix 5: Switch to hibernate as a reliable workaround

If modern standby keeps misbehaving after driver updates, hibernate gives you dependable sleep today.

1. Open Terminal as administrator and run `powercfg /hibernate on` to make sure hibernate is enabled.
2. Go to Control Panel > Power Options > "Choose what the power buttons do" and check the Hibernate box so it appears in power menus.
3. Set "When I close the lid" to Hibernate instead of Sleep.
4. Optionally set the power button to Hibernate as well for a one-press reliable sleep.
5. Note the tradeoff: waking from hibernate takes longer, but the machine is fully off — no heat, no drain, no mystery wakes.

### Fix 6: Reset the power plan and check for deeper faults

Corrupted power settings or a genuinely broken component are the last things to rule out.

1. Open Terminal as administrator and run `powercfg /restoredefaultschemes` to reset all power plans to defaults.
2. Reboot and retest sleep behavior with default settings before customizing anything.
3. Check Event Viewer > Windows Logs > System for Kernel-Power errors around the times sleep failed — event 41 or 142 entries point at abrupt power loss.
4. Test with all USB peripherals unplugged; a misbehaving dock or dongle can block sleep. Capture-device owners should also check [OBS Studio issues on ARM Windows](/articles/obs-studio-arm-windows-issues/).
5. If sleep still fails on a clean driver set with default plans, contact support — a firmware or board-level fault is possible under warranty.

## Closing

Sleep problems on Copilot+ PCs are almost never one thing — they are the intersection of a new sleep architecture, young drivers, and Windows defaults built for older hardware. The powercfg commands reveal what is actually happening, OEM BIOS and driver updates fix the platform bugs, and hibernate is a respectable fallback while drivers mature. Get sleep reliable and the laptop finally behaves as promised: close the lid, forget it, open to instant-on.
