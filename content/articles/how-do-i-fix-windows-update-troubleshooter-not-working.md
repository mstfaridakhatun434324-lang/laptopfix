---
title: "Windows Update Troubleshooter Not Working? Here's How to Fix the Fixer"
slug: how-do-i-fix-windows-update-troubleshooter-not-working
date: 2026-10-10
categories: ["windows-update"]
tags: ["update troubleshooter", "windows 11 24h2", "diagnostics", "troubleshooting", "services"]
description: "Fix the Windows Update troubleshooter when it crashes, hangs, or reports it can't run — repair its dependencies and get automated update repair working again."
thumbnail: "/images/thumbs/how-do-i-fix-windows-update-troubleshooter-not-working.webp"
faqs:
  - q: "Why does the Windows Update troubleshooter fail to start?"
    a: "It usually fails because the Background Intelligent Transfer Service or the Cryptographic Services it depends on are stopped or corrupted. Damaged system files and broken Windows Update components also prevent the troubleshooter from loading its diagnostic scripts. Checking these services in services.msc takes a minute and resolves most startup failures immediately."
  - q: "What does error 0x80070005 mean in the troubleshooter?"
    a: "Error 0x80070005 is an access-denied code. It means the troubleshooter cannot read or write the files and registry keys it needs, often because permissions were damaged by a third-party optimizer or a partially rolled-back update. Resetting permissions and rerunning as administrator resolves it. Running the System File Checker afterward restores the default permissions that optimizer tools stripped away."
  - q: "Is there a manual alternative to the troubleshooter?"
    a: "Yes. You can manually reset the Windows Update components with Command Prompt commands, clear the SoftwareDistribution folder, and re-register update DLLs. The manual path achieves everything the automated tool does and is often more reliable. Many technicians prefer the manual approach because each step produces visible feedback about what was actually repaired."
  - q: "Should I download a troubleshooter from a third-party site?"
    a: "No. Microsoft now ships troubleshooters inside the Settings app and the Get Help app. Third-party downloads claiming to be official troubleshooters are a common malware vector. Use only the built-in tools or scripts you type yourself. If a site insists you need their fix tool, close the tab — it is either useless or malicious, and the built-in tools cover every legitimate scenario."
---

The Windows Update troubleshooter is supposed to be the easy button: one click, and it diagnoses stuck downloads, broken services, and corrupted caches for you. So when the troubleshooter itself refuses to run — crashing on launch, hanging at "detecting problems," or finishing instantly with a cryptic error — it feels like the safety net has a hole in it. Good news: a dead troubleshooter is one of the most diagnosable problems in Windows, because it only has a handful of dependencies.

Work through this guide like a repair ticket. Each fix targets one specific dependency the troubleshooter needs, in the order a technician would check them. By the end, either the tool runs cleanly or you will have performed the manual equivalent of everything it does.

## Why this happens

- **Stopped dependency services:** The troubleshooter leans on Background Intelligent Transfer Service (BITS), Cryptographic Services, and the Windows Update service itself. If any are disabled, the tool cannot start its checks.
- **Corrupted system files:** The troubleshooter's diagnostic packages live in the system component store. Corruption there breaks the scripts before they execute.
- **Broken update components:** If SoftwareDistribution or the Catroot2 folder is damaged, the troubleshooter's first scan step hangs or errors out immediately.
- **Permission damage:** Third-party "debloater" and "optimizer" tools strip permissions from update-related registry keys and folders, causing access-denied failures like 0x80070005.
- **Stale troubleshooter cache:** The Get Help app caches diagnostic packages; a stale or half-downloaded cache makes every run fail the same way.
- **Pending restart locks:** A servicing operation waiting on a reboot holds locks on update files, and the troubleshooter cannot get the exclusive access it needs.
- **Conflicting security software:** Aggressive antivirus or firewall products can quarantine the troubleshooter's temporary scripts or block its network checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the three services the troubleshooter depends on

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Background Intelligent Transfer Service** — set Startup type to **Manual** (or Automatic) and start it if stopped.
3. Do the same for **Cryptographic Services** (Automatic) and **Windows Update** (Manual/trigger-start).
4. Now run the troubleshooter again via **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**.

### Fix 2: Clear a pending restart that is blocking the tool

1. Save your work, then fully restart the laptop — not shut down, but **Restart**, which clears pending servicing locks.
2. After the reboot, wait five minutes for background startup tasks to settle before touching anything.
3. Try the troubleshooter again. A surprising number of "troubleshooter won't run" tickets end right here.
4. If Windows is [stuck on the restarting screen](/articles/best-way-to-fix-windows-update-stuck-on-restarting-screen/) instead of completing the reboot, resolve that first — nothing else can proceed until the machine boots cleanly.

### Fix 3: Repair system files with SFC and DISM

1. Open **Terminal (Admin)** or an elevated Command Prompt.
2. Run `sfc /scannow` and wait for it to complete — do not close the window early.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store the troubleshooter's packages live in.
4. Restart once more and rerun the troubleshooter; repaired system files resolve most crash-on-launch cases.

### Fix 4: Reset Windows Update components manually

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. This is the manual equivalent of the troubleshooter's deepest repair — if [driver updates keep failing](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) too, this reset usually fixes both at once.

### Fix 5: Reset the Get Help app and its diagnostic cache

1. Open **Settings > Apps > Installed apps**, find **Get Help**, click the three dots, and choose **Advanced options**.
2. Click **Repair** first and test; if that fails, click **Reset** (this clears cached diagnostic packages).
3. Alternatively, launch the troubleshooter from the classic path: **Settings > System > Troubleshoot > Other troubleshooters**.
4. A fresh diagnostic package download often fixes the "hangs at detecting problems" symptom.

### Fix 6: Check permissions damage from optimizer tools

1. Think back: did you run a debloater, "privacy" script, or registry cleaner? These are the top cause of 0x80070005 in the troubleshooter.
2. Undo what you can through the tool's own restore/backup feature, then restart.
3. As a deeper repair, the SFC/DISM pass from Fix 3 restores many default permissions on system files.
4. Going forward, avoid registry cleaners entirely — Microsoft's own guidance at [Windows support](https://support.microsoft.com/en-us/windows) warns they cause more update breakage than they ever fix.

### Fix 7: Temporarily rule out security software interference

1. If you run third-party antivirus, temporarily disable its real-time protection (keep Windows Firewall on).
2. Rerun the troubleshooter immediately while protection is paused.
3. If it works, add an exclusion for `C:\Windows\diagnostics` or switch to Microsoft Defender, which never conflicts with built-in troubleshooters.
4. Re-enable protection right after the test — never leave the laptop unprotected while browsing.

### Fix 8: Re-register the diagnostic packages with PowerShell

1. Open an elevated PowerShell and run `Get-TroubleshootingPack -Path "C:\Windows\diagnostics\system\WindowsUpdate" | Invoke-TroubleshootingPack` to execute the Windows Update diagnostic pack directly, bypassing the Settings UI.
2. If the path is missing or the command errors, the diagnostic store itself is damaged — copy it from a healthy Windows 11 machine of the same build.
3. You can also force a fresh troubleshooter download by deleting `%localappdata%\Microsoft\Windows\GetHelp` cache data and relaunching Get Help.
4. A troubleshooter that runs from PowerShell but not from Settings points at a broken Settings-app registration, which an in-place upgrade repairs while keeping your files.

## Closing

A broken troubleshooter is annoying, but it is also a useful early warning: the same damaged services, files, or permissions that stop the tool will eventually stop real updates too. Fixing the fixer now — services, system files, component reset — leaves the whole update pipeline healthier than before. Once the tool runs green again, let it do its job on whatever update problem sent you here in the first place.
