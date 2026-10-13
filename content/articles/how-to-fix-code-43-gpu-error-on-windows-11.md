---
title: "How to Fix Code 43 GPU Error on Windows 11"
slug: how-to-fix-code-43-gpu-error-on-windows-11
date: 2026-09-27
categories: ["drivers"]
tags: ["code 43", "gpu error", "device manager", "graphics driver", "nvidia amd"]
description: "Device Manager shows Code 43 on your GPU and Windows has stopped the device? Here's what the error means and the driver, power, and hardware fixes that clear it."
thumbnail: "/images/thumbs/how-to-fix-code-43-gpu-error-on-windows-11.webp"
faqs:
  - q: "What does Code 43 actually mean?"
    a: "Code 43 means Windows asked the device driver to start the hardware, the driver reported a problem, and Windows stopped the device to protect the system. It's deliberately vague — the code says 'the driver told me something is wrong' without specifying what. The underlying cause ranges from corrupted driver files to actual hardware failure, which is why the fixes below work from software toward hardware."
  - q: "Can a Windows update cause Code 43 on a GPU?"
    a: "Yes, frequently. Windows Update can install a GPU driver that's incompatible with your specific card or conflicts with the vendor's control software. If Code 43 appeared right after an update, rolling back the driver is the fastest fix. Blocking automatic driver updates afterward prevents the bad version from reinstalling itself overnight."
  - q: "Does Code 43 mean my graphics card is dead?"
    a: "Not necessarily — most Code 43 cases are driver or power problems, not dead silicon. The hardware-death verdict only comes after a clean driver reinstall, power checks, and testing the card in another machine all fail. Laptop GPUs are soldered, so 'another machine' testing isn't possible; there, the verdict comes from exhausting every software fix."
  - q: "Why does Code 43 keep coming back after I fix it?"
    a: "Recurring Code 43 usually means Windows Update is reinstalling the problematic driver version, or there's an intermittent hardware issue like a failing power connection or overheating GPU. Pin the working driver version by disabling automatic driver updates, and monitor GPU temperatures — thermal shutdowns can manifest as Code 43 on reboot."
---

Code 43 is Windows' way of saying "the driver reported a problem and I stopped the device." On a GPU, the symptoms are unmistakable: the discrete graphics card vanishes from games and GPU-accelerated apps, Device Manager shows a yellow warning on the display adapter, and the status reads "Windows has stopped this device because it has reported problems. (Code 43)." Your laptop keeps running on integrated graphics, so everything looks normal until you need real GPU power.

The error is frustratingly non-specific by design — it's a messenger, not a diagnosis. The fixes below work the problem the way a technician does: driver state first (most common), then power and thermal causes, then the hardware verdict. If you're dealing with driver issues more broadly, our [clean NVIDIA install guide](/articles/how-to-update-nvidia-drivers-clean-install/) is a useful companion.

## Why this happens

- **Corrupted GPU driver files.** Partial updates, crashed installers, or disk errors leave the driver in a state that fails initialization.
- **Incompatible driver version.** A too-new (or too-old) driver for your specific GPU and Windows build fails the driver's own self-check.
- **Windows Update installed the wrong driver.** The automatically delivered version conflicts with the vendor's driver stack.
- **Insufficient or unstable power.** On desktops, a weak PSU rail; on laptops, a failing adapter or power-management fault can trigger Code 43.
- **GPU overheating.** Thermal damage or clogged cooling causes initialization failures that the driver reports as Code 43.
- **Hardware failure.** Dead VRAM, a failed GPU core, or broken solder joints — the last resort diagnosis.
- **Conflicting software.** Overclocking tools, mining software remnants, or multiple GPU utilities fighting over the card.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart cleanly and check for transient causes

Code 43 can be a one-time initialization failure. Rule that out in two minutes.

1. Shut down the laptop completely (not sleep, not hibernate) and wait 30 seconds.
2. If the battery is removable, remove it; otherwise hold the power button 30 seconds with the charger disconnected to drain residual power.
3. Reconnect power and boot normally, then check Device Manager.
4. If the error is gone, it was a transient power-state failure — monitor for recurrence before doing more.

This "full power drain" resets the GPU's power state machine, which a normal reboot doesn't always do. It's the cheapest fix in this guide and resolves a real (if small) percentage of cases.

### Fix 2: Roll back the driver

If Code 43 appeared after a driver or Windows update, revert immediately.

1. Open **Device Manager > Display adapters**, right-click the GPU, and choose **Properties > Driver**.
2. Click **Roll Back Driver**, select a reason, and confirm.
3. Restart and check whether the error clears.
4. If rollback is unavailable, note the current driver version — you'll need it for the clean reinstall in Fix 3.

Don't skip this just because "the driver was working yesterday." Driver updates are the single most common Code 43 trigger, and rollback is a two-minute test. If it works, [disable automatic driver updates](/articles/how-can-i-disable-automatic-driver-updates/) so the bad version doesn't return.

### Fix 3: Clean-reinstall the GPU driver

The heavy hitter: purge the corrupted driver state completely and install fresh.

1. Download the latest driver for your exact GPU from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
2. Run the installer and choose **Custom > Clean install** (NVIDIA) or **Factory Reset** (AMD) to wipe all previous driver state.
3. Restart and verify in Device Manager that the yellow warning is gone.
4. Test with a GPU workload (a game or benchmark) — idle-desktop success isn't proof the driver initializes under load.

For NVIDIA cards specifically, our detailed [clean install walkthrough](/articles/how-to-update-nvidia-drivers-clean-install/) covers the full procedure including the pre-install preparation that makes the difference between a clean install and a merely fresh-looking one.

### Fix 4: Remove conflicting GPU software

Overclocking utilities and abandoned GPU tools can wedge the driver into Code 43.

1. Uninstall MSI Afterburner, EVGA Precision, ASUS GPU Tweak, or similar tools via **Settings > Apps**.
2. Check **Task Manager > Startup** for lingering GPU utility processes and disable them.
3. After uninstalling, repeat the clean driver install from Fix 3 — these tools leave registry and driver hooks behind.
4. Retest before reinstalling any tuning utility; add them back one at a time if you need them.

An unstable overclock is a classic Code 43 source: the driver fails its self-test at the overclocked settings and reports the device as faulty. If you were overclocking, reset to stock clocks first — the "hardware failure" may just be an unstable tune.

### Fix 5: Check power delivery

GPUs are power-hungry, and marginal power produces exactly this error.

1. On a laptop, verify you're using the original manufacturer charger at the correct wattage — underpowered third-party chargers cause GPU initialization failures.
2. Set **Settings > System > Power & battery > Power mode** to **Best performance** and retest.
3. In the manufacturer's power utility (or BIOS), check that the discrete GPU isn't power-limited or disabled.
4. On a desktop, verify all PCIe power connectors are seated and the PSU meets the GPU's requirements.

Laptop dGPUs can draw 80W+ on their own; a 65W charger on a laptop that shipped with 200W will absolutely cause GPU errors. This is also why Code 43 sometimes appears only on battery — the system can't feed the GPU.

### Fix 6: Address thermals

Heat-damaged or heat-stressed GPUs fail initialization and report Code 43.

1. Monitor GPU temperatures with HWiNFO or the vendor's tool — sustained idle temps above 70°C on a laptop suggest cooling failure.
2. Clean dust from vents and fans with compressed air; replace dried thermal paste if the machine is old and you're comfortable opening it.
3. Elevate the laptop for airflow and retest — if Code 43 clears when cool but returns under load, thermals are confirmed.
4. Check that fans actually spin under GPU load; a dead fan on a dGPU is a common finding.

Thermal Code 43 has a signature: the error appears after gaming or heavy use, clears after the machine cools, then returns. If you see that pattern, cooling service — not driver reinstalls — is the fix.

### Fix 7: Test the hardware verdict

When every software fix fails, it's time to determine whether the GPU itself is dead.

1. Boot a Linux live USB and check whether the GPU is detected and functional there — if yes, it's a Windows/driver problem you haven't fully solved.
2. On a desktop, move the card to another PCIe slot or another machine; on a laptop, this isn't possible — instead, run the manufacturer's built-in hardware diagnostics (Dell, HP, and Lenovo all ship GPU tests).
3. Check for artifacting (visual glitches, colored squares) which indicate VRAM failure rather than driver issues.
4. If diagnostics confirm GPU failure on a laptop, the repair is a motherboard replacement — get a quote before deciding, as it may exceed the machine's value.

A Code 43 that survives a clean driver install, correct power, good thermals, and Linux testing is a hardware fault. At that point, further software attempts waste time — the decision becomes repair versus replace.

## Closing

Code 43 is a process of elimination with a clear gradient: transient power state, bad driver version, corrupted driver, conflicting software, power delivery, thermals, hardware. The overwhelming majority resolve in the first four fixes — which is why driver hygiene (clean installs, blocking bad auto-updates) prevents most recurrences. If you reach Fix 7 with the error intact, you've earned the hardware verdict honestly, and you can act on it without second-guessing.
