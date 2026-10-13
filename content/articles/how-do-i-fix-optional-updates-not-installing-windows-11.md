---
title: "Optional Updates Won't Install on Windows 11? Here's the Fix"
slug: how-do-i-fix-optional-updates-not-installing-windows-11
date: 2026-10-12
categories: ["windows-update"]
tags: ["optional updates", "windows 11", "driver updates", "update not installing", "windows update"]
description: "Optional updates in Windows 11 download but never install? Diagnose why they stall — from driver conflicts to service glitches — and get them installing reliably."
thumbnail: "/images/thumbs/how-do-i-fix-optional-updates-not-installing-windows-11.webp"
faqs:
  - q: "What are optional updates in Windows 11?"
    a: "They are non-critical updates Windows offers but does not install automatically: mostly driver updates for your hardware, plus occasional feature experience packs and firmware. They appear under Settings, Windows Update, Advanced options, Optional updates, and you choose which to install."
  - q: "Do I actually need to install optional updates?"
    a: "Usually not urgently. Windows marks updates optional precisely because they are not security-critical — they are driver refinements and minor improvements. If your hardware works fine, skipping them is completely harmless. Install them when a device misbehaves, when you want the latest manufacturer refinements, or when you are doing periodic maintenance and have time to verify everything still works afterward."
  - q: "Why do optional updates fail while regular updates succeed?"
    a: "Because they are almost all driver packages, and driver installs fail for driver-specific reasons: the driver does not match the hardware, a newer version is already installed, or the device is disconnected. Regular cumulative updates do not have these hardware-matching failure modes."
  - q: "Can optional updates cause problems if they do install?"
    a: "Occasionally, yes. A faulty driver delivered as an optional update can cause glitches in the device it targets — which is exactly why Microsoft keeps these updates optional rather than automatic. If a device misbehaves immediately after you install one, open Device Manager, roll the driver back to the previous version, and then hide that specific update so it is not offered again."
---

Optional updates in Windows 11 sit in a strange middle ground: Windows thinks they are worth offering but not worth installing on its own. When you click Download & install and nothing happens — or the install fails silently — it is frustrating precisely because these updates were your choice. The good news is that optional update failures are almost always driver problems in disguise, and driver problems have clean, well-understood fixes.

This guide focuses on Windows 11's optional updates pipeline specifically. If your main cumulative updates are also failing, start with the broader [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-every-time-on-laptop/) instead — but if only the optional ones misbehave, you are in the right place.

It helps to know why Microsoft made these updates optional in the first place. Driver updates carry a small but real risk: a bad driver can destabilize hardware that was working fine, and Microsoft would rather let you choose that risk than impose it. That philosophy is also why optional updates get less engineering attention in the update pipeline \u2014 they are the first to stall on metered connections, the first to be skipped when services are degraded, and the last to get clear error messages. Understanding their second-class status explains much of their flaky behavior.

## Why this happens

- **Driver already superseded:** The most common cause. A newer driver is already installed (by the manufacturer utility or a previous manual install), so the older optional package fails the version check.
- **Hardware mismatch:** Windows Update's driver catalog occasionally offers a driver for a hardware variant you do not have, and the install fails at the matching step.
- **Device disconnected or disabled:** Optional drivers for printers, docks, or USB devices that are no longer connected fail because there is no target device.
- **Corrupt optional update cache:** The downloaded driver package is damaged, and every install attempt reads the same broken files.
- **Manufacturer utility conflicts:** Dell, HP, or Lenovo tools managing the same drivers can install competing versions that make Windows Update's package fail.
- **Stalled update services:** The Windows Update or BITS service in a wedged state can leave optional updates perpetually "downloading" without ever installing.
- **Metered connection throttling:** Optional updates are the first thing Windows deprioritizes on metered connections — see the [metered connection blocking guide](/articles/how-do-i-fix-metered-connection-blocking-windows-update/) if your connection is metered.
- **Pending restart blocking the queue:** An earlier update awaiting restart can hold the entire install queue, including optional items, in limbo.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and clear the pending queue

A surprising number of stuck optional updates just need a clean restart.

1. Save your work and restart the laptop normally — not shutdown with fast startup, a full restart.
2. After reboot, go to Settings, Windows Update, Advanced options, Optional updates.
3. Try installing one optional update at a time instead of batching them. Batching hides which package is the problem.

### Fix 2: Identify the failing update and check the device

1. In Update history, expand Driver Updates and find any failures with error codes.
2. Open Device Manager and verify the corresponding device reports as working properly.
3. If the device works, the optional driver is unnecessary — skip to Fix 6 to hide it. If the device misbehaves, continue; you actually need this driver.

### Fix 3: Install the driver from the manufacturer instead

1. Find your exact laptop model and go to the manufacturer's support site.
2. Download the driver for the device in question — it will be newer and better matched than the optional package.
3. Install it and restart.
4. Return to Optional updates; Windows usually withdraws its offering once a current driver is in place.

### Fix 4: Clear the update cache

1. Open an elevated Command Prompt.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Delete the contents of C:\Windows\SoftwareDistribution.
4. Restart the services with `net start`, reboot, and re-check Optional updates for a fresh download.

### Fix 5: Reset the update components

1. In the elevated Command Prompt, also stop `msiserver`, then restart all four services (wuauserv, bits, cryptsvc, msiserver).
2. Run the Windows Update troubleshooter from Settings, System, Troubleshoot, Other troubleshooters.
3. Retry the optional updates one at a time.

### Fix 6: Hide optional updates you do not need

1. Download Microsoft's "Show or hide updates" troubleshooter (wushowhide.diagcab).
2. Run it, choose Hide updates, and select the failing optional packages.
3. They will stop appearing. This is Microsoft's supported way to decline an optional driver — not a workaround.

### Fix 7: Check connection settings and repair system files

1. Go to Settings, Network & internet, Wi-Fi (or Ethernet), and make sure "Metered connection" is off — optional updates are deprioritized on metered links.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated Command Prompt.
3. Restart and make a final attempt. If a specific optional driver still fails while the device works fine, hiding it is the correct resolution. For official documentation of these steps, see the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 8: Check for policies suppressing optional updates

Something may be configured to hold optionals back.

1. On Pro editions, open gpedit.msc and navigate to Computer Configuration, Administrative Templates, Windows Components, Windows Update.
2. Look for policies about optional updates or driver updates and set anything suspicious back to "Not configured".
3. In Settings, Windows Update, Advanced options, verify "Receive updates for other Microsoft products" is on \u2014 its state affects optional update visibility.
4. Run `gpupdate /force`, restart, and recheck the Optional updates page.

## Closing

Optional updates fail for boring, specific reasons \u2014 usually a driver you do not need, a package that does not match your hardware, or a pipeline that deprioritizes them. The decision framework is simple: if the device works, hide the update; if the device misbehaves, get the driver from the manufacturer; if nothing optional installs at all, check the policies that may be suppressing them. Either way, you are done in one sitting, and your important security updates were never at risk.
