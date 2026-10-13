---
title: "DRIVER_VERIFIER_IOMANAGER_VIOLATION: A Complete Step-by-Step Fix"
slug: how-to-fix-driver-verifier-iomanager-violation-step-by-step
date: 2026-10-08
categories: ["windows-errors"]
tags: ["bsod", "driver verifier", "stop code", "drivers"]
description: "The complete step-by-step fix for DRIVER_VERIFIER_IOMANAGER_VIOLATION: disable Verifier, read the dump, and replace the bad driver."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-iomanager-violation-step-by-step.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_IOMANAGER_VIOLATION?"
    a: "It's a blue screen raised when Driver Verifier catches a driver making an illegal I/O request — the driver asked the I/O manager to do something against the rules. Verifier then deliberately crashes the system to expose the bug. The crash is intentional; the driver is the real problem."
  - q: "What's the very first thing I should do?"
    a: "Run verifier /reset from an elevated Command Prompt and reboot. That disables Driver Verifier and stops the deliberate crashes. Do this before anything else — there's no point diagnosing while Verifier keeps crashing the machine."
  - q: "How do I find which driver caused it?"
    a: "Open the latest crash dump in C:\\Windows\\Minidump. The dump names the driver Verifier caught — often a storage, network, or filter driver. Match that filename to a device or program, then update, roll back, or remove it."
  - q: "Can this error damage my SSD or files?"
    a: "The blue screen itself doesn't damage anything — it's a controlled stop. But if the underlying cause is a buggy storage driver, running it long-term isn't ideal. Fix the driver promptly, and your files and SSD will be fine."
---

`DRIVER_VERIFIER_IOMANAGER_VIOLATION` is a mouthful, but the situation is simple: Driver Verifier — Windows' built-in driver diagnostic — caught a driver breaking I/O rules and crashed your laptop on purpose to prove it. This guide walks you through the entire fix as a numbered sequence, no guesswork: stop Verifier, read the evidence, fix the driver, verify stability.

Follow the steps in order and don't skip the verification at the end. That's what separates a fix from a hope.

## Why this happens

- **Verifier left running after a diagnostic session**: Someone enabled Driver Verifier to investigate a driver issue and never turned it off. Now it converts every I/O rule violation into a blue screen, indefinitely.
- **Buggy storage or controller driver**: The "IOMANAGER" in the name points at the I/O path — NVMe drivers, Intel RST, AMD storage drivers, and USB controller drivers are the most common real culprits.
- **Filter drivers from security or encryption software**: Antivirus, disk encryption, and backup tools install drivers that intercept I/O requests. When they mishandle a request, Verifier flags the violation.
- **Driver corrupted by a bad update**: A partially installed driver update leaves inconsistent binaries that fail Verifier's checks on the next I/O operation.
- **Old driver under a new Windows build**: Feature updates change I/O manager behavior. A driver that was technically borderline before can start violating rules after the update.
- **Hardware instability surfacing as driver errors**: A failing SSD or flaky RAM can cause I/O operations to fail in ways the driver mishandles — Verifier blames the driver, but the hardware is the root cause.

## How to fix it

Work through these in order — each step builds on the last.

### Fix 1: Disable Driver Verifier

Stop the intentional crashes first.

1. Press **Win + S**, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Type exactly:

   ```cmd
   verifier /reset
   ```

3. Press Enter and restart your laptop.
4. Can't boot normally? Reach Safe Mode first: force-shutdown during boot three times to open **Automatic Repair**, then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, press **4**, and run the command there.

### Fix 2: Confirm Verifier is actually off

Don't assume — verify, because a crash loop can make you think the reset didn't take.

1. After rebooting, open an elevated **Command Prompt** again.
2. Run:

   ```cmd
   verifier /query
   ```

3. If it reports that no drivers are being verified, you're clear. If Verifier is somehow still active, run `verifier /reset` once more and reboot again.

### Fix 3: Read the crash dump to name the driver

Now collect the evidence Verifier left behind.

1. In **File Explorer**, go to `C:\Windows\Minidump` and find the newest `.dmp` file.
2. Analyze it using the walkthrough in [how to check minidump files on Windows 11](/articles/how-to-check-minidump-files-on-windows-11/).
3. Write down the driver filename from the crash analysis — for example `stornvme.sys`, `iaStorAVC.sys`, or a third-party name like `avgtpx64.sys`.
4. If the dump names a Windows inbox driver (like `stornvme.sys`), the real culprit is usually the hardware or firmware beneath it — skip to Fix 6 after updating drivers.

### Fix 4: Update the identified driver

Get the fixed version from the source.

1. Press **Win + X** and open **Device Manager**.
2. Find the device using that driver. Right-click it and choose **Update driver** > **Search automatically for drivers**.
3. If that finds nothing, download the driver manually: chipset and storage drivers from [Intel](https://www.intel.com/content/www/us/en/support/detect.html) or [AMD](https://www.amd.com/en/support/download/drivers.html), network drivers from the adapter vendor, or the full package from your laptop manufacturer's support site.
4. Restart after installing.

### Fix 5: Roll back if the driver just updated

A fresh driver version can be the thing Verifier is complaining about.

1. In **Device Manager**, right-click the device, open **Properties**, and go to the **Driver** tab.
2. Click **Roll Back Driver** if it's available, choose a reason, and restart.
3. If the option is grayed out, manually install the previous version from the vendor's driver archive.

### Fix 6: Remove filter-driver software

Antivirus, encryption, and backup tools live in the I/O path — prime Verifier targets.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall third-party antivirus, disk encryption, and backup utilities (Windows Defender and File History are fine to keep).
3. Use each vendor's official removal tool — standard uninstalls frequently leave the filter driver behind, which defeats the purpose.
4. Restart and test for a full day.

### Fix 7: Check the health of the drive and memory

If the driver looked innocent, test what it talks to.

1. In an elevated Command Prompt, run:

   ```cmd
   chkdsk C: /f /r
   ```

   Type **Y**, restart, and let the scan complete.

2. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
3. Check your SSD's health with the manufacturer's tool (Samsung Magician, Crucial Storage Executive, WD Dashboard) — look at wear level and available spare.
4. If hardware errors show up, see [what to do about faulty hardware corrupted page](/articles/what-to-do-if-faulty-hardware-corrupted-page/) for the next steps.

### Fix 8: Verify stability and keep Verifier off

Close the loop properly.

1. Use the laptop normally for two to three days, doing the things that used to crash it.
2. Confirm no new dumps appear in `C:\Windows\Minidump`.
3. Make a note of which driver was at fault and avoid "driver updater" apps that might reinstall the bad version.
4. Leave Verifier off. If you ever enable it again for diagnosis, set a reminder to run `verifier /reset` when you're done.

## Closing

The `DRIVER_VERIFIER_IOMANAGER_VIOLATION` sequence is always the same: reset Verifier, read the dump, fix the named driver, verify. Follow it in order and the crashes end — no reinstallation, no data loss. For the HP-specific version of this error, see [how to fix it on HP laptops](/articles/how-to-fix-driver-verifier-iomanager-violation-on-hp-laptop/), and for Verifier crashes in general read [how to fix unexpected store exception](/articles/how-do-i-fix-unexpected-store-exception/).
