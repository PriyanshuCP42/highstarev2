import json

with open('templates/product.json', 'r') as f:
    data = json.load(f)

custom_liquid_content = """
<div class="custom-trust-badges">
  <div class="trust-title">
    <span class="trust-icon">🔒</span> GUARANTEED SECURE CHECKOUT
  </div>
  <div class="trust-payment-icons">
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/71/PhonePe_Logo.svg" alt="PhonePe" style="height:24px; width:auto; border-radius:3px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Paytm_Logo_%28standalone%29.svg" alt="Paytm" style="height:24px; width:auto; border-radius:3px;">
    {{ 'visa' | payment_type_svg_tag: class: 'icon icon--full-color' }}
    {{ 'master' | payment_type_svg_tag: class: 'icon icon--full-color' }}
    <div style="display:flex; align-items:center; background:#fff; border:1px solid #e2e2e2; border-radius:3px; padding:0 6px; height:24px; font-size:10px; font-weight:700; color:#333;">💳 DEBIT CARDS</div>
  </div>

  <div class="delivery-journey">
    <div class="journey-step">
      <div class="step-icon">📦</div>
      <div class="step-text">Order<br>Placed</div>
    </div>
    <div class="journey-line"></div>
    <div class="journey-step">
      <div class="step-icon">🚚</div>
      <div class="step-text">Dispatched<br>in 24 Hrs</div>
    </div>
    <div class="journey-line"></div>
    <div class="journey-step">
      <div class="step-icon">🏠</div>
      <div class="step-text">Delivered<br>in 6-7 Days</div>
    </div>
  </div>
</div>

<style>
  .custom-trust-badges {
    margin-top: 0.5rem;
    padding: 1.5rem 1.2rem;
    background: #fafafa;
    border: 1px solid #eaeaea;
    border-radius: 0.4rem;
    text-align: center;
    margin-bottom: 2rem;
  }
  .custom-trust-badges .trust-title {
    font-size: 1.1rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    color: #111;
    margin-bottom: 1.2rem;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }
  .custom-trust-badges .trust-payment-icons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.6rem;
    margin-bottom: 2rem;
  }
  .custom-trust-badges .trust-payment-icons svg {
    width: auto;
    height: 24px;
  }
  
  .delivery-journey {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 320px;
    margin: 0 auto;
    padding-top: 1rem;
    border-top: 1px dashed #ddd;
  }
  .journey-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.4rem;
    position: relative;
    z-index: 2;
  }
  .step-icon {
    font-size: 1.6rem;
    background: #fff;
    width: 3.5rem;
    height: 3.5rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #111;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  }
  .step-text {
    font-size: 0.85rem;
    font-weight: 700;
    color: #444;
    line-height: 1.2;
    text-transform: uppercase;
  }
  .journey-line {
    flex-grow: 1;
    height: 2px;
    background: #111;
    margin: 0 -1rem;
    margin-top: -2rem; /* offset to align with circle center */
    z-index: 1;
  }
</style>
"""

data['sections']['main']['blocks']['trust_badges']['settings']['custom_liquid'] = custom_liquid_content

with open('templates/product.json', 'w') as f:
    json.dump(data, f, indent=4)
