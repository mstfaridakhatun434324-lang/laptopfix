---
title: "How to Fix MediaTek Wi-Fi Not Working on a Laptop (Step by Step)"
slug: how-to-fix-mediatek-wifi-not-working-step-by-step
date: 2026-09-14
categories: ["drivers"]
tags: ["mediatek wifi", "wifi not working", "wireless driver", "step by step"]
description: "Fix MediaTek Wi-Fi not working on a laptop step by step: restore the wireless adapter, repair the MediaTek driver, and stabilize the connection."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-step-by-step.webp"
faqs:
  - q: "Why does my MediaTek Wi-Fi keep disconnecting randomly?"
    a: "Random disconnects usually come from aggressive power management turning the adapter off, an outdated driver with poor roaming logic, or the router's band steering confusing the MediaTek chip. Updating the driver from the laptop maker's site and disabling power saving on the adapter resolves most intermittent drops."
  - q: "Is MediaTek Wi-Fi worse than Intel Wi-Fi?"
    a: "MediaTek adapters are competent hardware that suffer mostly from driver maturity issues rather than bad silicon. Early drivers for chips like the MT7921 had well-documented disconnect bugs that later driver releases fixed. With a current driver, a MediaTek adapter performs reliably for everyday use."
  - q: "My Wi-Fi adapter is missing from Device Manager entirely. What now?"
    a: "A missing adapter points to the driver failing to load, the device being disabled in BIOS, or a hardware detection problem. First scan for hardware changes in Device Manager, then reinstall the driver from the laptop manufacturer's support page. If it never appears, check BIOS settings and run the built-in wireless diagnostics."
  - q: "Should I update the MediaTek driver through Windows Update or the manufacturer?"
    a: "Use the laptop manufacturer's driver. MediaTek's Wi-Fi behavior is tuned per laptop design for antenna layout and power limits, and the OEM package includes those calibrations. Windows Update drivers are generic and sometimes reintroduce the disconnect bugs that OEM releases had already fixed."
---

MediaTek Wi-Fi adapters — the MT7921, MT7922, and MT7961 found in millions of budget and midrange laptops — have a reputation for flaky wireless that is only partly deserved. The hardware is fine; the drivers shipped at launch were not, and Windows Update has a habit of reinstalling older, buggier versions over the fixed ones. The result is the familiar pattern: Wi-Fi works, then drops, then vanishes, then works again.

This guide treats MediaTek Wi-Fi as the driver problem it almost always is. You will verify the adapter is present, install the correct driver, fix the power and roaming settings that trigger disconnects, and lock the working driver in place so updates stop breaking it.

## Why this happens

- **Buggy launch-era drivers:** Early MediaTek Wi-Fi 6 drivers had documented disconnect and resume-from-sleep bugs that were fixed only in later releases.
- **Windows Update driver downgrades:** Windows may replace your working OEM driver with an older generic one, reintroducing fixed bugs.
- **Aggressive power management:** Windows turns the adapter off to save power and the MediaTek chip sometimes fails to wake cleanly.
- **Band steering conflicts:** Routers that merge 2.4GHz and 5GHz under one name can confuse the adapter's roaming logic into endless reconnect loops.
- **Corrupted driver state after sleep:** Resume-from-sleep is the single most common trigger for MediaTek disconnects.
- **Antenna or hardware issues:** Rare, but a loose antenna lead (usually after a repair) shows up as weak signal rather than total failure.
- **Router-side incompatibilities:** Some routers' 802.11ax features interact badly with older MediaTek firmware; disabling ax on the router is a valid test.
- **VPN or filter drivers:** Third-party network filter drivers can wedge the adapter's data path even when the radio itself is fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the adapter exists and is enabled

1. Press **Win + X → Device Manager → Network adapters** and look for a **MediaTek Wi-Fi** entry.
2. If it has a down-arrow, right-click → **Enable device**.
3. If it is missing entirely, click **Action → Scan for hardware changes** and watch for it to appear.
4. Check the physical wireless switch or **Fn + wireless key** on your laptop — some models have a hard kill switch that overrides everything.

### Fix 2: Install the correct OEM driver

1. Go to your laptop manufacturer's support page (not MediaTek's generic site) and download the latest **Wi-Fi driver** for your exact model.
2. In Device Manager, right-click the MediaTek adapter → **Uninstall device**, checking **"Attempt to remove the driver"** if offered.
3. Restart, then run the OEM installer as administrator and restart again.
4. Verify the driver date in **Properties → Driver** is recent. OEM drivers carry antenna and power calibrations that generic drivers lack — the same principle behind fixing [Intel AX201 issues](/articles/troubleshoot-intel-wifi-6-ax201-not-working/) with vendor packages.

### Fix 3: Disable power management on the adapter

1. In Device Manager, right-click the MediaTek adapter → **Properties → Power Management**.
2. Uncheck **"Allow the computer to turn off this device to save power"**.
3. Go to **Settings → System → Power & battery → Power mode** and set it to **Best performance** while testing.
4. Also check **Control Panel → Power Options → Change plan settings → Change advanced power settings → Wireless Adapter Settings → Power Saving Mode** and set it to **Maximum Performance** on both battery and plugged in.

### Fix 4: Tune the adapter's advanced settings

1. In the adapter's **Properties → Advanced** tab, find **Roaming Aggressiveness** and set it to **1. Lowest** if you stay near one router — this stops pointless roaming disconnects.
2. Set **Preferred Band** to **5GHz** (or **2.4GHz** if you are far from the router) instead of Auto, to stop band-hopping drops.
3. If you see **802.11a/b/g Wireless Mode** options, try limiting to **802.11ac** if your router's ax implementation seems to trigger the drops.
4. Click OK and test for a full day before judging — some fixes only prove themselves over time.

### Fix 5: Reset the network stack

1. Open **Settings → Network & internet → Advanced network settings → Network reset** and choose **Reset now**.
2. Restart when prompted. This reinstalls all network adapters and clears corrupted TCP/IP and Winsock state.
3. Reconnect to your Wi-Fi network afterward — you will need the password again.
4. For a manual approach, run in an elevated Command Prompt: **netsh winsock reset** and **netsh int ip reset**, then restart.

### Fix 6: Rule out the router

1. Test the laptop on a different network — a phone hotspot is perfect for this.
2. If Wi-Fi is stable on the hotspot but not your router, log into the router and try disabling **802.11ax / Wi-Fi 6 mode** or **band steering**.
3. Update the router's firmware; older firmware plus newer client drivers is a classic mismatch.
4. Try a different Wi-Fi channel to rule out interference, especially on crowded 2.4GHz.

### Fix 7: Stop Windows from replacing the driver

1. Once Wi-Fi is stable, set **Device Installation Settings** to **No** (**System → About → Advanced system settings → Hardware**).
2. This blocks Windows Update from reinstalling the older generic MediaTek driver that caused the original problem.
3. Check [Microsoft support](https://support.microsoft.com/en-us/windows) for the "show or hide updates" tool if a specific update keeps reappearing — the same technique used when [driver updates keep failing](/articles/troubleshoot-driver-updates-keep-failing-windows-update/).

### Fix 8: Check for hardware failure

1. Boot a Linux live USB — if Wi-Fi works flawlessly there, your hardware is fine and Windows is the problem.
2. Run your laptop maker's built-in wireless diagnostics (many have one in BIOS or a support app).
3. If the adapter never appears in Device Manager even after a scan and BIOS shows wireless enabled, the card itself may have failed — on many laptops the Wi-Fi card is a replaceable M.2 module.

## Closing

MediaTek Wi-Fi problems are driver problems wearing a hardware costume. The winning formula is consistent: install the laptop maker's latest driver, turn off the power-saving features that put the adapter to sleep, simplify the roaming decisions it has to make, and then lock that working driver in place so Windows Update cannot undo your work.
