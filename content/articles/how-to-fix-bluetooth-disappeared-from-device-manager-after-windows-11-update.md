---
title: "How to Fix Bluetooth Missing From Device Manager After a Windows 11 Update"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update"
date: "2026-09-26"
categories: ["drivers"]
tags: ["bluetooth disappeared", "device manager", "windows 11 update", "bluetooth driver", "bluetooth missing"]
description: "Bluetooth vanished from Device Manager right after a Windows 11 update? Learn why updates break Bluetooth enumeration and how to bring the adapter back step by step."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update.webp"
faqs:
  - q: "Why did Bluetooth disappear from Device Manager after a Windows 11 update?"
    a: "Feature and cumulative updates can replace your working Bluetooth driver with an incompatible generic one, corrupt the Bluetooth stack during installation, or reset power-management settings so the adapter never enumerates. The radio hardware is usually fine — Windows has simply lost the ability to see it, which is why the whole Bluetooth category vanishes."
  - q: "Should I roll back the Windows update that removed Bluetooth?"
    a: "Try rolling back the Bluetooth driver first — it is faster and preserves the update's security fixes. Only consider uninstalling the Windows update itself if the driver rollback fails and Bluetooth worked perfectly before. You can uninstall recent updates from Settings > Windows Update > Update history > Uninstall updates."
  - q: "What if Bluetooth is missing even under hidden devices?"
    a: "If the adapter does not appear even with View > Show hidden devices enabled, Windows truly cannot see the hardware. Power down fully, unplug the charger, hold the power button for 30 seconds to drain residual power, then boot and check again. This power-cycle often forces the Bluetooth radio to re-enumerate."
  - q: "Can I stop Windows Update from breaking Bluetooth again?"
    a: "Yes. Once Bluetooth works, block Windows from managing the driver: in Device Installation Settings choose not to download drivers automatically, and install future Bluetooth drivers only from your laptop manufacturer's support page. Creating a system restore point before each major Windows update also gives you a quick way back."
---

Opening Device Manager after a Windows 11 update to find the entire Bluetooth category simply gone — not disabled, just absent — is a special frustration. Yesterday's earbuds and mouse are unreachable, the Settings toggle vanished too. This is one of the most reported post-update faults, and it follows a consistent pattern.

The key insight: the Bluetooth hardware is almost certainly fine. The update broke Windows' ability to enumerate it — an incompatible replacement driver, a corrupted Bluetooth stack, or power settings that keep the adapter asleep at boot. The fix targets software, so recovery is very likely — but order matters.

Work through the steps in order. Early steps are non-destructive and take minutes; later steps dig into driver surgery. Check Device Manager for the Bluetooth category after each fix.

## Why this happens

- **The update replaced your Bluetooth driver**: Windows Update often installs a generic or older Bluetooth driver over the manufacturer's working one, and the mismatched driver fails to initialize the radio.
- **Corrupted Bluetooth stack during install**: if the update was interrupted or conflicted with third-party software, the Bluetooth service and driver entries can be left half-written.
- **Power-management reset**: updates can re-enable aggressive USB power saving that keeps the Bluetooth adapter (often on an internal USB bus) powered down at boot.
- **Fast Startup caching a broken state**: Windows' hybrid shutdown can preserve the broken post-update driver state across reboots, making the problem look permanent.
- **BIOS/firmware mismatch**: some updates change how Windows talks to the embedded controller, and an old BIOS may no longer enumerate the Bluetooth radio correctly.
- **Third-party driver updaters interfering**: tools that "updated" Bluetooth alongside Windows can leave two competing drivers installed.
- **Pending update debris**: a partially installed cumulative update can leave the driver store inconsistent until the update fully completes or is cleaned up.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a full shutdown to clear Fast Startup

A normal Windows 11 restart is not a full restart — Fast Startup preserves driver state across it. If the update broke the Bluetooth stack, every "restart" just reloads the broken state. A full shutdown clears it.

1. Hold **Shift** while clicking **Shut down** in the Start menu, then wait until the laptop is fully off.
2. Unplug the charger and hold the power button for 15 seconds to drain residual power.
3. Power on normally and open Device Manager (**Windows key + X > Device Manager**).
4. Check whether the Bluetooth category has returned; also check **Settings > Bluetooth & devices**.
5. If Bluetooth is back, the problem was a cached broken state — consider disabling Fast Startup (**Control Panel > Power Options > Choose what the power buttons do**) to prevent recurrence.

### Fix 2: Reveal hidden devices and re-enable the adapter

Sometimes the adapter is present but hidden — marked non-present after the update shuffled drivers. Showing hidden devices reveals it for re-enabling or reinstalling.

1. In Device Manager, click **View > Show hidden devices**.
2. Expand **Bluetooth** if it appears, or look under **Network adapters** and **Universal Serial Bus controllers** for grayed-out Bluetooth entries (often "Intel Wireless Bluetooth" or "Realtek Bluetooth").
3. Right-click any grayed-out Bluetooth adapter and choose **Uninstall device**, ticking "Attempt to remove the driver for this device" if offered.
4. Click **Action > Scan for hardware changes** and watch for the adapter to reappear as an active device.
5. If it returns with a yellow warning icon, the driver is the problem — continue to Fix 3 rather than stopping here.

### Fix 3: Roll back the Bluetooth driver

If Bluetooth worked before the update and broke after, the previous driver version is still on the disk in most cases. Rolling back is the fastest targeted fix and the one most specific to post-update breakage.

1. In Device Manager, right-click the Bluetooth adapter and open **Properties > Driver**.
2. Click **Roll Back Driver**, select a reason, and confirm.
3. Restart the laptop with a full shutdown (Shift + Shut down) rather than a quick restart.
4. Verify the Bluetooth category is stable across two or three reboots.
5. To stop Windows Update from re-breaking it, pause driver updates as described in [our NVIDIA driver guide](/articles/nvidia-driver-keeps-crashing-windows-11/) — the same Windows Update behavior causes both problems.

### Fix 4: Install the manufacturer's Bluetooth driver cleanly

When rollback is unavailable (the old driver was purged), install the correct driver yourself. The manufacturer's driver — from Dell, HP, Lenovo, ASUS, or Acer support — is matched to your exact Bluetooth chip, unlike the generic one Windows Update prefers.

1. Identify your Bluetooth chip: in Device Manager, check the adapter's **Properties > Details > Hardware Ids**, or look up your laptop model's spec sheet.
2. Download the latest Bluetooth driver from your laptop manufacturer's official support page for your exact model.
3. Disconnect from the internet temporarily to prevent Windows Update from interfering mid-install.
4. Run the installer, or in Device Manager choose **Update driver > Browse my computer for drivers** and point at the downloaded files.
5. Restart fully, then confirm Bluetooth appears in both Device Manager and Settings — and test pairing an actual device, not just the toggle.

### Fix 5: Restart the Bluetooth services and run the troubleshooter

With the driver fixed, the service layer may still be stuck. The Bluetooth Support Service must run for the Settings toggle and pairing to work, and updates sometimes leave it disabled.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Find **Bluetooth Support Service**, double-click it, set **Startup type** to **Automatic**, and click **Start** if it is not running.
3. Do the same for **Bluetooth Audio Gateway Service** if it exists on your system.
4. Run **Settings > System > Troubleshoot > Other troubleshooters > Bluetooth > Run** and apply any fixes it suggests.
5. If the troubleshooter reports it could not identify the problem but services are now running, retest pairing — service state and troubleshooter results do not always agree.

### Fix 6: Disable USB selective suspend and Bluetooth power saving

Post-update power-plan resets are a quiet cause of vanishing Bluetooth: the adapter sits on an internal USB bus, and aggressive power saving can keep it asleep through boot so it never enumerates. This fix is especially relevant for laptops.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both battery and plugged-in.
3. In Device Manager, right-click the Bluetooth adapter, open **Properties > Power Management**, and uncheck "Allow the computer to turn off this device to save power."
4. Do the same for the USB Root Hub entries the adapter may sit behind.
5. Shut down fully (Shift + Shut down), cold-boot, and check Device Manager — adapters suppressed by power policy often reappear immediately.

### Fix 7: Uninstall the problematic update or repair Windows

If a specific cumulative update killed Bluetooth and nothing else revives it, remove that update — then protect the working driver before reinstalling updates. This is the last resort before suspecting hardware.

1. Go to **Settings > Windows Update > Update history > Uninstall updates** and remove the most recent update that preceded the failure.
2. After the required restart, verify Bluetooth has returned in Device Manager.
3. Immediately block driver updates (**Device Installation Settings > No**) so a re-offered update does not re-break it.
4. Check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) and the [Update Catalog](https://www.catalog.update.microsoft.com/) for a revised version of the update that addresses Bluetooth regressions.
5. If even update removal fails, the radio itself may have coincidentally failed — but confirm with a Linux live USB (which uses its own Bluetooth stack) before paying for hardware repair, as explained in [our step-by-step Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-step-by-step/).

## Closing

Bluetooth disappearing after a Windows 11 update looks alarming but follows a well-worn script: the update disturbed the driver or power state, and the adapter is waiting to be re-enumerated. The full shutdown, hidden-device cleanup, and driver rollback in the first half of this guide resolve the great majority of cases without touching the update itself. Once Bluetooth is back, block automatic driver replacement and create a restore point — the next feature update will thank you for it.
