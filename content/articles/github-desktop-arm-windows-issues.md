---
title: "How to Fix GitHub Desktop Issues on ARM Windows Laptops"
slug: github-desktop-arm-windows-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["github desktop", "arm64", "git", "developer", "windows 11", "troubleshooting"]
description: "GitHub Desktop crashing or failing to sync on your ARM Windows laptop? Follow these step-by-step fixes for the ARM64 build, Git setup, and auth issues."
thumbnail: "/images/thumbs/github-desktop-arm-windows-issues.webp"
faqs:
  - q: "Is there a native ARM64 build of GitHub Desktop?"
    a: >
      GitHub Desktop publishes ARM64 builds for Windows alongside the x64 builds. Download the ARM64 installer from the official releases page — the x64 build runs under emulation and is slower and more crash-prone on Snapdragon laptops.
  - q: "Why does GitHub Desktop fail to clone or fetch?"
    a: >
      Network failures in the app usually come from the bundled Git or credential helper misbehaving under emulation, or from a proxy/VPN interfering. Installing native ARM64 Git for Windows and re-authenticating usually resolves it.
  - q: "GitHub Desktop opens but shows a blank window. What now?"
    a: >
      Blank-window issues are typically GPU or Electron rendering problems. Try launching with GPU acceleration disabled, update your graphics driver, and make sure you are on the latest GitHub Desktop release.
  - q: "Can I just use Git from the command line instead?"
    a: >
      Absolutely — native ARM64 Git for Windows works excellently on Snapdragon laptops and sidesteps every Electron issue. Many developers pair it with VS Code's built-in source control, which is also ARM64-native.
---

You installed GitHub Desktop on your Snapdragon laptop and it crashes on launch, shows a blank white window, or fails every clone and fetch with a vague error. The command-line git you used on your old machine worked fine — but you liked the GUI, and now it feels broken.

GitHub Desktop is an Electron app, and on ARM Windows the two things that break it are the wrong build (x64 under emulation instead of native ARM64) and its bundled Git/credential stack misbehaving under emulation. The app itself is fine — the failures are architecture friction, the same story as the rest of the dev tools on these laptops. If command-line Git is also acting up, our [WSL Git guidance](/articles/wsl-not-working-snapdragon-laptop/) covers the Linux side; for the Windows side, the fix is almost always "install the ARM64 build and ARM64 Git." Similar app-build confusion also breaks [Copilot in the Loop app](/articles/copilot-in-loop-app-not-working/) when the wrong architecture gets installed. Driver-side fixes follow the same logic — see [manually installing Intel NPU drivers](/articles/manually-install-intel-npu-driver-inf/) — and so do app features like [Snipping Tool Copilot actions going missing](/articles/snipping-tool-copilot-actions-missing/).

This guide gives you six fixes in order: install the ARM64 build, pair it with native ARM64 Git, fix authentication, resolve blank-window rendering issues, fix clone/fetch failures, and do a clean reinstall. No terminal wizardry required for most of it.

## Why this happens

- **x64 build running under emulation:** The default download is often x64. Under emulation the app is slower, hungrier, and more crash-prone — and its bundled tools inherit the same problems.
- **Bundled Git is the emulated build:** GitHub Desktop ships its own Git. The x64 app's bundled Git runs emulated, causing slow or failing clone/fetch/push operations.
- **Credential helper failures:** Authentication tokens stored by the emulated credential helper can fail to refresh, producing "authentication failed" on operations that worked yesterday.
- **Electron GPU rendering issues:** Blank or white windows are usually the Chromium GPU process crashing — a driver issue or an emulation artifact, not a Git problem.
- **Proxy or VPN interference:** Corporate proxies and VPN clients intercept the app's HTTPS traffic; the app's certificate handling under emulation can reject the interception.
- **Corrupted app data:** A crashed update or a forced shutdown can corrupt the app's local databases (repositories list, tokens), causing launch failures.
- **Antivirus quarantining app components:** Overzealous antivirus sometimes flags the app's updater or bundled Git binaries, breaking pieces of the installation silently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build

The wrong build is the root of most GitHub Desktop pain on Snapdragon laptops. Replace it deliberately.

1. Uninstall the current GitHub Desktop from **Settings > Apps > Installed apps**.
2. Go to the official GitHub Desktop releases page and download the installer labeled **ARM64** (the filename contains `arm64`).
3. Run the installer and launch the app — note whether it opens cleanly this time.
4. In Task Manager's **Details** tab, find GitHub Desktop's process — the **Architecture** column should read **ARM64**, not x64 emulation.
5. Sign in when prompted and let the app finish its first-run setup before testing any repository operations.

### Fix 2: Pair it with native ARM64 Git for Windows

Even the ARM64 app benefits from a proper system Git — and the x64 app absolutely needs it to behave.

1. Download **Git for Windows** and choose the **ARM64** installer (labeled for Windows ARM64).
2. During setup, accept the defaults but ensure **Git Credential Manager** is selected for authentication handling.
3. In GitHub Desktop, go to **File > Options > Git** and confirm which Git the app is using — point it at the system ARM64 Git if the option exists.
4. Open a terminal and run `git --version` to confirm the native ARM64 Git responds.
5. Retry a clone from within GitHub Desktop and compare speed and reliability against the bundled-Git behavior.

### Fix 3: Fix authentication and credential problems

"Authentication failed" on fetch/push after everything worked yesterday is a credential-store issue, not a network issue.

1. In GitHub Desktop, go to **File > Options > Accounts** and sign out of your GitHub account completely.
2. Open **Windows Credential Manager > Windows Credentials** and delete any `git:https://github.com` entries.
3. Sign back in through GitHub Desktop — use the browser-based OAuth flow when offered rather than pasting a token.
4. If you use a personal access token, generate a fresh fine-grained token with the scopes you need and sign in with it.
5. Test with a fetch on a known repository before assuming the fix worked — cached credentials can mask a still-broken flow.

### Fix 4: Resolve blank-window and rendering issues

The app launches but shows white/blank windows — the Electron GPU process is crashing.

1. Fully quit GitHub Desktop (check the system tray), then relaunch it and see if the window renders on the second attempt.
2. Update your graphics driver — for Qualcomm Adreno, use Windows Update and your OEM's driver page; for NVIDIA/AMD dGPUs use the [official NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) driver pages.
3. Try launching with GPU acceleration disabled: create a shortcut and add `--disable-gpu` to the target, then launch from it.
4. If the app renders with `--disable-gpu`, keep the flag while you wait for a driver or app update to fix the underlying issue.
5. As a cross-check, note whether other Electron apps (VS Code, Discord) render fine — if they do, the problem is GitHub Desktop-specific, not systemic.

### Fix 5: Fix clone, fetch, and push failures

Repositories list fine but network operations fail — work through the network stack methodically.

1. Test the same clone URL with native command-line Git (`git clone <url>`) — if the CLI works, the problem is the app's bundled Git or its network config.
2. Fully quit your VPN client and retry — VPNs are the most common cause of sudden Git network failures.
3. Check proxy settings: **File > Options > Git** in the app, and match them to what works in your browser or CLI Git.
4. For large repositories, increase the HTTP buffer: in the app's Git settings or via CLI `git config --global http.postBuffer 524288000`.
5. If only one repository fails, check its remote URL (**Repository > Repository settings**) for typos or a renamed/moved repo.

### Fix 6: Clean reinstall with fresh app data

When the app will not launch at all or behaves erratically after the above fixes, wipe its local state.

1. Uninstall GitHub Desktop from **Settings > Apps**.
2. Delete `%APPDATA%\GitHub Desktop` (this removes local databases and cached tokens — your repositories on disk are untouched).
3. Restart the laptop, then install the **ARM64** build fresh from the official releases page.
4. Sign in again through the browser OAuth flow and re-add your local repositories via **File > Add local repository**.
5. Confirm clone, fetch, and push all work before re-enabling any custom Git configurations.

## Closing

GitHub Desktop on Snapdragon laptops works well as long as you feed it the right binaries: the ARM64 app build plus native ARM64 Git for Windows. The x64 build under emulation is the source of nearly every crash, hang, and auth flake. And keep the honest fallback in mind — native command-line Git plus VS Code's source control gives you everything the GUI does, with zero Electron overhead. For deeper Git-on-Windows questions, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) links to current Git for Windows ARM64 documentation.
