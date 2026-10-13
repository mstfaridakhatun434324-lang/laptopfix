---
title: "How to Disable Automatic Driver Updates on Windows 10"
slug: "how-to-disable-automatic-driver-updates-on-windows-10"
date: "2026-09-15"
categories: ["drivers"]
tags: ["driver updates", "windows update", "windows 10", "group policy", "device installation"]
description: "Stop Windows 10 from replacing your working drivers. Four reliable methods: Device Installation Settings, Group Policy, Registry, and metered connections."
thumbnail: "/images/thumbs/how-to-disable-automatic-driver-updates-on-windows-10.webp"
faqs:
  - q: "Why would I want to disable automatic driver updates?"
    a: "Windows Update sometimes replaces a stable manufacturer-tuned driver with a generic version that breaks hardware — Wi-Fi cards, touchpads, audio, and graphics are frequent victims. If you have a working driver from your laptop maker, blocking automatic driver updates keeps Windows from swapping it out. You still receive security and feature updates; only driver delivery through Windows Update is stopped."
  - q: "Does disabling driver updates stop all Windows updates?"
    a: "No. The methods in this guide target driver delivery specifically, either by blocking driver installation through Device Installation Settings or by policy. Security patches, cumulative updates, and feature updates continue normally. Your system stays protected; it just stops silently replacing hardware drivers that were working fine."
  - q: "Which method works on Windows 10 Home?"
    a: "Windows 10 Home lacks the Group Policy Editor, so use the Device Installation Settings method or the Registry method instead. Both work on Home and Pro. The Registry method is the most thorough on Home because it enforces the block at the same level Group Policy does. The metered connection trick also works on any edition as a supplementary measure."
  - q: "How do I update drivers manually after disabling automatic updates?"
    a: "Download drivers from your laptop manufacturer's support site for your exact model, or from the component maker such as Intel, NVIDIA, or AMD. Install them manually and restart. For security-related driver needs, you can also fetch specific drivers from the Microsoft Update Catalog. Check for new manufacturer drivers every few months, especially graphics and wireless drivers."
---

Windows 10's habit of silently replacing working drivers is behind an enormous share of laptop hardware mysteries: Wi-Fi that dies overnight, a touchpad that loses gestures, audio that goes silent. The driver Windows Update installs is not always the driver your hardware needs — manufacturers tune drivers for specific models, and the generic replacements can break things. This guide shows four ways to stop Windows 10 from touching your drivers, from the simple toggle to the bulletproof policy method.

A quick note on scope: these methods stop driver delivery through Windows Update. They do not stop security updates, and they do not prevent you from installing drivers manually. That is exactly the balance most laptop owners want.

## Why this happens

- **Windows Update prioritizes newer over better:** A numerically newer generic driver replaces your older manufacturer-tuned driver, even when the generic one works worse.
- **OEM customizations get wiped:** Laptop makers customize wireless, audio, and graphics drivers; generic replacements drop those tweaks.
- **Silent installation:** Driver updates install without meaningful notification, so the breakage seems to happen "by itself."
- **No easy per-driver block:** Windows offers no built-in "never update this driver" button, forcing the system-wide methods below.
- **Feature updates reset settings:** Major Windows 10 updates can re-enable driver delivery you previously disabled.
- **Driver rollback windows expire:** Windows only keeps the previous driver briefly, so a bad update becomes permanent quickly.
- **Third-party tools conflict:** Driver updater utilities fight Windows Update, producing driver churn that destabilizes hardware.
- **Metered connections are ignored for drivers:** Even on metered connections, Windows may still push "important" driver updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Device Installation Settings (easiest)

This is the official user-facing toggle and works on all Windows 10 editions.

1. Press Win + R, type `sysdm.cpl`, and press Enter to open System Properties.
2. Go to the Hardware tab and click "Device Installation Settings".
3. Select "No (your device might not work as expected)" — despite the warning, this only stops automatic driver downloads.
4. Click "Save Changes" and restart the laptop.
5. Verify by checking Windows Update history after a few days: no new driver entries should appear.
6. Note that major feature updates can flip this back, so recheck it after each one.

### Fix 2: Block driver updates with Group Policy (Pro and Enterprise)

The policy method is stronger — Windows Update itself is told not to include drivers.

1. Press Win + R, type `gpedit.msc`, and press Enter.
2. Navigate to Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update.
3. Double-click "Do not include drivers with Windows Updates" and set it to Enabled.
4. Click OK and close the editor.
5. Open an elevated Command Prompt and run `gpupdate /force` to apply the policy immediately.
6. This survives reboots and is the method Microsoft documents on their [Windows support pages](https://support.microsoft.com/en-us/windows) for managed devices.

### Fix 3: Block driver updates with the Registry (all editions)

The registry method enforces the same block as Group Policy and works on Windows 10 Home.

1. Press Win + R, type `regedit`, and press Enter. Back up the registry first via File > Export.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`.
3. If the WindowsUpdate key does not exist, right-click Windows, choose New > Key, and name it `WindowsUpdate`.
4. Inside it, right-click empty space, choose New > DWORD (32-bit) Value, and name it `ExcludeWUDriversInQualityUpdate`.
5. Double-click it and set the value data to `1`.
6. Close the editor and restart the laptop for the change to take full effect.
7. To reverse it later, set the value to `0` or delete it.

### Fix 4: Set your connection as metered (supplementary)

Metered connections tell Windows to hold back most automatic downloads, including many drivers.

1. Open Settings > Network & Internet > Wi-Fi (or Ethernet) and click your connection.
2. Turn on "Set as metered connection".
3. Repeat for every network you regularly use — the setting is per-connection.
4. Be aware this also limits some app updates and background sync, which is usually acceptable.
5. Use this alongside Fix 1 or Fix 3, not instead of them, since Windows can still push critical drivers on metered links.

### Fix 5: Hide a specific problematic driver update

If one particular driver keeps coming back, hide just that update instead of blocking all drivers.

1. Download Microsoft's "Show or hide updates" troubleshooter package (wushowhide.diagcab).
2. Run it, click Next, then choose "Hide updates".
3. Select the offending driver update from the list and click Next to hide it.
4. Windows Update will skip that driver from now on while still offering others.
5. If you later want it back, run the tool again and choose "Show hidden updates".
6. This is ideal when exactly one driver (say, the touchpad) misbehaves but you are fine with other driver updates.

### Fix 6: Roll back and pin the working driver

If a bad driver is already installed, revert first, then apply your chosen block.

1. Open Device Manager, right-click the affected device, and choose Properties.
2. On the Driver tab, click "Roll Back Driver" and give a reason.
3. Immediately apply Fix 1, 2, or 3 so Windows does not reinstall the bad driver overnight.
4. Download the manufacturer's known-good driver and install it manually to pin the version.
5. For hard-to-find drivers, search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the exact version you want.
6. The [Windows 11 version of this guide](/articles/how-to-disable-automatic-driver-updates-on-windows-11/) covers the same techniques with Windows 11's reorganized Settings paths.

### Fix 7: Verify the block is holding

Do not assume — confirm Windows Update is actually leaving your drivers alone.

1. Go to Settings > Update & Security > Windows Update > View update history.
2. Check the Driver Updates section over the next week for new entries.
3. In Device Manager, note your key driver versions (wireless, graphics, audio) and compare after updates run.
4. If a driver still slips through, you likely need the Group Policy or Registry method rather than just Device Installation Settings.
5. Recheck these settings after every Windows 10 feature update, which can reset them.

## Closing

Disabling automatic driver updates is one of the highest-value stability tweaks a Windows 10 laptop owner can make. Pick the method that matches your edition — Device Installation Settings for simplicity, Group Policy or Registry for enforcement — then take ownership of your drivers by installing manufacturer packages manually. If a legacy package refuses to cooperate, the [compatibility-mode install method](/articles/how-to-install-driver-in-compatibility-mode-on-windows-10/) gets older drivers running. Your Wi-Fi card, touchpad, and audio chip will thank you with the rarest of Windows qualities: staying exactly as they were yesterday.
