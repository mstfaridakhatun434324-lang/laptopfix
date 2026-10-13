---
title: "How to Turn Off USB Selective Suspend on a Laptop"
slug: how-to-turn-off-usb-selective-suspend-on-laptop
date: 2026-09-07
categories: ["battery"]
tags: ["usb selective suspend", "usb power", "device disconnects"]
description: "USB devices randomly disconnecting or misbehaving on battery? USB selective suspend is often the culprit. Here is how to turn it off properly."
thumbnail: "/images/thumbs/how-to-turn-off-usb-selective-suspend-on-laptop.webp"
faqs:
  - q: "What is USB selective suspend?"
    a: "It is a Windows power-saving feature that puts individual USB ports into a low-power state when they appear idle. This saves a small amount of battery but can cause external drives, audio interfaces, and other USB devices to disconnect, lag, or fail to wake properly."
  - q: "Should I disable USB selective suspend?"
    a: "If your USB devices disconnect randomly, stutter, or fail to wake from sleep, yes. The power savings are tiny on modern laptops, while the stability problems are real. Gamers, musicians with USB audio interfaces, and anyone with flaky external drives should turn it off."
  - q: "Does disabling USB selective suspend hurt battery life?"
    a: "Barely. The feature saves only a small amount of power per port. On a modern laptop the difference is a few minutes at most over a full charge. The stability gain for external devices is worth far more than the negligible battery cost."
  - q: "Why does the setting keep turning itself back on?"
    a: "Some manufacturer power utilities and Windows updates reset power plan settings to defaults. If selective suspend keeps re-enabling, check your manufacturer's app for USB power options, and reapply the setting after major Windows updates."
---

Your external drive vanishes mid-transfer. Your USB headset crackles, then goes silent. Your mouse freezes for a second every few minutes. You replug, it works, then it happens again. Nine times out of ten on a laptop, the villain is a well-meaning power feature called USB selective suspend.

Windows puts "idle" USB ports to sleep to save a trickle of battery. The problem is that Windows is not always a good judge of idle, and many devices do not wake up gracefully. Turning it off costs almost nothing in battery life and fixes an entire category of flakiness.

## Why this happens

- **Aggressive power saving:** Selective suspend powers down ports Windows thinks are idle, cutting the device off mid-task.
- **Devices that sleep badly:** Many USB audio interfaces, drives, and dongles do not implement suspend and resume cleanly.
- **Enabled by default:** The setting is on in the Balanced plan on most laptops, so most users have it without knowing.
- **Separate battery and plugged-in values:** It can be off when plugged in but on when on battery, so problems appear only unplugged.
- **Plan resets:** Windows updates and manufacturer utilities can silently re-enable it.
- **Hub compounding:** The issue gets worse through USB hubs, where one suspended port can affect everything downstream.

## How to fix it

Work through these in order. The main switch is Fix 1; the rest cover the places it hides.

### Fix 1: Disable it in advanced power settings

1. Open **Control Panel** > **Hardware and Sound** > **Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **USB settings** > **USB selective suspend setting**.
4. Set both **On battery** and **Plugged in** to **Disabled**.
5. Click **Apply**, then **OK**. Test your USB devices for a day.

### Fix 2: Stop Windows from powering off individual devices

1. Press **Win + X** and open **Device Manager**.
2. Expand **Universal Serial Bus controllers**.
3. For each **USB Root Hub** and **Generic USB Hub**, right-click, choose **Properties**, and open the **Power Management** tab.
4. Uncheck **Allow the computer to turn off this device to save power**.
5. Click **OK** on each one. This stops per-device power cuts that selective suspend misses.

### Fix 3: Fix USB devices that fail to wake from sleep

1. In **Device Manager**, expand **Universal Serial Bus controllers** and find your USB host controllers.
2. Open **Properties** > **Power Management** on each and uncheck the power-saving box as in Fix 2.
3. If a specific device like a headset keeps dropping after sleep, also check its own entry under **Sound, video and game controllers** or **Human Interface Devices**.
4. If sleep itself is draining the battery oddly, see [laptop battery drains in sleep mode](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-on-windows-11/).

### Fix 4: Check your manufacturer's power utility

1. Open **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, or your HP utility.
2. Look for USB power, always-on USB, or USB charging settings.
3. Some of these utilities override Windows' selective suspend with their own logic. Align them with your choice.
4. If the utility has a USB always-on or charging port feature, decide whether you want it; it keeps ports powered even when the laptop sleeps.

### Fix 5: Update USB and chipset drivers

1. In **Device Manager**, right-click each USB host controller and choose **Update driver** > **Search automatically for drivers**.
2. Install the latest chipset driver package from your manufacturer's support site.
3. USB stability fixes frequently ship inside chipset driver updates.
4. Restart after installing and retest the problematic devices.

### Fix 6: Test without hubs and with different ports

1. Plug the misbehaving device directly into the laptop, bypassing any hub or dock.
2. Try different USB ports. On many laptops, ports on opposite sides hang off different controllers with different behavior.
3. If the device is stable direct-connected but flaky through the hub, the hub's own power management is the problem.
4. Use a powered hub for power-hungry devices like external drives.

### Fix 7: Reapply after Windows updates

1. After each major Windows update, revisit **Power Options** > **Change advanced power settings** and confirm selective suspend is still disabled.
2. Consider exporting your power scheme with `powercfg /export` so you can restore it quickly.
3. If a manufacturer utility keeps fighting you, check its settings for a USB power option to disable there too.
4. For related power-drain tuning, see [disabling fast startup](/articles/how-to-disable-fast-startup-to-fix-battery-drain-on-windows-11/).

### Fix 8: Disable it from the command line for all power plans

The GUI only changes the active plan. The command line fixes every plan at once.

1. Open an elevated Terminal (**Win + X** > **Terminal (Admin)**).
2. First list your power schemes with `powercfg /list` and note the GUID of each plan you use.
3. For each plan, run `powercfg /setacvalueindex <GUID> 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8fcc84 0` to disable selective suspend on AC.
4. Run the same with `/setdcvalueindex` instead of `/setacvalueindex` to disable it on battery.
5. Activate the changes with `powercfg /setactive <GUID>` for your current plan.
6. Verify with `powercfg /query` and check the USB settings section shows the disabled state.
7. This survives plan switches, which the GUI method does not, and it is scriptable if you manage multiple machines.

## Closing

USB selective suspend is a textbook case of a power feature whose savings do not justify its side effects. The few minutes of battery it saves per charge are invisible in real use, while the disconnects, audio dropouts, and failed wake-ups it causes are impossible to ignore. Turning it off in the advanced power plan settings fixes the common case, unchecking the per-device power management boxes in Device Manager catches the cases the plan setting misses, and the command-line approach locks it down across every power plan so a plan switch cannot reintroduce the problem. Testing without hubs and updating chipset drivers covers the hardware side, and reapplying after Windows updates handles the setting's habit of resurrecting itself. If you ever want the tiny savings back, you now know exactly where the switch lives and what it costs. For most laptop owners, though, leaving it permanently disabled is one of the highest sanity-per-click changes in Windows power management.
