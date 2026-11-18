# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import os
import sys

try:
    import stripe
except ImportError:
    print("[INFO] Installing stripe SDK...")
    os.system(f"{sys.executable} -m pip install stripe")
    import stripe

def create_catalog():
    api_key = os.environ.get("STRIPE_SECRET_KEY")
    if not api_key:
        print("\n[ERROR] STRIPE_SECRET_KEY environment variable not set.")
        print("Run: export STRIPE_SECRET_KEY='sk_live_your_actual_key_here'\n")
        return

    stripe.api_key = api_key
    print("[STRIPE] Initializing Castleberry Bloom Commercial Catalog...")

    # 1. Tier 1: $499 Certified PDF Audit
    prod_audit = stripe.Product.create(
        name="Certified Network & AI Pipeline SHA-256 Audit",
        description="Single executive-ready compliance and security audit report with SHA-256 verification."
    )
    price_audit = stripe.Price.create(
        product=prod_audit.id,
        unit_amount=49900,
        currency="usd",
    )
    link_audit = stripe.PaymentLink.create(
        line_items=[{"price": price_audit.id, "quantity": 1}]
    )

    # 2. Tier 2: $5,000/yr Guardrail Kit Commercial Exemption
    prod_lic = stripe.Product.create(
        name="Guardrail Kit Commercial Exemption License (Annual)",
        description="Allows closed-source commercial deployment of guardrail_kit and hex-coherence-engine for 1 year."
    )
    price_lic = stripe.Price.create(
        product=prod_lic.id,
        unit_amount=500000,
        currency="usd",
        recurring={"interval": "year"}
    )
    link_lic = stripe.PaymentLink.create(
        line_items=[{"price": price_lic.id, "quantity": 1}]
    )

    print("\n" + "="*72)
    print("✅ CASTLEBERRY BLOOM STRIPE CATALOG DEPLOYED SUCCESSFULLY")
    print("="*72)
    print(f"• $499 Audit Payment Link     : {link_audit.url}")
    print(f"• $5,000/yr License Payment Link : {link_lic.url}")
    print("="*72)

if __name__ == "__main__":
    create_catalog()
