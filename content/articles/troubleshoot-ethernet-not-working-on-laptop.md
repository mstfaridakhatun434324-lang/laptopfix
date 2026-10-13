---
title: "Troubleshoot Ethernet Not Working on a Laptop: Diagnostic Guide"
slug: troubleshoot-ethernet-not-working-on-laptop
date: 2026-09-04
categories: ["drivers"]
tags: ["ethernet troubleshooting", "lan issues", "network diagnostics", "wired connection", "windows 11"]
description: "Troubleshoot laptop Ethernet failures like a technician: a diagnostic flowchart from link lights to driver resets that isolates the fault fast."
thumbnail: "/images/thumbs/troubleshoot-ethernet-not-working-on-laptop.webp"
faqs:
  - q: "How do I systematically troubleshoot Ethernet on a laptop?"
    a: "Follow the layers: physical (cable, port LEDs, different router port), adapter state (Device Manager — present? enabled? driver errors?), IP configuration (ipconfig — valid address or 169.254?), and connectivity (ping gateway, ping internet). Each layer's test tells you exactly where the fault is. Jumping straight to driver reinstalls without checking link lights wastes time when the cable is the problem."
  - q: "What do the Ethernet port lights tell me?"
    a: "Most RJ45 ports have two LEDs: link (solid when a physical connection exists) and activity (blinking with traffic). No lights at all means no physical link — suspect cable, port, or far-end. Solid link but no activity with 'Unidentified network' means link is up but IP configuration failed — that's a DHCP or TCP/IP stack problem, not hardware."
  - q: "Why does Ethernet show 'Unidentified network, no internet'?"
    a: "Your laptop established a physical link but couldn't get a working IP configuration — usually DHCP failed. Release and renew the IP (ipconfig /release, ipconfig /renew), restart the router, and check for a 169.254.x.x self-assigned address (the telltale sign of DHCP failure). Corrupted TCP/IP stacks and bad cables that pass link but corrupt data cause this too."
  - q: "How can I tell if the Ethernet problem is the laptop or the network?"
    a: "Test with a second device on the same cable and router port: if it works, your laptop is the fault; if it fails, the cable, port, or router is. Similarly, test your laptop on a different known-good network (a friend's router, a USB tether won't test Ethernet though). This two-minute isolation prevents hours of fixing the wrong end."
---

Troubleshooting Ethernet is one of the most satisfying diagnostic exercises in PC repair, because wired networking is honest: link lights tell the truth, each layer is independently testable, and the fault is always somewhere specific. This guide is structured as a diagnostic flowchart — you'll run tests in order, and each result routes you to the next step. No guessing, no shotgun driver reinstalls.
If you'd rather have the straightforward fix-it sequence than the diagnostic method, our [Ethernet fix guide](/articles/what-to-do-if-ethernet-not-working-on-laptop/) covers the same ground as a procedure. This one teaches you to read what the laptop is telling you: LED states, ipconfig output, and Device Manager codes. The skill transfers to every wired network you'll ever touch.
One prerequisite: you need a known-good cable and, ideally, a second device for isolation testing. Borrow both before you start — they're the control group for every experiment below. For the driver-specific deep end, our [Ethernet driver guide](/articles/how-to-fix-ethernet-not-working-on-laptop-in-windows-11-24h2/) has the Device Manager details.

## Why this happens

- **Failed cable (most common).** Internal pair breaks kill data while the cable looks pristine.
- **Dead far-end port.** Router/switch ports fail; the laptop gets blamed for the network's problem.
- **No link: port or controller failure.** Dead LEDs with good cable and far end means laptop-side hardware.
- **Disabled adapter.** Device Manager or BIOS has the controller switched off.
- **DHCP failure.** Link up, no valid IP — the 'Unidentified network' signature.
- **TCP/IP stack corruption.** Winsock damage breaks connectivity despite perfect link and IP.
- **Driver fault.** Corrupted or mismatched Ethernet driver breaks initialization or performance.
- **Speed/duplex mismatch.** Forced settings disagreeing with the switch cause link-but-no-traffic.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the link lights and isolate the ends

The physical layer test: LEDs plus a second device tell you which end is broken in two minutes.

1. Plug in the cable and watch the laptop port's LEDs — note solid link vs. blinking activity vs. dark.
2. Test the same cable and router port with a second device (another laptop, a desktop).
3. If the second device works: fault is your laptop — continue to Fix 2. If it fails: swap the cable first, then try a different router port.
4. No LEDs with a proven-good cable and port: suspect the laptop's port or controller — check Device Manager next.
5. Document which combinations worked — this matrix is your evidence for every later step.

### Fix 2: Verify adapter state in Device Manager

Windows' view of the controller: present, enabled, and driver-healthy — or the source of the fault.

1. Open Device Manager → 'Network adapters' → find the Ethernet controller.
2. Down-arrow icon → right-click → Enable device. Yellow icon → Properties → note the error code.
3. Missing entirely → View → 'Show hidden devices'; still missing → check BIOS for onboard LAN enabled.
4. Right-click → Properties → Advanced → confirm 'Speed & Duplex' is 'Auto Negotiation.'
5. Power Management tab → uncheck 'Allow the computer to turn off this device to save power.'

### Fix 3: Diagnose the IP configuration

ipconfig output is a diagnostic readout — learn to read it and the fault announces itself.

1. Open Command Prompt → run ipconfig and find the Ethernet adapter section.
2. Valid 192.168.x.x/10.x.x.x/172.16.x.x address + gateway = IP layer fine; fault is higher (DNS, firewall) — try ping 8.8.8.8.
3. 169.254.x.x address = DHCP failed: restart the router, then ipconfig /release + ipconfig /renew.
4. 'Media disconnected' = no link: return to Fix 1, the physical layer is still broken.
5. No Ethernet section at all = adapter not present to Windows: return to Fix 2.

### Fix 4: Test connectivity layer by layer

Ping tests isolate exactly which layer fails: local stack, gateway, DNS, or internet.

1. ping 127.0.0.1 — tests your own TCP/IP stack. Failure here means stack corruption (Fix 5).
2. ping <default gateway from ipconfig> — tests the local link. Failure with good link lights suggests duplex mismatch or firewall.
3. ping 8.8.8.8 — tests internet routing. Success here but no browsing = DNS problem: try ipconfig /flushdns and alternate DNS.
4. ping google.com — tests DNS resolution. Failure here only = DNS configuration issue.
5. Each failing step names the layer to fix — don't skip ahead.

### Fix 5: Reset the TCP/IP stack and Winsock

When lower layers test fine but connectivity fails, the stack itself is corrupted — rebuild it.

1. Elevated Command Prompt: netsh winsock reset → Enter.
2. netsh int ip reset → Enter.
3. ipconfig /flushdns → Enter.
4. Restart the laptop.
5. Retest the ping ladder from Fix 4 — a corrupted stack shows all-green after reset.

### Fix 6: Reinstall the Ethernet driver diagnostically

Driver faults have signatures: Code 10/43 in Device Manager, or link that dies under load — reinstall cleanly.

1. Device Manager → Ethernet adapter → Uninstall device → check 'Attempt to remove the driver for this device.'
2. Restart — Windows installs a base driver; test immediately.
3. If the base driver works, install the maker's proper LAN driver for full performance.
4. Intel adapters: the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) identifies the right package.
5. If the fault persists across drivers, it's hardware or cabling — revisit Fix 1 with fresh eyes rather than reinstalling again.

### Fix 7: Confirm with alternate hardware and document

The final diagnostic proof: swap the variable you can't test in software.

1. Test a USB Ethernet adapter on the laptop — working USB Ethernet with dead built-in port proves the port/controller failed.
2. Test the laptop's port against a different switch/router to eliminate far-end quirks.
3. If the built-in port is dead and out of warranty, adopt the USB adapter permanently — it's the economical fix.
4. Write up the fault, the tests, and the working configuration for your records.
5. For ongoing WiFi-side issues after Ethernet is sorted, our [5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-step-by-step/) covers the wireless equivalent diagnostics.

## Closing

Ethernet troubleshooting is applied logic: lights, isolation, adapter state, IP config, ping ladder, stack reset, driver. Follow the evidence instead of guessing, and the fault — cable, port, DHCP, or driver — will identify itself every time.
