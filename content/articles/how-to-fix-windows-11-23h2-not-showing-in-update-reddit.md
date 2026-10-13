---
title: "Windows 11 23H2 Not Showing in Windows Update? Fixes That Work"
slug: how-to-fix-windows-11-23h2-not-showing-in-update-reddit
date: 2026-09-15
categories: ["windows-update"]
tags:
  - "windows 11 23h2"
  - "not showing"
  - "windows update"
  - "reddit fix"
description: "If Windows 11 23H2 never appears in Windows Update, the cause is usually a safeguard hold, missing prerequisites, or update settings. Here are the fixes Reddit threads confirm actually work."
thumbnail: "/images/thumbs/how-to-fix-windows-11-23h2-not-showing-in-update-reddit.webp"
faqs:
  - q: "Why isn't 23H2 showing up in my Windows Update?"
    a: "The most common reasons are a Microsoft safeguard hold on your hardware, missing prerequisites (TPM 2.0, Secure Boot, supported CPU), paused or deferred updates in your settings, or simply that Microsoft rolls out feature updates in waves and your device is not in the current wave yet."
  - q: "Is my laptop too old for Windows 11 23H2?"
    a: "Possibly. Windows 11 requires TPM 2.0, Secure Boot capability, and a supported CPU (generally 8th-gen Intel or newer, or AMD Ryzen 2000+). Use Microsoft's PC Health Check app to verify. If hardware is the blocker, no settings change will make 23H2 appear — and bypassing requirements is not recommended."
  - q: "How long do I wait before trying manual methods?"
    a: "Give Windows Update at least a few weeks past the release before concluding something is wrong, since rollouts are staged and your device may simply be in a later wave. If months pass with no offer while similar hardware has it, work through this guide's checks rather than waiting indefinitely."
  - q: "Do Reddit's registry tweaks to force 23H2 actually work?"
    a: "Some do force the offer, but forcing past a safeguard hold is risky — the hold exists because that hardware combination has a known documented problem. The safe Reddit-endorsed path is the Installation Assistant, not registry hacks to defeat holds."
---

Scroll through any Windows help forum and you will find the same thread repeated hundreds of times: Windows 11 is installed, updates arrive normally, but the 23H2 feature update simply never appears. No error, no explanation — just the same Check for updates button offering nothing new, month after month.

The forum wisdom on this one is actually solid, because the causes are few and well-documented: safeguard holds, unmet prerequisites, paused updates you forgot about, and staged rollouts. The fixes the community keeps confirming are the same ones technicians use.

This guide collects the verified path: rule out the simple settings issues, check the real prerequisites, understand holds, and use the safe manual method when waiting is no longer reasonable. If you are on 24H2 already and fighting a different battle, our [24H2 problem walkthrough](/articles/how-to-fix-windows-11-24h2-update-problems-step-by-step/) is the relevant guide.

## Why this happens

- **Safeguard hold on your hardware:** Microsoft deliberately withholds the update from device combinations with known issues.

- **Staged rollout waves:** feature updates deploy gradually; your device may simply not be in the current wave.

- **Updates paused or deferred:** a forgotten pause or a deferral policy silently suppresses feature updates.

- **Unmet hardware prerequisites:** TPM, Secure Boot, or CPU requirements block the offer entirely.

- **Outdated servicing stack:** without the latest servicing updates, the feature update may not be detected as applicable.

- **Corrupted update detection state:** damaged cache or database can prevent the offer from appearing.

- **Metered connection:** feature updates do not download — or sometimes even get offered — over metered connections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious: pauses, deferrals, and metered connections

Before anything clever, rule out the settings that silently suppress feature updates. These account for a large share of never offered cases and take two minutes to check.

1. Open Settings, Windows Update — confirm updates are not paused (check the pause banner).
2. Go to Advanced options and look for any deferral or target-version settings; clear them.
3. Check Settings, Network and internet — turn off Metered connection for your Wi-Fi.
4. Click Check for updates and wait for the scan to fully complete.
5. If 23H2 appears, install it; if not, continue diagnosing.

### Fix 2: Verify your hardware actually qualifies

No troubleshooting overcomes unmet requirements. Confirming eligibility first prevents wasted effort — and confirms whether the absence of 23H2 is expected behavior.

1. Download and run Microsoft's PC Health Check app from [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).
2. Confirm TPM 2.0 is present and enabled (check BIOS if it reports off).
3. Confirm Secure Boot is enabled in your BIOS/UEFI settings.
4. Check your CPU against Microsoft's supported processor list.
5. If hardware fails, 23H2 will never be offered — plan accordingly rather than forcing it.

### Fix 3: Bring the servicing stack current

The update that finds updates must itself be current. Installing all pending cumulative and servicing updates often makes a missing feature update appear on the next scan.

1. In Windows Update, install every pending update, including optionals you trust.
2. Restart and run Check for updates again — repeat until no more updates appear.
3. Run the Windows Update troubleshooter (Settings, System, Troubleshoot) to fix detection issues.
4. Clear the update cache if detection seems stuck: stop services, rename SoftwareDistribution, restart.
5. Check once more for the 23H2 offer after the system is fully patched.

### Fix 4: Investigate a possible safeguard hold

If everything is eligible and current but 23H2 never appears, a hold is the likely explanation. Holds are information, not errors — they tell you Microsoft knows about a problem with your configuration.

1. Search Microsoft's release health dashboard for 23H2 known issues.
2. Look for your laptop model, GPU, or driver versions in the hold descriptions.
3. Update BIOS and drivers from your maker's site — holds often lift when drivers update.
4. Uninstall software named in hold notices (some holds target specific apps).
5. Recheck monthly; do not use registry edits to bypass the hold.

### Fix 5: Use the Installation Assistant (the safe manual path)

When waiting is unreasonable and no hold applies to you, the [Windows 11 Installation Assistant](https://www.microsoft.com/en-us/software-download/windows11) installs 23H2 directly without fighting the offer logic — the community's preferred manual method.

1. Back up important files first.
2. Download the Installation Assistant from Microsoft's Windows 11 download page.
3. Run it and confirm it detects your system as eligible.
4. Let it download and install 23H2, keeping the laptop plugged in.
5. After completion, run Windows Update to catch post-23H2 cumulative updates.

### Fix 6: Try the Media Creation Tool upgrade

If the Installation Assistant also refuses, the Media Creation Tool's in-place upgrade is the next escalation — same result, different mechanism, and it repairs detection state as a side effect.

1. Back up important files.
2. Download the Media Creation Tool from Microsoft's Windows 11 download page.
3. Run it and choose Upgrade this PC now.
4. Select Keep personal files and apps when prompted.
5. Complete the upgrade, then verify 23H2 in Settings, System, About.

### Fix 7: Reset the update components as a last resort

Persistent absence of the offer after all of the above suggests corrupted detection state. A full component reset rebuilds the machinery that discovers applicable updates.

1. Open Terminal (Admin).
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Restart services with `net start` commands and reboot.
5. Run Check for updates and look for the 23H2 offer with fresh detection state.

## Closing

A missing 23H2 offer is almost never a mystery once you check the four usual suspects: pauses, prerequisites, holds, and rollout waves. Clear the settings issues, verify eligibility, respect the holds, and use the Installation Assistant when the wait stops making sense. The forums got this one right — the patient, official path beats the clever hack. If a metered connection is suppressing the offer, our [metered-connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-in-windows-11-24h2/) shows how to handle it.
