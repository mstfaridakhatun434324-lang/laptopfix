---
title: "Windows Feature Experience Pack Failed to Install? Fix It Here"
slug: how-to-fix-feature-experience-pack-failed-to-install
date: 2026-09-27
categories: ["windows-update"]
tags: ["feature experience pack", "failed to install", "windows 11", "windows 10", "fix"]
description: "The mysterious Windows Feature Experience Pack won't install? What it is, why it fails, and the exact fixes — it's simpler than it looks."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It's a small Microsoft package that delivers certain Windows shell and feature updates (like Snipping Tool and shell component improvements) independently of full OS builds. Think of it as a mini feature update for specific Windows experiences. It's versioned separately (e.g., 1000.xxxxx) and installs through Windows Update like any other update."
  - q: "Why does the Feature Experience Pack fail when other updates succeed?"
    a: "It has its own servicing manifest and dependency chain. Corruption in its specific package state, a mismatched shell component version, or a pending operation from a previous attempt blocks it while unrelated cumulative updates sail through. Its failures are usually package-specific, not system-wide."
  - q: "Can I just ignore the Feature Experience Pack if it won't install?"
    a: "Mostly yes — it's not a security update, and skipping it doesn't leave you vulnerable. But persistent failure can indicate underlying servicing corruption worth fixing, and some shell features won't update without it. Fix it when convenient; don't lose sleep, but don't ignore a pattern either."
  - q: "Does the Feature Experience Pack require a reboot?"
    a: "Sometimes — it depends on which shell components it touches. If it prompts for a restart, take it; shell file replacements need one. If it installs silently, no reboot is needed. A pending reboot from another update can block it, so clear those first."
---

Of all the updates Windows offers, the Feature Experience Pack is the most mysterious: a small package with a vague name that occasionally fails with no useful explanation. It's not a security update, not a driver, not a full build — it's Microsoft's vehicle for updating shell-level features (Snipping Tool, input, shell components) between major releases. When it fails, the fix is usually straightforward once you know what you're dealing with.

The failure causes are a short list: corrupted package-specific state in the update cache, a pending reboot blocking shell file replacement, servicing store issues affecting its manifest, or a simple version mismatch where Windows Update offers a pack your build can't take. Work the sequence below in order. For general pipeline corruption behind it, [resetting Windows Update components](/articles/how-to-reset-windows-update-components-on-windows-11/) is the deep fix.

Note the exact pack version from Update history (it looks like 1000.226xx.xxxx.0) — you'll need it if this goes to manual installation.

## Why this happens

- **Corrupted pack-specific cache state**: Its manifest and payload cache damage independently of other updates. The standard cache reset clears the pack's state along with everything else.
- **Pending reboot blocking shell replacement**: Shell files cannot be replaced while marked in-use by a pending operation. A second reboot clears staged shell flags that one restart leaves behind.
- **Servicing manifest mismatch**: The offered pack version does not match the installed shell component baseline. Compare the offered version against About — a match means the failure is phantom.
- **Component store corruption**: WinSxS damage breaks the pack's install-time validation. DISM repairs the store the pack validates against.
- **Interrupted previous attempt**: A killed earlier install leaves half-state that blocks retry. Always clear the cache after a killed attempt before retrying.
- **Third-party shell modifications**: Start-menu replacements and shell tweaks can conflict with shell-component updates. Re-enable tools one at a time afterward to identify the conflicting one.
- **Stuck update orchestrator state**: The orchestrator wedged on the pack's small payload, retrying identically. Restarting the update services clears the wedge without a full reset.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear any pending reboot first

Shell updates and pending reboots don't mix — clear the queue. Shell updates and pending reboots do not mix — clear the queue.

1. Settings → Windows Update: if a restart is pending, restart now.
2. After reboot, check Update history for anything mid-flight and let it settle.
3. Only then retry the Feature Experience Pack.
4. If no reboot was pending, continue — the block is elsewhere.
5. A second reboot after the first clears staged shell flags that a single restart leaves behind.

### Fix 2: Retry after a clean update-service restart

The gentle reset for the pack's stuck state. The gentle reset for the pack's stuck state.

1. Admin Command Prompt: `net stop wuauserv`, `net stop bits`.
2. `net start wuauserv`, `net start bits`.
3. Settings → Windows Update → **Retry** on the failed pack.
4. Small-package transient failures clear here surprisingly often.
5. If the retry fails instantly rather than after downloading, the block is a flag, not the payload — continue to Fix 3.

### Fix 3: Reset the update cache (pack-specific corruption included)

The standard reset clears the pack's damaged manifest state too. The standard reset clears the pack's damaged manifest state too.

1. Admin Command Prompt: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`; `ren C:\Windows\System32\catroot2 catroot2.old`.
3. `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. Check for updates — the pack re-downloads fresh. Full guide: [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/) (or the [Windows 10 version](/articles/how-to-reset-windows-update-components-on-windows-10/)).
5. The pack is small, so the post-reset re-download takes seconds — a quick confirmation the pipeline is healthy.

### Fix 4: Run DISM and SFC for manifest-level damage

When the pack fails validation, the servicing store is suspect. When the pack fails validation, the servicing store is suspect.

1. Admin Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth`.
2. `sfc /scannow`; restart.
3. Retry the Feature Experience Pack.
4. Check CBS.log for the pack's package name if it still fails — that names the exact broken manifest.
5. Search CBS.log for the pack's version number specifically — generic Failed lines may belong to other packages.

### Fix 5: Disable third-party shell modifications temporarily

Start-menu replacements and shell tweaks are the pack's natural enemies. Start-menu replacements and shell tweaks are the pack's natural enemies.

1. Uninstall or disable Start11/StartAllBack-style tools and shell extensions temporarily.
2. Retry the pack install in the stock-shell state.
3. If it succeeds, re-enable your tools afterward — and note the conflict for next time.
4. This is the fix the generic guides never mention, and it resolves a real minority of cases.
5. Re-enable tools one at a time after success — if one re-breaks future packs, you have identified the culprit.

### Fix 6: Install the pack manually from the Update Catalog

The bypass that works for small packs as well as big KBs. The bypass that works for small packs as well as big KBs.

1. Search the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) for 'Feature Experience Pack' plus your Windows version.
2. Match the pack version to your build; download the x64 package.
3. Install, reboot if prompted.
4. Verify in Update history. If manual install fails identically, the cause is systemic — return to Fixes 4–5.
5. Small-pack manual installs complete in under a minute — if it hangs, the cause is systemic, not the download.

### Fix 7: Check whether your build actually needs it

Sometimes the offered pack is simply inapplicable — and that's fine. Sometimes the offered pack is simply inapplicable — and that is fine.

1. Compare the offered pack version against your build's expected Experience Pack version (Settings → System → About shows it).
2. If they match already, the 'failure' is a phantom — hide the update or ignore it.
3. If mismatched, the manual install (Fix 6) is the authoritative path.
4. Either way, confirm subsequent cumulative updates install normally — that proves the pipeline is healthy.
5. An inapplicable-but-offered pack is a known Windows Update quirk, not a sign of system damage.

## Closing

The Feature Experience Pack looks mysterious but fails for mundane reasons: pending reboots, cache corruption, shell-tool conflicts, or simple inapplicability. Clear the reboot queue, reset the cache, sideline your shell tweaks, and install it manually if needed. Small package, small problem — once you know which small problem it is. Related guides: [resetting Windows Update components](/articles/how-to-reset-windows-update-components-on-windows-11/) and [Windows 10 version](/articles/how-to-reset-windows-update-components-on-windows-10/).
