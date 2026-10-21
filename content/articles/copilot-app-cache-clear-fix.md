---
title: "How to Clear the Copilot App Cache and Fix Stubborn Glitches on Windows 11"
slug: copilot-app-cache-clear-fix
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot app", "clear cache", "app reset", "copilot problems", "ai pc", "windows 11"]
description: "Clear the Copilot app cache on Windows 11 with five safe methods: Settings reset, terminal commands, temp-file cleanup, fresh reinstall, and account re-sync."
thumbnail: "/images/thumbs/copilot-app-cache-clear-fix.webp"
faqs:
  - q: "Is clearing the Copilot cache safe?"
    a: >
      Yes. The cache holds only temporary files — thumbnails, session tokens, and UI state. Your
      conversations stored in your Microsoft account, settings, and history are untouched. The app
      rebuilds a fresh cache on next launch.
  - q: "Will clearing the cache delete my Copilot chat history?"
    a: >
      No. Cloud-side history tied to your Microsoft account is preserved. Only locally cached copies
      are removed. If history seems missing afterward, you are likely signed in with a different
      account — check Settings > Accounts.
  - q: "How often should I clear the Copilot cache?"
    a: >
      There is no schedule needed. Clear it when the app misbehaves — freezes, blank screens, stale
      answers, or stuck loading. Most users never need to touch it more than a few times a year.
  - q: "Does clearing the cache fix Copilot not opening at all?"
    a: >
      Sometimes. A corrupt cache is one reason Copilot fails to launch, and a Settings reset fixes
      many of those cases. If the app still will not start, the problem is deeper — compare with the
      guide for [Copilot app not opening on Windows 11](/articles/copilot-app-not-opening-
      windows-11/).
---

When the Copilot app on your Windows 11 AI PC starts acting strangely — answers that repeat themselves, prompts that never send, a blank chat window, or the app freezing for seconds at a time — a stale or corrupt local cache is one of the most common causes. Like any app, Copilot stores temporary data on your machine to load faster, and that data can go bad after a crash, a Windows update, or a botched Microsoft Store update.

Cache trouble is easy to misdiagnose because the symptoms look like internet or server problems. The tell is that everything else works fine: your browser is fast, Teams runs smoothly, and other apps are snappy. Only Copilot misbehaves. On Copilot+ PCs, where Copilot is woven into the shell and the NPU, that misbehavior can even drag down related features, so clearing the cache promptly is worth the two minutes.

This guide covers five safe methods, from the one-click Settings reset to terminal-level cache removal and a full reinstall. None of them touches your files, your Microsoft account, or your cloud chat history. Work through them in order, testing Copilot after each step.

## Why this happens

- **Interrupted app updates**: If a Microsoft Store update of Copilot is interrupted mid-write, the cached package files no longer match the app's version, causing hangs and blank screens.
- **Corrupt session data**: A crash or forced shutdown while Copilot is mid-response can leave half-written session files in the cache that the app chokes on at next launch.
- **Stale authentication tokens**: Cached sign-in tokens can expire or desync after a password change or a Microsoft account security event, leaving Copilot stuck in a half-signed-in loop.
- **Temp-file bloat**: Months of thumbnails, conversation previews, and web-result caches accumulate until the app's storage quota fills and writes start failing silently.
- **Cross-version leftovers**: Major Windows feature updates sometimes change the app's data folder layout, orphaning old cache folders that conflict with the new layout.
- **Conflicted cloud sync state**: A mismatched local cache versus your account's cloud state can cause answers to duplicate or edits to refuse to save.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset the Copilot app from Windows Settings

The Settings reset is the official, safe one-click method. It clears the app's cache and local data while leaving the app itself installed — the equivalent of wiping the slate without reinstalling. Start here; it fixes most cache-related glitches in under a minute.

1. Open **Settings > Apps > Installed apps** and find **Microsoft Copilot** in the list.
2. Click the three-dot menu, choose **Advanced options**, and scroll to the Reset section.
3. Click **Repair** first — this reinstalls app files but keeps data, fixing version-mismatch cases.
4. If problems continue, click **Reset**, confirm, and relaunch Copilot to rebuild a fresh cache.
5. Sign back in if prompted, then test with a simple prompt to confirm responses flow normally.

### Fix 2: Clear temp files and the Store cache with terminal commands

Windows caches Store apps at the system level too, and the Microsoft Store's own download cache can hold a corrupted Copilot package. A couple of quick commands flush both, and neither deletes anything personal. Use this when the Settings reset did not fully help, or when Store updates keep failing.

1. Press **Win + R**, type **wsreset.exe**, and press Enter — a blank Store window opens and closes as the Store cache clears.
2. Open Terminal as administrator and run `rmdir /s /q %localappdata%\Packages\Microsoft.Copilot_*\AC\Temp` to drop Copilot's temp folder (adjust if your package name differs; use `dir` to check).
3. Run **Disk Cleanup** (search it in Start), select your system drive, and check **Temporary files** and **Thumbnails**.
4. Restart your PC so any locked cache files are released, then launch Copilot fresh.
5. If the app now updates through the Store successfully, you found the corrupt layer.

### Fix 3: Sign out and back in to refresh cached credentials

When the symptoms look like a cache problem but are really a token problem — the app loads but prompts time out, or it flashes a sign-in screen in a loop — refreshing your Microsoft account credentials clears the bad tokens without touching anything else. This is especially common after a password change or a security alert from Microsoft. It is also the right first move when [your chat history stops syncing between devices](/articles/copilot-chat-history-not-syncing/) — sync failures are usually expired tokens, not lost data.

1. In the Copilot app, open the profile menu (top right) and choose **Sign out**.
2. Open **Settings > Accounts > Your info** and confirm Windows itself is signed in with the right Microsoft account.
3. In **Settings > Accounts > Email & accounts**, remove the account and re-add it to force a fresh token set.
4. Reopen Copilot, sign in again, and wait for it to sync before testing a prompt.
5. If prompts still fail after a clean sign-in, move on — the cache layer is not the culprit.

### Fix 4: Reinstall Copilot cleanly through the Microsoft Store

Sometimes the app package itself is the corruption, not just its cache — damaged app binaries survive a Settings reset because Reset only touches data, not the install. A full uninstall and Store reinstall gives you a genuinely fresh copy. Do this after the lighter methods have failed, since it takes a few minutes.

1. In **Settings > Apps > Installed apps**, find Copilot, open the three-dot menu, and choose **Uninstall**, confirming both prompts.
2. Restart your PC so Windows releases the app's data folders completely.
3. Open the **Microsoft Store**, search **Copilot**, and install it fresh from Microsoft.
4. Launch it, sign in, and test a prompt plus one AI PC feature like [suggested prompts](/articles/copilot-suggested-prompts-missing/) to confirm full recovery.
5. If the Store version behaves differently than before, check [Windows Update](https://www.catalog.update.microsoft.com/) too — Copilot updates sometimes ride along with system updates.

### Fix 5: Check for a broader Windows shell or NPU issue

If a cleared cache, fresh tokens, and a clean reinstall still leave Copilot misbehaving, the problem may sit below the app — a glitchy Windows shell integration, or an NPU hiccup affecting Copilot+ features. Cache clearing cannot fix what the cache did not break, so widen the diagnosis before repeating steps.

1. Run `sfc /scannow` in an elevated Terminal to repair corrupted system files the shell relies on.
2. In Device Manager, check the NPU under System devices — a yellow warning there can [freeze AI-dependent features](/articles/zoom-virtual-background-arm-laptop/) even when the app itself is healthy.
3. If the NPU is missing entirely, see the [guide for OpenVINO not detecting the NPU](/articles/openvino-npu-not-detected-windows/) to restore hardware acceleration first.
4. As a last resort, use **Settings > System > Recovery > Reset this PC** with **Keep my files** — drastic, but it fixes shell-level corruption nothing else touches.
5. After any repair, give Windows one full restart cycle before judging Copilot's behavior — shell components settle during boot.

## Closing

Cache problems are the most forgiving kind of Copilot trouble: a Settings reset or a Store reinstall clears them without risking anything you care about. Keep this guide's order in mind — reset first, terminal cleanup second, credentials third, reinstall fourth — and resist the urge to jump straight to a full PC reset. If Copilot is still stuck after all five fixes, the issue is almost certainly in the Windows shell or your account state, not the app's cache, and that is where your next troubleshooting should go.
