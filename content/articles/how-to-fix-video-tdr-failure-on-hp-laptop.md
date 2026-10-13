---
title: "How to Fix VIDEO_TDR_FAILURE on an HP Laptop"
slug: how-to-fix-video-tdr-failure-on-hp-laptop
date: 2026-09-27
categories: ["windows-errors"]
tags: ["bsod", "video-tdr-failure", "hp-laptop"]
description: "VIDEO_TDR_FAILURE blue screen on your HP laptop? Clean-reinstall the GPU driver and fix heat and power causes with this guide."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-hp-laptop.webp"
faqs:
  - q: "Why does my HP laptop get VIDEO_TDR_FAILURE?"
    a: "Usually a corrupted or outdated graphics driver — HP laptops commonly ship with NVIDIA, AMD, or Intel graphics, and a bad driver update through Windows Update or HP Support Assistant can destabilize any of them. Overheating in the slim chassis and underpowered chargers are the next most common causes."
  - q: "Should I use HP's drivers or the GPU maker's drivers?"
    a: "Start with HP's drivers from HP Support Assistant or the support site, because they're validated for your exact model's power and thermal limits. If HP's driver is old and crashing, try the GPU maker's latest stable release as a second option."
  - q: "Can HP Support Assistant fix this automatically?"
    a: "Sometimes — it can detect and install missing or outdated drivers, which resolves straightforward cases. But it won't do a truly clean driver removal, so for persistent TDR crashes you still need the manual DDU process in this guide."
  - q: "Is it safe to open my HP laptop to clean the fans?"
    a: "Blowing compressed air through the exterior vents is safe. Opening the chassis may void the warranty on newer models, so check your warranty status first — if it's covered, let HP service handle internal cleaning and repasting."
---
# How to Fix VIDEO_TDR_FAILURE on an HP Laptop

**VIDEO_TDR_FAILURE** on an HP laptop usually names a driver file like `nvlddmkm.sys` (NVIDIA), `amdkmdag.sys` (AMD), or `igdkmd64.sys` (Intel). Translation: your graphics driver hung, Windows tried to reset it, and the reset failed. The fix is the same family of steps as on any laptop, with a few HP-specific twists around drivers, thermals, and power.

HP's slim chassis designs run warm, and Windows Update loves pushing generic GPU drivers over HP's validated ones — both feed this crash. Work through the fixes below in order. For the related family of driver power errors, see our [driver power state failure guide](/articles/driver-power-state-failure-windows-11-fix/).

## Why this happens

- **Corrupted GPU driver:** A bad update — via Windows Update, HP Support Assistant, or manual install — is the top cause.
- **Generic driver replacing HP's validated one:** Windows Update sometimes overwrites HP's tuned driver with a generic version that doesn't respect the laptop's thermal limits.
- **Overheating in the slim chassis:** Dust buildup hits thin HP models (Pavilion, Envy, Spectre) hard under sustained GPU load.
- **Underpowered or failing charger:** HP laptops throttle or crash when the adapter can't deliver full wattage.
- **Unstable graphics switching:** MUX/Optimus-style switching between integrated and discrete GPUs glitching during transitions.
- **Failing GPU hardware:** Rare, but possible — usually announced by visual artifacts before the crashes start.

## How to fix it

Work through these in order. HP-specific steps are marked so you can spot them.

### Fix 1: Identify the failing driver file

Knowing which GPU is crashing focuses every step after this.

1. Read the filename in parentheses after VIDEO_TDR_FAILURE on the blue screen.
2. `nvlddmkm.sys` = NVIDIA, `amdkmdag.sys` = AMD, `igdkmd64.sys` = Intel.
3. If it flashes by too fast, [disable automatic restart after a BSOD](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) to freeze the screen.
4. Note whether crashes happen on the discrete GPU only (games) or also on integrated graphics (video playback) — that distinction matters in Fix 7.

### Fix 2: Update drivers with HP Support Assistant first

HP validates drivers against your exact model's thermals and power delivery, so start here.

1. Open **HP Support Assistant** (preinstalled; download it from [HP's support site](https://support.hp.com/us-en) if missing).
2. Run **Updates** and install all recommended graphics, chipset, and BIOS updates.
3. Restart and test with the workload that crashed.
4. If HP Support Assistant shows no updates but crashes continue, don't stop here — its driver catalog lags behind the GPU makers, and Fix 3 does the deep clean.

### Fix 3: Clean-reinstall the graphics driver with DDU

When HP's update doesn't fix it, wipe the driver completely and reinstall fresh.

1. Download **Display Driver Uninstaller (DDU)** and the latest driver — either HP's version for your model or the GPU maker's stable release ([NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, or Intel's driver detection tool).
2. Disconnect from the internet so Windows Update can't interfere.
3. Boot into Safe Mode via **Settings > System > Recovery > Advanced startup**.
4. Run DDU, select your GPU brand, click **Clean and restart**.
5. Install the downloaded driver (use **Custom/Clean installation** if offered).
6. Reconnect and test. This resolves the majority of persistent TDR crashes.

### Fix 4: Stop Windows Update from replacing your driver

This is the HP-specific trap: you install a good driver, and Windows Update "helpfully" replaces it with a crashing one.

1. After a working driver is installed, open **Settings > Windows Update > Advanced options**.
2. Turn off **Receive updates for other Microsoft products**.
3. For a stronger block, open **System Properties > Hardware > Device Installation Settings** and choose **No** to prevent automatic driver downloads — you'll update drivers manually from then on.
4. Alternatively, use the **Show or hide updates** troubleshooter from Microsoft to hide the specific bad driver update.

### Fix 5: Cool the chassis down

HP's thin designs accumulate dust fast, and TDR crashes that appear months after purchase are often just heat.

1. Monitor GPU temperatures with HWiNFO during the crashing workload — sustained 88°C+ is trouble.
2. Shut down and blow compressed air through the intake and exhaust vents in short bursts.
3. Elevate the rear of the laptop for airflow and use a cooling pad during gaming or rendering.
4. In **OMEN Gaming Hub** (on Omen/Victus models), set the fan profile to **Max** or **Performance** while testing.
5. If the laptop is over two years old and still overheats after cleaning, the thermal paste has likely dried — check your warranty and let HP service repaste it rather than opening it yourself.

### Fix 6: Verify power delivery

An HP laptop on a weak charger can't feed its GPU under load, and the driver hang that follows looks exactly like a driver bug.

1. Use only the **original HP charger** with the correct wattage for your model — check the label on the brick.
2. Plug directly into a wall outlet, not a power strip shared with hungry devices.
3. Inspect the charging port and cable for damage or looseness; intermittent contact causes power dips.
4. In **Settings > System > Power & battery**, set power mode to **Best performance** while diagnosing.
5. If crashes happen only on battery, run `powercfg /batteryreport` — a degraded battery can't sustain boost clocks.

### Fix 7: Test integrated vs. discrete graphics

Isolating which GPU crashes tells you whether it's a driver issue or a hardware one.

1. Go to **Settings > System > Display > Graphics** and set the crashing app to **Power saving** (forces integrated graphics).
2. If crashes stop, the discrete GPU or its driver is the problem — focus driver efforts there, or keep the app on integrated graphics as a workaround.
3. If crashes continue on integrated graphics too, suspect system files: run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an admin Terminal.
4. Persistent crashes on both GPUs after clean drivers point to deeper system or motherboard issues — run HP's built-in hardware diagnostics (**F2** at boot > **Component Tests**) before concluding anything.

### Fix 8: Update the BIOS

HP BIOS updates frequently fix GPU power-management and switching bugs that cause TDR failures.

1. Find your model on HP's support site and download the latest BIOS.
2. Run the installer with the charger plugged in and don't touch the laptop until it finishes.
3. After the update, enter BIOS setup (**F10**) and **Load Setup Defaults** to clear stale settings.
4. Retest. If crashes persist after all eight fixes with clean drivers, the GPU itself may be failing — back up your data and contact HP support, especially if visual artifacts have appeared.

## Closing

On HP laptops, VIDEO_TDR_FAILURE is usually a driver problem wearing a hardware costume — Windows Update swapping in a generic driver, or an old install gone corrupt. Clean-reinstall the driver, lock Windows Update out of your GPU, then address heat and power. The HP-specific steps here (Support Assistant, driver blocking, OMEN fan controls) handle the quirks that the generic guides miss.
