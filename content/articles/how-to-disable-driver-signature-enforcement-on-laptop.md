---
title: "How to Disable Driver Signature Enforcement on a Laptop (Safely)"
slug: how-to-disable-driver-signature-enforcement-on-laptop
date: 2026-10-03
categories: ["windows-errors"]
tags: ["driver signature", "unsigned drivers", "windows 11", "secure boot", "device manager"]
description: "Need to install an unsigned driver? Here's how to disable driver signature enforcement on a laptop — temporarily and permanently — with the risks explained."
thumbnail: "/images/thumbs/how-to-disable-driver-signature-enforcement-on-laptop.webp"
faqs:
  - q: "Is it safe to disable driver signature enforcement?"
    a: "Temporarily, for installing a trusted unsigned driver, it's reasonably safe — enforcement returns on the next reboot. Permanently disabling it removes a key malware protection, so only do it if you understand the risk and keep good antivirus protection active."
  - q: "Does disabling driver signature enforcement persist after restart?"
    a: "The Startup Settings method only lasts until the next reboot. The bcdedit test-signing method persists until you turn it off. Choose based on whether you need a one-time install or ongoing use of unsigned drivers."
  - q: "Why does Windows block my driver with an unsigned error?"
    a: "Windows requires kernel-mode drivers to carry a valid digital signature proving they passed Microsoft's checks. Old hardware, hobbyist projects, and some specialized tools ship unsigned drivers, which Windows blocks to protect against rootkits."
  - q: "Can I enable it again after disabling?"
    a: "Yes, easily. For the temporary method, just restart. For the bcdedit method, run bcdedit /set testsigning off in an admin Command Prompt and reboot. Secure Boot systems may also need the setting re-enabled in BIOS."
---

Driver signature enforcement is Windows' bouncer: it refuses to load any kernel driver that isn't digitally signed, which blocks a whole class of rootkits and malicious drivers. But sometimes you genuinely need an unsigned driver — an old printer, a specialty USB device, a development board, or legacy hardware whose vendor stopped signing drivers years ago. In that case, you need to get past the bouncer.

There are two ways to do it: temporarily (lasts until reboot — the safe choice for a one-time install) and permanently via test-signing mode (persists, with a visible watermark and real security trade-offs). I'll show you both, in that order, so you can pick the one that fits.

## Why this happens

- **The driver was never signed.** Small vendors, open-source projects, and hobbyist hardware often can't afford or never pursued Microsoft's signing process.
- **An old signed driver lost its validity.** Certificates expire, and cross-signing rules changed — a driver signed years ago may no longer pass current checks.
- **You're installing modified drivers.** Tweaked GPU drivers or patched system drivers lose their valid signature the moment they're altered.
- **Test or development drivers.** If you're developing hardware or drivers yourself, your test builds are unsigned by definition.
- **Secure Boot is enforcing the policy.** On most modern laptops, Secure Boot plus signature enforcement forms a chain that blocks anything Microsoft hasn't blessed.
- **Windows is in its default secure configuration.** Enforcement is on by default in Windows 10 and 11, and there's no normal Settings toggle — it's intentionally a multi-step process.

## How to fix it

Work through these in order — start with Fix 1 and stop once your driver installs.

### Fix 1: Disable enforcement temporarily via Startup Settings

The safest method — enforcement comes back automatically on the next reboot.

1. Open **Settings > System > Recovery**.
2. Under **Advanced startup**, click **Restart now** and confirm.
3. When the blue menu appears, choose **Troubleshoot > Advanced options > Startup Settings**, then click **Restart**.
4. After rebooting, press **7** (or **F7**) for **Disable driver signature enforcement**.
5. Windows starts normally — install your unsigned driver now.
6. Restart once more to re-enable enforcement.

Do all your driver installation in this one session. The moment you reboot, protection is back, which is exactly what you want. If you're troubleshooting driver-related blue screens rather than installing hardware, our [DRIVER_IRQL_NOT_LESS_OR_EQUAL guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/) covers the repair side.

### Fix 2: Enable test-signing mode for persistent use

For drivers you need every day (like a development setup), use test-signing mode.

1. Right-click **Start** and open **Terminal (Admin)**.
2. Run `bcdedit /set testsigning on`.
3. You should see "The operation completed successfully."
4. Restart the laptop.
5. You'll see a **Test Mode** watermark in the bottom-right corner of the desktop — that's normal and confirms it's active.
6. Install your unsigned drivers; they'll now load on every boot.

The watermark is your reminder that protection is reduced. To turn it off later, run `bcdedit /set testsigning off` as admin and reboot. If Windows refuses the bcdedit command, Secure Boot is likely blocking it — see Fix 3.

### Fix 3: Disable Secure Boot in BIOS (if bcdedit is blocked)

Some laptops won't accept test-signing changes while Secure Boot is on.

1. Restart and enter the BIOS/UEFI (usually **F2**, **Del**, or **F12** at the logo screen — varies by brand).
2. Find the **Security** or **Boot** tab and locate **Secure Boot**.
3. Change it from **Enabled** to **Disabled**.
4. Save and exit (**F10** on most systems).
5. Boot into Windows and retry the `bcdedit /set testsigning on` command.

Warning: disabling Secure Boot weakens boot-level protection against bootkits. Re-enable it when you no longer need unsigned drivers. On some corporate or school laptops, the BIOS is password-locked — you'll need the administrator to make this change. Microsoft documents Secure Boot behavior on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 4: Sign the driver yourself (advanced, best long-term fix)

If you have the driver source or the .sys/.cat files, self-signing is cleaner than disabling protection.

1. Install the **Windows SDK** and **Windows Driver Kit (WDK)** on a development machine.
2. Create a test certificate with `MakeCert` or the WDK's tools.
3. Sign the driver package with `SignTool sign` using your test certificate.
4. Install your test certificate into the machine's **Trusted Root** and **Trusted Publishers** stores.
5. Enable test-signing mode (Fix 2) — self-signed drivers still need it, but now only your signed drivers load, not any random unsigned code.

This is the approach driver developers actually use. It's more work up front, but it keeps the "only my code loads" property instead of opening the door to everything.

### Fix 5: Use the "install anyway" path for user-mode software

Not everything that complains about signatures is a kernel driver.

1. Read the exact error message — if it mentions a **.sys** file or "driver," it's kernel-mode and needs the fixes above.
2. If it's an application installer warning about an **unknown publisher**, that's SmartScreen, not signature enforcement: click **More info > Run anyway**.
3. Check whether the vendor offers a newer signed version — many "unsigned driver" problems are just outdated downloads.
4. For old printers and scanners, try Windows' built-in drivers first: **Settings > Bluetooth & devices > Printers & scanners > Add device** often finds a working inbox driver.

### Fix 6: Re-enable everything when you're done

Don't leave the door open longer than necessary.

1. Uninstall any test drivers you no longer need via **Device Manager**.
2. Run `bcdedit /set testsigning off` in an admin Terminal and reboot.
3. Confirm the **Test Mode** watermark is gone.
4. Re-enable **Secure Boot** in the BIOS if you disabled it.
5. Run a full scan with **Windows Security** to make sure nothing unwanted loaded during the unprotected window.

If you disabled enforcement to troubleshoot crashes and the crashes persist, the driver probably wasn't the issue — see our guide on [disabling automatic restart after a blue screen](/articles/how-to-disable-automatic-restart-after-bsod-on-windows-11/) so you can capture the real stop code.

## Closing

Disabling driver signature enforcement is a legitimate tool, not a hack — Microsoft built these exact paths for developers and legacy hardware. Just respect the hierarchy: temporary disable for a one-time install, test-signing for ongoing development use, and always re-enable protection when you're done. The watermark in the corner is there to remind you the bouncer is off duty — don't ignore it forever.
