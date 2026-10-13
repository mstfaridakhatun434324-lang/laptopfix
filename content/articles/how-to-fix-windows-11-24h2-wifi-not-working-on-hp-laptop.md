---
title: "Windows 11 24H2 Wi-Fi Not Working on Your HP Laptop? How to Fix It"
slug: how-to-fix-windows-11-24h2-wifi-not-working-on-hp-laptop
date: 2026-09-18
categories: ["windows-update"]
tags: ["wifi not working", "windows 11 24h2", "hp laptop", "wireless driver"]
description: "Wi-Fi broke after the Windows 11 24H2 update on your HP laptop? Restore your wireless connection with these driver-focused fixes."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-wifi-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why did 24H2 break my HP laptop's Wi-Fi?"
    a: "The 24H2 feature update commonly replaces HP's customized wireless driver with a generic Microsoft version that does not work correctly with HP's hardware configuration. The adapter may vanish from Device Manager, show a warning icon, or appear fine while refusing to connect. Reinstalling HP's driver fixes the large majority of cases."
  - q: "Should I roll back to the previous Windows version?"
    a: "Only as a last resort. The Wi-Fi problem is a driver issue, not a Windows issue, and it is fixable without abandoning 24H2. Try the driver fixes below first — rollback is a ten-day-limited option that also removes 24H2's security improvements, so it should be the final fallback, not the first response."
  - q: "My Wi-Fi adapter is missing from Device Manager entirely. Is the hardware dead?"
    a: "Probably not. A missing adapter after 24H2 usually means the driver failed to load, not that the hardware died. Check Device Manager's View > Show hidden devices, look under Other devices for an unknown device, and reinstall the HP wireless driver — the adapter typically reappears immediately."
  - q: "Can I prevent Windows Update from breaking the driver again?"
    a: "Yes. After installing HP's working driver, you can block driver updates through Windows Update via Device Installation Settings, or use the Show or hide updates troubleshooter to hide the specific bad driver version. HP's own support assistant can then manage wireless driver updates on your schedule."
---

Few things are as annoying as a feature update that kills your internet. After installing Windows 11 24H2 on an HP laptop, the Wi-Fi may refuse to connect, drop constantly, run at a crawl — or the wireless adapter may vanish entirely. You are not imagining it, and the hardware is almost certainly fine. What happened is that 24H2 replaced HP's tuned wireless driver with a generic one that does not understand your laptop's specific wireless card configuration.

This happens because of how feature updates migrate drivers. During the upgrade, Windows inventories your drivers, installs the new OS, then reinstalls drivers — but where it has a newer "inbox" driver version, it prefers its own over the manufacturer's. For most hardware that is harmless. For HP's wireless cards, which often rely on HP-specific configuration for power management, antenna behavior, and regulatory settings, the generic replacement is a functional downgrade that presents as broken Wi-Fi. The hardware did not change; the software driving it got swapped for a worse version.

The fix is driver surgery, not Windows surgery. Work through these steps in order and your Wi-Fi will be back, usually by Fix 3.

## Why this happens

- **24H2 replaced HP's wireless driver with a generic one.** The generic driver lacks HP-specific configuration for the wireless card and fails or misbehaves.
- **The old driver is incompatible with 24H2's networking stack.** Even HP's previous driver version can break against 24H2's updated Wi-Fi framework.
- **The adapter is disabled in the new power plan.** 24H2's power management can aggressively disable the wireless adapter to save battery.
- **Corrupted driver migration.** The upgrade's driver migration step damaged the installation, leaving a half-configured adapter.
- **BIOS/firmware mismatch.** Old HP BIOS versions can misreport the wireless hardware to 24H2's new driver model.
- **VPN or filter drivers conflicting.** Third-party VPN clients and network filters that worked before can break against the new stack.
- **The WLAN AutoConfig service failed to start.** A disabled or crashed WLAN service leaves Wi-Fi dead regardless of driver state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the basics and the WLAN service

Rule out the simple before touching drivers.

1. Check the physical wireless switch or **Fn** key combo on your HP laptop — 24H2 upgrades have been known to leave the radio switched off.
2. Press **Windows key + R**, type `services.msc`, find **WLAN AutoConfig**, and make sure it is **Running** and set to **Automatic**. Start it if it is not.
3. In **Settings** > **Network & internet** > **Wi-Fi**, confirm Wi-Fi is toggled on and airplane mode is off.

### Fix 2: Inspect Device Manager for the real story

See exactly what 24H2 did to your wireless driver.

1. Open **Device Manager**, expand **Network adapters**, and look for your Wi-Fi adapter. Note any yellow warning icon.
2. If the adapter is missing, click **View** > **Show hidden devices** and check for it grayed out, or look under **Other devices** for an unknown device.
3. Right-click the adapter (if present), choose **Properties**, and read the **Device status** on the General tab — the error code tells you whether this is a driver problem or a hardware detection problem.

### Fix 3: Install HP's 24H2 wireless driver

This is the fix that resolves most cases.

1. On another device (or via Ethernet/USB tethering), go to [HP's support site](https://support.hp.com/us-en) and enter your exact model.
2. Download the latest **wireless/WLAN driver** listed for Windows 11 24H2.
3. In Device Manager, right-click the Wi-Fi adapter, choose **Uninstall device**, and check **Attempt to remove the driver for this device** to purge 24H2's generic version.
4. Install HP's driver and restart. Wi-Fi typically returns immediately.

### Fix 4: Roll back if HP's previous driver worked

When the pre-24H2 driver was fine and the new one is not.

1. In Device Manager, right-click the Wi-Fi adapter > **Properties** > **Driver** > **Roll Back Driver**.
2. Choose "a previous version of the driver worked better" and complete the rollback.
3. Restart and test. Then block the bad driver from reinstalling using the Show or hide updates troubleshooter so 24H2's generic version does not come back.

### Fix 5: Reset the network stack

Clear corrupted network configuration the upgrade left behind.

1. Open an elevated Command Prompt and run, in order:
   ```
   netsh winsock reset
   netsh int ip reset
   ipconfig /release
   ipconfig /renew
   ipconfig /flushdns
   ```
2. Restart the laptop.
3. Reconnect to your Wi-Fi network. This clears the configuration corruption that sometimes survives driver fixes.

### Fix 6: Disable power management on the adapter

Stop 24H2 from putting the adapter to sleep.

1. In Device Manager, right-click the Wi-Fi adapter > **Properties** > **Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. In **Settings** > **System** > **Power & battery** > **Power mode**, avoid the most aggressive battery-saver settings while testing. Constant disconnects after 24H2 are frequently just overzealous power saving.

### Fix 7: Update the BIOS and block future driver replacement

Finish the job so it stays fixed.

1. Install the latest HP BIOS for your model from [HP support](https://support.hp.com/us-en) — BIOS updates fix hardware reporting issues that confuse 24H2's driver model.
2. Go to **System** > **About** > **Advanced system settings** > **Hardware** > **Device Installation Settings** and select **No** to stop Windows Update replacing your working HP driver.
3. If Wi-Fi is still dead after all of this, the ten-day rollback at **Settings** > **System** > **Recovery** > **Go back** remains available, and [Microsoft's Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the official escalation path.

## Closing

24H2 breaking Wi-Fi on HP laptops is a driver replacement problem, and driver replacement problems have driver fixes: identify what 24H2 installed, remove it completely, and install HP's version for your exact model. The network stack reset and power management tweaks handle the secondary issues. Once HP's driver is in place and Windows Update is told to leave drivers alone, the Wi-Fi stays working — which is how it should have been from the start. To keep the rest of the update pipeline healthy afterward, see our [guide to fixing updates stuck downloading on HP laptops](/articles/how-to-fix-windows-update-stuck-downloading-on-hp-laptop/), and learn [how to check exactly when updates installed](/articles/how-to-check-update-installation-date-in-windows-11-24h2/) so you can correlate any future breakage with the update that caused it.
