---
title: "How to Fix an SD Card Not Detected After a Windows 11 Update"
slug: how-to-fix-sd-card-not-detected-after-windows-11-update
date: 2026-09-27
categories: ["drivers"]
tags: ["sd card", "windows 11 update", "card reader", "device manager"]
description: "SD card stopped working after a Windows 11 update? Work through driver, power, and slot checks to get your card reader recognizing cards again."
thumbnail: "/images/thumbs/how-to-fix-sd-card-not-detected-after-windows-11-update.webp"
faqs:
  - q: "Why did my SD card stop working right after a Windows 11 update?"
    a: "Updates frequently replace the card reader driver with a generic Windows version that does not initialize certain Realtek or Genesys Logic controllers correctly. The hardware is fine; the driver binding changed. Rolling back or reinstalling the manufacturer's driver almost always restores detection without touching the card itself."
  - q: "Does an undetected SD card mean my files are lost?"
    a: "Almost certainly not. A detection problem is between Windows and the reader, not the card's data. Do not format the card. Once the reader works again, the files are usually intact. If the card stays unreadable everywhere, test it in a phone or camera before assuming data loss."
  - q: "Should I disable and re-enable the card reader in Device Manager?"
    a: "Yes, that is a safe and sensible first step. Disabling and re-enabling forces Windows to re-enumerate the device and reload its driver from scratch, which clears transient glitches cleanly. If the reader reappears but still ignores cards, move on to a full driver reinstallation — a disable cycle only fixes temporary enumeration hiccups, never a genuine driver mismatch left behind by the update."
  - q: "Can a USB card reader replace my broken built-in slot?"
    a: "Yes, and cheaply. A USB 3.0 SD reader costs a few dollars and works independently of the built-in controller, bypassing whatever driver or hardware fault killed the internal slot. Use one as a temporary workaround while troubleshooting, or permanently if you decide the internal repair is not worth the effort — for most people, a tiny USB reader is the pragmatic end of this problem."
---

An SD card that worked yesterday and is invisible today, right after a Windows 11 update, points at one prime suspect: the update swapped your card reader's driver. The card itself is almost certainly fine, and so is the reader hardware. What changed is the software contract between Windows and the reader controller — and that is repairable in well under an hour.

Before diving in, rule out the trivial: try a second SD card and, if possible, try your card in a phone or camera. If the card works elsewhere and no card works in the laptop, the problem is firmly on the laptop side. That thirty-second test saves you from chasing the wrong trail.
It helps to know what you're dealing with: most laptop SD readers are USB-attached internally, even though the slot looks like dedicated hardware. That means the reader depends on the USB driver stack as well as its own controller driver — and a Windows update can break either layer. The fixes below cover both, so a reader that fails for USB power reasons gets fixed just as surely as one with a mismatched controller driver.

## Why this happens

- **Driver replaced by Windows Update:** The update installs a generic SD host controller driver over the manufacturer's tuned one, and the generic driver fails to initialize the reader.
- **Reader disabled in Device Manager:** Post-update re-enumeration sometimes leaves the SD host controller in a disabled state.
- **Power management suspending the reader:** USB-based internal card readers can get stuck in selective suspend after the update changes power policies.
- **Drive letter conflict:** Windows may detect the card but fail to assign it a drive letter, making it invisible in File Explorer while present in Disk Management.
- **Corrupt card file system misread:** If the update was interrupted, the card's partition table can be left in a state Windows refuses to mount.
- **Fast Startup stale device state:** Fast Startup can carry a broken device state across reboots, making the reader stay dead until a full shutdown.
- **BIOS storage settings changed:** Rare, but some updates toggle storage controller modes that affect how the reader enumerates.
- **Physical slot contamination:** Unrelated to the update but worth ruling out — dust or a bent pin in the slot causes intermittent or total detection failure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm where the card actually disappears

1. Insert the SD card and open **Disk Management** (Win + X → Disk Management).
2. If the card appears there without a drive letter, right-click it → **Change Drive Letter and Paths → Add** and assign a letter. Problem solved.
3. If it appears as unallocated or RAW, do not format yet — note it and continue to the driver fixes.
4. If it does not appear in Disk Management either, the reader itself is not enumerating, which points to drivers.

### Fix 2: Re-enable and rescan the card reader in Device Manager

1. Open **Device Manager** and expand **Memory technology devices** or **Universal Serial Bus controllers** to find the card reader (often labeled Realtek PCIE CardReader or similar).
2. If it shows a down arrow, right-click → **Enable device**.
3. If it looks normal, right-click → **Disable device**, wait ten seconds, then **Enable device** again.
4. Click **Action → Scan for hardware changes** and reinsert the card.
5. If the reader shows up under **Universal Serial Bus controllers** as an unknown USB device, uninstall that entry as well and restart. Windows then rebuilds the entire USB enumeration for the reader, clearing faults that touching the reader entry alone never reaches.

### Fix 3: Roll back or reinstall the card reader driver

1. In Device Manager, right-click the card reader → **Properties → Driver → Roll Back Driver** if the option is available.
2. If rollback is grayed out, choose **Uninstall device**, tick **Attempt to remove the driver** if offered, then restart — Windows will reinstall a driver on boot.
3. For the lasting fix, download the card reader driver from your laptop maker's support page and install it manually, blocking Windows from overwriting it. This is the same driver discipline used for [WiFi adapters that vanish after updates](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/).
4. After installing, check [Windows Update history](https://support.microsoft.com/en-us/windows) and pause updates briefly to confirm the fix holds.
5. The same remove-then-reinstall discipline restores [wireless adapters that vanish after updates](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) — across every device class, deleting the bad driver completely before installing the good one is what makes the fix stick.

### Fix 4: Disable USB selective suspend

1. Open **Control Panel → Power Options → Change plan settings → Change advanced power settings**.
2. Expand **USB settings → USB selective suspend setting** and set it to **Disabled** for both battery and plugged-in.
3. Also, in Device Manager, find the USB hub feeding the reader, open **Properties → Power Management**, and uncheck **Allow the computer to turn off this device to save power**.
4. Restart and test the card again.

### Fix 5: Do a full shutdown to clear Fast Startup state

1. Hold **Shift** while clicking **Shut down** in the Start menu — this forces a full shutdown instead of hybrid sleep.
2. Wait ten seconds, then power on.
3. Insert the card and check detection. If it works now, consider disabling Fast Startup in **Control Panel → Power Options → Choose what the power button does**.

### Fix 6: Assign or repair the card via Diskpart (careful)

1. Open **Terminal (Admin)** and run `diskpart`, then `list disk` to identify the SD card by size.
2. If the disk shows but has no volume, `select disk N` then `attributes disk clear readonly` can remove a stuck read-only flag the update may have set.
3. Exit diskpart and recheck Disk Management. Never run `clean` on the card unless you have accepted data loss — that command wipes the partition table.

### Fix 7: Test the slot physically and fall back to USB

1. Power off, and use a can of compressed air to blow out the SD slot — dust causes more "dead reader" cases than people expect.
2. Inspect the slot with a flashlight for bent pins; do not probe them with metal tools.
3. If the slot is damaged or still dead after every software fix, buy a USB 3.0 SD reader as a permanent workaround — it bypasses the internal controller entirely.

## Closing

SD card detection failures after a Windows 11 update are a driver story in the overwhelming majority of cases, and the manufacturer's card reader driver is the fix. Once detection is restored, leave USB selective suspend off and keep a copy of the working driver — the next feature update will try to replace it again, and this time you will be ready in two minutes. Updates that knock out card readers often take USB devices down with them, so if your USB drives vanished in the same update, the [USB device not recognized after the update](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) guide runs the parallel fix.
