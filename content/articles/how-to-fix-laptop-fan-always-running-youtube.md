---
title: "How to Fix a Laptop Fan That's Always Running"
slug: how-to-fix-laptop-fan-always-running-youtube
date: 2026-09-12
categories: ["performance"]
tags: ["fan always running", "fan noise", "cooling", "windows 11", "cpu usage"]
description: "Laptop fan never stops spinning? Find the constant load or cooling fault behind it and quiet your machine with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-laptop-fan-always-running-youtube.webp"
faqs:
  - q: "Why won't my laptop fan ever turn off?"
    a: "Because something is continuously generating heat or the fan control is broken. The usual suspects: a background process with constant CPU usage (updaters, miners, stuck services), the discrete GPU stuck awake, dust-clogged cooling that can't shed even idle heat, dried thermal paste, or a BIOS/firmware fan curve stuck at high speed. Constant fan means constant cause — find what's constant."
  - q: "Is it bad to leave a laptop with the fan always running?"
    a: "The fan running constantly won't damage the fan quickly — they're rated for continuous duty — but the underlying cause might be harming the laptop. Constant high temperatures degrade batteries and thermal paste faster. And constant full-speed operation from a firmware bug is just noise pollution. Either way, the always-on fan is a symptom worth fixing, not a state to accept."
  - q: "Can malware cause the fan to run constantly?"
    a: "Yes — cryptominers are the classic example, deliberately maxing CPU/GPU 24/7, which pins fans at full speed. If Task Manager shows high constant CPU from an unfamiliar process, or high usage with no visible cause, run a full Microsoft Defender scan plus a second-opinion scan. Miners often hide as legitimate-sounding processes, so check file locations, not just names."
  - q: "Will limiting max CPU speed quiet the fan?"
    a: "It can, as a workaround. Setting maximum processor state to 95–99% in the power plan disables turbo boost, cutting heat dramatically with a modest performance cost. It's a legitimate tactic for hot-running laptops, especially on battery. But it's a bandage — if a stuck process is the cause, fixing the process is better than throttling the whole CPU."
---

There's "fan spins up sometimes" (normal) and "fan has not stopped in three days" (not normal). A fan that runs constantly is responding to something constant — and your job is to find the constant. In practice it's one of four things: a process that never sleeps, a GPU that never idles, cooling that can't cope with even baseline heat, or firmware telling the fan to ignore reality.

The diagnostic split from the start: check temperatures and CPU load together. High temps + high load = software burning cycles. High temps + low load = cooling failure. Normal temps + loud fan = fan control problem. Each points to a different fix section below. See also [fan always running on Windows 11](/articles/how-to-fix-laptop-fan-always-running-on-windows-11/) and [disabling background apps](/articles/how-to-disable-background-apps-on-laptop/).

## Why this happens

- **A process with constant CPU usage**: Miners, stuck updaters, runaway services — the fan's fuel.
- **Discrete GPU stuck awake**: Never idling, generating heat around the clock.
- **Dust-choked cooling**: Heatsinks so clogged that idle heat needs full fan speed.
- **Failed thermal paste**: Heat trapped at the CPU, fans maxed trying to compensate.
- **Firmware fan curve stuck**: BIOS bug or misconfiguration ignoring temperature input.
- **Malware**: Cryptominers designed to burn CPU/GPU continuously.
- **Always-on turbo/boost**: Power plans that never let the CPU downclock.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the constant load

Find what's burning cycles around the clock.

1. Open Task Manager > **Details**, sort by **CPU**, and watch for 2–3 minutes — you're looking for what's *always* active, not what spikes.
2. Check the **GPU** column too — constant GPU usage from a stuck process explains fans with calm CPU numbers.
3. Open **Resource Monitor** > **CPU** and look at per-service breakdowns under svchost — a runaway Windows service hides here.
4. Note the process name *and* its file location (right-click > **Open file location**) — malware often wears a legitimate-sounding name in a wrong folder.
5. If total CPU is low (<10%) yet the fan screams, skip to Fix 4 (cooling) and Fix 5 (firmware) — there's no software fire, so it's a cooling or control problem.

### Fix 2: Rule out malware

Constant unexplained load demands a security check.

1. Run a **full** Microsoft Defender scan (**Windows Security** > **Virus & threat protection** > **Scan options** > **Full scan**) — not the quick scan.
2. Follow with a **Microsoft Defender Offline scan** from the same menu — it reboots into a clean environment that catches persistent miners.
3. Check **Task Scheduler** for unfamiliar tasks set to run constantly or at logon — miners often persist via scheduled tasks.
4. Review **Startup apps** and `shell:startup` for anything you don't recognize — disable first, research second.
5. If scans find a miner, change passwords for important accounts afterward — the infection vector may have harvested credentials. Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) documents Defender's offline scan officially.

### Fix 3: Stop the legitimate constant burners

Not all constant load is malicious.

1. **Windows Update**: check for stuck updates — a failed update retrying forever burns CPU. Run the update troubleshooter and reset components if needed.
2. **Search indexing**: a corrupt index rebuilds endlessly — check Indexing Options, exclude churn folders, or rebuild the index.
3. **Cloud sync**: OneDrive/Dropbox stuck syncing a problematic file loops forever — pause sync and check for sync errors.
4. **Third-party updaters and telemetry**: motherboard utilities, RGB software, and "helper" apps with constant background activity — disable their startup entries.
5. **Browser**: a tab running a crypto miner via JavaScript (malicious ads do this) — close the browser entirely as a test; if the fan stops, the culprit was a tab.

### Fix 4: Fix the cooling system

For high temps with low load — the heat can't escape.

1. Check idle temperatures with HWiNFO — 70°C+ at true idle (no apps, low CPU) confirms a cooling failure, not a software fire.
2. Power off and blow out intake/exhaust vents with compressed air, holding fan blades still — expect dramatic improvement on neglected machines.
3. Open the chassis if comfortable (mind warranty): clean fan blades and heatsink fins directly, verify fans spin freely.
4. On 3+ year old laptops with persistent high idle temps after cleaning, repaste the CPU/GPU — dried paste is the classic "fan always on" hardware cause.
5. Verify heatsink mounting pressure is even — a loose heatsink corner creates a hotspot that drives fans to maximum.

### Fix 5: Fix fan control and firmware

For normal temps with a screaming fan.

1. Check the vendor control app (Armoury Crate, Legion Zone, OMEN Hub, Dell Power Manager) — switch to **Silent**/**Quiet** profile and inspect the fan curve.
2. Update the BIOS from the vendor's support site — fan-control bugs are fixed in BIOS updates regularly; some updates even document "fan curve" fixes explicitly.
3. Reset BIOS to optimized defaults if a previous tweak broke fan behavior.
4. In advanced power settings, check **Processor power management** > **System cooling policy** — set to **Passive** as a test (slows CPU before ramping fans).
5. As a workaround, set **Maximum processor state** to 95–99% (disables turbo boost) — massively reduces heat with modest performance cost, useful while diagnosing.

### Fix 6: Calm the power behavior

Stop the CPU from never resting.

1. **Settings** > **System** > **Power & battery** > **Power mode** — **Balanced** or **Best power efficiency** for daily use; reserve **Best performance** for when you need it.
2. In the vendor app, avoid **Turbo**/max-performance profiles as a 24/7 setting — they're for gaming sessions, not desktop idling.
3. Disable **Fast Startup** as a test — its hibernation resume occasionally leaves drivers (including thermal/fan drivers) in bad states.
4. Check **Background apps** permissions (**Settings** > **Apps** > **Installed apps** > per-app **Background app permissions**) — restrict apps that don't need to run constantly.
5. For NVIDIA laptops, **NVIDIA Control Panel** > **Power management mode** → **Optimal power** (not Maximum performance) for desktop use.

## Closing

An always-running fan is a constant cause made audible: constant load, constant heat that can't escape, or a constant firmware command. Measure load and temperature together, and the pair tells you which fix section owns your problem. Most cases end at Fix 1 (a stuck process) or Fix 4 (dust) — the two constants that hide in plain sight. Silence is the sound of a laptop with nothing to complain about.
