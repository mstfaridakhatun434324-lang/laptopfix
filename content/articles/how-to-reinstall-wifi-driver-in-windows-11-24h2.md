---
title: "How to Reinstall the Wi-Fi Driver in Windows 11 24H2"
slug: how-to-reinstall-wifi-driver-in-windows-11-24h2
date: 2026-09-16
categories: ["drivers"]
tags: ["reinstall wifi driver", "windows 11 24h2", "wifi driver fix", "network adapter", "intel wifi"]
description: "Need to reinstall your Wi-Fi driver on Windows 11 24H2? This guide covers the safe Device Manager method, clean reinstalls, and stopping bad driver updates."
thumbnail: "/images/thumbs/how-to-reinstall-wifi-driver-in-windows-11-24h2.webp"
faqs:
  - q: "Will reinstalling the Wi-Fi driver delete my saved networks?"
    a: "A plain Device Manager uninstall/reinstall keeps your saved Wi-Fi profiles and passwords. A full Network reset (Fix 5) does delete them, requiring you to re-enter passwords. If you want to preserve profiles through a clean reinstall, export them first with `netsh wlan export profile` in an elevated Command Prompt, then import afterward."
  - q: "How do I download a Wi-Fi driver if my Wi-Fi is completely dead?"
    a: "Three options: connect via Ethernet cable, USB-tether your phone (Android: Settings > Network > Hotspot > USB tethering; iPhone via cable with iTunes drivers), or download the driver on another computer and transfer it via USB stick. Download the driver before uninstalling the old one — a laptop with no network and no driver package is a frustrating place to be."
  - q: "Should I use the laptop maker's Wi-Fi driver or Intel's generic driver?"
    a: "Start with the laptop manufacturer's driver for your exact model — it is validated against your machine's antenna configuration and power behavior. If the maker has not released a 24H2-era update and problems persist, Intel's generic Wi-Fi driver (via the Intel Driver & Support Assistant) is the next best option and often newer. Avoid the bare driver Windows Update installs on its own."
  - q: "Why does Windows 11 24H2 keep breaking my Wi-Fi driver?"
    a: "24H2 made significant changes to the network stack and power management, and its driver packages for Intel AX201/AX211 and MediaTek cards have had buggy releases pushed through Windows Update. The pattern — working Wi-Fi, 24H2 update, broken Wi-Fi — is well documented. A clean manufacturer-driver install plus blocking driver updates via Windows Update is the durable fix until Microsoft stabilizes the update-channel drivers."
---

Reinstalling the Wi-Fi driver is the single most effective repair for wireless problems on Windows 11 24H2: connections that drop, speeds that collapsed after an update, Wi-Fi that vanished entirely, or adapters stuck with yellow warnings in Device Manager. The 24H2 update in particular has a track record of replacing working Wi-Fi drivers — especially Intel and MediaTek — with versions that misbehave.

The procedure is safe: Windows keeps a copy of a working driver, and even if it does not, you can download the fresh driver on another device or over Ethernet/USB tethering. The key is doing it cleanly — removing the old driver fully rather than installing over it — and then preventing Windows Update from immediately reinstalling the problematic version.

If Wi-Fi disappeared completely rather than misbehaving, start with our [missing Wi-Fi guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) to confirm the adapter is visible; for general driver hygiene, [updating drivers properly](/articles/how-to-update-drivers-on-windows-11-laptop/) is worth a read. Otherwise, work through the methods below from gentlest to most thorough.

## Why this happens

- **Corrupt driver files after 24H2 update** — The feature update can damage the driver store or install a mismatched Wi-Fi driver version.
- **Windows Update auto-installing a bad driver** — A newer-but-buggy driver delivered via Windows Update replaces your stable one silently.
- **Stale driver configuration / profiles** — Corrupt wireless profiles and power settings persist across simple updates.
- **Power management disabling the adapter** — 24H2's power policies can aggressively suspend the Wi-Fi radio.
- **Conflicting VPN or filter drivers** — VPN clients and third-party firewalls install filter drivers that break the Wi-Fi stack.
- **Failing adapter hardware** — Intermittent drops that survive every driver reinstall point at the card itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Quick reinstall via Device Manager

The standard method: remove the device, let Windows redetect it. Takes two minutes and fixes simple corruption.

1. Press Win + X > **Device Manager** > expand Network adapters.
2. Right-click your Wi-Fi adapter (Intel Wi-Fi 6 AX201/AX211, MediaTek, Realtek, or similar) > **Uninstall device**.
3. In the confirmation dialog, do NOT tick 'delete driver' for this first attempt.
4. Click Action > **Scan for hardware changes** — Windows reinstalls the adapter immediately.
5. Reconnect to your Wi-Fi network and test.

### Fix 2: Full clean reinstall with driver deletion

When the quick method fails, delete the driver package too, then install a fresh copy from the manufacturer. This is the definitive version.

A useful safety net before the full clean reinstall: create a System Restore point (search Start for 'Create a restore point') so you can roll back if anything goes sideways. Driver operations are normally safe, but having a restore point means a failed install can never leave you worse off than when you started.

1. Download the latest Wi-Fi driver for your exact laptop model from the manufacturer's support site first (use Ethernet or USB phone tethering if Wi-Fi is dead). Intel users can also use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. In Device Manager, right-click the Wi-Fi adapter > Uninstall device and TICK **'Attempt to remove the driver for this device'**.
3. Restart the PC. If Windows installs a generic driver, proceed anyway.
4. Run the manufacturer's driver installer you downloaded, restart again, and test.

### Fix 3: Roll back to the previous driver

If Wi-Fi broke immediately after a driver update, rolling back is faster than any reinstall.

1. In Device Manager, right-click the Wi-Fi adapter > **Properties** > Driver tab.
2. Click **Roll Back Driver** (if greyed out, no previous driver is stored — skip to Fix 4).
3. Choose a reason and confirm, then restart.
4. Test stability for a day before allowing any driver updates.

### Fix 4: Block Windows Update from replacing it

Essential on 24H2: otherwise Windows Update will eventually reinstall the bad driver and the problem returns.

1. After installing your good driver, open Settings > Windows Update > Advanced options.
2. Turn off **'Receive updates for other Microsoft products'** driver delivery where applicable, and check Optional updates for Wi-Fi drivers to decline them.
3. On Pro: gpedit.msc > Windows Update > Manage updates offered from Windows Update > enable **Do not include drivers with Windows Updates**.
4. Verify your driver version is unchanged after the next Patch Tuesday.

### Fix 5: Reset network settings after reinstall

A fresh driver with corrupt old profiles still misbehaves. Clear the slate.

1. Open Settings > Network & internet > Advanced network settings > **Network reset** > Reset now.
2. Restart when prompted.
3. Reconnect to Wi-Fi fresh (re-enter the password) and test speed and stability.
4. For enterprise networks, re-add any certificates or VPN profiles afterward.

### Fix 6: Disable power saving on the adapter

24H2 power policies can suspend the radio mid-session, mimicking driver failure.

1. In Device Manager > Wi-Fi adapter > Properties > Power Management, uncheck **'Allow the computer to turn off this device to save power'**.
2. On the Advanced tab, set Preferred Band, Roaming Aggressiveness, and Transmit Power to stable values (avoid 'Maximum power saving').
3. In Settings > Power & battery, use **Best performance** while testing.
4. Monitor for a full day of typical use.

### Fix 7: Test the adapter in a clean boot

If drops persist through every driver operation, third-party software is interfering.

1. Press Win + R > `msconfig` > Services tab > tick **Hide all Microsoft services** > Disable all.
2. In Task Manager > Startup, disable all startup apps. Restart.
3. If Wi-Fi is stable in the clean boot, re-enable services in halves to find the culprit — VPN clients and 'network optimizer' utilities are usual suspects.
4. Microsoft's [Windows networking support](https://support.microsoft.com/en-us/windows) documents clean-boot procedure in detail.

## Closing

Reinstalling the Wi-Fi driver on Windows 11 24H2 is straightforward, but the order matters: try the simple Device Manager reinstall first, escalate to a full clean reinstall with driver deletion, and always finish by blocking Windows Update from reinstalling the bad version. Skip that last step and you will be repeating this guide after the next update cycle.
