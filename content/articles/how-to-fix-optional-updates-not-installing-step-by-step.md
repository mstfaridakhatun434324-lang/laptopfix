---
title: "Optional Updates Not Installing? Step-by-Step Fix for Windows 11"
slug: how-to-fix-optional-updates-not-installing-step-by-step
date: 2026-09-13
categories: ["windows-update"]
tags:
  - "optional updates"
  - "driver updates"
  - "windows update"
  - "windows 11"
description: "Optional updates — mostly drivers and firmware — fail more often than regular updates. Learn why they stall and the exact steps to get them installing on your laptop."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-step-by-step.webp"
faqs:
  - q: "What are optional updates in Windows 11?"
    a: "Optional updates are driver updates, firmware, and some feature previews that Microsoft offers but does not install automatically. You find them under Settings, Windows Update, Advanced options, Optional updates. They are safe to install but not mandatory, which is why they sit in a separate list."
  - q: "Should I install all optional updates?"
    a: "Install driver and firmware optionals for hardware you actually use, especially from your laptop maker. Skip optionals for devices you do not have or features you do not want. Unlike security updates, there is no penalty for leaving an optional update uninstalled."
  - q: "Why do optional driver updates fail so often?"
    a: "Driver optionals fail because they compete with manufacturer drivers, target the wrong device revision, or require a reboot sequence the automatic installer mishandles. Laptops with heavy OEM customization (HP, Dell, Lenovo) see this most, since Windows Update's generic drivers clash with tuned OEM ones."
  - q: "Can a failed optional update break my laptop?"
    a: "Rarely. Failed optionals roll back like any update, and since they are non-critical, skipping them entirely is always safe. The annoyance is the repeated failure noise, not system damage — which is exactly what this guide quiets, so you can stop the noise without risking anything important."
---

Optional updates live in the quiet corner of Windows Update — Advanced options, Optional updates — and they fail with disproportionate frequency. A Realtek audio driver that will not take, an Intel Bluetooth update stuck at installing, firmware that errors out every Patch Tuesday: familiar sights for laptop owners who peek into that list.

The reason is structural. Optional updates are overwhelmingly driver updates, and drivers are where Windows Update's one-size-fits-all model collides with your laptop maker's custom hardware. The failures are annoying rather than dangerous, but they clutter your update experience and can mask real problems.

This guide fixes them properly: understanding which optionals matter, clearing the failures, and — the real solution — getting the right drivers from the right source. If driver updates are failing outside the optional list too, our [driver update failure guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/) goes deeper.

## Why this happens

- **OEM driver conflicts:** Windows Update's generic driver fights the laptop maker's tuned version for the same device.

- **Wrong device revision targeting:** the optional package targets a hardware revision you do not have, so it fails applicability checks.

- **Stale driver store entries:** previous partial installs leave the driver store confused about what is already installed.

- **Firmware needing special conditions:** some firmware optionals require AC power or a specific BIOS version and fail without them.

- **Corrupted optional update cache:** the same SoftwareDistribution corruption that breaks regular updates hits optionals too.

- **Reboot sequencing bugs:** a few optionals need a restart between download and install that the automatic flow skips.

- **Already-newer driver installed:** the optional is older than your current driver, and the installer refuses the downgrade.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Triage: decide which optionals actually matter

Not every optional deserves a fight. Triaging first means you only troubleshoot the updates that benefit your laptop, and simply hide or ignore the rest.

1. Open Settings, Windows Update, Advanced options, Optional updates.
2. Expand Driver updates and note each device and version.
3. Prioritize: network, Bluetooth, graphics, and chipset drivers for hardware you use.
4. Ignore optionals for devices you do not have or features you disabled.
5. For anything critical, prefer the laptop maker's own driver over the optional.

### Fix 2: Clear the failures and retry cleanly

Failed optionals leave stale state that poisons retries. Clearing the cache gives each optional a fresh download and a clean applicability check.

1. Open Terminal (Admin) from the Start right-click menu.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Restart the services with `net start` commands and reboot.
5. Return to Optional updates and try the important ones individually, not all at once.

### Fix 3: Install drivers from the laptop maker instead

The durable fix for failing driver optionals is to stop using Windows Update for drivers at all. Your maker's drivers are tuned for your exact model and install without the applicability fights.

1. Identify your exact model (bottom sticker or system info).
2. Visit your maker's support site — HP, Dell, Lenovo, ASUS, and Acer all host model-specific drivers.
3. Download the driver matching the failing optional (chipset, graphics, network).
4. Install the maker's version; it will supersede the optional.
5. The optional should then vanish from the list or show as not needed.

### Fix 4: Use Device Manager for stubborn driver optionals

When both Windows Update and the maker's installer struggle, Device Manager's manual driver targeting cuts through: you point Windows at the exact .inf instead of letting it guess.

1. Download and extract the driver package from the maker's site (extract, do not just run).
2. Open Device Manager (Win + X), find the device, right-click, Update driver.
3. Choose Browse my computer for drivers and point at the extracted folder.
4. Enable Include subfolders and let it install the exact match.
5. Restart and verify the device works; the optional should clear.

### Fix 5: Handle firmware optionals with care

Firmware optionals deserve respect: they touch the hardware itself. Failed firmware updates usually mean an unmet precondition, not a broken updater.

1. Connect the charger — firmware updates refuse to run on battery alone.
2. Check the maker's site: is a newer BIOS/firmware offered there instead? Prefer it.
3. Close all apps and disable sleep during the firmware install.
4. Never interrupt a firmware flash for any reason.
5. If the optional keeps failing, install the maker's firmware utility version instead.

### Fix 6: Hide optionals you do not want

Some optionals will never apply cleanly to your hardware, and that is fine. Hiding them stops the failure noise without affecting anything important.

1. In the Optional updates list, uncheck anything you have decided to skip.
2. For drivers you replaced with maker versions, the optional usually disappears on its own.
3. If a specific optional reappears and fails endlessly, leave it unchecked permanently.
4. Microsoft's Show/Hide troubleshooter tool can hide truly stubborn ones.
5. Recheck the list monthly — new, better optionals appear over time.

### Fix 7: Repair the engine if all optionals fail

When every optional fails — not just drivers — the problem is the update engine, not the optionals. Escalate to the full servicing repair.

1. Run the Windows Update troubleshooter (Settings, System, Troubleshoot).
2. In Terminal (Admin), run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Follow with `sfc /scannow` and a restart.
4. Retest one simple optional to confirm the engine is healthy.
5. If failures persist, Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) covers advanced servicing repair.

## Closing

Optional updates fail because drivers are the hardest thing Windows Update does, especially on customized laptop hardware. Triage what matters, clear the stale failures, and get the important drivers from your laptop maker instead of fighting the optional list. Treat optionals as suggestions, not obligations, and they stop being a source of stress. For driver updates that fail outside the optional list as well, our [driver update failure guide](/articles/how-to-fix-driver-updates-keep-failing-windows-update-in-windows-11-24h2/) goes deeper.
