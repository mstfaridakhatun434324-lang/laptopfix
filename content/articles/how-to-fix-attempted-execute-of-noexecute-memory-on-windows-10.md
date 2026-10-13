---
title: "Fix ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY on Windows 10"
slug: how-to-fix-attempted-execute-of-noexecute-memory-on-windows-10
date: 2026-09-20
categories: ["windows-errors"]
tags: ["attempted execute of noexecute memory", "blue screen", "windows 10"]
description: "Fix the ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen on Windows 10: update drivers, test memory, and remove the bad software causing it."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-on-windows-10.webp"
faqs:
  - q: "What is ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY?"
    a: "It is stop code 0x000000FC: a driver tried to run program code from a memory region marked non-executable. Windows uses Data Execution Prevention to block this, and crashes rather than allow it. A faulty or outdated driver is the cause in nearly every case."
  - q: "Is this error caused by a virus?"
    a: "Rarely, but it is possible — malware sometimes injects code into memory regions where it does not belong. Run a full scan with Microsoft Defender first to rule it out, then focus on drivers, which are the cause the vast majority of the time."
  - q: "Can bad RAM cause this blue screen?"
    a: "Yes. Failing memory can flip the attributes of memory pages or corrupt driver code in transit, producing exactly this stop code. If driver updates do not help, run Windows Memory Diagnostic before assuming anything else."
  - q: "Why does it happen when I play games or run heavy apps?"
    a: "Graphics and audio drivers work hardest under load, so a buggy driver only trips the no-execute protection when pushed. Updating the graphics driver and chipset driver fixes most load-triggered cases."
---

The ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen — stop code 0x000000FC — is Windows' memory bodyguard doing its job. A driver tried to execute code from a memory page marked "data only," which is exactly the kind of thing exploits do. Windows killed the session instantly rather than risk it.

On Windows 10 this crash almost always traces back to one outdated or corrupted driver, most often graphics, chipset, or network. The fixes below walk you from the easy wins to the deeper checks, in the order a technician would actually try them.

## Why this happens

- **Outdated graphics driver:** The single most common trigger. Old GPU drivers misbehave with newer Windows 10 builds and trip Data Execution Prevention.
- **Corrupted driver installation:** A driver that installed badly — interrupted download, failed update — can attempt to run from the wrong memory region.
- **Failing RAM:** Bad memory cells corrupt page attributes or driver code, producing this exact stop code even with perfect drivers.
- **Third-party antivirus or VPN drivers:** Kernel-level security and networking software runs in sensitive memory areas; an outdated version is a classic culprit.
- **Overclocked CPU or RAM:** Unstable overclocks corrupt execution flow. If you run XMP or a CPU overclock, this error can appear out of nowhere.
- **Malware:** Some infections inject code into protected memory. Unlikely, but worth ruling out with a scan before you spend hours on drivers.
- **Windows system file corruption:** Damaged kernel files can mismanage memory protection flags after a bad update or sudden power loss.

## How to fix it

Work through these in order — most cases resolve by Fix 3.

### Fix 1: Scan for malware first to rule it out

1. Open **Settings → Privacy & Security → Windows Security → Virus & threat protection**.
2. Click **Scan options → Full scan → Scan now**. A full scan takes 30–60 minutes.
3. If anything is found, remove it and restart. Retest for a day before moving on.
4. If the scan is clean, you can confidently focus on drivers and hardware — the cause is almost certainly not malware. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has additional scanning guidance if Defender will not start.

### Fix 2: Update your graphics driver from the official source

1. Find out your GPU: press **Win + R**, type `dxdiag`, press Enter, and check the **Display** tab.
2. Download the latest driver directly from the manufacturer's site — [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx), AMD's driver page, or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html).
3. During NVIDIA/AMD installation choose **Custom → Clean installation** to wipe the old driver completely.
4. Restart and use the laptop normally. Graphics drivers are the number one fix for this stop code, so do not settle for the version Windows Update offers.

### Fix 3: Update chipset and network drivers

1. Visit your laptop manufacturer's support page (Dell, HP, Lenovo, ASUS, Acer) and download the latest **chipset** driver for your exact model.
2. Update **Wi-Fi** and **Bluetooth** drivers from the same page — network drivers are the second most common trigger.
3. In **Device Manager**, expand each category, right-click the device, and use **Update driver → Search automatically** only if the manufacturer's site has nothing newer.
4. Restart after installing. If the crashes were network-related, they typically vanish after this step.

### Fix 4: Remove recently installed software and its drivers

1. Open **Settings → Apps → Installed apps** and sort by install date.
2. Uninstall anything added just before the crashes started — VPN clients, virtual machine tools, RGB utilities, and third-party antivirus are prime suspects.
3. After uninstalling, check **Device Manager → View → Show hidden devices** for leftover greyed-out entries from that software and uninstall those too.
4. Restart and test for a day. Kernel-level software you installed last month and forgot about is a very common hidden cause.

### Fix 5: Run SFC and DISM to repair system files

1. Right-click **Start → Windows Terminal (Admin)** (or Command Prompt as administrator).
2. Run `sfc /scannow` and wait for it to complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the Windows image itself.
4. Restart. If system files were corrupted by a bad update or a hard shutdown, this pair of commands clears it up.

### Fix 6: Test your RAM with Windows Memory Diagnostic

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Select **Restart now and check for problems** and let the test run to completion.
3. If errors are reported, power off, reseat the RAM modules (if your laptop allows access), and retest.
4. If errors persist, the RAM itself is failing and needs replacement — no driver update fixes bad memory. Persistent errors also warrant a look at other [memory-related blue screens](/articles/how-to-fix-stop-code-memory-management/) since the symptoms overlap.

### Fix 7: Reset BIOS settings and disable overclocks

1. Restart and enter the BIOS (usually **F2**, **Del**, or **Esc** at boot, depending on brand).
2. Find **Load Optimized Defaults** or **Load Setup Defaults** and apply it — this clears any CPU or RAM overclock, including XMP.
3. While there, check that **Data Execution Prevention (DEP)** is enabled under CPU/security settings; it should be on by default.
4. Save and exit. If the overclock was the problem, the crashes stop immediately and permanently.

### Fix 8: Reset overclocks and verify DEP is enforcing

If an overclock is corrupting execution flow, no driver update will hold. Reset firmware to stock and confirm Data Execution Prevention is actually enforcing its policy.

1. Restart into the BIOS and choose **Load Optimized Defaults** to clear XMP, CPU, and GPU overclocks.
2. In Windows, press **Win + R**, type `sysdm.cpl`, and go to **Advanced → Performance → Settings → Data Execution Prevention**.
3. Confirm it is set to **Turn on DEP for essential Windows programs and services only** (the Windows default).
4. Save, restart, and stress-test with the workload that used to crash. If the system is now stable, the overclock was corrupting execution — leave it off or re-tune it conservatively.
5. For context on other execution-related crashes, our [IRQL guide](/articles/irql-not-less-or-equal-bsod-windows-11/) covers the closely related stop code.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY sounds like a security incident, but on Windows 10 it is a driver maintenance issue far more often than anything sinister — usually the graphics driver, sometimes chipset or network, occasionally the RAM itself. Rule out malware, refresh drivers from official sources, strip out recent kernel-level software, repair system files, test the memory, and reset any overclocks. Worked in order, that sequence ends this crash for nearly everyone who sees it.
