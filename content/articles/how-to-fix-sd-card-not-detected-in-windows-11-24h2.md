---
title: "SD Card Not Detected in Windows 11 24H2? 7 Fixes for the Card Reader"
slug: how-to-fix-sd-card-not-detected-in-windows-11-24h2
date: 2026-09-16
categories: ["drivers"]
tags: ["sd card", "card reader", "windows 11 24h2", "realtek"]
description: "SD card not detected after Windows 11 24H2? Fix the card reader with these 7 steps — driver reinstalls, drive letter assignment, and 24H2-specific repairs."
thumbnail: "/images/thumbs/how-to-fix-sd-card-not-detected-in-windows-11-24h2.webp"
faqs:
  - q: "Why is my SD card not detected after the Windows 11 24H2 update?"
    a: "The 24H2 update has a known pattern of breaking SD card readers: it replaces the working Realtek card reader driver with an incompatible version, and in some cases the reader disappears from Device Manager entirely. The fix is to uninstall the card reader driver with driver deletion, then install the manufacturer's version from your laptop maker's support site. Also check Disk Management — the card may be detected but missing a drive letter after the update."
  - q: "How do I know if the SD card or the reader is broken?"
    a: "Test the card in another device — a phone, camera, or different computer. If the card works elsewhere, your reader or its driver is the problem. If the card fails everywhere, the card itself is faulty; try data recovery software before reformatting. Also test a different card in your laptop's reader: if no card works in the reader but all cards work elsewhere, the reader hardware or driver is at fault."
  - q: "Should the SD card show up in Device Manager?"
    a: "The card reader shows up — the card itself doesn't get its own Device Manager entry. Look under Memory technology devices, SD host adapters, or Universal Serial Bus controllers for entries like Realtek PCIE CardReader or USB Mass Storage Device. If the reader is missing entirely, enable Show hidden devices; a greyed-out reader means Windows disabled it. The card appears in File Explorer and Disk Management once the reader works."
  - q: "Can I recover data from an SD card Windows won't detect?"
    a: "If the card isn't detected at all, recovery software can't see it either — fix detection first using the steps above. Once the card appears in Disk Management (even as unallocated or RAW), tools like Recuva, PhotoRec, or Disk Drill can scan it. Never format the card before attempting recovery. If the card is physically damaged, professional recovery is the only option — see the [SD card troubleshooting guide](/articles/how-do-i-fix-sd-card-not-detected/) for the recovery workflow."
---

You slide the SD card into the slot, and... nothing. No autoplay, no new drive in File Explorer, no sound. If this started after the Windows 11 24H2 update, you're in crowded company — 24H2 has a particular talent for breaking built-in card readers, usually by swapping in an incompatible Realtek driver.

This guide targets the 24H2 scenario specifically but works for any Windows 11 card reader failure. The fixes move from driver repair (the most common cause) through Windows configuration to hardware isolation.

## Why this happens

- **24H2 replaced the card reader driver:** The update installs a generic or mismatched Realtek RTS driver that can't initialize the reader.
- **Card reader missing from Device Manager:** The driver fails so early that Windows doesn't enumerate the reader at all.
- **Drive letter missing:** The card is detected at the hardware level but Windows never assigns it a letter.
- **Card inserted incorrectly or dirty contacts:** SD cards only seat one way; dust or oxidation on contacts breaks the connection.
- **Corrupt card filesystem:** A card with a damaged filesystem may not mount even when the reader works.
- **Write-protect or lock switch:** The physical lock slider in the wrong position can prevent mounting on some readers.
- **Power management disabling the reader:** USB power saving turns off the reader between uses.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean the card, check the lock switch, and reseat it

Rule out the physical basics in sixty seconds.

1. Remove the card and check the **lock slider** on its left edge — slide it **up** (toward the contacts) to unlock.
2. Wipe the gold contacts gently with a dry microfiber cloth or pencil eraser to remove oxidation.
3. Blow out the reader slot with compressed air — lint accumulates in laptop slots.
4. Reinsert the card firmly until it clicks or seats fully (orientation matters — contacts face the right way per your laptop's diagram).
5. Listen for the Windows device-connection sound.

Try a second card if you have one — this immediately splits card problems from reader problems.

### Fix 2: Check Disk Management for a letterless card

The reader may be working fine while Windows hides the card for lack of a drive letter — extremely common after 24H2.

1. Press **Win + X** and open **Disk Management**.
2. Insert the card and watch for a new removable disk appearing in the lower pane.
3. If it appears without a drive letter, right-click it and choose **Change Drive Letter and Paths > Add**, assign a letter, and click OK.
4. If it appears as **RAW** or **Unallocated**, don't format yet — that's a filesystem problem (Fix 6), not a detection problem.
5. Open File Explorer and check for the drive.

If Disk Management shows nothing at all when the card is inserted, the reader driver isn't working — continue.

### Fix 3: Reinstall the card reader driver (the 24H2 fix)

This is the core repair for post-24H2 reader failures.

1. Open Device Manager (**Win + X**).
2. Expand **Memory technology devices** or **SD host adapters** — look for **Realtek PCIE CardReader**, **Realtek USB Card Reader**, or similar.
3. If the category doesn't exist, check under **Universal Serial Bus controllers** and enable **View > Show hidden devices**.
4. Right-click the reader and choose **Uninstall device**, ticking **Attempt to remove the driver for this device**.
5. Restart the laptop.

After reboot, Windows installs a base driver. Test the card — then install the manufacturer's card reader driver from your laptop maker's support site for the permanent fix, since Windows' choice may be the same broken one 24H2 installed.

### Fix 4: Install the manufacturer's card reader driver

Don't rely on the driver Windows picks — get the validated one.

1. Go to your laptop maker's support site (Dell, HP, Lenovo) and find your exact model.
2. Download the **card reader / Realtek RTS** driver package.
3. Install it and restart.
4. Insert the card and check both Device Manager (reader present, no warning) and File Explorer.

For Dell machines specifically, [Dell support](https://www.dell.com/support) hosts the validated Realtek reader drivers. If the manufacturer's driver is older than what 24H2 installed, install it anyway — older-but-working beats newer-and-broken.

### Fix 5: Disable power management on the reader

Power saving can shut the reader down between insertions.

1. In Device Manager, find the card reader entry.
2. Open **Properties > Power Management** and untick **Allow the computer to turn off this device to save power** (USB-connected readers).
3. For PCIe readers without that tab, go to **Settings > System > Power & battery** and set **Power mode** to **Best performance** while testing.
4. Also disable **USB selective suspend**: **Control Panel > Power Options > Change plan settings > Change advanced power settings > USB settings > USB selective suspend setting > Disabled**.

Test card insertion several times — intermittent detection that works right after boot but fails later is the classic power-management pattern. If the reader itself has vanished from Device Manager rather than misbehaving, the [USB ports troubleshooting guide](/articles/best-way-to-fix-usb-ports-not-working/) covers controller-level repairs.

### Fix 6: Repair the card's filesystem

If the reader works but the card won't mount, the filesystem is corrupt.

1. Confirm the reader works with a different card first.
2. Open Command Prompt as administrator and run `chkdsk X: /f` (replace X: with the card's letter if it has one).
3. If the card has no letter, assign one in Disk Management (Fix 2), then run chkdsk.
4. If chkdsk can't fix it, recover data first with PhotoRec or Recuva, then format the card **in the device you'll use it in** (camera, phone) — or as **exFAT** in Windows for cross-device use.

Never format before recovering data you need. Cards that repeatedly corrupt may be counterfeit or worn out — replace them.

### Fix 7: Roll back 24H2's driver update and block it

If a working reader broke the moment 24H2 installed, stop Windows from re-breaking it.

1. In Device Manager, open the reader's **Properties > Driver** tab and click **Roll Back Driver** if available.
2. Go to **Settings > Windows Update** and **Pause updates** temporarily.
3. Use Microsoft's **Show or hide updates** troubleshooter to hide the card reader driver update.
4. As a last resort for driver enforcement issues, **Settings > System > About > Advanced system settings > Hardware > Device Installation Settings** > **No** stops Windows from auto-installing manufacturer drivers.

If the reader never appears in Device Manager even with hidden devices shown, across driver reinstalls, the reader hardware may have failed — USB card readers cost under $15 and bypass the internal reader entirely. The general [SD card detection guide](/articles/how-do-i-fix-sd-card-not-detected/) covers non-24H2 scenarios.

## Closing

Post-24H2 SD card failures are overwhelmingly driver problems: the update swaps in a reader driver that doesn't work, and reinstalling the manufacturer's driver puts it right. The Disk Management letter check catches the second-biggest group. Once the reader enumerates reliably, keep the manufacturer's driver pinned and 24H2's driver meddling blocked.
