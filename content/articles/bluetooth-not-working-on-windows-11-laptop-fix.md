---
title: "Bluetooth Not Working on Your Windows 11 Laptop? Here's the Fix"
slug: bluetooth-not-working-on-windows-11-laptop-fix
date: 2026-09-19
categories: ["drivers"]
tags: ["bluetooth not working", "windows 11", "bluetooth driver", "device manager", "wireless"]
description: "Bluetooth not working on Windows 11? Fix missing toggles, pairing failures, and dead adapters with 7 proven driver and service repairs."
thumbnail: "/images/thumbs/bluetooth-not-working-on-windows-11-laptop-fix.webp"
faqs:
  - q: "Why did Bluetooth disappear from my Windows 11 laptop?"
    a: "The Bluetooth adapter usually vanished from Device Manager because its driver failed to load — often after a Windows update replaced the manufacturer's driver, or the adapter got disabled at the BIOS or function-key level. Less commonly, the wireless card itself has failed. The fix sequence re-enables and reinstalls before concluding hardware failure."
  - q: "Why won't my Bluetooth headphones pair anymore?"
    a: "Pairing failures are usually stale pairing data on one side — remove the device from both Windows (Settings, Bluetooth & devices, Remove device) and the headphones (their reset procedure), then pair fresh. If fresh pairing fails, update the Bluetooth driver; outdated drivers are the top cause of pairing regressions."
  - q: "Is there a Bluetooth troubleshooter in Windows 11?"
    a: "Yes — Settings, System, Troubleshoot, Other troubleshooters, then run Bluetooth. It checks the radio state, driver, and required services automatically. It fixes simple cases (stopped services, disabled radio) in under a minute, so run it early rather than as a last resort."
  - q: "Can a BIOS update fix Bluetooth?"
    a: "Sometimes. The Bluetooth radio lives on the Wi-Fi card, and BIOS updates include firmware and power-management fixes for that card. If Bluetooth is unstable specifically after sleep/wake, a BIOS update plus the manufacturer's wireless driver package is a high-yield combination."
---

Bluetooth failures on Windows 11 come in three flavors: the toggle is gone entirely, devices won't pair, or paired devices connect and immediately misbehave. All three usually trace to the same neighborhood — the Bluetooth driver, the radio's power state, or the services underneath. The Bluetooth stack is more fragile than Wi-Fi's because it involves pairing cryptography, audio profiles, and power management all cooperating; one broken layer and the whole thing looks dead.

This guide covers all three flavors in one ordered sequence, from the 30-second checks (airplane mode, function keys, the troubleshooter) through driver surgery to the hardware verdict. Most cases resolve in the first half.

## Why this happens

- **Driver replaced or corrupted by Windows Update.** The top cause — a generic or half-installed Bluetooth driver.
- **Bluetooth adapter disabled.** Via function key, airplane mode, BIOS toggle, or Windows' own device disable.
- **Stale pairing data.** Corrupted pairing keys on the Windows side or the device side.
- **Stopped Bluetooth services.** Required services killed by updates or "optimizer" tools.
- **Power management turning off the radio.** Windows powering down the adapter to save battery, then failing to wake it.
- **Wi-Fi/Bluetooth combo card issues.** The shared card's firmware or driver mishandling the Bluetooth side.
- **Failed wireless card hardware.** Least common — the radio itself dying.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious toggles

Thirty seconds that resolve an embarrassing share of cases.

1. Check **airplane mode** — off, obviously, but also toggle it on and back off to reset the radios.
2. Look for a **function key** (often Fn+F5 or a wireless icon key) that toggles Bluetooth/Wi-Fi — press it.
3. Open **Settings > Bluetooth & devices** — if the Bluetooth toggle is missing entirely, the driver isn't loading (skip to Fix 3).
4. Run the **Bluetooth troubleshooter**: Settings > System > Troubleshoot > Other troubleshooters > Bluetooth > Run.
5. Restart the laptop — Bluetooth stack glitches often clear with a full restart (not just sleep/wake).

### Fix 2: Restart Bluetooth services

The services the stack depends on.

1. Press **Windows + R**, type `services.msc`, press Enter.
2. Find **Bluetooth Audio Gateway Service**, **Bluetooth Support Service**, and **Bluetooth User Support Service**.
3. Set each to **Automatic** (or Automatic Delayed Start) and **Start** them if stopped.
4. If a "debloat" tool disabled them, re-enable — those tools break Bluetooth routinely.
5. Restart and test pairing again.

### Fix 3: Reinstall the Bluetooth driver

The core fix for missing toggles and broken stacks.

1. **Device Manager** → **Bluetooth** → right-click your adapter → **Uninstall device** (check "delete driver software").
2. Also check under **Network adapters** — the Bluetooth enumerator sometimes lives with the Wi-Fi card entry.
3. Restart — Windows reinstalls a baseline driver.
4. If Bluetooth is still broken, download the **wireless/Bluetooth driver package** from your laptop maker's support page — Bluetooth and Wi-Fi ship as one package on combo cards.
5. For Intel cards, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the newest Bluetooth + Wi-Fi drivers reliably.

If the adapter is missing from Device Manager entirely, see [how to fix Bluetooth disappeared from Device Manager in Windows 11 24H2](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2/).

### Fix 4: Fix pairing failures specifically

When the radio works but devices won't pair.

1. **Settings > Bluetooth & devices** → find the device → **Remove device**.
2. Reset the peripheral itself (headphones/speakers all have a pairing-reset procedure — hold the power/pair button per the manual).
3. Put the peripheral in pairing mode fresh, then **Add device** in Windows.
4. If pairing starts but fails, move the devices closer — weak-signal pairing fails cryptically.
5. For audio devices that pair but sound wrong: **Settings > System > Sound** → check the output is the **Stereo** profile, not Hands-Free (which sounds terrible and is a profile issue, not a failure).

### Fix 5: Stop power management from killing the radio

The "works until sleep" pattern.

1. **Device Manager** → **Bluetooth** → adapter → **Properties > Power Management** → **uncheck** "Allow the computer to turn off this device to save power."
2. Do the same for the Wi-Fi adapter under **Network adapters** — the combo card shares power logic.
3. **Settings > System > Power & battery** → set **Power mode** to Best performance while plugged in for testing.
4. Test sleep/wake cycles deliberately — if Bluetooth dies specifically after sleep, this was the cause.
5. Update the BIOS from your maker's support page; sleep/wake radio fixes are common in changelogs.

The general driver-update method for all of this: [how to update drivers on a Windows 11 laptop](/articles/how-to-update-drivers-on-windows-11-laptop/).

### Fix 6: Repair system files and reset the stack

For corruption beneath the driver.

1. **Terminal (Admin)**: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`, then restart.
2. Install all pending Windows updates — Bluetooth stack fixes ship in cumulative updates.
3. If a specific update broke Bluetooth, check the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for a superseding fix, or uninstall the offending KB.
4. As a deeper reset, remove **all** Bluetooth devices from Settings, uninstall the adapter driver (Fix 3), restart, and re-pair everything from scratch.
5. Test with a different Bluetooth peripheral to rule out a device-side problem masquerading as a Windows problem.

### Fix 7: Check BIOS toggles and hardware

The final verdict on the radio itself.

1. Enter BIOS/UEFI and verify **Wireless/Bluetooth** isn't disabled there.
2. Check for a physical wireless switch on the laptop chassis (rare now, but some business laptops still have them).
3. In Device Manager, show hidden devices — a grayed-out Bluetooth adapter with an error code points at driver/firmware, not dead hardware.
4. Boot a Linux USB live environment and test Bluetooth there — working in Linux + dead in Windows = software; dead in both = hardware.
5. A failed combo card is usually a replaceable M.2 module (Intel AX210 and similar) — cheap on models where it's socketed, a service job where it's soldered.

## Closing

Bluetooth on Windows 11 breaks in familiar ways: updates replace the driver, power management strangles the radio after sleep, pairing data goes stale, or a "tuning" tool murders the services. Work the sequence — toggles, services, driver reinstall, pairing hygiene, power settings — and the radio almost always comes back. The hardware verdict is genuinely rare, so don't order a replacement card until you've done the driver work; the number of "dead" Bluetooth adapters revived by the manufacturer's own wireless package would surprise you.
