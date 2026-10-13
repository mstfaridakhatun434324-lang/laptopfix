---
title: "Driver IRQL Not Less or Equal on a Lenovo Laptop: How to Fix It"
slug: how-to-fix-driver-irql-not-less-or-equal-on-lenovo-laptop
date: 2026-09-26
categories: ["windows-errors"]
tags: ["windows 11", "lenovo", "irql not less or equal"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL on your Lenovo laptop? A driver touched memory at the wrong privilege level — here is how to identify and fix it fast."
thumbnail: "/images/thumbs/how-to-fix-driver-irql-not-less-or-equal-on-lenovo-laptop.webp"
faqs:
  - q: "What does IRQL actually mean?"
    a: "Interrupt Request Level — the processor's priority scheme for handling interrupts. Code running at high IRQL (dispatch level and above) cannot wait, so it is forbidden from touching pageable memory (which might require waiting for a disk read). A driver that breaks this rule gets the system crashed immediately, because continuing would corrupt memory management."
  - q: "Why is it always my Wi-Fi driver?"
    a: "Not always, but often on laptops: wireless drivers do complex work at high IRQL (managing radio interrupts, power states, roaming), giving them many opportunities to mishandle memory. Intel's wireless drivers have had several well-documented IRQL bug eras. The good news is they also get fixed quickly — updating usually resolves it."
  - q: "Can I just disable the device that's crashing?"
    a: "As a temporary workaround, yes — disabling the Wi-Fi adapter in Device Manager stops its driver loading, which stops the crashes and confirms the diagnosis. But it is not a fix; update or replace the driver so you get your hardware back. Use the disabled period for diagnosis, not as a lifestyle."
  - q: "Does this crash damage my files?"
    a: "The crash itself does not corrupt user files — Windows bug-checks precisely to prevent memory corruption from spreading. However, anything unsaved in open applications is lost, and repeated crashes during disk writes theoretically risk file-system inconsistency (which chkdsk repairs). Save often while diagnosing."
---

DRIVER_IRQL_NOT_LESS_OR_EQUAL is the most common driver-caused blue screen in Windows, and its name is more informative than it looks. IRQL is the processor's interrupt request level — a priority scheme. The crash means a driver tried to access pageable memory while running at too high a priority (dispatch level or above), where page faults are illegal. Windows stops the system rather than allow the illegal access.

On Lenovo laptops, network drivers are the classic offenders (the Wi-Fi driver misbehaving at high IRQL), followed by graphics and storage drivers. The dump file almost always names the guilty driver, which makes this one of the most diagnosable blue screens — if you read the dump instead of guessing.

## Why this happens

- **A buggy network driver:** Intel and Realtek Wi-Fi drivers are the single most common cause on Lenovo laptops — high-IRQL mishandling in the wireless stack.
- **Graphics driver bugs:** GPU drivers operating at dispatch level with bad memory references, common after driver updates on Legion and IdeaPad Gaming models.
- **Corrupted driver binaries:** a damaged driver file misbehaves in ways the intact version never would.
- **Conflicting drivers:** two drivers (often old VPN or virtualization network filters plus the Wi-Fi driver) interfering at high IRQL.
- **Faulty RAM:** memory errors can make a correct driver read garbage addresses, producing this crash with no driver actually at fault.
- **Overclocking or unstable power:** marginal hardware causing the CPU to mishandle interrupt levels under load.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Read the dump and name the driver

Do this first — it turns a generic troubleshooting session into a targeted one-driver fix.

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open the newest `.dmp` in `C:\Windows\Minidump`, run `!analyze -v`.
3. The **IMAGE_NAME** line is your answer 90% of the time — `Netwtw10.sys`/`Netwtw12.sys` (Intel Wi-Fi), `rtwlanu.sys` (Realtek), `nvlddmkm.sys` (NVIDIA).
4. Note the driver version too — you will compare it against the fixed version later.
5. If every dump names a different driver, suspect RAM (Fix 6) rather than any single driver.

### Fix 2: Update the Wi-Fi/network driver first

Because network drivers cause this crash most often on Lenovos, start there even before the dump if you want — but the dump should confirm.

1. Open **Device Manager > Network adapters**, right-click your Wi-Fi adapter, **Properties** — note the driver date and version.
2. Run **Lenovo Vantage** and install its network driver update; Lenovo validates these against your exact model.
3. Or get it direct: [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel wireless, or Lenovo Support for Realtek/MediaTek variants.
4. In the adapter's **Properties > Advanced tab**, note any non-default settings (roaming aggressiveness, preferred band) — reset them to defaults while diagnosing.
5. Restart and use Wi-Fi heavily (large downloads, video calls) — network-driver IRQL crashes surface under network load.

### Fix 3: Roll back if the crash followed an update

When the crashes have a clear start date matching a driver update, undo that update.

1. In **Device Manager**, open the suspect device's **Properties > Driver tab** and click **Roll Back Driver**.
2. If greyed out, **Uninstall device** with **Delete the driver software for this device** ticked, then reboot — Windows installs its inbox driver.
3. Block the bad version from returning: use Microsoft's show/hide updates troubleshooter to hide that driver update.
4. For Lenovo Vantage-pushed drivers, Vantage history shows the version — note it so you recognize the bad one.
5. Report the bad driver to Lenovo or the chip vendor; regressions get fixed when reported with dump files attached.

### Fix 4: Remove conflicting network filter drivers

VPNs, virtualization, and some firewalls install filter drivers that share the network stack at high IRQL — a classic conflict source.

1. Open **Settings > Apps > Installed apps** and look for VPN clients, virtual machine software, or third-party firewalls installed around when crashes began.
2. Uninstall the most recent one first, reboot, and test for a few days.
3. In **Device Manager > View > Show hidden devices**, check **Network adapters** for greyed-out ghost adapters from old VPNs — uninstall those too.
4. If you need the VPN, reinstall its latest version after confirming stability — vendors fix filter-driver IRQL bugs regularly.
5. Never stack two VPN clients or two third-party firewalls; their filters conflict by design at high IRQL.

### Fix 5: Update graphics and chipset drivers

The second tier of suspects. Cover them once the network stack is clean.

1. Update the GPU driver: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx) for GeForce (Legion), [AMD drivers](https://www.amd.com/en/support/download/drivers.html) for Radeon, or Intel integrated graphics via the detection tool linked in Fix 2.
2. Update the chipset driver from Lenovo Support for your exact model.
3. Check **Optional updates** under Windows Update for anything driver-related you missed.
4. Restart and test the crash scenario — gaming for GPU suspects, heavy multitasking for chipset.
5. One driver category at a time, with testing between — changing everything at once teaches you nothing about which one was guilty.

### Fix 6: Test the RAM

For dumps with inconsistent culprits or crashes surviving driver fixes, test the memory.

1. **Win + R**, `mdsched.exe`, **Restart now and check for problems** for the quick screen.
2. **MemTest86** from USB, 2+ passes, for the definitive answer.
3. Reseat/replace faulty modules; soldered-RAM errors go to Lenovo Support as a warranty claim with screenshots.
4. Also run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` — corrupted system files can mimic driver IRQL faults.
5. The [memory management stop code guide](/articles/how-to-fix-stop-code-memory-management-in-windows-11-24h2/) covers RAM diagnosis in more depth if this path confirms hardware.

### Fix 7: Clean boot and clean install

The final escalation ladder: isolate software, then eliminate it entirely.

1. Clean boot (`msconfig`, hide Microsoft services, disable all, disable startup apps) — stable here means a third-party driver or service; binary-search to find it.
2. If clean boot still crashes, the cause is a core driver or hardware — update BIOS from Lenovo Support (firmware fixes IRQL-handling errata).
3. Last resort: clean-install Windows from Microsoft's Windows 11 download page, install Lenovo drivers first, test before adding software.
4. Still crashing on clean Windows with stock drivers? Hardware — usually RAM or motherboard — needs professional diagnosis.
5. Bring your dump files and MemTest86 results to the shop; they compress hours of diagnosis into minutes. Safe Mode techniques in [this guide](/articles/how-to-boot-windows-11-in-safe-mode/) help with any minimal-environment testing.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is Windows at its most helpful: it crashes, and the dump file tells you exactly which driver did it. Read the dump, fix that driver, and resist the urge to shotgun-update everything at once. On Lenovo laptops the answer is the Wi-Fi driver often enough that checking it first is just good triage — but let the dump confirm before you commit.
