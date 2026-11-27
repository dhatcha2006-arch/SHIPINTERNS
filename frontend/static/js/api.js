/**
 * SkillForge Unified API Client
 * Coordinates with Ari's Flask REST APIs
 */
const SkillForgeAPI = {
  baseURL: '/api/v1',

  async request(endpoint, options = {}) {
    const token = localStorage.getItem('sf_token');
    const headers = {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` }),
      ...options.headers
    };

    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        ...options,
        headers
      });

      const contentType = response.headers.get('content-type');
      let data = {};
      if (contentType && contentType.includes('application/json')) {
        data = await response.json();
      } else {
        data = { message: await response.text() };
      }

      if (!response.ok) {
        throw new Error(data.message || `Request failed with status ${response.status}`);
      }

      return { success: true, data };
    } catch (err) {
      console.warn(`[SkillForge API Error] ${endpoint}:`, err.message);
      return { success: false, error: err.message };
    }
  },

  // Auth Methods
  auth: {
    async login(credentials) {
      const res = await SkillForgeAPI.request('/auth/login', {
        method: 'POST',
        body: JSON.stringify(credentials)
      });
      if (res.success && res.data.token) {
        localStorage.setItem('sf_token', res.data.token);
        localStorage.setItem('sf_user', JSON.stringify(res.data.user));
      }
      return res;
    },
    async register(userData) {
      return SkillForgeAPI.request('/auth/register', {
        method: 'POST',
        body: JSON.stringify(userData)
      });
    },
    logout() {
      localStorage.removeItem('sf_token');
      localStorage.removeItem('sf_user');
      window.location.href = '/auth/login';
    },
    getUser() {
      const u = localStorage.getItem('sf_user');
      return u ? JSON.parse(u) : null;
    }
  },

  // System Health
  async checkHealth() {
    return SkillForgeAPI.request('/health');
  }
};

window.SkillForgeAPI = SkillForgeAPI;
