---
title: "How to Install OEM Drivers Manually in Windows 11 24H2"
slug: how-to-install-oem-drivers-manually-in-windows-11-24h2
date: 2026-10-08
categories: ["drivers"]
tags: ["oem drivers", "manual driver install", "windows 11 24h2", "device manager"]
description: "Need to install OEM drivers manually on Windows 11 24H2? Learn the right way to install manufacturer drivers via Device Manager and INF files."
thumbnail: "/images/thumbs/how-to-install-oem-drivers-manually-in-windows-11-24h2.webp"
faqs:
  - q: "When should I install OEM drivers manually instead of using Windows Update?"
    a: "Install manually when Windows Update provides a generic driver that misbehaves on your hardware, when a device is missing or error-flagged and no update is offered at all, or when the manufacturer releases a newer tuned driver than Microsoft's catalog carries. Manual installation gives you exact version control that automatic updates never provide, which matters for finicky devices like audio codecs and wireless cards."
  - q: "Is it safe to install drivers from INF files manually?"
    a: "Yes, when the INF comes from your laptop manufacturer's official support site for your exact model. The risk comes from third-party driver sites bundling modified INFs. Stick to Dell, HP, Lenovo, or the component maker's official downloads and manual INF installation is completely safe."
  - q: "What do I do if Windows says the best driver is already installed?"
    a: "That message only means Windows prefers its current choice, not that it is correct. Use the Have Disk path in Device Manager to force your INF, or uninstall the current driver with driver deletion first and then install yours before Windows Update can intervene."
  - q: "Should I disable driver signature enforcement to install OEM drivers?"
    a: "No. Legitimate OEM drivers from major manufacturers are properly signed and install without touching signature enforcement at all. If a driver demands disabled enforcement, treat that as a red flag about its source rather than a routine step — it likely came from an untrustworthy third-party site. Real manufacturer packages from Dell, HP, Lenovo, Intel, or Realtek never require this."
---

There are times when letting Windows handle drivers is the wrong call: the update catalog serves a generic build that crashes your audio, Device Manager shows an unknown device Windows cannot identify, or the manufacturer's tuned package simply never appears in Windows Update. In those cases, installing the OEM driver manually — pointing Windows at the exact driver files yourself — is the precise, controlled fix.

Manual installation is not hacking. Device Manager has a supported "Have Disk" path designed exactly for this, and every major laptop maker publishes raw driver packages for their models. The skill is knowing where to get the files, how to feed them to Windows, and how to stop Windows Update from undoing your work afterward.
One thing to internalize before you start: manual driver installation isn't a hack or a workaround — it's the same mechanism Windows itself uses, just with you choosing the files instead of Windows Update. Device Manager's "Have Disk" path is a supported, documented feature. The only real risks are picking the wrong driver for your hardware and letting Windows Update undo your work, and the steps below guard against both.

## Why this happens

- **Windows Update serves generic drivers:** Microsoft's catalog prioritizes broad compatibility over per-model tuning, so maker-specific features and fixes get lost.
- **New hardware, old catalog:** Recently released components may have no Windows Update driver at all, leaving unknown devices.
- **Corrupted automatic installs:** Interrupted updates leave half-installed drivers that block both automatic and manual reinstalls until cleaned out.
- **Version conflicts:** Windows considers its catalog driver "best" by date or rank and refuses to yield to the better OEM build without manual forcing.
- **Missing installer packages:** Some makers ship drivers as bare INF packages with no setup.exe, requiring manual installation by design.
- **24H2 driver model changes:** Windows 11 24H2 tightened driver handling, making manual installation the reliable path where auto-install stumbles.
- **Downgrade needs:** Rolling back to a known-good older driver version requires manual installation — Windows Update only moves forward.
- **Clean installations:** Fresh Windows installs need the full OEM driver set applied manually before everything works properly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Download the correct OEM driver package

1. Go to your maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — and enter your exact model or serial number.
2. Select **Windows 11** (and 24H2 if offered) as the OS to filter the list.
3. Download the driver for your specific device (audio, WiFi, graphics, chipset) — prefer the newest version dated for your OS.
4. If the download is a ZIP, extract it to a memorable folder like `C:\Drivers\Audio`; note where the `.inf` files land.

### Fix 2: Install via Device Manager's Have Disk path

1. Open **Device Manager**, right-click the target device → **Update driver → Browse my computer for drivers**.
2. Click **Let me pick from a list of available drivers**, then **Have Disk**.
3. Browse to the extracted folder, select the `.inf` file, and click OK.
4. Choose the correct model from the list if several appear, then **Next** to install. Accept any signature prompt for official drivers.
5. If Device Manager lists several compatible models and you're unsure, check how [battery driver updates](/articles/how-to-update-battery-drivers-in-windows-11-24h2/) pick the right entry — the same "match the hardware ID" principle applies to every device class.

### Fix 3: Clean out the old driver first when forcing a version

1. In Device Manager, right-click the device → **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Restart the laptop — Windows will load a basic fallback driver or leave the device unrecognized.
3. Immediately perform the Have Disk install from Fix 2 before Windows Update runs.
4. Temporarily disconnect from the internet during this window if Windows Update keeps racing you to install its version.

### Fix 4: Install using the manufacturer's setup when available

1. If the package includes a `setup.exe`, prefer it over manual INF installation — it handles dependencies, utilities, and registry settings the INF alone skips.
2. Right-click `setup.exe` → **Run as administrator**.
3. For packages that refuse on 24H2, try **Properties → Compatibility → Windows 11** or Windows 10 mode.
4. Restart after installation even if not prompted — driver bindings often finalize only at boot.

### Fix 5: Handle "best driver already installed" blocks

1. When Windows refuses your driver claiming a better one exists, open the device's **Properties → Driver → Driver Details** and note the current version.
2. Use **Uninstall device** with driver deletion to remove the blocking version entirely.
3. In **Group Policy** (`gpedit.msc → Computer Configuration → Administrative Templates → System → Device Installation`), you can restrict driver installation sources on Pro editions.
4. Then Have Disk-install your OEM driver into the now-empty slot.
5. As a last resort for truly stubborn blocks, disconnect from the internet entirely during the install — with no Windows Update reachable, Windows can't second-guess your choice, and you can reconnect after verifying the driver version stuck.

### Fix 6: Verify the installation actually took

1. In Device Manager, check the device's **Properties → Driver** tab — the **Driver Provider** should show the manufacturer (Realtek, Intel, Synaptics), not Microsoft.
2. Confirm the **Driver Date** and **Version** match the package you downloaded.
3. Test the device's actual function — a driver that installs but does not work needs the clean-out treatment from Fix 3.
4. Check **Event Viewer → Windows Logs → System** for driver load errors if the device still misbehaves.
5. Take a screenshot or note of the working driver version and date once everything works — when the next Windows update breaks the device again, you'll know exactly which version to reinstall without repeating the detective work.

### Fix 7: Stop Windows Update from replacing your driver

1. Once the working OEM driver is in place, open **System → About → Advanced system settings → Hardware → Device Installation Settings** and choose **No**.
2. On Pro editions, use Group Policy: **Do not include drivers with Windows Updates** under **Windows Update → Manage updates offered from Windows Update**.
3. Alternatively, use the registry `ExcludeWUDriversInQualityUpdate` value documented in Microsoft's official Windows support documentation.
4. Recheck after each feature update — major updates can reset this preference.

## Closing

Manual OEM driver installation is a core technician skill: get the right package from the maker, feed it to Device Manager via Have Disk after cleaning out the old driver, verify the provider and version, then lock Windows Update out of the driver's business. It takes longer than clicking "update driver" and hoping, but it is the difference between a driver that happens to install and a driver that actually works. The same discipline underpins fixing [vanished WiFi adapters](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) and other driver-level failures.
