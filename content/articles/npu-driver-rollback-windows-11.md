---
title: "How to Roll Back Your NPU Driver in Windows 11"
slug: npu-driver-rollback-windows-11
date: 2026-10-19
categories: ["ai-pc"]
tags: ["npu driver", "rollback", "device manager", "windows 11", "driver"]
description: "Need to roll back your NPU driver in Windows 11? Undo bad driver updates step by step and stop Windows from reinstalling the broken version."
thumbnail: "/images/thumbs/npu-driver-rollback-windows-11.webp"
faqs:
  - q: "When should I roll back an NPU driver?"
    a: "When AI features or NPU detection broke immediately after a driver update. If it worked yesterday and fails today with only a driver change in between, rollback is the fastest fix — far quicker than a full reinstall."
  - q: "Why is the Roll Back Driver button greyed out?"
    a: "Windows only keeps the previous driver when an update actually replaced one. Fresh installs, manual deletions, and some Windows Update pushes leave no previous version to return to — then a clean reinstall is the alternative."
  - q: "Will Windows just reinstall the bad driver again?"
    a: "It can, which is why rollback alone is half the job. Pause updates or hide the bad driver version after rolling back, or Windows Update may undo your fix within days."
  - q: "Is rollback safe for the NPU?"
    a: "Yes — it simply restores the previously working driver files. It does not touch firmware, BIOS, or your files. It is the lowest-risk driver fix available."
---

A driver update lands, and your NPU goes from working to broken overnight — AI features die, Device Manager shows warnings, or the chip vanishes entirely. Before you reach for the nuclear option of a full reinstall, try the undo button Windows keeps for exactly this situation: driver rollback. It takes two minutes and reverses only the driver, nothing else.

Rollback works when a newer driver replaced an older working one. If your problem started with a Windows Update, also read our guide on the [NPU disappearing after Windows Update](/articles/npu-disappeared-after-windows-update/) — and if the installer itself is the problem, see [Intel AI Boost driver installation failures](/articles/intel-ai-boost-driver-not-installing/).

## Why this happens (why rollback is needed)

- **Windows Update pushed a bad NPU driver:** The most common trigger — a mismatched or buggy driver replaces your working one.
- **OEM vs generic mismatch:** A generic Intel/AMD package overwrites a tuned OEM driver and breaks hardware-specific hooks.
- **Beta driver through optional updates:** Optional driver updates are less tested; NPU ones have caused real regressions.
- **Firmware skew introduced:** Sometimes the old driver was fine until a BIOS update changed what the NPU expects — rollback still helps diagnose.
- **Partial update corruption:** An interrupted driver update leaves a half-new, half-old state that behaves like a bad driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the built-in Roll Back Driver button

The two-minute fix. Try this first, always.

1. Open Device Manager (Win + X, Device Manager), expand Neural processors.
2. Right-click the NPU entry, choose Properties, then the Driver tab.
3. Click "Roll Back Driver." Pick a reason ("previous version worked better") and confirm.
4. Reboot when prompted — the old driver only fully loads after restart.
5. Test your AI features immediately; if they work, the new driver was the problem.

### Fix 2: Roll back via Device Manager history (alternative path)

If the button is greyed out in Properties, try the device-level route.

1. Right-click the NPU entry and choose "Uninstall device" — but do NOT tick "Attempt to remove the driver."
2. Without the tick, Windows keeps the driver files; reboot.
3. On boot, Windows redetects the hardware and typically reinstalls the previous driver version from its store.
4. Check the Driver tab — the version/date should now show the older build.
5. Verify AI features work again before proceeding.

### Fix 3: Stop Windows from reinstalling the bad driver

Rollback without blocking the update is a temporary win.

1. Settings, Windows Update — pause updates for 1-2 weeks to create breathing room.
2. For a permanent block on a specific bad version, use Microsoft's "Show or hide updates" troubleshooter to hide the NPU driver update.
3. Alternatively, in Device Manager, NPU Properties, Driver tab, "Update Driver" — choose "Browse my computer" and manually keep your known-good version selected.
4. Note the bad version number somewhere — when a *newer* fixed version appears, you will want to allow that one.
5. Unpause updates after you have installed a confirmed-good driver.

### Fix 4: Reinstall the known-good OEM driver manually

When no rollback target exists, recreate the "previous good state" by hand.

1. Download the last working driver version from your OEM's support archive ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) — support pages often keep older versions.
2. Disconnect from the internet, uninstall the current NPU driver (ticking "remove driver software").
3. Install the older OEM package, reboot, reconnect.
4. Confirm the driver version in Device Manager matches the intended older build.
5. This is functionally identical to a rollback — you have restored the last-known-good state.

### Fix 5: Verify the rollback actually stuck

Drivers sometimes look rolled back but are not.

1. After reboot, check Driver tab: version and date should match the older build, not the bad one.
2. Run `pnputil /enum-drivers` in admin Command Prompt and confirm no trace of the bad version's .inf remains.
3. Test across a second reboot — some bad drivers reinstall on boot via Windows Update.
4. If the bad version keeps returning, the hide-updates tool from Fix 3 is mandatory, not optional.
5. Once stable for a week, you can cautiously try the next driver release — regressions do get fixed.

## Closing

Driver rollback is the fastest recovery from a bad NPU update because it changes the least: same hardware, same firmware, just the previously working driver. Always try it before a full reinstall, and always pair it with blocking the bad version — otherwise Windows Update will happily break your NPU again next Tuesday. When rollback is not available, a manual reinstall of the older OEM package achieves the same result, and keeping that installer archived means you never scramble for it twice. If the bad version arrived as part of a failed update process rather than a working-but-wrong driver, our [Intel NPU update failure guide](/articles/intel-npu-driver-update-failed/) covers that adjacent scenario.
