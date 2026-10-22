---
title: "How to Fix an NPU Power State Stuck in Sleep or Offline Mode"
slug: npu-power-state-stuck-fix
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu", "power-state", "windows-11", "device-manager", "ai-pc", "troubleshooting"]
description: "NPU stuck in a low-power or offline state on your AI PC? Learn why Windows cannot wake the neural processor and apply these safe fixes to bring it back online."
thumbnail: "/images/thumbs/npu-power-state-stuck-fix.webp"
faqs:
  - q: "Why does my NPU work after a full shutdown but not after sleep?"
    a: >
      Sleep and hibernate preserve device power states, so a stuck state
      survives them. A full shutdown forces every device to re-enumerate
      from scratch, which clears the wedge. This is why disabling Fast
      Startup, which hibernates the kernel instead of shutting down, is
      such an effective first fix.
  - q: "Can a power plan really disable my NPU?"
    a: >
      It cannot remove the device, but aggressive settings like PCIe
      link-state power management can park the NPU's bus link so deeply
      that workloads fail to wake it. The chip looks present in Device
      Manager while being unusable, which is exactly the stuck-state
      symptom this guide addresses.
  - q: "Is it safe to turn off PCIe link-state power management?"
    a: >
      Yes for testing, and generally safe long-term on a laptop that
      stays plugged in; it slightly increases idle power draw. If battery
      life matters to you, re-enable it after diagnosing and update your
      drivers and firmware instead, since those fix the underlying wake
      failure rather than working around it.
  - q: "How do I know the fix actually worked?"
    a: >
      Run a guaranteed NPU workload such as Studio Effects background
      blur and watch Task Manager's Performance tab. A healthy NPU shows
      activity spikes instead of staying flat or greyed out. Repeat the
      test after a sleep-wake cycle to confirm the fix survives standby.
---

You open Task Manager's Performance tab and your NPU entry is greyed out, frozen at zero, or stuck in a strange low-power state while the CPU handles AI work alone. The chip worked yesterday — background blur, live captions, all fine — and now Windows acts as though the neural processor has gone to sleep and refuses to wake up.

A stuck power state differs from a merely idle NPU: an idle chip wakes the instant work arrives, while a stuck one ignores the wake call entirely. If you have ruled out the idle case in our [NPU stuck at 0% usage guide](/articles/npu-stuck-at-zero-percent-usage/), the next suspect is power management — Windows, the BIOS, or the driver has parked the chip in a sleep state it cannot exit.

The good news is that a stuck power state is almost never a dead chip — usually just a confused power policy: Fast Startup resuming a stale sleep state, an aggressive plan pinning the NPU in deep idle, or a driver whose power handling broke during an update. These six fixes run in order, from a clean wake-up to a full policy reset, using the [live captions offline speech models](/articles/live-captions-offline-speech-models/) pipeline as a reliable test workload.

## Why this happens

- **Aggressive PCIe link-state power management:** The NPU sits on the PCIe bus, which Windows can drop into deep low-power states. If the link fails to renegotiate on wake, the chip stays reachable on paper but unusable in practice.
- **Fast Startup resume glitches:** Fast Startup hibernates the kernel instead of shutting down. If the NPU was in a low-power state at hibernate time, the resumed session can inherit a power state the hardware has already forgotten.
- **Modern Standby transitions:** Modern Standby laptops cycle the NPU through sleep many times daily. One firmware or driver bug in that handshake can leave the chip wedged.
- **Corrupt driver power policy:** The NPU driver's power policy lives partly in the registry. A failed or interrupted update can leave entries telling Windows to keep the chip parked indefinitely.
- **BIOS or embedded-controller power gating:** Some firmware gates NPU power aggressively on battery or under heat. If the embedded controller misreads a sensor, it may never release the gate even after conditions improve.
- **Chipset or ACPI driver mismatch:** The NPU relies on chipset and ACPI drivers to report its power capabilities. An outdated chipset driver can describe the wrong states, parking the chip where it cannot wake from.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the stuck state before changing anything

First, prove the NPU is genuinely stuck rather than merely idle. In Device Manager, check the neural processor's reported state — a stuck chip may show a power-related warning instead of "working properly." Then watch Task Manager's Performance tab during a guaranteed NPU workload. Unlike a transient spike from a heavy app — the kind covered in our [Copilot app high memory usage guide](/articles/copilot-app-high-memory-usage/) — a stuck chip's graph stays flat or greyed out no matter what you run.

1. Open Device Manager (press Win + X, then select Device Manager) and find the NPU under Neural processors or System devices.
2. Double-click it and check the Power Management tab, noting whether "Allow the computer to turn off this device to save power" is checked.
3. Open Task Manager (Ctrl + Shift + Esc), go to the Performance tab, and select NPU.
4. Start a known NPU workload like Studio Effects background blur and watch the graph for 30 seconds.
5. If the graph stays flat or greyed out, the power state is stuck — continue to Fix 2.

### Fix 2: Do a full shutdown to clear the Fast Startup state

Fast Startup is the most common reason a stuck power state survives a reboot — it hibernates the kernel instead of shutting down. You need a true cold boot to force every device, including the NPU, to re-enumerate its power states from scratch.

1. In Control Panel, go to Hardware and Sound > Power Options and click "Choose what the power buttons do."
2. Click "Change settings that are currently unavailable" and uncheck "Turn on fast startup," then save changes.
3. Shut down completely (not Restart), unplug the charger, and wait 60 seconds.
4. Plug back in, power on, and let Windows boot fully before opening anything.
5. Retest with a Studio Effects workload in Task Manager to check whether the NPU now wakes.

### Fix 3: Stop the power plan from parking the NPU

Next suspect: the power plan itself. PCIe link-state power management can park the NPU's bus link so deeply that workloads cannot wake it — a close cousin of the behavior in our [NPU throttling under load fix](/articles/npu-throttling-under-load-fix/) guide. Loosening these settings tells you whether policy, rather than hardware, is the jailer.

1. In Control Panel, go to Hardware and Sound > Power Options and click "Change plan settings" on your active plan.
2. Click "Change advanced power settings" to open the detailed dialog.
3. Expand "PCI Express," then "Link State Power Management," and set both On battery and Plugged in to Off.
4. Expand "USB settings," then "USB selective suspend setting," and set both entries to Disabled.
5. Click Apply, restart, and retest the NPU under load before moving on.

### Fix 4: Reinstall the NPU and chipset drivers cleanly

A driver with corrupt power-handling code can report a healthy device while mishandling every wake request. The fix is a true clean reinstall: remove the driver software entirely, then install a fresh package — ideally the laptop maker's — so the power policy is rebuilt from scratch.

1. Download the latest NPU and chipset drivers for your exact model from your maker's support site (or find the package via the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/)).
2. In Device Manager, right-click the NPU, choose Uninstall device, and check "Attempt to remove the driver for this device."
3. Restart the laptop and confirm Windows loads a basic driver or lists the device as unknown.
4. Install the NPU driver package first, then the chipset package, restarting when prompted.
5. Retest with an AI workload and confirm the NPU graph responds in Task Manager.

### Fix 5: Update BIOS, UEFI, and platform firmware

When drivers do not help, the wedge often lives one layer deeper — in firmware. BIOS and embedded-controller updates frequently fix Modern Standby transitions and power gating, the exact mechanisms that trap an NPU in a sleep state. This step takes longer but resolves cases software alone cannot.

1. Find your exact model and current BIOS version in System Information under BIOS Version/Date.
2. On your maker's support site, check for a newer BIOS with power or NPU-related fixes in its release notes.
3. On AC power with apps closed, run the BIOS update exactly as the maker instructs — never interrupt it.
4. After the update, enter BIOS setup, choose "Load optimized defaults," then save and exit.
5. Boot into Windows, retest the NPU, and recheck the power-state reading in Device Manager.

### Fix 6: Reset all power plans to their defaults

If a custom plan or tuning utility has buried a bad policy somewhere, wipe the slate: resetting restores Microsoft's tested defaults for every hidden power setting, including device idle and wake behavior. Microsoft documents these defaults and the powercfg tool on its [Windows support pages](https://support.microsoft.com/en-us/windows).

1. Open Terminal as administrator (press Win + X, then choose Terminal (Admin)).
2. Type `powercfg -restoredefaultschemes` and press Enter.
3. Restart the laptop so the defaults apply to all devices.
4. Open Task Manager and run your AI workload test one final time.
5. If the NPU now wakes normally, rebuild any custom plan one setting at a time so you can spot the culprit if it returns.

## Closing

A power state surviving all six fixes is rare and usually means a hardware-level fault — a failing embedded controller or damaged power rail — which is a warranty conversation, not a settings one. Otherwise the pattern is consistent: a true cold boot plus sane power policies wakes the chip, and a clean driver reinstall keeps it awake. Remember Fast Startup's behavior the next time the NPU looks dead after a restart, and you will diagnose it in minutes.
