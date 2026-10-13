---
title: "'We Couldn't Complete the Updates, Undoing Changes' on an HP Laptop — Fixed"
slug: how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-hp-laptop
date: 2026-09-22
categories: ["windows-update"]
tags: ["hp laptop", "couldn't complete updates", "undoing changes", "hp support assistant", "windows 11"]
description: "HP laptop caught in the 'We couldn't complete the updates, undoing changes' loop? Fix it with HP-specific driver and BIOS steps plus ordered Windows repairs."
thumbnail: "/images/thumbs/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-hp-laptop.webp"
faqs:
  - q: "Why do HP laptops get stuck in the undoing changes loop?"
    a: "HP ships a deep OEM layer — HP Support Assistant services, custom power and thermal drivers, Bang & Olufsen or Realtek audio packages, and BIOS-level integrations — that Windows Update must migrate during feature updates. When one of these HP-specific components conflicts with the incoming build, the installer aborts and rolls back. Updating through HP's own channels before running Windows Update prevents most of these collisions."
  - q: "Should I use HP Support Assistant or Windows Update for drivers?"
    a: "Use HP Support Assistant or HP's support site for drivers on an HP laptop. HP validates its driver packages against your model's firmware, while Windows Update sometimes pushes generic versions that fail against HP hardware and trigger the rollback loop. Let HP handle drivers and BIOS, and let Windows Update handle OS patches — that division keeps both pipelines healthy."
  - q: "Can HP's built-in hardware diagnostics help with update loops?"
    a: "Yes. Pressing F2 or Esc at boot opens HP's UEFI diagnostics, which test the SSD, memory, and system board in minutes. Recurring rollbacks across different KB numbers often trace to marginal storage rather than software, and HP's diagnostics catch that quickly. Ruling out hardware first saves hours of servicing repairs aimed at the wrong target."
  - q: "Is updating the HP BIOS safe when updates keep failing?"
    a: "Yes, when done correctly. Download the BIOS update for your exact model from HP support or through HP Support Assistant, keep the charger connected, close all applications, and let the flash complete without interruption. BIOS updates fix firmware prerequisite failures that silently abort Windows 11 feature updates, making them a legitimate repair step rather than a risk."
---

HP laptops — Pavilion, Envy, Spectre, Omen, EliteBook — bring a characteristic software stack to every Windows update: HP Support Assistant and its background services, custom thermal and power drivers, audio packages tuned per model, and firmware integrations for HP docks and displays. When a Windows 11 feature update tries to migrate that stack and an HP component resists, the transaction aborts and you land on "We couldn't complete the updates, undoing changes."

HP also equips you well to fight back: HP Support Assistant keeps drivers and BIOS validated for your exact model, the UEFI diagnostics (F2 at boot) rule out hardware in minutes, and HP's support site documents model-specific update quirks. The playbook below uses them in order — let the rollback finish, bring HP's stack current, then apply the standard servicing repairs.

One HP-specific caution: if you use an HP USB-C dock, disconnect it before retrying the update. Dock drivers and display firmware are disproportionate contributors to migration failures, and the update goes much more smoothly without them attached. On HP business models, remember that Wolf Security and Sure Sense add a second security layer that behaves like another antivirus during installs — account for it before blaming Windows Update.

## Why this happens

- **HP OEM drivers conflicting with migration:** Support Assistant services and custom power/thermal drivers resisting replacement during feature updates.
- **Dock and display drivers:** HP USB-C docks stalling the plug-and-play migration phase.
- **Outdated HP BIOS firmware:** prerequisite mismatches on recent Windows 11 builds failing silently.
- **A corrupted update cache:** interrupted downloads failing integrity checks.
- **Insufficient free disk space:** the staged update plus rollback snapshot needs 10 to 20 GB.
- **Third-party antivirus locking files:** security suites intercepting file operations during installation.
- **Aging storage health:** older HP laptops with worn SSDs throwing errors the installer reads as corruption.
- **HP Wolf Security or Sure Sense interference:** HP's own security suite can behave like third-party antivirus, locking files during installation on business models.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Let the rollback finish, then run HP UEFI diagnostics

HP's built-in diagnostics give the fastest hardware verdict available — take it before assuming software.

1. Keep the charger connected and give the "undoing changes" screen 30 to 60 minutes, watching the disk light.
2. Once the machine is off, power on and press F2 (or Esc, then F2) to enter HP UEFI diagnostics.
3. Run the system and component tests, especially storage and memory.
4. If anything fails, address the hardware first — no servicing repair fixes a dying drive.
5. If hardware passes, continue below. For machines frozen on the rollback screen, our [HP undoing-changes stuck guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-hp-laptop/) covers recovery.

### Fix 2: Update drivers and BIOS through HP's own channels

HP-validated packages remove the top cause of these loops before Windows Update runs.

1. Open HP Support Assistant and install all offered drivers and firmware, prioritizing chipset, storage, and BIOS.
2. Alternatively, enter your serial number at [HP support](https://support.hp.com/us-en) for model-exact downloads.
3. Install BIOS updates with the charger connected and nothing else running.
4. Disconnect any HP dock before the next Windows Update attempt.
5. Reboot, then run Windows Update and retry the failed package.
6. On business models (EliteBook, ProBook), check HP's driver packs for your exact image — corporate configurations sometimes need HP's managed releases rather than the consumer ones.

### Fix 3: Run the Windows Update troubleshooter

Clear the generic blockages automatically once HP's side is current.

1. Open Settings, then System, then Troubleshoot, then Other troubleshooters.
2. Run the Windows Update troubleshooter and apply all recommended fixes.
3. Restart the laptop.
4. Check for updates again. If the troubleshooter will not run, the [troubleshooter repair guide](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-hp-laptop/) has the manual path.

### Fix 4: Reset the update cache

A poisoned SoftwareDistribution folder fails the same package identically on every retry.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` and `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart the services and reboot.
5. Retry Windows Update on a stable connection — Microsoft documents this on its [update support pages](https://support.microsoft.com/en-us/windows).

### Fix 5: Repair the component store with DISM and SFC

Store damage blocks staging for every package.

1. In an elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Allow 10 to 30 minutes for completion.
3. Run `sfc /scannow` afterward.
4. Reboot and retry the update.

### Fix 6: Free disk space and strip interference

Quick environmental wins.

1. Confirm at least 20 GB free on C: via Settings, then System, then Storage.
2. Run Disk Cleanup as administrator; select Windows Update Cleanup and Temporary files.
3. Disconnect USB peripherals and docks; temporarily disable third-party antivirus.
4. Disconnect any VPN during the attempt.
5. Retry Windows Update in this clean state.
6. If you run HP Wolf Security, add the update process to its exclusions temporarily rather than disabling protection entirely.

### Fix 7: Hide the failing update or repair-install Windows

Quarantine a repeat offender, or rebuild the servicing stack.

1. Note the failing KB in Update history.
2. Hide it with Microsoft's show-or-hide updates troubleshooter.
3. If rollbacks span multiple KBs, download the Windows 11 ISO from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
4. Mount the ISO, run setup.exe, choose "Keep personal files and apps," and allow 30 to 90 minutes.
5. Afterward, run HP Support Assistant first, then Windows Update.

## Closing

On HP laptops, the undoing-changes loop is usually a driver or firmware negotiation — and HP's own tools are the negotiators. Run Support Assistant ahead of Windows feature updates, keep the BIOS reasonably current, unplug the dock during the big installs, and keep the standard servicing repairs ready for the generic causes. The rollback screen appears when the installer trips; remove what it trips over and it stops appearing. Schedule HP Support Assistant to check monthly, and treat each Patch Tuesday as a two-step routine: HP's updates first, Windows' second.
