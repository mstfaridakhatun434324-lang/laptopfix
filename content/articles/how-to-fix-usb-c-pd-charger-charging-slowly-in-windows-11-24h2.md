---
title: "Fix a Slow USB-C PD Charger on Windows 11 24H2"
slug: how-to-fix-usb-c-pd-charger-charging-slowly-in-windows-11-24h2
date: 2026-09-26
categories: ["battery"]
tags: ["usb-c charging", "pd charger", "windows 11 24h2"]
description: "USB-C charger suddenly slow after Windows 11 24H2? Find out why Power Delivery negotiates the wrong wattage and how to restore full-speed charging."
thumbnail: "/images/thumbs/how-to-fix-usb-c-pd-charger-charging-slowly-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my USB-C charger suddenly slow after the Windows 11 24H2 update?"
    a: "The update can reset USB power-delivery drivers or change how Windows negotiates wattage with the charger. The laptop may fall back to a 15W or 27W 'safe' profile instead of the 65W or 100W your brick supports. Reinstalling USB and battery drivers, plus checking the cable, usually restores full speed."
  - q: "How do I check what wattage my laptop is actually charging at?"
    a: "Hover over the battery icon or open Settings > System > Power & battery — Windows 11 shows 'plugged in' status and sometimes a slow-charger warning. For exact wattage, use your manufacturer's tool (Lenovo Vantage, Dell Power Manager) or a USB-C power meter dongle, which shows live negotiated voltage and current."
  - q: "Can the cable really make USB-C charging slow?"
    a: "Absolutely — it's the most common cause. Only cables rated for the wattage you need (look for 100W/5A or 240W markings, or USB-IF certification) can carry full Power Delivery. A cheap charge-only or 60W cable silently caps a 100W charger, and no software fix can override that."
  - q: "Does Windows 11 24H2 limit USB-C charging speed?"
    a: "Windows doesn't impose a wattage cap, but the update can install generic USB drivers that negotiate Power Delivery poorly, or re-enable battery-health features that slow charging near full. The fix is driver and settings work, not fighting an OS limit that doesn't exist."
---

Your USB-C charger used to fill the battery in under two hours. Since the Windows 11 24H2 update, the same brick crawls — Windows even pops up a "slow charger" warning, or the percentage barely moves while you're working. The charger didn't get weaker overnight. Something in the negotiation between laptop, cable, and brick changed.

USB-C Power Delivery is a conversation: the laptop and charger agree on a voltage and current. When that conversation goes wrong, the laptop picks a conservative low-power profile to stay safe. Here's how to get the full wattage back.

## Why this happens

- **Underrated or damaged cable.** The cable is the weakest link — a 60W cable on a 100W charger caps everything at 60W, and a damaged cable can drop negotiation to 15W.
- **Driver reset by the 24H2 update.** Fresh USB and ACPI drivers may negotiate PD profiles poorly until updated.
- **Wrong PD port.** Many laptops have multiple USB-C ports but only one (or some) support full-wattage charging; the update can't change this, but users often switch ports during troubleshooting.
- **Charger wattage below the laptop's needs.** A 45W brick on a laptop that wants 65W+ charges slowly by design — 24H2's warning just made the existing situation visible.
- **Battery-health charging limits.** Vendor apps (MyASUS, Lenovo Vantage) may have re-enabled "slow/optimized charging" modes during the update.
- **Dirty or loose USB-C connector.** Lint or a partially seated plug causes renegotiation loops that settle on the lowest safe wattage.
- **Dock or hub in the middle.** USB-C docks and hubs take their own cut of the power budget before passing the rest to the laptop.

## How to fix it

Work through these in order, from hardware to software.

### Fix 1: Verify the cable is rated for your wattage

1. Check the cable for printed markings: **100W**, **5A**, **240W**, or **USB-IF certified**. No marking usually means a basic 60W-or-less cable.
2. Swap in a known-good cable rated at or above your charger's wattage.
3. Plug it in firmly — USB-C should seat with a solid click and no wobble.
4. Wait 5 minutes and check whether the "slow charger" warning disappears or the percentage climbs faster.

### Fix 2: Use the correct USB-C port

1. Check your laptop's manual or the port icons: charging-capable ports are usually marked with a **plug/lightning symbol** or labeled PD.
2. Move the charger to that port — on many models it's the rear-left port, not the front one.
3. Avoid charging through a dock or hub for this test; plug the brick directly into the laptop.
4. If speed returns on the right port, you've found it — label it mentally and stop here.

### Fix 3: Check the charger's actual output

1. Read the fine print on the brick: it lists PD profiles like **20V⎓3.25A (65W)**.
2. Compare with your laptop's required wattage (on the original charger or the spec sheet).
3. If you're using a phone charger (18–30W) on a 65W laptop, slow charging is expected — get a proper PD brick.
4. For a definitive answer, a $15–20 USB-C power meter shows the live negotiated watts; it's the fastest way to see what the laptop actually agreed to.

### Fix 4: Clean the port and reseat everything

1. Power the laptop off.
2. Shine a light into the USB-C port and pick out lint with a **wooden or plastic toothpick** — never metal.
3. Blow out dust with short bursts of compressed air.
4. Reconnect and check charging speed. A surprising number of "slow charger" cases end here.

### Fix 5: Reinstall USB and battery drivers

1. Open **Device Manager** (**Win + X**).
2. Expand **Universal Serial Bus controllers**. Right-click each **USB Root Hub (USB 3.0)** and **USB-C** related entry > **Uninstall device**. Don't worry — they reinstall on reboot.
3. Expand **Batteries** and uninstall **Microsoft ACPI-Compliant Control Method Battery** and **Microsoft AC Adapter**.
4. Restart the laptop with the charger connected. Windows rebuilds the whole PD negotiation stack fresh.

### Fix 6: Check vendor battery/charging settings

The 24H2 update often reinstalls or resets manufacturer apps.

1. Open **Lenovo Vantage**, **MyASUS**, **Dell Power Manager**, or your brand's equivalent.
2. Look for battery modes like "Battery Health Charging," "Conservation Mode," or "Optimized charging" — set it to **full/balanced charging** while testing.
3. Check for a "slow charging" or "quiet charging" toggle and turn it off.
4. Restart and retest. If speed returns, you can re-enable longevity features later once you know they were the cause.

### Fix 7: Update BIOS, chipset, and USB drivers

1. Download the latest **BIOS** and **chipset** drivers from your manufacturer's support site — [Lenovo](https://support.lenovo.com/us/en/), [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or ASUS.
2. Install chipset first, then BIOS (with AC connected), letting each reboot fully.
3. In **Device Manager**, check **Universal Serial Bus controllers** for any remaining warning icons and update those drivers.
4. Retest charging speed with your rated cable on the correct port.

### Fix 8: Test with the original charger

If you're using a third-party brick, borrow the laptop's original charger for a day.

1. Note the charging speed and whether Windows still shows a slow-charger warning.
2. If the original charger is fast and the third-party one is slow, the third-party brick's PD profiles don't match your laptop — replace it with one that lists your laptop's required voltage profile explicitly.
3. If both are slow, the issue is in the laptop: port, drivers, or battery. Run your vendor's hardware diagnostics and check the [battery health report](/articles/how-to-check-battery-health-on-windows-11-laptop/) for a worn battery that can't accept charge quickly.

## Closing

Slow USB-C charging after 24H2 is a negotiation failure, not a hardware death sentence. Cable first, correct port second, drivers third — that sequence resolves the large majority of cases, and a USB-C power meter takes all the guesswork out if you want certainty. If your charger produces no charging at all rather than slow charging, work through our guide to [USB-C charging not working on Windows 11](/articles/how-to-fix-usb-c-charging-not-working-on-laptop-on-windows-11/) instead — different symptom, different sequence.
