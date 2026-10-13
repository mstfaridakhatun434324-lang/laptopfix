---
title: "How to Turn Off USB Selective Suspend in Windows 11"
slug: how-can-i-turn-off-usb-selective-suspend
date: 2026-09-27
categories: ["battery"]
tags: ["usb selective suspend", "power settings", "usb issues"]
description: "USB devices randomly disconnecting or misbehaving? Turning off USB selective suspend often fixes it — here's how, plus when to leave it on."
thumbnail: "/images/thumbs/how-can-i-turn-off-usb-selective-suspend.webp"
faqs:
  - q: "What is USB selective suspend?"
    a: "A Windows power-saving feature that puts individual USB ports into a low-power state when they're idle. It saves a small amount of battery but can cause disconnects, lag, or devices that won't wake up properly."
  - q: "Will turning it off drain my battery faster?"
    a: "Slightly — USB ports stay fully powered instead of sleeping. The impact is small (typically a few percent over a full battery cycle) unless you have many power-hungry USB devices connected."
  - q: "Why do my USB devices keep disconnecting?"
    a: "Selective suspend is a prime suspect: Windows puts the port to sleep and the device doesn't wake cleanly. Other causes include loose cables, underpowered hubs, and outdated USB controller drivers."
  - q: "Should I disable it on battery, plugged in, or both?"
    a: "If a device misbehaves, disable it for both to fully rule it out. Once the problem is solved, you can re-enable it for battery mode to reclaim the small power saving — if the device tolerates it."
---
Your USB headset crackles, your external drive randomly disconnects, or your mouse freezes for a second every few minutes — and it only happens on your laptop, never your desktop. Before you blame the device, blame the power management: Windows is probably putting your USB ports to sleep.

That feature is called USB selective suspend. It's meant to save battery by idling unused USB ports, but plenty of devices don't wake up gracefully — especially audio interfaces, external drives, and older peripherals. Turning it off is a two-minute change that fixes a whole category of flaky-USB complaints.

## Why this happens

- **Selective suspend powers down idle USB ports.** When Windows thinks a port isn't busy, it suspends it to save power. Well-behaved devices resume instantly; many real-world devices don't.
- **It's enabled by default on battery power.** Windows 11 turns it on for the On battery power plan out of the box, which is why problems appear on laptops and vanish when plugged in (or on desktops).
- **Some devices never wake cleanly.** External hard drives may spin down and not spin back up, USB audio devices develop crackling, and wireless dongles drop connections — all classic suspend/wake failures.
- **The setting is buried.** It lives in the advanced power plan settings, three dialogs deep, which is why most people suffer the symptoms for months without knowing the cause exists.
- **Hubs multiply the problem.** An unpowered USB hub with several devices is more likely to hit suspend issues, because the hub itself may suspend and take everything downstream with it.
- **Driver updates can change the behavior.** A USB controller driver update can alter suspend timing, which is why a device that worked fine for a year suddenly starts disconnecting after an update.

## How to fix it

Work through these in order. The main setting is Fix 1; the rest handle stubborn cases.

### Fix 1: Disable USB selective suspend in power settings

The core fix — do this first.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Next to your active plan, click **Change plan settings**, then **Change advanced power settings**.
3. In the list, expand **USB settings**, then expand **USB selective suspend setting**.
4. Set both **On battery** and **Plugged in** to **Disabled**.
5. Click **Apply**, then **OK**. Test your USB devices for a day — disconnects, crackling, and wake failures caused by suspend should be gone.

### Fix 2: Disable it for all power plans

The setting is per-plan, and Windows can switch plans on you.

1. In the same **Advanced power settings** dialog, use the dropdown at the top to switch to each power plan (**Balanced**, **Best power efficiency**, **Best performance**, and any custom plans).
2. For each plan, expand **USB settings > USB selective suspend setting** and set both **On battery** and **Plugged in** to **Disabled**.
3. Click **Apply** for each plan before switching to the next — the dialog doesn't auto-save when you change the dropdown.
4. This matters because Windows sometimes switches plans silently (plugging/unplugging, manufacturer utilities), and a plan you forgot about can reintroduce the problem.

### Fix 3: Stop individual devices from being powered down

Device-level power management can suspend devices even with the global setting off.

1. Open **Device Manager** (**Windows key + X > Device Manager**) and expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub** (and **Generic USB Hub**), right-click → **Properties** → **Power Management** tab.
3. Uncheck **Allow the computer to turn off this device to save power**. Click **OK**.
4. Do the same for the specific problematic device if it appears under its own category (e.g., your headset under **Audio inputs and outputs**, or the drive under **Disk drives**). Not every device exposes this tab — that's fine, the hub-level change covers most cases.

### Fix 4: Update USB controller drivers

Buggy suspend behavior is often just buggy drivers.

1. In **Device Manager > Universal Serial Bus controllers**, right-click each **USB Root Hub** and **USB Host Controller** entry and choose **Update driver > Search automatically for drivers**.
2. Better: get the chipset driver package from your laptop manufacturer's support page — [Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en/) — since USB controllers hang off the chipset.
3. For AMD or Intel-based laptops, the chipset driver package from your manufacturer covers USB controllers too — no separate download needed.
4. Restart after updating and retest the problematic devices.

### Fix 5: Use a powered hub for hungry devices

Sometimes the issue isn't suspend — it's power delivery.

1. If the disconnecting device is a spinning external hard drive, audio interface, or anything with its own power demands, connect it through a **powered** USB hub (one with its own wall adapter).
2. Unpowered hubs split the port's limited power budget across everything plugged in; suspend makes a marginal power situation worse.
3. Retest with the powered hub and selective suspend still disabled. If disconnects stop, power — not just suspend — was part of the problem.
4. For drives specifically, also check **Device Manager > Disk drives > [your drive] > Properties > Policies** — the write-caching policy interacts with surprise removals.

### Fix 6: Test whether you even need it off

Don't leave power savings disabled forever without checking.

1. After a week of stable USB behavior with suspend disabled, note your typical battery life.
2. Re-enable selective suspend for **On battery** only (leave **Plugged in** disabled), and use the laptop normally for a few days.
3. If the USB problems return, you have your answer: your devices genuinely can't handle suspend, and leaving it off costs you only a small amount of battery. That's a fine trade.
4. If everything stays stable, keep the battery-mode saving — free battery life with no downside. Either way, you've made the decision with data instead of guessing. For broader battery savings that don't involve USB at all, our [battery drain guide](/articles/laptop-battery-drains-fast-windows-11/) covers the big wins.

## Closing

USB selective suspend is a good idea that fails on contact with real hardware — the power it saves is tiny, and the disconnects it causes are maddening. Turn it off, fix the per-device power management too, and your USB devices will just work. If you later find your specific devices tolerate it, re-enable the battery-mode saving and pocket the difference. If your USB-C port won't charge at all — not just disconnect devices — that's a different problem covered in our [USB-C charging guide](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-in-windows-11-24h2/).
