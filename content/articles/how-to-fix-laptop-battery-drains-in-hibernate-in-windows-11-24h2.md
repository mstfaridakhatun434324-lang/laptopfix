---
title: "How to Fix Laptop Battery Draining in Hibernate on Windows 11 (24H2)"
slug: how-to-fix-laptop-battery-drains-in-hibernate-in-windows-11-24h2
date: 2026-09-15
categories: ["battery"]
tags: ["hibernate", "battery drain", "windows 11 24h2", "sleep study", "power settings"]
description: "Laptop losing battery overnight in hibernate on Windows 11 24H2? Learn why true hibernation isn't kicking in and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-laptop-battery-drains-in-hibernate-in-windows-11-24h2.webp"
faqs:
  - q: "Is it normal for a laptop to lose battery in hibernate?"
    a: "No. True hibernation powers the machine fully off after writing RAM to disk, so drain should be 0-2% overnight. If you're losing 10% or more, the laptop is probably entering Modern Standby sleep instead of hibernating, or something is waking it up."
  - q: "How do I know if my laptop really hibernated?"
    a: "After resuming, check the time it takes to wake and whether apps reload from disk (slower resume means real hibernate). More reliably, run powercfg /sleepstudy in an admin Command Prompt to see which sleep state the machine actually entered and what woke it."
  - q: "Does Windows 11 24H2 change how hibernate works?"
    a: "24H2 didn't remove hibernate, but on many newer laptops the Hibernate option is hidden by default and machines ship with Modern Standby (S0), which keeps the system semi-awake. Updates can also reset your power plan settings, re-enabling wake timers."
  - q: "Can a corrupted hiberfil.sys cause battery drain?"
    a: "Yes. If the hibernation file is damaged, Windows may fail to hibernate and silently fall back to sleep instead. Deleting and recreating it with powercfg /hibernate off followed by powercfg /hibernate on usually resolves this."
---

You close the lid, pick Hibernate, and expect the laptop to be stone cold until morning. Instead you open it to find 15, 25, sometimes 40 percent of the battery gone overnight. That is not how hibernation is supposed to behave.

Hibernate writes everything in RAM to disk and then shuts the machine off completely. In that state the battery should barely move — a percent or two at most, and that's mostly the battery's own natural self-discharge. When you see real drain, something is wrong: either the laptop never actually hibernated, or something woke it back up in the night. Here's how to find out which one it is and fix it.

## Why this happens

- **The laptop is using Modern Standby (S0) instead of real hibernate.** Most new laptops ship with S0 low-power idle, which looks like sleep but keeps the CPU, Wi-Fi, and background apps semi-active. It drains battery like the machine is on.
- **Hibernate is disabled or hidden.** On many Windows 11 machines the Hibernate option doesn't even appear in the power menu until you turn it on manually.
- **The hibernation file (hiberfil.sys) is corrupted.** If Windows can't write RAM to disk, it quietly falls back to sleep — and sleep drains.
- **Wake timers fire overnight.** Scheduled tasks, Windows Update, and maintenance wakes can pull the machine out of hibernation or sleep.
- **USB devices or the network adapter wake the PC.** A mouse jiggle, a network packet, or a dock can wake a "sleeping" laptop.
- **Fast Startup interferes.** Fast Startup uses a partial hibernate on shutdown; when misconfigured it can leave the machine in a half-awake state.
- **A Windows 11 24H2 update reset your power settings.** Feature updates sometimes restore default power plans, re-enabling wake timers and aggressive sleep defaults.

## How to fix it

Work through these in order. Most people find the culprit by Fix 3.

### Fix 1: Confirm hibernate is actually enabled

First, make sure your laptop can hibernate at all.

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Type `powercfg /a` and press Enter. Look for "Hibernate" in the list of available states. If it says hibernate is not available, continue.
3. In the same admin terminal, run `powercfg /hibernate on` and press Enter.
4. Now add Hibernate to the power menu: open **Control Panel → Hardware and Sound → Power Options → Choose what the power buttons do**.
5. Click **Change settings that are currently unavailable**, tick **Hibernate**, and click **Save changes**.

From now on, use **Start → Power → Hibernate** explicitly rather than just closing the lid, at least while testing.

### Fix 2: Check which sleep state your laptop actually entered

Windows keeps a log. Use it instead of guessing.

1. Open **Terminal (Admin)** and run `powercfg /sleepstudy`. This generates an HTML report at `C:\Windows\System32\sleepstudy-report.html`.
2. Open that file in your browser. Look at the last overnight session: the "Sleep State" column tells you whether the machine entered **Hibernate**, **Modern Standby**, or plain **Sleep**.
3. If you see Modern Standby where you expected Hibernate, that's your drain — S0 standby routinely uses several percent per hour.
4. Also run `powercfg /lastwake` in the admin terminal. It names the device or timer that last woke the machine, which is a direct lead for the next fixes.
5. If you regularly find the machine awake in the morning, [check which app is draining battery](/articles/how-can-i-find-which-app-is-draining-battery/) to identify background culprits, and see our guide on [battery drain overnight when the laptop is off](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-after-windows-11-update/) for related causes.

### Fix 3: Disable wake timers on battery

Wake timers are the most common reason a hibernating or sleeping laptop stirs in the night.

1. Open **Control Panel → Hardware and Sound → Power Options** and click **Change plan settings** next to your active plan.
2. Click **Change advanced power settings**.
3. Expand **Sleep → Allow wake timers**.
4. Set **On battery** to **Disable**. Leave **Plugged in** as you like (keeping it enabled on AC is fine).
5. Click **Apply**, then **OK**.
6. For extra certainty, open **Task Scheduler** (search it in Start), browse **Task Scheduler Library → Microsoft → Windows → UpdateOrchestrator**, right-click tasks like **Reboot**, choose **Properties → Conditions**, and untick **Wake the computer to run this task**.

### Fix 4: Turn off Fast Startup

Fast Startup can leave the system in a strange half-hibernated state that never fully powers down.

1. Go to **Control Panel → Hardware and Sound → Power Options → Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Untick **Turn on fast startup (recommended)**.
4. Click **Save changes** and restart the laptop once normally.

You may notice shutdown takes a few seconds longer. That's the price of a genuinely powered-off machine — and it's worth it for the test.

### Fix 5: Stop devices from waking the laptop

A network adapter that wakes on any packet, or a sensitive USB mouse, can undo hibernation.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Network adapters**, right-click your Wi-Fi adapter, and choose **Properties**.
3. Go to the **Power Management** tab and untick **Allow this device to wake the computer**. Click **OK**.
4. Expand **Mice and other pointing devices** and **Keyboards**, and do the same for external mice/keyboards you don't need as wake sources.
5. Expand **Universal Serial Bus controllers**, right-click each **USB Root Hub**, choose **Properties → Power Management**, and untick **Allow this device to wake the computer** for hubs that don't need it.
6. If you'd rather see exactly which device is allowed to wake the PC, run `powercfg /devicequery wake_armed` in an admin terminal — it lists every armed wake device.

### Fix 6: Rebuild the hibernation file

If `powercfg /a` claims hibernate works but the machine still won't stay off, the hibernation file itself may be damaged.

1. Open **Terminal (Admin)**.
2. Run `powercfg /hibernate off` and press Enter. This deletes `hiberfil.sys`.
3. Restart the laptop.
4. Open **Terminal (Admin)** again and run `powercfg /hibernate on`.
5. Hibernate the machine overnight and check the battery in the morning. A fresh hibernation file fixes the silent fallback-to-sleep problem in most cases.

### Fix 7: Update the BIOS, chipset drivers, and Windows

Power-state bugs are frequently fixed in firmware updates, and 24H2-era machines have seen several.

1. Go to **Settings → Windows Update** and install every pending update, then restart.
2. Visit your laptop maker's support site and install the latest **BIOS** and **chipset** drivers for your exact model. Microsoft's own guidance on keeping drivers current is at [Windows support](https://support.microsoft.com/en-us/windows).
3. After updating, re-check **Power Options → Change advanced power settings**, since BIOS and feature updates can reset wake-timer and sleep settings to defaults.
4. Hibernate overnight one more time and compare the drain.

## Closing

Hibernate drain almost always comes down to one of two things: the machine never truly hibernated, or something woke it up. Work the list from the top, verify with `powercfg /sleepstudy`, and your overnight drain should drop back to the 0-2 percent that real hibernation delivers.
