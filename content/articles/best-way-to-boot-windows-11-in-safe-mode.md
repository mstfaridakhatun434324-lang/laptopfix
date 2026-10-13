---
title: "The Best Way to Boot Windows 11 in Safe Mode (All Methods)"
slug: best-way-to-boot-windows-11-in-safe-mode
date: 2026-09-22
categories: ["windows-errors"]
tags: ["safe mode", "windows 11", "boot options", "troubleshooting"]
description: "Need Safe Mode on Windows 11? Here are all the working methods — from Settings to the recovery environment — plus when to use each one."
thumbnail: "/images/thumbs/best-way-to-boot-windows-11-in-safe-mode.webp"
faqs:
  - q: "What is Safe Mode and why would I use it?"
    a: "Safe Mode starts Windows with only essential Microsoft drivers and services — no third-party drivers, no startup programs. It's a diagnostic environment: if your problem disappears in Safe Mode, a third-party driver or program is the cause. You'd use it to uninstall bad drivers, remove malware, or undo changes that broke normal boot."
  - q: "What's the difference between Safe Mode and Safe Mode with Networking?"
    a: "Safe Mode with Networking adds the network drivers, so you can access the internet to download fixed drivers or research the problem. Use plain Safe Mode when testing whether the network driver itself is the problem; use with Networking when you need to download a replacement driver or look up instructions."
  - q: "How do I get out of Safe Mode?"
    a: "If you entered via msconfig, you must undo it: press Windows + R, type msconfig, go to the Boot tab, untick Safe boot, and restart. If you entered via recovery or Settings, just restart normally — Windows boots normally by default. Forgetting the msconfig step is the most common reason people get stuck in Safe Mode."
  - q: "Can I boot to Safe Mode if Windows won't start at all?"
    a: "Yes — interrupt the boot three times at the Windows logo to force the Automatic Repair screen, then go to Troubleshoot, Advanced options, Startup Settings, Restart, and press 4. This works even when Windows can't boot, because the recovery environment is separate from the broken installation."
---

Safe Mode is Windows' diagnostic workshop: it starts the OS with only the essential Microsoft drivers and services, leaving every third-party driver, startup program, and fancy shell extension behind. When your laptop blue-screens, boot-loops, or misbehaves in normal mode but runs fine in Safe Mode, you've just learned something crucial — the problem is third-party software, not Windows itself. Every serious troubleshooting guide references Safe Mode, so knowing all the ways to reach it (including when Windows won't boot at all) is foundational.

Windows 11 made Safe Mode slightly harder to reach than older versions — the old F8 trick is gone — but there are still four reliable methods, each suited to a different situation. This guide covers all of them, explains which to use when, and warns you about the one trap that strands people in Safe Mode indefinitely. For using Safe Mode to diagnose blue screens specifically, see our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/); to stop crashes from auto-rebooting past the error, see our [disable automatic restart guide](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/).

## Why this happens

- **You need it because**: Safe Mode is the answer to "is it Windows or is it something I installed?" — the most important diagnostic question in troubleshooting.
- **F8 was removed**: Windows 11 boots too fast for the old interrupt key, so Microsoft moved Safe Mode behind Settings and recovery menus.
- **Method depends on state**: A working Windows uses Settings/msconfig methods; a broken boot needs the recovery environment method.
- **Three Safe Mode flavors exist**: Minimal (no network), with Networking (internet access), and with Command Prompt (no GUI at all).
- **The msconfig trap**: Setting Safe boot in msconfig persists across restarts — forgetting to untick it strands you in Safe Mode.
- **BitLocker complication**: On encrypted drives, recovery methods may ask for the 48-digit recovery key — have it ready.
- **It's temporary by design**: Safe Mode disables so much that it's unpleasant for real work — use it, fix the problem, leave.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Settings (Windows boots normally)

The cleanest method when Windows works.

1. Go to **Settings** > **System** > **Recovery**.
2. Next to **Advanced startup**, click **Restart now** and confirm.
3. After restarting to the blue menu: **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
4. Press **4** for Safe Mode, **5** for Safe Mode with Networking, or **6** for Safe Mode with Command Prompt.
5. To exit: just restart — Windows returns to normal boot automatically with this method.

### Fix 2: Use msconfig (quickest for repeated Safe Mode boots)

Best when you'll be entering Safe Mode multiple times during a repair.

1. Press **Windows + R**, type `msconfig`, and press Enter.
2. Go to the **Boot** tab and tick **Safe boot**. Choose **Minimal** (plain Safe Mode) or **Network** (with Networking).
3. Click **OK** and **Restart**. Windows now boots into Safe Mode every time until you undo this.
4. **Critical**: when finished, reopen `msconfig`, untick **Safe boot**, and restart — otherwise you're stuck in Safe Mode permanently.
5. This method is ideal for multi-step repairs (uninstall driver → test → reinstall driver → test) where re-entering Safe Mode repeatedly would be tedious.

### Fix 3: Force the recovery environment (Windows won't boot)

The method for broken boots.

1. Power on the laptop; when the Windows logo or spinning dots appear, hold the power button to force off.
2. Repeat twice more — on the third boot, Windows enters **Automatic Repair** instead of trying to start.
3. Click **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
4. Press **4**, **5**, or **6** for your desired Safe Mode flavor.
5. If Automatic Repair never appears after three interrupts, boot from installation USB (made with [Microsoft's Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11)) and choose **Repair your computer** to reach the same menu.

### Fix 4: Use Shift + Restart (fastest from a running system)

The speed-run method.

1. Click **Start** > **Power**, then hold **Shift** and click **Restart**.
2. Keep holding Shift until the blue **Choose an option** screen appears.
3. Navigate **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, then press **4/5/6**.
4. This also works from the login screen: hold **Shift** while clicking the power icon > **Restart** — useful when you can reach login but the desktop crashes.
5. Like Fix 1, exiting is just a restart — no persistent setting to undo.

### Fix 5: Choose the right Safe Mode flavor

Match the environment to the job.

1. **Safe Mode (Minimal)**: use for driver uninstalls and testing whether the network stack is implicated — no internet, minimal drivers.
2. **Safe Mode with Networking**: use when you need to download a fixed driver, research the error, or run online scans. Note it still skips third-party startup programs.
3. **Safe Mode with Command Prompt**: use for command-line repairs (SFC, DISM, BCD rebuilds) when even the GUI is unstable.
4. If the problem reproduces in Safe Mode Minimal, it's a Microsoft component, system file corruption, or hardware — third-party software is exonerated.

### Fix 6: Do the actual repair work in Safe Mode

Safe Mode is a means, not an end — here's what to do once inside.

1. **Bad driver**: **Device Manager** > right-click the suspect device > **Uninstall device** (or **Roll Back Driver**), then restart normally.
2. **Bad program**: **Settings** > **Apps** > **Installed apps** > sort by date > uninstall recent additions, especially antivirus trials and system utilities.
3. **Malware**: run a full **Microsoft Defender** scan — check [Microsoft's security guidance](https://support.microsoft.com/en-us/windows) for offline scan options if the infection resists.
4. **System files**: open an elevated terminal and run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`.
5. After each repair, restart into normal Windows and test — Safe Mode stability means nothing until normal mode is stable too.

### Fix 7: Escape if you're stuck in Safe Mode

The recovery for the msconfig trap.

1. In Safe Mode, press **Windows + R**, type `msconfig`, go to the **Boot** tab, untick **Safe boot**, **OK**, restart.
2. If msconfig won't open, use the terminal: `bcdedit /deletevalue {default} safeboot` then restart.
3. If you used `bcdedit /set {default} safeboot minimal` manually, the deletevalue command above reverses it — for network flavor you set `safeboot network`, same reversal.
4. After escaping, verify normal boot works fully before considering the original problem resolved.

## Closing

Safe Mode isn't a fix — it's the diagnostic lens that makes fixes possible. The method you use depends on your situation: Settings or Shift+Restart when Windows runs, the triple-interrupt when it doesn't, msconfig when you'll be going back repeatedly. And the rule that saves everyone exactly once: if you used msconfig to get in, you must use msconfig to get out. Master these four doors into Safe Mode and every other troubleshooting guide — including every blue screen fix on this site — becomes executable instead of theoretical. For putting Safe Mode to work on crash diagnosis specifically, our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) is the natural next read.
