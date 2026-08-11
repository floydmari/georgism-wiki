#!/usr/bin/env python3
"""
send_email.py — send wiki-editorial email via the Gmail API (stdlib only).

Used by the loop for T1 verdict emails to Floyd (public-suggestion oversight,
Floyd's ask 2026-08-14) and available to any editorial script that must notify
a human. Sends from floyd@floydmarinescu.com using the restricted-scope token
"Gmail Token - Floyd mail box modify (JSON)" in the agent vault (gmail.modify
covers messages.send; verified live 2026-08-14, message id 19fef6068bbf3326).

Usage:
    python3 scripts/send_email.py --to floydmarinescu@gmail.com \
        --subject "[Georgism Wiki] ..." --body-file /path/to/body.txt [--html]

    or import: from send_email import send_mail
"""
import argparse, base64, json, os, subprocess, sys, time, urllib.parse, urllib.request
from email.mime.text import MIMEText

VAULT = "Emma - Floyd Agent"
ITEM = "mhrlepgxvhhqgedfp7fxnycziq"   # Gmail Token - Floyd mail box modify (JSON)


def _creds():
    for i in range(4):
        try:
            out = subprocess.run(
                ["op", "document", "get", ITEM, "--vault", VAULT],
                capture_output=True, timeout=30)
            if out.returncode == 0 and out.stdout.strip().startswith(b"{"):
                return json.loads(out.stdout)
        except Exception:
            pass
        time.sleep(2 * (i + 1))          # op flakes transiently; always retry
    raise RuntimeError("could not fetch Gmail credentials from 1Password")


def _access_token(j):
    data = urllib.parse.urlencode({
        "client_id": j["client_id"], "client_secret": j["client_secret"],
        "refresh_token": j["refresh_token"], "grant_type": "refresh_token"}).encode()
    tok = json.loads(urllib.request.urlopen(
        urllib.request.Request(j["token_uri"], data=data), timeout=30).read())
    return tok["access_token"]


def send_mail(to, subject, body, html=False):
    j = _creds()
    at = _access_token(j)
    m = MIMEText(body, "html" if html else "plain", "utf-8")
    m["To"] = to
    m["Subject"] = subject
    raw = base64.urlsafe_b64encode(m.as_bytes()).decode()
    req = urllib.request.Request(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
        data=json.dumps({"raw": raw}).encode(),
        headers={"Authorization": f"Bearer {at}", "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=30).read())
    return r.get("id")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--to", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--body-file", required=True)
    p.add_argument("--html", action="store_true")
    a = p.parse_args()
    body = open(a.body_file, encoding="utf-8").read()
    mid = send_mail(a.to, a.subject, body, html=a.html)
    print(f"sent: {mid}")


if __name__ == "__main__":
    main()
