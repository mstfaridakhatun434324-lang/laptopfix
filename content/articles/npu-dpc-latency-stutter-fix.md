---
title: "How to Fix NPU DPC Latency Stuttering in Windows 11 (Audio and Video)"
slug: npu-dpc-latency-stutter-fix
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu","dpc-latency","stuttering","windows-11","audio-fix","troubleshooting"]
description: "NPU DPC latency spikes cause audio crackling and video stutter on AI laptops. Measure it with LatencyMon and fix it with driver, BIOS, and power tweaks."
thumbnail: "/images/thumbs/npu-dpc-latency-stutter-fix.webp"
faqs:
  - q: "What is DPC latency and why does the NPU affect it?"
    a: >
      DPC (Deferred Procedure Call) latency measures how long drivers take to
      finish interrupt work. If the NPU driver holds the system too long, audio
      buffers underrun and you hear crackling or see frame stutters, even though
      CPU usage looks low.
  - q: "Is LatencyMon safe to run on my laptop?"
    a: >
      Yes. LatencyMon only measures and reports driver timing; it changes
      nothing on your system. Run it for a few minutes while reproducing the
      stutter, then read which driver shows the highest DPC execution time.
  - q: "Can disabling the NPU fix the stuttering?"
    a: >
      It can confirm the diagnosis, but it is not a real fix — you lose Copilot+
      features. Use it as a test only, then work through driver, BIOS, and power
      fixes so the NPU stays enabled and quiet.
  - q: "Will updating the BIOS really help DPC latency?"
    a: >
      Often, yes. Many NPU DPC spikes trace back to firmware-level interrupt
      handling and power-state transitions, which BIOS updates regularly improve.
      Check your laptop maker's support page for a newer BIOS before replacing
      hardware in your head.
---

Audio crackling during a call, micro-stutters in video, mouse movement that hitches for a split second — and Task Manager shows the CPU barely working. On AI laptops, the culprit is often the NPU driver holding the system in a Deferred Procedure Call for too long. DPC latency spikes like these are invisible in normal monitoring, which is why the stutter feels so mysterious.

The good news is that DPC latency is measurable. A free tool called LatencyMon will point at the exact driver responsible within minutes, and once you know the NPU driver is the offender, the fixes are concrete: update or reinstall the driver, adjust power behavior, and update the BIOS. If your stutter shows up specifically while gaming, also read our [NPU game stutter fix](/articles/npu-causing-game-stutter-fix/) — it covers the gaming-specific side of the same problem.

Do not just disable the NPU and call it done. That "fix" costs you every Copilot+ feature your laptop was bought for. The walkthrough below diagnoses first with real measurements, then applies fixes in order — and along the way you may notice other flakiness, like [Teams Live Captions acting up](/articles/live-captions-teams-meeting/) or a [Copilot app WebView2 runtime error](/articles/copilot-app-webview2-runtime-error/), which often share the same unstable driver underneath.

## Why this happens

- **DPCs block everything briefly:** When a driver services an interrupt, it runs a Deferred Procedure Call that delays all other work — audio included.
- **NPU drivers are still maturing:** AI accelerator drivers are newer than GPU drivers and more prone to long DPC execution times, especially in early releases.
- **Power-state transitions spike latency:** The NPU constantly sleeps and wakes to save battery; each transition can stall the system if the driver handles it poorly.
- **Old BIOS firmware mishandles interrupts:** Firmware-level interrupt routing and C-state behavior directly affect how long NPU DPCs take.
- **Aggressive CPU power saving compounds it:** Deep C-states and core parking make every wake-up slower, amplifying the NPU driver's own delays.
- **Conflicting drivers stack up:** Network, audio, and storage drivers with their own latency issues combine with NPU spikes to push audio buffers over the edge.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure DPC latency with LatencyMon

Never guess at latency problems — measure them. LatencyMon runs for a few minutes and names the driver with the highest DPC execution time, turning a vague "my laptop stutters" into a named offender you can actually fix.

1. Download LatencyMon (free) and install it, then close unnecessary background apps.
2. Click the green play button to start monitoring and use the laptop normally for 3–5 minutes — reproduce the stutter if you can.
3. Open the Drivers tab and sort by "DPC count" and "Highest execution (ms)".
4. If the top offender is your NPU driver (ndis-adjacent names vary, but look for Intel, AMD IPU, or Qualcomm entries), you have confirmed the diagnosis.
5. Note the numbers — you will re-run this test after each fix to prove improvement.
6. If a different driver tops the list, fix that one first; NPU tweaks will not help a network-driver latency problem.

### Fix 2: Update the NPU driver to the latest release

Most NPU DPC latency bugs are fixed in newer driver releases — vendors actively tune interrupt handling once reports come in. An update is the highest-probability fix and takes minutes.

1. Identify your NPU in Device Manager under Neural processors.
2. Get the latest driver from the vendor: Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), AMD from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html), or Windows Update for Qualcomm.
3. Install it, restart, and re-run LatencyMon for 5 minutes.
4. Compare the NPU driver's highest DPC execution time against your baseline.
5. If the numbers dropped into the green, you are done — the update was the fix.
6. If nothing changed, keep the new driver anyway (it rules out the old one) and continue.

### Fix 3: Do a clean reinstall of the NPU driver

A driver that updated in place can carry corrupted settings or conflicting remnants. A clean reinstall — remove fully, then install fresh — eliminates that whole class of problems and often resolves latency the update alone did not.

1. Download the latest NPU driver installer first, so you are not left without one.
2. In Device Manager, right-click the NPU, choose Uninstall device, and tick "Attempt to remove the driver for this device".
3. Restart the laptop — Windows will install a basic driver or none at all.
4. Run the fresh vendor installer you downloaded and restart again.
5. Re-run LatencyMon and compare against baseline; clean installs frequently cut DPC times dramatically.
6. If stutter persists, note it — the problem is likely firmware or power behavior, covered next.

### Fix 4: Update the system BIOS

BIOS updates regularly fix interrupt routing, C-state behavior, and NPU power management — all direct contributors to DPC latency. Laptop makers publish these specifically to address stutter reports, and skipping this step leaves a common fix on the table.

1. Find your exact laptop model and visit the maker's support page ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
2. Check the BIOS changelog for mentions of NPU, AI, latency, or stutter fixes.
3. Download the latest BIOS and install it with the charger plugged in — never interrupt a BIOS flash.
4. After the restart, re-run LatencyMon and check the NPU driver's numbers again.
5. Also verify in the BIOS that the NPU is enabled; a half-initialized device can behave worse than a disabled one.

### Fix 5: Tune Windows power settings to reduce latency

Aggressive power saving forces the NPU and CPU through constant sleep-wake cycles, and every transition is a chance for a DPC spike. On AC power especially, trading a little efficiency for responsiveness is the right call.

1. Open Settings, System, Power & battery, and set Power mode to "Best performance" while testing.
2. Open the legacy Power Options (search "power plan"), choose High performance or create a custom plan.
3. In advanced settings, expand "Processor power management" and raise the minimum processor state to 50–100% on AC.
4. Disable USB selective suspend under USB settings — it is a classic stutter source.
5. Re-run LatencyMon; if latency dropped, keep the settings and consider a separate battery-saver plan for unplugged use.
6. Do not leave "Best performance" on battery permanently if you need all-day runtime — make it an AC-power profile.

### Fix 6: Disable CPU C-states and problematic devices as a test

Deep CPU sleep states (C-states) make every interrupt wake-up slower, and a misbehaving secondary device can add its own latency on top. This fix is diagnostic: if it helps, you know power management is the lever, and you can then find the minimal change.

1. Enter the BIOS/UEFI and look for CPU C-state or power-saving options under Advanced or Power.
2. Disable the deepest C-states (keep C1E if offered) as a test — save and reboot.
3. Re-run LatencyMon and note whether the NPU driver's worst-case execution time improved.
4. In Device Manager, also try disabling devices you do not use (unused network adapters, for example) one at a time, testing between each.
5. If a specific device's removal fixes it, update that device's driver rather than leaving it disabled.
6. Re-enable C-states afterward if disabling them made no difference — there is no benefit in running hotter for nothing.

## Closing

NPU DPC latency stutter is fixable because it is measurable: LatencyMon names the driver, and driver, BIOS, and power fixes address the known causes in order of likelihood. Re-run the measurement after each change so you know which one actually worked. If the stutter followed a recent system change, check whether the [laptop slowed down after a Windows update](/articles/ai-pc-slow-after-windows-update/) — the same update that brought the stutter may have brought the NPU driver with it.
