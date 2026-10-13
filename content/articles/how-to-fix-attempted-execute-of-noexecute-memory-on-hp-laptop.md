---
title: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on an HP Laptop"
slug: how-to-fix-attempted-execute-of-noexecute-memory-on-hp-laptop
date: 2026-10-06
categories: ["windows-errors"]
tags: ["attempted execute of noexecute memory", "hp", "blue screen"]
description: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on your HP laptop: update HP drivers, scan for malware, and test memory with these steps."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-on-hp-laptop.webp"
faqs:
  - q: "What does this error mean on my HP laptop?"
    a: "Stop code 0x000000FC: a driver tried to run code from memory marked non-executable, and Windows' Data Execution Prevention stopped it with a blue screen. On HP laptops the cause is usually an outdated graphics, chipset, or network driver."
  - q: "Where should I download drivers for my HP?"
    a: "Use HP Support Assistant or HP's support pages with your exact model number. HP tests those drivers against your hardware. For the GPU you can also go direct to the chip vendor, but HP's versions are the safer first choice."
  - q: "Could this be a virus?"
    a: "Unlikely but worth ruling out — run a full Microsoft Defender scan first. In the vast majority of cases the cause is a legitimate driver misbehaving, not malware."
  - q: "It only crashes when I play games. Why?"
    a: "The graphics driver works hardest during gaming, so a buggy GPU driver only trips the protection under load. A clean install of the latest graphics driver fixes most gaming-triggered cases."
---

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (0x000000FC) on an HP laptop is Windows' memory protection catching a driver red-handed: it tried to execute code from a page marked data-only. Windows treats that the way it treats an exploit attempt — instant blue screen, no negotiation. The name sounds like a cyberattack, but on HP machines the offender is almost always mundane: an outdated graphics driver, a stale chipset driver, or a network driver that has not kept up with the Windows build.

HP gives you a clean path through this with HP Support Assistant and the support site's model-specific drivers. The repair sequence below is the same one a technician would run: rule out malware, refresh drivers from HP's validated set, then check memory and firmware.

## Why this happens

- **Outdated HP graphics driver:** The top cause by a wide margin. GPU drivers that lag behind the Windows build trip Data Execution Prevention, especially under gaming or video load.
- **Old chipset drivers:** HP's chipset drivers manage memory behavior at a low level; outdated ones cause exactly this fault.
- **Network driver bugs:** Wi-Fi and Ethernet drivers run in protected memory regions and are the second most common trigger.
- **Failing RAM:** Bad memory cells corrupt page attributes, making perfectly good driver code look like an execution violation.
- **Kernel-level third-party software:** VPN clients, old antivirus products, and outdated HP utilities install drivers into sensitive memory areas.
- **Overclocking on Omen/Victus:** XMP or CPU tweaks destabilize execution flow and can produce this stop code out of nowhere.
- **Corrupted driver installation:** An interrupted driver update leaves a driver that misbehaves in ways its version number does not explain.

## How to fix it

Work through these in order — most HP cases resolve by Fix 3.

### Fix 1: Rule out malware with a full Defender scan

1. Open **Settings → Privacy & security → Windows Security → Virus & threat protection**.
2. Choose **Scan options → Full scan → Scan now** and let it finish (30–60 minutes).
3. Remove anything found, restart, and test for a day before moving on.
4. A clean scan lets you focus on drivers with confidence — the cause is almost certainly not malware at that point.
5. If Defender will not start or complete, boot into Safe Mode and run the scan from there, where third-party interference is minimal.

### Fix 2: Update all drivers via HP Support Assistant

1. Open **HP Support Assistant** (preinstalled on most HPs) and go to **Updates**.
2. Install everything it recommends, with priority on **graphics**, **chipset**, **network**, and **BIOS** (BIOS updates only on AC power — never on battery).
3. If Support Assistant is missing, go to [HP support](https://support.hp.com/us-en), enter your exact model number, and download the drivers manually.
4. Restart after installing and use the laptop normally for a day.
5. HP-validated drivers are tested against your exact hardware combination — this resolves most 0xFC cases on HP machines in a single pass.

### Fix 3: Clean-install the graphics driver

1. If crashes happen during gaming, video editing, or video calls, identify your GPU: press **Win + R**, type `dxdiag`, and check the **Display** tab.
2. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD's driver page, or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html).
3. Run the installer, choose **Custom**, and tick **Perform a clean installation** (NVIDIA/AMD) to wipe all traces of the old driver.
4. Restart and test under the same load that triggered the crashes.
5. On Omen and Victus gaming models, this step alone fixes the large majority of 0xFC crashes — do not settle for the driver version Windows Update offers.

### Fix 4: Update network drivers specifically

1. Open **Device Manager** and expand **Network adapters**.
2. Note your Wi-Fi adapter model, then download the latest Wi-Fi and Bluetooth drivers for your exact HP model from [HP support](https://support.hp.com/us-en).
3. Install them and restart.
4. If crashes correlate with Wi-Fi activity — video calls, large downloads, hotspot use — the network driver was likely the culprit all along.
5. Similar network-driver crashes show up under other stop codes too; our [driver power state guide](/articles/driver-power-state-failure-windows-11-fix/) covers the sleep/wake variant.

### Fix 5: Remove suspect kernel-level software

1. Open **Settings → Apps → Installed apps**, sort by install date, and look at what was added near the time crashes began.
2. Uninstall VPN clients, old antivirus products, and system "optimizers" you do not actively use — these install drivers that live in exactly the memory regions this error protects.
3. In **Device Manager**, enable **View → Show hidden devices** and uninstall greyed-out remnants of removed software.
4. Restart and test for a day or two before concluding.
5. If you removed third-party antivirus, confirm Microsoft Defender is active (**Settings → Privacy & security → Windows Security**) so you are not left unprotected.

### Fix 6: Repair system files and test memory

1. Open **Terminal (Admin)** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` once more.
2. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems** — let the full test complete.
3. If memory errors appear, power off, reseat the modules (if your HP has accessible slots), and retest; persistent errors mean the module needs replacing.
4. HP also ships hardware diagnostics: restart and press **F2** at the HP logo, then run **Component Tests → Memory**. Two agreeing tests make the verdict solid.
5. If you are seeing several different stop codes rather than just 0xFC, our [general blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) helps you decide which one to chase first.

### Fix 7: Reset BIOS to defaults and update it

1. Restart and press **F10** to enter HP BIOS Setup.
2. Choose **Load Setup Defaults** (on Omen, also reset any overclocking profiles in Omen Gaming Hub).
3. Check HP Support Assistant for a newer BIOS and install it on AC power if one is offered.
4. Save, exit, and retest under load. Default firmware settings eliminate XMP/CPU instability as a cause.
5. If the crashes stop after the reset, the overclock or a stale firmware setting was the problem all along — leave the defaults in place.

### Fix 8: Use System Restore as a safety net

1. If a specific change started the crashes and driver work has not helped, press **Win + R**, type `rstrui`, and pick a restore point from before the crashes began.
2. Your files are untouched — only system files, drivers, and registry settings roll back.
3. After restoring, immediately update drivers via HP Support Assistant before Windows Update reinstalls the problematic version.
4. Going forward, keep System Protection enabled (**sysdm.cpl → System Protection → Configure → Turn on system protection**) so you always have a restore point for the next bad driver.

## Closing

On HP laptops, ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY is a driver refresh away from fixed in the large majority of cases — run HP Support Assistant, clean-install the graphics driver, and update network drivers. Rule out malware first so you are not chasing ghosts, test the RAM if drivers do not solve it, and reset the BIOS as the final check. The error name sounds like a cyberattack; the reality is usually just a tired driver that HP already shipped a replacement for.
