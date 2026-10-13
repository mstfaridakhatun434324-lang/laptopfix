---
title: "Disable Fast Startup to Fix Battery Drain on Windows 11: The Complete Guide"
slug: how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2
date: 2026-09-06
categories: ["battery"]
tags: ["fast startup", "battery drain", "power options", "hybrid shutdown"]
description: "Fast Startup keeps your laptop half-awake and draining battery. Learn what it does, when to disable it, and how to turn it off properly."
thumbnail: "/images/thumbs/how-to-disable-fast-startup-to-fix-battery-drain-in-windows-11-24h2.webp"
faqs:
  - q: "What is Fast Startup in Windows 11?"
    a: "It's a hybrid shutdown: instead of fully powering off, Windows saves the kernel session to disk (like hibernation) and shuts down user sessions. Booting restores that session, which is faster — but hardware stays in low-power states instead of truly off, and those states sip battery."
  - q: "Will disabling Fast Startup slow down my laptop?"
    a: "Boot takes a few seconds longer — barely noticeable on an SSD, more so on a spinning hard drive. Once booted, there's zero performance difference. The tradeoff is almost always worth it if you're fighting battery drain."
  - q: "Does Fast Startup really drain the battery?"
    a: "Yes, measurably. With Fast Startup on, USB ports can stay powered, network adapters stay half-awake, and the cached device state can preserve glitches. Users commonly report 5–15% overnight loss with it on versus 1–2% with it off."
  - q: "Is it safe to turn off Fast Startup?"
    a: "Completely. It's a convenience feature, not a requirement. Microsoft includes the toggle precisely because some hardware and some users are better off without it. Nothing breaks — shutdowns just become genuine shutdowns."
---

Fast Startup sounds like a pure win: faster boots, no downside mentioned anywhere in the interface. But that speed comes from a trick — your laptop never fully turns off. It hibernates the core of Windows while pretending to shut down, leaving hardware in twilight states that draw power all night, every night. If your battery melts away overnight while the laptop is "off," this one checkbox is the most likely reason — and the fix takes about ninety seconds.

This guide explains what Fast Startup actually does, how to disable it properly on Windows 11 24H2 (including when the checkbox is greyed out), and what to do when disabling it doesn't fully solve the drain. It's also the key step in the broader [overnight drain](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-11/) fix.

## Why this happens

- **Hybrid shutdown keeps devices powered.** Fast Startup saves the kernel to hiberfil.sys and leaves hardware in S4/S5-adjacent low states rather than cutting power.
- **USB ports stay live.** Many laptops keep USB power on through Fast Startup shutdowns, draining the battery if anything is connected.
- **Network adapters stay half-awake.** Wake-on-LAN and connected standby behaviors persist through hybrid shutdown.
- **Cached device states preserve glitches.** If a driver was misbehaving at shutdown, Fast Startup faithfully restores the misbehavior at every boot.
- **The 24H2 update re-enables it.** Feature updates frequently reset this setting to Microsoft's default (on), reintroducing drain users had previously fixed.
- **Hiberfil.sys corruption.** A damaged hibernation file can cause restless pseudo-shutdowns that drain far more than a clean hybrid shutdown would.
- **Dual-boot complications.** Fast Startup locks the NTFS partitions, which is a separate headache for dual-boot users — another reason to disable it.
- **Encrypted-drive quirks.** On some BitLocker setups, hybrid shutdown can cause extra unlock prompts or slow resume; a true shutdown avoids the ambiguity entirely.

## How to fix it

Work through these in order.

### Fix 1: Disable Fast Startup in Power Options

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable** at the top (requires admin).
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**.
6. Shut down fully (not restart) and power back on — the first genuine cold boot in a while. Notice the slightly longer boot: that's the sound of honesty.

### Fix 2: Disable it via Command Prompt (when the checkbox is greyed out)

1. Open **Terminal (Admin)** from **Win + X**.
2. Run `powercfg /h off` — this disables hibernation entirely, which also disables Fast Startup (it depends on the hibernation file).
3. Restart the laptop.
4. Note: this also removes the Hibernate option from the power menu. If you want hibernate back later without Fast Startup, that needs a registry-free alternative — see Fix 3.

### Fix 3: Keep hibernate but kill Fast Startup via registry-free policy

1. Actually, the supported method is simpler than it sounds: disable Fast Startup in Power Options (Fix 1) while leaving hibernation on — they're independent toggles despite sharing the hibernation file.
2. Verify with `powercfg /a` in an elevated terminal: hibernate should list as available while Fast Startup stays off.
3. If your edition has Group Policy (**gpedit.msc**), go to **Computer Configuration > Administrative Templates > System > Shutdown** and set **Require use of fast startup** to **Disabled** — this locks it off against updates re-enabling it.
4. Home edition users can rely on Fix 1; just recheck the setting after each feature update.

### Fix 4: Rebuild hiberfil.sys

1. Open **Terminal (Admin)**.
2. Run `powercfg /h off`, restart, then run `powercfg /h on`.
3. This deletes and recreates the hibernation file, clearing corruption that causes restless shutdowns.
4. Then re-apply Fix 1 to ensure Fast Startup stays off with the fresh file.

### Fix 5: Address the remaining drain sources

1. With Fast Startup off, test one overnight shutdown. If drain persists, the culprits are elsewhere — Fast Startup was a contributor, not the whole story.
2. Disable wake timers: **Power Options > Change plan settings > Change advanced power settings > Sleep > Allow wake timers > Disable**.
3. Turn off USB PowerShare / Always On USB in the BIOS.
4. Unplug all peripherals before shutdown — docks and drives can keep rails alive regardless of Fast Startup.
5. Run `powercfg /waketimers` in an elevated terminal to audit what Windows has scheduled to wake the machine; disable offenders in Task Scheduler.

### Fix 6: Verify the setting survived

1. After the next Windows update, recheck **Power Options > Choose what the power buttons do**.
2. Feature updates are notorious for silently re-enabling Fast Startup.
3. Make it a habit: after every major update, glance at the checkbox.
4. Consider the Group Policy lock (Fix 3) on Pro editions to make the setting stick permanently.

### Fix 7: Measure the improvement

1. Before-and-after test: note the battery percentage at shutdown, check it in the morning, with Fast Startup on vs. off. One night each gives you a clean comparison.
2. Run `powercfg /batteryreport` and compare the overnight discharge rates in the recent usage section.
3. Typical improvement: from 8–15% overnight loss down to 1–3% — the difference between a real shutdown and a fake one, measured in percent.
4. If you see no improvement, the drain is hardware-level (battery self-discharge) — run a [battery health check](/articles/how-to-check-battery-health-on-windows-11-laptop/) to confirm, and stop blaming the software.

## Closing

Fast Startup is a classic engineering tradeoff: faster boots in exchange for a laptop that's never truly off. For desktop-replacement machines that live on chargers, it's harmless. For anyone who closes the lid and expects the battery to still be there in the morning, it's the first thing to disable. One checkbox, one genuine shutdown, and the phantom overnight drain usually vanishes — which tells you everything about where it was coming from, and costs you nothing but a few seconds of boot time.
