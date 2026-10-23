---
title: "Diagnosing NPU Errors with Event Viewer on Windows 11"
slug: event-viewer-npu-errors-windows-11
date: 2026-10-23
categories: ["ai-pc"]
tags: ["event viewer", "npu errors", "diagnostics", "windows 11", "ai pc", "troubleshooting"]
description: "Diagnose NPU errors using Event Viewer on Windows 11: find the right logs, decode error codes, and trace failures to drivers or apps step by step."
thumbnail: "/images/thumbs/event-viewer-npu-errors-windows-11.webp"
faqs:
  - q: "Where do NPU errors appear in Event Viewer?"
    a: "Check Windows Logs > System for driver events (source names vary: the NPU driver, PCI, or Kernel-PnP), Windows Logs > Application for app-level AI failures, and Applications and Services Logs > Microsoft > Windows for component-specific logs like DriverFrameworks-UserMode."
  - q: "What does 'device not started' mean for an NPU?"
    a: "It means Windows tried to start the NPU device and the driver failed — usually a driver/firmware mismatch, a corrupted driver, or a resource conflict. The Details tab often names the failing component."
  - q: "Are occasional NPU warnings normal?"
    a: "Yes — isolated warnings during boot or driver updates are common and harmless. Worry when errors repeat in a pattern, correlate with AI features failing, or appear as red Error events rather than yellow Warnings."
  - q: "Can Event Viewer tell me which app crashed the NPU?"
    a: "Often yes. Match timestamps: find the NPU driver error in System log, then check the Application log at the same time for the app that was active. The pair usually identifies the trigger."
---

When AI features fail on your laptop — Studio Effects error out, Recall stops, an app reports the NPU unavailable — guessing wastes time. Event Viewer holds the actual record: which component failed, when, and often why. Learning to read its NPU-related entries turns "the AI stuff is broken" into a precise diagnosis.

This guide is a diagnostic walkthrough, not a single fix: where to look, what the entries mean, how to correlate them with symptoms, and which repairs each pattern points to. Work through it in order the next time the NPU misbehaves.

## Why this happens

- **NPU failures are silent at the UI level:** Apps report "NPU unavailable" with no detail. The real error — driver timeout, failed start, resource conflict — is only logged in Event Viewer.
- **Multiple components log separately:** The NPU driver, the PCI bus, Plug-and-Play manager, and the app each log their own view of the same failure in different logs. You need all of them for the full picture.
- **Driver events use cryptic sources:** NPU driver events appear under vendor-specific source names (Intel, AMD, Qualcomm driver names) that don't say "NPU" — you have to know what to filter for.
- **Errors cascade:** One root failure (driver failed to start) generates a dozen downstream events (apps failing, services erroring). Reading newest-first misleads; reading chronologically reveals the root.
- **Transient vs. persistent patterns differ:** A single error at boot after an update is noise; the same error every 10 minutes is a real fault. The log's pattern matters more than any single entry.
- **Correlated app crashes hide the trigger:** An app that hammers the NPU can cause driver timeouts logged as driver errors — blaming the driver when the app is the trigger, the same misattribution behind [Unity editor issues](/articles/unity-editor-arm-windows-issues/).
- **Firmware events look like driver events:** NPU firmware failures surface through the driver, so a firmware problem reads as a driver error until you check versions and pair them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Open the right logs and filter for NPU events

Event Viewer is a firehose — filtering is the skill. Start with the System log and narrow to the relevant sources and time window.

1. Press **Win + R**, type `eventvwr.msc`, and open **Windows Logs > System**.
2. Click **Filter Current Log** and set the time range to when the problem occurred (Last hour, or a Custom range covering the failure).
3. Check **Error** and **Warning** levels, and in the **Event sources** dropdown look for your NPU driver's source name, plus **Kernel-PnP**, **PCI**, and **DriverFrameworks-UserMode**.
4. Sort by **Date and Time** ascending (oldest first) within the window — the first error in a cascade is usually the root cause; everything after is fallout.
5. Double-click the earliest NPU-related error and read the **General** tab text fully before moving on — it often names the failing file or operation directly.

### Fix 2: Decode the common NPU error patterns

Most NPU log entries fall into a handful of patterns, each pointing at a different repair. Learn to recognize them.

1. **"Device not started" / Error 10:** The driver failed to initialize the NPU — points to driver/firmware mismatch or corruption. Repair: clean-reinstall the OEM NPU/chipset driver.
2. **Driver timeout / TDR-style resets:** The NPU stopped responding and Windows reset it — points to driver bugs, overheating, or an app hammering the accelerator. Repair: update the driver; check thermals; identify the app by timestamp correlation.
3. **"Device not migrated" after an update:** Windows failed to carry the driver across a Windows update — points to update damage. Repair: reinstall the OEM driver package.
4. **Repeated PnP re-enumeration:** The NPU keeps disappearing and reappearing — points to power management cutting the device or a loose firmware state. Repair: disable power management on the NPU in Device Manager; update BIOS.
5. **Side-by-side with app errors:** NPU driver errors timestamp-matched with one app's crash in the Application log — the app is the trigger. Repair: update or reconfigure that app rather than the driver.

### Fix 3: Correlate System and Application logs by timestamp

The System log shows the driver failing; the Application log shows what the user was doing. Together they name the trigger.

1. Note the exact timestamp of the first NPU error in the System log (down to the second).
2. Switch to **Windows Logs > Application**, filter to the same time window, and look for Error events within a minute of the NPU error.
3. If an app crash or hang appears at the same timestamp, that app triggered the NPU failure — update it, change its AI/acceleration settings, or test with its hardware acceleration disabled.
4. Check **Applications and Services Logs > Microsoft > Windows > DriverFrameworks-UserMode > Operational** for user-mode driver failures that bridge the two logs.
5. Document the correlation (app name, NPU error text, timestamp) — if you end up contacting support, this is exactly what they need. The same timestamp discipline helps with [facial recognition failures](/articles/windows-hello-face-not-working-ai-pc/), where camera-driver and app-log correlation identifies the break.

### Fix 4: Check driver and firmware versions against the errors

Log entries gain meaning when paired with version data — a "not started" error on a brand-new driver suggests a bad update; on a two-year-old driver suggests rot.

1. In **Device Manager**, open the NPU device's **Properties > Driver** tab and record provider, date, and version.
2. Open the error's **Details** tab in Event Viewer (Friendly View) and look for version or file references — compare against the installed driver.
3. Check your maker's support page for the current NPU/chipset driver and any NPU **firmware** updates for your model.
4. If the installed driver is older than the available one and errors are persistent, update — the log pattern plus the version gap is a confident diagnosis.
5. If the driver is current and errors persist, suspect firmware: install any pending platform/NPU firmware update, then reinstall the driver (firmware updates can change what the driver must match).

### Fix 5: Create a custom view for ongoing NPU monitoring

If the problem is intermittent, a one-time log dive is not enough — set up a persistent filtered view and check it after each failure.

1. In Event Viewer, right-click **Custom Views**, choose **Create Custom View**, and filter **Windows Logs > System** (and Application) for Error/Warning from your NPU driver sources plus Kernel-PnP and DriverFrameworks-UserMode.
2. Name it "NPU diagnostics" and save — it now shows only relevant events across reboots.
3. The next time an AI feature fails, open the custom view immediately and read the newest entries — fresh evidence beats memory.
4. Look for patterns across days: same time of day (scheduled task trigger?), after sleep (power management?), or after updates (driver churn?).
5. Export the view (**Action > Export Custom View**) if you need to share logs with support — filtered evidence gets faster answers than "it's broken sometimes."

### Fix 6: Act on the diagnosis — the repairs each pattern needs

Diagnosis without repair is trivia. Match your log pattern to the fix and verify the errors stop.

1. **Driver mismatch/corruption pattern** → clean-reinstall the OEM NPU/chipset driver (uninstall with driver removal, reinstall, restart), then block bad Windows Update drivers.
2. **Power management pattern** (errors after sleep) → in Device Manager, disable **"Allow the computer to turn off this device to save power"** on the NPU and related controllers.
3. **App-trigger pattern** → update the triggering app, disable its NPU/hardware acceleration, or reinstall it; confirm the errors stop when the app is not running.
4. **Firmware pattern** → install the platform/NPU firmware update from the OEM, then reinstall the driver to match.
5. **No clear pattern / errors persist through all repairs** → run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` for system corruption, and consider that the symptom may live in a different subsystem — [external webcam conflicts](/articles/studio-effects-external-webcam-issues/) with Studio Effects, for example, log as camera errors, not NPU errors. Scope the investigation to what the logs actually say.

## Closing

Event Viewer turns NPU failures from mysteries into work orders: filter the System log to the failure window, read the earliest error first, correlate with the Application log, pair entries with driver/firmware versions, and match the pattern to the repair. The logs always knew what was wrong — this guide just teaches you to ask them.
