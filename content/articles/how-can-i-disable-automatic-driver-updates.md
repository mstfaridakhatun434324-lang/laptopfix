---
title: "How to Disable Automatic Driver Updates in Windows 11/10 (3 Reliable Ways)"
slug: how-can-i-disable-automatic-driver-updates
date: 2026-09-17
categories: ["drivers"]
tags: ["automatic driver updates", "windows update", "device installation settings", "group policy", "driver rollback"]
description: "Windows keeps overwriting your stable drivers with buggy new ones? Three reliable methods to disable automatic driver updates on Windows 11 and 10 — while keeping security patches flowing."
thumbnail: "/images/thumbs/how-can-i-disable-automatic-driver-updates.webp"
faqs:
  - q: "Will disabling automatic driver updates stop security updates?"
    a: "No. The methods in this guide only stop Windows Update from delivering hardware driver packages. Security patches, feature updates, .NET updates, and Defender definition updates continue normally. You keep the protection and stay in control of which driver versions run on your hardware."
  - q: "Can I block updates for just one device instead of all drivers?"
    a: "Yes, and it's often the better option. In Device Manager, note the device's hardware IDs, then use Group Policy (Device Installation Restrictions) to block installation for those exact IDs. Your GPU or Wi-Fi adapter stays pinned to a known-good version while other devices update normally."
  - q: "Do I still get driver updates if I disable automatic driver installation?"
    a: "Windows Update won't install them automatically, but nothing stops you from updating manually. Download the latest package from your laptop maker's support page and run the installer yourself. Manual installation always overrides the block, so you can test new drivers on your own schedule."
  - q: "Does this setting survive a Windows feature update?"
    a: "Usually, but not guaranteed. Major feature updates sometimes reset the Device Installation Settings option back to Yes. The Group Policy method is more persistent, though upgrades can occasionally alter policies too. It's worth re-checking your setting after each annual feature update."
---

Nothing erodes trust in Windows Update like a perfectly stable laptop suddenly misbehaving after an overnight reboot. One morning your display flickers, your Wi-Fi drops every few minutes, or your audio crackles — and the culprit is a driver Windows quietly replaced with a newer, buggier version. Automatic driver updates are well-intentioned: they keep hardware running on fresh code. But "fresh" doesn't mean "tested on your exact machine," and vendor drivers that were stable for months can be displaced by generic Microsoft-distributed versions.

Disabling automatic driver updates isn't about rejecting updates wholesale. It's about separating two different jobs: security patching (which you absolutely want) and driver management (which you may want to handle yourself, on your schedule). Below are three methods ranked by reliability, from the built-in setting most people should use to the Group Policy approach for maximum control. If a bad driver already landed and you need damage control, our [missing drivers troubleshooting guide](/articles/how-to-find-missing-drivers-on-windows-11/) covers recovery first.

## Why this happens

- **Windows treats drivers like any other update.** By default, Windows Update delivers hardware drivers alongside security patches, and installs them with no separate approval step.
- **The "best" driver is chosen by ranking, not by your experience.** Windows picks the highest-ranked driver package, which may be newer but not necessarily better on your specific laptop hardware.
- **Vendor customizations get replaced by generic drivers.** A laptop maker's tuned audio or power-management driver can be overwritten by a generic version that lacks those customizations.
- **Rollback windows are time-limited.** You can roll back a bad driver — but only within days, and only if Windows hasn't already overwritten it again.
- **Feature updates reset your preferences.** Annual Windows upgrades occasionally restore automatic driver installation to its default state without asking.
- **Optional updates quietly become automatic.** What was an "optional" driver in one month can be reclassified and installed automatically later.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use Device Installation Settings (easiest, all editions)

This is the built-in toggle most users should start with. It tells Windows not to download manufacturer apps and custom icons — and, critically, not to fetch drivers from Windows Update.

1. Press **Win + S**, type `change device installation settings`, and open the result.
2. Select **No (your device might not work as expected)** and click **Save Changes**.
3. Restart the laptop to make sure the policy applies to pending updates.
4. To verify: open **Settings > Windows Update > Advanced options** and confirm no driver updates are offered on the next scan.

The wording of the prompt is deliberately scary — "your device might not work as expected" — but on a laptop whose drivers you manage yourself, the effect is simply that Windows Update stops pushing driver packages. Everything else updates normally. The downside: as noted above, feature updates can flip this back, so check it after each upgrade.

### Fix 2: Block driver updates via Group Policy (Windows 11/10 Pro)

The Group Policy method is more surgical: it blocks driver installation through Windows Update while leaving every other update category untouched. It also survives better than the Fix 1 toggle.

1. Press **Win + R**, type `gpedit.msc`, and press Enter.
2. Navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update**.
3. Double-click **Do not include drivers with Windows Updates**, set it to **Enabled**, and click OK.
4. Open an elevated Command Prompt and run `gpupdate /force` to apply it immediately.
5. Restart and confirm no drivers appear under **Settings > Windows Update > Optional updates**.

This is the method most technicians recommend for Windows Pro users because it is explicit, documented, and persistent. It doesn't block manual driver installation in any way — you're free to install newer drivers from [Microsoft's support pages](https://support.microsoft.com/en-us/windows) or your vendor whenever you choose.

### Fix 3: Registry edit for Windows Home users

Windows Home has no Group Policy editor, but the same setting exists as a registry value. This achieves exactly what Fix 2 does.

1. Press **Win + R**, type `regedit`, and approve the UAC prompt.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`.
3. If the **WindowsUpdate** key doesn't exist, right-click **Windows** and create it.
4. Inside it, create a new **DWORD (32-bit) Value** named `ExcludeWUDriversInQualityUpdate`.
5. Set its value to `1` and restart the laptop.

Back up the registry key first (File > Export) so you can undo the change. A value of `1` excludes drivers from quality updates; deleting the value or setting it to `0` restores default behavior. This registry setting is respected by the same Windows Update engine as the policy, so it behaves identically on Home editions.

### Fix 4: Pin a single device with hardware-ID restrictions

Sometimes you only want to freeze one device — usually the GPU or Wi-Fi adapter — while letting everything else update. Device Installation Restrictions handle this precisely.

1. Open **Device Manager**, right-click the device, choose **Properties > Details**, and select **Hardware Ids** from the dropdown.
2. Copy the top hardware ID (the most specific one).
3. In **gpedit.msc**, go to **Computer Configuration > Administrative Templates > System > Device Installation > Device Installation Restrictions**.
4. Enable **Prevent installation of devices that match any of these device IDs** and paste your hardware ID into the list.
5. Run `gpupdate /force` and restart.

With this in place, Windows will never replace that device's driver — even via a manual driver install from Device Manager's "update" wizard, so remove the restriction first if you later decide to upgrade that driver yourself. This pairs well with a [clean NVIDIA driver install](/articles/how-to-update-nvidia-drivers-clean-install/) that you perform manually.

### Fix 5: Roll back the bad driver that already landed

If you're doing this because a bad driver already installed, block it first, then roll it back before the evidence disappears.

1. Open **Device Manager**, right-click the affected device, and choose **Properties > Driver**.
2. Click **Roll Back Driver**, pick a reason, and confirm.
3. Immediately apply Fix 1 or Fix 2 so Windows doesn't reinstall the same version tonight.
4. If rollback is grayed out, the driver store no longer has the old version — download the previous release from your vendor's support page (e.g. [Dell's support site](https://www.dell.com/support)) and install it manually with the block already in place.

### Fix 6: Hide the specific update with the troubleshooter package

For one bad driver that keeps coming back despite the blocks, Microsoft's "Show or hide updates" troubleshooter can hide that specific update package so it's never offered again.

1. Download the **wushowhide** troubleshooter package from Microsoft's support channels.
2. Run it, choose **Hide updates**, and select the offending driver package.
3. Confirm it disappears from the available-updates list on the next Windows Update scan.

This is a targeted fix rather than a global policy, which makes it ideal when everything updates fine except one stubborn driver. Keep the tool handy: it's also useful to re-hide a package if a feature update re-offers it.

### Fix 7: Re-enable cleanly when you're ready

Blocking drivers is a stance, not a permanent rule. When a vendor releases a driver that fixes something you care about, you should take it — on your terms.

1. Download the new driver directly from your laptop maker or the component vendor's official page.
2. Install it manually with the blocks still in place — manual installs always work.
3. Test for a week before declaring it stable; keep the previous installer archived locally.
4. If you ever want automatic drivers back, reverse whichever fix you applied (set the policy to **Not Configured**, delete the registry value, or answer **Yes** in Device Installation Settings).

## Closing

Automatic driver updates exist because most users never install drivers themselves, and an outdated driver is worse than a mediocre new one. But if you're reading this, you're not most users — you know which driver versions work on your machine. Pick Fix 1 for simplicity, Fix 2 or 3 for durability, or Fix 4 when a single device is the troublemaker. Either way, remember the pairing: block the automatic delivery, then update manually from vendor sources. You keep the stability and the security patches — the best of both worlds.
