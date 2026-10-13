---
title: "Night Light Not Working in Windows 11? Get It Back On"
slug: how-to-fix-night-light-not-working
date: 2026-09-10
categories: ["drivers"]
tags: ["night light", "display", "blue light filter", "windows 11"]
description: "Night Light stuck off or greyed out on your Windows 11 laptop? Here's how to fix the schedule, the registry key, and the driver behind it."
thumbnail: "/images/thumbs/how-to-fix-night-light-not-working.webp"
faqs:
  - q: "Why is Night Light greyed out in Windows 11 settings?"
    a: "A greyed-out Night Light toggle usually means the display driver isn't reporting color-temperature support, or a group/registry policy disabled it. Update your graphics driver first — this fixes most cases. If the toggle is still greyed out, check the registry key CloudStore entries under the defaultuser blob, which sometimes corrupt and freeze the toggle in place."
  - q: "Night Light turns on but the screen doesn't change color. Why?"
    a: "If the toggle flips but nothing visibly changes, the strength slider is probably set too low, or the graphics driver's color management is overriding Night Light. Push the strength slider to at least 50 and test. Also check your GPU control panel (Intel Graphics Command Center, NVIDIA Control Panel) for its own night/blue-light mode, which can conflict with Windows' version."
  - q: "Can a Windows update break Night Light?"
    a: "Yes — graphics driver updates delivered through Windows Update are the most common trigger. A new display driver can reset color profiles or break the communication channel Night Light uses to shift color temperature. Rolling the display driver back or reinstalling it from your laptop manufacturer's support page usually restores the feature."
  - q: "Does Night Light work on external monitors?"
    a: "It should, but behavior varies. Night Light applies per display, and some external monitors — especially those connected through certain docks or adapters — don't report the capabilities Windows needs. If Night Light works on the laptop screen but not the external monitor, try connecting the monitor directly rather than through a dock, and check for [second monitor detection issues](/articles/how-to-fix-laptop-not-detecting-second-monitor-after-windows-11-update/)."
---

Night Light is the kind of feature you don't think about until it stops working — then every evening at the laptop feels like staring into a headlight. The toggle flips but nothing changes, or it's greyed out entirely, or the schedule you set weeks ago simply never fires. Because Night Light depends on a chain of components (the Settings app, the graphics driver, and a scheduled task), the failure can sit at any link.

The fix sequence is: check the schedule and strength first, repair the Settings state, then fix the graphics driver underneath it. In my experience the driver is the culprit more often than the Settings UI admits — especially after a Windows Update swapped your display driver. If your screen has other odd behavior too, like flickering, work through our [screen flickering fixes](/articles/how-to-fix-screen-flickering-on-laptop-after-windows-11-update/) alongside this guide.

## Why this happens

- **Graphics driver updated or corrupted**: Night Light talks to the display through the GPU driver; a bad update breaks that channel silently.
- **Corrupted CloudStore registry blob**: Night Light's on/off and schedule state lives in a registry blob that can corrupt and freeze the toggle.
- **Strength slider set too low**: At very low strength the color shift is nearly invisible, which looks like "not working."
- **Conflicting GPU blue-light mode**: Intel, NVIDIA, or AMD control panels with their own night mode can fight Windows' Night Light.
- **Schedule misconfigured**: The "sunset to sunrise" option depends on location services; without location, the schedule never triggers.
- **Display color profile overriding**: A custom ICC color profile can override the color-temperature shift Night Light applies.
- **Group policy or registry lock**: Some managed or debloated systems have Night Light disabled by policy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the schedule and strength settings

Rule out the simple misconfiguration before touching drivers.

1. Open **Settings** > **System** > **Display** > **Night light** and confirm the main toggle is **On**.
2. Drag the **Strength** slider to 60–80 and watch the screen — the preview updates live, so you'll see immediately whether the shift works.
3. Click **Schedule night light** and verify the hours. If you use **Set hours** with a start time later than the end time (e.g., 22:00 to 06:00), that's fine — just make sure AM/PM is right.
4. If you use **Sunset to sunrise**, ensure **Location services** are on (**Settings** > **Privacy & security** > **Location**), because Windows needs your location to compute sunset.
5. Test with **Turn on now** — if the manual toggle works but the schedule doesn't, the problem is purely the schedule, not the feature.

### Fix 2: Reset Night Light's registry state

When the toggle is stuck or greyed out, its stored state is often corrupt.

1. Press **Win + R**, type `regedit`, and press Enter (approve the UAC prompt).
2. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Cloud`.
3. Find the subkeys starting with `default$windows.data.bluelightreduction.bluelightreductionstate` and `default$windows.data.bluelightreduction.settings` — right-click each and **Delete** them.
4. Close Registry Editor and restart the laptop.
5. Go back to **Settings** > **System** > **Display** > **Night light** — the toggle should be responsive again. Reconfigure your schedule from scratch.

### Fix 3: Update or reinstall the display driver

The most common real cause, especially after Windows Update.

1. Open **Device Manager** (**Win + X**), expand **Display adapters**, right-click your GPU, and choose **Update driver** > **Search automatically for drivers**.
2. If that doesn't help, right-click > **Uninstall device** (do NOT check delete driver software on the first pass), restart, and let Windows reinstall.
3. For a proper fix, get the driver from your laptop maker's support page instead of Windows Update — OEM display drivers are validated against your panel. See Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for driver troubleshooting guidance.
4. Install, restart, and test Night Light at 70+ strength.
5. If a recent update broke it, use **Roll Back Driver** on the Driver tab instead — see our [driver rollback guide](/articles/best-way-to-rollback-driver-update/) for the full procedure. It's the fastest path when the timeline matches an update.

### Fix 4: Disable conflicting GPU color features

Two night modes fighting looks exactly like one broken one.

1. Open your GPU control panel: **Intel Graphics Command Center**, **NVIDIA Control Panel**, or **AMD Software**, whichever matches your hardware.
2. Look for any blue-light filter, night mode, or "video color" enhancement and turn it **off**.
3. In Windows, go to **Settings** > **System** > **Display** > **Advanced display** and check the color profile — remove any custom ICC profile temporarily.
4. Also check for third-party apps like f.lux, which hook the same color-temperature APIs and can block Night Light entirely. Quit or uninstall them for testing.
5. Retest Night Light. If it now works, reintroduce third-party tools one at a time to find the conflict.

### Fix 5: Restart the related services and scheduled task

Night Light's schedule runs through Task Scheduler and display services.

1. Press **Win + R**, type `services.msc`, and restart the **Windows Location Provider** and **Sensor Service** if present.
2. Open **Task Scheduler** (`taskschd.msc`), navigate to **Microsoft** > **Windows** > **Display**, and check the Night Light-related tasks are **Enabled** and their last run result was success.
3. If a task shows errors, right-click > **Run** it manually and watch for the screen shift.
4. Run the display troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** — run anything display-related.
5. Restart once more and confirm the schedule fires at the configured time.

### Fix 6: Check for policy locks

For systems where the toggle is greyed out no matter what.

1. Press **Win + R**, type `gpedit.msc` (Pro editions) and check **Computer Configuration** > **Administrative Templates** for anything disabling Night Light or blue-light features.
2. On Home editions, check the registry at `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows` for Night Light-related keys and remove them if you (or a debloat script) added them.
3. If this is a work or school laptop, the policy may be managed — check with IT before changing it.
4. After clearing the policy, restart and retest.
5. If the toggle was greyed out due to policy, it should now respond normally.

### Fix 7: Repair Windows system files

The last resort for a feature that should "just work."

1. Open an elevated Command Prompt or Terminal (**Win + X** > **Terminal (Admin)**).
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to complete.
3. Then run `sfc /scannow` and restart when done.
4. Reconfigure Night Light from scratch after the repair.
5. If it still fails, consider an in-place upgrade using the [Windows 11 Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11), which repairs system components without touching your files.

## Closing

Night Light failures look like a Settings bug but are usually a driver or corrupted-state problem underneath — which is why reinstalling the display driver fixes more cases than any toggle-fiddling. Work the sequence once, set your schedule, and your evenings go back to warm instead of headlight-white.
