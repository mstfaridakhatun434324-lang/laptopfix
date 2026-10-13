---
title: "How to Boot Windows 11 in Safe Mode on a Laptop"
slug: how-to-boot-windows-11-in-safe-mode-on-laptop
date: 2026-09-22
categories: ["windows-errors"]
tags: ["safe-mode", "windows-11", "recovery"]
description: "Need Safe Mode on your Windows 11 laptop? Here are 5 reliable ways to boot into Safe Mode — even when Windows won't start normally."
thumbnail: "/images/thumbs/how-to-boot-windows-11-in-safe-mode-on-laptop.webp"
faqs:
  - q: "What is Safe Mode and when should I use it?"
    a: "Safe Mode starts Windows with only the essential drivers and services, skipping third-party software. Use it when normal boot crashes, when you need to uninstall a bad driver or program, or when malware blocks your cleanup tools. If the problem disappears in Safe Mode, a third-party driver or startup program is the cause."
  - q: "What's the difference between Safe Mode and Safe Mode with Networking?"
    a: "Plain Safe Mode loads no network drivers, so you can't access the internet. Safe Mode with Networking adds network drivers, letting you download drivers, research fixes, or run online scans. Choose Networking when you need the internet; choose plain Safe Mode when you suspect a network driver is the problem."
  - q: "Why doesn't pressing F8 work on Windows 11?"
    a: "Windows 11 boots too fast for the old F8 interrupt on most modern laptops with UEFI and fast startup. The key press simply isn't detected in time. Microsoft replaced it with the Shift+Restart method and the recovery environment, which work reliably regardless of boot speed."
  - q: "How do I get out of Safe Mode?"
    a: "Just restart normally from the Start menu — unless you used msconfig to force Safe Mode, in which case you must undo it. Open msconfig, go to the Boot tab, uncheck Safe boot, click OK, and restart. Forgetting this step is the most common reason people get stuck in Safe Mode."
---
Safe Mode is the single most useful troubleshooting tool in Windows, and on a laptop you'll reach for it exactly when things are at their worst: a driver that blue-screens on boot, a program that hijacks the login screen, or malware that fights your antivirus. The good news is that Windows 11 gives you several ways in — including methods that work when Windows won't boot at all.

This guide covers every reliable method, from the quick Settings route to the force-it-open trick for unbootable machines. Pick whichever matches your situation; they all land in the same Safe Mode. And once you're in, the last section tells you exactly what to do with the access — because reaching Safe Mode is only useful if you know the triage order.

## Why this happens

- **You're reading this because something is broken** — Safe Mode itself rarely fails; the challenge is reaching it when normal Windows won't cooperate.
- **Fast startup and UEFI** make the old F8-during-boot trick unreliable on modern laptops, so the familiar key press does nothing.
- **A crashing display or storage driver** can block normal boot entirely, which is exactly when Safe Mode's minimal drivers save the day.
- **BitLocker or a PIN issue** can complicate recovery-environment access if you don't have your recovery key handy.
- **Interrupted updates** sometimes leave the boot configuration pointing at a half-installed state that only Safe Mode can bypass.
- **Third-party "fast boot" utilities** from laptop makers can skip the window where recovery key combinations register.
- **A damaged recovery partition** that prevents the normal Advanced startup path from loading, forcing you to use installation media instead.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Use Shift + Restart (works from the login screen too)

This is the method to memorize — it works whether you're signed in or stuck at the login screen.

1. Hold down **Shift** and click **Restart** — from the Start menu's power button, or from the power icon on the login screen.
2. Keep holding Shift until the blue **Choose an option** screen appears, then release it.
3. Go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**.
4. After the reboot, press **4** for Safe Mode, **5** for Safe Mode with Networking, or **6** for Safe Mode with Command Prompt.

### Fix 2: Use the Settings app

If Windows boots fine and you just want Safe Mode for maintenance, this is the cleanest path.

1. Open **Settings** → **System** → **Recovery**.
2. Under **Recovery options**, click **Restart now** next to **Advanced startup** and confirm.
3. When the blue screen appears, go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**.
4. Press **4**, **5**, or **6** to choose your Safe Mode flavor.

### Fix 3: Force the recovery environment (for unbootable laptops)

When Windows won't start at all, you can force it to open the recovery tools.

1. Power the laptop on. As soon as you see the manufacturer's logo or the Windows spinner, press and hold the power button until it shuts off.
2. Repeat this two more times — three interrupted boots total.
3. On the fourth boot, Windows opens **Automatic Repair** and then the **Choose an option** screen by itself.
4. Go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**, then press **4**, **5**, or **6**.

This trick also helps when you're stuck in an [automatic repair loop](/articles/how-to-fix-automatic-repair-loop-windows-11-step-by-step/) — it's the same doorway into the recovery tools.

### Fix 4: Use msconfig (and remember to undo it)

The System Configuration tool can force Safe Mode on every boot — handy, but it has a trap.

1. Press **Win + R**, type `msconfig`, and press Enter.
2. Go to the **Boot** tab and tick **Safe boot**. Choose **Minimal** for plain Safe Mode or **Network** for networking.
3. Click **OK** and restart when prompted — the laptop will boot straight into Safe Mode.
4. When you're done troubleshooting, run `msconfig` again, untick **Safe boot**, and restart. Skip this and you'll boot into Safe Mode forever.

### Fix 5: Use installation media when nothing else works

If the internal recovery partition is damaged, a USB installer becomes your recovery environment.

1. On another computer, create Windows 11 installation media with the [official download tool](https://www.microsoft.com/en-us/software-download/windows11).
2. Boot your laptop from the USB (usually **F12**, **F9**, or **Esc** at the logo for the boot menu).
3. Choose your language, then click **Repair your computer** — not Install.
4. Go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**, then press **4**, **5**, or **6**.

### Fix 6: Enable Safe Mode from the Command Prompt

If you can reach a command prompt but not the graphical recovery menus, one command sets the next boot to Safe Mode.

1. In the recovery environment, go to **Troubleshoot** → **Advanced options** → **Command Prompt**.
2. For Safe Mode, run: `bcdedit /set {default} safeboot minimal`
3. For Safe Mode with Networking, run: `bcdedit /set {default} safeboot network`
4. Type `exit` and choose **Continue**. To undo later, boot into Safe Mode's command prompt and run `bcdedit /deletevalue {default} safeboot`.

### Fix 7: What to do once you're in Safe Mode

Getting in is only half the battle — here's the standard triage order.

1. Open **Device Manager** and roll back or uninstall the suspect driver (display and network drivers first).
2. Open **Settings** → **Apps** → **Installed apps** and remove whatever you installed just before the trouble started.
3. Run `sfc /scannow` from an admin terminal to repair system files.
4. Restart normally and confirm the problem is gone before reinstalling anything you removed.

If Safe Mode itself refuses to boot or crashes, that's a deeper problem — our guide to [fixing Safe Mode when it won't work](/articles/how-to-fix-windows-11-safe-mode-not-working-step-by-step/) picks up where this one leaves off.

## Closing

Safe Mode is Windows' emergency room: minimal, unglamorous, and exactly what you need when normal boot is broken. Memorize the Shift+Restart path and the three-interrupted-boots trick, and you'll never be locked out of your own laptop again. Just remember the golden rule of msconfig and bcdedit methods — always undo the forced Safe Mode flag when you're done, or your "temporary" troubleshooting boot becomes permanent.
