---
title: "Enable Hardware-Accelerated GPU Scheduling the Right Way"
slug: best-way-to-enable-hardware-accelerated-gpu-scheduling
date: 2026-10-12
categories: ["performance"]
tags: ["hags", "gpu scheduling", "gaming", "performance", "windows 11"]
description: "Hardware-Accelerated GPU Scheduling can cut latency and smooth frame times — if your hardware supports it and your drivers are current. Here's the correct way to enable it."
thumbnail: "/images/thumbs/best-way-to-enable-hardware-accelerated-gpu-scheduling.webp"
faqs:
  - q: "What does Hardware-Accelerated GPU Scheduling actually do?"
    a: "Normally your CPU manages GPU video memory scheduling — deciding what the GPU works on and when. HAGS hands that scheduling to a dedicated GPU-based scheduler instead, reducing CPU overhead and, more importantly, cutting the latency between the CPU submitting work and the GPU executing it. On CPU-bottlenecked systems this translates to slightly higher FPS and noticeably more consistent frame times."
  - q: "Will HAGS make my games faster?"
    a: "Expect small gains, not miracles: typically 1–5% higher average FPS, with the bigger win being reduced latency and smoother frame pacing on systems where the CPU is the bottleneck. On heavily GPU-bound systems you may measure no difference at all. It's a free, safe optimization on supported hardware — worth enabling, but not worth upgrading hardware for."
  - q: "Why don't I see the HAGS option in Settings?"
    a: "The toggle only appears when your GPU and driver support it: you need a relatively modern GPU (NVIDIA GTX 10-series or newer, AMD RX 5600/5700 or newer, Intel integrated graphics from 11th-gen-ish onward) with a current WDDM 2.7+ driver. If it's missing, update your GPU driver first — outdated drivers are the most common reason. Very old GPUs simply don't support it, and no setting can change that."
  - q: "Can HAGS cause problems?"
    a: "Rarely, with current drivers — but early HAGS implementations and some older driver versions caused stuttering, crashes, or black screens in specific games, which gave it a mixed reputation. The rule: enable it on fully updated drivers, test your main games, and if anything misbehaves, toggle it off — it's instantly reversible. On 2024+ drivers, problems are uncommon."
---

Hardware-Accelerated GPU Scheduling (HAGS) is one of those Windows features that's been quietly available since 2020 but still trips people up: the toggle hides in an unintuitive Settings page, it requires specific hardware and driver support, and it only activates after a reboot that nobody tells you about. Done right, it's free latency reduction — the GPU scheduling its own work instead of waiting on the CPU. Done wrong (toggled on ancient drivers, or expected to double FPS), it's disappointment. This guide does it right.

Quick expectation-setting: HAGS shines on CPU-limited systems and high-refresh gaming; on a GPU-bound laptop at 4K, you'll barely measure it. It's one optimization among several — pair it with our [game stuttering guide](/articles/how-to-fix-windows-11-stuttering-in-games-step-by-step/) for the full picture.

## Why this happens

- **CPU-bottlenecked scheduling**: the traditional model makes the CPU a middleman for every GPU scheduling decision, adding latency.
- **Driver-gated availability**: the toggle only appears with WDDM 2.7+ drivers on supported GPUs — old drivers hide it entirely.
- **Reboot required**: HAGS activates at boot; toggling without restarting does nothing, confusing many users.
- **Early-implementation reputation**: buggy 2020-era rollouts left a lingering belief that HAGS is unstable — long since fixed on current drivers.
- **Marginal on GPU-bound systems**: when the GPU is the limit, scheduling latency isn't the bottleneck, so gains vanish.
- **Conflicting "optimization" guides**: random tweaks (disabling it via registry myths) create confusion about its actual state.
- **Windows updates resetting graphics settings**: feature updates occasionally revert the toggle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify your hardware supports HAGS

Don't hunt for a toggle your GPU can't offer. HAGS needs a GPU with a hardware scheduler and a WDDM 2.7+ driver to drive it — older GPUs physically lack the scheduler block, so no driver update or registry tweak can conjure support. Five minutes checking your GPU model against the support lines below saves a frustrating hunt through Settings for a toggle that will never appear.

1. Check your GPU: **Task Manager > Performance > GPU** — note the model.
2. Rough support lines: **NVIDIA** GTX 10-series / RTX 20-series and newer; **AMD** RX 5600/5700 and newer; **Intel** integrated from ~11th gen onward with current drivers.
3. Check your driver date in **Device Manager > Display adapters > Properties > Driver** — drivers older than ~2023 likely lack proper HAGS support.
4. If the hardware qualifies but the toggle is missing, it's a driver problem — Fix 2 solves it.
5. If the GPU predates support, stop here — no software enables HAGS on unsupported silicon.

### Fix 2: Update the GPU driver properly

Current drivers are the prerequisite for everything else.

1. NVIDIA: official [NVIDIA download page](https://www.nvidia.com/Download/index.aspx); AMD: AMD's official driver page; Intel: Intel's [driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html).
2. Choose **Clean installation** — HAGS interacts with the driver at a low level; a clean driver state matters.
3. After installing, reboot — then check for the toggle before changing anything else.
4. Keep the driver current afterward; HAGS stability tracks driver maturity closely.
5. On laptops with dual GPUs (integrated + discrete), update *both* drivers — HAGS settings apply per-GPU and the iGPU driver matters too.

### Fix 3: Enable HAGS in Settings

The actual toggle, in its unintuitive home.

1. Go to **Settings > System > Display > Graphics**.
2. Click **Change default graphics settings** (small link near the top).
3. Toggle on **Hardware-accelerated GPU scheduling**.
4. Also review **Variable refresh rate** on the same page — enable it if your display supports it; it complements HAGS for smoothness.
5. Note the "restart required" prompt — the setting does nothing until you reboot.

### Fix 4: Reboot and verify it's active

Confirm the change actually took effect.

1. Restart the laptop — full restart, not sleep/wake.
2. Return to **Change default graphics settings** and confirm the toggle is still on (updates and driver reinstalls can flip it).
3. Advanced verification: tools like GPU-Z or DXDiag won't directly show HAGS state; the Settings toggle is the source of truth.
4. If the toggle reverted itself, your driver may have failed to initialize HAGS — update the driver again or try the vendor's Studio/stable branch.
5. Once confirmed on, leave it — there's no ongoing maintenance; it just works.

### Fix 5: Test with real games and frame times

Measure the actual benefit on your system.

1. Pick 2–3 of your regular games and enable a frame-time overlay (in-game or GPU vendor overlay).
2. Play the same demanding scene with HAGS on; note average FPS and frame-time consistency.
3. Toggle HAGS off, reboot, and repeat the same scene for comparison — same settings, same scene, honest A/B.
4. Expect 1–5% FPS gains and smoother frame pacing on CPU-limited setups; little to no change on GPU-bound ones.
5. Keep whichever is better *for your games* — on current drivers, "on" wins the vast majority of comparisons, but your hardware gets the vote. For the power side of the equation, also consider [switching to Best performance mode](/articles/how-to-change-power-plan-to-best-performance-in-windows-11-24h2/) so the CPU doesn't throttle the gains HAGS delivers.

### Fix 6: Handle the rare misbehavior

If a specific game dislikes HAGS.

1. Symptoms of HAGS trouble: new stuttering, crashes, or black screens in a game that was fine before — appearing right after enabling.
2. First, update the GPU driver once more — most HAGS issues are actually driver issues wearing a HAGS costume.
3. If one game misbehaves while others benefit, toggle HAGS off, reboot, and retest that game — per-game exceptions aren't possible, so it's a global choice.
4. Check the game's forums for known HAGS interactions — a few titles have documented quirks with workarounds.
5. Remember it's instantly reversible: off + reboot returns you to the classic scheduler with zero residue. Microsoft's Windows support hub documents the graphics settings officially.

## Closing

HAGS is a small, free, safe win on supported hardware: update the driver, flip the toggle in Change default graphics settings, reboot, verify, and enjoy the latency reduction. It won't transform a weak GPU, but on CPU-limited laptops it's one of the few settings that genuinely reduces the delay between your input and the pixels — and unlike most "optimization" tweaks, this one is real, documented, and reversible.
