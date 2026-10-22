---
title: "How to Set Up Git ARM64 Correctly on Windows 11"
slug: git-arm64-windows-setup
date: 2026-10-22
categories: ["ai-pc"]
tags:
  - git
  - arm64
  - windows-on-arm
  - developers
  - setup
description: "Setting up Git on a Snapdragon laptop? Install the right ARM64 build and configure credentials, SSH, and line endings correctly from the start. Set it up now."
thumbnail: "/images/thumbs/git-arm64-windows-setup.webp"
faqs:
  - q: "Is there a native ARM64 build of Git for Windows?"
    a: >
      Yes. Git for Windows publishes ARM64 builds alongside x64. On Snapdragon laptops the ARM64 build
      is faster and avoids the subtle issues emulated Git can cause with hooks and credential helpers.
  - q: "Will my existing repositories work after switching Git builds?"
    a: >
      Yes. Repositories are architecture-independent. Switching Git builds does not touch your working
      trees; just make sure global config and credentials carry over.
  - q: "Do Git GUIs work on ARM Windows?"
    a: >
      Most do, especially those built on Electron with ARM64 support or .NET. Check each client's
      release notes for an ARM64 or Windows-on-ARM build before installing.
  - q: "Why are Git operations slow on my ARM laptop?"
    a: >
      The usual cause is emulated x64 Git, antivirus scanning the .git directory, or a network drive
      hosting the repo. Native Git plus local SSD storage is dramatically faster.
---

Git feels like it should just work everywhere, and mostly it does — until a Snapdragon laptop serves you the x64 build through emulation and everything gets slightly worse: slower status calls, hooks that misbehave, credential helpers that flake. The fix is a proper ARM64 Git for Windows install plus a few configuration choices that matter more on ARM than they did on Intel. Done right, Git on Snapdragon is fast and boring, exactly as it should be. Git is architecture-independent in theory, but the Git for Windows build, its credential manager, and your editor integration all run as native code — so the build you install still matters.

Verify your current Git first: one command reveals whether you are native or emulated. If your workflow lives partly in Linux, fixing [WSL on ARM laptops](/articles/wsl-not-working-arm-laptop/) first gives you a second, fully native Git to compare against. Editor integration counts too — our [VS Code ARM versus x64 guide](/articles/vscode-arm-native-vs-x64/) keeps the editor side consistent — and shared-machine quirks like [Recall multi-user issues](/articles/recall-multi-user-account-issues/) are separate platform matters. If your repositories live inside a OneDrive-synced folder and act strangely, also rule out [Recall's OneDrive sync conflicts](/articles/recall-onedrive-sync-conflicts/) — cloud-sync interference is a different problem from Git configuration.

This guide covers installing ARM64 Git, configuring credentials and line endings, speeding up slow operations, and handling the GUI-client question. If you use Live Captions while pair-programming, [profanity filter settings](/articles/live-captions-profanity-filter-settings/) are unrelated — keep audio and version-control troubleshooting separate.

## Why this happens

- **x64 Git running under emulation:** Emulated Git works but is slower, and native hooks or helpers can fail in edge cases. Translated Git pays an overhead on every process spawn, and hooks or helpers compiled for x64 can fail outright.
- **Multiple Git installs conflicting:** Store, Scoop, and manual installs can stack up, with PATH deciding which Git actually runs. With several Git installs present, PATH order silently decides which git.exe answers — often the oldest one.
- **Credential manager architecture mismatch:** The Git Credential Manager must match the Git build; mismatches cause silent auth failures. The credential helper is a separate binary; an x64 helper paired with ARM64 Git fails to store or retrieve tokens.
- **Antivirus scanning .git directories:** Real-time scanning of thousands of small git objects tanks performance. Git operations touch thousands of small files, and real-time scanning multiplies each access into noticeable lag.
- **Wrong line-ending configuration:** Migrated configs from Intel machines sometimes carry settings that cause noise on new checkouts. A config migrated from Intel may set autocrlf or file paths that produce noisy diffs on the new machine.
- **SSH client mismatch:** The bundled OpenSSH versus Windows' own can differ in key handling and agent behavior. Windows ships its own OpenSSH while Git bundles another; agent and key handling differ subtly between them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install Git for Windows ARM64

One correct install beats three conflicting ones.

1. Uninstall existing Git versions to avoid PATH fights.
2. Download the ARM64 Git for Windows installer.
3. During setup, choose the ARM64 components and defaults you prefer.
4. Verify the install reports the ARM64 build.
5. Confirm git works from a fresh terminal.

### Fix 2: Configure identity and line endings

A clean config prevents the classic first-commit headaches.

1. Set your user name and email globally.
2. Set core.autocrlf appropriately for Windows collaboration.
3. Configure the default branch name to match your hosting.
4. Test with a scratch repo: init, add, commit.
5. Review the resulting config file for sanity.

### Fix 3: Set up the credential manager

Smooth authentication is the difference between Git feeling native and feeling broken.

1. Ensure Git Credential Manager is installed with the ARM64 build.
2. Connect to your hosting and complete the OAuth or token flow.
3. Verify credentials persist across terminal restarts.
4. For SSH, generate keys with the bundled OpenSSH and add them to your host.
5. Test push and pull to confirm auth is solid.

### Fix 4: Speed up slow Git operations

Native Git should be fast; if it is not, something environmental is slowing it.

1. Exclude repo folders from real-time antivirus scanning.
2. Keep repositories on the local SSD, not network drives.
3. Enable filesystem caching options appropriate for Windows.
4. Run garbage collection on old, bloated repositories.
5. For Windows performance help, see [Copilot in Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Choose ARM64-friendly Git GUIs

GUI clients vary widely in ARM support; picking right avoids a second round of troubleshooting.

1. Check each client's releases for ARM64 or Windows-on-ARM builds.
2. Prefer clients with native builds over emulated ones.
3. Test core operations — clone, commit, push — before committing to a client.
4. Keep the CLI installed as a fallback regardless.
5. Revisit choices yearly as ARM support improves.

### Fix 6: Handle WSL Git separately

WSL has its own Git; keep the two worlds' configs from interfering.

1. Install Git inside WSL via the distro package manager.
2. Configure identity separately in the Linux environment.
3. Use the Windows credential manager bridge or Linux auth consistently.
4. Avoid operating on the same repo from both sides simultaneously.
5. Document which side owns each workflow for teammates.

### Fix 7: Run an end-to-end hosting test

Configuration looks right on paper, but only a real round-trip proves it. Cloning, committing, and pushing to your actual hosting exercises credentials, SSH, and line endings together — catching the integration issues that isolated checks miss.

1. Clone a test repository from your hosting provider.
2. Create a branch, make a commit, and push it.
3. Open a pull request to verify web integration works.
4. Check the committed files for line-ending correctness.
5. Delete the test branch once everything passes.

## Closing

Git on ARM Windows rewards the same discipline as the rest of the toolchain: install the ARM64 build, configure it once, keep antivirus out of its way, and align your editor and helpers. Do that and version control fades into the background where it belongs. One green end-to-end test — clone to push — is worth a dozen config inspections, and it gives you a baseline to return to if things ever regress.
