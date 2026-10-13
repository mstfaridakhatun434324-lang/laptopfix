---
title: "How to Turn Off USB Selective Suspend in Windows 10"
slug: how-to-turn-off-usb-selective-suspend-on-windows-10
date: 2026-09-04
categories: ["battery"]
tags: ["USB selective suspend", "Windows 10", "power settings", "USB devices"]
description: "USB devices disconnecting or misbehaving on battery? Learn how to disable USB selective suspend in Windows 10 step by step."
thumbnail: "/images/thumbs/how-to-turn-off-usb-selective-suspend-on-windows-10.webp"
faqs:
  - q: "What is USB selective suspend?"
    a: "It's a Windows power-saving feature that puts individual USB ports into a low-power suspended state when they're not actively in use. This saves battery but can cause USB devices — external drives, audio interfaces, headsets — to disconnect, lag, or fail to wake properly."
  - q: "Should I turn off USB selective suspend?"
    a: "Turn it off if USB devices disconnect randomly, take seconds to respond after idle, or fail on battery power but work fine plugged in. The battery cost of disabling it is small on most laptops. Leave it on if all your USB devices behave and you want maximum battery life."
  - q: "Where is the USB selective suspend setting in Windows 10?"
    a: "It's in the advanced power plan settings: Control Panel > Hardware and Sound > Power Options > Change plan settings > Change advanced power settings > USB settings > USB selective suspend setting. Set it to Disabled for both On battery and Plugged in."
  - q: "Does disabling USB selective suspend drain the battery faster?"
    a: "Slightly — USB ports stay fully powered instead of dozing between uses. In practice the difference is a few percent over a full day for most people, because the ports still enter low-power states with the system. The tradeoff is worth it if suspend is breaking your devices."
---

USB selective suspend is one of Windows 10's quieter power-saving features: when a USB device goes idle, Windows puts its port to sleep. On paper, great for battery life. In practice, it's behind a whole category of maddening issues — mice that take two seconds to wake, external drives that vanish mid-transfer, audio interfaces that crackle, and headsets that disconnect on battery power.

If your USB devices misbehave specifically when unplugged — the mouse that takes two seconds to wake, the external drive that vanishes mid-transfer — selective suspend is suspect number one. It's also a prime suspect when a USB audio interface crackles on battery but sounds perfect on AC power. Here's how to turn it off, from the simple Control Panel toggle to per-device and command-line methods.

## Why this happens

- **Aggressive power saving:** Windows suspends idle USB ports to save milliwatts, but many devices don't resume cleanly.
- **Battery vs plugged-in behavior:** The setting can differ between power states, so devices work fine on AC but fail on battery.
- **Old or cheap device firmware:** Many peripherals implement USB suspend incorrectly and never wake properly.
- **Driver conflicts:** USB host controller drivers that mishandle the suspend/resume handshake cause disconnect loops.
- **Hub multiplication:** The problem compounds through USB hubs and docks, where one suspended port can take down everything downstream.
- **Selective suspend vs. system sleep:** Don't confuse this with the laptop sleeping — selective suspend acts on individual idle ports while you're actively using the machine.

## How to fix it

### Fix 1: Disable it in advanced power settings

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** next to your active power plan.
3. Click **Change advanced power settings**.
4. Expand **USB settings**, then expand **USB selective suspend setting**.
5. Set both **On battery** and **Plugged in** to **Disabled**.
6. Click **Apply**, then **OK**. Test your USB devices on battery power.

### Fix 2: Disable it for the current plan only (quick test)

1. If you don't want a permanent change yet, create a test: duplicate your power plan first via **Create a power plan** in Power Options.
2. Disable selective suspend only on the duplicate plan.
3. Switch between plans to compare device behavior and battery impact.
4. This tells you definitively whether selective suspend is your culprit before committing.

### Fix 3: Disable it via Device Manager per device

1. Open **Device Manager** and expand **Universal Serial Bus controllers**.
2. Right-click each **USB Root Hub** and choose **Properties > Power Management**.
3. Uncheck **Allow the computer to turn off this device to save power**.
4. Repeat for every USB Root Hub entry — missing one leaves the problem half-fixed.
5. This is more granular than Fix 1 and useful when you only distrust specific ports.

### Fix 4: Update USB controller drivers

1. In **Device Manager**, expand **Universal Serial Bus controllers**.
2. Right-click the **USB host controller** entries and choose **Update driver > Search automatically for drivers**.
3. Then install your manufacturer's **chipset drivers** from their support site — these contain the definitive USB controller drivers.
4. Updated controllers handle suspend/resume far more reliably even with the setting left on.

### Fix 5: Check the specific misbehaving device

1. If only one device fails, test it on another computer to rule out a dying peripheral.
2. Check the manufacturer's site for a firmware update for the device itself — many USB audio and storage devices got suspend-related firmware fixes.
3. Try a different USB port: ports wired directly to the motherboard behave better than hub-connected ones.
4. For external drives, ensure they have adequate power — bus-powered drives on suspended ports are the classic failure.

### Fix 6: Adjust the USB hub power management

1. In **Device Manager**, expand **Universal Serial Bus controllers** and open each **Generic USB Hub > Properties > Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power** on hubs too.
3. If you use a docking station, check its own power settings in the manufacturer's utility.
4. Docks with their own power supplies are far less affected — the dock keeps ports alive independently.

### Fix 7: Verify the fix and measure battery impact

1. Run your normal workload on battery for a day with selective suspend disabled.
2. Confirm the USB problems are gone — no disconnects, no wake lag.
3. Compare battery life to before: most users notice little to no difference, since USB suspend savings are modest next to the display and CPU.
4. If battery life drops noticeably and USB was fine, re-enable the setting — it wasn't your problem. Our guide to [finding which app drains your battery](/articles/how-to-find-which-app-is-draining-battery-on-laptop/) can help hunt the real drain.

### Fix 8: Disable it via Command Prompt

1. Open **Command Prompt as administrator**.
2. To disable for battery mode, run: `powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3a 48e6b7a6a-50f5-4782-a5d4-53bb8f07e226 0`
3. To disable for plugged-in mode, run: `powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3a 48e6b7a6a-50f5-4782-a5d4-53bb8f07e226 0`
4. Run `powercfg /S SCHEME_CURRENT` to apply the scheme immediately.
5. This sets the same option as Fix 1 — useful for scripting across multiple machines or when the Control Panel UI is locked by policy.

## Closing

USB selective suspend is a classic tradeoff feature: tiny battery savings in exchange for occasional device weirdness. When your peripherals work on AC but flake on battery, disabling it is a two-minute fix with minimal downside — and now you know the command-line version too, which is handy if you manage several machines. Keep it off if it solves your problem: the few percent of battery it costs is cheaper than a corrupted file transfer or a dropped call. And if the issues persist with suspend disabled, the device or its driver is the real problem, not the power setting.

Microsoft documents USB power management at the [Windows support hub](https://support.microsoft.com/en-us/windows). For broader sleep-related drain issues, see [troubleshooting laptop battery drain in sleep mode](/articles/laptop-battery-drains-in-sleep-mode-troubleshooting/).
