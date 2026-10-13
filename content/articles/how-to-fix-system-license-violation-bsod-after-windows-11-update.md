---
title: "Fix SYSTEM_LICENSE_VIOLATION BSOD After a Windows 11 Update"
slug: how-to-fix-system-license-violation-bsod-after-windows-11-update
date: 2026-09-01
categories: ["windows-errors"]
tags: ["bsod", "stop code 0x9a", "activation", "windows 11 update"]
description: "Fix the rare SYSTEM_LICENSE_VIOLATION blue screen after a Windows 11 update — repair activation and licensing components safely."
thumbnail: "/images/thumbs/how-to-fix-system-license-violation-bsod-after-windows-11-update.webp"
faqs:
  - q: "What is SYSTEM_LICENSE_VIOLATION?"
    a: "Stop code 0x0000009A means Windows' software licensing components detected a violation and halted the system. After an update, this is usually licensing file corruption or a damaged Software Protection service — not actual piracy. Genuine, activated systems hit this too."
  - q: "Will Microsoft lock my PC for this?"
    a: "No. This stop code is a crash, not an enforcement action. Microsoft doesn't brick machines over licensing disagreements. Fix the corrupted licensing components with the steps below and your activated Windows keeps working normally."
  - q: "I have a genuine license — why is this happening?"
    a: "Because the error is about damaged licensing machinery, not about your key's validity. A bad update can corrupt the tokens.dat store or break the Software Protection Platform service, and Windows blue-screens when its license checks malfunction — even on fully genuine systems."
  - q: "Do I need to buy a new Windows key?"
    a: "Almost certainly not. Your existing digital license or product key is fine. The fixes rebuild the licensing store and re-verify activation against Microsoft's servers using the license you already own."
---
SYSTEM_LICENSE_VIOLATION (stop code 0x0000009A) is the blue screen that makes honest users panic: it sounds like Windows accusing you of piracy. It isn't. This crash means Windows' internal licensing machinery malfunctioned — corrupted license store files, a broken Software Protection service, or activation components damaged by the update. Genuine, properly activated systems hit this regularly after bad updates, and the fix is repairing the machinery, not buying a new key.

Because the licensing system touches the kernel, its failures are fatal to the running session — hence the blue screen instead of a polite activation warning. Work through these fixes in order; they rebuild the licensing components from the ground up.

## Why this happens

- **Corrupted licensing store (tokens.dat).** The file holding your activation tokens gets damaged during the update, and the license check crashes instead of failing gracefully.
- **Broken Software Protection Platform service.** If `sppsvc` can't start or crashes, every license verification in the system fails catastrophically.
- **Mismatched licensing files after a feature update.** Old and new licensing components mixed by a faulty update produce inconsistent state that trips the violation check.
- **KMS or volume-license client misconfiguration.** Corporate or school laptops that can't reach their KMS server after a network/driver change can fall into this state.
- **Disk corruption in the licensing directories.** Bad sectors landing on `C:\Windows\System32\spp` files corrupt exactly the wrong bytes.
- **Third-party "activators" or license tools.** Crack tools patch the same licensing components; an update that replaces their patches with genuine files creates a Frankenstein state that crashes.

## How to fix it

Work through these in order. Fixes 1–3 resolve the overwhelming majority of cases.

### Fix 1: Rebuild the licensing store

The core fix: throw away the corrupted token store and let Windows rebuild it.

1. Boot into Safe Mode (interrupt boot three times > **Automatic Repair** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **4**).
2. Open **Terminal (Admin)** and stop the service: `net stop sppsvc`.
3. Rename the corrupted store: `ren C:\Windows\System32\spp\store\2.0\tokens.dat tokens.old`. (If the path differs slightly on your build, look under `C:\Windows\System32\spp\store\` for the version folder.)
4. Restart the service: `net start sppsvc`, then force reactivation: `slmgr /ato`.
5. Reboot normally. Windows rebuilds the store and reactivates against Microsoft's servers using your existing digital license.

### Fix 2: Re-register the licensing components

If the store rebuild didn't finish the job, re-register the DLLs the licensing system depends on.

1. In **Terminal (Admin)**, run these commands one at a time:
   `regsvr32 /s licmgr10.dll`
   `regsvr32 /s licwmi.dll`
2. Then reset the licensing status completely: `slmgr /rearm` and reboot when prompted.
3. After reboot, check activation: **Settings** > **System** > **Activation**. It should show **Active** with a digital license.
4. If activation shows an error code, use the **Troubleshoot** button on that same page — it resolves most post-rebuild activation hiccups automatically. Microsoft documents the activation flow on [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 3: Repair system files and the component store

Licensing components are system files; repair them like any other.

1. In **Terminal (Admin)**, run `sfc /scannow` and wait for completion.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow` once more, then reboot.
4. SFC specifically restores damaged `spp` service files from the component store, which is often the actual root cause behind the corrupted store in Fix 1.

### Fix 4: Check the disk underneath the licensing files

If the store keeps corrupting, suspect the storage.

1. In **Terminal (Admin)**, run `chkdsk C: /f /r`, type **Y**, and reboot to let the full scan run.
2. If chkdsk repairs sectors under `C:\Windows\System32\spp`, back up your data — recurring corruption in the same area suggests a failing SSD.
3. Also check drive health with your manufacturer's tool (Samsung Magician, WD Dashboard, Crucial Storage Executive) for reallocated sector counts.

### Fix 5: Uninstall the update that broke it

When the timeline is unmistakable, remove the trigger.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the update matching the crash timeline, reboot, and verify stability for a day.
3. Rebuild the licensing store again (Fix 1) after uninstalling, since the bad update may have corrupted it on the way out too.
4. If the update refuses to uninstall, [roll the system back with System Restore](/articles/how-to-use-system-restore-on-windows-11/) to a point before the update instead — it reverses the same changes.

### Fix 6: Fix KMS client issues on work or school laptops

If this is a managed device, the violation may be a KMS communication failure.

1. In **Terminal (Admin)**, check status: `slmgr /dlv`. Look at the **KMS machine name** and activation interval.
2. If you're off the corporate network, connect via VPN and run `slmgr /ato` to reactivate.
3. If the KMS server changed, your IT department needs to set it: `slmgr /skms <server-name>` — but only do this on IT's instruction, never from internet advice.
4. Don't attempt KMS fixes on a personal retail/OEM license — they don't apply and will confuse activation further.

### Fix 7: Remove piracy tools and repair the damage

If any "activator," KMS emulator, or license patcher was ever run on this machine, say so honestly — it matters.

1. Uninstall the tool and reboot into Safe Mode.
2. Run Fixes 1–3 in sequence: rebuild the store, re-register components, run SFC/DISM. The tool's patches must be fully replaced with genuine files.
3. Enter your genuine product key: **Settings** > **System** > **Activation** > **Change product key**.
4. Run `slmgr /ato` and confirm **Active** status. Genuine activation after cleanup is stable; leftover patch fragments are what keep crashing.

### Fix 8: Link the digital license to your Microsoft account

Prevent recurrence by tying activation to your account rather than hardware alone.

1. Go to **Settings** > **System** > **Activation**. If it shows **Windows is activated with a digital license**, click **Add an account** under **Add a Microsoft account** and sign in.
2. The status should change to **Windows is activated with a digital license linked to your Microsoft account**.
3. This makes future reactivations — after hardware changes or repairs — a matter of running the Activation Troubleshooter while signed in, instead of rebuilding the licensing store from scratch.
4. Verify once more with `slmgr /dlv` in Terminal: **License Status** should read **Licensed**.

## Closing

SYSTEM_LICENSE_VIOLATION is a repair job, not a purchasing decision. The licensing store rebuild in Fix 1 resolves most post-update cases in ten minutes, and the re-registration and SFC passes clean up the rest. Your genuine license was never the problem — the machinery that checks it was. Once rebuilt and reactivated, this particular blue screen doesn't come back, because there's nothing left in the corrupted state that caused it. And if a future update misbehaves similarly, the [update error code guide](/articles/error-code-0x80070057-fix/) covers the same corrupted-cache repair techniques from the update side.
