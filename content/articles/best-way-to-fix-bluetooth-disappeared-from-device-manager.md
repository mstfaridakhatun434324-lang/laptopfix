---
title: "Best Way to Fix Bluetooth Disappeared From Device Manager"
slug: best-way-to-fix-bluetooth-disappeared-from-device-manager
date: 2026-09-08
categories: ["drivers"]
tags: ["bluetooth disappeared", "bluetooth missing device manager", "bluetooth driver fix"]
description: "Bluetooth disappeared from Device Manager? Restore the missing Bluetooth adapter with driver reinstalls, service restarts, and BIOS checks."
thumbnail: "/images/thumbs/best-way-to-fix-bluetooth-disappeared-from-device-manager.webp"
faqs:
  - q: "Why did Bluetooth vanish from Device Manager?"
    a: "The Bluetooth driver usually failed to load after a Windows update, leaving the adapter undetected. It can also be disabled in BIOS, stuck in a power-saving state, or — on combo Wi-Fi/Bluetooth cards — affected by the wireless driver. Hardware failure is the least common cause."
  - q: "Is Bluetooth part of the Wi-Fi card?"
    a: "On most modern laptops, yes. Bluetooth and Wi-Fi share a single M.2 combo card (commonly Intel or MediaTek), though they use separate drivers. That is why Bluetooth and Wi-Fi problems often appear together — and why reinstalling the wireless driver package sometimes fixes both."
  - q: "Will reinstalling Windows bring Bluetooth back?"
    a: "It can, but it is overkill. A clean reinstall of the Bluetooth and chipset drivers fixes the problem in nearly all software cases without wiping your system. Reserve a Windows reinstall for situations where multiple subsystems are broken simultaneously. An in-place repair install is the middle ground if you want to refresh Windows without losing apps and files."
  - q: "What if Bluetooth is missing even in the BIOS?"
    a: "If the BIOS setup shows no Bluetooth device or toggle, the firmware cannot see the hardware — that points to a physical problem with the combo card or its connection. Reseating the M.2 card or replacing it are the remaining options."
---

Bluetooth was there yesterday — today the toggle is gone from Settings, the icon is missing from the taskbar, and Device Manager shows no Bluetooth section at all. Not disabled, not error-flagged: simply absent. This "disappeared" variant is distinct from Bluetooth that is present but not working, and it has its own set of causes centered on driver loading and hardware enumeration.

Because most laptop Bluetooth lives on the Wi-Fi combo card, the fixes below cover both the Bluetooth-specific driver path and the shared hardware underneath. Follow them in order; the adapter reappears at one of these stages in nearly every software-caused case.

## Why this happens

- **Bluetooth driver failed to load:** A Windows update replaced or corrupted the Bluetooth driver, so the adapter never enumerates.
- **Bluetooth Support Service stopped:** The background service Bluetooth depends on is disabled or crashed.
- **Disabled in BIOS:** A firmware toggle for Bluetooth (sometimes grouped under wireless) got switched off.
- **Airplane mode or radio kill:** A stuck airplane mode state or hardware radio switch hides the Bluetooth radio along with Wi-Fi.
- **Power management suspension:** USB power saving suspends the Bluetooth radio's USB interface permanently.
- **Combo card driver mismatch:** The Wi-Fi driver updated but the Bluetooth driver did not (or vice versa), breaking the shared card's initialization.
- **Fast startup stale state:** The cached boot state preserves a failed Bluetooth enumeration across restarts.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check for hidden devices and the Bluetooth service

Determine whether Bluetooth is hidden, stopped, or truly gone.

1. Open Device Manager, click **View > Show hidden devices**, and look for a grayed-out **Bluetooth** section.
2. Press **Win + R**, type `services.msc`, and find **Bluetooth Support Service**. Set its **Startup type** to **Automatic** and start it if stopped. Do the same for **Bluetooth Audio Gateway Service** if present.
3. Restart and check Settings > **Bluetooth & devices** for the toggle.

If the service was the problem, Bluetooth returns immediately. If the service will not stay running, the driver underneath is broken — continue below.

### Fix 2: Reinstall the Bluetooth driver from the manufacturer

The primary fix for update-broken Bluetooth enumeration.

1. Identify your combo card (Intel AX200/AX210, MediaTek, Realtek, or Qualcomm) from your laptop's specs or the hidden Device Manager entry.
2. Download the **Bluetooth** driver for your exact model from [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), [Lenovo Support](https://support.lenovo.com/us/en/), or the Intel Driver & Support Assistant.
3. In Device Manager (show hidden devices), right-click any Bluetooth entries, choose **Uninstall device**, and check driver removal.
4. Install the downloaded driver and restart.

Install the matching **Wi-Fi driver** too when using a combo card — the two drivers initialize the shared hardware together, and mismatched pairs are a classic disappearance cause. Our [Bluetooth not working guide](/articles/best-way-to-fix-bluetooth-not-working/) covers the next layer if the adapter returns but will not connect.

### Fix 3: Run the Bluetooth troubleshooter

Windows' automated troubleshooter catches service and configuration issues quickly.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Bluetooth** troubleshooter and apply its recommendations.
3. Restart afterward even if it reports no problems found.

The troubleshooter is not magic, but it resets several Bluetooth services and stack components in one pass, which resolves the simpler disappearance cases.

### Fix 4: Disable USB selective suspend and adapter power saving

Bluetooth radios connect via internal USB, so USB power saving can silence them.

1. In **Control Panel > Power Options > Change advanced power settings**, set **USB selective suspend** to **Disabled**.
2. In Device Manager, expand **Universal Serial Bus controllers**, and on each **USB Root Hub** uncheck **Allow the computer to turn off this device to save power** under **Power Management**.
3. If a Bluetooth entry is visible, uncheck power saving on it too.
4. Restart.

This prevents Windows from parking the Bluetooth radio in a suspended state it cannot wake from — a common cause of Bluetooth that disappears after sleep.

### Fix 5: Check BIOS for the Bluetooth toggle

Firmware-level disablement hides Bluetooth from Windows completely.

1. Reboot into BIOS/UEFI setup.
2. Look for **Bluetooth**, **Wireless**, or **BT** toggles under Advanced or Devices sections.
3. Enable it, save, and boot into Windows.
4. If the BIOS has no Bluetooth entry at all, note that — it suggests the firmware cannot see the combo card hardware.

Some BIOS versions group Bluetooth under a single "Wireless" switch shared with Wi-Fi. If Wi-Fi also misbehaves, treat them as one problem on the shared card.

### Fix 6: Clear airplane mode and radio states

A stuck radio state hides Bluetooth alongside Wi-Fi.

1. Go to **Settings > Network & internet > Airplane mode** and ensure it is **Off**.
2. Check for a physical wireless switch or **Fn** radio key on the laptop and toggle it.
3. In an elevated Command Prompt, run `netsh winsock reset` and restart.

If airplane mode is stuck on, our [airplane mode fix guide](/articles/best-way-to-fix-airplane-mode-stuck-on/) addresses that root cause directly — Bluetooth returns once the radio state clears.

### Fix 7: Cold-boot reset and hardware check

The last software step before suspecting the card itself.

1. Shut down fully, unplug the charger, and hold the power button for 30 seconds (drains residual power and resets the embedded controller).
2. Power on and check Device Manager.
3. If Bluetooth is still absent, test with a USB Bluetooth dongle — if the dongle works, the internal combo card or its connection is at fault.
4. Reseat or replace the M.2 combo card if you are comfortable opening the laptop; otherwise contact manufacturer support.

Also consider [blocking automatic driver updates](/articles/best-way-to-disable-automatic-driver-updates/) once Bluetooth works, since a bad update is what broke it in the first place.

## Closing

Bluetooth that disappears from Device Manager is a driver-loading or enumeration failure far more often than a hardware death. Restart the Bluetooth Support Service, reinstall the matched Bluetooth (and Wi-Fi) driver from your laptop maker, and check the BIOS toggle — the adapter reappears at one of those steps on the vast majority of laptops.
