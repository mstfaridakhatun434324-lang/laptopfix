---
title: "MediaTek WiFi Not Working on HP Laptops — Driver Fixes That Work"
slug: how-to-fix-mediatek-wifi-not-working-on-hp-laptop
date: 2026-09-08
categories: ["drivers"]
tags: ["mediatek wifi", "hp laptop", "wifi not working", "mt7921", "hp drivers"]
description: "MediaTek WiFi not working on your HP laptop? Fix dead wireless and Code 10 errors with 7 HP-specific driver and power repairs."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-on-hp-laptop.webp"
faqs:
  - q: "Why does MediaTek WiFi fail so often on HP laptops?"
    a: "HP's Pavilion, Victus, and budget ProBook lines ship MediaTek MT7921/MT7922 cards widely, and the combination of HP's firmware, Windows Update's generic MediaTek driver, and the card's sleep-reinitialization bug produces dead adapters and Code 10 errors. HP validates specific driver builds per model — installing HP's package instead of Windows Update's is the fix that sticks."
  - q: "Where do I download the MediaTek driver for my HP laptop?"
    a: "From HP Support (support.hp.com) — enter your serial number or exact model, select your Windows version, and download the MediaTek/Realtek wireless driver package HP lists. HP's package is validated against your laptop's BIOS and card firmware. Don't use third-party updater tools or generic MediaTek downloads; version mismatch is what causes these failures."
  - q: "Does HP Support Assistant fix WiFi driver problems?"
    a: "Often, yes — HP Support Assistant automates detection and installs HP-validated driver updates including the wireless driver. It's the easiest correct path if you're unsure which package to pick. But when the card is in a Code 10 state, a manual uninstall with driver deletion followed by HP's standalone driver package is more reliable than the assistant's update-in-place."
  - q: "Can I replace the MediaTek card in my HP laptop with Intel?"
    a: "On many HP models the WiFi card is a standard M.2 2230 module and swappable — the Intel AX210 is the popular upgrade that ends MediaTek issues permanently. Check your model's service manual first: some thin HP laptops solder the card, and a few have BIOS whitelists. If it's soldered, the driver fixes below are your permanent path."
---

HP laptops — Pavilion, Victus, 15s, and Pavilion Gaming lines especially — are among the most common carriers of MediaTek wireless cards. The MT7921 and MT7922 show up everywhere in HP's mid-range, which means HP owners hit the full MediaTek catalog of failures: adapters dying after sleep, Code 10 in Device Manager, WiFi vanishing after Windows updates. The hardware is fine in most cases; the driver story is HP-specific, so the fixes are too.

This guide uses HP's channels — HP Support, HP Support Assistant, HP's validated driver builds — in the order that resolves these failures.

## Why this happens

- **Windows Update's generic MediaTek driver.** Replacing HP's validated build — the top cause on HP machines.
- **HP firmware + driver version mismatch.** The card's firmware expecting the HP-validated driver behavior.
- **Sleep/wake reinitialization failure.** The MediaTek card not coming back after HP's power management cycles it.
- **Fast Startup wedged state.** Hybrid boot preserving the card's failed state across restarts.
- **Code 10 from corrupt install.** Partial update mixing driver files.
- **Outdated HP BIOS.** Platform firmware predating the card's requirements.
- **Failing M.2 card.** Genuine hardware failure — last resort.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the adapter state and do a cold boot

Establish the failure mode before touching drivers.

1. Open **Device Manager > Network adapters** — find the **MediaTek Wi-Fi** entry (MT7921/MT7922).
2. Classify: **missing**, **yellow bang** (note the code — usually Code 10), or **present but no networks**.
3. Do a full cold boot: **Shift + Shut down**, unplug AC for 30 seconds, power on.
4. If the card returns after cold boot but dies after sleep, it's the power-management bug — note it and continue; Fix 4 addresses it.
5. Check **Settings > Network & internet** — no WiFi category means Windows sees no adapter.

### Fix 2: Use HP Support Assistant first

HP's own tool is the easiest correct driver path.

1. Open **HP Support Assistant** (preinstalled on most HP laptops; downloadable from HP if missing).
2. Go to **Updates** and install any **wireless/network** driver updates it offers.
3. Restart when prompted and test — including a sleep/wake cycle, since that's the MediaTek failure trigger.
4. If Support Assistant reports everything current but WiFi still fails, continue — the assistant updates in place, which sometimes isn't enough for a wedged driver.
5. HP's official driver portal is [HP Support](https://support.hp.com/us-en) for manual downloads.

### Fix 3: Clean-install HP's MediaTek driver package

The definitive fix — remove the bad driver completely, install HP's validated build.

1. On [HP Support](https://support.hp.com/us-en), enter your **serial number** (bottom sticker or `wmic bios get serialnumber`), select your OS, and download the **MediaTek/Realtek wireless LAN driver**.
2. **Device Manager** — right-click the MediaTek adapter > **Uninstall device**, checking **Delete the driver software for this device**.
3. Restart.
4. Install HP's downloaded package as administrator, restart again.
5. Verify **Properties > Driver** shows HP's version — provider and date matching the package.

### Fix 4: Tame the power settings that kill the card

The sleep-death workaround MediaTek cards need on HP machines.

1. **Device Manager > MediaTek adapter > Properties > Power Management** — uncheck **Allow the computer to turn off this device to save power**.
2. **Control Panel > Power Options > Change advanced power settings > Wireless Adapter Settings > Power Saving Mode** — **Maximum Performance** on battery and plugged in.
3. **Power Options > Choose what the power buttons do** — uncheck **Turn on fast startup**, then full shutdown.
4. In **HP BIOS** (F10 at boot), check **Advanced > Power Management** for wireless-related power options if present.
5. Test **three sleep/wake cycles** — MediaTek sleep failures are intermittent.

### Fix 5: Reset the network stack and profiles

For adapters that are present but won't connect.

1. **Command Prompt as administrator**: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /flushdns` — restart after.
2. **Settings > Network & internet > WiFi > Manage known networks** — **Forget** the problem network, reconnect fresh.
3. If still failing: **Settings > Network & internet > Advanced network settings > Network reset**.
4. Re-apply Fix 4's power settings after a network reset — defaults return.
5. Test close to the router to separate signal issues from driver issues.

### Fix 6: Update the HP BIOS

Firmware fixes for the card's platform initialization.

1. Check HP's support site for a **BIOS update** for your exact model.
2. Install on **AC power** with nothing else running — do not interrupt it.
3. Changelogs mentioning **WLAN, wireless, or MT7921** are directly relevant.
4. After the BIOS update, retest sleep/wake behavior specifically — and reinstall HP's wireless driver if the BIOS update reset anything.
5. Microsoft's update and firmware background: [Windows support](https://support.microsoft.com/en-us/windows).

When WiFi disappears from Windows entirely rather than just misbehaving: [WiFi disappeared on Windows 11 — no WiFi option](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 7: Code 10 deep drill, reseat, or replace

The last stops for stubborn Code 10 and dead adapters.

1. Confirm **Code 10** in **Properties > General** (not 43/45 — different fixes).
2. Full drill: uninstall with driver deletion, **Shift+Shutdown**, unplug AC, hold power 15 seconds, boot, install HP's driver while offline.
3. Boot a **Linux live USB** — working WiFi there proves the hardware and isolates it to Windows drivers.
4. Check your model's **service manual** — if the card is a removable **M.2 2230** module, reseat it (loose cards cause Code 10); an **Intel AX210** (~$20) is the popular permanent upgrade.
5. If soldered and Code 10 survives everything, a **USB WiFi adapter** is the pragmatic workaround — and HP's own Bluetooth stack is unaffected, so wireless peripherals keep working regardless (see [how to fix Bluetooth disappeared from Device Manager on HP laptop](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-on-hp-laptop/) if that side ever acts up).

## Closing

MediaTek WiFi on HP laptops is a solved problem with a specific recipe: HP's validated driver installed clean, Windows Update blocked from replacing it, the card's power management tamed, and the BIOS current. That combination ends the sleep-death and Code 10 cycle on the overwhelming majority of HP machines — the card hardware is innocent until the Linux test says otherwise.
