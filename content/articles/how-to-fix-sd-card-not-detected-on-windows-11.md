---
title: "SD Card Not Detected on Windows 11? Here's How to Fix It"
slug: how-to-fix-sd-card-not-detected-on-windows-11
date: 2026-09-08
categories: ["drivers"]
tags: ["sd card", "card reader", "not detected", "windows 11"]
description: "SD card not showing up on Windows 11? Fix undetected SD cards from the reader driver to the card itself, step by step."
thumbnail: "/images/thumbs/how-to-fix-sd-card-not-detected-on-windows-11.webp"
faqs:
  - q: "Why is my SD card not showing up in File Explorer on Windows 11?"
    a: "The usual chain is: the card reader driver isn't loaded, the card has no drive letter assigned, or the card's partition table is damaged. Check Disk Management first — if the card appears there without a drive letter, assigning one fixes it instantly. If it's absent there too, the problem is the reader driver or the card itself."
  - q: "My SD card works in my camera but not in my laptop. What's wrong?"
    a: "Then the card is fine and the laptop's reader or driver is the problem. Camera-formatted cards (often exFAT) are readable by Windows, so format isn't the issue — focus on the card reader driver, try the card in a USB reader to isolate the built-in reader, and check Disk Management for the device."
  - q: "Can a Windows 11 update break the SD card reader?"
    a: "Yes. Card readers depend on chipset and storage controller drivers that Windows Update sometimes replaces with incompatible versions. If the reader died right after an update, reinstall the chipset and card-reader drivers from your laptop manufacturer's site — that restores detection in most cases."
  - q: "Should I format an SD card that Windows 11 can't detect?"
    a: "Not until you've ruled out driver and hardware causes, and never before recovering your data. If Disk Management sees the card but calls it RAW or unallocated, photo-recovery software can often rescue files first. Format only as a last resort, and use the SD Association's formatter rather than Windows' quick format for the healthiest result."
---

You slide the SD card in, the laptop does nothing — no chime, no drive letter, no sign in File Explorer that anything happened. Or worse, it chimes and then shows nothing. SD card detection failures on Windows 11 sit at the intersection of three systems — the card reader hardware, its driver, and the card's own filesystem — and the fix depends entirely on which one is actually broken.

The diagnostic that splits the problem in half takes thirty seconds: open **Disk Management** (**Win + X** > Disk Management) with the card inserted. If the card appears there, Windows sees the hardware and the issue is logical — a missing drive letter or a damaged filesystem. If it doesn't appear there at all, the issue is physical or driver-level: the reader, its driver, or a dead card. Everything below branches from that observation.

Windows 10 users should follow our [SD card fix for Windows 10](/articles/how-to-fix-sd-card-not-detected-on-windows-10/) — the steps are similar but the Settings paths differ.

## Why this happens

- **The card reader driver is missing or broken.** After clean installs and some Windows updates, the Realtek/Genesys card-reader driver is absent — the slot is electrically dead to Windows.
- **No drive letter is assigned.** Windows detects the card but doesn't mount it — common after partition changes or when another device claimed the expected letter.
- **The card's filesystem is corrupted.** An unsafe ejection or a dying card produces RAW or unrecognized partitions that Windows won't mount.
- **The card isn't seated properly.** SD slots — especially spring-loaded ones — can fail to make contact if the card isn't fully inserted or the slot is full of dust.
- **Power management suspended the reader.** USB-connected internal readers get powered down by Windows' aggressive USB power saving and never wake.
- **The card itself has died.** Flash memory wears out; a card that isn't detected in any device — camera, phone, USB reader — is simply dead.
- **A Windows 11 update changed the storage stack.** Chipset driver mismatches after feature updates can take the reader offline along with other internal devices.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reseat the card and check Disk Management

The physical basics plus the key diagnostic.

1. Remove the card, blow out the slot (compressed air, not your mouth — moisture), and reinsert firmly until it clicks or sits flush.
2. Press **Win + X** > **Disk Management** and look for the card — it may appear as a removable disk with no drive letter, as unallocated space, or as RAW.
3. If it appears **without a drive letter**: right-click it > **Change Drive Letter and Paths** > **Add** > assign a letter. Check File Explorer — the card should now be there.
4. If it appears as **unallocated or RAW**, don't format yet — that's Fix 6. If it's **absent entirely**, continue to Fix 2.

### Fix 2: Reinstall the card reader driver

The anchor fix when Disk Management sees nothing.

1. Open **Device Manager** and look under **Memory technology devices** (or **Universal Serial Bus controllers**) for the card reader — often *Realtek PCIE CardReader* or similar.
2. If it's missing or has a warning icon, download the **card reader** and **chipset** drivers for your exact model from the laptop maker's support site.
3. Right-click the reader > **Uninstall device** (check *Attempt to remove the driver*), then install the downloaded packages — chipset first, then the reader driver — and reboot.
4. Reinsert the card and recheck Disk Management. A healthy reader shows up in Device Manager with no warnings even with no card inserted.

### Fix 3: Test with a USB card reader

The definitive isolation test — built-in reader vs. card.

1. Plug the SD card into an external **USB card reader** ($8–12) and connect it to the laptop.
2. If the card appears, your **built-in reader or its driver** is the fault — revisit Fix 2, and check the BIOS for a card-reader toggle (some business laptops have one).
3. If the card doesn't appear in the USB reader either, try the USB reader on a **different computer**.
4. Card dead everywhere = dead card (Fix 7). Card works elsewhere = your laptop's USB subsystem or Windows install needs attention — try the [USB device troubleshooting steps](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/).

### Fix 4: Disable USB power management

For readers that work after boot but vanish later, or never wake.

1. In **Device Manager**, expand **Universal Serial Bus controllers**.
2. For each **USB Root Hub** and **Generic USB Hub**: **Properties > Power Management** > uncheck *Allow the computer to turn off this device to save power*.
3. In **Power Options > Change advanced power settings**, set **USB settings > USB selective suspend** to **Disabled**.
4. Reboot, insert the card, and leave it for a few minutes — then check whether it's still detected after the laptop sleeps and wakes.

### Fix 5: Update the chipset drivers

The card reader hangs off the chipset; a broken chipset driver orphans it.

1. Download the **chipset driver** package for your exact model from the laptop manufacturer's support site — not from the chip vendor's generic page.
2. Install it (as administrator) and reboot. Chipset installers re-enumerate internal devices, which often resurrects a missing reader.
3. After reboot, check **Device Manager** for the reader's reappearance before reinserting the card.
4. If Windows Update previously replaced your chipset driver, consider blocking automatic driver updates afterward — our [driver update control guide](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) covers how.

### Fix 6: Repair the filesystem (data-safe order)

Only for cards that appear in Disk Management but won't mount — and recover data first.

1. If the card shows as **RAW** or with errors, first try photo/data recovery software (Recuva, PhotoRec) to copy files off — recovery works best before any repair attempts.
2. Then open an **elevated Command Prompt** and run `chkdsk X: /f /r` (replace X: with the card's letter if it has one) to repair filesystem errors.
3. If chkdsk can't help, use **Disk Management** > right-click the card > **Format** — choose **exFAT** for cards over 32 GB, **FAT32** for smaller ones, and uncheck *Quick Format* for a thorough job.
4. For the healthiest format, use the free **SD Memory Card Formatter** from the SD Association rather than Windows' formatter — it's designed for flash media. Microsoft's [Windows storage support pages](https://support.microsoft.com/en-us/windows) document the built-in disk tools if you prefer staying native.

### Fix 7: Accept a dead card and protect the next one

When the card is detected nowhere, it's over — focus on data and prevention.

1. Confirm death: card not detected in the laptop, in a USB reader, in a camera, or in a phone. Four strikes = dead flash.
2. If the data matters, professional recovery labs can sometimes read dead cards by removing the flash chip — expensive ($300+), but the only option when nothing detects the card.
3. For the replacement: buy cards from reputable brands and retailers (counterfeit cards die young and lie about capacity), and always **eject safely** before removal.
4. Keep a spare USB reader handy — it also serves as the fastest way to test whether future "not detected" scares are the card or the laptop.

## Closing

SD card detection is a chain — card, reader, driver, mount — and the fix is always at the broken link: reseat and check Disk Management to find it, reinstall the reader and chipset drivers when the link is software, and test in another device when you suspect the card. Most "dead" SD cards turn out to be driver or drive-letter problems; the genuinely dead ones are the ones no device on earth will acknowledge.
