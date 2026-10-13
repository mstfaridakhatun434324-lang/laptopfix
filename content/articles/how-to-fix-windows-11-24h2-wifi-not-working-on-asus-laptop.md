---
title: "Wi-Fi Not Working After Windows 11 24H2 on an Asus Laptop? Fix It"
slug: how-to-fix-windows-11-24h2-wifi-not-working-on-asus-laptop
date: 2026-09-15
categories: ["windows-update"]
tags: ["wifi not working", "windows 11 24h2", "asus", "wireless driver"]
description: "Lost Wi-Fi after Windows 11 24H2 on your Asus laptop? This is the classic 24H2 driver migration failure. Follow this ordered fix to bring wireless back."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-wifi-not-working-on-asus-laptop.webp"
faqs:
  - q: "Why is there no Wi-Fi option at all after 24H2 on my Asus?"
    a: "Because the wireless adapter's driver failed to migrate, Windows no longer sees a working Wi-Fi device. With no functional adapter, Settings hides the entire Wi-Fi section — the option is not disabled, the hardware is effectively missing to the OS."
  - q: "Does Asus Armoury Crate affect Wi-Fi after 24H2?"
    a: "It can. Armoury Crate and MyASUS install their own network and power profiles, and outdated versions conflict with the 24H2 network stack. Updating these utilities is a legitimate step in the fix sequence. If Wi-Fi returns immediately after updating these utilities, you have found your culprit without touching a single driver."
  - q: "Should I use the Asus driver or the Intel/MediaTek driver?"
    a: "Start with the Asus-published driver for your exact model — it is validated against your hardware. If Asus has not released a 24H2-ready version, the chipmaker's driver from Intel is the next best option and usually works fine. Whichever you choose, keep the installer file — 24H2-era driver regressions have a habit of recurring."
  - q: "My Ethernet works but Wi-Fi does not. What does that mean?"
    a: "It means the network stack is healthy and the problem is isolated to the wireless adapter or its driver. That is actually the best-case diagnosis — it narrows the fix to the driver steps in this guide. Start with the driver rollback and clean reinstall steps, since the rest of the networking stack is proven healthy."
---

After the Windows 11 24H2 update, your Asus laptop boots up and Wi-Fi is simply gone. Not disconnected — gone. No available networks, no Wi-Fi toggle in Quick Settings, and in Device Manager the wireless adapter wears a yellow warning triangle or has disappeared under Network adapters entirely. If you plug in Ethernet, everything works, which tells you the whole story: the update broke the wireless driver and nothing else.

Asus laptops are heavily represented in 24H2 Wi-Fi reports, particularly models with MediaTek and Intel wireless cards, and the MyASUS/Armoury Crate software layer adds an extra wrinkle other brands do not have. The fix sequence below accounts for that: driver triage first, Asus utilities second, network stack third. Most Asus owners get Wi-Fi back by Fix 4.

Asus ships two very different wireless cards — Intel and MediaTek — and they fail differently under 24H2. Intel cards usually fail with a driver that loads but cannot start the radio (Code 10), fixed by the Intel driver from the DSA. MediaTek cards more often vanish from Device Manager entirely, needing the Asus-published driver package to reappear. Check which card you have under Network adapters before downloading anything: the wrong vendor's driver wastes the attempt. This brand split is why generic advice so often misses on Asus machines.

## Why this happens

- **The wireless driver failed 24H2 migration.** The feature update could not carry the old driver forward, leaving a non-functional adapter.
- **Windows installed a mismatched generic driver.** The inbox driver covers the card's PCI ID but not its actual feature set, so it cannot start the radio.
- **MyASUS or Armoury Crate network profiles conflict.** Outdated Asus utilities apply power and network policies the new stack rejects.
- **The adapter is disabled at a firmware level.** Fast Startup or a BIOS reset can leave the radio in a disabled state the OS cannot override.
- **Corrupted network stack from the update.** Winsock and TCP/IP catalog damage breaks connectivity above the driver layer.
- **Power management aggressively sleeps the adapter.** 24H2 resets power plans, and Asus battery-saving profiles compound the effect.
- **A stuck driver update in Windows Update.** A half-installed wireless driver from Windows Update blocks any replacement from loading.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Inspect the adapter state in Device Manager

Know exactly what you are dealing with before touching anything.

1. Open **Device Manager** > **Network adapters** and find your wireless card.
1. Note any error code: Code 10, 31, and 43 are the classic post-24H2 driver failures.
1. Check the **Driver** tab for the driver date — a 2006 Microsoft date means a generic fallback is loaded.
1. If the adapter is missing entirely, check **View** > **Show hidden devices**; a grayed-out entry confirms a driver problem, not dead hardware.

### Fix 2: Roll back or reinstall the wireless driver

The two-minute fixes that resolve most cases.

1. On the **Driver** tab, click **Roll Back Driver** if it is available and restart.
1. If not, choose **Uninstall device**, check **Attempt to remove the driver**, and restart.
1. Let Windows redetect the hardware on boot.
1. Test Wi-Fi before doing anything else — stop here if it works.

### Fix 3: Update MyASUS and Armoury Crate

Asus-specific step: outdated utilities sabotage the new network stack.

1. Open the **Microsoft Store** and update **MyASUS** and **Armoury Crate** to their latest versions.
1. In MyASUS, run **System Diagnostics** > **Connectivity** if available.
1. Restart after the utility updates.
1. Retest Wi-Fi — utility conflicts resolve silently more often than people expect.

### Fix 4: Install the correct wireless driver manually

When rollback is unavailable, bring the right driver yourself.

1. Download the wireless driver for your exact model from Asus support.
1. For Intel-based cards, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is the fastest reliable source.
1. Install on AC power, restart, and verify the warning icon is gone.
1. Keep the installer — you will need it again if Windows Update overwrites the driver.

### Fix 5: Reset TCP/IP and Winsock

For cases where the adapter looks healthy but no connection ever completes.

1. Run `netsh winsock reset` and `netsh int ip reset` in an elevated Command Prompt.
1. Follow with `ipconfig /flushdns`.
1. Restart and reconnect to your network.
1. If Settings still shows no Wi-Fi section, the driver — not the stack — remains the problem; return to Fix 4.

### Fix 6: Stop Windows Update from breaking it again

Asus drivers from Windows Update are a repeat offender for 24H2 machines.

1. Set **Device Installation Settings** to **No** so Windows stops auto-replacing your working driver.
1. Pause driver updates via **Settings** > **Windows Update** > **Advanced options** if needed.
1. Document which driver version works, in case a future update regresses it.
1. The [driver update failure guide](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/) covers hiding specific bad driver updates.

### Fix 7: Check BIOS wireless settings and the physical switch

The rare hardware-level causes, checked last because they are rare.

1. Enter BIOS (F2 during Asus boot) and confirm the wireless radio is enabled.
1. Check for a physical wireless switch or Fn-key toggle and cycle it.
1. Disable **Fast Startup** in `powercfg.cpl` — it can leave the radio in a bad power state.
1. If the adapter is still invisible everywhere, [Microsoft support](https://support.microsoft.com/en-us/windows) documents the remaining 24H2 network recovery steps, and Asus support can confirm a hardware fault. Compare notes with the [Acer 24H2 Wi-Fi guide](/articles/how-to-fix-windows-11-24h2-wifi-not-working-on-acer-laptop/) — the driver logic is identical across brands.

### Fix 8: Reset the BIOS to optimized defaults

Clears firmware-level radio disables that survive OS fixes.

1. Restart and press **F2** repeatedly to enter the Asus BIOS.
1. Press **F9** (or find Load Optimized Defaults) and confirm.
1. Verify the wireless radio is enabled in the Advanced settings.
1. Save with **F10**, boot into Windows, and re-check Device Manager for the adapter.

## Closing

On Asus laptops, post-24H2 Wi-Fi failure is a driver migration problem wearing a hardware costume. Work the driver angle first — rollback, clean reinstall, then the correct Asus or Intel driver — update the Asus utilities, and only then touch the network stack. Lock the working driver in place afterward, and 24H2 goes back to being the uneventful update it was supposed to be.
