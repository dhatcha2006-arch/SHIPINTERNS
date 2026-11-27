/**
 * ShipInterns UI Interactive Components Library
 * Handles alerts, toast system, mobile sidebar toggle and modals
 */

const ShipInternsUI = {
  // Toast Notification System
  showToast(message, type = 'info', title = '') {
    const container = document.getElementById('sfToastContainer');
    if (!container) return;

    const toastId = 'toast_' + Math.random().toString(36).substring(2, 9);
    const borderClass = type === 'success' ? 'border-success' : type === 'danger' ? 'border-danger' : 'border-primary';
    const iconName = type === 'success' ? 'check-circle' : type === 'danger' ? 'alert-circle' : 'info';

    const toastEl = document.createElement('div');
    toastEl.className = `toast align-items-center bg-white border-start border-4 ${borderClass} shadow-sm`;
    toastEl.id = toastId;
    toastEl.setAttribute('role', 'alert');
    toastEl.setAttribute('aria-live', 'assertive');
    toastEl.setAttribute('aria-atomic', 'true');

    toastEl.innerHTML = `
      <div class="d-flex p-3">
        <div class="me-3 text-${type === 'danger' ? 'danger' : type === 'success' ? 'success' : 'primary'}">
          <i data-lucide="${iconName}"></i>
        </div>
        <div class="toast-body p-0 flex-grow-1">
          ${title ? `<div class="fw-semibold text-slate-900 mb-1">${title}</div>` : ''}
          <div class="text-secondary small">${message}</div>
        </div>
        <button type="button" class="btn-close ms-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
    `;

    container.appendChild(toastEl);
    if (window.lucide) lucide.createIcons();

    const bsToast = new bootstrap.Toast(toastEl, { delay: 4500 });
    bsToast.show();

    toastEl.addEventListener('hidden.bs.toast', () => {
      toastEl.remove();
    });
  },

  // Toggle Sidebar for mobile viewports
  toggleSidebar() {
    const sidebar = document.querySelector('.sf-sidebar');
    if (sidebar) {
      sidebar.classList.toggle('open');
    }
  },

  // Toggle Mobile Navigation Menu
  initMobileNav() {
    const toggleBtn = document.getElementById('sfMobileNavToggle');
    const menu = document.getElementById('sfMobileMenu');
    if (toggleBtn && menu) {
      toggleBtn.addEventListener('click', () => {
        menu.classList.toggle('d-none');
      });
    }
  },

  // Hydrate dynamic user profile name across pages
  hydrateUser() {
    try {
      const stored = localStorage.getItem('sf_user');
      if (stored) {
        const u = JSON.parse(stored);
        if (u && u.name) {
          document.querySelectorAll('.sf-dynamic-user-name').forEach(el => {
            el.textContent = u.name;
          });
          document.querySelectorAll('.sf-dynamic-user-name-val').forEach(el => {
            el.value = u.name;
          });
          const initials = u.name.split(' ').filter(Boolean).map(n => n[0]).join('').substring(0, 2).toUpperCase() || 'SI';
          document.querySelectorAll('.sf-dynamic-user-initials').forEach(el => {
            el.textContent = initials;
          });
        }
      }
    } catch (e) {
      console.warn('Hydration error:', e);
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  ShipInternsUI.initMobileNav();
  ShipInternsUI.hydrateUser();
});

window.ShipInternsUI = ShipInternsUI;

// Backward compatibility alias
window.SkillForgeUI = window.ShipInternsUI;
