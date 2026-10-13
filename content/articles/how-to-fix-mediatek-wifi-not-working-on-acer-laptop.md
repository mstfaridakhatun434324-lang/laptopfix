---
title: "MediaTek WiFi Not Working on Acer Laptop? Fix It Fast"
slug: how-to-fix-mediatek-wifi-not-working-on-acer-laptop
date: 2026-09-27
categories: ["drivers"]
tags: ["acer laptop", "mediatek wifi", "mt7921", "wireless driver", "wifi not working"]
description: "Fix MediaTek WiFi not working on Acer laptops: repair the MT7921/MT7922 driver, fix code 10 errors, and restore wireless connectivity step by step."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-on-acer-laptop.webp"
faqs:
  - q: "Why does my Acer laptop's MediaTek WiFi stop working after Windows updates?"
    a: "Windows Update frequently replaces Acer's validated MediaTek driver with a generic build the card rejects, causing Code 10 or Code 43 errors. Download the Wireless LAN (MediaTek) driver from Acer support for your exact model, uninstall the current driver with the 'remove driver' option, and install Acer's package."
  - q: "What is Code 10 on a MediaTek WiFi adapter?"
    a: "Code 10 means this device cannot start — the driver failed to initialize the MediaTek card. On the MT7921 and MT7922 this almost always indicates a driver mismatch rather than dead hardware, typically after Windows Update installed a generic build. Uninstall the driver with the remove option checked, then install Acer's Wireless LAN driver package for your exact model."
  - q: "Why does my WiFi disconnect after sleep on my Acer laptop?"
    a: "Windows power management is turning the adapter off and it fails to wake. Uncheck 'Allow the computer to turn off this device' in the adapter's Power Management tab and set Wireless Adapter Settings to Maximum Performance in your power plan."
  - q: "Should I use MediaTek's driver or Acer's driver?"
    a: "Use Acer's driver for your exact model. Acer validates the driver against the card's firmware revision, the laptop's antenna design, and its power delivery — three variables generic drivers get wrong. MediaTek-direct or Windows Update drivers are the most common source of these failures, so Acer's package is always the safer and more stable choice."
---

MediaTek WiFi cards — the MT7921 and MT7922 found in millions of Acer Aspire, Swift, and Nitro laptops — have a reputation. They work fine until a Windows update swaps their driver, and then the WiFi vanishes, crawls, or throws cryptic errors. If your Acer's wireless died overnight, the MediaTek driver is suspect number one.

The good news: this is almost never dead hardware. The card is usually fine; it is the driver binding, the power management, or Windows' enthusiastic driver replacement that broke. The pattern is so consistent that technicians check the driver date before anything else.

Below is the exact sequence that restores MediaTek WiFi on Acer laptops, from the 30-second checks to the full driver rebuild.

## Why this happens

- **Windows replaced the MediaTek driver:** Windows Update installs a generic or mismatched MediaTek driver that the card rejects — often showing Code 10 or Code 43 in Device Manager.
- **Driver power management shutting the card off:** Aggressive power saving disables the WiFi adapter to save battery and it never wakes, especially after sleep.
- **Corrupted driver binding after feature update:** Major Windows updates can leave the old driver half-registered: the device appears with a warning icon and will not start.
- **Acer Care Center driver mismatch:** Acer's own driver builds are tuned for the card's firmware; mixing an Acer driver with a MediaTek-direct driver can conflict.
- **Router-side incompatibilities:** Some MediaTek firmware revisions clash with specific router features (802.11ax target wake time, certain WPA3 modes), causing drops rather than total failure.
- **Antenna leads disturbed:** On laptops that were opened for RAM/SSD upgrades, the tiny antenna connectors on the WiFi card pop off easily — weak or no signal results.
- **BIOS wireless toggle disabled:** Some Acer BIOS versions have a wireless device toggle that updates can flip off.
- **Fast Startup preserving a dead adapter state:** The hibernated driver state keeps the card wedged across reboots until a full shutdown clears it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Device Manager for the card's true state

Read the error before treating it — the code tells you which fix to use.

1. Open **Device Manager → Network adapters** and find the **MediaTek Wi-Fi** entry.
2. If it shows a yellow warning, double-click it and read the **Device status** on the General tab — note Code 10, 43, or 45 exactly.
3. If the adapter is missing entirely, click **View → Show hidden devices** — a grayed-out entry means Windows disabled it or it failed to start.
4. Check the **Driver** tab for the driver date: a very recent date matching a Windows update confirms the driver-swap theory.

### Fix 2: Install the Acer MediaTek driver package

The fix for most Code 10/43 cases: the exact driver Acer validated for your model.

1. Go to Acer's support site, enter your exact model, and download the **Wireless LAN (MediaTek)** driver.
2. In Device Manager, right-click the MediaTek adapter → **Uninstall device**, checking **Attempt to remove the driver**.
3. Reboot, then install the Acer driver package you downloaded.
4. Reboot once more and verify the adapter starts cleanly with no warning icon.

### Fix 3: Disable power management on the adapter

This stops Windows from putting the card to sleep — the classic fix for WiFi that dies after sleep or idles out.

1. In Device Manager, right-click the MediaTek adapter → **Properties → Power Management** tab.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. Go to **Advanced** tab: set **Power Saving Mode** to **Maximum Performance** and disable any **Selective Suspend** options.
4. In **Power Options → Advanced**, set **Wireless Adapter Settings → Power Saving Mode** to **Maximum Performance** for both battery and plugged in.

### Fix 4: Reset the network stack

When the driver is fine but connections still fail, the Windows network stack itself is corrupted.

1. Open **Settings → Network & internet → Advanced network settings → Network reset** and click **Reset now**.
2. Alternatively, in an elevated Command Prompt run: **netsh winsock reset**, **netsh int ip reset**, then **ipconfig /flushdns**.
3. Reboot. You will need to re-enter WiFi passwords — that is expected.
4. Reconnect to your network and test for stability over 30 minutes.

### Fix 5: Turn off Fast Startup and do a full shutdown

A wedged adapter state can survive normal reboots.

1. Open **Control Panel → Power Options → Choose what the power buttons do → Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup**, then **Shut down** (not restart).
3. Wait 15 seconds, power on, and check whether the adapter now starts.
4. If it does, the hibernated driver state was the problem — leave Fast Startup off.

### Fix 6: Tune router-side settings for MediaTek compatibility

If the card connects but drops constantly, the router and card are disagreeing.

1. Log into your router and try disabling **802.11ax / WiFi 6 mode** temporarily, or set the 5 GHz band to **802.11ac** only as a test.
2. Disable **Target Wake Time (TWT)** if your router exposes it — several MediaTek firmware builds handle it badly.
3. Try **WPA2** instead of WPA3 on your network as a diagnostic step.
4. If stability returns, update the router firmware, then re-enable features one at a time.

### Fix 7: Check BIOS and physical antenna connections

When software fixes all fail, verify the hardware layer.

1. Enter BIOS (F2 on Acer) and confirm any **Wireless** or **WLAN** device toggle is **Enabled**.
2. If the laptop was recently opened, re-check the two tiny antenna leads on the WiFi card — they snap on with light pressure and pop off easily.
3. In Device Manager, try **Roll Back Driver** if the option is available — the previous driver was working, after all.
4. As a final test, boot a Linux live USB: working WiFi there proves the hardware is fine and the fault is purely Windows drivers.

## Closing

MediaTek WiFi failures on Acer laptops follow a script: Windows swaps the driver, power management wedges the card, and the user assumes the hardware died. It didn't. Install Acer's exact driver, strip the power-saving behavior, and reset the stack — that sequence restores wireless in the overwhelming majority of cases. Block the generic driver from returning and you won't be doing this again next month. If Device Manager reports Code 10 specifically, our [Code 10 WiFi repair](/articles/how-to-fix-wifi-driver-code-10-error-on-dell-laptop/) walks through that error in depth. Persistent power-related crashes may also involve [driver power state failures](/articles/driver-power-state-failure-windows-11-fix/). Microsoft also documents wireless repair steps at [Windows network support](https://support.microsoft.com/en-us/windows).
