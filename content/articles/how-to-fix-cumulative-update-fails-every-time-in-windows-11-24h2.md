---
title: "Fix a Cumulative Update That Fails Every Time on Windows 11 24H2"
slug: how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2
date: 2026-09-20
categories: ["windows-update"]
tags: ["cumulative update fails", "every time", "windows 11 24h2", "repeat failure"]
description: "Cumulative update failing every single time on Windows 11 24H2? Break the repeat-failure cycle with this deep repair sequence."
thumbnail: "/images/thumbs/how-to-fix-cumulative-update-fails-every-time-in-windows-11-24h2.webp"
faqs:
  - q: "Why does the same cumulative update fail every time?"
    a: "Repeat identical failures mean a deterministic blocker: the same corrupt cache, the same damaged store entry, or the same conflicting driver meets the same installer every attempt. Retrying without changing the conditions reproduces the failure by design. The repeatability is actually helpful — it rules out transient causes and points at a persistent blocker."
  - q: "How many times should I retry before doing deep repairs?"
    a: "Twice. If two attempts fail with the same code at the same stage, stop retrying and start the repair sequence. Further blind retries only cost time and risk compounding the problem. Two failures with the same code is the threshold where diagnosis replaces hope as the strategy."
  - q: "Will the next month's cumulative update fix it automatically?"
    a: "Sometimes — if the blocker was specific to that month's payload. But store corruption, bad caches, and driver conflicts persist across months, so a machine failing in October usually fails in November too. Fix the underlying cause rather than waiting. A month of waiting costs the same effort as an hour of proper repair, with worse odds."
  - q: "Is a clean install the answer for repeat failures?"
    a: "Almost never needed. The in-place upgrade repair (keeping files and apps) resolves even stubborn repeat failures by rebuilding the servicing environment. Reserve clean installs for machines with additional serious problems. The in-place repair keeps your files, apps, and settings while rebuilding the servicing environment underneath them."
---

A cumulative update that fails once is an annoyance; one that fails every time — same code, same percentage, month after month — is a system telling you something is structurally wrong. The repeatability is actually useful information: it rules out transient causes (server load, cosmic rays) and points squarely at a persistent blocker in your machine.

Breaking the cycle requires changing the conditions, not the attempt count. The sequence below escalates deliberately: cache, store, blockers, manual install, servicing stack, and finally the in-place repair that rebuilds the whole update environment. Each step eliminates a class of persistent cause.

If your cumulative update fails intermittently rather than every time, start with the [single-failure install guide](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) — the diagnostics differ when the failure is not deterministic.

## Why this happens

- **Permanently corrupt cache:** A damaged payload that survives reboots because the cache is never cleared between attempts.
- **Component store damage:** WinSxS corruption that every month's installer trips over identically.
- **Stale servicing stack:** An SSU that never installed properly, blocking every cumulative update behind it the same way.
- **Persistent driver conflict:** The same incompatible driver aborting each month's install at the same phase.
- **Third-party software hook:** An antivirus or system utility interfering with every install identically.
- **Failing storage:** Bad sectors corrupting each staged payload in the same way, producing eerily identical failures.
- **Policy or registry damage:** Broken update policies forcing the same misconfiguration on every attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Document the exact repeat pattern

Precision turns 'it always fails' into actionable data.

1. Record the KB number, error code, and failure percentage from Update history.
2. Confirm it is truly identical each time: same code, same stage.
3. Check whether other updates install fine — if only this KB fails, the payload may be the problem; if all fail, the environment is.
4. This record tells you which later step to emphasize.

### Fix 2: Nuke the cache completely

The standard cache reset, done thoroughly — including the download subfolder and DataStore.

1. Elevated prompt: stop wuauserv, cryptSvc, bits, msiserver.
2. Rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old` (do not just empty it).
3. Rename `C:\Windows\System32\catroot2` to `catroot2.old`.
4. Restart services, reboot, and attempt once. If it fails identically again, the cache was not the cause — continue.

### Fix 3: Repair the store deeply

Surface DISM is not enough for repeat failures; verify the repair actually took.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` and confirm it reports success (not just completion).
2. Run `DISM /Online /Cleanup-Image /StartComponentCleanup`.
3. Run `sfc /scannow`, reboot, and attempt the update once.
4. If DISM reports it could not repair, note that — the in-place repair in Fix 7 becomes the plan.

### Fix 4: Ensure the servicing stack is current

A stale SSU fails every cumulative update identically — the textbook repeat pattern.

1. Check Update history for failed or missing servicing stack updates.
2. Download the latest SSU for 24H2 from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and install manually.
3. Reboot, then attempt the cumulative update.
4. The [servicing stack failure guide](/articles/how-to-fix-servicing-stack-update-failed-after-windows-11-update/) covers this layer in full.

### Fix 5: Strip persistent blockers

Remove the software that interferes identically every time.

1. Uninstall third-party antivirus completely for the test.
2. Update BIOS, chipset, and storage drivers from the manufacturer.
3. Disconnect peripherals; clean-boot with `msconfig` (non-Microsoft services off).
4. Attempt once in this stripped state.

### Fix 6: Install the cumulative update manually

Bypass the entire automatic pipeline for the stubborn KB.

1. Download the KB's MSU from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) (x64 for most laptops).
2. Install directly, reboot, and verify the build number advanced.
3. If the manual install fails identically, the problem is definitively systemic — proceed to Fix 7.
4. Check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for known issues with that specific KB.

### Fix 7: Perform the in-place upgrade repair

The definitive fix for repeat failures: rebuild the servicing environment while keeping everything.

1. Back up your files (belt and suspenders).
2. Mount a Windows 11 24H2 ISO, run setup.exe, choose Keep personal files and apps.
3. After the repair, the previously failing cumulative update installs normally in nearly all cases.
4. If even this fails, check drive health with `chkdsk` and SMART — hardware is the last remaining variable.

### Fix 8: Clear wedged servicing state: pending.xml and staging temp

A wedged pending servicing operation blocks every cumulative update identically — and it survives cache clears because it lives in the servicing stack, not the download cache. This is the hidden state behind many 'fails every time' cases. Unlike the download cache, which you have already cleared several times by now, this state is invisible to every standard reset — which is exactly why the failures kept repeating identically. Clearing it is safe when done from WinRE: you are removing a stuck operation, not deleting updates. Servicing rebuilds its queue cleanly on the next boot.

1. Check whether `C:\Windows\WinSxS\pending.xml` exists and is weeks old — that signals a wedged servicing operation.
2. Boot into WinRE: Settings → System → Recovery → Advanced startup → Restart now → Troubleshoot → Command Prompt.
3. In WinRE, verify drive letters with `diskpart` → `list volume` (they shift in recovery), then rename the stale pending.xml to pending.xml.old.
4. While there, clear `\Windows\WinSxS\Temp\PendingDeletes` if it is bloated with ancient entries.
5. Reboot normally, run `DISM /Online /Cleanup-Image /RestoreHealth` to let servicing rebuild clean state, then retry the update.

## Closing

A cumulative update failing every time is a deterministic problem, and deterministic problems have discoverable causes: corrupt cache, damaged store, stale servicing stack, or a persistent blocker. Work the sequence once, changing conditions at each step instead of repeating attempts, and finish with the in-place repair if needed. The cycle breaks the moment the underlying cause is removed — because there was never anything random about it.
