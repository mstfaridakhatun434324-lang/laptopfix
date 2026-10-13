---
title: "WiFi 6 Not Working on Your Laptop? Fix It Here"
slug: how-to-fix-wifi-6-not-working-on-laptop
date: 2026-09-26
categories: ["drivers"]
tags: ["wifi 6", "802.11ax", "intel ax201", "wireless slow", "wifi not connecting"]
description: "WiFi 6 (802.11ax) not working or painfully slow on your laptop? Fix driver, router, and band issues to get full WiFi 6 speeds."
thumbnail: "/images/thumbs/how-to-fix-wifi-6-not-working-on-laptop.webp"
faqs:
  - q: "How do I know if my laptop actually supports WiFi 6?"
    a: "Check Device Manager → Network adapters: Intel AX200, AX201, AX210, AX211, Killer AX1650/1675, MediaTek MT7921/7922, and Qualcomm FastConnect 6900 are WiFi 6 cards. Older cards like Intel AC8265/9260/9560 are WiFi 5 only and cannot do WiFi 6 no matter what driver you install. The card model, not the driver, determines capability."
  - q: "Why is my WiFi 6 slower than my old WiFi 5 connection?"
    a: "Usually a configuration mismatch: the router's WiFi 6 features (OFDMA, 1024-QAM, 160 MHz channels) may be disabled, the laptop may have connected on the 2.4 GHz band instead of 5 GHz, or an outdated driver negotiates a fallback mode. Both ends must have WiFi 6 enabled and use the 5 GHz band for the speed advantage to appear."
  - q: "Do I need a WiFi 6 router to use a WiFi 6 laptop card?"
    a: "No — WiFi 6 cards are fully backward compatible and work fine on WiFi 5 and older routers. You just won't get WiFi 6-specific benefits (higher throughput, better congestion handling) until both the router and the client support it. The card working on an older router but failing on a WiFi 6 router points to a router configuration issue."
  - q: "Can I upgrade my laptop to WiFi 6 with a new card?"
    a: "On many laptops, yes — if the card is a socketed M.2 module and not BIOS-whitelisted. Intel AX210 cards are inexpensive and fit most laptops with an M.2 2230 slot. Check a teardown guide for your model first: some ultrabooks solder the WiFi card, and some Lenovo/HP models whitelist approved cards in BIOS."
---

WiFi 6 promises faster speeds, better congested-network performance, and improved battery life — but only when the whole chain cooperates: a WiFi 6-capable card, a correct driver, a WiFi 6-enabled router, and the right band. Break any link and you get symptoms ranging from "won't connect at all" to "connected but mysteriously slow," which users naturally blame on WiFi 6 itself.

The fixes divide cleanly into laptop-side (driver, card settings) and router-side (WiFi 6 features, channel width, band). Diagnose which side is at fault before changing settings blindly.

## Why this happens

- **Outdated wireless driver:** Old drivers lack proper 802.11ax support or contain WiFi 6 bugs fixed in later releases.
- **Router's WiFi 6 mode disabled:** Many routers ship with 802.11ax mode off or in "compatibility" mode that hobbles performance.
- **Connected on 2.4 GHz instead of 5 GHz:** The big WiFi 6 speed gains need the 5 GHz band; 2.4 GHz connections stay slow.
- **160 MHz channel width disabled:** WiFi 6's top speeds require wide channels that routers often disable by default.
- **WPA3/transition mode conflicts:** Some older WiFi 6 drivers mishandle WPA3, causing connection failures.
- **Intel AX201-specific driver bugs:** The AX201 (common in Intel 10th/11th gen laptops) has well-documented driver quirks.
- **Power management throttling the card:** Aggressive power saving prevents the card from using WiFi 6's higher rates.
- **Router firmware bugs:** Early WiFi 6 router firmware had interoperability bugs with specific client cards.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your card is actually WiFi 6

1. Open **Device Manager → Network adapters** and note the exact card model.
2. WiFi 6 cards include Intel AX200/AX201/AX210/AX211, Killer AX1650/AX1675, MediaTek MT7921/MT7922, Realtek 8852. Intel AC-series cards are WiFi 5 — no driver will change that.
3. If your card is WiFi 5, your options are a card upgrade (Fix 8) or accepting WiFi 5 speeds — don't chase WiFi 6 settings for hardware that can't use them.
4. This check takes 30 seconds and prevents hours of futile troubleshooting.

### Fix 2: Install the latest wireless driver

1. Download the newest driver from your laptop maker's support page, or use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel cards.
2. In Device Manager, uninstall the current wireless driver (delete driver software checked), then install the fresh package and reboot.
3. Intel's driver releases specifically fix 802.11ax interoperability bugs — the changelog often names WiFi 6 fixes directly.
4. For the notoriously finicky AX201, the dedicated [AX201 repair guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) covers card-specific workarounds.

### Fix 3: Force the 5 GHz band

1. In Device Manager, right-click the wireless adapter → **Properties → Advanced** tab.
2. Find **Preferred Band** and set it to **5 GHz** (or "Prefer 5GHz").
3. Set **802.11a/b/g Wireless Mode** or **VHT Mode** to include the highest available (AC/AX).
4. Reconnect and verify in **Settings → Network & internet → WiFi → Hardware properties** that you're on 5 GHz — WiFi 6's headline speeds don't exist on 2.4 GHz.

### Fix 4: Enable WiFi 6 mode on the router

1. Log into your router's admin page (usually 192.168.1.1 or 192.168.0.1).
2. Find the wireless settings and ensure **802.11ax / WiFi 6 mode** is **Enabled** (not Auto-compatibility or Off).
3. Set the 5 GHz **channel width** to **160 MHz** if available (80 MHz minimum for good WiFi 6 performance).
4. Save and reboot the router. Check your laptop's link speed afterward — it should jump significantly.

### Fix 5: Fix WPA3 and security mode issues

1. In the router, try **WPA2/WPA3 Transition mode** first — pure WPA3 breaks some older WiFi 6 drivers.
2. If connections fail entirely on the WiFi 6 network, temporarily set WPA2 only to isolate whether security negotiation is the problem.
3. On the laptop, **forget the network** (Settings → Network & internet → WiFi → Manage known networks) and reconnect fresh after router changes.
4. Update router firmware — vendors fixed many WPA3/ax handshake bugs in later releases.

### Fix 6: Disable power saving on the wireless card

1. In Device Manager → wireless adapter → **Power Management**, uncheck **"Allow the computer to turn off this device to save power."**
2. In **Advanced** tab, set **Transmit Power** to **Highest** and **Power Saving Mode** to **Maximum Performance**.
3. In Windows power plan advanced settings, set **Wireless Adapter Settings → Power Saving Mode** to **Maximum Performance**.
4. Power saving directly caps the modulation rates WiFi 6 uses — this setting alone can double real-world throughput.

### Fix 7: Optimize router placement and channels

1. In the router admin, set the 5 GHz channel manually — try **36-48** (low interference) or use a WiFi analyzer app to find the clearest channel.
2. Keep the router elevated, central, and away from metal objects and microwaves.
3. If the router has **OFDMA** and **MU-MIMO** toggles, ensure both are on — they're core WiFi 6 features.
4. Test speed with the laptop in the same room as the router to establish your baseline before blaming distance. Related band issues are covered in the [5 GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).

### Fix 8: Upgrade the card or use a workaround

1. If your card is WiFi 5 and socketed, an **Intel AX210** (M.2 2230) is a cheap, straightforward upgrade — two antenna wires, one screw.
2. Check BIOS whitelists first on Lenovo/HP business models, which may reject unauthorized cards.
3. As a zero-disassembly alternative, a **USB WiFi 6 adapter** delivers WiFi 6 without opening the laptop.
4. After any hardware change, install the driver from Intel or the maker before expecting WiFi 6 features — Windows' inbox driver may only enable WiFi 5 modes.

## Closing

WiFi 6 problems are chain problems: card, driver, band, router settings. Verify each link in order and the promised speeds appear — most "broken WiFi 6" is just one misconfigured link in an otherwise fine chain. Keep a note of the settings that worked (driver version, router channel width, band preference); WiFi 6 configurations are finicky enough that a future router firmware update can quietly undo them, and your notes turn a repeat diagnosis into a two-minute restore.
