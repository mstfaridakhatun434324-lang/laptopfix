---
title: "How to Turn Off USB Selective Suspend on Windows 11"
slug: how-to-turn-off-usb-selective-suspend-on-windows-11
date: 2026-09-10
categories: ["battery"]
tags: ["usb selective suspend", "windows 11 power settings", "usb keeps disconnecting"]
description: "USB mouse, drive, or headset keeps dropping out on Windows 11? Here's how to turn off USB selective suspend and stop random disconnects for good."
thumbnail: "/images/thumbs/how-to-turn-off-usb-selective-suspend-on-windows-11.webp"
faqs:
  - q: "What does USB selective suspend do on Windows 11?"
    a: "It lets Windows put individual USB ports into a low-power state when the connected device looks idle. That saves a small amount of battery, but buggy drivers or devices that misreport their idle state get suspended while you're actively using them, which causes dropouts, lag, and devices that vanish from Device Manager until you unplug and replug them."
  - q: "Will turning off USB selective suspend hurt battery life?"
    a: "Barely. The setting saves only a tiny amount of power on a modern laptop — typically a few minutes of runtime at most — because USB controllers already manage idle power efficiently. Unless you're squeezing every last minute out of a nearly dead battery, disabling it is a safe trade for stable USB devices."
  - q: "I turned it off but my USB drive still disconnects. What next?"
    a: "Turn off per-device power management on each USB Root Hub in Device Manager, update your chipset drivers from the laptop maker, and try a different port — front-panel ports and unpowered hubs are the usual suspects. If the disconnects happen only on battery power, your power plan may still be throttling the controller."
  - q: "Should I disable it for On battery, Plugged in, or both?"
    a: "Disable it for both. Selective suspend is most aggressive on battery power, but driver quirks can suspend devices on AC power too. Changing both entries in Advanced Power Settings takes ten seconds and rules the setting out completely as a cause."
---

Your external hard drive vanishes mid-transfer, your USB headset crackles and reconnects, or your mouse freezes for a second every few minutes. On Windows 11, one of the most common culprits is a power-saving feature called USB selective suspend, and it's buried deep enough that most people never know it exists.

The good news is that turning it off takes about a minute, and it fixes an outsized share of mysterious USB problems on laptops. The setting is per power plan, though, so you need to change it everywhere it matters — and a couple of related Device Manager toggles can undo your fix if you skip them.

## Why this happens

- **Selective suspend puts "idle" USB ports to sleep.** Windows monitors each USB device and suspends the port when the device appears idle. Some devices never wake cleanly, so they drop, stutter, or disappear.
- **It's enabled by default on battery power.** Most Windows 11 power plans enable selective suspend for the On battery profile, which is why disconnects often start the moment you unplug the charger.
- **Drivers misreport device state.** Older or generic USB controller drivers tell Windows a device is idle when it isn't, so an active webcam, audio interface, or external SSD gets suspended mid-use.
- **Per-device power management stacks on top.** Even with selective suspend off, the **Allow the computer to turn off this device to save power** checkbox on USB Root Hubs can power down the same ports independently.
- **Underpowered ports and hubs amplify it.** A port that can't deliver stable current makes a device look unresponsive, Windows suspends the port "to save power," and the device never recovers until replugged.
- **Firmware and chipset drivers lag behind.** Laptop makers regularly fix USB power-handling bugs in BIOS and chipset updates that Windows Update never delivers on its own.

## How to fix it

Work through these in order — most people are fixed by Fix 1 and Fix 3.

### Fix 1: Disable USB selective suspend in Advanced Power Settings

This is the main switch. Do it for every power plan you use.

1. Press **Win + R**, type `control`, and press **Enter** to open the Control Panel.
2. Go to **Hardware and Sound > Power Options**.
3. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
4. Expand **USB settings**, then expand **USB selective suspend setting**.
5. Set **On battery** to **Disabled** and **Plugged in** to **Disabled**.
6. Click **Apply**, then **OK**.
7. Repeat steps 3–6 for every other plan listed (Balanced, Power saver, and any manufacturer plan) so the setting can't sneak back when Windows switches profiles.

### Fix 2: Stop Windows from switching plans behind your back

Windows 11 sometimes jumps between power modes when you plug or unplug the charger, which can re-enable aggressive USB power saving.

1. Open **Settings > System > Power & battery**.
2. Under **Power mode**, note which mode is active on battery versus plugged in.
3. Open **Control Panel > Hardware and Sound > Power Options** and confirm the selected plan matches what you edited in Fix 1.
4. If you use a manufacturer utility (Lenovo Vantage, MyASUS, Dell Power Manager), check its power profile too — these can override Windows' plan silently.
5. If USB trouble only strikes on battery, [check your battery's health](/articles/how-to-check-battery-health-on-windows-11-laptop/) as well, since a worn battery makes Windows lean harder on every power-saving trick it has.

### Fix 3: Disable per-device power management on USB hubs

This is the second switch that undoes Fix 1 if left on.

1. Press **Win + X** and choose **Device Manager**.
2. Expand **Universal Serial Bus controllers**.
3. Right-click each **USB Root Hub** (and **USB Root Hub (USB 3.0)**) entry, choose **Properties**, and open the **Power Management** tab.
4. Uncheck **Allow the computer to turn off this device to save power**.
5. Click **OK** and repeat for every USB Root Hub and **Generic USB Hub** entry in the list.
6. Restart the laptop so the new power policy applies to already-connected devices.

### Fix 4: Update chipset and USB controller drivers

Stale controller drivers are the reason selective suspend misbehaves in the first place.

1. In **Device Manager**, expand **Universal Serial Bus controllers**, right-click the **USB xHCI Compliant Host Controller**, and choose **Update driver > Search automatically for drivers**.
2. Visit your laptop maker's support site — [Dell](https://www.dell.com/support) or [HP](https://support.hp.com/us-en) — enter your exact model, and install the latest **chipset** driver package.
3. Intel-based laptops can also use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to catch chipset updates Windows misses.
4. Check your BIOS version against the maker's support page; USB power-handling fixes frequently ship in BIOS updates.
5. Restart after installing, then re-verify the Fix 1 setting — a driver reinstall occasionally resets power plan defaults.

### Fix 5: Rule out the port, cable, and hub

1. Plug the problem device directly into the laptop, bypassing any dock or hub.
2. Try a different USB port — ports on opposite sides of the laptop often sit on different controllers.
3. Swap the cable; charge-only or damaged USB-C cables cause exactly the flaky behavior selective suspend gets blamed for.
4. If you must use a hub, use a **powered** hub with its own AC adapter so the device never browns out.
5. If disconnects only happen on battery, generate a [battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/) — a battery that can't hold voltage under load makes USB instability worse.

### Fix 6: Run the hardware troubleshooter

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **USB** troubleshooter if listed (on some builds it's under **Hardware and Devices** via `msdt.exe -id DeviceDiagnostic`).
3. Apply any recommended fixes and restart.
4. Alternatively, reset the plan to defaults and redo Fix 1: in an elevated Command Prompt, run `powercfg -restoredefaultschemes`, then disable selective suspend again.

### Fix 7: Check for device-specific firmware

1. External SSDs, docks, and audio interfaces often have their own firmware updaters on the manufacturer's site — install any that apply.
2. In **Device Manager**, check the problem device's **Properties > Events** tab for repeated surprise-removal entries, which confirm power-related disconnects rather than a dead device.
3. As a last resort, uninstall the device in Device Manager (check **Attempt to remove the driver** only if you have the driver installer handy), unplug it, restart, and let Windows reinstall fresh.

## Closing

USB selective suspend is one of those features that works fine in theory and causes real grief in practice, especially on laptops where power plans change constantly. Disable it in every power plan, uncheck the per-hub power management boxes, and keep your chipset drivers current — that combination ends the random-disconnect saga for the vast majority of Windows 11 laptops.
