---
title: "How to Fix Battery Saver Greyed Out After a Windows 11 Update"
slug: how-to-fix-battery-saver-greyed-out-after-windows-11-update
date: 2026-10-10
categories: ["battery"]
tags: ["battery saver", "greyed out", "windows 11 update", "power settings"]
description: "Battery saver option greyed out after a Windows 11 update? 6 fixes — from power plan resets to policy checks — that restore the toggle."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-greyed-out-after-windows-11-update.webp"
faqs:
  - q: "Why is Battery saver greyed out after updating Windows 11?"
    a: "The update typically corrupted the active power plan or flipped a registry/policy value that locks the toggle. On some machines it also happens because Windows thinks the laptop is on AC power permanently — for example when the battery driver isn't reporting. The fixes below address each cause."
  - q: "Can I still save battery if the toggle is greyed out?"
    a: "Yes, partially. You can lower screen brightness, switch the power mode to Best power efficiency, and close background apps manually. But those are workarounds — the steps below restore the actual toggle so Battery saver works automatically again."
  - q: "Is Battery saver the same as power mode?"
    a: "No. Power mode (Best power efficiency / Balanced / Best performance) is a general performance setting. Battery saver is an aggressive mode that kicks in at low battery — dimming the screen, throttling background activity, and pausing mail sync. They complement each other."
  - q: "Will a registry edit fix the greyed-out toggle?"
    a: "It can, if a policy value is locking it — but only edit the registry as a last resort and back up the key first. The safer fixes (power plan reset, driver reinstall, update repair) resolve most cases without touching the registry."
---
You open Quick Settings or the battery page after a Windows 11 update, and the Battery saver toggle is greyed out — unclickable, mocking you. Your laptop is clearly running on battery, yet Windows acts like the option doesn't apply. It's a small control with an outsized effect on battery life, and losing it stings on long days away from power.

The toggle greys out for a handful of specific reasons, and they're all fixable. The update didn't remove the feature; it broke the conditions Windows checks before enabling the switch. On Windows 11 the feature is technically called Energy Saver under the hood, which is why some of the policy and registry names you'll encounter below don't say "Battery saver" at all — don't let that throw you off, they're the same feature.

## Why this happens

- **The power plan got corrupted.** Updates can damage the active power scheme's battery-saver settings, and Windows greys out the toggle when the underlying plan is invalid.
- **Windows thinks you're always on AC power.** If the battery driver stopped reporting after the update, Windows assumes AC power and disables battery-only features.
- **A policy is locking it.** The update may have applied (or exposed) a Group Policy or MDM setting that disables Battery saver, common on work and school laptops.
- **The toggle's registry state is stuck.** The `EnergySaver` policy values can latch into a disabled state during a failed update.
- **The Settings app cache is stale.** Sometimes the toggle is actually functional but the Settings UI renders it disabled until its cache refreshes.
- **A third-party power utility took over.** Manufacturer tools occasionally seize control of power features and grey out the Windows-native controls.

## How to fix it

Work through these in order, from safest to most invasive.

### Fix 1: Reset the power plans to defaults

This rebuilds the power scheme Battery saver depends on, and it's the highest-yield fix.

1. Open **Terminal (Admin)** via **Win + X**.
2. Run `powercfg -restoredefaultschemes` and press Enter — this deletes custom plans and rebuilds the defaults.
3. Restart the laptop.
4. Open **Settings** > **System** > **Power & battery** and check whether Battery saver is clickable again. If your battery has other quirks too, [checking the battery health report](/articles/how-to-check-battery-health-on-windows-11-laptop/) is a good parallel step.

### Fix 2: Make sure Windows sees the battery

Battery saver is a battery-only feature — if Windows can't see the battery, the toggle stays grey.

1. Look at the taskbar battery icon: does it show a percentage, or is it missing/glitching?
2. Open **Device Manager** (**Win + X**) > **Batteries** and confirm **Microsoft ACPI-Compliant Control Method Battery** is present with no warning icon.
3. If there's a warning — or the icon is missing — uninstall the battery driver entries, shut down fully, and boot so Windows reinstalls them.
4. Once the taskbar shows a proper battery percentage, recheck the Battery saver toggle. If the icon shows a red X instead, see our [red X battery icon fix](/articles/how-to-fix-battery-x-icon-red-cross-after-windows-11-update/).

### Fix 3: Toggle it from Quick Settings instead

Sometimes only the Settings page is stuck while the underlying feature still works.

1. Click the battery/network/volume icon cluster to open **Quick Settings**.
2. Look for the **Battery saver** tile — if it's not there, click the pencil icon to add it.
3. Try toggling it from Quick Settings. If it works there, the Settings page was just rendering stale state.
4. Restart once more; the Settings page toggle usually syncs up after the feature is used once.

### Fix 4: Check Group Policy and MDM locks

On managed devices the toggle may be deliberately disabled — but updates sometimes apply phantom policies to personal machines too.

1. Press **Win + R**, type `gpedit.msc` (Pro/Enterprise/Education), and go to **Computer Configuration** > **Administrative Templates** > **System** > **Power Management** > **Energy Saver Settings**.
2. Ensure **Turn off Energy Saver** (or similarly named policies) are **Not Configured**.
3. Also check **Settings** > **Accounts** > **Access work or school** — if the laptop is enrolled in management you didn't expect, that's your answer, and only the administrator can unlock it.
4. Run `gpupdate /force` in an elevated Terminal and restart.

### Fix 5: Repair the Settings app and system files

Corruption in the Settings app or system components can freeze the toggle's state.

1. In an elevated Terminal, run `sfc /scannow` and wait for it to finish. This checks every protected system file, including the components that render the Settings pages.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`, then restart. DISM repairs the underlying image that SFC draws from, so run it whenever SFC reports corruption it couldn't fix.
3. Open **Settings** > **Apps** > **Installed apps**, find **Settings** (listed as a system component on newer builds), and use **Repair** if available.
4. Check the toggle again. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) also document known update-specific Settings glitches worth checking against your build number.

### Fix 6: Check the registry policy values (careful)

Only do this if everything above failed — you're looking for a value that's locking the feature off.

1. Press **Win + R**, type `regedit`, and first export a backup via **File** > **Export**.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Power\PowerSettings` and look for energy-saver-related DWORDs set to disable the feature — delete the offending values (not the whole key).
3. Also check `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies` for anything power-related you didn't set.
4. Restart. If the toggle is still grey after a registry cleanup, an in-place repair install of Windows 11 (keeping files and apps) is the remaining option — it rebuilds the policy and Settings stack cleanly.

## Closing

A greyed-out Battery saver toggle is Windows being overcautious about broken prerequisites — usually a corrupt power plan or a battery driver that stopped reporting. Reset the plans, confirm Windows sees the battery, and the toggle comes back to life in the large majority of cases.
