---
title: "Night Light Not Working? How to Fix It in Windows"
slug: how-do-i-fix-night-light-not-working
date: 2026-09-13
categories: ["drivers"]
tags: ["night light", "blue light", "display", "windows 11"]
description: "Windows Night Light won't turn on or is greyed out? Fix the registry, driver, and settings issues behind it with this guide."
thumbnail: "/images/thumbs/how-do-i-fix-night-light-not-working.webp"
faqs:
  - q: "Why is the Night Light toggle greyed out in Windows settings?"
    a: "A greyed-out Night Light toggle almost always means a corrupted registry entry or a graphics driver problem. The specific registry key that controls Night Light's cloud-store data frequently corrupts after Windows updates. Deleting that key and restarting — or reinstalling the graphics driver — restores the toggle in the majority of cases."
  - q: "Night Light turns on but I see no color change — why?"
    a: "This usually means the color temperature or strength slider is set too subtly to notice, or a manufacturer display utility (like Dell PremierColor or Lenovo display profiles) is overriding Windows' color management. Check the Night Light strength slider first, then look for conflicting display software applying its own color profile."
  - q: "Can my graphics driver break Night Light?"
    a: "Yes. Night Light depends on the GPU driver's color pipeline, so a corrupted or generic graphics driver can silently disable it. If Night Light broke after a driver or Windows update, a clean reinstall of the manufacturer's graphics driver is one of the most reliable fixes."
  - q: "Does Night Light work on external monitors?"
    a: "It should, since Night Light is applied by Windows at the GPU level rather than by the monitor. If Night Light works on the laptop screen but not the external monitor, the monitor is likely applying its own color processing or the GPU driver is handling the external output through a different color path — updating the graphics driver usually aligns them."
---

Night Light — Windows' built-in blue-light filter — is one of those features you do not appreciate until it stops working. The toggle goes grey, or it claims to be on while the screen stays stubbornly blue-white, usually right after a Windows update. The underlying cause is rarely mysterious: Night Light depends on a fragile chain of registry data, graphics driver color support, and display settings, and updates love breaking links in that chain.

The good news is that the fixes are well understood and quick. The famous registry-key deletion resolves the greyed-out toggle for most people in under two minutes, and the graphics driver reinstall covers most of the rest. This guide walks through the full sequence, including the display-driver and color-profile checks for the subtler cases. For the Windows 11 24H2-specific variant, see our [Night Light troubleshooting walkthrough](/articles/troubleshoot-night-light-not-working/), and for general display driver issues, the [display driver stopped responding guide](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/).

## Why this happens

- **Corrupted Night Light registry data.** The CloudStore registry key holding Night Light state corrupts frequently after feature updates.
- **Graphics driver problems.** Night Light needs the GPU driver's color pipeline; generic or corrupted drivers break it silently.
- **Conflicting display utilities.** Manufacturer color tools (Dell PremierColor, Lenovo Vantage display, ASUS Splendid) override Windows color management.
- **Corrupted color profile.** A damaged ICC color profile can prevent Night Light's color shift from applying.
- **Group Policy or registry locks.** Managed or tweaked systems may have Night Light disabled by policy.
- **Location services disabled.** The sunset-to-sunrise schedule needs location; without it, scheduling misbehaves.
- **HDR conflicts.** HDR display modes can override or conflict with Night Light's color adjustments.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Delete the corrupted Night Light registry key

The classic fix for the greyed-out toggle.

1. Press **Win + R**, type `regedit`, and press Enter.
2. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current`.
3. Find and delete the subkey named `default$windows.data.bluelightreduction.bluelightreductionstate` (and the similarly named `...settings` key if present).
4. Restart the laptop. Windows rebuilds the keys with clean defaults and the Night Light toggle should work again.

### Fix 2: Toggle Night Light via Settings and check the schedule

Rule out simple misconfiguration.

1. Open **Settings > System > Display > Night light** and turn the main toggle off and back on.
2. Drag the **Strength** slider to the far right temporarily — a subtle setting can be nearly invisible, making you think the feature is broken.
3. Under **Schedule**, try switching between **Sunset to sunrise** and **Set hours**. If scheduling is the problem, manual hours work as a reliable workaround.
4. For sunset-to-sunrise scheduling, confirm **Location services** are on (**Settings > Privacy & security > Location**) so Windows knows when sunset is.

### Fix 3: Reinstall the graphics driver

Fix the color pipeline Night Light depends on.

1. Open Device Manager, expand **Display adapters**, right-click your GPU, and choose **Uninstall device** (check **Attempt to remove the driver** if offered).
2. Restart, then install the latest driver from the official source: [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html) — or your laptop maker's support page for a tuned version.
3. After reinstalling, retest Night Light before changing any other display settings.
4. On dual-GPU laptops, update both GPU drivers — Night Light can break when the two drivers are mismatched.

### Fix 4: Remove conflicting display software and color profiles

Third-party color management fights Night Light.

1. Check for manufacturer display utilities (Dell PremierColor, HP Display Control, Lenovo Vantage display settings, ASUS Splendid) and either disable their color features or uninstall them temporarily.
2. Open **Control Panel > Color Management**, select your display, and check the **Profiles** list. Remove any custom ICC profile and check **Use my settings for this device** with the default sRGB profile.
3. In the GPU control panel (Intel/NVIDIA/AMD), reset any custom color settings to defaults.
4. Retest Night Light with all third-party color processing disabled.

### Fix 5: Check HDR and display mode settings

HDR and Night Light do not always coexist peacefully.

1. Open **Settings > System > Display > HDR** and try turning **HDR** off temporarily to see if Night Light starts working.
2. If you need HDR, check whether your GPU control panel has a separate night-mode or blue-light feature that conflicts — use one or the other, not both.
3. On external monitors, check the monitor's own menu for a **blue light filter** or **reading mode** — the monitor's hardware filter can make it look like Night Light is doing nothing (or double-apply the effect).

### Fix 6: Check Group Policy and registry locks

For systems where Night Light seems administratively disabled.

1. Press **Win + R**, type `gpedit.msc` (Pro editions), and check **Computer Configuration > Administrative Templates** for anything display-related that could lock the feature.
2. In regedit, check `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore` for any obviously broken Night Light entries beyond the ones deleted in Fix 1.
3. If the laptop is managed by an organization, the IT policy may disable Night Light — this is not fixable locally and needs an admin exception.

### Fix 7: Use the Action Center toggle and test a new user profile

Isolate profile-level corruption.

1. Press **Win + A** to open Quick Settings and try the Night Light toggle there — sometimes the Quick Settings toggle works when the Settings page toggle does not (or vice versa), which points at UI-level rather than system-level breakage.
2. Create a new local user account (**Settings > Accounts > Other users**) and test Night Light there. If it works in the new account, your main profile's settings store is corrupted — migrate to the new profile or reset the old one's display settings.
3. As a final fallback, third-party blue-light filters like f.lux provide the same functionality independently of Windows' Night Light system. [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) also documents display troubleshooting steps.

## Closing

Night Light failures look like a broken feature but are almost always corrupted state: the CloudStore registry key for the greyed-out toggle, the graphics driver for the silently-not-working case, or a conflicting color utility for the subtle cases. The registry deletion takes two minutes and has the highest hit rate of any single step in this guide. Work through the list, testing the toggle after each fix, and the warm evening glow usually returns well before you reach the fallbacks.
