---
title: "NPU Driver Error Code 43 in Windows 11: How to Fix It"
slug: npu-driver-error-code-43
date: 2026-10-19
categories: ["ai-pc"]
tags: ["error code 43", "npu driver", "device manager", "windows 11", "ai pc"]
description: "NPU driver showing error code 43 in Device Manager? Learn what stops the device and follow step-by-step fixes to get your AI accelerator running again."
thumbnail: "/images/thumbs/npu-driver-error-code-43.webp"
faqs:
  - q: "What does error code 43 mean on an NPU?"
    a: "It means Windows has stopped the device because it reported a problem — usually a driver fault, not dead hardware. The NPU is visible to the OS but cannot start, so AI features that need it stay offline until the driver issue is resolved."
  - q: "Is code 43 a sign my NPU hardware is dead?"
    a: "Rarely. Code 43 is overwhelmingly a driver problem on NPUs: wrong version, corrupted install, or a conflict. Only suspect hardware after multiple clean driver installs from different sources all produce the same error."
  - q: "Can Windows Update cause code 43 on the NPU?"
    a: "Yes — it is one of the top causes. Windows Update sometimes installs an NPU driver that mismatches your chip revision or firmware, and the device immediately reports code 43. Rolling back to the OEM driver fixes it."
  - q: "Will code 43 go away on its own after updates?"
    a: "Sometimes a later driver update resolves it, but waiting is unreliable. The targeted fixes below resolve it in minutes, while Windows may take months to ship a corrected driver for your specific machine."
---

Device Manager shows your NPU with a yellow warning triangle, and the device status reads: "Windows has stopped this device because it has reported problems. (Code 43)." The hardware is detected — unlike the [missing Neural processors section](/articles/neural-processors-missing-device-manager/) problem — but Windows refuses to start it. Your AI features are dead in the water until the device can initialize.

Code 43 is Windows' generic "the driver told me something is wrong" signal. On NPUs, which have young and occasionally fragile drivers, it is almost always fixable in software. Work through these fixes in order; the first three resolve the large majority of cases.

## Why this happens

- **Wrong driver version for your chip:** NPU drivers are chip-revision sensitive. A driver built for a different stepping can load just far enough to report a fault.
- **Corrupted driver install:** Interrupted updates or partial installs leave the driver in a state where initialization fails every boot.
- **Windows Update driver mismatch:** The number-one trigger — Windows replaces your working OEM driver with a generic one that your firmware rejects.
- **Firmware/driver version skew:** A BIOS update can change what the NPU expects from its driver; an old driver then fails to start the device.
- **Power management conflicts:** Aggressive PCIe power saving can starve the NPU during initialization, producing a code 43 that looks like a driver fault.
- **Conflicting driver remnants:** Two driver versions' files mixed together create an inconsistent state the device cannot start from.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable and re-enable the device

The simplest reset sometimes clears a one-time initialization failure.

1. Open Device Manager, expand Neural processors.
2. Right-click the NPU entry and choose Disable device, confirm.
3. Wait 10 seconds, right-click again, and choose Enable device.
4. Check whether the warning clears — if code 43 returns immediately, continue to Fix 2.
5. Reboot and check once more; a clean boot occasionally succeeds where a hot re-enable fails.

### Fix 2: Roll back or reinstall the OEM driver

Code 43 after an update means the new driver is the problem.

1. Right-click the NPU, Properties, Driver tab — click "Roll Back Driver" if available.
2. If greyed out, uninstall the device, ticking "Attempt to remove the driver."
3. Install the NPU driver from your maker's support page: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
4. Reboot and verify the warning is gone in Device Manager.
5. Pause Windows updates for a week so the bad driver is not immediately reinstalled.

### Fix 3: Clean-install the driver stack

When rollback is unavailable or fails, wipe everything and start fresh.

1. Disconnect from the internet.
2. Uninstall all Neural processors entries, removing driver software each time.
3. In admin Command Prompt, run `pnputil /enum-drivers`, find stale NPU packages, and remove them with `pnputil /delete-driver oemXX.inf /uninstall`.
4. Reboot, stay offline, install the single correct OEM driver.
5. Reconnect and confirm the device starts cleanly across a second reboot.

### Fix 4: Update BIOS/firmware

Firmware/driver skew causes code 43 that no driver swap fixes.

1. Check your current BIOS version: `msinfo32`, look at BIOS Version/Date.
2. Compare against your maker's support page for your exact model.
3. If a newer BIOS exists, install it following the maker's instructions exactly — keep the charger plugged in.
4. After the BIOS update, reinstall the latest OEM NPU driver (firmware updates can invalidate old driver pairings).
5. Check Device Manager — the combination of new firmware plus matching driver clears skew-induced code 43.

### Fix 5: Disable PCIe power saving for the NPU

Power starvation during init masquerades as a driver fault.

1. Open Control Panel, Power Options, "Change plan settings," "Change advanced power settings."
2. Expand PCI Express, "Link State Power Management," set it to Off for both battery and plugged in.
3. In Device Manager, open the NPU's Properties, Power Management tab, and uncheck "Allow the computer to turn off this device to save power" if present.
4. Reboot and check whether code 43 clears — if it does, the driver was fine and power policy was the culprit.
5. You can re-enable moderate power saving later once stability is confirmed.

### Fix 6: Test in a clean boot

Rule out third-party software interfering with device initialization.

1. Press Win + R, type `msconfig`, Enter. On the Services tab, tick "Hide all Microsoft services," then "Disable all."
2. On the Startup tab, open Task Manager and disable all startup items.
3. Reboot — check Device Manager for code 43 in this minimal state.
4. If the NPU starts cleanly, re-enable services in halves to find the conflicting software.
5. If code 43 persists even in a clean boot with a fresh OEM driver and current BIOS, contact your maker's support — you have exhausted software causes.

## Closing

Code 43 on an NPU looks alarming but is a driver problem in nearly every case we see — wrong version, corrupted install, or firmware skew. The disable/re-enable trick, a driver rollback, or a true clean install resolves it the large majority of the time. Because this error often arrives via Windows Update, the same update that [made your NPU disappear entirely](/articles/npu-disappeared-after-windows-update/) can also produce code 43 — the fix path is similar, so do not hesitate to combine approaches. Note that AMD and Qualcomm NPUs have their own driver ecosystems: see our guides for [Ryzen AI NPU issues](/articles/amd-ryzen-ai-npu-not-showing-up/) and [Snapdragon X NPU driver problems](/articles/snapdragon-x-elite-npu-driver-issues/) if you are not on Intel hardware.
