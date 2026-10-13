---
title: "How to Disable Automatic Driver Updates on Windows 11"
slug: "how-to-disable-automatic-driver-updates-on-windows-11"
date: "2026-09-27"
categories: ["drivers"]
tags: ["driver updates", "windows update", "windows 11", "group policy", "driver block"]
description: "Stop Windows 11 from replacing your working drivers. Methods for Home and Pro: Device Installation Settings, Group Policy, Registry, and update hiding."
thumbnail: "/images/thumbs/how-to-disable-automatic-driver-updates-on-windows-11.webp"
faqs:
  - q: "Why does Windows 11 keep replacing my working drivers?"
    a: "Windows Update treats drivers like any other update and installs whatever version Microsoft's catalog considers current, which is often a generic build rather than your laptop maker's tuned version. The replacement happens silently, usually overnight, so hardware that worked yesterday breaks today with no obvious cause. Blocking driver delivery through the methods in this guide keeps your chosen drivers in place while security updates continue normally."
  - q: "Will disabling driver updates make my system insecure?"
    a: "No. Driver updates and security updates are separate channels. The methods here stop Windows Update from delivering hardware drivers; security patches, cumulative updates, and Microsoft Defender definitions continue exactly as before. You remain responsible for updating drivers manually from your manufacturer's site every few months, which is a small price for stability."
  - q: "What's the difference between the Group Policy and Registry methods?"
    a: "They enforce the same block at different levels. Group Policy (Pro, Enterprise, Education) sets a managed policy that Windows Update honors and that survives most resets. The Registry method writes the equivalent value directly and works on Windows 11 Home, which lacks the Group Policy Editor. Both are stronger than the basic Device Installation Settings toggle, which feature updates sometimes revert."
  - q: "How do I update a driver manually after blocking automatic updates?"
    a: "Download the driver from your laptop manufacturer's support page for your exact model, or from the component maker (Intel, NVIDIA, AMD, Realtek). Run the installer and restart. For individual driver files, the Microsoft Update Catalog lets you search by hardware ID. Check manufacturer pages quarterly — graphics and wireless drivers benefit most from periodic manual updates."
---

Windows 11 is more aggressive than its predecessors about replacing drivers: Wi-Fi cards, touchpads, audio chips, and GPUs can all wake up with a new, worse driver after an overnight update. If you have ever fixed a hardware problem only to have it return mysteriously, automatic driver updates are the likely culprit. This guide shows how to stop Windows 11 from touching your drivers — on both Home and Pro — while keeping every security update flowing.

Windows 11 reorganized the Settings app compared to Windows 10, so the click paths differ even where the underlying mechanisms are the same. (If you still run Windows 10 on another machine, our [Windows 10 driver-update guide](/articles/how-to-disable-automatic-driver-updates-on-windows-10/) covers it.)

## Why this happens

- **Windows Update bundles drivers silently:** Driver updates install with no meaningful prompt, so breakage appears spontaneous.
- **Generic beats tuned:** Microsoft's catalog version is often generic, lacking the laptop maker's hardware-specific tuning.
- **No per-device opt-out:** Windows 11 offers no built-in "leave this driver alone" switch, forcing system-wide blocks.
- **Feature updates reset toggles:** Annual updates like 24H2 can re-enable driver delivery you previously turned off.
- **Driver ranking quirks:** Windows considers a higher version number "better" even when the older OEM driver works better.
- **Rollback window is short:** Windows keeps the previous driver only briefly, making bad updates hard to undo later.
- **Third-party updaters compound the churn:** Driver utility apps fight Windows Update, destabilizing hardware further.
- **Optional updates sneak drivers in:** The "Optional updates" section quietly offers driver updates users install without realizing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Device Installation Settings

The simplest toggle, available on every Windows 11 edition.

1. Press Win + R, type `sysdm.cpl`, and press Enter.
2. Go to the Hardware tab and click "Device Installation Settings".
3. Choose "No (your device might not work as expected)" and click Save Changes.
4. Restart the laptop for the setting to take full effect.
5. Check Settings > Windows Update > Update history > Driver updates over the next week to confirm nothing new arrives.
6. Recheck this toggle after every Windows 11 feature update — they are notorious for flipping it back.

### Fix 2: Enable the Group Policy block (Pro and higher)

The policy method tells Windows Update itself to exclude drivers.

1. Press Win + R, type `gpedit.msc`, and press Enter.
2. Navigate to Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update.
3. Open "Do not include drivers with Windows Updates", set it to Enabled, and click OK.
4. Run `gpupdate /force` in an elevated Command Prompt to apply it immediately.
5. This is the method Microsoft documents for managed devices on their [Windows support pages](https://support.microsoft.com/en-us/windows).
6. Verify it holds by watching update history — driver entries should stop appearing entirely.

### Fix 3: Set the Registry block (Windows 11 Home)

Home edition lacks gpedit, but the registry enforces the identical block.

1. Press Win + R, type `regedit`, and press Enter. Export a backup via File > Export first.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`, creating the WindowsUpdate key if needed.
3. Create a new DWORD (32-bit) Value named `ExcludeWUDriversInQualityUpdate` and set it to `1`.
4. Close the editor and restart.
5. To undo later, set the value to `0` or delete the value.
6. This is the most reliable method on Home — prefer it over the basic toggle alone.

### Fix 4: Decline optional driver updates

Windows 11 lists driver updates under Optional updates, where they are easy to install accidentally.

1. Open Settings > Windows Update > Advanced options > Optional updates.
2. Expand "Driver updates" and review what is offered — do not install drivers for hardware that already works.
3. Uncheck any driver updates before clicking "Download & install" for other optional items.
4. Make a habit of checking this section rather than blindly installing everything optional.
5. If a driver you need is genuinely newer here, install only that one — then verify the hardware still works afterward.

### Fix 5: Hide a specific recurring driver update

When one driver keeps returning despite your blocks, hide just that update.

1. Download Microsoft's "Show or hide updates" troubleshooter (wushowhide.diagcab).
2. Run it, choose "Hide updates", and select the offending driver from the list.
3. Windows Update will skip it going forward while still offering everything else.
4. Run the tool again and choose "Show hidden updates" if you ever want it back.
5. This pairs well with the system-wide blocks: use the block for prevention and hiding for the stubborn exception.

### Fix 6: Roll back the damage, then lock the working driver in

If a bad driver is already installed, revert first so you are protecting a good state.

1. In Device Manager, open the affected device's Properties > Driver tab and click "Roll Back Driver".
2. If rollback is unavailable, uninstall the device with "Attempt to remove the driver" ticked, restart, and install the manufacturer's driver manually.
3. Immediately apply Fix 2 or Fix 3 so the bad version does not return overnight.
4. For elusive driver versions, search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) by hardware ID.
5. If an older driver package refuses to install on Windows 11, the [compatibility-mode install method](/articles/how-to-install-driver-in-compatibility-mode-on-windows-11/) usually gets it running.

### Fix 7: Verify and maintain the block

A block you never verify is a hope, not a configuration.

1. After applying your chosen method, note current driver versions for wireless, graphics, and audio in Device Manager.
2. Over the next two weeks, compare versions after Patch Tuesday and confirm nothing changed.
3. After each annual feature update, re-verify every setting in this guide — assume it was reset until proven otherwise.
4. Keep a simple log (a text file works) of which driver versions you installed manually and when.
5. Revisit manufacturer support pages quarterly for graphics and wireless updates worth installing by hand.

## Closing

Windows 11's driver enthusiasm is well-meant but frequently destructive to laptop hardware that was working perfectly. Pick the enforcement method that fits your edition, decline optional driver updates as a habit, and take manual ownership of the drivers that matter — wireless, graphics, audio, chipset. Do that, and the era of waking up to mysteriously broken hardware ends.
