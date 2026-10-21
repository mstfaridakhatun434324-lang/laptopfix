---
title: "How to Fix NPU Error Code 52 (Unsigned Driver)"
slug: npu-error-code-52-unsigned-driver
date: 2026-10-21
categories: ["ai-pc"]
tags: ["npu error code 52", "unsigned driver", "driver signature", "device manager", "ai pc", "troubleshooting"]
description: "NPU blocked by error code 52 for an unsigned driver? Learn what breaks driver signature checks and restore your neural processor with six step-by-step fixes."
thumbnail: "/images/thumbs/npu-error-code-52-unsigned-driver.webp"
faqs:
  - q: "What does NPU error code 52 mean?"
    a: >
      Code 52 means Windows refused to load the NPU driver because its digital signature couldn't be verified. Windows 11 requires signed drivers as a security boundary, so it blocks the driver entirely rather than risk loading tampered code. Your files and settings are untouched.
  - q: "Should I disable driver signature enforcement to fix it?"
    a: >
      No — that's a diagnostic shortcut some guides suggest, but it weakens a core Windows security protection and the fix doesn't survive reboots. The methods below get you a properly signed driver instead, which is the real solution.
  - q: "Did my NPU driver come from a bad source?"
    a: >
      Often, yes: third-party driver updaters and unofficial download sites distribute modified or outdated driver packages with broken signatures. Drivers from your laptop maker or the chip vendor are properly signed — get those and code 52 disappears.
  - q: "Can Secure Boot cause code 52?"
    a: >
      Secure Boot doesn't cause it, but it enforces the same signature policy more strictly. If code 52 appeared after toggling Secure Boot or updating the BIOS, the driver was likely already improperly signed and the stricter check merely exposed it.
---

Device Manager shows your NPU with a yellow warning: "Windows cannot verify the digital signature for the drivers required for this device (Code 52)." The neural processor is present, Windows knows what it is — and refuses to load its driver anyway. Studio Effects, Recall, and every other NPU feature goes dark.

Code 52 is Windows' security boundary doing its job. Every kernel driver on Windows 11 must carry a valid digital signature proving it comes from a trusted publisher and hasn't been tampered with. When that check fails, Windows blocks the driver completely rather than gamble on untrusted code running at the deepest level of your system.

The fix is almost never to weaken the security check — it is to give Windows a driver that passes it. This guide walks through six fixes in technician order: identify the bad package, replace it with a properly signed one, and clean up anything that keeps dragging the unsigned copy back.

## Why this happens

- **Driver from an unofficial source:** Third-party driver updaters and random download sites distribute repackaged, outdated, or modified NPU drivers whose signatures are broken or missing. This is the number one cause of code 52.
- **Corrupt driver files:** A signature is a cryptographic seal over the driver files. If an interrupted install or disk error alters even one byte, the seal no longer matches and Windows reports code 52.
- **Expired signing certificate:** Driver signatures are timestamped, but very old packages can still trip verification on systems with strict policies or incorrect clocks.
- **Wrong system clock:** Signature verification is time-sensitive. A CMOS battery failure that resets your clock to 2015 can make a perfectly valid signature look untrustworthy.
- **Leftover driver store contamination:** An unsigned package lingering in the Driver Store can get reinstalled over your good driver, bringing code 52 back like a bad sequel.
- **Tampered or patched driver:** "Modded" drivers that unlock features or bypass limits break their signatures by definition — Windows will always block them with code 52 on a default configuration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check where the current driver came from

Before replacing anything, confirm the diagnosis. The driver's origin usually tells the whole story.

1. In Device Manager, open the NPU's **Properties > Driver** and note the **Driver Provider** and **Driver Date**.
2. If the provider is unknown, blank, or a name you don't recognize — instead of Intel, AMD, Qualcomm, or your laptop maker — you have found your unsigned package.
3. Check the **Digital Signer** field on the **Details** tab (property: Digital Signer). Missing or untrusted signer confirms code 52's complaint.
4. If the driver came from a third-party updater, uninstall that updater too — otherwise it will "helpfully" reinstall the bad driver later.

### Fix 2: Correct the system clock

It sounds too simple, but a wrong clock genuinely breaks signature verification. Rule it out in thirty seconds before doing driver surgery.

1. Right-click the clock in the taskbar and open **Adjust date/time**.
2. Enable **Set time automatically** and **Set time zone automatically**, then click **Sync now**.
3. Restart and check Device Manager — if code 52 clears, the clock was the whole problem.
4. If the clock resets to a wrong date on every boot, your CMOS battery is dying; replace it (or have a shop do it) so the problem doesn't return.

### Fix 3: Install the properly signed driver from your laptop maker

This is the real fix in most cases. OEM drivers are signed with the vendor's certificate and validated against your exact model.

1. Find your exact model in **Settings > System > About**.
2. On [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support, download the latest NPU/chipset driver package for Windows 11.
3. In Device Manager, uninstall the NPU with **"Attempt to remove the driver for this device"** checked, then restart.
4. Run the OEM installer as administrator, restart, and verify the warning is gone and the Digital Signer field shows a trusted publisher.

### Fix 4: Purge the unsigned package from the Driver Store

If code 52 returns after you install the good driver, an unsigned copy is lurking in the Driver Store and Windows keeps reinstalling it. This is also worth doing when [signature verification failed during the install itself](/articles/npu-driver-signature-verification-failed/).

1. Open an elevated terminal and run `pnputil /enum-drivers` to list third-party driver packages.
2. Find entries from the NPU vendor with old dates or unknown providers and note their published names (oemNN.inf).
3. Remove each suspect with `pnputil /delete-driver oemNN.inf /uninstall /force`, being careful to target only NPU-related packages.
4. Reinstall your signed OEM driver, restart, and confirm code 52 stays gone.

### Fix 5: Get the driver from the chip vendor as a fallback

When your laptop maker hasn't published a recent NPU driver, the chip vendor's own signed package is the next-best source — still properly signed, still trustworthy.

1. Identify your NPU: Intel Core Ultra (AI Boost), AMD Ryzen AI, or Snapdragon X.
2. For Intel, use [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html); for AMD, the [AMD driver page](https://www.amd.com/en/support/download/drivers.html). Download only from these official pages.
3. Uninstall the current NPU driver with file deletion, restart, then install the vendor package as administrator.
4. Verify the Digital Signer field and test an AI feature — [Recall indexing](/articles/recall-indexing-stuck-fix/) is a good stress test since it exercises the NPU continuously.

### Fix 6: Repair Windows' signature infrastructure

Rare, but real: the problem isn't the driver, it's Windows' ability to verify anything. Corrupt certificate stores or damaged system files make every signature check fail.

1. Run `sfc /scannow` in an elevated terminal, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Open **certmgr.msc** and confirm the **Trusted Publishers** and **Trusted Root Certification Authorities** stores are populated — on a healthy system they contain hundreds of entries.
3. If you previously disabled driver signature enforcement (via bcdedit or the startup menu), re-enable it: `bcdedit /set testsigning off` in an elevated terminal, then restart.
4. Reinstall the signed OEM driver one final time. If code 52 survives all of this, escalate to your laptop maker's support — and if [video features flicker or misbehave](/articles/studio-effects-flickering-video-fix/) alongside it, mention that too, since both can trace to the same broken driver package.

## Closing

Code 52 looks like Windows being stubborn, but it is Windows protecting you from untrusted kernel code. Don't disable the protection — replace the driver with one that passes it. Get the package from your laptop maker or the chip vendor, purge unsigned leftovers from the Driver Store, and check the system clock. A properly signed driver loads silently, the warning disappears, and your NPU gets back to work with the security boundary intact.
