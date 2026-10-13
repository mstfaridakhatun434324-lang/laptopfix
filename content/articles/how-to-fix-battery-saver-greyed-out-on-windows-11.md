---
title: "How to Fix Battery Saver Greyed Out on Windows 11"
slug: how-to-fix-battery-saver-greyed-out-on-windows-11
date: 2026-09-26
categories: ["battery"]
tags: ["battery saver", "windows 11", "power settings"]
description: "Can't turn on Battery Saver because the toggle is greyed out? These fixes restore it on Windows 11, from power settings to group policy and driver repairs."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-greyed-out-on-windows-11.webp"
faqs:
  - q: "Why is Battery Saver greyed out on Windows 11?"
    a: "The usual reasons: the laptop is plugged in (Battery Saver only runs on battery power), a group policy or registry setting disabled it, the power plan is corrupted, or a recent update broke the toggle. It's rarely a hardware problem."
  - q: "Can I use Battery Saver while my laptop is plugged in?"
    a: "No — Windows 11 only lets Battery Saver run on battery power, and the toggle greys out while charging by design. If you want lower power draw while plugged in, use the Best power efficiency mode under Settings > System > Power & battery instead."
  - q: "Is Battery Saver the same as a power plan?"
    a: "Not exactly. Power plans control the overall performance/power balance, while Battery Saver is a temporary state that kicks in at a battery threshold to stretch remaining runtime by dimming the screen, limiting background activity, and pausing non-critical sync."
  - q: "Will enabling Battery Saver slow down my laptop?"
    a: "Slightly, yes — that's the point. It reduces background activity and may cap CPU boost behavior to save power. The effect is mild and temporary; turn it off when you're back on the charger and full performance returns immediately."
---

You open **Settings** > **System** > **Power & battery**, reach for the Battery Saver toggle — and it's greyed out, unclickable, mocking you. This is one of those Windows 11 annoyances that looks like a bug but is usually a setting, a policy, or a driver quietly blocking the switch.

The important thing to know first: Battery Saver is *supposed* to be greyed out while your laptop is plugged in. It only works on battery power. If your charger is connected, unplug it and check again — you may not have a problem at all. If it's still greyed out on battery power, work through the fixes below.

## Why this happens

- **The charger is connected.** By design, Windows 11 disables Battery Saver while on AC power. This alone accounts for a huge share of "greyed out" reports.
- **A group policy disabled it.** On work or school laptops, IT policies can turn Battery Saver off entirely — the toggle greys out and no local setting overrides it.
- **The power plan is corrupted.** Battery Saver ties into the active power plan. A damaged plan (common after feature updates) can leave the toggle in a permanently disabled state.
- **Battery drivers aren't reporting correctly.** If Windows can't see a working battery — generic driver, failed ACPI driver — Battery Saver has nothing to manage and stays greyed out.
- **A registry tweak or "debloater" broke it.** Third-party privacy tools and scripts sometimes disable Battery Saver via registry or policy as a side effect, leaving the toggle dead.

## How to fix it

Work through these in order. Skip Fix 1 only if you've already confirmed the charger is unplugged.

### Fix 1: Unplug the charger and check the battery threshold

This is the "is it plugged in?" of Battery Saver troubleshooting — embarrassingly common.

1. Unplug the AC adapter completely and wait about 10 seconds.
2. Go to **Settings** > **System** > **Power & battery** and look at the **Battery saver** section.
3. If the toggle is now clickable, there was never a problem — Battery Saver only engages on battery power by design.
4. Check the **Turn battery saver on automatically at** dropdown too. If it's set to **Never**, the toggle may appear inactive; set it to **20%** or **Always** and test again.

### Fix 2: Verify Windows actually sees your battery

Battery Saver can't run if Windows doesn't detect a battery. A missing or broken battery driver greys out everything power-related.

1. Click the battery icon in the taskbar. If it shows **Unknown** or no percentage, Windows isn't reading the battery.
2. Press **Win + X**, open **Device Manager**, and expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** > **Uninstall device**, confirm, then restart the laptop. Windows reinstalls the driver on boot.
4. After restarting, check the taskbar icon again — if the percentage is back, the Battery Saver toggle usually follows. If the battery icon itself is missing entirely, see the guide on [fixing a battery icon missing from the taskbar](/articles/battery-icon-missing-from-taskbar-troubleshooting/).

### Fix 3: Restore the default power plans

A corrupted power plan can silently disable Battery Saver. Resetting the plans to defaults is safe and takes a minute.

1. Right-click **Start** and open **Terminal (Admin)**.
2. Run `powercfg -restoredefaultschemes` and wait for the prompt to return.
3. Restart the laptop.
4. Go back to **Settings** > **System** > **Power & battery** and check the toggle. The reset also restores the default Battery Saver threshold behavior.

### Fix 4: Check group policy (work and school laptops)

If this is a managed device, IT may have disabled Battery Saver deliberately. You can't override a real policy — but many "policies" are just leftover settings you can clear.

1. Press **Win + R**, type `gpedit.msc`, and press Enter. (If it says the snap-in isn't available, you're on Windows 11 Home — skip to Fix 5.)
2. Navigate to **Computer Configuration** > **Administrative Templates** > **System** > **Power Management**.
3. Look for anything mentioning **Energy Saver** or **Battery Saver** set to **Disabled**. Double-click it and set it to **Not Configured**.
4. Open **Terminal** and run `gpupdate /force`, then restart and recheck the toggle.

### Fix 5: Repair the Energy Saver registry setting

On Windows 11 Home (no group policy editor) or after a debloater script ran, the block is often a single registry value. This is safe to check and fix.

1. Press **Win + R**, type `regedit`, and press Enter. Click **Yes** on the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Power\PowerSettings`.
3. Look for a value related to Energy Saver / Battery Saver set to disable it. If you find one, right-click and **Delete** it.
4. Also check `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies` for anything power-related and remove it.
5. Restart the laptop. If you're unsure about a value, export the key first (**File** > **Export**) so you can restore it — never delete registry entries blindly.

### Fix 6: Run the Power troubleshooter

Windows 11 still ships a dedicated Power troubleshooter that catches configuration problems the manual steps miss.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Find **Power** in the list and click **Run**.
3. Let it scan and apply whatever fixes it recommends — it commonly repairs the Battery Saver threshold and plan associations.
4. Restart and check the toggle. If the troubleshooter reports it "couldn't identify the problem," continue to the next fix.

### Fix 7: Repair system files with SFC and DISM

If the toggle broke right after a Windows update, corrupted system files may be responsible. This pair of commands repairs them.

1. Open **Terminal (Admin)**.
2. Run `sfc /scannow` and wait for it to finish — this takes 10–20 minutes.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and let it complete.
4. Restart the laptop and check **Settings** > **System** > **Power & battery** again.
5. If Battery Saver is still greyed out at this point and the laptop is on battery with a detected battery, a Windows in-place repair install (using the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)) is the remaining option — it keeps your files and apps while rebuilding the OS components.

## Closing

Nine times out of ten, a greyed-out Battery Saver is the charger being plugged in, a group policy, or a corrupted power plan — not a broken laptop. Unplug, check the policy and registry, restore the default plans, and reinstall the battery driver, and the toggle comes back. If the toggle works but Battery Saver doesn't seem to save any power once enabled, see [Battery Saver not working on laptop](/articles/battery-saver-not-working-on-laptop-troubleshooting/) for the next layer of fixes. If this is a work machine and the policy is intentional, your IT department is the final authority — but for personal laptops, one of these fixes almost always does it.
