---
title: "How to Fix NPU Error Code 10: Device Cannot Start on Your AI PC"
slug: npu-error-code-10-device-cannot-start
date: 2026-10-20
categories: ["ai-pc"]
tags: ["npu error code 10", "device cannot start", "npu driver", "troubleshooting", "ai pc", "device manager"]
description: "Fix NPU error code 10 on your AI PC laptop with six step-by-step methods covering driver repair, power settings, BIOS updates, and a full clean reinstall."
thumbnail: "/images/thumbs/npu-error-code-10-device-cannot-start.webp"
faqs:
  - q: "What does NPU error code 10 mean?"
    a: "Code 10 means Windows loaded the NPU driver but the hardware failed to initialize. It usually points to a corrupt driver, a failed update, or a power-management conflict — not dead hardware — and most cases recover after a proper driver reinstall."
  - q: "Can a restart fix NPU error code 10?"
    a: "Rarely. A plain restart reuses the same failing driver state. A full shutdown (hold Shift while clicking Shut down) sometimes works by forcing the firmware to re-enumerate the NPU. If the warning returns, work through the driver fixes below."
  - q: "Will fixing code 10 delete my files?"
    a: "No. Reinstalling the NPU driver and adjusting power settings does not touch your files, apps, or Windows settings. Only driver-level preferences for the neural processor reset, and they rebuild automatically on the next boot."
  - q: "When should I suspect a hardware fault?"
    a: "Only if code 10 survives a clean driver reinstall and a BIOS update — especially if the NPU also vanishes from Device Manager between reboots. Then a warranty check with your laptop maker is the right move."
---

Seeing your NPU flagged with a yellow triangle and "This device cannot start (Code 10)" in Device Manager is unsettling on an AI PC laptop. The neural processor runs Windows Studio Effects, live captions, and on-device Copilot features — when it cannot start, those features silently stop or fall back to the CPU, draining your battery faster.

The good news: code 10 is almost never dead hardware. It is a driver-initialization failure — Windows loads the NPU driver, asks the chip to power up, and the handshake fails. On Intel Core Ultra, AMD Ryzen AI, and Snapdragon X machines, that handshake depends on the driver package, firmware, power policy, and BIOS.

This guide gives you six fixes in technician order: quick state resets first, then driver repair, then power and firmware checks. Work through them in sequence and recheck Device Manager after each step.

## Why this happens

- **Corrupt NPU driver install:** An interrupted update — forced shutdown, Windows Update conflict, half-installed OEM package — leaves files and registry entries out of sync, so the driver crashes while initializing.
- **Wrong driver for your NPU:** A mismatched package (Intel AI Boost driver on AMD Ryzen AI hardware, or vice versa) loads but cannot talk to the real chip, triggering code 10 immediately.
- **Aggressive power management:** PCI Express link-state power management can cut power to the NPU before it finishes starting, especially on battery-saver profiles.
- **Outdated BIOS firmware:** The BIOS enumerates the NPU for Windows at boot. Firmware bugs hand Windows a broken device description the driver then fails to initialize — common after big Windows feature updates.
- **Conflicting Windows Update driver:** Windows Update sometimes pushes a newer-but-incompatible NPU driver over a working OEM one, and code 10 appears overnight.
- **Residual driver state:** Uninstalling without deleting driver files leaves stale copies behind, so Windows reinstalls the same broken package from cache and the failure repeats.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Force a full hardware re-enumeration with a cold boot

A normal restart preserves the kernel session and some device power states, so a stuck NPU stays stuck. A full shutdown forces the firmware to rediscover every device from scratch — and this alone clears code 10 surprisingly often.

1. Hold **Shift** and click **Shut down** to force a true shutdown instead of hybrid sleep.
2. Once fully off, unplug the charger and USB devices, then hold the power button 15 seconds to drain residual board power.
3. Wait 30 seconds, reconnect the charger, power on, and check Device Manager.
4. If the warning is gone, you are done — no driver surgery needed.

### Fix 2: Uninstall the NPU driver with its files deleted

A plain uninstall leaves the driver package on disk, so Windows reinstalls the same broken copy on reboot. Deleting the driver software forces a fallback to the inbox driver or a fresh Windows Update copy — the most effective fix for corrupt installs.

1. In Device Manager, right-click the NPU, choose **Uninstall device**, and check **"Attempt to remove the driver for this device"**.
2. Restart — the cleanup completes during boot, so do not skip it.
3. Reopen Device Manager. If the NPU now shows [code 28 (drivers not installed)](/articles/npu-error-code-28-drivers-not-installed/), that is progress — install a fresh driver in Fix 4.
4. If code 10 persists, continue — the problem likely sits below the driver layer.

### Fix 3: Disable PCI Express power management

When link-state power management parks the PCIe lane the NPU sits on too aggressively, the driver fails its startup handshake because the hardware never fully wakes. Try this if code 10 appeared after a power-plan change.

1. Open **Control Panel > Hardware and Sound > Power Options**, click **Change plan settings**, then **Change advanced power settings**.
2. Expand **PCI Express > Link State Power Management** and set it to **Off** for both On battery and Plugged in.
3. Click Apply, restart, and check Device Manager.
4. If the NPU starts cleanly, you found the culprit — later try Moderate power savings for better battery life.

### Fix 4: Install the correct NPU driver from your laptop maker

With the broken package cleared, install a driver that matches your hardware. Your laptop maker's support page is safest — OEM drivers are validated against your exact model's BIOS and power firmware.

1. Find your exact model in **Settings > System > About**, then search it on [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support and download the latest chipset/NPU package for Windows 11.
2. Run the installer as administrator and let it finish without interruption.
3. Restart when prompted and verify the NPU starts cleanly. For a different error code, compare with the [code 43 NPU driver guide](/articles/npu-driver-error-code-43/) — the two share several root causes.
4. Confirm an AI feature like background blur actually works, not just that the warning cleared.

### Fix 5: Update the BIOS/UEFI firmware

The BIOS describes the NPU to Windows during boot, and firmware bugs in that description are a classic hidden cause of code 10 — especially when the error appeared right after a Windows feature update. Keep the charger plugged in and never interrupt the flash.

1. On your manufacturer's support page, find a BIOS newer than yours (`msinfo32` shows BIOS Version/Date), download it, and close all programs.
2. Run the updater with the charger connected — a black screen for several minutes during the flash is normal.
3. After Windows loads, verify the NPU in Device Manager and test an AI feature.
4. If [live captions and the microphone stopped working](/articles/live-captions-microphone-not-working/) at the same time, this often fixes both, since both depend on the NPU starting cleanly.

### Fix 6: Block Windows Update from replacing the working driver

If the NPU heals but code 10 returns after the next Windows Update, Windows is pushing an incompatible driver over your working one. Block the replacement with the supported device-ID restriction.

1. In Device Manager, open the NPU's **Properties > Details > Hardware Ids** and copy the ID.
2. Open **gpedit.msc** (Windows 11 Pro) and go to Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions.
3. Enable **"Prevent installation of devices that match any of these device IDs"** and add the NPU hardware ID.
4. Reinstall your known-good OEM driver once more, restart, and confirm the NPU stays healthy past the next Patch Tuesday.

## Closing

Code 10 looks alarming but is a software problem in the vast majority of cases — a cold boot, a true driver purge, or the correct OEM package clears it. Keep your BIOS reasonably current, get NPU drivers from your laptop maker, and guard a working driver from Windows Update. If the warning survives everything here, it points at hardware — and a warranty call goes faster when you can say you worked through the full driver stack.
