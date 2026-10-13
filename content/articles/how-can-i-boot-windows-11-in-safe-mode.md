---
title: "How Can I Boot Windows 11 in Safe Mode? Every Method Explained"
slug: how-can-i-boot-windows-11-in-safe-mode
date: 2026-09-14
categories: ["windows-errors"]
tags: ["safe mode", "windows 11", "boot options", "troubleshooting", "winre"]
description: "Need Safe Mode on Windows 11? Every method explained — from Settings and msconfig to Shift+Restart and WinRE — plus what to do in each."
thumbnail: "/images/thumbs/how-can-i-boot-windows-11-in-safe-mode.webp"
faqs:
  - q: "What is the easiest way to boot Windows 11 in Safe Mode?"
    a: "Hold Shift while clicking Restart from the Start menu power button, then go to Troubleshoot, Advanced options, Startup Settings, Restart, and press 4. It takes about a minute, works from a running system, and needs no commands or installation media."
  - q: "What is the difference between Safe Mode and Safe Mode with Networking?"
    a: "Plain Safe Mode loads minimal drivers with no network access — best for removing bad drivers or malware. Safe Mode with Networking adds network drivers so you can download tools or drivers. Choose Networking when you need the internet; otherwise plain Safe Mode is the cleaner diagnostic environment."
  - q: "Can I get into Safe Mode if Windows won't boot?"
    a: "Yes — interrupt the boot three times to trigger the Recovery Environment, then go to Troubleshoot, Advanced options, Startup Settings, Restart, and press 4. Alternatively, boot from Windows 11 installation media, choose Repair your computer, and follow the same path. Both methods work even when Windows itself cannot start."
  - q: "How do I exit Safe Mode?"
    a: "Just restart normally — unless you used msconfig to force Safe Mode, in which case you must reopen msconfig, uncheck Safe boot on the Boot tab, and restart. Forgetting that checkbox is the classic reason people get stuck in Safe Mode."
---

Safe Mode is Windows 11's diagnostic boot: minimal drivers, no startup programs, a stripped-down environment where misbehaving software can't hide. It's where you go to remove a bad driver, uninstall crashing software, run malware scans, or use tools like Driver Verifier's reset — all the jobs from our blue-screen guides that need a stable, minimal Windows. The catch is that Windows 11 boots too fast for the old "mash F8" trick, so you need to know the modern methods.

There are four reliable ways in, each suited to a different situation: from a working desktop, from the login screen, via msconfig for repeated Safe Mode sessions, and from the Recovery Environment when Windows won't boot at all. Here's every method, when to use it, and how to get back out.

## Why this happens

- **You need Safe Mode for driver removal.** Bad drivers can't be cleanly removed while they're loaded — Safe Mode doesn't load them.
- **Crashing software blocks normal boot.** A broken startup program or service can make normal Windows unusable.
- **Malware resists removal.** Many threats can't be cleaned while their processes are running; Safe Mode keeps them dormant.
- **Windows won't boot normally.** The Recovery Environment path gets you into Safe Mode when the desktop is unreachable.
- **You need repeated Safe Mode sessions.** The msconfig method persists across restarts for multi-step repairs.
- **Driver Verifier needs resetting.** After Verifier catches a bad driver, Safe Mode is where you run `verifier /reset`.
- **You got stuck in Safe Mode.** Usually the msconfig "Safe boot" checkbox left on — covered in the exit section.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Shift + Restart from the desktop

The fastest method from a working system.

1. Click **Start > Power**, then hold **Shift** and click **Restart** (keep holding Shift until the blue screen appears).
2. Choose **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. After reboot, press **4** for Safe Mode, **5** for Safe Mode with Networking, **6** for Safe Mode with Command Prompt.
4. Log in — the desktop will say "Safe Mode" in the corners and look low-resolution. That's normal.
5. Do your repair work, then simply **Restart** to return to normal Windows.

This is the method to reach for in most situations — no commands, no configuration changes, no persistence.

### Fix 2: Use Shift + Restart from the login screen

When you can reach the login screen but not the desktop.

1. On the login screen, click the **Power** icon in the bottom-right corner.
2. Hold **Shift** and click **Restart**.
3. Follow the same path: **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4/5/6**.
4. You'll need your account password (PIN may not work in Safe Mode — have the password ready).
5. Restart normally when done.

If even the login screen is unreachable, Fix 4's Recovery Environment path is next. Our general Safe Mode reference is [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 3: Use msconfig for persistent Safe Mode

When you need Safe Mode across multiple restarts.

1. Press **Windows + R**, type `msconfig`, press Enter.
2. Go to the **Boot** tab and check **Safe boot**; choose **Minimal** (or **Network** for networking).
3. Click **OK** and **Restart** — Windows now boots to Safe Mode every time.
4. Do your multi-step repair (driver removal, Verifier reset, malware scans across reboots).
5. **Critical:** when finished, reopen `msconfig`, **uncheck Safe boot**, and restart — otherwise you're stuck in Safe Mode permanently.

This is the method our driver guides assume when they say "boot to Safe Mode to reset Driver Verifier" — it survives the restarts those procedures need.

### Fix 4: Reach Safe Mode from the Recovery Environment

When Windows won't boot at all.

1. Interrupt the boot three times (power off at the Windows logo) to trigger WinRE, or boot from installation media (create it with the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) Media Creation Tool) → **Repair your computer**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. Press **4**, **5**, or **6** after the reboot.
4. If Startup Settings isn't listed, use **Command Prompt** instead and run `bcdedit /set {default} safeboot minimal`, then `exit` and continue booting.
5. To undo the bcdedit method later: in Safe Mode's command prompt, run `bcdedit /deletevalue {default} safeboot` and restart.

If Safe Mode itself won't start, that's a deeper problem — see [how to fix Windows 11 Safe Mode not working, step by step](/articles/how-to-fix-windows-11-safe-mode-not-working-step-by-step/).

### Fix 5: Know what to do once you're in Safe Mode

Safe Mode is a means, not an end — use it purposefully.

1. **Remove bad drivers:** Device Manager → uninstall the suspect device (check "delete driver software").
2. **Uninstall crashing software:** Settings > Apps > Installed apps — the culprit can't fight back in Safe Mode.
3. **Run malware scans:** Microsoft Defender full scan with the threat's processes dormant.
4. **Reset Driver Verifier:** command prompt → `verifier /reset` → restart.
5. **Don't** try to install most software, run Windows Update, or judge performance in Safe Mode — it's a minimal environment, not a functional one.

### Fix 6: Exit Safe Mode correctly

Get back to normal Windows without drama.

1. If you entered via Shift+Restart or WinRE: just **Restart** — Safe Mode doesn't persist.
2. If you used msconfig: reopen `msconfig` → **Boot** tab → **uncheck Safe boot** → **OK** → **Restart**.
3. If you used bcdedit: `bcdedit /deletevalue {default} safeboot` from an admin prompt, then restart.
4. Verify you're out: the "Safe Mode" corner text is gone and resolution is normal.
5. If Windows still boots to Safe Mode after all this, check msconfig once more — the checkbox is the culprit 99% of the time.

### Fix 7: When Safe Mode won't start

Diagnose the deeper failure.

1. Try **Safe Mode with Command Prompt** (option 6) — sometimes the Explorer shell is the broken part, not the boot.
2. From WinRE's Command Prompt, run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (use your actual drive letter).
3. Run `chkdsk C: /f` to rule out filesystem damage blocking the minimal boot.
4. Check for a corrupted BCD: `bootrec /rebuildbcd` from WinRE.
5. If Safe Mode fails but WinRE works, an in-place upgrade from installation media — built with the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — keeping files rebuilds the boot path.

## Closing

Safe Mode in Windows 11 isn't hard — it's just different from the F8 days. Learn the Shift+Restart path for everyday use, the msconfig method for multi-reboot repairs (and its all-important uncheck step), and the Recovery Environment route for when Windows won't boot. Nearly every serious troubleshooting procedure — driver removal, Verifier resets, malware cleanup — passes through Safe Mode at some point, so these methods are worth committing to memory. Get in, do the job the minimal environment enables, get out cleanly, and never leave that msconfig checkbox ticked.
