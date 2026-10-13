---
title: "Best Way to Disable Automatic Driver Updates in Windows"
slug: best-way-to-disable-automatic-driver-updates
date: 2026-09-09
categories: ["drivers"]
tags: ["disable driver updates", "automatic driver updates", "windows update drivers", "driver control"]
description: "Tired of Windows Update breaking your drivers? Learn the best ways to disable automatic driver updates while keeping security updates flowing."
thumbnail: "/images/thumbs/best-way-to-disable-automatic-driver-updates.webp"
faqs:
  - q: "Is it safe to disable automatic driver updates?"
    a: "Yes, with one condition: you take over driver maintenance yourself. Windows Update's driver packages are convenient but generic, and they are a leading cause of broken audio, WiFi, and touchpads. Disabling them is safe if you update drivers manually from the laptop maker a few times a year. Security updates are separate and should always stay enabled."
  - q: "Will disabling driver updates stop all Windows updates?"
    a: "No — the methods here target driver delivery specifically. Security patches, feature updates, and Microsoft product updates continue normally. You are only telling Windows not to replace your hardware drivers. This distinction matters: never disable Windows Update entirely, since unpatched security flaws are far worse than any driver inconvenience."
  - q: "Which method of disabling driver updates is most reliable?"
    a: "The Group Policy or registry method that excludes drivers from Windows Update is the most thorough, because it stops driver delivery at the source. The Device Installation Settings dialog is easier but less complete, and the hardware-ID block is the most surgical — it pins one specific device while letting others update. Most users do well with the policy method plus manual driver installs."
  - q: "Can I re-enable automatic driver updates later?"
    a: "Yes, every method here is reversible. Group Policy and registry changes can be set back to defaults, Device Installation Settings can be re-enabled, and hardware-ID blocks can be removed. If you buy new hardware that needs a driver Windows would provide, temporarily re-enabling updates is the fastest way to get it, then disable again."
---

Windows Update means well when it installs drivers: fresh drivers, no effort. But its driver packages are generic builds that have repeatedly broken working laptops — the Realtek audio that went silent overnight, the WiFi card that picked up a Code 10, the touchpad that lost its gestures. When you have been burned, the rational move is to take driver delivery out of Windows Update's hands while leaving security patches alone.

There are several ways to do this, from a simple dialog to Group Policy, and they differ in thoroughness. The right choice depends on your Windows edition and how much control you want. All of them are reversible, and none of them touches security updates.

## Why this happens

- **Windows Update ships generic driver builds** that lack the laptop maker's tuning.
- **Driver updates install silently**, so the breakage appears 'out of nowhere'.
- **Newer is not validated**: the update was never tested on your exact model.
- **Driver and firmware pairs get split** when only the driver updates.
- **Rollback windows expire**, leaving no easy path back after 10 days for some components.
- **Optional driver updates auto-install** on some configurations without clear consent.
- **Reinstall loops**: Windows re-applies a bad driver after you manually fix it.
- **No per-device control by default**, so one bad package affects every device class.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Device Installation Settings (easiest)

The simplest switch lives in the old System Properties dialog. Open Settings > System > About > Advanced system settings, go to the Hardware tab, and click Device Installation Settings. Choose 'No (your device might not work as expected)'. This tells Windows not to download manufacturer apps and custom icons — and on many builds it reduces driver delivery. It is the least thorough method, but it takes twenty seconds and is fully reversible, so it is the right first try.

1. Open Advanced system settings > Hardware tab.
2. Click Device Installation Settings.
3. Select 'No' and save changes.
4. Reboot and monitor whether driver updates still arrive.

### Fix 2: Exclude drivers via Group Policy (Windows Pro)

On Windows Pro, the proper control is Group Policy: open gpedit.msc and navigate to Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update. Enable 'Do not include drivers with Windows Updates'. This is the policy Microsoft documents for exactly this purpose, and it stops driver delivery at the source while security and feature updates continue. Run gpupdate /force and reboot. Microsoft's update documentation is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open gpedit.msc as an administrator.
2. Navigate to Windows Update > Manage updates offered from Windows Update.
3. Enable 'Do not include drivers with Windows Updates'.
4. Run `gpupdate /force` and reboot.

### Fix 3: Set the registry policy (Windows Home)

Windows Home has no gpedit, but the same policy exists as a registry value. Open regedit and go to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate, create a DWORD named ExcludeWUDriversInQualityUpdate, and set it to 1. Create any missing keys along the path. Reboot for it to take effect. This is the exact same switch the Group Policy editor flips, so it is equally thorough — just reached by hand. Back up the registry key before editing, as always.

1. Open regedit as an administrator.
2. Navigate to the WindowsUpdate policy key, creating it if needed.
3. Create DWORD ExcludeWUDriversInQualityUpdate = 1.
4. Reboot and verify drivers no longer appear in updates.

### Fix 4: Block a specific device by hardware ID (surgical)

If only one device keeps getting a bad driver — say, the WiFi card — block just that device. In Device Manager, find the device, open Properties > Details, and copy a Hardware ID. Then in gpedit (or the corresponding registry key), open 'Prevent installation of devices that match these device IDs' under Device Installation Restrictions and paste the ID. This pins that one device to your manually installed driver while everything else updates normally. It is the most surgical option and ideal when 95% of Windows' drivers are fine.

1. Copy the device's Hardware ID from Device Manager.
2. Open Device Installation Restrictions in Group Policy.
3. Enable 'Prevent installation of devices that match these device IDs'.
4. Paste the ID, apply, and reboot.

### Fix 5: Roll back and hide the bad update

If a bad driver already installed, roll it back in Device Manager first (Properties > Driver > Roll Back Driver). Then prevent its return: download Microsoft's 'Show or hide updates' troubleshooter package, run it, and hide the driver update. Hidden updates stay hidden until you unhide them, which breaks the reinstall loop where Windows keeps re-applying the driver you just removed. This pairs well with any of the blocking methods above.

1. Roll back the bad driver in Device Manager.
2. Download Microsoft's 'Show or hide updates' troubleshooter.
3. Run it and hide the problematic driver update.
4. Confirm the update no longer reappears.

### Fix 6: Take over driver maintenance manually

Blocking automatic drivers only works if you update drivers yourself. Set a calendar reminder every three to six months: visit the laptop maker's support page for your exact model and install the validated driver bundle — chipset first, then graphics, network, and audio. For Intel-based wireless and Bluetooth, Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) automates the check. This cadence gets you tested drivers without the surprise breakage, and the [chipset driver guide](/articles/how-to-install-chipset-drivers-in-windows-11-24h2/) covers the most important package.

1. Bookmark the laptop maker's support page for your exact model.
2. Every 3-6 months, install the maker's validated driver bundle.
3. Install chipset drivers before graphics and network drivers.
4. Keep the installers so you can roll back instantly.

### Fix 7: Verify the block is holding

After applying a method, verify it: open Settings > Windows Update > Update history and check that no driver entries appear after the next Patch Tuesday. In Device Manager, confirm driver dates stay where you put them. If a driver still slips through, you likely applied the Device Installation Settings dialog only — escalate to the policy/registry method, which is enforced more strictly. Also re-check after feature updates, which occasionally reset update policies. Driver-related blue screens have their own diagnostics in the [driver power state guide](/articles/driver-power-state-failure-windows-11-fix/).

1. Check Update history after the next update cycle.
2. Confirm driver versions in Device Manager are unchanged.
3. Escalate to the policy method if drivers still arrive.
4. Re-verify after each Windows feature update.

## Closing

Automatic driver updates are a convenience that charges a hidden price: the occasional silently broken laptop. The fix is not to disable updates — security patches are non-negotiable — but to separate driver delivery from the update stream and take drivers over yourself. The Group Policy or registry exclusion is the set-and-forget answer for most people; the hardware-ID block is the scalpel for single-device problems. Whichever you choose, pair it with a manual driver routine twice a year from the laptop maker's support page. Drivers updated on your schedule, from sources validated for your machine, give you the stability Windows Update's generic packages never promised.
