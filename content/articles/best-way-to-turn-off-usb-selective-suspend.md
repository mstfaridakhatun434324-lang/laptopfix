---
title: "How to Turn Off USB Selective Suspend in Windows"
slug: best-way-to-turn-off-usb-selective-suspend
date: 2026-09-29
categories: ["battery"]
tags: ["usb selective suspend", "power settings", "usb devices", "windows 11"]
description: "USB devices disconnecting or misbehaving on battery? Learn how to disable USB selective suspend in Windows power settings."
thumbnail: "/images/thumbs/best-way-to-turn-off-usb-selective-suspend.webp"
faqs:
  - q: "What is USB selective suspend?"
    a: "It's a Windows power-saving feature that puts individual USB ports into a low-power suspended state when they're not actively in use. This saves battery but can cause USB devices — mice, keyboards, audio interfaces, external drives — to disconnect, lag, or fail to wake up properly."
  - q: "Should I disable USB selective suspend?"
    a: "If your USB devices disconnect randomly, lag after idle, or fail to wake the laptop, yes — disabling it is a safe and common fix. The battery cost is small. If everything works fine, leave it enabled to save a little power."
  - q: "Does disabling USB selective suspend drain the battery faster?"
    a: "Slightly, but the impact is minimal — usually a few percent over a full day. USB ports stay fully powered instead of dozing, which matters far less than your screen brightness or CPU load."
  - q: "Why does my USB device keep disconnecting on battery but not on AC?"
    a: "Because selective suspend is often enabled for the On battery power plan but disabled for Plugged in. Windows aggressively suspends USB ports to save battery, and some devices handle the wake-up poorly. Disabling it for the battery plan fixes the disconnects."
---
Your USB mouse freezes for a second after you stop moving it. Your external drive vanishes mid-transfer. Your audio interface crackles when the laptop idles. If these gremlins only appear on battery power, there's a good chance USB selective suspend is the culprit.

Selective suspend is Windows trying to be helpful — putting idle USB ports to sleep to save battery. The problem is that plenty of USB devices wake up badly, or not at all. Turning it off is a thirty-second fix with almost no downside.

## Why this happens

- **Selective suspend is enabled by default.** Most Windows power plans turn it on for both battery and AC, so it's active unless someone changed it.
- **It's stricter on battery.** The Balanced and Power Saver plans suspend USB ports aggressively when unplugged, which is exactly when devices start acting up.
- **Some devices handle suspend poorly.** Cheap hubs, older peripherals, and finicky audio/MIDI interfaces often fail to renegotiate properly after a suspend.
- **The setting is buried.** It lives several clicks deep in the advanced power options, so most people never know it exists — they just live with the flakiness.
- **Windows updates can re-enable it.** A feature update sometimes resets custom power plan tweaks, bringing the disconnects back.
- **Hubs compound the problem.** A suspend-prone hub can take every device behind it down at once, making it look like a bigger failure.

## How to fix it

Work through these in order — the Control Panel method is the main one.

### Fix 1: Disable it in advanced power settings

This is the definitive fix and covers both power states.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **USB settings**, then **USB selective suspend setting**.
4. Set both **On battery** and **Plugged in** to **Disabled**.
5. Click **Apply**, then **OK**, and restart your laptop.

### Fix 2: Disable it for all power plans

If you switch between plans, cover them all.

1. In **Power Options**, repeat Fix 1's steps for each plan you use (**Balanced**, **Power Saver**, **High Performance**).
2. Alternatively, open an **administrator** Command Prompt and run: `powercfg -SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8fcc84 Disabled` followed by `powercfg -SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8fcc84 Disabled` — AC and DC (battery) respectively.
3. Restart and test your USB devices on battery.

### Fix 3: Stop Windows from powering off individual USB devices

Device Manager has its own per-device power management that stacks with selective suspend.

1. Press **Win + X**, open **Device Manager**, and expand **Universal Serial Bus controllers**.
2. Right-click each **USB Root Hub** (and **Generic USB Hub**), choose **Properties**, and open the **Power Management** tab.
3. Uncheck **Allow the computer to turn off this device to save power**.
4. Click **OK** and repeat for every hub entry, then restart.

### Fix 4: Update USB and chipset drivers

Outdated drivers make suspend/wake behavior worse.

1. Install the latest **chipset drivers** from your laptop maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. In **Device Manager**, check **Universal Serial Bus controllers** for any device with a yellow warning icon and update its driver.
3. Retest the problematic USB device on battery power.

### Fix 5: Test with a direct connection

Rule out the hub as the real problem.

1. Plug the misbehaving device **directly into the laptop**, bypassing any hub or dock.
2. If it behaves, the hub is the weak link — replace it with a **powered hub** (one with its own wall adapter) rather than a bus-powered one.
3. If it still misbehaves directly connected, the device itself may be at fault.

### Fix 6: Check USB power in the BIOS

Some laptops have firmware-level USB power options that override Windows.

1. Restart into **BIOS/UEFI** (usually **F2** or **Del** at boot).
2. Look under **Advanced** or **Power** for USB power-saving or "USB power share" options.
3. Disable aggressive USB power saving, save with **F10**, and exit.

### Fix 7: Weigh the battery tradeoff honestly

Disabling selective suspend costs a little battery — make sure it's worth it.

1. After disabling, monitor drain for a day or two using **Settings > System > Power & battery > Battery usage**.
2. If a specific device was the only problem, consider re-enabling selective suspend and just replacing that one device.
3. For maximum runtime when you don't need peripherals, unplug USB devices entirely — that saves more than selective suspend ever did.

## Closing

USB selective suspend is a classic case of a power-saving feature that costs more in frustration than it saves in battery. If your peripherals misbehave on battery, turning it off is quick, safe, and reversible — and the battery impact is genuinely tiny compared to your display and processor. Keep it disabled for the plans you actually use, and save your troubleshooting energy for the [apps that really drain your battery](/articles/how-to-find-which-app-is-draining-battery/). If you dock and undock frequently, it's also worth checking whether your [background apps are piling up](/articles/how-to-turn-off-background-apps-to-save-battery-in-windows-11-24h2/) — the combination of a wakeful USB stack and dozens of background processes is what turns a mild drain into a dead-by-lunch battery. Fix the peripherals first, then audit the software, and you'll have both stability and runtime.

A final note for dock users: some USB-C docks have their own firmware with independent power management, and a dock running old firmware can suspend its ports no matter what Windows is set to. If disconnects persist after disabling selective suspend everywhere in Windows, check the dock manufacturer's site for a firmware updater — it's a separate step most people never think of, and it resolves a stubborn minority of cases. The same goes for the laptop's USB4/Thunderbolt drivers, which handle port power on modern machines; keep those current alongside the chipset drivers and the whole USB stack behaves far more predictably.
