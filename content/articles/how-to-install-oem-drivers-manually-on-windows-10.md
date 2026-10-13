---
title: "How to Install OEM Drivers Manually on Windows 10"
slug: how-to-install-oem-drivers-manually-on-windows-10
date: 2026-09-07
categories: ["drivers"]
tags: ["oem drivers", "manual driver install", "windows 10", "device manager", "driver inf"]
description: "Need to install OEM drivers manually on Windows 10? Learn the exact Device Manager method, INF installs, and the order that avoids conflicts."
thumbnail: "/images/thumbs/how-to-install-oem-drivers-manually-on-windows-10.webp"
faqs:
  - q: "What is the difference between OEM and generic drivers?"
    a: "OEM drivers are customized by your laptop maker (Dell, HP, Lenovo, ASUS, Acer) for your exact model's hardware — power management, hotkeys, touchpad gestures, and audio tuning are OEM-specific. Generic drivers from the chip maker (Intel, Realtek, NVIDIA) drive the silicon but lack those customizations. For laptop-specific hardware, the OEM package is almost always the better choice; for the GPU, the chip maker's current driver is often fine."
  - q: "How do I manually install a driver from an INF file?"
    a: "Extract the driver package, open Device Manager, right-click the device, choose Update driver, then Browse my computer for drivers, and point it at the folder containing the INF file. Windows matches the hardware ID and installs it. Alternatively, right-click the INF file itself and choose Install — though the Device Manager method gives you better error feedback when something mismatches."
  - q: "In what order should I install OEM drivers?"
    a: "Chipset first, then storage/SATA, then graphics (integrated before discrete), then network (Ethernet, WiFi, Bluetooth), then audio, then touchpad/input, then the maker's utilities (hotkeys, power management) last. The chipset driver defines the platform everything else builds on — installing graphics before the chipset is the classic cause of mysterious device conflicts."
  - q: "Why did Windows replace my manually installed OEM driver?"
    a: "Windows Update treats drivers as updatable components and will replace your manual install with whatever its catalog considers newer — which is often older in reality. After a manual install, use the Show or hide updates troubleshooter to hide that driver update, or on Pro editions enable 'Do not include drivers with Windows Updates' in Group Policy. Otherwise your careful manual work unravels at the next update cycle."
---

Automatic driver installation covers most needs, but sometimes you must do it by hand: a fresh Windows install with no network driver, a device Windows can't identify, a specific OEM version you need to pin, or a driver package that only ships as loose INF files. Manual installation isn't difficult — it's just unforgiving of wrong packages and wrong order, which is why a strict procedure matters.

This guide covers the full manual workflow on Windows 10: identifying the exact device, getting the right OEM package, the three installation methods, the correct order, and protecting your work from Windows Update.

## Why this happens

- **Fresh Windows install missing drivers.** Clean installs lack network, chipset, and OEM drivers.
- **Windows can't identify the device.** Unknown devices needing manual INF matching.
- **Needing a specific OEM version.** Pinning a known-good build against Windows Update's whims.
- **Driver only ships as INF files.** No installer EXE — manual installation is the only path.
- **Corrupt automatic install.** The auto-installed driver broken, needing manual replacement.
- **Wrong driver installed automatically.** Windows picking a plausible-but-wrong match.
- **OEM customizations required.** Generic driver working but missing laptop-specific features.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the exact device and get its hardware ID

Manual installation starts with knowing precisely what you're installing for.

1. Open **Device Manager**, find the device (or **Unknown device** / device with a yellow warning).
2. Right-click > **Properties > Details tab > Property: Hardware Ids**.
3. Copy the top **PCI\VEN_xxxx&DEV_xxxx** string — this is the device's fingerprint.
4. Search that string online to confirm the exact chip (e.g., VEN_8086 = Intel, VEN_10DE = NVIDIA, VEN_14E4 = Broadcom).
5. This ID is also how you verify a downloaded INF actually targets your hardware before installing.

### Fix 2: Download the correct OEM package

The right package is everything — a wrong one either refuses or installs badly.

1. Go to your **laptop maker's support site** (Dell, HP, Lenovo, ASUS, Acer), enter your **serial number or exact model**.
2. Filter by **Windows 10 64-bit** and download the driver for your component.
3. Prefer packages with an **installer EXE** when available — run it first; manual INF installation is for packages without one.
4. For INF-only packages, extract the ZIP to a permanent folder (e.g., C:\Drivers\Component) — don't install from a temp folder you'll delete.
5. Verify the INF targets your hardware: open it in Notepad and search for your **VEN/DEV** strings.

### Fix 3: Install via Device Manager (the standard method)

The reliable manual path with the best error feedback.

1. In **Device Manager**, right-click the device > **Update driver**.
2. Choose **Browse my computer for drivers** (not automatic search).
3. Click **Browse**, select the folder containing the extracted INF files, check **Include subfolders**, click Next.
4. Windows matches the hardware ID and installs — restart if prompted.
5. Verify: **Properties > Driver tab** — the version and provider should match the package you installed.

### Fix 4: Install via INF right-click and Have Disk

The two alternate methods for stubborn cases.

1. **INF right-click method**: in File Explorer, right-click the **.inf** file > **Install**. Quick, but gives minimal feedback — use it when you trust the package.
2. **Have Disk method**: Device Manager > Update driver > Browse my computer > **Let me pick from a list** > **Have Disk** > browse to the INF. This forces Windows to use your file even when it thinks it has a better match.
3. If Windows warns the driver is **unsigned**, stop — don't install unsigned drivers from untrusted sources; get the signed OEM package instead.
4. For **Unknown devices**, the Have Disk method with the right INF is often the only thing that works.
5. After any manual install, restart — driver registration completes at boot.

### Fix 5: Install in the correct order

Order prevents the conflicts that plague manual driver sessions.

1. **Chipset/INF** first — the platform foundation.
2. **Storage** (Intel RST / AMD SATA) and **Management Engine** next.
3. **Graphics**: integrated GPU first, then discrete (NVIDIA/AMD) with clean-install option.
4. **Network**: Ethernet, then WiFi, then Bluetooth.
5. **Audio** (Realtek), **touchpad/input**, then the maker's **utilities and hotkey software** last.
6. Restart between major groups — don't stack six driver installs without rebooting.
7. Our NVIDIA-specific guide demonstrates the clean-install discipline: [how to update NVIDIA drivers with a clean install in Windows 11 24H2](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/).

### Fix 6: Handle compatibility-mode installs

For OEM drivers written for older Windows.

1. If the OEM installer refuses on Windows 10 ("unsupported OS"), right-click the setup EXE > **Properties > Compatibility**.
2. Check **Run this program in compatibility mode for** and try **Windows 8** or **Windows 7**.
3. Also check **Run as administrator**.
4. This commonly rescues old touchpad, hotkey, and card-reader drivers whose installers predate Windows 10.
5. The deeper compatibility technique is covered in [how to install driver in compatibility mode in Windows 11 24H2](/articles/how-to-install-driver-in-compatibility-mode-in-windows-11-24h2/) — the mechanics are identical on Windows 10.

### Fix 7: Protect the manual install from Windows Update

Your hand-installed driver is exactly what Windows Update loves to "fix."

1. After verifying the driver (Fix 3's step 5), run the **Show or hide updates** troubleshooter and hide any update for that device.
2. On Windows 10 Pro: **Group Policy > Computer Configuration > Administrative Templates > Windows Components > Windows Update > Do not include drivers with Windows Updates** = Enabled.
3. Recheck the driver version after the next Patch Tuesday — swaps happen then.
4. Keep the extracted driver folder — you'll need it again if Windows replaces the driver despite the block.
5. Microsoft's driver servicing background: [Windows support](https://support.microsoft.com/en-us/windows).

## Closing

Manual OEM driver installation is a procedure, not a hack: identify by hardware ID, download the exact OEM package, install via Device Manager in chipset-first order, verify the version took, and block Windows Update from undoing it. Follow the sequence and manual installs are as reliable as any installer EXE — skip steps and you'll be doing it twice.
