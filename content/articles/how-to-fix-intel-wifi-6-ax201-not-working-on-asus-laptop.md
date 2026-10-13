---
title: "Intel Wi-Fi 6 AX201 Failure on ASUS Laptops: Diagnosis and Repair"
slug: how-to-fix-intel-wifi-6-ax201-not-working-on-asus-laptop
date: 2026-10-09
categories: ["drivers"]
tags: ["intel ax201", "wifi not working", "asus laptop", "wifi 6", "wireless driver"]
description: "AX201 Wi-Fi dead on your ASUS Vivobook or Zenbook? Diagnose error codes, reinstall drivers, and fix CNVi and power issues."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why does the AX201 show code 10 in Device Manager on ASUS laptops?"
    a: "Code 10 means the driver failed to start the device — on the AX201 this usually follows a Windows update installing a mismatched driver, or corruption in the existing Intel wireless driver. Because the AX201 depends on the CNVi interface, an outdated chipset driver or BIOS can also trigger code 10 even with a correct Wi-Fi driver. Clean-reinstall the Intel Wi-Fi driver first, then update chipset and BIOS if it persists."
  - q: "MyASUS offers a Wi-Fi driver update. Should I use it?"
    a: "MyASUS driver updates are validated for your exact model, so they are a safe first choice — especially when the generic Intel driver misbehaves. However, MyASUS versions can lag months behind Intel's releases. If the MyASUS driver does not fix the problem, Intel's generic AX201 driver is a legitimate fallback since the card uses the standard CNVi interface across manufacturers."
  - q: "Can the AX201 be replaced with a different Wi-Fi card on ASUS laptops?"
    a: "Sometimes, but check carefully. Many ASUS models use the CNVi interface where part of the Wi-Fi logic lives in the chipset, so only CNVi-compatible cards (like other Intel CNVi models) work in that slot — a standard non-CNVi card will not function. Also verify the BIOS whitelist situation for your model and the antenna connector types before buying a replacement."
  - q: "Wi-Fi works but is extremely slow on the AX201. Is that a driver issue?"
    a: "Often yes. Slow AX201 speeds commonly come from the driver negotiating a weak link — wrong band preference, aggressive power saving throttling the radio, or a mismatch with the router's Wi-Fi 6 features. Update to the latest Intel driver, set the wireless adapter power saving to Maximum Performance, and test against both 2.4 and 5 GHz bands to isolate whether it is a band-specific negotiation failure."
---

The Intel AX201 in ASUS Vivobook, Zenbook, and TUF laptops fails in recognizable patterns: code 10 in Device Manager, the adapter vanishing after sleep, connections that drop minutes after boot, or full-speed Wi-Fi that degrades to a crawl. Because the AX201 is a CNVi card — half its logic lives in the Intel chipset — these failures can originate in the Wi-Fi driver, the chipset driver, the BIOS, or Windows power management. Guessing which one wastes time; the diagnostic sequence below does not.

ASUS's MyASUS utility complicates the picture slightly by offering its own validated driver builds, which are safe but often dated. This guide uses both ASUS and Intel sources strategically. For the Acer perspective on the same card, see our [Acer AX201 repair](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-acer-laptop/), and if Wi-Fi has disappeared from Windows entirely, the [vanished Wi-Fi guide](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/) covers the broader symptom.

## Why this happens

- **The Intel wireless driver is corrupted or mismatched**, producing code 10 or 43 after a Windows update.
- **The CNVi interface is unstable** due to an outdated chipset driver or BIOS on early production runs.
- **Windows power management suspends the adapter** and it fails to resume cleanly, dropping connections.
- **The adapter is hidden after repeated init failures**, making it look like the hardware vanished.
- **MyASUS installed an outdated validated driver** that conflicts with a newer Windows build.
- **Router feature mismatches** (WPA3, 160 MHz channels, Wi-Fi 6 modes) cause negotiation failures with certain driver builds.
- **Third-party VPN filter drivers** interfere with the adapter's initialization.

- **ASUS's Wi-Fi power-saving profiles in MyASUS or Armoury Crate** throttle the AX201 radio independently of Windows settings, causing drops that survive every Windows-side power tweak.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the adapter's error code

The code determines whether you chase drivers, power, or firmware. Screenshot the error code screen — you will need the exact code if you escalate to support.

1. Press Win + X, open Device Manager, and expand Network adapters.
2. If the AX201 is missing, open View and select Show hidden devices.
3. Double-click the Intel Wi-Fi 6 AX201 and read Device status.
4. Code 10/43 means driver failure; code 45 means disconnected hardware; absent entirely suggests firmware or BIOS.

### Fix 2: Check MyASUS for the validated driver

Start with ASUS's own build before going generic. MyASUS driver scans sometimes miss the Wi-Fi entry — check the full driver list manually.

1. Open MyASUS and go to the driver update section.
2. Install any Wi-Fi or wireless driver update it offers.
3. Restart and test for a full day of normal use.
4. If the problem persists or MyASUS offers nothing, move to Intel's driver.

### Fix 3: Clean-reinstall the Intel Wi-Fi driver

The deep fix for corrupted driver states. Intel's [detection tool](https://www.intel.com/content/www/us/en/support/detect.html) identifies the right package for your system. Armoury Crate's power profiles can re-enable Wi-Fi power saving after Windows updates.

1. Download the latest AX201 Wi-Fi driver from Intel.
2. In Device Manager, right-click the AX201, choose Uninstall device, and tick Delete the driver software.
3. Restart the laptop.
4. Install the Intel package immediately after boot, then restart once more.

### Fix 4: Disable adapter power saving

Stops the resume failures behind drop-after-boot symptoms. Run the network reset commands from an elevated prompt or they will fail silently.

1. In the AX201's Properties, Power Management tab, untick Allow the computer to turn off this device.
2. In Power Options advanced settings, set Wireless Adapter Settings to Maximum Performance for battery and plugged in.
3. In MyASUS or Windows battery settings, disable aggressive Wi-Fi power saving profiles.
4. Test with the laptop on battery — the most common dropout scenario.

### Fix 5: Reset the network stack

Clears corrupted Winsock and TCP/IP state that mimics adapter failure. BIOS changelogs sometimes describe the fix as 'system stability' rather than naming Wi-Fi.

1. Open an elevated Terminal (Win + X, Terminal as administrator).
2. Run `netsh winsock reset` and press Enter.
3. Run `netsh int ip reset` and press Enter.
4. Restart and reconnect to your network.

### Fix 6: Update the BIOS and chipset driver

For CNVi-level instability that survives driver reinstalls. Test with the router's Wi-Fi 6 mode temporarily disabled to isolate 802.11ax negotiation bugs.

1. Check the ASUS support page for your model for a newer BIOS mentioning wireless or connectivity.
2. Flash on AC power with nothing else running; never interrupt it.
3. Install the latest Intel chipset driver for your model.
4. Reinstall the AX201 driver after the platform update so it binds cleanly.

### Fix 7: Test band and router compatibility

Isolate negotiation failures from adapter failures.

1. In the AX201 Advanced properties, try setting Preferred Band to 5 GHz only, then 2.4 GHz only.
2. On your router, temporarily disable WPA3 or 160 MHz channel width as a test.
3. If one band works reliably and the other does not, the issue is negotiation, not hardware.
4. Update the router firmware if band-specific failures persist across driver versions.

## Closing

The AX201 on ASUS laptops is almost always recoverable: the error code tells you where to look, MyASUS or Intel provides the driver, and power management plus BIOS updates cover the stubborn cases. Slow-speed variants deserve the band and router tests before anyone blames the card. Only a permanently absent adapter — code 45 or invisible even as a hidden device after all fixes — justifies opening the machine to check the card and antenna leads. Once stable, run a sustained speed test and a long video call to confirm the fix holds under load — brief connectivity checks miss the resume-from-sleep failures that plague this card. Note the working driver version somewhere safe, since Windows Update will eventually offer a replacement and you will want to compare before accepting.
