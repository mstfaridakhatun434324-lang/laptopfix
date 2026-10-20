---
title: "Copilot+ PC SSD Upgrade Guide: What Actually Works"
slug: copilot-plus-pc-ssd-upgrade-guide
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot+ pc", "ssd upgrade", "storage", "hardware", "ai pc", "windows 11"]
description: "Want more storage on your Copilot+ PC? Learn which models allow an SSD upgrade, which M.2 drive sizes to buy, and how to swap the drive safely at home."
thumbnail: "/images/thumbs/copilot-plus-pc-ssd-upgrade-guide.webp"
faqs:
  - q: "Can I upgrade the SSD on any Copilot+ PC?"
    a: "No. Surface Pro 11 and Surface Laptop 7 use a removable M.2 2230 SSD that owners can swap. Many Snapdragon laptops from other makers have soldered storage that cannot be upgraded. Intel and AMD AI laptops vary by model — check your service manual before buying anything."
  - q: "What size SSD fits a Surface Laptop 7 or Surface Pro 11?"
    a: "They use the compact M.2 2230 form factor, not the standard 2280 size found in most laptops. Make sure the drive you buy is labeled 2230. Gen4 drives work, but the slot runs at Gen4 speeds, so do not pay extra for Gen5."
  - q: "Will opening my Copilot+ PC void the warranty?"
    a: "Microsoft explicitly allows SSD replacement on Surface Pro 11 and Surface Laptop 7 and documents the procedure. For other brands, check the warranty terms first — some makers void the warranty if the bottom cover is removed, while others allow user-replaceable parts."
  - q: "Do I need to reinstall Windows after swapping the SSD?"
    a: "Yes, the new drive is blank. Use the Windows 11 installation media from the [official Microsoft download page](https://www.microsoft.com/en-us/software-download/windows11) on a USB stick, and the Snapdragon or Intel drivers install automatically on most models. Sign in with your Microsoft account to reactivate your digital license."
---

That 512GB drive filled up fast, and now you are wondering whether your Copilot+ PC can take a bigger SSD. The answer depends entirely on which model you bought, because the AI PC market is split between machines with user-replaceable storage and machines where everything is soldered to the board. Upgrading the wrong way can waste money — or worse, void your warranty.

The most upgrade-friendly Copilot+ PCs are the Surface Pro 11 and Surface Laptop 7, which Microsoft designed with a removable M.2 2230 SSD. On the Intel and AMD side, machines like many Lenovo, HP, and Dell AI laptops keep the classic removable 2280 SSD, though some thin models solder it. The storage question often comes up alongside memory: if you are wondering about RAM too, read our guide on whether you can [upgrade RAM on a Copilot+ PC](/articles/copilot-plus-pc-ram-upgrade-possible/).

This guide tells you which models are upgradeable, which SSD to buy, and the exact swap procedure — so you spend money once and get it right.

## Why this happens

- **Soldered storage:** Many thin AI laptops solder the flash chips directly to the motherboard, making upgrades impossible by design.
- **Uncommon M.2 2230 size:** Surface Copilot+ PCs use the short 2230 format, and buyers often order the standard 2280 by mistake.
- **Drive encryption blocks cloning:** BitLocker-encrypted drives need the recovery key before any clone or reinstall.
- **Wrong generation expectations:** Buying a Gen5 drive for a Gen4 slot wastes money with zero speed benefit.
- **Opening the wrong screws:** Some models hide screws under rubber feet or use pentalobe heads that standard kits lack.
- **Firmware-locked SSDs:** A few OEMs restrict boot drives to approved part numbers, rejecting third-party SSDs.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Confirm your model is actually upgradeable

Before buying anything, verify your exact model allows an SSD swap. Guessing wrong means a drive you cannot install — or a warranty you should not have voided.

1. Find your full model name in Settings > System > About (for example "Surface Laptop, 7th Edition").
2. Look up the official service manual or teardown guide for that model.
3. Surface Pro 11 and Surface Laptop 7: yes, removable M.2 2230. Most other Snapdragon Copilot+ PCs: no, soldered.
4. Intel/AMD AI laptops: check the manual — many Lenovo, HP, and Dell models keep a removable 2280 slot, while thin ultrabooks solder it.

### Fix 2: Buy the right drive size and generation

Copilot+ PCs are picky about form factor. The wrong physical size simply does not fit, and an over-specced generation wastes money.

1. For Surface Pro 11 / Laptop 7, buy an M.2 2230 NVMe SSD (Gen4) — double-check "2230" on the product page.
2. For standard Intel/AMD AI laptops, buy an M.2 2280 NVMe SSD matching your slot's generation (usually Gen4).
3. Stick with reputable brands (Samsung, WD, Crucial, SK hynix) and avoid no-name drives with missing firmware support.
4. If you also need more memory, read our guide on whether you can [upgrade RAM on a Copilot+ PC](/articles/copilot-plus-pc-ram-upgrade-possible/) before spending — most models cannot.

### Fix 3: Back up and get your BitLocker key

Swapping the drive wipes everything. A proper backup plus your BitLocker recovery key turns a risky operation into a routine one.

1. Save your BitLocker recovery key from your Microsoft account at account.microsoft.com/devices.
2. Back up personal files to OneDrive or an external drive.
3. Create a list of installed apps you will need to reinstall.
4. Charge the laptop above 50% and unplug it before opening anything.

### Fix 4: Create Windows 11 installation media

The new SSD is blank, so you need bootable Windows media. Microsoft's official tool is the only source you should trust.

1. On another PC, download the Media Creation Tool from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create a bootable USB drive (at least 8GB) with the tool.
3. On Snapdragon models, the installer includes ARM64 support automatically — no special ISO needed.
4. Keep the USB drive handy; you will boot from it after the physical swap.

### Fix 5: Perform the physical swap carefully

This is the delicate part. Work slowly, keep track of screws, and ground yourself to avoid static damage to the board.

1. Power off fully, disconnect the charger, and work on a clean, static-free surface.
2. Remove the bottom cover (Surface devices: remove the kickstand/feet screws per the service guide; other models: unscrew the base panel).
3. Unscrew the SSD retention screw, slide the old drive out at its angle, and insert the new drive the same way.
4. Secure the screw, replace the cover, and boot while holding the boot-menu key to select the USB installer.

### Fix 6: Install Windows and verify the drive

After the swap, install Windows, let drivers settle, and confirm the new SSD runs at full speed before you call it done.

1. Boot from the USB drive and install Windows 11 on the new SSD.
2. Sign in with your Microsoft account — the digital license reactivates automatically.
3. Run Windows Update fully; NPU, camera, and Wi-Fi drivers arrive through it on most AI laptops.
4. Verify capacity in Settings > System > Storage and run a quick speed check; your old drive can live on in a USB enclosure as backup storage.

## Closing

An SSD upgrade is one of the few meaningful hardware improvements you can still make on a Copilot+ PC — but only on models designed for it. Confirm upgradeability, buy the exact 2230 or 2280 drive your model takes, back up with your BitLocker key in hand, and reinstall Windows from official media. Do it right once, and you get years of extra breathing room from a thirty-minute job. Peripheral driver quirks are common on ARM-based AI PCs — see our [Canon printer driver guide for ARM64](/articles/canon-printer-driver-arm64-windows/) — and confirm your AI hardware with [how to check if your laptop has an NPU](/articles/check-if-laptop-has-npu/).
