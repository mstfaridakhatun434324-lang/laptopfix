---
title: "HP Laptop Battery Draining in Sleep? Troubleshooting Steps"
slug: troubleshoot-hp-laptop-battery-drains-in-sleep
date: 2026-09-30
categories: ["battery"]
tags: ["HP laptop", "sleep drain", "wake timers", "HP BIOS"]
description: "HP laptops have their own sleep quirks, from Sure Start to USB PowerShare. These HP-specific steps stop overnight battery drain."
thumbnail: "/images/thumbs/troubleshoot-hp-laptop-battery-drains-in-sleep.webp"
faqs:
  - q: "Why does my HP laptop lose so much battery in sleep?"
    a: "The usual causes are wake timers waking the machine overnight, HP utilities like Support Assistant running background tasks, USB charging staying active in sleep, and Modern Standby keeping the network alive. HP-specific settings in the BIOS and in HP apps cover several of these, which is why generic Windows fixes sometimes miss them."
  - q: "Does HP Support Assistant drain the battery in sleep?"
    a: "It can contribute. Support Assistant schedules automated tune-ups and update checks that may run as wake timers. If you see it in powercfg /waketimers output, reschedule its automated tasks to daytime hours inside the app's settings rather than uninstalling it outright."
  - q: "Should I disable Modern Standby on my HP laptop?"
    a: "If your HP model offers a BIOS option to switch between Modern Standby and classic S3 sleep, trying S3 is worthwhile when drain is severe — S3 uses measurably less power. Not all models offer the choice; on those that do not, the fixes below still cut drain substantially."
  - q: "Can HP's BIOS affect sleep battery drain?"
    a: "Yes. HP BIOS updates frequently include power-management fixes, and settings like USB charging in sleep, wake on LAN, and the sleep state itself live in the BIOS. An outdated BIOS is one of the most common reasons HP-specific drain persists after all Windows settings are correct."
---

HP laptops lose battery in sleep for the same general reasons any Windows laptop does — wake timers, network activity, Modern Standby — plus a few HP-specific wrinkles: HP Support Assistant's scheduled tasks, BIOS-level USB charging, and firmware power quirks that only HP updates fix. If you have already tried the generic advice and the drain continues, the HP-specific steps below are what you are missing.

Start with the general [sleep drain troubleshooting](/articles/how-to-fix-laptop-battery-drains-in-sleep-mode-on-windows-10/) for the Windows-side fixes, then work through the HP-focused steps here. Together they cover the full picture.

## Why this happens

- **Wake timers fire overnight.** Windows Update, HP Support Assistant, and third-party updaters wake the machine to work while you sleep.
- **Modern Standby stays semi-awake.** Most recent HP models use S0 low-power idle, which keeps networking and background tasks alive.
- **HP Support Assistant schedules night tasks.** Automated maintenance and update checks can run during sleep hours.
- **USB charging stays on in sleep.** HP BIOS options can keep USB ports powered, feeding anything plugged in.
- **Wake-on-LAN is enabled.** The network adapter wakes the laptop on network traffic.
- **Outdated HP BIOS or drivers.** Power-management bugs fixed in later firmware keep draining older installs.
- **Fast startup leaves a hybrid state.** A stuck driver in fast startup's half-hibernate can draw power all night.
- **Connected peripherals wake the machine.** A mouse, external drive, or even a monitor's USB hub can send wake signals that pull the laptop out of sleep repeatedly.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the drain continues.

### Fix 1: Identify what is draining power overnight

Open an elevated **Command Prompt** (search "cmd", right-click, **Run as administrator**) and run:

```
powercfg /sleepstudy
```

This HTML report shows each sleep session and which hardware or software consumed power. On HP machines, look specifically for entries naming HP services, the network adapter, or USB devices — the report even scores each session so you can see which nights were worst. Also run `powercfg /lastwake` first thing in the morning after a bad night — it names exactly what woke the laptop. These two commands turn guessing into evidence, and you should run them before changing any settings so you have a baseline to compare against.

### Fix 2: Disable wake timers in the power plan

Go to **Control Panel > Hardware and Sound > Power Options**, click **Change plan settings** on your active plan, then **Change advanced power settings**. Expand **Sleep > Allow wake timers** and set both **On battery** and **Plugged in** to **Disable**. Click **Apply**, then **OK**. This single change stops scheduled tasks — including HP's — from rousing the laptop overnight. Verify with `powercfg /waketimers`, which should now show no active timers able to wake the machine.

### Fix 3: Reschedule HP Support Assistant tasks

Open **HP Support Assistant**, go to its settings, and look for automated tune-ups, health checks, or update checks scheduled overnight. Move them to a daytime hour when the laptop is awake and plugged in — or disable the automated schedule and run checks manually monthly. Do not uninstall Support Assistant over this; it is genuinely useful for driver updates, it just should not be working the night shift on battery power. HP documents the app's features at [HP's support site](https://support.hp.com/us-en).

### Fix 4: Turn off USB charging in sleep via BIOS

Restart and press **F10** during boot to enter HP's BIOS setup. Navigate to **Advanced > Power Management Options** (exact path varies by model) and look for **USB charging in sleep/off**, **USB PowerShare**, or similar. Disable it. While in the BIOS, also check for **Wake on LAN** and disable it unless you use it, and look for any **Modern Standby / S3 sleep** selector — if your model offers classic S3, try it. Press **F10** to save and exit.

### Fix 5: Quiet the network adapter during sleep

Open **Device Manager > Network adapters**, right-click your Wi-Fi adapter, and open **Properties**. On the **Power Management** tab, check **Allow the computer to turn off this device to save power** and uncheck **Allow this device to wake the computer**. On the **Advanced** tab, disable **Wake on Magic Packet** and **Wake on Pattern Match** if present. In the advanced power plan settings, set any **network connectivity during standby** option to **Disable** on battery. This stops the number-one Modern Standby drain source: a chatty network.

### Fix 6: Update the HP BIOS and drivers

HP regularly ships power-management fixes in BIOS updates. Open **HP Support Assistant** and check for updates, or visit [HP's support site](https://support.hp.com/us-en), enter your model or serial number, and install the latest **BIOS** plus **chipset** and **network** drivers. Keep the adapter plugged in during a BIOS flash and do not interrupt it. After updating, run one overnight sleep test and compare against your earlier sleep study numbers — firmware fixes often show up as dramatically lower drain.

### Fix 7: Switch to hibernate for long idle periods

If drain persists on a Modern Standby machine despite everything, make hibernate the default for lid-close and long idle. Go to **Control Panel > Hardware and Sound > Power Options > Choose what closing the lid does** and set lid-close to **Hibernate**. In advanced power settings, expand **Sleep > Hibernate after** and set **On battery** to 60 minutes — so even if you forget, the laptop drops from sleep into zero-drain hibernate by itself. Resume takes a few seconds longer, but the battery stops melting away overnight.

## Closing

HP sleep drain is a mix of Windows habits and HP-specific settings, which is why generic guides sometimes fall short on these machines. Work the Windows side — wake timers, network, USB — then the HP side — Support Assistant scheduling, BIOS USB charging, and firmware updates — and measure with the sleep study report as you go. When the numbers drop to single digits overnight, you are done, and the laptop will finally sleep as deeply as you do. For a Windows-10-specific take on the same HP fixes, see [HP sleep drain on Windows 10](/articles/how-to-fix-hp-laptop-battery-drains-in-sleep-on-windows-10/).
