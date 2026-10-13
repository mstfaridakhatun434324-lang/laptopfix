---
title: "MediaTek Wi-Fi Driver Problems: Full Repair Walkthrough"
slug: how-do-i-fix-mediatek-wifi-not-working
date: 2026-09-10
categories: ["drivers"]
tags: ["mediatek wifi fix", "mt7921 driver", "wifi repair", "windows 11"]
description: "Fix MediaTek Wi-Fi on your laptop with this full walkthrough: clean driver reinstall, power settings, band tuning, and hardware checks."
thumbnail: "/images/thumbs/how-do-i-fix-mediatek-wifi-not-working.webp"
faqs:
  - q: "Which MediaTek driver version should I install?"
    a: "Use the driver package from your laptop manufacturer's support page for your exact model — it's tested against your card's firmware and power profile. Only if the maker's package is years old and broken should you try MediaTek's reference driver or a newer version from another laptop maker's site for the same card. Newer isn't automatically better with MediaTek; matched is better."
  - q: "Why does my MediaTek Wi-Fi only break on battery power?"
    a: "That's the classic power-management signature. On battery, Windows aggressively powers down the Wi-Fi card, and the MediaTek firmware often fails to wake cleanly, causing drops or a dead adapter. Disable power saving on the adapter in Device Manager and set wireless performance to Maximum in Power Options for both battery and plugged-in states."
  - q: "How do I stop Windows Update from breaking my MediaTek driver?"
    a: "After installing a working driver, block driver updates from Windows Update via Group Policy (Pro) or the 'show or hide updates' troubleshooter to hide the specific Wi-Fi driver update. This is the number one recurrence-prevention step for MediaTek cards, since Windows loves replacing the working driver with a broken generic one."
  - q: "My MT7921 shows no networks at all — is it dead?"
    a: "Not necessarily. 'No networks found' with the adapter present usually means the radio is off (airplane mode, Fn key, or BIOS), the driver failed to initialize the radio, or the antenna leads are disconnected. Check the physical radio switches first, then Device Manager for error codes, before concluding the card is dead."
---

The MediaTek MT7921 and MT7922 cards in many AMD laptops can be genuinely troublesome — but most of the trouble is fixable software. Dropped connections, dead adapters after sleep, and "no networks found" errors follow a familiar pattern, and this walkthrough repairs them in the order that works: proper driver, power management, radio tuning, then hardware. For the diagnostic-first approach, see [MediaTek Wi-Fi troubleshooting](/articles/troubleshoot-mediatek-wifi-not-working/).

Before starting, note your exact card model in Device Manager (MT7921, MT7921K, MT7922, or similar) and your current driver version. You'll need both to get the right package, and the version number tells you whether you're running one of the notoriously bad early drivers.

## Why this happens

- **Buggy early driver versions:** The first MT7921 drivers had real stability defects; old installs still suffer.
- **Windows Update driver replacement:** A generic driver overwrites the tuned package and breaks radio behavior.
- **Power management wake failures:** The card sleeps on battery and its firmware can't wake properly.
- **Radio disabled at some layer:** Airplane mode, Fn key, Windows toggle, or BIOS setting has the radio off.
- **Antenna lead problems:** Loose or swapped antenna connections cause weak signal mistaken for driver faults.
- **Band steering confusion:** The card sticks to a congested 2.4GHz network instead of roaming to 5GHz.
- **Router feature incompatibility:** WPA3-only, OFDMA, or aggressive 802.11ax settings confuse older firmware.
- **Corrupted driver installation:** Partial installs from interrupted updates leave the card half-initialized.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check every radio switch and toggle

Start with the embarrassingly simple: is airplane mode off (check the Quick Settings panel and the physical switch if your laptop has one)? Press the Wi-Fi Fn key combination — on many laptops Fn + F-something toggles the radio with no on-screen indication. In Settings, Network & internet, confirm Wi-Fi is on. Then check BIOS setup for a wireless toggle. A surprising number of "dead Wi-Fi" cases end right here, so don't skip it out of pride.

1. Turn off airplane mode in Quick Settings.
2. Press the laptop's Wi-Fi Fn key combination.
3. Confirm Wi-Fi is enabled in Settings, Network & internet.
4. Check for a wireless toggle in BIOS setup.
5. Look for a physical wireless switch on the chassis.

### Fix 2: Clean-reinstall the manufacturer's MediaTek driver

Download the Wi-Fi driver package for your exact model from the maker — [Lenovo's support site](https://support.lenovo.com/us/en/) or [Dell's support portal](https://www.dell.com/support). In Device Manager, uninstall the MediaTek adapter with "Attempt to remove the driver for this device" ticked. Reboot, install the downloaded package, reboot again. Do this on AC power with a stable connection (use Ethernet or USB tethering if Wi-Fi is your only link — download first, obviously).

1. Download the maker's Wi-Fi driver for your exact model.
2. Uninstall the MediaTek adapter with driver software removed.
3. Restart the laptop.
4. Install the downloaded driver package.
5. Restart and verify stable connection.

### Fix 3: Tame power management completely

Open the adapter's Properties in Device Manager: on the Power Management tab, uncheck "Allow the computer to turn off this device to save power." On the Advanced tab, set any power-saving or power-management mode to Maximum Performance. Then open Power Options, find Wireless Adapter Settings, and set both On battery and Plugged in to Maximum Performance. This triple lock eliminates the sleep/wake failures that plague MediaTek cards. Test across several sleep cycles before moving on.

1. Uncheck power-saving on the adapter's Power Management tab.
2. Set Advanced power mode to Maximum Performance.
3. Set Wireless Adapter Settings to Maximum in Power Options.
4. Apply to both battery and plugged-in profiles.
5. Test across multiple sleep/wake cycles.

### Fix 4: Lock the card to the 5GHz band

In the adapter's Advanced tab, set "Preferred Band" to 5G or 5GHz. The 2.4GHz band is crowded — neighbors' routers, microwaves, Bluetooth — and MediaTek cards are particularly bad at thriving in it. While there, set "Wireless Mode" to prefer 802.11ax/ac if your router supports it. On the router side, give the 5GHz network a distinct SSID if it shares one with 2.4GHz, so the card can't accidentally camp on the slow band. If 5GHz range is the issue, a [5GHz connection check](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) helps verify the basics, and Microsoft's support pages document how to reach the adapter properties.

1. Set Preferred Band to 5GHz in the Advanced tab.
2. Prefer 802.11ax/ac wireless modes if available.
3. Give the router's 5GHz band a distinct SSID.
4. Forget the 2.4GHz network on the laptop to avoid fallback.
5. Test speed and stability on 5GHz.

### Fix 5: Block Windows from replacing the driver

Once you have a working driver, protect it. On Windows 11 Pro, use `gpedit.msc`: Computer Configuration, Administrative Templates, Windows Components, Windows Update, Manage updates offered from Windows Update — enable "Do not include drivers with Windows Updates." On Home, use the "Show or hide updates" troubleshooter to hide the MediaTek driver update specifically. Verify after the next Patch Tuesday that your driver version survived. This single step prevents most MediaTek relapses.

1. Open `gpedit.msc` (Pro) and enable the no-drivers-with-updates policy.
2. On Home, hide the specific driver update with the troubleshooter.
3. Record your working driver version number.
4. Verify the version after the next Windows Update.
5. Reinstall manually if Windows ever replaces it.

### Fix 6: Update the card's firmware and check coexistence

Some maker driver packages include a separate firmware updater for the MT7921/MT7922 — run it if present. For the combo card's Bluetooth side, update the Bluetooth driver from the same package; mismatched Wi-Fi/Bluetooth versions cause the coexistence arbitration bugs that drop Wi-Fi when Bluetooth is active. Test with Bluetooth disabled for a day as a diagnostic. If your Bluetooth has vanished entirely, see [Bluetooth missing from Device Manager](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/).

1. Run any firmware updater included in the driver package.
2. Update the Bluetooth driver from the same package.
3. Test Wi-Fi stability with Bluetooth disabled for a day.
4. Toggle Bluetooth Collaboration in the Advanced tab.
5. Keep Wi-Fi and Bluetooth drivers version-matched.

### Fix 7: Inspect antennas and consider replacement

If signal is weak everywhere (one bar next to the router), power off, open the chassis per the service manual, and check the antenna leads on the M.2 card — black to MAIN, white to AUX, both snapped firmly. Reseat the card itself. If everything software fails and the card drops constantly, replace it with an Intel AX210 (check BIOS whitelisting first). The swap takes ten minutes and ends the MediaTek saga permanently for most people.

1. Open the chassis per the service manual.
2. Verify antenna leads: black to MAIN, white to AUX.
3. Reseat the M.2 card firmly.
4. Consider an Intel AX210 replacement if software fails.
5. Check BIOS whitelisting before buying the replacement.

## Closing

MediaTek Wi-Fi is fixable far more often than its reputation suggests: the right maker driver, aggressive power-management lockdown, and protection from Windows Update resolve the large majority of cases. Work the list in order, give each change a day of testing, and keep the working driver installer somewhere safe. And if the card truly won't behave, the Intel swap is a well-traveled road with a happy ending.
