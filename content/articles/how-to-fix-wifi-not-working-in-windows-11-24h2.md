---
title: "Wi-Fi Not Working After Windows 11 24H2? Fix It"
slug: how-to-fix-wifi-not-working-in-windows-11-24h2
date: 2026-10-11
categories: ["drivers"]
tags: ["windows 11 24h2 wifi", "24h2 wifi not working", "wifi broken after update", "24h2 network fix"]
description: "Wi-Fi broke after the Windows 11 24H2 update? Fix driver incompatibilities, reset the network stack, and roll back what 24H2 changed."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why does 24H2 break Wi-Fi on some laptops?"
    a: "The 24H2 update refreshes core networking components and often replaces wireless drivers with versions that have not been validated against the new build. Intel, Realtek, and Mediatek cards have all had 24H2-specific driver issues. Installing the driver version the card maker released for 24H2, rather than the one Windows installed, is the reliable fix."
  - q: "Should I roll back the 24H2 update to fix Wi-Fi?"
    a: "Rolling back is a valid short-term test but a poor long-term strategy, since 24H2 will be re-offered. Better to fix the driver properly: install the 24H2-compatible wireless driver from the card or laptop maker, which keeps you on the supported build with working Wi-Fi."
  - q: "How do I stop Windows Update from breaking my Wi-Fi driver again?"
    a: "After installing a working driver, you can pause updates briefly, or use the 'show or hide updates' troubleshooter to block the specific driver update. The cleaner long-term approach is keeping the manufacturer's driver current, since newer validated drivers eventually flow through Windows Update anyway."
  - q: "Does the 24H2 network reset delete anything important?"
    a: "It removes all network adapters and returns networking settings to defaults, which forgets saved Wi-Fi passwords and VPN configurations. It does not touch personal files, apps, or documents. Export VPN settings and note Wi-Fi passwords before running it, since every network must be set up again afterward."
---

The Windows 11 24H2 feature update has a track record with Wi-Fi: across Intel, Realtek, and Mediatek wireless cards, users report Wi-Fi dying, slowing to a crawl, or vanishing entirely right after the update completes. If your wireless worked on 23H2 and broke on 24H2, the update is the cause until proven otherwise.

24H2 changes both the networking stack and which drivers Windows considers acceptable, so the failure modes cluster around driver incompatibility and corrupted network configuration. The fixes below are 24H2-specific: the right driver versions, the stack resets that match what 24H2 changes, and the rollback options when nothing else works.

## Why this happens

- **24H2 replaced the wireless driver** with a version not validated for the new build.
- **Network profile and stack corruption** during the feature update migration.
- **Old VPN or filter drivers** incompatible with 24H2's networking changes.
- **Wi-Fi Sense / randomized MAC settings** conflicting with router security after the update.
- **Power management defaults reset** by the update, letting Windows park the adapter.
- **Router-side incompatibility** — 24H2's stricter protocol handling versus old router firmware.
- **Failed update leaving hybrid state** — part 23H2 networking, part 24H2, fully broken.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the 24H2-compatible wireless driver

Go to the card maker's site — Intel, Realtek, or Mediatek — and download the driver version explicitly supporting 24H2, or get it from the laptop maker's support page. Uninstall the current driver in Device Manager first, deleting the driver software, so the 24H2-incompatible version cannot linger. Intel users should run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) afterward to stay current.

1. Identify your wireless card in Device Manager.
2. Download the 24H2-era driver from the card or laptop maker.
3. Uninstall the current driver, deleting the driver software.
4. Install the fresh driver and reboot.

### Fix 2: Reset the network stack for 24H2

Feature updates migrate network configuration, and the migration sometimes corrupts it. Reset everything: the built-in Network reset plus the terminal commands for Winsock and TCP/IP. This clears whatever 24H2's migration left behind. Microsoft's reset guidance is in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Run Settings > Network & internet > Advanced network settings > Network reset.
2. In an elevated terminal, run `netsh winsock reset` and `netsh int ip reset`.
3. Run `ipconfig /flushdns` and restart.
4. Reconnect to Wi-Fi and test speed and stability.

### Fix 3: Remove incompatible VPN and filter drivers

VPN clients install network filter drivers, and old versions break under 24H2 — sometimes taking all Wi-Fi down. Uninstall VPN clients and third-party firewalls temporarily. If Wi-Fi returns, reinstall the latest versions, which are 24H2-compatible. Check Device Manager > Network adapters for greyed-out WAN Miniport entries as evidence.

1. Uninstall VPN clients and third-party firewalls.
2. In Device Manager, remove greyed-out WAN Miniport adapters.
3. Restart and test Wi-Fi without the VPN.
4. Reinstall only the latest VPN version if needed.

### Fix 4: Fix power management and MAC randomization

24H2 resets power defaults, so re-disable 'allow the computer to turn off this device' on the wireless adapter in Device Manager. Separately, toggle the random MAC address setting for your network: Settings > Wi-Fi > your network > set Random hardware addresses to Off. Some routers with MAC filtering or old firmware drop 24H2 clients that randomize.

1. Disable adapter power-off in Device Manager > adapter Properties.
2. Set the wireless adapter to Maximum Performance in Power Options.
3. Turn off random hardware addresses for your home network.
4. Forget and rejoin the network, then test.

### Fix 5: Update router firmware and check bands

24H2 tightened some protocol handling, exposing old router firmware bugs. Log into the router and install its latest firmware. While there, check whether the laptop connects on 2.4GHz but not 5GHz (or vice versa) — band-specific failure after 24H2 usually means the driver, but confirming the pattern helps. The [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) digs into band-specific faults.

1. Log into the router admin page and update its firmware.
2. Test both 2.4GHz and 5GHz bands separately.
3. Note which band fails — it narrows the driver diagnosis.
4. Reboot the router after the firmware update.

### Fix 6: Roll back the driver or the update

If Wi-Fi worked an hour ago on 23H2, rolling back is legitimate triage. First try Device Manager > driver Roll Back on the wireless adapter. If the whole update is suspect, Settings > System > Recovery offers 'Go back' within ten days of installing 24H2. Use the time bought to find a proper driver fix rather than staying on the old build forever.

1. Try Roll Back Driver on the wireless adapter first.
2. If that fails, use Settings > System > Recovery > Go back.
3. Confirm Wi-Fi works on the previous build.
4. Plan the driver fix before 24H2 is re-offered.

### Fix 7: Repair-install Windows 11

For the failed-migration cases — where 24H2 left networking half-upgraded — an in-place repair install fixes it without losing files or apps. Download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run setup, and choose to keep everything. This reinstalls 24H2's networking components cleanly.

1. Download the Windows 11 ISO from Microsoft.
2. Mount it and run setup.exe.
3. Choose 'Keep personal files and apps'.
4. After setup completes, reinstall the wireless driver and test.

### Fix 8: Report the bug and bridge with USB Wi-Fi

If nothing has worked, file feedback through the Feedback Hub (Win + F) under Network and Internet > Wi-Fi — Microsoft triages 24H2 wireless regressions from these reports, and card makers monitor them too. Include your card model and driver version. Meanwhile, a USB Wi-Fi adapter gets you back online for little money and proves the rest of the system is healthy. Keep hunting the proper 24H2-compatible driver in parallel; the USB adapter is a bridge, not the destination.

1. File detailed feedback in the Feedback Hub.
2. Note your wireless card model and driver version in the report.
3. Use a USB Wi-Fi adapter to stay online meanwhile.
4. Install the proper driver once the maker releases it.

## Closing

24H2 Wi-Fi failures are update-migration problems wearing a driver costume: the right driver version plus a full network reset fixes nearly all of them. Resist the urge to live on the rolled-back build — the driver makers have shipped 24H2-compatible versions, and installing them keeps you supported and connected. If one specific card model keeps breaking, the manufacturer's driver page is the place to watch, not Windows Update. For Wi-Fi 6-specific breakage on this build, see [fixing Wi-Fi 6 on 24H2](/articles/how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2/).
