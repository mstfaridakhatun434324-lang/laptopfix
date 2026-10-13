---
title: "How to Fix Battery Saver Greyed Out on an HP Laptop"
slug: how-to-fix-battery-saver-greyed-out-on-hp-laptop
date: 2026-09-05
categories: ["battery"]
tags: ["battery saver", "hp laptop", "greyed out", "windows 10", "windows 11"]
description: "Battery saver option greyed out on your HP laptop? Here is why HP machines do this and seven fixes to get the toggle working again."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-greyed-out-on-hp-laptop.webp"
faqs:
  - q: "Why is battery saver greyed out on my HP laptop?"
    a: "The usual cause is HP's own power software overriding Windows. HP Support Assistant or the BIOS Battery Health Manager can take control of battery settings and lock the Windows toggle. Outdated battery drivers, a group policy set by an employer or school, and a battery the system cannot detect will also grey it out."
  - q: "Can I still save battery if the toggle is greyed out?"
    a: "Yes. You can lower screen brightness, shorten the display timeout, and close background apps manually, which together save more power than battery saver alone. But the greyed-out toggle usually signals a driver or policy problem worth fixing, since it can mask other power issues."
  - q: "Is this a Windows 10 or Windows 11 problem?"
    a: "It happens on both. On Windows 10 the quick-action toggle in the Action Center greys out; on Windows 11 the switch under Settings, System, Power and battery does. The fixes below cover both versions because the underlying causes are the same."
  - q: "Will reinstalling HP Support Assistant fix it?"
    a: "Often, yes. A corrupted HP Support Assistant or HP System Event Utility install is one of the most common reasons the toggle locks up. A clean reinstall from HP's site restores the background services that let Windows manage the battery again."
---
You open the battery settings on your HP laptop, ready to stretch the last 25 percent through the end of the day, and the Battery saver toggle just sits there, greyed out and unclickable. On HP machines this is rarely a Windows bug. It is usually HP's own software, a policy, or a driver getting in the way.

The good news is that the fix is almost always on your side of the screen. These steps go from the most common causes to the rarest, and one of them will bring that toggle back to life.

## Why this happens

- **HP power software has taken over.** HP Support Assistant, HP Power Manager, or the BIOS Battery Health Manager can seize control of battery profiles and lock the Windows toggle.
- **Battery drivers are stale or corrupted.** If Windows cannot cleanly talk to the battery, it greys out battery saver rather than offering a broken feature.
- **Group policy is blocking it.** School and work laptops often ship with a policy that disables battery saver. It can also linger after the machine leaves the organization.
- **The battery is not detected.** A loose internal connector or a dead battery makes Windows treat the machine like a desktop, where battery saver makes no sense.
- **Power plan corruption.** A damaged power scheme can carry a battery-saver threshold that Windows cannot apply, so the UI disables the option.
- **Pending updates.** A half-installed Windows update can leave power settings in a limbo state until the update finishes.

## How to fix it

Work through these in order, checking the toggle after each step.

### Fix 1: Check HP's battery tools first

1. Open **HP Support Assistant** from the Start menu and go to the battery or power section.
2. Look for any active battery profile, such as "HP Optimized" or a Battery Health Manager setting like "Let HP manage my charging settings."
3. If HP is managing charging, that is likely what locked the Windows toggle. You can leave HP in charge, or switch it to **Standard** mode to hand control back to Windows.
4. Also open **Windows Settings > System > Power & battery** (Windows 11) or **Settings > System > Battery** (Windows 10) and confirm the toggle state after the change.

### Fix 2: Reinstall the battery drivers

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You will see **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery**.
3. Right-click each one, choose **Uninstall device**, and confirm. Do not delete any driver software if it asks.
4. Restart the laptop. Windows reinstalls both drivers automatically during boot.
5. Check the battery saver toggle again. This single step resolves the issue more often than any other. HP's [support site](https://support.hp.com/us-en) also lists driver packs if Windows fails to reinstall them.

### Fix 3: Rule out a group policy lock

1. Press **Win + R**, type `gpedit.msc`, and press Enter. (If you are on Windows Home, this tool is not included, so skip to Fix 4.)
2. Navigate to **Computer Configuration > Administrative Templates > System > Power Management > Energy Saver Settings**.
3. Double-click **Turn off Energy Saver (plugged in)** and **Turn off Energy Saver (on battery)**. Set both to **Not Configured**.
4. Open an elevated Command Prompt and run `gpupdate /force`, then restart and retest.

### Fix 4: Reset the power plans to defaults

1. Press **Win + R**, type `cmd`, then press **Ctrl + Shift + Enter** for an elevated prompt.
2. Run `powercfg -restoredefaultschemes` and press Enter. This rebuilds all power plans from scratch.
3. Restart the laptop.
4. Go back to **Settings > System > Power & battery** and check the toggle. If the plan was corrupt, battery saver should be clickable now. If your machine also [loses battery in sleep](/articles/how-to-fix-hp-laptop-battery-drains-in-sleep-after-windows-11-update/), a plan reset often helps that too.

### Fix 5: Check the battery is actually detected

1. Click the battery icon in the taskbar. If Windows shows no battery icon at all, or Device Manager shows no battery devices, the hardware is not being seen.
2. Shut the laptop down completely, unplug it, and hold the power button for 20 seconds to drain residual charge.
3. If the battery is removable, take it out, check the contacts for corrosion, and reseat it firmly.
4. Boot up and check Device Manager again. A battery that appears here but not before points to a loose connector, which is worth having a technician reseat properly.

### Fix 6: Update HP System Event Utility and BIOS

1. The HP System Event Utility is the background service that bridges HP hardware and Windows power features. An old version can lock settings.
2. Download the latest version for your model from [HP Support](https://support.hp.com/us-en) and install it.
3. While you are there, check for a BIOS update and install it with the charger connected.
4. Restart and test the toggle. BIOS updates frequently fix power-management handshake bugs on HP laptops.

### Fix 7: Finish pending Windows updates

1. Open **Settings > Update & Security > Windows Update** (Windows 10) or **Settings > Windows Update** (Windows 11).
2. Install everything pending, including optional driver updates under **Advanced options > Optional updates**.
3. Restart even if Windows does not insist. Power settings are applied during boot, and a pending restart can leave them half-configured.
4. After the restart, the battery saver toggle should behave normally. If it is still greyed out at this point, the machine may need a look from HP support, since you have eliminated every software cause.

## Closing

A greyed-out battery saver on an HP laptop is almost never a hardware failure. It is HP's software, a driver, or a policy holding the toggle hostage. Reinstall the battery drivers, check HP's own tools, and reset the power plans, and you will almost certainly have it back. Once the toggle works again, if saver still seems to do little, work through our guide to [battery saver not making a difference](/articles/how-to-fix-battery-saver-not-working-on-laptop-in-windows-11-24h2/), which covers the workload and health issues that blunt its effect. If the toggle stays locked after all seven fixes, that is the point to call HP support with your model and serial number in hand. Keep a note of which fix worked, too, because the same underlying cause tends to resurface after major Windows updates, and knowing your fix saves you the whole hunt next time.
