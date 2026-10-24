---
title: "How to Fix HP EliteBook Ultra G1q Issues on Windows 11"
slug: hp-elitebook-ultra-g1q-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["elitebook-ultra-g1q", "hp", "snapdragon-x", "business-laptop", "troubleshooting"]
description: "HP EliteBook Ultra G1q glitching on Windows 11? Fix Snapdragon driver gaps, Wolf Security conflicts, USB-C dock issues, and Copilot+ features step by step."
thumbnail: "/images/thumbs/hp-elitebook-ultra-g1q-issues.webp"
faqs:
  - q: "Why is my EliteBook Ultra G1q slow with some apps?"
    a: >
      Slowdowns usually come from x86 apps running under emulation or from HP Wolf Security scanning aggressively. Check Task Manager's Architecture column for emulated processes, and review Wolf Security policies with your IT admin.
  - q: "Does the EliteBook Ultra G1q support all Copilot+ features?"
    a: >
      Yes — the Snapdragon X Elite model is a full Copilot+ PC. If Recall or Studio Effects are missing, the Qualcomm NPU driver or the Windows AI components need updating through HP's driver packages and Windows Update.
  - q: "Why won't my USB-C dock work reliably with the G1q?"
    a: >
      Dock issues on the G1q are usually USB4 negotiation problems with older dock firmware, or HP's power management putting ports to sleep. Update the dock firmware and disable USB selective suspend.
  - q: "Can I downgrade the EliteBook Ultra G1q to Windows 10?"
    a: >
      No — Windows 10 has no Snapdragon X support and HP provides no drivers for it on this model. The G1q is Windows 11 on ARM only, so all fixes must happen within Windows 11.
---

The EliteBook Ultra G1q is HP's flagship business AI PC — Snapdragon X Elite, enterprise security, premium build. It's also the machine where IT departments discover that "Windows is Windows" isn't quite true anymore. The VPN works, Office flies, then the security agent blocks something, the dock misbehaves, and a Copilot+ feature demo falls flat in front of a client.

Most G1q issues fall into three buckets: HP's enterprise software stack (Wolf Security, Sure Start, management agents) colliding with the ARM platform, driver packages that matured after launch, and the standard Snapdragon app-compatibility learning curve. None of these are fatal. All of them are diagnosable.

This guide works through the six most common G1q problems in technician order: HP's driver and firmware stack first, then Wolf Security and enterprise conflicts, then app compatibility, then NPU and Copilot+ features, then docks and peripherals, and finally the honest architectural limits. The same ARM patterns recur across vendors — our [AutoHotkey on ARM notes](/articles/autohotkey-arm-windows-not-working/) and the [MediaTek Filogic Wi-Fi 7 rundown](/articles/mediatek-filogic-wifi7-issues-laptop/) cover the shared driver family — and if [CapCut misbehaves on your ARM laptop](/articles/capcut-arm-windows-laptop-issues/), the compatibility logic is identical.

## Why this happens

- **HP Wolf Security conflicting with ARM components:** Wolf Pro Security's deep hooks were tuned on x64; on Snapdragon they can block legitimate ARM64 drivers or throttle emulated apps, causing mysterious slowdowns and blocks.
- **Stale HP Snapdragon driver bundle:** Early G1q driver packages had NPU, USB4, and power-management gaps. HP has revised them several times since launch.
- **Enterprise management agents assuming x64:** Older SCCM clients, imaging tools, and custom IT scripts target x64 only and fail silently or loudly on the ARM G1q.
- **x86-only LOB apps with drivers:** Line-of-business apps with kernel components (old VPNs, smart-card middleware, USB license dongles) are the hard blockers on any ARM machine.
- **USB4 dock negotiation with legacy docks:** The G1q's USB4 ports negotiate differently than Thunderbolt; older HP docks with old firmware drop monitors or Ethernet after sleep.
- **NPU driver not deployed by IT image:** Corporate images sometimes strip the Qualcomm NPU driver, leaving Copilot+ features permanently unavailable until it's reinstalled.
- **Sure Start / BIOS security false positives:** HP Sure Start can flag legitimate firmware updates or recovery media as tampering, blocking updates that would fix the other issues.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update HP's full driver and firmware stack

The G1q's launch-era driver bundle is behind most current complaints. HP's updated packages fix NPU detection, USB4 stability, and power management — but they must come from HP, not generic Windows Update drivers.

1. Install **HP Image Assistant** or use [HP's support site](https://support.hp.com/us-en) — enter your exact G1q product number and download the latest driver pack.
2. Prioritize the UEFI/BIOS, chipset, Qualcomm NPU, and USB4/Thunderbolt driver updates; install with the laptop plugged into AC power.
3. Restart and allow all firmware phases to complete — Sure Start will verify each stage, which takes a few extra minutes.
4. After boot, open **Device Manager > Neural processors** and confirm the NPU is present with no warning icon.
5. Retest your specific symptom before continuing — dock issues and NPU absence most commonly resolve here.

### Fix 2: Resolve Wolf Security and enterprise software conflicts

When the G1q is slow or blocks legitimate software, Wolf Security is suspect number one. Its behavioral monitoring can misjudge ARM64 processes and emulated apps — but don't just disable it; tune it, preferably with IT.

1. Open **HP Wolf Security** and check the threat and block history for entries matching your problem app or driver.
2. Ask your IT admin whether Wolf Pro policies can whitelist the affected ARM64 executables — this is the correct enterprise fix.
3. Check Task Manager for Wolf services consuming high CPU during your slowdowns — sustained scanning of emulated apps is a known pattern.
4. Verify your management agent (Intune, SCCM) has an ARM64-compatible version deployed — legacy x64 agents cause policy and inventory gaps.
5. Never permanently disable Wolf Security to "fix" performance — on a business laptop that trades one problem for a compliance violation.

### Fix 3: Handle x86 app and driver compatibility

The G1q runs user-mode x86 apps fine under Prism emulation, but kernel-driver installers fail hard. Identifying which of your apps fall in which bucket determines whether there's a fix or only a workaround.

1. In Task Manager's **Details** tab, add the **Architecture** column — anything marked x86 is emulated; ARM64 is native.
2. For slow emulated apps, check the vendor for an ARM64 build (browsers, Teams, Zoom, and VPNs increasingly have them).
3. For installers that fail, determine whether they bundle a driver — check the vendor's ARM64 support statement before retrying.
4. Smart-card readers, USB license dongles, and old printers are the classic casualties — look for ARM64 driver packages from those vendors specifically.
5. Where no ARM64 path exists, use the web app version or remote desktop to an x64 machine — document these for IT so the fleet plan accounts for them.

### Fix 4: Restore NPU and Copilot+ functionality

A G1q without working Copilot+ features is usually missing the NPU driver — corporate images are notorious for stripping it. The fix is reinstalling the driver and letting Windows fetch the AI components.

1. Confirm the NPU's absence in **Device Manager > Neural processors** — if the category doesn't exist, the driver was never installed.
2. Install the Qualcomm NPU driver from HP's G1q driver page (not a generic Qualcomm package — HP customizes the INF).
3. Run **Windows Update** including optional updates — the Copilot+ on-device models download as separate components.
4. Check **Settings > Privacy & security > Recall & snapshots** to confirm the AI feature pages appear.
5. If IT manages the device, ask them to include the NPU driver in the task sequence — otherwise every reimage breaks Copilot+ again.

### Fix 5: Stabilize docks, monitors, and USB-C

G1q dock problems — monitors not waking, Ethernet dropping, USB devices vanishing after sleep — are USB4 negotiation issues compounded by aggressive power management. Dock firmware plus port settings fix the vast majority.

1. Update your dock's firmware from the dock manufacturer's site — this single step resolves most "worked until sleep" cases.
2. In **Device Manager > Universal Serial Bus controllers**, ensure the USB4 host drivers are HP's current versions.
3. Disable **USB selective suspend** in Power Options advanced settings to stop Windows sleeping ports mid-session.
4. Test the failing peripheral directly on the laptop to isolate dock vs. machine — if it works direct, the dock (or its firmware) is the problem.
5. For HP docks specifically, check HP's accessory support pages for G1q compatibility notes — some older docks need a specific firmware floor.

### Fix  6: Recognize the architectural limits honestly

Some G1q issues have no driver fix because they're architectural: x86 kernel drivers will never run on ARM, and some enterprise tools will never be ported. Naming these clearly saves everyone from endless troubleshooting loops.

1. Accept that x86-only kernel software (old VPN drivers, legacy endpoint tools) needs an ARM64 replacement or a different access method — no setting changes this.
2. If your role depends on such software daily, the G1q may be the wrong machine — raise it with IT with specifics, not frustration.
3. Keep HP's cloud recovery tool handy so you can restore the factory ARM64 image cleanly if Windows gets wedged.
4. Document every workaround your team adopts — the next Snapdragon EliteBook deployment will hit the same list.
5. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) periodically for Windows on ARM compatibility announcements that change the picture.

## Closing

The EliteBook Ultra G1q's issues are enterprise growing pains, not hardware faults: update HP's full driver stack, tune Wolf Security with IT instead of fighting it, sort apps into native/emulated/driver-blocked buckets, restore the NPU driver for Copilot+ features, and update dock firmware for USB4 stability. The rest is architecture — work around it honestly, and the G1q does exactly what HP built it for: secure, all-day business computing.
