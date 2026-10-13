---
title: "How to Fix Windows Update Error 0x80070490 Step by Step"
slug: how-to-fix-windows-update-error-0x80070490-step-by-step
date: 2026-09-27
categories: ["windows-update"]
tags: ["windows update", "0x80070490", "update error", "windows 11"]
description: "Error 0x80070490 means Windows Update couldn't find an expected element. Follow this step-by-step guide — troubleshoot, repair the component store, and reset update components."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-step-by-step.webp"
faqs:
  - q: "What causes Windows Update error 0x80070490?"
    a: "The code means ERROR_NOT_FOUND: an update package, file, or registry element that Windows expected was missing. Typical triggers are a driver update that failed halfway, corruption in the component store, a corrupted SoftwareDistribution cache, or an interrupted feature update. The error rarely indicates bad hardware; it is a bookkeeping failure inside the update system that the step-by-step repairs below can resolve."
  - q: "Is 0x80070490 a virus or malware symptom?"
    a: "No. This is a standard Windows Update failure code, not an infection indicator. Malware can theoretically damage update components, but 0x80070490 appears overwhelmingly on healthy systems because of failed drivers or corrupted update metadata. If your antivirus reports the system clean, treat this purely as an update-repair task rather than a security incident."
  - q: "How long does the DISM repair take?"
    a: "Typically fifteen to forty-five minutes on a modern laptop with an SSD, depending on the extent of corruption and your internet speed, since DISM downloads clean files. Let it reach one hundred percent without closing the window or putting the laptop to sleep. Interrupting DISM can leave the component store in a worse state than when you started."
  - q: "Should I use a registry cleaner to fix this error?"
    a: "No — avoid registry cleaners entirely. They cannot fix 0x80070490 and frequently create new problems by deleting keys Windows needs. The error is about missing update elements, not general registry clutter. Stick to the official tools: the troubleshooter, SFC, DISM, and a component reset, all of which are designed for exactly this failure."
---

Error 0x80070490 shows up with the cryptic label "element not found," which is honest but unhelpful. Somewhere in the installation chain, Windows Update reached for a package, file, or registry entry that was supposed to be there and found nothing. Updates then refuse to proceed, and retrying the same check produces the same code every time.

This is a bookkeeping failure, not hardware damage, and it follows a predictable pattern: a driver update stalls halfway, the component store loses track of a file, or the download cache records a package that never fully arrived. The repair sequence below goes from the lightest touch — the built-in troubleshooter — to the heavier artillery of DISM and a component reset, in the order that wastes the least of your time.

One practical note before you start: work the fixes in order and test the update after each one. These repairs build on each other — the troubleshooter clears bad metadata, SFC fixes system files, DISM rebuilds the store those files come from — so skipping ahead can leave you repairing a layer whose foundation is still broken. Each fix takes only a few minutes except DISM, and none of them touches your personal files.

## Why this happens

- **A driver update failed midway.** The update registers as pending but its payload is gone, so every later operation hits a missing element.
- **Component store corruption.** The WinSxS store's manifests reference files that were damaged or deleted, and installers trust those manifests.
- **Corrupted SoftwareDistribution cache.** Partial downloads or stale metadata tell Windows a package exists when it doesn't.
- **An interrupted feature update.** A power cut or forced reboot during a version upgrade strands package elements in an indeterminate state.
- **Third-party driver tools.** External updaters that install drivers outside the Windows Update pipeline leave inconsistent metadata behind.
- **Antivirus quarantining update files.** Overzealous security software occasionally flags and removes files the updater needs.
- **Disk errors silently dropping files.** Bad sectors or a failing SSD can remove files the component store still lists.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pin down the failing update

Knowing exactly which package fails keeps you from repairing the wrong thing.

1. Go to **Settings > Windows Update > Update history** and find the 0x80070490 entry; write down the KB number and type (driver, quality update, or feature update).
2. Note whether the same update fails every time or different ones fail — a single repeating package points at that package; rotating failures point at the store itself.
3. If it is a driver, open **Device Manager** and verify the device works; a working device means the problem is update metadata, not the driver.

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter resets the exact metadata this error complains about.

1. Open **Settings > System > Troubleshoot > Other troubleshooters** and click **Run** next to **Windows Update**.
2. Accept every recommended fix it offers — it commonly repairs the service registration and clears bad pending entries.
3. Restart the laptop and check for updates. For pure metadata damage, this is often the whole fix.

### Fix 3: Repair system files with SFC

If the troubleshooter doesn't clear it, check the protected system files next.

1. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` and wait for it to reach 100 percent — don't use the laptop heavily during the scan.
3. If SFC says it found and repaired corruption, restart and retry the update.
4. If SFC reports it could not fix everything, don't repeat it endlessly — move to DISM in the next fix, which repairs the source SFC draws from.

### Fix 4: Repair the component store with DISM

DISM rebuilds the store that SFC and the updater both depend on.

1. In the same elevated Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Let it complete — it downloads clean component copies from Windows Update, so keep the laptop awake and online.
3. When it finishes, run `sfc /scannow` again to confirm the system files are now intact.
4. Retry **Settings > Windows Update > Check for updates**. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) has more on these repair tools if you want background reading.

### Fix 5: Reset the Windows Update components

A healthy store with a poisoned cache still fails, so clear the cache folders.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, `net stop msiserver`.
2. Rename the cache: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`, `net start msiserver`.
4. Check for updates again; Windows rebuilds the cache from scratch and the phantom entry vanishes.

### Fix 6: Install the package manually or hide it

For one stubborn package, sidestep the broken automatic chain.

1. Find the KB number from Fix 1 on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the x64 `.msu`.
2. Run the standalone installer — it often succeeds where the automatic path fails because it doesn't depend on the corrupted cache.
3. If it's a driver that already works fine, use Microsoft's "show or hide updates" troubleshooter to hide that driver update so Windows stops retrying it, then get the driver from the laptop maker's site instead.

### Fix 7: Perform an in-place upgrade as the final repair

When every targeted repair leaves the error in place, reinstall Windows over itself while keeping everything.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and double-click it to mount.
2. Run `setup.exe` from the mounted drive, accept the license terms, and on the "Choose what to keep" screen select **Keep personal files and apps**.
3. Let setup complete — it takes 30 to 90 minutes with several restarts; keep the laptop plugged in and don't interrupt it.
4. After signing in, run **Settings > Windows Update > Check for updates**; the rebuilt component store and fresh metadata clear the missing-element failure.

## Closing

Error 0x80070490 is almost always missing update bookkeeping rather than broken hardware, and the troubleshooter-to-DISM sequence above clears the great majority of cases. On HP hardware, where driver-channel conflicts are common, prefer the HP-specific [0x80070490 guide for HP laptops](/articles/how-to-fix-windows-update-error-0x80070490-on-hp-laptop/), and if your update failure shows a different code — like the service-disabled [0x80070422](/articles/how-to-fix-windows-update-error-0x80070422-step-by-step/) — work from that code's own guide instead of repeating these steps.
