---
title: "Windows 11 Black Screen After an Update? Fix It With These Steps"
slug: windows-11-black-screen-after-update-fix
date: 2026-09-15
categories: ["windows-errors"]
tags: ["windows-11", "black-screen", "update-issues"]
description: "Black screen after a Windows 11 update is usually a display driver or failed update problem. These steps bring your screen back."
thumbnail: "/images/thumbs/windows-11-black-screen-after-update-fix.webp"
faqs:
  - q: "Why is my screen black after updating Windows 11?"
    a: "The update most likely installed a graphics driver that doesn't work with your laptop, or the update itself failed partway through. Less often, an external display setting or a corrupted user profile is responsible. The fixes below walk through each cause in the order techs actually check them."
  - q: "My laptop turns on but the screen stays black. Is it dead?"
    a: "Probably not. If you hear fans or see keyboard backlighting, the laptop is running — it's just not displaying anything. Try the Win + Ctrl + Shift + B graphics reset shortcut first; if the screen flashes back to life, it was purely a display driver hiccup."
  - q: "How do I fix it if I can't see anything at all?"
    a: "Force the recovery environment by interrupting the boot three times (hold the power button at the logo screen). From there you can boot into Safe Mode, run Startup Repair, or roll back the update — all without needing a working display in normal Windows."
  - q: "Should I uninstall the update that caused it?"
    a: "If the black screen started immediately after a specific update, yes — uninstall it as a diagnostic step. You can always reinstall it later once the display driver is updated. The instructions are in Fix 5 below."
---
You updated Windows 11, restarted, and now… nothing. The laptop powers on — you can hear the fan, maybe the keyboard lights up — but the screen stays black. This is one of the most common post-update problems on laptops, and it's almost never a dead machine.

Nine times out of ten, the update replaced your graphics driver with one that doesn't work, or the update itself failed halfway through and left the display stack in a broken state. Here's how to get your screen back, in the order a technician would actually try things.

## Why this happens

- **The update installed a bad graphics driver.** Windows Update sometimes pushes a display driver that conflicts with your laptop's GPU or its switchable-graphics setup.
- **The update failed partway through.** An interrupted or corrupted update can leave Windows in a state where the display subsystem never initializes.
- **Display output got routed to the wrong screen.** Laptops with external monitors sometimes wake up sending video to a display that isn't there.
- **A corrupted user profile or shell.** If Windows loads but Explorer can't start, you get a black screen with a cursor — technically booted, but unusable.
- **Fast Startup loaded a broken driver state.** The hybrid shutdown can preserve the exact broken graphics state the update created.
- **BIOS or firmware mismatch.** A major Windows build update can clash with old firmware that handles display initialization.

## How to fix it

Work through these in order, from the quickest and safest fixes to the deeper ones. Stop once your screen is back.

### Fix 1: Try the graphics driver reset shortcut

This takes five seconds and fixes a surprising number of black screens.

1. Press **Win + Ctrl + Shift + B** all at once.
2. You should hear a beep and see the screen flicker as Windows restarts the graphics driver.
3. If your display comes back, the problem was a hung graphics driver — but still continue to Fix 2, because the bad driver that caused it is probably still installed.
4. Also try **Win + P**, then press the **Down arrow** and **Enter** — this cycles display modes and can recover a laptop that's outputting to a phantom external monitor.

### Fix 2: Boot into Safe Mode and roll back the display driver

Safe Mode loads a basic display driver, which bypasses the broken one.

1. Force the laptop off, power on, and hold the power button at the logo screen to interrupt the boot. Do this **three times** to reach the **Windows Recovery Environment**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode. Our full [Safe Mode boot guide](/articles/how-to-boot-windows-11-in-safe-mode/) covers every method if this one gives you trouble.
3. Once in Safe Mode, press **Win + X** and open **Device Manager**.
4. Expand **Display adapters**, right-click your GPU, and choose **Properties > Driver tab > Roll Back Driver**. If the button is greyed out, choose **Uninstall device** instead and check **Attempt to remove the driver for this device**.
5. Restart normally. Windows will fall back to a basic driver, and your screen should work.

### Fix 3: Install the correct graphics driver from the manufacturer

The generic driver got you a picture; now get the right one.

1. In normal Windows (or Safe Mode with Networking), visit your laptop maker's support site — [Dell](https://www.dell.com/support), HP, or Lenovo — and download the graphics driver for your exact model.
2. If you have an NVIDIA GPU, you can also get it directly from [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx).
3. Install the driver and restart. Then go to **Settings > Windows Update > Advanced options > Optional updates** and uncheck any display driver Windows offers there, so it doesn't overwrite your working driver again.

### Fix 4: Run Startup Repair

If Safe Mode doesn't even work, let the recovery environment fix the boot.

1. Boot into the **Windows Recovery Environment** using the three-interrupt method from Fix 2.
2. Go to **Troubleshoot > Advanced options > Startup Repair**.
3. Let it diagnose and repair automatically. This fixes corrupted boot and display-initialization components. See [how to use Startup Repair](/articles/how-can-i-use-startup-repair-windows-11/) for what to do if it reports it couldn't fix the problem.

### Fix 5: Uninstall the problematic update

If the black screen started immediately after a specific update, remove it.

1. In the recovery environment, go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall the latest quality update** first — this is the most common culprit and the safest to remove.
3. If that doesn't help, you can also try **Uninstall the latest feature update**, though this takes longer and rolls back more.
4. Restart and check. If the screen works, pause updates for a week via **Settings > Windows Update > Pause updates** to give Microsoft time to fix the bad update.

### Fix 6: Repair system files from the recovery command prompt

Corrupted files from a failed update can keep the display stack from loading.

1. In the recovery environment, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` — the offline flags let it scan the installed Windows from recovery.
3. Then run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Type `exit`, choose **Continue** to boot Windows, and check your display.

### Fix 7: Reset Windows while keeping your files

The last resort when nothing else restores the display.

1. In the recovery environment, go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files**, then **Cloud download** for the cleanest reinstall.
3. After setup completes, install the manufacturer's graphics driver first (Fix 3) before letting Windows Update run. If even this doesn't bring the screen back, you're likely looking at a hardware display failure — time for a repair shop. Microsoft's [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) also offers a clean installation media option if you prefer a full wipe.

## Closing

A black screen after a Windows 11 update feels catastrophic, but it's a driver or update problem in the overwhelming majority of cases — not a dead laptop. The graphics reset shortcut, a Safe Mode driver rollback, and uninstalling the offending update resolve it for most people. And once you're back up, installing the manufacturer's graphics driver and blocking Windows from overwriting it is what keeps the black screen from coming back with the next update.
