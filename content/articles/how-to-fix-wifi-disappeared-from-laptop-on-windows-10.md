---
title: "Wi-Fi Disappeared From Your Laptop on Windows 10? 7 Fixes That Work"
slug: how-to-fix-wifi-disappeared-from-laptop-on-windows-10
date: 2026-09-06
categories: ["drivers"]
tags: ["wifi", "windows 10", "wireless", "network", "disappeared"]
description: "Wi-Fi option completely gone from your Windows 10 laptop? 7 fixes to bring it back — from airplane mode checks to network resets and driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop-on-windows-10.webp"
faqs:
  - q: "Why did the Wi-Fi option vanish from Windows 10?"
    a: "Windows 10 hides the entire Wi-Fi section when it can't communicate with the wireless adapter. The usual triggers: a Windows update replaced the wireless driver with a broken one, the adapter got disabled in Device Manager or BIOS, airplane mode got stuck on, or the WLAN AutoConfig service stopped. The hardware is rarely at fault."
  - q: "What's the difference between Wi-Fi disappeared and no internet?"
    a: "No internet means Wi-Fi is visible and connected (or trying) but traffic doesn't flow — a router or ISP issue. Wi-Fi disappeared means the Wi-Fi toggle, network list, and sometimes the adapter itself are gone from Windows entirely — a local driver or hardware-state problem. They need completely different fixes, so identifying which you have matters."
  - q: "Can airplane mode get stuck and hide Wi-Fi permanently?"
    a: "Yes — this is a real Windows 10 bug on some laptops. The airplane mode toggle gets stuck in the on position at a system level even when the UI shows it off, which keeps the radio disabled and hides Wi-Fi. Toggling airplane mode on and off deliberately, or resetting it via Settings, usually unsticks it."
  - q: "Should I reset my network settings if Wi-Fi disappeared?"
    a: "It's an effective fix but a destructive one — a network reset erases saved Wi-Fi passwords, VPN profiles, and custom network settings. Try the driver and service fixes first. Use the network reset when those fail, and make sure you know your Wi-Fi password before you start, because you'll need to re-enter it."
---

The Wi-Fi icon is gone from the taskbar. Settings > Network & Internet shows Ethernet and maybe VPN, but no Wi-Fi section at all — as if wireless never existed on this laptop. On Windows 10, this total disappearance means Windows has lost communication with the wireless adapter, and the fix depends on which layer broke: a stuck toggle, a dead service, or a bad driver.

Don't confuse this with weak signal or "connected, no internet" — those are different problems with different fixes. A missing Wi-Fi section is a local system issue, and it's very fixable. Work through the seven fixes below in order. If your adapter is missing from Device Manager entirely, our [adapter-missing guide](/articles/how-to-fix-network-adapter-missing-in-windows-11-24h2/) covers the deeper hardware-visibility problem.

## Why this happens

- **Airplane mode is stuck on** — the toggle desyncs and keeps the radio disabled invisibly.
- **The wireless adapter is disabled in Device Manager** — updates or power settings turned it off.
- **The WLAN AutoConfig service stopped** — without this service, Windows 10 can't manage wireless at all.
- **A Windows update broke the wireless driver** — the new driver fails, hiding the whole Wi-Fi subsystem.
- **The Wi-Fi driver is corrupted** — damaged files prevent the adapter from initializing.
- **Power management disabled the adapter** — aggressive saving turned the radio off and never woke it.
- **The network stack is corrupted** — damaged Winsock/TCPIP components break wireless initialization.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle airplane mode deliberately

Airplane mode desync is a genuine Windows 10 bug: the system thinks it's on while the UI suggests otherwise, keeping the radio off and Wi-Fi hidden. Force a resync by turning airplane mode explicitly ON, waiting ten seconds, then turning it OFF. Do this in Settings rather than the Action Center toggle — the Settings path is more reliable at actually flipping the underlying state.

1. Open **Settings > Network & Internet** and find the **Airplane mode** toggle.
2. Turn it **ON**, wait a full 10 seconds.
3. Turn it **OFF** and wait another 10 seconds.
4. Check whether the Wi-Fi section reappears in Network & Internet.

### Fix 2: Check the wireless adapter in Device Manager

The adapter might be present but disabled — Windows 10 hides Wi-Fi settings for disabled adapters. Open Device Manager, expand Network adapters, and look for your wireless device. A down-arrow icon means disabled: right-click and enable it. If the adapter isn't listed, enable "Show hidden devices" from the View menu — it may be hiding there. For the full hidden-device technique, see our [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/), which covers adapter visibility issues too.

1. Open **Device Manager** and expand **Network adapters**.
2. If the wireless adapter shows a down arrow, right-click and choose **Enable device**.
3. If it's absent, click **View > Show hidden devices** and look again.
4. Check **Settings > Network & Internet** for the Wi-Fi section after enabling.

### Fix 3: Restart the WLAN AutoConfig service

WLAN AutoConfig is the Windows 10 service that manages all wireless connections — if it's stopped or disabled, the Wi-Fi section vanishes completely. Updates sometimes leave it in a bad state. Open the Services console, find it, set it to Automatic, and start it. This single fix resolves a large share of disappearance cases, especially those that appeared after updates.

1. Press **Windows + R**, type `services.msc`, and press **Enter**.
2. Find **WLAN AutoConfig**, double-click it.
3. Set **Startup type** to **Automatic** and click **Start** if it's stopped.
4. Wait 30 seconds, then check for the Wi-Fi section in Settings.

### Fix 4: Update or reinstall the wireless driver

A broken wireless driver hides the entire Wi-Fi subsystem. In Device Manager, right-click the wireless adapter and try Update driver first — but don't trust "best driver already installed." The reliable path is downloading the wireless driver for your exact model from the manufacturer's support site (or Intel/Realtek directly) and installing it manually. If the adapter shows an error code, uninstall it completely first, then install fresh.

1. Download the Wi-Fi driver for your exact laptop model from the manufacturer's site.
2. In **Device Manager**, right-click the wireless adapter and choose **Uninstall device**.
3. Check **Delete the driver software for this device** if the option appears, then confirm.
4. Restart, install the downloaded driver, restart again, and check for Wi-Fi.

### Fix 5: Disable power management on the wireless adapter

Windows 10's power saving can switch the wireless adapter off and fail to bring it back — particularly on battery power. In the adapter's Properties, the Power Management tab has the "allow the computer to turn off this device" checkbox. Uncheck it. The battery cost is trivial, and it eliminates an entire class of "Wi-Fi vanished after sleep" problems.

1. In **Device Manager**, right-click the wireless adapter and choose **Properties**.
2. Open the **Power Management** tab.
3. Uncheck **Allow the computer to turn off this device to save power**.
4. Click **OK**, restart, and verify Wi-Fi appears and stays.

### Fix 6: Reset TCP/IP and Winsock

Corrupted network stack components can prevent the wireless subsystem from initializing, which presents as missing Wi-Fi. The netsh reset commands rebuild Winsock and the TCP/IP stack from scratch. Run them from an elevated Command Prompt in order, restart, and check. This is non-destructive to your files — it only resets network configuration.

1. Open **Command Prompt as administrator** (right-click Start > Command Prompt (Admin)).
2. Run `netsh winsock reset` and press Enter.
3. Run `netsh int ip reset` and press Enter.
4. Restart the laptop and check whether Wi-Fi has returned.

### Fix 7: Perform a Windows 10 network reset

The nuclear option for software causes: Settings > Network & Internet > Status > Network reset reinstalls all network adapters and wipes every network configuration back to defaults. It erases saved Wi-Fi passwords and VPN settings, so have your Wi-Fi password ready. After the automatic restart, Wi-Fi should be back — reconnect and re-enter your password. Microsoft documents this at [Windows support](https://support.microsoft.com/en-us/windows).

1. Go to **Settings > Network & Internet > Status**.
2. Click **Network reset** at the bottom, then **Reset now**.
3. Confirm and let the laptop restart automatically.
4. Reconnect to your Wi-Fi network with your password.

## Closing

Wi-Fi disappearing from Windows 10 is Windows losing contact with the wireless adapter — usually a stuck airplane mode, a stopped WLAN service, or a bad driver update. The service restart and driver reinstall in the middle fixes resolve the vast majority of cases. And remember the password warning before any network reset: it's the one fix here with a real cost, so save it for when the gentler options have failed.
