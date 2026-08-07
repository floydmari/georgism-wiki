#!/usr/bin/env python3
"""
create_utility_pages.py — upsert the two wiki utility PAGES on Ghost:

    /wiki-history/   — per-article edit timeline (reads ?slug=…)
    /wiki-cite/      — per-article revision-pinned citations (reads ?slug=…)

Both are ordinary Ghost pages, so they render inside the site's own chrome
(header, nav, typography) — Floyd's ask that Cite/History live within the
progress.org UX rather than on the worker's bare pages. Content is filled
client-side from the wiki-edit Worker's CORS-restricted JSON APIs
(/api/history/<slug>, /api/cite/<slug>); the pages themselves are static and
carry only the render script (data-cfasync so Rocket Loader leaves it alone).

These are UTILITY pages, not wiki content pages: they live outside the git
page corpus deliberately (no frontmatter, no lint), and sync_to_ghost.py never
touches page-type resources, so §0's one-way-sync rule is not violated — this
script is their single source of truth and is idempotent (upsert by slug).

Auth: same as sync_to_ghost.py (GHOST_ADMIN_KEY via env or 1Password).
Usage:  python3 scripts/create_utility_pages.py
"""
import sys, time, os

import jwt, requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _secrets import require_ghost

WORKER = "https://wiki-edit.progress.org"

HISTORY_HTML = """
<p id="wh-sub">Loading the edit history…</p>
<ul id="wh-list" style="list-style:none;padding:0"></ul>
<p id="wh-links"></p>
<script data-cfasync="false">
(function(){
  var slug = new URLSearchParams(location.search).get('slug') || '';
  var sub = document.getElementById('wh-sub'), list = document.getElementById('wh-list');
  if (!/^[a-z0-9-]+$/.test(slug)) { sub.textContent = 'No article specified.'; return; }
  function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML}
  fetch('""" + WORKER + """/api/history/' + slug)
    .then(function(r){ return r.json(); })
    .then(function(d){
      if (d.error) { sub.textContent = d.error; return; }
      sub.innerHTML = 'Every change to <a href="/wiki/' + esc(slug) + '/"><b>' + esc(slug) +
        '</b></a>, newest first — the unedited record from the wiki\\u2019s public source ' +
        'repository. Entries by the editorial loop are authored as Progress LLM and ' +
        'reviewed before publish; community suggestions carry their submitter\\u2019s credit.';
      list.innerHTML = d.commits.map(function(c){
        return '<li style="padding:.5em 0;border-bottom:1px solid rgba(0,0,0,.08)">' +
          '<span style="font-family:monospace;opacity:.65;margin-right:.7em">' + esc(c.date) + '</span>' +
          esc(c.subject) +
          (c.suggestedBy ? ' <em style="opacity:.75">\\u00B7 suggested by ' + esc(c.suggestedBy) + '</em>' : '') +
          ' <a href="' + esc(c.diffUrl) + '" rel="nofollow" style="float:right;font-size:.85em">view change</a></li>';
      }).join('');
      document.getElementById('wh-links').innerHTML =
        '<a href="' + esc(d.fullHistoryUrl) + '">Full history with diffs on GitHub \\u2192</a>' +
        ' \\u00B7 <a href="/wiki/' + esc(slug) + '/">\\u2190 Back to the article</a>';
    })
    .catch(function(){ sub.textContent = 'Could not load history — please try again.'; });
})();
</script>
"""

CITE_HTML = """
<p id="wc-sub">Loading citation…</p>
<div id="wc-out"></div>
<script data-cfasync="false">
(function(){
  var slug = new URLSearchParams(location.search).get('slug') || '';
  var sub = document.getElementById('wc-sub'), out = document.getElementById('wc-out');
  if (!/^[a-z0-9-]+$/.test(slug)) { sub.textContent = 'No article specified.'; return; }
  function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML}
  var today = new Date().toISOString().slice(0,10);
  fetch('""" + WORKER + """/api/cite/' + slug)
    .then(function(r){ return r.json(); })
    .then(function(d){
      if (d.error) { sub.textContent = d.error; return; }
      sub.innerHTML = '<b>' + esc(d.title) + '</b> \\u2014 each format is pinned to revision ' +
        '<a href="' + esc(d.permaUrl) + '"><code>' + esc(d.shortSha) + '</code></a> (' + esc(d.editDate) +
        '), so what you cite never changes even when the page does.';
      var cites = {
        'APA': 'Progress.org Georgism Wiki. (' + d.year + '). <i>' + esc(d.title) + '</i> (rev. ' + esc(d.shortSha) +
               '). Progress.org. Retrieved ' + today + ', from ' + esc(d.url),
        'Chicago': 'Progress.org Georgism Wiki. \\u201C' + esc(d.title) + '.\\u201D Revision ' + esc(d.shortSha) +
               ', last modified ' + esc(d.editDate) + '. ' + esc(d.url) + '.',
        'MLA': '\\u201C' + esc(d.title) + '.\\u201D <i>Progress.org Georgism Wiki</i>, rev. ' + esc(d.shortSha) +
               ', ' + esc(d.editDate) + ', ' + esc(d.url) + '. Accessed ' + today + '.',
        'BibTeX': '@misc{georgismwiki-' + esc(d.slug) + ',<br>' +
               '&nbsp;&nbsp;title = {' + esc(d.title) + '},<br>' +
               '&nbsp;&nbsp;author = {{Progress.org Georgism Wiki}},<br>' +
               '&nbsp;&nbsp;year = {' + d.year + '},<br>' +
               '&nbsp;&nbsp;howpublished = {\\\\url{' + esc(d.url) + '}},<br>' +
               '&nbsp;&nbsp;note = {Revision ' + esc(d.shortSha) + ' (' + esc(d.editDate) +
               '); permanent version: ' + esc(d.permaUrl) + '}<br>}'
      };
      out.innerHTML = Object.keys(cites).map(function(k){
        return '<h3 style="margin:1.2em 0 .3em">' + k + '</h3>' +
          '<div class="wc-cite" style="border:1px solid rgba(0,0,0,.12);border-radius:6px;padding:.8em;font-size:.92em">' +
          cites[k] + '</div>' +
          '<button class="wc-copy" style="margin-top:.4em;font-size:.8em;padding:.3em .9em;cursor:pointer">Copy</button>';
      }).join('');
      out.innerHTML += '<p style="margin-top:1.4em"><a href="/wiki/' + esc(slug) + '/">\\u2190 Back to the article</a></p>';
      out.querySelectorAll('.wc-copy').forEach(function(b){
        b.addEventListener('click', function(){
          navigator.clipboard.writeText(b.previousElementSibling.innerText)
            .then(function(){ b.textContent = 'Copied!'; });
        });
      });
    })
    .catch(function(){ sub.textContent = 'Could not load citation data — please try again.'; });
})();
</script>
"""

# Ghost converts ?source=html to Lexical and STRIPS raw divs/scripts unless the
# block is wrapped as a raw-HTML card (verified live 2026-08-07: unwrapped upsert
# lost the ids and the fetch script). These markers preserve the block verbatim.
def html_card(inner):
    return "<!--kg-card-begin: html-->\n" + inner + "\n<!--kg-card-end: html-->"

PAGES = [
    {"slug": "wiki-history", "title": "Edit history", "html": html_card(HISTORY_HTML)},
    {"slug": "wiki-cite", "title": "Cite this page", "html": html_card(CITE_HTML)},
]


def main():
    key, url = require_ghost()
    kid, secret = key.split(":")

    def hdr():
        tok = jwt.encode(
            {"iat": int(time.time()), "exp": int(time.time()) + 300, "aud": "/admin/"},
            bytes.fromhex(secret), algorithm="HS256", headers={"kid": kid})
        return {"Authorization": f"Ghost {tok}"}

    for pg in PAGES:
        r = requests.get(f"{url}/ghost/api/admin/pages/slug/{pg['slug']}/", headers=hdr(), timeout=30)
        payload = {"pages": [{"title": pg["title"], "slug": pg["slug"],
                              "html": pg["html"], "status": "published"}]}
        if r.status_code == 200:
            existing = r.json()["pages"][0]
            payload["pages"][0]["updated_at"] = existing["updated_at"]
            resp = requests.put(f"{url}/ghost/api/admin/pages/{existing['id']}/?source=html",
                                headers={**hdr(), "Content-Type": "application/json"},
                                json=payload, timeout=30)
            verb = "updated"
        else:
            resp = requests.post(f"{url}/ghost/api/admin/pages/?source=html",
                                 headers={**hdr(), "Content-Type": "application/json"},
                                 json=payload, timeout=30)
            verb = "created"
        resp.raise_for_status()
        out = resp.json()["pages"][0]
        print(f"  {verb}: /{out['slug']}/ (status {out['status']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
