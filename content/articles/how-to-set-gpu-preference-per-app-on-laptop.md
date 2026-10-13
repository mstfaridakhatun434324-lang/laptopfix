---
title: "How to Set GPU Preference Per App on a Windows Laptop"
slug: "how-to-set-gpu-preference-per-app-on-laptop"
date: "2026-09-22"
categories: ["performance"]
tags: ["gpu preference", "nvidia optimus", "integrated graphics", "windows 11"]
description: "Force games onto the discrete GPU and browsers onto integrated graphics: set per-app GPU preferences on Windows 11 laptops."
thumbnail: "/images/thumbs/how-to-set-gpu-preference-per-app-on-laptop.webp"
faqs:
  - q: "What is the difference between the integrated and discrete GPU?"
    a: "The integrated GPU lives inside your CPU, sips power, and handles everyday tasks like browsing and video playback efficiently. The discrete GPU, from NVIDIA or AMD, is a separate chip with far more rendering power but much higher power draw. Windows assigns apps automatically, but its guesses are sometimes wrong, which is why manual per-app preferences exist."
  - q: "Will forcing the discrete GPU drain my battery faster?"
    a: "Yes, significantly. The discrete GPU can draw 50 to 100 watts under load versus a few watts for integrated graphics. That is why the best practice is surgical: assign the discrete GPU only to games and creative apps that need it, and leave everything else on integrated or power-saving. Blanket-assigning everything to high performance will halve your battery life."
  - q: "Why is there no GPU preference option on my laptop?"
    a: "The setting appears only on systems with switchable graphics, meaning both an integrated and a discrete GPU. If your laptop has only integrated graphics, there is nothing to switch between and Windows hides the option. It can also be missing if the discrete GPU driver is not installed correctly, so a driver reinstall is worth trying first."
  - q: "Does the Windows setting override NVIDIA Control Panel?"
    a: "Mostly yes on Windows 11. The Windows graphics preference is the modern authority and generally takes precedence for Store apps and most desktop apps. The NVIDIA Control Panel still works for its own profiles, but when both are set, Windows' per-app preference usually wins. For consistency, manage GPU assignment in one place: Windows Settings."
---

Gaming laptops carry two graphics chips: a frugal integrated GPU for everyday work and a powerful discrete GPU for demanding tasks. Windows is supposed to assign each app to the right one automatically, but its guesses fail regularly. Games launch on integrated graphics and stutter, while a video call app wakes the power-hungry discrete GPU and drains the battery for no reason.

The fix is the per-app GPU preference in Windows 11 Settings. It lets you pin specific applications to a specific GPU: high performance for your games and creative tools, power saving for browsers and chat apps, and let Windows decide for everything else. Two minutes of configuration pays off every day in both frame rates and battery life.

This guide shows how to set preferences for both desktop and Store apps, how to verify which GPU an app actually used, and what to do when the option is missing.

## Why this happens

- **Windows auto-assignment guessing wrong:** The automatic heuristic sometimes puts games on integrated graphics, causing severe stutter.
- **Battery-draining apps on discrete GPU:** Chat and browser apps waking the discrete GPU waste enormous power for zero benefit.
- **Driver install missing the GPU:** Without a proper discrete GPU driver, Windows cannot offer the choice at all.
- **Single-GPU systems:** Laptops with only integrated graphics legitimately have no preference to set.
- **Conflicting NVIDIA Control Panel profiles:** Old profiles in the vendor panel can fight the Windows setting.
- **Game launchers vs game executables:** Setting the preference on the launcher instead of the actual game binary has no effect.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open the graphics settings page

The per-app preferences live under Display settings. This is the control center for all GPU assignment.

1. Press Win+I to open Settings, then System, then Display.
2. Scroll down and click Graphics.
3. You will see a list of added apps and an Add button.
4. If the page is missing entirely, your laptop likely has only one GPU.

### Fix 2: Add a desktop app and set its GPU

Desktop apps like games must be added by browsing to their executable. Target the real game binary, not the launcher.

1. On the Graphics page, click Add an app and choose Desktop app.
2. Browse to the game's actual executable, for example in its Steam folder.
3. Click Add, then select the app in the list and click Options.
4. Choose High performance for the discrete GPU or Power saving for integrated.
5. Click Save and launch the app to test.

### Fix 3: Set preferences for Store apps

Microsoft Store apps are added differently, through a searchable list rather than file browsing.

1. On the Graphics page, click Add an app and choose Microsoft Store app.
2. Pick the app from the dropdown list.
3. Click Add, select it, and click Options.
4. Assign High performance or Power saving as appropriate.
5. Store apps like video editors benefit most from explicit assignment.

### Fix 4: Verify which GPU an app actually used

Do not trust the setting blindly. Task Manager's GPU engine column shows the truth per process.

1. Launch the app you configured.
2. Open Task Manager with Ctrl+Shift+Esc.
3. Go to Details, right-click the column headers, and enable GPU and GPU engine.
4. Find your app's process and read which GPU engine it uses.
5. GPU 0 is typically integrated and GPU 1 discrete; confirm in the Performance tab.

### Fix 5: Fix a missing GPU preference option

If the Graphics page lacks options or only shows one GPU, the discrete driver is usually the problem.

1. Open Device Manager and expand Display adapters.
2. Confirm both the integrated and discrete GPUs appear without warning icons.
3. Download the latest discrete GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
4. Install it and restart.
5. Reopen the Graphics settings page and check for both options.

### Fix 6: Set sensible defaults by app type

A good assignment strategy maximizes both performance and battery without micromanaging every app.

1. Assign High performance to games, 3D software, and video editors.
2. Assign Power saving to browsers, chat apps, and office software.
3. Leave Let Windows decide for utilities and small tools.
4. Revisit assignments after major driver updates, which can reset them.
5. Test battery life over a day to confirm the savings.

### Fix 7: Use the BIOS MUX switch on supported laptops

Many gaming laptops have a multiplexer that can route the display directly to the discrete GPU, bypassing the integrated chip entirely. This dGPU mode maximizes game performance at the cost of battery life.

1. Restart and enter the BIOS or UEFI setup.
2. Look for Display Mode, Graphics Mode, or MUX switch settings.
3. Switch from Hybrid to Discrete or dGPU mode.
4. Save and exit; Windows will redetect displays.
5. Use this mode for plugged-in gaming and switch back to Hybrid for travel.

### Fix 8: Use the BIOS MUX switch on supported laptops

Many gaming laptops have a multiplexer that can route the display directly to the discrete GPU, bypassing the integrated chip entirely. This dGPU mode maximizes game performance at the cost of battery life.

1. Restart and enter the BIOS or UEFI setup.
2. Look for Display Mode, Graphics Mode, or MUX switch settings.
3. Switch from Hybrid to Discrete or dGPU mode.
4. Save and exit; Windows will redetect displays.
5. Use this mode for plugged-in gaming and switch back to Hybrid for travel.

## Closing

Per-app GPU preferences are one of the highest-value tweaks on a dual-GPU laptop: games get the frames they deserve while everyday apps stop waking the power-hungry chip. Set it once per app, verify with Task Manager, and revisit after driver updates. If your laptop still feels slow in games after the discrete GPU is confirmed active, the next suspects are thermal throttling and background CPU load, covered in our [startup optimization guide](/articles/how-to-disable-startup-apps-on-windows-11/). For everyday use, keep the laptop in hybrid graphics mode and let the per-app preferences do the work. If you want the quick-reference version of these settings, see [this GPU preference guide](/articles/best-way-to-set-gpu-preference-per-app/). For everyday use, keep the laptop in hybrid graphics mode and let the per-app preferences do the work. If you want the quick-reference version of these settings, see [this GPU preference guide](/articles/best-way-to-set-gpu-preference-per-app/). Recheck your assignments after every major driver update, since installers occasionally reset per-app preferences without any warning to the user. Keep a screenshot of your working configuration so restoring it takes seconds.
