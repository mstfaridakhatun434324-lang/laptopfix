---
title: "Airplane Mode Stuck On? What to Do"
slug: what-to-do-if-airplane-mode-stuck-on
date: 2026-09-22
categories: ["drivers"]
tags: ["airplane mode", "stuck", "wifi", "windows 11"]
description: "Airplane mode won't turn off on your laptop? Fix the stuck toggle with these steps — from quick switches to driver and registry fixes."
thumbnail: "/images/thumbs/what-to-do-if-airplane-mode-stuck-on.webp"
faqs:
  - q: "Why is airplane mode stuck on and greyed out?"
    a: "A greyed-out airplane mode toggle usually means the wireless hardware is disabled at a lower level — a physical Wi-Fi switch, an Fn-key toggle, or a BIOS setting — so Windows has nothing to turn on. It can also mean the Wi-Fi driver has failed. Check the physical switch and Device Manager first; the toggle un-greys itself once the underlying hardware is available again."
  - q: "Can I turn off airplane mode without the toggle working?"
    a: "Sometimes. Try the physical wireless switch or Fn-key toggle, which operate below Windows' software toggle. You can also try restarting the WLAN AutoConfig service or using the network reset feature. But if the toggle is stuck because the Wi-Fi adapter driver has failed, you need to fix the driver first — no toggle workaround will help until the hardware is visible to Windows."
  - q: "Why did airplane mode get stuck after a Windows update?"
    a: "Updates can install an incompatible Wi-Fi driver that fails to initialize the radio, leaving Windows thinking no wireless hardware exists — which freezes the airplane mode state. Rolling back the Wi-Fi driver or installing the manufacturer's version usually unsticks it. The timing correlation with the update is the key diagnostic clue."
  - q: "Does airplane mode stuck on mean my Wi-Fi card is broken?"
    a: "Rarely. In the vast majority of cases it is a software state issue: a stuck service, a bad driver, or a toggled hardware switch. Test with a USB Wi-Fi adapter — if that works fine, your Windows wireless stack is healthy and the internal card's driver or switch state is the problem, not dead hardware."
---

Airplane mode stuck on is a special kind of maddening: the toggle mocks you, greyed out or snapping back on, while your Wi-Fi sits dead. The underlying mechanics are straightforward once you see them. Airplane mode is just Windows telling all radios to shut down — and it gets "stuck" when something prevents the radios from coming back: a hardware switch, a failed driver, or a wedged system service. The toggle is the symptom; the radio state is the disease.

Fixes therefore target the radio layer, not the toggle itself. This guide moves from the physical switches (which override everything) through drivers and services to the deeper resets. For the Windows 11 24H2-specific variant, see our [airplane mode troubleshooting guide](/articles/troubleshoot-airplane-mode-stuck-on/), and if the underlying issue is a vanished adapter, the [missing network adapter guide](/articles/troubleshoot-network-adapter-missing/) covers that path.

## Why this happens

- **Physical wireless switch or Fn key.** A hardware switch turned off — the software toggle cannot override it.
- **Wi-Fi driver failure.** If the adapter driver fails, Windows has no radio to enable and the toggle sticks.
- **WLAN AutoConfig service stuck.** The service managing wireless can wedge in the wrong state.
- **Airplane mode state corruption.** The system state flag itself can corrupt, usually after a bad shutdown or update.
- **BIOS wireless disable.** Firmware-level wireless disable leaves Windows with nothing to turn on.
- **Power management parking the radio.** Deep power states can leave the adapter unresponsive to the toggle.
- **Third-party VPN or network software.** Some network tools hook the radio state and interfere with toggling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical wireless switch and Fn key

Hardware switches override the software toggle completely.

1. Inspect the laptop's sides and front edge for a physical wireless switch — slide it to the on position.
2. Look for a wireless/airplane icon on the function keys (often **F2**, **F8**, or **F12**) and press **Fn + that key**. Try it twice to be sure of the final state.
3. Watch the system tray Wi-Fi icon as you toggle — any change confirms the switch was the blocker.
4. If there is no physical switch and no Fn key, continue — the problem is software.

### Fix 2: Restart the WLAN AutoConfig service

Unwedge the service that manages the radio state.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **WLAN AutoConfig**, right-click it, and choose **Restart**. If it is stopped, choose **Start**.
3. Double-click it and set **Startup type** to **Automatic**.
4. Also restart the **Radio Management Service** if present. Then try the airplane mode toggle again.

### Fix 3: Reinstall the Wi-Fi adapter driver

A failed driver is the most common software cause.

1. Open Device Manager, expand **Network adapters**, and check the Wi-Fi adapter's status — a yellow warning or an error here explains the stuck toggle.
2. Right-click the adapter, choose **Uninstall device**, and check **Attempt to remove the driver**.
3. Restart the laptop and let Windows reinstall, then install the manufacturer's Wi-Fi driver from their support page — for Intel cards, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) finds the right version.
4. After the driver reinstall, the airplane mode toggle usually frees up immediately.

### Fix 4: Use the network reset feature

Reset the entire network state, including the airplane mode flag.

1. Open **Settings > Network & internet > Advanced network settings > Network reset**.
2. Click **Reset now** and confirm. The laptop will restart.
3. After rebooting, check the airplane mode toggle before reconnecting to anything — the reset clears the corrupted state flag.
4. Reconnect to your Wi-Fi network fresh. If the toggle sticks again immediately, a driver or service issue remains — continue below.

### Fix 5: Check BIOS wireless settings

Firmware can hold the radio off where Windows cannot reach.

1. Restart and enter the BIOS (**F2**, **Delete**, **Esc**).
2. Find **Wireless**, **WLAN**, or **Wireless LAN** settings and ensure they are **Enabled**.
3. Look for any **Wireless Switch** behavior setting and set it to OS-controlled if available.
4. Save, exit, and test the toggle in Windows.

### Fix 6: Disable power management on the adapter and Fast Startup

Stop power states from trapping the radio.

1. In Device Manager, open the Wi-Fi adapter's **Properties > Power Management** tab and uncheck **Allow the computer to turn off this device to save power**.
2. Open **Control Panel > Power Options > Choose what the power buttons do**, click **Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
3. Perform a full shutdown (not restart), wait 30 seconds, and power on.
4. Test the airplane mode toggle through several on/off cycles to confirm it is truly unstuck.

### Fix 7: Check for interfering software and test with a USB adapter

Rule out third-party hooks and confirm the stack.

1. Temporarily disable or uninstall VPN clients and third-party firewall/network tools — these hook into the network state and can freeze the toggle.
2. Boot into **Safe Mode with Networking** and test the toggle there. If it works in Safe Mode, a startup program is the culprit — use **msconfig** to isolate it.
3. Plug in a USB Wi-Fi adapter as a test: if it works and the toggle behaves with it, the internal adapter's driver or hardware is the specific problem. [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) documents additional wireless troubleshooting steps.
4. If nothing unsticks the toggle and the internal adapter is invisible even in BIOS, the Wi-Fi card itself may have failed — the USB adapter remains a valid permanent workaround.

## Closing

A stuck airplane mode toggle is Windows telling you the truth: as far as it knows, there is no working radio to turn on. The physical switch check resolves the "it was hardware all along" cases in seconds, the driver reinstall fixes the most common software cause, and the network reset clears the corrupted state flags. Work the list in radio-layer order — switch, driver, service, state — and the toggle almost always comes back to life before the last step.
