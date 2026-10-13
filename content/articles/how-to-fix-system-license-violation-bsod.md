---
title: "How to Fix the System License Violation BSOD"
slug: how-to-fix-system-license-violation-bsod
date: 2026-09-24
categories: ["windows-errors"]
tags: ["system license violation", "bsod", "activation", "windows 11"]
description: "The SYSTEM_LICENSE_VIOLATION blue screen relates to Windows licensing components. Here's how to repair licensing, reactivate, and rule out deeper causes."
thumbnail: "/images/thumbs/how-to-fix-system-license-violation-bsod.webp"
faqs:
  - q: "What causes the System License Violation blue screen?"
    a: "Windows' licensing components detected an inconsistency — usually after a major hardware change (especially motherboard), a corrupted licensing store, or a failed update touching licensing files. Stop code 0x0000009A. It's rarely about piracy; it's almost always a corrupted license store or a hardware change Windows hasn't reconciled."
  - q: "Will this error delete my files or deactivate Windows?"
    a: "No to both. The blue screen is a protective stop, not a wipe, and fixing the licensing store doesn't touch personal files. As for activation: repairing licensing typically restores your existing activation. Only a motherboard replacement on an OEM license genuinely requires a new key — everything else reactivates with your existing digital license."
  - q: "I changed my motherboard and now get this error. What do I do?"
    a: "Link your digital license to your Microsoft account before the swap if possible (Settings, System, Activation). After the swap, run the Activation troubleshooter and select 'I changed hardware on this device recently.' Retail licenses transfer; OEM licenses technically don't — you may need a new key for OEM boards."
  - q: "Can a Windows update cause this?"
    a: "Yes. Updates that touch the Software Protection Platform or licensing files can corrupt the store if interrupted. If the error started right after an update, rolling it back from recovery often resolves it immediately — then repair the licensing store with the commands in Fix 3 before allowing the update again."
---

SYSTEM_LICENSE_VIOLATION (stop code 0x0000009A) is one of the more alarming-looking blue screens, because the word "violation" suggests you've done something wrong. You almost certainly haven't. This error means Windows' licensing subsystem — the Software Protection Platform that validates your activation — hit an inconsistency it couldn't resolve. The triggers are mundane: a corrupted licensing store, a major hardware change (motherboard swaps are the classic), or an update that damaged licensing files.

The fix path is correspondingly mundane: repair the licensing store, revalidate activation, and address whatever corrupted it. Your files are never at risk from these repairs. One important distinction upfront: if this started immediately after a motherboard replacement, skip to Fix 5 — that's a licensing-transfer situation, not a corruption situation. For the update-triggered variant, see our [post-update license violation guide](/articles/how-to-fix-system-license-violation-bsod-after-windows-11-update/); for general blue screen methodology, see our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Why this happens

- **Corrupt licensing store**: The tokens.dat and related files damaged by disk errors or interrupted updates.
- **Major hardware change**: Motherboard (or multiple component) swaps invalidating the hardware-bound activation.
- **Failed Windows update**: Updates touching the Software Protection Platform leaving it inconsistent.
- **Corrupt system files**: Damaged licensing components (sppsvc and friends) failing validation.
- **Disk errors**: Bad sectors landing on licensing store files.
- **Third-party "activators"**: Piracy tools and KMS hacks that break the licensing subsystem — then break Windows.
- **BIOS/UEFI changes**: Firmware updates altering the hardware hash Windows uses for activation binding.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Boot into Safe Mode and assess

Determine whether the system is otherwise healthy.

1. Boot into Safe Mode (interrupt boot three times → **Troubleshoot** > **Advanced options** > **Startup Settings** > **4**).
2. If Safe Mode is stable, the core OS is fine and this is a licensing-store problem — continue with the fixes below.
3. Open **Settings** > **System** > **Activation** and note the current activation state and error code, if any.
4. If you recently changed hardware, note exactly what — motherboard changes go to Fix 5; everything else continues here.

### Fix 2: Roll back the triggering update

If timing implicates an update, reverse it first.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the most recent quality update.
2. If Windows won't boot normally, do this from recovery: **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
3. Check [Microsoft's support pages](https://support.microsoft.com/en-us/windows) for known licensing issues with that KB.
4. Retest — if the blue screens stop, the update damaged the licensing store; proceed to Fix 3 to repair it properly before reinstalling the update.

### Fix 3: Rebuild the licensing store

The core repair for store corruption.

1. Open **Terminal (Admin)** or an elevated Command Prompt.
2. Stop the Software Protection service: `net stop sppsvc`
3. Navigate to the store: `cd %windir%\System32\spp\store\2.0` (the version folder number may differ — use `dir` to check).
4. Rename the corrupt token file: `ren tokens.dat tokens.old`
5. Restart the service: `net start sppsvc` — Windows rebuilds the store automatically.
6. Then re-register licensing components: `slmgr /rilc` (re-installs licenses). Restart and check **Settings** > **System** > **Activation**.

### Fix 4: Repair system files and revalidate

Fix the components around the store.

1. Run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal.
2. Run the Activation troubleshooter: **Settings** > **System** > **Activation** > **Troubleshoot** — it resolves common post-repair activation states automatically.
3. If you have your product key, try `slmgr /ipk YOUR-KEY` followed by `slmgr /ato` to install and activate it manually.
4. Run `chkdsk C: /f` to rule out disk errors as the corruption source — recurring store corruption means the disk is suspect.

### Fix 5: Handle the post-hardware-change case

Motherboard swaps need license transfer, not just repair.

1. If you linked your digital license to your Microsoft account before the change: **Settings** > **System** > **Activation** > **Troubleshoot** > **I changed hardware on this device recently** > select your device from the list.
2. If you didn't link it beforehand, linking now won't retroactively help — but signing in with the Microsoft account that holds the digital license sometimes still resolves it via the troubleshooter.
3. Retail licenses transfer between motherboards; OEM licenses (preinstalled) are bound to the original board — a new board legitimately needs a new key.
4. Never use KMS activators or "license repair" tools from unofficial sources — they cause this exact blue screen and often bundle malware.

### Fix 6: Clean up licensing-related software conflicts

Remove interference with the protection platform.

1. Uninstall any third-party "Windows activator," KMS tool, or license-management utility — these directly corrupt the store.
2. Temporarily disable third-party antivirus during the repair (use the vendor's removal tool for a clean test), then re-enable — overzealous security software occasionally quarantines licensing files.
3. Check **Services** (`services.msc`) that **Software Protection** is set to **Automatic (Delayed Start)** and running.
4. Restart and verify both stability (no more blue screens) and activation state.

### Fix 7: In-place upgrade repair as the last resort

When the licensing subsystem is damaged beyond targeted repair.

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it (or create USB media).
2. Run `setup.exe` from inside Windows and choose **Upgrade** — keep files and apps. This reinstalls Windows' system files, including the entire licensing stack, without touching your data.
3. After the upgrade, run the Activation troubleshooter once more.
4. If blue screens persist after an in-place upgrade, suspect hardware (disk/RAM corrupting the store repeatedly) — run full diagnostics before anything else.

## Closing

SYSTEM_LICENSE_VIOLATION sounds like an accusation but it's really a corruption report: the licensing store or its components got damaged, usually by an update, a disk error, or a hardware change. Rebuilding the store (Fix 3) resolves the corruption cases; the hardware-change path (Fix 5) resolves the transfer cases. The one thing never to do is reach for unofficial "activators" — they cause this exact crash and trade a fixable problem for malware. Repair the store, revalidate, and confirm the disk isn't re-corrupting it, and this blue screen stays in the past. For the variant tied specifically to updates, our [post-update guide](/articles/how-to-fix-system-license-violation-bsod-after-windows-11-update/) has the targeted sequence.
