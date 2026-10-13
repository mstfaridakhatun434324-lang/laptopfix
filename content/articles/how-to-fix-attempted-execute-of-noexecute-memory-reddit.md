---
title: "How to Fix the ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY BSOD"
slug: how-to-fix-attempted-execute-of-noexecute-memory-reddit
date: 2026-09-30
categories: ["windows-errors"]
tags: ["attempted execute of noexecute memory", "bsod", "0xfc", "dep", "driver error"]
description: "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY blue screen (0xFC)? A driver tried to run code from protected memory — here's how to find and fix it."
thumbnail: "/images/thumbs/how-to-fix-attempted-execute-of-noexecute-memory-reddit.webp"
faqs:
  - q: "What is no-execute memory?"
    a: "Modern CPUs mark memory regions as non-executable (the NX bit / Data Execution Prevention) so data areas cannot be run as code — a key defense against malware. When a driver tries to execute code from such a region, the CPU refuses and Windows crashes with this stop code. It means a driver violated a fundamental memory safety rule."
  - q: "Is this error caused by a virus?"
    a: "Almost never. Malware does try to execute code from data regions, which is exactly what DEP is designed to stop — but on a normal user's laptop, this stop code is overwhelmingly caused by buggy legitimate drivers, not malware. Still, running a full Windows Security scan is cheap peace of mind while you troubleshoot."
  - q: "Why do forums say to check RAM for this error?"
    a: "Because corrupted RAM can garble the page-table flags that mark memory as executable or not, making good drivers look like violators. It is a less common cause than drivers, but the symptom overlap is real — which is why a memory test is part of every solid 0xFC troubleshooting sequence."
  - q: "Can outdated BIOS cause this?"
    a: "Yes, indirectly. The BIOS/UEFI configures CPU memory-protection features at boot. Outdated firmware can misconfigure DEP/NX settings or mishandle the handoff to Windows, and vendors do ship firmware fixes for memory-protection issues. Updating the BIOS is a legitimate step if driver fixes do not resolve it."
---
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY (0x000000FC) is Windows' Data Execution Prevention catching a driver trying to run code from memory marked "data only." The CPU itself raises the alarm, and Windows blue-screens rather than let it proceed. It is the kind of error that sends people down forum rabbit holes — let's skip the rabbit hole and go straight to what works.

In practice, this is a driver bug in the large majority of cases, with bad RAM as the runner-up. The sequence below finds which one you have.

## Why this happens

- **Buggy driver executing from a data page:** The classic cause — a driver bug makes it jump to an address in non-executable memory.
- **Outdated drivers predating DEP enforcement:** Old drivers written before strict NX-bit enforcement trip over modern protections.
- **Corrupted driver binaries:** Damaged driver files on disk execute unpredictably.
- **Faulty RAM corrupting page-table flags:** Bad memory garbles the executable/non-executable markings, framing innocent drivers.
- **Antivirus and virtualization drivers:** These manipulate memory protections by design and are frequent 0xFC offenders when outdated.
- **Overclocking instability:** Unstable CPU/RAM produces erratic execution that lands in protected regions.
- **Corrupted system files:** Damaged Windows components can violate their own memory protections.

## How to fix it

Work through these in order, starting at Fix 1.

### Fix 1: Identify the violating driver from the dump

1. Press **Win + R**, type `%SystemRoot%\Minidump`, press Enter; open the newest `.dmp` in BlueScreenView (free, NirSoft).
2. Note any highlighted third-party `.sys` driver — that is your prime suspect for Fix 2.
3. If the dump only blames `ntoskrnl.exe`, continue through the sequence; Fix 5's verifier step will expose the real culprit.

For the Windows Update-triggered variant, see [fixing this error after a Windows 11 update](/articles/how-to-fix-attempted-execute-of-noexecute-memory-after-windows-11-update/).

### Fix 2: Update the suspect driver — and the usual suspects

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Update the driver named in the dump first: right-click → **Update driver > Search automatically for drivers**.
3. Then proactively update **Display adapters**, **Network adapters**, and **System devices** — the three families most implicated in 0xFC.
4. Check your laptop manufacturer's support page for validated versions, since Windows Update lags behind vendor releases.
5. Restart and test with the workload that triggered the crash.

### Fix 3: Roll back recent driver or Windows updates

If the crashes started days after an update, reverse it.

1. **Device Manager** → suspect device → **Properties** → **Driver** → **Roll Back Driver**.
2. Or **Settings > Windows Update > Update history > Uninstall updates** → remove the recent update.
3. Restart, monitor for 48 hours. The 24H2-specific variant is covered in our [0xFC on Windows 11 24H2 guide](/articles/how-to-fix-attempted-execute-of-noexecute-memory-in-windows-11-24h2/).

### Fix 4: Test the RAM

Because corrupted page-table flags mimic driver violations:

1. **Win + R** → `mdsched.exe` → **Restart now and check for problems**.
2. Check **Event Viewer > Windows Logs > System** for **MemoryDiagnostics-Results**.
3. Errors → reseat/replace RAM. Clean → continue with confidence that drivers are the issue.

### Fix 5: Use Driver Verifier to catch it red-handed (advanced)

1. **Win + R** → `verifier` → **Create standard settings** → **Select driver names from a list** → tick non-Microsoft drivers (network, graphics, antivirus, virtualization).
2. **Finish**, restart, use the laptop normally. Verifier forces an immediate, well-labeled crash on the violator.
3. Read the new dump to name the driver, then boot to Safe Mode and run `verifier /reset` to switch Verifier off. Do not leave it enabled.

### Fix 6: Remove or update antivirus and virtualization software

These manipulate memory protections by design, so outdated versions are prime suspects.

1. **Settings > Apps > Installed apps** → uninstall third-party antivirus and any virtualization tools (old VMware/VirtualBox versions, Android emulators) temporarily.
2. Restart, test for a day or two. Windows Security covers you meanwhile.
3. If stable, reinstall only current versions from official sources.

### Fix 7: Update BIOS and repair system files

The firmware-and-foundation pass:

1. Check your BIOS version with `msinfo32` (**Win + R** → `msinfo32`), then compare against your manufacturer's support page and update following their instructions exactly (charger plugged in, no interruptions).
2. In **Terminal (Admin)**, run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Also verify DEP is at its default: in **Terminal (Admin)**, `bcdedit` should show `nx OptIn` — if it shows `AlwaysOff`, restore it with `bcdedit /set nx OptIn` and restart.
4. Microsoft documents DEP behavior on the [Windows support page](https://support.microsoft.com/en-us/windows).

### Fix 8: Perform a clean boot to isolate software triggers

When 0xFC crashes need a specific trigger — a particular app, a scheduled task, a background service — a clean boot finds it.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, check **Hide all Microsoft services**, then click **Disable all**.
3. Switch to the **Startup** tab, click **Open Task Manager**, and disable every startup item.
4. Restart. Use the laptop normally — if the crashes stop, some third-party software was the trigger.
5. Re-enable services and startup items in small groups (five at a time), restarting between groups, until the crash returns. The last group contains the culprit.
6. Common finds in this hunt: outdated Android emulators, old VPN clients, "game booster" utilities, and legacy virtualization tools — all of which install drivers that manipulate memory protections.
7. Once identified, update the program to its latest version or uninstall it via **Settings > Apps > Installed apps**. Do not just leave it disabled in msconfig forever; a disabled-but-present buggy driver can still load in edge cases.

### Fix 9: Check for CPU and motherboard firmware updates

The final layer when software isolation does not name a culprit.

1. Visit your laptop manufacturer's support page and check for BIOS updates mentioning "stability," "microcode," or "memory compatibility" — CPU microcode updates fix hardware-level memory-protection errata.
2. Install chipset drivers from the manufacturer (not just Windows Update) so the OS and firmware agree on memory management.
3. If crashes persist across a fully updated driver set, current BIOS, clean memory test, and clean boot, you are looking at a rare hardware fault in the CPU's memory-management unit — back up your data and contact the manufacturer's support with your documented troubleshooting steps, which will speed up the warranty process considerably.

## Closing

ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY looks exotic, but the fix is the same discipline that resolves most blue screens: read the dump, update or roll back the named driver, test the RAM, and clear out outdated antivirus and virtualization drivers. The DEP angle is a red herring for most people — leave the default `OptIn` setting alone and fix the driver that is actually misbehaving, and the 0xFC crashes stop.
