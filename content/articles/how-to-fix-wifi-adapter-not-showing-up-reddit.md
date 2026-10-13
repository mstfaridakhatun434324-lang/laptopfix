---
title: "WiFi Adapter Completely Missing? How to Fix It When It Doesn't Show Up"
slug: how-to-fix-wifi-adapter-not-showing-up-reddit
date: 2026-09-21
categories: ["drivers"]
tags: ["wifi adapter missing", "no wifi adapter", "network adapter not found", "wireless adapter gone", "device manager wifi"]
description: "Your WiFi adapter has vanished from Device Manager and the taskbar. This guide walks through the fixes that actually bring it back, from hidden devices to BIOS checks."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-reddit.webp"
faqs:
  - q: "Why is my WiFi adapter not showing in Device Manager at all?"
    a: "The most common reasons are that Windows hid it as a ghosted device, the BIOS disabled the wireless card, or the driver is corrupted after an update. Open Device Manager, click View, and enable Show hidden devices first. If it still doesn't appear, check the BIOS to confirm the wireless LAN is enabled, since some firmware toggles can switch it off silently."
  - q: "Can a Windows update make my WiFi adapter disappear?"
    a: "Yes, and it happens more often than you'd think. Feature updates sometimes install a generic driver that the adapter doesn't understand, or the update resets power management settings that keep the card asleep. Rolling the driver back or reinstalling the manufacturer's driver package usually restores it. Check the update history to see if the disappearance lines up with a recent install."
  - q: "What should I do if the WiFi adapter shows a yellow exclamation mark instead?"
    a: "That usually means the hardware is detected but the driver failed to load. Note the error code in the device properties — Code 10 and Code 43 are the usual suspects. Uninstall the device, tick the option to delete the driver software, and reinstall a fresh driver from your laptop maker's support site rather than letting Windows pick one automatically."
  - q: "How do I know if the WiFi card itself has failed?"
    a: "If the adapter doesn't appear in Device Manager even with hidden devices shown, doesn't show in the BIOS hardware list, and isn't visible from a Linux live USB, the card is likely dead or unseated. Most laptops use an M.2 WiFi module that's user-replaceable. Reseat it first, since a card that shifted in its socket during a drop behaves exactly like a dead one."
---

Few things are more unsettling than opening your laptop and finding no WiFi icon, no network list, and no wireless adapter anywhere in Device Manager. You didn't change anything — it was working yesterday. This is one of those problems that looks catastrophic but is usually a driver or firmware hiccup, and it shows up in support forums so often that whole troubleshooting threads have become folk knowledge.

The good news: when the adapter vanishes entirely, the cause is almost always logical rather than physical. Windows either can't see the hardware (BIOS or hardware switch), can see it but won't load the driver (corruption or bad update), or is hiding it from you (ghosted hidden device). The fixes below go from least invasive to most involved, and one of them resolves the majority of cases.

Before you start, grab another device with internet access if you can. You may need to download a driver from your laptop manufacturer's support site, and doing that on the affected machine is obviously impossible without a wired Ethernet connection or USB tethering from your phone.

## Why this happens

- **The adapter is a hidden ghost device.** When Windows fails to enumerate a device cleanly, it can leave it in a ghosted state that's invisible unless you enable "Show hidden devices."
- **A Windows update broke the driver.** Feature and cumulative updates occasionally replace a working vendor driver with an incompatible generic one, or fail mid-install and leave no working driver at all.
- **The BIOS or UEFI disabled the wireless card.** Some firmware has a wireless LAN toggle, and it can get flipped by a BIOS update, a reset to defaults, or an accidental keypress.
- **A physical wireless switch or function key** turned the radio off. Business laptops from HP, Lenovo, and Dell still ship these, and airplane-mode key combos (Fn+F-something) do the same.
- **Power management shut the card down.** Aggressive power saving can put the adapter to sleep so deeply that Windows stops listing it until a full power cycle.
- **The driver stack is corrupted.** Registry entries under the network class can go bad, especially after failed driver installs or interrupted updates.
- **The M.2 WiFi module is loose or dead.** Drops, heat cycles, and age can unseat the card in its slot or kill it outright — rare, but real.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reveal hidden devices in Device Manager

The fastest check takes thirty seconds and catches a surprising number of cases.

1. Press **Win + X** and open **Device Manager**.
2. Click the **View** menu and select **Show hidden devices**.
3. Expand **Network adapters** and look for your wireless adapter (Intel, Realtek, MediaTek, Qualcomm, or Broadcom). It may appear grayed out.
4. If you see it grayed out, right-click it and choose **Uninstall device**. If offered, tick **Attempt to remove the driver for this device**.
5. Restart the laptop. Windows re-detects the hardware and reinstalls the driver.

If you want the full background on adapter quirks after updates, see [how WiFi adapters can vanish after a Windows 11 update](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).

### Fix 2: Check the physical wireless switch and airplane mode

Don't skip this — it's embarrassing how often it's the answer.

1. Look along the sides and front edge of your laptop for a small slider or button with a wireless/antenna icon. Slide or press it to the ON position.
2. Press **Win + A** to open Quick Settings and make sure **Airplane mode** is off.
3. Try the function-key combo for your brand (commonly **Fn+F2**, **Fn+F3**, or **Fn+F12** — look for the antenna icon on the key).
4. On Lenovo ThinkPads, also check the BIOS-level wireless toggle under the Security tab if a key combo doesn't help.

### Fix 3: Run the network troubleshooter

Windows has a built-in diagnostic that occasionally nails this.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Run the **Network and Internet** troubleshooter.
3. Let it complete — it can reset the network stack and re-enable disabled adapters.
4. Restart even if it claims nothing was wrong; the reset it performs silently sometimes finishes the job.

### Fix 4: Reset the network stack with commands

If the adapter shows up but won't work, or appears intermittently, a stack reset clears corrupted configuration.

1. Open an elevated terminal: right-click **Start**, choose **Terminal (Admin)**.
2. Run these commands one at a time, pressing Enter after each:
   `netsh winsock reset`
   `netsh int ip reset`
   `ipconfig /release`
   `ipconfig /renew`
   `ipconfig /flushdns`
3. Restart the laptop and check whether the adapter returns.

### Fix 5: Reinstall the driver from your laptop manufacturer's site

This is the heavy hitter. Generic Windows drivers cause more missing-adapter cases than anything else.

1. On another device, go to your laptop maker's support page (Dell, HP, Lenovo, or Acer) and download the wireless driver for your exact model.
2. Copy it to the laptop via USB drive, or USB-tether your phone for temporary internet.
3. In Device Manager, uninstall the wireless adapter with driver deletion as in Fix 1.
4. Run the manufacturer's installer. Avoid "driver updater" utilities — they cause as many problems as they solve.
5. Restart and confirm the adapter appears and connects.

For Intel-based cards, Intel's own [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can identify the right driver if your manufacturer's site is hard to navigate.

### Fix 6: Check the BIOS for a disabled wireless LAN

Firmware-level disables survive driver reinstalls, so this is the fix when nothing else works.

1. Restart and enter the BIOS/UEFI (usually **F2**, **Del**, or **F10** during boot — watch the splash screen).
2. Look under **Advanced**, **Devices**, or **Security** for **Wireless LAN**, **WLAN**, or **WiFi**.
3. Make sure it's **Enabled**. While you're there, confirm the setting wasn't flipped by a recent BIOS update.
4. Save and exit. The adapter should enumerate on the next boot.

### Fix 7: Disable power management on the adapter

Some laptops aggressively power-gate the WiFi card, and it doesn't always wake up.

1. In Device Manager, right-click the wireless adapter and choose **Properties**.
2. Open the **Power Management** tab and uncheck **Allow the computer to turn off this device to save power**.
3. In **Settings > System > Power & battery**, switch the power mode away from maximum battery saver while testing.
4. Restart and watch whether the adapter stays visible across sleep/wake cycles.

### Fix 8: Reseat or replace the WiFi module

When software fixes all fail, look at the hardware.

1. Power off, unplug, and remove the bottom panel (check your model's service manual first — some require removing the battery).
2. Find the small M.2 card with two antenna wires (usually black and white). Gently disconnect the antennas, unscrew the card, and reseat it firmly.
3. Reconnect the antennas — they snap on with light pressure — and reassemble.
4. If the card is still invisible after reseating, replace it. Intel AX200/AX210 cards are inexpensive drop-in upgrades for most laptops, and swapping one is a ten-minute job.

## Closing

A missing WiFi adapter feels like a hardware failure, but nine times out of ten it's Windows hiding the device, a bad driver from an update, or a firmware toggle you never touched. The hidden-devices check and a clean manufacturer driver install resolve the bulk of cases, and the BIOS check catches the stubborn remainder. If you've reconnected to your network but it keeps dropping the 5 GHz band specifically, our guide on [5 GHz connection problems](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-on-windows-11/) picks up from there. And if the module itself has failed, a replacement card is one of the cheapest laptop repairs you'll ever do.
