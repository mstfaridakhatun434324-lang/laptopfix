---
title: "How to Disable Fast Startup to Stop Battery Drain"
slug: best-way-to-disable-fast-startup-to-fix-battery-drain
date: 2026-10-11
categories: ["battery"]
tags: ["fast startup", "battery drain", "shutdown"]
description: "Laptop losing charge while shut down? Fast Startup's hybrid shutdown is a common culprit — here's how to turn it off properly."
thumbnail: "/images/thumbs/best-way-to-disable-fast-startup-to-fix-battery-drain.webp"
faqs:
  - q: "What is fast startup in Windows 11?"
    a: "Fast startup is a hybrid shutdown: Windows logs you out, then hibernates the kernel session instead of fully powering off. Boot is quicker because the system state is reloaded from disk, but the machine never truly powers down."
  - q: "Can fast startup drain my battery overnight?"
    a: "Yes. Because the hardware stays in a low-power state rather than fully off, some laptops keep USB ports, network adapters, or the embedded controller powered. On machines with buggy firmware this can drain several percent overnight."
  - q: "Does disabling fast startup slow down my boot?"
    a: "Slightly, on older machines with spinning hard drives. On modern laptops with NVMe SSDs the difference is usually one or two seconds — barely noticeable in daily use."
  - q: "Will disabling fast startup fix all battery drain?"
    a: "No — it only fixes drain caused by the hybrid shutdown state. If your battery drains while the laptop is on, or in real sleep mode, the cause is elsewhere: background apps, wake timers, or connected peripherals."
---

You shut your laptop down at 80%, open it the next morning, and it's at 71%. You definitely clicked Shut down, not Sleep — so where did the charge go? The answer is often fast startup: Windows 11's default shutdown isn't a real shutdown. It hibernates the kernel, leaving hardware in a half-awake state that can sip power all night.

Disabling fast startup forces a true full shutdown. It costs you a second or two of boot time on most modern machines, and for many people it completely stops the mysterious overnight drain.

## Why this happens

- **Hybrid shutdown keeps hardware semi-powered:** the kernel hibernates instead of unloading, so USB ports and network chips may stay energized.
- **Buggy firmware never sleeps properly:** some BIOS/EC versions handle the hibernated state badly and keep components awake.
- **Wake timers fire during hybrid shutdown:** scheduled tasks can partially wake the machine, burning power while the lid is closed.
- **USB selective suspend misbehaves:** peripherals that should power down keep drawing current through powered ports.
- **Modern Standby confusion:** on some laptops the hybrid state interacts badly with Modern Standby networking, keeping the Wi-Fi radio alive.
- **Driver state carried over:** a misbehaving driver gets its state saved into the hibernation file and resumed, fault and all, every boot.

## How to fix it

Work through these in order. The core fix is step 1; the rest handle related drain sources that mimic the same symptom.

### Fix 1: Turn off fast startup in Power Options

This is the main event — a proper toggle-off, done with administrator rights.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. In the left sidebar, click **Choose what the power buttons do**.
3. At the top of the page, click **Change settings that are currently unavailable**. This unlocks the greyed-out options.
4. Under **Shutdown settings**, uncheck **Turn on fast startup (recommended)**.
5. Click **Save changes**.
6. Now do a full shutdown: click **Start > Power > Shut down** (not Restart — Restart always does a full reboot anyway).
7. Leave the laptop off overnight and compare the battery percentage. Many users see the overnight drop shrink to zero.

### Fix 2: Disable hibernation's supporting pieces (optional)

If you want the machine to behave like the old days — off means off — you can go further.

1. Right-click **Start** and choose **Terminal (Admin)** or **Windows PowerShell (Admin)**.
2. To disable hibernation entirely, type `powercfg /hibernate off` and press Enter. This also removes the hiberfil.sys file and frees disk space.
3. Note: this disables actual Hibernate from the power menu too. If you use Hibernate deliberately, skip this step.
4. Alternatively, keep hibernation but reduce its footprint: `powercfg /hibernate /type reduced` keeps fast startup working while shrinking the hiberfil file.
5. Restart once and confirm the setting with `powercfg /a` — it lists which sleep states are available.

### Fix 3: Stop USB devices from staying powered

Powered USB ports are a classic overnight drain source on laptops with "always-on" charging ports.

1. Open **Device Manager** (right-click **Start**).
2. Expand **Universal Serial Bus controllers**.
3. For each **USB Root Hub**, right-click, choose **Properties**, and open the **Power Management** tab.
4. Check **Allow the computer to turn off this device to save power**.
5. Enter your BIOS (**F2**, **F10**, or **Del** during boot) and look for **USB PowerShare**, **Always On USB**, or **USB charging in sleep** — disable it if you don't need to charge phones from a sleeping laptop.
6. Unplug dongles, external drives, and USB hubs before shutdown as a test.

### Fix 4: Disable wake timers

Wake timers can rouse a "shut down" machine just enough to burn battery.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Change plan settings** next to your active plan, then **Change advanced power settings**.
3. Expand **Sleep > Allow wake timers** and set both **On battery** and **Plugged in** to **Disable**.
4. Click **OK**.
5. To see what's been waking your machine, open an admin terminal and run `powercfg /waketimers`.
6. For a deeper dive on overnight drain, see [how to fix battery draining overnight while the laptop is off](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-step-by-step/).

### Fix 5: Check Modern Standby network behavior

On Modern Standby laptops, the Wi-Fi radio can stay connected during low-power states.

1. In the same **Advanced power settings** dialog, expand **Sleep > Allow standby states (S1-S3) when sleeping** if present.
2. Go to **Settings > System > Power & battery > Screen, sleep, & hibernate timeouts** and shorten the sleep timeout on battery.
3. In **Device Manager**, open your Wi-Fi adapter's **Properties > Power Management** tab and check **Allow the computer to turn off this device to save power**.
4. Uncheck **Allow this device to wake the computer** on the same tab unless you use Wake-on-LAN deliberately.
5. Test another overnight shutdown and compare.

### Fix 6: Update the BIOS and chipset drivers

Firmware bugs are behind many "drains while off" cases, and manufacturers do fix them.

1. Note your model from **Settings > System > About**.
2. Download the latest **BIOS** and **chipset** drivers from your manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
3. Install the BIOS update with the charger connected and the battery above 50%. Don't interrupt it.
4. Install the chipset drivers and reboot.
5. Re-verify that fast startup is still off (BIOS updates occasionally reset power settings).

### Fix 7: Rule out a genuinely worn battery

If the drain persists with fast startup off and everything unplugged, the battery itself may be the problem.

1. Open an admin terminal and run `powercfg /batteryreport`. Open the generated HTML file from the path it prints.
2. Compare **Design Capacity** with **Full Charge Capacity**. If the full charge capacity is under 60% of design, the battery is heavily worn.
3. A worn battery self-discharges faster and reports percentages unreliably, which looks exactly like overnight drain.
4. Follow [how to check your battery's health in Windows 11](/articles/how-to-check-laptop-battery-health-in-windows-11-24h2/) for the full interpretation.
5. If wear is severe, a replacement battery — not more settings tweaks — is the real fix.

## Closing

Disabling fast startup is a two-minute change that solves overnight drain for a surprising number of laptops. If your battery still drops with a true shutdown, work through the wake timers, USB power, and battery-health checks above — one of them is almost certainly your answer.
