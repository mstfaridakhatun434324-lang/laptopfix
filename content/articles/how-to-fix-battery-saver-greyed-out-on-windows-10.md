---
title: "How to Fix Battery Saver Greyed Out on Windows 10"
slug: how-to-fix-battery-saver-greyed-out-on-windows-10
date: 2026-10-02
categories: ["battery"]
tags: ["battery saver", "windows 10", "power settings"]
description: "Battery Saver won't turn on in Windows 10? Fix the greyed-out toggle with these steps covering power plans, drivers, policies, and system repairs."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-greyed-out-on-windows-10.webp"
faqs:
  - q: "Why is Battery Saver greyed out in Windows 10?"
    a: "Most often the laptop is plugged in — Battery Saver only works on battery power. Other causes include a corrupted power plan, a group policy disabling it, battery drivers not detecting the battery, or a third-party tweaker that turned the feature off."
  - q: "Where is Battery Saver in Windows 10?"
    a: "Click the battery icon in the notification area to open the quick slider panel, where Battery Saver appears as a tile. You can also find it under Settings > System > Battery. The automatic threshold is configured in the Battery settings page."
  - q: "Does Battery Saver actually extend battery life much?"
    a: "It typically adds 30–60 minutes by reducing background activity, lowering screen brightness, and limiting push notifications and some visual effects. It's most effective when the battery is low — it's a stretch-the-last-hour tool, not a double-your-runtime tool."
  - q: "Can I force Battery Saver to stay on?"
    a: "Yes — in Settings > System > Battery, set Battery Saver to turn on automatically and drag the threshold up, or toggle it on manually whenever you're on battery. It turns itself off when you plug in, since it only applies to battery power by design."
---

On Windows 10, Battery Saver lives in the quick-action panel behind the battery icon — and when its toggle is greyed out, you can't stretch those last precious percentages. Before you assume something is broken, check the obvious: is the charger plugged in? Battery Saver is battery-only by design, and Windows 10 greys it out on AC power. That's not a bug.

If you're unplugged and it's still greyed out, something is genuinely blocking it. Here's how to find and remove the block, starting with the quick checks and ending with the deeper repairs.

## Why this happens

- **You're on AC power.** Battery Saver only engages on battery. Plugged in = greyed out, always, by design.
- **The power plan is damaged.** Battery Saver hooks into the active power plan. A corrupted plan — often a souvenir from a feature update — can disable the feature silently.
- **Group policy turned it off.** Work and school machines frequently have Battery Saver disabled by IT policy, which greys out every local control.
- **Windows can't see the battery.** If the battery driver failed, Battery Saver has nothing to manage and Windows disables the toggle.
- **A "tweaker" or debloater disabled it.** Privacy scripts and system tweakers sometimes switch Battery Saver off via registry or policy as a side effect, and the change persists after the tool is gone.

## How to fix it

Work through these in order. Confirm the charger situation first — it resolves more cases than everything else combined.

### Fix 1: Unplug and check the automatic threshold

Start with the basics before touching anything else.

1. Unplug the AC adapter and wait 10–15 seconds for Windows to register the switch to battery.
2. Click the **battery icon** in the notification area to open the power panel.
3. If Battery Saver is now available, that was the whole story — it only works on battery power.
4. Go to **Settings** > **System** > **Battery** and check **Turn battery saver on automatically if my battery falls below**. If it's set oddly high or the feature looks off, set it to **20%** and test by toggling it manually.

### Fix 2: Make sure Windows detects the battery

A greyed-out Battery Saver with a missing or broken battery driver is a package deal.

1. Look at the battery icon in the notification area. If it shows no percentage or an error, Windows isn't reading the battery.
2. Press **Win + X** > **Device Manager** > **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device** and confirm. Do the same for **Microsoft AC Adapter**.
4. Restart the laptop — Windows reinstalls both drivers automatically during boot.
5. Recheck the Battery Saver toggle on battery power. Driver reinstalls fix a surprising number of "greyed out" cases, especially after feature updates.

### Fix 3: Restore the default power plans

Corrupted power plans are a classic Windows 10 issue. Resetting them is quick and harmless.

1. Right-click **Start** > **Windows PowerShell (Admin)** or **Command Prompt (Admin)**.
2. Run `powercfg -restoredefaultschemes` and wait for the command to return.
3. Restart the laptop.
4. On battery power, open the battery flyout and check Battery Saver. The reset rebuilds the plan that Battery Saver attaches to.

### Fix 4: Run the Power troubleshooter

Windows 10's troubleshooter specifically checks the Battery Saver configuration.

1. Go to **Settings** > **Update & Security** > **Troubleshoot** > **Additional troubleshooters**.
2. Select **Power** > **Run the troubleshooter**.
3. Apply whatever it recommends. It commonly fixes the automatic threshold and re-links Battery Saver to the active plan.
4. Restart and test the toggle on battery power. If the troubleshooter finds nothing, keep going — the block is likely policy or registry based.

### Fix 5: Check group policy

If this laptop is (or ever was) managed by an organization, a policy may be doing this.

1. Press **Win + R**, type `gpedit.msc`, and press Enter. (Windows 10 Home doesn't have it — skip to Fix 6.)
2. Go to **Computer Configuration** > **Administrative Templates** > **System** > **Power Management** and look for **Turn off Battery Saver** or similar entries set to **Enabled**.
3. Set any you find to **Not Configured**.
4. Open an admin terminal and run `gpupdate /force`, then restart and recheck.
5. If the policy is genuinely set by your IT department, leave it alone — overriding managed policies can violate your organization's rules. For deeper Battery Saver problems beyond the greyed-out toggle, see [Battery Saver not working on laptop](/articles/battery-saver-not-working-on-laptop-troubleshooting/).

### Fix 6: Clean up the registry block

Tweaker tools often leave a registry value behind that keeps Battery Saver off permanently.

1. Press **Win + R**, type `regedit`, and approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Power\PowerSettings` and look for values disabling Battery Saver or Energy Saver.
3. Check `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows` as well.
4. **Export the key first** (**File** > **Export**) as a backup, then delete the offending value.
5. Restart. The toggle should be back — registry blocks are stubborn but simple once found.

### Fix 7: Repair system files

If the toggle broke after an update and nothing else helped, the OS components behind Battery Saver may be damaged.

1. Open an admin terminal and run `sfc /scannow`. Give it 10–20 minutes.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and check Battery Saver on battery power.
4. As a final option, a repair install using installation media from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) (for an upgrade) rebuilds system components while keeping files and apps — but for most people, one of the earlier fixes resolves it. If the taskbar battery icon is also missing or misbehaving, the [missing battery icon guide](/articles/battery-icon-missing-from-taskbar-troubleshooting/) covers that overlapping problem.

## Closing

A greyed-out Battery Saver on Windows 10 is the charger, a policy, or a broken power plan far more often than a broken laptop. Unplug, verify the battery is detected, restore the default power plans, and clear any policy or registry block — the toggle comes back in nearly every case. Once it's working, set the automatic threshold to 20% and let Windows handle the rest; that's the whole point of the feature.
