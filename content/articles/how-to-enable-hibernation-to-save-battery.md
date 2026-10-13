---
title: "How to Enable Hibernation to Save Battery in Windows 11"
slug: how-to-enable-hibernation-to-save-battery
date: 2026-09-10
categories: ["battery"]
tags: ["hibernation", "sleep mode", "power settings"]
description: "Sleep still drains your battery overnight. Hibernation uses zero power — here's how to enable it and make Windows 11 use it automatically."
thumbnail: "/images/thumbs/how-to-enable-hibernation-to-save-battery.webp"
faqs:
  - q: "What's the difference between sleep and hibernation?"
    a: "Sleep keeps your session in RAM, which needs constant power — typically draining 1–5% of battery per hour. Hibernation writes everything to disk (hiberfil.sys) and powers off completely, using zero battery. Resume from hibernation takes longer (10–30 seconds) but your work is exactly where you left it."
  - q: "Does hibernation wear out my SSD?"
    a: "Negligibly. Each hibernation writes a few gigabytes once, which is trivial compared to normal daily SSD writes from Windows, browsers, and apps. You'd need to hibernate hundreds of times a day for years to matter."
  - q: "Why is hibernate missing from my power menu?"
    a: "Windows 11 hides it by default on many laptops. It's usually just disabled — run powercfg /hibernate on as administrator and then enable it in the power button settings. On some systems with certain firmware, it can't be enabled at all."
  - q: "Should I use hibernation or shut down?"
    a: "Hibernation for daily use when you'll resume within a day or two — it's faster than a full boot with all apps reopened. Full shutdown for longer storage, before travel, or when troubleshooting, since it clears system state completely."
---
You close the lid at night with 60% battery, open it in the morning, and somehow you're at 41%. That overnight drain is sleep mode doing its job — keeping your RAM powered so everything resumes instantly. Convenient, yes. Free, no.

Hibernation is the better deal for saving battery: it snapshots your entire session to disk and powers the laptop off completely. Zero drain. Open the lid hours or days later and everything is exactly where you left it. Windows 11 often hides the option, but enabling it takes about two minutes — and it's the most effective answer to [fast battery drain](/articles/laptop-battery-drains-fast-windows-11/) that happens while you're not even using the machine.

## Why this happens

- **Sleep keeps RAM powered.** Your open apps, documents, and browser tabs live in memory, and memory needs electricity. That constant draw is what eats 10–20% overnight.
- **Background activity continues in modern sleep.** Windows 11's Modern Standby lets the system do maintenance, check mail, and update apps while "asleep" — useful, but it costs battery. Hibernation stops all of it.
- **Windows 11 hides hibernation by default.** On many laptops the Hibernate option is disabled out of the box, so most people never know it exists and just accept the overnight drain.
- **Fast Startup complicates the picture.** Fast Startup (enabled by default) is a partial hibernation of the kernel at shutdown. It speeds boot but can mask battery issues and occasionally glitches — knowing the difference matters when diagnosing drain.
- **Some firmware blocks hibernation.** A few modern laptops with "Modern Standby only" firmware can't hibernate at all, no matter what you enable in Windows. The fixes below will tell you quickly if yours is one of them.
- **Disk space matters.** Hibernation needs room for hiberfil.sys (roughly 40% of your RAM by default on Windows 11). A nearly-full drive can silently prevent it.

## How to fix it

Work through these in order. The first two enable hibernation; the rest make it automatic and fix common blockers.

### Fix 1: Enable hibernation from an elevated terminal

This is the master switch. Everything else depends on it.

1. Press **Windows key + X** and select **Terminal (Admin)**. Click **Yes** on the UAC prompt.
2. Type `powercfg /hibernate on` and press Enter. There's no confirmation message — silence means success.
3. Verify it worked: run `powercfg /availablesleepstates`. If **Hibernate** appears in the available states list, you're good. If it says it's not available, your firmware likely blocks it — skip to Fix 6.
4. Check disk space while you're here: hibernation needs free space roughly equal to 40% of your RAM. Open **Settings > System > Storage** and make sure you have breathing room.

### Fix 2: Add Hibernate to the power menu

Enabling it isn't enough — you need the button to actually use it.

1. Open **Control Panel > Hardware and Sound > Power Options**, then click **Choose what the power buttons do** in the left sidebar.
2. Click **Change settings that are currently unavailable** at the top (this unlocks the greyed-out options).
3. Under **Shutdown settings**, check the **Hibernate** box. Also check **Show in the power menu** if that option appears.
4. Click **Save changes**. Now **Start > Power** should offer Hibernate alongside Sleep, Shut down, and Restart.

### Fix 3: Make the laptop hibernate automatically

Manual hibernation is nice; automatic hibernation is the real battery saver.

1. Go to **Settings > System > Power & battery > Screen, sleep, & hibernate timeouts**.
2. Set **Put my device to sleep** to something reasonable like 10–15 minutes on battery.
3. For true automatic hibernation, open the classic advanced settings: **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
4. Expand **Sleep > Hibernate after** and set **On battery** to 30–60 minutes. This means: sleep first for quick resumes, then hibernate automatically if you don't come back — the best of both worlds.
5. While you're in there, check **Sleep > Allow hybrid sleep** — on desktops it's useful, but on laptops it can interfere; leaving it off is usually fine.

### Fix 4: Set the lid and power button to hibernate

One habit change that saves the most battery: hibernate on lid close instead of sleep.

1. In **Control Panel > Power Options**, click **Choose what closing the lid does**.
2. Set **When I close the lid** to **Hibernate** for **On battery** (keep **Plugged in** as Sleep or Shut down — your choice, since power is free).
3. Optionally set **When I press the power button** to **Hibernate** for On battery too — faster than opening the Start menu.
4. Click **Save changes** and test it: close the lid on battery, wait a minute, open it. The power light should be fully off (not pulsing), and resume should take 10–30 seconds.

### Fix 5: Fix hibernation that fails or immediately wakes

If enabling it didn't stick, something is blocking it.

1. Run `powercfg /energy` in an elevated Terminal, wait 60 seconds, and read the errors — it flags devices and drivers that prevent low-power states.
2. Check for the usual wake culprits: in **Device Manager**, right-click your network adapter and mouse under their categories, open **Properties > Power Management**, and uncheck **Allow this device to wake the computer** if hibernation keeps getting interrupted.
3. Make sure Fast Startup isn't conflicting: **Control Panel > Power Options > Choose what the power buttons do** — try unchecking **Turn on fast startup**, saving, and testing hibernation again. (Fast Startup causes its own [battery drain issues](/articles/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2/) on some machines, so this doubles as a drain fix.)
4. Update chipset and BIOS drivers from your manufacturer ([Dell](https://www.dell.com/support), [Lenovo](https://support.lenovo.com/us/en/)) — power-state bugs are frequently fixed in firmware updates.

### Fix 6: When hibernation truly isn't available

Some laptops can't do it, and it's better to know than to fight it.

1. If `powercfg /availablesleepstates` shows Hibernate as unavailable even after `powercfg /hibernate on`, your firmware is Modern Standby-only. No Windows setting overrides this.
2. Your best alternative: aggressive sleep timeouts plus **Battery saver** always on. Go to **Settings > System > Power & battery** and set sleep to 5 minutes on battery.
3. Reduce Modern Standby drain: **Settings > System > Power & battery > Battery usage** reveals which apps drain during sleep — restrict background activity for the worst offenders.
4. For overnight or travel, just shut down fully. It's the only true zero-drain option on these machines, and with an SSD, boot takes seconds anyway. Microsoft documents sleep-state behavior on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Reclaim disk space from hiberfil.sys if needed

If you're tight on storage, you can shrink hibernation's footprint instead of disabling it.

1. In an elevated Terminal, run: `powercfg /hibernate /size 50` — this shrinks hiberfil.sys to 50% of RAM (the minimum that still supports full hibernation reliably).
2. Check **Settings > System > Storage** to confirm the freed space.
3. Never set it below 50 or delete the file manually — Windows manages hiberfil.sys, and hand-deleting it just breaks hibernation until you re-enable it.

## Closing

Hibernation is the closest thing to a free lunch in laptop power management: zero battery drain, and your whole session waiting exactly as you left it. Enable it once, set the lid to hibernate on battery, and that mysterious overnight drain becomes a thing of the past — your morning battery percentage will finally match the night before.
