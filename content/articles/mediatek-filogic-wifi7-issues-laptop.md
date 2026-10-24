---
title: "How to Fix MediaTek Filogic Wi-Fi 7 Issues on Laptops"
slug: mediatek-filogic-wifi7-issues-laptop
date: 2026-10-24
categories: ["ai-pc"]
tags: ["mediatek", "filogic", "wifi 7", "wireless", "windows 11", "troubleshooting"]
description: "MediaTek Filogic Wi-Fi 7 dropping or slow on your laptop? Follow these step-by-step fixes for the right driver, router settings, and power management."
thumbnail: "/images/thumbs/mediatek-filogic-wifi7-issues-laptop.webp"
faqs:
  - q: "Which MediaTek cards support Wi-Fi 7?"
    a: >
      The MediaTek Filogic 380 (MT7927) and Filogic 360 (MT7925) are the Wi-Fi 7 capable parts found in laptops. Older MT7921/MT7922 cards are Wi-Fi 6/6E only and cannot do Wi-Fi 7 regardless of driver.
  - q: "Where do I download Filogic Wi-Fi 7 drivers?"
    a: >
      From your laptop maker's support page first — OEMs validate the driver against their antenna design. MediaTek also publishes drivers through Windows Update; check optional updates if the OEM page is stale.
  - q: "Why does my Filogic card only connect at Wi-Fi 6 speeds?"
    a: >
      The usual reasons: the router is not actually broadcasting Wi-Fi 7, the driver is outdated, or Windows is older than 24H2. Confirm the router's BE mode is on and the driver is current before suspecting the card.
  - q: "My Filogic Wi-Fi disconnects when the laptop sleeps. How do I fix it?"
    a: >
      Disable the adapter's power-saving in Device Manager (uncheck the allow-turn-off box) and set the wireless power plan to Maximum Performance. If the adapter vanishes entirely after sleep, update the driver — that is a known fixed bug in newer releases.
---

Your laptop's MediaTek Filogic Wi-Fi 7 card connects at disappointing speeds, drops under load, or disappears after sleep — while your friend's Intel-based laptop on the same router is flawless. It is tempting to blame the card, but MediaTek's BE silicon is solid; the failures are almost always drivers, power management, or router negotiation.

Filogic 380/360 cards appear in a growing share of AMD and Intel AI laptops as OEMs diversify beyond Intel wireless. They need the same four-layer alignment as any Wi-Fi 7 setup — BE card, Windows 11 24H2+, current driver, BE-configured router — plus attention to MediaTek-specific driver quirks around sleep/wake and band behavior. The laptop-side checklist mirrors our [Wi-Fi 7 not working guide](/articles/wifi-7-not-working-windows-11/); this guide focuses on Filogic-specific angles. Similar wireless-driver detective work also applies to [ThinkPad T14s Gen 6 problems](/articles/lenovo-thinkpad-t14s-gen6-problems/) and [natural-language file search issues](/articles/file-search-natural-language-not-working/) where drivers are the hidden culprit. Driver trouble can cascade into OS features too — if search indexing broke after a driver change, [rebuilding the Recall search index](/articles/rebuild-recall-search-index/) may help.

This guide gives you six fixes in order: confirm the card model, install the right driver, fix speed negotiation, resolve drops, fix sleep/wake disappearance, and reset the network stack.

## Why this happens

- **Wrong card assumed to be Wi-Fi 7:** MT7921/MT7922 are Wi-Fi 6/6E. Only Filogic 380 (MT7927) and 360 (MT7925) do Wi-Fi 7 — misidentified cards produce "not working" reports for a feature the hardware lacks.
- **Outdated Filogic driver:** MediaTek's early BE drivers had real bugs — sleep/wake failures, MLO drops, slow negotiation. Current drivers fixed most of them; old drivers did not.
- **Windows Update driver downgrade:** Windows Update occasionally replaces the OEM's newer Filogic driver with an older inbox version, regressing Wi-Fi 7 support overnight.
- **Router BE misconfiguration:** The Filogic cards negotiate down politely — a router with BE mode off yields Wi-Fi 6 speeds with no error, looking exactly like a card problem.
- **Aggressive power management:** Windows' default wireless power saving hits MediaTek cards harder than some competitors — drops, slow reconnects, and post-sleep disappearance.
- **Band and channel negotiation quirks:** Some Filogic driver versions prefer 5 GHz over 6 GHz or mishandle 320 MHz channels on certain routers, capping speeds.
- **Corrupted wireless profile or stack:** Damaged saved-network profiles or Winsock state cause failures that persist across driver updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the exact Filogic card model

Verify the silicon before troubleshooting — the model number decides what is possible.

1. Open **Device Manager > Network adapters** and read the full wireless adapter name.
2. Look for **MT7927** (Filogic 380), **MT7925** (Filogic 360), or **Filogic** branding — these are Wi-Fi 7 capable.
3. If you see **MT7921** or **MT7922**, your card is Wi-Fi 6/6E — Wi-Fi 7 is not available, and no driver will change that.
4. Note the driver version and date in **Properties > Driver** — you will compare it after updating.
5. Confirm Windows 11 **24H2** or newer in **Settings > System > About** — older builds cannot do Wi-Fi 7 regardless of card.

### Fix 2: Install the correct Filogic driver

The driver is the fix in most Filogic cases. Get it from the right source and verify it stuck.

1. Go to your laptop maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) and download the latest wireless driver for your exact model.
2. Check **Settings > Windows Update > Advanced options > Optional updates** too — newer Filogic drivers often land there before the OEM page updates.
3. Install the driver package and restart even if not prompted.
4. Recheck **Properties > Driver** in Device Manager — confirm the version actually changed (Windows sometimes keeps the old driver if the install is blocked).
5. If the version did not change, uninstall the device (checking **delete driver**) from Device Manager, restart, and install the downloaded package again.

### Fix 3: Fix speed negotiation and band behavior

Driver current, router BE-capable, but speeds disappoint — force the negotiation to behave.

1. Verify the router: Wi-Fi 7/BE mode on, current firmware, 6 GHz radio on, 320 MHz channels allowed.
2. On the laptop, check **Settings > Network & internet > Wi-Fi > Hardware properties** for the reported protocol and band while connected.
3. In Device Manager, open the adapter's **Advanced** tab and set **Preferred Band** to **6 GHz** (near the router) to stop the driver camping on 5 GHz.
4. Forget and rejoin the network to force a fresh capability negotiation against the current router config.
5. Test speed at close range on 6 GHz — if it hits expected BE speeds there, the card is fine and remaining issues are band/range behavior.

### Fix 4: Resolve drops and instability under load

Connections drop during large downloads or video calls — stabilize the link.

1. In the adapter's **Power Management** tab, **uncheck** "Allow the computer to turn off this device to save power."
2. Set **Settings > System > Power & battery > Power mode** to **Best performance** while testing plugged in.
3. In the **Advanced** tab, look for transmit power or power-saving mode settings and set them to maximum performance as a test.
4. On the router, try disabling MLO temporarily — early Filogic MLO implementations dropped on some router firmware.
5. If drops happen only on one network, test the laptop on a different BE network to isolate router vs. client.

### Fix 5: Fix the adapter vanishing after sleep

The classic Filogic bug: sleep the laptop, wake it, and Wi-Fi is gone until reboot. Newer drivers fixed this — but verify.

1. Update the driver per Fix 2 first — the sleep/wake reinitialization bug is fixed in current Filogic drivers.
2. Disable **Modern Standby** network disconnection if your OEM exposes it: check the BIOS/UEFI power settings and the OEM's power utility.
3. In Device Manager **Power Management**, uncheck the allow-turn-off box (also from Fix 4 — confirm it persisted).
4. As a workaround while testing, use **Hibernate** instead of **Sleep** — hibernate fully reinitializes the adapter on wake.
5. If the adapter still vanishes after sleep on the latest driver, file it with your OEM with the driver version and sleep/wake repro steps — this is a driver bug they need to hear about.

### Fix 6: Reset the network stack and profiles

Correct driver, correct router, still failing — clear corrupted network state.

1. In an elevated Terminal, run `netsh winsock reset` and `netsh int ip reset`, then restart.
2. Forget all saved Wi-Fi networks (**Settings > Network & internet > Wi-Fi > Manage known networks**) and rejoin only your main network.
3. Use **Settings > Network & internet > Advanced network settings > Network reset** as the heavier option — it reinstalls adapters and clears everything.
4. After the reset, reinstall the OEM Filogic driver from Fix 2 (the reset can revert to the inbox driver).
5. Reconnect fresh and verify the protocol, band, and a sustained speed test.

## Closing

Filogic Wi-Fi 7 cards reward the same discipline as every other BE client: confirm the exact model, keep the driver current from the OEM, configure the router's BE features, and tame power management. The sleep/wake disappearance that gave these cards a bad reputation is fixed in current drivers — if you are still seeing it, you are almost certainly on an old driver. And the honest check from Fix 1 stands: MT7921/7922 owners are not missing a driver update, they are missing Wi-Fi 7 hardware. For general wireless diagnostics, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the built-in network troubleshooting tools.
