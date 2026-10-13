---
title: "How to Update Your Laptop BIOS on Windows 11 24H2 Safely"
slug: how-to-update-bios-on-laptop-in-windows-11-24h2
date: 2026-09-05
categories: ["drivers"]
tags: ["bios update", "firmware", "windows 11 24h2", "uefi", "laptop maintenance"]
description: "Need to update your laptop BIOS on Windows 11 24H2? Follow this safe, step-by-step method with precautions that prevent a bricked machine."
thumbnail: "/images/thumbs/how-to-update-bios-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Is it safe to update my laptop's BIOS?"
    a: "Yes, when done correctly: with the charger plugged in, the battery charged, no interruptions, and the exact BIOS file for your model. Modern BIOS updates are routine and include safety checks. The danger comes from power loss mid-flash or installing the wrong model's BIOS — both are entirely preventable by following the precautions in this guide."
  - q: "How do I check my current BIOS version?"
    a: "Press Win+R, type msinfo32, and look for BIOS Version/Date in the system summary. Compare it against the latest version on your laptop manufacturer's support site for your exact model. Only update if the new version is actually newer or fixes a specific problem you have — BIOS updates aren't like app updates you install reflexively."
  - q: "Will a BIOS update delete my files or Windows?"
    a: "No. A BIOS update only rewrites firmware on the motherboard — your files, Windows installation, and programs are untouched. However, BIOS updates can reset firmware settings (boot order, virtualization, secure boot), so note your custom settings beforehand. Backing up important files before any firmware operation is still wise practice."
  - q: "What should I do if a BIOS update fails or interrupts?"
    a: "Don't panic and don't power off — many laptops can recover. First, wait at least 30 minutes; some updates appear stuck but are still working. If it's truly dead, most modern laptops have a BIOS recovery feature (check your manufacturer's documentation for the key combination). If recovery fails, it's a manufacturer repair — which is why the charger-plugged-in rule is absolute."
---

The BIOS (or UEFI, technically) is the firmware that wakes your hardware before Windows even exists. Updating it fixes hardware bugs, patches security vulnerabilities, improves battery behavior, and sometimes unlocks performance — but it also carries the most feared warning in computing: interrupt it and you can brick the machine. That warning is real, but it's also manageable. Thousands of BIOS updates happen safely every day because the process is straightforward when you respect the rules.

On Windows 11 24H2 specifically, BIOS updates matter more than usual: the new Windows build changed how it interacts with firmware, and manufacturers have shipped BIOS updates addressing compatibility, sleep behavior, and driver handoff. This guide gives you the safe method — preparation, verification, the update itself, and what to check afterward — whether your manufacturer delivers BIOS through Windows Update, their own app, or a manual flash.

## Why this happens

- **Firmware bugs need firmware fixes:** Hardware quirks (sleep/wake failures, fan misbehavior, USB issues) live below the OS — only a BIOS update reaches them.
- **Windows 11 24H2 changed firmware expectations:** The new build exercises UEFI features more aggressively, exposing firmware bugs that older Windows tolerated silently.
- **Security vulnerabilities in firmware:** Researchers regularly find UEFI vulnerabilities; manufacturers patch them via BIOS updates you should install.
- **New hardware support:** BIOS updates add compatibility for newer CPUs, memory, or storage that didn't exist when the laptop shipped.
- **Driver dependencies:** Some driver packages check the BIOS version and refuse to install on outdated firmware — a failed driver install is sometimes really a stale BIOS.
- **Corrupted firmware settings:** A bad settings state can mimic hardware failure; updating (or even just resetting) the BIOS clears it.
- **Manufacturer update utilities:** Dell, HP, Lenovo, and ASUS all ship tools that deliver BIOS updates through Windows — convenient but still firmware flashes deserving respect.
- **Skipped updates compound:** Missing several BIOS generations can make the jump to a new Windows build rocky, since each update assumed the previous one's fixes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decide whether you actually need the update

1. Press **Win+R**, type `msinfo32`, and note your **BIOS Version/Date**.
2. Visit your manufacturer's support site, enter your model/serial, and compare against the latest BIOS.
3. Read the release notes: update if it fixes a problem you have, patches a security issue, or adds Windows 11 24H2 compatibility. If your BIOS is current and everything works, the best update is no update.

### Fix 2: Prepare the machine properly

1. Plug in the **original charger** — not a dock, not a USB-C phone charger. Verify the battery is charging.
2. Close all programs and disable sleep: **Settings > System > Power & battery** — set screen and sleep to **Never** temporarily.
3. Disconnect all external devices except the charger (docks, USB drives, external monitors).
4. Back up critical files. The update won't touch them, but firmware operations deserve a backup as a matter of principle.

### Fix 3: Note your current BIOS settings

1. Restart and enter the BIOS setup (F2/Del/F10 depending on brand).
2. Photograph or write down any custom settings: boot order, virtualization (VT-x/AMD-V), Secure Boot state, TPM, fan profiles, MUX/GPU mode.
3. Exit without saving changes. After the update you may need to restore these — particularly virtualization and Secure Boot, which affect VMs and some games' anti-cheat.

### Fix 4: Use the manufacturer's recommended method

1. **Preferred:** Use the manufacturer's update utility (Dell SupportAssist, Lenovo Vantage, HP Support Assistant, MyASUS) — it verifies the file matches your machine automatically.
2. **Alternative:** Download the BIOS file from the [manufacturer's official support site](https://www.dell.com/support) (Dell shown; use your brand's portal) and run the Windows-based flasher it provides.
3. **Advanced:** Some manufacturers offer USB-based flashing from within the BIOS itself — the safest method, since Windows isn't involved at all. Follow their guide exactly.
4. Never download BIOS files from third-party sites. Ever. A wrong or tampered firmware image is the one mistake recovery can't always fix.

### Fix 5: Run the update without interruption

1. Launch the updater and confirm the target version matches what you downloaded.
2. Click through and **do not touch the machine** — no typing, no closing the lid, no unplugging anything.
3. The laptop will reboot one or more times, possibly showing a progress bar or a black screen for several minutes. This is normal.
4. Wait until Windows fully loads again before declaring success. If the screen stays black longer than 30 minutes, consult the manufacturer's BIOS recovery procedure — don't power off in a panic at minute ten.

### Fix 6: Verify and restore settings afterward

1. Run `msinfo32` again and confirm the BIOS version updated.
2. Enter the BIOS and check that your custom settings survived; restore virtualization, Secure Boot, and boot order from your notes if they were reset.
3. Boot into Windows and verify the problem the update was meant to fix. Check Device Manager for any new warnings — occasionally a BIOS update changes hardware IDs and Windows wants a driver refresh. If a driver broke after the update, the [battery-after-BIOS-update guide](/articles/how-to-fix-battery-not-charging-after-bios-update-on-windows-11/) covers the most common post-flash driver symptom, and the [24H2 battery variant](/articles/how-to-fix-battery-not-charging-after-bios-update-in-windows-11-24h2/) addresses the Windows 11 24H2-specific cases.

### Fix 7: Know the recovery options

1. Learn your manufacturer's **BIOS recovery** key combination before you need it (many use Win+B or Fn+Esc held during power-on with a recovery USB).
2. If an update fails: wait 30+ minutes, then attempt the recovery procedure with the charger connected.
3. If recovery fails, contact manufacturer support — a failed flash under warranty is their repair, and having followed their official process strengthens your case. Document the exact BIOS versions involved.

## Closing

BIOS updates are safe when you treat them with the respect firmware deserves: right file, charger in, no interruptions, settings noted. On Windows 11 24H2 they're more relevant than ever, with manufacturers actively shipping compatibility and security fixes. Update deliberately — for a reason, not out of habit — and your laptop's foundation stays solid for everything Windows builds on top of it.
