---
title: "How to Update Your Laptop BIOS Safely (The Right Way)"
slug: best-way-to-update-bios-on-laptop
date: 2026-09-25
categories: ["drivers"]
tags: ["bios update", "uefi", "firmware", "laptop firmware"]
description: "BIOS update needed on your laptop? Do it safely: the right file, AC power, no interruptions — plus how to recover if it goes wrong."
thumbnail: "/images/thumbs/best-way-to-update-bios-on-laptop.webp"
faqs:
  - q: "Is it safe to update the BIOS on a laptop?"
    a: "Yes, when done correctly — modern BIOS updates are routine and include safeguards like verification and dual-BIOS recovery on many models. The safety rules are absolute: use only the BIOS file for your exact model from the manufacturer's support page, stay plugged into AC power with a charged battery, close all programs, and never interrupt the process. Interruptions during the actual flash are what brick boards."
  - q: "Should I update the BIOS if everything works fine?"
    a: "Generally no. The old technician's rule — 'if it ain't broke, don't fix it' — applies to BIOS more than anywhere. Update when the release notes mention a problem you actually have (fan control, battery, security vulnerability, new CPU support), not just because a newer version exists. Each flash carries small risk; take it for a reason."
  - q: "How long does a BIOS update take?"
    a: "The actual flash usually takes 2–10 minutes, during which the screen may go black, the fans may spin up, and the laptop may reboot itself once or twice — all normal. Budget 30 minutes total including downloading, verifying, and the post-update boot. If the screen stays black longer than 30 minutes with no disk activity, then worry — not before."
  - q: "What happens if the BIOS update is interrupted?"
    a: "An interrupted flash can corrupt the firmware and leave the laptop unable to boot — a 'bricked' board. Many modern laptops have recovery: USB BIOS recovery (holding a key combo with a BIOS file on USB), dual-BIOS fallback, or a manufacturer recovery tool. Check your manufacturer's documentation for your model's specific recovery method before you start, so you know the escape route."
---

The BIOS (or UEFI firmware) is the lowest-level software on your laptop — it initializes hardware before Windows even starts. Updating it can fix fan curves, battery behavior, security vulnerabilities, and hardware compatibility. It can also brick the machine if interrupted mid-flash, which is why BIOS updates deserve more respect than driver updates. The good news: done by the book, they're uneventful.

The safe procedure: verify you actually need the update, get the exact file from your manufacturer, prepare (AC power, charged battery, backups), flash without touching anything, and verify afterward. Never use third-party "BIOS updater" tools, and never flash a BIOS file meant for a different model — even a close one. If a bad driver update is your actual problem rather than firmware, our [driver rollback guide](/articles/best-way-to-rollback-driver-update/) is the safer fix; for the chipset drivers that pair with BIOS updates, see [installing chipset drivers](/articles/how-can-i-install-chipset-drivers/).

## Why this happens

- **You need a fix the update provides**: Fan control bugs, battery quirks, and security patches (like LogoFAIL or CPU microcode fixes) are legitimate reasons.
- **Support asked you to**: Manufacturer troubleshooting sometimes requires the latest BIOS before they'll help further.
- **New hardware support**: CPU microcode or memory-compatibility updates needed for upgrades.
- **Windows Update offers a firmware update**: Microsoft distributes some OEM firmware through Windows Update — convenient but opaque.
- **BIOS settings got scrambled**: Sometimes "updating" is really about the reset that comes with it, which clears corrupted settings.
- **Security compliance**: BitLocker, Secure Boot, and corporate policies sometimes mandate minimum firmware versions.
- **Chasing performance**: Rarely a real reason — BIOS updates almost never make laptops faster.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decide whether you actually need the update

The most important step is deciding not to update.

1. Find your current BIOS version: press **Win + R**, type `msinfo32`, and note **BIOS Version/Date**.
2. Go to your manufacturer's support page — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — enter your exact model (or service tag/serial), and open the BIOS/driver section.
3. Read the release notes for versions newer than yours. Update if they mention: a problem you're experiencing, a security vulnerability (CVEs), or a fix in an area you care about (battery, thermals).
4. Don't update for: vague "improved system stability" with no details, versions far newer that skip many revisions (read intermediate notes), or simply because the number is bigger.
5. If Windows Update is offering a firmware update you didn't ask for, you can usually defer it — firmware via Windows Update is optional in most cases.

### Fix 2: Get the exact BIOS file from the manufacturer

Only the manufacturer's file for your exact model. No exceptions.

1. On the support page, triple-check the model — many laptops have sub-variants (e.g., "IdeaPad 5 15ITL05" vs. "15ARE05") with incompatible BIOS files. Use your serial number/service tag for certainty.
2. Download the BIOS update package — manufacturers provide either a Windows executable (easiest) or a USB-flash package (for BIOS-level flashing).
3. Verify the download if checksums are provided (compare the SHA-256) — a corrupted BIOS file is a brick waiting to happen.
4. Read the included instructions or the support page's flash guide for your model — some models have quirks (BitLocker suspension required, specific USB ports for flash drives).
5. Save a copy of the file somewhere safe (and keep the old version's installer if available) — you'll want it if you ever need to roll back.

### Fix 3: Prepare the laptop — power and backups

Non-negotiable pre-flight checks.

1. Plug into AC power with the original adapter, and ensure the battery is charged above 50% (most updaters refuse to run below a threshold — that's a feature, not a bug).
2. If you use BitLocker, **suspend** it first (**Manage BitLocker** > **Suspend protection**) — BIOS updates change firmware measurements and can trigger BitLocker recovery on next boot.
3. Close all applications, disable sleep/hibernate temporarily (**Settings** > **System** > **Power & battery** > set screen/sleep to **Never** for this session).
4. Disconnect all peripherals except AC power — docks, USB drives, external monitors. Flash with the minimal configuration.
5. Back up irreplaceable files. BIOS updates don't touch your data, but you're about to do the riskiest routine operation on the machine — backups are cheap insurance.

### Fix 4: Run the update and don't touch anything

The actual flash — boring is good.

1. If using the Windows executable: right-click > **Run as administrator**, confirm the current vs. new version numbers match your expectation, and start.
2. If using USB/BIOS flash: copy the file to a FAT32 USB drive, reboot into BIOS, and use the built-in flash utility (often called EZ Flash, Q-Flash, or similar) — follow the on-screen prompts.
3. Once the flash starts: do not touch the keyboard, do not close the lid, do not unplug anything. The screen may go black for minutes, fans may roar, the machine may reboot itself — all normal.
4. Wait for the explicit "update complete" message and the boot back into Windows. Budget up to 30 minutes before worrying.
5. If it seems stuck (black screen, no activity for 30+ minutes): don't yank power immediately — check for disk/activity LEDs; if truly dead, that's what Fix 7's recovery is for.

### Fix 5: Verify and reconfigure after the update

The update isn't done when the flash finishes.

1. On first boot, enter BIOS/UEFI and check the version number reflects the update.
2. BIOS updates often reset settings to defaults — reconfigure anything you changed: boot order, virtualization (VT-x/AMD-V), TPM/Secure Boot state, fan profiles, undervolts (write these down *before* updating).
3. If you suspended BitLocker, resume protection (**Manage BitLocker** > **Resume protection**).
4. Boot into Windows and verify everything works: Wi-Fi, audio, camera, battery charging. Driver reinstallation is sometimes needed after major firmware changes — particularly [chipset drivers](/articles/how-can-i-install-chipset-drivers/).
5. Use the laptop normally for a few days before declaring victory — firmware issues sometimes surface under specific workloads.

### Fix 6: Roll back the BIOS if the update caused problems

When the new firmware is worse than the old.

1. Check whether your manufacturer supports BIOS rollback — Dell and Lenovo generally allow flashing an older version; HP often restricts it. Check the support page or manual.
2. If allowed, download the previous version and flash it using the same safe procedure (Fixes 3–4).
3. If rollback is blocked, check for a *newer* BIOS that fixes the regression — manufacturers sometimes ship quick follow-ups.
4. For settings-level problems (not firmware bugs), **Load Optimized Defaults** in BIOS often resolves post-update weirdness without reflashing.
5. Document what the bad version broke — if you contact support, precise symptoms ("fan stuck at 100% after BIOS 1.14") get faster escalation than "BIOS bad."

### Fix 7: Recover from a failed flash

The escape routes — know them before you need them.

1. **USB BIOS recovery**: Many laptops support crisis recovery — a specific key combo (often **Win + B** or **Fn + Esc** held at power-on, varies by maker) with the BIOS file on a FAT32 USB stick. Look up your model's exact combo in the manual *before* flashing.
2. **Dual BIOS**: Some gaming/business laptops have a backup BIOS that auto-recovers — if the machine boots after several failed attempts, let it sit; it may be recovering.
3. **Manufacturer recovery tools**: Dell, HP, and Lenovo each have documented BIOS recovery procedures — search their support sites for "BIOS recovery" + your model.
4. If nothing works and the machine shows zero signs of life (no lights, no fan), it's a board-level repair — the BIOS chip can sometimes be reprogrammed by a shop with an SPI programmer, or the board needs replacement.
5. Lesson for next time: the recovery research in step 1 takes five minutes and turns a potential brick into an inconvenience. Always know the escape route before flashing.

## Closing

BIOS updates are safe when they're boring: right file, right model, AC power, no interruptions, verify after. The risk isn't in the update itself — it's in rushing it, grabbing the wrong file, or flashing on a dying battery. Respect the firmware layer and it respects you back.
