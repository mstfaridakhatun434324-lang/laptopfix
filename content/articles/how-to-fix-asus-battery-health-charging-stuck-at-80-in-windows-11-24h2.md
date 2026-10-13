---
title: "ASUS Battery Health Charging Stuck at 80% in Windows 11 24H2"
slug: how-to-fix-asus-battery-health-charging-stuck-at-80-in-windows-11-24h2
date: 2026-09-24
categories: ["battery"]
tags: ["asus", "windows 11 24h2", "charge limit"]
description: "ASUS laptop capped at 80% specifically on Windows 11 24H2? Fix the 24H2-specific driver and MyASUS issues that keep reasserting the limit."
thumbnail: "/images/thumbs/how-to-fix-asus-battery-health-charging-stuck-at-80-in-windows-11-24h2.webp"
faqs:
  - q: "Why does 24H2 specifically cause the ASUS 80% cap?"
    a: "24H2 reinstalls the ASUS System Control Interface driver and resets MyASUS to defaults (Balanced mode = 80%). It can also break the driver-MyASUS communication, so changing the setting appears to do nothing."
  - q: "I set Full capacity mode but it still stops at 80%. Why?"
    a: "The setting isn't reaching the embedded controller — usually because the System Control Interface driver is the wrong version for 24H2. Update it from ASUS support, then set Full capacity mode again."
  - q: "Does the 80% cap hurt anything if I just leave it?"
    a: "No. Balanced mode at 80% is ASUS's recommended daily setting for battery longevity. Only change it if you genuinely need the extra runtime — for desk use, 80% is the healthier choice."
  - q: "Can I set a custom limit like 90% on ASUS?"
    a: "MyASUS only offers the three presets (60/80/100%). There's no official 90% option. Some users work around it with third-party tools, but those aren't supported by ASUS and can conflict with MyASUS."
---
Same symptom as the general ASUS stuck-at-80 problem, but with a 24H2 twist: you set Full capacity mode in MyASUS and the laptop *still* stops at 80%. Or the setting reverts to Balanced on every reboot. Or MyASUS shows the options greyed out entirely. These are 24H2-specific breakages in the driver chain between MyASUS and the embedded controller — and they need 24H2-specific fixes.

If you haven't tried the basic toggle yet, start there — but this guide picks up where the basics fail. The 24H2 version of this problem is sneakier than the general one: the setting can look correct in MyASUS while the embedded controller quietly ignores it, which is why the driver chain below matters more than the toggle itself.

## Why this happens

- **24H2 replaced the System Control Interface driver.** The new version from Windows Update doesn't fully support the Battery Health Charging calls on some ASUS models.
- **MyASUS settings don't persist.** The app writes the mode, but the broken driver can't commit it to the embedded controller — so it reverts on reboot.
- **MyASUS itself is outdated for 24H2.** Older MyASUS builds misbehave on 24H2; the 24H2-compatible build comes from the Microsoft Store, not Windows Update.
- **Windows Update keeps "fixing" the driver.** Even after you install ASUS's driver, Windows Update may replace it with its own version again.
- **The embedded controller latched the limit.** The controller stored the 80% cap in firmware and isn't accepting new commands until reset.
- **Fast Startup preserves the stale state.** The hibernated kernel keeps reloading the old driver state across "shutdowns."

## How to fix it

Work through these in order. The driver version dance (Fixes 2-4) is the heart of the 24H2-specific problem.

### Fix 1: Confirm the basic toggle is actually set

1. Open **MyASUS** > **Customization** > **Battery health charging**.
2. Select **Full capacity mode**. Unplug the charger for 10 seconds, replug, and watch for 5 minutes.
3. If it now charges past 80% — done. If it reverts after reboot or never takes effect, continue. The [post-update ASUS guide](/articles/how-to-fix-asus-battery-health-charging-stuck-at-80-after-windows-11-update/) covers the non-24H2 basics in more detail.

### Fix 2: Update MyASUS from the Microsoft Store

1. Open the **Microsoft Store**, search **MyASUS**, and install any available update — the Store build is the 24H2-compatible one.
2. If MyASUS is missing entirely, install it fresh from the Store.
3. Open it, go to **Battery health charging**, set **Full capacity mode** again, and reboot to test persistence.
4. An outdated MyASUS on 24H2 is the most common reason the toggle "does nothing."

### Fix 3: Install ASUS's own System Control Interface driver

1. Go to the ASUS support site, enter your exact model, and download the **ASUS System Control Interface** driver (v3 or newer for 24H2-era models).
2. Install it over whatever Windows Update provided, then restart.
3. Reopen MyASUS — the Battery health charging options should now be responsive instead of greyed out or reverting.
4. Set **Full capacity mode** once more after the driver install.

### Fix 4: Stop Windows Update from replacing the driver

1. **Settings** > **Windows Update** > **Advanced options** — check whether driver updates are being forced.
2. The reliable method: in **Device Manager**, find the **ASUS System Control Interface** device, note the working driver version from ASUS.
3. If Windows Update replaces it again later, use **Show or hide updates** troubleshooter (from Microsoft) to hide that specific driver update. This prevents the monthly re-breakage cycle.

### Fix 5: Disable Fast Startup to clear the stale state

1. **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup**. Shut down fully (not restart).
3. Power on, set **Full capacity mode** in MyASUS with a truly cold boot behind you.
4. Fast Startup's hibernated kernel was preserving the broken driver state across your "shutdowns" — a real shutdown lets the new driver load cleanly.

### Fix 6: Reset the embedded controller

1. Shut down fully, unplug the charger and all peripherals.
2. Hold the power button **30-60 seconds** (ASUS models sometimes need the longer hold).
3. Plug in, boot, set **Full capacity mode** in MyASUS.
4. This clears a firmware-latched 80% cap that no driver change can override. If you'd rather keep a deliberate cap, the [80% limit guide](/articles/how-to-limit-battery-charge-to-80/) explains the longevity trade-off.

### Fix 7: Check for a BIOS-level charge setting

1. Enter BIOS (**F2** at boot on most ASUS models).
2. Under **Advanced**, look for any battery care or charge limit function.
3. If present and set to 80%, change it — a BIOS-level cap overrides everything MyASUS does.
4. Save, exit, and verify in Windows that charging passes 80%.

### Fix 8: Clean-reinstall the ASUS software stack in the right order

When the driver dance fails, nuke the whole ASUS stack and rebuild it cleanly — order matters.

1. Uninstall in this order: **MyASUS** (**Settings** > **Apps**), then **ASUS System Control Interface** (**Device Manager** > **System devices** > uninstall), then restart.
2. Install in reverse: the **System Control Interface** driver from ASUS support first, restart, then **MyASUS** from the Microsoft Store.
3. Open MyASUS, set **Full capacity mode**, and do a full shutdown (not restart) so the cold boot loads the fresh stack cleanly.
4. The wrong order — app before driver — is why many "reinstalls" don't work. Driver first, app second, cold boot third. After rebuilding, the [general ASUS stuck-at-80 guide](/articles/how-to-fix-asus-battery-health-charging-stuck-at-80-after-windows-11-update/) covers the non-24H2 variants if this machine ever leaves 24H2.

## Closing

The 24H2 ASUS 80% problem is a driver-chain problem: Windows Update's driver, an outdated MyASUS, and Fast Startup conspiring to keep the limit latched. Update MyASUS from the Store, install ASUS's own driver, block the bad driver from returning, and do one true cold boot. The setting sticks — and the battery charges past 80% again, this time for good.
