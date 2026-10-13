---
title: "Bluetooth Missing From Device Manager on Windows 10: Fix Guide"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-10"
date: "2026-10-07"
categories: ["drivers"]
tags: ["bluetooth disappeared", "device manager", "windows 10", "bluetooth driver", "bluetooth fix"]
description: "Bluetooth vanished from Device Manager on Windows 10? These fixes cover the classic Bluetooth Support Service, driver stack, and power issues specific to Windows 10."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-10.webp"
faqs:
  - q: "Why does Bluetooth disappear from Device Manager on Windows 10?"
    a: "On Windows 10 the usual causes are a corrupted Bluetooth driver, the Bluetooth Support Service failing to start, aggressive USB power management keeping the radio asleep, or a Windows update replacing the working driver. Because Windows 10's Bluetooth stack is older, driver incompatibilities after updates are especially common."
  - q: "Is the Bluetooth Support Service important on Windows 10?"
    a: "Yes — it is essential. The Bluetooth Support Service discovers and pairs Bluetooth devices on Windows 10; if it is stopped or disabled, Bluetooth functionality breaks even when the driver is fine. Setting it to Automatic and starting it resolves a significant share of Windows 10 Bluetooth failures."
  - q: "Should I upgrade to Windows 11 to fix Bluetooth?"
    a: "Upgrading is not a Bluetooth fix by itself — Windows 11 has its own Bluetooth issues, and the underlying driver problem usually follows you. Fix the Windows 10 Bluetooth stack first using this guide. Consider upgrading only for broader reasons, and verify your laptop manufacturer's Windows 11 Bluetooth drivers exist before you do."
  - q: "What if Bluetooth is missing after a Windows 10 feature update?"
    a: "Feature updates on Windows 10 (like 22H2) reinstall drivers and can break the Bluetooth stack the same way Windows 11 updates do. Roll back the Bluetooth driver in Device Manager, reinstall the manufacturer's Windows 10 driver package, and block driver updates until you confirm stability."
---

Windows 10's Bluetooth stack is older and, in some ways, more fragile than Windows 11's — but it is also extremely well documented after a decade of troubleshooting. When Bluetooth disappears from Device Manager on Windows 10, the fault follows familiar patterns: the Bluetooth Support Service stalls, a driver update breaks the stack, or power management sleeps the radio into invisibility.

This guide is written specifically for Windows 10's interfaces and behaviors — the Control Panel paths, the service names, and the update mechanics that differ from Windows 11. If you are on Windows 11, use our [Windows 11 Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-windows-11/) instead; the steps overlap but the details matter.

Work through the fixes in order, checking Device Manager after each step.

## Why this happens

- **Bluetooth Support Service stopped**: this service is mandatory on Windows 10 for discovery and pairing; updates and tune-up tools frequently leave it disabled.
- **Driver replaced by Windows Update**: Windows 10 Update installs generic Bluetooth drivers that fail on many laptop radios, particularly older Broadcom and Atheros chips.
- **Corrupted Bluetooth stack**: the layered driver/service architecture can corrupt during feature updates, hiding the adapter entirely.
- **USB selective suspend**: Windows 10's default power plans aggressively sleep the internal USB bus where the Bluetooth radio lives.
- **Fast Startup caching**: hybrid shutdown preserves a failed Bluetooth initialization across restarts.
- **Airplane mode stuck**: the Windows 10 Action Center airplane toggle can stick in a half-state, disabling Bluetooth while Wi-Fi appears normal.
- **Third-party "optimizer" tools**: registry cleaners and driver updaters popular in the Windows 10 era are notorious Bluetooth breakers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle airplane mode and run the Windows 10 troubleshooter

Windows 10's Action Center airplane toggle and its built-in Bluetooth troubleshooter resolve the simplest cases — including the stuck half-state where the toggle UI and the actual radio disagree.

1. Click the **Action Center** icon (bottom-right), and toggle **Airplane mode** on, wait 10 seconds, then off.
2. Open **Settings > Update & Security > Troubleshoot > Additional troubleshooters > Bluetooth > Run the troubleshooter**.
3. Apply any fixes it recommends and restart if prompted.
4. Check **Settings > Devices > Bluetooth & other devices** for the Bluetooth toggle.
5. Open Device Manager (**Windows key + X > Device Manager**) and look for the Bluetooth category.

### Fix 2: Start the Bluetooth Support Service

On Windows 10, this service is the backbone of Bluetooth. It must be running — set to Automatic — or nothing Bluetooth-related works regardless of driver state.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Bluetooth Support Service**, double-click it, and set **Startup type** to **Automatic**.
3. Click **Start** if the service is not running, then click OK.
4. Also check **Bluetooth Audio Gateway Service** and **Bluetooth User Support Service** where present.
5. Restart the laptop and verify — a surprising number of "dead Bluetooth" cases on Windows 10 end right here.

### Fix 3: Show hidden devices and remove ghost adapters

Failed Bluetooth adapters hide as non-present devices. Clearing them lets Windows attempt a clean enumeration on the next boot.

1. In Device Manager, click **View > Show hidden devices**.
2. Expand **Bluetooth** and **Network adapters**, looking for grayed-out entries.
3. Right-click each grayed-out Bluetooth adapter, choose **Uninstall**, and tick "Delete the driver software for this device" if offered.
4. Click **Action > Scan for hardware changes**.
5. If the adapter reappears with a warning icon, the driver needs replacement — continue to Fix 4.

### Fix 4: Install the manufacturer's Windows 10 driver

Windows 10-era laptops often need the manufacturer's driver package — the generic Windows 10 Bluetooth driver lacks support for many older radio chips (Broadcom, Atheros, early Realtek). Get the right one.

1. Identify your exact laptop model and download its Windows 10 Bluetooth/wireless driver from the manufacturer's official support page.
2. If the manufacturer no longer lists Windows 10 drivers, use the newest available package — Windows 10 driver compatibility is broad.
3. Uninstall the current Bluetooth driver first (Device Manager > Uninstall, ticking driver deletion).
4. Install the downloaded package, then restart with a full shutdown (Shift + Shut down).
5. Verify in Device Manager that the adapter shows the manufacturer's driver date — and consider [blocking driver updates](https://support.microsoft.com/en-us/windows) via Microsoft's documented methods so Windows Update does not replace it.

### Fix 5: Disable power management on the radio

Windows 10's Balanced power plan enables USB selective suspend by default, which can keep the Bluetooth radio asleep through boot so it never enumerates.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both On battery and Plugged in.
3. In Device Manager, right-click the Bluetooth adapter > **Properties > Power Management** and uncheck "Allow the computer to turn off this device to save power."
4. Apply the same uncheck to **USB Root Hub** devices.
5. Shut down fully (Shift + Shut down), cold-boot, and check Device Manager across several boots.

### Fix 6: Undo optimizer and driver-updater damage

The Windows 10 era popularized "PC optimizer" and third-party driver-updater tools, and they remain a top cause of Bluetooth breakage — they disable services, "clean" registry keys the Bluetooth stack needs, and install wrong drivers.

1. Uninstall any PC optimizer, registry cleaner, or third-party driver updater.
2. Re-check the Bluetooth Support Service (Fix 2) — optimizers love disabling it.
3. In an elevated Command Prompt, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
4. If a driver updater installed the Bluetooth driver, remove it and install the manufacturer's package per Fix 4.
5. Create a system restore point once Bluetooth works, so future "optimization" is reversible — the same protective habit in [our step-by-step Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-step-by-step/).

### Fix 7: Check BIOS, then isolate hardware

If the adapter never appears even as a hidden device, check the firmware layer — then prove hardware health with an independent OS before spending money.

1. Try the function-key wireless toggle (**Fn + F2**/**F3**/**F8** varies by brand) and any physical wireless switch.
2. Enter the BIOS/UEFI during boot and verify Bluetooth/wireless devices are enabled; load optimized defaults.
3. Boot an Ubuntu live USB and check Settings > Bluetooth — Linux uses its own stack.
4. If Linux sees the adapter, repair Windows with an in-place upgrade from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) or a Windows 10 repair install.
5. If neither OS sees it, the wireless card has failed — a standard M.2 replacement on most laptops, inexpensive compared to board-level repair.

## Closing

Windows 10 Bluetooth failures are a solved problem in the sense that the checklist is short and well-tested: the Support Service, hidden-device cleanup, the manufacturer's driver, power management, and undoing optimizer damage. The service check alone deserves emphasis — on Windows 10 it is the single most common fix and takes thirty seconds. Work the list in order, lock the working driver against Windows Update when you are done, and Bluetooth on Windows 10 stays as reliable as the decade-old stack can be.
