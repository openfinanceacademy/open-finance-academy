(() => {
  const storageKey = 'ofa-theme';
  const root = document.documentElement;
  let preference = 'system';

  try {
    const saved = localStorage.getItem(storageKey);
    if (saved === 'light' || saved === 'dark') preference = saved;
  } catch {
    // The theme still works when browser storage is unavailable.
  }

  function applyTheme() {
    if (preference === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', preference);
  }

  // Apply saved preferences before the stylesheet is loaded to avoid a flash.
  applyTheme();

  document.addEventListener('DOMContentLoaded', () => {
    const select = document.getElementById('theme-preference');
    if (!select) return;
    select.value = preference;
    select.parentElement.hidden = false;

    select.addEventListener('change', () => {
      preference = select.value;
      applyTheme();
      try {
        if (preference === 'system') localStorage.removeItem(storageKey);
        else localStorage.setItem(storageKey, preference);
      } catch {
        // Keep the selected theme for this page even if it cannot be saved.
      }
    });
  });
})();
