---
title: "How to Enable Hibernation on a Laptop to Save Battery"
slug: how-can-i-enable-hibernation-to-save-battery
date: 2026-10-04
categories: ["battery"]
tags: ["hibernation", "power settings", "battery life"]
description: "Turn hibernation on in Windows so your laptop stops draining battery overnight — step-by-step enable and configure guide."
thumbnail: "/images/thumbs/how-can-i-enable-hibernation-to-save-battery.webp"
faqs:
  - q: "Why does my laptop lose battery even when the lid is closed?"
    a: "Closing the lid usually puts the laptop into sleep, which still draws power to keep RAM alive. Over several hours, or overnight, that can drain 10-30% of the battery. Hibernation writes RAM to disk and powers everything off, so it draws essentially zero power while preserving your open work."
  - q: "Is hibernation bad for an SSD?"
    a: "No. Hibernation writes one hiberfil.sys file per cycle — a few gigabytes — which is negligible compared to normal SSD wear from the operating system and applications. Modern SSDs are rated for hundreds of terabytes of writes, so hibernating daily has no meaningful effect on drive lifespan."
  - q: "What is the difference between sleep and hibernation?"
    a: "Sleep keeps RAM powered so the laptop wakes in seconds but continues to drain the battery. Hibernation saves RAM contents to the hard drive and shuts the machine fully off, using no battery at all. Wake-up takes a bit longer — typically 20-40 seconds — because the data is read back from storage."
  - q: "Why is hibernation missing from my power menu?"
    a: "Windows 11 hides the hibernate option by default on some machines. You can restore it in Control Panel power options, enable it via command line with powercfg /hibernate on, or check whether your BIOS/UEFI firmware or disk space is blocking it. Each of these is covered in the fixes below."
---

Sleep is convenient but it is not free: your laptop keeps feeding power to RAM the whole time the lid is shut, and on some machines a background task or a wake timer can keep the machine half-awake for hours. If you keep finding your battery lower than you left it, hibernation is the answer. It snapshots everything in memory to disk and powers the machine completely off — zero drain, and your open apps and documents are exactly where you left them when you wake up.

The catch is that Windows 11 (and some Windows 10 builds) ships with hibernation disabled or hidden on many laptops. Enabling it takes a few minutes across Control Panel, the command line, and your power plan settings. This guide walks through all of it, plus how to make hibernation trigger automatically so you stop thinking about it. If your [battery drains overnight even when the laptop is off](/articles/how-do-i-fix-battery-drains-overnight-when-laptop-is-off/), hibernation is the single biggest fix for that pattern.

## Why this happens

- **Sleep draws continuous power:** RAM stays energized and the chipset stays in a low-power state, so the battery drains steadily while the lid is closed.
- **Wake timers fire at night:** Scheduled tasks, Windows Update, and some apps can wake the machine from sleep and keep it awake, multiplying the drain.
- **Hibernation is disabled by default:** Many OEM builds and Windows 11 installs ship with hibernation off, so the option never appears in the power menu.
- **The hibernate button is hidden:** Even when hibernation is technically available, the checkbox that adds it to the Start menu power options is often unchecked.
- **Not enough free disk space:** Hibernation needs disk space for the hiberfil.sys snapshot file; a nearly full drive can block it silently.
- **Fast Startup confusion:** Windows' Fast Startup uses a partial hibernation of its own, which can make the full hibernation option behave oddly or disappear after driver updates.

## How to fix it

Work through these in order — enable hibernation first, then configure it to save battery automatically.

### Fix 1: Check whether hibernation is currently available

See where you stand before changing anything.

1. Press **Win + R**, type `powercfg /availablesleepstates` and press Enter in an elevated Command Prompt.
2. Read the output: if **Hibernation** is listed as available, the feature works and you only need to unhide it (Fix 2).
3. If hibernation is listed as "not available," the output gives a reason — commonly the hiberfile type, insufficient disk space, or a firmware setting — which tells you which fix below to jump to.
4. Also check **Settings > System > Power & battery > Screen, sleep, & hibernate timeouts** to see what your machine currently does when idle.

### Fix 2: Enable hibernation from the command line

The fastest way to switch it on.

1. Right-click **Start** and choose **Windows Terminal (Admin)** (or **Command Prompt (Admin)** on Windows 10).
2. Type `powercfg /hibernate on` and press Enter. There is no confirmation message — silence means success.
3. Run `powercfg /availablesleepstates` again to confirm hibernation now shows as available.
4. If you get an error about the hiberfile, run `powercfg /h /type full` to ensure the full hibernation file is used rather than the reduced type that some OEMs set.
5. Restart the laptop once so power menus pick up the change. If your machine refuses to keep hibernation enabled, the firmware or a driver is overriding it — see [fixing battery drain in hibernate](/articles/best-way-to-fix-laptop-battery-drains-in-hibernate/).

### Fix 3: Add Hibernate to the Start menu power options

Making the option visible so you can actually use it.

1. Open **Control Panel > Hardware and Sound > Power Options** and click **Choose what the power buttons do** on the left.
2. Click **Change settings that are currently unavailable** at the top to unlock the checkboxes.
3. Scroll to **Shutdown settings** and tick the **Hibernate** checkbox.
4. Click **Save changes**, then open the Start menu power icon to confirm **Hibernate** now appears alongside Sleep and Shut down.
5. Test it once: hibernate with a few apps open, then power back on and confirm everything restores.

### Fix 4: Make hibernation automatic after a set time

Stop relying on yourself to remember.

1. In **Power Options**, click **Change plan settings** next to your active plan, then **Change advanced power settings**.
2. Expand **Sleep > Hibernate after** and set **On battery** to something like **30 minutes** — long enough for coffee breaks on sleep, short enough that a forgotten laptop stops draining itself.
3. While you are there, expand **Sleep > Sleep after** and keep it shorter than the hibernate value (for example, sleep after 10 minutes, hibernate after 30).
4. Expand **Sleep > Allow hybrid sleep** and set it to **Off** on battery — hybrid sleep keeps RAM powered and partly defeats the purpose.
5. Click **OK**. Now an idle laptop sleeps first, then drops into zero-drain hibernation on its own.

### Fix 5: Map the power button and lid to hibernate

Make the hardware do what you want.

1. Back in **Choose what the power buttons do**, set **When I press the power button** to **Hibernate** for **On battery**.
2. Set **When I close the lid** to **Hibernate** for **On battery** as well — or keep Sleep for short closes and rely on the automatic timer from Fix 4 for the deep state.
3. Click **Save changes** and test: close the lid on battery, wait a minute, and confirm the machine is fully off rather than warm and humming in a bag.

### Fix 6: Free disk space if hibernation fails to engage

The hiberfile needs room to write.

1. Check free space on your C: drive — hibernation typically needs RAM-size space, so 8-16 GB free is a safe minimum.
2. Run **Settings > System > Storage > Temporary files** and clear categories you do not need.
3. Run `powercfg /h /size 40` in an elevated prompt to shrink the hiberfile to 40% of RAM if you are tight on space (the default is 40% on Windows 11 anyway; raise to 100 only if hibernation fails).
4. Retry hibernation after freeing space. If it still fails, check for a firmware-level "Modern Standby" lock — some machines reserve hibernation behavior in **BIOS/UEFI** under power settings.

### Fix 7: Disable rogue wake timers that fight hibernation

A machine that wakes itself defeats every power state.

1. In the advanced power settings from Fix 4, expand **Sleep > Allow wake timers** and set **On battery** to **Disable**.
2. Open **Device Manager**, expand **Network adapters**, right-click your Wi-Fi adapter, choose **Properties > Power Management**, and uncheck **Allow this device to wake the computer**.
3. Do the same for the mouse under **Mice and other pointing devices** if you carry the laptop in a bag — a jostled mouse wakes machines constantly.
4. Run `powercfg /waketimers` in a prompt to see what is scheduled; disable unnecessary scheduled tasks in **Task Scheduler** that wake the machine.
5. Microsoft's [Windows power and sleep documentation](https://support.microsoft.com/en-us/windows) covers the official behavior of each sleep state if you want the full reference.

## Closing

With hibernation enabled and set to trigger automatically, an idle laptop stops being a slow battery leak and becomes a machine that is simply off when you are not using it. The wake-up takes a few seconds longer than sleep, but you trade that for a battery that is exactly where you left it — which, for anyone who carries a laptop around all day, is the better deal by far.
