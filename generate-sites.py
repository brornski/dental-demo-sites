#!/usr/bin/env python3
"""Generate 7 dental website variations from the base template."""

import os, re

# Read base template
with open('/root/Projects/portfolio-sites/site1-apex/index.html') as f:
    base = f.read()

variations = [
    {
        "dir": "site2-luminance",
        "title": "Luminance Smile Design",
        "brand": "Luminance<span class=\"text-secondary\">Smile</span>",
        "brand_footer": "Luminance<span class=\"text-secondary\">Smile</span> Design",
        "tagline": "Philadelphia's premier cosmetic smile studio.",
        "headline": "Your Dream Smile,<br><span class=\"text-secondary\">Designed</span> By Experts.",
        "subheadline": "Luxury cosmetic dentistry combining artistry and advanced technology for stunning, natural-looking results.",
        "primary": "#2D1B69",
        "secondary": "#E879A8",
        "gradient_from": "#2D1B69",
        "gradient_to": "#1a1040",
        "specialty": "Cosmetic",
        "hero_img": "https://images.unsplash.com/photo-1629909615184-74f495363b67?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1581585740085-2d2861dc4b73?w=800&q=80",
        "services": [
            ("💎", "Porcelain Veneers", "Custom-crafted veneers that mimic natural teeth for a flawless, radiant smile."),
            ("🌟", "Teeth Whitening", "Professional-grade whitening treatments that deliver dramatic results in a single visit."),
            ("😊", "Smile Makeovers", "Complete aesthetic transformations combining multiple treatments for your perfect look."),
            ("👄", "Lip & Gum Contouring", "Precise reshaping for a balanced, harmonious smile that frames your features."),
        ],
        "reviews": [
            ("AM", "Amanda M.", "The veneers Dr. Chen gave me are absolutely stunning. People keep asking if I'm a model now. Worth every penny!"),
            ("RP", "Robert P.", "I was self-conscious about my smile for decades. One visit to Luminance and that all changed. The whitening results are incredible."),
            ("KW", "Karen W.", "The level of artistry here is unmatched. My smile makeover looks so natural that even my dentist back home couldn't tell."),
            ("JD", "James D.", "Premium experience from start to finish. The consultation alone was worth it - they really listen to what you want."),
        ],
        "badge_text": "Top Cosmetic Practice 2026",
        "shadow_color": "rgba(232,121,168,",
    },
    {
        "dir": "site3-greenfield",
        "title": "Greenfield Family Dental",
        "brand": "Greenfield<span class=\"text-secondary\">Family</span>",
        "brand_footer": "Greenfield<span class=\"text-secondary\">Family</span> Dental",
        "tagline": "Where families come first, every visit.",
        "headline": "Gentle Care for<br><span class=\"text-secondary\">Every</span> Generation.",
        "subheadline": "A warm, welcoming dental home for your entire family. From first teeth to grandparents, we treat everyone with care.",
        "primary": "#1B4332",
        "secondary": "#52B788",
        "gradient_from": "#1B4332",
        "gradient_to": "#2D6A4F",
        "specialty": "Family",
        "hero_img": "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1600170311833-c2cf5280ce49?w=800&q=80",
        "services": [
            ("👨‍👩‍👧‍👦", "Family Dentistry", "Comprehensive care for patients of all ages in a comfortable, friendly environment."),
            ("🧒", "Pediatric Dentistry", "Gentle, fun dental visits designed to keep kids smiling and cavity-free."),
            ("🛡️", "Preventive Care", "Regular cleanings, sealants, and fluoride treatments to protect your family's oral health."),
            ("🚑", "Emergency Dental", "Same-day emergency appointments for toothaches, broken teeth, and urgent needs."),
        ],
        "reviews": [
            ("LM", "Lisa M.", "Finally found a dentist my kids actually look forward to visiting! The children's area is amazing and Dr. Patel is so patient."),
            ("TC", "Tom C.", "Three generations of our family go to Greenfield. That says everything about the quality of care."),
            ("NR", "Nancy R.", "The hygienists are so gentle and thorough. I've never had a cleaning this comfortable anywhere else."),
            ("BH", "Brian H.", "Called on a Saturday with a broken tooth. They got me in within an hour. Can't beat that kind of service."),
        ],
        "badge_text": "Best Family Practice 2026",
        "shadow_color": "rgba(82,183,136,",
    },
    {
        "dir": "site4-precision",
        "title": "Precision Implant Center",
        "brand": "Precision<span class=\"text-secondary\">Implant</span>",
        "brand_footer": "Precision<span class=\"text-secondary\">Implant</span> Center",
        "tagline": "Advanced implantology for lasting results.",
        "headline": "Permanent Solutions,<br><span class=\"text-secondary\">Precision</span> Results.",
        "subheadline": "State-of-the-art dental implant center using guided surgery and 3D planning for perfect outcomes every time.",
        "primary": "#1C1917",
        "secondary": "#D4AF37",
        "gradient_from": "#1C1917",
        "gradient_to": "#292524",
        "specialty": "Implants",
        "hero_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=800&q=80",
        "services": [
            ("🔩", "Single Implants", "Individual tooth replacement with titanium implants that look and function like natural teeth."),
            ("🦷", "All-on-4 Solutions", "Full-arch restoration in a single day using just four strategically placed implants."),
            ("🏗️", "Bone Grafting", "Advanced bone regeneration techniques to build the foundation for successful implants."),
            ("💻", "3D Guided Surgery", "Computer-planned precision placement for predictable, minimally invasive procedures."),
        ],
        "reviews": [
            ("GS", "George S.", "After years of dentures, I finally got All-on-4 implants. Life-changing doesn't begin to describe it. I can eat steak again!"),
            ("PW", "Patricia W.", "The 3D planning showed me exactly what my results would look like before surgery. No surprises, just perfection."),
            ("RJ", "Richard J.", "I was told by two other dentists I didn't have enough bone for implants. Precision found a way. Incredible team."),
            ("ML", "Maria L.", "The guided surgery was remarkably comfortable. Minimal swelling, minimal downtime. Back to work in 3 days."),
        ],
        "badge_text": "Top Implant Center 2026",
        "shadow_color": "rgba(212,175,55,",
    },
    {
        "dir": "site5-align",
        "title": "Align Orthodontics",
        "brand": "Align<span class=\"text-secondary\">Ortho</span>",
        "brand_footer": "Align<span class=\"text-secondary\">Ortho</span>dontics",
        "tagline": "Straighten your path to confidence.",
        "headline": "Straighter Teeth,<br><span class=\"text-secondary\">Brighter</span> Future.",
        "subheadline": "Expert orthodontic care using Invisalign, clear braces, and advanced digital planning for perfect alignment.",
        "primary": "#0C4A6E",
        "secondary": "#38BDF8",
        "gradient_from": "#0C4A6E",
        "gradient_to": "#164E63",
        "specialty": "Orthodontics",
        "hero_img": "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1595005559643-1e8e9df70291?w=800&q=80",
        "services": [
            ("😁", "Invisalign", "Virtually invisible aligners that straighten teeth without metal brackets or wires."),
            ("✨", "Clear Braces", "Ceramic brackets that blend with your natural tooth color for discreet treatment."),
            ("👶", "Early Orthodontics", "Phase 1 treatment to guide jaw growth and prevent complex issues later."),
            ("📱", "Digital Smile Design", "See your future smile before treatment begins with 3D simulation technology."),
        ],
        "reviews": [
            ("EK", "Emily K.", "Nobody even noticed I was wearing Invisalign! 14 months later, my teeth are perfectly straight. So glad I chose Align."),
            ("DM", "Daniel M.", "The digital preview sold me. Seeing my future smile before committing was incredible. Results matched perfectly."),
            ("SW", "Sophia W.", "My son's early treatment corrected his bite at age 8. Dr. Lee caught it early and saved us from jaw surgery later."),
            ("AT", "Alex T.", "Had braces as a kid that relapsed. Align's retention program means my investment is protected for life."),
        ],
        "badge_text": "Diamond Invisalign Provider",
        "shadow_color": "rgba(56,189,248,",
    },
    {
        "dir": "site6-riverstone",
        "title": "Riverstone Dental Spa",
        "brand": "Riverstone<span class=\"text-secondary\">Spa</span>",
        "brand_footer": "Riverstone<span class=\"text-secondary\">Spa</span> Dental",
        "tagline": "Where relaxation meets dental excellence.",
        "headline": "Dental Care That<br><span class=\"text-secondary\">Feels Like</span> a Retreat.",
        "subheadline": "A spa-like dental experience with aromatherapy, weighted blankets, noise-canceling headphones, and gentle sedation options.",
        "primary": "#44403C",
        "secondary": "#A3B18A",
        "gradient_from": "#44403C",
        "gradient_to": "#292524",
        "specialty": "Spa-Style",
        "hero_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=800&q=80",
        "services": [
            ("🧘", "Spa-Style Cleanings", "Enjoy aromatherapy, heated neck pillows, and paraffin hand wax during your cleaning."),
            ("😴", "Sedation Dentistry", "Anxiety-free procedures with oral sedation and nitrous oxide for total comfort."),
            ("💆", "Holistic Approach", "Mercury-free fillings, biocompatible materials, and minimally invasive techniques."),
            ("🌿", "Wellness Consultations", "Comprehensive oral-systemic health assessments connecting dental and overall wellness."),
        ],
        "reviews": [
            ("CH", "Christina H.", "I used to have panic attacks at the dentist. At Riverstone, I actually fell asleep during my procedure. Unbelievable."),
            ("MW", "Mark W.", "The weighted blanket and noise-canceling headphones transformed the experience. It genuinely felt like a spa visit."),
            ("JS", "Julie S.", "The holistic approach makes so much sense. They explained how my oral health connects to everything else. Eye-opening."),
            ("TP", "Thomas P.", "My wife and I now look forward to our dental appointments. Never thought I'd say that. Riverstone is special."),
        ],
        "badge_text": "Best Dental Spa 2026",
        "shadow_color": "rgba(163,177,138,",
    },
    {
        "dir": "site7-novacare",
        "title": "NovaCare Periodontics",
        "brand": "Nova<span class=\"text-secondary\">Care</span>",
        "brand_footer": "Nova<span class=\"text-secondary\">Care</span> Periodontics",
        "tagline": "Advanced gum care and reconstruction.",
        "headline": "Protect Your Foundation,<br><span class=\"text-secondary\">Preserve</span> Your Smile.",
        "subheadline": "Specialized periodontal care using laser therapy, regenerative techniques, and precision microsurgery for lasting gum health.",
        "primary": "#1E293B",
        "secondary": "#94A3B8",
        "gradient_from": "#1E293B",
        "gradient_to": "#0F172A",
        "specialty": "Periodontics",
        "hero_img": "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1551190822-a9ce113d0d15?w=800&q=80",
        "services": [
            ("🔬", "Laser Gum Therapy", "Minimally invasive LANAP laser treatment to eliminate gum disease without surgery."),
            ("🧬", "Gum Regeneration", "Advanced grafting techniques to rebuild lost tissue and restore your gumline."),
            ("🩺", "Deep Cleanings", "Thorough scaling and root planing to halt periodontal disease progression."),
            ("🔧", "Dental Implants", "Periodontal expertise ensures optimal implant placement and long-term success."),
        ],
        "reviews": [
            ("FG", "Frank G.", "Was told I'd lose my teeth to gum disease. Dr. Nakamura's laser treatment saved them all. Two years later, zero issues."),
            ("SB", "Sandra B.", "The gum grafting was painless and the results are remarkable. My receding gums look completely normal again."),
            ("HN", "Henry N.", "After years of being told I needed surgery, NovaCare's laser approach was a game-changer. No cutting, fast recovery."),
            ("LD", "Linda D.", "The thoroughness of care here is beyond anything I've experienced. They caught early gum disease others missed."),
        ],
        "badge_text": "Top Periodontist 2026",
        "shadow_color": "rgba(148,163,184,",
    },
    {
        "dir": "site8-brightpath",
        "title": "Bright Path Pediatric Dentistry",
        "brand": "Bright<span class=\"text-secondary\">Path</span>",
        "brand_footer": "Bright<span class=\"text-secondary\">Path</span> Pediatric Dentistry",
        "tagline": "Making every kid's dental journey fun.",
        "headline": "Happy Kids,<br><span class=\"text-secondary\">Healthy</span> Smiles.",
        "subheadline": "A colorful, adventure-themed dental office designed specifically for children from infancy through teens.",
        "primary": "#581C87",
        "secondary": "#F59E0B",
        "gradient_from": "#581C87",
        "gradient_to": "#7C3AED",
        "specialty": "Pediatric",
        "hero_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=1920&q=80",
        "side_img": "https://images.unsplash.com/photo-1600170311833-c2cf5280ce49?w=800&q=80",
        "services": [
            ("🦸", "Kid-Friendly Exams", "Fun, gentle checkups with TVs on the ceiling, prizes, and a team that speaks kid."),
            ("🛡️", "Sealants & Fluoride", "Protective treatments that prevent cavities before they start."),
            ("😴", "Gentle Sedation", "Safe sedation options for anxious little ones who need extra comfort."),
            ("🦷", "Orthodontic Screening", "Early evaluation at age 7 to catch alignment issues while they're easy to fix."),
        ],
        "reviews": [
            ("JR", "Jennifer R.", "My daughter used to scream at the dentist. At Bright Path, she asks when we can go back! The staff is magical with kids."),
            ("MH", "Marcus H.", "The adventure-themed rooms make it feel like a theme park, not a dental office. Both my boys love going."),
            ("AS", "Amanda S.", "Dr. Kim caught an alignment issue at my son's age 7 screening. Early treatment saved us years of braces later."),
            ("CP", "Carlos P.", "The sedation for my anxious daughter was handled with such care. She didn't even realize she had a filling done."),
        ],
        "badge_text": "Top Pediatric Practice 2026",
        "shadow_color": "rgba(245,158,11,",
    },
]

def generate(var):
    html = base
    
    # Replace title
    html = html.replace("Apex Dental Studio | Modern Dentistry, Pain-Free Experience", f"{var['title']} | {var['headline'].split('<')[0].strip()}")
    
    # Replace colors in tailwind config
    html = html.replace("primary: '#0F172A'", f"primary: '{var['primary']}'")
    html = html.replace("secondary: '#14B8A6'", f"secondary: '{var['secondary']}'")
    
    # Replace gradient
    html = html.replace("from-primary via-slate-800 to-primary", "from-primary to-primary")
    
    # Replace brand name in nav
    html = html.replace("Apex<span class=\"text-secondary\">Dental</span>", var['brand'])
    
    # Replace hero headline
    html = html.replace(
        "Modern Dentistry,<br><span class=\"text-secondary\">Pain-Free</span> Experience.",
        var['headline']
    )
    
    # Replace hero subtitle  
    html = html.replace(
        "Experience world-class dental care with cutting-edge technology and a compassionate team dedicated to your comfort.",
        var['subheadline']
    )
    
    # Replace hero images
    html = html.replace(
        "https://images.unsplash.com/photo-1629909613654-28e377c37b09?w=1920&q=80",
        var['hero_img']
    )
    html = html.replace(
        "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?w=800&q=80",
        var['side_img']
    )
    
    # Replace trust badge
    html = html.replace("Top Rated Clinic 2026", var['badge_text'])
    
    # Replace services section
    old_services = []
    service_icons = ["🦷", "✨", "😁", "🔩"]
    service_names = ["General Dentistry", "Cosmetic Dentistry", "Invisalign & Ortho", "Dental Implants"]
    service_descs = [
        "Comprehensive exams, cleanings, fillings, and preventive care for the whole family.",
        "Veneers, professional whitening, and smile design to give you the confidence you deserve.",
        "Straighten your teeth discreetly with clear aligners and advanced orthodontic solutions.",
        "Permanent, natural-looking tooth replacement with state-of-the-art implant technology.",
    ]
    
    for i in range(4):
        html = html.replace(f"<span class=\"text-2xl\">{service_icons[i]}</span>", f"<span class=\"text-2xl\">{var['services'][i][0]}</span>", 1)
        html = html.replace(f"<h3 class=\"text-xl font-bold text-primary mb-3\">{service_names[i]}</h3>", f"<h3 class=\"text-xl font-bold text-primary mb-3\">{var['services'][i][1]}</h3>", 1)
        html = html.replace(service_descs[i], var['services'][i][2], 1)
    
    # Replace reviews
    old_reviews = [
        ("SR", "Sarah R.", "Absolutely painless experience! Dr. Martinez and the team made me feel completely at ease. My new smile is incredible — I can't stop looking in the mirror."),
        ("MK", "Michael K.", "Best dental experience I've ever had. The technology they use is incredible — my implants look and feel completely natural. Life-changing."),
        ("JT", "Jennifer T.", "I was terrified of the dentist for years. Apex Dental changed that completely. The sedation options and gentle approach made all the difference."),
        ("DL", "David L.", "From the moment I walked in, everything felt premium. The results of my whitening treatment exceeded all expectations. Highly recommend!"),
    ]
    
    for i in range(4):
        # Each review appears twice (duplicated for marquee), so replace both
        html = html.replace(f">{old_reviews[i][0]}<", f">{var['reviews'][i][0]}<")
        html = html.replace(f">{old_reviews[i][1]}<", f">{var['reviews'][i][1]}<")
        html = html.replace(old_reviews[i][2], var['reviews'][i][2])
    
    # Replace footer brand
    html = html.replace("Apex<span class=\"text-secondary\">Dental</span> Studio", var['brand_footer'])
    html = html.replace("Philadelphia's premier dental experience.", var['tagline'])
    
    # Replace shadow colors
    html = html.replace("rgba(20,184,166,", var['shadow_color'])
    
    # Replace contact section phone
    html = html.replace("hello@apexdental.com", f"hello@{var['dir'].split('-')[1]}.com")
    
    return html

for var in variations:
    out_dir = f"/root/Projects/portfolio-sites/{var['dir']}"
    os.makedirs(out_dir, exist_ok=True)
    html = generate(var)
    with open(f"{out_dir}/index.html", "w") as f:
        f.write(html)
    print(f"✓ Generated {var['dir']} ({var['title']})")

print("\nAll 7 variations generated!")
