---
title: "Best Way to Fix the REFERENCE_BY_POINTER Blue Screen"
slug: best-way-to-fix-reference-by-pointer-bsod
date: 2026-09-21
categories: ["windows-errors"]
tags: ["bsod", "reference-by-pointer", "driver-fix"]
description: "Stop the REFERENCE_BY_POINTER blue screen for good with the driver cleanup and memory checks that fix it in most cases."
thumbnail: "/images/thumbs/best-way-to-fix-reference-by-pointer-bsod.webp"
faqs:
  - q: "What causes REFERENCE_BY_POINTER?"
    a: "It happens when a driver decrements an object's reference count incorrectly, usually after the object was already freed. Outdated or buggy third-party drivers — especially antivirus, virtual drive, and old hardware drivers — are the most common cause, followed by corrupted system files and faulty RAM."
  - q: "Is REFERENCE_BY_POINTER a hardware problem?"
    a: "Usually not, but it can be. Start with drivers and system files, since those fix the majority of cases. If crashes persist after a clean driver reinstall and file repairs, test the RAM and hard drive, because bad memory can produce the same reference-count corruption."
  - q: "Can I fix REFERENCE_BY_POINTER without reinstalling Windows?"
    a: "Yes, in most cases. Updating or removing the offending driver, running SFC and DISM, and testing memory resolves it without a reinstall. A Windows reset is only the last resort when the faulty component can't be identified."
  - q: "Does Driver Verifier help find the cause?"
    a: "Yes. Driver Verifier stresses drivers and forces the faulty one to crash the system immediately instead of corrupting memory silently, which makes the minidump point straight at the culprit. Use it carefully — only verify non-Microsoft drivers, and turn it off after diagnosing."
---
# Best Way to Fix the REFERENCE_BY_POINTER Blue Screen

**REFERENCE_BY_POINTER** is one of those blue screens that gives you almost nothing to work with — no helpful filename, just a stop code. In practice, though, it's a driver bug nearly every time: some driver fumbled a reference count on a system object, and Windows crashed rather than let the corruption spread.

The best approach is methodical driver cleanup, not guesswork. Follow the order below; the first two fixes resolve the majority of cases. If crashes persist across driver changes, our [blue screen of death fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers deeper system-level causes.

## Why this happens

- **Buggy third-party drivers:** Antivirus filter drivers, virtual CD/DVD tools, and old printer or USB drivers are classic offenders.
- **Outdated chipset or storage drivers:** These manage objects the kernel references constantly, so a counting bug surfaces fast.
- **Corrupted system files:** A damaged kernel or driver framework file can mishandle references that healthy code handles fine.
- **Faulty RAM:** Bad memory cells corrupt the reference counts stored in them, producing crashes that look exactly like driver bugs.
- **Conflicting security software:** Two antivirus products (or one plus Windows Defender's real-time protection fighting it) install competing filter drivers.
- **Bad Windows update:** Occasionally a cumulative update ships with a regression in a Microsoft driver that triggers this on specific hardware.

## How to fix it

Work through these in order. The best fix is the one that identifies and removes the bad driver — everything after that is verification and cleanup.

### Fix 1: Remove recently added or updated drivers

Since this stop code almost always follows a driver change, undoing that change is the fastest win.

1. Press **Win + X** and open **Device Manager**.
2. Click **View > Show hidden devices** so uninstalled-but-present drivers appear.
3. Look for devices with yellow warnings, then think back: did you install a printer, VPN, antivirus, virtual drive tool, or USB gadget right before crashes started?
4. Right-click the suspect device and choose **Uninstall device**, ticking **Attempt to remove the driver for this device** if offered.
5. Restart. If the crashes stop, you've found it — reinstall only the latest driver from the manufacturer's site, never from a driver-updater app.

### Fix 2: Update every core driver from the manufacturer

When no single culprit is obvious, refresh the whole driver stack with known-good versions.

1. Update the **chipset** driver first (Intel, AMD, or your laptop maker), then **storage controllers** (SATA/NVMe), then **network** adapters.
2. Get them from your laptop manufacturer's support page or the component maker's site — [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html) detects what's outdated automatically.
3. Avoid "driver updater" utilities; they frequently install wrong or unsigned drivers that cause exactly this class of crash.
4. Reboot after each major driver install and use the laptop normally for a while before moving on.

### Fix 3: Run SFC and DISM to repair system files

If a Windows component is damaged, no driver update will help until the underlying files are healthy.

1. Open **Terminal (Admin)** from the **Win + X** menu.
2. Run `sfc /scannow` and let it complete.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and run `sfc /scannow` once more to confirm everything is clean.
5. Microsoft documents both tools in detail on the [Windows support hub](https://support.microsoft.com/en-us/windows) if you want the full reference.

### Fix 4: Use Driver Verifier to catch the culprit

When the crashes are random and no driver stands out, Driver Verifier forces the guilty driver to reveal itself.

1. Press **Win + R**, type `verifier.exe`, and press **Enter**.
2. Choose **Create custom settings**, enable all checks except **Low Resource Simulation**, then select **Select driver names from a list**.
3. Tick every **non-Microsoft** driver and click **Finish**, then restart.
4. Use the laptop normally — Verifier will blue-screen deliberately when a driver misbehaves, and the dump will name it.
5. After identifying it, boot into Safe Mode, run `verifier /reset`, uninstall the bad driver, and reboot normally.
6. Never leave Verifier on permanently; it slows the system and can cause boot loops if a critical driver is buggy.

### Fix 5: Test the RAM

Bad memory corrupts reference counts just like a bad driver does, so rule it out before going further.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Let the full scan run; check results afterward in **Event Viewer > Windows Logs > System** for the MemoryDiagnostics-Results entry.
3. If errors appear, reseat the modules and retest, then test sticks individually to isolate the bad one.
4. Replace faulty RAM — this is a hardware failure no software tweak can fix. For related memory stop codes, see our guide to [fixing the Memory Management BSOD](/articles/memory-management-bsod-windows-11-fix/).

### Fix 6: Remove conflicting security software

Two security products fighting over the same file-system hooks is a well-known REFERENCE_BY_POINTER trigger.

1. Open **Settings > Apps > Installed apps** and look for more than one antivirus, firewall, or "system optimizer."
2. Uninstall all but one using the vendor's official removal tool (regular uninstall often leaves filter drivers behind).
3. Restart and confirm Windows Security is active as your baseline protection.
4. Test for a day or two before reinstalling any third-party security product — and only reinstall one.

### Fix 7: Reset Windows as a last resort

If the crash survives driver cleanup, file repair, and memory testing, a clean Windows install eliminates every software variable at once.

1. Back up your files to an external drive or cloud storage.
2. Go to **Settings > System > Recovery > Reset this PC**.
3. Choose **Remove everything** and **Cloud download** for the cleanest result.
4. After setup, install drivers one at a time from manufacturer sources and test between installs so a returning crash points straight at the last driver added.

## Closing

REFERENCE_BY_POINTER rewards patience more than anything: strip away recent driver changes, refresh the core driver stack from trusted sources, verify system files and RAM, and use Driver Verifier when you need a name for the culprit. Most people never need the reset at Fix 7 — the bad driver usually gives itself away by Fix 2.
