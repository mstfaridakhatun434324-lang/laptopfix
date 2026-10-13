---
title: "DRIVER_POWER_STATE_FAILURE: Reddit's Best Fixes That Actually Work"
slug: how-to-fix-driver-power-state-failure-reddit
date: 2026-10-03
categories: ["windows-errors"]
tags: ["DRIVER_POWER_STATE_FAILURE", "Reddit fixes", "power management"]
description: "Fix DRIVER_POWER_STATE_FAILURE with Reddit's most confirmed solutions: power-plan tweaks, driver updates, fast startup fixes, and sleep-state repairs."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-reddit.webp"
faqs:
  - q: "What does DRIVER_POWER_STATE_FAILURE mean?"
    a: "It means a driver didn't respond correctly to a power-state change — usually when your laptop sleeps, hibernates, or wakes up. Stop code 0x9F fires when a driver takes too long to power down or up, or reports an inconsistent state. Wi-Fi, Bluetooth, and graphics drivers are the usual offenders on laptops."
  - q: "Why does this error happen when my laptop wakes from sleep?"
    a: "Sleep and wake are the moments drivers must switch power states, so any driver with a power-management bug shows itself there. Outdated network drivers, aggressive link-state power management, and fast startup's hybrid shutdown are the classic triggers. The crash dump almost always names the misbehaving driver."
  - q: "Which fix works most often according to Reddit?"
    a: "Across r/techsupport threads, the top fixes are: turning off fast startup, updating Wi-Fi and chipset drivers, changing the PCI Express link-state power management to moderate or off, and updating the BIOS. Disabling fast startup alone resolves a remarkable number of cases because it forces a true full shutdown."
  - q: "Can this error damage my laptop's hardware?"
    a: "No — it's a software timeout, not a hardware fault signal. The crash itself is Windows protecting the system from a driver stuck in a bad power state. That said, repeated forced shutdowns from crashes aren't great for open files, so fix the underlying driver rather than living with the crashes."
---

DRIVER_POWER_STATE_FAILURE (stop code `0x9F`) is the blue screen of bad naps: it strikes when your laptop sleeps, hibernates, shuts down, or wakes up, because some driver fumbled the power-state handoff. Reddit's laptop communities have chased this one for years, and the fix list has stabilized into a reliable order.

The pattern is consistent — network drivers first, power settings second, BIOS third. Work this list top-down and you'll find the culprit. It's a close relative of the [DPC_WATCHDOG_VIOLATION](/articles/dpc-watchdog-violation-blue-screen-error-fix/) crash, which shares the same driver suspects.

## Why this happens

- Wi-Fi or Bluetooth drivers failing to handle sleep/wake power transitions correctly.
- Fast startup's hybrid shutdown leaving drivers in a half-powered limbo state.
- Aggressive PCI Express link-state power management starving a device of power during transitions.
- Outdated BIOS/UEFI firmware with buggy ACPI power-state tables.
- Graphics drivers (especially switchable Intel + NVIDIA/AMD setups) mishandling the wake sequence.
- USB devices or docks that don't resume cleanly, hanging the power IRP queue.
- Windows Update silently replacing a working manufacturer driver with a generic one that handles power states poorly.

## How to fix it

Work through these in order — Fixes 1 and 2 alone end a huge share of cases.

### Fix 1: Turn off fast startup

Reddit's single most upvoted fix for this error. Fast startup's hybrid shutdown is a notorious trigger.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do** in the left sidebar.
3. Click **Change settings that are currently unavailable**.
4. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
5. Shut down fully (not restart) and power back on — test sleep/wake cycles afterwards.

### Fix 2: Update Wi-Fi, Bluetooth, and chipset drivers

Network drivers are the top driver-side cause; update them from the right source.

1. Identify your Wi-Fi chip in **Device Manager > Network adapters** (Intel, Realtek, MediaTek, or Qualcomm).
2. Download the latest driver from the chip maker's site — or use [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel hardware.
3. Update **Bluetooth** drivers the same way; they're often bundled with Wi-Fi.
4. Install the latest **chipset** driver from your laptop maker's support page.
5. Restart, then test several sleep/wake cycles in a row.

### Fix 3: Adjust PCI Express link-state power management

This setting lets Windows aggressively power down PCIe devices — great for battery, bad for buggy drivers.

1. Open **Control Panel > Power Options** and click **Change plan settings** on your active plan.
2. Click **Change advanced power settings**.
3. Expand **PCI Express > Link State Power Management**.
4. Set it to **Moderate power savings** (or **Off** for testing) on both battery and plugged in.
5. Click **Apply** and test sleep/wake behavior for a day.

### Fix 4: Update the BIOS/UEFI firmware

The BIOS owns the ACPI tables that describe power states to Windows — old firmware means wrong descriptions.

1. Check your current BIOS version: press **Win + R**, type `msinfo32`, and note **BIOS Version/Date**.
2. Visit your laptop maker's support site and compare against the latest for your exact model.
3. Download and run the BIOS update **with the charger plugged in** — never on battery.
4. Do not interrupt the update; the laptop will restart itself.
5. After updating, load BIOS defaults once, then retest sleep/wake.

### Fix 5: Identify the driver from the crash dump

If the above didn't nail it, let the dump name the driver so you stop guessing.

1. Open the latest `.dmp` in `C:\Windows\Minidump` with **WinDbg Preview**.
2. Run `!analyze -v` after configuring symbols.
3. The fourth parameter of the `0x9F` bug check identifies the blocked IRP; **IMAGE_NAME** names the driver.
4. The dump commonly names `Netwtw10.sys`/`Netwtw12.sys` (Intel Wi-Fi), `rtwlanu.sys` (Realtek), or a USB driver.
5. Update or replace that specific driver — or disable the device in **Device Manager** as a test.

### Fix 6: Change the sleep configuration

Sometimes the fix is avoiding the problematic power state entirely.

1. Open **Settings > System > Power & battery > Screen and sleep** and set sleep to **Never** temporarily as a test.
2. If crashes stop, the issue is specifically in the sleep/wake path.
3. In an elevated Command Prompt, run `powercfg /a` to see which sleep states your hardware supports.
4. If **Modern Standby (S0)** is in use, check for a BIOS option to prefer **S3** sleep instead.
5. Alternatively, use **Hibernate** instead of **Sleep** — it powers everything fully off.

### Fix 7: Disconnect USB devices and docks

External devices with bad resume behavior hang the whole power transition.

1. Unplug all USB devices, docks, and external drives.
2. Test sleep/wake with nothing attached for a full day.
3. Reconnect devices one at a time, testing sleep after each.
4. For the offending device, check the maker's site for firmware updates.
5. In **Device Manager**, you can also uncheck **Allow the computer to turn off this device to save power** on the device's **Power Management** tab as a workaround.

### Fix 8: Reset the power plans to defaults

Years of tweaks can leave power plans in contradictory states.

1. Open an elevated Command Prompt.
2. Run `powercfg -restoredefaultschemes` to reset all plans to factory defaults.
3. Restart the laptop.
4. Re-apply only the changes you need, testing sleep/wake after each.
5. If crashes persist after all of this, the [Windows support hub](https://support.microsoft.com/en-us/windows) documents advanced power troubleshooting, or consider a repair install.

## Closing

DRIVER_POWER_STATE_FAILURE is Windows catching a driver asleep at the wheel during power transitions — and the fix is almost always in the power path: fast startup off, network drivers current, PCIe power management tamed, BIOS fresh. Reddit's collective experience converges on this order for a reason. Apply it, test with real sleep/wake cycles over several days, and the 0x9F screen becomes permanent history. Keep a note of the driver versions that work, so the next Windows update can't silently undo your fix. If your crashes happen during startup rather than sleep, our [startup BSOD guide](/articles/how-to-fix-bsod-on-startup-windows-11-on-dell-laptop/) covers that side of the problem.
