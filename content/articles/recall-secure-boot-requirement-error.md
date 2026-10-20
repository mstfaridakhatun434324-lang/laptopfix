---
title: "How to Fix the Recall Secure Boot Requirement Error on Windows 11"
slug: recall-secure-boot-requirement-error
date: 2026-10-20
categories: ["ai-pc"]
tags: ["recall secure boot", "secure boot requirement", "troubleshooting", "ai pc", "windows 11 uefi"]
description: "Recall blocked by a Secure Boot requirement error? Learn what Secure Boot does, why Recall needs it, and how to enable it in UEFI on your Copilot+ PC."
thumbnail: "/images/thumbs/recall-secure-boot-requirement-error.webp"
faqs:
  - q: "What is Secure Boot and why does Recall require it?"
    a: "Secure Boot is a UEFI firmware feature that only allows trusted, signed software to load during startup. Recall requires it because it stores sensitive snapshots locally, and Microsoft wants the boot chain protected against malware that could tamper with Recall's data."
  - q: "Will enabling Secure Boot delete my files?"
    a: "No. Enabling Secure Boot changes only a firmware setting that controls what is allowed to boot. Your files, apps, and Windows installation are untouched."
  - q: "My PC doesn't have a Secure Boot option. What now?"
    a: "Very old PCs that boot in legacy BIOS (CSM) mode lack Secure Boot entirely. Recall requires a Copilot+ PC with modern UEFI firmware, so if your machine genuinely has no Secure Boot option, it does not meet Recall's hardware requirements and the feature cannot be enabled."
  - q: "Can I bypass the Secure Boot check for Recall?"
    a: "There is no supported bypass. The Secure Boot requirement is enforced as part of Recall's security model alongside BitLocker and Windows Hello. Disabling or circumventing it would defeat the protections the feature was designed with."
---

Of all the prerequisites Recall demands, Secure Boot produces the most confusing error message. Users see a terse warning that their PC "doesn't meet the Secure Boot requirement," with no explanation of what Secure Boot is or where to find it. Unlike a missing driver, this is a firmware setting buried in your UEFI — the pre-Windows environment most people never open — so it feels far more intimidating than it actually is.

The reasoning behind the requirement is security: if malware could slip in before Windows loads, it could compromise everything Recall stores. Secure Boot guarantees that only trusted, signed code runs at startup, closing that hole. This guide explains how to check your Secure Boot state and enable it correctly, step by step.

One important note: Secure Boot is one of several firmware-level requirements. If enabling it doesn't clear Recall's error, check encryption next — see [Recall not working with BitLocker enabled](/articles/recall-not-working-bitlocker-enabled/).

## Why this happens

- **Secure Boot is disabled in UEFI:** The most common cause — the setting exists but was switched off, sometimes by a previous owner or a repair shop.
- **CSM/legacy boot mode is active:** Compatibility Support Module forces legacy BIOS booting, which disables Secure Boot by definition.
- **Disk uses MBR partitioning:** Secure Boot with UEFI requires a GPT-partitioned system disk; MBR disks boot in legacy mode.
- **BIOS update reset firmware settings:** Some firmware updates revert custom settings, silently turning Secure Boot off.
- **Custom or cleared Secure Boot keys:** If the key database was cleared or set to custom mode, Windows may report Secure Boot as off or unsupported.
- **Dual-boot configurations:** Linux or other OS installations sometimes require Secure Boot to be disabled, and it was never re-enabled.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check your current Secure Boot state in Windows

Before touching firmware settings, confirm what Windows actually reports. This tells you whether Secure Boot is off, on, or unsupported.

1. Press Win + R, type `msinfo32`, and press Enter to open System Information.
2. Find the "Secure Boot State" row and note whether it says On, Off, or Unsupported.
3. Also check "BIOS Mode" — it must say UEFI, not Legacy, for Secure Boot to be possible.
4. If Secure Boot State is Unsupported, your hardware lacks the feature and Recall cannot run on this PC.
5. If it says Off with BIOS Mode UEFI, continue to the next fix to enable it.

### Fix 2: Enable Secure Boot in UEFI firmware

This is the core fix for most users. The setting lives in your firmware's security or boot section, and while every manufacturer's menu looks different, the path is consistent: find the Secure Boot option and switch it on.

1. Open Settings, go to System, then Recovery, and click Restart now under Advanced startup.
2. Choose Troubleshoot, then Advanced options, then UEFI Firmware Settings, and click Restart.
3. In the firmware menus, navigate to the Security or Boot tab and find the Secure Boot option.
4. Change Secure Boot from Disabled to Enabled.
5. If Secure Boot is greyed out, look for a CSM or Legacy Boot option and disable that first.
6. Save changes and exit — the PC will reboot into Windows with Secure Boot active.

### Fix 3: Convert MBR to GPT if the disk blocks UEFI boot

Secure Boot cannot work on an MBR-partitioned system disk, because MBR implies legacy booting. Windows includes a safe, non-destructive conversion tool, but back up important data first.

1. Open Command Prompt as administrator.
2. Run `mbr2gpt /validate /disk:0 /allowFullOS` to check whether conversion is possible.
3. If validation succeeds, run `mbr2gpt /convert /disk:0 /allowFullOS` and wait for it to finish.
4. Restart into UEFI firmware settings and confirm the boot mode is now UEFI rather than Legacy.
5. Enable Secure Boot using the steps in Fix 2, then save and exit.

### Fix 4: Restore default Secure Boot keys

If Secure Boot shows as enabled in firmware but Windows still reports it off, the key database may have been cleared or corrupted. Restoring factory keys re-establishes the trust chain.

1. Enter UEFI firmware settings using the Advanced startup path from Fix 2.
2. Find the Secure Boot section and look for Key Management or a similar submenu.
3. Choose the option to restore factory default keys or install default Secure Boot keys.
4. Confirm Secure Boot mode is set to Standard rather than Custom.
5. Save, exit, and boot into Windows.
6. Verify in `msinfo32` that Secure Boot State now reports On.

### Fix 5: Check for Group Policy disabling Secure Boot enforcement

On managed PCs, a policy can interfere with how Windows evaluates the Secure Boot requirement, producing a requirement error even when firmware is correct. This overlaps with policy-driven Recall problems — see [Recall group policy keeps disabling it](/articles/recall-group-policy-keeps-disabling/) for the broader picture.

1. Press Win + R, type `gpedit.msc`, and press Enter (Pro editions; Home users can skip this).
2. Browse Computer Configuration, Administrative Templates, System, Device Guard and related security nodes.
3. Look for policies governing Secure Boot or virtualization-based security set to Disabled.
4. Set any conflicting policies to Not Configured and restart the PC.
5. Re-check Secure Boot State in `msinfo32` and test Recall again.
6. On organization-owned PCs, ask IT before changing policies — the restriction may be intentional.

### Fix 6: Update UEFI firmware from the manufacturer

A buggy or outdated firmware can misreport Secure Boot status or fail to enforce it properly. Manufacturers regularly fix these issues in BIOS updates. Some users mistake this for an unrelated feature outage, like the [Copilot daily briefing not showing](/articles/copilot-daily-briefing-not-showing/), but firmware-level Recall blocks always trace back to the requirements stack.

1. Identify your exact laptop model from System Information or the manufacturer's sticker.
2. Visit your manufacturer's support site — for example [Dell support](https://www.dell.com/support) or [HP support](https://support.hp.com/us-en) — and find the latest BIOS/UEFI update.
3. Download the update and run it with the laptop plugged into AC power — never on battery alone.
4. Let the update complete without interruption; the PC will reboot itself.
5. Re-enter firmware settings, confirm Secure Boot is still enabled, and save.
6. Boot Windows, verify Secure Boot State is On, and open Recall.

## Closing

The Secure Boot requirement error looks scary because it points at firmware, but the fix is usually a single toggle in your UEFI settings — occasionally preceded by a disk conversion or a key restore. Once `msinfo32` reports Secure Boot State as On with UEFI boot mode, Recall's firmware check is satisfied for good. If Recall still refuses after that, the block is elsewhere in its security stack. And since Recall depends on the whole Copilot+ platform being healthy, the walkthrough for [Intel AI Boost driver installation problems](/articles/intel-ai-boost-driver-not-installing/) is worth a look too.
