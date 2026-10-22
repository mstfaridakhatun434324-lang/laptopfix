---
title: "How to Check Your NPU Firmware Version in Windows 11 (Step by Step)"
slug: check-npu-firmware-version-windows
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu","firmware-version","windows-11","device-manager","ai-pc","troubleshooting"]
description: "Learn how to check your NPU firmware version in Windows 11 with Device Manager, vendor tools, and Windows Update history. Confirm your AI chip is current."
thumbnail: "/images/thumbs/check-npu-firmware-version-windows.webp"
faqs:
  - q: "Is the NPU firmware version the same as the driver version?"
    a: >
      No. The driver is the software Windows uses to talk to the NPU, while the
      firmware runs on the chip itself. Vendors usually bundle them in one
      package, so the numbers move together, but they are separate layers and a
      driver update does not always change the firmware build.
  - q: "Where is the NPU listed in Device Manager?"
    a: >
      Open Device Manager and expand the "Neural processors" category. Depending
      on your chip, the entry may be named "Intel(R) AI Boost", "AMD IPU Device",
      or "Qualcomm Hexagon NPU". Right-click it and choose Properties to see
      version details.
  - q: "Can Windows Update change my NPU firmware?"
    a: >
      Yes. NPU firmware often arrives as a driver update through Windows Update,
      and some machines receive it as a UEFI capsule "firmware" entry instead.
      Check Settings, Windows Update, Update history, Driver updates to see what
      was delivered.
  - q: "Do I need to update NPU firmware manually?"
    a: >
      Usually not. If AI features work correctly, the firmware Windows installed
      is fine. Only chase a manual update if a vendor release notes document a
      fix for a problem you actually have, since a bad flash can destabilize the
      NPU.
---

Your NPU runs two layers of software: the driver that Windows talks to, and the firmware that runs on the chip itself. When AI features like Live Captions or Studio Effects start misbehaving, knowing exactly which firmware build sits on your NPU is the fastest way to tell whether you are behind, stuck on a buggy release, or already on the latest stable build.

Windows 11 does not print this number anywhere obvious, but it takes less than a minute to find once you know where to look. The quickest route runs through Device Manager's Driver and Details tabs, and a second check in Windows Update history catches firmware delivered as a UEFI capsule update. If you are here because an update went wrong rather than because you are curious, start with our guide to [NPU firmware update failures](/articles/npu-firmware-update-failed-laptop/) instead — it covers the recovery path.

This walkthrough covers every reliable way to read the version: Device Manager, vendor utilities, Windows Update history, and the BIOS itself. Odd NPU behavior can show up in strange places — from [Live Captions system audio not working](/articles/live-captions-system-audio-not-working/) to a [Copilot key that registers two presses](/articles/copilot-key-double-press-issue/) — and confirming your firmware build is the same first diagnostic step for all of them.

## Why this happens

- **Firmware and driver are separate layers:** The driver lives in Windows; the firmware lives on the NPU chip. Windows surfaces the driver version prominently and buries the firmware build.
- **Windows hides firmware behind the driver:** In Device Manager, the Driver tab gets all the attention, while the firmware revision sits on the Details tab under property names most people never open.
- **Vendors bundle firmware inside driver packages:** Intel, AMD, and Qualcomm ship NPU firmware together with driver releases, so the two version numbers change at the same time but are not the same number.
- **Some updates arrive as UEFI capsule updates:** BIOS-level firmware can be delivered through Windows Update as a separate "firmware" entry that Device Manager never shows.
- **OEMs rename the device:** Your NPU may appear as "Intel(R) AI Boost", "AMD IPU Device", or "Qualcomm Hexagon NPU", so the entry you are looking for does not always say "NPU".
- **Property names vary by vendor:** One vendor exposes "Firmware version" directly, another encodes the build into Hardware Ids — there is no single standard label.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the version in Device Manager's Driver tab

This is the fastest check and works on every Copilot+ laptop. The Driver tab shows the installed driver package, which on Intel and AMD systems moves in lockstep with the firmware build, so it is a reliable proxy even before you dig deeper.

1. Press Win + X and choose Device Manager.
2. Expand the "Neural processors" category.
3. Right-click your NPU entry (Intel(R) AI Boost, AMD IPU Device, or Qualcomm Hexagon NPU) and choose Properties.
4. Open the Driver tab and note the Driver Version and Driver Date.
5. Write the version down — you will compare it against the vendor's latest in Fix 6.

### Fix 2: Find the firmware build on the Details tab

When you need the actual on-chip firmware revision rather than the driver package, the Details tab has it. The exact property name depends on the vendor, but the build number is always in this dropdown somewhere.

1. In the same NPU Properties window, switch to the Details tab.
2. Open the Property dropdown and look for "Firmware version" or "Firmware revision".
3. If it is not there, select "Hardware Ids" — the firmware build is often encoded in the revision portion of the ID string.
4. Also check "Driver version" in this dropdown to confirm it matches what the Driver tab showed.
5. Note both numbers: firmware build plus driver version gives you the complete picture.
6. If neither property exists, your vendor exposes firmware only through its own utility — move to Fix 3.

### Fix 3: Use the chip vendor's own utility

Intel, AMD, and Qualcomm each ship a tool that reports NPU details more completely than Device Manager. These utilities also tell you when a newer package is available, which closes the loop between "what I have" and "what is current."

1. On Intel Core Ultra systems, install the Intel Driver & Support Assistant from [intel.com](https://www.intel.com/content/www/us/en/support/detect.html) and run a scan — it lists the NPU package version.
2. On AMD Ryzen AI systems, open AMD Software (Adrenalin) and check the System panel for the XDNA NPU driver and firmware entries.
3. On Snapdragon X systems, check Windows Update first — Qualcomm delivers NPU updates through it — then confirm in Device Manager.
4. Compare the reported version against the vendor's driver download page for your exact chip.
5. If the utility offers an update and your AI features are misbehaving, install it; if everything works, there is no need to chase the newest number.

### Fix 4: Check Windows Update history for firmware deliveries

Some NPU firmware arrives outside Device Manager entirely, as a UEFI capsule or a driver update pushed by Windows Update. The update history is the only place that records these, and it tells you the date each one landed.

1. Open Settings, then Windows Update.
2. Click "Update history" and scroll to Driver updates.
3. Look for entries mentioning Neural, NPU, AI Boost, IPU, or your chip vendor.
4. Also check the "Other updates" section — UEFI capsule firmware sometimes lands here.
5. Match the most recent NPU-related date against when your symptoms started; a firmware delivery right before the problem is a strong clue.
6. If Windows Update is offering an optional driver update for the NPU, review it before installing — optional does not mean required.

### Fix 5: Confirm the firmware from the BIOS or UEFI

On many laptops the system firmware setup screen shows the NPU or AI accelerator firmware revision directly. This is also where you can verify the NPU is enabled at the hardware level, which matters if Device Manager shows nothing at all.

1. Restart the laptop and enter the BIOS/UEFI (usually F2, Del, or F12 during boot).
2. Look under Advanced, Devices, or a dedicated AI/NPU section — the layout varies by manufacturer.
3. Find the NPU entry and note any firmware or microcode revision shown.
4. Confirm the NPU is enabled; a disabled NPU will not appear in Windows at all.
5. Save and exit without changing anything unless you intended to toggle the setting.

### Fix 6: Compare your build against the vendor's latest release

A version number means nothing without a reference. Once you have your firmware and driver numbers, a two-minute comparison tells you whether you are current, one release behind, or running something old enough to explain your problems.

1. Go to your vendor's driver page — Intel, [AMD](https://www.amd.com/en/support/download/drivers.html), or Qualcomm — and find the latest NPU package for your exact chip.
2. Compare its version against the numbers you recorded in Fixes 1 and 2.
3. If you are several releases behind and AI features misbehave, update using the vendor installer rather than a third-party tool.
4. If you are current and still have problems, the firmware is not the cause — look at drivers, power settings, or the app itself.
5. Record the "known good" version somewhere; it is invaluable if a future update breaks things and you need to roll back.

## Closing

Checking your NPU firmware version is a two-minute job once you know the three places it hides: the Driver tab for the package, the Details tab for the on-chip build, and Windows Update history for capsule deliveries. Make it the first step whenever AI features act up, and if a previous update left you worse off, the [Intel NPU firmware update stuck](/articles/intel-npu-firmware-update-stuck/) guide walks through the recovery. A known-good version number written down today saves real troubleshooting time tomorrow.
