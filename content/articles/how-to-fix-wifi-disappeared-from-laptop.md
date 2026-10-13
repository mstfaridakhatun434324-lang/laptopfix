---
title: "How to Fix Wi-Fi That Disappeared from Your Laptop"
slug: how-to-fix-wifi-disappeared-from-laptop
date: 2026-10-01
categories: ["drivers"]
tags: ["wifi disappeared", "wifi adapter", "wireless driver", "no wifi option", "windows 11"]
description: "Wi-Fi disappeared from your laptop entirely? Diagnose whether it is a driver, hardware, or settings problem, and bring the wireless adapter back step by step."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop.webp"
faqs:
  - q: "Why did the Wi-Fi option completely vanish from my laptop?"
    a: "In most cases, Windows can no longer see the wireless adapter, so it removes every Wi-Fi control from the taskbar, Settings, and quick settings. The usual culprits are a failed driver update, the adapter being disabled in Device Manager or BIOS, a hardware kill switch being toggled, or power management shutting the adapter down and failing to wake it. Rarely, it is a dead Wi-Fi card."
  - q: "Can airplane mode cause Wi-Fi to disappear completely?"
    a: "Yes. If airplane mode is stuck on, Windows hides the Wi-Fi toggle and the adapter may show as disabled in Device Manager. Check the physical airplane-mode key on your keyboard and the software switch in quick settings. If the key was pressed accidentally, toggling it back usually restores Wi-Fi within seconds, though some laptops need a restart before the adapter reappears and reconnects to known networks."
  - q: "Should I reinstall the Wi-Fi driver or update it first?"
    a: "Update first, reinstall second. An in-place driver update keeps your saved networks and settings intact, so try that through Device Manager or the manufacturer's support page. If updating does not restore the adapter, do a full uninstall with the Delete driver option checked, restart, and let Windows reinstall fresh. Full reinstallation also clears corrupted driver state that a simple update leaves behind."
  - q: "Does resetting network settings delete my saved Wi-Fi passwords?"
    a: "Yes. A Windows network reset removes all saved wireless networks, passwords, VPN connections, and custom adapter settings, then reinstalls every network adapter. Treat it as a last resort before suspecting hardware failure. Write down any passwords you do not have stored elsewhere, because you will need to re-enter them when you reconnect to each network afterward."
---

Opening your laptop to find no Wi-Fi icon, no networks list, and no Wi-Fi toggle in Settings is disorienting — the laptop looks fine, but the wireless world has simply gone quiet. This is one of the most common Windows laptop problems, and the good news is that it is a software issue more than nine times out of ten. The wireless adapter has not necessarily died; Windows has usually just lost the ability to talk to it.

The key insight is that a missing Wi-Fi option is a symptom, not a diagnosis. Your job is to find out where in the chain things broke: the driver, the Windows network stack, a disabled device, or the physical hardware. Work through the steps below in order. Each fix builds on the last, and most people get their Wi-Fi back before reaching the end.

## Why this happens

- **Corrupted or incompatible Wi-Fi driver:** A Windows update, a failed driver install, or a half-applied manufacturer update can leave the driver in a broken state. Windows then hides the adapter and every Wi-Fi control with it.
- **Adapter disabled in software:** The Wi-Fi adapter can be disabled in Device Manager, in Settings, or through a BIOS toggle. Any one of these removes Wi-Fi from the interface entirely.
- **Airplane mode stuck on:** A stuck airplane-mode key or a bug in Windows can lock the radio off. When airplane mode is on, Windows hides the Wi-Fi toggle rather than showing a disabled one.
- **Power management shutdown:** Windows can power down the Wi-Fi adapter to save battery and then fail to bring it back after sleep or hibernation. This is the classic "Wi-Fi gone after waking the laptop" scenario.
- **Hardware kill switch or function key:** Many laptops have a physical switch, a function-key combination, or a BIOS-level radio toggle. An accidental press kills the radio instantly.
- **Failed Windows network stack:** Winsock corruption or a damaged TCP/IP stack can make the adapter unusable. Device Manager may still show the adapter, but Windows cannot use it.
- **BIOS or UEFI update side effects:** A BIOS update can reset wireless settings to defaults or change how the card is enumerated, causing Windows to lose track of it.
- **Dead or loose Wi-Fi card:** The least common cause, but real — a failed M.2 Wi-Fi card or a card unseated by a drop produces exactly this symptom, and no driver fix will bring it back.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out airplane mode and the kill switch

Start with the simplest explanations, because they are the most embarrassing to miss.

1. Press **Win + A** to open quick settings and confirm airplane mode is off. If it is on, turn it off and wait 30 seconds.
2. Check for a physical Wi-Fi switch or an airplane-mode function key (often **Fn + F2**, **Fn + F3**, or a dedicated key). Press it once and watch for an indicator light.
3. Restart the laptop. A stuck airplane-mode state often clears on a full restart, not just a sleep-wake cycle.
4. If Wi-Fi returns, you are done — but consider disabling the function key in BIOS if it keeps getting bumped accidentally.

### Fix 2: Check whether Windows can see the adapter

This is the diagnostic step that tells you which fixes matter.

1. Press **Win + X** and open **Device Manager**. Expand **Network adapters**.
2. Look for your wireless adapter (Intel, Realtek, MediaTek, or Qualcomm). If it is missing entirely, expand **View → Show hidden devices** and look for a grayed-out entry.
3. If the adapter shows a yellow warning icon, note the error code (Code 10, Code 43, Code 45) — it tells you whether this is a driver failure, a power problem, or a disconnected device.
4. If the adapter is not there at all, even as hidden, skip to Fix 6 — the problem is likely BIOS-level or hardware. For a full walkthrough of this scenario, see our guide on [Wi-Fi disappeared in Windows 11](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 3: Re-enable a disabled adapter

If Device Manager shows the adapter with a small down-arrow, Windows has simply turned it off.

1. Right-click the adapter and choose **Enable device**. Wait 15 seconds and check for the Wi-Fi icon.
2. Also check **Settings → Network & internet → Advanced network settings → Advanced sharing settings** to make sure the adapter is not disabled there.
3. If it re-disables itself after a restart, a startup program or power policy is the culprit — proceed to Fix 5 to disable power management on the adapter.
4. Check BIOS: restart, enter setup (usually **F2** or **Del**), and confirm **Wireless** or **WLAN** is enabled under the device or security settings.

### Fix 4: Update the Wi-Fi driver from the manufacturer

Generic Windows drivers are the single biggest source of vanishing Wi-Fi adapters. Always prefer the laptop maker's driver.

1. Identify your exact model and Wi-Fi card from Device Manager or the laptop's bottom label.
2. Visit the manufacturer's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and download the wireless driver for your exact model.
3. Install it, restart, and check whether the adapter reappears. Manufacturer drivers include card-specific firmware and power tables that generic drivers lack.
4. If you cannot reach the support site on the laptop, download the driver on another device and transfer it via USB. Our companion guide on [Wi-Fi adapter not showing up](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) covers more driver-recovery techniques.

### Fix 5: Stop Windows from powering down the adapter

This fixes the "Wi-Fi gone after sleep" variant permanently.

1. In Device Manager, right-click the Wi-Fi adapter and open **Properties → Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power** and click OK.
3. Open **Settings → System → Power & battery → Power mode** and avoid the most aggressive battery-saver plans if the problem recurs on battery.
4. In **Control Panel → Power Options → Change plan settings → Change advanced power settings**, expand **Wireless Adapter Settings → Power Saving Mode** and set it to **Maximum Performance** on both battery and plugged in.

### Fix 6: Reset the network stack

When the adapter is visible but unusable — or when drivers did not help — the network stack itself may be damaged.

1. Open an elevated Command Prompt and run `netsh winsock reset`, then `netsh int ip reset`, then `ipconfig /flushdns`.
2. Restart the laptop. Windows rebuilds the network stack from scratch during boot.
3. If that fails, go to **Settings → Network & internet → Advanced network settings → Network reset** and run it. This reinstalls all adapters and clears saved networks.
4. After a network reset, reinstall the manufacturer's Wi-Fi driver from Fix 4, because Windows may have fallen back to a generic one.

### Fix 7: Check BIOS and reseat the Wi-Fi card

If nothing above worked, the card may be disabled at the firmware level or physically unseated.

1. Enter BIOS and look for **Wireless**, **WLAN**, or **Wireless Radio** settings. Enable everything related to wireless.
2. If the laptop recently received a BIOS update, check whether a newer BIOS is available from the manufacturer — early firmware releases sometimes break card enumeration.
3. As a last resort on user-serviceable laptops: power down, remove the charger and battery if possible, open the bottom panel, and reseat the M.2 Wi-Fi card, reconnecting both antenna wires (main and aux).
4. If reseating does not help, the card is likely dead. M.2 Wi-Fi cards are inexpensive and user-replaceable on most models — an Intel AX210 upgrade often improves the laptop anyway.

## Closing

Wi-Fi disappearing is almost never the death of your laptop's wireless hardware. It is Windows losing track of the adapter — a driver problem, a disabled device, or a stuck power state in the vast majority of cases. Work the list in order, and note at which step the adapter came back: that tells you what to watch for next time a Windows update tries to break it again.
