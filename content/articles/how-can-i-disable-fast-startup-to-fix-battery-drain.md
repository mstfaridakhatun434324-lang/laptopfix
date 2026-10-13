---
title: "How to Disable Fast Startup to Fix Battery Drain"
slug: how-can-i-disable-fast-startup-to-fix-battery-drain
date: 2026-10-10
categories: ["battery"]
tags: ["fast startup", "battery drain", "sleep", "power settings"]
description: "Fast Startup can secretly drain your laptop battery overnight. Learn how to turn it off and stop the mysterious power loss."
thumbnail: "/images/thumbs/how-can-i-disable-fast-startup-to-fix-battery-drain.webp"
faqs:
  - q: "What is Fast Startup and why does it drain battery?"
    a: "Fast Startup is a hybrid shutdown that saves the system kernel to disk so the laptop boots faster. But it keeps hardware in a semi-powered state instead of fully off, and on some laptops this prevents deep sleep states — so the battery keeps draining as if the machine were half-awake."
  - q: "Will disabling Fast Startup make my laptop slower to boot?"
    a: "On modern laptops with SSDs, the difference is a few seconds at most — often imperceptible. The battery savings and the cleaner shutdown state are worth far more than the tiny boot-time gain, especially if you're losing charge overnight."
  - q: "How do I know if Fast Startup is causing my battery drain?"
    a: "The classic symptom is losing 10 to 30 percent overnight with the lid closed and the laptop supposedly 'off.' If the drain stops after a true Restart (which bypasses Fast Startup) but continues after Shutdown, Fast Startup is the culprit."
  - q: "Does Windows 11 still have Fast Startup?"
    a: "Yes. It's enabled by default in both Windows 10 and Windows 11, buried in the classic Control Panel power options. The steps to disable it are identical on both versions."
---

You shut your laptop down at 80 percent, open it the next morning, and it's at 55. The laptop was "off" — so where did the power go? On many machines the answer is Fast Startup, a Windows feature that doesn't actually turn your laptop fully off. It was designed to make booting faster, but on some hardware it leaves components sipping power all night. Disabling it is a five-minute fix for one of the most confusing battery drains in Windows.

## Why this happens

- **Hybrid shutdown isn't a real shutdown:** Fast Startup saves the kernel session to disk and powers down only partially, leaving devices in a low-power-but-not-off state.
- **Blocked deep sleep:** Some firmware never enters its lowest power states during hybrid shutdown, so the drain continues all night.
- **Wake timers still fire:** Scheduled tasks and devices can wake a "fast-startup off" machine more easily than a truly shut-down one.
- **Restart bypasses it:** A Restart does a full shutdown, which is why the drain mysteriously stops after restarts but not shutdowns — a dead giveaway.
- **Driver state carried over:** The saved kernel session can preserve a misbehaving driver state across "shutdowns," including one that's keeping hardware awake.
- **USB devices stay powered:** On some laptops, USB ports remain energized during hybrid shutdown to support wake-on-USB, and a connected peripheral keeps drawing power through the night.
- **Network adapters stay half-awake:** Wake-on-LAN and connected-standby networking keep the Wi-Fi radio in a low-power listening state instead of fully off, adding a slow but steady drain.

## How to fix it

### Fix 1: Disable Fast Startup in Power Options

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable** (requires admin).
4. Uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**, then shut down fully and check the battery the next morning.

### Fix 2: Confirm the drain pattern first

1. Charge to a known percentage and note it.
2. **Shut down** (not restart) and leave the laptop closed overnight.
3. Check the percentage in the morning and note the loss.
4. The next night, do a **Restart** instead, then shut down from the login screen — a full shutdown.
5. If the second night loses far less, Fast Startup was the cause and Fix 1 will resolve it.

### Fix 3: Disable it via Command Prompt (alternative)

1. Open **Terminal (Admin)** or **Command Prompt as administrator**.
2. Run `powercfg /h off` — this disables hibernation, which also disables Fast Startup since it depends on the hibernation file.
3. To re-enable later, run `powercfg /h on` and re-tick the Fast Startup box.
4. Note: this also removes the Hibernate option from the power menu, which some people prefer anyway.

### Fix 4: Check wake timers and scheduled tasks

1. In an admin terminal, run `powercfg /waketimers` to list what's allowed to wake the machine.
2. Open **Task Scheduler** and check tasks under **Microsoft > Windows > UpdateOrchestrator** — disable **Reboot** task wake triggers if present.
3. In **Device Manager**, open your network adapter's **Properties > Power Management** and uncheck **Allow this device to wake the computer**.
4. These wake sources compound the Fast Startup drain; fixing both gives the best result.

### Fix 5: Update BIOS and chipset drivers

1. Visit your manufacturer's support site (Dell, HP, Lenovo, ASUS) and check for a BIOS update — many fix sleep-state bugs.
2. Install the latest chipset drivers from the manufacturer, not just Windows Update.
3. Firmware updates often fix the underlying reason the hardware can't reach deep sleep during hybrid shutdown.
4. After updating, retest an overnight shutdown before assuming anything else.

### Fix 6: Switch the power button to hibernate or full shutdown

1. In **Choose what the power buttons do**, set **When I press the power button** to **Shut down** for both battery and plugged-in.
2. If you disabled hibernation in Fix 3, consider re-enabling it (`powercfg /h on`) and using **Hibernate** instead — it's a true zero-power state unlike hybrid shutdown.
3. Set **When I close the lid** to **Sleep** (not shutdown) for daily use convenience.

### Fix 7: Rule out the battery itself

1. Run `powercfg /batteryreport` in an admin terminal.
2. Check **Design Capacity** vs **Full Charge Capacity** — a worn battery loses charge faster in every state, making normal drain look like a Fast Startup problem.
3. If wear is under 20 percent and the overnight loss exceeds 10 percent with Fast Startup off, investigate further with our guide to [laptop battery draining in sleep mode](/articles/laptop-battery-drains-in-sleep-mode-troubleshooting/).

### Fix 8: Check whether your laptop uses Modern Standby

1. In an admin terminal, run `powercfg /a` and look at the available sleep states.
2. If you see **Standby (S0 Low Power Idle)** — Modern Standby — your laptop stays semi-awake in sleep by design, syncing mail and updates like a phone.
3. Modern Standby plus Fast Startup is the worst combination for overnight drain; disabling Fast Startup helps, but also go to **Settings > System > Power & battery** and restrict background network activity during sleep if the option exists.
4. Some manufacturers let you switch to classic S3 sleep in the BIOS under **Power** or **Advanced** settings — S3 uses far less power but wakes more slowly.

## Closing

Fast Startup is a classic "helpful" feature with a hidden cost: your laptop never truly sleeps, and the battery pays for it. Turning it off costs you a couple of seconds at boot and often recovers 10-20 percent of overnight charge. Make it a permanent change rather than a test — there's no real downside on an SSD-equipped laptop. If the drain persists after disabling it, the next suspects are wake timers and a worn battery — both covered above.

Microsoft documents startup and power behavior at the [Windows support hub](https://support.microsoft.com/en-us/windows). For the full picture on overnight drain, see [how to fix battery drains overnight when the laptop is off](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-step-by-step/).
