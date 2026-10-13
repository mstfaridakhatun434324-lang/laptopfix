---
title: "SD Card Not Detected on Windows 10? Here's the Fix"
slug: how-to-fix-sd-card-not-detected-on-windows-10
date: 2026-09-13
categories: ["drivers"]
tags: ["sd card", "card reader", "windows 10", "not detected"]
description: "SD card invisible on Windows 10? Fix undetected cards from drive letters to reader drivers with this step-by-step guide."
thumbnail: "/images/thumbs/how-to-fix-sd-card-not-detected-on-windows-10.webp"
faqs:
  - q: "Why doesn't my SD card show up in Windows 10 File Explorer?"
    a: "Either Windows can't see the reader hardware (driver problem), or it sees the card but won't mount it (missing drive letter or filesystem damage). The split-second diagnostic is Disk Management: card visible there means a mount problem, usually fixed by assigning a drive letter; card absent there means the reader driver or the card itself needs attention."
  - q: "The SD card worked yesterday on this same Windows 10 laptop. What changed?"
    a: "Overnight changes are almost always software: a Windows update replaced the card-reader or chipset driver, or a power setting suspended the reader. Physically, the card may have shifted in the slot. Re-seat the card, check Disk Management, and look at the reader driver date — if it matches the update, reinstall the manufacturer's driver."
  - q: "Windows 10 asks me to format the SD card. Should I?"
    a: "Not before recovering your data. The format prompt means Windows sees the card but can't read its filesystem — your files may still be recoverable with data-recovery software. Only format after recovery (or if the card is empty), and prefer exFAT for cards over 32 GB. If the prompt appears for a card that works in your camera, the issue is Windows-side, not the card."
  - q: "Can I use the SD slot for extra storage permanently?"
    a: "You can, but SD cards are slower and less durable than SSDs — fine for documents and media, poor for programs or anything write-intensive. If you do, buy a high-endurance card, keep backups, and never remove it without ejecting. For genuinely useful expansion, a small USB 3.0 flash drive usually outperforms an SD card."
---

Windows 10 has been reading SD cards for a decade, which makes it doubly confusing when your card suddenly goes invisible — no autoplay, no drive letter, nothing in File Explorer. The maturity of the OS doesn't matter here; the failure points are the same handful they've always been: the reader driver, the drive letter assignment, the card's filesystem, and the card itself.

The fastest diagnostic hasn't changed either: **Disk Management** (**Win + X** > Disk Management) with the card inserted. Card visible there = Windows sees the hardware and the problem is mounting (drive letter or filesystem). Card absent = the reader, its driver, or the card is at fault. That one check decides which half of this guide applies to you.

Windows 11 users should follow our [SD card fix for Windows 11](/articles/how-to-fix-sd-card-not-detected-on-windows-11/) instead — the steps are similar but the Settings paths differ.

## Why this happens

- **The card reader driver is missing or outdated.** Clean installs and updates leave the Realtek/Genesys reader driver absent — the slot goes electrically dead as far as Windows is concerned.
- **Windows didn't assign a drive letter.** The card is detected but unmounted — common when the expected letter is taken by a network drive or another device.
- **The filesystem is damaged.** Unsafe ejections corrupt the partition table; Windows sees a card it can't read and may prompt to format.
- **The card isn't making contact.** Dust in the slot or a partially inserted card — spring-loaded slots are finicky about full insertion.
- **USB selective suspend parked the reader.** Windows 10's aggressive USB power saving puts internal readers to sleep and sometimes never wakes them.
- **The card has worn out.** Flash cells degrade; a card that's undetectable in every device has reached end of life.
- **A drive-letter conflict with mapped network drives.** Corporate laptops with mapped drives can steal the letter Windows wants for the card, leaving it letterless.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reseat the card and inspect Disk Management

Physical basics plus the decisive diagnostic.

1. Eject the card, check the slot for visible dust or debris, and reinsert firmly until it seats fully — on spring-loaded slots, push until it clicks.
2. Open **Disk Management** (**Win + X** > Disk Management) and find the card. Note exactly how it appears: healthy with no letter, unallocated, RAW, or absent.
3. If present **without a drive letter**: right-click > **Change Drive Letter and Paths** > **Add** > pick a high, unused letter like **S:** or **T:** to avoid network-drive conflicts.
4. Open File Explorer and confirm the card is accessible. If it was a letter problem, you're done — this is the single most common fix.

### Fix 2: Reinstall the card reader and chipset drivers

For cards absent from Disk Management entirely.

1. Open **Device Manager** and look for the reader under **Memory technology devices** — typically *Realtek PCIE CardReader*.
2. If it's missing or flagged, download the **card reader** and **chipset** drivers for your exact model from the laptop manufacturer's support site.
3. Uninstall the existing reader entry (check *Delete the driver software for this device* on Windows 10), install the chipset package first, then the reader driver, and reboot.
4. With no card inserted, the reader should now appear in Device Manager cleanly — insert the card and recheck Disk Management.

### Fix 3: Isolate with a USB reader

Determines whether the fault is the built-in reader or the card.

1. Insert the card into an external **USB card reader** and plug it into the laptop.
2. Card appears = built-in reader or its driver is the problem. Revisit Fix 2, and check the BIOS for a media-card-reader toggle (present on some business models).
3. Card still absent = try the USB reader on another computer to confirm.
4. Dead in all devices = dead card (see Fix 7). If the USB path also misbehaves generally, the [USB device troubleshooting guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) covers the broader USB stack.

### Fix 4: Disable USB selective suspend

For readers that vanish after idle or sleep.

1. Open **Control Panel > Power Options > Change plan settings > Change advanced power settings**.
2. Expand **USB settings > USB selective suspend setting** and set it to **Disabled** for both On battery and Plugged in.
3. In **Device Manager > Universal Serial Bus controllers**, uncheck *Allow the computer to turn off this device to save power* on each **USB Root Hub**.
4. Restart and test across a sleep/wake cycle with the card inserted.

### Fix 5: Resolve drive-letter conflicts

When the card appears but won't take a letter.

1. In **Disk Management**, if **Change Drive Letter and Paths** is grayed out or the letter won't stick, a mapped network drive or hidden device is squatting on the letter.
2. Assign a high letter (**S:** through **Z:**) that no network mapping uses — corporate environments rarely map that high.
3. Check for phantom devices: **Device Manager > View > Show hidden devices** > look under **Storage volumes** and **Portable Devices** for grayed-out entries from old cards and uninstall them.
4. Reinsert the card and confirm it mounts with the new letter consistently across reboots.

### Fix 6: Repair or reformat the filesystem (data first)

For cards visible in Disk Management but unreadable.

1. If Windows prompts to format, **decline** for now — run data-recovery software (Recuva, PhotoRec) first if the files matter.
2. Try repair: elevated Command Prompt > `chkdsk X: /f` (X: = the card's letter) — this fixes logical filesystem errors without data loss.
3. If repair fails and data is recovered or unimportant: **Disk Management** > right-click > **Format** > **exFAT** (cards over 32 GB), allocation unit size **Default**, and give it a label.
4. For the most flash-friendly format, use the SD Association's free **SD Memory Card Formatter**. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the built-in disk-management tools for reference.

### Fix 7: Retire a dead card properly

When no device anywhere detects the card.

1. Confirm across at least three devices (laptop, USB reader on another PC, camera or phone) — unanimous silence means dead flash.
2. For valuable data, professional chip-off recovery is the only option — weigh the $300+ cost against the data's worth.
3. Replace with a card from a reputable brand bought from a reputable seller; counterfeit cards are the leading cause of premature SD death.
4. Going forward: always use **Safely Remove Hardware** before ejecting, and don't use the SD slot as the only copy of anything important.

## Closing

Windows 10 SD detection comes down to the same chain it always has: seat the card, check Disk Management, assign the letter if it's missing, reinstall the reader driver if the hardware's invisible, and test the card in another device before declaring it dead. The fix is at the broken link — and the broken link is usually the driver or the drive letter, not the card.
