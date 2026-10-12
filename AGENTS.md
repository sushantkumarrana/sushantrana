# sushantrana.com — plain HTML/CSS/JS + PHP

No Node.js, no React, no build step. Edit the files directly; what is in this
repo is exactly what runs on the live site. Read `README.md` for the folder
map, deploy steps and editing rules.

- Pages: one folder per URL with an `index.html` (`about/index.html`, `blog/<slug>/index.html` …).
- Styling: `assets/css/style.css`. Interactivity and animations: `assets/js/site.js`.
- Lead forms post to `api/lead.php`. Keys live in `api/config.php` (git-ignored).
- Local preview: `php -S localhost:8090 dev/router.php` from the repo root.
- `.htaccess` hides `dev/`, `supabase/`, `.claude/` and every `.md` file from visitors.
