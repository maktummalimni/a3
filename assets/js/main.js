// APERTURE CASTLE - MASTER JAVASCRIPT ENGINE
// Synchronized with Ridevora Interaction Standards

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Year
  document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // 2. Mobile Navigation Toggle
  const navToggle = document.querySelector('.nav-toggle');
  const mainNav = document.getElementById('main-nav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', () => {
      const isOpen = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // 3. Back to Top Button
  const toTop = document.querySelector('.to-top');
  if (toTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        toTop.classList.add('visible');
      } else {
        toTop.classList.remove('visible');
      }
    });
    toTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 4. Cookie Consent Dialog
  const cookieBanner = document.querySelector('.cookie');
  const cookieButtons = document.querySelectorAll('[data-consent]');
  const cookieOpenBtn = document.querySelector('[data-open-cookies]');

  if (cookieBanner) {
    if (!localStorage.getItem('ac_cookie_consent')) {
      setTimeout(() => cookieBanner.classList.add('show'), 800);
    }
    cookieButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const choice = btn.getAttribute('data-consent');
        localStorage.setItem('ac_cookie_consent', choice);
        cookieBanner.classList.remove('show');
      });
    });
    if (cookieOpenBtn) {
      cookieOpenBtn.addEventListener('click', () => {
        cookieBanner.classList.add('show');
      });
    }
  }

  // 5. Interactive Stepper & Pricing Calculator (booking.html)
  const bookingForm = document.getElementById('booking-form');
  if (bookingForm) {
    let currentStep = 1;
    let selectedTier = { name: 'Chrono Complication Reserve', rate: 450 };
    let selectedExtras = 0;
    let days = 3;

    const panels = document.querySelectorAll('.b-panel');
    const stepIndicators = document.querySelectorAll('.stepper li');
    const sumPiece = document.getElementById('sum-car');
    const sumTrip = document.getElementById('sum-trip');
    const sumLines = document.getElementById('sum-lines');
    const sumTotal = document.getElementById('sum-total');

    function updateSummary() {
      if (sumPiece) sumPiece.textContent = selectedTier.name;
      if (sumTrip) {
        sumTrip.innerHTML = `<li><span>Session / Curatorial Duration:</span> <b>${days} days</b></li>
                             <li><span>Viewing Salon:</span> <b>Boston Financial Suite</b></li>`;
      }
      const baseCost = selectedTier.rate * days;
      const total = baseCost + selectedExtras;
      if (sumLines) {
        sumLines.innerHTML = `<li><span>Timepiece reservation (${days}d @ $${selectedTier.rate}):</span> <b>$${baseCost}</b></li>
                              <li><span>Curatorial services &amp; certification:</span> <b>$${selectedExtras}</b></li>`;
      }
      if (sumTotal) sumTotal.textContent = `$${total.toLocaleString()}`;
    }

    function goToStep(step) {
      currentStep = step;
      panels.forEach(p => {
        p.classList.toggle('active', parseInt(p.getAttribute('data-step')) === currentStep);
      });
      stepIndicators.forEach(li => {
        const s = parseInt(li.getAttribute('data-step'));
        li.classList.toggle('active', s === currentStep);
      });
      window.scrollTo({ top: bookingForm.offsetTop - 80, behavior: 'smooth' });
    }

    document.querySelectorAll('[data-next]').forEach(btn => {
      btn.addEventListener('click', () => {
        if (currentStep < 4) goToStep(currentStep + 1);
      });
    });

    document.querySelectorAll('[data-prev]').forEach(btn => {
      btn.addEventListener('click', () => {
        if (currentStep > 1) goToStep(currentStep - 1);
      });
    });

    // Pick cards
    document.querySelectorAll('.pick-card').forEach(card => {
      card.addEventListener('click', () => {
        document.querySelectorAll('.pick-card').forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        const name = card.querySelector('h4').textContent;
        const rate = parseInt(card.getAttribute('data-rate')) || 450;
        selectedTier = { name, rate };
        updateSummary();
      });
    });

    // Extras
    document.querySelectorAll('.extra-item input[type="checkbox"]').forEach(box => {
      box.addEventListener('change', () => {
        selectedExtras = 0;
        document.querySelectorAll('.extra-item input[type="checkbox"]:checked').forEach(c => {
          selectedExtras += parseInt(c.value) || 0;
        });
        updateSummary();
      });
    });

    // Form submit
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const terms = document.getElementById('b-terms');
      if (terms && !terms.checked) {
        alert('Please review and agree to the Terms & Conditions and Horological Service Policy.');
        return;
      }
      alert('Thank you for reserving a private salon viewing with Aperture Castle. Our senior horologist will review your request and transmit your authenticated confirmation within two business hours.');
      bookingForm.reset();
      goToStep(1);
    });

    updateSummary();
  }

  // 6. Contact Form feedback
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Thank you for contacting Aperture Castle Horological Atelier. Our concierge desk will review your inquiry and reply within one business day.');
      contactForm.reset();
    });
  }
});
