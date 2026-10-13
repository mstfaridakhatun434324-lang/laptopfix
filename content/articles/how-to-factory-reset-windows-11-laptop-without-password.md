---
title: "How to Factory Reset a Windows 11 Laptop Without the Password"
slug: how-to-factory-reset-windows-11-laptop-without-password
date: 2026-09-10
categories: ["windows-errors"]
tags: ["factory reset", "windows 11", "locked out"]
description: "Locked out of your Windows 11 laptop? Reset it without the password using the sign-in screen, recovery environment, or installation media."
thumbnail: "/images/thumbs/how-to-factory-reset-windows-11-laptop-without-password.webp"
faqs:
  - q: "Can I factory reset Windows 11 without knowing the password?"
    a: "Yes. From the sign-in screen, hold Shift while clicking the power icon, then Restart to enter the Windows Recovery Environment. Choose Troubleshoot, then Reset this PC, and follow the prompts — no password is required for the reset itself. Note this erases your personal files unless you choose the keep-files option (which still requires signing in afterward)."
  - q: "Will resetting without a password remove the Microsoft account lock?"
    a: "No — and this is important. A factory reset does not remove Activation Lock-style protections or a firmware password. After resetting, Windows will still ask for the Microsoft account previously linked to the device in some configurations. If you are the legitimate owner and forgot the password, reset the Microsoft account password online instead."
  - q: "Does 'Reset this PC' delete everything?"
    a: "You get two choices: 'Keep my files' (removes apps and settings, keeps personal files) and 'Remove everything' (wipes the drive). Without the password you can generally only complete 'Remove everything' from the recovery environment. Either way, installed programs are always removed. Back up anything important first if you can access the drive."
  - q: "What if 'Reset this PC' fails or the option is missing?"
    a: "Use Windows 11 installation media instead: create a bootable USB on another PC, boot from it, and choose Install now, then the repair/reset options — or do a clean install, which achieves the same wiped state. Corrupted recovery partitions are the usual reason the built-in reset fails, and installation media bypasses them entirely."
---

Being locked out of your own laptop is miserable — and before anyone asks, this guide is for legitimate owners who forgot a password or inherited a machine from a family member. A factory reset without the password is a built-in Windows recovery path, not a hack: Microsoft designed the recovery environment to be reachable from the sign-in screen precisely for this situation.

Work through the methods in order. The first one needs nothing but the laptop itself. If your problem is not a forgotten password but a system that will not boot properly, [booting into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) first may let you fix things without wiping anything.

## Why This Happens

- **Forgotten local account password.** No password reset disk was ever created, and security questions were skipped or forgotten.
- **Secondhand or family laptop.** Previous owner's account is still on the machine with no password provided.
- **Microsoft account confusion.** The laptop expects a Microsoft account password, but the owner only remembers an old local password (or vice versa).
- **Corrupted user profile.** Sometimes the password is correct but the profile will not load — a reset is the pragmatic fix.
- **PIN vs password mismatch.** Windows Hello PINs stop working after certain hardware changes, and the fallback password is long forgotten.
- **Recovery partition intact but unused.** Most people do not know the recovery environment is one Shift+Restart away.

## How to Fix It

Work through these in order. Method 1 works for most people with no extra tools.

### Fix 1: Reset From the Sign-In Screen (No Tools Needed)

Windows Recovery is reachable without signing in. This is the intended path.

1. On the Windows 11 sign-in screen, click the **power icon** in the bottom-right corner.
2. Hold **Shift** on the keyboard and click **Restart**. Keep holding Shift until the blue recovery screen appears.
3. Choose **Troubleshoot** > **Reset this PC**.
4. Select **Remove everything** (the reliable choice from outside Windows; "Keep my files" may demand credentials you do not have).
5. Choose **Cloud download** if you have internet (fresher Windows image) or **Local reinstall** if not.
6. Confirm and let it run — 30 minutes to a few hours depending on the drive. The laptop restarts several times; do not interrupt it.

### Fix 2: Reset From the Recovery Environment via Forced Boot

If Shift+Restart does not work, force Windows into recovery the hard way.

1. Power the laptop on. As soon as the Windows logo or spinning dots appear, hold the power button to force it off.
2. Repeat this **two more times** (three interrupted boots total).
3. On the fourth boot, Windows enters **Automatic Repair** and then the recovery environment on its own.
4. Choose **Advanced options** > **Troubleshoot** > **Reset this PC**.
5. Follow the same choices as Fix 1: **Remove everything**, then Cloud or Local reinstall.
6. If Automatic Repair loops instead of offering reset options, the recovery partition may be damaged — move to Fix 4 (installation media).

### Fix 3: Try Account Recovery Before Wiping

Wiping is permanent. If there is any chance of recovering access, take ten minutes to try.

1. On another device, go to Microsoft's account recovery page and attempt to reset the **Microsoft account** password — many "forgotten laptop passwords" are actually forgotten Microsoft account passwords.
2. Check whether the laptop even uses a Microsoft account: the sign-in screen shows an email address under the name if so.
3. For local accounts, check for a password hint on the sign-in screen, and ask anyone who may have set up the machine.
4. Look for a previously created password reset USB — long shot, but check drawers.
5. If the data on the drive matters and you cannot sign in, consider removing the drive and copying files via another PC (or a live Linux USB) *before* resetting.
6. Only proceed to wiping when you have accepted the data loss or secured the files. There is no undo after "Remove everything."

### Fix 4: Clean Install From USB Installation Media

When the built-in reset fails or the recovery partition is gone, installation media does the job.

1. On a working computer, download the Windows 11 Media Creation Tool from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) and create a bootable USB (8GB+).
2. Plug the USB into the locked laptop and boot from it: power on while tapping **F12**, **F9**, **Esc**, or **F2** (varies by brand) to open the boot menu, then select the USB drive.
3. Choose your language, click **Install now**, and enter the product key if asked (most laptops have it embedded in firmware — choose "I don't have a product key" and Windows activates automatically).
4. Choose **Custom: Install Windows only**, delete the old partitions if you want a truly clean slate, and install to the unallocated space.
5. Complete setup with a new account. Install drivers from your manufacturer's support site afterward.
6. This method also fixes the corrupted-recovery-partition problem permanently, since you are not depending on it anymore.

### Fix 5: Handle Post-Reset Account and Activation Locks

The reset wipes Windows, but some locks survive. Know what to expect.

1. After reset, Windows setup may ask for the **previously linked Microsoft account** (device protection on some configurations). Have those credentials ready — or recover them via Microsoft account recovery.
2. Check activation: **Settings** > **System** > **Activation**. Digital licenses tied to the motherboard reactivate automatically once online.
3. If a **BIOS/firmware password** blocks booting or settings changes, a Windows reset cannot remove it — that requires the password or manufacturer assistance with proof of ownership.
4. Reinstall essential drivers first: chipset, graphics, Wi-Fi, then Windows Update for the rest. Manufacturer support pages have the correct packages.
5. Set up a password reset USB *now* (**Control Panel** > **User Accounts** > **Create a password reset disk**) so this never happens again — or better, link a Microsoft account and store its credentials safely.
6. Microsoft documents the full reset process on the [Windows support site](https://support.microsoft.com/en-us/windows) if you want the official reference with screenshots.

### Fix 6: Back Up Your Files From the Recovery Environment First

"Remove everything" is permanent. If the drive holds anything irreplaceable, rescue it before resetting — no password needed.

1. From the sign-in screen, Shift + Restart into the recovery environment (Fix 1, steps 1-2).
2. Choose **Troubleshoot** > **Advanced options** > **Command Prompt**. The laptop restarts into a command line running as SYSTEM — full access, no password.
3. Type `notepad.exe` and press Enter. In Notepad, go to **File** > **Open**. This opens a graphical file browser with full drive access.
4. Plug in a USB drive. In the file browser, navigate to **This PC** > your Windows drive (note: the letter may be D: or E: here, not C:) > **Users** > your username.
5. Copy Documents, Pictures, Desktop, and any other important folders to the USB drive via right-click > **Send to** or copy-paste.
6. Verify the copies on another computer if possible. If repeated [blue screens](/articles/how-to-fix-blue-screen-of-death-windows-11/) are part of why you are resetting, back up first — crash-damaged systems are the ones most likely to lose data mid-reset. Only then proceed with "Remove everything."

## Closing

A forgotten password feels like losing the laptop, but the recovery environment exists for exactly this moment — Shift+Restart, Troubleshoot, Reset this PC. The real lesson comes after: set up account recovery options, make that password reset USB, and write the password down somewhere safe. Future-you, staring at a sign-in screen at midnight, will be grateful.
