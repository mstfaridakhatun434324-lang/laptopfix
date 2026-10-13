---
title: "How to Fix Optional Updates Not Installing on an ASUS Laptop"
slug: how-to-fix-optional-updates-not-installing-on-asus-laptop
date: 2026-09-08
categories: ["windows-update"]
tags: ["optional updates", "asus laptop", "driver updates", "armoury crate"]
description: "Optional updates failing on your ASUS laptop? From Armoury Crate conflicts to manual driver installs, here's how to get them working."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-on-asus-laptop.webp"
faqs:
  - q: "Why do optional updates fail on ASUS laptops specifically?"
    a: "ASUS ships its own driver management through Armoury Crate and MyASUS, which can install versions that differ from what Windows Update offers. When Windows then tries to install its own version over ASUS's, the install can fail on version conflicts or locked files. ASUS gaming laptops with complex component stacks see this more than most brands."
  - q: "Does Armoury Crate block Windows optional updates?"
    a: "It can. Armoury Crate's background services manage power profiles, fan curves, and some device settings, and they occasionally hold locks on devices that Windows Update is trying to update. Updating Armoury Crate to the latest version or temporarily stopping its services before installing optional updates usually clears the conflict."
  - q: "Are ASUS optional driver updates safe to install?"
    a: "Generally yes, but ASUS-specific drivers from MyASUS are preferable for core components like the chipset, BIOS-adjacent firmware, and the discrete GPU on gaming models. Windows optional updates are fine for peripherals and generic devices. When both offer a driver for the same device, take the ASUS one for core hardware."
  - q: "What if an optional update keeps failing after all fixes?"
    a: "Hide it and move on. Use Microsoft's Show or Hide Updates troubleshooter to stop Windows offering that specific driver, then get the driver from ASUS support or the component maker's site instead. A single stubborn optional update is never worth hours of troubleshooting when the driver is available elsewhere."
---

Optional updates on an ASUS laptop live at the intersection of two driver systems that do not always agree: Windows Update's optional driver offerings and ASUS's own Armoury Crate/MyASUS driver management. When they disagree — different versions, locked devices, conflicting installers — the optional update fails, sometimes repeatedly, and the entry just sits there daring you to click it again.

ASUS machines add specific wrinkles. Armoury Crate's services touch power and device management, ASUS often customizes reference drivers for its ROG and TUF gaming lines, and MyASUS may have already installed a newer driver than the one Windows is offering. This guide sorts out which situation you are in and gets the updates you actually need installed.

ASUS's driver ecosystem is unusually active: Armoury Crate updates itself, MyASUS pushes driver notifications, and Windows Update offers its own versions, all on different schedules. That is three cooks in the driver kitchen, and optional-update failures are what dinner looks like when they disagree. The trick is appointing a head chef — for core hardware, that is ASUS's own tools — and letting Windows Update handle only the side dishes it is good at.

## Why this happens

- **Armoury Crate or MyASUS holding device locks** that block Windows Update's driver installer.
- **Version conflicts**: ASUS installed a newer (or custom) driver, and Windows Update's older package fails against it.
- **Custom ASUS driver builds** for ROG/TUF hardware that generic Windows Update packages cannot cleanly replace.
- **The optional update was superseded or withdrawn** by Microsoft but the stale entry remains.
- **Corrupted driver store** preventing the new driver package from staging.
- **Pending reboot** from an earlier install that Windows does not clearly flag.
- **Metered connection settings** silently blocking optional update downloads.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether you need the update at all

1. Open **Settings** > **Windows Update** > **Advanced options** > **Optional updates** and identify the exact driver offered.
2. Check **MyASUS** — if ASUS already installed an equal or newer driver for that device, you do not need Windows' version.
3. If the device works perfectly, uncheck the update and ignore it. Not every offered update deserves installation.
4. Only continue if a device is misbehaving and the optional update targets it.

### Fix 2: Update Armoury Crate and MyASUS first

1. Open the **Microsoft Store**, go to **Library**, and update **Armoury Crate** and **MyASUS** to their latest versions.
2. Open **MyASUS** and install any driver updates it offers for the device in question — prefer ASUS's driver over Windows'.
3. Restart the laptop after ASUS's updates complete.
4. Re-check optional updates. In many cases the entry disappears because ASUS's driver satisfied the requirement.

### Fix 3: Stop ASUS background services temporarily

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Stop any services starting with **Armoury Crate** or **ASUS** (right-click > **Stop**).
3. Open Task Manager's **Startup apps** tab and disable Armoury Crate entries temporarily.
4. Retry the optional update install now, with ASUS's services quiet. Re-enable them afterward. The official [Windows Update support page](https://support.microsoft.com/en-us/windows) covers service-conflict troubleshooting generally.

### Fix 4: Install one update at a time after a clean restart

1. Do a full **Restart** from the Start menu.
2. In **Optional updates**, select only the single driver you need and click **Download & install**.
3. Never batch multiple driver updates — one failure masks the others and wastes the whole attempt.
4. Restart again after installation before attempting any additional optional updates.

### Fix 5: Get the driver from the component maker

1. Identify the actual hardware: in **Device Manager**, check the device's **Hardware Ids** under Properties > Details if needed.
2. For graphics, download directly from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD's driver download page, or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
3. Run the manufacturer's installer as administrator — these packages are more current than Windows Update's and bypass it entirely.
4. After installing, the optional update entry typically clears itself within a day. Related driver-update failures: [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/).

### Fix 6: Repair the driver store and update cache

1. Open an elevated Command Prompt and run:
   `net stop wuauserv`
2. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
3. Run `net start wuauserv`, then retry the optional update.
4. If it still fails, the driver store itself may be damaged — in the same elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`, reboot, and retry. See also [stuck download repairs](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/).

### Fix 7: Hide the stubborn update and move on

1. Download Microsoft's **Show or Hide Updates** troubleshooter (`wushowhide.diagcab`).
2. Run it, choose **Hide updates**, and select the failing optional driver.
3. Windows stops offering it; install the driver from ASUS or the component maker instead (Fix 5).
4. Check back in a few months — updated packages usually appear that install cleanly.

### Fix 8: Extract the ASUS driver package and install via Have Disk

ASUS driver installers sometimes refuse to run when they detect a version conflict; extracting the files and installing manually sidesteps the check.

1. Download the driver from ASUS support for your exact model and extract it (an archive tool opens most ASUS installer packages).
2. In **Device Manager**, right-click the device > **Update driver** > **Browse my computer for drivers** > **Let me pick from a list** > **Have Disk**.
3. Point at the extracted `.inf` file and finish the wizard.
4. Restart, verify the device, and confirm the optional update entry clears. This is the definitive manual path when every automated route fails.

## Closing

On ASUS laptops, optional update failures are usually a turf war between ASUS's driver management and Windows Update's. Let ASUS win for core hardware — update Armoury Crate and MyASUS first, quiet their services during installs, and go straight to the component maker for graphics drivers. The optional updates list is a suggestion box, not a to-do list. Once the driver you need is installed by whatever route worked, stop and declare victory — do not keep clicking the remaining optional updates out of completeness. A stable ASUS with one manually installed driver beats a churned one with ten, every time.
