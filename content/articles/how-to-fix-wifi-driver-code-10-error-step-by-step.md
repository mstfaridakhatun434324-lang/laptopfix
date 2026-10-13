---
title: "How to Fix WiFi Driver Code 10 Error — Step by Step"
slug: how-to-fix-wifi-driver-code-10-error-step-by-step
date: 2026-09-10
categories: ["drivers"]
tags: ["wifi code 10", "code 10 error", "wifi driver", "device cannot start", "device manager"]
description: "WiFi adapter showing Code 10 'device cannot start'? Fix it step by step — driver reinstalls, power resets, BIOS updates, and hardware checks."
thumbnail: "/images/thumbs/how-to-fix-wifi-driver-code-10-error-step-by-step.webp"
faqs:
  - q: "What does Code 10 mean on a WiFi adapter?"
    a: "Code 10 — 'This device cannot start' — means Windows loaded a driver for the WiFi adapter but the hardware failed to initialize when the driver talked to it. On wireless cards this is a driver/firmware mismatch far more often than dead hardware: the wrong driver version, corrupt driver files, or the card wedged in a bad power state. The step-by-step sequence below resolves most Code 10 cases without replacing anything."
  - q: "Is Code 10 a hardware or software problem?"
    a: "Usually software. Code 10 specifically indicates the driver-to-hardware handshake failed, and the common causes are all fixable: mismatched driver version, corrupt installation, Fast Startup resuming a wedged card state, or outdated BIOS firmware. It becomes a hardware suspicion only after a clean manufacturer driver install, full power-cycle, and BIOS update all fail — and a Linux live USB test is the definitive tiebreaker."
  - q: "Why did my WiFi get Code 10 after a Windows update?"
    a: "Windows Update replaced your working wireless driver with a different build that doesn't match your card's firmware — this is the single most common Code 10 trigger on WiFi adapters. The fix is uninstalling with driver deletion and installing the laptop maker's validated driver, then hiding the Windows Update driver so it doesn't recur. Rolling back in Device Manager works too when the option is available."
  - q: "Can I fix Code 10 without internet access?"
    a: "Yes, with preparation: download the wireless driver on another device (phone or second computer), transfer it via USB drive, then uninstall the broken driver and install the downloaded package offline. Device Manager's rollback and Windows' built-in driver store also work offline. The only online-dependent step is fetching the newest driver — everything else in the sequence below works without connectivity."
---

Code 10 on a WiFi adapter — "This device cannot start" in Device Manager — is uniquely annoying because it kills your internet, cutting off the easiest path to the fix (downloading a new driver). The error means the driver loaded but the hardware wouldn't start talking to it. That handshake failure has a short list of causes, and they're almost all software: wrong driver version, corrupt files, wedged power state, or outdated firmware.

This step-by-step guide is ordered for the offline reality of a dead WiFi card — including how to get the driver without internet.

## Why this happens

- **Windows Update driver mismatch.** A replaced driver that doesn't match the card's firmware — the top cause.
- **Corrupt driver installation.** Partial update mixing incompatible driver files.
- **Wedged power state.** Fast Startup or sleep leaving the card unresponsive to initialization.
- **Outdated BIOS/firmware.** Platform firmware the card's driver expects to be newer.
- **Wrong driver for the card.** A plausible-but-wrong automatic match by Windows.
- **Loose M.2 card.** Physical connection issue presenting as a start failure.
- **Failed wireless card.** Genuine hardware death — the last resort.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's Code 10 and note the details

Precision matters — other codes need different fixes.

1. Open **Device Manager > Network adapters**, right-click the WiFi adapter > **Properties > General**.
2. Confirm the message is **"This device cannot start. (Code 10)"** — Code 43, 45, or 31 follow different paths.
3. Note the adapter's exact model and the current **Driver tab** version/date — you'll compare later.
4. Check **Events tab** for the driver's load history — repeated failed starts confirm the pattern.
5. If you have another way online (phone tethering via USB, Ethernet), set it up now — it makes the later steps far easier.

### Fix 2: Full power-cycle to unwedge the card

Clear the stuck hardware state before touching software.

1. In **Device Manager**, right-click the adapter and choose **Disable device**, wait 10 seconds, then **Enable device** — test.
2. If still Code 10: **Shut down** holding **Shift** (skips Fast Startup), unplug the AC adapter.
3. Hold the power button for **15 seconds** (drains residual power and resets embedded controller state).
4. Wait a minute, reconnect AC, power on, and check Device Manager.
5. Cards wedged by sleep/hybrid-boot often start cleanly after this — if Code 10 returns only after sleep, it's the power-management issue (Fix 5).

### Fix 3: Roll back or reinstall the driver

The central fix — get the correct driver loaded.

1. **Properties > Driver tab** — if **Roll Back Driver** is available, use it (this undoes the update that caused Code 10), restart, test.
2. If rollback isn't available: **Uninstall device**, checking **Delete the driver software for this device**.
3. Restart — Windows loads a baseline driver from its store; check if Code 10 clears.
4. If it clears with the baseline, install the proper driver: your **laptop maker's wireless driver** for your exact model — download it on another device and transfer via USB if you have no internet.
5. Install offline if needed (disconnect WiFi/Ethernet during install so Windows doesn't interfere), restart, verify the version.

### Fix 4: Get the right driver without internet

The offline logistics that make Fix 3 possible.

1. On a **phone or second computer**, go to your laptop maker's support site and download the **wireless/WiFi driver** for your exact model.
2. Transfer it via **USB drive** (or USB phone tethering, which also gives the laptop temporary internet).
3. For Intel cards, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can run from the phone-tethered connection.
4. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) also hosts wireless drivers searchable by card model — download the CAB, extract, and install via **Device Manager > Update driver > Browse my computer**.
5. Keep the downloaded package on the USB drive — you'll need it again if Windows Update replaces the driver.

### Fix 5: Disable the power settings that wedge the card

Stop the OS from putting the card in unrecoverable states.

1. **Device Manager > adapter > Properties > Power Management** — uncheck **Allow the computer to turn off this device to save power**.
2. **Power Options > Change advanced power settings > Wireless Adapter Settings > Power Saving Mode** — **Maximum Performance** for both states.
3. **Power Options > Choose what the power buttons do** — uncheck **Turn on fast startup**; do a full shutdown.
4. Restart and verify Code 10 is gone — then test sleep/wake specifically, since that's the trigger.
5. If Code 10 only ever appears after sleep, these settings are the permanent fix, not a workaround.

### Fix 6: Update the BIOS and block driver replacement

Firmware-level repair plus protecting the fix.

1. Check your maker's support site for a **BIOS update** — install on AC power, uninterrupted.
2. BIOS updates frequently include wireless card initialization fixes — retest after updating.
3. Once a working driver is in place, run the **Show or hide updates** troubleshooter and hide the wireless driver update — this stops the Code 10 from recurring at the next update.
4. On Pro editions, **Group Policy > Do not include drivers with Windows Updates** = Enabled.
5. Microsoft's driver servicing documentation: [Windows support](https://support.microsoft.com/en-us/windows).

For identifying truly unknown devices that resist all driver attempts: [how to fix unknown device in Device Manager in Windows 11 24H2](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/).

### Fix 7: Hardware verification — reseat, live USB, replace

The definitive hardware tests.

1. Boot a **Linux live USB** — if WiFi works there, the card is fine and it's purely a Windows driver problem; if Linux also fails to start the card, it's hardware.
2. If your model has a removable **M.2 wireless card** (check the service manual): power off, remove battery/AC, reseat the card and its antenna leads (main/aux — note which is which).
3. While reseating, inspect the antenna cables — a pinched or disconnected antenna causes failures that mimic driver issues.
4. A replacement **Intel AX210** (~$20) fits most M.2 slots and is the standard upgrade — verify your BIOS has no card whitelist (rare on modern consumer laptops).
5. If the card is soldered and dead, a **USB WiFi adapter** bypasses it entirely — and if Device Manager's device list looks wrong during diagnosis, our guide on [how to enable hidden devices in Device Manager in Windows 11 24H2](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) shows how to reveal what's really present.

## Closing

WiFi Code 10 is a handshake failure with a software heart: power-cycle the wedged state, roll back or clean-install the maker's validated driver (fetching it offline via USB if you must), tame the power settings, and block Windows Update from re-breaking it. The Linux live-USB test is your hardware tiebreaker — run it before spending money on a replacement card.
