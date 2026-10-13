---
title: "VIDEO_TDR_FAILURE on a Dell Laptop: How to Fix It"
slug: how-to-fix-video-tdr-failure-on-dell-laptop
date: 2026-10-04
categories: ["windows-errors"]
tags: ["video-tdr-failure", "dell", "gpu-driver"]
description: "VIDEO_TDR_FAILURE on a Dell laptop is almost always the graphics driver timing out. Here is the Dell-specific fix sequence that actually works."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-on-dell-laptop.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout Detection and Recovery. Windows gives the GPU two seconds to respond; if it does not, Windows resets the driver instead of freezing forever. When the reset itself fails, you get the VIDEO_TDR_FAILURE blue screen (stop code 0x116), usually naming atikmdag.sys, nvlddmkm.sys, or igdkmd64.sys."
  - q: "Why is this common on Dell laptops?"
    a: "Dell ships many models with switchable graphics (Intel + NVIDIA/AMD) and custom Dell graphics drivers. A generic driver from Windows Update or the GPU maker can conflict with Dell's power-management layer, causing the timeouts. Using Dell-validated drivers avoids most of these conflicts."
  - q: "Can overheating cause VIDEO_TDR_FAILURE?"
    a: "Absolutely — it is the second most common cause after drivers. A GPU choked with dust hits its thermal limit, throttles, and stops responding within the TDR window. If crashes happen during gaming or video work but never at idle, heat is a prime suspect."
  - q: "Should I use Dell's drivers or NVIDIA/AMD's drivers?"
    a: "Start with Dell's. They are validated against your exact model's BIOS and power delivery. Only try the GPU maker's reference drivers if Dell's are outdated and the problem persists — and be ready to roll back if timeouts get worse."
---
VIDEO_TDR_FAILURE is Windows telling you the graphics driver stopped answering and the recovery attempt failed. On Dell laptops this crops up a lot, because Dell's switchable-graphics setups and custom drivers add extra moving parts to the GPU timeout dance. The Dell-specific angle matters here: the fix sequence below leans on Dell's own tools and validated drivers first, because generic drivers are a leading cause of this exact crash on Dell hardware.

The Dell-specific angle matters here: the fix sequence below leans on Dell's own tools and validated drivers first, because generic drivers are a leading cause of this exact crash on Dell hardware. Dell's SupportAssist and validated driver packages are built for exactly this situation, so the sequence below uses them before reaching for generic tools.

## Why this happens

- **A corrupted or mismatched graphics driver.** The top cause — especially a reference NVIDIA/AMD driver fighting Dell's power management.
- **Overheating GPU.** Dust-clogged fans push the GPU past its thermal limit until it stops responding in time.
- **Dell BIOS/firmware out of date.** Old BIOS versions mishandle GPU power states on some models, triggering timeouts.
- **Failing GPU hardware.** Less common, but a dying discrete GPU times out under load with increasing frequency.
- **Overclocking or aggressive tuning.** Any GPU overclock on a laptop is living dangerously close to the TDR timeout.
- **Windows Update replacing your Dell driver.** A forced generic driver update can break a previously stable Dell-validated setup overnight.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Run Dell SupportAssist's full scan

Dell's own diagnostic catches driver, BIOS, and hardware issues in one pass. Let the scan finish completely — the BIOS check alone can take several minutes, and interrupting anything mid-flash is the one thing you must avoid.

1. Open **SupportAssist** from the Start menu (install it from [Dell Support](https://www.dell.com/support) if missing).
2. Run a full system scan and let it check drivers, BIOS, and hardware.
3. Install every driver and BIOS update it recommends — especially anything under graphics or chipset.
4. Restart and test under the workload that used to crash.

### Fix 2: Clean-install the Dell-validated graphics driver

Dell tests these drivers against your exact model, which is why they fix TDR crashes generic drivers cause. Dell's driver packages sometimes include firmware for the GPU's power controller, which is another reason the Dell-specific package beats the generic one for TDR issues.

1. Go to [Dell Support](https://www.dell.com/support) and enter your Service Tag (on the sticker underneath the laptop).
2. Download the latest graphics driver listed for your model.
3. In **Device Manager**, uninstall the current display driver, ticking **Attempt to remove the driver for this device**.
4. Install the Dell driver, restart, and stress-test with the app or game that triggered crashes.

### Fix 3: Update the BIOS

Dell regularly fixes GPU power-state bugs in BIOS updates, and TDR failures are a classic symptom. Note your current BIOS version first (run `msinfo32` and check **BIOS Version/Date**) so you can confirm the flash actually applied — assuming success after a failed flash wastes days.

1. On the same Dell Support page for your Service Tag, download the latest BIOS.
2. Plug the laptop into AC power — never flash a BIOS on battery.
3. Run the BIOS update executable and do not touch anything until it completes and reboots.
4. Re-test. If TDR crashes started after a specific BIOS version, this step often ends them. For background on reading crash screens, see our [blue screen walkthrough](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 4: Rule out overheating

Heat-induced timeouts follow a pattern: fine at idle, crashing under load. Dell's thin-and-light models are especially prone to heat timeouts: their cooling is tuned for quiet office work, and sustained gaming heat-soaks the chassis until the GPU throttles into timeouts.

1. Install a temperature monitor like HWMonitor and watch GPU temps during the crashing workload.
2. Sustained temps above 90C under load point at cooling: blow compressed air through the vents (laptop off), and use a cooling pad.
3. If the laptop is over two years old and still runs hot, dried thermal paste is likely — a repair shop can repaste the CPU/GPU in under an hour.
4. Also check that Windows power mode is not forcing maximum performance constantly: **Settings > System > Power & battery > Power mode**.

### Fix 5: Increase the TDR timeout (advanced)

Giving the GPU more than two seconds to recover can stop crashes on marginal hardware — a workaround, not a cure. This is a diagnostic aid as much as a workaround — if an 8-second timeout stops the crashes, you have confirmed the GPU was recovering slowly rather than hard-failing.

1. Press **Win + R**, type `regedit`, and press **Enter**.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Create a new **DWORD (32-bit) Value** named `TdrDelay` and set it to `8`.
4. Create another named `TdrDdiDelay` set to `8`, then restart. If crashes stop, the GPU was just slow to recover; still pursue the driver and heat fixes above.

### Fix 6: Test with the discrete GPU disabled

This isolates whether the NVIDIA/AMD chip itself is the problem. If the laptop has switchable graphics, also check the BIOS for a graphics-switching option — forcing integrated graphics at the firmware level is a cleaner test than Device Manager alone.

1. Open **Device Manager > Display adapters**, right-click the discrete GPU (NVIDIA/AMD), and choose **Disable device**.
2. Use the laptop on Intel integrated graphics for a day.
3. If crashes vanish, the discrete GPU or its driver is the culprit — try the GPU maker's reference driver from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx) as a last resort before suspecting hardware failure.
4. Re-enable the device afterward if you need its performance. Our guide to [disabling automatic restart](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) helps you capture the exact failing module if it still crashes.

## Closing

On Dell laptops, VIDEO_TDR_FAILURE is a driver story far more often than a hardware story. Dell-validated graphics drivers plus a current BIOS resolve the overwhelming majority of cases. Only when those fail — and heat is ruled out — should you start worrying about the GPU itself. And if you ever try the GPU maker's reference drivers later, come straight back to Dell's if the timeouts return — the validated package exists for a reason.
