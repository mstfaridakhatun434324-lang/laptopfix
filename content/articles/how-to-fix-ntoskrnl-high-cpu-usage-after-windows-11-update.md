---
title: "Fix Ntoskrnl High CPU Usage After a Windows 11 Update"
slug: how-to-fix-ntoskrnl-high-cpu-usage-after-windows-11-update
date: 2026-10-08
categories: ["performance"]
tags: ["ntoskrnl", "high cpu", "windows 11 update", "ntoskrnl.exe", "kernel cpu"]
description: "Diagnose ntoskrnl.exe high CPU after a Windows 11 update: find the misbehaving driver, fix memory compression, and calm kernel CPU usage."
thumbnail: "/images/thumbs/how-to-fix-ntoskrnl-high-cpu-usage-after-windows-11-update.webp"
faqs:
  - q: "What is ntoskrnl.exe and why does it use CPU?"
    a: "Ntoskrnl.exe is the Windows kernel itself — the core of the operating system handling memory, processes, and hardware abstraction. It shows CPU usage when kernel-mode work is heavy, but it's almost never the actual culprit. High ntoskrnl CPU after an update means some driver or kernel component the update touched is misbehaving, and the kernel is just where the cost appears. The fix is finding that driver, not touching the kernel."
  - q: "Is ntoskrnl.exe a virus?"
    a: "No. Ntoskrnl.exe is a legitimate, essential Windows system file located in C:\\Windows\\System32. Malware sometimes uses similar-looking names, but the real file in System32 with a valid Microsoft signature is safe. If Task Manager shows high CPU on the genuine ntoskrnl.exe, the cause is a driver or system issue — never delete or 'fix' the file itself."
  - q: "Why did ntoskrnl CPU spike right after a Windows update?"
    a: "Updates replace drivers, change kernel behavior, and reset settings like memory compression. A storage or network driver that worked on the old build can generate excessive interrupts or DPCs on the new one, and that kernel-mode cost shows up under ntoskrnl.exe. Memory compression settings and outdated drivers are the two most common update-triggered causes."
  - q: "Can I disable ntoskrnl.exe to stop the CPU usage?"
    a: "Absolutely not. Ntoskrnl.exe is the Windows kernel — terminating it crashes the system instantly. It also can't be uninstalled or disabled. Any guide suggesting you delete or block it is dangerous misinformation. The correct approach is diagnosing which driver or subsystem is generating the kernel load and fixing that component."
---

Seeing **ntoskrnl.exe** at the top of Task Manager with 20–40% CPU right after a Windows 11 update is alarming — the name looks cryptic, the process can't be ended, and forum threads are full of bad advice. Here's the calm truth: ntoskrnl.exe is the Windows kernel, and it's essentially never the villain. It's the *location* where the cost of some other misbehaving component shows up. Your job is detective work: find what's making the kernel work so hard, and fix that.

Post-update ntoskrnl spikes have a short list of usual suspects — outdated drivers colliding with the new build, memory compression working overtime, or a stuck servicing process. This guide walks you through identifying the real cause and fixing it, without touching the kernel itself.

## Why this happens

- **Outdated drivers on the new build:** The update changes kernel interfaces; old storage, network, or chipset drivers generate excessive interrupts (DPCs) that bill to ntoskrnl.
- **Memory compression working overtime:** The update can reset or intensify memory compression, and compressing/decompressing RAM constantly costs kernel CPU.
- **Corrupted system files:** A partially applied update leaves kernel components in a bad state, causing inefficient kernel-mode loops.
- **Stuck update servicing:** TiWorker.exe and related processes doing kernel-heavy work during a wedged update appear partly under system processes.
- **Faulty RAM:** Bad memory causes the kernel's memory manager to work overtime handling errors — memtest territory.
- **Third-party drivers with kernel hooks:** Antivirus filter drivers, VPN clients, and disk utilities hook the kernel; outdated versions thrash after an update.
- **Power plan and firmware mismatch:** The new build's power management fighting outdated BIOS/firmware generates excessive kernel power-transition work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's really ntoskrnl and check the pattern

Open Task Manager → **Details**, confirm **ntoskrnl.exe** (listed as "System" in the Processes tab) is the high-CPU entry, and note whether it's constant or tied to activity. Then open **Resource Monitor** (search for it in Start) → **CPU** tab and check the **DPC** and **Interrupt** load — high DPC/interrupt time alongside ntoskrnl points squarely at a driver problem rather than memory compression.

1. Task Manager → Details → confirm ntoskrnl.exe sustained high CPU.
2. Open Resource Monitor → CPU tab; note DPC and interrupt percentages.
3. High DPC/interrupts = driver issue (Fix 3); low DPC with high ntoskrnl = memory/system cause (Fix 2/4).
4. Record the pattern before changing anything.

### Fix 2: Check memory compression and memory pressure

Memory compression shows under ntoskrnl/System. Open Task Manager → **Performance → Memory** and check the **Compressed** figure and overall pressure. If memory is nearly full and compression is working hard, the kernel CPU is a symptom of RAM pressure — close heavy apps or add RAM. You can test with compression temporarily disabled (elevated PowerShell: `Disable-MMAgent -mc`), but only as a diagnostic; don't leave it off permanently without understanding the tradeoff.

1. Check Performance → Memory: Compressed size and total pressure.
2. If memory is maxed, close heavy apps and re-observe.
3. Diagnostic only: elevated PowerShell → `Disable-MMAgent -mc` → reboot → observe.
4. Re-enable with `Enable-MMAgent -mc` after testing unless pressure is resolved by other means.

### Fix 3: Update the drivers the update disturbed

Prioritize **chipset**, **storage (Intel RST/AMD)**, **network (Wi-Fi/Ethernet)**, and **graphics** drivers — in that order — from your laptop manufacturer's support site, matched to the new Windows build. These are the drivers whose kernel-mode misbehavior bills to ntoskrnl. Don't rely on Windows Update's generics for this step; get the manufacturer's validated versions.

1. Identify your exact model and current Windows build (**Settings → System → About**).
2. Download chipset, storage, network, and graphics drivers from the manufacturer's site.
3. Install in that order, rebooting between major ones.
4. Re-observe ntoskrnl CPU for an hour. Related kernel-level CPU on specific brands is covered in the [system interrupts guides](/articles/how-to-fix-system-interrupts-high-cpu-after-windows-11-update/).

### Fix 4: Repair update corruption

A wedged update leaves the kernel doing redundant work. Run the standard repair sequence elevated: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`. Then run **Settings → System → Troubleshoot → Other troubleshooters → Windows Update**, and install any pending updates. This resolves the "update half-applied" state that keeps kernel workers busy.

1. Elevated Command Prompt: `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run the Windows Update troubleshooter; install pending updates.
4. Restart; observe over several hours. Microsoft's servicing help: [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Remove or update kernel-hooking third-party software

Antivirus filter drivers, VPN clients, disk encryption, and "system optimizer" tools hook into the kernel. After a build update, outdated hooks are a prime ntoskrnl-CPU source. Temporarily uninstall VPN clients and third-party antivirus (keeping Defender), reboot, and observe. If CPU normalizes, reinstall only the latest versions — or leave them off if you don't need them.

1. Inventory kernel-hooking software: VPNs, third-party AV, disk tools.
2. Uninstall them temporarily (one category at a time).
3. Reboot and observe ntoskrnl CPU after each removal.
4. Reinstall only current versions of what you actually need.

### Fix 6: Test the RAM

Faulty RAM makes the kernel's memory manager work overtime, and it can absolutely appear as ntoskrnl CPU. Run **Windows Memory Diagnostic** (search in Start → Restart now and check), or better, boot **MemTest86** from USB for a thorough multi-pass test. Even one error means the stick needs replacing — no software fix compensates for bad hardware.

1. Search **Windows Memory Diagnostic** → Restart now and check for problems.
2. For a definitive test, run MemTest86 from a bootable USB (several passes).
3. Any errors → replace the faulty RAM stick.
4. Re-observe after replacement.

### Fix 7: Update BIOS/firmware and consider rollback

Outdated BIOS/UEFI firmware interacting with a new Windows build's power management generates kernel overhead. Check your manufacturer's support site for a BIOS update (apply on AC power, uninterrupted). If ntoskrnl CPU began exactly with the update and nothing else helps, the 10-day rollback (**Settings → System → Recovery → Go back**) is the last resort — it returns the driver/kernel pairing that worked. The [Lenovo system-interrupts walkthrough](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-on-lenovo-laptop/) covers adjacent kernel-CPU diagnosis if you need a second angle.

1. Check for a BIOS/firmware update from the manufacturer; apply carefully.
2. If onset matches the update exactly and all else failed, use **Go back** within 10 days.
3. After rollback, pause feature updates while researching the driver conflict.
4. Document the working driver versions for next time.

## Closing

Ntoskrnl.exe high CPU after a Windows 11 update is the kernel telling you something underneath changed — usually a driver the update disturbed, memory compression under pressure, or servicing that didn't finish cleanly. Don't fight the kernel; interrogate it. Update the drivers, repair the update, test the RAM, and the kernel goes back to the quiet background work it does best.
