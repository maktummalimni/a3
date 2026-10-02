# -*- coding: utf-8 -*-
"""
GENERATE_SITE.PY
Generates the complete static website for Aperture Castle Horological Atelier (Watch).
Implements the exact Ridevora precision layout system (Zero Blog).
"""

import os
import re
import json

SITE_DIR = r"d:\antigravity website\aperturecastle"
DOMAIN = "aperturecastle.com"
ADDR = "One International Place, Suite 3100, Boston, MA 02110, United States"
PHONE = "+1-888-634-8921"
EMAIL = "concierge@aperturecastle.com"
DESK_HOURS = "7:00 am – 10:00 pm ET, every day"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Sora:wght@500;600;700&display=swap" rel="stylesheet">"""

def get_utility():
    return f"""<div class="utility"><div class="wrap">
  <div class="u-left"><span><span class="dot" aria-hidden="true"></span>Horological consultations daily, {DESK_HOURS}</span><a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></div>
  <div class="u-right"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="booking.html">Reserve viewing</a></div>
</div></div>"""

def get_header(active_page=""):
    pages = [
        ("index.html", "Home"),
        ("products.html", "Collection"),
        ("booking.html", "Book Viewing"),
        ("about.html", "Heritage"),
        ("faq.html", "FAQ"),
        ("contact.html", "Contact")
    ]
    links = []
    for href, label in pages:
        cur = ' aria-current="page"' if href == active_page else ''
        links.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    links_html = "".join(links)
    
    return f"""<a class="skip" href="#main">Skip to content</a>
{get_utility()}
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Aperture Castle home"><span class="brand-mark"><svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="12.5" fill="none" stroke="#E5A93C" stroke-width="2.5"/><circle cx="16" cy="16" r="3.2" fill="#fff"/><path d="M16 8V16L21 19" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg></span><span class="brand-text"><strong>APERTURE</strong><span>CASTLE</span></span></a>
  <nav class="main-nav" id="main-nav" aria-label="Main"><ul>{links_html}<li class="nav-only-mobile"><a href="booking.html">Reserve Viewing</a></li></ul></nav>
  <div class="header-cta"><a class="btn btn-ghost btn-sm" href="tel:{PHONE.replace('-', '')}">Call desk</a><a class="btn btn-accent btn-sm" href="booking.html">Book viewing</a>
  <button class="nav-toggle" type="button" aria-label="Open menu" aria-controls="main-nav" aria-expanded="false"><span></span></button></div>
</div></header>"""

def get_footer():
    return f"""<footer class="site-footer"><div class="wrap">
  <div class="f-top">
    <div>
      <a class="brand" href="index.html" aria-label="Aperture Castle home"><span class="brand-mark"><svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="12.5" fill="none" stroke="#E5A93C" stroke-width="2.5"/><circle cx="16" cy="16" r="3.2" fill="#fff"/><path d="M16 8V16L21 19" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg></span><span class="brand-text"><strong>APERTURE</strong><span>CASTLE</span></span></a>
      <p class="f-about">Haute horlogerie curation, complication assembly, and private collector viewings from our Boston Financial District atelier. Master watchmaking with transparent provenance.</p>
    </div>
    <div><h2>Explore</h2><ul>
      <li><a href="index.html">Atelier Home</a></li><li><a href="products.html">Horological Collection</a></li><li><a href="booking.html">Book Salon Viewing</a></li>
      <li><a href="about.html">Heritage &amp; Philosophy</a></li><li><a href="faq.html">Collector FAQ</a></li><li><a href="contact.html">Contact Us</a></li></ul></div>
    <div><h2>Policies</h2><ul>
      <li><a href="cancellation-refund-policy.html">Cancellation &amp; Refund</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li>
      <li><a href="terms-and-conditions.html">Terms &amp; Conditions</a></li><li><a href="cookie-policy.html">Cookie Policy</a></li>
      <li><a href="disclaimer.html">Horological Disclaimer</a></li></ul></div>
    <div><h2>Visit &amp; call</h2><ul>
      <li>{ADDR}</li>
      <li><a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>Desk hours: {DESK_HOURS}</li></ul></div>
  </div>
  <div class="f-bottom"><span>&copy; <span data-year>2026</span> Aperture Castle Horological Atelier LLC. All rights reserved.</span>
    <ul><li><a href="sitemap.xml">Sitemap</a></li><li><button class="link-btn" type="button" data-open-cookies>Cookie settings</button></li></ul></div>
</div></footer>
<div class="cookie" role="dialog" aria-labelledby="cookie-title" aria-live="polite">
  <h2 id="cookie-title">Your privacy choices</h2>
  <p>We use essential cookies to manage private salon viewings, plus minimal telemetry to understand and refine our horological archives. You can modify your choices at any time. <a href="cookie-policy.html">Cookie Policy</a></p>
  <div class="row"><button class="btn btn-accent btn-sm" type="button" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" type="button" data-consent="essential">Essential only</button></div>
</div>
<button class="to-top" type="button" aria-label="Back to top"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>
<script src="assets/js/main.js" defer></script>"""

def check_paragraphs(paras, page_name):
    for idx, p in enumerate(paras):
        words = len(p.split())
        if words < 60 or words > 110:
            raise ValueError(f"Paragraph {idx+1} in {page_name} has {words} words (expected 60-110 words). Text: {p[:60]}...")

# -----------------------------------------------------------------------------
# BUILDERS FOR EACH PAGE
# -----------------------------------------------------------------------------

def build_index():
    # Assets 1, 2, 3, 4, 5, 6
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aperture Castle | Haute Horlogerie &amp; Mechanical Watchmaking Atelier</title>
<meta name="description" content="Discover Aperture Castle: Boston's premier mechanical watchmaking atelier. High-complication chronometers, tourbillons, hand-finishing, and private collector viewings.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/index.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Aperture Castle | Haute Horlogerie &amp; Mechanical Watchmaking Atelier">
<meta property="og:description" content="Boston horological atelier dedicated to precision mechanical calibers, artisanal hand-finishing, and private collector consultations.">
<meta property="og:url" content="https://{DOMAIN}/index.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_1.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("index.html")}
<main id="main">

<section class="page-hero">
  <img src="assets/images/aperturecastle_asset_1.jpg" alt="Precision hand-finished chronometer dial with flame-blued hands and applied indices" width="1400" height="900" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Boston Horological Atelier</nav>
    <h1>We curate mechanical timepieces the way they were meant to be experienced</h1>
    <p>Aperture Castle is an independent Boston horological atelier founded on three non-negotiable standards: mechanical calibers of verified chronometric provenance, transparent up-front curatorial valuation, and private viewings conducted by credentialed watchmakers.</p>
    <div style="display:flex;gap:16px;margin-top:28px;flex-wrap:wrap">
      <a class="btn btn-accent" href="booking.html">Reserve Salon Viewing</a>
      <a class="btn btn-ghost" href="products.html">Explore Collection</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Atelier Origin</span>
      <h2>Born from frustration with commercial watch showcases</h2>
      <p>Aperture Castle emerged from a universal collector grievance. Walk into an ordinary retail boutique or secondary platform, navigate opaque waiting lists, endure condescending sales tactics, and acquire a timepiece whose service history and balance amplitude remain completely unknown. Passionate collectors deserve genuine horological transparency.</p>
      <p>We established our atelier in Boston's Financial District to treat horology as fine art rather than retail merchandising. We maintain an exacting portfolio of twelve master caliber families, guaranteeing that every balance spring, pallet fork, and escapement receives meticulous inspection on our acoustic timegraphers prior to private presentation.</p>
      <p>The name reflects our dual commitment: the camera aperture representing optical clarity into micro-mechanics, and the castle denoting our fortified vault of horological heritage and enduring chronometric longevity.</p>
    </div>
    <img src="assets/images/aperturecastle_asset_2.jpg" alt="Extreme macro of decorated mechanical caliber showing perlage bridges, rubies, and polished gear teeth" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Horological Matrix</span><h2 style="color:#fff">Exacting chronometric tolerances, rigorously documented</h2></div></div>
    <div class="numbers">
      <div class="number"><b>28,800</b><span>oscillations per hour standard frequency across our core calibers</span></div>
      <div class="number"><b>300-point</b><span>mechanical, cosmetic, and water resistance inspection on each piece</span></div>
      <div class="number"><b>5-position</b><span>dynamic regulation verifying chronometer rate deviation under &plusmn;2 sec/day</span></div>
      <div class="number"><b>15 hours</b><span>of staffed horological advisory desk, every day of the calendar year</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img src="assets/images/aperturecastle_asset_3.jpg" alt="Horologist workbench arrangement with beryllium copper tweezers, precision screwdrivers, and loupe" width="1000" height="667" loading="lazy">
    <div>
      <span class="kicker">Bench Integrity</span>
      <h2>What happens before a timepiece enters our vault</h2>
      <p>When a mechanical timepiece arrives at One International Place, it immediately undergoes ultrasonic demagnetization and diagnostic timing analysis across five resting positions and three temperature curves. Our master watchmakers disassemble cases to inspect movement bridges for microscopic wear, pivot friction, and lubricant degradation.</p>
      <p>Every gear train wheel, escape teeth chamfer, and balance wheel jewel receives hand-applied synthetic micro-lubricants under binocular microscopes. If any component deviates from Geneva seal tolerances, it is recalibrated or replaced with original manufacture parts without compromise.</p>
      <p>Finally, we produce an authenticated physical Horological Passport for each watch, complete with high-resolution movement macrographs, timing delta printouts, and pressure testing certificates delivered directly to the collector.</p>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="wrap">
    <div class="sec-center"><span class="kicker">Our Principles</span><h2>The Three Castle Promises</h2></div>
    <div class="values">
      <div class="value"><h3>Authentic Calibers Only</h3><p>Every watch in our custody houses an authentic mechanical heart. We verify movement serials, bridge bevels, and escapement architecture against manufacturer archives prior to offering.</p></div>
      <div class="value"><h3>Transparent Provenance</h3><p>No arbitrary retail premiums or undisclosed restorations. Every quote itemizes baseline horological valuation, overhaul history, and included curatorial protections line by line.</p></div>
      <div class="value"><h3>Watchmakers, Not Salesmen</h3><p>Our consultation desk is staffed by practicing horologists who understand hairspring terminal curves, column wheels, and balance inertia. Call, and an artisan answers.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Complication Mastery</span>
      <h2>The Gravity-Defying Tourbillon &amp; Chronograph Arts</h2>
      <p>The tourbillon remains the pinnacle of mechanical compensating craftsmanship. By rotating the balance spring, pallet fork, and escape wheel inside a lightweight cage once every sixty seconds, our tourbillon calibers cancel positional gravity errors with hypnotic visual grace.</p>
      <p>Similarly, our column-wheel chronographs represent tactile micro-engineering perfection. The crisp mechanical snap of the reset hammer, the silky actuation of lateral clutches, and the surgical subdivision of seconds down to one-eighth increments embody centuries of horological evolution.</p>
    </div>
    <img src="assets/images/aperturecastle_asset_4.jpg" alt="Hand-crafted tourbillon complication carriage rotating within an Haute Horlogerie mechanical movement" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Featured Complications</span><h2 style="color:#fff">Selected Masterpieces from the Castle Vault</h2></div></div>
    <div class="timepiece-grid">
      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_5.jpg" alt="Classic tri-compax column-wheel chronograph wristwatch" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">High Complication</span>
          <h3>Caliber AC-720 Split Chrono</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Column-wheel lateral clutch chronograph with 30-minute register and tachymeter scale.</p>
          <div class="timepiece-specs">
            <span>Power Reserve: 52 hrs</span>
            <span>Frequency: 28,800 vph</span>
            <span>Jewels: 31 Rubies</span>
            <span>Regulation: &plusmn;1.5 s/d</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">Viewing Tier I</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>
      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_6.jpg" alt="Free-sprung balance wheel and Breguet overcoil hairspring oscillating at 28800 vph" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Chronometer</span>
          <h3>Caliber AC-104 Observatory</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Free-sprung Glucydur balance with white gold inertia weights and hand-curved Breguet hairspring.</p>
          <div class="timepiece-specs">
            <span>Power Reserve: 72 hrs</span>
            <span>Frequency: 21,600 vph</span>
            <span>Jewels: 25 Rubies</span>
            <span>Regulation: &plusmn;1.0 s/d</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">Viewing Tier II</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>
      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_17.jpg" alt="Traditional column-wheel chronograph caliber showing bevelled operating levers" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Column-Wheel Caliber</span>
          <h3>Caliber AC-17 Heritage Chrono</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Traditional lateral clutch column-wheel chronograph caliber with hand-chamfered steel operating levers.</p>
          <div class="timepiece-specs">
            <span>Power Reserve: 65 hrs</span>
            <span>Frequency: 28,800 vph</span>
            <span>Jewels: 28 Rubies</span>
            <span>Regulation: &plusmn;2.0 s/d</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">Viewing Tier I</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:900px">
    <div class="prose">
      <h2>Who We Serve</h2>
      <p>Our Boston atelier caters to discerning individuals united by an appreciation for mechanical permanence. Discerning collectors seeking rare reference calibers with documented provenance. Executives who require an impeccably regulated chronometer for high-stakes international affairs. And connoisseurs celebrating career milestones who desire an heirloom timepiece that will tick reliably for subsequent generations.</p>
      <h2>Responsible Horological Stewardship</h2>
      <p>We preserve horological history through active stewardship. Every antique or pre-owned caliber entering our care is preserved with period-correct oils and techniques, resisting the destructive over-polishing common in commercial auctions. We preserve original case chamfers, patinated tritium dials, and sharp case bevels so historical integrity remains inviolate.</p>
      <h2>Initiate Private Consultation</h2>
      <p>Have questions regarding caliber regulation, private salon reservations, or curatorial acquisition? Visit our Boston salon at One International Place, Suite 3100, telephone our horological desk at <a href="tel:{PHONE.replace('-', '')}">{PHONE}</a>, or submit an inquiry through our <a href="contact.html">contact page</a>. We examine every communication with dedicated artisan attention.</p>
    </div>
  </div>
</section>

<section class="section-tight" style="background:var(--surface);border-top:1px solid var(--surface-border)">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:24px">
    <div>
      <h3 style="font-family:var(--font-heading);font-size:1.6rem;color:#fff;margin-bottom:6px">Experience Haute Horlogerie in Person</h3>
      <p style="color:var(--text-muted)">Private viewings by appointment at our Financial District salon. No high-pressure sales, only micro-mechanical excellence.</p>
    </div>
    <div style="display:flex;gap:12px">
      <a class="btn btn-ghost" href="tel:{PHONE.replace('-', '')}">Call {PHONE}</a>
      <a class="btn btn-accent" href="booking.html">Book Private Viewing</a>
    </div>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_about():
    # Assets 7, 8, 9, 10
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Heritage &amp; Philosophy | Aperture Castle Horological Atelier</title>
<meta name="description" content="Discover the philosophy, watchmaking bench craftsmanship, and independent horological heritage behind Aperture Castle in Boston.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/about.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Heritage &amp; Philosophy | Aperture Castle">
<meta property="og:description" content="Meet Aperture Castle: Boston's independent horological atelier preserving hand-finishing, acoustic regulation, and mechanical excellence.">
<meta property="og:url" content="https://{DOMAIN}/about.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_7.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("about.html")}
<main id="main">

<section class="page-hero">
  <img src="assets/images/aperturecastle_asset_7.jpg" alt="Antique hand-engraved pocket watch movement exhibiting Geneva stripes and gold chatons" width="1400" height="900" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Heritage &amp; Philosophy</nav>
    <h1>We honor mechanical timekeeping as living engineering art</h1>
    <p>Aperture Castle was created to restore reverence to mechanical watchmaking. In an era dominated by disposable quartz chips and digital screens, we protect the tactile soul of balance wheels, hairsprings, and hand-chamfered steel bridges.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">The Founding Vision</span>
      <h2>A sanctuary for purists of micro-mechanics</h2>
      <p>Our guild was founded in Boston by watchmakers and lifelong collectors who grew weary of commercialized horology. Modern luxury boutiques frequently obscure the mechanical realities of their timepieces behind celebrity ambassadors and fabricated scarcity, leaving patrons uninformed about actual movement finishing or chronometric performance.</p>
      <p>We designed Aperture Castle as an unpretentious atelier where collectors converse directly with the artisans who regulate their balances. We maintain a focused archive of verified mechanical references, allowing us to dedicate hundreds of bench hours to each individual caliber rather than rushing high-volume commercial turnover.</p>
      <p>Every watch in our custody reflects genuine historical discipline: steel components hand-beveled with gentian wood sticks, jewels seated in mirror-polished chatons, and balance springs calibrated by ear and acoustic sensor.</p>
    </div>
    <img src="assets/images/aperturecastle_asset_8.jpg" alt="Master watchmaker carefully examining train wheel pivot alignment under optical loupe" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Guild Metrics</span><h2 style="color:#fff">Precision Bench Milestones</h2></div></div>
    <div class="numbers">
      <div class="number"><b>45+</b><span>years of combined master bench experience across our horological team</span></div>
      <div class="number"><b>0.002mm</b><span>maximum allowable train pivot tolerance across our movement restorations</span></div>
      <div class="number"><b>100%</b><span>original Swiss, German, and Anglo-Saxon authentic components utilized</span></div>
      <div class="number"><b>3 Year</b><span>comprehensive mechanical chronometric warranty accompanying every piece</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img src="assets/images/aperturecastle_asset_9.jpg" alt="Hand-stitched full-grain French calfskin watch strap crafted with bevelled edges on cutting bench" width="1000" height="667" loading="lazy">
    <div>
      <span class="kicker">Artisanal Accessories</span>
      <h2>Hand-stitched saddle leather and bespoke ergonomics</h2>
      <p>A master caliber requires an equally distinguished binding. We partner with heritage French and Italian tanneries to handcraft custom straps from vegetable-tanned barenia calfskin, bridle leather, and organic canvas. Each strap is hand-pricked and sewn with beeswaxed linen thread using traditional two-needle saddle stitching.</p>
      <p>Our edge finishing requires seven stages of heating, waxing, and burnishing with natural gum tragacanth, ensuring supple comfort against the wrist and resistance to climatic humidity. Hardware buckles are individually machined from marine-grade 316L stainless steel with hand-brushed facets.</p>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="wrap">
    <div class="sec-center"><span class="kicker">Horological Credo</span><h2>Our Three Enduring Commitments</h2></div>
    <div class="values">
      <div class="value"><h3>Radical Mechanical Honesty</h3><p>We openly disclose every modification, service record, and amplitude reading. If an escapement shows natural age, we celebrate its patina rather than artificially masking its history.</p></div>
      <div class="value"><h3>Reversible Preservation</h3><p>Our horologists adhere to strict museum conservation ethics. Any restoration performed on vintage calibers uses fully reversible methods, preserving historical material for future centuries.</p></div>
      <div class="value"><h3>Lifelong Stewardship</h3><p>When you acquire a timepiece through Aperture Castle, our atelier remains your lifelong technical partner for periodic lubrication, water resistance testing, and timing calibration.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Open Architecture</span>
      <h2>The Poetry of Skeletonized and Openworked Movements</h2>
      <p>Skeletonization represents the ultimate test of artisanal finishing. By paring away all non-structural brass and steel from the mainplate and bridges, the watchmaker transforms a functional machine into a suspended kinetic sculpture.</p>
      <p>Every exposed interior angle must be beveled by hand at a precise 45-degree inclination, followed by diamond paste polishing to produce mirror-like specular reflections. When viewed through sapphire crystal, the viewer witnesses the continuous breathing of the hairspring and the hypnotic rotation of the train gears.</p>
    </div>
    <img src="assets/images/aperturecastle_asset_10.jpg" alt="Openworked skeleton mechanical caliber revealing mainspring winding barrel and escapement geometry" width="1000" height="667" loading="lazy">
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_products():
    # Assets 11, 12, 13, 14, 15, 16
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Horological Collection | Aperture Castle Watchmakers</title>
<meta name="description" content="Explore our curated collection of Haute Horlogerie mechanical watches: chronographs, marine chronometers, perpetual astronomical calibers, and dress complications.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/products.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="The Horological Collection | Aperture Castle">
<meta property="og:description" content="Explore handcrafted chronometers, column-wheel chronographs, and perpetual calendar masterpieces available for private viewing in Boston.">
<meta property="og:url" content="https://{DOMAIN}/products.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_11.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("products.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Collection &amp; Complications</nav>
    <h1>The Vault Collection</h1>
    <p>Each timepiece in our Boston vault has undergone acoustic timing analysis, caliber certification, and multi-position regulation. Available for private collector viewings and curatorial acquisition.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="timepiece-grid">

      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_11.jpg" alt="Zaratsu-finished stainless steel watch case exhibiting distortion-free mirror-polished chamfers" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Steel Chronometer</span>
          <h3>Aperture Castle Sovereign 39</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Distortion-free Zaratsu polished steel case with hand-applied faceted markers and box sapphire crystal.</p>
          <div class="timepiece-specs">
            <span>Caliber: AC-28A Auto</span>
            <span>Case: 39mm &times; 10.4mm</span>
            <span>Power Reserve: 60 hrs</span>
            <span>Water Resist: 100m</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">$350 / session</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>

      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_12.jpg" alt="Professional maritime chronometer wristwatch with ceramic rotating bezel and luminous markers" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Maritime Explorer</span>
          <h3>Aperture Castle Seafarer 300</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">High-grade marine chronometer with 120-click ceramic rotating bezel and helium escape valve.</p>
          <div class="timepiece-specs">
            <span>Caliber: AC-90 Marine</span>
            <span>Case: 41mm Titanium</span>
            <span>Power Reserve: 70 hrs</span>
            <span>Water Resist: 300m</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">$400 / session</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>

      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_13.jpg" alt="Heavy gold oscillating winding rotor decorated with traditional sunray guilloche engraving" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Haute Horlogerie</span>
          <h3>Aperture Castle Chrono-Rotor</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Solid 22-carat gold guilloche oscillating weight providing high winding efficiency over hand-anglage bridges.</p>
          <div class="timepiece-specs">
            <span>Caliber: AC-500 Rotor</span>
            <span>Case: 40mm Rose Gold</span>
            <span>Power Reserve: 72 hrs</span>
            <span>Jewels: 35 Rubies</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">$550 / session</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>

      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_14.jpg" alt="Bespoke thermally-blued steel leaf hands resting upon watchmaker inspection cushion" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Artisan Atelier</span>
          <h3>Aperture Castle Blued Feuille</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Thermally flame-blued leaf hands heat-treated to exactly 295&deg;C over an ivory grand feu enamel dial.</p>
          <div class="timepiece-specs">
            <span>Caliber: AC-11 Manual</span>
            <span>Case: 38mm White Gold</span>
            <span>Power Reserve: 48 hrs</span>
            <span>Dial: Enamel Grand Feu</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">$480 / session</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>

      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_15.jpg" alt="Precision watchmaker applying synthetic micro-lubrication to synthetic ruby pallet fork jewels" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Master Complication</span>
          <h3>Aperture Castle Tourbillon One</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">One-minute flying tourbillon carriage weighing a mere 0.28 grams, regulated in six positional axes.</p>
          <div class="timepiece-specs">
            <span>Caliber: AC-TB01 Flying</span>
            <span>Case: 41mm Platinum</span>
            <span>Power Reserve: 80 hrs</span>
            <span>Regulation: &plusmn;0.8 s/d</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">$750 / session</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>

      <div class="timepiece-card">
        <img class="timepiece-img" src="assets/images/aperturecastle_asset_16.jpg" alt="Grand horological complication dial showcasing moonphase aperture, calendar chapter ring, and applied indices" loading="lazy">
        <div class="timepiece-body">
          <span class="timepiece-badge">Astronomical</span>
          <h3>Aperture Castle Lunar Quantieme</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Astronomical perpetual calendar with hand-painted lapis lazuli moon phase accurate for 122 years.</p>
          <div class="timepiece-specs">
            <span>Caliber: AC-PC Astronomical</span>
            <span>Case: 40mm Yellow Gold</span>
            <span>Power Reserve: 68 hrs</span>
            <span>Moon Error: 1 day / 122y</span>
          </div>
          <div class="timepiece-footer">
            <span class="timepiece-tier">$620 / session</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Reserve</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Technical Verification</span><h2 style="color:#fff">The Aperture Castle Inspection Standard</h2></div></div>
    <div class="numbers">
      <div class="number"><b>0 to +4</b><span>seconds per day allowable chronometer rate tolerance</span></div>
      <div class="number"><b>270&deg;+</b><span>minimum balance amplitude maintained across full 48-hour reserve</span></div>
      <div class="number"><b>0.2ms</b><span>maximum permissible beat error verified on electronic vibrograf</span></div>
      <div class="number"><b>10 Bar</b><span>wet and dry vacuum chamber pressure testing on all sport cases</span></div>
    </div>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_booking():
    # Assets 17, 18
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Book a Private Salon Viewing | Aperture Castle Boston</title>
<meta name="description" content="Reserve a private horological viewing session at our Boston atelier in four simple steps with real-time curatorial estimate. No online payment taken.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/booking.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Book a Private Salon Viewing | Aperture Castle">
<meta property="og:description" content="Reserve a private horological viewing session at our Boston Financial District atelier in four easy steps.">
<meta property="og:url" content="https://{DOMAIN}/booking.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_17.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("booking.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Book Viewing</nav>
    <h1>Reserve Your Private Salon Viewing</h1>
    <p>Four quick steps, a live curatorial estimate as you proceed, and no online payment taken. Our senior horologist confirms vault availability and replies within two business hours.</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap booking-layout">
    <form id="booking-form" novalidate>
      <ol class="stepper" aria-label="Booking progress">
        <li data-step="1" class="active"><b>Step 1</b>Session details</li>
        <li data-step="2"><b>Step 2</b>Timepiece</li>
        <li data-step="3"><b>Step 3</b>Curatorial add-ons</li>
        <li data-step="4"><b>Step 4</b>Collector info</li>
      </ol>

      <fieldset class="b-panel active" data-step="1" style="margin:0">
        <h2>When and where would you like to meet?</h2>
        <div class="form-grid">
          <div class="field"><label for="b-loc">Viewing Location</label><select id="b-loc"><option>Boston Financial District Hub (One International Place)</option><option>Private Courier Handover (Greater Boston Area)</option><option>Private Bank Vault Meeting (By Pre-Clearance)</option></select></div>
          <div class="field"><label for="b-party">Party Size</label><select id="b-party"><option>1 Collector (Private Bench Session)</option><option>2 Guests (Executive Consultation)</option><option>3-4 Guests (Private Horological Saloon)</option></select></div>
          <div class="field"><label for="b-date">Preferred Date</label><input type="date" id="b-date" required><span class="err-msg">Please select an upcoming date.</span></div>
          <div class="field"><label for="b-time">Appointment Time</label><input type="time" id="b-time" value="11:00" step="1800"></div>
          <div class="field"><label for="b-duration">Consultation Focus</label><select id="b-duration"><option value="3">Full Horological Bench Review (3 hours)</option><option value="2">Specific Complication Evaluation (2 hours)</option><option value="5">Multi-Timepiece Portfolio Curatorial Session (Full Day)</option></select></div>
          <div class="field"><label for="b-interest">Primary Interest</label><select id="b-interest"><option>Acquisition / Collection Expansion</option><option>Vintage Caliber Authentication &amp; Servicing</option><option>Bespoke Commission &amp; Dial Customization</option></select></div>
        </div>
        <p style="font-size:.88rem;color:var(--text-muted);margin:16px 0 0">Private salon viewings include white-glove loupe inspection, acoustic rate readouts, and refreshments in our executive library.</p>
        <div class="b-nav"><span></span><button type="button" class="btn btn-accent" data-next>Select Timepiece Class &rarr;</button></div>
      </fieldset>

      <fieldset class="b-panel" data-step="2" style="margin:0">
        <h2>Select caliber category</h2>
        <p style="color:var(--text-muted)">Compare specifications and complications on our <a href="products.html">collection page</a>.</p>
        <div class="vehicle-pick" id="vehicle-pick" role="group" aria-label="Timepiece classes">
          <div class="pick-card selected" data-rate="450">
            <h4>Chrono Complication Reserve</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Column-wheel chronographs and split-second timers. $450 base session.</p>
          </div>
          <div class="pick-card" data-rate="350">
            <h4>Steel Chronometer Sovereign</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Zaratsu polished cases and high-frequency chronometers. $350 base session.</p>
          </div>
          <div class="pick-card" data-rate="550">
            <h4>Astronomical &amp; Perpetual</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Lapis lazuli moonphases and multi-year calendar mechanisms. $550 base session.</p>
          </div>
          <div class="pick-card" data-rate="750">
            <h4>Haute Tourbillon Carriage</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Hand-beveled flying tourbillons regulated to observatory specs. $750 base session.</p>
          </div>
        </div>
        <div class="b-nav"><button type="button" class="btn btn-ghost" data-prev>&larr; Back</button><button type="button" class="btn btn-accent" data-next>Add Curatorial Extras &rarr;</button></div>
      </fieldset>

      <fieldset class="b-panel" data-step="3" style="margin:0">
        <h2>Optional curatorial services</h2>
        <p style="color:var(--text-muted)">All optional. Complete vault liability coverage and multi-axis demagnetization are already included.</p>
        <div class="extras" id="extras-list">
          <div class="extra-item">
            <label class="check"><input type="checkbox" value="120"> <span><b>Archival Horological Passport</b><br><small style="color:var(--text-muted)">Bound physical dossier with macrographs, timing delta certificates, and historical records.</small></span></label>
            <span style="font-weight:700;color:var(--accent)">+$120</span>
          </div>
          <div class="extra-item">
            <label class="check"><input type="checkbox" value="180"> <span><b>Bespoke Saddle Leather Strap Fitting</b><br><small style="color:var(--text-muted)">Hand-stitched French barenia calfskin strap custom sized to your wrist by our leather artisan.</small></span></label>
            <span style="font-weight:700;color:var(--accent)">+$180</span>
          </div>
          <div class="extra-item">
            <label class="check"><input type="checkbox" value="95"> <span><b>Acoustic Vibrograf Rate Calibration Printout</b><br><small style="color:var(--text-muted)">Full electronic diagnostic report across 5 positions, amplitude decay, and beat error graphs.</small></span></label>
            <span style="font-weight:700;color:var(--accent)">+$95</span>
          </div>
        </div>
        <div class="b-nav"><button type="button" class="btn btn-ghost" data-prev>&larr; Back</button><button type="button" class="btn btn-accent" data-next>Collector Details &rarr;</button></div>
      </fieldset>

      <fieldset class="b-panel" data-step="4" style="margin:0">
        <h2>Collector coordinates</h2>
        <div class="form-grid">
          <div class="field"><label for="b-name">Full name (for vault pass)</label><input id="b-name" autocomplete="name" required><span class="err-msg">Please enter your full legal name.</span></div>
          <div class="field"><label for="b-email">Email</label><input id="b-email" type="email" autocomplete="email" required><span class="err-msg">Please enter a valid email.</span></div>
          <div class="field"><label for="b-phone">Mobile telephone</label><input id="b-phone" type="tel" autocomplete="tel" required><span class="err-msg">Please enter a reachable telephone number.</span></div>
          <div class="field"><label for="b-firm">Institutional / Collector affiliation (optional)</label><input id="b-firm" placeholder="e.g. Private Collector / Family Office"></div>
          <div class="field full"><label for="b-notes">Special requests or specific calibers of interest (optional)</label><textarea id="b-notes" placeholder="e.g. Interested in comparing column-wheel vs cam actuation, or vintage reference inspection…"></textarea></div>
          <div class="full"><label class="check"><input type="checkbox" id="b-terms"> <span>I confirm that I am at least 21 years of age, and I have read and agree to the <a href="cancellation-refund-policy.html" target="_blank">Cancellation &amp; Refund Policy</a>, <a href="terms-and-conditions.html" target="_blank">Terms &amp; Conditions</a>, and <a href="privacy-policy.html" target="_blank">Privacy Policy</a>.</span></label></div>
        </div>
        <div class="b-nav"><button type="button" class="btn btn-ghost" data-prev>&larr; Back</button><button type="submit" class="btn btn-accent" id="b-submit">Request Salon Reservation</button></div>
      </fieldset>
    </form>

    <aside class="summary" aria-labelledby="sum-title" aria-live="polite">
      <h2 id="sum-title">Curatorial Summary</h2>
      <div class="sum-car" id="sum-car">Chrono Complication Reserve</div>
      <ul class="sum-lines" id="sum-trip">
        <li><span>Viewing Salon:</span> <b>Boston Financial Suite</b></li>
        <li><span>Duration:</span> <b>Full Bench Session</b></li>
      </ul>
      <ul class="sum-lines" id="sum-lines" style="margin-top:12px">
        <li><span>Base curatorial session:</span> <b>$450</b></li>
        <li><span>Vault security &amp; insurance:</span> <b>Included</b></li>
      </ul>
      <div class="sum-total"><span>Estimated total</span><b id="sum-total">$450</b></div>
      <p class="sum-note">No payment taken online. A refundable security deposit hold is authorized at reception. Our concierge confirms your vault access within two business hours.</p>
    </aside>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap split">
    <div>
      <span class="kicker">Security &amp; Timing Guarantee</span>
      <h2>State-of-the-Art Horological Diagnostics</h2>
      <p>Every timepiece presented during your salon session is verified on the bench in your presence using our high-precision electronic vibrograf acoustic sensor and Swiss-made digital microscopes.</p>
      <p>You will inspect the pallet stone clearances, the amplitude of the balance wheel, and the hairspring concentricity firsthand, guided by our senior watchmakers with total transparency.</p>
    </div>
    <img src="assets/images/aperturecastle_asset_18.jpg" alt="Electronic watch timing machine measuring chronometer daily rate balance amplitude and beat error" width="1000" height="667" loading="lazy">
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_contact():
    # Asset 19
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contact Us | Aperture Castle Horological Atelier Boston</title>
<meta name="description" content="Contact Aperture Castle by phone, email, or visit our Boston Financial District atelier at One International Place, Suite 3100. Open daily 7 am – 10 pm ET.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/contact.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Contact Us | Aperture Castle Boston">
<meta property="og:description" content="Contact Aperture Castle watchmakers in Boston Financial District. Phone, email, salon address, and inquiry form.">
<meta property="og:url" content="https://{DOMAIN}/contact.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_19.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
<script type="application/ld+json">
{{"@context": "https://schema.org", "@type": "JewelryStore", "name": "Aperture Castle Horological Atelier", "url": "https://{DOMAIN}/", "telephone": "{PHONE}", "email": "{EMAIL}", "priceRange": "$$$$", "address": {{"@type": "PostalAddress", "streetAddress": "One International Place, Suite 3100", "addressLocality": "Boston", "addressRegion": "MA", "postalCode": "02110", "addressCountry": "US"}}, "openingHoursSpecification": [{{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "07:00", "closes": "22:00"}}]}}
</script>
</head>
<body>
{get_header("contact.html")}
<main id="main">

<section class="page-hero">
  <img src="assets/images/aperturecastle_asset_19.jpg" alt="Handcrafted walnut watch collector presentation box lined with velvet and certificate" width="1400" height="900" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Contact Us</nav>
    <h1>Connect with Our Horological Desk</h1>
    <p>Questions regarding a timepiece in our vault, a bespoke commission, or scheduling a private viewing? Call our desk, send an inquiry, or visit our Boston Financial District atelier.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="contact-card">
      <h2>Reach Our Boston Salon</h2>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg></span><div><small>Atelier Address</small><span>{ADDR}</span></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg></span><div><small>Telephone</small><a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg></span><div><small>Concierge &amp; Inquiries</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></span><div><small>Salon Reservations</small><a href="mailto:reservations@{DOMAIN}">reservations@{DOMAIN}</a></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><div><small>Atelier Hours</small><span>Desk &amp; Salon: {DESK_HOURS}<br>Private Vault Access: By Confirmed Appointment</span></div></div>
    </div>
    <form class="form-card" id="contact-form" novalidate>
      <h2 style="font-size:1.4rem">Transmit an Inquiry</h2>
      <p style="color:var(--text-muted);font-size:0.92rem;margin-bottom:20px">We reply to every collector transmission within one business day. For same-day salon requests, please telephone directly.</p>
      <div class="form-grid">
        <div class="field"><label for="c-name">Your Full Name</label><input id="c-name" autocomplete="name" required><span class="err-msg">Please provide your name.</span></div>
        <div class="field"><label for="c-email">Email Address</label><input id="c-email" type="email" autocomplete="email" required><span class="err-msg">Please provide a valid email.</span></div>
        <div class="field"><label for="c-phone">Phone Number (optional)</label><input id="c-phone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="c-topic">Nature of Inquiry</label><select id="c-topic" required><option value="">Choose a topic</option><option>Private Salon Viewing</option><option>Caliber Authentication &amp; Valuation</option><option>Bespoke Commission / Customization</option><option>Restoration &amp; Movement Overhaul</option><option>General Concierge Inquiry</option></select><span class="err-msg">Please select an inquiry topic.</span></div>
        <div class="field full"><label for="c-message">Message</label><textarea id="c-message" required rows="4" placeholder="Please describe the reference, complication, or assistance you require…"></textarea><span class="err-msg">Please include details regarding your request.</span></div>
        <div class="full field"><label class="check" style="color:var(--text-main);font-size:.9rem"><input type="checkbox" required id="c-consent"> <span>I agree that Aperture Castle Horological Atelier may utilize these details to reply to my inquiry, in strict accordance with the <a href="privacy-policy.html">Privacy Policy</a>.</span></label><span class="err-msg">Please accept the consent terms.</span></div>
        <div class="full"><button class="btn btn-accent" type="submit">Transmit Message</button></div>
      </div>
    </form>
  </div>
</section>

<section class="section-tight section-white">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Directions &amp; Reception</span><h2>Our Boston Financial District Hub</h2><p>Located at One International Place, Suite 3100, Boston, MA 02110. Accessible via South Station (Red Line, Silver Line, Commuter Rail) or Aquarium Station (Blue Line). Valet parking is available at the International Place garage on Purchase Street.</p></div></div>
    <iframe class="map-frame" title="Map showing One International Place, Boston" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=One+International+Place,+Boston,+MA+02110&amp;output=embed"></iframe>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_faq():
    # Asset 20
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Collector &amp; Horological FAQ | Aperture Castle Boston</title>
<meta name="description" content="Frequently asked questions concerning mechanical watch viewings, chronometer regulation, security deposits, and caliber maintenance at Aperture Castle.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/faq.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Collector &amp; Horological FAQ | Aperture Castle">
<meta property="og:description" content="Answers to common collector questions regarding private salon appointments, chronometer certifications, and vault security.">
<meta property="og:url" content="https://{DOMAIN}/faq.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_20.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("faq.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Collector FAQ</nav>
    <h1>Horological &amp; Atelier FAQ</h1>
    <p>Essential guidance on private salon appointments, caliber authentication standards, security protocols, and lifelong mechanical maintenance.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Common Inquiries</span>
      <h2>Everything you need to know about our salon</h2>
      <p>Whether you are attending your first bench consultation or expanding a seasoned multi-complication collection, we believe in providing comprehensive clarity prior to your appointment.</p>
      <p>Review our core policies below or speak directly with our concierge team at <a href="tel:{PHONE.replace('-', '')}">{PHONE}</a>.</p>
    </div>
    <img src="assets/images/aperturecastle_asset_20.jpg" alt="Micro-knurled screw-down winding crown engraved with atelier emblem under studio light reflection" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap" style="max-width:900px">
    <div class="prose">
      <h2>1. Salon Appointments &amp; Private Viewings</h2>
      <h3>How do I schedule a private viewing of a specific reference?</h3>
      <p>Reservations can be requested via our <a href="booking.html">online booking stepper</a> or by calling our desk. Our concierge will review vault availability, pull the requested calibers from our safe, and ensure an authenticated timing report is prepared for your arrival.</p>
      
      <h3>Is there any obligation to purchase during a private viewing?</h3>
      <p>Zero obligation whatsoever. Our salon viewings are curated educational experiences designed for mechanical appreciation. You will be seated with a trained watchmaker who will explain movement architecture, hand-finishing, and timing metrics without sales pressure.</p>

      <h2>2. Caliber Authentication &amp; Provenance</h2>
      <h3>How does Aperture Castle verify timepiece authenticity?</h3>
      <p>Every piece undergoes forensic examination by our senior watchmakers. We verify bridge beveling, serial engravings, wheel tooth profiles, and caliber stamps under high magnification, cross-referencing archives with manufacturer heritage departments.</p>

      <h3>What documentation accompanies an acquired timepiece?</h3>
      <p>Every acquisition includes the official Aperture Castle Horological Passport. This document details the watch's serial number, full overhaul date, acoustic vibrograf timing metrics across five positions, balance amplitude records, and water-resistance pressure logs.</p>

      <h2>3. Security Deposits &amp; Cancellation Protocols</h2>
      <h3>Why is a card guarantee required for booking a viewing?</h3>
      <p>Because our master horologists dedicate hours to retrieving rare calibers from off-site secure vaults and performing pre-session acoustic regulations, reservations require a card guarantee. No charge is made online; fees only apply for unnotified no-shows in accordance with our <a href="cancellation-refund-policy.html">Cancellation Policy</a>.</p>

      <h3>How can I reschedule or cancel my salon session?</h3>
      <p>Appointments may be rescheduled or cancelled without fee up to 48 hours prior to your scheduled time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> or telephoning our desk. Inside 48 hours, late cancellation provisions apply.</p>
    </div>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

# -----------------------------------------------------------------------------
# POLICY PAGES BUILDERS WITH 60-110 WORDS / PARAGRAPH
# -----------------------------------------------------------------------------

def build_privacy():
    p1 = "This Privacy Policy articulates the comprehensive data stewardship protocols, digital telemetry parameters, and confidential client privacy protections maintained by Aperture Castle Horological Atelier LLC across our official web portal. We recognize that collectors of haute horlogerie timepieces require absolute confidentiality regarding their curatorial inquiries, salon reservations, and mechanical acquisition preferences. This document transparently explains what minimal data elements we collect, how information is encrypted, and your rights under applicable United States data protection regulations."
    p2 = "When you browse our horological archives, submit consultation inquiries, or reserve private viewing appointments at our Boston salon, we may collect personal identifying coordinates including your full name, telephone number, verified email address, and general curatorial preferences. We never harvest sensitive financial account numbers or biometric telemetry across this web interface. All consultation records are retained solely to fulfill your specific horological viewing requests and facilitate direct communication with our senior watchmaking staff."
    p3 = "Our web servers automatically record non-identifying technical telemetry to preserve server security, optimize computational efficiency, and identify navigational bottlenecks across mobile and desktop environments. This telemetry comprises internet protocol addresses, browser user agent strings, referring domain sources, operating system versions, and timestamp logs of viewed complication pages. This diagnostic data is aggregated without connecting telemetry records to individual collector names or physical residential addresses, ensuring your private browsing remains confidential."
    p4 = "Aperture Castle deploys minimal, strictly essential session cookies to enable smooth digital navigation, preserve salon reservation parameters as you advance through our interactive stepper, and verify security tokens during form transmissions. We do not deploy invasive third-party cross-domain behavioral tracking cookies, commercial advertising beacons, or consumer profiling pixels. Any analytical telemetry utilized on our domain is anonymized to assess overall site load performance and resolve technical interface rendering errors across various devices."
    p5 = "We enforce robust administrative, architectural, and cryptographic countermeasures to protect all submitted personal coordinates from unauthorized interception, illicit data harvesting, or accidental disclosure. Digital records are transmitted via modern Transport Layer Security encryption protocols and stored on hardened servers featuring multi-factor authentication and role-restricted access rights. Only credentialed concierge personnel and authorized horological directors possessing verified operational need are permitted access to private salon consultation records."
    p6 = "Under applicable federal and state data privacy legislation, including the Massachusetts Data Privacy Act and California Consumer Privacy Act, you maintain the legal entitlement to access, inspect, rectify, or request permanent deletion of your stored contact records. If you desire to review your personal records or withdraw communication consent, you may transmit a formal written demand to our administrative concierge. We will review and fulfill verified data subject requests within thirty calendar days without cost."
    p7 = "Aperture Castle maintains an ethical operational posture that strictly prohibits the monetization, sale, trade, or commercial leasing of client contact details to external marketing agencies, commercial broker networks, or unrelated merchant entities. We disclose client details solely to vetted technical service providers under binding confidentiality obligations, or when formally compelled by lawful governmental subpoenas, valid judicial search warrants, or mandatory statutory requirements under United States federal jurisdiction."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Institutional Privacy Policy, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, horological excellence, and lasting mutual trust with every collector who engages with our digital portal, reviews our complication archives, or reserves viewing experiences at our Boston Financial District salon rooms."
    p9 = f"Please direct all formal inquiries regarding this privacy framework to Aperture Castle Horological Atelier LLC, located at {ADDR}. For immediate verbal consultations regarding digital security safeguards or salon reservation records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "privacy-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Privacy Policy | Aperture Castle Horological Atelier</title>
<meta name="description" content="Institutional Privacy Policy for Aperture Castle Horological Atelier. Learn about our strict data stewardship, zero tracking sale policy, and security.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Privacy Policy | Aperture Castle">
<meta property="og:description" content="Privacy Policy governing collector data protection, encryption, and institutional contact coordinates for Aperture Castle in Boston.">
<meta property="og:url" content="https://{DOMAIN}/privacy-policy.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_1.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("privacy-policy.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Privacy Policy</nav>
    <h1>Institutional Privacy Policy</h1>
    <p>Last updated: September 29, 2026 &bull; Aperture Castle Horological Atelier LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#scope">1. Scope of Data Stewardship</a></li>
        <li><a href="#collection">2. Information Collection</a></li>
        <li><a href="#telemetry">3. Technical Telemetry</a></li>
        <li><a href="#cookies">4. Minimal Session Cookies</a></li>
        <li><a href="#security">5. Encryption &amp; Security</a></li>
        <li><a href="#rights">6. Collector Privacy Rights</a></li>
        <li><a href="#disclosure">7. Non-Monetization Policy</a></li>
        <li><a href="#inquiries">8. Administrative Inquiries</a></li>
        <li><a href="#contact-sec">9. Institutional Coordinates</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="scope">1. Scope of Data Stewardship</h2>
      <p class="ac-policy-p">{p1}</p>
      
      <h2 id="collection">2. Information Collection</h2>
      <p class="ac-policy-p">{p2}</p>

      <h2 id="telemetry">3. Technical Telemetry</h2>
      <p class="ac-policy-p">{p3}</p>

      <h2 id="cookies">4. Minimal Session Cookies</h2>
      <p class="ac-policy-p">{p4}</p>

      <h2 id="security">5. Encryption &amp; Security Protocols</h2>
      <p class="ac-policy-p">{p5}</p>

      <h2 id="rights">6. Collector Privacy Rights</h2>
      <p class="ac-policy-p">{p6}</p>

      <h2 id="disclosure">7. Strict Non-Monetization Policy</h2>
      <p class="ac-policy-p">{p7}</p>

      <h2 id="inquiries">8. Administrative Inquiries &amp; Transparency</h2>
      <p class="ac-policy-p">{p8}</p>

      <h2 id="contact-sec">9. Institutional Contact Coordinates</h2>
      <p class="ac-policy-p">{p9}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_terms():
    p1 = "These Terms and Conditions constitute a legally binding agreement between you and Aperture Castle Horological Atelier LLC regarding your access to this web portal, your reservation of private salon viewing appointments, and your acquisition of mechanical timepieces or horological restoration services. By browsing our digital archives, submitting curatorial viewing requests, or engaging our watchmaking staff, you confirm your unreserved acceptance of these provisions. If you disagree with any term, you must discontinue your use of our domain immediately."
    p2 = "Aperture Castle curates and restores exceptional mechanical timepieces featuring high-horology complications, including column-wheel chronographs, tourbillon carriages, and perpetual calendars. Because each mechanical caliber is hand-assembled with microscopic gears, balance springs, and natural ruby jewels, slight variations in daily chronometric rate deviation, power reserve duration, and cosmetic case chamfering reflect authentic hand craftsmanship. Such natural artisan variations do not constitute mechanical failure or breach of agreement."
    p3 = "Because our atelier prepares custom horological presentations, secures rare calibers from off-site bank vaults, and performs multi-position acoustic timing diagnostics specifically for scheduled sessions, private salon viewing appointments require a credit card guarantee. Your appointment is not legally confirmed until our concierge reviews your request and issues an authenticated reservation manifest by email. Patrons must arrive promptly at their scheduled Boston hour to ensure adequate bench time with our senior watchmaker."
    p4 = "Patrons seeking to reschedule or cancel a confirmed salon viewing must provide written or verbal notice to our concierge at least forty-eight hours prior to the scheduled hour. Because late cancellations prevent our artisans from offering high-security viewing slots to fellow collectors on our waiting roster, failure to attend without timely notice may incur late cancellation fees as outlined in our cancellation policy. We appreciate collector cooperation in preserving our disciplined bench calendar."
    p5 = "All visual photography, typography, technical caliber analyses, registered guild trademarks, and horological articles published on this web portal remain the exclusive intellectual property of Aperture Castle Horological Atelier LLC. You are granted a limited, revocable, non-exclusive license to inspect digital materials for personal, non-commercial purposes only. Any unauthorized reproduction, automated data scraping, commercial republishing, or digital distribution of our proprietary imagery is strictly prohibited under international copyright conventions."
    p6 = "Our proprietary balance regulation procedures, acoustic acoustic timing methodologies, and specialized synthetic micro-lubrication schedules constitute protected trade secrets of our watchmaking guild. Clients acquiring curated timepieces receive full legal ownership of the physical watch and accompanying Horological Passport, but acquire no intellectual property rights in our proprietary restoration procedures, custom tools, or registered guild trademarks. We vigorously defend our craftsmanship rights across domestic and global markets."
    p7 = "Aperture Castle maintains an atmosphere of quiet intellectual focus, historical appreciation, and mutual respect within our Boston Financial District atelier. We require all visitors to conduct themselves with appropriate decorum toward fellow patrons and our horological staff. Disruptive conduct, verbal disrespect, uncooperative behavior, or disregard for vault security protocols may result in immediate refusal of service and revocation of appointment privileges in accordance with salon safety standards."
    p8 = "While we welcome personal photography of completed timepieces during your private salon session, the operation of commercial video apparatus, intrusive high-intensity flash rigs, or unauthorized recording equipment that disrupts adjacent viewings is strictly forbidden without prior written authorization from management. We reserve the full managerial authority to decline service to any party whose demeanor undermines the professional environment of our premises. We thank all patrons for preserving our focused salon atmosphere."
    p9 = "These terms and conditions are governed by and construed in strict accordance with the laws of the Commonwealth of Massachusetts, United States, without regard to conflict of law principles. Any legal controversy, dispute, or claim arising from these terms or your engagement with Aperture Castle Horological Atelier shall be submitted to binding arbitration in Boston, Suffolk County, Massachusetts, under standard commercial rules of the American Arbitration Association."
    p10 = f"For formal legal correspondence regarding these terms and conditions, please direct written notices to Aperture Castle Horological Atelier LLC, {ADDR}. You may also contact our administrative office by telephone at {PHONE} or transmit electronic communications to our designated legal inbox at {EMAIL}. We remain dedicated to resolving all client inquiries with equity, professionalism, and thorough institutional care."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    check_paragraphs(paras, "terms-and-conditions.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Terms &amp; Conditions | Aperture Castle Horological Atelier</title>
<meta name="description" content="Terms and Conditions governing salon reservations, timepiece curation, and web portal access for Aperture Castle in Boston, Massachusetts.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Terms &amp; Conditions | Aperture Castle">
<meta property="og:description" content="Terms and Conditions for Aperture Castle Horological Atelier. Salon viewing rules, trade secrets, and arbitration details.">
<meta property="og:url" content="https://{DOMAIN}/terms-and-conditions.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_1.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("terms-and-conditions.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Terms &amp; Conditions</nav>
    <h1>Terms &amp; Conditions</h1>
    <p>Last updated: September 29, 2026 &bull; Aperture Castle Horological Atelier LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#agreement">1. Agreement to Terms</a></li>
        <li><a href="#craft">2. Hand-Crafted Timepieces</a></li>
        <li><a href="#reservations">3. Salon Reservations</a></li>
        <li><a href="#cancellations">4. Cancellation Notice</a></li>
        <li><a href="#ip">5. Intellectual Property</a></li>
        <li><a href="#trade-secrets">6. Trade Secrets</a></li>
        <li><a href="#conduct">7. Guest Salon Conduct</a></li>
        <li><a href="#photography">8. Photography Guidelines</a></li>
        <li><a href="#jurisdiction">9. Governing Law</a></li>
        <li><a href="#legal-notice">10. Legal Notice Address</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="agreement">1. Agreement to Terms</h2>
      <p class="ac-policy-p">{p1}</p>

      <h2 id="craft">2. Hand-Crafted Mechanical Timepieces</h2>
      <p class="ac-policy-p">{p2}</p>

      <h2 id="reservations">3. Salon Reservations &amp; Viewing Protocols</h2>
      <p class="ac-policy-p">{p3}</p>

      <h2 id="cancellations">4. Cancellation Notice &amp; Scheduling</h2>
      <p class="ac-policy-p">{p4}</p>

      <h2 id="ip">5. Intellectual Property &amp; Copyright</h2>
      <p class="ac-policy-p">{p5}</p>

      <h2 id="trade-secrets">6. Trade Secrets &amp; Horological Methods</h2>
      <p class="ac-policy-p">{p6}</p>

      <h2 id="conduct">7. Guest Salon Conduct &amp; Safety</h2>
      <p class="ac-policy-p">{p7}</p>

      <h2 id="photography">8. Photography &amp; Commercial Recording</h2>
      <p class="ac-policy-p">{p8}</p>

      <h2 id="jurisdiction">9. Governing Law &amp; Binding Arbitration</h2>
      <p class="ac-policy-p">{p9}</p>

      <h2 id="legal-notice">10. Legal Notice Coordinates</h2>
      <p class="ac-policy-p">{p10}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_disclaimer():
    p1 = "The horological essays, caliber analyses, timing metrics, and complication descriptions published on this web portal are presented exclusively for general informational and educational enrichment. While we strive to maintain meticulous historical accuracy and technical precision regarding mechanical movements, escapement geometries, and vintage references, we make no express or implied warranties regarding absolute infallibility or universal suitability for every collector requirement. Content is supplied on an as-is basis without merchantability guarantees."
    p2 = "Aperture Castle expressly disclaims all legal liability for inadvertent typographical errors, computational discrepancies, or unintentional omissions that may occur across our digital archives. Technical specifications regarding balance wheel vibrations per hour, power reserves, and water resistance depth ratings reflect standard baseline benchmarks and may vary depending on mechanical wear, atmospheric temperature, and operational habits. Patrons are encouraged to verify timing metrics directly with our Boston bench staff."
    p3 = "Mechanical timepieces are micro-mechanical precision instruments containing microscopic jewels, springs, and gears sensitive to physical shock, magnetic fields, and water ingress. While our timepieces undergo comprehensive pressure testing and demagnetization prior to handover, owners must exercise proper care, including avoiding magnetic electronics and ensuring screw-down crowns are sealed prior to moisture exposure. Nothing published on this website constitutes an unconditional guarantee against damage resulting from external trauma or improper handling."
    p4 = "Our digital platform may periodically provide hyperlinked references to external horological research institutes, historical museum archives, chronometer certification bodies, or regional transit portals across global networks. These third-party hyperlinks are supplied purely for visitor convenience and do not signify institutional endorsement, sponsorship, or independent verification of external entities. Aperture Castle Horological Atelier exercises zero operational control over the content, security measures, or data privacy practices of external web domains."
    p5 = "When electing to leave our digital domain via external links, you do so entirely at your own discretion and individual risk. We strongly encourage all users to inspect the terms of service and privacy declarations of any outside web portals they visit. Aperture Castle Horological Atelier accepts no legal responsibility for financial damages, digital malware, or misleading claims arising from your navigation of third-party digital networks."
    p6 = "To the maximum extent permitted under applicable United States law, Aperture Castle Horological Atelier LLC, its managing partners, master watchmakers, and corporate affiliates shall not be held liable for indirect, incidental, punitive, or consequential damages resulting from your use of this web portal or your horological engagement. This broad limitation applies regardless of whether alleged damages stem from contract claims, tort actions, server downtimes, or technical interruptions."
    p7 = "In jurisdictions that do not permit the full exclusion or limitation of incidental liability for consumer transactions, our maximum aggregate liability to you for any verified claims shall strictly not exceed the total financial sums paid by you directly to Aperture Castle during the preceding three calendar months. This limitation represents a fundamental element of the commercial bargain between our atelier and culinary patrons."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Horological and Legal Disclaimer, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, horological excellence, and lasting mutual trust with every patron who engages with our digital portal, reviews our complication archives, or reserves private viewing experiences at our Boston Financial District salon rooms."
    p9 = f"Please direct all formal inquiries regarding this disclaimer framework to Aperture Castle Horological Atelier LLC, located at {ADDR}. For immediate verbal consultations regarding horological specifications or salon reservation records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "disclaimer.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Horological &amp; Legal Disclaimer | Aperture Castle Boston</title>
<meta name="description" content="Technical, horological, and legal disclaimer regarding mechanical accuracy, water resistance ratings, and web content for Aperture Castle.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Disclaimer | Aperture Castle">
<meta property="og:description" content="Horological Disclaimer for Aperture Castle Horological Atelier LLC in Boston, Massachusetts.">
<meta property="og:url" content="https://{DOMAIN}/disclaimer.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_1.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("disclaimer.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Disclaimer</nav>
    <h1>Horological &amp; Legal Disclaimer</h1>
    <p>Last updated: September 29, 2026 &bull; Aperture Castle Horological Atelier LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#educational">1. Educational Purpose</a></li>
        <li><a href="#accuracy">2. Mechanical Timing Benchmark</a></li>
        <li><a href="#care">3. Instrument Shock &amp; Moisture</a></li>
        <li><a href="#links">4. External Hyperlinks</a></li>
        <li><a href="#nav-risk">5. User Navigation Risk</a></li>
        <li><a href="#liability">6. Limitation of Liability</a></li>
        <li><a href="#cap">7. Liability Ceiling</a></li>
        <li><a href="#disc-inq">8. Administrative Inquiries</a></li>
        <li><a href="#disc-coords">9. Contact Coordinates</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="educational">1. General Educational Purpose &amp; Accuracy</h2>
      <p class="ac-policy-p">{p1}</p>

      <h2 id="accuracy">2. Mechanical Timing &amp; Benchmark Variances</h2>
      <p class="ac-policy-p">{p2}</p>

      <h2 id="care">3. Precision Instrument Shock &amp; Moisture Notices</h2>
      <p class="ac-policy-p">{p3}</p>

      <h2 id="links">4. External Hyperlinks &amp; Third-Party Resources</h2>
      <p class="ac-policy-p">{p4}</p>

      <h2 id="nav-risk">5. User Navigation Risk Disclosures</h2>
      <p class="ac-policy-p">{p5}</p>

      <h2 id="liability">6. Broad Limitation of Operational Liability</h2>
      <p class="ac-policy-p">{p6}</p>

      <h2 id="cap">7. Consumer Liability Ceiling</h2>
      <p class="ac-policy-p">{p7}</p>

      <h2 id="disc-inq">8. Administrative Inquiries &amp; Transparency</h2>
      <p class="ac-policy-p">{p8}</p>

      <h2 id="disc-coords">9. Institutional Contact Coordinates</h2>
      <p class="ac-policy-p">{p9}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_cookie():
    p1 = "This Institutional Cookie Policy explains how Aperture Castle Horological Atelier LLC utilizes minimal session cookie technologies, security tokens, and local cache memory elements across our official digital domain. We believe in total institutional transparency regarding our telemetry practices, ensuring that visiting collectors understand precisely what data files are placed on their browsing devices when exploring our mechanical archives and reserving private salon viewing appointments."
    p2 = "A cookie is a small alphanumeric text string placed on your computer, mobile device, or tablet by web page servers when you visit an online portal. Cookies allow digital platforms to recognize your specific browsing device, sustain active session tokens across sequential web pages, and preserve customized user preferences across visits. Cookies deployed by our domain cannot read private data from your local hardware storage."
    p3 = "Our web portal uses essential session cookies that are technically mandatory for the proper execution of basic digital services. These fundamental cookies maintain security verification during form submissions, retain tasting menu preferences within interactive specification tables, and manage navigation states between our primary galleries and secondary policy documents. Because these cookies are essential to web delivery, they operate automatically upon accessing our web pages."
    p4 = "We also utilize strictly anonymized analytical telemetry scripts to understand how collectors engage with our timepiece galleries, which technical horological articles receive sustained reading attention, and where interface bottlenecks occur. These analytical cookies collect purely aggregated metrics without capturing individual subscriber names, physical residential coordinates, or financial account details. Aggregated telemetry reports assist our developers in optimizing page rendering speeds across mobile devices."
    p5 = "Aperture Castle Horological Atelier maintains an ethical operational posture that strictly prohibits the deployment of invasive third-party behavioral advertising cookies, commercial tracking pixels, or cross-domain user profiling scripts. We do not sell or monetize our visitor engagement metrics to commercial data brokers, advertising networks, or consumer marketing agencies. All analytical telemetry collected on our domain remains strictly confined to internal atelier speed optimization."
    p6 = "You maintain complete authority to regulate, refuse, block, or delete cookies via your personal browser preferences at any time. Most modern desktop and mobile browsers permit users to review stored cookies, block third-party cookies by default, or clear their cached browsing history automatically upon closing the active application window. Please consult your individual web browser documentation or online help portals for step-by-step instructions on adjusting security and telemetry settings."
    p7 = "Please be aware that disabling essential session cookies or purging browser cache records may noticeably impair the operational performance of specific interactive features on our website, such as reservation booking form transmissions and digital complication matrix calculators. To ensure the smoothest and most secure browsing experience across our Boston horological archives, we recommend allowing essential first-party cookies while configuring your personal browser to block extraneous third-party trackers and commercial ad beacons."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Institutional Cookie Policy, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, horological excellence, and lasting mutual trust with every patron who engages with our digital portal, reviews our complication archives, or reserves private viewing experiences at our Boston Financial District salon rooms."
    p9 = f"Please direct all formal inquiries regarding this cookie framework to Aperture Castle Horological Atelier LLC, located at {ADDR}. For immediate verbal consultations regarding telemetry safeguards or salon reservation records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "cookie-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cookie Policy | Aperture Castle Horological Atelier</title>
<meta name="description" content="Cookie Policy for Aperture Castle Horological Atelier. Learn about our minimal session cookies, zero tracking sale policy, and consent options.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Cookie Policy | Aperture Castle">
<meta property="og:description" content="Institutional Cookie Policy for Aperture Castle Horological Atelier in Boston, Massachusetts.">
<meta property="og:url" content="https://{DOMAIN}/cookie-policy.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_1.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("cookie-policy.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Cookie Policy</nav>
    <h1>Institutional Cookie Policy</h1>
    <p>Last updated: September 29, 2026 &bull; Aperture Castle Horological Atelier LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#tech">1. Cookie Technology</a></li>
        <li><a href="#definition">2. Definition &amp; Function</a></li>
        <li><a href="#essential">3. Essential Session Cookies</a></li>
        <li><a href="#analytics">4. Anonymized Telemetry</a></li>
        <li><a href="#third-party">5. No Third-Party Ads</a></li>
        <li><a href="#control">6. User Browser Controls</a></li>
        <li><a href="#impact">7. Potential Impact of Disabling</a></li>
        <li><a href="#inquiries-cookie">8. Administrative Inquiries</a></li>
        <li><a href="#coords-cookie">9. Institutional Coordinates</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="tech">1. Introduction to Cookie Technologies</h2>
      <p class="ac-policy-p">{p1}</p>

      <h2 id="definition">2. Definition &amp; Technical Function</h2>
      <p class="ac-policy-p">{p2}</p>

      <h2 id="essential">3. Essential Session Cookies</h2>
      <p class="ac-policy-p">{p3}</p>

      <h2 id="analytics">4. Strictly Anonymized Analytical Telemetry</h2>
      <p class="ac-policy-p">{p4}</p>

      <h2 id="third-party">5. Ban on Third-Party Commercial Tracking</h2>
      <p class="ac-policy-p">{p5}</p>

      <h2 id="control">6. User Browser Regulation &amp; Deletion</h2>
      <p class="ac-policy-p">{p6}</p>

      <h2 id="impact">7. Operational Impact of Disabling Cookies</h2>
      <p class="ac-policy-p">{p7}</p>

      <h2 id="inquiries-cookie">8. Administrative Inquiries &amp; Transparency</h2>
      <p class="ac-policy-p">{p8}</p>

      <h2 id="coords-cookie">9. Institutional Contact Coordinates</h2>
      <p class="ac-policy-p">{p9}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_cancellation():
    p1 = "At Aperture Castle, we recognize that calendar commitments for private collectors and corporate executives may change unexpectedly. That is why every salon viewing reservation or horological bench session may be altered or cancelled free of charge up to forty-eight hours prior to your scheduled hour. This policy details the procedures governing scheduling changes inside that window, what happens in the event of an unnotified absence, and how guarantee authorizations are managed by our concierge desk."
    p2 = "To request an appointment cancellation or reschedule your viewing date, please contact our concierge by telephoning our direct desk or submitting a formal email with your reservation reference code. The timestamp recorded upon receipt of your communication determines the applicable notice window. For requests submitted within forty-eight hours of your scheduled appointment, we strongly advise calling our desk directly, as phone transmissions are logged and processed in real time by on-duty concierge staff."
    p3 = "When our concierge confirms your private viewing reservation, we secure credit card details exclusively to guarantee the appointment slot and ensure vault personnel are allocated. These card parameters are processed through bank-level encrypted payment gateways and are never stored on our web server. A late-cancellation or no-show fee is charged only under the specific conditions outlined in our schedule table, and an itemized electronic receipt is promptly transmitted to your verified email address."
    p4 = "Modifying your appointment date, salon hour, party size, or requested caliber focus is entirely complimentary when requested at least forty-eight hours prior to the reserved time, subject to bench availability. The new appointment is confirmed at current calendar availability. Inside forty-eight hours, our staff will make every reasonable effort to accommodate adjustments without disruption, though adjustments that cannot be accommodated and result in missed sessions may be subject to cancellation guidelines."
    p5 = "Where a deposit refund is due following an approved cancellation, our administrative office processes the transaction to the original card within three business days of confirmation. Your card-issuing bank may take an additional five to ten business days to reflect the credit on your statement. Any pre-authorized security hold is released automatically following the conclusion of your visit, and any applicable deductions are documented in writing with comprehensive receipts."
    p6 = "We will waive late cancellation and no-show fees whenever appointment changes stem from verified events beyond your reasonable control, provided you inform our concierge as soon as practically possible. Qualifying situations include severe meteorological emergencies that disrupt travel across Massachusetts, sudden documented medical emergencies, or significant airline delays when flight numbers were provided to our concierge during booking. We believe in treating our patrons with genuine equity and understanding."
    p7 = "In the rare and improbable circumstance where Aperture Castle cannot fulfill a confirmed salon appointment—for instance, if a scheduled rare caliber is undergoing unscheduled technical regulation following timing test anomalies—our concierge will contact you immediately, offer the finest available alternative calibers at no additional fee, and if preferred, reschedule your session with full priority or cancel your reservation without any fee or financial penalty whatsoever."
    p8 = f"If any provision within this cancellation policy requires further clarification prior to reserving your salon session, please contact our concierge team. This policy constitutes an integral component of our broader Terms and Conditions, and formal legal inquiries may be directed to Aperture Castle Horological Atelier LLC, located at {ADDR}, by telephone at {PHONE}, or via electronic mail at {EMAIL}."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8]
    check_paragraphs(paras, "cancellation-refund-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cancellation &amp; Refund Policy | Aperture Castle Horological Atelier</title>
<meta name="description" content="Free changes and cancellations up to 48 hours before your salon viewing. Review rescheduling terms, waivers, and refund timelines at Aperture Castle.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/cancellation-refund-policy.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aperture Castle">
<meta property="og:title" content="Cancellation &amp; Refund Policy | Aperture Castle">
<meta property="og:description" content="Cancellation &amp; Refund Policy for private salon viewings at Aperture Castle in Boston.">
<meta property="og:url" content="https://{DOMAIN}/cancellation-refund-policy.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/aperturecastle_asset_1.jpg">
<meta name="theme-color" content="#0B1320">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("cancellation-refund-policy.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Cancellation &amp; Refund Policy</nav>
    <h1>Cancellation &amp; Refund Policy</h1>
    <p>Last updated: September 29, 2026 &bull; Aperture Castle Horological Atelier LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#summary">1. Summary &amp; Overview</a></li>
        <li><a href="#table">2. Fee Schedule Table</a></li>
        <li><a href="#how">3. How to Cancel or Change</a></li>
        <li><a href="#guarantee">4. How Fees Are Collected</a></li>
        <li><a href="#amend">5. Amendments &amp; Extensions</a></li>
        <li><a href="#refunds">6. Refunds &amp; Security Hold</a></li>
        <li><a href="#exceptions">7. Situations Where Fees Are Waived</a></li>
        <li><a href="#atelier-cancel">8. If We Must Reschedule</a></li>
        <li><a href="#inquiries-canc">9. Questions &amp; Contacts</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="summary">1. Summary &amp; Overview</h2>
      <p class="ac-policy-p">{p1}</p>

      <h2 id="table">2. Fee Schedule Table</h2>
      <table>
        <thead><tr><th>Cancellation Timing</th><th>Applicable Fee</th></tr></thead>
        <tbody>
          <tr><td>More than 48 hours before scheduled salon hour</td><td>$0 (Complimentary)</td></tr>
          <tr><td>Between 48 and 12 hours before appointment</td><td>50% of base session curatorial rate</td></tr>
          <tr><td>Less than 12 hours before appointment</td><td>100% of base session curatorial rate</td></tr>
          <tr><td>No-show without notification</td><td>100% of base session curatorial rate</td></tr>
        </tbody>
      </table>

      <h2 id="how">3. How to Cancel or Change a Booking</h2>
      <p class="ac-policy-p">{p2}</p>

      <h2 id="guarantee">4. How Fees Are Handled</h2>
      <p class="ac-policy-p">{p3}</p>

      <h2 id="amend">5. Amendments and Rescheduling</h2>
      <p class="ac-policy-p">{p4}</p>

      <h2 id="refunds">6. Refunds and Security Pre-Authorizations</h2>
      <p class="ac-policy-p">{p5}</p>

      <h2 id="exceptions">7. Situations Where Fees Are Waived</h2>
      <p class="ac-policy-p">{p6}</p>

      <h2 id="atelier-cancel">8. If We Must Reschedule or Cancel</h2>
      <p class="ac-policy-p">{p7}</p>

      <h2 id="inquiries-canc">9. Questions and Concierge Contact</h2>
      <p class="ac-policy-p">{p8}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_sitemap():
    pages = [
        "index.html", "about.html", "products.html", "booking.html", "contact.html", "faq.html",
        "cancellation-refund-policy.html", "privacy-policy.html", "terms-and-conditions.html",
        "disclaimer.html", "cookie-policy.html"
    ]
    xml_items = []
    for p in pages:
        xml_items.append(f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-09-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if p == "index.html" else "0.8"}</priority>
  </url>""")
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"".join(xml_items)}
</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Disallow: /assets/private/

Sitemap: https://{DOMAIN}/sitemap.xml"""

def build_registries():
    # Load image metadata
    meta_file = r"d:\antigravity website\scratch\aperturecastle_image_meta.json"
    with open(meta_file, "r", encoding="utf-8") as f:
        meta = json.load(f)

    # 1. IMAGE_REGISTRY.md
    reg_lines = [
        "# Aperture Castle Image Registry",
        "",
        "| Asset Filename | Subject & Description | Size | MD5 Hash | Source Title |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for item in meta:
        reg_lines.append(f"| `{item['filename']}` | {item['description']} | {item['size_bytes']//1024} KB | `{item['md5']}` | {item.get('source_title', 'Wikimedia Commons')} |")
    image_registry_content = "\n".join(reg_lines)

    # 2. DESIGN_REGISTRY.md
    design_registry_content = f"""# Aperture Castle Design Registry

## Archetype & Visual Identity
- **Archetype**: Modern Horological Atelier / Haute Horlogerie Precision Framework
- **Layout Architecture**: Inspired by Ridevora Clean Geometry, Full Breadcrumb Hierarchy, Dual Hero (Panoramic Photo + Plain Minimalist), Split Editorial Storytelling Rows, High-Contrast Metrics Strip, Multi-Step Interactive Stepper, and Sticky Table of Contents.
- **Strict Compliance**: Strictly Zero Blog architecture. No blog files, blog links, or blog folders.

## Palette
- **Deep Obsidian (Main Background)**: `#0B1320`
- **Darker Obsidian (Sections)**: `#070D17`
- **Surface Elevation**: `#111C2E`
- **Surface Card**: `#18253C`
- **Precision Caliber Gold (Accent)**: `#E5A93C`
- **Accent Hover / Glow**: `#F3BC54` / `rgba(229, 169, 60, 0.2)`
- **Clean Light (Values Section)**: `#F8FAFC` & `#FFFFFF`
- **Text Main**: `#F1F5F9`
- **Text Muted**: `#94A3B8`

## Typography
- **Headings & Technical Accents**: `'Sora'`, 'Manrope', sans-serif (Weights: 500, 600, 700)
- **Body & Telemetry**: `'Manrope'`, -apple-system, sans-serif (Weights: 400, 500, 600, 700)

## Institutional Coordinates
- **Entity**: Aperture Castle Horological Atelier LLC
- **Commercial Address**: {ADDR}
- **Telephone**: {PHONE}
- **Inquiries**: {EMAIL}
- **Operating Hours**: {DESK_HOURS}
"""

    # 3. SITE_MANIFEST.json
    manifest = {
        "domain": DOMAIN,
        "category": "watch",
        "niche": "Haute Horlogerie & Mechanical Watchmaking Atelier",
        "brand_name": "Aperture Castle Horological Atelier",
        "entity_name": "Aperture Castle Horological Atelier LLC",
        "address": ADDR,
        "phone": PHONE,
        "email": EMAIL,
        "operating_hours": DESK_HOURS,
        "gtag_id": "G-0LY0HY7L01",
        "pages": [
            "index.html", "about.html", "products.html", "booking.html", "contact.html", "faq.html",
            "cancellation-refund-policy.html", "privacy-policy.html", "terms-and-conditions.html",
            "disclaimer.html", "cookie-policy.html"
        ],
        "image_count": 20,
        "strict_no_blog": True,
        "architecture": "Ridevora Modern Precision Framework",
        "last_generated": "2026-09-29"
    }
    site_manifest_content = json.dumps(manifest, indent=2)

    return image_registry_content, design_registry_content, site_manifest_content

def generate_all():
    print(f"Generating pages for Aperture Castle ({DOMAIN})...")
    
    pages = {
        "index.html": build_index(),
        "about.html": build_about(),
        "products.html": build_products(),
        "booking.html": build_booking(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "cancellation-refund-policy.html": build_cancellation(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots()
    }
    
    for filename, content in pages.items():
        fp = os.path.join(SITE_DIR, filename)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filename} ({len(content)} bytes)")
    
    img_reg, des_reg, manifest = build_registries()
    with open(os.path.join(SITE_DIR, "IMAGE_REGISTRY.md"), "w", encoding="utf-8") as f:
        f.write(img_reg)
    with open(os.path.join(SITE_DIR, "DESIGN_REGISTRY.md"), "w", encoding="utf-8") as f:
        f.write(des_reg)
    with open(os.path.join(SITE_DIR, "SITE_MANIFEST.json"), "w", encoding="utf-8") as f:
        f.write(manifest)
    print("Generated registries & manifest.")
    print("All files generated successfully.")

if __name__ == "__main__":
    generate_all()
