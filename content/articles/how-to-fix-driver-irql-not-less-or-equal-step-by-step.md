---
title: "DRIVER_IRQL_NOT_LESS_OR_EQUAL: Fix It Step by Step"
slug: how-to-fix-driver-irql-not-less-or-equal-step-by-step
date: 2026-09-02
categories: ["windows-errors"]
tags: ["blue screen", "driver irql", "windows 11", "stop code 0xD1", "driver fix"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen? This step-by-step guide finds the faulty driver behind stop code 0xD1 and fixes it for good."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-step-by-step.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "A driver tried to access memory at an improper interrupt request level — stop code 0x000000D1. In plain terms, a driver touched memory it wasn't allowed to touch at that moment. It's faulty-driver territory in the vast majority of cases."
  - q: "Which driver is causing it?"
    a: "The blue screen often names the .sys file. Common ones: ndis.sys (network), nvlddmkm.sys (NVIDIA), Netwtw12.sys (Intel Wi-Fi). If no file is shown, analyze the minidump with WinDbg or update the usual suspects: network, graphics, and storage drivers."
  - q: "Can bad RAM cause DRIVER_IRQL_NOT_LESS_OR_EQUAL?"
    a: "Yes, though it's less common than a driver bug. If the blamed driver changes with every crash, test your RAM — inconsistent blame is the signature of memory corruption rather than one bad driver."
  - q: "Why does it happen when I connect to Wi-Fi?"
    a: "Because the Wi-Fi driver is the one misbehaving. Network drivers run at raised IRQL constantly, so a buggy wireless driver triggers 0xD1 the moment it does real work. Updating or replacing the Wi-Fi driver fixes it."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL (stop code 0xD1) is the most famous blue screen in Windows history, and it means exactly what it says: a driver tried to access memory at the wrong privilege level. Drivers operate at different "interrupt request levels," and touching pageable memory while running at a high IRQL is illegal — Windows enforces the rule with an instant crash. The good news: this is one of the most diagnosable stop codes, because the crash dump almost always names the offender.

Here's the step-by-step sequence that finds and fixes it, ordered so the most likely culprits get checked first.

## Why this happens

- **Faulty network drivers.** Wi-Fi and Ethernet drivers run at high IRQL by nature, making them the number one 0xD1 source — especially after Windows Update swaps them.
- **Buggy GPU drivers.** Graphics drivers touch memory at raised IRQL during rendering; bad releases crash under gaming or video workloads.
- **Corrupted driver installations.** Half-applied updates leave driver files mismatched, producing illegal memory accesses.
- **Antivirus filter drivers.** Kernel network and filesystem filters operate at elevated IRQL and are frequent offenders.
- **Failing RAM.** Corrupts driver code and data, producing 0xD1 crashes that blame different drivers each time.
- **Overclocked or unstable hardware.** Timing violations make drivers misbehave at the exact moments IRQL rules are strictest.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Note the named driver on the blue screen

The crash often hands you the answer.

1. Next time it blue-screens, look for a filename like `ndis.sys`, `nvlddmkm.sys`, or `Netwtw12.sys` on the screen — photograph it if it flashes by.
2. Map it: `ndis.sys` → network stack (update Wi-Fi/Ethernet), `nvlddmkm.sys` → NVIDIA GPU, `storahci.sys` → storage controller.
3. If the screen disappears too fast, disable auto-restart (see our [automatic restart guide](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/)) so you can read it next time.
4. Check `C:\Windows\Minidump` for dump files to analyze later if needed.

### Fix 2: Update the network drivers

Network drivers cause most 0xD1 crashes — start here.

1. Open **Device Manager > Network adapters** and identify your Wi-Fi and Ethernet chips.
2. Download the latest drivers from your laptop manufacturer's support page (OEM-validated beats generic).
3. Uninstall the current drivers first (tick **Attempt to remove the driver**), then install the fresh ones.
4. For Intel wireless, [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the newest stable build.
5. Restart and test — especially the activity that triggered crashes (video calls, large downloads, gaming).

The update-triggered variant is covered in our [DRIVER_IRQL_NOT_LESS_OR_EQUAL after Windows 11 update guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/).

### Fix 3: Clean-install the GPU driver

The second most common culprit.

1. Download the latest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html).
2. Boot into **Safe Mode** (interrupt startup three times → **Troubleshoot > Advanced options > Startup Settings**).
3. In **Device Manager**, uninstall the display adapter, ticking driver removal.
4. Restart normally and install the downloaded driver with **clean installation** selected.
5. Skip beta/Game Ready hotfix drivers if stability is the priority.

### Fix 4: Remove antivirus filter drivers temporarily

Security software hooks the network stack at elevated IRQL.

1. Uninstall third-party antivirus via **Settings > Apps > Installed apps**.
2. Run the vendor's removal tool to clear leftover filter drivers.
3. Restart and test on **Microsoft Defender** for a few days.
4. If crashes stop, the antivirus filter was guilty — update it or switch products.
5. Also temporarily disable any third-party firewall with kernel components.

### Fix 5: Test RAM and repair system files

Cover hardware memory and Windows corruption.

1. Press **Windows + R**, type `mdsched.exe`, and run the memory diagnostic.
2. Check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
3. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow`.
4. If RAM fails, isolate and replace the bad stick.
5. If crashes blame a different driver every time even with good RAM, suspect the motherboard or run MemTest86 overnight for a deeper check.

### Fix 6: Use Driver Verifier to confirm the culprit

When you need proof before replacing a driver.

1. Press **Windows + R**, type `verifier.exe`, and press Enter.
2. Choose **Create standard settings**, then select the suspected drivers (or all unsigned drivers).
3. Restart — Verifier will crash the guilty driver quickly and identifiably.
4. Boot to Safe Mode, run `verifier /reset` in an admin Command Prompt, then fix the identified driver.
5. Don't leave Verifier on permanently.

For the 24H2-specific variant, see [DRIVER_IRQL_NOT_LESS_OR_EQUAL in Windows 11 24H2](/articles/how-to-fix-driver-irql-not-less-or-equal-in-windows-11-24h2/).

### Fix 7: Reset the network stack

A corrupted network stack can mimic driver faults.

1. Open **Terminal (Admin)**.
2. Run `netsh winsock reset` and press Enter.
3. Run `netsh int ip reset` and press Enter.
4. Run `ipconfig /flushdns`.
5. Restart the laptop and test network-heavy activity.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is the blue screen equivalent of a signed confession — the dump usually names the driver, and the fix is updating or replacing that one driver. Work the network angle first, then graphics, then security filters, and use Driver Verifier when you need certainty. It's a common crash with an uncommonly straightforward cure.

A final note on prevention: most 0xD1 crashes arrive via driver updates, whether from Windows Update or manual installs. Before updating network or graphics drivers, create a system restore point (**Control Panel > System > System Protection > Create**) — it takes a minute and gives you a one-click undo if the new driver misbehaves. And when a driver update does trigger crashes, report it: use **Feedback Hub** for Windows Update drivers or the vendor's support channel for manual installs. Buggy drivers only get fixed when the people who ship them hear about the crashes.
