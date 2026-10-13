---
title: "Fix Windows Update Error 0x80070490 on Windows 11: Element Not Found"
slug: how-to-fix-windows-update-error-0x80070490-on-windows-11
date: 2026-09-01
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x80070490", "element not found", "component store"]
description: "Error 0x80070490 ('element not found') on Windows 11 signals component store damage. Repair it with DISM, reset the cache, and get updates working."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-on-windows-11.webp"
faqs:
  - q: "What does error 0x80070490 mean?"
    a: "It means 'element not found' — the update engine looked for a component, manifest, or package in the component store and it was not there. This is a classic sign of WinSxS corruption, where the store's index disagrees with its actual contents."
  - q: "Is 0x80070490 related to drivers?"
    a: "Often, yes. It frequently appears when a driver update's package references components missing from the store, or when the driver store itself is corrupted. That is why the error sometimes names a driver update specifically while cumulative updates install fine."
  - q: "Will DISM fix 0x80070490?"
    a: "In most cases, yes. DISM's RestoreHealth operation is specifically designed to repair the component store, which is exactly what this error complains about. Run it before anything more drastic — it resolves the majority of 0x80070490 cases, especially when followed by SFC to repair system files from the fixed store."
  - q: "What if DISM fails with 0x80070490 too?"
    a: "Then the store is damaged beyond what online repair can fix. The next steps are an offline DISM repair from recovery media, or an in-place upgrade repair install, which replaces the entire component store while keeping your files and apps."
---

Error 0x80070490 — "element not found" — is Windows Update telling you that its parts catalog is lying. The update engine consulted the component store (WinSxS), expected to find a particular component, manifest, or package, and found an empty shelf. On Windows 11 this error shows up for cumulative updates, feature updates, and especially driver updates, and it points squarely at component store corruption rather than network or cache trivia.

The good news is that the component store has a dedicated repair tool: DISM. The bad news is that when DISM itself struggles, you need heavier measures. This guide is ordered accordingly — quick checks, cache reset, DISM/SFC, driver-store repair, and finally the repair install. Note which updates fail: if only driver updates fail with 0x80070490, jump to the driver-store fix first.

## Why this happens

- **Corrupted component store (WinSxS):** The store's index references components that are missing or damaged — the textbook cause of "element not found."
- **Damaged driver store:** Corrupted driver packages in the DriverStore produce the same error specifically for driver updates.
- **Interrupted update leaving partial components:** A failed install can leave half-registered components that the store index references but cannot deliver.
- **Corrupted update manifests:** Damaged manifest files in the cache describe components with wrong identities, so lookups fail.
- **Registry damage in servicing keys:** Corrupted servicing registry entries misdirect component lookups.
- **Disk corruption under WinSxS:** Bad sectors in the component store's files create genuine missing elements.
- **Third-party "cleaner" tools:** Aggressive system cleaners that delete "unused" WinSxS files destroy components Windows still needs.
- **Failed servicing stack update:** A broken SSU leaves the servicing machinery unable to resolve component identities correctly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Windows Update troubleshooter

A quick automated pass that fixes common servicing registrations.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and apply all fixes.
3. Restart and check for updates.

### Fix 2: Reset the update cache

Clear corrupted manifests and partial packages before repairing the store itself.

1. Open **Terminal (Admin)**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart and retry the update.

### Fix 3: Repair the component store with DISM

This is the primary fix for 0x80070490. DISM compares the store against known-good sources and repairs discrepancies.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Wait for completion — 15 to 30 minutes is normal. Do not interrupt it.
3. If it reports the corruption was repaired, restart and check for updates immediately.
4. If DISM itself errors out, note its error code — you will need it for Fix 6.

### Fix 4: Run SFC to repair protected system files

After DISM fixes the store, SFC uses the repaired store to fix system files.

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Let verification reach 100% and report its result.
3. If it found and fixed corruption, restart and retry the update.
4. The DISM-then-SFC sequence also clears [0x80070057 parameter errors](/articles/how-to-fix-windows-update-error-0x80070057-on-windows-11/), which often accompany store corruption.

### Fix 5: Clean the driver store (for driver-update failures)

If 0x80070490 appears specifically on driver updates, the driver store — not WinSxS — is the damaged element.

1. In **Terminal (Admin)**, run `pnputil /enum-drivers` and look for packages related to the failing device.
2. Remove suspicious ones: `pnputil /delete-driver oemXX.inf /uninstall`.
3. In **Device Manager**, uninstall the device with driver removal ticked, then restart.
4. Install the fresh driver from your manufacturer's support site (Dell, HP, or [Lenovo](https://support.lenovo.com/us/en/)) and retry Windows Update.

### Fix 6: Run DISM offline from the recovery environment

When online DISM cannot repair the store, run it against the offline installation where nothing is locked.

1. Boot into WinRE (interrupt boot three times at the logo, then **Troubleshoot > Advanced options > Command Prompt**).
2. Identify your Windows drive letter (`dir C:` — adjust if needed).
3. Run `DISM /Image:C:\ /Cleanup-Image /RestoreHealth`.
4. Follow with `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.
5. Exit, boot normally, and check for updates.

### Fix 7: Perform an in-place upgrade repair install

The final backstop: reinstall Windows 11 over itself, replacing the entire component store while keeping files and apps. Download the installer from the [official Windows 11 page](https://www.microsoft.com/en-us/software-download/windows11), run setup, choose **Keep personal files and apps**, and allow 30–60 minutes. Afterward, the component store is factory-fresh and 0x80070490 is gone. Review the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) for post-repair update best practices.

A specific warning for this error: aggressive system-cleaner tools. Utilities that promise to reclaim gigabytes by purging unnecessary Windows files sometimes target the WinSxS component store or the servicing metadata — the exact structures 0x80070490 complains about. The space they free is rarely worth the servicing damage they cause, and Windows 11's built-in Disk Cleanup with the Windows Update Cleanup option achieves most of the same savings safely. If you ran such a tool shortly before this error appeared, that is very likely your cause, and DISM is the repair. For the Windows 10 version of this error, see our [Windows 10 0x80070490 guide](/articles/how-to-fix-windows-update-error-0x80070490-on-windows-10/). Going forward, treat the component store as load-bearing: it is.

## Closing

Error 0x80070490 is the component store crying for help, and DISM is the answer it is crying for. Run the troubleshooter and cache reset first, then DISM followed by SFC — that sequence resolves the large majority of cases. Reserve the driver-store cleanup for driver-specific failures and the offline DISM or repair install for the stubborn remainder. Once the store's index matches reality again, "element not found" stops appearing because every element is finally where it should be.
