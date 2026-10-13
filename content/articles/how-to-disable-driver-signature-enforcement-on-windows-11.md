---
title: "How to Disable Driver Signature Enforcement on Windows 11"
slug: how-to-disable-driver-signature-enforcement-on-windows-11
date: 2026-10-02
categories: ["windows-errors"]
tags: ["windows 11", "driver signature", "drivers"]
description: "Need an unsigned driver on Windows 11? Learn the safe temporary and persistent ways to disable driver signature enforcement — and when not to."
thumbnail: "/images/thumbs/how-to-disable-driver-signature-enforcement-on-windows-11.webp"
faqs:
  - q: "Does Windows 11 handle this differently from Windows 10?"
    a: "The core methods are the same (Startup Settings F7, bcdedit testsigning), but Windows 11 adds wrinkles: stricter Secure Boot defaults, virtualization-based security and Memory Integrity on more machines, and tighter Smart App Control integration. The one-boot Startup Settings method sidesteps all of these, which is why it is the recommended path on Windows 11 specifically."
  - q: "Will my unsigned driver survive Windows updates?"
    a: "Usually yes for cumulative updates, sometimes no for feature updates — a new Windows build can invalidate the driver registration or re-tighten enforcement paths. If the device breaks after a feature update, repeat the one-boot bypass and reinstall. Keeping the driver installer on hand turns this into a five-minute job."
  - q: "Is test mode detectable by games and apps?"
    a: "Yes — anti-cheat systems commonly detect test signing mode and refuse to run, and some enterprise software checks for it. This is by design: test mode weakens driver trust, and competitive games do not accept that. Disable test mode (bcdedit /set testsigning off, reboot) before gaming."
  - q: "Can I disable it permanently without the watermark?"
    a: "The methods that persist (testsigning, nointegritychecks) show the watermark or otherwise signal their state deliberately — Microsoft does not offer a silent permanent bypass, because silent bypasses are what malware wants. Anyone selling you a silent permanent method is selling you a security hole. Use the one-boot method per install instead."
---

Windows 11 requires drivers to carry a valid digital signature before it will load them. This enforcement blocks entire categories of malware — rootkits live or die by their ability to load unsigned kernel drivers — but it also stands in the way of legitimate unsigned drivers: aging hardware abandoned by its vendor, drivers you compiled yourself, and niche professional equipment.

Windows 11 gives you several ways past enforcement, and they differ in duration, reversibility, and interaction with Secure Boot and virtualization-based security. This guide lays them out from the safest one-boot bypass to the persistent options, with clear guidance on which fits your situation. The ground rule never changes: only install drivers you trust, from sources you trust.

## Why this happens

- **Legacy hardware with no signed driver:** older printers, scanners, audio interfaces, and lab gear whose vendors never produced a signed Windows 11 driver.
- **Driver development and testing:** developers iterating on a driver need to load unsigned builds dozens of times a day.
- **Small-vendor drivers:** niche manufacturers who never completed Microsoft's Hardware Developer Program signing process.
- **The symptom is error 52:** Device Manager shows Windows cannot verify the digital signature for this device — the classic enforcement block.
- **Virtualization-based security complicates things:** on Windows 11, VBS features like Memory Integrity add layers beyond basic signature enforcement that some bypasses do not affect.
- **Temporary need, permanent temptation:** most people need enforcement off for one install; understanding the methods prevents leaving the system exposed indefinitely.

## How to fix it

Work through these in order, from the quickest checks to the deeper repairs. Most people are back up and running by Fix 4 or 5.

### Fix 1: Use Startup Settings for a one-boot bypass

The recommended method for almost everyone: enforcement off for a single boot, automatically restored after. Ideal for installing one unsigned driver.

1. Open **Settings > System > Recovery**. Next to **Advanced startup**, click **Restart now**.
2. At the blue menu: **Troubleshoot > Advanced options > Startup Settings > Restart**.
3. When the numbered menu appears, press **7** (or **F7**) for **Disable driver signature enforcement**.
4. Install your unsigned driver during this session — Device Manager and vendor installers will accept it.
5. Restart normally when done. Enforcement is automatically back on; the installed driver continues to work.
6. This method works with Secure Boot enabled and is unaffected by most VBS settings — it is the path of least resistance.

### Fix 2: Use the advanced startup command sequence

The same one-boot bypass reached via command line — useful when Settings is awkward or for remote guidance.

1. Open an elevated Terminal and run `shutdown /r /o /f /t 00` — the PC restarts directly into the blue recovery menu.
2. Navigate **Troubleshoot > Advanced options > Startup Settings > Restart** as in Fix 1.
3. Press **7**/**F7** at the menu.
4. Install the driver, then restart normally.
5. Bookmark this command — it is the fastest way to reach Startup Settings on Windows 11, useful beyond just driver work.

### Fix 3: Enable test signing mode (persistent, for developers)

For repeated unsigned-driver loading: test mode persists across reboots with a visible watermark reminder.

1. Open **Terminal (Admin)** and run `bcdedit /set testsigning on`.
2. Restart — a **Test Mode** watermark appears on the desktop confirming the state.
3. Install and iterate on unsigned drivers freely across reboots.
4. When finished: `bcdedit /set testsigning off` from the elevated prompt, restart, watermark gone.
5. Caveats: some anti-cheat software refuses to run in test mode, and on systems with Secure Boot plus VBS, testsigning may be blocked — Fix 1 remains the fallback.

### Fix 4: Disable Memory Integrity if it blocks your driver

Windows 11's Memory Integrity (HVCI) can block drivers that pass signature enforcement but use incompatible techniques. Know the distinction.

1. Go to **Settings > Privacy & security > Windows Security > Device security > Core isolation**.
2. If **Memory integrity** is on and your (signed or unsigned) driver fails to load, try toggling it off temporarily for the install, then reassess.
3. Check **Windows Security > Device security** for the incompatible driver list — Windows 11 names drivers HVCI blocks.
4. Weigh this carefully: Memory Integrity is a meaningful protection. Disabling it permanently for one old device is a poor trade — consider whether the device is worth it.
5. Re-enable Memory Integrity after testing unless you have a specific, accepted reason not to.

### Fix 5: Install the driver properly during the bypass window

The bypass only opens the door; correct installation walks through it.

1. During the enforcement-off session, open **Device Manager**, right-click the device, **Update driver > Browse my computer for drivers**, and point at the `.inf`.
2. At the unsigned-driver warning, choose **Install this driver software anyway**.
3. Verify the device reports **This device is working properly** with no warning icon.
4. For vendor `.exe` installers, run as administrator during the bypass session.
5. Reboot normally and re-verify — a correctly installed driver keeps working with enforcement re-enabled. If it breaks on normal boot, the install did not complete properly; repeat the bypass and reinstall.

### Fix 6: Verify enforcement is back on

Close the loop. Confirm the protection is restored, especially after the bcdedit methods.

1. Restart normally into regular Windows.
2. Confirm no Test Mode watermark on the desktop.
3. In an elevated prompt, run `bcdedit` and check `testsigning` reads **No** (or is absent).
4. Check **Windows Security > Device security > Core isolation** that Memory Integrity is back to your chosen state.
5. Confirm the device still functions. The round trip is complete: driver installed, protections restored.

### Fix 7: Find signed alternatives before bypassing

The best bypass is the one you do not need. Check these sources for signed drivers first.

1. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) for the device's hardware ID — Microsoft hosts signed drivers for thousands of legacy devices.
2. Check **Settings > Windows Update > Advanced options > Optional updates** — signed vendor drivers appear here regularly.
3. Look for community-maintained signed drivers for popular legacy hardware (some enthusiast communities pay for signing).
4. For developers: consider attestation signing through the Hardware Developer Program — it is the legitimate path to distributable signed drivers.
5. Only when no signed driver exists anywhere does the bypass become the right answer — and then Fix 1's one-boot method keeps the exposure minimal. If driver experiments lead to crashes, the [Driver Verifier violation guide](/articles/how-to-fix-driver-verifier-detected-violation-step-by-step/) and the [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) will get you out.

## Closing

Driver signature enforcement on Windows 11 is a security boundary worth respecting — and Windows gives you respectful ways across it when you have legitimate business there. The one-boot Startup Settings bypass handles nearly every real scenario: install the unsigned driver, reboot, protections restored. Save the persistent modes for actual driver development, verify you came back each time, and look for signed alternatives before reaching for any bypass at all.
