---
title: "How to Fix NVIDIA Driver Crashing on Windows 10 (7 Proven Fixes)"
slug: how-to-fix-nvidia-driver-crashing-on-windows-10
date: 2026-09-08
categories: ["drivers"]
tags: ["nvidia driver crashing", "windows 10", "gpu driver fix", "display driver", "clean install nvidia"]
description: "NVIDIA driver keeps crashing on Windows 10? Learn the real causes — from corrupted installs to TDR timeouts — and apply seven technician-tested fixes including a proper DDU clean install."
thumbnail: "/images/thumbs/how-to-fix-nvidia-driver-crashing-on-windows-10.webp"
faqs:
  - q: "What does 'Display driver nvlddmkm stopped responding' mean?"
    a: "That message is Windows' Timeout Detection and Recovery (TDR) system reporting that the NVIDIA driver took longer than two seconds to respond, so Windows reset it to avoid a full freeze. It appears in Event Viewer as Event ID 4101. It does not automatically mean the GPU is dying — corrupted driver files, unstable overclocks, overheating, and power delivery problems all produce the identical message, which is why a clean driver reinstall is always the first diagnostic step."
  - q: "Should I install NVIDIA drivers from GeForce Experience or Windows Update?"
    a: "Install them from NVIDIA directly — either GeForce Experience or the manual download from nvidia.com. Drivers delivered through Windows Update are WHQL-certified but often older, and Windows Update has a habit of installing its version on top of a working NVIDIA install, which is a classic crash trigger. After installing your chosen driver, use Device Installation Settings or Group Policy to stop Windows Update from replacing it."
  - q: "Can a bad power supply cause NVIDIA driver crashes?"
    a: "Yes, and it is one of the most misdiagnosed causes. If the 12V rail sags under load or a single daisy-chained PCIe cable cannot deliver enough current, the GPU resets and Windows blames the driver. Symptoms that point to power: crashes only in demanding games, never on the desktop, and a system that is stable after underclocking. Use separate PCIe cables per connector and test with a known-good PSU before replacing the card."
  - q: "Is it safe to increase the TDR delay in the registry?"
    a: "Raising TdrDelay from 2 to 8 seconds is a widely used and safe adjustment — it only changes how long Windows waits before resetting an unresponsive GPU. It cannot damage hardware. If the GPU is genuinely hung, you simply wait a few seconds longer before the reset happens. Always create a System Restore point before editing the registry, and revert the values if the change makes no difference."
---

An NVIDIA driver crash on Windows 10 usually announces itself the same way every time: the screen flickers black for a second, the game or app freezes, and Event Viewer logs a 'Display driver nvlddmkm stopped responding' error — the infamous TDR (Timeout Detection and Recovery) event. Sometimes the system recovers; sometimes it blue-screens with VIDEO_TDR_FAILURE. Either way, the GPU was fine yesterday and something changed.

The most common trigger is a driver update — either from GeForce Experience or pushed silently through Windows Update — that conflicts with the existing install, an overclock, or a game profile. But crashes also come from the GPU losing power under load, overheating, or Windows' TDR watchdog firing too aggressively on a card that simply needed a few more milliseconds to finish a frame.

If the driver installer itself refuses to run, see our companion piece on [NVIDIA installer failures](/articles/how-to-fix-nvidia-installer-cannot-continue-in-windows-11-24h2/) first. And if you want the definitive reinstall method before anything else, jump straight to our [clean-install walkthrough](/articles/best-way-to-update-nvidia-drivers-clean-install/) — for most crashing drivers it is the single most effective fix.

## Why this happens

- **Corrupted driver installation** — Leftover files and registry entries from previous installs clash with the new driver, causing random TDR crashes under load.
- **Driver pushed by Windows Update** — Microsoft's WHQL driver can be older or less stable than NVIDIA's Game Ready driver, and it may install on top of a working setup.
- **Unstable overclock or aggressive fan curve** — Factory or user overclocks that were stable for months can become unstable as the card ages or as drivers change power behavior.
- **Insufficient or unstable power delivery** — A failing PSU rail, daisy-chained PCIe power cables, or a laptop power plan starving the GPU causes crashes that look like driver bugs.
- **Overheating GPU or clogged cooling** — Dust-choked fans or dried thermal paste push the card past its thermal limit, triggering protective driver resets.
- **TDR timeout set too aggressively** — Windows' two-second watchdog sometimes fires on heavy but legitimate workloads, especially with newer cards on older driver branches.
- **Conflicting software overlays** — Discord, GeForce Experience, MSI Afterburner overlays, and some antivirus hooks can destabilize the driver during mode switches.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a clean reinstall with Display Driver Uninstaller

Nine times out of ten, a crashing NVIDIA driver is fixed by completely removing every trace of the old install and starting fresh. DDU (Display Driver Uninstaller) does this far more thoroughly than the NVIDIA installer's own clean option.

1. Download DDU and the latest NVIDIA driver for your card from [NVIDIA's official driver page](https://www.nvidia.com/Download/index.aspx) — save both before continuing.
2. Disconnect from the internet so Windows Update cannot sneak a driver in mid-process.
3. Boot into Safe Mode (Settings > Update & Security > Recovery > Advanced startup > Restart now > Troubleshoot > Startup Settings).
4. Run DDU, select GPU / NVIDIA, and choose 'Clean and restart'.
5. After reboot, install the downloaded NVIDIA driver, choosing **Custom (Advanced)** and ticking **Perform a clean installation**.
6. Reconnect to the internet and test with the game or app that was crashing.

### Fix 2: Stop Windows Update from replacing your driver

Even after a clean install, Windows Update can overwrite your NVIDIA driver with its own version within days. Blocking driver updates through Windows Update keeps your chosen driver in place.

1. Press Win + R, type `sysdm.cpl`, and open the Hardware tab.
2. Click **Device Installation Settings** and select **No (your device might not work as expected)**.
3. Alternatively, open the Group Policy Editor (Win 10 Pro): Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update > enable **Do not include drivers with Windows Updates**.
4. Restart and confirm your NVIDIA driver version stays put after the next Patch Tuesday.

### Fix 3: Reset any overclock to stock

If you run MSI Afterburner, ASUS GPU Tweak, or a factory-overclocked card, return everything to reference clocks and retest. This isolates hardware instability from driver problems in minutes.

1. Open your overclocking utility and click the reset button to restore default clocks and voltage.
2. Disable any custom fan curve temporarily — set fans to Auto.
3. Close the utility completely so it does not reapply the profile at startup.
4. Run your crashing workload for at least 30 minutes. If crashes stop, your overclock was the cause, not the driver.

### Fix 4: Check GPU temperatures and power

Crashes that happen only after several minutes of gaming point at heat or power rather than software. A quick monitoring pass rules both out.

1. Install HWiNFO64 or use Task Manager's Performance tab to watch GPU temperature during load.
2. If the card exceeds 85°C, clean dust from fans and heatsinks with compressed air and verify all fans spin.
3. On desktops, use two separate PCIe power cables from the PSU instead of one daisy-chained cable.
4. On laptops, run the test plugged in with the Windows power plan set to **Best performance** — battery modes throttle and undervolt the GPU aggressively.

### Fix 5: Increase the TDR delay in the registry

When Event Viewer shows the driver recovering on its own (Event ID 4101), the watchdog may simply be impatient. Raising the TDR delay gives the GPU more time before Windows resets it.

1. Press Win + R, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a new DWORD (32-bit) named **TdrDelay** and set its value to `8` (decimal).
3. Create another DWORD named **TdrDdiDelay** and set it to `8` as well.
4. Restart the PC. If crashes persist unchanged, revert both values — the problem lies elsewhere.

### Fix 6: Disable conflicting overlays and background apps

Overlays inject code into the rendering pipeline and are a documented source of TDR crashes, especially during alt-tab or resolution changes.

1. In GeForce Experience, open Settings and turn off **In-Game Overlay**.
2. In Discord, disable the in-game overlay under User Settings > Game Overlay.
3. Close MSI Afterburner / RivaTuner or any FPS overlay, then retest.
4. If the system is stable, re-enable overlays one at a time to identify the culprit.

### Fix 7: Test with an older known-stable driver

Occasionally a brand-new Game Ready driver has a genuine regression for a specific card. Rolling back to a driver version that was stable for you is a legitimate fix, not a workaround.

1. Check NVIDIA's driver archive for a version you remember being stable — community forums for your card model are a good guide.
2. Use DDU in Safe Mode to remove the current driver (see Fix 1).
3. Install the older driver with the clean-install option ticked.
4. Pause GeForce Experience auto-updates until a newer fixed driver is confirmed stable by other users with your GPU.

## Closing

NVIDIA driver crashes on Windows 10 are rarely mysterious once you work methodically: clean out the old install, keep Windows Update from meddling, and rule out clocks, heat, and power before blaming the driver itself. The DDU clean reinstall in Fix 1 alone resolves the majority of cases, and the remaining fixes cover the hardware and watchdog edge cases that a reinstall cannot touch.
