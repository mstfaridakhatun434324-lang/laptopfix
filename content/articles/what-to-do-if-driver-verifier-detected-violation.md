---
title: "What to Do When Driver Verifier Flags a Violation"
slug: what-to-do-if-driver-verifier-detected-violation
date: 2026-09-21
categories: ["windows-errors"]
tags: ["driver verifier", "bsod", "driver troubleshooting"]
description: "Seeing DRIVER_VERIFIER_DETECTED_VIOLATION? Learn what it means, which driver caused it, and how to turn Verifier off and fix the bad driver for good."
thumbnail: "/images/thumbs/what-to-do-if-driver-verifier-detected-violation.webp"
faqs:
  - q: "What does DRIVER_VERIFIER_DETECTED_VIOLATION mean?"
    a: "It means Driver Verifier, a Windows testing tool, caught a driver breaking the rules, such as freeing memory twice or using an invalid address. The tool itself is working as intended; the fault lies with the driver it flagged, and the stop code naming it is usually right next to the error."
  - q: "How do I turn off Driver Verifier?"
    a: "Open an elevated Command Prompt and run `verifier /reset`, then restart your laptop. If Windows will not boot normally, go to the recovery environment, open Command Prompt from the troubleshooting menu, and run `verifier /reset` there before rebooting. Verifier stays off until you deliberately enable it again."
  - q: "Which driver is causing the violation?"
    a: "Open the minidump at C:\\Windows\\Minidump with WinDbg Preview from the Microsoft Store, or run the free BlueScreenView tool. The analysis names the faulting driver file, for example something.sys, which tells you exactly which device or software to update, roll back, or uninstall."
  - q: "Is Driver Verifier safe to use?"
    a: "Yes, but only briefly and on purpose. It is a diagnostic tool that deliberately crashes Windows when a driver misbehaves, so your system will keep blue-screening while it is active. Always reset it with `verifier /reset` once you have identified the culprit, and do not leave it running during normal use."
---
A Driver Verifier crash is one of the few blue screens that is actually good news in disguise. It means you, or someone helping you, deliberately switched on Windows' built-in driver testing tool, and it caught a misbehaving driver red-handed. The stop code DRIVER_VERIFIER_DETECTED_VIOLATION tells you exactly which component is at fault — it just does it in the most dramatic way possible.

The important thing to understand is that Verifier itself is not broken. It is doing its job: stressing drivers until one of them violates the rules, then forcing a blue screen so the violation gets recorded in a memory dump. Your real task is reading that dump, fixing or replacing the bad driver, and then switching Verifier off so your laptop behaves normally again.

## Why this happens

- **A faulty or outdated driver is breaking Windows' driver rules.** Verifier caught it doing something illegal, like freeing the same memory twice, accessing an invalid memory address, or mishandling interrupt requests.
- **A recently installed driver is unstable.** The crash often starts right after a driver update for Wi-Fi, graphics, audio, or chipset components — the new version contains a bug Verifier exposes.
- **A third-party utility installed a kernel driver.** Antivirus tools, VPN clients, fan-control apps, and RGB software all install low-level drivers that Verifier scrutinizes closely.
- **Corrupted driver files.** A failed update or disk error can corrupt a driver binary, causing it to behave erratically when Verifier applies its checks.
- **Verifier was left enabled.** Someone ran `verifier` during troubleshooting and forgot to reset it, so the laptop keeps crashing during normal use.
- **An old driver is incompatible with your Windows version.** Drivers written for older Windows releases can trip Verifier's stricter checks on Windows 10 or 11.

## How to fix it

Work through these in order — each fix builds on the information the last one gave you. Start with identifying the culprit, then neutralize it, then switch Verifier off.

### Fix 1: Find the faulting driver in the minidump

The crash dump recorded exactly which driver file caused the violation, and reading it takes five minutes.

1. Boot into **Safe Mode** if normal boot keeps crashing: hold **Shift** while clicking **Restart**, then go to **Troubleshoot > Advanced options > Startup Settings > Restart** and press **4**.
2. Install **WinDbg Preview** from the Microsoft Store, or download the portable BlueScreenView tool.
3. Open the most recent dump at `C:\Windows\Minidump\` in your analysis tool.
4. In WinDbg, run the command `!analyze -v` and read the MODULE_NAME and IMAGE_NAME lines — they name the driver, e.g. `rtwlanu.sys`.
5. Note the driver name and which device it belongs to (graphics, Wi-Fi, audio, and so on) before moving on.

### Fix 2: Update the identified driver properly

Once you know the driver name, the safest move is a clean update from the real source rather than whatever Windows last installed.

1. Press **Win + X** and open **Device Manager**.
2. Expand the category matching the faulty driver (for example **Network adapters** for a Wi-Fi driver).
3. Right-click the device, choose **Uninstall device**, and tick **Attempt to remove the driver for this device** if the option appears.
4. Restart the laptop so Windows installs a baseline driver.
5. Download the newest driver from the laptop maker's site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/)) or the component vendor, and install it manually.
6. For graphics, get the driver straight from the source instead of relying on generic updates — [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) — since GPU drivers are a classic Verifier trigger.

### Fix 3: Roll back if the crash started after a driver update

If the blue screens began right after a driver update, the new version is the problem, not the old one.

1. Open **Device Manager** and double-click the suspect device.
2. Switch to the **Driver** tab and click **Roll Back Driver**; pick a reason and confirm.
3. If the button is greyed out, use **System Restore**: search for **Recovery** in the Start menu, open it, and choose **Open System Restore** to return to a point before the update.
4. Pause automatic driver updates afterwards: go to **Settings > Windows Update > Advanced options > Optional updates** and avoid reinstalling the same bad version.

### Fix 4: Remove suspect third-party kernel drivers

Antivirus suites, VPN clients, and hardware utilities install drivers that love to trip Verifier.

1. Go to **Settings > Apps > Installed apps** and uninstall any antivirus, VPN, or system-utility software you added recently.
2. In **Device Manager**, click **View > Show hidden devices** and look under **Non-Plug and Play Drivers** (or **Software devices**) for leftovers from those programs.
3. Right-click any leftover entry and choose **Uninstall device**.
4. Restart and see whether the crashes stop — this alone resolves a surprising number of Verifier violations, similar to how leftover drivers also cause [DRIVER_IRQL_NOT_LESS_OR_EQUAL](/articles/how-to-fix-driver-irql-not-less-or-equal-reddit/) crashes.

### Fix 5: Run system file and image checks

A corrupted driver binary or damaged system file can behave badly under Verifier's checks even when the driver version is correct.

1. Open an elevated **Command Prompt**: search for **cmd**, right-click it, and choose **Run as administrator**.
2. Run `sfc /scannow` and wait for it to finish — this repairs protected system files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store that SFC draws from.
4. Restart the laptop and check whether Verifier still flags a violation.

### Fix 6: Reset Driver Verifier to stop the forced crashes

Once you have identified and fixed the bad driver, Verifier has done its job — switch it off so Windows stops crashing on purpose.

1. Open an elevated **Command Prompt** and run `verifier /reset`.
2. Restart the laptop; Verifier is now disabled.
3. Confirm it is off by running `verifier /query` — it should report that no drivers are being verified.
4. If Windows will not boot to a command prompt, boot to recovery (**Shift + Restart > Troubleshoot > Advanced options > Command Prompt**) and run `verifier /reset` from there.
5. Only re-enable Verifier if you are actively diagnosing another driver problem, and always reset it afterwards.

### Fix 7: Update Windows and firmware

Outdated kernels and firmware can make Verifier overly aggressive or expose genuine incompatibilities.

1. Go to **Settings > Windows Update** and install every pending update, then restart.
2. Check your laptop maker's support page for BIOS/UEFI firmware updates and install any that apply — firmware bugs are a known Verifier trigger on some models.
3. After updating, run `verifier /standard /all` only if you are still diagnosing; otherwise leave Verifier reset.

## Closing

A Driver Verifier violation looks scary, but it is Windows telling you exactly where to look. Read the minidump to name the driver, replace or roll back that driver, remove suspicious third-party kernel software, and finish with `verifier /reset` so the deliberate crashing stops. If the same driver keeps failing even after a clean reinstall, report the bug to the vendor — some drivers are simply broken, and no amount of reinstalling will fix a bad binary. For step-by-step help booting into Safe Mode to perform these fixes, see the guide on [booting Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).
