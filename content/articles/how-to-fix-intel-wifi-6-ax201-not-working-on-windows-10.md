---
title: "How to Fix Intel WiFi 6 AX201 Not Working on Windows 10"
slug: how-to-fix-intel-wifi-6-ax201-not-working-on-windows-10
date: 2026-09-29
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "windows 10", "wireless driver"]
description: "Intel WiFi 6 AX201 dead on Windows 10? Fix driver failures, code errors, and power issues with this step-by-step repair guide."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-on-windows-10.webp"
faqs:
  - q: "Why does the Intel AX201 show a yellow exclamation mark in Device Manager?"
    a: "A yellow triangle on the AX201 usually means the driver failed to start, most often with Code 10 or Code 43. This happens when Windows 10 installs an incompatible driver build, when the driver files are corrupted, or when power management puts the card in a state it cannot recover from. Reinstalling the correct driver version resolves it."
  - q: "Which driver version should I install for the AX201 on Windows 10?"
    a: "Use the newest driver Intel offers for Windows 10, or your laptop maker's customized package if they provide one. Avoid letting Windows Update choose: its catalog sometimes pairs the AX201 with a driver branch meant for Windows 11. Download from Intel's driver assistant page to get the matched Windows 10 build."
  - q: "Does the AX201 need a specific Windows 10 version to work?"
    a: "The AX201 needs Windows 10 version 1809 or later for basic function, and 2004 or later for reliable WiFi 6 operation. If you are on an older build, update Windows first — no driver can compensate for missing OS-level WiFi 6 support in very old Windows 10 releases."
  - q: "Can I replace the AX201 with a newer WiFi card myself?"
    a: "On most laptops yes, if the card is a standard M.2 2230 module and not soldered. Check your service manual first — some machines whitelist cards in BIOS or solder the module down. An AX210 is the common upgrade, adding WiFi 6E, but confirm compatibility before buying."
---

The Intel WiFi 6 AX201 is one of the most widely shipped wireless cards in Windows 10 laptops, and it is also one of the most complained about — usually showing up in Device Manager with a yellow warning, throwing Code 10 errors, or simply refusing to see any networks. The good news: the AX201 is rarely actually dead. Its failures are overwhelmingly driver and power-management problems that respond to a careful driver rebuild.

What makes the AX201 tricky is that it is a CNVio2 card, meaning part of its logic lives in the Intel chipset rather than on the card itself. That tight coupling makes it sensitive to chipset driver versions and BIOS behavior in ways older cards were not. Keep that in mind as you work through the fixes — chipset and BIOS matter here more than usual.
One quirk worth understanding up front: the AX201 is a CNVio2 card, which means part of its wireless logic lives in the Intel chipset rather than on the card itself. That tight coupling is why AX201 failures so often survive a WiFi driver reinstall — the chipset driver and BIOS are part of the card's foundation. The steps below address all three layers, which is what separates a lasting fix from a temporary one.

## Why this happens

- **Incompatible driver from Windows Update:** Windows 10 sometimes installs a driver branch built for Windows 11, which fails to start the AX201 with Code 10.
- **Corrupted driver installation:** Interrupted updates leave half-written driver files that enumerate the card but cannot initialize it.
- **Power management killing the card:** The "turn off this device to save power" setting traps the CNVio2 interface in a dead state after sleep.
- **Outdated chipset drivers:** Because the AX201 depends on chipset logic, stale Intel chipset drivers break the card even when the WiFi driver itself is fine.
- **BIOS with broken CNVio support:** Some BIOS versions mishandle the CNVio2 interface after sleep or hibernate, requiring a BIOS update.
- **Router-side incompatibilities:** Certain WiFi 6 router settings (802.11ax mode, WPA3-only, 160 MHz channels) can make the AX201 fail to connect even when the driver is healthy.
- **Antenna wire issues:** After repairs, swapped or loose antenna leads cause the card to appear working but never find networks.
- **Actual card failure:** Rare for the AX201, but possible — usually preceded by months of intermittent disconnects.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the exact error code

1. Open **Device Manager → Network adapters**, right-click the AX201 → **Properties → General**, and note the **Device status** message and code.
2. Code 10 means the driver cannot start; Code 43 means Windows stopped the device after errors; Code 31 means the driver failed to load.
3. Also check **Events** tab for the timestamp of the failure — if it matches a Windows update, you have your culprit.
4. Write the code down; you will use it to confirm the fix worked after each step.

### Fix 2: Clean-install the correct Intel driver

1. Download the latest Windows 10 WiFi driver for the AX201 from the [Intel driver detection page](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop maker's support site.
2. In Device Manager, right-click the AX201 → **Uninstall device**, ticking **Attempt to remove the driver for this device**.
3. Restart the laptop — do not let Windows Update install a driver first; disconnect from the internet briefly if needed.
4. Run the Intel installer, restart again, and confirm the yellow warning is gone. This mirrors the clean-driver approach for [vanished WiFi adapters](/articles/how-to-fix-wifi-adapter-not-showing-up-on-lenovo-laptop/).

### Fix 3: Update the Intel chipset driver

1. From the same Intel support page, download the **Intel Chipset Device Software** (INF) for your platform.
2. Install it and restart — this refreshes the CNVio2 interface logic the AX201 depends on.
3. Recheck Device Manager. On many machines this single step clears persistent Code 10 errors that survived WiFi driver reinstalls.
4. If your laptop maker offers a chipset package, prefer theirs; it is validated against your BIOS.

### Fix 4: Disable power management on the AX201

1. In Device Manager, right-click the AX201 → **Properties → Power Management**.
2. Uncheck **Allow the computer to turn off this device to save power**.
3. In **Power Options → Advanced**, set **Wireless Adapter Settings → Power Saving Mode** to **Maximum Performance** on both battery and plugged-in.
4. Test sleep-wake cycles: close the lid, reopen, and confirm WiFi reconnects without the adapter erroring.
5. If drops persist specifically on WiFi 6 networks, compare notes with our [WiFi 6 laptop troubleshooting guide](/articles/how-to-fix-wifi-6-not-working-on-laptop-on-windows-10/) — some AX201 issues are really router-side WiFi 6 incompatibilities wearing a driver disguise.

### Fix 5: Reset the AX201's advanced settings

1. In the AX201's **Properties → Advanced** tab, note any non-default settings.
2. Set **802.11a/b/g Wireless Mode** to a dual-band default, **Preferred Band** to **No Preference**, and **Transmit Power** to **Highest**.
3. Disable **802.11ax** temporarily as a test — if connections stabilize, your router's WiFi 6 implementation is the problem, not the card.
4. Re-enable ax afterward if your router handles it, or leave it off for stability.

### Fix 6: Check BIOS and router compatibility

1. Update the BIOS from your laptop maker's support site if the changelog mentions wireless, CNVio, or connectivity fixes.
2. On your router, try WPA2 instead of WPA3, disable 160 MHz channel width, and ensure 802.11ax mode is actually supported by your router's firmware.
3. Test against a phone hotspot — if the AX201 works on the hotspot but not your router, the router configuration is at fault.
4. Update the router firmware regardless; AX201 quirks with specific router chipsets are well documented.
5. As a final router-side test, create a separate 2.4 GHz-only SSID and connect the AX201 to it for a day. Rock-solid stability on 2.4 GHz with failures on 5 GHz points squarely at band-specific incompatibilities rather than the card.

### Fix 7: Reseat or replace the card

1. If nothing software-side works, power off, open the back panel, and reseat the M.2 AX201 card, confirming both antenna wires are firmly attached.
2. If reseating fails and the card shows Code 10 on a fresh Windows install too, the card is likely dead — replace with an identical AX201 or a compatible AX210.
3. Install the Intel driver after the swap and verify in Device Manager.
4. Persistent failure across two cards points to the motherboard CNVio interface — a service center job.

## Closing

The AX201 on Windows 10 is a driver-sensitive card, not a fragile one. A clean install of the correct Intel driver, current chipset software, disabled power management, and a BIOS check resolve the vast majority of Code 10 and no-network cases. Keep the working driver version noted somewhere — when Windows Update next offers a wireless driver, you will know exactly which build to keep.
