---
title: "Fix Driver Power State Failure on Your ASUS Laptop"
slug: how-to-fix-driver-power-state-failure-on-asus-laptop
date: 2026-10-09
categories: ["windows-errors"]
tags: ["blue screen", "driver power state failure", "asus laptop", "bsod fix"]
description: "Driver Power State Failure crashing your ASUS laptop on sleep or wake? Fix it with driver reinstalls, Armoury Crate tweaks, and power-setting changes."
thumbnail: "/images/thumbs/how-to-fix-driver-power-state-failure-on-asus-laptop.webp"
faqs:
  - q: "Why does my ASUS laptop crash with Driver Power State Failure?"
    a: "A driver fails to complete a power transition — sleep, hibernate, shutdown, or wake — within Windows' timeout. On ASUS laptops the repeat offenders are the Wi-Fi driver, the NVIDIA/AMD graphics driver, and ASUS utilities like Armoury Crate and MyASUS that meddle with power profiles. Fast Startup and aggressive PCI Express power saving make it worse."
  - q: "Does Armoury Crate cause this blue screen?"
    a: "It can. Armoury Crate switches power profiles and fan curves dynamically, and its background services sometimes conflict with Windows' own power management during sleep transitions. If crashes started after an Armoury Crate update, try disabling its power-profile switching or uninstalling it temporarily as a test."
  - q: "Will updating the BIOS fix Driver Power State Failure?"
    a: "Sometimes. ASUS BIOS updates frequently include fixes for modern standby and power-state handling. Check your current BIOS version with `msinfo32` and compare it against the latest on ASUS support for your exact model. But update drivers and power settings first — BIOS flashing is a last resort, not a first step."
  - q: "How do I know which driver is causing it?"
    a: "Check **Event Viewer > Windows Logs > System** for warnings in the minutes before each crash — the stalled driver is often named. You can also run `powercfg /energy` in an elevated Command Prompt to generate a power-efficiency report that flags misbehaving drivers and devices."
---

If your ASUS laptop blue-screens with DRIVER_POWER_STATE_FAILURE every time it sleeps, wakes, or shuts down, you're dealing with a driver that can't handle power transitions. Windows asks every driver to power down or wake up in an orderly fashion; one driver dawdles past the timeout, and Windows crashes the whole system rather than risk corruption.

ASUS machines have their own flavor of this problem thanks to Armoury Crate, MyASUS, and the mix of MediaTek/Intel Wi-Fi cards ASUS ships. The good news: it's fixable without new hardware in nearly every case.

## Why this happens

- **Wi-Fi driver stalling on sleep/wake.** MediaTek and Intel wireless drivers are the number-one cause on ASUS laptops — they fail to suspend or resume cleanly.
- **GPU driver power-state bugs.** NVIDIA and AMD drivers that mishandle the transition between performance and low-power states crash on lid-close or wake.
- **Armoury Crate or MyASUS interfering.** These utilities switch power plans and fan profiles on the fly, occasionally colliding with Windows' own power management mid-transition.
- **Fast Startup's hybrid shutdown.** Drivers stay half-loaded between sessions, and a driver that can't handle the resume path crashes on the next boot.
- **PCI Express Link State Power Management set too aggressively.** Maximum power savings can starve a device of the time it needs to respond.
- **USB devices blocking sleep.** Docks, external drives, and wireless receivers that refuse selective suspend hold up the whole transition.
- **Outdated BIOS with buggy modern-standby handling.** Older firmware sometimes mismanages the sleep states Windows 11 expects.

## How to fix it

Work through these in order. Most ASUS cases are solved by the first three.

### Fix 1: Disable Fast Startup

The single most effective change for this stop code.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.
4. Perform a full shutdown and power on again. Test sleep and wake several times before moving on.

### Fix 2: Clean-reinstall the Wi-Fi driver

Get the driver from ASUS, not from Windows Update's generic pick.

1. Find your exact model on the sticker underneath the laptop.
2. Download the latest **WLAN** driver for your model from ASUS's official support download page.
3. Open **Device Manager** (**Win + X**), expand **Network adapters**, right-click the Wi-Fi adapter, and choose **Uninstall device**. Tick **Attempt to remove the driver for this device** if shown.
4. Install the ASUS driver package and restart. Test sleep/wake with the lid and the power button.

### Fix 3: Clean-reinstall the graphics driver

GPU drivers are the second most common trigger.

1. Download the current driver from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx), [AMD's driver page](https://www.amd.com/en/support/download/drivers.html), or Intel's detection tool at [Intel driver support](https://www.intel.com/content/www/us/en/support/detect.html), depending on your GPU.
2. For NVIDIA, choose **Custom install** and check **Perform a clean installation**. For AMD, use the **Factory Reset** option during install.
3. Restart and cycle sleep/wake a few times. If the crashes stop here, the old GPU driver was your culprit.

### Fix 4: Tame Armoury Crate and MyASUS

These utilities are useful, but their power-profile juggling can trigger exactly this crash.

1. Open Armoury Crate and check for updates first — ASUS does fix these bugs.
2. In Armoury Crate, set a fixed profile (e.g., **Silent** or **Performance**) instead of letting it auto-switch, and disable any "panel power saver" features temporarily.
3. As a diagnostic test, uninstall Armoury Crate and MyASUS from **Settings > Apps > Installed apps**, restart, and test sleep. If crashes vanish, reinstall only the utilities you actually use, one at a time.

### Fix 5: Run a power efficiency report

Let Windows point at the misbehaving driver or device.

1. Open **Terminal (Admin)** and run `powercfg /energy`. Leave the laptop idle for the 60-second trace.
2. Open the generated HTML report (the path is shown in the output, usually under `C:\Windows\System32`).
3. Look at the **Errors** and **Warnings** sections — they name devices and drivers with power-policy problems.
4. Update, disable, or replace whatever the report flags, then re-run the report to confirm.

### Fix 6: Relax PCI Express and USB power settings

Over-aggressive power saving starves devices of response time.

1. Go to **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **PCI Express > Link State Power Management** and set it to **Moderate power savings** (not Maximum).
3. Expand **USB settings > USB selective suspend setting** and set it to **Enabled**.
4. Expand **Sleep > Allow hybrid sleep** and set it to **Off**.
5. Apply and test sleep/wake cycles.

### Fix 7: Rebuild the hibernation file

If crashes cluster around hibernate, the hibernation file may be corrupt.

1. In **Terminal (Admin)**, run `powercfg /hibernate off` to delete `hiberfil.sys`.
2. Restart the laptop fully.
3. Run `powercfg /hibernate on` to rebuild the file.
4. Test with **Start > Power > Hibernate**, then wake the machine and watch for the crash.

### Fix 8: Update the BIOS

ASUS regularly ships standby and power-management fixes in BIOS updates.

1. Run `msinfo32` and note the **BIOS Version/Date**.
2. Compare against the latest BIOS for your exact model on ASUS's official support page.
3. Flash only with the charger connected, following ASUS's instructions exactly — a failed flash bricks the board.
4. After flashing, load optimized defaults in the BIOS before testing.

If crashes persist, inspect **Event Viewer > Windows Logs > System** around each crash timestamp — the stalling driver is frequently named there. This stop code has close cousins across brands: see our [Acer-specific guide](/articles/how-to-fix-driver-power-state-failure-on-acer-laptop/), the [general driver power state failure walkthrough](/articles/driver-power-state-failure-windows-11-fix/), and the [unexpected store exception fix](/articles/unexpected-store-exception-windows-11-fix/) for storage-flavored variants of the same family.

## Closing

On ASUS laptops, DRIVER_POWER_STATE_FAILURE is usually a Wi-Fi driver, a GPU driver, or Armoury Crate picking a fight with Windows over who controls sleep. Disable Fast Startup, reinstall those drivers cleanly, calm the ASUS utilities down, and your laptop will start sleeping and waking the way it should.
