---
title: "HDMI Not Working on Your Laptop? Fix the No-Signal Problem Step by Step"
slug: how-to-fix-hdmi-not-working-on-laptop
date: 2026-09-21
categories: ["drivers"]
tags: ["hdmi not working", "no signal hdmi", "laptop hdmi port", "external monitor", "gpu driver"]
description: "HDMI not working on your laptop? Fix no-signal errors, undetected displays, and flaky HDMI ports with this ordered guide covering cables, display settings, and GPU drivers."
thumbnail: "/images/thumbs/how-to-fix-hdmi-not-working-on-laptop.webp"
faqs:
  - q: "Why does my laptop say no signal on HDMI?"
    a: "No signal means the display sees a physical connection but receives no video data. The usual causes are a faulty cable, the wrong input selected on the monitor, the laptop outputting to the wrong display mode, or a broken GPU driver. Work the chain: cable, input source, display settings, then drivers. If a different cable and port on the same monitor work, the original cable was the problem."
  - q: "Can a Windows update break HDMI output?"
    a: "Yes, and it happens regularly. Display driver updates bundled with Windows Update can corrupt the GPU driver, break the HDMI handshake, or reset display topology settings. If HDMI died immediately after an update, rolling back the display driver in Device Manager or reinstalling the GPU driver from the manufacturer's site is the fastest fix."
  - q: "Does the HDMI cable quality matter?"
    a: "For 1080p it rarely does, but for 4K at 60Hz and above, cable quality matters a great deal. Cheap or very long cables fail the higher bandwidth handshake and produce no signal or flickering. If you are driving a 4K monitor, use a certified Premium High Speed cable under 2 meters before suspecting the laptop's port."
  - q: "Why does HDMI work on one monitor but not another?"
    a: "That points to an EDID or handshake issue with the specific monitor — the laptop and display fail to agree on resolution and timing. Try a different resolution and refresh rate in display settings, power-cycle the monitor, or update the monitor's firmware if the maker offers one. Some monitors also need a specific HDMI port for full bandwidth."
---

HDMI failures are maddening because the symptom is binary: either the second screen lights up or it shows "no signal" and nothing in between. The fault chain is long — cable, port, monitor input, display settings, GPU driver, firmware — and people usually guess at the expensive end first. In practice, well over half of dead-HDMI cases are the cable, the monitor's input selection, or the display mode Windows chose. This guide walks the chain from the cheap, physical end to the driver end so you replace a cable before you reinstall a GPU driver.

## Why this happens

- **Faulty or under-spec HDMI cable.** Broken conductors or a cable that can't handle 4K bandwidth.
- **Wrong input selected on the monitor/TV.** The display is listening on HDMI 2 while you're plugged into HDMI 1.
- **Incorrect display mode in Windows.** The output is disabled, or set to a resolution/refresh rate the monitor rejects.
- **Corrupted GPU driver after a Windows update.** The most common software cause — the HDMI handshake dies with the driver.
- **EDID handshake failure.** Laptop and monitor fail to agree on capabilities; common with adapters and KVM switches.
- **HDMI port power-saving or firmware bug.** Aggressive link power management shutting the port down.
- **Physically damaged HDMI port.** Loose or bent pins from repeated plugging, especially on thin ultrabooks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Rule out the cable and the monitor input

The physical layer first — it resolves most cases.

1. Unplug the HDMI cable at **both** ends and plug it back in firmly. HDMI connectors have no latch; they creep loose.
2. On the monitor or TV, open the input/source menu and select the **exact** HDMI port number you're plugged into.
3. Try a **different HDMI cable** — ideally a short, known-good one. Test the suspect cable on another device to confirm.
4. If you're using any adapter, dock, or KVM switch, remove it and connect the laptop directly to the display.
5. Inspect the laptop's HDMI port with a flashlight for bent pins or debris; blow it out gently.
6. Try a different HDMI port on the monitor itself — some monitors only enable full bandwidth on HDMI 1.

If the display still isn't detected at the Windows level, the broader detection walkthrough in [how to fix an external monitor not detected after a Windows 11 update](/articles/how-to-fix-external-monitor-not-detected-after-windows-11-update/) covers the OS side.

### Fix 2: Force Windows to detect the display

Sometimes the hardware is fine and Windows just isn't looking.

1. Press **Windows + P** and cycle through **Duplicate** and **Extend** — note whether the second screen option even appears.
2. Go to **Settings > System > Display**, scroll down, and click **Detect** next to "Multiple displays" (under Advanced display on some builds).
3. If the monitor appears but shows "no signal," lower the resolution to 1920×1080 and the refresh rate to 60Hz as a test — an over-ambitious mode can kill the handshake.
4. In **Advanced display settings**, check that Windows lists the correct monitor name, not "Generic PnP Monitor" with wrong capabilities.
5. Try **Win + Ctrl + Shift + B** to restart the graphics driver — the screen will blink; this often revives a stuck HDMI output instantly.

### Fix 3: Reinstall the GPU driver cleanly

The core software fix for handshake failures.

1. Open **Device Manager > Display adapters**, right-click your GPU (Intel, NVIDIA, or AMD), and choose **Uninstall device** — check "delete the driver software" if offered.
2. Restart. Windows will install a baseline driver; test HDMI before installing anything else.
3. For the real fix, download the driver from the source: NVIDIA users get it from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx), AMD users from the [AMD driver support page](https://www.amd.com/en/support/download/drivers.html), Intel users via Windows Update or their laptop maker's site.
4. During NVIDIA/AMD setup, choose **Custom > Clean installation** to wipe old profiles and corrupted settings.
5. If HDMI broke right after a Windows update, also check **Settings > Windows Update > Update history > Uninstall updates** for a display-driver update to roll back.
6. Laptops with dual GPUs (Intel + NVIDIA/AMD): update **both** drivers — the integrated GPU usually drives the HDMI port even when the discrete GPU renders.

The driver-first method generalizes well; see [how to fix the display driver stopped responding](/articles/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2/) for deeper GPU-driver repair.

### Fix 4: Fix the EDID handshake

When the cable is good and the driver is fresh but the monitor still won't sync.

1. Power the monitor fully off (unplug it for 30 seconds), then power it back on with the HDMI cable connected — this forces a fresh EDID handshake.
2. In the monitor's on-screen menu, disable any "HDMI deep sleep" or "auto input" features that interfere with detection.
3. Try each refresh rate Windows offers for that display (59/60/120Hz) — some panels only handshake at specific rates.
4. If you're on a TV, enable **HDMI UHD Deep Color / Enhanced format** on that specific port; without it, 4K signals fail.
5. As a test, boot with the HDMI cable already connected — cold-boot detection bypasses several hot-plug handshake bugs.
6. Check the monitor maker's site for a firmware update; panel firmware fixes for HDMI handshake issues are common.

### Fix 5: Check BIOS and firmware settings

Firmware-level routing problems are rare but real.

1. Enter BIOS/UEFI and look for display or graphics options — ensure the integrated GPU isn't disabled if your HDMI port is wired to it.
2. Update the BIOS from your laptop maker's support page; changelogs sometimes list HDMI/display output fixes.
3. If you use a USB-C to HDMI adapter instead of the built-in port, verify that USB-C port supports **DisplayPort alt-mode** — not all of them do, and the manual will say.
4. Disable **fast startup** (Control Panel > Power Options > Choose what the power buttons do) — it can leave the GPU in a bad state across reboots.
5. For dock users: update the dock's firmware from the dock maker's utility before blaming the laptop.

### Fix 6: Test the port hardware itself

When software is exhausted, verify the physical port.

1. Connect the laptop to a **different display** (any TV will do) with a known-good cable.
2. If no display works on the laptop's HDMI but the same cable+display works from another computer, the laptop's port is suspect.
3. Wiggle the connector gently while watching for flicker — intermittent signal means worn pins or a cracked solder joint.
4. Check whether the port works in BIOS/UEFI screens (connect the display and reboot into BIOS) — video in BIOS but not Windows is still a driver problem, not hardware.
5. A dead HDMI port on an out-of-warranty laptop is a board-level repair; a USB-C to HDMI adapter (on a DP alt-mode port) is a cheap workaround.

### Fix 7: Reset the display topology as a last resort

For stubborn cases where Windows remembers a broken configuration.

1. Disconnect all external displays and restart.
2. Delete the monitor's cached profile: **Device Manager > Monitors**, uninstall the external monitor entry, restart, reconnect.
3. Create a fresh Windows user profile temporarily — corrupted per-user display settings can block detection.
4. Run the **Hardware and Devices** troubleshooter via Terminal: `msdt.exe -id DeviceDiagnostic` (still present on most Windows 11 builds).
5. As a final step, an in-place Windows repair install (keeping files) rebuilds the display stack without wiping your data — documented on [Microsoft Support for Windows](https://support.microsoft.com/en-us/windows).

## Closing

HDMI troubleshooting is a chain, and the chain is only as strong as the cable — start physical, then make Windows look for the display, then reinstall the GPU driver cleanly, and only then suspect firmware or the port itself. The graphics-driver restart shortcut (Win + Ctrl + Shift + B) alone revives a surprising number of "dead" HDMI outputs in two seconds. Keep a known-good short HDMI cable in your bag; it is the fastest diagnostic tool you own, and it costs less than the coffee you'll drink while reinstalling drivers.
