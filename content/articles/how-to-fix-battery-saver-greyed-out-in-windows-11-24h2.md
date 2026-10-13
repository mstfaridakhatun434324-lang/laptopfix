---
title: "Battery Saver Greyed Out in Windows 11 24H2? Fix It"
slug: how-to-fix-battery-saver-greyed-out-in-windows-11-24h2
date: 2026-10-09
categories: ["battery"]
tags: ["battery saver", "greyed out", "windows 11 24h2"]
description: "The Battery Saver toggle is greyed out in Windows 11 24H2? Unlock it with these fixes for drivers, policies, and the new Energy saver."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-greyed-out-in-windows-11-24h2.webp"
faqs:
  - q: "Why is Battery Saver greyed out in Windows 11 24H2?"
    a: "The most common cause is simply being plugged into AC power — classic Battery Saver is battery-only. Other causes include a group policy disabling it, a missing or broken battery driver, or the 24H2 update renaming it to Energy saver, which has its own separate toggle."
  - q: "What is the difference between Battery saver and Energy saver?"
    a: "Battery saver is the older mode that only works on battery power. Energy saver, introduced more broadly in 24H2, reduces power on both battery and AC. If you're looking for the old toggle while plugged in, switch to Energy saver instead — that's the intended replacement."
  - q: "Can a driver make Battery Saver greyed out?"
    a: "Yes. If Windows can't detect the battery — due to a broken ACPI battery driver — the saver toggle greys out because there's no battery to save. Reinstalling the battery drivers in Device Manager restores both detection and the toggle."
  - q: "Does greyed out mean my battery is dead?"
    a: "Not necessarily. A greyed-out toggle is a software state, not a battery health reading. Check Settings > System > Power & battery first: if it shows a percentage, the battery is detected and the toggle issue is configuration, not hardware."
---
A greyed-out Battery Saver toggle is Windows telling you "this option doesn't apply right now" — but not telling you why. On Windows 11 24H2, the reasons range from the obvious (you're plugged in) to the obscure (a policy or driver issue hiding behind the UI).

This guide unlocks it step by step, and explains the Battery saver vs. Energy saver split that confuses everyone on 24H2.

## Why this happens

- **Running on AC power:** Classic Battery Saver is battery-only by design. On the charger, Windows greys it out — this is normal, not a bug.
- **24H2 renamed the feature:** On many 24H2 systems the toggle is now **Energy saver**, which works on AC too. Users hunting for the old name think it's broken when it's just renamed.
- **Battery not detected:** A broken ACPI battery driver means Windows sees no battery, so the saver toggle has nothing to act on and greys out.
- **Group policy lock:** IT-managed devices often have the saver disabled by policy, which renders the toggle inactive.
- **Corrupted power plan:** A damaged power scheme can leave the toggle in a permanently disabled state.
- **Tablet/posture detection:** On 2-in-1s, Windows sometimes misreads the device state after the 24H2 update and disables battery-only options.

## How to fix it

Work through these in order — the cause is usually in the first three steps.

### Fix 1: Unplug and check the toggle on battery

Rule out the by-design case first.

1. Unplug the charger completely.
2. Wait 10 seconds for Windows to register the power source change.
3. Open **Settings > System > Power & battery**.
4. If the Battery Saver toggle is now active, nothing was broken — it only works on battery.
5. If you want power saving while plugged in, use **Energy saver** instead (see Fix 2).

### Fix 2: Use Energy saver instead on 24H2

This is the intended replacement for plugged-in power saving.

1. Go to **Settings > System > Power & battery**.
2. Look for **Energy saver** (separate from Battery saver on 24H2).
3. Click **Turn on now** — it works whether you're on battery or AC.
4. Set **Turn on automatically** to **Always** if you want it permanently active.
5. Energy saver dims the screen, throttles background activity, and limits some visual effects — roughly the same savings as the old Battery Saver.

### Fix 3: Reinstall the battery drivers

If the toggle is greyed out even on battery power, Windows may not see the battery.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
3. Uninstall **Microsoft AC Adapter** as well.
4. Restart the laptop. Windows reinstalls both drivers on boot.
5. Unplug the charger and check the toggle again.
6. If the battery still isn't detected, our [battery detection guide](/articles/how-to-fix-battery-not-detected-on-laptop-step-by-step/) goes deeper.

### Fix 4: Check the Power & battery page for detection

Confirm the hardware is visible before chasing policies.

1. Go to **Settings > System > Power & battery**.
2. You should see a battery percentage and a usage graph.
3. If the page says battery information is unavailable, the driver or hardware detection is the real problem — return to Fix 3.
4. If the battery shows fine but the toggle is still greyed out on battery power, continue to Fix 5.

### Fix 5: Check group policy and registry locks

Policies can disable the saver silently.

1. Press **Win + R**, type `gpedit.msc` (Pro/Enterprise only), and go to **Computer Configuration > Administrative Templates > System > Power Management > Energy Saver Settings**.
2. Set any configured policies there to **Not Configured**.
3. Run `gpupdate /force` in an admin Terminal and restart.
4. On company devices, check with IT — they may enforce this deliberately.

### Fix 6: Restore default power schemes

A corrupted scheme can freeze the toggle in the disabled state.

1. Open **Terminal (Admin)** (right-click **Start**).
2. Run `powercfg /restoredefaultschemes`.
3. Restart the laptop.
4. Check the toggle on battery power.

### Fix 7: Run the Power troubleshooter and check for updates

Let Windows repair its own power stack, and make sure 24H2 is fully patched.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run **Power**.
2. Apply any suggested fixes.
3. Then go to **Settings > Windows Update** and install all pending updates — Microsoft fixed several 24H2 power UI bugs in cumulative updates.
4. For official documentation, see the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).
5. If the saver works but drains persist, hunt the drain itself with our [fast-discharge guide](/articles/how-to-fix-battery-discharges-quickly-on-laptop-step-by-step/).

### Fix 8: Reset the BIOS power settings to defaults

Sometimes the blockage lives below Windows entirely, in BIOS power options a previous owner or an update changed.

1. Shut down the laptop and enter the BIOS (usually **F2**, **Del**, or **Fn + F2** during boot).
2. Find the option to **Load Optimized Defaults** or **Reset to default** — often under the **Exit** tab.
3. Save and exit, boot into Windows, and check the toggle on battery power.
4. If your BIOS has its own battery saver or charge-limit options, reconfigure them afterward to your preference — but set them deliberately this time.
5. When the saver works but the charge still won't climb, the problem is charging itself: see our [plugged-in-not-charging guide](/articles/best-way-to-fix-laptop-battery-not-charging-when-plugged-in/).

## Closing

On 24H2, a greyed-out Battery Saver is usually one of three things: you're plugged in, you're looking at the old name instead of Energy saver, or the battery driver needs reinstalling. Sort out which one applies and the toggle comes back to life — and if you want power saving while docked, Energy saver is the feature Microsoft actually intends you to use there. Either way, the fix takes minutes once you know exactly which of the three causes you're dealing with. When Battery saver stays greyed out only on a specific power plan, duplicate the built-in Balanced plan and customize the copy — corrupted plan files sometimes lock the toggle in ways that survive every other fix.
