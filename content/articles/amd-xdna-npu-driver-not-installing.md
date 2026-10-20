---
title: "How to Fix the AMD XDNA NPU Driver Not Installing"
slug: amd-xdna-npu-driver-not-installing
date: 2026-10-20
categories: ["ai-pc"]
tags: ["amd xdna", "npu driver", "driver not installing", "ryzen ai", "windows 11"]
description: "AMD XDNA NPU driver not installing on your Ryzen AI laptop? Find out what blocks the installer and apply reliable fixes to get it installed on Windows 11."
thumbnail: "/images/thumbs/amd-xdna-npu-driver-not-installing.webp"
faqs:
  - q: "Where do I download the AMD XDNA NPU driver?"
    a: "Start with your laptop maker's support page, which carries the build validated for your exact model. AMD's generic chipset driver package from amd.com is the second choice. Avoid random driver-download sites — mismatched XDNA packages are a leading cause of install failures."
  - q: "Why does the AMD installer say my system is not supported?"
    a: "That message usually means the installer cannot see a Ryzen AI processor, either because the NPU is disabled in BIOS or because an older chipset driver is hiding the hardware. Enable the NPU in BIOS and update the AMD chipset driver first, then retry."
  - q: "Can I install the XDNA driver without the full AMD Software suite?"
    a: "Yes. The chipset driver package includes the NPU driver, and you can install just the driver components. A minimal install is actually preferable for troubleshooting, since it removes the Adrenalin software as a variable."
  - q: "Does the XDNA driver need a specific Windows 11 version?"
    a: "Ryzen AI NPUs need Windows 11 23H2 or newer for full support, and some XDNA 2 features want 24H2. If the installer refuses on an older build, update Windows first — the driver genuinely depends on OS-level NPU plumbing."
---

You download the AMD XDNA NPU driver, run the installer, and it fails — an error dialog, a rollback, or the installer simply vanishing with nothing installed. Task Manager shows no NPU, Device Manager has no AMD IPU device, and every AI feature that should run on the neural processor falls back to the CPU or refuses to work. For a Ryzen AI laptop owner, a missing NPU driver turns an AI PC into an ordinary one.

The XDNA install path is fussier than a typical driver install because the NPU driver rides inside AMD's chipset package and depends on the system correctly reporting a Ryzen AI processor. If the chipset driver is old, the NPU is disabled in firmware, or a previous partial install left the driver store in a contradictory state, the installer aborts rather than risk installing onto hardware it cannot verify.

This guide covers the real reasons the AMD XDNA NPU driver refuses to install and the fixes that work, ordered from quickest to most thorough. If your NPU appears in Device Manager but apps ignore it, see [DirectML not using the NPU on Windows 11](/articles/directml-not-using-npu-windows-11/). If the hardware seems gone entirely after install attempts, start with [AMD Ryzen AI NPU not showing up](/articles/amd-ryzen-ai-npu-not-showing-up/).

## Why this happens

- **NPU disabled in BIOS/UEFI:** Many laptops ship with the NPU toggle off, and the installer refuses to proceed when it cannot detect Ryzen AI hardware.
- **Outdated AMD chipset driver:** The XDNA NPU driver is bundled with the chipset package; an old chipset install cannot enumerate the NPU device.
- **Windows build too old:** XDNA drivers depend on OS-level NPU support that only exists in recent Windows 11 builds.
- **Partial install remnants:** A previous failed attempt leaves a staged driver package that conflicts with the new one.
- **Wrong package for the platform:** XDNA and XDNA 2 (Ryzen AI 300 series) use different driver branches, and installing the wrong one fails the hardware check.
- **Security software blocking the installer:** Endpoint protection sometimes flags the installer's kernel-mode components and silently blocks them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the hardware is actually there

No installer can succeed if the system does not report a Ryzen AI processor. This two-minute check prevents chasing a software problem when the real issue is a firmware toggle or a non-AI SKU.

1. Open Task Manager, go to Performance, and look for an NPU entry in the sidebar.
2. Open Device Manager, expand System devices, and look for "AMD IPU Device" or similar neural processor entries.
3. If neither appears, restart into BIOS/UEFI and find the NPU or AI Engine toggle — enable it if it is off.
4. Save, boot back into Windows, and check Device Manager again before retrying any installer.

### Fix 2: Update Windows 11 to a supported build

XDNA drivers lean on NPU plumbing that Microsoft only added in recent Windows 11 releases. Installing a current XDNA driver on an old build fails the OS check, and no retrying will change that.

1. Open Settings, go to Windows Update, and install all pending updates.
2. Confirm your build under Settings, System, About — you want 23H2 or newer, ideally 24H2 for Ryzen AI 300 series.
3. If Windows Update itself is stuck, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) offers the enablement packages as a manual route.
4. After updating, restart and retry the XDNA driver installer before changing anything else.

### Fix 3: Install the correct AMD chipset driver package first

The NPU driver lives inside AMD's chipset driver package, so the chipset install is the foundation. An outdated chipset driver cannot enumerate the XDNA device, making the NPU installer conclude the hardware is absent.

1. Identify your exact processor (Ryzen AI 300 series uses XDNA 2; 8000 series uses first-gen XDNA).
2. Download the matching chipset driver package from [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html) or your laptop maker's support site.
3. Run the chipset installer, choosing the driver-only option if offered, and restart when prompted.
4. Check Device Manager for the AMD IPU Device appearing — if it does, the NPU installer will now proceed.

### Fix 4: Remove remnants of failed install attempts

Each failed install can leave a staged driver package behind, and the next attempt trips over it. Clearing the staging area gives the installer a clean slate without touching your working drivers.

1. Open an elevated Command Prompt and run `pnputil /enum-drivers` to list staged packages.
2. Look for AMD IPU or neural processor entries with old dates or duplicates.
3. Remove the stale ones with `pnputil /delete-driver oemXX.inf`, substituting the correct number.
4. Clear `%TEMP%` of AMD installer leftovers, restart, and run the installer once more.

### Fix 5: Temporarily disable security software during install

Kernel-mode driver installers are a favorite false positive for aggressive antivirus and endpoint tools. If the installer fails at the exact moment it should be loading drivers, with no useful error, a silent block is a strong suspect.

1. Temporarily disable real-time protection in Windows Security (Virus & threat protection settings).
2. If you run third-party antivirus or a corporate endpoint agent, pause it too — these are the more common culprits.
3. Run the XDNA installer immediately while protection is down, and do not browse or download anything in between.
4. Re-enable all protection the moment the install completes, then verify the AMD IPU Device in Device Manager.

### Fix 6: Install from your laptop maker's package in a clean boot

When the generic AMD package keeps failing, the OEM-validated build is the answer — laptop makers sometimes customize power and firmware interfaces the generic driver does not expect. A clean boot removes third-party interference at the same time. Note that a working driver is also what features like [Copilot Vision](/articles/copilot-vision-not-working-windows/) need before they can use the NPU at all.

1. Download the chipset/NPU driver package from your laptop maker's support page for your exact model.
2. Press Win + R, type `msconfig`, and on the Services tab hide Microsoft services, then disable the rest; on the Startup tab, open Task Manager and disable all startup items.
3. Restart into this clean-boot state and run the OEM installer.
4. After success, reopen `msconfig`, restore normal startup, and restart once more.

## Closing

An AMD XDNA NPU driver that will not install is almost always a prerequisite problem — the NPU disabled in BIOS, an old chipset driver hiding the hardware, or a Windows build that predates NPU support. Work the chain from hardware visibility upward and the driver lands, letting your Ryzen AI laptop do the on-device AI work it was built for.
