# ElectraPro — Electrical Knowledge & Career Hub ⚡

A professional-style Streamlit starter platform for electrical engineering learning and career preparation.

## Included
- Structured learning modules across fundamentals, machines, power systems, automation, renewables/EVs, marine ETO, public-sector jobs and interviews
- MCQ practice with answer explanations
- Ohm's law, DC/resistive power, three-phase power, transformer ratio, synchronous speed, and energy/cost calculators
- Career checklists, interview answer structures and glossary
- Reference centre and privacy information
- Optional consent-based, pseudonymous visitor analytics using Supabase

## Run locally
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud
1. Upload `app.py`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Open https://share.streamlit.io/ and connect GitHub.
3. Create an app from the repository and choose `app.py` as the main file.
4. Deploy.

## Optional visitor analytics setup (Supabase)
Analytics is disabled unless a visitor opts in and the backend is configured. The app's analytics code does not intentionally collect names, emails, IP addresses or precise location. It stores a random session ID, event type, page name, timestamp and app version. A random session ID is pseudonymous data, so publish a suitable privacy notice and check applicable laws before enabling it.

1. Create a project at https://supabase.com/
2. In the Supabase SQL editor, run:

```sql
create table if not exists public.analytics_events (
  id bigint generated always as identity primary key,
  visitor_session_id text not null,
  event_name text not null,
  page_name text not null,
  created_at timestamptz not null default now(),
  app_version text not null
);

alter table public.analytics_events enable row level security;
```

3. In Streamlit Community Cloud, open your app's **Settings → Secrets** and add:

```toml
SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
SUPABASE_SERVICE_ROLE_KEY = "YOUR_SUPABASE_SERVICE_ROLE_KEY"
ADMIN_DASHBOARD_PASSWORD = "choose-a-long-unique-password"
```

**Security:** The service-role key bypasses Supabase row-level security. Keep it only in Streamlit's server-side Secrets. Never put it in `app.py`, GitHub, a browser, or a public message. Use a unique, strong dashboard password. Rotate credentials if exposed.

4. Restart the app. Visitors must opt in on **Privacy & Analytics** for page-view events to be sent.
5. Open **Owner Analytics** in the sidebar and enter your dashboard password.

Analytics is best-effort; do not use it for security, billing, identity verification or legally required audit records. It counts pseudonymous sessions, not verified individual people. Supabase retention, access, backups and deletion need to be managed by the owner.

## Important limitations
- The Question Desk is a structured form; it does **not** currently generate AI answers. A secure server-side AI integration is a separate next step.
- Learning content and MCQs are starter content, not an official exam bank or accredited course.
- COC/STCW, job eligibility and recruitment rules vary and must be verified against current official sources.
- Calculators are educational estimates only. Electrical work can be dangerous; use applicable codes, approved procedures and qualified supervision.
