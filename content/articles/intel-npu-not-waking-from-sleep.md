---
title: "Intel NPU Not Waking From Sleep: Fix AI Boost Resume Failures on Windows 11"
slug: intel-npu-not-waking-from-sleep
date: 2026-10-22
categories: ["ai-pc"]
tags: ["intel-npu","sleep","power-management","ai-boost","windows-11","troubleshooting"]
description: "Intel AI Boost NPU not waking from sleep? Fix the resume failure that kills Studio Effects, Recall, and Copilot+ features every time your laptop wakes up."
thumbnail: "/images/thumbs/intel-npu-not-waking-from-sleep.webp"
faqs:
  - q: "Why does my Intel NPU stop working after sleep?"
    a: >
      The NPU's power-management handshake can fail during resume: the
      device enters a low-power state at sleep, then does not reinitialize
      correctly on wake. Outdated drivers, aggressive USB selective suspend
      settings, and Modern Standby transitions are the usual triggers.
  - q: "Does disabling sleep fix the NPU wake problem?"
    a: >
      Setting the laptop to hibernate or shut down instead of sleep avoids
      the broken resume path, but it is a workaround, not a fix. Updating
      the Intel NPU driver and chipset drivers usually resolves the
      underlying resume failure so normal sleep works again.
  - q: "How do I check if the NPU woke up correctly?"
    a: >
      Open Device Manager after waking the laptop and look at the Intel AI
      Boost NPU entry. If it shows a warning or the device is missing, the
      resume failed. Task Manager's Performance tab should also list the
      NPU when it is awake and healthy.
  - q: "Can a BIOS update fix NPU sleep issues?"
    a: >
      Yes. Several laptop makers have released BIOS updates that fix ACPI
      power-state transitions for the NPU. If driver updates do not help,
      check your manufacturer's support page for a newer BIOS that mentions
      sleep, resume, or AI Boost fixes.
---

Everything works perfectly until you close the lid. When the laptop wakes up, the webcam background blur is gone, Recall has stopped capturing, and Device Manager shows the Intel AI Boost NPU with a warning — or the device has vanished entirely. The Intel NPU entered sleep with the rest of the system but never woke back up. This is one of the most annoying AI PC issues because it punishes the most natural habit in the world: letting your laptop sleep.

The root of the problem is power management. Modern Standby sleep puts devices into deep low-power states, and each device must negotiate its way back up through a sequence of ACPI power states on wake. If the NPU driver, the chipset driver, or the BIOS firmware disagrees about that sequence, the NPU stays dark. Related [Copilot+ PC sleep and wake problems](/articles/copilot-plus-pc-sleep-wake-problems/) cover the general case, but the Intel NPU has its own specific resume path that needs attention.

There is also a knock-on effect worth knowing: when the NPU fails to resume, features built on it degrade silently. You might open a video call and find [Studio Effects missing in Discord](/articles/studio-effects-discord-calls/), or notice [Click to Do's Copy as table option is gone](/articles/click-to-do-copy-as-table/) because the local model pipeline never came back online. Fix the NPU resume, and these features usually recover without any extra steps.

## Why this happens

- **Stale Intel NPU driver:** Older AI Boost drivers mishandle the D3-to-D0 power transition on wake, leaving the NPU in a hung low-power state.
- **Outdated chipset drivers:** The platform controller hub manages the NPU's power rails; mismatched chipset drivers break the resume sequencing.
- **Modern Standby transitions:** S0 low-power idle sleep cycles devices aggressively, and buggy firmware can lose the NPU across a transition.
- **USB selective suspend interference:** The NPU shares power domains with USB-attached components on some designs, and selective suspend can starve its wake signal.
- **Fast Startup hybrid state:** Fast Startup saves a kernel hibernation image that can preserve a broken NPU device state across "shutdowns".
- **BIOS ACPI bugs:** Incorrect _PR3 or power-resource tables in the BIOS cause the OS to sequence the NPU's power-up incorrectly.
- **Driver conflict after update:** A Windows Update can replace a working Intel NPU driver with an older inbox version that has the resume bug.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Confirm the failure and restart the driver

First, verify the NPU is actually the problem and not just a missing feature. A precise diagnosis saves you from reinstalling things that were never broken.

1. After a sleep-wake cycle, open Device Manager and check the Intel AI Boost NPU entry under "Neural processors".
2. If it shows a warning, right-click it and choose "Disable device", wait five seconds, then choose "Enable device".
3. Open Task Manager > Performance and check whether the NPU tile appears and shows activity.
4. Test an NPU feature like Studio Effects background blur in the Camera app.
5. If disabling and re-enabling restores the NPU, the hardware is fine — continue with the driver and power fixes below.

### Fix 2: Update the Intel NPU driver

The resume bug was fixed in later Intel AI Boost driver releases, so updating is the single most effective step. Grab the newest driver from Intel or your laptop maker.

1. Check your current driver version in Device Manager > NPU Properties > Driver tab.
2. Visit [Intel's driver detection page](https://www.intel.com/content/www/us/en/support/detect.html) or your laptop maker's support site for the latest AI Boost / NPU driver.
3. Download and install it, choosing a clean install if the installer offers one.
4. Restart the laptop, then put it to sleep for a full minute and wake it to test.
5. Confirm the NPU survives three consecutive sleep-wake cycles before calling this fixed.

### Fix 3: Update chipset and BIOS firmware

The NPU does not manage its own power — the chipset and BIOS do. If the driver is current but resume still fails, the platform firmware is the next suspect.

1. On your laptop maker's support page, download the latest chipset driver package for your exact model.
2. Check the BIOS/UEFI section for any update mentioning sleep, resume, Modern Standby, or AI Boost.
3. Install the chipset drivers first, restart, then install the BIOS update following the maker's instructions exactly (keep the charger plugged in).
4. After the BIOS update, enter BIOS setup once and load optimized defaults if the maker recommends it.
5. Test sleep-wake again and verify the NPU appears in Device Manager every time.

### Fix 4: Adjust Windows power settings

Aggressive power saving can cut the NPU's wake path. Loosening the relevant settings often resolves resume failures without any driver changes.

1. Open Settings > System > Power & battery and set the power mode to "Best performance" temporarily for testing.
2. Open Control Panel > Power Options > Change plan settings > Change advanced power settings.
3. Expand "USB settings" > "USB selective suspend setting" and set it to Disabled for both battery and plugged in.
4. Expand "PCI Express" > "Link State Power Management" and set it to Moderate or Off.
5. Put the laptop to sleep, wake it, and check whether the NPU resumes; you can tighten settings again later once the driver situation is stable.

### Fix 5: Disable Fast Startup

Fast Startup's hybrid shutdown can carry a broken NPU device state from one boot to the next, making the problem look permanent when it is really one bad resume being replayed.

1. Open Control Panel > Power Options and click "Choose what the power buttons do".
2. Click "Change settings that are currently unavailable" to unlock the shutdown options.
3. Uncheck "Turn on fast startup (recommended)" and click Save changes.
4. Shut the laptop down fully, wait ten seconds, then power it on fresh.
5. Test sleep-wake cycles again; many users find the NPU resumes reliably once the hybrid state is gone.

### Fix 6: Block driver downgrades after a working install

If a good driver fixes resume but Windows Update later replaces it with an older buggy one, the problem returns mysteriously. Pin the working driver in place.

1. Once the NPU survives sleep reliably, note the exact driver version in Device Manager.
2. Open Settings > Windows Update > Advanced options and turn off "Receive updates for other Microsoft products" temporarily, or pause updates briefly.
3. Alternatively, use the Group Policy "Do not include drivers with Windows Updates" (Pro editions) or the device installation restrictions policy.
4. After a Windows Update runs, recheck the NPU driver version to confirm it was not replaced.
5. If sleep issues are similar on other AI hardware, our guide on [Intel NPU driver updates getting stuck](/articles/intel-npu-driver-update-stuck/) covers the update-side failures.

## Closing

An Intel NPU that will not wake from sleep is a power-management sequencing failure, not dying hardware: update the AI Boost driver, then the chipset and BIOS, then calm down the power settings that interfere with resume. Most laptops are fixed by Fix 2 alone, and the rest by the firmware updates in Fix 3. Once the NPU resumes reliably, dependent features like [Studio Effects in Discord calls](/articles/studio-effects-discord-calls/) and [Click to Do's Copy as table](/articles/click-to-do-copy-as-table/) come back to life on their own. If nothing here helps, check your maker's forums for a model-specific BIOS beta — sleep-resume NPU bugs are exactly the kind of thing those fix.
