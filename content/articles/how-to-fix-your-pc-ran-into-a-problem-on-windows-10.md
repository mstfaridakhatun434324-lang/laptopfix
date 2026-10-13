---
title: "Your PC Ran Into a Problem (Windows 10): How to Fix It"
slug: how-to-fix-your-pc-ran-into-a-problem-on-windows-10
date: 2026-10-03
categories: ["windows-errors"]
tags: ["windows 10", "blue screen", "bsod", "startup"]
description: "Stuck on 'Your PC ran into a problem' on Windows 10? Here's how to get past the blue screen, find the cause, and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-your-pc-ran-into-a-problem-on-windows-10.webp"
faqs:
  - q: "What does 'Your PC ran into a problem' mean on Windows 10?"
    a: "It's Windows 10's friendly face for a blue screen (BSOD) — the system hit a critical error it couldn't recover from. The stop code shown at the bottom (like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL) identifies the specific cause."
  - q: "Why is my PC stuck in a 'ran into a problem' restart loop?"
    a: "Something loading at every boot is crashing — usually a bad driver, a failed update, or corrupt boot files. Because the trigger runs at startup, each reboot crashes the same way. Booting into Safe Mode breaks the loop so you can fix it."
  - q: "Will I lose my files fixing this?"
    a: "The fixes here — Safe Mode, driver updates, system file repair, System Restore — don't touch personal files. Only a clean reinstall risks data, and that's the last resort. Back up from the recovery environment first if you're worried."
  - q: "What should I do with the stop code on the screen?"
    a: "Write it down or photograph it. The stop code (and any named file like nvlddmkm.sys) is the single most useful diagnostic clue — it tells you whether to chase drivers, memory, or disk, instead of troubleshooting blindly."
---

"Your PC ran into a problem and needs to restart" is Windows 10's polite way of showing you a blue screen. Behind the sad emoticon is a stop code — the real diagnostic information — and behind that, one of the usual suspects: a bad driver, a failed update, corrupt system files, or failing hardware. The screen itself isn't the problem; it's the messenger.

The challenge with this error is that it often comes with a restart loop: the thing that crashed loads at every boot, so you crash at every boot. The fix strategy is therefore two-phase: first break the loop (Safe Mode or recovery), then find and fix the cause using the stop code as your guide. Don't skip phase one by repeatedly rebooting hopefully — that's how people waste entire weekends.

## Why this happens

- **Faulty or incompatible driver**: The most common cause. A driver that crashes during operation or at startup triggers the screen; graphics, network, and storage drivers lead the pack.
- **Failed or half-installed Windows update**: Updates that didn't complete cleanly leave the system in a state that crashes at boot.
- **Corrupt system files**: Damage to core Windows components from disk errors, malware, or bad updates.
- **Failing RAM**: Bad memory corrupts whatever it touches, producing crashes with varying stop codes.
- **Failing hard drive or SSD**: Bad sectors in system areas cause crashes that look like software problems.
- **Overheating**: Thermal crashes under load, especially on dust-clogged laptops.
- **New hardware or peripherals**: A newly installed device with a bad driver, or a failing USB device crashing the USB stack at boot.

## How to fix it

Work through these in order — break the loop first, then diagnose with the stop code.

### Fix 1: Break the loop by booting into Safe Mode

You can't fix a crash loop from inside the crash loop.

1. Force the recovery environment: power on, and when the Windows logo appears, hold the power button to force off. Do this twice; on the third boot, **Automatic Repair** appears.
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4** for Safe Mode.
3. If Safe Mode is stable, the cause is a third-party driver or startup program — not core Windows. That's good news; it's fixable.
4. If Safe Mode crashes too, you're looking at hardware, core system corruption, or a boot-critical driver — skip to Fixes 5 and 6.

### Fix 2: Record the stop code and check the dump

The code on the screen is your roadmap — capture it.

1. Photograph the blue screen, noting the stop code (e.g., `CRITICAL_PROCESS_DIED`) and any file named (e.g., `ntfs.sys`).
2. In Safe Mode, check `C:\Windows\Minidump` for dump files. Analyze with WinDbg if you're comfortable — the blamed driver is usually named.
3. Driver names point at driver fixes; `ntoskrnl.exe` or varying blame points at RAM; `ntfs.sys` points at the disk.
4. For stop-code-specific depth, [how to fix the blue screen of death on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the same codes with the same methodology — it applies to Windows 10 identically.

### Fix 3: Uninstall the most recent update

If the crashes started after Patch Tuesday, the update is suspect number one.

1. In Safe Mode, open **Settings** > **Update & Security** > **Windows Update** > **View update history** > **Uninstall updates**.
2. Remove the most recent quality update.
3. Restart normally and test. If stable, pause updates for a week or two before letting it reinstall.
4. Check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with that update — you're rarely the only one.

### Fix 4: Update or roll back drivers

Drivers are the top cause; address them deliberately.

1. In Safe Mode with Networking (option **5** in Startup Settings), open **Device Manager** (**Win + X**).
2. Look for devices with yellow warning icons — update those first.
3. Update **Display adapters**, **Network adapters**, and **Storage controllers** from the manufacturer's site, not just Windows Update.
4. If a driver updated right before crashes began, **Roll Back Driver** on it instead.
5. Also unplug all non-essential USB devices — a failing external drive or peripheral can crash the boot.

### Fix 5: Repair system files and the boot

Corruption in core files or boot data.

1. In the recovery environment, go to **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (adjust the drive letter if needed).
3. Then run `bootrec /fixmbr`, `bootrec /fixboot`, and `bootrec /rebuildbcd` to repair boot data.
4. Restart. Boot corruption is a common cause of the infinite "ran into a problem" loop specifically.

### Fix 6: Check disk and memory health

Hardware causes need hardware diagnostics.

1. From the recovery Command Prompt, run `chkdsk C: /f /r` and let it complete.
2. For RAM, use **Windows Memory Diagnostic** from the recovery tools or `mdsched.exe` once booted.
3. If chkdsk finds many bad sectors, back up immediately — the drive is failing and needs replacement, not repair.
4. Memory errors mean replacing the RAM (or a service visit for soldered RAM).

### Fix 7: Use System Restore

Roll back the system state without touching your files.

1. In recovery, go to **Troubleshoot** > **Advanced options** > **System Restore**.
2. Choose a restore point from before the crashes started.
3. Let it complete and boot normally. This reverses driver updates, Windows updates, and registry changes in one move.
4. After restoring, update drivers carefully one at a time so you can identify the bad one if it returns.

### Fix 8: Reset or clean-install Windows 10

When nothing else breaks the loop.

1. Back up your files first — from the recovery Command Prompt you can copy files to a USB drive with `xcopy` or `robocopy`.
2. In recovery, **Troubleshoot** > **Reset this PC** > **Keep my files** first.
3. If the reset fails or crashes persist, do a clean install from USB media — and if a clean install still blue-screens, it's definitively hardware.
4. For restart-specific variants, [Windows 11 stuck on restarting fix](/articles/windows-11-stuck-on-restarting-screen-fix/) covers the loop scenario on the newer OS.

## Closing

"Your PC ran into a problem" is a symptom, not a diagnosis — the stop code is the diagnosis, and Safe Mode is how you get to it. Break the reboot loop first, read the code, then work the cause: updates, drivers, system files, disk, memory. Most Windows 10 machines showing this screen are one rollback or one driver away from working again. The screen looks scary; the fix is usually methodical, not heroic.
