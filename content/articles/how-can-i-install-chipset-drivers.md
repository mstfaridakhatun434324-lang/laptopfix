---
title: "How to Install Chipset Drivers on a Windows Laptop"
slug: how-can-i-install-chipset-drivers
date: 2026-09-27
categories: ["drivers"]
tags: ["chipset drivers", "intel", "amd", "motherboard drivers"]
description: "What are chipset drivers and how do you install them? Get the right INF package for your Intel or AMD laptop, in the right order."
thumbnail: "/images/thumbs/how-can-i-install-chipset-drivers.webp"
faqs:
  - q: "What do chipset drivers actually do?"
    a: "Chipset drivers (Intel INF files, AMD chipset packages) tell Windows how to communicate with the motherboard's built-in controllers — USB ports, SATA storage, PCIe lanes, power management, the SMBus, and more. Without correct chipset drivers, individual device drivers (USB, audio, Wi-Fi) sit on a broken foundation and misbehave in confusing ways. They're the base layer everything else builds on."
  - q: "How do I know which chipset my laptop has?"
    a: "The chipset follows your CPU: Intel CPU means Intel chipset, AMD CPU means AMD chipset. Check Settings > System > About for your processor. For the exact chipset model, open Device Manager > System devices and look at the entries, or run msinfo32 and check System Model alongside the processor. You rarely need the exact chipset name — the CPU generation is enough to pick the right package."
  - q: "Should I get chipset drivers from Intel/AMD or my laptop maker?"
    a: "For Intel, the Intel Driver & Support Assistant or Intel's chipset INF download is fine and usually current. For AMD, AMD's chipset package from amd.com works well. However, if your laptop is from Dell, HP, or Lenovo, check their support page first — some models need OEM-customized chipset packages, and the manufacturer page is the only guaranteed-correct source for those."
  - q: "Do I need to reinstall chipset drivers after a Windows reinstall?"
    a: "Yes — it's one of the first things to install on a fresh Windows setup, right after getting network connectivity. Windows' inbox chipset support is generic; the proper INF package enables full USB speeds, correct power management, and proper device enumeration. Install chipset drivers before the individual device drivers (audio, Wi-Fi, graphics) so they build on the correct foundation."
---

Chipset drivers are the most underappreciated software on your laptop. Nobody thinks about them — until USB ports act strangely, sleep/wake misbehaves, or a fresh Windows install feels subtly wrong. The chipset driver package teaches Windows how to talk to the motherboard itself: the USB controllers, storage interfaces, PCIe lanes, and power-management circuitry that every other device depends on. Get this layer right and half your mysterious device problems never happen.

The procedure is simple but order matters: identify your platform, get the package from the right source, install it, restart, then install device drivers on top. If you're rescuing a machine with broken USB or unknown devices, pair this with [Snappy Driver Installer for offline use](/articles/how-to-use-snappy-driver-installer/); if a bad driver update broke things, [roll it back first](/articles/best-way-to-rollback-driver-update/).

## Why this happens

- **Fresh Windows install without chipset drivers**: Windows' generic support works but leaves USB, power management, and device enumeration suboptimal.
- **Windows Update installed a mismatched chipset driver**: Rare but real — a wrong-generation INF package causes subtle instability.
- **Chipset driver corrupted**: Partial updates break the bus drivers that USB/audio/Wi-Fi depend on.
- **Installed in the wrong order**: Device drivers installed before the chipset package sometimes bind to generic bus drivers permanently.
- **OEM customization missing**: Generic Intel/AMD packages lack laptop-specific tweaks some models need.
- **Very old chipset driver on new Windows build**: Major Windows upgrades (22H2 → 24H2) occasionally outpace old INF packages.
- **Confusion with other "chipset" software**: Intel ME (Management Engine), RST (Rapid Storage), and chipset INF are different packages — installing the wrong one doesn't help.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your platform and current state

Know what you're installing before downloading anything.

1. Open **Settings** > **System** > **About** and note the **Processor** — Intel or AMD, and the generation (e.g., Intel Core i7-13700H, AMD Ryzen 7 7840U).
2. Open **Device Manager** > **System devices** and scan for warning icons — chipset problems often show here as unknown devices or flagged PCI/SMBus entries.
3. Check **Device Manager** > **IDE ATA/ATAPI controllers** and **Universal Serial Bus controllers** for warnings too — these are chipset-provided.
4. Note the current chipset driver date if visible (**System devices** > Intel/AMD chipset entries > **Properties** > **Driver** tab) — if it's years old on a fresh-feeling problem, it's a candidate.
5. For Intel systems, also note whether **Intel Management Engine** components appear — ME firmware/drivers are separate from the chipset INF but related.

### Fix 2: Get the chipset package from the right source

Source selection determines success.

1. **Intel laptops**: Run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — it detects your chipset and offers the correct INF package. Alternatively, download the "Intel Chipset Device Software (INF)" for your generation from Intel's download center.
2. **AMD laptops**: Download the chipset driver package from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) — select **Chipsets**, then your socket/platform (laptop chipsets are listed by Ryzen generation).
3. **Dell/HP/Lenovo laptops**: Check the manufacturer's support page first ([Dell](https://www.dell.com/support), HP, or Lenovo) — if they publish a chipset package for your model, prefer it; some models need OEM-specific INFs.
4. Avoid third-party driver sites for chipset packages — a wrong INF is worse than an old one, and repacked downloads sometimes bundle junk.
5. Save the installer where you can find it — you'll want it again after the next clean Windows install.

### Fix 3: Install the chipset package properly

The actual installation — straightforward but do it cleanly.

1. Close all applications. Chipset installers touch low-level bus drivers; don't multitask through it.
2. Run the installer as administrator. Intel's INF installer mostly updates .INF files and may report "nothing to do" on some entries — that's normal; it updates what needs updating.
3. AMD's package installs chipset drivers plus the Ryzen power plans — accept the power plan installation; the **AMD Ryzen Balanced** plan genuinely improves laptop behavior.
4. Restart when prompted — even if it doesn't prompt, restart. Bus driver changes need the reboot to take effect.
5. After restart, recheck **Device Manager** > **System devices** — previously flagged entries should be clean, and driver dates should reflect the new package.

### Fix 4: Install in the correct order on fresh systems

For clean Windows installs, sequence matters.

1. First: get network working (install the Wi-Fi/Ethernet driver if needed — use a USB drive from another machine if you have no network).
2. Second: install the **chipset driver package** (this guide's Fix 2–3).
3. Third: install **Intel ME** (Management Engine) or AMD equivalent if your manufacturer provides it — it sits between firmware and OS.
4. Fourth: install device drivers — graphics, audio, Wi-Fi/Bluetooth, card reader, touchpad — from the manufacturer's support page.
5. Last: run **Windows Update** and let it fill gaps. This order (chipset → ME → devices → Windows Update) prevents devices binding to generic bus drivers.

### Fix 5: Repair a broken chipset installation

When the chipset driver itself is the problem.

1. In **Device Manager** > **System devices**, right-click flagged chipset entries > **Uninstall device** (do NOT check driver deletion on the first pass), then **Action** > **Scan for hardware changes**.
2. If problems persist, download the chipset package fresh (your copy may be corrupt) and reinstall over the top, then restart.
3. For Intel: also reinstall the **Intel Management Engine** driver from your manufacturer's page — ME driver corruption mimics chipset failure (sleep issues, device weirdness).
4. Check **Settings** > **Windows Update** > **Update history** — if a driver update coincides with the problem's start, [roll back](/articles/best-way-to-rollback-driver-update/) the specific driver rather than reinstalling everything.
5. After repair, verify with real-world tests: USB transfer speeds, sleep/wake cycles, and device enumeration in Device Manager — chipset health shows in behavior, not just icons.

### Fix 6: Handle the Intel RST / storage driver question

Storage drivers ride with the chipset — get this right.

1. Many Intel laptops use **Intel Rapid Storage Technology (RST)** for the NVMe/SATA controller — it appears in **Device Manager** > **Storage controllers**.
2. If your manufacturer's page offers an RST driver for your model, install it — it's the storage half of the chipset story and affects disk performance.
3. Don't install generic Intel RST on systems whose manufacturer doesn't provide it — mismatched RST versions cause boot failures (INACCESSIBLE_BOOT_DEVICE) in the worst cases.
4. AMD systems: the chipset package includes the storage drivers — no separate RST equivalent to worry about.
5. After storage-driver changes, verify the system boots cleanly twice before considering it done — boot-critical drivers deserve the extra check.

### Fix 7: Keep chipset drivers maintained (lightly)

Chipset drivers need less attention than GPU drivers — but not zero.

1. Check for chipset updates twice a year, or when experiencing USB/sleep/device weirdness — not monthly.
2. Before major Windows feature updates (annual), check your manufacturer/Intel/AMD for a chipset package validated for the new build.
3. Don't use aggressive "driver updater" tools for chipset drivers — they frequently install wrong-generation INFs. Manual, from the right source, twice a year.
4. After any chipset update, do the behavioral checks: USB ports all working, sleep/wake reliable, no new Device Manager warnings.
5. Document the working version (a text file on the machine or your phone) — when something breaks six months later, knowing the last-good chipset version speeds diagnosis enormously.

## Closing

Chipset drivers are foundation work — invisible when right, maddening when wrong. Install them from the right source, in the right order, and maintain them lightly. Most "mysterious" USB, sleep, and device problems trace back to this layer, which is why technicians install chipset drivers before anything else on a fresh system. Do the same and you'll skip an entire category of weirdness.
