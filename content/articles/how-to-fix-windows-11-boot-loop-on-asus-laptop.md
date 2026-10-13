---
title: "How to Fix a Windows 11 Boot Loop on an ASUS Laptop"
slug: how-to-fix-windows-11-boot-loop-on-asus-laptop
date: 2026-09-13
categories: ["windows-errors"]
tags: ["boot loop", "ASUS laptop", "Windows 11"]
description: "ASUS laptop stuck restarting over and over? Break the Windows 11 boot loop with these proven recovery steps, no data loss."
thumbnail: "/images/thumbs/how-to-fix-windows-11-boot-loop-on-asus-laptop.webp"
faqs:
  - q: "What exactly is a boot loop?"
    a: "It's when your laptop starts to boot, fails partway — showing the ASUS logo, a blue screen, or the 'Preparing Automatic Repair' message — and restarts itself, repeating the cycle forever. The system never reaches the login screen because something in the startup sequence keeps failing."
  - q: "Will breaking the boot loop delete my files?"
    a: "No. Every fix in this guide — interrupting the loop to reach recovery, Startup Repair, uninstalling updates, System Restore — preserves your personal files. Only a 'Remove everything' reset deletes data, and that's the last resort."
  - q: "Why does my ASUS laptop keep boot looping after updates?"
    a: "ASUS laptops are particularly prone to this when a Windows update clashes with ASUS-specific drivers or utilities like Armoury Crate or MyASUS. Fast Startup caching a failed boot state is another classic cause. Updating the BIOS and ASUS drivers from ASUS support usually prevents repeats."
  - q: "How do I stop the loop long enough to fix it?"
    a: "Force the laptop off by holding the power button, then interrupt the boot three times in a row (power off at the ASUS logo each time). On the fourth boot, Windows enters the Recovery Environment instead of trying to start normally, breaking the cycle."
---
There's a special kind of frustration in watching your ASUS laptop show its logo, go dark, and start over — again and again, never reaching Windows. That's a boot loop, and it usually strikes right after a Windows update, a driver install, or a BIOS change. The good news: the loop itself is just Windows failing the same way repeatedly, and once you break the cycle and get into the recovery tools, the underlying problem is very fixable.

ASUS laptops have their own flavor of this thanks to MyASUS, Armoury Crate, and ASUS-specific drivers that load early in the boot process. This guide accounts for all of that. Work from the top down, and don't skip the ASUS-specific steps — they're the ones that actually stop the loop from coming back.

## Why this happens

- **A bad Windows update.** The most common trigger, full stop. An update that doesn't finish cleanly leaves mismatched system files, and Windows fails at the same point on every boot attempt.
- **Fast Startup replaying a failed boot.** Fast Startup saves the kernel session to disk for faster boots. If it saved a broken state, every "fast" boot replays the failure. This alone causes a huge share of boot loops.
- **ASUS utility conflicts.** Armoury Crate, MyASUS, and ASUS System Control Interface load very early. A buggy version of one of these can crash the boot process before the login screen. After you're back in, update them from the official ASUS support site for your exact model.
- **Corrupted Boot Configuration Data.** If the BCD — the file telling Windows how to boot — is damaged, the boot fails at the same early stage every time.
- **Driver clashes after major updates.** Windows 11 feature updates sometimes replace a working ASUS-tuned driver (audio, chipset, graphics) with a generic one that doesn't initialize properly on your hardware.
- **Disk errors or a failing drive.** Bad sectors in the system area cause the same boot files to fail loading on every attempt, which looks exactly like a software boot loop until you test the drive.

## How to fix it

Work through these in order — start with Fix 1 and only move on if the problem is still there.

### Fix 1: Break the loop and reach the Recovery Environment

You can't fix anything while the laptop keeps restarting itself, so step one is forcing Windows into its recovery menus.

1. Let the laptop start looping, then hold the **power button** for 10 seconds to force it fully off.
2. Press the **power button** to start it, and the moment you see the **ASUS logo**, hold the power button again to force it off. This is one interrupted boot.
3. Repeat the interrupted boot **two more times** (three total). On the fourth start, don't touch anything — Windows should load the **Choose an option** screen instead of looping.
4. From here, every fix below is reachable via **Troubleshoot > Advanced options**. If the loop persists even here, skip to Fix 6 — your recovery partition may be damaged.

### Fix 2: Disable Fast Startup from the recovery menu

If a cached bad boot state is causing the loop, this breaks it immediately.

1. From **Choose an option**, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Type `reg load HKLM\TempHive C:\Windows\System32\config\SYSTEM` and press Enter to load the offline registry.
3. Then run:
   `reg add "HKLM\TempHive\ControlSet001\Control\Session Manager\Power" /v HiberbootEnabled /t REG_DWORD /d 0 /f`
4. Unload the hive with `reg unload HKLM\TempHive`, type `exit`, and choose **Continue** to restart. With Fast Startup off, Windows does a full clean boot every time.

### Fix 3: Uninstall the latest Windows update

If the loop started within a day of an update, the update is guilty until proven innocent.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Start with **Uninstall latest quality update** and let it complete.
3. Choose **Continue** to restart. If the loop is broken, go to **Settings > Windows Update > Pause updates** for two weeks once you're back in.
4. Still looping? Go back and try **Uninstall latest feature update** — feature updates are bigger, riskier, and more likely to clash with ASUS drivers.

### Fix 4: Run Startup Repair and rebuild the BCD

These two repair the actual boot machinery.

1. Go to **Troubleshoot > Advanced options > Startup Repair**. Let it run fully — up to 20 minutes.
2. If it fails, open **Command Prompt** from the same menu and run:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
3. If `fixboot` reports "Access is denied," run this sequence instead:
   `bcdedit /export C:\BCD_Backup`
   `attrib C:\boot\bcd -h -r -s`
   `ren C:\boot\bcd bcd.old`
   `bootrec /rebuildbcd`
4. Type `Y` when asked to add the installation, then `exit` and restart. Manual BCD rebuilds succeed where the automated tool gives up surprisingly often. Microsoft's [recovery documentation](https://support.microsoft.com/en-us/windows) covers these bootrec commands in more depth.

### Fix 5: Boot into Safe Mode and remove ASUS utilities

If a normal boot loops but Safe Mode works, a startup program or driver is the culprit — and on ASUS machines, the ASUS utilities are prime suspects.

1. From the recovery screen, go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
2. Once in, open **Settings > Apps > Installed apps** and uninstall **Armoury Crate**, **MyASUS** (you can reinstall it later), and any third-party antivirus you added yourself.
3. Press **Win + X**, open **Device Manager**, expand **Display adapters**, right-click your GPU, and choose **Uninstall device** (tick the driver-removal box). Windows will use the basic adapter on the next boot — enough to get you in.
4. Restart normally. If the loop is gone, reinstall drivers one at a time from ASUS's official support page for your exact model — this is the step that stops the loop from returning. For general blue-screen patterns that sometimes hide behind a loop, our [Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) is a useful companion. If the machine specifically hangs on the restarting screen rather than looping to black, see [Windows 11 stuck on restarting screen](/articles/windows-11-stuck-on-restarting-screen-fix/).

### Fix 6: Use System Restore

A restore point rewinds system files, drivers, and registry to before the loop began.

1. Go to **Troubleshoot > Advanced options > System Restore**.
2. Choose a restore point dated **before** the looping started and run the wizard.
3. The laptop restarts on its own when done. Personal files aren't affected.
4. If there are no restore points, that's a lesson for later — turn on System Protection once you're back in (**System > About > System protection**).

### Fix 7: Check the drive, then reset if needed

If everything above failed, verify the hardware before the nuclear option.

1. Open **Command Prompt** from the recovery menu and run `chkdsk C: /f /r`. Give it time — over an hour on big drives.
2. You can also run ASUS's built-in diagnostics: power off, then hold **F2** while pressing power to enter the **MyASUS in UEFI** diagnostics and run the storage test.
3. If the drive is healthy but Windows still loops, go to **Troubleshoot > Reset this PC > Keep my files**. Choose **Cloud download** for the freshest files.
4. After the reset, install the chipset and graphics drivers from ASUS support *before* letting Windows Update run wild — that ordering prevents most repeat loops.

## Closing

Boot loops feel endless, but they're almost always one bad update, one bad driver, or one cached bad boot state — and Fixes 2 through 5 cover all three. The ASUS-specific lesson here: keep Armoury Crate, MyASUS, and your BIOS reasonably current, and install major Windows feature updates only after ASUS has posted matching drivers for your model. Do that, and the logo-to-black-to-logo merry-go-round stays a one-time story instead of a recurring nightmare.
