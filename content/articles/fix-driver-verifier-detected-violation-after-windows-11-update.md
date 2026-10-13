---
title: "Fix DRIVER_VERIFIER_DETECTED_VIOLATION After a Windows 11 Update"
slug: fix-driver-verifier-detected-violation-after-windows-11-update
date: 2026-09-21
categories: ["windows-errors"]
tags: ["driver verifier detected violation", "blue screen", "windows 11 update"]
description: "Fix DRIVER_VERIFIER_DETECTED_VIOLATION after a Windows 11 update: turn off Driver Verifier, identify the bad driver, and get your laptop booting again."
thumbnail: "/images/thumbs/fix-driver-verifier-detected-violation-after-windows-11-update.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_DETECTED_VIOLATION?"
    a: "It is stop code 0x000000C4. Driver Verifier — a Windows testing tool — caught a driver breaking the rules and crashed the system on purpose. It usually means Verifier was left running (sometimes enabled by a technician or a support tool) and has now flagged a real driver bug."
  - q: "My laptop keeps crashing in a loop. How do I stop it?"
    a: "Boot into Safe Mode, open an elevated Command Prompt, and run verifier /reset. This turns Driver Verifier off immediately. Your laptop should then boot normally, and you can investigate the flagged driver at your own pace."
  - q: "Should I just leave Driver Verifier turned off?"
    a: "Yes, unless you are actively debugging a driver. Verifier is a stress-test tool, not something for daily use — it slows the system and crashes it on purpose when it finds violations. Turn it off with verifier /reset once it has served its purpose."
  - q: "How do I find which driver Verifier flagged?"
    a: "Run verifier /query in an elevated Command Prompt to see which drivers are being verified. The crash dump also names the offending .sys file — you can read it with WinDbg or check Event Viewer for the bugcheck details."
---

A DRIVER_VERIFIER_DETECTED_VIOLATION blue screen means one specific thing: Driver Verifier was running, and it caught a driver misbehaving. This is different from most blue screens — the crash was deliberate. Verifier is a stress-testing tool built into Windows, and when it spots a driver breaking kernel rules, it forces a crash with stop code 0x000000C4 so the bug cannot hide.

After a Windows 11 update, this usually happens because Verifier was left enabled from an earlier troubleshooting session and the update changed drivers enough to trip its checks. The fix has two parts: turn Verifier off to stop the crash loop, then deal with the driver it flagged.

## Why this happens

- **Verifier was left running:** Someone — a technician, a support script, or you during earlier troubleshooting — ran `verifier` and never turned it off. It keeps testing drivers on every boot.
- **An update replaced a verified driver:** The Windows 11 update swapped driver versions, and the new version trips a check the old one passed (or Verifier is now watching drivers it was not watching before).
- **A genuinely buggy driver:** Sometimes Verifier is right — a third-party driver really is corrupting memory or mishandling IRPs, and the crash is doing you a favor by naming it.
- **Verifier settings too aggressive:** Verifying all drivers with all checks (rather than a targeted set) makes crashes likely on any system with imperfect third-party drivers.
- **Outdated drivers under new scrutiny:** Drivers written for older Windows versions often fail Verifier's stricter checks on Windows 11 24H2.
- **Corrupted driver files from the update:** A half-installed driver from Windows Update can fail verification even though the driver version itself is fine.

- **Leftover Verifier settings from a repair shop:** If a technician ever debugged this laptop, they may have enabled Driver Verifier and forgotten to switch it off — run `verifier /query` even if you never touched the tool yourself.
## How to fix it

Work through these in order — stop the crash loop first, investigate second.

### Fix 1: Turn off Driver Verifier from Safe Mode

1. If you are stuck in a crash loop, force the recovery environment: power off the laptop during boot three times in a row.
2. Go to **Troubleshoot → Advanced options → Startup Settings → Restart** and press **4** for Safe Mode.
3. Open an elevated Command Prompt: right-click **Start → Terminal (Admin)**.
4. Type `verifier /reset` and press Enter. Restart normally.
5. The crash loop should be gone. Do not skip the remaining steps — Verifier flagged a real problem, and the driver still needs attention.

### Fix 2: Find out which driver Verifier flagged

1. In an elevated Command Prompt, run `verifier /query` to list the drivers that were under verification.
2. Open **Event Viewer → Windows Logs → System** and look for **BugCheck** events around the crash times — the details name the offending driver file (e.g., `nvlddmkm.sys` or `rtwlanu.sys`).
3. Note the exact `.sys` filename. That file is your target for the next steps.
4. If you want the full story, open the minidump in WinDbg — see our [dump-reading guide](/articles/best-way-to-read-dump-files-with-windbg/) for the exact commands.

### Fix 3: Update the flagged driver from an official source

1. Identify the hardware behind the `.sys` file — search the filename to find which device it belongs to (graphics, Wi-Fi, audio, etc.).
2. Download the newest driver from the hardware vendor: [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, [Intel](https://www.intel.com/content/www/us/en/support/detect.html), or your laptop maker's support page.
3. Install it, choosing a **clean installation** option where offered.
4. Restart and use the laptop for a day. Most Verifier violations disappear with a current, properly installed driver.

### Fix 4: Roll back if the flagged driver just updated

1. Open **Device Manager**, find the device matching the flagged driver, and open **Properties → Driver**.
2. Click **Roll Back Driver** if available and follow the prompts.
3. If rollback is unavailable, uninstall the device (tick **Attempt to remove the driver**) and restart so Windows installs its inbox driver.
4. Then block Windows Update from reinstalling the bad version: pause updates for a couple of weeks or use the "show or hide updates" approach via the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) to install a known-good version manually later.

### Fix 5: Remove the software that installed the bad driver

1. Some `.sys` files belong to applications, not hardware — VPN clients, virtual drives, RGB software, and old antivirus products.
2. Open **Settings → Apps → Installed apps**, sort by date, and uninstall the program tied to the flagged driver.
3. Check **Device Manager → View → Show hidden devices** and remove any greyed-out leftovers from that software.
4. Restart. Application-installed kernel drivers are frequent Verifier victims because they are updated far less carefully than hardware drivers.

### Fix 6: Run SFC and DISM to repair system files

1. In an elevated Command Prompt, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`, then run SFC once more.
3. Restart. If the Windows 11 update left corrupted system files behind, Verifier can trip on Microsoft's own components — this repairs them. For broader context on post-update crashes, see our [post-update blue screen guide](/articles/how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update/).

### Fix 7: Re-enable Verifier briefly to confirm the fix (optional, advanced)

1. Only do this when the system has been stable for several days and you want proof the driver is clean.
2. Run `verifier /standard /all` in an elevated Command Prompt and restart.
3. Use the laptop normally for a few hours. No crash means the driver is behaving.
4. Immediately run `verifier /reset` afterwards — never leave Verifier running as a permanent setting.

### Fix 8: Stop Windows from reinstalling the bad driver

Fixing the driver once is not enough if Windows Update keeps putting the bad version back. Tell Windows to leave your drivers alone.

1. Press **Win + R**, type `sysdm.cpl`, and open the **Hardware** tab.
2. Click **Device Installation Settings** and select **No (your device might not work as expected)**, then save.
3. This stops Windows Update from replacing your manually installed drivers with its own versions.
4. Install your chosen good driver versions from the manufacturers, then restart.
5. Revisit this setting in a month or two — once vendors have shipped fixed drivers, you can safely turn automatic driver installation back on.

## Closing

DRIVER_VERIFIER_DETECTED_VIOLATION is genuinely good news wearing a blue screen costume: Verifier already did the detective work and pointed at the bad driver. Run `verifier /reset` to break the crash loop, identify the flagged `.sys` file, replace that driver from an official source, and then stop Windows Update from reinstalling the bad version. Leave Verifier off when you are done — it is a diagnostic instrument, not a daily companion — and the crashes go with it.
