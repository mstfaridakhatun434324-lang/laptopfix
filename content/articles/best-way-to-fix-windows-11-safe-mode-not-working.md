---
title: "Windows 11 Safe Mode Not Working? Here's How to Fix It"
slug: best-way-to-fix-windows-11-safe-mode-not-working
date: 2026-09-12
categories: ["windows-errors"]
tags: ["safe mode", "windows 11", "boot", "troubleshooting"]
description: "Safe Mode won't start on Windows 11? Whether it loops, black-screens, or the option is missing — here's how to get it working."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-safe-mode-not-working.webp"
faqs:
  - q: "Why won't my PC boot into Safe Mode?"
    a: "The usual reasons: corrupted boot configuration data, a damaged Windows installation, Fast Startup interfering, or the recovery environment itself being broken. The fix depends on which symptom you see — the guide covers each one."
  - q: "Can I force Safe Mode if Windows won't boot at all?"
    a: "Yes. Interrupt the boot three times to trigger the recovery environment, then Troubleshoot > Advanced options > Startup Settings > Restart. Or boot from Windows installation USB and use the Command Prompt to set Safe Mode via bcdedit."
  - q: "What if Safe Mode shows a black screen?"
    a: "A black screen in Safe Mode usually means a display driver problem or corrupted system files. Boot into Safe Mode with Command Prompt instead, then update or remove the graphics driver, or run SFC offline."
  - q: "Is Safe Mode different on Windows 11 vs Windows 10?"
    a: "Functionally the same, but the old F8-during-boot shortcut doesn't work on modern UEFI systems with fast boot — Windows 11 relies on the recovery environment and Settings-based methods instead. The msconfig and bcdedit methods still work identically."
---

Safe Mode is the technician's best friend — a minimal Windows that loads only essential drivers, perfect for removing bad software or drivers. So when Safe Mode itself won't work, it's doubly frustrating: the tool you need to fix the problem is broken too. The failure comes in a few flavors — the option never appears, selecting it reboots normally, it hangs on a black screen, or it loops back to recovery — and each has its own fix.

This guide covers every failure mode in order of likelihood. Work through the methods until one gets you in; then fix whatever originally sent you to Safe Mode. If you're here because of a specific blue screen, our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) pairs well with this one — Safe Mode is often step one of those fixes.

## Why this happens

- **Corrupt Boot Configuration Data (BCD)**: Safe Mode is a boot option stored in the BCD. If the BCD is damaged, the Safe Mode entry may be missing or broken.
- **Fast Startup interference**: Fast Startup's hybrid shutdown can bypass the normal boot menu paths, making Safe Mode unreachable through the usual methods.
- **Damaged recovery environment (WinRE)**: If the Windows Recovery Environment itself is corrupt or disabled, the **Advanced startup** path to Safe Mode fails.
- **Corrupted system files**: Damage to the files Safe Mode needs can cause black screens or hangs during Safe Mode boot.
- **Bad display driver**: Safe Mode uses a basic display driver — but if the driver stack is thoroughly broken, even that can fail, producing a black screen.
- **BitLocker complications**: On encrypted drives, Safe Mode prompts for the recovery key at awkward moments; a missing key looks like Safe Mode "not working."
- **Third-party boot managers**: Dual-boot tools can interfere with Windows' boot menu.

## How to fix it

Work through these in order — alternative entry methods first, repairs second.

### Fix 1: Use the Shift + Restart method

The most reliable way to reach Safe Mode when Windows boots.

1. Click **Start** > **Power**, then hold **Shift** and click **Restart**. Keep holding Shift until the blue recovery screen appears.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **4** for Safe Mode, **5** for Safe Mode with Networking, or **6** for Safe Mode with Command Prompt.
4. If this works, the problem was just the entry method — use this one going forward.

This works from the sign-in screen too: hold **Shift** while clicking the power icon there.

### Fix 2: Force the recovery environment

When Windows won't boot normally, force WinRE by interrupting startup.

1. Power on the laptop, and as soon as you see the manufacturer's logo or spinning dots, hold the power button to force it off.
2. Repeat this **three times**. On the fourth boot, Windows should enter **Automatic Repair** / the recovery environment on its own.
3. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4**, **5**, or **6**.
4. If the recovery environment never appears, your WinRE may be broken — skip to Fix 5.

### Fix 3: Enable Safe Mode via msconfig (when Windows boots)

If Windows boots but the F8-style methods fail, set Safe Mode directly.

1. Press **Windows + R**, type `msconfig`, press Enter.
2. Go to the **Boot** tab and tick **Safe boot**, selecting **Minimal** (or **Network** if you need internet).
3. Click **OK** and restart — Windows boots straight into Safe Mode.
4. **Critical**: when you're done, run `msconfig` again and **untick Safe boot** — otherwise the PC boots into Safe Mode forever.

### Fix 4: Force Safe Mode with bcdedit (from recovery or USB)

When nothing else works, set the boot flag directly from a Command Prompt.

1. Boot into the recovery environment (Fix 2 method) or from a Windows 11 installation USB (**Repair your computer** > **Troubleshoot** > **Command Prompt**).
2. Run: `bcdedit /set {default} safeboot minimal` (use `network` instead of `minimal` if you need networking).
3. Type `exit` and choose **Continue**. Windows boots into Safe Mode.
4. When finished, open an admin Command Prompt in Safe Mode and run `bcdedit /deletevalue {default} safeboot` to return to normal boot.

If `{default}` doesn't work, run `bcdedit` alone first to see the actual identifier of your Windows boot entry.

### Fix 5: Repair or re-enable the recovery environment

If the recovery screens themselves are broken or missing, fix WinRE.

1. Open **Terminal (Admin)** and run `reagentc /info` — check whether **Windows RE status** is Enabled and a location is listed.
2. If disabled, run `reagentc /enable` and retry.
3. If it fails to enable, the WinRE image may be corrupt: run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth`, then try `reagentc /enable` again.
4. As a workaround, keep a Windows 11 installation USB handy — its **Repair your computer** option provides the same recovery tools regardless of WinRE's state. Create one with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 6: Fix the black-screen-in-Safe-Mode variant

If Safe Mode starts but shows only a black screen (possibly with a cursor):

1. Try **Safe Mode with Command Prompt** instead (option **6** at Startup Settings) — it skips more of the graphics stack.
2. From the command prompt, update or remove the graphics driver: run `devmgmt.msc` to open Device Manager, or use `pnputil` to manage drivers from the command line.
3. Run an offline system file check: `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter).
4. Check [Microsoft's black-screen guidance](https://support.microsoft.com/en-us/windows) for additional display-specific steps.

### Fix 7: Disable Fast Startup

Fast Startup can interfere with reaching the boot menu.

1. If you can boot Windows normally: **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable** > untick **Turn on fast startup** > **Save changes**.
2. From recovery Command Prompt: run `powercfg /h off` — this disables hibernation, which also disables Fast Startup (it depends on hibernation).
3. Shut down fully and try the Safe Mode methods again.

## Closing

Safe Mode "not working" is almost always an entry-method problem rather than Safe Mode itself being broken — the Shift+Restart and bcdedit methods succeed where the old habits fail. The deeper fixes (WinRE repair, BCD rebuild) are for the rarer cases where the boot infrastructure is genuinely damaged. Once you're in, remember to undo any boot flags you set (`msconfig` untick, `bcdedit /deletevalue`) — the classic self-inflicted follow-up problem is a PC permanently stuck in Safe Mode because the flag was never cleared. For using Safe Mode to chase a specific crash, our [dump analysis guide](/articles/how-to-read-dump-files-with-windbg-on-windows-11/) is the natural next step once you're booted.
