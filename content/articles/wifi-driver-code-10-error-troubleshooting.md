---
title: "WiFi Driver Code 10 Error? Troubleshoot It to Resolution"
slug: wifi-driver-code-10-error-troubleshooting
date: 2026-09-23
categories: ["drivers"]
tags: ["code 10", "wifi driver", "device cannot start", "troubleshooting", "device manager"]
description: "WiFi adapter showing 'This device cannot start (Code 10)'? Fix the failed driver initialization with power, driver, and hardware steps."
thumbnail: "/images/thumbs/wifi-driver-code-10-error-troubleshooting.webp"
faqs:
  - q: "What does Code 10 mean on a WiFi adapter?"
    a: "Code 10 means Windows loaded the driver but the hardware failed to start — the driver and the card couldn't complete initialization. It's a handshake failure between software and hardware, caused by driver/firmware mismatch, the card wedged in a bad power state, or actual hardware failure."
  - q: "Is Code 10 a driver problem or a hardware problem?"
    a: "Usually driver or power-state — the card is typically fine. The diagnostic order is: power-cycle to unwedge the firmware, roll back or reinstall the driver, check BIOS, then test in Linux. Only when all software avenues fail does Code 10 indicate dead hardware."
  - q: "Why did Code 10 appear right after a Windows update?"
    a: "Feature updates frequently install an incompatible WiFi driver version or corrupt the existing one during migration. The new driver can't initialize the card's firmware, producing Code 10 on hardware that worked minutes earlier. Rolling back the driver is the direct fix."
  - q: "Can Code 10 affect Bluetooth too?"
    a: "Yes, on combo cards (Intel AX201/AX210, MediaTek MT7921) WiFi and Bluetooth share one chip and often one driver package. A Code 10 on WiFi frequently comes with Bluetooth failing or vanishing too — fixing the combo driver resolves both together."
---

"This device cannot start. (Code 10)" — Device Manager's most frustrating WiFi error, because it's specific enough to name but vague enough to hide the cause. The WiFi adapter is there, the driver is there, but the two can't complete their handshake and the radio never comes up. No amount of clicking "enable" fixes it; the initialization itself is failing.

Code 10 is a driver-hardware handshake failure, and handshakes fail for concrete reasons: wedged firmware, wrong driver version, corrupted driver files, BIOS misconfiguration, or dead hardware. Test them in that order — cheapest first.

## Why this happens

- **The card's firmware is wedged.** A bad power state survives reboots; the driver can't initialize firmware that won't respond.
- **Driver/firmware version mismatch.** The installed driver expects a firmware interface the card isn't presenting — common after updates.
- **Corrupted driver files.** Partial updates or disk errors leave a driver that loads but can't complete initialization.
- **Windows Update installed the wrong driver.** An incompatible version that installs cleanly but can't start the hardware.
- **BIOS wireless misconfiguration.** The card partially disabled at firmware level confuses the driver's initialization. Compare [Intel AX201 Code 10 cases](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).
- **Power management interfering.** Aggressive PCIe power saving can starve the card during the initialization sequence.
- **Hardware failure.** The card genuinely can't start — dead radio, failed flash, or broken connection. Last suspect, not first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Full power-cycle to unwedge the firmware

Clears the wedged state that causes a large share of Code 10 errors.

1. **Shut down** completely (not restart). Unplug the charger and all peripherals.
2. Hold the power button for **30 seconds** to drain residual power — this forces the WiFi card's firmware to cold-boot.
3. Boot up, open **Device Manager** > **Network adapters**, and check the WiFi adapter's status.
4. If Code 10 persists, right-click the adapter > **Disable device**, wait 10 seconds, **Enable device** — forcing a clean re-initialization attempt.
5. Still Code 10? Continue — the firmware is responsive but the driver handshake is failing.

### Fix 2: Roll back the driver

The direct fix for update-induced Code 10.

1. Right-click the WiFi adapter > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is available, click it, choose a reason, and restart. This restores the driver version that was initializing the card successfully.
3. After reboot, verify the adapter starts without Code 10 and WiFi works.
4. Immediately protect the rolled-back driver: set **Device Installation Settings** to **No** so Windows Update doesn't reinstall the breaking version.
5. If rollback isn't available or doesn't help, continue to the clean reinstall.

### Fix 3: Clean-reinstall the correct driver

Removes corruption and version mismatch together.

1. Identify your exact card: adapter **Properties** > **Details** > **Hardware Ids** (e.g., Intel AX201, AX210, MediaTek MT7921, Realtek 8852).
2. Download the driver for that exact card: from the laptop maker's support page, or from the chip vendor — [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards.
3. In Device Manager, **Uninstall device** with **"Attempt to remove the driver"** checked. Restart.
4. Install the downloaded driver **as administrator**. Restart again.
5. Verify: no Code 10, adapter shows "This device is working properly," WiFi networks appear.

### Fix 4: Disable power management interference

For Code 10 that appears after sleep or is intermittent.

1. Adapter **Properties** > **Power Management** tab: uncheck "Allow the computer to turn off this device to save power."
2. **Advanced** tab: set any power-saving mode to **Maximum Performance**.
3. **Control Panel** > **Power Options** > advanced > **PCI Express** > **Link State Power Management** → **Off** (prevents the PCIe link from starving the card during init).
4. **Wireless Adapter Settings** > **Power Saving Mode** → **Maximum Performance** for both battery and plugged in.
5. Restart and check whether Code 10 clears — then test through a sleep/wake cycle.

### Fix 5: Check BIOS and reset firmware settings

Firmware-level causes of initialization failure.

1. Reboot into **BIOS/UEFI**. Verify **Wireless/WLAN** is **Enabled**.
2. Look for **Wake on WLAN**, **wireless auto-disable**, or similar — set sanely (disable exotic options as a test).
3. If the BIOS has a **"Reset to defaults"** option and wireless was working before a BIOS change, reset and retest.
4. Check for a **BIOS update** from the manufacturer — several vendors have shipped fixes for WiFi card initialization.
5. Save, boot to Windows, rescan hardware (**Action** > **Scan for hardware changes**).

### Fix 6: Test in Linux and check the hardware

The definitive driver-vs-hardware split.

1. Boot a **Linux live USB** and check WiFi. Linux uses completely different drivers — if the card initializes and works in Linux, your hardware is fine and it's purely a Windows driver problem (try additional driver versions).
2. If Linux also fails to bring the card up, the hardware is suspect.
3. For socketed M.2 cards: reseat the card and its antenna wires per the service manual. For soldered cards, this step is inspection-only.
4. Check for a **swollen battery** near the card — pressure damage causes exactly this kind of initialization failure and is a safety issue.
5. If [airplane mode is also stuck](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/), fix Code 10 first — the stuck radio state is often a downstream symptom of the failed initialization.

### Fix 7: Last-resort OS repair

For Code 10 surviving everything above with working hardware.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in an admin Terminal.
2. Try **System Restore** to before Code 10 appeared.
3. Do an **in-place Windows upgrade** (mount ISO, setup, keep files and apps) to rebuild the driver infrastructure.
4. Only then consider a clean Windows install — and if Code 10 survives even that on confirmed-working hardware, escalate to the manufacturer: it's a firmware defect needing their fix.

The official [Windows support pages](https://support.microsoft.com/en-us/windows) document Device Manager error codes.

## Closing

Code 10 is the driver and the card failing to shake hands, and handshakes get fixed by resetting the conditions: power-cycle the firmware cold, roll back the update that broke it, clean-install the exact right driver, remove power management from the initialization path, verify BIOS, then let Linux deliver the final verdict on the hardware. Most Code 10 errors end at Fix 1 or 3. The rest end with certainty about what to replace — which is the next best thing to a fix.
