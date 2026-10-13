---
title: "How to Fix Code 43 GPU Error on Windows 10 (Device Has Stopped)"
slug: how-to-fix-code-43-gpu-error-on-windows-10
date: "2026-09-14"
categories: ["drivers"]
tags: ["code 43", "gpu error", "graphics driver", "device manager error", "nvidia"]
description: "Seeing 'Windows has stopped this device (Code 43)' on your GPU? Learn how to fix the Code 43 graphics error on Windows 10 with driver repair steps."
thumbnail: "/images/thumbs/how-to-fix-code-43-gpu-error-on-windows-10.webp"
faqs:
- q: "What does Code 43 mean on a graphics card?"
  a: "Code 43 means Windows stopped the device because it reported a problem — the GPU's driver crashed during initialization or the card failed its self-check, so Windows halted it to protect the system. The card is still physically detected, which distinguishes Code 43 from a missing adapter. In most cases the trigger is a corrupted or incompatible graphics driver, and a clean driver reinstall resolves it without hardware involvement."
- q: "Can a Windows update cause Code 43 on my GPU?"
  a: "Yes, this is one of the most common triggers. Feature updates sometimes install a graphics driver version incompatible with your specific GPU or laptop firmware, and the driver then fails initialization with Code 43 on the next boot. If the error appeared immediately after an update, rolling back the driver in Device Manager or reinstalling the previous known-good version is the fastest fix."
- q: "Does Code 43 mean my graphics card is dead?"
  a: "Not necessarily — driver problems cause the large majority of Code 43 errors, and those are fully fixable in software. Hardware failure becomes likely only when the error survives a clean driver install, a driver rollback, and testing with the card reseated (on desktops), or when it appears alongside artifacts and crashes. On laptops with soldered GPUs, persistent Code 43 after driver repair warrants professional diagnosis."
- q: "Will reinstalling Windows fix a Code 43 GPU error?"
  a: "It can, as a last resort, because it replaces the entire driver stack and system files — but it is rarely necessary. The targeted fixes in this guide (clean driver install, rollback, disabling fast startup) resolve Code 43 in the large majority of cases with far less disruption. Reserve a Windows reinstall for when the error survives every driver-level repair and hardware has been ruled out."
---

Few Device Manager messages inspire as much dread as "Windows has stopped this device because it has reported problems. (Code 43)" sitting on your graphics card. The display may still work — running on the basic Microsoft adapter or the integrated GPU — but games stutter or refuse to launch, external monitors misbehave, and the discrete GPU sits idle with its yellow warning triangle.

Code 43 is Windows' protective response: the GPU's driver failed during startup — crashed, timed out, or reported a hardware fault — so Windows halted the device rather than risk instability. The crucial point is that the card is detected; Windows knows exactly what it is and simply will not run it. That distinction matters because detected-but-stopped is overwhelmingly a driver problem, while not-detected-at-all leans hardware.

This guide repairs the driver path methodically: quick resets first, then clean reinstalls and rollbacks, then the system-level causes, ending with how to recognize genuine hardware failure.

## Why this happens

- **Corrupted graphics driver**: Damaged driver files crash during GPU initialization.
- **Incompatible driver after Windows Update**: A new driver version conflicts with the GPU or laptop firmware.
- **Driver conflict between integrated and discrete GPUs**: Switchable-graphics handoff fails, stranding the discrete card.
- **Fast startup preserving a crashed state**: The failed driver state survives reboots via hibernation-based startup.
- **Overclock or undervolt instability**: Unstable tuning crashes the driver at load, triggering Code 43.
- **Failing GPU hardware**: Degraded memory or power delivery on the card fails initialization.
- **Corrupted system files**: Damaged Windows driver-framework files prevent any GPU driver from loading.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart properly and re-enable the device

Fast startup means most "restarts" are not really restarts — the driver state is preserved from the crashed session. A true cold boot plus manually re-enabling the device clears transient initialization failures, which account for a real share of Code 43 reports after updates and crashes.

1. In Device Manager, right-click the GPU and choose "Disable device," wait ten seconds, then "Enable device."
2. Check whether Code 43 clears — if it does, the failure was transient.
3. Regardless, perform a full shutdown: hold Shift while clicking Shut down.
4. Wait ten seconds, power on, and check Device Manager again.
5. If Code 43 returns, the driver itself needs repair — continue below.

### Fix 2: Clean-reinstall the graphics driver

This is the core fix for Code 43. A standard update installs over the broken driver and can inherit its corruption; a clean install removes everything first. Use the GPU vendor's installer with its clean-install option — [NVIDIA's driver download](https://www.nvidia.com/Download/index.aspx) and [AMD's driver support](https://www.amd.com/en/support/download/drivers.html) both offer it — or your laptop manufacturer's package for switchable-graphics models.

1. Download the latest driver for your exact GPU and Windows 10 from the vendor.
2. In Device Manager, right-click the GPU, choose "Uninstall device," and tick "Attempt to remove the driver."
3. Run the vendor installer and select the "clean install" option (NVIDIA) or factory reset (AMD).
4. Restart when prompted and check Device Manager for the warning's absence.
5. Test with a game or GPU benchmark to confirm stability under load.

### Fix 3: Roll back to the previous driver

If Code 43 appeared right after a driver update, the new driver is the problem — restore the old one. Rollback is faster than any reinstall and returns you to a version proven working on your exact hardware. This is the correct first driver move whenever the timeline implicates an update.

1. In Device Manager, right-click the GPU and open Properties.
2. Go to the Driver tab and click "Roll Back Driver."
3. Select a reason, confirm, and restart.
4. Verify Code 43 is gone in Device Manager.
5. Block the problematic version from reinstalling via Windows Update driver settings.

### Fix 4: Disable fast startup

Fast startup's hibernation-based shutdown preserves driver state across boots — including the crashed state that produced Code 43. With it disabled, every boot fully reinitializes the GPU driver, which both clears stuck failures and prevents their recurrence. The cost is a few extra seconds of boot time.

1. Open Control Panel, Power Options, "Choose what the power buttons do."
2. Click "Change settings that are currently unavailable."
3. Untick "Turn on fast startup" and save changes.
4. Shut down fully, wait ten seconds, and power on.
5. Check Device Manager — a Code 43 that only occurred with fast startup enabled will be gone.

### Fix 5: Reset any overclocking and check thermals

Unstable overclocks and undervolts crash GPU drivers in exactly the way that produces Code 43 — the driver fails under load and Windows halts the device. Even factory "OC edition" cards can become unstable as thermal paste ages. Returning clocks to stock and verifying cooling eliminates this entire category.

1. Open your GPU tuning utility (MSI Afterburner, ASUS GPU Tweak, or similar) and reset to defaults.
2. If you edited vBIOS or used registry tweaks, revert them.
3. Monitor GPU temperatures under load — sustained 90°C+ on a laptop suggests thermal throttling territory.
4. Clean dust from vents and ensure the laptop sits on a hard, flat surface.
5. Retest — a Code 43 that only appears under load was almost certainly clock or thermal instability.

### Fix 6: Repair Windows system files

When clean drivers still produce Code 43, the fault may be in Windows' driver framework rather than the GPU driver. Corrupted system files prevent even a perfect driver from initializing the card. The SFC and DISM tools repair these files in place without touching your data or applications.

1. Open Terminal or Command Prompt as administrator.
2. Run `sfc /scannow` and wait for it to complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart the laptop after both complete.
5. Check Device Manager — repaired framework files allow the driver to initialize normally.

### Fix 7: Assess for hardware failure

A Code 43 that survives clean installs, rollbacks, stock clocks, and system repair — especially when accompanied by visual artifacts, crashes, or failure in a Linux live environment — points at the GPU hardware. On laptops the GPU is usually soldered, making this a board-level repair decision: weigh the machine's value against repair cost, check warranty status, and get a professional diagnosis before committing.

1. Boot a Linux live USB and check whether the GPU initializes there.
2. Note any artifacts (glitched textures, colored blocks) — these are hardware signatures.
3. On the rare laptops with MXM removable GPUs, reseating is worth trying.
4. Check warranty — GPU failure on an in-warranty machine is a manufacturer repair.
5. Out of warranty, compare board-repair quotes against replacement; integrated graphics keep the laptop usable meanwhile.

If the GPU does not appear in Device Manager at all rather than showing Code 43, see [display adapter missing](/articles/how-to-fix-display-adapter-missing-youtube/) instead — that is a different fault. A GPU identified only as an [unknown device](/articles/how-to-fix-unknown-device-in-device-manager/) needs the hardware-ID identification approach.

## Closing

Code 43 is Windows protecting you from a GPU driver that failed to start — and failed driver starts are fixed with driver repairs: re-enable, clean-reinstall, roll back, and disable fast startup. Work that sequence before suspecting the silicon. When the error survives every software repair and artifacts appear, believe the hardware evidence and get a professional diagnosis.
