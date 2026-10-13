---
title: "Can't Change Brightness on Windows 10? Fix the Display Brightness Controls"
slug: how-to-fix-display-brightness-not-working-on-windows-10
date: 2026-09-14
categories: ["drivers"]
tags: ["display brightness", "windows 10", "brightness keys", "display driver"]
description: "Brightness stuck on Windows 10? The slider, Fn keys, and adaptive settings all depend on the driver chain — rebuild it with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-display-brightness-not-working-on-windows-10.webp"
faqs:
  - q: "Why is there no brightness slider in Windows 10 Settings?"
    a: "The brightness slider only appears when Windows can reach the panel's backlight through the display and monitor drivers. If the monitor driver binding broke or the display driver cannot drive the backlight interface — common after updates — Windows hides the slider entirely. Reinstalling both drivers brings it back."
  - q: "Do brightness Fn keys need special software?"
    a: "Yes. The Fn-key brightness combinations are handled by the manufacturer's hotkey utility layered on top of the display driver. If the display driver is broken, the keys do nothing; if the hotkey utility is missing after an update, the keys do nothing even with a good driver. Both layers need to be healthy."
  - q: "Can TeamViewer or remote software affect brightness?"
    a: "It can appear that way. Remote desktop sessions install a mirror display driver that becomes the active display, and brightness controls target the (nonexistent) remote panel. If brightness broke after installing remote-access software, check Device Manager for mirror drivers and disable the remote session's display adapter."
  - q: "Will updating the BIOS fix brightness control?"
    a: "Sometimes. Panel backlight initialization is firmware-controlled, and vendors ship BIOS updates that fix brightness regressions after Windows updates. It is worth checking the manufacturer's support site for a BIOS update if driver fixes fail — flash it with the charger connected."
---

No slider in the Action Center. No slider in Settings. The **Fn** brightness keys are dead, and the screen is pinned at whatever brightness it had when things broke — too dim for daytime or searing at night. Windows 10 gives you no error; the controls simply are not there.

Brightness control on Windows 10 depends on a driver chain: the display (graphics) driver drives the backlight interface, the monitor driver exposes the panel, and the hotkey utility handles the Fn keys. Updates break links in this chain routinely, and when the chain breaks, Windows quietly removes the controls instead of showing an error. Rebuild the chain and the controls return. (Windows 11 users should see our [Windows 11 brightness guide](/articles/how-to-fix-display-brightness-not-working-on-windows-11/) for the newer menus.)

## Why this happens

- **Display driver broken by an update.** The new graphics driver cannot drive the panel's backlight interface.
- **Monitor driver binding corrupted.** Windows lost the link between the OS and the panel driver.
- **Hotkey utility removed.** The manufacturer's Fn-key software was uninstalled or broken by the update.
- **Remote desktop mirror driver active.** A remote session's virtual display became the target of brightness commands.
- **Power plan values corrupted.** The per-plan brightness settings are stuck or unreadable.
- **Adaptive brightness overriding manual control.** The sensor-driven adjustment fights the slider.
- **Generic PnP monitor misidentified.** Windows bound the wrong monitor profile without backlight support.
- **BIOS backlight initialization changed.** A firmware update altered how the panel exposes brightness control.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reinstall the monitor driver

Open **Device Manager**, expand **Monitors**, right-click your display (likely **Generic PnP Monitor**), and choose **Uninstall device**. Restart — Windows redetects the panel and reinstalls the monitor driver during boot. Check **Settings > System > Display** for the brightness slider afterward. This fixes the missing-slider symptom directly, because the slider only renders when the monitor driver binding is healthy. If the slider appears but still does nothing, the display adapter driver is the broken link — continue.

### Fix 2: Reinstall the display adapter driver

In Device Manager, expand **Display adapters**, right-click your graphics device, and choose **Uninstall device** (do not delete the driver software unless you have the installer ready). Restart and test. If Device Manager shows the adapter with a warning icon, this reinstall is very likely the fix. For the thorough version, download the graphics driver from your laptop maker's site — [Lenovo support](https://support.lenovo.com/us/en/), [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en) — or from Intel, NVIDIA, or AMD, and install it clean. Vendor packages include the hotkey software the Fn keys need.

### Fix 3: Check for remote display drivers

If brightness broke after installing TeamViewer, AnyDesk, or similar, open Device Manager, expand **Display adapters**, and look for mirror or virtual display entries. Right-click any remote-session adapter and **Disable device** while testing. These virtual adapters hijack the display target that brightness commands address. You do not need to uninstall the remote software permanently — just confirm whether disabling its display driver restores the slider, which tells you exactly where the conflict lives.

### Fix 4: Turn off adaptive brightness

Go to **Settings > System > Display** and uncheck **Change brightness automatically when lighting changes**. Then open **Control Panel > Power Options > Change plan settings > Change advanced power settings**, expand **Display**, and set **Enable adaptive brightness** to **Off** for both battery and plugged-in. Adaptive brightness can pin or fight the manual control, making the slider feel dead. Set the **Display brightness** percentages in the same dialog to known-good values. Apply and retest the full slider range.

### Fix 5: Reinstall the manufacturer's hotkey software

The **Fn** brightness keys need the vendor utility: Lenovo Hotkeys, Dell QuickSet, HP Hotkey Support, or the ASUS ATK Package. Check **Settings > Apps > Apps & features** — if it is gone, download it from the manufacturer's support site for your exact model and install it. Restart and test the Fn combinations. Working slider plus dead Fn keys is the signature of a missing hotkey utility; dead slider plus dead keys points at the display driver instead. Fix the layer that matches your symptom.

### Fix 6: Repair the power plan

A corrupted power plan can hide or break brightness controls. In the advanced power settings dialog from Fix 4, click **Restore plan defaults** for your active plan. If the Display section is missing from advanced settings entirely, the plan is damaged beyond repair — switch to the **Balanced** plan or create a new custom plan. After restoring defaults, retest. Plan corruption is uncommon but real, and it produces the confusing symptom of brightness controls that exist but do nothing.

### Fix 7: Update the BIOS and verify in a clean boot

Check the manufacturer's support site for a **BIOS update** and flash it with the charger connected — firmware controls panel backlight initialization. Then perform a clean boot (**msconfig**, hide Microsoft services, disable the rest, restart) to rule out third-party software seizing the display stack. If brightness works in a clean boot, re-enable services in halves to find the culprit. If the slider is dead in every scenario including Safe Mode, but the screen itself is fine, an in-place Windows 10 repair install rebuilds the display stack as the final software step before suspecting panel hardware.

## Closing

Windows 10 brightness failures are chain failures: monitor driver, display driver, hotkey software. Work the chain in order and the controls come back — usually at the monitor driver reinstall or the graphics driver reinstall. If a second monitor is also misbehaving, our [second monitor flickering guide](/articles/how-to-fix-second-monitor-flickering-in-windows-11-24h2/) covers external display issues — and once the controls are back, avoid letting Windows Update silently replace the graphics driver again, since unattended driver swaps are the most common way this problem returns. When in doubt, the vendor's driver package beats anything Windows Update offers for display hardware.
