---
title: "How to Reinstall Your Wi-Fi Driver the Right Way"
slug: best-way-to-reinstall-wifi-driver
date: 2026-09-20
categories: ["drivers"]
tags: ["wifi driver", "reinstall driver", "wireless", "network adapter"]
description: "Wi-Fi broken after an update or acting flaky? Reinstall the wireless driver properly — the right source, the right order, no Windows Update sabotage."
thumbnail: "/images/thumbs/best-way-to-reinstall-wifi-driver.webp"
faqs:
  - q: "How do I reinstall my Wi-Fi driver in Windows 11?"
    a: "Open Device Manager, expand Network adapters, right-click your Wi-Fi adapter, choose Uninstall device (checking delete driver software if offered), then restart. Windows will reinstall a driver automatically. For the best result, download the driver from your laptop manufacturer's support page or Intel's site first, so you can install the correct version manually instead of accepting whatever Windows finds."
  - q: "Will reinstalling the Wi-Fi driver delete my saved networks?"
    a: "No. Reinstalling the driver doesn't touch your saved Wi-Fi profiles or passwords — those live in Windows' network configuration, not the driver package. Your networks will still be listed after the reinstall. (A full Network reset is different — that does wipe saved networks, so don't confuse the two.)"
  - q: "Should I get the Wi-Fi driver from Windows Update or the manufacturer?"
    a: "The manufacturer (or Intel, for Intel cards) almost always. Windows Update's wireless drivers lag behind and are a frequent source of the very problems you're trying to fix. Download the driver on another device if your Wi-Fi is completely dead, transfer it via USB, and install it with the network disconnected so Windows Update can't substitute its version mid-install."
  - q: "My Wi-Fi adapter is missing from Device Manager entirely. What now?"
    a: "First check View > Show hidden devices — a greyed-out adapter can be re-enabled. If it's truly absent, the driver stack is badly broken or the card is disabled in BIOS/airplane mode. Reinstall the chipset driver first (the Wi-Fi card hangs off the chipset bus), then the Wi-Fi driver. If the adapter never appears, check BIOS for a wireless enable option and consider hardware failure."
---

Reinstalling a Wi-Fi driver sounds simple — uninstall, restart, done — but the details determine whether it actually fixes anything. Windows' automatic reinstall often just puts back the same problematic driver version, and Windows Update loves to "help" by substituting its own version mid-process. Doing it the right way means controlling the driver source, the install order, and keeping Windows Update out of the way until you're done.

This guide covers the full proper procedure: preparation (getting the right driver while you still can), clean removal, manual installation, and lockdown. If your Wi-Fi option vanished entirely rather than just misbehaving, start with [Wi-Fi disappeared in Windows 11](/articles/wifi-disappeared-windows-11-no-wifi-option/); if airplane mode is trapping the radio, see [airplane mode stuck on](/articles/how-to-fix-airplane-mode-stuck-on/).

## Why this happens

- **Windows Update installed a bad wireless driver**: The most common reason a reinstall is needed — Intel/Realtek/MediaTek updates frequently regress.
- **Driver corruption from interrupted updates**: Partial installs leave the driver half-functional: connects but drops, slow speeds, missing 5 GHz.
- **Wrong driver for the card revision**: Generic drivers that don't match your specific wireless card's revision.
- **Reinstall puts back the same bad version**: Windows' automatic reinstall reuses the driver store — uninstalling without deleting the driver changes nothing.
- **Competing driver sources**: Manufacturer driver vs. Windows Update version fighting, each reinstall undoing the other.
- **Chipset driver underneath is broken**: The Wi-Fi card depends on the chipset/PCIe bus driver; reinstalling Wi-Fi alone can't fix a bus problem.
- **Power management crippling the adapter**: Not a driver problem at all — but it mimics one perfectly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Prepare — download the correct driver first

Never start a Wi-Fi driver reinstall without the replacement in hand.

1. Identify your exact wireless card: **Device Manager** > **Network adapters** — note the full name (e.g., Intel Wi-Fi 6 AX201, Realtek 8852BE, MediaTek MT7921).
2. Also note your exact laptop model (`msinfo32` > **System Model**) — you'll need it for the manufacturer's page.
3. Download the driver: Intel cards → the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html); anything else → your laptop maker's support page ([Dell](https://www.dell.com/support), HP, or Lenovo). Save the installer to Desktop or a USB drive.
4. If your Wi-Fi is completely dead, do this download on another device (phone + USB cable works) — don't skip it.
5. Note your current driver version (**Properties** > **Driver** tab) so you can confirm the reinstall actually changed something.

### Fix 2: Uninstall the old driver completely

Remove it properly — including the driver package.

1. In **Device Manager** > **Network adapters**, right-click the Wi-Fi adapter > **Uninstall device**.
2. Check **Attempt to remove the driver for this device** (wording varies: "Delete the driver software for this device"). This is the critical step — without it, Windows just reactivates the same files.
3. If the checkbox doesn't appear, the driver is inbox — proceed anyway; the manual install in Fix 3 will override it.
4. Do NOT restart yet if you plan to also refresh the chipset driver (Fix 5) — batch the removals, then restart once.
5. If the Wi-Fi adapter is missing entirely, first try **View** > **Show hidden devices**; a greyed-out adapter can be right-click > **Enable device** instead of this whole procedure.

### Fix 3: Install the downloaded driver manually

Take control of what gets installed.

1. Disconnect from the internet if you have any alternative connection (unplug Ethernet) — this stops Windows Update from racing your manual install. (If Wi-Fi is your only connection and it's dead, you're already offline. Good.)
2. Run the driver installer you downloaded in Fix 1. Prefer the manufacturer's installer over "have disk" manual INF installation — the installer also sets up the correct services and power profiles.
3. If the installer offers a **clean install** or **remove old settings** option, take it.
4. Restart when prompted — wireless driver installs genuinely need the reboot to bind correctly.
5. After restart, verify in **Device Manager** > **Properties** > **Driver** tab that the version matches what you downloaded, not what was there before.

### Fix 4: Lock down power management and Windows Update

Protect the fresh install from the two things that break it.

1. In **Device Manager**, right-click the Wi-Fi adapter > **Properties** > **Power Management** tab > uncheck **Allow the computer to turn off this device to save power**.
2. Go to **Settings** > **Network & internet** > **Wi-Fi** > your network > set **Metered connection** considerations aside — instead, run the **Show or hide updates** troubleshooter from [Microsoft's support hub](https://support.microsoft.com/en-us/windows) and hide the wireless driver update that caused the original problem.
3. In **Power Options** > advanced settings, set **Wireless Adapter Settings** > **Power Saving Mode** to **Maximum Performance** on both battery and plugged-in (at least for testing).
4. Reconnect to your Wi-Fi network and test for at least 30 minutes of real use — speed test, video stream, a large download. Quick "it connects!" checks miss intermittent drop issues.
5. If problems recur only on battery, power management is still the culprit — revisit step 3 rather than reinstalling again.

### Fix 5: Reinstall the chipset driver underneath

When Wi-Fi reinstalls keep failing, the bus is the problem.

1. The Wi-Fi card communicates over the chipset's PCIe/USB bus — a broken chipset driver breaks every Wi-Fi reinstall built on top of it.
2. Download the chipset driver package for your platform: Intel → the Intel Driver & Support Assistant; AMD → AMD's driver download page.
3. Install the chipset package, restart, then redo Fix 2 + Fix 3 (Wi-Fi uninstall + manual install) on the now-healthy bus.
4. Check **Device Manager** > **System devices** for any remaining warnings — clear those first if present.
5. This two-layer reinstall (chipset, then Wi-Fi) resolves the stubborn cases where Wi-Fi alone never sticks.

### Fix 6: Reset the network stack (TCP/IP and Winsock)

For Wi-Fi that connects but doesn't work — "connected, no internet."

1. Open an elevated terminal (**Win + X** > **Terminal (Admin)**).
2. Run, in order: `netsh winsock reset`, then `netsh int ip reset`, then `ipconfig /flushdns`.
3. Restart the laptop.
4. Reconnect to Wi-Fi and test. These commands rebuild the network stack configuration that driver problems sometimes corrupt — the driver is fine but the stack it talks through is broken.
5. If you use VPN software, reinstall or update it after the reset — VPN filter drivers interact with the stack reset and stale ones cause exactly these symptoms.

### Fix 7: Rule out hardware and router-side issues

When the driver is proven good but Wi-Fi still misbehaves.

1. Test with a Linux live USB — if Wi-Fi works flawlessly in Linux with the same hardware, your Windows driver/stack is still the issue; if it's equally broken, suspect the card.
2. Test on a different network (phone hotspot): works on hotspot but not home Wi-Fi = router settings (try changing the router's channel, or disabling "smart connect" band-steering).
3. Check whether 2.4 GHz works but 5 GHz doesn't (or vice versa) — band-specific failure can indicate antenna issues (laptop antennas run through the hinge/display, a common damage point).
4. As a workaround or test, a $15 USB Wi-Fi adapter bypasses the internal card entirely — if the USB adapter is rock-solid, the internal card or its antennas are the problem.
5. Internal wireless cards are usually replaceable M.2 modules — cheap parts, modest labor. Antennas are harder (they're routed through the display assembly), so get a diagnosis before assuming.

## Closing

The "right way" to reinstall a Wi-Fi driver is really about control: get the correct driver yourself, remove the old one completely, install manually, and keep Windows Update from undoing your work. The quick uninstall-restart loop feels productive but usually just reinstalls the same broken version — which is why people do it five times. Do it properly once.
