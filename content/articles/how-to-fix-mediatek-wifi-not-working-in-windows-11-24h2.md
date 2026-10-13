---
title: "MediaTek Wi-Fi Not Working in Windows 11 24H2? Here's the Fix"
slug: how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2
date: 2026-09-08
categories: ["drivers"]
tags: ["mediatek wifi", "windows 11 24h2", "wireless driver", "mt7921"]
description: "MediaTek MT7921/MT7922 Wi-Fi dead or dropping after Windows 11 24H2? This guide covers the chipset-specific fixes — driver versions that work and the settings that matter."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is MediaTek Wi-Fi especially fragile on Windows 11?"
    a: "MediaTek's MT7921 and MT7922 cards depend heavily on exact driver-firmware pairing, and Windows Update frequently installs a driver build that mismatches the card's firmware. The result is the classic MediaTek pattern: the adapter appears in Device Manager but shows Code 10, or Wi-Fi works until the laptop sleeps and then never recovers."
  - q: "Which driver version should I install for the MT7921?"
    a: "Install the Wi-Fi driver your laptop manufacturer lists for your exact model — vendors validate specific MediaTek builds against their hardware. If the vendor package is outdated, MediaTek's own newer releases sometimes help, but avoid random driver-aggregator sites. The laptop maker's package is the safe baseline that is known to pair with your card's firmware."
  - q: "Why does my MediaTek Wi-Fi die after sleep but work after restart?"
    a: "That pattern points to power management, not a broken card. The 24H2 update's power policies suspend the MediaTek adapter during sleep and the driver fails to reinitialize it on wake. Disabling 'allow the computer to turn off this device' on the adapter and turning off USB/Wi-Fi power saving in the power plan fixes the wake failure."
  - q: "Should I replace the MediaTek card with an Intel AX210?"
    a: "Swapping to an Intel AX210 is a popular and effective upgrade for laptops with a replaceable M.2 Wi-Fi card — Intel's driver support is more consistent. But try the driver and power fixes first; most MediaTek issues are software. Also check your laptop's BIOS whitelist and warranty terms before swapping hardware."
---

MediaTek Wi-Fi cards — the MT7921 (Wi-Fi 6) and MT7922 (Wi-Fi 6E) found in countless budget and mid-range laptops — have a reputation. They work beautifully until a Windows update arrives, and then they develop personalities: Code 10 errors in Device Manager, Wi-Fi that dies every time the laptop sleeps, connections that drop under load. The Windows 11 24H2 update triggered a fresh wave of these failures.

The root cause is almost always the driver-firmware pairing. MediaTek cards are picky about exact driver builds in a way Intel cards are not, and Windows Update's habit of installing whatever MediaTek build is newest breaks that pairing. The fixes below are ordered for MediaTek specifically: identify the exact card, install the right driver build, then lock down the power settings that kill these cards after sleep. For Intel wireless problems, our [Intel AX201 repair guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-windows-11/) covers the other major chipset.

## Why this happens

- **Windows Update installed a mismatched MediaTek driver.** The new build does not pair with the card's firmware — Code 10 follows.
- **Driver corrupted during 24H2 migration.** The MediaTek driver's firmware blob did not survive the update intact.
- **Power management suspends the card.** 24H2's aggressive policies kill the adapter on sleep and it cannot reinitialize.
- **Old driver remnants conflict.** Fragments of the previous MediaTek install fight the new one in the driver store.
- **Bluetooth coexistence misconfigured.** The combo card's Bluetooth and Wi-Fi drivers disagree after the update.
- **Roaming aggressiveness set wrong.** Bad defaults cause drops when moving between access points.
- **BIOS wireless settings reset.** Firmware updates bundled with 24H2 can toggle wireless or ASPM settings.
- **Antenna or card seating loosened.** Thermal cycling can unseat the M.2 card — rare, but real.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your exact MediaTek card

Open **Device Manager**, expand **Network adapters**, and note the exact name — **MediaTek Wi-Fi 6 MT7921 Wireless LAN Card** or **MT7922**, plus the driver version under **Properties > Driver**. Knowing the exact card and the currently installed version matters because MediaTek fixes are version-specific: you need to know what broke to pick the replacement. If the card shows a yellow warning with Code 10, note that too. If the card is missing entirely, check for unknown devices and scan for hardware changes before assuming hardware failure.

### Fix 2: Clean-reinstall the MediaTek driver

Right-click the MediaTek adapter in Device Manager, choose **Uninstall device**, and check **Attempt to remove the driver for this device**. This is critical for MediaTek — a plain uninstall without driver deletion leaves the mismatched build in the driver store, and Windows reinstalls the same broken version. Restart. If Windows installs a working driver on boot, test thoroughly including a sleep/wake cycle. If it reinstalls the broken one, you need the vendor package next.

### Fix 3: Install the laptop maker's MediaTek driver

Go to your laptop manufacturer's support site — [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), ASUS, or Acer — enter your exact model, and download the **MediaTek Wi-Fi driver** listed for Windows 11. Install it and restart. Vendor packages are validated against your card's firmware revision, which is exactly the pairing Windows Update breaks. This single step resolves the majority of post-24H2 MediaTek failures. After installing, verify the driver version in Device Manager matches the package you installed — Windows Update sometimes "helpfully" replaces it within hours.

### Fix 4: Block Windows Update from replacing the driver

Once the working driver is in place, stop Windows Update from breaking it again. The practical options: use the **Show or hide updates** troubleshooter to hide the bad MediaTek driver update, or set your connection as metered to slow driver delivery. Verify over the next few days that the driver version in Device Manager stays put. This step feels paranoid until the third time Windows Update reinstalls the broken build overnight — MediaTek owners learn to pin their working driver.

### Fix 5: Disable power management on the adapter

Open the MediaTek adapter's **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power**. Then open the advanced power plan settings (**Settings > System > Power & battery > Power mode**, then the control panel power options) and set **Wireless Adapter Settings > Power Saving Mode** to **Maximum Performance** on both battery and plugged in. MediaTek cards are notorious for failing to reinitialize after sleep under 24H2's power policies — the "works after restart, dead after sleep" pattern is the signature. Test with an actual sleep/wake cycle, not just a restart.

### Fix 6: Tune the adapter's advanced settings

In the adapter's **Properties > Advanced** tab, check these MediaTek-specific settings: set **Preferred Band** to your router's best band (or leave auto), set **Roaming Aggressiveness** to a middle value (3) if you drop when moving around, and make sure **802.11a/b/g Wireless Mode** includes your network's band. If your card is an MT7922 (Wi-Fi 6E), verify the 6 GHz band is enabled if your router supports it. Click OK after changes and toggle Wi-Fi off and on. These settings do not fix Code 10 — that is strictly a driver problem — but they fix the drops and slowness that survive the driver repair.

### Fix 7: Update the BIOS and reseat the card

Check the manufacturer's site for a **BIOS update** — wireless initialization and ASPM fixes ship in firmware, and 24H2-era BIOS updates addressed MediaTek-specific issues. Flash with the charger connected. If problems persist across every driver version, and you are comfortable opening the laptop (and it is out of warranty), power off, disconnect the battery, and reseat the M.2 Wi-Fi card — remove the retaining screw, lift and reseat the card, and check both antenna wires (black and white/grey) are firmly snapped on. A card loosened by thermal cycling produces intermittent failures no driver can fix.

## Closing

MediaTek Wi-Fi failures after 24H2 are a driver-pairing problem first and a power-management problem second. Clean out the broken driver completely, install the vendor's validated package, pin it against Windows Update, and disable the power settings that kill the card on sleep. If the Device Manager error is specifically Code 10, our [Wi-Fi Code 10 repair guide](/articles/how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2/) walks through that error in depth.
