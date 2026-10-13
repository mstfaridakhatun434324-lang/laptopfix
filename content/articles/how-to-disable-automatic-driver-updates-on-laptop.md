---
title: "How to Disable Automatic Driver Updates on Your Laptop"
slug: how-to-disable-automatic-driver-updates-on-laptop
date: 2026-10-06
categories: ["drivers"]
tags: ["automatic driver updates", "windows update drivers", "disable driver updates", "group policy", "registry"]
description: "Stop Windows from replacing your working drivers with bad updates. Disable automatic driver updates on your laptop using Device Installation Settings, Group Policy, or the Registry."
thumbnail: "/images/thumbs/how-to-disable-automatic-driver-updates-on-laptop.webp"
faqs:
  - q: "Will disabling automatic driver updates break Windows Update?"
    a: "No. Disabling driver delivery only stops Windows Update from installing hardware drivers. Security patches, cumulative updates, and feature updates keep arriving normally. You simply take over driver maintenance yourself, installing new versions from your laptop maker's support site when you choose. Most stable setups run this way for years without issues."
  - q: "Can I block just one bad driver instead of all of them?"
    a: "Yes, and it is often the better move. Use the wushowhide troubleshooter or the Group Policy setting that excludes specific device IDs, then roll back the bad driver in Device Manager. This keeps useful updates flowing while quarantining the one driver that broke your audio, Wi-Fi, or graphics."
  - q: "Does this setting survive Windows feature updates?"
    a: "Sometimes not. Major feature updates have been known to reset driver policies and re-enable automatic driver installation. After each feature update, verify your Group Policy or registry setting is still in place and reapply it if needed. A quick check takes under a minute."
  - q: "Is it safe to disable driver updates on Windows 11 Home?"
    a: "Yes, using the registry method, since Home lacks Group Policy. The setting is fully reversible — delete the key and automatic driver delivery returns. Just remember you are now responsible for checking your manufacturer's support page for important driver fixes yourself."
---

Automatic driver updates are one of those Windows features that work perfectly until they don't. One morning your laptop installs a new graphics driver overnight, and suddenly games stutter, the second monitor flickers, or the Wi-Fi drops every twenty minutes. The driver that arrived was technically newer — it was also technically worse for your specific machine.

Here is what happens behind the scenes: Windows Update ranks candidate drivers for your hardware from Microsoft's catalog and pushes the winner automatically. That ranking does not know your laptop maker's customized Realtek audio build sounds better than the generic one, or that a specific NVIDIA release breaks your dock. When the catalog disagrees with your laptop, you lose.

This guide shows you how to take control using three methods — the simple GUI toggle, Group Policy for Pro editions, and a registry edit for Home editions — plus how to block individual bad drivers and install them manually. Work through these in order — diagnose first, then act.

## Why this happens


- **Windows Update driver ranking:** Microsoft's servers score available drivers for your hardware IDs and install the highest-ranked match automatically, with no prompt and no rollback warning.
- **Generic drivers beating customized OEM builds:** Laptop makers tune drivers for their specific audio chips, thermal designs, and displays. Windows often replaces these with generic vendor drivers that lose those customizations.
- **Driver and OS release cycles misaligned:** A driver that passes Microsoft's tests on one Windows build can misbehave after the next cumulative update changes something underneath it.
- **Device Installation Settings default to Yes:** Out of the box, Windows is configured to download manufacturer apps and drivers automatically. Most users never touch this toggle.
- **Feature updates reset policies:** Major Windows upgrades occasionally revert driver-related policies and registry keys to defaults, silently re-enabling automatic driver installation.
- **No per-driver consent on Home editions:** Windows Home offers no built-in prompt before driver installs — updates simply arrive with the normal patch cycle.
- **Third-party updaters piling on:** Tools like manufacturer updaters and driver-utility apps can install their own driver versions on top of Windows Update's, creating version conflicts.
- **Staged drivers activating late:** Sometimes a driver downloads weeks before it activates, so the breakage appears to come out of nowhere long after the actual download.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Confirm automatic updates are the culprit


Before disabling anything, verify a driver update actually caused your problem. A two-minute check in Update history shows which driver arrived and when.

1. Open Settings, then Windows Update, then Update history.
2. Scroll to Driver updates and note the most recent entries and their dates.
3. Match those dates against when your problem started.
4. If a driver update lines up with the breakage, roll it back in Device Manager (right-click the device, Properties, Driver tab, Roll Back Driver) and then proceed to block future updates.
5. If no driver update appears, your issue likely has a different cause — check our driver troubleshooting guides first.

### Fix 2: Turn off driver downloads in Device Installation Settings


This is the simplest method and works on every Windows edition. It tells Windows not to fetch manufacturer apps and drivers automatically. It is not the strongest block, but it stops the routine updates.

1. Press Windows + R, type sysdm.cpl, and press Enter to open System Properties.
2. Go to the Hardware tab and click Device Installation Settings.
3. Select No (your device might not work as expected), then click Save Changes.
4. Restart your laptop so the change takes effect cleanly.
5. Note that this setting mainly governs initial device setup drivers; for bulletproof control, combine it with Fix 3 or Fix 4 below. For the Windows 11-specific walkthrough, see our guide to [disabling automatic driver updates on Windows 11](/articles/how-to-disable-automatic-driver-updates-on-windows-11/).

### Fix 3: Block driver updates with Group Policy (Pro, Enterprise, Education)


Group Policy gives you the strongest native control. The dedicated policy tells Windows Update to skip drivers entirely, and unlike the GUI toggle it is enforced at the update-client level. If you run Windows Pro or higher, this is the method to use.

1. Press Windows + R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, Windows Update, then Manage updates offered from Windows Update.
3. Double-click Do not include drivers with Windows Updates and set it to Enabled.
4. Click Apply, then OK.
5. Run gpupdate /force in an elevated Command Prompt to apply immediately.
6. Verify by checking Windows Update — future driver entries should stop appearing while security updates continue normally.

### Fix 4: Block driver updates with the Registry (Windows Home)


Windows Home has no Group Policy editor, but the same setting lives in the registry. This edit is safe, reversible, and takes effect after a restart. You are writing one value that the update client reads on every scan.

1. Press Windows + R, type regedit, and press Enter. Approve the UAC prompt.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate.
3. If the WindowsUpdate key does not exist, right-click the Windows key, choose New, Key, and name it WindowsUpdate.
4. Right-click in the right pane, choose New, DWORD (32-bit) Value, and name it ExcludeWUDriversInQualityUpdate.
5. Double-click it and set the value data to 1, then click OK.
6. Restart your laptop. Automatic driver delivery is now off.
7. To reverse it later, set the value to 0 or delete the DWORD.

### Fix 5: Hide a specific bad driver with the wushowhide tool


If you only want to stop one troublesome driver — say, the Realtek audio update that kills your sound every month — hiding it is cleaner than a blanket block. Microsoft's official show/hide troubleshooter removes selected updates from the offer list.

1. Download the wushowhide.diagcab troubleshooter from the official [Microsoft support site](https://support.microsoft.com/en-us/windows).
2. Run it and click Next, then choose Hide updates.
3. Select the driver update you want to block from the list.
4. Click Next to apply, then Close.
5. The hidden driver will no longer be offered. If you ever want it back, rerun the tool and choose Show hidden updates.
6. Install a known-good version of that driver manually from your laptop maker's support page instead.

### Fix 6: Use a metered connection or pause updates as a temporary hold


Sometimes you need breathing room after a driver breaks something. Pausing updates or marking your connection as metered buys you time without permanent changes.

1. Open Settings, then Windows Update.
2. Click Pause updates and choose a duration of up to five weeks.
3. For a metered connection: Settings, Network & internet, Wi-Fi or Ethernet, your connection, then turn on Metered connection.
4. Windows will hold back most driver and feature downloads on metered networks.
5. Use the pause window to find and install the correct driver manually, then unpause when ready.

### Fix 7: Install drivers manually and keep them pinned


Disabling automatic updates only works if you take over the job. The right source is your laptop manufacturer's support page, which hosts drivers validated for your exact model — not generic builds from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) that may lack OEM customizations.

1. Find your exact model number on the sticker under the laptop or in System Information.
2. Visit your maker's support site and download the driver set for your Windows version.
3. Install in this order: chipset, graphics, audio, network, then everything else.
4. After each install, restart and verify the device works in Device Manager.
5. Bookmark the support page and check it quarterly — you are now the update manager.
6. For deeper control of individual installs, see our guide to [manually installing OEM drivers](/articles/how-to-install-oem-drivers-manually-on-windows-11/).

## Closing


Disabling automatic driver updates is one of the highest-leverage stability tweaks a laptop owner can make. You trade Microsoft's convenience for your manufacturer's tested drivers and your own schedule — and on machines where a single bad graphics or audio driver can ruin a week, that trade is worth it. Set it once, check it after each feature update, and your drivers will stay exactly where you put them.
