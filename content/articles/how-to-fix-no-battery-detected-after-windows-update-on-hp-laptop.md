---
title: "No Battery Detected After a Windows Update on Your HP Laptop? Fix It Here"
slug: how-to-fix-no-battery-detected-after-windows-update-on-hp-laptop
date: 2026-09-17
categories: ["battery"]
tags: ["no battery detected", "hp laptop", "windows update", "battery driver", "acpi battery"]
description: "HP laptop says no battery detected after a Windows update? Reinstall the battery drivers and reset the hardware to bring it back."
thumbnail: "/images/thumbs/how-to-fix-no-battery-detected-after-windows-update-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop say no battery is detected after updating Windows?"
    a: "Windows Update often replaces HP's battery drivers with generic ones, or the ACPI battery driver fails to reload after the update. The battery is usually fine — the operating system has simply lost communication with it. Reinstalling the drivers typically restores detection within minutes."
  - q: "Can a Windows update physically damage my laptop battery?"
    a: "No. Updates can't damage battery cells. What they can do is install an incompatible driver or corrupt the driver stack that reports battery status. The 'no battery detected' message after an update is a software communication problem, not hardware damage."
  - q: "Should I use HP Support Assistant or Windows Update for battery drivers?"
    a: "Use HP's own drivers. HP Support Assistant or the HP support site provides battery and chipset drivers tested for your exact model. Windows Update's generic drivers work for most things, but HP-specific power management features need HP's drivers."
  - q: "What if the battery still isn't detected after reinstalling drivers?"
    a: "Run HP's built-in battery diagnostics from the UEFI menu (press Esc at boot, then F2). If the UEFI test also can't see the battery, you're looking at a hardware issue — a disconnected or failed battery — and it's time for service."
---

Nothing kills your confidence in an update like rebooting to a red X over the battery icon and the cheerful message "No battery detected." On HP laptops this shows up regularly after Windows updates, and the good news is that it's almost never a dead battery — it's Windows losing track of a battery that's sitting there perfectly fine.

HP machines rely on a small stack of drivers (ACPI battery, chipset, and HP's own power management pieces) to talk to the battery. A Windows update can replace one of those with a generic version, fail to reload it, or leave the driver stack in a confused state. Here's how to get Windows talking to your battery again.

## Why this happens

- **The Microsoft ACPI-Compliant Control Method Battery driver failed to reload** after the update and is stuck in an error state.
- **Windows Update installed a generic battery or chipset driver** over HP's tested version, breaking HP-specific communication.
- **The driver stack is corrupted** — the update was interrupted, or two drivers are now fighting over the same device.
- **Fast Startup cached the broken state.** The bad driver state gets saved into the hibernation file and reloaded on every "shutdown."
- **The EC (embedded controller) needs a reset.** The chip that manages battery communication can lock up during the update's reboots.
- **In rare cases, the battery connector worked loose** — but only suspect this if the UEFI diagnostics also can't see the battery.

## How to fix it

Work through these in order. Fix 1 alone resolves this for most people.

### Fix 1: Reinstall the ACPI battery drivers

This is the classic fix and it works because it forces Windows to rediscover the battery hardware from scratch.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**. You'll usually see **Microsoft AC Adapter** and **Microsoft ACPI-Compliant Control Method Battery**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. If Windows asks, do NOT tick "delete the driver software" — just uninstall.
4. Do the same for **Microsoft AC Adapter**.
5. Click **Action → Scan for hardware changes** in the Device Manager menu bar. Windows will redetect both devices and reinstall fresh drivers.
6. Restart the laptop. Check the battery icon — the red X should be gone.
7. If the icon still shows no battery, also try the generic version of this fix in our [step-by-step no battery detected guide](/articles/how-to-fix-no-battery-detected-after-windows-update-step-by-step/).

### Fix 2: Do a full shutdown to clear Fast Startup's cache

A normal shutdown with Fast Startup enabled doesn't fully reset drivers.

1. Press **Win + X**, choose **Terminal (Admin)**, and run `shutdown /s /t 0`. This performs a complete shutdown, bypassing Fast Startup.
2. Wait 30 seconds, then power the laptop back on.
3. Check whether the battery is now detected. If it is, consider turning off Fast Startup permanently at **Control Panel → Hardware and Sound → Power Options → Choose what the power buttons do → Change settings that are currently unavailable** — untick **Turn on fast startup**.

### Fix 3: Reset the embedded controller

The EC is the chip that actually talks to the battery. A hard reset clears its confused state.

1. Shut the laptop down completely and unplug the AC adapter.
2. If your HP has a removable battery, remove it. If it's internal (most modern HPs), skip this.
3. Press and hold the **power button for 15-20 seconds**. This drains residual power and resets the EC.
4. Reconnect the AC adapter (and battery if removed), then power on.
5. Give Windows a minute after boot to redetect the battery.

### Fix 4: Install HP's own battery and chipset drivers

If Windows Update replaced HP's drivers, put HP's back.

1. Go to [HP Support](https://support.hp.com/us-en) and enter your exact model or serial number.
2. Download the latest **chipset** driver and any **battery / power management** driver listed for your model.
3. Install the chipset driver first, restart, then install the battery-related driver and restart again.
4. Alternatively, install **HP Support Assistant** from the Microsoft Store and let it find the right drivers automatically.
5. After installing, repeat Fix 1 (uninstall the ACPI battery devices and scan for hardware changes) so Windows binds the new drivers cleanly.

### Fix 5: Roll back the problematic Windows update

If the battery vanished immediately after a specific update, that update is the prime suspect.

1. Go to **Settings → Windows Update → Update history**.
2. Scroll down and click **Uninstall updates**.
3. Find the most recent update (note the KB number and date), select it, and click **Uninstall**.
4. Restart and check battery detection. If it returns, pause updates for a week or two at **Settings → Windows Update → Pause updates** to avoid reinstalling the same broken update immediately.
5. Report the issue via **Feedback Hub** so Microsoft sees it.

### Fix 6: Run HP's UEFI battery diagnostics

Time to determine whether this is software or hardware.

1. Shut down the laptop, then power it on and immediately tap **Esc** repeatedly until the Startup Menu appears.
2. Press **F2** to open **HP PC Hardware Diagnostics UEFI**.
3. Choose **Component Tests → Power → Battery** and run the test.
4. If the UEFI test detects the battery and it passes, your hardware is fine — the problem is 100% in Windows, and a repair install (Fix 7) will sort it.
5. If the UEFI test says no battery is found, the battery is likely disconnected or dead. Contact HP support or a repair shop — and check our guide on [laptops that shut down when unplugged](/articles/how-do-i-fix-laptop-shuts-down-when-unplugged/) for what to expect.

### Fix 7: Repair Windows without losing your files

When the driver stack is thoroughly tangled, an in-place repair rebuilds it.

1. Go to [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and download the **Installation Assistant** or ISO.
2. Run setup from within Windows and choose **Keep personal files and apps**.
3. Let the repair complete — it reinstalls Windows system files and redetects all hardware, including the battery.
4. Afterward, reinstall HP's chipset drivers (Fix 4) before letting Windows Update run wild again.

## Closing

"No battery detected" after a Windows update on an HP is a driver communication failure, not a dead battery, in the overwhelming majority of cases. Reinstall the ACPI battery devices, do a true full shutdown, and put HP's own drivers back — one of those three steps brings the battery back for almost everyone.
